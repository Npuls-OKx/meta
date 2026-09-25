"""Testgevallen voor scripts/exporteer-conceptplaat.py.

Elke verwachting komt uit het fixture-model in de test zelf. Het echte model wordt
alleen gebruikt om te toetsen dat het script het niet wijzigt.
"""

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("exporteer_conceptplaat", WORTEL / "scripts/exporteer-conceptplaat.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

XSI = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate"'


def model_xml(elementen, relaties, view_kinderen, viewnaam="Conceptview"):
    e = "".join(f'<element xsi:type="archimate:{s}" name="{n}" id="{i}"/>' for i, s, n in elementen)
    r = "".join(f'<element xsi:type="archimate:{s}Relationship" id="{i}" source="{b}" target="{d}"{" name=%s" % json.dumps(n, ensure_ascii=False) if n else ""}/>'
                for i, s, b, d, n in relaties)
    return (f'<?xml version="1.0" encoding="UTF-8"?><archimate:model {XSI} name="t" id="m" version="5.0.0">'
            f'<folder name="Business" id="f1" type="business">{e}</folder>'
            f'<folder name="Relations" id="f2" type="relations">{r}</folder>'
            f'<folder name="Views" id="f3" type="diagrams"><element xsi:type="archimate:ArchimateDiagramModel" name="{viewnaam}" id="v1">'
            f'{view_kinderen}</element></folder></archimate:model>')


def obj(oid, element, conns="", kinderen=""):
    return f'<child xsi:type="archimate:DiagramObject" id="{oid}" archimateElement="{element}"><bounds x="0" y="0" width="120" height="55"/>{conns}{kinderen}</child>'


def conn(cid, doel, relatie):
    return f'<sourceConnection xsi:type="archimate:Connection" id="{cid}" source="x" target="{doel}" archimateRelationship="{relatie}"/>'


class Fixture:
    def __init__(self, xml, test):
        self.map = tempfile.TemporaryDirectory()
        test.addCleanup(self.map.cleanup)
        self.pad = Path(self.map.name) / "model.archimate"
        self.pad.write_text(xml, encoding="utf-8")


class ExporteerConceptplaatTests(unittest.TestCase):
    def basis(self):
        elementen = [("G", "Grouping", "Onderwijskundig ontwerp"), ("P", "BusinessObject", "Onderwijsplan"),
                     ("L", "BusinessObject", "Leerdoel  "), ("U", "BusinessObject", "Leeruitkomst"),
                     ("K", "BusinessObject", "Kerntaak"), ("N", "Note", "")]
        relaties = [("rGP", "Aggregation", "G", "P", ""), ("rPL", "Aggregation", "P", "L", ""),
                    ("rLU", "Association", "L", "U", "Heeft één of meer"), ("rKL", "Association", "K", "L", "Word onderwijskundig vertaald tot"),
                    ("rKU", "Association", "K", "U", "niet op de view")]
        view = (f'<child xsi:type="archimate:DiagramObject" id="oG" archimateElement="G"><bounds x="0" y="0" width="600" height="300"/>'
                + conn("cGP", "oP", "rGP")
                + obj("oP", "P", conn("cPL", "oL", "rPL"), obj("oL", "L", conn("cLU", "oU", "rLU")) + obj("oU", "U"))
                + '</child>'
                + obj("oK", "K", conn("cKL", "oL", "rKL"))
                + '<child xsi:type="archimate:Note" id="oN"><bounds x="0" y="0" width="10" height="10"/></child>')
        return Fixture(model_xml(elementen, relaties, view), self)

    def test_given_view_with_grouping_when_exported_then_objects_carry_group_and_grouping_is_no_object(self):
        uit = ex.exporteer(self.basis().pad, "Conceptview")
        namen = {o["naam"]: o for o in uit["objecttypen"]}
        self.assertEqual(set(namen), {"Onderwijsplan", "Leerdoel", "Leeruitkomst", "Kerntaak"})
        self.assertEqual(namen["Leerdoel"]["groep"], "Onderwijskundig ontwerp")
        self.assertIsNone(namen["Kerntaak"]["groep"])

    def test_given_relations_when_exported_then_only_those_drawn_on_view_and_without_groupings(self):
        uit = ex.exporteer(self.basis().pad, "Conceptview")
        rel = {(r["soort"], r["van"], r["naar"], r["label"]) for r in uit["relaties"]}
        self.assertIn(("Association", "Kerntaak", "Leerdoel", "Word onderwijskundig vertaald tot"), rel)
        self.assertIn(("Association", "Leerdoel", "Leeruitkomst", "Heeft één of meer"), rel)
        self.assertIn(("Aggregation", "Onderwijsplan", "Leerdoel", None), rel)
        self.assertNotIn(("Association", "Kerntaak", "Leeruitkomst", "niet op de view"), rel)
        self.assertFalse(any("Onderwijskundig ontwerp" in (r["van"], r["naar"]) for r in uit["relaties"]))

    def test_given_whitespace_in_names_when_exported_then_normalised(self):
        uit = ex.exporteer(self.basis().pad, "Conceptview")
        self.assertIn("Leerdoel", [o["naam"] for o in uit["objecttypen"]])

    def test_given_unknown_view_when_exported_then_exit_with_available_views(self):
        with self.assertRaises(SystemExit) as cm:
            ex.exporteer(self.basis().pad, "Bestaat niet")
        self.assertIn("Conceptview", str(cm.exception))

    def test_given_same_model_twice_when_exported_then_identical_and_sorted(self):
        f = self.basis()
        a, b = ex.exporteer(f.pad, "Conceptview"), ex.exporteer(f.pad, "Conceptview")
        self.assertEqual(a, b)
        self.assertEqual([o["naam"] for o in a["objecttypen"]], sorted(o["naam"] for o in a["objecttypen"]))

    def test_given_real_model_when_exported_then_model_file_unchanged(self):
        pad = WORTEL / "architecture/model/model.archimate"
        voor = hashlib.sha256(pad.read_bytes()).hexdigest()
        uit = ex.exporteer(pad, ex.VIEW)
        self.assertEqual(hashlib.sha256(pad.read_bytes()).hexdigest(), voor)
        self.assertIn("Onderwijsvorm specificatie", [o["naam"] for o in uit["objecttypen"]])

    def test_given_missing_model_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            self.assertEqual(ex.main(["--model", str(Path(map_) / "x.archimate"), "--uit", str(Path(map_) / "u.json")]), 2)


if __name__ == "__main__":
    unittest.main()
