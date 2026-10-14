"""Testgevallen voor scripts/teken-hoofdplaat-ruim.py.

De plaat mag ruimer worden, maar de onderlinge ligging van de vakken moet blijven staan: dat is
het verhaal van hoofdplaat v1.7. En een naam die niet past hoort niet stilletjes af te breken.
"""

import importlib.util
import tempfile
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
    """De markering van een casus: welke stromen zij uitlicht en wat de plaat nog niet kent."""

    @staticmethod
    def component(ident, x, y, naam):
        return dict(id=ident, x=x, y=y, ax=x, ay=y, w=120, h=60, naam=naam,
                    type="ApplicationComponent", opschrift=[], tekst="", soort="DiagramObject",
                    kinderen=[], ouder=None, vul=None, lijn=None, letter=None)

    def bestand(self, inhoud):
        pad = Path(self.enterContext(tempfile.TemporaryDirectory())) / "casus.json"
        pad.write_text(inhoud, encoding="utf-8")
        return pad

    def test_given_a_file_without_op_de_plaat_when_read_then_the_flow_counts_as_known(self):
        pad = self.bestand('{"naam": "Een casus", "stromen": [{"van": "A", "naar": "B", '
                           '"label": "wat"}]}')
        naam, stromen = ruim.lees_markering(pad)
        self.assertEqual(naam, "Een casus")
        self.assertEqual(stromen, [dict(van="A", naar="B", label="wat", op_de_plaat=True,
                                        stroom="")])

    def test_given_a_file_with_a_flow_id_when_read_then_that_id_comes_along(self):
        pad = self.bestand('{"stromen": [{"van": "A", "naar": "B", "stroom": "id-7"}]}')
        self.assertEqual(ruim.lees_markering(pad)[1][0]["stroom"], "id-7")

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


class MarkeerpadTests(unittest.TestCase):
    """Welke benen van de plaat een markering uitlicht; een stroom door een junctie hoort er heel bij."""

    @staticmethod
    def stroom(relatie, bron, doel):
        return dict(relatie=relatie, bron=bron, doel=doel, label="", punten=[(0, 0), (10, 0)])

    def setUp(self):
        self.knopen = {"oc": dict(id="oc", naam="Onderwijscatalogus", type="ApplicationComponent"),
                       "sks": dict(id="sks", naam="Student Keuze Systeem (SKS)",
                                   type="ApplicationComponent"),
                       "krs": dict(id="krs", naam="Kernregistratie systeem studenten (KRS)",
                                   type="ApplicationComponent"),
                       "j": dict(id="j", naam="", type="Junction")}

    def pad(self, stromen, van, naar, relatie=""):
        return ruim.markeerpad(stromen, self.knopen, self.knopen[van], self.knopen[naar], relatie)

    def test_given_a_flow_between_two_components_when_sought_then_its_leg_is_found(self):
        s = self.stroom("r1", "oc", "sks")
        self.assertEqual(self.pad([s], "oc", "sks"), [s])

    def test_given_a_junction_in_between_when_sought_then_the_sender_leg_comes_first(self):
        aanvoer, been = self.stroom("r1", "krs", "j"), self.stroom("r2", "j", "sks")
        self.assertEqual(self.pad([aanvoer, been], "krs", "sks"), [aanvoer, been])

    def test_given_a_junction_with_more_receivers_when_sought_then_one_leg_joins(self):
        aanvoer = self.stroom("r1", "krs", "j")
        naar_sks, naar_oc = self.stroom("r2", "j", "sks"), self.stroom("r3", "j", "oc")
        self.assertEqual(self.pad([aanvoer, naar_oc, naar_sks], "krs", "sks"), [aanvoer, naar_sks])

    def test_given_two_flows_between_one_pair_when_an_id_is_given_then_that_flow_wins(self):
        een, twee = self.stroom("r1", "oc", "sks"), self.stroom("r2", "oc", "sks")
        self.assertEqual(self.pad([een, twee], "oc", "sks", "r2"), [twee])

    def test_given_an_id_the_plate_does_not_carry_when_sought_then_the_pair_decides(self):
        s = self.stroom("r1", "oc", "sks")
        self.assertEqual(self.pad([s], "oc", "sks", "r9"), [s])

    def test_given_an_id_that_ends_elsewhere_when_sought_then_the_path_stays_empty(self):
        s = self.stroom("r1", "oc", "sks")
        self.assertEqual(self.pad([s], "oc", "krs", "r1"), [])

    def test_given_a_flow_the_plate_lacks_when_sought_then_the_path_stays_empty(self):
        s = self.stroom("r1", "oc", "sks")
        self.assertEqual(self.pad([s], "sks", "oc"), [])


