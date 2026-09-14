"""Testgevallen voor scripts/publiceer-informatiemodel.py, given-when-then."""

import importlib.util
import json
import sys
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publiceer", WORTEL / "scripts" / "publiceer-informatiemodel.py")
publiceer = importlib.util.module_from_spec(spec)
sys.modules["publiceer"] = publiceer
spec.loader.exec_module(publiceer)

COMMIT = "abc123def456"


class Verwijzingen(unittest.TestCase):
    def herschrijf(self, tekst, pakket=None, fouten=None):
        fouten = [] if fouten is None else fouten
        return publiceer.herschrijf(tekst, COMMIT, pakket or Path("/nergens"), fouten, "test.md"), fouten

    def test_given_link_naar_begrippenlijst_in_meta_when_herschreven_then_relatief_in_pakket(self):
        uit, fouten = self.herschrijf("zie [lijst](../../docs/specificatie/begrippen/begrippenlijst.md#dekking)")
        self.assertEqual(uit, "zie [lijst](begrippen.md#dekking)")
        self.assertEqual(fouten, [])

    def test_given_link_naar_begrippenkader_when_herschreven_then_ankertabel_met_eigen_anchor(self):
        uit, _ = self.herschrijf("[kader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md#ankertabel)")
        self.assertEqual(uit, f"[kader]({publiceer.ANKERTABEL})")

    def test_given_link_die_in_meta_blijft_when_herschreven_then_gepind_op_commit(self):
        uit, _ = self.herschrijf("[R7](../../docs/specificatie/student-keuze/keuze-requirements.md#r7)")
        self.assertIn(f"/meta/blob/{COMMIT}/architecture/docs/specificatie/student-keuze/keuze-requirements.md#r7", uit)

    def test_given_adr_link_naar_public_dev_when_herschreven_then_relatief(self):
        uit, _ = self.herschrijf("[ADR](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-x.md)")
        self.assertEqual(uit, "[ADR](../Referentiemateriaal/adr/0026-x.md)")

    def test_given_plaat_met_spaties_when_herschreven_then_img_zonder_versie(self):
        uit, _ = self.herschrijf("![plaat](<OKx informatiemodel v0.1.jpg>)")
        self.assertEqual(uit, "![plaat](img/informatiemodel.jpg)")

    def test_given_onbekende_relatieve_link_when_herschreven_then_fout(self):
        _, fouten = self.herschrijf("[x](../ergens/anders.md)")
        self.assertEqual(len(fouten), 1)
        self.assertIn("onbekende verwijzing", fouten[0])

    def test_given_link_naar_okx_repo_zonder_omzetting_when_herschreven_then_fout(self):
        _, fouten = self.herschrijf("[x](https://github.com/Npuls-OKx/meta/blob/dev/README.md)")
        self.assertEqual(len(fouten), 1)
        self.assertIn("zonder omzetting", fouten[0])

    def test_given_externe_link_en_anchor_in_document_when_herschreven_then_ongewijzigd(self):
        tekst = "[MIM](https://docs.geostandaarden.nl/mim/mim/) en [hier](#scope)"
        uit, fouten = self.herschrijf(tekst)
        self.assertEqual(uit, tekst)
        self.assertEqual(fouten, [])

    def test_given_link_naar_bestand_in_pakket_when_herschreven_then_ongewijzigd(self):
        uit, fouten = self.herschrijf("[json](informatiemodel.json)")
        self.assertEqual(uit, "[json](informatiemodel.json)")
        self.assertEqual(fouten, [])


