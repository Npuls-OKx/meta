"""Testgevallen voor scripts/controleer-voorbeeldregels.py.

Elk geval werkt op een klein fixture-model en een fixture-regeltabel die in de
test zelf worden opgebouwd; de verwachtingen volgen uit die fixtures, niet uit de
inhoud van de repository. Elk negatief geval breekt precies een ding.
"""

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
SCHEMA = WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.schema.json"
spec = importlib.util.spec_from_file_location("controleer_voorbeeldregels", WORTEL / "scripts/controleer-voorbeeldregels.py")
cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv)


def model():
    return {"objecttypen": [
                {"naam": "Opleidingaanbod", "scope": "binnen"},
                {"naam": "Opleidingsprogramma aanbod", "scope": "binnen"},
                {"naam": "Aanmelding", "scope": "binnen"},
                {"naam": "Opleiding aanbod  verbintenis", "scope": "binnen"},
                {"naam": "Lesgelegenheid", "scope": "buiten"},
                {"naam": "OER", "scope": "buiten"}],
            "relaties": [
                {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Opleidingsprogramma aanbod", "label": None},
                {"soort": "Association", "van": "Opleidingaanbod", "naar": "Aanmelding", "label": "Op basis van"},
                {"soort": "Association", "van": "Aanmelding", "naar": "Opleiding aanbod  verbintenis", "label": "middels"}]}


def stromen():
    return {"stromen": [{"id": "rel-1", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "label": "", "koppeling": "OC-P&R"}]}


def nummer(r):
    """Elke regel het ID van haar beeld geven (F<fase>-<volgnummer>), zoals de regeltabel dat doet."""
    ids, teller = {}, {}
    for x in r["regels"]:
        b = x.get("beeld")
        if not b:
            continue
        if b not in ids:
            teller[x["fase"]] = teller.get(x["fase"], 0) + 1
            ids[b] = f"F{x['fase']}-{teller[x['fase']]:02d}"
        x.setdefault("beeld_id", ids[b])
    return r


def regels():
    return nummer({"model": {"informatiemodel_commit": "abc123", "begrippen_commit": "def456"},
            "fasen": [
                {"nummer": 2, "naam": "Publiceren", "bron": "ks", "stappen": ["Aanbod maken", "Aanbod publiceren"], "verwacht": ["Opleidingaanbod", "Opleidingsprogramma aanbod"]},
                {"nummer": 3, "naam": "Instroom", "bron": "ks", "stappen": ["Aanmelden"], "verwacht": ["Aanmelding", "Opleiding aanbod verbintenis"]},
                {"nummer": 4, "naam": "Roosteren", "bron": "ks", "stappen": ["Roosteren"], "verwacht": ["Lesgelegenheid"]}],
            "rollen": ["planner", "student"],
            "toestanden": [{"naam": "geroosterd", "bron": "ks"}],
            "scope_uitzonderingen": [{"objecttype": "Lesgelegenheid", "motivering": "besluit"}],
            "koppelingen": {"Planningssysteem > Onderwijscatalogus": "OC-P&R"},
            "regels": [
                {"beeld": "Aanbod gemaakt", "fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "ks r1"},
                {"beeld": "Aanbod gemaakt", "fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingsprogramma aanbod", "instantie": "Regulier BOL 2026", "bron": "ks r2",
                 "relatie": {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Opleidingsprogramma aanbod", "nesting": True}},
                {"beeld": "Aanbod naar de catalogus", "fase": 2, "stap": "Aanbod publiceren", "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1", "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "v1.7"},
                {"beeld": "Aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Aanmelding", "instantie": "April 2026", "bron": "ks r3",
                 "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Aanmelding", "label": "Op basis van"}},
                {"beeld": "Aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Opleiding aanbod verbintenis", "instantie": "Jochem 2026", "bron": "ks r4"},
                {"beeld": "Geroosterd", "fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "planner", "objecttype": "Lesgelegenheid", "instantie": "ma 09:00", "bron": "ks r5"},
                {"beeld": "Geroosterd", "fase": 4, "stap": "Roosteren", "soort": "verandert", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "toestand": "geroosterd", "bron": "ks r6"}]})


def bevindingen(r=None, m=None, s="standaard", **kw):
    kw.setdefault("schema_pad", SCHEMA)
    b, w, o = cv.controleer(r or regels(), m or model(), stromen() if s == "standaard" else s, **kw)
    return b, w, o


def register_regels(**velden):
    """De fixture met een register van een bevinding erin, zodat de controles op het register iets hebben."""
    r = regels()
    r["thema_toelichting"] = {"clustering": "leeronderdelen clusteren tot leergelegenheden"}
    bevinding = {"nummer": "B01", "beeld_id": r["regels"][0]["beeld_id"], "lezer": "NvDuin",
                 "datum": "2026-09-28", "bron": "https://github.com/x/y/pull/252#discussion_r1",
                 "tekst": "deze stap lijkt te rechtlijnig", "themas": ["clustering"],
                 "issue": 283, "status": "open"}
    bevinding.update(velden)
    r["bevindingen"] = [bevinding]
    return r


class ControleTests(unittest.TestCase):
    def test_given_valid_table_when_checked_then_no_findings(self):
        b, w, o = bevindingen()
        self.assertEqual(b, [])
        self.assertEqual(o, {})

    def test_given_rule_without_required_field_when_checked_then_finding_names_rule_and_field(self):
        r = regels(); del r["regels"][0]["instantie"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("regel 1 (F2-01 - Aanbod gemaakt: Opleidingaanbod)" in x and "instantie" in x for x in b))

    def test_given_beeld_id_when_checked_then_one_id_per_beeld_in_the_right_form_and_rising(self):
        r = regels(); r["regels"][0]["beeld_id"] = "R2-1"
        self.assertTrue(any("heeft niet de vorm" in x for x in bevindingen(r)[0]))
        r = regels(); r["regels"][0]["beeld_id"] = "F3-01"
        b = bevindingen(r)[0]
        self.assertTrue(any("noemt een andere fase" in x for x in b))
        self.assertTrue(any("draagt twee ID's" in x for x in b))
        r = regels(); r["regels"][3]["beeld_id"] = r["regels"][4]["beeld_id"] = "F2-01"
        self.assertTrue(any("hoort al bij beeld" in x for x in bevindingen(r)[0]))
        r = regels(); r["regels"][5]["beeld_id"] = r["regels"][6]["beeld_id"] = "F4-01"
        r["regels"][0]["beeld_id"] = r["regels"][1]["beeld_id"] = "F2-02"
        r["regels"][2]["beeld_id"] = "F2-01"
        self.assertTrue(any("loopt niet op" in x for x in bevindingen(r)[0]))
        self.assertEqual(bevindingen()[0], [])

    def test_given_direct_link_to_kwalificatiekader_when_checked_then_warning_about_the_route(self):
        r = regels()
        r["regels"][0]["relaties"] = [{"soort": "Association", "van": "Kerntaak", "naar": "Opleidingaanbod"}]
        m = model()
        m["objecttypen"].append({"naam": "Kerntaak", "kolom": "Kwalificatiekader MBO", "scope": "buiten"})
        m["relaties"].append({"soort": "Association", "van": "Kerntaak", "naar": "Opleidingaanbod"})
        b, w, _ = cv.controleer(r, m, stromen())
        self.assertEqual(b, [])
        self.assertTrue(any("loopt via de leeruitkomst" in x for x in w))

    def test_given_leeruitkomst_linked_to_kerntaak_when_checked_then_no_warning(self):
        r = regels()
        r["regels"][0]["objecttype"] = "Leeruitkomst"
        r["regels"][0]["relaties"] = [{"soort": "Association", "van": "Kerntaak", "naar": "Leeruitkomst"}]
        m = model()
        m["objecttypen"] += [{"naam": "Kerntaak", "kolom": "Kwalificatiekader MBO", "scope": "buiten"},
                             {"naam": "Leeruitkomst", "kolom": "Onderwijskundigkader instelling", "scope": "buiten"}]
        m["relaties"].append({"soort": "Association", "van": "Kerntaak", "naar": "Leeruitkomst"})
        _, w, _ = cv.controleer(r, m, stromen())
        self.assertFalse(any("loopt via de leeruitkomst" in x for x in w))

    def test_given_unknown_objecttype_when_checked_then_signal_with_the_place_in_the_line(self):
        """Een objecttype dat de plaat nog niet draagt hoort een fase niet te blokkeren, dus het is een
        signalering met de fase en de stap erbij en de exitcode gaat eraan voorbij."""
        r = regels(); r["regels"][0]["objecttype"] = "Bestaat niet"
        b, w, _ = bevindingen(r)
        self.assertEqual([x for x in b if "Bestaat niet" in x], [])
        self.assertTrue(any("Bestaat niet" in x and "fase 2" in x and "Aanbod maken" in x for x in w), w)

    def test_given_name_differing_only_in_whitespace_when_checked_then_accepted(self):
        # de fixture kent "Opleiding aanbod  verbintenis" met dubbele spatie; de regel gebruikt een spatie
        b, _, _ = bevindingen()
        self.assertFalse(any("Opleiding aanbod verbintenis" in x for x in b))

    def test_given_assumed_instance_on_known_type_when_checked_then_accepted(self):
        r = regels(); r["regels"][0]["aanname"] = True
        b, _, _ = bevindingen(r)
        self.assertEqual(b, [])

    def test_given_assumed_objecttype_not_on_plate_when_checked_then_signal(self):
        r = regels(); r["regels"][0]["objecttype"] = "Verzonnen"; r["regels"][0]["aanname"] = True
        b, w, _ = bevindingen(r)
        self.assertEqual([x for x in b if "Verzonnen" in x], [])
        self.assertTrue(any("Verzonnen" in x for x in w))

    def test_given_relation_triple_on_plate_when_checked_then_accepted(self):
        b, _, _ = bevindingen()
        self.assertFalse(any("relatie" in x for x in b))

    def test_given_label_existing_elsewhere_but_triple_missing_when_checked_then_finding(self):
        r = regels(); r["regels"][3]["relatie"] = {"soort": "Association", "van": "Aanmelding", "naar": "Opleidingaanbod", "label": "Op basis van"}
        b, _, _ = bevindingen(r)
        self.assertTrue(any("staat niet op de plaat" in x for x in b))

    def test_given_label_differing_from_plate_when_checked_then_finding(self):
        r = regels(); r["regels"][3]["relatie"]["label"] = "Verkeerd"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("wijkt af van de plaat" in x for x in b))

    def test_given_unlabeled_aggregation_when_nested_then_accepted(self):
        b, _, _ = bevindingen()
        self.assertFalse(any("nesting" in x for x in b))

    def test_given_nesting_on_association_when_checked_then_finding(self):
        r = regels(); r["regels"][3]["relatie"]["nesting"] = True
        b, _, _ = bevindingen(r)
        self.assertTrue(any("nesting alleen op een aggregatie" in x for x in b))

    def test_given_role_not_in_list_when_checked_then_finding(self):
        r = regels(); r["regels"][0]["wie"] = "conciërge"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("rol 'conciërge'" in x for x in b))

    def test_given_toestand_not_in_list_when_checked_then_finding(self):
        r = regels(); r["regels"][6]["toestand"] = "verzonnen"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("toestand 'verzonnen'" in x for x in b))

    def test_given_stroomt_rule_on_unknown_relation_id_when_checked_then_finding_names_id(self):
        r = regels(); r["regels"][2]["pijl"] = "rel-99"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("rel-99" in x and "stromen.json" in x for x in b))

    def test_given_stroomt_rule_marked_no_arrow_when_checked_then_accepted_and_warned(self):
        r = regels(); r["regels"][2]["pijl"] = cv.GEEN_PIJL
        b, w, _ = bevindingen(r)
        self.assertEqual(b, [])
        self.assertTrue(any("geen pijl op de hoofdplaat" in x for x in w))

    def test_given_stroomt_rule_without_van_when_checked_then_finding(self):
        r = regels(); del r["regels"][2]["van"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("veld van ontbreekt bij stroomt" in x for x in b))

    def test_given_in_scope_type_without_rule_when_checked_then_listed_per_fase(self):
        r = regels(); r["regels"] = [x for x in r["regels"] if x["objecttype"] != "Aanmelding"]
        b, _, o = bevindingen(r)
        self.assertEqual(o, {3: ["Aanmelding"]})
        self.assertTrue(any("fase 3: geen ontstaat-regel voor Aanmelding" in x for x in b))

    def test_given_fase_filter_when_checked_then_only_those_fases_listed(self):
        r = regels(); r["regels"] = [x for x in r["regels"] if x["objecttype"] not in ("Aanmelding", "Lesgelegenheid")]
        _, _, o = bevindingen(r, fasen_filter={2, 3})
        self.assertEqual(o, {3: ["Aanmelding"]})

    def test_given_type_with_two_ontstaat_rules_when_checked_then_finding(self):
        r = regels(); r["regels"].append(dict(r["regels"][0], stap="Aanbod publiceren"))
        b, _, _ = bevindingen(r)
        self.assertTrue(any("2 ontstaat-regels" in x for x in b))

    def test_given_self_nested_child_of_same_type_when_checked_then_not_a_second_ontstaat(self):
        m = model(); m["relaties"].append({"soort": "Aggregation", "van": "Aanmelding", "naar": "Aanmelding", "label": None})
        r = regels(); r["regels"].append({"fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Aanmelding", "instantie": "genest", "bron": "b",
                                          "relatie": {"soort": "Aggregation", "van": "Aanmelding", "naar": "Aanmelding", "nesting": True}})
        b, _, _ = bevindingen(r, m)
        self.assertFalse(any("ontstaat-regels" in x for x in b))

    def test_given_type_with_ontstaat_and_verandert_when_checked_then_accepted(self):
        b, _, _ = bevindingen()
        self.assertFalse(any("Opleidingaanbod" in x and "ontstaat-regels" in x for x in b))

    def test_given_ontstaat_in_wrong_fase_when_checked_then_finding(self):
        r = regels(); r["regels"][3]["fase"] = 2; r["regels"][3]["stap"] = "Aanbod maken"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("ontstaat in fase 2, verwacht in fase 3" in x for x in b))

    def test_given_out_of_scope_type_with_rule_when_checked_then_finding(self):
        r = regels(); r["regels"].append({"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "OER", "instantie": "x", "bron": "y"})
        b, _, _ = bevindingen(r)
        self.assertTrue(any("'OER' staat buiten scope" in x for x in b))

    def test_given_scope_exception_type_when_checked_then_treated_as_in_scope(self):
        b, _, _ = bevindingen()
        self.assertFalse(any("Lesgelegenheid" in x for x in b))

    def test_given_unknown_step_when_checked_then_finding(self):
        r = regels(); r["regels"][0]["stap"] = "Bestaat niet"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("stap 'Bestaat niet' staat niet in fase 2" in x for x in b))

    def test_given_model_commit_mismatch_when_checked_then_warning_not_finding(self):
        b, w, _ = bevindingen(model_commit="zzz999")
        self.assertEqual(b, [])
        self.assertTrue(any("zzz999" in x for x in w))

    def test_given_empty_table_when_checked_then_missing_equals_expectation(self):
        r = regels(); r["regels"] = []
        _, _, o = bevindingen(r)
        verwacht = {f["nummer"]: sorted(cv.norm(v) for v in f["verwacht"]) for f in r["fasen"]}
        self.assertEqual({k: sorted(v) for k, v in o.items()}, verwacht)

    def test_given_missing_stromen_when_checked_then_arrows_not_checked(self):
        r = regels(); r["regels"][2]["pijl"] = "rel-99"
        b, _, _ = bevindingen(r, s=None)
        self.assertFalse(any("rel-99" in x for x in b))


def conceptplaat():
    return {"bron": {"view": "Conceptview"},
            "objecttypen": [{"naam": "Leerdoel", "groep": "Onderwijsplan"}, {"naam": "Leervormstrategie", "groep": "Strategisch kader"}],
            "relaties": [{"soort": "Association", "van": "Leervormstrategie", "naar": "Leerdoel", "label": None}]}


def conceptregel(**extra):
    """Een regel tegen de conceptplaat. Een veld op None laten betekent het veld weglaten: null is in de
    regeltabel geen waarde, behalve bij koppeling, waar het voor een stroom zonder specificatie staat."""
    r = {"beeld_id": "F2-09", "beeld": "Kader (concept)", "fase": 2, "stap": "Aanbod maken", "verdieping": "kader", "plaat": "onderwijsontwerp", "soort": "ontstaat", "wie": "planner",
         "objecttype": "Leerdoel", "instantie": "Leren door te doen", "bron": "conceptplaat",
         "relatie": {"soort": "Association", "van": "Leervormstrategie", "naar": "Leerdoel"}}
    r.update(extra)
    return {k: v for k, v in r.items() if v is not None or k == "koppeling"}


class ConceptplaatTests(unittest.TestCase):
    def test_given_concept_rule_in_verdieping_when_checked_against_conceptplaat_then_no_findings(self):
        r = regels(); r["regels"].append(conceptregel())
        b, _, o = bevindingen(r, conceptplaat=conceptplaat())
        self.assertEqual(b, [])
        self.assertEqual(o, {})

    def test_given_concept_rule_without_verdieping_when_checked_then_finding_unless_stroomt(self):
        r = regels(); r["regels"].append(conceptregel(verdieping=None))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("alleen in een verdieping" in x for x in b))
        r = regels(); r["regels"].append(conceptregel(verdieping=None, beeld="Leerdoel naar de catalogus", soort="stroomt", van="Planningssysteem", naar="Onderwijscatalogus", pijl="rel-1", koppeling="OC-P&R", stap="Aanbod publiceren", relatie=None))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertEqual(b, [])

    def test_given_concept_rule_when_conceptplaat_not_loaded_then_finding(self):
        r = regels(); r["regels"].append(conceptregel())
        b, _, _ = bevindingen(r)
        self.assertTrue(any("conceptplaat is niet geladen" in x for x in b))

    def test_given_concept_rule_with_unknown_type_or_relation_when_checked_then_named_against_the_conceptplaat(self):
        r = regels(); r["regels"].append(conceptregel(objecttype="Onderwijsvorm specificatie"))
        b, w, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("bestaat niet op de conceptplaat" in x for x in w), w)
        r = regels(); r["regels"].append(conceptregel(relatie={"soort": "Aggregation", "van": "Leervormstrategie", "naar": "Leerdoel"}))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("staat niet op de conceptplaat" in x for x in b))

    def test_given_concept_rule_when_checked_then_not_counted_in_coverage_nor_scope(self):
        r = regels(); r["regels"].append(conceptregel(objecttype="Leerdoel", instantie="x", relatie=None))
        r["regels"].append(conceptregel(instantie="y", relatie=None))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertFalse(any("ontstaat-regels" in x or "buiten scope" in x for x in b))

    def test_given_unknown_plaat_when_checked_then_finding(self):
        r = regels(); r["regels"].append(conceptregel(plaat="hoofdplaat"))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("plaat 'hoofdplaat'" in x for x in b))