class MarkeerStromenTests(unittest.TestCase):
    """Elke markering naast de plaat gelegd: wat zij uitlicht, en wat er voor wie meeleest ontbreekt."""

    def setUp(self):
        self.oc = MarkeringTests.component("oc", 0, 0, "Onderwijscatalogus")
        self.sks = MarkeringTests.component("sks", 600, 0, "Student Keuze Systeem (SKS)")
        self.knopen = {"oc": dict(self.oc), "sks": dict(self.sks)}
        self.stroom = MarkeerpadTests.stroom("r1", "oc", "sks")

    def markering(self, **erbij):
        return dict(dict(van="Onderwijscatalogus", naar="Student Keuze Systeem (SKS)",
                         label="kiesbaar aanbod", op_de_plaat=True, stroom=""), **erbij)

    def leg_naast(self, markeringen, stromen):
        return ruim.markeer_stromen(markeringen, stromen, self.knopen, [self.oc, self.sks])

    def test_given_a_flow_the_file_calls_known_when_matched_then_its_leg_is_found(self):
        raakt, zonder, ontbreekt = self.leg_naast([self.markering()], [self.stroom])
        self.assertEqual((len(raakt), zonder, ontbreekt), (1, [], []))
        m, a, b, benen = raakt[0]
        self.assertEqual((a["id"], b["id"], benen), ("oc", "sks", [self.stroom]))

    def test_given_a_flow_the_file_calls_unknown_when_matched_then_no_leg_is_sought(self):
        raakt, zonder, ontbreekt = self.leg_naast([self.markering(op_de_plaat=False)],
                                                  [self.stroom])
        self.assertEqual((raakt, len(zonder), ontbreekt), ([], 1, []))

    def test_given_a_known_flow_without_a_line_when_matched_then_it_is_reported(self):
        raakt, zonder, ontbreekt = self.leg_naast([self.markering()], [])
        self.assertEqual((raakt, len(zonder)), ([], 1))
        self.assertEqual(ontbreekt, ["kiesbaar aanbod: Onderwijscatalogus naar Student Keuze "
                                     "Systeem (SKS) staat in het bestand als lijn die de plaat "
                                     "kent, de plaat heeft deze stroom niet"])

    def test_given_a_flow_the_plate_has_no_component_for_when_matched_then_it_is_reported(self):
        raakt, zonder, ontbreekt = self.leg_naast([self.markering(van="Keuzeportaal")],
                                                  [self.stroom])
        self.assertEqual((raakt, zonder), ([], []))
        self.assertEqual(ontbreekt, ["kiesbaar aanbod: Keuzeportaal naar Student Keuze "
                                     "Systeem (SKS) is niet op de plaat te plaatsen"])


