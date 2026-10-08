"""Testgevallen voor scripts/teken-sectorketen.py.

De plaat draagt haar boodschap in drie kenmerken: de ArchiMate-laag in de vulkleur, de aard
in de rand, en het MIM-niveau met het AMIGO-inhoudsgebied in twee aanduidingen onderin. Wat
hier wordt bewaakt is dat die kenmerken op het beeld terechtkomen, dat een naam nooit
stilletjes wordt afgekapt, dat de aanduidingen elkaar niet overlappen, en dat de plaat door
de leesbaarheidspoort komt.
"""

import importlib.util
import json
import tempfile
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


def alle_producten():
    for laag in BRON["lagen"]:
        for product in laag["producten"]:
            yield laag, teken.volledig(laag, product)


class BreekTests(unittest.TestCase):
    """Een afgebroken naam valt pas op als iemand de plaat voorleest, dus hij mag niet ontstaan."""

    def test_een_woord_dat_te_breed_is_valt_af(self):
        self.assertIsNone(teken.breek("Koppelvlakspecificatiedocumentatie", 40, 12, True))

    def test_past_het_wel_dan_komen_de_woorden_terug(self):
        regels = teken.breek("Referentie interactiepatroon", 170, 12, True)
        self.assertEqual(" ".join(regels), "Referentie interactiepatroon")

    def test_meer_regels_dan_toegestaan_valt_af(self):
        self.assertIsNone(teken.breek("een twee drie vier vijf zes zeven", 40, 12, regels=2))

    def test_ruim_breken_geeft_altijd_regels(self):
        """De laatste uitwijk mag nooit None teruggeven, anders verdwijnt een naam."""
        regels = teken.breek_ruim("Afsprakenstelsels per toepassingsgebied", 90, 12, True)
        self.assertEqual(" ".join(regels), "Afsprakenstelsels per toepassingsgebied")


class BlokTests(unittest.TestCase):
    def test_een_lang_woord_verbreedt_het_blok(self):
        """Afkappen hoort niet; het blok wijkt uit in plaats van de naam."""
        product = {"naam": "MORA-koppelvlakperspectief", "mim_niveau": "niet van toepassing"}
        breedte, _, regels, _ = teken.meet_blok(product, 200)
        self.assertEqual(regels, ["MORA-koppelvlakperspectief"])
        self.assertGreaterEqual(breedte, teken.tw("MORA-koppelvlakperspectief", 12, True) + 22)

    def test_de_voet_biedt_ruimte_aan_staafje_wig_en_jaartal(self):
        product = {"naam": "Logische gegevensmodellen", "bron_datum": "2025-10-16",
                   "mim_niveau": "logisch gegevensmodel", "inhoudsgebied": "toepassingsgebied"}
        breedte, _, _, _ = teken.meet_blok(product, 252)
        nodig = teken.MIMBREEDTE + 8 + teken.INHOUDBREEDTE + 8 + teken.tw("2025", 10) + 10 + 22
        self.assertGreaterEqual(breedte, nodig)

    def test_zonder_aanduidingen_blijft_het_blok_laag(self):
        kaal = {"naam": "x", "mim_niveau": "niet van toepassing"}
        vol = {"naam": "x", "mim_niveau": "logisch gegevensmodel"}
        self.assertLess(teken.blokhoogte(["x"], [], kaal), teken.blokhoogte(["x"], [], vol))

    def test_voorgenomen_werk_draagt_een_voet(self):
        product = {"naam": "x", "mim_niveau": "niet van toepassing", "voorgenomen": True}
        self.assertGreater(teken.blokhoogte(["x"], [], product), teken.blokhoogte(["x"], [], {"naam": "x"}))


class AanduidingTests(unittest.TestCase):
    def test_het_staafje_vult_tot_het_niveau(self):
        diep = teken.mimbalk(0, 0, "technisch gegevensmodel", "#000")
        ondiep = teken.mimbalk(0, 0, "begrippen", "#000")
        self.assertEqual(diep.count(teken.VOL), 4)
        self.assertEqual(ondiep.count(teken.VOL), 1)

    def test_zonder_niveau_geen_staafje(self):
        self.assertEqual(teken.mimbalk(0, 0, "niet van toepassing", "#000"), "")

    def test_de_wig_vult_een_vak(self):
        """De wig markeert een vak en vult er nooit meer dan een, anders leest zij als het staafje."""
        for gebied in teken.INHOUD:
            self.assertEqual(teken.inhoudwig(0, 0, gebied, "#000").count(teken.VOL), 1)

    def test_de_wig_gebruikt_een_andere_vorm_dan_het_staafje(self):
        """Twee aanduidingen naast elkaar moeten op het eerste oog verschillen."""
        self.assertIn("polygon", teken.inhoudwig(0, 0, "inrichting", "#000"))
        self.assertIn("rect", teken.mimbalk(0, 0, "begrippen", "#000"))
        self.assertNotIn("polygon", teken.mimbalk(0, 0, "begrippen", "#000"))


