"""Testgevallen voor tools/scripts/teken-hoofdplaat-ruim.py.

De plaat mag ruimer worden, maar de onderlinge ligging van de vakken moet blijven staan: dat is
het verhaal van hoofdplaat v1.7a. En een naam die niet past hoort niet stilletjes af te breken.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("ruim", WORTEL / "tools/scripts/teken-hoofdplaat-ruim.py")
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


class KoppelingIdTests(unittest.TestCase):
    """Het voorlopige koppeling-ID volgt de regel uit Public #107: twee componenten, een naam."""

    def test_given_two_components_when_named_then_the_catalogue_goes_first(self):
        self.assertEqual(ruim.koppeling_id("Leer management systeem (LMS)", "Onderwijscatalogus"),
                         "OC-LMS")

    def test_given_both_directions_when_named_then_the_id_is_the_same(self):
        heen = ruim.koppeling_id("Roostersysteem", "Student Keuze Systeem (SKS)")
        terug = ruim.koppeling_id("Student Keuze Systeem (SKS)", "Roostersysteem")
        self.assertEqual((heen, terug), ("R-SKS", "R-SKS"))

    def test_given_a_component_without_an_abbreviation_when_named_then_there_is_no_id(self):
        self.assertEqual(ruim.koppeling_id("Onderwijscatalogus", "Financieel systeem"), "")

    def test_given_a_junction_when_labelled_then_the_leg_carries_the_sender(self):
        knopen = {"oc": dict(type="ApplicationComponent", naam="Onderwijscatalogus"),
                  "j": dict(type="Junction", naam=""),
                  "krs": dict(type="ApplicationComponent",
                              naam="Kernregistratie systeem studenten (KRS)")}
        stromen = [dict(bron="oc", doel="j", label=""), dict(bron="j", doel="krs", label="")]
        self.assertEqual(ruim.zet_koppeling_ids(stromen, knopen), ["OC-KRS"])
        self.assertEqual([s["label"] for s in stromen], ["", "OC-KRS"])


class LegendaTests(unittest.TestCase):
    """De legenda vertelt per koppeling-ID zijn kleur en hoeveel informatiestromen eronder vallen."""

    RIJEN = [("OC-P", "#d9531e", 3), ("R-SKS", "#1f5fd0", 1)]

    def test_given_no_ids_when_measured_then_the_legend_takes_no_room(self):
        self.assertEqual(ruim.legenda_hoogte(0), 0)
        self.assertEqual(ruim.legenda_svg([], 0, 0, 600), "")

    def test_given_more_ids_than_columns_when_measured_then_a_row_is_added(self):
        self.assertGreater(ruim.legenda_hoogte(7, kolommen=6), ruim.legenda_hoogte(6, kolommen=6))

    def test_given_ids_when_drawn_then_each_shows_its_colour_and_its_count(self):
        svg = ruim.legenda_svg(self.RIJEN, 0, 0, 600)
        for stuk in ("OC-P", "R-SKS", "#d9531e", "#1f5fd0", "3 stromen", "1 stroom"):
            self.assertIn(stuk, svg)

    def test_given_ids_when_drawn_then_the_heading_counts_them_and_their_flows(self):
        svg = ruim.legenda_svg(self.RIJEN, 0, 0, 600)
        self.assertIn("2 voorlopige koppeling-ID's, samen 4 informatiestromen", svg)


