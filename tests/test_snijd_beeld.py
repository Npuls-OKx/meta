"""Testgevallen voor scripts/snijd-beeld.py.

Een beeld in banen snijden mag nooit door een vak heen gaan, en een breed beeld hoeft niet
gesneden te worden ook al is het hoog in punten. Beide kanten staan hier.
"""

import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("snijd", WORTEL / "scripts/snijd-beeld.py")
snijd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(snijd)


def beeld(hoogte, vakken, breedte=1000):
    """Een SVG met een omhullend kader en de gevraagde vakken eronder."""
    rects = "".join(f'<rect x="10" y="{y}" width="200" height="{h}" fill="#ffffb5"/>' for y, h in vakken)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breedte} {hoogte}" '
            f'width="{breedte}" height="{hoogte}">'
            f'<rect x="0.5" y="0.5" width="{breedte - 2}" height="{hoogte - 2}" fill="#fff"/>'
            f'{rects}</svg>')


class DoekTests(unittest.TestCase):
    def test_given_a_viewbox_when_read_then_the_size_comes_back(self):
        self.assertEqual(snijd.doek(beeld(400, [])), [0.0, 0.0, 1000.0, 400.0])

    def test_given_no_viewbox_when_read_then_it_fails(self):
        with self.assertRaises(ValueError):
            snijd.doek('<svg xmlns="http://www.w3.org/2000/svg"></svg>')


class BezetTests(unittest.TestCase):
    def test_given_the_outer_frame_when_measured_then_it_does_not_count(self):
        self.assertEqual(snijd.bezet(beeld(400, []), 400), [])

    def test_given_a_box_when_measured_then_its_band_is_reported(self):
        self.assertEqual(snijd.bezet(beeld(400, [(40, 60)]), 400), [(40.0, 100.0)])

    def test_given_an_icon_group_when_measured_then_it_is_skipped(self):
        svg = beeld(400, [(40, 60)]).replace("</svg>",
                                             '<g transform="translate(5,5)"><rect y="900" height="20"/></g></svg>')
        self.assertEqual(snijd.bezet(svg, 400), [(40.0, 100.0)])


class BanenTests(unittest.TestCase):
    def test_given_a_wide_low_plate_when_split_then_it_stays_whole(self):
        self.assertEqual(len(snijd.banen(beeld(300, [(40, 60)], breedte=1800))), 1)

    def test_given_a_tall_plate_when_split_then_the_cut_falls_in_a_gap(self):
        vakken = [(40, 60), (140, 60), (240, 60), (340, 60), (440, 60), (540, 60)]
        delen = snijd.banen(beeld(640, vakken, breedte=1000))
        self.assertGreater(len(delen), 1)
        for deel in delen:
            _, boven, _, hoog = snijd.doek(deel)
            for y, h in vakken:                       # geen vak mag doormidden
                self.assertFalse(y < boven < y + h, f"snede door een vak op {boven}")
                self.assertFalse(y < boven + hoog < y + h, f"snede door een vak op {boven + hoog}")

    def test_given_bands_when_split_then_together_they_cover_the_whole_plate(self):
        delen = snijd.banen(beeld(640, [(40, 60), (140, 60), (240, 60), (340, 60), (440, 60), (540, 60)]))
        self.assertEqual(snijd.doek(delen[0])[1], 0.0)
        laatste = snijd.doek(delen[-1])
        self.assertEqual(laatste[1] + laatste[3], 640.0)

    def test_given_a_band_when_split_then_the_drawing_itself_is_unchanged(self):
        svg = beeld(640, [(40, 60), (140, 60), (240, 60), (340, 60), (440, 60), (540, 60)])
        for deel in snijd.banen(svg):
            self.assertIn('<rect x="10" y="540"', deel)   # elke baan draagt de hele tekening


if __name__ == "__main__":
    unittest.main()
