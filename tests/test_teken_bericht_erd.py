"""Testgevallen voor scripts/teken-bericht-erd.py.

Elk geval bouwt zijn eigen document en zijn eigen informatiemodel, zodat de verwachting uit het
fixture volgt. Het laatste geval draait op de interactiespecificaties in deze repository.
"""

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
SPECIFICATIE = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod"
MODEL = WORTEL / "architecture/model/informatiemodel/informatiemodel.json"

spec = importlib.util.spec_from_file_location("erd", WORTEL / "scripts/teken-bericht-erd.py")
erd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(erd)

BEKEND = {"Opleiding specificatie", "Onderwijseenheid specificatie", "Leeruitkomst"}
RELATIES = [
    {"soort": "Aggregation", "van": "Opleiding specificatie",
     "naar": "Onderwijseenheid specificatie", "label": None},
    {"soort": "Association", "van": "Onderwijseenheid specificatie",
     "naar": "Leeruitkomst", "label": "verwijst naar"},
]


def document(secties, hoofdstuk="De berichten"):
    """Een markdown-document met een berichtenhoofdstuk en de meegegeven secties."""
    regels = ["# Een specificatie", "", "## De stroom", "", "tekst", "", f"## {hoofdstuk}", ""]
    for kop, rijen in secties:
        regels += [f"### {kop}", "", "| Veld | Objecttype |", "|---|---|"]
        regels += [f"| `veld` | {rij} |" for rij in rijen]
        regels.append("")
    return "\n".join(regels)


def maak(tekst, naam="is-oa-01.md"):
    map_ = Path(tempfile.mkdtemp())
    (map_ / naam).write_text(tekst, encoding="utf-8")
    (map_ / "model.json").write_text(
        json.dumps({"objecttypen": [{"naam": n} for n in BEKEND], "relaties": RELATIES}),
        encoding="utf-8")
    return map_


class DeBerichtenVinden(unittest.TestCase):
    """Welke secties van een document een bericht zijn."""

    def test_given_een_berichtenhoofdstuk_when_lezen_then_komen_zijn_secties_terug(self):
        t = document([("Een bericht", ["`Leeruitkomst`"]), ("Nog een", ["`Leeruitkomst`"])])
        self.assertEqual([kop for kop, _ in erd.berichten(t)], ["Een bericht", "Nog een"])

    def test_given_een_ander_hoofdstuk_when_lezen_then_blijven_zijn_secties_erbuiten(self):
        """Alleen het hoofdstuk dat de berichten draagt telt, en dat heet per document anders."""
        t = document([("Een bericht", ["`Leeruitkomst`"])], hoofdstuk="De operaties")
        self.assertEqual(erd.berichten(t), [])

    def test_given_het_hoofdstuk_berichtspecificatie_when_lezen_then_telt_het_mee(self):
        t = document([("Een bericht", ["`Leeruitkomst`"])], hoofdstuk="Berichtspecificatie")
        self.assertEqual([kop for kop, _ in erd.berichten(t)], ["Een bericht"])


class DeObjecttypenEruit(unittest.TestCase):
    """Wat er uit de kolom Objecttype komt."""

    def test_given_een_naam_in_de_kolom_objecttype_when_lezen_then_komt_hij_terug(self):
        _, blok = erd.berichten(document([("Een bericht", ["`Leeruitkomst`"])]))[0]
        self.assertEqual(erd.objecttypen_in(blok, BEKEND), ["Leeruitkomst"])

    def test_given_een_naam_die_het_model_niet_kent_when_lezen_then_blijft_hij_erbuiten(self):
        _, blok = erd.berichten(document([("Een bericht", ["`Verzonnen type`"])]))[0]
        self.assertEqual(erd.objecttypen_in(blok, BEKEND), [])

    def test_given_contracteigenschappen_when_lezen_then_komt_er_geen_objecttype(self):
        """Een afkeuring draagt velden van het contract en geen objecttype uit het model."""
        _, blok = erd.berichten(document([("Een bericht", ["contracteigenschap"])]))[0]
        self.assertEqual(erd.objecttypen_in(blok, BEKEND), [])

    def test_given_dezelfde_naam_tweemaal_when_lezen_then_komt_hij_een_keer(self):
        _, blok = erd.berichten(document([("B", ["`Leeruitkomst`", "`Leeruitkomst`"])]))[0]
        self.assertEqual(erd.objecttypen_in(blok, BEKEND), ["Leeruitkomst"])


class DeRelatiesErtussen(unittest.TestCase):

    def test_given_twee_objecttypen_met_een_relatie_when_zoeken_then_komt_zij_terug(self):
        namen = ["Opleiding specificatie", "Onderwijseenheid specificatie"]
        self.assertEqual(len(erd.relaties_tussen(namen, RELATIES)), 1)

    def test_given_een_relatie_naar_buiten_de_selectie_when_zoeken_then_blijft_zij_erbuiten(self):
        self.assertEqual(erd.relaties_tussen(["Leeruitkomst"], RELATIES), [])

    def test_given_een_geheel_deelrelatie_when_de_kardinaliteit_bepalen_then_een_en_n(self):
        self.assertEqual(erd.kardinaliteit(RELATIES[0])[:2], ("1", "n"))

    def test_given_een_specialisatie_when_de_kardinaliteit_bepalen_then_is_een(self):
        self.assertEqual(erd.kardinaliteit({"soort": "Specialization", "label": None})[2], "is een")

    def test_given_een_associatie_met_label_when_de_kardinaliteit_bepalen_then_komt_het_label(self):
        self.assertEqual(erd.kardinaliteit(RELATIES[1])[2], "verwijst naar")


