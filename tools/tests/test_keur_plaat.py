"""Testgevallen voor scripts/keur-plaat.py.

Het harnas moet vinden wat een plaat onleesbaar maakt, en moet zwijgen over wat alleen een
afronding is. Beide kanten staan hier: een echte schuine lijn valt op, een pixel drift niet.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("keur", WORTEL / "scripts/keur-plaat.py")
keur = importlib.util.module_from_spec(spec)
spec.loader.exec_module(keur)

KOP = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">')


def plaat(inhoud, kop=KOP):
    """Een SVG naar schijf schrijven en het pad teruggeven; keur() leest van schijf."""
    map_ = tempfile.mkdtemp()
    pad = Path(map_) / "plaat.svg"
    pad.write_text(kop + inhoud + "</svg>", encoding="utf-8")
    return pad


class LengteTests(unittest.TestCase):
    def test_given_a_size_in_points_when_read_then_it_becomes_pixels(self):
        self.assertAlmostEqual(keur.lengte("12pt"), 16.0)

    def test_given_a_plain_number_when_read_then_it_stays(self):
        self.assertEqual(keur.lengte("15"), 15.0)

    def test_given_nothing_when_read_then_the_default_holds(self):
        self.assertEqual(keur.lengte(None, 9.0), 9.0)


class PolylijnTests(unittest.TestCase):
    def test_given_a_straight_path_when_read_then_the_points_come_back(self):
        self.assertEqual(keur.polylijn("M10,20 L30,20 L30,50"), [(10, 20), (30, 20), (30, 50)])

    def test_given_shorthand_commands_when_read_then_they_are_resolved(self):
        self.assertEqual(keur.polylijn("M0,0 H40 V30"), [(0, 0), (40, 0), (40, 30)])

    def test_given_a_curve_when_read_then_it_is_left_alone(self):
        self.assertIsNone(keur.polylijn("M0,0 C10,10 20,20 30,30"))


class SchuinTests(unittest.TestCase):
    def test_given_a_diagonal_when_measured_then_it_is_reported(self):
        self.assertEqual(len(keur.schuin([[(0, 0), (100, 60)]])), 1)

    def test_given_a_pixel_of_drift_on_a_long_leg_when_measured_then_it_stays_quiet(self):
        self.assertEqual(keur.schuin([[(0, 0), (400, 1)]]), [])

    def test_given_orthogonal_segments_when_measured_then_nothing_is_reported(self):
        self.assertEqual(keur.schuin([[(0, 0), (100, 0), (100, 80)]]), [])


class KruisingTests(unittest.TestCase):
    def test_given_two_lines_over_each_other_when_counted_then_one_shows_up(self):
        self.assertEqual(keur.kruisingen([[(0, 50), (200, 50)], [(100, 0), (100, 100)]]),
                         [(100, 50)])

    def test_given_two_lines_that_only_meet_when_counted_then_none_shows_up(self):
        self.assertEqual(keur.kruisingen([[(0, 50), (100, 50)], [(100, 50), (100, 100)]]), [])

    def test_given_one_line_with_a_corner_when_counted_then_it_is_not_its_own_crossing(self):
        self.assertEqual(keur.kruisingen([[(0, 50), (100, 50), (100, 100)]]), [])


class OntleedTests(unittest.TestCase):
    """Een groep verschuift haar inhoud, en een pijlpunt in defs hoort niet bij de tekening."""

    def test_given_a_translated_group_when_read_then_the_points_move_with_it(self):
        pad = plaat('<g transform="translate(10,20)"><path fill="none" d="M0,0 L50,0"/></g>')
        import xml.etree.ElementTree as ET
        lijn, _ = keur.ontleed(ET.parse(pad).getroot())
        self.assertEqual(lijn, [[(10.0, 20.0), (60.0, 20.0)]])

    def test_given_a_marker_in_defs_when_read_then_it_is_skipped(self):
        pad = plaat('<defs><marker id="p"><path d="M0 0 L10 5 L0 10 z"/></marker></defs>'
                    '<path fill="none" d="M0,0 L50,0"/>')
        import xml.etree.ElementTree as ET
        lijn, _ = keur.ontleed(ET.parse(pad).getroot())
        self.assertEqual(len(lijn), 1)

    def test_given_a_white_underlay_when_read_then_the_line_counts_once(self):
        pad = plaat('<path d="M0,0 L50,0" fill="none" stroke="#fff" stroke-width="7"/>'
                    '<path d="M0,0 L50,0" fill="none" stroke="#000"/>')
        import xml.etree.ElementTree as ET
        lijn, _ = keur.ontleed(ET.parse(pad).getroot())
        self.assertEqual(len(lijn), 1)

    def test_given_an_inherited_size_when_read_then_the_text_carries_it(self):
        pad = plaat('<g font-size="12pt"><text x="10" y="30">Aanbod</text></g>')
        import xml.etree.ElementTree as ET
        _, tekst = keur.ontleed(ET.parse(pad).getroot())
        self.assertAlmostEqual(tekst[0]["maat"], 16.0)


class KeurTests(unittest.TestCase):
    def test_given_a_tidy_plate_when_checked_then_there_is_nothing_to_report(self):
        pad = plaat('<path fill="none" d="M10,10 L200,10 L200,120"/>'
                    '<text x="20" y="40" font-size="15">Onderwijscatalogus</text>')
        bevindingen, maat = keur.keur(pad)
        self.assertEqual([str(b) for b in bevindingen], [])
        self.assertEqual((maat["lijnen"], maat["teksten"]), (1, 1))

    def test_given_text_over_the_edge_when_checked_then_it_is_reported(self):
        pad = plaat('<text x="380" y="40" font-size="15">Voorziening Centraal Aanmelden</text>')
        self.assertEqual([b.code for b in keur.keur(pad)[0]], ["BUITEN"])

    def test_given_text_under_the_floor_when_checked_then_it_is_reported(self):
        pad = plaat('<text x="20" y="40" font-size="6">klein</text>')
        self.assertIn("KLEIN", [b.code for b in keur.keur(pad)[0]])

    def test_given_text_thin_against_a_wide_plate_when_checked_then_it_is_reported(self):
        kop = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6000 2000">'
        pad = plaat('<text x="20" y="40" font-size="12">smal</text>', kop)
        self.assertIn("IJL", [b.code for b in keur.keur(pad)[0]])

    def test_given_a_crossing_beyond_the_agreed_number_when_checked_then_it_is_reported(self):
        pad = plaat('<path fill="none" d="M0,50 L200,50"/><path fill="none" d="M100,0 L100,100"/>')
        self.assertEqual([b.code for b in keur.keur(pad, max_kruisingen=0)[0]], ["KRUISING"])
        self.assertEqual(keur.keur(pad, max_kruisingen=1)[0], [])


if __name__ == "__main__":
    unittest.main()
