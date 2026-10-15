"""Testgevallen voor scripts/controleer-interactiespec-vorm.py.

Elk geval bouwt zijn eigen map met een hoofddocument en waar nodig een verdieping, zodat de
verwachting uit het fixture volgt en elk negatief geval precies een maat breekt. Het laatste
geval draait de controle op de interactiespecificatie in deze repository.
"""

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
SPECIFICATIE = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod"

spec = importlib.util.spec_from_file_location(
    "controleer_vorm", WORTEL / "scripts/controleer-interactiespec-vorm.py"
)
cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv)

TABEL = "| Wat | Waar |\n|---|---|\n| een rij | hier |"
BEELD = "![Een beeld dat iets toont](../img/regels/f1-01-iets.svg)"
LEESREGEL = "Links staat de ontwerper, rechts de catalogus. De pijl ertussen draagt de levering."


def maak(map_, hoofd, verdieping=None):
    """Een map met een hoofddocument, en een verdieping zodra een geval die vraagt."""
    map_ = Path(map_)
    (map_ / "README.md").write_text(hoofd, encoding="utf-8")
    if verdieping is not None:
        (map_ / "stroom-is-oa-01.md").write_text(verdieping, encoding="utf-8")
    return map_


def waarover(bevindingen):
    """De bevindingen als tekst, zodat een geval op een woord kan toetsen."""
    return " | ".join(str(b) for b in bevindingen)


class DeKopOpent(unittest.TestCase):
    """Een kop opent met een beeld, een tabel of een diagram, en niet met een alinea."""

    def test_given_een_kop_die_met_een_tabel_opent_when_toetsen_then_blijft_het_zonder_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\n## Een deel\n\n{TABEL}\n")
            verslagen = cv.controleer(map_)
            self.assertEqual(waarover(verslagen[0]["bevindingen"]), "")

    def test_given_een_kop_die_met_een_alinea_opent_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\n## Een deel\n\nEen alinea vooraan.\n")
            verslagen = cv.controleer(map_)
            self.assertEqual(len(verslagen[0]["bevindingen"]), 1)
            self.assertIn("opent met een alinea", waarover(verslagen[0]["bevindingen"]))

    def test_given_een_kop_die_met_een_diagram_opent_when_toetsen_then_blijft_het_zonder_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, "# Een snede\n\n```mermaid\nflowchart LR\n  A --> B\n```\n")
            self.assertEqual(cv.controleer(map_)[0]["bevindingen"], [])

    def test_given_een_verdieping_die_met_een_alinea_opent_when_toetsen_then_blijft_het_zonder_bevinding(self):
        """Een berichtsectie in een verdieping opent terecht met de regel die haar schema aanwijst."""
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n",
                        verdieping="# IS-OA-01\n\nEen alinea vooraan.\n\n## Berichten\n\nSchema x.\n")
            verdieping = [v for v in cv.controleer(map_) if not v["hoofddocument"]][0]
            self.assertEqual(verdieping["bevindingen"], [])


class HetBeeldInHetVerhaal(unittest.TestCase):
    """Een beeldregel uit de voorbeelduitwerking staat als beeld, ook in een verdieping."""

    def test_given_een_beeldregel_als_link_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\nZie [F1-12](../img/regels/f1-12-iets.svg).\n")
            self.assertIn("staat als link", waarover(cv.controleer(map_)[0]["bevindingen"]))

    def test_given_een_beeldregel_als_link_in_een_verdieping_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n",
                        verdieping="# IS-OA-01\n\nZie [F1-12](../img/regels/f1-12-iets.svg).\n")
            verdieping = [v for v in cv.controleer(map_) if not v["hoofddocument"]][0]
            self.assertEqual(len(verdieping["bevindingen"]), 1)

    def test_given_een_uitsnede_van_de_hoofdplaat_als_link_when_toetsen_then_blijft_het_zonder_bevinding(self):
        """Een plaatuitsnede wijst naar een grotere plaat en toont niet wat deze stap oplevert."""
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\nZie [fase 1](../img/hoofdplaat/f1.svg).\n")
            self.assertEqual(cv.controleer(map_)[0]["bevindingen"], [])


