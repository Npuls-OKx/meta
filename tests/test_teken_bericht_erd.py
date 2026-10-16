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


class DeAttributen(unittest.TestCase):
    """De velden van het bericht landen bij het objecttype dat hun rij noemt."""

    def tabel(self, rijen, kop="| Veld | Type | Kardinaliteit | Verplicht | Objecttype |"):
        regels = ["# S", "", "## De berichten", "", "### Een bericht", "", kop,
                  "|" + "---|" * (kop.count("|") - 1)] + rijen + [""]
        _, blok = erd.berichten("\n".join(regels))[0]
        return erd.attributen_in(blok, BEKEND)

    def test_given_een_veld_met_een_objecttype_when_lezen_then_hangt_het_eraan(self):
        uit = self.tabel(["| `id` | uuid | 1 | ja | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["naam"], "id")
        self.assertEqual(uit["Leeruitkomst"][0]["type"], "uuid")

    def test_given_het_veld_id_when_lezen_then_is_het_de_sleutel(self):
        uit = self.tabel(["| `id` | uuid | 1 | ja | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["sleutel"], "PK")

    def test_given_een_veld_dat_op_id_eindigt_when_lezen_then_is_het_een_verwijzing(self):
        uit = self.tabel(["| `parentId` | uuid | 1 | ja | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["sleutel"], "FK")

    def test_given_een_veld_in_een_array_when_lezen_then_draagt_het_zijn_niveau(self):
        uit = self.tabel(["| `members[].studentId` | uuid | 1 | ja | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["naam"], "members_studentId")

    def test_given_twee_array_niveaus_when_lezen_then_blijft_elk_niveau_gescheiden(self):
        """Zonder scheiding plakken de niveaus aan elkaar: placementGroupsmembers_studentId."""
        uit = self.tabel(
            ["| `placementGroups[].members[].studentId` | uuid | 1 | ja | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["naam"], "placementGroups_members_studentId")

    def test_given_kardinaliteit_en_verplicht_when_lezen_then_staan_zij_in_de_opmerking(self):
        uit = self.tabel(["| `naam` | string | 0..1 | nee | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["opmerking"], "0..1")

    def test_given_een_samengesteld_type_when_lezen_then_blijft_een_woord_over(self):
        """Mermaid neemt geen spatie in een type; de eerste term is het type."""
        uit = self.tabel(["| `vorm` | object: `waarde`, `eenheid` | 1 | ja | `Leeruitkomst` |"])
        self.assertEqual(uit["Leeruitkomst"][0]["type"], "object")

    def test_given_een_tabel_zonder_kolom_veld_when_lezen_then_komen_er_geen_attributen(self):
        uit = self.tabel(["| `x` | `Leeruitkomst` |"], kop="| Soort | Objecttype |")
        self.assertEqual(dict(uit), {})


class HetMermaidBlok(unittest.TestCase):
    """Wat er tussen de merktekens komt."""

    def test_given_een_geheel_deelrelatie_when_bouwen_then_is_zij_een_op_veel(self):
        blok = erd.mermaid(["Opleiding specificatie", "Onderwijseenheid specificatie"],
                           [RELATIES[0]], {})
        self.assertIn('"Opleiding specificatie" ||--o{ "Onderwijseenheid specificatie"', blok)

    def test_given_een_associatie_met_label_when_bouwen_then_draagt_de_lijn_dat_label(self):
        blok = erd.mermaid(["Onderwijseenheid specificatie", "Leeruitkomst"], [RELATIES[1]], {})
        self.assertIn(': "verwijst naar"', blok)

    def test_given_een_specialisatie_when_bouwen_then_staat_er_is_een(self):
        rel = {"soort": "Specialization", "van": "Leeruitkomst", "naar": "Leeruitkomst", "label": None}
        self.assertIn(': "is een"', erd.mermaid(["Leeruitkomst"], [rel], {}))

    def test_given_de_naam_uit_het_model_when_bouwen_then_staat_zij_er_letterlijk(self):
        """De entiteit draagt de naam van het objecttype, zodat beide documenten hetzelfde zeggen."""
        self.assertIn('"Opleiding specificatie"', erd.mermaid(["Opleiding specificatie"], [], {}))

    def test_given_attributen_when_bouwen_then_dragen_zij_type_sleutel_en_opmerking(self):
        attributen = {"Leeruitkomst": [{"naam": "id", "type": "uuid", "sleutel": "PK",
                                        "opmerking": "1, verplicht"}]}
        blok = erd.mermaid(["Leeruitkomst"], [], attributen)
        self.assertIn('uuid id PK "1, verplicht"', blok)

    def test_given_geen_objecttype_when_bouwen_then_komt_de_reden_in_plaats_van_een_diagram(self):
        """Een leeg diagram leest als een gat in het model."""
        self.assertIn("eigenschappen van het contract", erd.blok_voor([], [], {}))


class DeMerktekens(unittest.TestCase):
    """Het blok wordt tussen de merktekens geschreven, en alleen daar."""

    def document(self, secties):
        regels = ["# S", "", "## De berichten", ""]
        for kop, rijen in secties:
            regels += [f"### {kop}", "", "<!-- erd -->", "<!-- /erd -->", "",
                       "| Veld | Type | Objecttype |", "|---|---|---|"]
            regels += rijen + [""]
        return "\n".join(regels)

    def schrijf(self, tekst):
        map_ = Path(tempfile.mkdtemp())
        bestand = map_ / "is-oa-01.md"
        bestand.write_text(tekst, encoding="utf-8")
        return bestand

    def test_given_lege_merktekens_when_bijwerken_then_komt_het_diagram_erin(self):
        bestand = self.schrijf(self.document([("Een bericht", ["| `id` | uuid | `Leeruitkomst` |"])]))
        erd.verwerk(bestand, BEKEND, RELATIES)
        self.assertIn("erDiagram", bestand.read_text(encoding="utf-8"))

    def test_given_twee_lege_blokken_when_bijwerken_then_krijgt_elk_zijn_eigen_diagram(self):
        """Twee lege blokken zijn letterlijk gelijk; vervangen gaat daarom op plek."""
        bestand = self.schrijf(self.document([
            ("Eerste", ["| `id` | uuid | `Leeruitkomst` |"]),
            ("Tweede", ["| `x` | string | contracteigenschap |"]),
        ]))
        erd.verwerk(bestand, BEKEND, RELATIES)
        tekst = bestand.read_text(encoding="utf-8")
        self.assertIn("erDiagram", tekst.split("### Tweede")[0])
        self.assertIn("eigenschappen van het contract", tekst.split("### Tweede")[1])

    def test_given_een_bericht_zonder_merktekens_when_bijwerken_then_staat_het_in_de_uitvoer(self):
        tekst = "# S\n\n## De berichten\n\n### Een bericht\n\n| Veld | Objecttype |\n|---|---|\n| `id` | `Leeruitkomst` |\n"
        verslag, veranderd = erd.verwerk(self.schrijf(tekst), BEKEND, RELATIES)
        self.assertEqual(verslag[0][1], "geen merktekens")
        self.assertFalse(veranderd)

    def test_given_een_tweede_ronde_when_bijwerken_then_wijzigt_er_niets(self):
        bestand = self.schrijf(self.document([("Een bericht", ["| `id` | uuid | `Leeruitkomst` |"])]))
        erd.verwerk(bestand, BEKEND, RELATIES)
        verslag, veranderd = erd.verwerk(bestand, BEKEND, RELATIES)
        self.assertFalse(veranderd)
        self.assertEqual(verslag[0][1], "ongewijzigd")

    def test_given_controleer_when_bijwerken_then_blijft_het_bestand_ongemoeid(self):
        bestand = self.schrijf(self.document([("Een bericht", ["| `id` | uuid | `Leeruitkomst` |"])]))
        voor = bestand.read_text(encoding="utf-8")
        erd.verwerk(bestand, BEKEND, RELATIES, controleer=True)
        self.assertEqual(bestand.read_text(encoding="utf-8"), voor)


class DeBinding(unittest.TestCase):
    """De objecttypen komen uit de binding wanneer die het schema van dit bericht kent."""

    BINDING = {
        "schemas": {
            "education-specification.json": {
                "soort": "begrip",
                "draagt": ["Opleiding specificatie", "Onderwijseenheid specificatie"],
            },
            "subscription.json": {"soort": "vervoer", "reden": "richt het kanaal in"},
        },
        "objecttypen": {
            "Opleiding specificatie": {"attributen": [
                {"naam": "id", "datatype": "identificatie", "kardinaliteit": "1..1",
                 "rol": "sleutel", "bron": "schema education-specification.json"},
                {"naam": "elders", "datatype": "string", "kardinaliteit": "0..1",
                 "rol": "", "bron": "schema ander-schema.json"},
            ]},
        },
    }

    def sectie(self, regels):
        return "\n".join(["# S", "", "## De berichten", "", "### Een bericht", "", *regels, ""])

    def test_given_een_bericht_dat_een_begripsschema_noemt_when_lezen_then_komen_zijn_objecttypen(self):
        _, blok = erd.berichten(self.sectie(["Volgt [education-specification.json](x)."]))[0]
        self.assertEqual(erd.objecttypen_uit_binding(blok, self.BINDING),
                         ["Opleiding specificatie", "Onderwijseenheid specificatie"])

    def test_given_een_bericht_dat_een_vervoersschema_noemt_when_lezen_then_komt_er_geen_objecttype(self):
        _, blok = erd.berichten(self.sectie(["Volgt [subscription.json](x)."]))[0]
        self.assertEqual(erd.objecttypen_uit_binding(blok, self.BINDING), [])

    def test_given_een_schema_dat_de_binding_niet_kent_when_lezen_then_komt_er_geen_objecttype(self):
        _, blok = erd.berichten(self.sectie(["Volgt [onbekend.json](x)."]))[0]
        self.assertEqual(erd.objecttypen_uit_binding(blok, self.BINDING), [])

    def test_given_de_binding_when_attributen_zoeken_then_telt_alleen_de_bron_van_dit_bericht(self):
        """Een attribuutsoort uit een ander schema hoort niet in dit diagram."""
        _, blok = erd.berichten(self.sectie(["Volgt [education-specification.json](x)."]))[0]
        uit = erd.attributen_uit_binding(blok, self.BINDING)
        self.assertEqual([a["naam"] for a in uit["Opleiding specificatie"]], ["id"])

    def test_given_de_rol_sleutel_when_attributen_zoeken_then_wordt_het_pk(self):
        _, blok = erd.berichten(self.sectie(["Volgt [education-specification.json](x)."]))[0]
        uit = erd.attributen_uit_binding(blok, self.BINDING)
        self.assertEqual(uit["Opleiding specificatie"][0]["sleutel"], "PK")

    def test_given_een_tabel_en_de_binding_when_bijwerken_then_vult_de_binding_de_tabel_aan(self):
        """De tabel gaat voor, want zij draagt de kardinaliteit van dit bericht."""
        map_ = Path(tempfile.mkdtemp())
        bestand = map_ / "is-oa-01.md"
        bestand.write_text(self.sectie([
            "Volgt [education-specification.json](x).", "",
            "<!-- erd -->", "<!-- /erd -->", "",
            "| Veld | Type | Kardinaliteit | Objecttype |", "|---|---|---|---|",
            "| `id` | uuid | 9..9 | `Opleiding specificatie` |",
        ]), encoding="utf-8")
        erd.verwerk(bestand, {"Opleiding specificatie", "Onderwijseenheid specificatie"}, [],
                    binding=self.BINDING)
        tekst = bestand.read_text(encoding="utf-8")
        self.assertIn('uuid id PK "9..9"', tekst)
        self.assertIn('"Onderwijseenheid specificatie"', tekst)


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return erd.main(argv)

    def test_given_een_document_when_draaien_then_exitcode_nul(self):
        map_ = maak(document([("Een bericht", ["`Leeruitkomst`"])]))
        self.assertEqual(self.draai(["--bestand", str(map_ / "is-oa-01.md"),
                                     "--model", str(map_ / "model.json")]), 0)

    def test_given_een_erd_die_achterloopt_when_controleren_then_exitcode_een(self):
        """De poort voor een bouwmachine: het document moet het model volgen."""
        tekst = ("# S\n\n## De berichten\n\n### Een bericht\n\n<!-- erd -->\n<!-- /erd -->\n\n"
                 "| Veld | Objecttype |\n|---|---|\n| `id` | `Leeruitkomst` |\n")
        map_ = maak(tekst)
        self.assertEqual(self.draai(["--bestand", str(map_ / "is-oa-01.md"),
                                     "--model", str(map_ / "model.json"), "--controleer"]), 1)

    def test_given_een_model_dat_ontbreekt_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--model", str(Path(tmp) / "weg.json")]), 2)

    def test_given_een_map_zonder_specificatie_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--map", tmp, "--model", str(MODEL)]), 2)


class InDezeRepository(unittest.TestCase):

    def test_given_is_oa_01_when_controleren_then_lopen_de_erds_niet_achter(self):
        """De ERDs komen uit het model en de binding; lopen zij achter, dan klopt het document niet."""
        bekend, relaties = erd.lees_model(MODEL)
        binding = erd.lees_binding(WORTEL / erd.BINDING)
        _, veranderd = erd.verwerk(SPECIFICATIE / "is-oa-01.md", bekend, relaties,
                                   controleer=True, binding=binding)
        self.assertFalse(veranderd, "draai scripts/teken-bericht-erd.py")

    def test_given_is_oa_01_when_lezen_then_draagt_elk_bericht_een_blok(self):
        bekend, _ = erd.lees_model(MODEL)
        tekst = (SPECIFICATIE / "is-oa-01.md").read_text(encoding="utf-8")
        secties = erd.berichten(tekst)
        self.assertGreaterEqual(len(secties), 8)
        zonder = [kop for kop, blok in secties if not erd.MERKTEKEN.search(blok)]
        self.assertEqual(zonder, [])


if __name__ == "__main__":
    unittest.main()
