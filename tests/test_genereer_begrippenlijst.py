"""Testgevallen voor scripts/genereer-begrippenlijst.py.

Elk negatief geval breekt precies een ding in een verder geldige invoer, zodat de
melding herleidbaar is naar de mutatie. De verwachte waarden worden berekend uit
de invoer van het testgeval zelf, niet uit de inhoud van de repository.
"""

import copy
import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "genereer_begrippenlijst", WORTEL / "scripts/genereer-begrippenlijst.py")
gb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gb)

KADER_URL = "https://voorbeeld.nl/kader/Onderwijsresultaat"
KADER_DEF = "Vastgelegde en geformaliseerde beoordeling op basis van een of meer leerresultaten."


def referentie():
    return {"opgehaald": "2026-09-09",
            "kaders": {"KADER": {"naam": "Testkader", "overzicht": "https://voorbeeld.nl/",
                                 "begrippen": [{"naam": "resultaat", "url": KADER_URL,
                                                "definitie": KADER_DEF}]}}}


def kaderblok(uitkomst="tegenhanger"):
    if uitkomst == "tegenhanger":
        return {"KADER": {"uitkomst": "tegenhanger", "begrip": "resultaat",
                          "url": KADER_URL, "citaat": KADER_DEF}}
    if uitkomst == "geen tegenhanger gevonden":
        return {"KADER": {"uitkomst": "geen tegenhanger gevonden", "zoekterm": "resultaat"}}
    return {"KADER": {"uitkomst": uitkomst}}


def data():
    return {
        "versie": "vtest",
        "scope": "test",
        "zoekmethode": "test",
        "kaders": ["KADER"],
        "indeling_negeerlijst": ["veldnaam"],
        "werkvoorraad": ["achtergrondterm"],
        "begrippen": [
            {"naam": "Onderwijsresultaat", "niveau": 1, "familie": "Onderwijsresultaat",
             "definitie": KADER_DEF, "vindplaats": KADER_URL, "bron_soort": "referentiekader",
             "status": "gedefinieerd", "herkomst": "overgenomen uit KADER",
             "varianten": [], "kaders": kaderblok()},
            {"naam": "Toetsonderdeel", "niveau": 2, "familie": "Onderwijsresultaat",
             "definitie": None, "vindplaats": None, "bron_soort": None,
             "status": "nog te definieren", "herkomst": "nieuw voor de solution-laag",
             "varianten": ["toetsonderdeel"], "kaders": kaderblok("geen tegenhanger gevonden")},
        ],
        "negeerlijst": [{"term": "id", "reden": "veldnaam"}],
    }


def extractie():
    def term(sleutel, indeling, schrijfwijzen):
        return {"sleutel": sleutel, "aantal": len(schrijfwijzen), "indeling": indeling,
                "schrijfwijzen": [{"schrijfwijze": s, "aantal": 1, "vindplaatsen": ["meta:x.md:1"]}
                                  for s in schrijfwijzen]}
    return {"bron": {}, "termen": [
        term("onderwijsresultaat", "kandidaat-begrip", ["Onderwijsresultaat"]),
        term("toetsonderdeel", "kandidaat-begrip", ["toetsonderdeel"]),
        term("achtergrondterm", "kandidaat-begrip", ["achtergrondterm"]),
        term("id", "veldnaam", ["id"]),
    ]}


def im():
    return {"objecttypen": [{"naam": "Toetsonderdeel", "kolom": "Onderwijsresultaat"}]}