class BeeldEnRelatiesTests(unittest.TestCase):
    def test_given_beeld_missing_or_inconsistent_when_checked_then_finding(self):
        r = regels(); del r["regels"][0]["beeld"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("veld beeld ontbreekt" in x for x in b))
        r = regels(); r["regels"][3]["beeld"] = "Aanbod gemaakt"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("ligt ook in een andere fase, stap, soort of verdieping" in x for x in b))
        r = regels(); r["regels"][4]["beeld"] = "Aanmelding"; r["regels"][4]["fase"] = 3; r["regels"][4]["stap"] = "Aanmelden"
        r["regels"].insert(4, {"beeld": "Tussen", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Opleidingsprogramma aanbod", "instantie": "x", "bron": "b"})
        b, _, _ = bevindingen(r)
        self.assertTrue(any("niet aaneengesloten" in x for x in b))

    def test_given_extra_relations_when_checked_then_each_must_exist_on_plaat_touch_object_and_not_nest(self):
        r = regels()
        r["regels"][0]["relaties"] = [{"soort": "Association", "van": "Opleidingaanbod", "naar": "Aanmelding", "label": "Op basis van"}]
        b, _, _ = bevindingen(r)
        self.assertEqual(b, [])
        r["regels"][0]["relaties"] = [{"soort": "Association", "van": "Opleidingaanbod", "naar": "Aanmelding", "label": "fout"},
                                      {"soort": "Aggregation", "van": "Aanmelding", "naar": "Lesgelegenheid"},
                                      {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Opleidingsprogramma aanbod", "nesting": True}]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("(relaties) wijkt af" in x for x in b))
        self.assertTrue(any("raakt het objecttype" in x for x in b))
        self.assertTrue(any("nesting hoort in relatie" in x for x in b))


class SchemaContractTests(unittest.TestCase):
    """Het schema naast de tabel is de woordenlijst van de velden; wat het niet kent hoort op te vallen."""

    def test_given_the_real_table_when_validated_then_it_passes_and_the_schema_knows_every_field(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        fouten, waarschuwingen = cv.schemavalidatie(tabel, SCHEMA)
        self.assertEqual(fouten, [])
        self.assertEqual(waarschuwingen, [])
        velden = {k for r in tabel["regels"] for k in r}
        beschreven = set(json.loads(SCHEMA.read_text(encoding="utf-8"))["properties"]["regels"]["items"]["properties"])
        self.assertEqual(velden - beschreven, set())

    def test_given_rule_with_unknown_field_when_checked_then_finding_names_that_field(self):
        r = regels(); r["regels"][0]["objecttyp"] = "Opleidingaanbod"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("'objecttyp' kent het schema niet" in x for x in b), b)

    def test_given_unknown_field_inside_a_relation_when_checked_then_finding_names_that_field(self):
        r = regels(); r["regels"][1]["relatie"]["nestng"] = True
        b, _, _ = bevindingen(r)
        self.assertTrue(any("'nestng' kent het schema niet" in x for x in b), b)

    def test_given_missing_required_field_when_checked_then_finding_names_beeld_id_and_field(self):
        r = regels(); del r["regels"][0]["objecttype"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("F2-01" in x and "objecttype" in x for x in b), b)

    def test_given_unknown_top_level_field_when_checked_then_finding_on_the_head(self):
        r = regels(); r["regles"] = []
        b, _, _ = bevindingen(r)
        self.assertTrue(any(x.startswith("kop:") and "'regles'" in x for x in b), b)

    def test_given_koppeling_outside_the_list_when_checked_then_finding(self):
        r = regels(); r["regels"][2]["koppeling"] = "OC-XYZ"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("koppeling 'OC-XYZ' staat niet in de koppelingenlijst" in x for x in b), b)

    def test_given_koppeling_null_on_a_stroomt_rule_when_checked_then_accepted(self):
        r = regels(); r["regels"][2]["koppeling"] = None
        b, _, _ = bevindingen(r)
        self.assertEqual(b, [])

    def test_given_stroomt_rule_without_koppeling_when_checked_then_finding(self):
        r = regels(); del r["regels"][2]["koppeling"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("veld koppeling ontbreekt bij stroomt" in x for x in b), b)

    def test_given_koppeling_on_an_ontstaat_rule_when_checked_then_finding(self):
        r = regels(); r["regels"][0]["koppeling"] = "OC-P&R"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("hoort bij een stroomt-regel" in x for x in b), b)

    def test_given_missing_schema_file_when_checked_then_warning_and_no_finding(self):
        r = regels()
        fouten, waarschuwingen = cv.schemavalidatie(r, Path("geen-schema.json"))
        self.assertEqual(fouten, [])
        self.assertTrue(any("schema ontbreekt" in w for w in waarschuwingen))


class RegisterTests(unittest.TestCase):
    """Het register houdt bij wat er met een reviewbevinding is gedaan, dus het moet naar iets bestaands wijzen."""

    def test_given_a_sound_register_when_checked_then_no_findings(self):
        b, _, _ = bevindingen(register_regels())
        self.assertEqual(b, [])

    def test_given_finding_on_unknown_beeld_when_checked_then_finding(self):
        b, _, _ = bevindingen(register_regels(beeld_id="F9-99"))
        self.assertTrue(any("bestaat niet in de regeltabel" in x or "niet de vorm" in x for x in b), b)

    def test_given_finding_with_unknown_thema_when_checked_then_finding(self):
        b, _, _ = bevindingen(register_regels(themas=["verzonnen"]))
        self.assertTrue(any("staat niet in thema_toelichting" in x for x in b), b)

    def test_given_parked_finding_without_reason_when_checked_then_finding(self):
        b, _, _ = bevindingen(register_regels(status="geparkeerd"))
        self.assertTrue(any("geparkeerd zonder reden" in x for x in b), b)

    def test_given_parked_finding_with_reason_when_checked_then_accepted(self):
        b, _, _ = bevindingen(register_regels(status="geparkeerd", reden="wacht op de modelronde"))
        self.assertEqual(b, [])

    def test_given_a_processed_finding_without_an_account_when_checked_then_finding(self):
        """Criterium 5 van een fase vraagt per bevinding wat er is gewijzigd; doorgevoerd zonder dat
        verhaal laat de lezer met een vinkje achter."""
        b, _, _ = bevindingen(register_regels(status="doorgevoerd"))
        self.assertTrue(any("doorgevoerd zonder te zeggen wat er is gewijzigd" in x for x in b), b)

    def test_given_a_processed_finding_with_an_account_when_checked_then_accepted(self):
        b, _, _ = bevindingen(register_regels(status="doorgevoerd", verwerking="F2-01: de zin herschreven"))
        self.assertEqual(b, [])

    def test_given_the_register_when_read_then_phase_one_is_fully_processed(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        fase1 = [b for b in tabel["bevindingen"] if b["issue"] == 283]
        self.assertEqual(len(fase1), 5)
        for b in fase1:
            self.assertEqual(b["status"], "doorgevoerd", b["nummer"])
            self.assertTrue(b["verwerking"].startswith(b["beeld_id"]), b["nummer"])

    def test_given_status_outside_the_list_when_checked_then_finding(self):
        b, _, _ = bevindingen(register_regels(status="afgehandeld"))
        self.assertTrue(any("staat niet in de lijst" in x for x in b), b)

    def test_given_reference_to_unknown_beeld_when_checked_then_finding(self):
        b, _, _ = bevindingen(register_regels(verwijst_naar="F8-07"))
        self.assertTrue(any("verwijst naar beeld" in x for x in b), b)

    def test_given_the_register_when_read_then_six_findings_have_no_decision_in_the_feature_plan(self):
        """Het featureplan is van 29 september 17:23; zes bevindingen kwamen daarna binnen en wachten
        dus nog op een besluit. Dit geval houdt dat getal zichtbaar in plaats van in een commitbericht."""
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        zonder = [b["nummer"] for b in tabel["bevindingen"] if not b.get("werkpakketten")]
        self.assertEqual(zonder, ["B33", "B34", "B35", "B36", "B37", "B38"])

    def test_given_every_finding_of_the_round_when_counted_then_the_register_holds_all_of_them(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        self.assertEqual(len(tabel["bevindingen"]), 38)
        beelden = {r["beeld_id"] for r in tabel["regels"]}
        for b in tabel["bevindingen"]:
            self.assertIn(b["beeld_id"], beelden)
            self.assertTrue(b["bron"].startswith("https://github.com/Npuls-OKx/meta/pull/252#discussion_r"))
            self.assertTrue(set(b["themas"]) <= set(tabel["thema_toelichting"]))


class DekkingTests(unittest.TestCase):
    """De uitwisselingen die het kaderscenario per fase noemt, afgezet tegen de beelden die er zijn.
    Zo is criterium 1 van een fase-issue een machinale controle in plaats van een oordeel."""

    def fase(self, nummer, **velden):
        r = regels()
        for f in r["fasen"]:
            if f["nummer"] == nummer:
                f.update(velden)
        return r

    def uitwisseling(self, **extra):
        u = {"van": "Planningssysteem", "naar": "Onderwijscatalogus", "objecten": ["opleidingsaanbod"],
             "bron": "leerroute-1-regulier.md, Fase 2"}
        u.update(extra)
        return u

    def test_given_phase_with_exchange_without_image_when_checked_then_that_phase_and_exchange_are_named(self):
        r = self.fase(2, uitwisselingen=[self.uitwisseling(van="Onderwijscatalogus", naar="Leer management systeem (LMS)")])
        _, w, _ = bevindingen(r)
        self.assertTrue(any("fase 2" in x and "Onderwijscatalogus naar Leer management systeem (LMS)" in x
                            and "draagt geen beeld" in x for x in w), w)

    def test_given_exchange_with_an_image_when_checked_then_nothing_is_reported(self):
        r = self.fase(2, uitwisselingen=[self.uitwisseling()])
        b, w, _ = bevindingen(r)
        self.assertEqual(b, [])
        self.assertEqual([x for x in w if "draagt geen beeld" in x], [])

    def test_given_full_coverage_when_an_exchange_lacks_an_image_then_finding_not_signal(self):
        r = self.fase(2, dekking="volledig",
                      uitwisselingen=[self.uitwisseling(van="Onderwijscatalogus", naar="Leer management systeem (LMS)")])
        b, w, _ = bevindingen(r)
        self.assertTrue(any("draagt geen beeld" in x for x in b), b)
        self.assertEqual([x for x in w if "draagt geen beeld" in x], [])

    def test_given_exchange_shown_in_another_phase_when_that_phase_carries_it_then_accepted(self):
        r = self.fase(3, uitwisselingen=[self.uitwisseling(beeld_in_fase=2)])
        b, w, _ = bevindingen(r)
        self.assertEqual(b, [])
        self.assertEqual([x for x in w if "draagt geen beeld" in x], [])

    def test_given_exchange_pointing_at_a_phase_without_that_flow_when_checked_then_finding(self):
        r = self.fase(3, uitwisselingen=[self.uitwisseling(beeld_in_fase=4)])
        b, _, _ = bevindingen(r)
        self.assertTrue(any("verwijst naar fase 4" in x for x in b), b)

    def test_given_exchange_outside_okx_when_checked_then_signal_with_the_reason(self):
        r = self.fase(2, uitwisselingen=[self.uitwisseling(naar="Aanwezigheidsregistratie",
                                                          buiten_scope="aanwezigheidsregistratie valt buiten OKx")])
        b, w, _ = bevindingen(r)
        self.assertEqual(b, [])
        self.assertTrue(any("valt buiten OKx" in x for x in w), w)

    def test_given_exchange_the_example_routes_differently_when_checked_then_signal_with_the_reason(self):
        r = self.fase(2, uitwisselingen=[self.uitwisseling(van="Onderwijscatalogus", naar="Intake systeem",
                                                          afwijking="het voorbeeld loopt via de kernregistratie")])
        b, w, _ = bevindingen(r)
        self.assertEqual(b, [])
        self.assertTrue(any("loopt in het voorbeeld anders" in x for x in w), w)

    def test_given_a_phase_filter_when_checked_then_only_those_phases_are_measured(self):
        r = self.fase(2, uitwisselingen=[self.uitwisseling(van="Onderwijscatalogus", naar="Leer management systeem (LMS)")])
        _, w, _ = bevindingen(r, fasen_filter={3})
        self.assertEqual([x for x in w if "draagt geen beeld" in x], [])

    def test_given_an_exchange_naming_an_unknown_component_when_checked_then_signal(self):
        r = self.fase(2, uitwisselingen=[self.uitwisseling(naar="Verzonnen systeem")])
        _, w, _ = bevindingen(r, componenten={"componenten": [{"naam": "Planningssysteem"}, {"naam": "Onderwijscatalogus"}]})
        self.assertTrue(any("componenten.json niet kent" in x for x in w), w)

    def test_given_the_real_table_when_measured_then_twelve_exchanges_wait_for_an_answer(self):
        """De werklijst van de acht fase-issues: elk gat krijgt daar beeld_in_fase, afwijking of
        buiten_scope, en de fase gaat op dekking volledig."""
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        b, w = cv.dekking_uitwisselingen(tabel)
        self.assertEqual(b, [])
        self.assertEqual(len([x for x in w if "draagt geen beeld" in x]), 12)


class AanvullendeStroomTests(unittest.TestCase):
    """Een stroom die hoofdplaat 1.7a kent en 1.7 nog niet, komt via stromen-aanvullingen.json in
    stromen.json terecht. Een regel moet daarnaar kunnen wijzen, anders kan fase 6 de conditionele
    keuze niet tonen."""

    def echte_stromen(self):
        """De echte export naast de fixture-stroom, zodat de bestaande regels van de fixture blijven kloppen."""
        echt = json.loads((WORTEL / "architecture/model/informatiemodel/stromen.json").read_text(encoding="utf-8"))
        return {"stromen": stromen()["stromen"] + echt["stromen"]}

    def test_given_a_rule_pointing_at_an_addition_when_checked_then_the_arrow_is_accepted(self):
        r = regels()
        r["regels"].append({"beeld_id": "F3-02", "beeld": "Voltooide verbintenissen naar het keuzesysteem",
                            "fase": 3, "stap": "Aanmelden", "soort": "stroomt",
                            "van": "Student volg systeem (SVS)", "naar": "Student Keuze Systeem (SKS)",
                            "pijl": "aanvulling-svs-naar-sks-voltooide-verbintenissen", "koppeling": None,
                            "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026",
                            "bron": "stromen-aanvullingen.json"})
        b, w, _ = bevindingen(r, s=self.echte_stromen())
        self.assertEqual([x for x in b if "pijl" in x], [])
        self.assertEqual([x for x in w if "geen pijl op de hoofdplaat" in x], [])

    def test_given_a_rule_pointing_at_an_unknown_addition_when_checked_then_finding(self):
        r = regels()
        r["regels"].append({"beeld_id": "F3-02", "beeld": "Verzonnen aanvulling", "fase": 3, "stap": "Aanmelden",
                            "soort": "stroomt", "van": "Student volg systeem (SVS)",
                            "naar": "Student Keuze Systeem (SKS)", "pijl": "aanvulling-bestaat-niet",
                            "koppeling": None, "objecttype": "Opleidingaanbod", "instantie": "x",
                            "bron": "b"})
        b, _, _ = bevindingen(r, s=self.echte_stromen())
        self.assertTrue(any("aanvulling-bestaat-niet" in x for x in b), b)


class KoppelingoverzichtTests(unittest.TestCase):
    def test_given_rules_per_koppeling_when_counted_then_each_koppeling_is_listed(self):
        overzicht = cv.koppelingoverzicht(regels())
        self.assertTrue(any(x == "koppeling OC-P&R: 1 regels" for x in overzicht), overzicht)

    def test_given_a_koppeling_without_rules_when_counted_then_it_is_listed_as_empty(self):
        r = regels(); r["koppelingen"]["Onderwijscatalogus > Leer management systeem (LMS)"] = "OC-LMS"
        overzicht = cv.koppelingoverzicht(r)
        self.assertTrue(any("OC-LMS: 0 regels" in x and "geen enkele regel" in x for x in overzicht), overzicht)

    def test_given_a_flow_without_a_koppelingspecificatie_when_counted_then_the_pair_is_listed(self):
        r = regels(); r["regels"][2]["koppeling"] = None
        overzicht = cv.koppelingoverzicht(r)
        self.assertTrue(any("zonder koppelingspecificatie: Planningssysteem naar Onderwijscatalogus, 1 regels" in x
                            for x in overzicht), overzicht)

    def test_given_the_real_table_when_counted_then_the_curriculum_tool_has_no_specification(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        overzicht = cv.koppelingoverzicht(tabel)
        self.assertTrue(any("Curriculum ontwerptool naar Onderwijscatalogus, 29 regels" in x for x in overzicht), overzicht)


class RolPerBeeldTests(unittest.TestCase):
    """De renderer groepeert op rol; twee rollen in een beeld leveren twee bestanden met dezelfde naam op."""

    def test_given_an_image_with_two_roles_when_checked_then_signal_names_both(self):
        r = regels()
        r["regels"][6]["beeld"] = r["regels"][5]["beeld"]
        r["regels"][6]["beeld_id"] = r["regels"][5]["beeld_id"]
        r["regels"][6]["wie"] = "student"
        _, w, _ = bevindingen(r)
        self.assertTrue(any("draagt meer dan een rol" in x and "planner" in x and "student" in x for x in w), w)

    def test_given_an_image_with_one_role_when_checked_then_nothing_is_reported(self):
        _, w, _ = bevindingen(regels())
        self.assertEqual([x for x in w if "meer dan een rol" in x], [])

    def test_given_the_real_table_when_checked_then_only_f4_09_carries_two_roles(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        gevonden = cv.rol_per_beeld(tabel)
        self.assertEqual(len(gevonden), 1)
        self.assertIn("F4-09", gevonden[0])


class UitvoerTests(unittest.TestCase):
    def test_given_a_finding_and_a_signal_when_run_then_exit_one_and_both_in_their_own_group(self):
        import contextlib, io
        with tempfile.TemporaryDirectory() as map_:
            r = regels()
            r["regels"][0]["objecttype"] = "Bestaat niet"          # signalering
            r["regels"].append({"beeld_id": "F2-09", "beeld": "Zonder soort", "fase": 2, "stap": "Aanbod maken",
                                "soort": "ontstaat", "objecttype": "Opleidingaanbod", "instantie": "x", "bron": "b"})
            rp = Path(map_) / "r.json"; rp.write_text(json.dumps(r), encoding="utf-8")
            mp = Path(map_) / "m.json"; mp.write_text(json.dumps(model()), encoding="utf-8")
            sp = Path(map_) / "s.json"; sp.write_text(json.dumps(stromen()), encoding="utf-8")
            uit = io.StringIO()
            with contextlib.redirect_stdout(uit):
                code = cv.main(["--regels", str(rp), "--model", str(mp), "--stromen", str(sp), "--schema", str(SCHEMA)])
            tekst = uit.getvalue()
        self.assertEqual(code, 1)
        self.assertIn("Signaleringen", tekst)
        self.assertIn("Bevindingen", tekst)
        self.assertLess(tekst.index("Signaleringen"), tekst.index("Bevindingen"))
        self.assertIn("signaleringen", tekst.splitlines()[-1])

    def test_given_only_a_signal_when_run_then_exit_zero(self):
        import contextlib, io
        with tempfile.TemporaryDirectory() as map_:
            # een extra regel op een onbekend objecttype: dat is een signalering, en de dekking van de
            # bestaande objecttypen blijft heel, zodat er geen bevinding naast staat
            r = regels()
            r["regels"].append({"beeld_id": "F4-02", "beeld": "Onbekend object", "fase": 4, "stap": "Roosteren",
                                "soort": "ontstaat", "wie": "planner", "objecttype": "Bestaat niet",
                                "instantie": "x", "bron": "b"})
            rp = Path(map_) / "r.json"; rp.write_text(json.dumps(r), encoding="utf-8")
            mp = Path(map_) / "m.json"; mp.write_text(json.dumps(model()), encoding="utf-8")
            sp = Path(map_) / "s.json"; sp.write_text(json.dumps(stromen()), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                code = cv.main(["--regels", str(rp), "--model", str(mp), "--stromen", str(sp), "--schema", str(SCHEMA)])
        self.assertEqual(code, 0)


class MainTests(unittest.TestCase):
    def schrijf(self, map_, naam, inhoud):
        p = Path(map_) / naam
        p.write_text(inhoud if isinstance(inhoud, str) else json.dumps(inhoud), encoding="utf-8")
        return p

    def test_given_missing_input_file_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            m = self.schrijf(map_, "m.json", model())
            self.assertEqual(cv.main(["--regels", str(Path(map_) / "geen.json"), "--model", str(m)]), 2)

    def test_given_invalid_json_when_run_then_exit_one(self):
        with tempfile.TemporaryDirectory() as map_:
            r = self.schrijf(map_, "r.json", "{niet json")
            m = self.schrijf(map_, "m.json", model())
            with self.assertRaises(SystemExit) as fout:
                cv.main(["--regels", str(r), "--model", str(m)])
            self.assertEqual(fout.exception.code, 1)

    def test_given_valid_files_when_run_then_exit_zero(self):
        with tempfile.TemporaryDirectory() as map_:
            r = self.schrijf(map_, "r.json", regels()); m = self.schrijf(map_, "m.json", model()); s = self.schrijf(map_, "s.json", stromen())
            self.assertEqual(cv.main(["--regels", str(r), "--model", str(m), "--stromen", str(s)]), 0)


if __name__ == "__main__":
    unittest.main()
