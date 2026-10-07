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
    return nummer({"model": {"informatiemodel_commit": "abc", "begrippen_commit": "def"},
            "fasen": [{"nummer": 2, "naam": "Publiceren", "mora_hoofdproces": "Plannen", "bron": "ks", "stappen": ["Aanbod maken"], "verwacht": ["Opleidingaanbod"]},
                      {"nummer": 3, "naam": "Instroom", "bron": "ks", "stappen": ["Aanmelden"], "verwacht": ["Aanmelding"]},
                      {"nummer": 4, "naam": "Roosteren", "bron": "ks", "stappen": ["Roosteren"], "verwacht": ["Lesgelegenheid"]}],
            "rollen": ["planner", "student"], "toestanden": [], "scope_uitzonderingen": [{"objecttype": "Lesgelegenheid", "motivering": "besluit"}],
            "koppelingen": {"Planningssysteem > Onderwijscatalogus": "OC-P&R"},
            "regels": [
                {"beeld": "Het aanbod gemaakt", "fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "bron": "leerroute-1-regulier.md, r52 en r1026", "aanname": True, "vraag": "Is cohort een object?"},
                {"beeld": "Aanbod naar de catalogus", "fase": 2, "stap": "Aanbod maken", "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1", "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "bron": "b"},
                {"beeld": "De aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "ontstaat", "wie": "student", "objecttype": "Aanmelding", "instantie": "April", "bron": "b", "vraag": "Is inschrijving een toestand?"}]})


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
        self.assertEqual(beelden[0][1], "f2-01-het-aanbod-gemaakt.svg")
        self.assertEqual(beelden[1], ("ontstaat: Aanbod maken, verdieping: aanbod naar skills", "f2-02-aanbod-maken-verdieping.svg"))

    def test_given_rules_when_generated_then_invulblad_is_own_document_without_reading_text(self):
        r = regels()
        blad = gv.invulblad(r)
        self.assertTrue(blad.startswith("# Invulblad bij de voorbeelduitwerking van leerroute 1"))
        self.assertIn("| 2 | F2-01 | Opleidingaanbod | | | | |", blad)
        self.assertIn("(voorbeeld-leerroute-1-jochem.md)", blad)
        doc = self.bouw(r)
        self.assertNotIn("Invulblad", doc)
        self.assertNotIn("invulblad", doc)

    def test_given_concept_rule_when_generated_then_image_shown_but_not_in_chips_nor_invulblad(self):
        r = regels()
        r["regels"].insert(1, {"fase": 2, "stap": "Aanbod maken", "verdieping": "kader", "plaat": "onderwijsontwerp", "soort": "ontstaat", "wie": "planner",
                               "objecttype": "Leervormstrategie", "instantie": "Leren door te doen", "bron": "c"})
        doc = self.bouw(r)
        self.assertIn("f2-02-aanbod-maken-verdieping.svg", doc)
        self.assertNotIn("`Leervormstrategie`", doc)
        self.assertNotIn("| 2 | F2-02 | Leervormstrategie |", gv.invulblad(r))
        self.assertIn("conceptplaat", doc)

    def test_given_beeld_titles_when_generated_then_heading_per_image_and_register_per_beeld(self):
        doc = self.bouw()
        self.assertIn("### F2-01 - Het aanbod gemaakt\n\n![ontstaat: Aanbod maken](img/regels/f2-01-het-aanbod-gemaakt.svg)", doc)
        reg = doc[doc.index("## Regelregister"):]
        self.assertIn("**F2-01 - Het aanbod gemaakt** (fase 2, Aanbod maken; [f2-01-het-aanbod-gemaakt.svg](img/regels/f2-01-het-aanbod-gemaakt.svg))", reg)
        self.assertIn("| ontstaat | Opleidingaanbod | AA 2026 | [leerroute-1-regulier.md](", reg)
        self.assertIn("?plain=1#L1026)", reg)
        self.assertIn("(F2-01, `Opleidingaanbod`)", doc)

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

    def vragen_in(self, doc):
        """De vragen zoals het document ze nummert, met hun plek erachter."""
        return re.findall(r"^\d+\. (.+?) \(", doc[doc.index("## Vragen"):], re.M)

    def test_given_questions_when_generated_then_each_refers_to_a_rule(self):
        doc = self.bouw()
        vragen = self.vragen_in(doc)
        self.assertEqual(vragen, ["Is cohort een object?", "Is inschrijving een toestand?"])
        self.assertRegex(doc[doc.index("## Vragen"):], r"Is cohort een object\? \(F2-01, `Opleidingaanbod`\)")

    def test_given_nine_questions_when_generated_then_all_nine_stand_in_the_document(self):
        """Eerder stopte de pagina na zeven en ging de rest alleen naar stderr; dan verdwijnt een vraag
        die iemand bewust heeft opgeschreven uit het product."""
        r = regels()
        for i in range(7):
            r["regels"].append({"beeld": "De aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "verandert",
                                "wie": "student", "objecttype": "Aanmelding", "instantie": "x", "toestand": "t",
                                "bron": "b", "vraag": f"Vraag {i}?"})
        doc = self.bouw(nummer(r))
        vragen = self.vragen_in(doc)
        self.assertEqual(len(vragen), 9)
        for i in range(7):
            self.assertIn(f"Vraag {i}?", vragen)

    def test_given_more_questions_than_fit_when_generated_then_a_next_page_with_continuous_numbering(self):
        r = regels()
        for i in range(7):
            r["regels"].append({"beeld": "De aanmelding", "fase": 3, "stap": "Aanmelden", "soort": "verandert",
                                "wie": "student", "objecttype": "Aanmelding", "instantie": "x", "toestand": "t",
                                "bron": "b", "vraag": f"Vraag {i}?"})
        doc = self.bouw(nummer(r))
        staart = doc[doc.index("## Vragen"):]
        self.assertIn("### Vragen, vervolg (2 van 2)", staart)
        self.assertIn("8. Vraag 5?", staart)
        self.assertIn("9. Vraag 6?", staart)
        self.assertIn("De eerste 7 vragen gaan als ronde mee naar de kerngroep", staart)
        self.assertIn("overige 2", staart)

    def test_given_the_page_size_when_read_then_it_is_an_explicit_setting(self):
        self.assertEqual(gv.VRAGEN_PER_PAGINA, 7)

    def test_given_seven_questions_or_fewer_when_generated_then_no_overflow_text(self):
        doc = self.bouw()
        self.assertNotIn("Vragen, vervolg", doc)
        self.assertNotIn("wachten op een volgende ronde", doc)

    def test_given_a_parked_finding_with_a_question_when_generated_then_it_stands_in_the_document(self):
        """Een bevinding die blijft liggen levert een vraag op, en die hoort in het product te komen."""
        r = regels()
        r["bevindingen"] = [{"nummer": "B01", "beeld_id": "F2-01", "lezer": "NvDuin", "datum": "2026-09-28",
                             "bron": "https://github.com/x/y/pull/252#discussion_r1", "tekst": "te rechtlijnig",
                             "themas": ["clustering"], "issue": 283, "status": "geparkeerd",
                             "reden": "wacht op de modelronde",
                             "vraag": "Heeft de specificatiekant een container nodig?"}]
        doc = self.bouw(r)
        self.assertIn("Heeft de specificatiekant een container nodig? (F2-01, bevinding B01)", doc)

    def test_given_no_questions_when_generated_then_the_page_says_so(self):
        r = regels()
        for x in r["regels"]:
            x.pop("vraag", None)
        doc = self.bouw(r)
        self.assertIn("Er staan nu geen vragen in de regeltabel.", doc)

    def test_given_the_reading_guide_when_read_then_it_explains_specification_offer_and_association(self):
        """Criterium 9 van elke fase: de primaire lezer kent die termen niet van huis uit, dus het
        onderscheid hoort uit de tekst zelf te blijken."""
        doc = self.bouw()
        guide = doc[doc.index("## Leeswijzer"):doc.index("## ", doc.index("## Leeswijzer") + 5)]
        for term in ("Specificatie", "Aanbod", "Verbintenis", "Resultaat"):
            self.assertIn(f"| {term} |", guide)
        self.assertIn("zonder dat er iemand voor kiest", guide)

    def test_given_the_examples_in_the_reading_guide_when_checked_then_the_table_still_carries_them(self):
        """De leeswijzer noemt instanties uit de regeltabel; verdwijnt er een, dan liegt de uitleg."""
        tabel = json.loads((Path(__file__).resolve().parent.parent / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        alles = " | ".join(r.get("instantie", "") for r in tabel["regels"])
        for voorbeeld in ("Apothekersassistent, versie 2026.1", "Apothekersassistent 2026", "Jochem op Regulier BOL 2026"):
            self.assertIn(voorbeeld, alles)

    def test_given_the_specialisation_table_when_read_then_the_plate_carries_every_pair(self):
        """De leeswijzer legt de specialisatieregel uit met het keuzedeel als voorbeeld. Klopt een paar niet
        meer met de plaat, dan legt de uitleg iets uit dat er niet staat."""
        wortel = Path(__file__).resolve().parent.parent
        model = json.loads((wortel / "architecture/model/informatiemodel/informatiemodel.json").read_text(encoding="utf-8"))
        paren = {(r["van"], r["naar"]) for r in model["relaties"] if r["soort"] == "Specialization"}
        for bijzonder, algemeen in (
                ("Keuzedeel", "Opleidingsprogramma specificatie"),
                ("Keuzedeelruimte", "Opleidingsprogramma specificatie"),
                ("Keuzedeelaanbod", "Opleidingsprogramma aanbod"),
                ("Keuzedeel aanbod verbintenis", "Opleidingsprogramma aanbod verbintenis"),
                ("Keuzedeel resultaat", "Opleidingsprogramma resultaat")):
            self.assertIn((bijzonder, algemeen), paren, f"{bijzonder} is geen specialisatie van {algemeen}")
        doc = self.bouw()
        self.assertIn("| Aanbod | `Opleidingsprogramma aanbod` | `Keuzedeelaanbod` |", doc)

    def test_given_document_when_generated_then_no_dash_and_no_frontmatter(self):
        doc = self.bouw()
        self.assertFalse(doc.startswith("---"))
        self.assertNotIn("—", doc)
        self.assertNotIn("–", doc)

    def test_given_same_input_twice_when_generated_then_identical_output(self):
        self.assertEqual(self.bouw(), self.bouw())

    def test_given_definition_status_when_generated_then_shown(self):
        doc = self.bouw()
        self.assertRegex(doc, r"\| Opleidingaanbod \| F2-01 \| AA 2026 \| 2 \| ja \| ja \| ProgrammeOffering \|")
        self.assertRegex(doc, r"\| Aanmelding \| F3-01 \| April \| 3 \|  \| nog niet \| geen equivalent \|")

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

    def test_given_a_run_when_it_ends_then_the_last_line_names_the_counts(self):
        """De aantallen aan het eind, zodat verlies opvalt zonder het bestand te vergelijken."""
        import contextlib, io
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            for naam, inhoud in (("r.json", regels()), ("m.json", model()), ("b.json", begrippen())):
                (m / naam).write_text(json.dumps(inhoud), encoding="utf-8")
            tv.teken(regels(), m / "img" / "regels")
            (m / "informatiemodel.md").write_text("# Informatiemodel\n", encoding="utf-8")
            uit = io.StringIO()
            with contextlib.redirect_stdout(uit):
                code = gv.main(["--regels", str(m / "r.json"), "--model", str(m / "m.json"),
                                "--begrippen", str(m / "b.json"), "--uit", str(m / "doc.md")])
        self.assertEqual(code, 0)
        self.assertEqual(uit.getvalue().splitlines()[-1], "verwerkt: 3 beelden, 3 regels, 2 vragen")

    def test_given_unchanged_input_when_run_twice_then_the_file_does_not_differ(self):
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            for naam, inhoud in (("r.json", regels()), ("m.json", model()), ("b.json", begrippen())):
                (m / naam).write_text(json.dumps(inhoud), encoding="utf-8")
            tv.teken(regels(), m / "img" / "regels")
            (m / "informatiemodel.md").write_text("# Informatiemodel\n", encoding="utf-8")
            argv = ["--regels", str(m / "r.json"), "--model", str(m / "m.json"),
                    "--begrippen", str(m / "b.json"), "--uit", str(m / "doc.md")]
            import contextlib, io
            with contextlib.redirect_stdout(io.StringIO()):
                gv.main(argv)
                eerst = (m / "doc.md").read_text(encoding="utf-8")
                blad_eerst = (m / "voorbeeld-leerroute-1-jochem-invulblad.md").read_text(encoding="utf-8")
                gv.main(argv)
            self.assertEqual(eerst, (m / "doc.md").read_text(encoding="utf-8"))
            self.assertEqual(blad_eerst, (m / "voorbeeld-leerroute-1-jochem-invulblad.md").read_text(encoding="utf-8"))

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