class ControleTest(unittest.TestCase):
    def controle(self, d=None, e=None, i=None, r=None):
        return gb.controleer(d or data(), e or extractie(), i or im(), r or referentie(), WORTEL)

    def test_given_geldige_invoer_when_controleren_then_geen_fouten(self):
        self.assertEqual(self.controle(), [])

    def test_given_gedefinieerd_zonder_vindplaats_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][0]["vindplaats"] = None
        self.assertIn("zonder vindplaats", " ".join(self.controle(d)))

    def test_given_gedefinieerd_zonder_definitie_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][0]["definitie"] = None
        self.assertIn("zonder definitie", " ".join(self.controle(d)))

    def test_given_citaat_wijkt_af_van_de_bron_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][0]["kaders"]["KADER"]["citaat"] = "iets anders"
        self.assertIn("citaat bij KADER wijkt af", " ".join(self.controle(d)))

    def test_given_url_wijkt_af_van_de_bron_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][0]["kaders"]["KADER"]["url"] = "https://voorbeeld.nl/anders"
        self.assertIn("url bij KADER wijkt af", " ".join(self.controle(d)))

    def test_given_tegenhanger_niet_in_referentiekaders_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][0]["kaders"]["KADER"]["begrip"] = "onbekend"
        self.assertIn("staat niet in referentiekaders.json", " ".join(self.controle(d)))

    def test_given_geen_tegenhanger_zonder_zoekterm_when_controleren_then_fout(self):
        d = data()
        del d["begrippen"][1]["kaders"]["KADER"]["zoekterm"]
        self.assertIn("zonder zoekterm", " ".join(self.controle(d)))

    def test_given_onbekende_uitkomst_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][1]["kaders"]["KADER"]["uitkomst"] = "misschien"
        self.assertIn("onbekende uitkomst", " ".join(self.controle(d)))

    def test_given_ontbrekend_kader_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][1]["kaders"] = {}
        self.assertIn("ontbreekt in de mapping", " ".join(self.controle(d)))

    def test_given_begrip_zonder_kaderblok_when_controleren_then_fout(self):
        d = data()
        del d["begrippen"][1]["kaders"]
        self.assertIn("zonder mapping naar de referentiekaders", " ".join(self.controle(d)))

    def test_given_objecttype_ontbreekt_in_de_lijst_when_controleren_then_fout(self):
        d = data()
        d["begrippen"] = d["begrippen"][:1]
        self.assertIn("objecttype van het informatiemodel ontbreekt", " ".join(self.controle(d)))

    def test_given_kolom_ontbreekt_in_de_lijst_when_controleren_then_fout(self):
        i = im()
        i["objecttypen"][0]["kolom"] = "Onbekende kolom"
        self.assertIn("kolom van het informatiemodel ontbreekt", " ".join(self.controle(i=i)))

    def test_given_verzonnen_begrip_when_controleren_then_fout(self):
        d = data()
        b = copy.deepcopy(d["begrippen"][1])
        b.update({"naam": "Fantasiebegrip", "varianten": []})
        d["begrippen"].append(b)
        self.assertIn("komt nergens voor", " ".join(self.controle(d)))

    def test_given_dubbel_begrip_when_controleren_then_fout(self):
        d = data()
        d["begrippen"].append(copy.deepcopy(d["begrippen"][1]))
        self.assertIn("meer dan één keer", " ".join(self.controle(d)))

    def test_given_onbekend_niveau_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][1]["niveau"] = 3
        self.assertIn("zonder geldig niveau", " ".join(self.controle(d)))

    def test_given_onbekende_status_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][1]["status"] = "bijna"
        self.assertIn("onbekende status", " ".join(self.controle(d)))

    def test_given_definitie_bij_nog_te_definieren_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][1]["definitie"] = "iets"
        self.assertIn("definitie bij status nog te definieren", " ".join(self.controle(d)))

    def test_given_negeerregel_zonder_voorkomen_when_controleren_then_fout(self):
        d = data()
        d["negeerlijst"] = [{"term": "bestaatniet", "reden": "veldnaam"}]
        self.assertIn("in geen enkel bestand voorkomt", " ".join(self.controle(d)))

    def test_given_negeerregel_met_onbekende_reden_when_controleren_then_fout(self):
        d = data()
        d["negeerlijst"] = [{"term": "id", "reden": "zomaar"}]
        self.assertIn("onbekende reden", " ".join(self.controle(d)))

    def test_given_nieuwe_term_in_de_markdown_when_controleren_then_fout(self):
        e = extractie()
        e["termen"].append({"sleutel": "nieuwbegrip", "aantal": 1, "indeling": "kandidaat-begrip",
                            "schrijfwijzen": [{"schrijfwijze": "Nieuwbegrip", "aantal": 1,
                                               "vindplaatsen": ["meta:y.md:2"]}]})
        self.assertIn("niet in de werkvoorraad", " ".join(self.controle(e=e)))

    def test_given_term_in_de_werkvoorraad_when_controleren_then_geen_fout(self):
        self.assertEqual(self.controle(), [])

    def test_given_ontbrekende_sleutel_when_controleren_then_nederlandse_melding(self):
        d = data()
        del d["begrippen"][1]["status"]
        self.assertIn("onbekende status", " ".join(self.controle(d)))

    def test_given_okx_vindplaats_zonder_bestand_when_controleren_then_fout(self):
        d = data()
        d["begrippen"][0]["vindplaats"] = "bestaat/niet.md#kop"
        d["begrippen"][0]["bron_soort"] = "okx-document"
        self.assertIn("bestand dat niet bestaat", " ".join(self.controle(d)))


class SchrijfTest(unittest.TestCase):
    def test_given_geldige_invoer_when_schrijven_then_document_bevat_elke_naam(self):
        import tempfile
        d, r = data(), referentie()
        with tempfile.TemporaryDirectory() as tmp:
            doel = Path(tmp) / "begrippenlijst.md"
            gb.schrijf(d, r, doel)
            tekst = doel.read_text(encoding="utf-8")
        for b in d["begrippen"]:
            self.assertIn(b["naam"], tekst)
        self.assertIn(KADER_URL, tekst)
        self.assertIn(str(len(d["begrippen"])), tekst)


if __name__ == "__main__":
    unittest.main()
