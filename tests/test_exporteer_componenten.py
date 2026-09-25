"""Testgevallen voor scripts/exporteer-componenten.py.

Elk geval bouwt een klein ArchiMate-bestand in een tijdelijke map, zodat de test
niet afhangt van het echte model en dat model ook nooit aanraakt.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("exporteer_componenten", WORTEL / "scripts/exporteer-componenten.py")
ec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ec)

MODEL = """<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:archimate="http://www.archimatetool.com/archimate"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="test">
  <folder name="Application" type="application">
    <element xsi:type="archimate:ApplicationComponent" name="Onderwijscatalogus" id="c1">
      <documentation>Een systeem voor het beheren en publiceren van het onderwijsaanbod.</documentation>
    </element>
    <element xsi:type="archimate:ApplicationComponent" name="Planningssysteem" id="c2"/>
    <element xsi:type="archimate:ApplicationService" name="Onderwijs beheer" id="s1">
      <documentation>Het beheren van het onderwijsaanbod.</documentation>
    </element>
    <element xsi:type="archimate:ApplicationService" name="Jaar planning" id="s2"/>
    <element xsi:type="archimate:RealizationRelationship" id="r1" source="c1" target="s1"/>
    <element xsi:type="archimate:RealizationRelationship" id="r2" source="c2" target="s2"/>
  </folder>
</archimate:model>
"""

STROMEN = {"stromen": [{"id": "x1", "van": "Onderwijscatalogus", "naar": "Planningssysteem"}]}


class ExporteerComponentenTests(unittest.TestCase):
    def draai(self, extra=()):
        with tempfile.TemporaryDirectory() as tmp:
            model = Path(tmp) / "model.archimate"
            model.write_text(MODEL, encoding="utf-8")
            stromen = Path(tmp) / "stromen.json"
            stromen.write_text(json.dumps(STROMEN, ensure_ascii=False), encoding="utf-8")
            uit = Path(tmp) / "componenten.json"
            ec.main(["--model", str(model), "--stromen", str(stromen), "--uit", str(uit), "--extra", *extra])
            return json.loads(uit.read_text(encoding="utf-8"))

    def test_given_components_on_the_plate_when_exported_then_definition_and_services_follow(self):
        uit = self.draai()
        namen = [c["naam"] for c in uit["componenten"]]
        self.assertEqual(namen, ["Onderwijscatalogus", "Planningssysteem"])
        oc = uit["componenten"][0]
        self.assertIn("beheren en publiceren", oc["definitie"])
        self.assertEqual([d["naam"] for d in oc["diensten"]], ["Onderwijs beheer"])
        self.assertIn("beheren van het onderwijsaanbod", oc["diensten"][0]["definitie"])

    def test_given_component_without_documentation_when_exported_then_definition_is_empty(self):
        plan = self.draai()["componenten"][1]
        self.assertEqual(plan["definitie"], "")
        self.assertEqual([d["naam"] for d in plan["diensten"]], ["Jaar planning"])

    def test_given_component_outside_the_plate_when_requested_then_it_is_marked(self):
        uit = self.draai(extra=["Intake systeem"])
        intake = next(c for c in uit["componenten"] if c["naam"] == "Intake systeem")
        self.assertIn("staat niet als applicatiecomponent", intake["opmerking"])
        self.assertEqual(intake["diensten"], [])


if __name__ == "__main__":
    unittest.main()