class BronTests(unittest.TestCase):
    def test_elk_product_draagt_de_verplichte_velden(self):
        for laag, product in alle_producten():
            with self.subTest(product=product["naam"]):
                self.assertIn(product.get("aard"), ("voorschrift", "herbruikbaar product"))
                self.assertIn(product.get("archimate"), teken.ELEMENTLAAG)
                self.assertIn(product.get("mim_niveau"), teken.MIM + ["niet van toepassing"])
                self.assertIn(product.get("inhoudsgebied"), teken.INHOUD + [None])

    def test_laag_vijf_telt_elf_producten(self):
        """De gesloten lijst uit het MOKA-template en de voorbeelduitwerking."""
        laag5 = next(l for l in BRON["lagen"] if l["nummer"] == 5)
        self.assertEqual(len(laag5["producten"]), 11)

    def test_de_ketenleden_bestaan_en_worden_dieper(self):
        namen = {p["naam"]: p for _, p in alle_producten()}
        diepte = []
        for lid in BRON["ketens"][0]["leden"]:
            self.assertIn(lid, namen, f"onbekend ketenlid: {lid}")
            diepte.append(teken.MIM.index(namen[lid]["mim_niveau"]))
        self.assertEqual(diepte, sorted(diepte), "de keten moet oplopen in MIM-diepte")

    def test_gemeenschappelijke_velden_vullen_een_product_aan(self):
        laag = {"producten": [{"naam": "X"}], "gemeenschappelijk": {"aard": "voorschrift"}}
        self.assertEqual(teken.volledig(laag, laag["producten"][0])["aard"], "voorschrift")

    def test_eigen_veld_gaat_voor_het_gemeenschappelijke(self):
        laag = {"producten": [{"naam": "X", "aard": "herbruikbaar product"}],
                "gemeenschappelijk": {"aard": "voorschrift"}}
        self.assertEqual(teken.volledig(laag, laag["producten"][0])["aard"], "herbruikbaar product")


class PlaatTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.svg, cls.aantal, cls.segmenten = teken.teken(BRON, 1680)

    def test_elk_product_met_op_plaat_staat_erop(self):
        verwacht = [p["naam"] for _, p in alle_producten() if p.get("op_plaat")]
        self.assertEqual(len(verwacht), self.aantal)
        for naam in verwacht:
            woord = naam.split()[0].replace("(", "").replace(")", "")
            self.assertIn(woord, self.svg, f"ontbreekt op de plaat: {naam}")

    def test_elke_laag_draagt_haar_naam(self):
        for laag in BRON["lagen"]:
            self.assertIn(laag["naam"], self.svg)

    def test_de_ladder_verbindt_alle_lagen(self):
        """Zonder de ladder toont de plaat alleen de uitzonderingen."""
        self.assertIn("levert aan de laag eronder", self.svg)

    def test_de_legenda_staat_in_de_plaat(self):
        """Een legenda naast de plaat raakt los zodra iemand het beeld doorstuurt."""
        self.assertIn("Legenda", self.svg)
        for laag in teken.LAAGKLEUR:
            self.assertIn(laag, self.svg)
        for niveau in teken.MIM:
            self.assertIn(niveau, self.svg)
        for gebied in teken.INHOUD:
            self.assertIn(gebied, self.svg)

    def test_de_plaat_komt_door_de_poort(self):
        pad = Path(tempfile.mkdtemp()) / "sectorketen.svg"
        pad.write_text(self.svg, encoding="utf-8")
        bevindingen, _ = keur.keur(pad, keur.MIN_LETTER, keur.MIN_VERHOUDING, 0)[:2]
        self.assertEqual([str(b) for b in bevindingen], [])


if __name__ == "__main__":
    unittest.main()
