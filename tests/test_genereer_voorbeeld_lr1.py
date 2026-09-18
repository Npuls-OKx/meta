"""Testgevallen voor scripts/genereer-voorbeeld-lr1.py.

Fixture-regeltabel, -model en -begrippen in de test zelf; het document wordt in
een tijdelijke map gebouwd met lege SVG's op de verwachte paden.
"""

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("genereer_voorbeeld_lr1", WORTEL / "scripts/genereer-voorbeeld-lr1.py")
gv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gv)
spec2 = importlib.util.spec_from_file_location("teken_voorbeeldregels", WORTEL / "scripts/teken-voorbeeldregels.py")
tv = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(tv)


def model():
    return {"objecttypen": [
                {"naam": "Opleidingaanbod", "kolom": "Onderwijsaanbod", "scope": "binnen"},
                {"naam": "Aanmelding", "kolom": "Onderwijsverbintenis", "scope": "binnen"},
                {"naam": "Lesgelegenheid", "kolom": "Onderwijsaanbod", "scope": "buiten"},
                {"naam": "OER", "kolom": None, "scope": "buiten"}],
            "relaties": [], "oeapi_mapping": [{"okx": "Opleidingaanbod", "oeapi": "ProgrammeOffering", "relatie": "Realization"}]}


def begrippen():
    return {"begrippen": [{"naam": "Opleidingaanbod", "varianten": [], "status": "gedefinieerd"}, {"naam": "Aanmelding", "varianten": [], "status": "open"}]}