class Brug(unittest.TestCase):
    LGM = "    LEERUITKOMST {\n        uuid id PK\n    }\n    GROEP {\n        uuid id PK\n    }\n"
    MODEL = {"objecttypen": [{"naam": "Leeruitkomst"}, {"naam": "Plaatsingsgroep"}]}

    def brug(self, rijen):
        return ("## Naar het logisch gegevensmodel\n\n| Entiteit (niveau 3) | Objecttype (niveau 2) | Verhouding |\n|---|---|---|\n"
                + "\n".join(rijen) + "\n\n## Verwante documenten\n")

    def test_given_kloppende_brug_when_gecontroleerd_then_geen_fouten(self):
        fouten = []
        publiceer.controleer_brug(self.brug(["| `LEERUITKOMST` | `Leeruitkomst` | Gelijk |", "| `GROEP` | `Plaatsingsgroep` | Gelijk |"]),
                                  self.LGM, self.MODEL, fouten)
        self.assertEqual(fouten, [])

    def test_given_entiteit_die_niet_in_lgm_staat_when_gecontroleerd_then_fout(self):
        fouten = []
        publiceer.controleer_brug(self.brug(["| `LEERUITKOMST` | `Leeruitkomst` | |", "| `GROEP` | `Plaatsingsgroep` | |", "| `ROOSTER` | `Leeruitkomst` | |"]),
                                  self.LGM, self.MODEL, fouten)
        self.assertTrue(any("`ROOSTER`" in f and "niet in logisch-gegevensmodel" in f for f in fouten))

    def test_given_objecttype_dat_niet_in_model_staat_when_gecontroleerd_then_fout(self):
        fouten = []
        publiceer.controleer_brug(self.brug(["| `LEERUITKOMST` | `Leerdoel` | |", "| `GROEP` | `Plaatsingsgroep` | |"]),
                                  self.LGM, self.MODEL, fouten)
        self.assertTrue(any("`Leerdoel`" in f for f in fouten))

    def test_given_entiteit_uit_lgm_ontbreekt_in_brug_when_gecontroleerd_then_fout(self):
        fouten = []
        publiceer.controleer_brug(self.brug(["| `LEERUITKOMST` | `Leeruitkomst` | |"]), self.LGM, self.MODEL, fouten)
        self.assertTrue(any("`GROEP`" in f and "staat niet in de brugtabel" in f for f in fouten))

    def test_given_familie_als_objecttype_when_gecontroleerd_then_toegestaan(self):
        fouten = []
        publiceer.controleer_brug(self.brug(["| `LEERUITKOMST` | De familie `Onderwijsaanbod` | |", "| `GROEP` | `Plaatsingsgroep` | |"]),
                                  self.LGM, self.MODEL, fouten)
        self.assertEqual(fouten, [])


class Vindplaatsen(unittest.TestCase):
    def test_given_definitie_letterlijk_in_kaderscenario_when_gecontroleerd_then_geen_fout(self):
        begrippen = {"begrippen": [{"naam": "Toetsgelegenheid", "definitie": "Het aanbod van een `toetsmoment`.",
                                    "vindplaats": "architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#x"}]}
        fouten = []
        publiceer.controleer_vindplaatsen(begrippen, "| Toetsgelegenheid | Het aanbod van een toetsmoment. |", fouten)
        self.assertEqual(fouten, [])

    def test_given_definitie_niet_in_kaderscenario_when_gecontroleerd_then_fout(self):
        begrippen = {"begrippen": [{"naam": "Toetsgelegenheid", "definitie": "Iets anders.",
                                    "vindplaats": "architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#x"}]}
        fouten = []
        publiceer.controleer_vindplaatsen(begrippen, "| Toetsgelegenheid | Het aanbod van een toetsmoment. |", fouten)
        self.assertEqual(len(fouten), 1)

    def test_given_vindplaats_elders_when_gecontroleerd_then_overgeslagen(self):
        begrippen = {"begrippen": [{"naam": "X", "definitie": "Iets.", "vindplaats": "architecture/model/informatiemodel/informatiemodel.md#y"}]}
        fouten = []
        publiceer.controleer_vindplaatsen(begrippen, "", fouten)
        self.assertEqual(fouten, [])


class Tabel(unittest.TestCase):
    def test_given_bronbestanden_in_tabel_when_gecontroleerd_then_bestaan_ze(self):
        for bron in list(publiceer.DOCUMENTEN) + list(publiceer.BESTANDEN):
            self.assertTrue(bron.exists(), bron)

    def test_given_verwijzingstabel_when_gelezen_then_meta_doelen_dragen_commit_plaatshouder(self):
        for doel in publiceer.VERWIJZINGEN.values():
            if "github.com/Npuls-OKx/meta/" in doel:
                self.assertIn("{commit}", doel)


if __name__ == "__main__":
    unittest.main()
