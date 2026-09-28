"""Testgevallen voor scripts/teken-stromen-voorstel.py.

De plaat leest alleen als twee stromen die elkaar overlappen ook echt naast elkaar komen te
liggen, en als een naam binnen haar baan past.
"""

import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("voorstel", WORTEL / "scripts/teken-stromen-voorstel.py")
vs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vs)

KOLOMMEN = ["a", "b", "c", "d"]
VAKKEN = {naam: {"kolom": kolom} for naam, kolom in
          (("A", "a"), ("B", "b"), ("C", "c"), ("D", "d"))}


def stroom(van, naar, band="boven"):
    return dict(van=van, naar=naar, band=band, label="")


class BanenTests(unittest.TestCase):
    def test_given_overlapping_flows_when_assigned_then_they_get_their_own_lane(self):
        stromen = [stroom("A", "D"), stroom("B", "C"), stroom("A", "C")]
        vs.kies_banen(stromen, VAKKEN, KOLOMMEN)
        self.assertEqual(len({s["baan"] for s in stromen}), 3)

    def test_given_flows_beside_each_other_when_assigned_then_they_share_a_lane(self):
        stromen = [stroom("A", "B"), stroom("C", "D")]
        vs.kies_banen(stromen, VAKKEN, KOLOMMEN)
        self.assertEqual(stromen[0]["baan"], stromen[1]["baan"])

    def test_given_both_bands_when_assigned_then_they_are_counted_apart(self):
        stromen = [stroom("A", "D"), stroom("A", "D", band="onder"), stroom("B", "C", band="onder")]
        boven, onder = vs.kies_banen(stromen, VAKKEN, KOLOMMEN)
        self.assertEqual((boven, onder), (1, 2))

    def test_given_a_lane_when_flows_share_it_then_their_spans_stay_apart(self):
        stromen = [stroom(a, b) for a, b in (("A", "B"), ("B", "C"), ("C", "D"), ("A", "D"), ("A", "C"))]
        vs.kies_banen(stromen, VAKKEN, KOLOMMEN)
        for baan in {s["baan"] for s in stromen}:
            samen = [s["span"] for s in stromen if s["baan"] == baan]
            for i, een in enumerate(samen):
                for ander in samen[i + 1:]:
                    self.assertLess(min(een[1], ander[1]), max(een[0], ander[0]),
                                    f"twee stromen in baan {baan} overlappen: {een} en {ander}")


class NaamTests(unittest.TestCase):
    def test_given_a_long_name_when_broken_then_it_stays_within_two_lines(self):
        naam = "Verzoek tot maken onderwijsaanbod obv opleidingsprogramma- en onderwijseenheid specificaties"
        regels = vs.breek(naam, 300)
        self.assertLessEqual(len(regels), 2)
        self.assertTrue(all(len(r) * vs.TEKEN <= 300 for r in regels))

    def test_given_a_short_name_when_broken_then_it_stays_on_one_line(self):
        self.assertEqual(vs.breek("Onderwijs specificatie", 300), ["Onderwijs specificatie"])

    def test_given_no_name_when_broken_then_nothing_is_drawn(self):
        self.assertEqual(vs.breek("", 300), [])


if __name__ == "__main__":
    unittest.main()