class MarkeringTests(unittest.TestCase):
    """De markering van een casus: welke lijnen worden uitgelicht en wat de plaat nog niet kent."""

    @staticmethod
    def component(ident, x, y, naam):
        return dict(id=ident, x=x, y=y, ax=x, ay=y, w=120, h=60, naam=naam,
                    type="ApplicationComponent", opschrift=[], tekst="", soort="DiagramObject",
                    kinderen=[], ouder=None, vul=None, lijn=None, letter=None)

    def plaat(self, *componenten):
        vakken = {k["id"]: dict(x=k["ax"], y=k["ay"], w=k["w"], h=k["h"]) for k in componenten}
        routers = {"rechts": ruim.hoofdplaat.Haaks(list(vakken.values()), [])}
        per_zone = {k["id"]: "rechts" for k in componenten}
        return list(componenten), per_zone, routers, vakken

    def test_given_a_file_without_op_de_plaat_when_read_then_the_flow_counts_as_known(self):
        pad = Path(self.enterContext(tempfile.TemporaryDirectory())) / "casus.json"
        pad.write_text('{"naam": "Een casus", "stromen": [{"van": "A", "naar": "B", '
                       '"label": "wat"}]}', encoding="utf-8")
        naam, stromen = ruim.lees_markering(pad)
        self.assertEqual(naam, "Een casus")
        self.assertEqual(stromen, [dict(van="A", naar="B", label="wat", op_de_plaat=True)])

    def test_given_a_component_twice_on_the_plate_when_paired_then_the_nearest_one_wins(self):
        ver = self.component("oc-ver", 0, 0, "Onderwijscatalogus")
        dichtbij = self.component("oc-bij", 900, 0, "Onderwijscatalogus")
        sks = self.component("sks", 1100, 0, "Student Keuze Systeem (SKS)")
        a, b = ruim.dichtste_vakken([ver, dichtbij, sks], "Onderwijscatalogus",
                                    "Student Keuze Systeem (SKS)")
        self.assertEqual((a["id"], b["id"]), ("oc-bij", "sks"))

    def test_given_a_name_that_is_not_on_the_plate_when_paired_then_nothing_is_found(self):
        sks = self.component("sks", 0, 0, "Student Keuze Systeem (SKS)")
        self.assertEqual(ruim.dichtste_vakken([sks], "Keuzeportaal", "Student Keuze Systeem (SKS)"),
                         (None, None))

    def test_given_a_flow_the_plate_does_not_know_when_drawn_then_the_line_is_dashed(self):
        punten = [(0, 0), (100, 0)]
        self.assertIn("stroke-dasharray", ruim.markeerlijn_svg(punten, gestippeld=True))
        self.assertNotIn("stroke-dasharray", ruim.markeerlijn_svg(punten, gestippeld=False))

    def test_given_two_flows_on_one_component_when_marked_then_it_is_outlined_once(self):
        oc = self.component("oc", 0, 0, "Onderwijscatalogus")
        sks = self.component("sks", 600, 0, "Student Keuze Systeem (SKS)")
        krs = self.component("krs", 0, 400, "Kernregistratie systeem studenten (KRS)")
        alles, per_zone, routers, vakken = self.plaat(oc, sks, krs)
        markeringen = [dict(van="Onderwijscatalogus", naar="Student Keuze Systeem (SKS)",
                            label="kiesbaar aanbod", op_de_plaat=True),
                       dict(van="Kernregistratie systeem studenten (KRS)",
                            naar="Student Keuze Systeem (SKS)", label="student",
                            op_de_plaat=True)]
        delen, ontbreekt = ruim.markeer_svg(markeringen, alles, per_zone, routers, vakken, [],
                                            (800, 600))
        svg = "".join(delen)
        self.assertEqual(ontbreekt, [])
        self.assertEqual(svg.count(f'stroke="{ruim.MARKEER_RAND}"'), 3)
        for stuk in ("kiesbaar aanbod", "student"):
            self.assertIn(stuk, svg)

    def test_given_a_flow_the_plate_has_no_component_for_when_marked_then_it_is_reported(self):
        sks = self.component("sks", 0, 0, "Student Keuze Systeem (SKS)")
        alles, per_zone, routers, vakken = self.plaat(sks)
        markeringen = [dict(van="Keuzeportaal", naar="Student Keuze Systeem (SKS)",
                            label="kiesbaar aanbod", op_de_plaat=True)]
        delen, ontbreekt = ruim.markeer_svg(markeringen, alles, per_zone, routers, vakken, [],
                                            (800, 600))
        self.assertEqual(delen, [])
        self.assertEqual(ontbreekt, ["kiesbaar aanbod: Keuzeportaal naar Student Keuze Systeem (SKS)"])

    def test_given_a_marking_when_the_legend_is_drawn_then_it_explains_all_three_signs(self):
        svg = ruim.markeer_legenda_svg("Keuzedeel kiesbaar maken", 0, 0, 900)
        for stuk in ("Keuzedeel kiesbaar maken", "stroom van deze casus",
                     "nog niet kent", "component dat meedoet", ruim.MARKEER_RAND):
            self.assertIn(stuk, svg)


if __name__ == "__main__":
    unittest.main()
