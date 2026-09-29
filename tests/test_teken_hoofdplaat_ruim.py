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


def kind(x, y, w=100, h=50, naam="vak", type_="ApplicationComponent", vul=None, letter=None):
    return dict(x=x, y=y, w=w, h=h, naam=naam, opschrift=[], tekst="", soort="DiagramObject",
                type=type_, kinderen=[], ouder=None, vul=vul, lijn=None, letter=letter)


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


class KleurTests(unittest.TestCase):
    """De plaat kleurt zoals Archi kleurt: de view beslist, en anders de ArchiMate-laag."""

    def test_given_a_component_without_a_colour_when_drawn_then_it_gets_its_layer_colour(self):
        self.assertEqual(ruim.kleuren(kind(0, 0)), ruim.ARCHIMATE["Application"])

    def test_given_an_actor_when_drawn_then_it_gets_the_colour_of_the_business_layer(self):
        self.assertEqual(ruim.kleuren(kind(0, 0, type_="BusinessActor")), ruim.ARCHIMATE["Business"])

    def test_given_a_colour_in_the_view_when_drawn_then_that_choice_stays(self):
        vul, rand, tekst = ruim.kleuren(kind(0, 0, vul="#ffffff", letter="#408080"))
        self.assertEqual((vul, tekst), ("#ffffff", "#408080"))
        self.assertNotEqual(rand, "#ffffff")           # de rand blijft zichtbaar op wit

    def test_given_a_fill_when_a_border_is_derived_then_it_is_darker(self):
        self.assertEqual(ruim.donkerder("#ffffff", 0.5), "#808080")


class KruisingTests(unittest.TestCase):
    """De telling die de kwaliteit van de routering meet."""

    def test_given_two_lines_over_each_other_when_counted_then_it_finds_one(self):
        self.assertEqual(ruim.kruisingen([[(0, 10), (100, 10)], [(50, 0), (50, 100)]]), 1)

    def test_given_two_lines_that_only_meet_when_counted_then_it_finds_none(self):
        self.assertEqual(ruim.kruisingen([[(0, 10), (50, 10)], [(50, 10), (50, 100)]]), 0)


if __name__ == "__main__":
    unittest.main()
