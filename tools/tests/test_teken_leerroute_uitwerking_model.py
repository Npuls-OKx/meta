"""Testgevallen voor tools/scripts/teken-leerroute-uitwerking-model.py.

Elke verwachting volgt uit een fixture-regeltabel in de test; de SVG wordt als XML
geparst en op inhoud en geometrie getoetst, niet op een momentopname.
"""

import importlib.util
import json
import tempfile
import pathlib
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("teken_leerroute_uitwerking_model", WORTEL / "tools/scripts/teken-leerroute-uitwerking-model.py")
tv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tv)

SVG = "{http://www.w3.org/2000/svg}"


def regels(extra=None):
    basis = {"scope_uitzonderingen": [{"objecttype": "Lesgelegenheid", "motivering": "besluit"}],
             "regels": [
                 {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "b", "zin": "De planner maakt aanbod."},
                 {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingsprogramma aanbod", "instantie": "Regulier BOL 2026", "bron": "b",
                  "relatie": {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Opleidingsprogramma aanbod", "nesting": True}},
                 {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Cohort / periode", "instantie": "2026", "bron": "b", "aanname": True,
                  "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Cohort / periode", "label": "Op basis van"}},
                 {"fase": 2, "stap": "Aanbod publiceren", "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1", "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "b", "zin": "Terug naar de catalogus."},
                 {"fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "roosteraar", "objecttype": "Lesgelegenheid", "instantie": "ma 09:00", "bron": "b"},
                 {"fase": 4, "stap": "Roosteren", "soort": "verandert", "wie": "roosteraar", "objecttype": "Leergelegenheid", "instantie": "B1-K1-W1", "toestand": "geroosterd", "bron": "b"}]}
    if extra:
        basis["regels"] += extra
    return basis


def teksten(svg):
    return [t.text or "" for t in ET.fromstring(svg).iter(f"{SVG}text")]


def rects(svg):
    return [dict(r.attrib) for r in ET.fromstring(svg).iter(f"{SVG}rect")]


class TekenTests(unittest.TestCase):
    def blokken(self, r=None):
        return tv.groepeer(r or regels())

    def test_given_rules_same_step_when_grouped_then_one_block_with_role_once(self):
        b = self.blokken()
        ontstaat = [x for x in b if x["soort"] == "ontstaat" and x["stap"] == "Aanbod maken"]
        self.assertEqual(len(ontstaat), 1)
        self.assertEqual(ontstaat[0]["wie"], "planner")

    def test_given_verdieping_in_same_step_when_grouped_then_own_block_named_and_drawn_with_it(self):
        extra = [{"fase": 2, "stap": "Aanbod maken", "verdieping": "aanbod naar skills", "soort": "verandert", "wie": "planner",
                  "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "toestand": "verdiept", "bron": "b"}]
        b = [x for x in self.blokken(regels(extra)) if x["soort"] == "ontstaat" and x["stap"] == "Aanbod maken"]
        self.assertEqual([x.get("verdieping") for x in b], [None, "aanbod naar skills"])
        self.assertTrue(tv.bestandsnaam(b[1], 2).endswith("-aanbod-maken-verdieping.svg"))
        self.assertFalse(tv.bestandsnaam(b[0], 1).endswith("-verdieping.svg"))
        self.assertEqual(tv.bestandsnaam({"fase": 1, "beeld": "Leeruitkomsten uit het dossier, in de stem van de instelling"}), "f1-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.svg")
        self.assertIn("verdieping: aanbod naar skills", teksten(tv.regel_ontstaat(b[1], set())))
        self.assertNotIn("verdieping: aanbod naar skills", teksten(tv.regel_ontstaat(b[0], set())))

    def test_given_beeld_id_when_drawn_then_id_before_title_and_first_in_filename(self):
        r = regels()
        for x in r["regels"][:3]:
            x["beeld_id"], x["beeld"] = "F2-01", "Het aanbod gemaakt"
        blok = [b for b in self.blokken(r) if b.get("beeld")][0]
        self.assertEqual(tv.beeldtitel(blok), "F2-01 - Het aanbod gemaakt")
        self.assertEqual(tv.bestandsnaam(blok), "f2-01-het-aanbod-gemaakt.svg")
        self.assertIn("F2-01 - Het aanbod gemaakt", teksten(tv.regel_ontstaat(blok, set())))

    def test_given_specialization_when_nested_then_child_lands_in_the_specialization(self):
        r = {"scope_uitzonderingen": [], "regels": [
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Keuzedeel", "instantie": "K0262", "bron": "b",
             "relatie": {"soort": "Specialization", "van": "Keuzedeel", "naar": "Opleidingsprogramma specificatie"}},
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Onderwijseenheid specificatie", "instantie": "D1-K1", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie", "naar": "Onderwijseenheid specificatie", "nesting": True}},
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Onderwijseenheid specificatie", "instantie": "D1-K2", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie", "naar": "Onderwijseenheid specificatie", "nesting": True}},
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Leeronderdeel specificatie", "instantie": "D1-K2-W1", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Onderwijseenheid specificatie", "naar": "Leeronderdeel specificatie", "nesting": True}}]}
        blok = self.blokken(r)[0]
        keuzedeel = blok["objecten"][0]
        self.assertEqual(keuzedeel["type"], "Keuzedeel")
        eenheden = keuzedeel["kinderen"]
        self.assertEqual([k["instantie"] for k in eenheden], ["D1-K1", "D1-K2"])
        # het leeronderdeel hangt onder de laatst getoonde eenheid, niet onder de eerste
        self.assertEqual([k["instantie"] for k in eenheden[1]["kinderen"]], ["D1-K2-W1"])
        self.assertNotIn("kinderen", eenheden[0])

    def test_given_specialization_in_a_flow_when_nested_then_child_lands_in_the_specialization(self):
        # F6-02: de specificatiestructuur van een keuzedeel stroomt als geheel naar het studentkeuzesysteem
        stroom = {"beeld_id": "F6-02", "beeld": "Specificatie naar het SKS", "fase": 6, "stap": "Ontsluiten", "soort": "stroomt",
                  "van": "Onderwijscatalogus", "naar": "Student Keuze Systeem (SKS)", "pijl": "rel-1", "koppeling": None, "bron": "b"}
        r = {"scope_uitzonderingen": [], "regels": [
            {**stroom, "objecttype": "Keuzedeel specificatie", "instantie": "K0037",
             "relatie": {"soort": "Specialization", "van": "Keuzedeel specificatie", "naar": "Opleidingsprogramma specificatie"}},
            {**stroom, "objecttype": "Onderwijseenheid specificatie", "instantie": "D1-K1",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie", "naar": "Onderwijseenheid specificatie", "nesting": True}},
            {**stroom, "objecttype": "Leeronderdeel specificatie", "instantie": "Het medicatieoverzicht opstellen",
             "relatie": {"soort": "Aggregation", "van": "Onderwijseenheid specificatie", "naar": "Leeronderdeel specificatie", "nesting": True}}]}
        blok = self.blokken(r)[0]
        self.assertEqual(len(blok["objecten"]), 1)
        eenheid = blok["objecten"][0]["kinderen"][0]
        self.assertEqual(eenheid["instantie"], "D1-K1")
        self.assertEqual([k["instantie"] for k in eenheid["kinderen"]], ["Het medicatieoverzicht opstellen"])

    def test_given_specialization_among_extra_relations_when_nested_then_child_lands_in_the_specialization(self):
        # F6-04: de verbintenis hangt met 'middels' aan de aanmelding en is daarnaast een specialisatie
        r = {"scope_uitzonderingen": [], "regels": [
            {"beeld_id": "F6-04", "beeld": "Jochem kiest", "fase": 6, "stap": "Kiezen", "soort": "ontstaat", "wie": "student",
             "objecttype": "Aanmelding", "instantie": "Keuze K0037", "bron": "b"},
            {"beeld_id": "F6-04", "beeld": "Jochem kiest", "fase": 6, "stap": "Kiezen", "soort": "ontstaat", "wie": "student",
             "objecttype": "Keuzedeel aanbod verbintenis", "instantie": "Jochem op K0037", "bron": "b",
             "relatie": {"soort": "Association", "van": "Aanmelding", "naar": "Keuzedeel aanbod verbintenis", "label": "middels"},
             "relaties": [{"soort": "Specialization", "van": "Keuzedeel aanbod verbintenis", "naar": "Opleidingsprogramma aanbod verbintenis"}]},
            {"beeld_id": "F6-04", "beeld": "Jochem kiest", "fase": 6, "stap": "Kiezen", "soort": "ontstaat", "wie": "student",
             "objecttype": "Onderwijseenheid aanbod verbintenis", "instantie": "Jochem op D1-K1", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma aanbod verbintenis", "naar": "Onderwijseenheid aanbod verbintenis", "nesting": True}}]}
        blok = self.blokken(r)[0]
        verbintenis = next(o for o in blok["objecten"] if o.get("type") == "Keuzedeel aanbod verbintenis")
        self.assertEqual([k["instantie"] for k in verbintenis.get("kinderen", [])], ["Jochem op D1-K1"])
        self.assertNotIn("Jochem op D1-K1", [o.get("instantie") for o in blok["objecten"]])

    def herkomstregels(self, met_herkomstbeeld=True):
        """F6-01 in het klein: de specificatie uit F1-08 staat links, het aanbod ontstaat rechts."""
        b = {"beeld_id": "F6-01", "beeld": "Aanbod per laag", "fase": 6, "stap": "Aanbod maken", "bron": "b"}
        f1 = {"beeld_id": "F1-08", "beeld": "Keuzedeel ontworpen", "fase": 1, "stap": "Keuzedeel vormgeven", "bron": "b",
              "soort": "ontstaat", "wie": "onderwijsontwerper"}
        regels = [
            {**b, "soort": "bestaat", "objecttype": "Keuzedeel specificatie", "instantie": "K0037", "herkomst": "F1-08",
             "relatie": {"soort": "Specialization", "van": "Keuzedeel specificatie", "naar": "Opleidingsprogramma specificatie"}},
            {**b, "soort": "bestaat", "objecttype": "Onderwijseenheid specificatie", "instantie": "D1-K1", "herkomst": "F1-08",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie", "naar": "Onderwijseenheid specificatie", "nesting": True}},
            {**b, "soort": "ontstaat", "wie": "planner", "objecttype": "Keuzedeel aanbod", "instantie": "K0037, periode 7",
             "relatie": {"soort": "Specialization", "van": "Keuzedeel aanbod", "naar": "Opleidingsprogramma aanbod"},
             "relaties": [{"soort": "Association", "van": "Keuzedeel specificatie", "naar": "Keuzedeel aanbod", "label": "wordt aangeboden als", "instantie": "K0037"}]},
            {**b, "soort": "ontstaat", "wie": "planner", "objecttype": "Onderwijseenheid aanbod", "instantie": "D1-K1, periode 7",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma aanbod", "naar": "Onderwijseenheid aanbod", "nesting": True},
             "relaties": [{"soort": "Association", "van": "Onderwijseenheid specificatie", "naar": "Onderwijseenheid aanbod", "label": "wordt aangeboden als", "instantie": "D1-K1"}]}]
        if met_herkomstbeeld:
            regels.insert(0, {**f1, "objecttype": "Keuzedeel specificatie", "instantie": "K0037"})
        return {"scope_uitzonderingen": [], "regels": regels}

    def herkomstblok(self, met_herkomstbeeld=True):
        return [x for x in self.blokken(self.herkomstregels(met_herkomstbeeld)) if x.get("beeld_id") == "F6-01"][0]

    def test_given_bestaat_rules_when_grouped_then_own_column_with_herkomst_and_nesting(self):
        blok = self.herkomstblok()
        self.assertEqual([o["type"] for o in blok["bestaand"]], ["Keuzedeel specificatie"])
        self.assertEqual(blok["bestaand"][0]["herkomst"], "F1-08")
        self.assertEqual([k["instantie"] for k in blok["bestaand"][0]["kinderen"]], ["D1-K1"])
        self.assertNotIn("Keuzedeel specificatie", [o.get("type") for o in blok["objecten"]])
        self.assertEqual(blok["wie"], "planner")
        # de processtap waarin het bestaande object ontstond, staat boven de kolom links
        self.assertEqual(blok["herkomst_kop"], {"beeld_id": "F1-08", "stap": "Keuzedeel vormgeven", "wie": "onderwijsontwerper"})

    def test_given_relation_to_a_bestaat_object_when_grouped_then_a_line_and_no_reference(self):
        blok = self.herkomstblok()
        lijnen = {(l["bron"], l["doel"], l["label"]) for l in blok["herkomstlijnen"]}
        self.assertEqual(lijnen, {(("Keuzedeel specificatie", "K0037"), ("Keuzedeel aanbod", "K0037, periode 7"), "wordt aangeboden als"),
                                  (("Onderwijseenheid specificatie", "D1-K1"), ("Onderwijseenheid aanbod", "D1-K1, periode 7"), "wordt aangeboden als")})
        aanbod = blok["objecten"][0]
        self.assertFalse(any("wordt aangeboden als" in v for v in aanbod.get("verwijzingen", [])))
        self.assertFalse(any("wordt aangeboden als" in v for v in aanbod["kinderen"][0].get("verwijzingen", [])))

    def test_given_bestaat_objects_when_drawn_then_two_panels_with_role_over_step_and_a_trigger(self):
        svg = tv.regel_ontstaat(self.herkomstblok(), set())
        t = teksten(svg)
        self.assertIn("Eerder ontstaan · F1-08", t)
        self.assertIn("Ontstaat hier · F6-01", t)
        self.assertIn("Keuzedeel vormgeven", t)
        self.assertIn("onderwijsontwerper", t)
        self.assertIn("Aanbod maken", t)
        paden = {p.get("class") for p in ET.fromstring(svg).iter(f"{SVG}path")}
        # de rol voert de processtap uit (toewijzing) en de eerdere processtap triggert de huidige
        self.assertEqual(sum(1 for p in ET.fromstring(svg).iter(f"{SVG}path") if p.get("class") == "toewijzing"), 2)
        self.assertIn("trigger", paden)
        vlakken = {r.get("class"): r for r in rects(svg) if r.get("class")}
        self.assertEqual(vlakken["vlak-eerder"]["fill"], tv.VLAK_EERDER)
        self.assertEqual(vlakken["vlak-hier"]["stroke"], tv.VLAK_HIER_L)

    def test_given_bestaat_objects_when_drawn_then_a_line_per_relation_on_top_of_the_boxes(self):
        svg = tv.regel_ontstaat(self.herkomstblok(), set())
        self.assertEqual(teksten(svg).count("wordt aangeboden als"), 2)
        lijnen = [p for p in ET.fromstring(svg).iter(f"{SVG}path") if p.get("class") == "herkomstlijn"]
        self.assertEqual(len(lijnen), 2)
        # de lijnen liggen boven de vakken, zodat de pijlpunt naar een genest object zichtbaar blijft
        self.assertGreater(svg.rindex('class="herkomstlijn"'), svg.rindex("D1-K1, periode 7"))

    def test_given_bestaat_objects_when_drawn_then_objects_keep_the_archimate_business_look(self):
        svg = tv.regel_ontstaat(self.herkomstblok(), set())
        objectvakken = [r for r in rects(svg) if r.get("fill") == tv.BUS and r.get("rx") == "0"]
        self.assertEqual(len(objectvakken), 4)
        self.assertEqual({r.get("stroke") for r in objectvakken}, {tv.BUS_L})

    def test_given_herkomst_beeld_when_drawn_then_a_visual_legend_in_the_image(self):
        t = teksten(tv.regel_ontstaat(self.herkomstblok(), set()))
        for sleutel in tv.LEGENDA_HERKOMST:
            self.assertIn(sleutel, t)

    def test_given_paired_layers_when_drawn_then_each_pair_on_the_same_height(self):
        # het aanbod rechts draagt een toestand en is daardoor hoger dan de specificatie links;
        # de laag eronder moet toch op dezelfde hoogte beginnen
        r = self.herkomstregels()
        r["regels"][3]["toestand"] = "gepland"
        blok = [x for x in self.blokken(r) if x.get("beeld_id") == "F6-01"][0]
        svg = tv.regel_ontstaat(blok, set())
        root = ET.fromstring(svg)
        y_van = {t.text: float(t.get("y")) for t in root.iter(f"{SVG}text")}
        x_van = {t.text: float(t.get("x")) for t in root.iter(f"{SVG}text")}
        self.assertEqual(y_van["K0037"], y_van["K0037, periode 7"])
        self.assertEqual(y_van["D1-K1"], y_van["D1-K1, periode 7"])
        self.assertLess(x_van["K0037"], x_van["K0037, periode 7"])

    def test_given_pairs_out_of_order_when_drawn_then_left_column_stacked_inside_its_panel(self):
        # twee bestaande objecten waarvan de paren rechts in omgekeerde volgorde staan: geen uitlijning,
        # maar de kolom links blijft onder elkaar en binnen haar vlak
        r = self.herkomstregels()
        b = {k: r["regels"][1][k] for k in ("beeld_id", "beeld", "fase", "stap", "bron")}
        r["regels"].insert(1, {**b, "soort": "bestaat", "objecttype": "Planningsgroep", "instantie": "PG", "herkomst": "F1-08"})
        r["regels"].insert(0, {"beeld_id": "F1-08", "beeld": "Keuzedeel ontworpen", "fase": 1, "stap": "Keuzedeel vormgeven", "bron": "b",
                               "soort": "ontstaat", "wie": "planner", "objecttype": "Planningsgroep", "instantie": "PG"})
        r["regels"][-1]["relaties"] = r["regels"][-1].get("relaties", []) + [
            {"soort": "Association", "van": "Planningsgroep", "naar": "Onderwijseenheid aanbod", "label": "plant", "voorstel": True, "instantie": "PG"}]
        blok = [x for x in self.blokken(r) if x.get("beeld_id") == "F6-01"][0]
        svg = tv.regel_ontstaat(blok, set())
        root = ET.fromstring(svg)
        vlak = {x.get("class"): x for x in root.iter(f"{SVG}rect") if x.get("class")}
        rand = float(vlak["vlak-eerder"].get("x")) + float(vlak["vlak-eerder"].get("width"))
        links = [x for x in root.iter(f"{SVG}rect") if x.get("fill") == tv.BUS and x.get("rx") == "0"
                 and float(x.get("x")) < float(vlak["vlak-hier"].get("x"))]
        self.assertTrue(links)
        for x in links:
            self.assertLessEqual(float(x.get("x")) + float(x.get("width")), rand)

    def test_given_herkomst_beeld_unknown_when_drawn_then_chip_per_object(self):
        svg = tv.regel_ontstaat(self.herkomstblok(met_herkomstbeeld=False), set())
        t = teksten(svg)
        self.assertIn("uit F1-08", t)
        self.assertIn("Eerder ontstaan", t)
        self.assertIn("Ontstaat hier · F6-01", t)

    def test_given_relation_at_the_start_of_a_next_row_when_drawn_then_reference_names_the_other_end(self):
        items = [{"type": "Leergelegenheid", "instantie": "Medicatieoverzicht, periode 7", "verwijzingen": []},
                 {"relatie": "", "soort": "Association", "naar_rechts": True, "ander": "Leergelegenheid",
                  "ander_instantie": "Medicatieoverzicht, periode 7"},
                 {"type": "Leergelegenheid verbintenis", "instantie": "Jochem op Medicatieoverzicht", "verwijzingen": []}]
        svg, *_ = tv._objecten_rijen(0, 0, items, set(), maxbreedte=200)
        self.assertIn("Leergelegenheid hangt aan: Medicatieoverzicht, periode 7",
                      teksten(f'<svg xmlns="http://www.w3.org/2000/svg">{svg}</svg>'))

    def test_given_relation_proposal_when_grouped_then_reference_marked_and_object_not_a_proposal(self):
        r = {"scope_uitzonderingen": [], "regels": [
            {"beeld_id": "F2-08", "beeld": "Plannen", "fase": 2, "stap": "Plannen", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Planningsgroep", "instantie": "K0037 periode 7", "bron": "b",
             "relatie": {"soort": "Association", "van": "Planningsgroep", "naar": "Keuzedeel aanbod", "label": "plant", "voorstel": True}}]}
        item = self.blokken(r)[0]["objecten"][0]
        self.assertIn("plant Keuzedeel aanbod (voorstel)", item.get("verwijzing", ""))
        self.assertFalse(item.get("aanname"))
        self.assertNotIn(tv.VOORSTEL_MERK, item.get("verwijzingen", []))

    def test_given_state_on_a_created_object_when_drawn_then_state_is_shown(self):
        r = regels()
        r["regels"][0]["toestand"] = "intentie"
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        self.assertEqual(blok["objecten"][0]["toestand"], "intentie")
        self.assertIn("toestand: intentie", teksten(tv.regel_ontstaat(blok, set())))

    def test_given_relation_to_object_earlier_in_the_block_when_grouped_then_line_over_distance(self):
        r = regels()
        r["regels"].insert(3, {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Student keuze regelset", "instantie": "Regels", "bron": "b",
                               "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Student keuze regelset"}})
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        self.assertEqual(blok["objecten"][-1]["type"], "Student keuze regelset")
        # het andere eind staat verder terug in het blok: een relatie met een omweg, geen verwijzing
        rel = blok["objecten"][-2]
        self.assertTrue(rel.get("over_afstand"))
        self.assertEqual(rel["ander"], "Opleidingaanbod")
        self.assertNotIn("verwijzing", blok["objecten"][-1])

    def test_given_relation_to_object_outside_the_block_when_grouped_then_reference(self):
        r = regels()
        r["regels"].insert(3, {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Student keuze regelset", "instantie": "Regels", "bron": "b",
                               "relatie": {"soort": "Association", "van": "Kerntaak", "naar": "Student keuze regelset"}})
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        laatste = blok["objecten"][-1]
        self.assertEqual(laatste["type"], "Student keuze regelset")
        self.assertEqual(laatste["verwijzing"], "Kerntaak hangt aan")

    def test_given_a_line_over_distance_when_drawn_then_it_routes_around_the_boxes(self):
        r = regels()
        r["regels"].insert(3, {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Student keuze regelset", "instantie": "Regels", "bron": "b",
                               "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Student keuze regelset", "label": "hangt aan"}})
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        svg = tv.regel_ontstaat(blok, set())
        # een omweg is een pad met twee knikken: horizontaal, verticaal, horizontaal
        paden = [m for m in re.findall(r'd="(M[^"]+)"', svg) if "H" in m and "V" in m]
        self.assertTrue(paden, "verwacht een haaks pad voor de relatie over afstand")

    def test_given_lines_from_several_existing_objects_to_one_target_when_drawn_then_the_label_once(self):
        # F6-06: vier verbintenissen worden in dezelfde planningsgroep geplaatst; vier labels vallen over elkaar
        tv.POSITIES.clear()
        for i, n in enumerate("abcd"):
            tv.POSITIES[("V", n)] = (10, 10 + 80 * i, 200)
        tv.POSITIES[("P", "p")] = (400, 10, 200)
        blok = {"herkomstlijnen": [{"bron": ("V", n), "doel": ("P", "p"), "soort": "Association",
                                    "label": "wordt geplaatst in", "naar_rechts": True} for n in "abcd"]}
        svg = tv._herkomstlijnen(blok, 210)
        self.assertEqual(svg.count("herkomstlijn"), 4)
        self.assertEqual(teksten(f'<svg xmlns="http://www.w3.org/2000/svg">{svg}</svg>').count("wordt geplaatst in"), 1)

    def test_given_a_line_over_distance_to_a_nested_object_when_drawn_then_the_line_is_not_dropped(self):
        # F2-08: de planningsgroep is gepland op de onderwijseenheid, die genest in het opleidingsprogramma staat
        items = [{"type": "A", "instantie": "a", "verwijzingen": [],
                  "kinderen": [{"type": "B", "instantie": "b", "verwijzingen": []}]},
                 {"type": "C", "instantie": "c", "verwijzingen": []},
                 {"relatie": "is gepland op", "soort": "Association", "naar_rechts": False, "ander": "B", "over_afstand": True},
                 {"type": "D", "instantie": "d", "verwijzingen": []}]
        tv.POSITIES.clear()
        svg, _, _ = tv.objecten(10, 10, items, set())
        self.assertIn("is gepland op", teksten(f'<svg xmlns="http://www.w3.org/2000/svg">{svg}</svg>'))
        paden = [m for m in re.findall(r'd="(M[^"]+)"', svg) if "H" in m and "V" in m]
        self.assertTrue(paden, "verwacht een haaks pad naar het geneste object")

    def test_given_a_line_over_distance_when_drawn_then_the_label_is_shown(self):
        r = regels()
        r["regels"].insert(3, {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Student keuze regelset", "instantie": "Regels", "bron": "b",
                               "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Student keuze regelset", "label": "stuurt"}})
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        self.assertIn("stuurt", teksten(tv.regel_ontstaat(blok, set())))

    def test_given_concept_block_when_drawn_then_chip_and_dashed_frame(self):
        extra = [{"fase": 2, "stap": "Aanbod maken", "verdieping": "kader", "plaat": "onderwijsontwerp", "soort": "ontstaat", "wie": "planner",
                  "objecttype": "Leervormstrategie", "instantie": "Leren door te doen", "bron": "c"}]
        blokken = [b for b in self.blokken(regels(extra)) if b["stap"] == "Aanbod maken"]
        self.assertEqual([b.get("plaat") for b in blokken], ["informatiemodel", "onderwijsontwerp"])
        svg = tv.regel_ontstaat(blokken[1], set())
        self.assertIn("conceptplaat: Informatiemodel Onderwijsontwerp", teksten(svg))
        self.assertIn("6 4", rects(svg)[0].get("stroke-dasharray", ""))
        self.assertNotIn("stroke-dasharray", rects(tv.regel_ontstaat(blokken[0], set()))[0])

    def test_given_beeld_title_when_grouped_then_own_block_titled_and_filename_from_title(self):
        r = regels()
        for x in r["regels"][:2]:
            x["beeld"] = "Het aanbod gemaakt: opleiding en programma"
        r["regels"][2]["beeld"] = "Het cohort erbij"
        blokken = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"]
        self.assertEqual([b.get("beeld") for b in blokken], ["Het aanbod gemaakt: opleiding en programma", "Het cohort erbij"])
        self.assertEqual(tv.bestandsnaam(blokken[0]), "f2-het-aanbod-gemaakt-opleiding-en-programma.svg")
        svg = tv.regel_ontstaat(blokken[0], set())
        self.assertIn("Het aanbod gemaakt: opleiding en programma", teksten(svg))
        self.assertNotIn("Het cohort erbij", teksten(svg))

    def test_given_extra_relations_when_grouped_then_each_a_reference_with_instance_and_stacked(self):
        r = regels()
        r["regels"][3]["relaties"] = [{"soort": "Association", "van": "Opleidingaanbod", "naar": "Leeruitkomst", "instantie": "Baliegesprek"},
                                      {"soort": "Association", "van": "Toetsonderdeel specificatie", "naar": "Opleidingaanbod", "label": "toetst"}]
        blok = [b for b in self.blokken(r) if b["soort"] == "stroomt"][0]
        self.assertEqual(blok["objecten"][0]["verwijzingen"], ["hangt aan Leeruitkomst: Baliegesprek", "Toetsonderdeel specificatie toetst"])
        svg = tv.regel_stroomt(blok, set())
        ys = {x.text: float(x.get("y")) for x in ET.fromstring(svg).iter(f"{SVG}text") if x.text in ("hangt aan Leeruitkomst: Baliegesprek", "Toetsonderdeel specificatie toetst")}
        self.assertEqual(len(ys), 2)
        self.assertNotEqual(*ys.values())

    def test_given_ontstaat_rule_when_drawn_then_svg_contains_role_step_and_each_instance(self):
        blok = self.blokken()[0]
        svg = tv.regel_ontstaat(blok, {"Lesgelegenheid"})
        t = teksten(svg)
        for s in ("planner", "Aanbod maken", "Apothekersassistent 2026", "Regulier BOL 2026", "2026"):
            self.assertIn(s, t)
        self.assertEqual(svg.count(tv.ICONS["proces"]), 1)

    def test_given_nested_objects_when_drawn_then_child_rect_within_parent_rect(self):
        blok = self.blokken()[0]
        svg = tv.regel_ontstaat(blok, set())
        rs = [r for r in rects(svg) if r.get("fill") == tv.BUS and r.get("rx", "0") == "0"]
        rs = sorted(rs, key=lambda r: float(r["width"]), reverse=True)
        ouder, kind = rs[0], next(r for r in rs[1:] if float(r["x"]) > float(rs[0]["x"]))
        self.assertGreaterEqual(float(kind["x"]), float(ouder["x"]))
        self.assertLessEqual(float(kind["x"]) + float(kind["width"]), float(ouder["x"]) + float(ouder["width"]))
        self.assertLessEqual(float(kind["y"]) + float(kind["height"]), float(ouder["y"]) + float(ouder["height"]))

    def test_given_container_with_toestand_when_drawn_then_toestand_shown_above_children(self):
        extra = [{"fase": 4, "stap": "Roosteren", "soort": "verandert", "wie": "roosteraar", "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "toestand": "geroosterd", "bron": "b"},
                 {"fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "roosteraar", "objecttype": "Onderwijseenheid aanbod", "instantie": "Blok 1", "bron": "b",
                  "relatie": {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Onderwijseenheid aanbod", "nesting": True}}]
        blok = [b for b in self.blokken(regels(extra)) if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, set())
        ts = {t.text: (float(t.get("x")), float(t.get("y"))) for t in ET.fromstring(svg).iter(f"{SVG}text") if t.text}
        self.assertIn("toestand: geroosterd", ts)
        self.assertLess(ts["toestand: geroosterd"][1], ts["Blok 1"][1])
        self.assertIn(("AA 2026"), ts)

    def test_given_wide_row_of_children_when_drawn_then_stacked_within_parent(self):
        lang = "Een heel lange instantienaam die de rij van kinderen ver voorbij de maximale breedte duwt"
        extra = [{"fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "roosteraar", "objecttype": f"Kind {i}", "instantie": lang, "bron": "b",
                  "relatie": {"soort": "Aggregation", "van": "Lesgelegenheid", "naar": f"Kind {i}", "nesting": True}} for i in range(3)]
        blok = [b for b in self.blokken(regels(extra)) if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, set())
        ys = {t.text: float(t.get("y")) for t in ET.fromstring(svg).iter(f"{SVG}text") if t.text and t.text.startswith("Kind ")}
        self.assertEqual(len(ys), 3)
        self.assertEqual(len(set(ys.values())), 3)
        self.assertLess(float(ET.fromstring(svg).get("width")), 1500)

    def test_given_assumption_when_drawn_then_rect_has_dasharray(self):
        blok = self.blokken()[0]
        svg = tv.regel_ontstaat(blok, set())
        gestippeld = [r for r in rects(svg) if r.get("stroke-dasharray") == "5 3"]
        self.assertEqual(len(gestippeld), 1)

    def test_given_proposal_when_drawn_then_marked_in_the_box_and_dashed(self):
        extra = [{"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
                  "objecttype": "Nominale leerroute", "instantie": "Jochem, cohort 2026", "bron": "b", "voorstel": True}]
        blok = [x for x in self.blokken(regels(extra))
                if any(o.get("type") == "Nominale leerroute" for o in x["objecten"])][0]
        svg = tv.regel_ontstaat(blok, set())
        self.assertIn(tv.VOORSTEL_MERK, teksten(svg))
        self.assertEqual(len([r for r in rects(svg) if r.get("stroke-dasharray") == "5 3"]), 1)

    def test_given_no_proposal_when_drawn_then_no_mark(self):
        svg = tv.regel_ontstaat(self.blokken()[0], set())
        self.assertNotIn(tv.VOORSTEL_MERK, teksten(svg))

    def test_given_relation_label_when_drawn_then_label_between_objects(self):
        svg = tv.regel_ontstaat(self.blokken()[0], set())
        self.assertIn("Op basis van", teksten(svg))

    def test_given_scope_exception_when_drawn_then_grey_fill(self):
        blok = [b for b in self.blokken() if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, {"Lesgelegenheid"})
        self.assertTrue(any(r.get("fill") == tv.GRIJS for r in rects(svg)))

    def test_given_verandert_rule_when_drawn_then_toestand_shown(self):
        blok = [b for b in self.blokken() if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, set())
        self.assertIn("toestand: geroosterd", teksten(svg))

    def test_given_stroomt_rule_when_drawn_then_van_naar_object_id_and_step(self):
        blok = [b for b in self.blokken() if b["soort"] == "stroomt"][0]
        svg = tv.regel_stroomt(blok, set())
        t = teksten(svg)
        for s in ("Planningssysteem", "Onderwijscatalogus", "Opleidingaanbod", "OC-P&R", "na: Aanbod publiceren"):
            self.assertIn(s, t)
        self.assertTrue(any(r.get("fill") == tv.APP for r in rects(svg)))

    def test_given_first_stroomt_object_with_relation_when_grouped_then_reference_shown(self):
        r = regels()
        r["regels"][3]["relatie"] = {"soort": "Specialization", "van": "Opleidingaanbod", "naar": "Opleidingsaanbod van Instelling"}
        blok = [b for b in self.blokken(r) if b["soort"] == "stroomt"][0]
        self.assertEqual(blok["objecten"][0]["verwijzing"], "is een Opleidingsaanbod van Instelling")

    def test_given_stroomt_without_koppeling_when_drawn_then_marked(self):
        blok = [b for b in self.blokken() if b["soort"] == "stroomt"][0]
        blok["koppeling"] = None
        svg = tv.regel_stroomt(blok, set())
        self.assertIn("zonder koppelingspecificatie", teksten(svg))

    def test_given_stroomt_without_arrow_on_hoofdplaat_when_drawn_then_marked_as_such(self):
        extra = [{"fase": 2, "stap": "Aanbod publiceren", "soort": "stroomt", "van": "Curriculum ontwerptool", "naar": "Onderwijscatalogus",
                  "pijl": "geen pijl op de hoofdplaat", "koppeling": None, "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "bron": "b"}]
        blok = [b for b in self.blokken(regels(extra)) if b["soort"] == "stroomt" and b["van"] == "Curriculum ontwerptool"][0]
        svg = tv.regel_stroomt(blok, set())
        self.assertIn("geen pijl op de hoofdplaat", teksten(svg))
        self.assertNotIn("zonder koppelingspecificatie", teksten(svg))

    def test_given_any_rule_when_drawn_then_svg_wellformed_and_self_contained(self):
        for blok in self.blokken():
            svg = tv.regel_stroomt(blok, set()) if blok["soort"] == "stroomt" else tv.regel_ontstaat(blok, set())
            ET.fromstring(svg)
            for verboden in ("<link", "@import", "url(", "<script", "<foreignObject"):
                self.assertNotIn(verboden, svg)

    def test_given_long_instance_name_when_drawn_then_text_fits_box(self):
        naam = "x" * 60
        s, w, h = tv.element(0, 0, "object", "Objecttype", naam)
        self.assertGreaterEqual(w, tv.tw(naam, 13, True) + 42)

    def test_given_special_characters_when_drawn_then_escaped(self):
        r = regels(); r["regels"][0]["instantie"] = "A & <B> 'C'"
        svg = tv.regel_ontstaat(tv.groepeer(r)[0], set())
        ET.fromstring(svg)

    def test_given_empty_relation_label_when_validated_then_exit(self):
        r = regels(); r["regels"][2]["relatie"]["label"] = ""
        with self.assertRaises(SystemExit):
            tv.valideer(r)

    def test_given_missing_instance_when_validated_then_exit_names_type(self):
        r = regels(); r["regels"][0]["instantie"] = ""
        with self.assertRaises(SystemExit) as fout:
            tv.valideer(r)
        self.assertIn("Opleidingaanbod", str(fout.exception))

    def test_given_unknown_kind_when_validated_then_exit(self):
        r = regels(); r["regels"][0]["soort"] = "verdwijnt"
        with self.assertRaises(SystemExit):
            tv.valideer(r)

    def test_given_table_when_drawn_then_one_file_per_block_with_deterministic_names(self):
        with tempfile.TemporaryDirectory() as map_:
            uit = tv.teken(regels(), map_)
            self.assertEqual(len(uit), len(tv.groepeer(regels())))
            self.assertEqual(len(list(Path(map_).glob("*.svg"))), len(uit))
            self.assertTrue(all(n.startswith("f") and n.endswith(".svg") for n, _ in uit))

    def test_given_same_input_twice_when_drawn_then_identical_output(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            tv.teken(regels(), a); tv.teken(regels(), b)
            for p in Path(a).glob("*.svg"):
                self.assertEqual(p.read_bytes(), (Path(b) / p.name).read_bytes())

    def test_given_missing_table_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            self.assertEqual(tv.main(["--regels", str(Path(map_) / "geen.json"), "--uit", map_]), 2)


class BeeldIsBestandTests(unittest.TestCase):
    """Een beeld is een bestand. Viel een beeld in twee blokken, dan overschreef het tweede het eerste
    en toonde het beeld minder dan de tabel zegt."""

    def beeld_regels(self):
        r = regels()
        for x in r["regels"][:3]:
            x["beeld_id"], x["beeld"] = "F2-01", "Het aanbod gemaakt"
        r["regels"][2]["wie"] = "onderwijsontwerper"
        return r

    def test_given_an_image_whose_rules_change_role_when_grouped_then_one_block_with_both_roles(self):
        blokken = [b for b in tv.groepeer(self.beeld_regels()) if b.get("beeld")]
        self.assertEqual(len(blokken), 1)
        self.assertEqual(blokken[0]["rollen"], ["planner", "onderwijsontwerper"])
        self.assertEqual(blokken[0]["wie"], "planner, onderwijsontwerper")
        def tel(items):
            return sum(1 + tel(o.get("kinderen", [])) for o in items if "type" in o)
        self.assertEqual(tel(blokken[0]["objecten"]), 3)   # de genestte blijft meetellen

    def test_given_an_image_with_two_roles_when_drawn_then_both_stand_in_the_header(self):
        blok = [b for b in tv.groepeer(self.beeld_regels()) if b.get("beeld")][0]
        self.assertIn("planner, onderwijsontwerper", teksten(tv.regel_ontstaat(blok, set())))

    def test_given_rules_without_an_image_when_grouped_then_the_role_still_separates_blocks(self):
        r = regels()
        r["regels"][2]["wie"] = "onderwijsontwerper"
        rollen = [b.get("wie") for b in tv.groepeer(r) if b["soort"] == "ontstaat" and b["stap"] == "Aanbod maken"]
        self.assertEqual(rollen, ["planner", "onderwijsontwerper"])

    def test_given_two_blocks_with_the_same_filename_when_drawn_then_it_stops_and_names_both(self):
        r = regels()
        for x in r["regels"][:3]:
            x["beeld_id"], x["beeld"] = "F2-01", "Het aanbod gemaakt"
        r["regels"][1]["stap"] = "Aanbod publiceren"   # eigen blok, zelfde beeld en dus zelfde naam
        with tempfile.TemporaryDirectory() as map_:
            with self.assertRaises(SystemExit) as fout:
                tv.teken(r, Path(map_))
        self.assertIn("f2-01-het-aanbod-gemaakt.svg", str(fout.exception))
        self.assertIn("een beeld is een bestand", str(fout.exception))

    def test_given_the_real_table_when_drawn_then_every_block_gets_its_own_file(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/leerroute-uitwerking-model-lr1.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as map_:
            uit = tv.teken(tabel, Path(map_))
            self.assertEqual(len(uit), len({n for n, _ in uit}))
            self.assertEqual(len(uit), len(list(Path(map_).glob("*.svg"))))


class OpruimenTests(unittest.TestCase):
    def test_given_a_renamed_image_when_drawn_then_the_old_file_is_gone(self):
        with tempfile.TemporaryDirectory() as map_:
            tv.teken(regels(), Path(map_))
            (Path(map_) / "f9-99-oude-naam.svg").write_text("<svg/>", encoding="utf-8")
            tv.teken(regels(), Path(map_), opruimen=True)
            self.assertFalse((Path(map_) / "f9-99-oude-naam.svg").exists())

    def test_given_the_keep_switch_when_drawn_then_the_orphan_stays(self):
        with tempfile.TemporaryDirectory() as map_:
            tv.teken(regels(), Path(map_))
            (Path(map_) / "f9-99-oude-naam.svg").write_text("<svg/>", encoding="utf-8")
            tv.teken(regels(), Path(map_), opruimen=False)
            self.assertTrue((Path(map_) / "f9-99-oude-naam.svg").exists())


class MatenTests(unittest.TestCase):
    """De uitvoer noemt per beeld de hoogte en de banen, zodat een onleesbaar beeld opvalt."""

    def test_given_a_run_when_it_reports_then_each_image_carries_its_size_and_bands(self):
        import contextlib, io
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            (m / "r.json").write_text(json.dumps(regels()), encoding="utf-8")
            uit = io.StringIO()
            with contextlib.redirect_stdout(uit):
                code = tv.main(["--regels", str(m / "r.json"), "--uit", str(m / "beelden")])
            tekst = uit.getvalue()
        self.assertEqual(code, 0)
        self.assertRegex(tekst, r"\.svg: \d+ bij \d+, \d+ ba")
        self.assertIn("beelden getekend naar", tekst.splitlines()[-1])

    def test_given_no_band_when_measured_then_none_is_taller_than_the_slide_allows(self):
        """Over alle beelden van de echte tabel: een baan blijft binnen de verhouding die een slide toelaat."""
        snijd = tv._snijd()
        map_ = WORTEL / "architecture/model/informatiemodel/img/regels"
        for naam, breedte, _, hoogtes, reden in tv.maten(map_, sorted(p.name for p in map_.glob("*.svg"))):
            if reden:
                continue
            for h in hoogtes:
                self.assertLessEqual(h, breedte * snijd.VERHOUDING + 1, naam)

    def test_given_an_image_that_cannot_be_cut_when_measured_then_the_reason_comes_along(self):
        """De voorbeelduitwerking is een document, dus een beeld dat niet in banen past is geen gebrek:
        het snijden telt pas als zo'n beeld op een slide moet. Welke beelden dat zijn beweegt mee met de
        inhoud, dus dit geval legt de regel vast en geen lijst: is een beeld niet te snijden, dan noemt de
        melding het bereik waar de witregel ontbreekt."""
        map_ = WORTEL / "architecture/model/informatiemodel/img/regels"
        redenen = {naam: reden for naam, _, _, _, reden in
                   tv.maten(map_, sorted(p.name for p in map_.glob("*.svg"))) if reden}
        for naam, reden in redenen.items():
            self.assertIn("geen witregel", reden, naam)
            self.assertRegex(reden, r"tussen y=[\d.]+ en y=[\d.]+", naam)


class AfbrekenTests(unittest.TestCase):
    """Een instantie breekt af in plaats van het vak op te rekken. Zonder die regel maakt een
    leeruitkomst die volgens het tuning model is geformuleerd, en dus een hele zin is, een beeld bijna
    twee keer zo breed als een document aankan."""

    def test_given_a_long_instance_when_broken_then_every_line_fits_the_maximum(self):
        zin = ("Verleent farmaceutische patientenzorg, volgens de vigerende protocollen en met navolgbare "
               "vastlegging, in een levensechte apotheekomgeving (apothekersassistent NLQF 4, kerntaak B1-K1)")
        regels = tv.afbreken(zin, tv.INSTANTIE_MAX_BREEDTE)
        self.assertGreater(len(regels), 1)
        for r in regels:
            self.assertLessEqual(tv.tw(r, 14, True), tv.INSTANTIE_MAX_BREEDTE, r)
        self.assertEqual(" ".join(regels), zin)

    def test_given_a_long_instance_when_drawn_then_the_box_stays_within_the_maximum(self):
        zin = "x " * 60
        _, w, h = tv.element(0, 0, "object", "Leeruitkomst", zin.strip())
        self.assertLessEqual(w, tv.INSTANTIE_MAX_BREEDTE + 42)
        self.assertGreater(h, 48)

    def test_given_the_real_images_when_read_then_no_instance_line_exceeds_the_maximum(self):
        """Over alle beelden: geen enkele instantieregel is breder dan de maat die de renderer stelt."""
        map_ = WORTEL / "architecture/model/informatiemodel/img/regels"
        for pad in sorted(map_.glob("*.svg")):
            for el in ET.fromstring(pad.read_text(encoding="utf-8")).iter(f"{SVG}text"):
                if el.get("font-size") == "14" and el.get("font-weight") == "bold" and el.text:
                    self.assertLessEqual(tv.tw(el.text, 14, True), tv.INSTANTIE_MAX_BREEDTE + 1,
                                         f"{pad.name}: {el.text[:60]}")



class VoorbeeldOmweg(unittest.TestCase):
    """Het voorbeeld in tests/voorbeelden draagt drie relaties over afstand in een beeld.

    Het dient als zichtbare controle bij de pull request en als terugvaltest: gaat de routering
    stuk, dan verandert het aantal haakse paden of valt een label buiten het doek.
    """

    def setUp(self):
        pad = pathlib.Path(__file__).parent / "voorbeelden" / "omweg-regels.json"
        self.regels = json.loads(pad.read_text(encoding="utf-8"))

    def beeld(self):
        blokken = tv.groepeer(self.regels)
        return tv.regel_ontstaat(blokken[0], set())

    def test_given_the_example_when_drawn_then_three_lines_route_around_the_boxes(self):
        # een omweg loopt haaks: alleen H, V en de boogjes van een brug, en nooit schuin.
        # de pictogrammen vallen af, want die tekenen met kleine letters
        paden = [m for m in re.findall(r'd="(M[^"]+)"', self.beeld())
                 if "H" in m and "V" in m and not re.search(r"[a-z]", m)]
        self.assertEqual(len(paden), 3)

    def test_given_the_example_when_drawn_then_every_label_fits_on_the_canvas(self):
        svg = self.beeld()
        breedte = float(re.search(r'viewBox="0 0 ([\d.]+)', svg).group(1))
        for x in re.findall(r'<text x="([\d.]+)"', svg):
            self.assertLess(float(x), breedte, "tekst valt buiten het doek")

    def test_given_several_detours_when_drawn_then_each_line_has_its_own_colour(self):
        svg = self.beeld()
        kleuren = {k for k in re.findall(r'stroke="(#[0-9a-f]{6})"', svg) if k in tv.OMWEG_KLEUREN}
        self.assertEqual(len(kleuren), 3, "drie omwegen horen drie kleuren te krijgen")

    def test_given_several_detours_when_drawn_then_each_label_matches_its_line(self):
        svg = self.beeld()
        labels = re.findall(r'fill="(#[0-9a-f]{6})"[^>]*>Wordt vertaald naar<', svg)
        gekleurd = [k for k in labels if k in tv.OMWEG_KLEUREN]
        self.assertEqual(len(set(gekleurd)), 2, "twee gelijke labels horen bij twee lijnen van eigen kleur")

    def test_given_one_detour_when_drawn_then_the_line_stays_in_the_plain_colour(self):
        r = regels()
        r["regels"].insert(3, {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
                               "objecttype": "Student keuze regelset", "instantie": "Regels", "bron": "b",
                               "relatie": {"soort": "Association", "van": "Opleidingaanbod",
                                           "naar": "Student keuze regelset", "label": "stuurt"}})
        svg = tv.regel_ontstaat([b for b in tv.groepeer(r) if b["stap"] == "Aanbod maken"][0], set())
        self.assertFalse([k for k in re.findall(r'stroke="(#[0-9a-f]{6})"', svg) if k in tv.OMWEG_KLEUREN])


class OmwegDeMoeite(unittest.TestCase):
    """Wanneer een relatie over afstand een lijn wordt en wanneer zij een verwijzing blijft."""

    def objecten(self, *typen):
        return [{"type": t} for t in typen]

    def test_given_target_within_reach_when_weighed_then_a_line(self):
        self.assertTrue(tv._de_moeite(self.objecten("A", "B", "C"), "A", None))

    def test_given_target_beyond_reach_and_no_label_when_weighed_then_a_reference(self):
        self.assertFalse(tv._de_moeite(self.objecten("A", "B", "C", "D"), "A", None))

    def test_given_target_beyond_reach_but_labelled_when_weighed_then_a_line(self):
        self.assertTrue(tv._de_moeite(self.objecten("A", "B", "C", "D", "E"), "A", "hangt aan"))

    def test_given_the_block_already_holds_three_detours_when_weighed_then_a_reference(self):
        vol = self.objecten("A", "B") + [{"over_afstand": True} for _ in range(tv.OMWEG_MAX)]
        self.assertFalse(tv._de_moeite(vol, "A", "hangt aan"))


def _naast_regels(met_bestaand=True):
    """F2-08 in het klein: specificatie links, aanbod in het midden, groepen ernaast."""
    k = {"beeld_id": "F2-08", "beeld": "Planner plant", "fase": 2, "stap": "Aanbod plannen", "bron": "b"}
    r = []
    if met_bestaand:
        r.append(dict(k, soort="bestaat", objecttype="Opleidingsprogramma specificatie", instantie="s", herkomst="F1-01"))
    r += [
        dict(k, soort="ontstaat", wie="planner", objecttype="Opleidingsprogramma aanbod", instantie="a",
             relaties=[{"soort": "Association", "van": "Opleidingsprogramma specificatie", "naar": "Opleidingsprogramma aanbod",
                        "label": "wordt aangeboden als", "instantie": "s"}]),
        dict(k, soort="ontstaat", wie="planner", objecttype="Onderwijseenheid aanbod", instantie="b",
             relatie={"soort": "Aggregation", "van": "Opleidingsprogramma aanbod", "naar": "Onderwijseenheid aanbod", "nesting": True}),
        dict(k, soort="ontstaat", wie="planner", objecttype="Plaatsingsgroep", instantie="g1", naast=True,
             relatie={"soort": "Association", "van": "Plaatsingsgroep", "naar": "Opleidingsprogramma aanbod", "label": "is gepland op", "instantie": "a"}),
        dict(k, soort="ontstaat", wie="planner", objecttype="Planningsgroep", instantie="g2", naast=True,
             relatie={"soort": "Composition", "van": "Plaatsingsgroep", "naar": "Planningsgroep"},
             relaties=[{"soort": "Association", "van": "Planningsgroep", "naar": "Onderwijseenheid aanbod", "label": "is gepland op"}]),
    ]
    return {"regels": r}


class NaastTests(unittest.TestCase):
    """Een groep staat in een kolom naast het aanbod waarop zij gepland is, op dezelfde hoogte (F2-08)."""

    def test_given_group_marked_naast_when_grouped_then_it_is_beside_and_not_in_the_column(self):
        blok = tv.groepeer(_naast_regels())[0]
        self.assertEqual([g["type"] for g in blok["naast"]], ["Plaatsingsgroep", "Planningsgroep"])
        self.assertNotIn("Plaatsingsgroep", tv._types_in_blok(blok["objecten"]))
        self.assertEqual(blok["naast"][0]["anker"], ("Opleidingsprogramma aanbod", "a"))
        self.assertEqual(blok["naast"][1]["anker"], ("Onderwijseenheid aanbod", "b"))
        self.assertEqual(blok["naast"][1]["groep_rel"]["soort"], "Composition")

    def test_given_groups_beside_when_drawn_then_each_at_the_height_of_its_offer(self):
        blok = tv.groepeer(_naast_regels())[0]
        svg = tv.regel_ontstaat(blok, set())
        P = tv.POSITIES
        self.assertEqual(P[("Plaatsingsgroep", "g1")][1], P[("Opleidingsprogramma aanbod", "a")][1])
        self.assertEqual(P[("Planningsgroep", "g2")][1], P[("Onderwijseenheid aanbod", "b")][1])
        self.assertGreater(P[("Plaatsingsgroep", "g1")][0], P[("Opleidingsprogramma aanbod", "a")][0] + P[("Opleidingsprogramma aanbod", "a")][2])
        self.assertIn("is gepland op", teksten(svg))

    def test_given_groups_beside_without_existing_objects_when_grouped_then_they_are_not_lost(self):
        blok = tv.groepeer(_naast_regels(met_bestaand=False))[0]
        self.assertIn("Plaatsingsgroep", tv._types_in_blok(blok["objecten"]))
        self.assertIn("Planningsgroep", tv._types_in_blok(blok["objecten"]))


def _naast_met_verbintenissen():
    """F6-06 in het klein: de groep naast het aanbod, en eronder de verbintenissen die erin geplaatst worden."""
    r = _naast_regels()
    k = {"beeld_id": "F2-08", "beeld": "Planner plant", "fase": 2, "stap": "Aanbod plannen", "bron": "b"}
    for n in ("v1", "v2", "v3"):
        r["regels"].append(dict(k, soort="bestaat", objecttype="Keuzedeel aanbod verbintenis", instantie=n, herkomst="F6-04",
                                naast=True, relatie={"soort": "Association", "van": "Keuzedeel aanbod verbintenis",
                                                     "naar": "Planningsgroep", "label": "wordt geplaatst in", "instantie": "g2"}))
    return r


class NaastVerbintenisTests(unittest.TestCase):
    """Een object dat al bestond kan in de kolom ernaast staan, met een lijn naar de groep erboven (F6-06)."""

    def test_given_existing_objects_beside_when_grouped_then_in_the_column_with_their_origin(self):
        blok = tv.groepeer(_naast_met_verbintenissen())[0]
        typen = [g["type"] for g in blok["naast"]]
        self.assertEqual(typen.count("Keuzedeel aanbod verbintenis"), 3)
        v = blok["naast"][2]
        self.assertIn("uit F6-04", v["verwijzingen"])
        self.assertEqual(v["groep_rel"]["relatie"], "wordt geplaatst in")
        self.assertEqual(blok["naast"][3]["groep_doel"], ("Planningsgroep", "g2"))

    def test_given_several_objects_to_one_group_when_drawn_then_a_line_each_and_the_label_once(self):
        blok = tv.groepeer(_naast_met_verbintenissen())[0]
        svg = tv.regel_ontstaat(blok, set())
        self.assertEqual(svg.count('class="naastlijn-groep"'), 2)
        self.assertEqual(teksten(svg).count("wordt geplaatst in"), 1)


    def test_given_a_composition_to_a_group_further_up_when_drawn_then_the_diamond_is_at_the_whole(self):
        r = _naast_regels()
        k = {"beeld_id": "F2-08", "beeld": "Planner plant", "fase": 2, "stap": "Aanbod plannen", "bron": "b"}
        r["regels"].append(dict(k, soort="ontstaat", wie="planner", objecttype="Planningsgroep", instantie="g3", naast=True,
                                relatie={"soort": "Association", "van": "Planningsgroep", "naar": "Onderwijseenheid aanbod", "label": "is gepland op"}))
        r["regels"].append(dict(k, soort="ontstaat", wie="planner", objecttype="Planningsgroep", instantie="g4", naast=True,
                                relaties=[{"soort": "Composition", "van": "Plaatsingsgroep", "naar": "Planningsgroep"}]))
        blok = tv.groepeer(r)[0]
        self.assertEqual(blok["naast"][3]["groep_doel"], ("Plaatsingsgroep", "g1"))
        svg = tv.regel_ontstaat(blok, set())
        self.assertIn('class="naastlijn-groep"', svg)
        self.assertRegex(svg, r'<path d="M[0-9]+ [0-9]+l-7 -5l-7 5l7 5z" fill="#444"')


class NaastBreedteTests(unittest.TestCase):
    def test_given_groups_with_different_text_when_drawn_then_all_boxes_in_the_column_equally_wide(self):
        # Niels van Duin, 25 november 2026: "maak die balkjes aan de rechterkant even groot"
        r = _naast_regels()
        r["regels"][-1]["instantie"] = "een veel langere instantie van de planningsgroep"
        blok = tv.groepeer(r)[0]
        tv.regel_ontstaat(blok, set())
        breedtes = {tv.POSITIES[(g["type"], g["instantie"])][2] for g in blok["naast"]}
        self.assertEqual(len(breedtes), 1)


class HerkomstValTerugTests(unittest.TestCase):
    """Twee eerdere objecten wijzen naar dezelfde verbintenis (zoals in fase 4), dus uitlijnen lukt niet. Dan staat de
    kolom rechts onder elkaar, zodat geen herkomstlijn door een ander vak loopt."""

    def test_given_alignment_fails_when_drawn_then_the_new_objects_stand_below_each_other(self):
        k = {"beeld_id": "F4-09", "beeld": "Verbinden", "fase": 4, "stap": "Verbinden", "bron": "b"}
        r = {"regels": [
            dict(k, soort="bestaat", objecttype="A", instantie="a", herkomst="F2-01"),
            dict(k, soort="bestaat", objecttype="B", instantie="b", herkomst="F2-01"),
            dict(k, soort="ontstaat", wie="planner", objecttype="X", instantie="x",
                 relatie={"soort": "Association", "van": "B", "naar": "X", "instantie": "b"}),
            dict(k, soort="ontstaat", wie="planner", objecttype="Y", instantie="y",
                 relatie={"soort": "Association", "van": "A", "naar": "Y", "instantie": "a"})]}
        blok = tv.groepeer(r)[0]
        tv.regel_ontstaat(blok, set())
        px, py = tv.POSITIES[("X", "x")][:2], tv.POSITIES[("Y", "y")][:2]
        self.assertEqual(px[0], py[0], "X en Y horen in dezelfde kolom te staan")
        self.assertNotEqual(px[1], py[1])



class UitlijnenTweeBronnenTests(unittest.TestCase):
    """F4-07: twee eerdere objecten wijzen naar dezelfde verbintenis. Het uitlijnen lukt dan nog steeds, zodat
    de groepen ernaast hun lijn houden."""

    def test_given_two_existing_objects_to_one_new_object_when_drawn_then_aligned_and_groups_keep_their_line(self):
        k = {"beeld_id": "F4-07", "beeld": "Plannen", "fase": 4, "stap": "Plannen", "bron": "b"}
        r = {"regels": [
            dict(k, soort="bestaat", objecttype="A", instantie="a", herkomst="F2-01"),
            dict(k, soort="bestaat", objecttype="B", instantie="b", herkomst="F2-01"),
            dict(k, soort="ontstaat", wie="planner", objecttype="X", instantie="x",
                 relatie={"soort": "Association", "van": "A", "naar": "X", "instantie": "a"},
                 relaties=[{"soort": "Association", "van": "B", "naar": "X", "instantie": "b"}]),
            dict(k, soort="ontstaat", wie="planner", objecttype="G", instantie="g", naast=True,
                 relatie={"soort": "Association", "van": "G", "naar": "X", "label": "is gepland op"})]}
        blok = tv.groepeer(r)[0]
        svg = tv.regel_ontstaat(blok, set())
        self.assertIn('class="naastlijn"', svg)



if __name__ == "__main__":
    unittest.main()