def regels():
    return {"model": {"informatiemodel_commit": "abc", "begrippen_commit": "def"},
            "fasen": [{"nummer": 2, "naam": "Publiceren", "mora_hoofdproces": "Plannen", "bron": "ks", "stappen": ["Aanbod maken"], "verwacht": ["Opleidingaanbod"]},
                      {"nummer": 3, "naam": "Instroom", "bron": "ks", "stappen": ["Aanmelden"], "verwacht": ["Aanmelding"]},
                      {"nummer": 4, "naam": "Roosteren", "bron": "ks", "stappen": ["Roosteren"], "verwacht": ["Lesgelegenheid"]}],
            "rollen": ["planner", "student"], "toestanden": [], "scope_uitzonderingen": [{"objecttype": "Lesgelegenheid", "motivering": "besluit"}],
            "koppelingen": {"Planningssysteem > Onderwijscatalogus": "OC-P&R"},
            "regels": [
                {"beeld": "Het aanbod gemaakt", "fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "bron": "leerroute-1-regulier.md, r52 en r1026", "aanname": True, "vraag": "Is cohort een object?"},
                {"beeld": "Aanbod naar de catalogus", "fase": 2, "stap": "Aanbod maken", "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1", "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "bron": "b"},
                {"beeld": "De aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Aanmelding", "instantie": "April", "bron": "b", "vraag": "Is inschrijving een toestand?"}]}


class GenereerTests(unittest.TestCase):
    def bouw(self, r=None):
        return gv.bouw(r or regels(), model(), begrippen())

    def test_given_fasenlijst_when_generated_then_sections_in_order(self):
        doc = self.bouw()
        koppen = re.findall(r"^## Fase (\d):", doc, re.M)
        self.assertEqual(koppen, ["2", "3", "4"])

    def test_given_rules_when_generated_then_svg_names_match_renderer(self):
        r = regels()
        doc = self.bouw(r)
        verwezen = sorted(set(re.findall(r"img/regels/([^)]+)", doc)))
        with tempfile.TemporaryDirectory() as map_:
            getekend = sorted(n for n, _ in tv.teken(r, map_))
        self.assertEqual(verwezen, getekend)

    def test_given_verdieping_when_generated_then_own_image_after_step_with_alt_text(self):
        r = regels()
        r["regels"].insert(1, {"fase": 2, "stap": "Aanbod maken", "verdieping": "aanbod naar skills", "soort": "verandert", "wie": "planner",
                               "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "toestand": "verdiept", "bron": "b"})
        doc = self.bouw(r)
        beelden = re.findall(r"!\[([^\]]+)\]\(img/regels/([^)]+)\)", doc)
        self.assertEqual(beelden[0][1], "f2-het-aanbod-gemaakt.svg")
        self.assertEqual(beelden[1], ("ontstaat: Aanbod maken, verdieping: aanbod naar skills", "f2-02-aanbod-maken-verdieping.svg"))

    def test_given_concept_rule_when_generated_then_image_shown_but_not_in_chips_nor_invulblad(self):
        r = regels()
        r["regels"].insert(1, {"fase": 2, "stap": "Aanbod maken", "verdieping": "kader", "plaat": "onderwijsontwerp", "soort": "ontstaat", "wie": "planner",
                               "objecttype": "Leervormstrategie", "instantie": "Leren door te doen", "bron": "c"})
        doc = self.bouw(r)
        self.assertIn("f2-02-aanbod-maken-verdieping.svg", doc)
        self.assertNotIn("`Leervormstrategie`", doc)
        self.assertNotIn("| 2 | Aanbod maken | Leervormstrategie |", doc)
        self.assertIn("conceptplaat", doc)

    def test_given_beeld_titles_when_generated_then_heading_per_image_and_register_per_beeld(self):
        doc = self.bouw()
        self.assertIn("### Het aanbod gemaakt\n\n![ontstaat: Aanbod maken](img/regels/f2-het-aanbod-gemaakt.svg)", doc)
        reg = doc[doc.index("## Regelregister"):]
        self.assertIn("**Het aanbod gemaakt** (fase 2, Aanbod maken; [f2-het-aanbod-gemaakt.svg](img/regels/f2-het-aanbod-gemaakt.svg))", reg)
        self.assertIn("| ontstaat | Opleidingaanbod | AA 2026 | [leerroute-1-regulier.md](", reg)
        self.assertIn("?plain=1#L1026)", reg)
        self.assertIn("| 2 | Het aanbod gemaakt | Opleidingaanbod | | | | |", doc[doc.index("### Invulblad"):])
        self.assertIn("(Het aanbod gemaakt, `Opleidingaanbod`)", doc)

    def test_given_source_with_fase_when_linked_then_fase_anchor_and_unknown_source_stays_text(self):
        links = {1: "https://x/#fase-1"}
        self.assertEqual(gv.bronlinks("leerroute-1-regulier.md, Fase 1: iets", links), "[leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://x/#fase-1): iets")
        self.assertEqual(gv.bronlinks("geen bron, keuze van het voorbeeld"), "geen bron, keuze van het voorbeeld")
        self.assertIn("scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L82", gv.bronlinks("scenario-1.1-regulier-happyflow.md, r82: intake"))

    def test_given_scope_when_generated_then_family_tables_cover_in_scope_types(self):
        doc = self.bouw()
        bijlage = doc[doc.index("## Bijlage"):doc.index("## Vragen")]
        rijen = {m.group(1) for m in re.finditer(r"^\| ([^|]+?) \|", bijlage, re.M)} - {"Objecttype"}
        self.assertEqual(rijen, {"Opleidingaanbod", "Aanmelding", "Lesgelegenheid"})

    def test_given_type_without_rule_when_generated_then_marked_with_stub_sentence(self):
        doc = self.bouw()
        self.assertRegex(doc, r"\| Lesgelegenheid \|  \| regels volgen na 30 september \| 4 \|")

    def test_given_fase_without_rules_when_generated_then_stub_with_chips_and_sentence(self):
        doc = self.bouw()
        sectie = doc[doc.index("## Fase 4"):doc.index("## Bijlage")]
        self.assertIn("`Lesgelegenheid`", sectie)
        self.assertIn(gv.STUBZIN, sectie)
        self.assertNotIn("img/regels", sectie)

    def test_given_chips_when_generated_then_equal_to_rules_in_fase(self):
        doc = self.bouw()
        sectie = doc[doc.index("## Fase 2"):doc.index("## Fase 3")]
        self.assertIn("**Ontstaat:** `Opleidingaanbod`", sectie)
        self.assertIn("**Stroomt:** Planningssysteem naar Onderwijscatalogus", sectie)
        self.assertIn("**MORA-hoofdproces:** Plannen", sectie)

    def test_given_questions_when_generated_then_each_refers_to_rule_and_max_seven(self):
        r = regels()
        for i in range(10):
            r["regels"].append({"beeld": "De aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "verandert", "wie": "student", "objecttype": "Aanmelding", "instantie": "x", "toestand": "t", "bron": "b", "vraag": f"Vraag {i}?"})
        doc = self.bouw(r)
        vragen = re.findall(r"^\d+\. (.+?) \([^,]+, `", doc[doc.index("## Vragen"):], re.M)
        self.assertEqual(len(vragen), 7)
        self.assertIn("Is cohort een object?", vragen)

    def test_given_document_when_generated_then_no_dash_and_no_frontmatter(self):
        doc = self.bouw()
        self.assertFalse(doc.startswith("---"))
        self.assertNotIn("—", doc)
        self.assertNotIn("–", doc)

    def test_given_same_input_twice_when_generated_then_identical_output(self):
        self.assertEqual(self.bouw(), self.bouw())

    def test_given_definition_status_when_generated_then_shown(self):
        doc = self.bouw()
        self.assertRegex(doc, r"\| Opleidingaanbod \| Het aanbod gemaakt \| AA 2026 \| 2 \| ja \| ja \| ProgrammeOffering \|")
        self.assertRegex(doc, r"\| Aanmelding \| De aanmelding \| April \| 3 \|  \| nog niet \| geen equivalent \|")

    def test_given_missing_svg_directory_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            for naam, inhoud in (("r.json", regels()), ("m.json", model()), ("b.json", begrippen())):
                (m / naam).write_text(json.dumps(inhoud), encoding="utf-8")
            code = gv.main(["--regels", str(m / "r.json"), "--model", str(m / "m.json"), "--begrippen", str(m / "b.json"), "--uit", str(m / "doc.md")])
        self.assertEqual(code, 2)

    def test_given_svg_missing_when_run_then_exit_one_names_it(self):
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            for naam, inhoud in (("r.json", regels()), ("m.json", model()), ("b.json", begrippen())):
                (m / naam).write_text(json.dumps(inhoud), encoding="utf-8")
            (m / "img" / "regels").mkdir(parents=True)
            code = gv.main(["--regels", str(m / "r.json"), "--model", str(m / "m.json"), "--begrippen", str(m / "b.json"), "--uit", str(m / "doc.md")])
        self.assertEqual(code, 1)

    def test_given_all_svgs_present_when_run_then_document_written_and_validate_docs_zero(self):
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            for naam, inhoud in (("r.json", regels()), ("m.json", model()), ("b.json", begrippen())):
                (m / naam).write_text(json.dumps(inhoud), encoding="utf-8")
            tv.teken(regels(), m / "img" / "regels")
            (m / "informatiemodel.md").write_text("# Informatiemodel\n", encoding="utf-8")  # het document verwijst ernaar
            code = gv.main(["--regels", str(m / "r.json"), "--model", str(m / "m.json"), "--begrippen", str(m / "b.json"), "--uit", str(m / "doc.md")])
            self.assertEqual(code, 0)
            uit = subprocess.run([sys.executable, str(WORTEL / "scripts/validate-docs.py"), str(m / "doc.md")], capture_output=True, text=True)
            self.assertEqual(uit.returncode, 0, uit.stdout + uit.stderr)


if __name__ == "__main__":
    unittest.main()
