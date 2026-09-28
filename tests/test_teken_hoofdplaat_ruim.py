"""Testgevallen voor scripts/teken-hoofdplaat-ruim.py.

De plaat mag ruimer worden, maar de onderlinge ligging van de vakken moet blijven staan: dat is
het verhaal van hoofdplaat v1.7. En een naam die niet past hoort niet stilletjes af te breken.
"""

import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("ruim", WORTEL / "scripts/teken-hoofdplaat-ruim.py")
ruim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ruim)


def kind(x, y, w=100, h=50, naam="vak"):
    return dict(x=x, y=y, w=w, h=h, naam=naam, opschrift=[], tekst="", soort="DiagramObject",
                type="ApplicationComponent", kinderen=[], ouder=None)


def groep(kinderen):
    return dict(x=0, y=0, w=10, h=10, naam="", opschrift=[], tekst="", soort="Group", type="",
                kinderen=kinderen, ouder=None)


class DuwenTests(unittest.TestCase):
    def test_given_overlapping_boxes_when_pushed_then_they_keep_a_lane_between_them(self):
        a, b = kind(0, 0), kind(40, 0)
        ruim.duw_uit_elkaar(groep([a, b]), marge=30)
        self.assertGreaterEqual(b["x"] - (a["x"] + a["w"]), 29.5)

    def test_given_boxes_side_by_side_when_pushed_then_the_order_stays(self):
        links, rechts = kind(0, 0), kind(40, 0)
        ruim.duw_uit_elkaar(groep([links, rechts]), marge=30)
        self.assertLess(links["x"], rechts["x"])

    def test_given_boxes_with_room_when_pushed_then_nothing_moves(self):
        a, b = kind(0, 0), kind(400, 0)
        ruim.duw_uit_elkaar(groep([a, b]), marge=30)
        self.assertEqual((a["x"], b["x"]), (0, 400))

    def test_given_a_group_when_widened_then_the_arrangement_is_kept(self):
        g = groep([kind(0, 0, naam="een"), kind(200, 0, naam="twee"), kind(0, 200, naam="drie")])
        ruim.ruimer(g, 1.5, 1.5)
        een, twee, drie = g["kinderen"]
        self.assertLess(een["x"], twee["x"])
        self.assertLess(een["y"], drie["y"])
        self.assertGreaterEqual(twee["x"] - (een["x"] + een["w"]), 30)


class PassendTests(unittest.TestCase):
    def test_given_a_long_name_when_fitted_then_nothing_falls_off(self):
        naam = "Toets- en examenplanning- en inschrijfsysteem"
        grootte, regels = ruim.passend(naam, 150, 60)
        self.assertEqual(" ".join(regels), naam)
        self.assertLessEqual(len(regels) * grootte * 1.2, 60)

    def test_given_ready_made_lines_when_fitted_then_they_stay_as_they_are(self):
        regels = ["Verzoek tot", "roosteren"]
        self.assertEqual(ruim.passend(regels, 150, 60)[1], regels)

    def test_given_a_box_too_small_for_its_name_when_measured_then_it_grows(self):
        vak = kind(100, 100, w=60, h=30, naam="Kernregistratie systeem studenten (KRS)")
        ruim.op_maat(vak)
        self.assertGreater(vak["w"], 60)
        regels = ruim.passend(vak["naam"], vak["w"] - 14, vak["h"] - 8, minimaal=11)[1]
        self.assertEqual(" ".join(regels), vak["naam"])


if __name__ == "__main__":
    unittest.main()
