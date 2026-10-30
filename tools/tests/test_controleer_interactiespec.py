"""Testgevallen voor tools/scripts/controleer-interactiespec.py.

Elk geval bouwt zijn eigen interactiespecificatie op: een tijdelijke map met een
markdown-bestand en een map `schemas/` ernaast. De verwachting volgt daarmee uit het
fixture en niet uit de inhoud van de repository, en elk negatief geval breekt precies een
ding. Het laatste geval draait de controle op de interactiespecificatie in deze repository
en toetst de uitkomst zonder een aantal vast te leggen dat veroudert zodra de specificatie
groeit.
"""

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
SPECIFICATIE = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod"

spec = importlib.util.spec_from_file_location(
    "controleer_interactiespec", WORTEL / "tools/scripts/controleer-interactiespec.py"
)
ci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ci)


def schema_melding():
    """Een klein schema met een gesloten enum en een verplichte sleutel."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/melding/voorstel",
        "title": "Notification",
        "DutchName": "Melding",
        "type": "object",
        "required": ["status"],
        "properties": {
            "status": {"enum": ["ontvangen", "gelukt"], "DutchName": "status"},
            "reference": {
                "$ref": "https://okx.npuls.nl/schema/verwijzing/voorstel",
                "DutchName": "verwijzing",
            },
        },
    }


def schema_verwijzing():
    """Het schema waarnaar schema_melding verwijst, zodat ook de verwijzing meeloopt."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/verwijzing/voorstel",
        "title": "Reference",
        "DutchName": "Verwijzing",
        "type": "object",
        "required": ["objectId"],
        "properties": {"objectId": {"type": "string", "format": "uuid", "DutchName": "objectId"}},
    }


def schema_overlay():
    """Een overlay die een sleutel toevoegt die het dragende schema niet kent."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://okx.npuls.nl/schema/melding-overlay/voorstel",
        "title": "Notification overlay",
        "DutchName": "Melding-overlay",
        "type": "object",
        "properties": {"duration": {"type": "number", "DutchName": "duur"}},
    }


class Controle(unittest.TestCase):

    def specificatie(self, blokken, schemas=None):
        """Een tijdelijke interactiespecificatie met de meegegeven codeblokken en schema's.

        Een blok is een paar van de aanduiding achter de taal en de payload als tekst; een
        aanduiding zonder inhoud levert een codeblok zonder schema-aanduiding op.
        """
        map_ = Path(tempfile.mkdtemp())
        (map_ / "schemas").mkdir()
        for naam, inhoud in (schemas or {}).items():
            (map_ / "schemas" / f"{naam}.json").write_text(
                json.dumps(inhoud), encoding="utf-8"
            )
        regels = ["# Proefspecificatie", ""]
        for aanduiding, payload in blokken:
            taal = "json" + (f" schema={aanduiding}" if aanduiding else "")
            regels += [f"```{taal}", payload, "```", ""]
        (map_ / "stroom-proef.md").write_text("\n".join(regels), encoding="utf-8")
        return map_

    def controleer(self, map_):
        """De controle draaien op een map, met alleen de schema's van die map als grond."""
        return ci.controleer(map_, [map_ / "schemas"])

    def test_given_a_payload_that_matches_its_schema_when_checked_then_no_findings(self):
        map_ = self.specificatie(
            [("melding", '{"status": "gelukt"}')], {"melding": schema_melding()}
        )
        uitkomsten, gaten, bevindingen = self.controleer(map_)
        self.assertEqual(bevindingen, [])
        self.assertEqual(gaten, [])
        self.assertEqual([stand for _, _, stand in uitkomsten], ["valideert"])

    def test_given_a_payload_that_breaks_its_schema_when_checked_then_a_finding(self):
        map_ = self.specificatie(
            [("melding", '{"status": "geslaagd"}')], {"melding": schema_melding()}
        )
        uitkomsten, _, bevindingen = self.controleer(map_)
        self.assertEqual([stand for _, _, stand in uitkomsten], ["valideert niet"])
        self.assertEqual(len(bevindingen), 1)
        self.assertIn("/status", bevindingen[0])

    def test_given_a_payload_without_a_schema_marker_when_checked_then_reported_as_a_gap(self):
        map_ = self.specificatie(
            [("", '{"status": "gelukt"}')], {"melding": schema_melding()}
        )
        uitkomsten, gaten, bevindingen = self.controleer(map_)
        self.assertEqual(uitkomsten, [])
        self.assertEqual(bevindingen, [])
        self.assertEqual(len(gaten), 1)
        self.assertTrue(gaten[0].plek.endswith("stroom-proef.md:3"))

    def test_given_a_marker_naming_a_missing_schema_when_checked_then_a_finding(self):
        map_ = self.specificatie(
            [("bestaat-niet", '{"status": "gelukt"}')], {"melding": schema_melding()}
        )
        uitkomsten, _, bevindingen = self.controleer(map_)
        self.assertEqual([stand for _, _, stand in uitkomsten], ["schema ontbreekt"])
        self.assertEqual(len(bevindingen), 1)
        self.assertIn("staat in geen van de schemamappen", bevindingen[0])

    def test_given_a_payload_key_that_no_schema_declares_when_checked_then_a_finding(self):
        """Het gat dat Npuls-OKx/Public#132 aanwijst: een sleutel buiten elk schema.

        Het schema zet `additionalProperties` niet op `false`, dus laat de validatie de
        sleutel door. De sleuteltoets meldt hem.
        """
        map_ = self.specificatie(
            [("melding", '{"status": "gelukt", "doorlooptijd": "3 dagen"}')],
            {"melding": schema_melding()},
        )
        uitkomsten, _, bevindingen = self.controleer(map_)
        self.assertEqual([stand for _, _, stand in uitkomsten], ["valideert"])
        self.assertEqual(len(bevindingen), 1)
        self.assertIn("/doorlooptijd", bevindingen[0])

    def test_given_two_schemas_on_one_payload_when_checked_then_both_cover_their_keys(self):
        map_ = self.specificatie(
            [("melding,melding-overlay", '{"status": "gelukt", "duration": 3}')],
            {"melding": schema_melding(), "melding-overlay": schema_overlay()},
        )
        uitkomsten, _, bevindingen = self.controleer(map_)
        self.assertEqual(bevindingen, [])
        self.assertEqual([stand for _, _, stand in uitkomsten], ["valideert", "valideert"])

    def test_given_a_schema_that_refers_to_another_schema_when_checked_then_the_reference_applies(self):
        map_ = self.specificatie(
            [("melding", '{"status": "gelukt", "reference": {"objectId": "geen-uuid"}}')],
            {"melding": schema_melding(), "verwijzing": schema_verwijzing()},
        )
        _, _, bevindingen = self.controleer(map_)
        self.assertEqual(len(bevindingen), 1)
        self.assertIn("/reference/objectId", bevindingen[0])

    def test_given_a_payload_that_is_not_valid_json_when_checked_then_a_finding(self):
        map_ = self.specificatie(
            [("melding", '{"status": "gelukt",}')], {"melding": schema_melding()}
        )
        uitkomsten, _, bevindingen = self.controleer(map_)
        self.assertEqual([stand for _, _, stand in uitkomsten], ["onleesbaar"])
        self.assertIn("geen geldige json", bevindingen[0])

    def test_given_a_fenced_block_that_is_not_json_when_checked_then_it_is_left_alone(self):
        map_ = Path(tempfile.mkdtemp())
        (map_ / "schemas").mkdir()
        (map_ / "stroom-proef.md").write_text(
            "# Proef\n\n```mermaid\nflowchart LR\n  A --> B\n```\n", encoding="utf-8"
        )
        uitkomsten, gaten, bevindingen = self.controleer(map_)
        self.assertEqual((uitkomsten, gaten, bevindingen), ([], [], []))


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        """De controle als opdrachtregel draaien, met de uitvoer buiten de testuitvoer."""
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return ci.main(argv)

    def op(self, blokken, schemas=None):
        map_ = Controle().specificatie(blokken, schemas)
        return self.draai(
            [str(map_), "--schemas", str(map_ / "schemas"), "--public-schemas", str(map_), "--kort"]
        )

    def test_given_only_valid_payloads_when_run_then_exit_code_zero(self):
        self.assertEqual(
            self.op([("melding", '{"status": "gelukt"}')], {"melding": schema_melding()}), 0
        )

    def test_given_an_invalid_payload_when_run_then_exit_code_one(self):
        self.assertEqual(
            self.op([("melding", '{"status": "geslaagd"}')], {"melding": schema_melding()}), 1
        )

    def test_given_a_payload_without_a_marker_when_run_then_exit_code_two(self):
        self.assertEqual(
            self.op([("", '{"status": "gelukt"}')], {"melding": schema_melding()}), 2
        )

    def test_given_a_map_that_does_not_exist_when_run_then_exit_code_three(self):
        map_ = Path(tempfile.mkdtemp()) / "bestaat-niet"
        self.assertEqual(self.draai([str(map_), "--kort"]), 3)


