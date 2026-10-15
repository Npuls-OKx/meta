"""Testgevallen voor scripts/genereer-oas.py.

Elk geval bouwt zijn eigen interactiespecificatie op: een tijdelijke map met een
`operaties.json`, een map `schemas/` en een markdown-bestand met de voorbeeldpayloads. De
verwachting volgt daarmee uit het fixture en niet uit de inhoud van deze repository, en elk
negatief geval breekt precies een ding. De laatste twee gevallen draaien de generator op de
interactiespecificatie in deze repository en toetsen de uitkomst zonder een aantal vast te
leggen dat veroudert zodra de specificatie groeit.
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
PUBLIC = WORTEL / "../Public/Informatie-en-gegevensmodellen/schemas"

spec = importlib.util.spec_from_file_location("genereer_oas", WORTEL / "scripts/genereer-oas.py")
gos = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gos)


# ------------------------------------------------------------------------------- de fixtures


def schema_melding():
    """Een schema met een gesloten enum, zonder verwijzing naar een ander schema."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/melding/voorstel",
        "title": "Notification",
        "DutchName": "Melding",
        "type": "object",
        "required": ["status"],
        "properties": {"status": {"enum": ["ontvangen", "gelukt"], "DutchName": "status"}},
    }


def schema_bericht():
    """Een schema dat naar een ander schema verwijst en een eigen `$defs` draagt."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/bericht/voorstel",
        "type": "object",
        "required": ["verwijzing"],
        "properties": {
            "verwijzing": {"$ref": "https://okx.npuls.nl/schema/melding/voorstel"},
            "maat": {"$ref": "#/$defs/maat"},
        },
        "$defs": {"maat": {"type": "integer", "minimum": 0}},
    }


def schema_overlay():
    """Een overlay: een eigen wortel die een sleutel naast het dragende schema legt."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/overlay/voorstel",
        "type": "object",
        "properties": {"extra": {"enum": ["een", "twee"]}},
    }


def operatie_aanroep(**af):
    """Een aanroep op de onderwijscatalogus, met de velden die een geval overschrijft."""
    operatie = {
        "id": "IS-OA-01-O1",
        "stroom": "IS-OA-01",
        "soort": "aanroep",
        "samenvatting": "Een specificatie ophalen",
        "component": "onderwijscatalogus",
        "aanroeper": "curriculum-ontwerptool",
        "pad": "/specificaties/{id}",
        "methode": "get",
        "parameters": [{
            "naam": "id",
            "plaats": "path",
            "verplicht": True,
            "type": {"type": "string", "format": "uuid"},
            "omschrijving": "De wortel van de structuur.",
        }],
        "antwoorden": [{"code": "200", "omschrijving": "De structuur.", "schema": "melding"}],
        "foutgedrag": "HTTP-foutcode.",
        "stand": {"kern": "vastgelegd"},
    }
    operatie.update(af)
    return operatie


def operatie_melding(**af):
    """Een melding die de onderwijscatalogus verstuurt."""
    operatie = {
        "id": "IS-OA-01-O6",
        "stroom": "IS-OA-01",
        "soort": "melding",
        "samenvatting": "De uitkomst melden",
        "melding": "verwerkingsstatus",
        "melder": "onderwijscatalogus",
        "ontvanger": "curriculum-ontwerptool",
        "methode": "post",
        "verzoek": {"schema": "melding", "omschrijving": "De toestand van de levering."},
        "antwoorden": [{
            "code": "200",
            "omschrijving": "De ontvanger bevestigt.",
            "zonder_lichaam": "De bevestiging draagt geen lichaam.",
        }],
        "stand": {"kern": "vastgelegd"},
    }
    operatie.update(af)
    return operatie


