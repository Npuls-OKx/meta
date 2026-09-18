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


def regels():
    return {"model": {"informatiemodel_commit": "abc123", "begrippen_commit": "def456"},
            "fasen": [
                {"nummer": 2, "naam": "Publiceren", "bron": "ks", "stappen": ["Aanbod maken", "Aanbod publiceren"], "verwacht": ["Opleidingaanbod", "Opleidingsprogramma aanbod"]},
                {"nummer": 3, "naam": "Instroom", "bron": "ks", "stappen": ["Aanmelden"], "verwacht": ["Aanmelding", "Opleiding aanbod verbintenis"]},
                {"nummer": 4, "naam": "Roosteren", "bron": "ks", "stappen": ["Roosteren"], "verwacht": ["Lesgelegenheid"]}],
            "rollen": ["planner", "student"],
            "toestanden": [{"naam": "geroosterd", "bron": "ks"}],
            "scope_uitzonderingen": [{"objecttype": "Lesgelegenheid", "motivering": "besluit"}],
            "koppelingen": {"Planningssysteem > Onderwijscatalogus": "OC-P&R"},
            "regels": [
                {"id": "R2-001", "fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "ks r1"},
                {"id": "R2-002", "fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingsprogramma aanbod", "instantie": "Regulier BOL 2026", "bron": "ks r2",
                 "relatie": {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Opleidingsprogramma aanbod", "nesting": True}},
                {"id": "R2-003", "fase": 2, "stap": "Aanbod publiceren", "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "v1.7"},
                {"id": "R3-001", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Aanmelding", "instantie": "April 2026", "bron": "ks r3",
                 "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Aanmelding", "label": "Op basis van"}},
                {"id": "R3-002", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Opleiding aanbod verbintenis", "instantie": "Jochem 2026", "bron": "ks r4"},
                {"id": "R4-001", "fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "planner", "objecttype": "Lesgelegenheid", "instantie": "ma 09:00", "bron": "ks r5"},
                {"id": "R4-002", "fase": 4, "stap": "Roosteren", "soort": "verandert", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "toestand": "geroosterd", "bron": "ks r6"}]}


def bevindingen(r=None, m=None, s="standaard", **kw):
    b, w, o = cv.controleer(r or regels(), m or model(), stromen() if s == "standaard" else s, **kw)
    return b, w, o


class ControleTests(unittest.TestCase):
    def test_given_valid_table_when_checked_then_no_findings(self):
        b, w, o = bevindingen()
        self.assertEqual(b, [])
        self.assertEqual(o, {})

    def test_given_rule_without_required_field_when_checked_then_finding_names_rule_and_field(self):
        r = regels(); del r["regels"][0]["instantie"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("regel R2-001" in x and "instantie" in x for x in b))

    def test_given_unknown_objecttype_when_checked_then_finding_names_type(self):
        r = regels(); r["regels"][0]["objecttype"] = "Bestaat niet"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("Bestaat niet" in x and "bestaat niet in het informatiemodel" in x for x in b))

    def test_given_name_differing_only_in_whitespace_when_checked_then_accepted(self):
        # de fixture kent "Opleiding aanbod  verbintenis" met dubbele spatie; de regel gebruikt een spatie
        b, _, _ = bevindingen()
        self.assertFalse(any("Opleiding aanbod verbintenis" in x for x in b))

    def test_given_assumed_instance_on_known_type_when_checked_then_accepted(self):
        r = regels(); r["regels"][0]["aanname"] = True
        b, _, _ = bevindingen(r)
        self.assertEqual(b, [])

    def test_given_assumed_objecttype_not_on_plate_when_checked_then_finding(self):
        r = regels(); r["regels"][0]["objecttype"] = "Verzonnen"; r["regels"][0]["aanname"] = True
        b, _, _ = bevindingen(r)
        self.assertTrue(any("Verzonnen" in x for x in b))

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
    r = {"id": "R2-009", "fase": 2, "stap": "Aanbod maken", "verdieping": "kader", "plaat": "onderwijsontwerp", "soort": "ontstaat", "wie": "planner",
         "objecttype": "Leerdoel", "instantie": "Leren door te doen", "bron": "conceptplaat",
         "relatie": {"soort": "Association", "van": "Leervormstrategie", "naar": "Leerdoel"}}
    r.update(extra)
    return r


class ConceptplaatTests(unittest.TestCase):
    def test_given_concept_rule_in_verdieping_when_checked_against_conceptplaat_then_no_findings(self):
        r = regels(); r["regels"].append(conceptregel())
        b, _, o = bevindingen(r, conceptplaat=conceptplaat())
        self.assertEqual(b, [])
        self.assertEqual(o, {})

    def test_given_concept_rule_without_verdieping_when_checked_then_finding(self):
        r = regels(); r["regels"].append(conceptregel(verdieping=None))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("alleen in een verdieping" in x for x in b))

    def test_given_concept_rule_when_conceptplaat_not_loaded_then_finding(self):
        r = regels(); r["regels"].append(conceptregel())
        b, _, _ = bevindingen(r)
        self.assertTrue(any("conceptplaat is niet geladen" in x for x in b))

    def test_given_concept_rule_with_unknown_type_or_relation_when_checked_then_finding_names_conceptplaat(self):
        r = regels(); r["regels"].append(conceptregel(objecttype="Onderwijsvorm specificatie"))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("bestaat niet op de conceptplaat" in x for x in b))
        r = regels(); r["regels"].append(conceptregel(relatie={"soort": "Aggregation", "van": "Leervormstrategie", "naar": "Leerdoel"}))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("staat niet op de conceptplaat" in x for x in b))

    def test_given_concept_rule_when_checked_then_not_counted_in_coverage_nor_scope(self):
        r = regels(); r["regels"].append(conceptregel(objecttype="Leerdoel", instantie="x", relatie=None))
        r["regels"].append(conceptregel(id="R2-010", instantie="y", relatie=None))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertFalse(any("ontstaat-regels" in x or "buiten scope" in x for x in b))

    def test_given_unknown_plaat_when_checked_then_finding(self):
        r = regels(); r["regels"].append(conceptregel(plaat="hoofdplaat"))
        b, _, _ = bevindingen(r, conceptplaat=conceptplaat())
        self.assertTrue(any("plaat 'hoofdplaat'" in x for x in b))


class IdEnRelatiesTests(unittest.TestCase):
    def test_given_id_missing_or_wrong_when_checked_then_finding(self):
        r = regels(); del r["regels"][0]["id"]
        b, _, _ = bevindingen(r)
        self.assertTrue(any("veld id ontbreekt" in x for x in b))
        r = regels(); r["regels"][0]["id"] = "F2-01"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("volgt niet R<fase>-<nnn>" in x for x in b))
        r = regels(); r["regels"][0]["id"] = "R3-001"
        b, _, _ = bevindingen(r)
        self.assertTrue(any("andere fase" in x for x in b))
        self.assertTrue(any("is al gebruikt" in x for x in b))

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
