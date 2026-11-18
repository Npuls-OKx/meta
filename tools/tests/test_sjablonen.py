"""Testgevallen bij de sjablonen voor de adviesgroep (#554).

De poort bewaakt drie dingen. Het skelet is uit zijn uitwerking afgeleid en
draagt elke kop daarvan, zodat een sjabloon niet kleiner is dan het document
dat het nadoet. Het draagt de vaste aanwijzingen die een invuller nodig heeft.
En de .docx die in versiebeheer staat hoort bij het skelet, zodat de
adviesgroep nooit een sjabloon opent dat achterloopt op de bron.
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
KOP = re.compile(r"^#{1,6} ", re.M)


def document_xml(pad: pathlib.Path) -> bytes:
    """De inhoud van de .docx, zonder de zip-tijdstempels die per bouw wisselen."""
    with zipfile.ZipFile(pad) as z:
        return z.read("word/document.xml")


def skelet(naam: str) -> str:
    return (SKELET / f"{naam}.md").read_text(encoding="utf-8")


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
                              gevolgd, "de adviesgroep moet dit bestand kunnen "
                              "openen zonder iets te bouwen")

    def test_controleer_meldt_een_ontbrekend_sjabloon(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(
                bouw_docx.bouw(pathlib.Path(tmp), bouw_docx.REFERENTIE,
                               controleer=True), 1)


class HetSkeletDraagtZijnUitwerking(unittest.TestCase):
    def test_elke_kop_van_de_bron_staat_erin(self):
        """Een sjabloon dat koppen weglaat, laat de invuller hoofdstukken missen."""
        for naam, cfg in CONFIG.items():
            with self.subTest(naam):
                bron = maak.Sjabloon(naam, cfg).brontekst()
                self.assertGreaterEqual(
                    len(KOP.findall(skelet(naam))), len(KOP.findall(bron)),
                    f"{naam} draagt minder koppen dan {cfg['bron']}")

    def test_opnieuw_afleiden_geeft_hetzelfde_skelet(self):
        for naam, cfg in CONFIG.items():
            with self.subTest(naam):
                self.assertEqual(
                    maak.Sjabloon(naam, cfg).maak(), skelet(naam),
                    f"gegenereerd/{naam}.md loopt achter op {cfg['bron']}; "
                    "genereer opnieuw met maak-sjabloon-uit-document.py")

    def test_geen_relatieve_verwijzing(self):
        """Een Word-bestand staat niet in de repository."""
        for naam in CONFIG:
            with self.subTest(naam):
                los = [d for d in re.findall(r"\]\(([^)]+)\)", skelet(naam))
                       if not d.startswith(("http://", "https://", "#"))]
                self.assertEqual(los, [], f"{naam} draagt een pad dat in Word "
                                          "nergens heen wijst")

    def test_elke_tabel_heeft_een_kopregel(self):
        for naam in CONFIG:
            for nr, regel in enumerate(skelet(naam).splitlines(), 1):
                if regel.startswith("|") and not regel.replace("|", "").strip():
                    if re.match(r"^\|[\s:|-]+\|\s*$", regel):
                        continue  # de scheidingsregel is geen kopregel
                    vorige = skelet(naam).splitlines()[nr - 2]
                    if not vorige.startswith("|"):
                        self.fail(f"{naam}.md regel {nr}: een lege kopregel "
                                  "wordt in Word een lege rij")


class HetSkeletDraagtDeAanwijzingen(unittest.TestCase):
    def test_de_aggregatiestap_staat_erin(self):
        for naam in CONFIG:
            with self.subTest(naam):
                t = skelet(naam)
                self.assertIn("## De grootst gemene deler", t)
                self.assertIn("niet voor de sector", t)
                self.assertIn("## Afwijkingen per instelling", t)

    def test_de_invultabel_staat_erin(self):
        for naam in CONFIG:
            with self.subTest(naam):
                t = skelet(naam)
                self.assertIn("## Invullen", t)
                for veld in ("Wat dit wordt", "Wie dit invult",
                             "Voorbeelduitwerking", "Inleveren"):
                    self.assertIn(veld, t)

    def test_de_koppen_blijven_staan(self):
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertIn("lezer (parser)", skelet(naam))

    def test_elk_skelet_verwijst_naar_zijn_uitwerking(self):
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertIn("https://github.com/Npuls-OKx/meta/blob/",
                              skelet(naam))

    def test_elk_skelet_biedt_schrijfruimte(self):
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertIn(maak.RUIMTE, skelet(naam),
                              "zonder schrijfruimte is het geen invulsjabloon")

    def test_een_vraagsectie_sluit_elk_skelet_af(self):
        for naam in CONFIG:
            with self.subTest(naam):
                self.assertIn("## Vragen aan OKx", skelet(naam))


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

    def test_een_verwijzing_blijft_heel_bij_het_vervangen(self):
        """De naam in een linkdoel is geen inhoud en mag niet wijzigen."""
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
    def test_de_npuls_kleuren_en_de_letter(self):
        with zipfile.ZipFile(bouw_docx.REFERENTIE) as z:
            thema = z.read("word/theme/theme1.xml").decode("utf-8")
            stijlen = z.read("word/styles.xml").decode("utf-8")
        self.assertIn(bouw_ref.ORANJE, thema)
        self.assertIn(bouw_ref.ORANJE, stijlen, "een lezer die het thema niet "
                      "oplost ziet dan de standaardkleur")
        self.assertIn(bouw_ref.LETTER, thema)
        self.assertIn(bouw_ref.BLAUW, stijlen)
        self.assertIn(bouw_ref.GRIJS, stijlen, "een invultabel zonder randen "
                      "is niet te gebruiken")
        self.assertIn("nl-NL", stijlen)

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