class Herkenning(unittest.TestCase):

    def test_given_a_marker_behind_the_language_when_read_then_the_names_are_split(self):
        map_ = Controle().specificatie([("een,twee", "{}")])
        payloads = ci.lees_payloads(map_)
        self.assertEqual([p.namen for p in payloads], [["een", "twee"]])

    def test_given_a_marker_with_a_json_suffix_when_resolved_then_the_file_is_found(self):
        map_ = Controle().specificatie([], {"melding": schema_melding()})
        gevonden = ci.schemabestand("melding.json", [map_ / "schemas"])
        self.assertEqual(gevonden, map_ / "schemas" / "melding.json")

    def test_given_an_alfa_label_in_a_reference_when_resolved_then_the_file_is_found(self):
        map_ = Controle().specificatie([], {"melding": schema_melding()})
        register = ci.maak_register([map_ / "schemas"])
        opgelost = register.get_or_retrieve("https://okx.npuls.nl/schema/melding/voorstel")
        self.assertEqual(opgelost.value.contents["title"], "Notification")


class InDezeRepository(unittest.TestCase):
    """De controle op de interactiespecificatie onderwijsaanbod zelf."""

    def test_given_the_specification_in_this_repository_when_checked_then_no_findings(self):
        public = WORTEL / ci.PUBLIC_STANDAARD
        if not public.is_dir():
            # De schema's van deze snede verwijzen naar de vastgelegde schema's in
            # Npuls-OKx/Public. Zonder die werkmap valt er niets te valideren, en een
            # bevinding zou dan loos alarm zijn.
            self.skipTest(f"{ci.PUBLIC_STANDAARD} ontbreekt; zet Npuls-OKx/Public ernaast")
        mappen = [SPECIFICATIE / "schemas", public]
        uitkomsten, gaten, bevindingen = ci.controleer(SPECIFICATIE, mappen)
        self.assertEqual(bevindingen, [])
        self.assertEqual([p.plek for p in gaten], [])
        self.assertTrue(uitkomsten, "de specificatie draagt geen enkele voorbeeldpayload")
        self.assertEqual(
            [stand for _, _, stand in uitkomsten if stand != "valideert"], []
        )


if __name__ == "__main__":
    unittest.main()
