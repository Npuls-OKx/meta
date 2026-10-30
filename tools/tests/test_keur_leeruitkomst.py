"""Testgevallen voor scripts/keur-leeruitkomst.py.

Elke verwachting volgt uit de vier machinaal toetsbare vragen uit de checklist van de
Handleiding Formuleren leeruitkomsten (NCP NLQF, december 2020).
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("keur_leeruitkomst", WORTEL / "scripts/keur-leeruitkomst.py")
kl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kl)

GOED = ("Stelt mechanische apparatuur af aan de hand van technische specificaties, "
        "in een mechanische productieomgeving")


def codes(zin, taxonomie=None):
    return {b.code for b in kl.keur(zin, taxonomie)}


def blokkerend(zin, taxonomie=None):
    return {b.code for b in kl.keur(zin, taxonomie) if b.blokkeert}


class DeVijfPlekken(unittest.TestCase):

    def test_given_a_complete_outcome_when_checked_then_only_the_taxonomy_is_missing(self):
        self.assertEqual(codes(GOED), {"TAXONOMIE"})

    def test_given_an_outcome_without_a_standard_when_checked_then_reported(self):
        zin = "Stelt mechanische apparatuur af in een mechanische productieomgeving"
        self.assertIn("STANDAARD", codes(zin))

    def test_given_an_outcome_without_a_context_when_checked_then_reported(self):
        zin = "Stelt mechanische apparatuur af aan de hand van technische specificaties"
        self.assertIn("CONTEXT", codes(zin))

    def test_given_each_signal_word_for_a_standard_when_checked_then_accepted(self):
        for woord in ("volgens het protocol", "aan de hand van specificaties",
                      "toetsbaar aan de normen", "op basis van de richtlijn"):
            with self.subTest(woord=woord):
                self.assertNotIn("STANDAARD", codes(f"Stelt apparatuur af {woord}, in een werkplaats"))


class EenHandelingPerLeeruitkomst(unittest.TestCase):

    def test_given_two_active_verbs_when_checked_then_reported(self):
        zin = ("Analyseert de situatie van een tuin, volgens de normen voor groenaanleg, "
               "en verwerkt de verbeteringen in een ontwerp, in een particuliere tuin")
        self.assertIn("WERKWOORDEN", codes(zin))

    def test_given_a_noun_ending_in_en_when_checked_then_not_mistaken_for_a_verb(self):
        # arbeidsomstandigheden is geen tweede handeling
        zin = ("Draagt bij aan kwaliteitszorg en arbeidsomstandigheden, volgens de "
               "RI&E-systematiek, op de eigen werkplek")
        self.assertNotIn("WERKWOORDEN", codes(zin))

    def test_given_an_article_after_en_when_checked_then_not_mistaken_for_a_verb(self):
        zin = ("Levert een bijdrage, toetsbaar aan de normen en het kwaliteitshandboek, "
               "in de eigen apotheek")
        self.assertNotIn("WERKWOORDEN", codes(zin))


class TaxonomieBijHetNiveau(unittest.TestCase):

    def test_given_no_taxonomy_when_checked_then_reported(self):
        self.assertIn("TAXONOMIE", codes(GOED))

    def test_given_romiszowski_at_mbo_level_when_checked_then_accepted(self):
        zin = GOED + " (operator productietechniek NLQF 2)"
        self.assertNotIn("TAXONOMIE", codes(zin, "Rpm"))

    def test_given_solo_at_higher_education_level_when_checked_then_accepted(self):
        zin = GOED + " (hbo-bachelor NLQF 6)"
        self.assertNotIn("TAXONOMIE", codes(zin, "solo4"))

    def test_given_solo_at_mbo_level_when_checked_then_an_advice_that_does_not_block(self):
        zin = GOED + " (operator productietechniek NLQF 2)"
        self.assertIn("TAXONOMIE", codes(zin, "solo4"))
        self.assertNotIn("TAXONOMIE", blokkerend(zin, "solo4"))

    def test_given_romiszowski_at_higher_education_level_when_checked_then_an_advice_that_does_not_block(self):
        zin = GOED + " (hbo-bachelor NLQF 6)"
        self.assertIn("TAXONOMIE", codes(zin, "Rpm"))
        self.assertNotIn("TAXONOMIE", blokkerend(zin, "Rpm"))

    def test_given_an_unknown_taxonomy_when_checked_then_an_advice_that_does_not_block(self):
        zin = GOED + " (operator productietechniek NLQF 2)"
        self.assertNotIn("TAXONOMIE", blokkerend(zin, "bloom3"))

    def test_given_no_taxonomy_when_checked_then_it_blocks(self):
        self.assertIn("TAXONOMIE", blokkerend(GOED))

    def test_given_a_level_written_as_niveau_when_read_then_found(self):
        self.assertEqual(kl.niveau_van("iets (NLQF niveau 2), technische module"), 2)

    def test_given_no_level_when_read_then_none(self):
        self.assertIsNone(kl.niveau_van(GOED))


class UitEenRegeltabel(unittest.TestCase):

    def test_given_a_rule_table_when_read_then_only_outcomes_once_each(self):
        model = {"regels": [
            {"objecttype": "Leeruitkomst", "soort": "ontstaat", "instantie": GOED},
            {"objecttype": "Leeruitkomst", "soort": "ontstaat", "instantie": GOED},
            {"objecttype": "Competentie", "soort": "ontstaat", "instantie": "iets anders"},
            {"objecttype": "Leeruitkomst", "soort": "ontstaat", "taxonomie": "Rc",
             "instantie": "Voert uit volgens protocol, in de apotheek"},
        ]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(model, f)
            pad = f.name
        stel = kl.leeruitkomsten_uit(pad)
        self.assertEqual(len(stel), 2)
        self.assertEqual(stel[1][1], "Rc")


if __name__ == "__main__":
    unittest.main()


class AlleenWatOntstaat(unittest.TestCase):
    """Een leeruitkomst die stroomt is lading, geen formulering."""

    def tabel(self, *regels):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump({"regels": list(regels)}, f)
            return f.name

    def test_given_an_outcome_that_flows_when_read_then_it_is_not_checked(self):
        pad = self.tabel({"objecttype": "Leeruitkomst", "soort": "stroomt",
                          "instantie": "Al behaald door Jochem: geen, hij start zonder vrijstellingen"})
        self.assertEqual(kl.leeruitkomsten_uit(pad), [])

    def test_given_an_outcome_that_is_formulated_when_read_then_it_is_checked(self):
        pad = self.tabel({"objecttype": "Leeruitkomst", "soort": "ontstaat", "instantie": GOED})
        self.assertEqual(len(kl.leeruitkomsten_uit(pad)), 1)