class MarkeerTekenTests(unittest.TestCase):
    """Hoe een markering op de plaat terechtkomt: de lijn zelf, de omlijning, de legenda."""

    def plaat(self, *componenten):
        vakken = {k["id"]: dict(x=k["ax"], y=k["ay"], w=k["w"], h=k["h"]) for k in componenten}
        routers = {"rechts": ruim.hoofdplaat.Haaks(list(vakken.values()), [])}
        per_zone = {k["id"]: "rechts" for k in componenten}
        return per_zone, routers, vakken

    def test_given_a_marked_flow_when_its_line_is_drawn_then_one_path_carries_the_accent(self):
        svg = ruim.lijn_svg([(0, 0), (100, 0)], ruim.MARKEER, "pijl0", dik=True)
        self.assertEqual(svg.count("<path"), 2)        # de witte onderlaag en de lijn zelf
        self.assertEqual(svg.count(f'stroke="{ruim.MARKEER}"'), 1)
        self.assertIn(f'stroke-width="{ruim.MARKEER_DIK}"', svg)

    def test_given_an_ordinary_flow_when_its_line_is_drawn_then_it_keeps_its_thin_line(self):
        svg = ruim.lijn_svg([(0, 0), (100, 0)], "#1f5fd0", "pijl1")
        self.assertIn('stroke-width="2.6"', svg)
        self.assertNotIn(f'stroke-width="{ruim.MARKEER_DIK}"', svg)

    def test_given_a_flow_the_plate_does_not_know_when_drawn_then_the_line_is_dashed(self):
        svg = ruim.markeerlijn_svg([(0, 0), (100, 0)])
        self.assertIn('stroke-dasharray="16 11"', svg)
        self.assertIn('marker-end="url(#markeerpunt)"', svg)

    def test_given_a_known_flow_when_marked_then_no_second_path_comes_over_it(self):
        oc = MarkeringTests.component("oc", 0, 0, "Onderwijscatalogus")
        sks = MarkeringTests.component("sks", 600, 0, "Student Keuze Systeem (SKS)")
        been = MarkeerpadTests.stroom("r1", "oc", "sks")
        markering = dict(van="Onderwijscatalogus", naar="Student Keuze Systeem (SKS)",
                         label="kiesbaar aanbod", op_de_plaat=True, stroom="")
        per_zone, routers, vakken = self.plaat(oc, sks)
        svg = "".join(ruim.markeer_svg([(markering, oc, sks, [been])], [], per_zone, routers,
                                       vakken, [], (800, 600)))
        self.assertNotIn("<path", svg)                 # de lijn staat al in de eerste tekenronde
        self.assertIn("kiesbaar aanbod", svg)

    def test_given_a_flow_without_a_line_when_marked_then_it_gets_a_dashed_lane(self):
        svs = MarkeringTests.component("svs", 0, 0, "Student volg systeem (SVS)")
        sks = MarkeringTests.component("sks", 600, 0, "Student Keuze Systeem (SKS)")
        markering = dict(van="Student volg systeem (SVS)", naar="Student Keuze Systeem (SKS)",
                         label="behaalde leeruitkomsten", op_de_plaat=False, stroom="")
        per_zone, routers, vakken = self.plaat(svs, sks)
        svg = "".join(ruim.markeer_svg([], [(markering, svs, sks)], per_zone, routers, vakken, [],
                                       (800, 600)))
        self.assertEqual(svg.count("<path"), 2)        # de witte onderlaag en de gestippelde lijn
        self.assertIn('stroke-dasharray="16 11"', svg)
        # het etiket draagt alleen de naam van de stroom: dat de plaat haar niet kent zegt de
        # onderbroken lijn, en herhalen in het etiket maakt het breder dan de ruimte ernaast
        self.assertIn(">behaalde leeruitkomsten</text>", svg)
        self.assertNotIn("geen lijn op deze plaat", svg)

    def test_given_two_flows_on_one_component_when_marked_then_it_is_outlined_once(self):
        oc = MarkeringTests.component("oc", 0, 0, "Onderwijscatalogus")
        sks = MarkeringTests.component("sks", 600, 0, "Student Keuze Systeem (SKS)")
        krs = MarkeringTests.component("krs", 0, 400, "Kernregistratie systeem studenten (KRS)")
        per_zone, routers, vakken = self.plaat(oc, sks, krs)
        raakt = [(dict(label="kiesbaar aanbod"), oc, sks, [MarkeerpadTests.stroom("r1", "oc", "sks")]),
                 (dict(label="student"), krs, sks, [MarkeerpadTests.stroom("r2", "krs", "sks")])]
        svg = "".join(ruim.markeer_svg(raakt, [], per_zone, routers, vakken, [], (800, 600)))
        self.assertEqual(svg.count(f'stroke="{ruim.MARKEER_RAND}"'), 3)
        for stuk in ("kiesbaar aanbod", "student"):
            self.assertIn(stuk, svg)

    def test_given_a_marking_when_the_legend_is_drawn_then_it_explains_all_three_signs(self):
        svg = ruim.markeer_legenda_svg("Keuzedeel kiesbaar maken", 0, 0, 900)
        for stuk in ("Keuzedeel kiesbaar maken", "stroom van deze casus",
                     "nog niet kent", "component dat meedoet", ruim.MARKEER_RAND):
            self.assertIn(stuk, svg)