class DeLeesregel(unittest.TestCase):
    """Elk beeld in het hoofddocument draagt een leesregel van hoogstens twee zinnen."""

    def test_given_een_beeld_met_twee_zinnen_eronder_when_toetsen_then_blijft_het_zonder_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{BEELD}\n\n{LEESREGEL}\n")
            self.assertEqual(cv.controleer(map_)[0]["bevindingen"], [])

    def test_given_een_beeld_met_drie_zinnen_eronder_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{BEELD}\n\n{LEESREGEL} En nog een derde zin erbij.\n")
            self.assertIn("draagt 3 zinnen", waarover(cv.controleer(map_)[0]["bevindingen"]))

    def test_given_een_beeld_zonder_leesregel_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{BEELD}\n\n{TABEL}\n")
            self.assertIn("geen leesregel", waarover(cv.controleer(map_)[0]["bevindingen"]))

    def test_given_een_versienummer_in_de_leesregel_when_toetsen_then_telt_het_niet_als_zinseinde(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{BEELD}\n\nDe plaat staat op v1.7 en toont de keten. "
                             f"De pijlen dragen de lading.\n")
            self.assertEqual(cv.controleer(map_)[0]["bevindingen"], [])


class DeMaatVanDeTekst(unittest.TestCase):
    """De alinea en het hoofddocument blijven binnen hun maat."""

    def test_given_een_alinea_binnen_de_maat_when_toetsen_then_blijft_het_zonder_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\n{'woord ' * 70}\n")
            self.assertEqual(cv.controleer(map_)[0]["bevindingen"], [])

    def test_given_een_alinea_boven_de_maat_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\n{'woord ' * 80}\n")
            self.assertIn("draagt 80 woorden", waarover(cv.controleer(map_)[0]["bevindingen"]))

    def test_given_een_hoofddocument_boven_de_maat_when_toetsen_then_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            alineas = "\n\n".join("woord " * 70 for _ in range(11))
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n\n{alineas}\n")
            self.assertIn("buiten de tabellen", waarover(cv.controleer(map_)[0]["bevindingen"]))

    def test_given_een_verdieping_boven_de_maat_when_toetsen_then_blijft_het_zonder_bevinding(self):
        """Een verdieping draagt de details, en daar hoort de tekst volledig te zijn."""
        with tempfile.TemporaryDirectory() as tmp:
            alineas = "\n\n".join("woord " * 80 for _ in range(11))
            map_ = maak(tmp, f"# Een snede\n\n{TABEL}\n", verdieping=f"# IS-OA-01\n\n{alineas}\n")
            verdieping = [v for v in cv.controleer(map_) if not v["hoofddocument"]][0]
            self.assertEqual(verdieping["bevindingen"], [])


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return cv.main(argv)

    def test_given_een_document_dat_elke_maat_haalt_when_draaien_then_exitcode_nul(self):
        with tempfile.TemporaryDirectory() as tmp:
            maak(tmp, f"# Een snede\n\n{TABEL}\n")
            self.assertEqual(self.draai([tmp, "--kort"]), 0)

    def test_given_een_maat_die_niet_gehaald_wordt_when_draaien_then_exitcode_een(self):
        with tempfile.TemporaryDirectory() as tmp:
            maak(tmp, "# Een snede\n\nEen alinea vooraan.\n")
            self.assertEqual(self.draai([tmp, "--kort"]), 1)

    def test_given_een_map_die_niet_bestaat_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai([str(Path(tmp) / "bestaat-niet"), "--kort"]), 2)

    def test_given_een_map_zonder_markdown_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai([tmp, "--kort"]), 2)


class InDezeRepository(unittest.TestCase):

    def test_given_de_interactiespecificatie_in_deze_repository_when_toetsen_then_elke_maat_gehaald(self):
        verslagen = cv.controleer(SPECIFICATIE)
        self.assertTrue(verslagen, "de specificatie draagt geen markdown-bestand")
        bevindingen = [str(b) for v in verslagen for b in v["bevindingen"]]
        self.assertEqual(bevindingen, [])

    def test_given_het_hoofddocument_when_toetsen_then_draagt_het_acht_beelden(self):
        hoofd = [v for v in cv.controleer(SPECIFICATIE) if v["hoofddocument"]][0]
        self.assertGreaterEqual(hoofd["beelden"], 8)
        self.assertLessEqual(hoofd["buiten_tabellen"], cv.MAX_WOORDEN_BUITEN_TABELLEN)


if __name__ == "__main__":
    unittest.main()
