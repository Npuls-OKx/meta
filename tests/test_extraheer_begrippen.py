"""Testgevallen voor scripts/extraheer-begrippen.py.

Het testcorpus wordt per geval opgebouwd, zodat de verwachte aantallen uit de
invoer volgen en niet uit de inhoud van de repository.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "extraheer_begrippen", WORTEL / "scripts/extraheer-begrippen.py")
eb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eb)


class Corpus:
    """Een tijdelijk corpus met twee repositories."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.wortel = Path(self.tmp.name)
        for naam in ("meta", "public"):
            (self.wortel / naam).mkdir()

    def bestand(self, pad, tekst):
        p = self.wortel / pad
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(tekst, encoding="utf-8")
        return self

    @property
    def repos(self):
        return {"meta": self.wortel / "meta", "public": self.wortel / "public"}

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.tmp.cleanup()


def termen_van(resultaat):
    return {t["sleutel"]: t for t in resultaat[0]}


class ExtractieTest(unittest.TestCase):
    def test_given_afgebakend_codeblok_when_extraheren_then_inhoud_telt_niet_mee(self):
        with Corpus() as c:
            c.bestand("meta/a.md", "Tekst met `Buitenblok`.\n\n```\nregel met `Binnenblok`\n```\n")
            t = termen_van(eb.extraheer(c.repos))
        self.assertIn("buitenblok", t)
        self.assertNotIn("binnenblok", t)

    def test_given_tilde_codeblok_when_extraheren_then_inhoud_telt_niet_mee(self):
        with Corpus() as c:
            c.bestand("meta/a.md", "~~~\n`TildeTerm`\n~~~\n")
            t = termen_van(eb.extraheer(c.repos))
        self.assertNotIn("tildeterm", t)

    def test_given_html_commentaar_when_extraheren_then_inhoud_telt_niet_mee(self):
        with Corpus() as c:
            c.bestand("meta/a.md", "<!-- `Commentaarterm` -->\nGewone `Zichtbareterm`.\n")
            t = termen_van(eb.extraheer(c.repos))
        self.assertNotIn("commentaarterm", t)
        self.assertIn("zichtbareterm", t)

    def test_given_node_modules_when_extraheren_then_map_wordt_overgeslagen(self):
        with Corpus() as c:
            c.bestand("meta/node_modules/a.md", "`Genegeerdeterm`\n")
            c.bestand("meta/b.md", "`Meegenomenterm`\n")
            termen, bestanden, _ = eb.extraheer(c.repos)
        self.assertEqual(bestanden, 1)
        self.assertNotIn("genegeerdeterm", termen_van((termen,)))

    def test_given_uitgesloten_pad_when_extraheren_then_eigen_map_telt_niet_mee(self):
        """De begrippenlijst mag zichzelf niet bewijzen."""
        with Corpus() as c:
            c.bestand("meta/eigen/map/lijst.md", "`Zelfbewijs`\n")
            c.bestand("meta/b.md", "`Elders`\n")
            t = termen_van(eb.extraheer(c.repos, uitgesloten_paden=("eigen/map",)))
        self.assertNotIn("zelfbewijs", t)
        self.assertIn("elders", t)

    def test_given_drie_schrijfwijzen_when_extraheren_then_een_sleutel_met_totaal(self):
        with Corpus() as c:
            c.bestand("meta/a.md", "`Onderwijseenheid-specificatie` en `Onderwijseenheid specificatie`\n")
            c.bestand("public/b.md", "`onderwijseenheidspecificatie`\n")
            t = termen_van(eb.extraheer(c.repos))
        self.assertIn("onderwijseenheidspecificatie", t)
        self.assertEqual(t["onderwijseenheidspecificatie"]["aantal"], 3)
        self.assertEqual(len(t["onderwijseenheidspecificatie"]["schrijfwijzen"]), 3)

    def test_given_meer_voorkomens_dan_de_cap_when_extraheren_then_vindplaatsen_afgekapt(self):
        with Corpus() as c:
            c.bestand("meta/a.md", "\n".join(["`Herhaling`"] * 5) + "\n")
            termen, _, weggelaten = eb.extraheer(c.repos, max_vindplaatsen=2)
            sw = termen_van((termen,))["herhaling"]["schrijfwijzen"][0]
        self.assertEqual(sw["aantal"], 5)
        self.assertEqual(len(sw["vindplaatsen"]), 2)
        self.assertEqual(weggelaten, 3)

    def test_given_leeg_corpus_when_extraheren_then_geen_termen(self):
        with Corpus() as c:
            termen, bestanden, _ = eb.extraheer(c.repos)
        self.assertEqual((termen, bestanden), ([], 0))

    def test_given_ontbrekende_repository_when_extraheren_then_geen_uitzondering(self):
        with Corpus() as c:
            repos = dict(c.repos, afwezig=c.wortel / "bestaat-niet")
            c.bestand("meta/a.md", "`Term`\n")
            termen, bestanden, _ = eb.extraheer(repos)
        self.assertEqual(bestanden, 1)


class IndelingTest(unittest.TestCase):
    def test_given_oeapi_schema_when_classificeren_then_oeapi_schema(self):
        self.assertEqual(eb.classificeer("LearningOutcome", {"LearningOutcome"}, set()), "oeapi-schema")

    def test_given_camelcase_when_classificeren_then_veldnaam(self):
        self.assertEqual(eb.classificeer("hierarchyLevel"), "veldnaam")

    def test_given_cardinaliteit_when_classificeren_then_expressie(self):
        self.assertEqual(eb.classificeer("Kerntaak (1..*) Werkproces"), "expressie")

    def test_given_pad_when_classificeren_then_pad(self):
        self.assertEqual(eb.classificeer("architecture/model/README.md"), "pad")

    def test_given_commando_when_classificeren_then_commando(self):
        self.assertEqual(eb.classificeer("python3 scripts/validate-docs.py"), "commando")

    def test_given_nederlands_begrip_when_classificeren_then_kandidaat_begrip(self):
        self.assertEqual(eb.classificeer("Onderwijseenheid specificatie"), "kandidaat-begrip")

    def test_given_koppelteken_en_spatie_when_normaliseren_then_dezelfde_sleutel(self):
        self.assertEqual(eb.normaliseer("Onderwijseenheid-specificatie"),
                         eb.normaliseer("Onderwijseenheid specificatie"))


if __name__ == "__main__":
    unittest.main()