def schema_abonnement(waarden=("verwerkingsstatus",)):
    """Een abonnementsschema met de gesloten lijst waarop een partij zich abonneert."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/abonnement/alfa",
        "title": "Subscription",
        "DutchName": "Abonnement",
        "type": "object",
        "required": ["callbackUrl", "events"],
        "properties": {
            "callbackUrl": {"type": "string", "format": "uri", "DutchName": "callbackUrl"},
            "events": {"type": "array", "items": {"enum": list(waarden)}, "DutchName": "events"},
        },
    }


def operatie_abonnement(**af):
    """De abonnementsoperatie: het afleveradres met de meldingssoorten erbij."""
    operatie = {
        "id": "IS-OA-01-O8",
        "stroom": "IS-OA-01",
        "soort": "aanroep",
        "samenvatting": "Het afleveradres vastleggen",
        "component": "onderwijscatalogus",
        "aanroeper": "curriculum-ontwerptool",
        "pad": "/abonnementen",
        "methode": "post",
        "parameters": [],
        "verzoek": {"schema": "abonnement", "omschrijving": "Het afleveradres."},
        "antwoorden": [{"code": "201", "omschrijving": "Vastgelegd.", "schema": "abonnement"}],
        "foutgedrag": "HTTP-foutcode.",
        "stand": {"kern": "vastgelegd"},
    }
    operatie.update(af)
    return operatie


def maak_spec(map_, operaties, componenten=None, schemas=None, markdown=None):
    """Een interactiespecificatie als fixture op schijf zetten, en het operatiebestand teruggeven."""
    map_ = Path(map_)
    (map_ / "schemas").mkdir(parents=True, exist_ok=True)
    (map_ / "public").mkdir(parents=True, exist_ok=True)
    for naam, inhoud in (schemas or {"melding": schema_melding()}).items():
        (map_ / "schemas" / f"{naam}.json").write_text(
            json.dumps(inhoud, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if markdown:
        (map_ / "stroom-is-oa-01.md").write_text(markdown, encoding="utf-8")
    data = {
        "naam": "Een fixture",
        "versie": "0.0.1",
        "bron": {"wie_is_de_bron": "dit bestand"},
        "componenten": componenten or {
            "onderwijscatalogus": {"naam": "Onderwijscatalogus", "afgerond": True, "toelichting": "volledig"}
        },
        "stromen": {"IS-OA-01": {"bestand": "stroom-is-oa-01.md"}},
        "servers": {"openstaand": "De keuze staat open.", "plaatshouder": "https://component.invalid/okx"},
        "beveiliging": {
            "grond": "OAuth 2.0 Client Credentials.",
            "verwijzing": "https://voorbeeld.invalid/auth-standaard.md",
            "openstaand": "De tokenUrl staat open.",
        },
        "operaties": operaties,
    }
    bestand = map_ / "operaties.json"
    bestand.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return bestand


def draai(bestand, extra=None):
    """De generator draaien op een fixture, en code, uitvoer en document teruggeven."""
    map_ = Path(bestand).parent
    argv = ["--operaties", str(bestand), "--uit", str(map_ / "oas"),
            "--public-schemas", str(map_ / "public")] + (extra or [])
    uitvoer = io.StringIO()
    with contextlib.redirect_stdout(uitvoer), contextlib.redirect_stderr(uitvoer):
        code = gos.main(argv)
    document = None
    geschreven = map_ / "oas" / "onderwijscatalogus.openapi.json"
    if geschreven.is_file():
        document = json.loads(geschreven.read_text(encoding="utf-8"))
    return code, uitvoer.getvalue(), document


def fence(schemas, lading):
    """Een markdown-bestand met een voorbeeldpayload achter de aanduiding `schema=`."""
    return (
        "# Een stroom\n\nDe payload:\n\n"
        f"```json schema={schemas}\n{json.dumps(lading, indent=2, ensure_ascii=False)}\n```\n"
    )


# -------------------------------------------------------------------------------- de gevallen


class EenDocumentPerComponent(unittest.TestCase):
    """Welk document er komt, en voor welk component."""

    def test_given_een_afgerond_component_when_genereren_then_een_openapi_document_met_haar_paden(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            code, uitvoer, document = draai(bestand)
            self.assertIsNotNone(document, uitvoer)
            self.assertEqual(document["openapi"], "3.1.0")
            self.assertIn("/specificaties/{id}", document["paths"])
            self.assertIn("get", document["paths"]["/specificaties/{id}"])
            self.assertEqual(code, 0, uitvoer)

    def test_given_een_component_dat_niet_afgerond_is_when_genereren_then_schrijft_het_script_geen_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp, [operatie_aanroep()],
                componenten={"onderwijscatalogus": {
                    "naam": "Onderwijscatalogus", "afgerond": False,
                    "toelichting": "IS-OA-02 staat nog niet in dit bestand",
                }},
            )
            code, uitvoer, document = draai(bestand)
            self.assertIsNone(document)
            self.assertIn("geen document", uitvoer)
            self.assertIn("IS-OA-02 staat nog niet in dit bestand", uitvoer)
            self.assertEqual(code, 2, uitvoer)

    def test_given_een_component_dat_niet_afgerond_is_when_alles_gevraagd_wordt_then_komt_het_document_er_toch(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp, [operatie_aanroep()],
                componenten={"onderwijscatalogus": {
                    "naam": "Onderwijscatalogus", "afgerond": False, "toelichting": "onvolledig",
                }},
            )
            _, uitvoer, document = draai(bestand, ["--alles"])
            self.assertIsNotNone(document, uitvoer)
            self.assertIn("/specificaties/{id}", document["paths"])

    def test_given_een_onbekend_component_when_gevraagd_then_stopt_het_script_met_de_code_voor_onbruikbaar(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            code, uitvoer, _ = draai(bestand, ["--component", "boekhouding"])
            self.assertEqual(code, 3)
            self.assertIn("Onbekend component", uitvoer)


class DeSchemasInDeBundel(unittest.TestCase):
    """Wat de bundeling aan een schema verandert, en wat niet."""

    def test_given_een_schema_zonder_verwijzingen_when_bundelen_then_staat_het_ongewijzigd_in_het_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            _, uitvoer, document = draai(bestand)
            origineel = json.loads(
                (Path(tmp) / "schemas/melding.json").read_text(encoding="utf-8")
            )
            zonder_wortelsleutels = {
                s: w for s, w in origineel.items() if s not in ("$id", "$schema")
            }
            self.assertEqual(document["components"]["schemas"]["melding"], zonder_wortelsleutels)

    def test_given_een_schema_met_een_verwijzing_naar_een_ander_schema_when_bundelen_then_wijst_zij_binnen_het_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp,
                [operatie_aanroep(antwoorden=[
                    {"code": "200", "omschrijving": "Het bericht.", "schema": "bericht"}
                ])],
                schemas={"bericht": schema_bericht(), "melding": schema_melding()},
            )
            _, uitvoer, document = draai(bestand)
            gebundeld = document["components"]["schemas"]["bericht"]
            self.assertEqual(
                gebundeld["properties"]["verwijzing"]["$ref"], "#/components/schemas/melding"
            )
            self.assertIn("melding", document["components"]["schemas"])

    def test_given_een_schema_met_een_eigen_defs_when_bundelen_then_schuift_de_verwijzing_mee(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp,
                [operatie_aanroep(antwoorden=[
                    {"code": "200", "omschrijving": "Het bericht.", "schema": "bericht"}
                ])],
                schemas={"bericht": schema_bericht(), "melding": schema_melding()},
            )
            _, uitvoer, document = draai(bestand)
            gebundeld = document["components"]["schemas"]["bericht"]
            self.assertEqual(
                gebundeld["properties"]["maat"]["$ref"],
                "#/components/schemas/bericht/$defs/maat",
            )
            self.assertIsNotNone(gos.los_pointer_op(document, gebundeld["properties"]["maat"]["$ref"]))

    def test_given_een_schema_op_voorstel_when_bundelen_then_draagt_het_document_die_stand(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            _, uitvoer, document = draai(bestand)
            herkomst = document["x-okx-schemas"]["melding"]
            self.assertEqual(herkomst["stand"], "voorstel")
            self.assertEqual(herkomst["schemaId"], "https://okx.npuls.nl/schema/melding/voorstel")

    def test_given_een_schema_dat_in_geen_enkele_map_staat_when_genereren_then_meldt_het_script_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(antwoorden=[
                {"code": "200", "omschrijving": "Iets.", "schema": "bestaat-niet"}
            ])])
            code, uitvoer, _ = draai(bestand)
            self.assertIn("het schema bestaat-niet staat in geen enkele schemamap", uitvoer)
            self.assertEqual(code, 1, uitvoer)

    def test_given_een_verwijzing_die_nergens_uitkomt_when_controleren_then_meldt_het_script_een_bevinding(self):
        document = {"components": {"schemas": {"melding": {"$ref": "#/components/schemas/weg"}}}}
        gaten = []
        gos.controleer_verwijzingen(document, "proef", gaten)
        self.assertEqual(len(gaten), 1)
        self.assertIsInstance(gaten[0], gos.Bevinding)
        self.assertIn("komt nergens uit", str(gaten[0]))


class DeVoorbeelden(unittest.TestCase):
    """Of een voorbeeld tegen zijn schema gaat, en wat er gebeurt als het niet valideert."""

    def test_given_een_voorbeeld_dat_valideert_when_controleren_then_blijft_het_zonder_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp,
                [operatie_aanroep(antwoorden=[{
                    "code": "200", "omschrijving": "De melding.", "schema": "melding",
                    "voorbeeld": {"bestand": "stroom-is-oa-01.md", "schema": "melding", "nummer": 1},
                }])],
                markdown=fence("melding", {"status": "gelukt"}),
            )
            code, uitvoer, document = draai(bestand)
            voorbeelden = (document["paths"]["/specificaties/{id}"]["get"]["responses"]["200"]
                           ["content"]["application/json"]["examples"])
            self.assertEqual(voorbeelden["voorbeeld-1"]["value"], {"status": "gelukt"})
            self.assertEqual(code, 0, uitvoer)

    def test_given_een_voorbeeld_dat_niet_valideert_when_controleren_then_meldt_het_script_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp,
                [operatie_aanroep(antwoorden=[{
                    "code": "200", "omschrijving": "De melding.", "schema": "melding",
                    "voorbeeld": {"bestand": "stroom-is-oa-01.md", "schema": "melding", "nummer": 1},
                }])],
                markdown=fence("melding", {"status": "verzonnen"}),
            )
            code, uitvoer, _ = draai(bestand)
            self.assertIn("BEVINDING", uitvoer)
            self.assertIn("'verzonnen' is not one of", uitvoer)
            self.assertEqual(code, 1, uitvoer)

    def test_given_een_voorbeeldverwijzing_naar_een_ontbrekende_fence_when_genereren_then_meldt_het_script_een_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp,
                [operatie_aanroep(antwoorden=[{
                    "code": "200", "omschrijving": "De melding.", "schema": "melding",
                    "voorbeeld": {"bestand": "stroom-is-oa-01.md", "schema": "melding", "nummer": 2},
                }])],
                markdown=fence("melding", {"status": "gelukt"}),
            )
            code, uitvoer, _ = draai(bestand)
            self.assertIn("voorbeeld 2 met schema melding staat niet in stroom-is-oa-01.md", uitvoer)
            self.assertEqual(code, 2, uitvoer)

    def test_given_een_overlay_bij_een_bericht_when_genereren_then_gaat_het_voorbeeld_tegen_beide_schemas(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(
                tmp,
                [operatie_aanroep(antwoorden=[{
                    "code": "200", "omschrijving": "Het bericht met zijn overlay.",
                    "schema": "melding", "overlay": ["overlay"],
                    "voorbeeld": {"bestand": "stroom-is-oa-01.md", "schema": "melding", "nummer": 1},
                }])],
                schemas={"melding": schema_melding(), "overlay": schema_overlay()},
                markdown=fence("melding,overlay", {"status": "gelukt", "extra": "drie"}),
            )
            code, uitvoer, document = draai(bestand)
            schema = (document["paths"]["/specificaties/{id}"]["get"]["responses"]["200"]
                      ["content"]["application/json"]["schema"])
            self.assertEqual(schema, {"allOf": [
                {"$ref": "#/components/schemas/melding"},
                {"$ref": "#/components/schemas/overlay"},
            ]})
            self.assertIn("'drie' is not one of", uitvoer)
            self.assertEqual(code, 1, uitvoer)


class DeStandInHetDocument(unittest.TestCase):
    """Of wat de specificatie als voorstel draagt dat ook in het document draagt."""

    def test_given_een_operatie_op_voorstel_when_genereren_then_draagt_het_document_die_stand(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(stand={"kern": "voorstel"})])
            _, uitvoer, document = draai(bestand)
            operatie = document["paths"]["/specificaties/{id}"]["get"]
            self.assertEqual(operatie["x-okx-stand"], "voorstel")
            self.assertIn("Stand: voorstel", operatie["description"])

    def test_given_een_stand_met_een_kwalificatie_when_genereren_then_blijft_de_kwalificatie_staan(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(stand={
                "kern": "vastgelegd",
                "kwalificatie": "de parameter leeruitkomstId staat op voorstel",
                "werkbrieven": ["W3"],
            })])
            _, uitvoer, document = draai(bestand)
            operatie = document["paths"]["/specificaties/{id}"]["get"]
            self.assertEqual(
                operatie["x-okx-stand-kwalificatie"],
                "de parameter leeruitkomstId staat op voorstel",
            )
            self.assertEqual(operatie["x-okx-werkbrieven"], ["IS-OA-01 W3"])
            self.assertIn("de parameter leeruitkomstId staat op voorstel", operatie["description"])

    def test_given_een_parameter_op_voorstel_when_genereren_then_draagt_die_parameter_de_stand(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(parameters=[{
                "naam": "leeruitkomstId", "plaats": "query", "verplicht": False,
                "type": {"type": "string", "format": "uuid"},
                "omschrijving": "De leeruitkomst waarop de lijst filtert.",
                "stand": {"kern": "voorstel", "werkbrieven": ["W3"]},
            }])])
            _, uitvoer, document = draai(bestand)
            parameter = document["paths"]["/specificaties/{id}"]["get"]["parameters"][0]
            self.assertEqual(parameter["x-okx-stand"], "voorstel")
            self.assertIn("Stand: voorstel", parameter["description"])


class DeMeldingen(unittest.TestCase):
    """Waar een melding landt: bij wie haar verstuurt, of bij wie haar ontvangt."""

    def test_given_een_melding_die_het_component_verstuurt_when_genereren_then_staat_zij_onder_webhooks(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(), operatie_melding()])
            _, uitvoer, document = draai(bestand)
            self.assertIn("verwerkingsstatus", document["webhooks"])
            melding = document["webhooks"]["verwerkingsstatus"]["post"]
            self.assertEqual(melding["x-okx-ontvanger"], "curriculum-ontwerptool")
            self.assertEqual(melding["security"], [{"okxAfleverCredentials": []}])
            self.assertNotIn("verwerkingsstatus", document["paths"])

    def test_given_een_melding_die_het_component_ontvangt_when_genereren_then_staat_zij_niet_onder_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(), operatie_melding(
                melder="kernregistratie", ontvanger="onderwijscatalogus", melding="inrichtingsstatus",
            )])
            _, uitvoer, document = draai(bestand)
            self.assertNotIn("webhooks", document)
            ontvangen = document["x-okx-ontvangen-meldingen"]
            self.assertEqual([m["melding"] for m in ontvangen], ["inrichtingsstatus"])
            self.assertEqual(ontvangen[0]["melder"], "kernregistratie")
            self.assertEqual(
                ontvangen[0]["content"]["application/json"]["schema"],
                {"$ref": "#/components/schemas/melding"},
            )
            self.assertNotIn("inrichtingsstatus", document["paths"])

    def test_given_een_bevestiging_zonder_lichaam_when_genereren_then_meldt_het_script_geen_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(), operatie_melding()])
            code, uitvoer, document = draai(bestand)
            antwoord = document["webhooks"]["verwerkingsstatus"]["post"]["responses"]["200"]
            self.assertIn("De bevestiging draagt geen lichaam.", antwoord["description"])
            self.assertNotIn("geen antwoordlichaam", uitvoer)
            self.assertEqual(code, 0, uitvoer)


class TweeVormen(unittest.TestCase):
    """Het document als JSON en als YAML, uit een generatorronde."""

    def test_given_een_document_when_genereren_then_staat_het_er_in_beide_vormen(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            code, uitvoer, document = draai(bestand)
            in_yaml = Path(tmp) / "oas" / "onderwijscatalogus.openapi.yaml"
            self.assertTrue(in_yaml.is_file(), uitvoer)
            self.assertIn("en als YAML:", uitvoer)

    def test_given_de_yaml_vorm_when_terugladen_then_is_zij_hetzelfde_document(self):
        """De twee vormen kunnen niet uiteenlopen, en dat moet aantoonbaar zijn."""
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(), operatie_melding()])
            _, uitvoer, document = draai(bestand)
            in_yaml = Path(tmp) / "oas" / "onderwijscatalogus.openapi.yaml"
            self.assertEqual(gos.yaml.safe_load(in_yaml.read_text(encoding="utf-8")), document)

    def test_given_de_yaml_vorm_when_lezen_then_draagt_zij_geen_python_merken(self):
        """Een veilige dump zonder tags en zonder ankers, want een vreemd werktuig leest mee."""
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            draai(bestand)
            tekst = (Path(tmp) / "oas" / "onderwijscatalogus.openapi.yaml").read_text(encoding="utf-8")
            self.assertNotIn("!!python", tekst)
            self.assertNotIn("&id00", tekst)
            self.assertTrue(tekst.startswith("openapi:"), tekst[:40])

    def test_given_pyyaml_dat_ontbreekt_when_genereren_then_blijft_alleen_de_json_met_een_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            bewaard = gos.yaml
            gos.yaml = None
            try:
                code, uitvoer, document = draai(bestand)
            finally:
                gos.yaml = bewaard
            self.assertFalse((Path(tmp) / "oas" / "onderwijscatalogus.openapi.yaml").exists())
            self.assertIn("PyYAML ontbreekt", " ".join(document["x-okx-openstaand"]))
            self.assertEqual(code, 2, uitvoer)


class DeWerkbrieven(unittest.TestCase):
    """De legenda bij de werkbriefcodes, zodat een code in het document ergens heen wijst."""

    tabel = (
        "# Een stroom\n\n## Werkbrieven\n\n"
        "| Nr | Wat erbij moet | Waar | Versie-impact |\n|---|---|---|---|\n"
        "| W3 | De parameter erbij | onderwijscatalogus.md | MINOR |\n"
        "| W9 | Een waarde in een gesloten lijst | subscription.json | MAJOR |\n"
    )

    def test_given_een_aangehaalde_code_when_genereren_then_draagt_het_document_haar_tekst(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(
                stand={"kern": "voorstel", "werkbrieven": ["W3"]},
            )], markdown=self.tabel)
            code, uitvoer, document = draai(bestand)
            legenda = document["x-okx-werkbrieven"]
            self.assertEqual(list(legenda), ["IS-OA-01 W3"])
            self.assertEqual(legenda["IS-OA-01 W3"]["wat"], "De parameter erbij")
            self.assertEqual(legenda["IS-OA-01 W3"]["versie-impact"], "MINOR")
            self.assertEqual(
                document["paths"]["/specificaties/{id}"]["get"]["x-okx-werkbrieven"],
                ["IS-OA-01 W3"],
            )

    def test_given_een_code_die_niet_wordt_aangehaald_when_genereren_then_blijft_zij_uit_de_legenda(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(
                stand={"kern": "voorstel", "werkbrieven": ["W3"]},
            )], markdown=self.tabel)
            _, _, document = draai(bestand)
            self.assertNotIn("IS-OA-01 W9", document["x-okx-werkbrieven"])

    def test_given_dezelfde_code_in_twee_stromen_when_genereren_then_houdt_de_legenda_hen_apart(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [
                operatie_aanroep(stand={"kern": "voorstel", "werkbrieven": ["W3"]}),
                operatie_aanroep(
                    id="IS-OA-03-O2", stroom="IS-OA-03", pad="/specificaties",
                    stand={"kern": "voorstel", "werkbrieven": ["W3"]},
                ),
            ], markdown=self.tabel)
            map_ = Path(bestand).parent
            (map_ / "stroom-is-oa-03.md").write_text(
                self.tabel.replace("De parameter erbij", "Een ander verzoek"), encoding="utf-8"
            )
            data = json.loads(bestand.read_text(encoding="utf-8"))
            data["stromen"]["IS-OA-03"] = {"bestand": "stroom-is-oa-03.md"}
            bestand.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            _, uitvoer, document = draai(bestand)
            legenda = document["x-okx-werkbrieven"]
            self.assertEqual(sorted(legenda), ["IS-OA-01 W3", "IS-OA-03 W3"])
            self.assertEqual(legenda["IS-OA-03 W3"]["wat"], "Een ander verzoek")

    def test_given_een_code_zonder_tekst_in_de_verdieping_when_genereren_then_meldt_het_script_een_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(
                stand={"kern": "voorstel", "werkbrieven": ["W42"]},
            )], markdown=self.tabel)
            code, uitvoer, document = draai(bestand)
            self.assertEqual(code, 2, uitvoer)
            self.assertIn("IS-OA-01 W42", " ".join(document["x-okx-openstaand"]))
            self.assertNotIn("x-okx-werkbrieven", document)


class DeBestellijst(unittest.TestCase):
    """De lijst waarop een partij zich abonneert, tegen de meldingen die het document publiceert."""

    def spec(self, tmp, waarden, operaties=None):
        return maak_spec(
            tmp,
            operaties or [operatie_abonnement(), operatie_melding()],
            schemas={"melding": schema_melding(), "abonnement": schema_abonnement(waarden)},
        )

    def test_given_een_lijst_die_de_gepubliceerde_melding_draagt_when_genereren_then_blijft_het_zonder_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, uitvoer, document = draai(self.spec(tmp, ("verwerkingsstatus",)))
            self.assertEqual(code, 0, uitvoer)
            self.assertNotIn("abonneert", uitvoer)
            self.assertIn("verwerkingsstatus", document["webhooks"])

    def test_given_een_gepubliceerde_melding_buiten_de_lijst_when_genereren_then_meldt_het_script_een_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, uitvoer, document = draai(self.spec(tmp, ("specificatie-planbaar",)))
            self.assertEqual(code, 2, uitvoer)
            open_ = [g for g in document["x-okx-openstaand"] if "onbereikbaar" in g]
            self.assertEqual(len(open_), 1, document["x-okx-openstaand"])
            self.assertIn("abonnement.events", open_[0])
            self.assertIn("verwerkingsstatus", open_[0])

    def test_given_een_lijstwaarde_zonder_vorm_in_de_specificatie_when_genereren_then_meldt_het_script_een_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, uitvoer, document = draai(
                self.spec(tmp, ("verwerkingsstatus", "specificatie-gewijzigd"))
            )
            self.assertEqual(code, 2, uitvoer)
            open_ = [g for g in document["x-okx-openstaand"] if "nergens een vorm legt" in g]
            self.assertEqual(len(open_), 1, document["x-okx-openstaand"])
            self.assertIn("specificatie-gewijzigd", open_[0])

    def test_given_dezelfde_abonnementsoperatie_in_twee_stromen_when_genereren_then_komt_het_gat_een_keer(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = self.spec(tmp, ("specificatie-planbaar",), operaties=[
                operatie_abonnement(),
                operatie_abonnement(id="IS-OA-03-O6", stroom="IS-OA-03"),
                operatie_melding(),
            ])
            code, uitvoer, document = draai(bestand)
            self.assertEqual(code, 2, uitvoer)
            open_ = [g for g in document["x-okx-openstaand"] if "onbereikbaar" in g]
            self.assertEqual(len(open_), 1, document["x-okx-openstaand"])
            self.assertIn("IS-OA-01-O8, IS-OA-03-O6", open_[0])


class TweeStromenOpEenPad(unittest.TestCase):
    """Wat er gebeurt als twee stromen dezelfde operatie dragen."""

    def test_given_twee_stromen_op_hetzelfde_pad_when_genereren_then_draagt_het_document_een_operatie(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [
                operatie_aanroep(),
                operatie_aanroep(
                    id="IS-OA-03-O2", stroom="IS-OA-03", aanroeper="planningssysteem",
                    parameters=[{
                        "naam": "versie", "plaats": "query", "verplicht": False,
                        "type": {"type": "string"}, "omschrijving": "De versie.",
                    }],
                ),
            ])
            _, uitvoer, document = draai(bestand)
            operatie = document["paths"]["/specificaties/{id}"]["get"]
            self.assertEqual(operatie["x-okx-herkomst"], ["IS-OA-01-O1", "IS-OA-03-O2"])
            self.assertEqual([p["name"] for p in operatie["parameters"]], ["id", "versie"])
            self.assertIn("samengevoegd", uitvoer)

    def test_given_twee_stromen_waarvan_een_het_antwoordlichaam_noemt_when_genereren_then_draagt_het_document_dat_lichaam(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [
                operatie_aanroep(antwoorden=[
                    {"code": "200", "omschrijving": "De structuur.", "schema": "melding"},
                    {"code": "404", "omschrijving": "Onbekend.", "schema": None},
                ]),
                operatie_aanroep(
                    id="IS-OA-03-O2", stroom="IS-OA-03",
                    antwoorden=[
                        {"code": "200", "omschrijving": "De structuur.", "schema": "melding"},
                        {"code": "404", "omschrijving": "Onbekend.", "schema": "bericht",
                         "stand": {"kern": "voorstel", "werkbrieven": ["W15"]}},
                    ],
                ),
            ], schemas={"melding": schema_melding(), "bericht": schema_bericht()},
                markdown=(
                    "# Een stroom\n\n## Werkbrieven\n\n"
                    "| Nr | Wat erbij moet | Waar | Versie-impact |\n|---|---|---|---|\n"
                    "| W15 | Een foutschema | de schemamap | MINOR |\n"
                ))
            # W15 komt uit IS-OA-03, dus staat haar tekst in het bestand van die stroom.
            map_ = Path(bestand).parent
            (map_ / "stroom-is-oa-03.md").write_text(
                (map_ / "stroom-is-oa-01.md").read_text(encoding="utf-8"), encoding="utf-8"
            )
            data = json.loads(bestand.read_text(encoding="utf-8"))
            data["stromen"]["IS-OA-03"] = {"bestand": "stroom-is-oa-03.md"}
            bestand.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            code, uitvoer, document = draai(bestand)
            antwoord = document["paths"]["/specificaties/{id}"]["get"]["responses"]["404"]
            self.assertEqual(
                antwoord["content"]["application/json"]["schema"],
                {"$ref": "#/components/schemas/bericht"},
            )
            self.assertEqual(antwoord["x-okx-stand"], "voorstel")
            self.assertNotIn("geen antwoordlichaam", uitvoer)
            self.assertEqual(code, 0, uitvoer)

    def test_given_twee_stromen_met_een_ander_antwoordlichaam_when_genereren_then_meldt_het_script_een_bevinding(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [
                operatie_aanroep(),
                operatie_aanroep(id="IS-OA-03-O2", stroom="IS-OA-03", antwoorden=[
                    {"code": "200", "omschrijving": "Iets anders.", "schema": "bericht"}
                ]),
            ], schemas={"melding": schema_melding(), "bericht": schema_bericht()})
            code, uitvoer, _ = draai(bestand)
            self.assertIn("twee stromen dragen een ander antwoordlichaam op 200", uitvoer)
            self.assertEqual(code, 1, uitvoer)

    def test_given_een_overlay_in_de_ene_stroom_en_niet_in_de_andere_when_genereren_then_draagt_het_document_de_overlay(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [
                operatie_aanroep(),
                operatie_aanroep(id="IS-OA-03-O2", stroom="IS-OA-03", antwoorden=[
                    {"code": "200", "omschrijving": "De structuur met haar overlay.",
                     "schema": "melding", "overlay": ["overlay"]}
                ]),
            ], schemas={"melding": schema_melding(), "overlay": schema_overlay()})
            code, uitvoer, document = draai(bestand)
            schema = (document["paths"]["/specificaties/{id}"]["get"]["responses"]["200"]
                      ["content"]["application/json"]["schema"])
            self.assertIn("allOf", schema)
            self.assertIn("draagt de ene stroom een overlay over het schema van de andere", uitvoer)
            self.assertEqual(code, 2, uitvoer)


class WatOpenstaat(unittest.TestCase):
    """Of het script meldt wat het niet kon plaatsen."""

    def test_given_een_respons_zonder_schema_when_genereren_then_meldt_het_script_een_gat(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(antwoorden=[
                {"code": "200", "omschrijving": "De structuur.", "schema": "melding"},
                {"code": "404", "omschrijving": "Onbekend.", "schema": None},
            ])])
            code, uitvoer, document = draai(bestand)
            self.assertIn("geen antwoordlichaam", uitvoer)
            self.assertIn("geen antwoordlichaam", " ".join(document["x-okx-openstaand"]))
            self.assertNotIn("content", document["paths"]["/specificaties/{id}"]["get"]["responses"]["404"])
            self.assertEqual(code, 2, uitvoer)

    def test_given_een_gat_op_een_parameter_when_genereren_then_staat_de_reden_in_haar_beschrijving(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep(pad="/specificaties", parameters=[{
                "naam": "status", "plaats": "query", "verplicht": False,
                "type": {"type": "string", "default": "gepubliceerd"},
                "omschrijving": "De status waarop de lijst filtert.",
                "gat": "De operatietabel noemt de standaardwaarde en niet de waardenlijst.",
            }])])
            code, uitvoer, document = draai(bestand)
            parameter = document["paths"]["/specificaties"]["get"]["parameters"][0]
            self.assertIn("Hier staat iets open", parameter["description"])
            self.assertIn("niet de waardenlijst", uitvoer)
            self.assertEqual(code, 2, uitvoer)


class ServersEnBeveiliging(unittest.TestCase):
    """Wat er staat waar de specificatie niets zegt, en wat er staat waar zij dat wel doet."""

    def test_given_geen_servers_in_de_specificatie_when_genereren_then_staat_er_een_plaatshouder_die_dat_zegt(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            _, uitvoer, document = draai(bestand)
            server = document["servers"][0]
            self.assertIn("Plaatshouder", server["description"])
            self.assertIn("De keuze staat open.", server["description"])
            self.assertIn(".invalid", server["variables"]["basis"]["default"])

    def test_given_de_auth_standaard_when_genereren_then_draagt_het_document_oauth2_client_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = maak_spec(tmp, [operatie_aanroep()])
            _, uitvoer, document = draai(bestand)
            schemas = document["components"]["securitySchemes"]
            self.assertEqual(schemas["okxClientCredentials"]["type"], "oauth2")
            self.assertIn("clientCredentials", schemas["okxClientCredentials"]["flows"])
            self.assertIn("De tokenUrl staat open.", schemas["okxClientCredentials"]["description"])
            self.assertEqual(document["security"], [{"okxClientCredentials": []}])


class DeInvoer(unittest.TestCase):
    """Wat het script doet met invoer die het niet kan gebruiken."""

    def test_given_een_operatiebestand_dat_niet_bestaat_when_genereren_then_stopt_het_script(self):
        uitvoer = io.StringIO()
        with contextlib.redirect_stdout(uitvoer), contextlib.redirect_stderr(uitvoer):
            code = gos.main(["--operaties", "/bestaat/niet/operaties.json"])
        self.assertEqual(code, 3)
        self.assertIn("bestaat niet", uitvoer.getvalue())

    def test_given_een_operatiebestand_zonder_componenten_when_genereren_then_stopt_het_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            bestand = Path(tmp) / "operaties.json"
            bestand.write_text(json.dumps({"operaties": []}), encoding="utf-8")
            code, uitvoer, _ = draai(bestand)
            self.assertEqual(code, 3)
            self.assertIn("draagt geen componenten", uitvoer)


class DeInteractiespecificatieVanDezeRepository(unittest.TestCase):
    """De generator op de specificatie in deze repository, zonder een aantal vast te leggen."""

    @unittest.skipUnless(PUBLIC.is_dir(), "de schemamap van Npuls-OKx/Public staat er niet naast")
    def test_given_de_interactiespecificatie_in_deze_repository_when_genereren_then_blijft_het_zonder_bevindingen(self):
        with tempfile.TemporaryDirectory() as tmp:
            uitvoer = io.StringIO()
            with contextlib.redirect_stdout(uitvoer), contextlib.redirect_stderr(uitvoer):
                code = gos.main(["--uit", tmp, "--kort"])
            tekst = uitvoer.getvalue()
            self.assertNotIn("BEVINDING", tekst)
            self.assertIn("geldige OpenAPI: ja", tekst)
            self.assertIn(code, (0, 2), tekst)
            document = json.loads(
                (Path(tmp) / "onderwijscatalogus.openapi.json").read_text(encoding="utf-8")
            )
            self.assertEqual(document["openapi"], "3.1.0")
            for pad in ("/onderwijsspecificaties", "/aanmeldbaar-aanbod", "/abonnementen"):
                self.assertIn(pad, document["paths"])
            self.assertIn("aanbod-aanmeldbaar", document["webhooks"])
            self.assertIn("inrichtingsstatus", [
                m["melding"] for m in document["x-okx-ontvangen-meldingen"]
            ])

    @unittest.skipUnless(PUBLIC.is_dir(), "de schemamap van Npuls-OKx/Public staat er niet naast")
    def test_given_het_gegenereerde_document_when_valideren_then_komt_elke_verwijzing_in_het_document_uit(self):
        with tempfile.TemporaryDirectory() as tmp:
            uitvoer = io.StringIO()
            with contextlib.redirect_stdout(uitvoer), contextlib.redirect_stderr(uitvoer):
                gos.main(["--uit", tmp, "--kort"])
            document = json.loads(
                (Path(tmp) / "onderwijscatalogus.openapi.json").read_text(encoding="utf-8")
            )
            gaten = []
            gos.controleer_verwijzingen(document, "onderwijscatalogus", gaten)
            self.assertEqual([str(g) for g in gaten], [])

    @unittest.skipUnless(PUBLIC.is_dir(), "de schemamap van Npuls-OKx/Public staat er niet naast")
    def test_given_een_vastgelegd_schema_uit_public_when_bundelen_then_draagt_het_document_de_stand_vastgelegd(self):
        with tempfile.TemporaryDirectory() as tmp:
            uitvoer = io.StringIO()
            with contextlib.redirect_stdout(uitvoer), contextlib.redirect_stderr(uitvoer):
                gos.main(["--uit", tmp, "--kort"])
            document = json.loads(
                (Path(tmp) / "onderwijscatalogus.openapi.json").read_text(encoding="utf-8")
            )
            standen = {n: h["stand"] for n, h in document["x-okx-schemas"].items()}
            self.assertEqual(standen["education-specification"], "vastgelegd")
            self.assertEqual(standen["offering-open-for-application"], "voorstel")
            self.assertNotIn(None, standen.values())


if __name__ == "__main__":
    unittest.main()
