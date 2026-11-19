"""Testgevallen bij de sjablonen voor de adviesgroep (#554).

De poort bewaakt vier dingen. Het skelet is uit zijn uitwerking afgeleid en
draagt elke kop daarvan. Elke kop is een feitelijk label en geen vraag. Elk
hoofdstuk draagt het verwachtingsblok dat zegt wat er wordt opgeleverd. En een
beeld staat als beeld in het document, niet als beschrijving van een beeld.
"""

import importlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

WORTEL = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WORTEL / "tools/scripts"))

bouw_docx = importlib.import_module("bouw-sjablonen-docx")
bouw_ref = importlib.import_module("bouw-sjabloon-referentie")
maak = importlib.import_module("maak-sjabloon-uit-document")

MAP = WORTEL / "architecture/docs/sjablonen"
SKELET = MAP / "gegenereerd"
CONFIG = json.loads((MAP / "bron/sjablonen.json").read_text(encoding="utf-8"))
KOP = re.compile(r"^(#{1,6}) +(.*)$", re.M)
VRAAGWOORD = re.compile(r"^(Wat|Hoe|Waarom|Wanneer|Welke|Wie)\b", re.I)


def skelet(naam: str) -> str:
    return (SKELET / f"{naam}.md").read_text(encoding="utf-8")


def document_xml(pad: pathlib.Path) -> bytes:
    with zipfile.ZipFile(pad) as z:
        return z.read("word/document.xml")


