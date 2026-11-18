"""Testgevallen bij de sjablonen voor de adviesgroep (#554).

De poort bewaakt twee dingen. Het sjabloon draagt wat een invuller nodig heeft:
de aggregatiestap, de invultabel, de aanwijzing over de koppen en een
voorbeelduitwerking. En de .docx die in versiebeheer staat hoort bij het skelet
ernaast, zodat de adviesgroep nooit een sjabloon opent dat achterloopt.
"""

import pathlib
import subprocess
import sys
import tempfile
import unittest
import zipfile

WORTEL = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WORTEL / "tools/scripts"))

import importlib

bouw_docx = importlib.import_module("bouw-sjablonen-docx")
bouw_ref = importlib.import_module("bouw-sjabloon-referentie")

MAP = WORTEL / "architecture/docs/sjablonen"
BRON = MAP / "bron"


def document_xml(pad: pathlib.Path) -> bytes:
    """De inhoud van de .docx, zonder de zip-tijdstempels die per bouw wisselen."""
    with zipfile.ZipFile(pad) as z:
        return z.read("word/document.xml")


class ElkSjabloonBestaat(unittest.TestCase):
    def test_vijf_skeletten(self):
        self.assertEqual(len(bouw_docx.SJABLONEN), 5)
        for naam in bouw_docx.SJABLONEN:
            with self.subTest(naam):
                self.assertTrue((BRON / f"{naam}.md").exists(),
                                f"het skelet {naam}.md ontbreekt")

    def test_elke_docx_staat_in_versiebeheer(self):
        gevolgd = subprocess.run(
            ["git", "ls-files", "architecture/docs/sjablonen"],
            cwd=WORTEL, capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        for bestand in bouw_docx.SJABLONEN.values():
            with self.subTest(bestand):
                self.assertIn(f"architecture/docs/sjablonen/{bestand}", gevolgd,
                              "de adviesgroep moet dit bestand kunnen openen "
                              "zonder iets te bouwen")

    def test_controleer_meldt_een_ontbrekend_sjabloon(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(
                bouw_docx.bouw(pathlib.Path(tmp), bouw_docx.REFERENTIE,
                               controleer=True), 1)


class HetSkeletDraagtDeAanwijzingen(unittest.TestCase):
    def setUp(self):
        self.skeletten = {n: (BRON / f"{n}.md").read_text(encoding="utf-8")
                          for n in bouw_docx.SJABLONEN}

    def test_de_aggregatiestap_staat_erin(self):
        for naam, tekst in self.skeletten.items():
            with self.subTest(naam):
                self.assertIn("## De grootst gemene deler", tekst)
                self.assertIn("niet voor de sector", tekst,
                              "de waarschuwing dat een instelling voor haar "
                              "eigen praktijk spreekt ontbreekt")
                self.assertIn("## Afwijkingen per instelling", tekst)

    def test_de_invultabel_staat_erin(self):
        for naam, tekst in self.skeletten.items():
            with self.subTest(naam):
                self.assertIn("## Invullen", tekst)
                for veld in ("Wat dit wordt", "Wie dit invult",
                             "Voorbeelduitwerking", "Inleveren"):
                    self.assertIn(veld, tekst, f"het veld {veld} ontbreekt")

    def test_de_koppen_blijven_staan(self):
        for naam, tekst in self.skeletten.items():
            with self.subTest(naam):
                self.assertIn("lezer (parser)", tekst,
                              "de aanwijzing dat de koppen blijven staan "
                              "ontbreekt")

    def test_elk_skelet_verwijst_naar_een_voorbeeld(self):
        for naam, tekst in self.skeletten.items():
            with self.subTest(naam):
                self.assertIn("https://github.com/Npuls-OKx/meta/blob/", tekst,
                              "een volledige verwijzing is nodig, want een "
                              "relatief pad werkt niet in een Word-bestand")

    def test_elke_tabel_heeft_een_kopregel(self):
        for naam, tekst in self.skeletten.items():
            for nr, regel in enumerate(tekst.splitlines(), 1):
                kaal = regel.replace("|", "").strip()
                if regel.startswith("|") and not kaal:
                    self.fail(f"{naam}.md regel {nr}: een lege kopregel wordt "
                              f"in Word een lege rij; geef de tabel een kop")

    def test_een_vraagsectie_sluit_elk_skelet_af(self):
        for naam, tekst in self.skeletten.items():
            with self.subTest(naam):
                self.assertIn("## Vragen aan OKx", tekst)


class DeDocxHoortBijHetSkelet(unittest.TestCase):
    def test_opnieuw_bouwen_geeft_hetzelfde_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            bouw_docx.bouw(tmp, bouw_docx.REFERENTIE)
            for naam, bestand in bouw_docx.SJABLONEN.items():
                with self.subTest(naam):
                    self.assertEqual(
                        document_xml(MAP / bestand), document_xml(tmp / bestand),
                        f"{bestand} loopt achter op bron/{naam}.md; bouw opnieuw "
                        "met tools/scripts/bouw-sjablonen-docx.py")

    def test_zonder_referentie_weigert_het_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            with self.assertRaises(SystemExit) as e:
                bouw_docx.bouw(tmp, tmp / "bestaat-niet.docx")
            self.assertIn("ontbreekt", str(e.exception))
            self.assertEqual(list(tmp.iterdir()), [],
                             "een weigering schrijft niets")


class DeReferentieDraagtDeHuisstijl(unittest.TestCase):
    def test_de_npuls_kleuren_en_de_letter(self):
        with zipfile.ZipFile(bouw_docx.REFERENTIE) as z:
            thema = z.read("word/theme/theme1.xml").decode("utf-8")
            stijlen = z.read("word/styles.xml").decode("utf-8")
        self.assertIn(bouw_ref.ORANJE, thema, "de koppen staan niet in het "
                      "primaire accent van Npuls")
        self.assertIn(bouw_ref.LETTER, thema)
        self.assertIn(bouw_ref.BLAUW, stijlen, "links staan niet in Npuls-blauw")
        self.assertIn("nl-NL", stijlen, "Word onderstreept dan elk woord")

    def test_de_referentie_is_opnieuw_te_bouwen(self):
        with tempfile.TemporaryDirectory() as tmp:
            uit = pathlib.Path(tmp) / "ref.docx"
            bouw_ref.bouw(uit)
            for deel in ("word/theme/theme1.xml", "word/styles.xml"):
                with self.subTest(deel), zipfile.ZipFile(uit) as nieuw, \
                        zipfile.ZipFile(bouw_docx.REFERENTIE) as oud:
                    self.assertEqual(nieuw.read(deel), oud.read(deel),
                                     "de referentie in versiebeheer wijkt af "
                                     "van wat het script nu bouwt")


if __name__ == "__main__":
    unittest.main()