class DeRijen(unittest.TestCase):
    """Een geheel staat boven zijn delen."""

    def test_given_een_geheel_en_zijn_deel_when_rijen_maken_then_staat_het_geheel_boven(self):
        rijen = erd.rijen_van(["Onderwijseenheid specificatie", "Opleiding specificatie"], RELATIES)
        self.assertEqual(rijen[0], ["Opleiding specificatie"])
        self.assertEqual(rijen[1], ["Onderwijseenheid specificatie"])

    def test_given_alleen_associaties_when_rijen_maken_then_staat_alles_in_een_rij(self):
        rijen = erd.rijen_van(["Onderwijseenheid specificatie", "Leeruitkomst"], [RELATIES[1]])
        self.assertEqual(len(rijen), 1)


class DePlaat(unittest.TestCase):

    def test_given_een_bericht_met_objecttypen_when_tekenen_then_komt_er_een_svg(self):
        map_ = maak(document([("Een bericht", ["`Opleiding specificatie`",
                                               "`Onderwijseenheid specificatie`"])]))
        uit = map_ / "erd"
        verslag = erd.verwerk(map_ / "is-oa-01.md", BEKEND, RELATIES, uit)
        self.assertEqual(len(verslag), 1)
        self.assertIsNotNone(verslag[0][1])
        self.assertTrue((uit / verslag[0][1]).read_text(encoding="utf-8").startswith("<svg"))

    def test_given_een_bericht_zonder_objecttype_when_tekenen_then_komt_er_geen_svg(self):
        """Een lege plaat leest als een gat in het model."""
        map_ = maak(document([("Een bericht", ["contracteigenschap"])]))
        verslag = erd.verwerk(map_ / "is-oa-01.md", BEKEND, RELATIES, map_ / "erd")
        self.assertIsNone(verslag[0][1])
        self.assertIn("draagt geen objecttype", verslag[0][2])

    def test_given_een_titel_breder_dan_de_vakken_when_tekenen_then_past_zij_op_het_doek(self):
        svg = erd.teken(["Leeruitkomst"], [], "Een heel lange titel die breder is dan het vak eronder")
        breedte = float(svg.split('width="')[1].split('"')[0])
        self.assertGreater(breedte, erd.breedte("Een heel lange titel die breder is dan het vak eronder", 15, True))

    def test_given_een_relatie_binnen_de_bovenste_rij_when_tekenen_then_blijft_de_lijn_op_het_doek(self):
        svg = erd.teken(["Onderwijseenheid specificatie", "Leeruitkomst"], [RELATIES[1]], "Titel")
        self.assertNotIn("-", svg.split('viewBox="')[1].split('"')[0])
        self.assertNotIn('y="-', svg)


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return erd.main(argv)

    def test_given_een_document_when_draaien_then_exitcode_nul(self):
        map_ = maak(document([("Een bericht", ["`Leeruitkomst`"])]))
        self.assertEqual(self.draai(["--bestand", str(map_ / "is-oa-01.md"),
                                     "--model", str(map_ / "model.json"),
                                     "--uit", str(map_ / "erd")]), 0)

    def test_given_een_model_dat_ontbreekt_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--model", str(Path(tmp) / "weg.json")]), 2)

    def test_given_een_map_zonder_specificatie_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--map", tmp, "--model", str(MODEL)]), 2)


class InDezeRepository(unittest.TestCase):

    def test_given_is_oa_01_when_tekenen_then_draagt_elk_bericht_met_objecttypen_een_plaat(self):
        bekend, relaties = erd.lees_model(MODEL)
        bestand = SPECIFICATIE / "is-oa-01.md"
        zonder = [kop for kop, blok in erd.berichten(bestand.read_text(encoding="utf-8"))
                  if not erd.objecttypen_in(blok, bekend)]
        # Alleen de afkeuring draagt contracteigenschappen in plaats van objecttypen.
        self.assertEqual(len(zonder), 1, zonder)
        self.assertIn("Afkeuring", zonder[0])

    def test_given_de_getekende_platen_when_lezen_then_staan_zij_naast_de_specificatie(self):
        platen = sorted((SPECIFICATIE / "img/erd").glob("is-oa-01-*.svg"))
        if not platen:
            self.skipTest("de platen ontbreken; draai eerst het script")
        self.assertGreaterEqual(len(platen), 7)
        for plaat in platen:
            self.assertTrue(plaat.read_text(encoding="utf-8").startswith("<svg"))


if __name__ == "__main__":
    unittest.main()