class ElkSjabloonBestaat(unittest.TestCase):
    def test_vijf_sjablonen(self):
        self.assertEqual(len(CONFIG), 5)
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertTrue((SKELET / f"{naam}.md").exists())

    def test_elke_docx_staat_in_versiebeheer(self):
        gevolgd = subprocess.run(
            ["git", "ls-files", "architecture/docs/sjablonen"],
            cwd=WORTEL, capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        for cfg in CONFIG.values():
            with self.subTest(cfg["bestand"]):
                self.assertIn(f"architecture/docs/sjablonen/{cfg['bestand']}",
                              gevolgd)

    def test_controleer_meldt_een_ontbrekend_sjabloon(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(
                bouw_docx.bouw(pathlib.Path(tmp), bouw_docx.REFERENTIE,
                               controleer=True), 1)


class EenKopIsEenLabel(unittest.TestCase):
    """Een kop noemt wat eronder staat; hij stelt geen vraag en vat niet samen."""

    def test_geen_vraagteken(self):
        for naam in CONFIG:
            for _, kop in KOP.findall(skelet(naam)):
                with self.subTest(f"{naam}: {kop}"):
                    self.assertNotIn("?", kop)

    def test_geen_vraagwoord_aan_het_begin(self):
        for naam in CONFIG:
            for _, kop in KOP.findall(skelet(naam)):
                kaal = maak.NUMMER.sub("", kop).strip()
                with self.subTest(f"{naam}: {kop}"):
                    self.assertIsNone(VRAAGWOORD.match(kaal),
                                      "zet een feitelijk label in kop_labels")

    def test_geen_eigen_nummering(self):
        """Het Npuls-sjabloon nummert zijn koppen zelf; twee tellers botsen."""
        for naam in CONFIG:
            for _, kop in KOP.findall(skelet(naam)):
                with self.subTest(f"{naam}: {kop}"):
                    self.assertIsNone(maak.NUMMER.match(kop))

    def test_een_vraagkop_wordt_een_label(self):
        self.assertEqual(maak.label("3.1 Wat is dit document?", {}),
                         "Dit document")
        self.assertEqual(maak.label("Wat levert dit op?",
                                    {"Wat levert dit op?": "Opbrengst"}),
                         "Opbrengst")


class ElkHoofdstukZegtWatErWordtVerwacht(unittest.TestCase):
    def test_het_verwachtingsblok_staat_er_even_vaak_als_een_hoofdstuk(self):
        vast = ("Invullen", "Van user story naar eis", "De grootst gemene deler",
                "Afwijkingen per instelling", "Vragen aan OKx")
        for naam in CONFIG:
            t = skelet(naam)
            eigen = len([k for _, k in KOP.findall(t) if k in vast])
            with self.subTest(naam):
                self.assertEqual(t.count("**Voorbeeld** ["),
                                 len(KOP.findall(t)) - eigen,
                                 "elk hoofdstuk uit de bron draagt een "
                                 "verwachtingsblok")

    def test_elk_blok_draagt_voorbeeld_criteria_en_een_laag(self):
        for naam in CONFIG:
            t = skelet(naam)
            with self.subTest(naam):
                self.assertIn("**Voorbeeld** [", t)
                self.assertEqual(t.count("**Voorbeeld** ["),
                                 t.count("**Acceptatiecriteria** "))
                lagen = sum(t.count(regel.split("*")[2]) for regel in
                            maak.LAGEN.values())
                self.assertEqual(lagen, t.count("**Voorbeeld** ["),
                                 "elk hoofdstuk noemt zijn laag in de "
                                 "requirementketen")

    def test_niet_elk_hoofdstuk_vraagt_user_stories(self):
        """Een journey brengt een behoefte naar boven; een gegevenshoofdstuk niet."""
        t = skelet("leerroute-scenario")
        stories = t.count("**User stories**")
        self.assertGreater(stories, 0)
        self.assertLess(stories, t.count("**Voorbeeld** [") / 2,
                        "als elk hoofdstuk user stories vraagt, zegt de "
                        "indeling niets meer")
        for laag in ("**Business requirements**", "**Functional requirements**",
                     "**Technical requirements**"):
            self.assertIn(laag, t)

    def test_een_acceptatiecriterium_noemt_de_context(self):
        t = skelet("leerroute-scenario")
        self.assertIn("procesplaat van de studentreis", t)
        self.assertIn("in het kader van de persona", t)
        self.assertIn("mermaid, BPMN, UML of vergelijkbaar", t)

    def test_een_hoofdstuk_dat_niet_elke_route_raakt_is_optioneel(self):
        t = skelet("leerroute-scenario")
        self.assertIn("*Optioneel:", t)
        self.assertIn("laat de kop staan met die reden eronder", t)

    def test_het_verwachte_artefact_komt_uit_de_bron(self):
        """Een hoofdstuk met een diagram vraagt om een diagram."""
        s = maak.Sjabloon("x", {"bron": "README.md", "voorbeeld_naam": "Bron"})
        met_diagram = s.verwachting("Kop", "Kop", ["```mermaid", "graph TD", "```"])
        self.assertIn("procesplaat", "\n".join(met_diagram))
        met_tabel = s.verwachting("Kop", "Kop", ["| a | b |", "|---|---|"])
        self.assertIn("tabel", "\n".join(met_tabel))
        leeg = s.verwachting("Kop", "Kop", ["gewone tekst"])
        self.assertIn("lopende tekst", "\n".join(leeg))

    def test_de_user_stories_en_de_requirementlagen_staan_uitgelegd(self):
        for naam in CONFIG:
            t = skelet(naam)
            with self.subTest(naam):
                self.assertIn("# Van user story naar eis", t)
                for laag in ("Business requirement", "Functional requirement",
                             "Technical requirement"):
                    self.assertIn(laag, t)
                self.assertIn("pakket van eisen", t)


class EenBeeldIsEenBeeld(unittest.TestCase):
    def test_geen_beschrijving_in_plaats_van_een_beeld(self):
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertNotIn("Voeg hier het beeld in", skelet(naam),
                                 "een beeld hoort in het document te staan")

    def test_elk_genoemd_beeld_bestaat(self):
        for naam in CONFIG:
            for alt, pad in re.findall(r"!\[([^\]]*)\]\(<?([^)>]*)>?\)",
                                       skelet(naam)):
                with self.subTest(f"{naam}: {pad}"):
                    self.assertTrue((SKELET / pad).exists(),
                                    f"{pad} staat niet naast het skelet")

    def test_geen_vectorbeeld_in_het_skelet(self):
        """Het Word-formaat draagt geen SVG."""
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertEqual(
                    [p for _, p in re.findall(r"!\[([^\]]*)\]\(<?([^)>]*)>?\)",
                                              skelet(naam))
                     if p.lower().endswith(".svg")], [])


class HetSkeletDraagtZijnUitwerking(unittest.TestCase):
    def test_opnieuw_afleiden_geeft_hetzelfde_skelet(self):
        with tempfile.TemporaryDirectory() as tmp:
            for naam, cfg in CONFIG.items():
                with self.subTest(naam):
                    self.assertEqual(
                        maak.Sjabloon(naam, cfg, pathlib.Path(tmp)).maak(),
                        skelet(naam),
                        f"gegenereerd/{naam}.md loopt achter op {cfg['bron']}")

    def test_geen_relatieve_verwijzing_behalve_naar_een_beeld(self):
        for naam in CONFIG:
            los = [d for d in re.findall(r"(?<!!)\[[^\]]*\]\(<?([^)>]+)>?\)",
                                         skelet(naam))
                   if not d.startswith(("http://", "https://", "#", "img/"))]
            with self.subTest(naam):
                self.assertEqual(los, [], "in Word wijst dit nergens heen")

    def test_elke_tabel_heeft_een_kopregel(self):
        for naam in CONFIG:
            regels = skelet(naam).splitlines()
            for nr, regel in enumerate(regels, 1):
                if (regel.startswith("|") and not regel.replace("|", "").strip()
                        and not re.match(r"^\|[\s:|-]+\|\s*$", regel)
                        and not regels[nr - 2].startswith("|")):
                    self.fail(f"{naam}.md regel {nr}: lege kopregel")

    def test_de_aggregatiestap_en_het_slot(self):
        for naam in CONFIG:
            t = skelet(naam)
            with self.subTest(naam):
                self.assertIn("# De grootst gemene deler", t)
                self.assertIn("niet voor de sector", t)
                self.assertIn("# Afwijkingen per instelling", t)
                self.assertIn("# Vragen aan OKx", t)
                self.assertIn(maak.RUIMTE, t)


class DeGeneratorWeigertWatHijNietKan(unittest.TestCase):
    def test_een_onbekend_sjabloon(self):
        with self.assertRaises(SystemExit):
            maak.main(["--sjabloon", "bestaat-niet"])

    def test_een_bron_die_niet_bestaat(self):
        with self.assertRaises(SystemExit) as e:
            maak.Sjabloon("x", {"bron": "nergens.md"}).brontekst()
        self.assertIn("bestaat niet", str(e.exception))

    def test_een_bron_op_een_tak_die_er_niet_is(self):
        with self.assertRaises(SystemExit) as e:
            maak.Sjabloon("x", {"bron": "README.md",
                                "bron_ref": "geen-tak"}).brontekst()
        self.assertIn("git fetch", str(e.exception))

    def test_een_grens_die_alles_weglaat(self):
        kaal = {"bron": "README.md", "titel": "T", "wat": "w", "wie": "w",
                "voorbeeld": "v", "aggregatie": "a",
                "weglaten_tot": "bestaat niet"}
        with self.assertRaises(SystemExit) as e:
            maak.Sjabloon("x", kaal).maak()
        self.assertIn("geen enkel hoofdstuk", str(e.exception))

    def test_een_verwijzing_blijft_heel_bij_het_vervangen(self):
        uit = maak.vervang("[(2) Temporiseren](persona_larissa.md) van Larissa",
                           [["Larissa", "<student>"]])
        self.assertIn("persona_larissa.md", uit)
        self.assertIn("van <student>", uit)

    def test_een_linkdoel_maakt_een_alinea_niet_bronspecifiek(self):
        self.assertFalse(maak.bronspecifiek("zie [tempo](persona_larissa.md)",
                                            [["Larissa", "<student>"]]))
        self.assertTrue(maak.bronspecifiek("Larissa studeert",
                                           [["Larissa", "<student>"]]))

    def test_een_kop_houdt_haar_hoofdletter(self):
        self.assertEqual(maak.vervang("Leerroute 1 en leerroute 1",
                                      [["leerroute 1", "leerroute <n>"]]),
                         "Leerroute <n> en leerroute <n>")


class DeDocxHoortBijHetSkelet(unittest.TestCase):
    def test_opnieuw_bouwen_geeft_hetzelfde_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            bouw_docx.bouw(tmp, bouw_docx.REFERENTIE)
            for naam, bestand in bouw_docx.SJABLONEN.items():
                with self.subTest(naam):
                    self.assertEqual(
                        document_xml(MAP / bestand), document_xml(tmp / bestand),
                        f"{bestand} loopt achter op gegenereerd/{naam}.md")

    def test_zonder_referentie_weigert_het_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            with self.assertRaises(SystemExit) as e:
                bouw_docx.bouw(tmp, tmp / "bestaat-niet.docx")
            self.assertIn("ontbreekt", str(e.exception))
            self.assertEqual(list(tmp.iterdir()), [])


class DeReferentieDraagtDeHuisstijl(unittest.TestCase):
    def test_de_referentie_komt_uit_het_npuls_sjabloon(self):
        with zipfile.ZipFile(bouw_docx.REFERENTIE) as z:
            namen = z.namelist()
            thema = z.read("word/theme/theme1.xml").decode("utf-8")
            stijlen = z.read("word/styles.xml").decode("utf-8")
        self.assertTrue(any("media" in n for n in namen),
                        "het logo van de omslag ontbreekt")
        self.assertIn("word/numbering.xml", namen,
                      "zonder de nummering telt Word de koppen niet")
        self.assertIn("Kop1", stijlen, "dit is het Npuls-sjabloon niet")
        self.assertIn(bouw_ref.ORANJE, thema)
        self.assertIn(bouw_ref.LETTER, thema)

    def test_de_stijlen_die_pandoc_zoekt_zijn_toegevoegd(self):
        with zipfile.ZipFile(bouw_docx.REFERENTIE) as z:
            stijlen = z.read("word/styles.xml").decode("utf-8")
        for sid in ("Table", "BodyText", "BlockText", "Hyperlink", "Compact"):
            with self.subTest(sid):
                self.assertIn(f'w:styleId="{sid}"', stijlen)
        self.assertIn(bouw_ref.BLAUW, stijlen)
        self.assertIn(bouw_ref.GRIJS, stijlen)
        self.assertIn("nl-NL", stijlen)

    def test_de_titel_staat_onder_het_logo(self):
        with zipfile.ZipFile(bouw_docx.REFERENTIE) as z:
            stijlen = z.read("word/styles.xml").decode("utf-8")
        titel = re.search(r'<w:style [^>]*w:styleId="Titel".*?</w:style>',
                          stijlen, re.S).group(0)
        self.assertIn('w:before="2400"', titel,
                      "zonder ruimte loopt de titel door het logo")

    def test_de_voettekst_draagt_de_titel_van_het_sjabloon(self):
        for naam, bestand in bouw_docx.SJABLONEN.items():
            with zipfile.ZipFile(MAP / bestand) as z:
                voet = b"".join(z.read(n) for n in z.namelist()
                                if n.startswith("word/footer"))
            with self.subTest(naam):
                self.assertNotIn(b"[titel]", voet,
                                 "de plaatshouder van het Npuls-sjabloon staat "
                                 "er nog in")

    def test_de_referentie_is_opnieuw_te_bouwen(self):
        with tempfile.TemporaryDirectory() as tmp:
            uit = pathlib.Path(tmp) / "ref.docx"
            bouw_ref.bouw(uit)
            for deel in ("word/theme/theme1.xml", "word/styles.xml"):
                with self.subTest(deel), zipfile.ZipFile(uit) as nieuw, \
                        zipfile.ZipFile(bouw_docx.REFERENTIE) as oud:
                    self.assertEqual(nieuw.read(deel), oud.read(deel))


if __name__ == "__main__":
    unittest.main()
