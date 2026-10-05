"""Testgevallen voor scripts/teken-sectorketen.py.

De plaat draagt haar boodschap in twee kenmerken, de aard en het detailniveau, en zij
beschrijft zonder te oordelen. Wat hier wordt bewaakt is dat die kenmerken op het beeld
terechtkomen, dat een naam nooit stilletjes wordt afgekapt, dat een jaartal nooit over
een andere tekst valt, en dat de plaat door de leesbaarheidspoort komt.
"""

import importlib.util
import json
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent


def laad(naam, bestand):
    spec = importlib.util.spec_from_file_location(naam, WORTEL / bestand)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


teken = laad("sectorketen", "scripts/teken-sectorketen.py")
keur = laad("keur", "scripts/keur-plaat.py")
BRON = json.loads((WORTEL / "doc/sectorketen-producten.json").read_text(encoding="utf-8"))


class BreekTests(unittest.TestCase):
    """Een afgebroken naam valt pas op als iemand de plaat voorleest, dus hij mag niet ontstaan."""

    def test_een_woord_dat_te_breed_is_valt_af(self):
        self.assertIsNone(teken.breek("Koppelvlakspecificatiedocumentatie", 40, 12, True))

    def test_past_het_wel_dan_komen_de_woorden_terug(self):
        regels = teken.breek("Referentie interactiepatroon", 160, 12, True)
        self.assertEqual(" ".join(regels), "Referentie interactiepatroon")

    def test_meer_regels_dan_toegestaan_valt_af(self):
        self.assertIsNone(teken.breek("een twee drie vier vijf zes zeven", 40, 12, regels=2))


class BlokTests(unittest.TestCase):
    def test_het_jaartal_krijgt_eigen_ruimte_naast_de_omvang(self):
        """Zonder gereserveerde ruimte loopt het jaartal over de omvang heen."""
        product = {"naam": "MORA-informatiemodel", "bron_datum": "2022-10-13",
                   "omvang": "Ruim 100 informatieobjecten, zonder attributen"}
        breedte, _, _, omvangregels = teken.meet_blok(product, 248)
        nodig = max(teken.tw(r, 10) for r in omvangregels) + 22 + teken.tw("2022", 9) + 10
        self.assertGreaterEqual(breedte, nodig)

    def test_een_lange_omvang_blijft_staan(self):
        """Een omvang die over twee regels net niet past verdween eerder stil."""
        product = {"naam": "Vijflaagsmodel",
                   "omvang": "5 lagen: grondslagen, organisatorisch, informatie, "
                             "applicatie, IT-infrastructuur"}
        _, _, _, omvangregels = teken.meet_blok(product, 248)
        self.assertEqual(" ".join(omvangregels), product["omvang"])

    def test_zonder_omvang_blijft_het_blok_laag(self):
        hoog = teken.blokhoogte(["een"], ["a", "b"], "2022")
        laag = teken.blokhoogte(["een"], [], "")
        self.assertLess(laag, hoog)


class LaagTests(unittest.TestCase):
    def test_gemeenschappelijke_velden_vullen_een_product_aan(self):
        laag = {"producten": [{"naam": "X"}], "gemeenschappelijk": {"aard": "voorschrift"}}
        self.assertEqual(teken.volledig(laag, laag["producten"][0])["aard"], "voorschrift")

    def test_eigen_veld_gaat_voor_het_gemeenschappelijke(self):
        laag = {"producten": [{"naam": "X", "aard": "herbruikbaar product"}],
                "gemeenschappelijk": {"aard": "voorschrift"}}
        self.assertEqual(teken.volledig(laag, laag["producten"][0])["aard"], "herbruikbaar product")

    def test_een_gedeelde_omvang_wordt_herkend(self):
        """Staat bij elk product dezelfde omvang, dan draagt de laagkop hem een keer."""
        laag = {"producten": [{"naam": "A", "op_plaat": True}, {"naam": "B", "op_plaat": True}],
                "gemeenschappelijk": {"omvang": "Sjabloon"}}
        self.assertEqual(teken.gedeelde_omvang(laag), "Sjabloon")

    def test_verschillende_omvang_blijft_bij_het_product(self):
        laag = {"producten": [{"naam": "A", "op_plaat": True, "omvang": "3 modellen"},
                              {"naam": "B", "op_plaat": True, "omvang": "87 componenten"}]}
        self.assertEqual(teken.gedeelde_omvang(laag), "")


class PlaatTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.svg, cls.aantal = teken.teken(BRON, 1680)

    def test_elk_product_met_op_plaat_staat_erop(self):
        verwacht = [teken.volledig(laag, p)["naam"]
                    for laag in BRON["lagen"] for p in laag["producten"]
                    if teken.volledig(laag, p).get("op_plaat")]
        self.assertEqual(len(verwacht), self.aantal)
        for naam in verwacht:
            woord = naam.split()[0].replace("(", "").replace(")", "")
            self.assertIn(woord, self.svg, f"ontbreekt op de plaat: {naam}")

    def test_een_product_buiten_het_pad_blijft_eraf(self):
        self.assertNotIn("Europese interoperabiliteitsreferentie", self.svg)

    def test_elke_laag_draagt_haar_partijen(self):
        for laag in BRON["lagen"]:
            self.assertIn(laag["naam"], self.svg)

    def test_de_legenda_staat_in_de_plaat(self):
        """Een legenda naast de plaat raakt los zodra iemand het beeld doorstuurt."""
        self.assertIn("Legenda", self.svg)
        for niveau in teken.NIVEAU:
            self.assertIn(niveau, self.svg)

    def test_de_plaat_komt_door_de_poort(self, ):
        import tempfile
        pad = Path(tempfile.mkdtemp()) / "sectorketen.svg"
        pad.write_text(self.svg, encoding="utf-8")
        bevindingen = keur.keur(pad, keur.MIN_LETTER, keur.MIN_VERHOUDING, 1)[0]
        hard = [b for b in bevindingen if b.code != "KRUISING"]
        self.assertEqual(hard, [], "\n".join(str(b) for b in hard))


if __name__ == "__main__":
    unittest.main()