class PlaatMetMarkeringTests(unittest.TestCase):
    """De hele plaat met een markering erover, uit het model zelf."""

    CASUS = WORTEL / "architecture/docs/specificatie/koppelvlak-keuzedeel-kiesbaar/stromen-kiesbaar.json"

    @classmethod
    def setUpClass(cls):
        # het model en de stroomnamen met hun volledige pad, zodat de werkmap er niet toe doet
        ruim.MODEL = WORTEL / "architecture/model/model.archimate"
        ruim.STROMEN = WORTEL / "architecture/model/informatiemodel/stromen.json"
        cls.naam, cls.markeringen = ruim.lees_markering(cls.CASUS)
        cls.kaal = ruim.bouw()[0]
        cls.svg, cls.stromen, *cls.rest = ruim.bouw(markeer=cls.markeringen,
                                                    markeer_naam=cls.naam)

    def test_given_a_marked_plate_when_built_then_the_number_of_plate_arrows_stays(self):
        self.assertEqual(self.svg.count('marker-end="url(#pijl'),
                         self.kaal.count('marker-end="url(#pijl'))

    def test_given_a_known_flow_when_marked_then_its_own_line_carries_the_accent(self):
        gemarkeerd = [s for s in self.stromen if s.get("markeer")]
        self.assertTrue(gemarkeerd)
        for s in gemarkeerd:
            self.assertEqual(s["kleur"], ruim.MARKEER)
        self.assertEqual(self.svg.count(f'stroke="{ruim.MARKEER}" '
                                        f'stroke-width="{ruim.MARKEER_DIK}" stroke-linejoin'),
                         len(gemarkeerd))

    def test_given_a_marked_flow_when_the_plate_is_built_then_its_line_lies_over_the_veil(self):
        sluier = self.svg.index(f'fill-opacity="{ruim.SLUIER}"')
        lijn = self.svg.index(f'stroke="{ruim.MARKEER}" stroke-width="{ruim.MARKEER_DIK}" '
                              f'stroke-linejoin')
        self.assertLess(sluier, lijn)

    def test_given_a_marked_flow_when_the_plate_is_built_then_the_casus_name_takes_over(self):
        self.assertIn("keuzeregelset", self.svg)
        self.assertIn(">Onderwijsprogramma<", self.kaal)      # de naam van de plaat zelf
        self.assertNotIn(">Onderwijsprogramma<", self.svg)

    def test_given_a_flow_the_plate_lacks_when_the_plate_is_built_then_it_stays_dashed(self):
        self.assertEqual(self.svg.count('marker-end="url(#markeerpunt)"'),
                         sum(1 for m in self.markeringen if not m["op_de_plaat"]))


if __name__ == "__main__":
    unittest.main()
