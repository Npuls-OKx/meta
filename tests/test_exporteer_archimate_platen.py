"""Testgevallen voor scripts/exporteer-archimate-platen.py.

De geometrie (knikpunten, rand, langste segment, objectenlaag) wordt getoetst op
een fixture-model. De aanroep van Archi zelf is een integratietest die alleen
draait als Archi in de container staat, en die controleert dat het model
byte-gelijk blijft.
"""

import hashlib
import importlib.util
import json
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("exporteer_archimate_platen", WORTEL / "scripts/exporteer-archimate-platen.py")
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)

XSI = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate"'
PNG_1X1 = bytes.fromhex("89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4890000000d49444154789c6360000002000154a24f5d0000000049454e44ae426082")


def model_xml(view_kinderen, viewnaam="Testview"):
    elementen = [("A", "ApplicationComponent", "A"), ("B", "ApplicationComponent", "B")]
    e = "".join(f'<element xsi:type="archimate:{s}" name="{n}" id="{i}"/>' for i, s, n in elementen)
    r = '<element xsi:type="archimate:FlowRelationship" id="rAB" source="A" target="B"/><element xsi:type="archimate:ServingRelationship" id="sAB" source="A" target="B"/>'
    return (f'<?xml version="1.0" encoding="UTF-8"?><archimate:model {XSI} name="t" id="m" version="5.0.0">'
            f'<folder name="Application" id="f1" type="application">{e}</folder><folder name="Relations" id="f2" type="relations">{r}</folder>'
            f'<folder name="Views" id="f3" type="diagrams"><element xsi:type="archimate:ArchimateDiagramModel" name="{viewnaam}" id="v1">{view_kinderen}</element></folder></archimate:model>')


def obj(oid, element, x, y, w=100, h=50, conns="", kinderen=""):
    return f'<child xsi:type="archimate:DiagramObject" id="{oid}" archimateElement="{element}"><bounds x="{x}" y="{y}" width="{w}" height="{h}"/>{conns}{kinderen}</child>'


def conn(doel, relatie, bendpoints=""):
    return f'<sourceConnection xsi:type="archimate:Connection" id="c-{relatie}" source="x" target="{doel}" archimateRelationship="{relatie}">{bendpoints}</sourceConnection>'


class GeometrieTests(unittest.TestCase):
    def schrijf(self, xml):
        map_ = tempfile.TemporaryDirectory()
        self.addCleanup(map_.cleanup)
        pad = Path(map_.name) / "model.archimate"
        pad.write_text(xml, encoding="utf-8")
        return pad

    def test_given_bendpoint_when_path_computed_then_average_of_start_and_end_offsets(self):
        # A midden (50,25), B midden (350,25); bendpoint start (100,80) end (-200,80): Archi tekent op ((50+100+350-200)/2, (25+80+25+80)/2) = (150,105)
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0, conns=conn("oB", "rAB", '<bendpoint startX="100" startY="80" endX="-200" endY="80"/>')) + obj("oB", "B", 300, 0)))
        knopen, connecties, _ = ep.lees_view(pad, "Testview")
        punten = ep.pad(connecties[0], knopen)
        self.assertEqual((round(punten[1][0]), round(punten[1][1])), (150, 105))

    def test_given_bendpoint_when_only_start_offset_used_then_differs(self):
        # bron- en doeloffset wijzen naar verschillende punten; alleen de bronoffset gebruiken geeft (150, 105), Archi rekent (200, 105)
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0, conns=conn("oB", "rAB", '<bendpoint startX="100" startY="80" endX="-100" endY="80"/>')) + obj("oB", "B", 300, 0)))
        knopen, connecties, _ = ep.lees_view(pad, "Testview")
        punten = ep.pad(connecties[0], knopen)
        alleen_start = (50 + 100, 25 + 80)  # de oude PoC-formule
        self.assertEqual((round(punten[1][0]), round(punten[1][1])), (200, 105))
        self.assertNotEqual((round(punten[1][0]), round(punten[1][1])), alleen_start)

    def test_given_straight_connection_when_path_computed_then_endpoints_on_element_edges(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0, conns=conn("oB", "rAB")) + obj("oB", "B", 300, 0)))
        knopen, connecties, _ = ep.lees_view(pad, "Testview")
        punten = ep.pad(connecties[0], knopen)
        self.assertEqual((round(punten[0][0]), round(punten[0][1])), (100, 25))
        self.assertEqual((round(punten[-1][0]), round(punten[-1][1])), (300, 25))

    def test_given_nested_element_when_read_then_absolute_position_adds_parent_offset(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 100, 100, w=200, h=200, kinderen=obj("oB", "B", 10, 10))))
        knopen, _, _ = ep.lees_view(pad, "Testview")
        self.assertEqual((knopen["oB"]["x"], knopen["oB"]["y"]), (110, 110))

    def test_given_three_segments_when_longest_chosen_then_its_midpoint(self):
        punten = [(0, 0), (10, 0), (10, 100), (20, 100)]
        self.assertEqual(ep.midden_langste_segment(punten), (10, 50))

    def test_given_objects_when_overlay_made_then_one_box_per_flow_with_object(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0, conns=conn("oB", "rAB") + conn("oB", "sAB")) + obj("oB", "B", 300, 0)))
        png = pad.parent / "p.png"
        png.write_bytes(PNG_1X1)
        svg, aantal, ongebruikt = ep.met_objecten(pad, "Testview", png, {"rAB": "Opleidingaanbod", "sAB": "Niet een flow", "xx": "Bestaat niet"})
        self.assertEqual(aantal, 1)
        self.assertEqual(ongebruikt, ["sAB", "xx"])
        self.assertIn("Opleidingaanbod", svg)
        ET.fromstring(svg)

    def test_given_overlay_when_made_then_canvas_matches_archi_export_extent(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 40, 60) + obj("oB", "B", 300, 60)))
        png = pad.parent / "p.png"
        png.write_bytes(PNG_1X1)
        svg, _, _ = ep.met_objecten(pad, "Testview", png, {})
        wortel = ET.fromstring(svg)
        # extent 40..400 bij 60..110, plus 10 px marge rondom: 380 bij 70
        self.assertEqual((wortel.get("width"), wortel.get("height")), ("380", "70"))

    def test_given_special_characters_when_overlay_made_then_escaped(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0, conns=conn("oB", "rAB")) + obj("oB", "B", 300, 0)))
        png = pad.parent / "p.png"
        png.write_bytes(PNG_1X1)
        svg, _, _ = ep.met_objecten(pad, "Testview", png, {"rAB": "Verzoek tot Aanbod & <intekening>"})
        ET.fromstring(svg)

    def test_given_unknown_view_when_run_then_exit_lists_views(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0)))
        with self.assertRaises(SystemExit) as fout:
            ep.main(["--model", str(pad), "--view", "Bestaat niet", "--uit", str(pad.parent / "u.png")])
        self.assertIn("Testview", str(fout.exception))

    def test_given_mismatched_view_and_uit_when_run_then_exit(self):
        pad = self.schrijf(model_xml(obj("oA", "A", 0, 0)))
        with self.assertRaises(SystemExit):
            ep.main(["--model", str(pad), "--view", "Testview", "--view", "Testview", "--uit", str(pad.parent / "u.png")])

    def test_given_missing_model_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            self.assertEqual(ep.main(["--model", str(Path(map_) / "geen.archimate"), "--view", "x", "--uit", str(Path(map_) / "u.png")]), 2)


@unittest.skipUnless(shutil.which("archi") or Path("/opt/Archi/Archi").exists(), "Archi niet in deze container")
class ArchiIntegratieTests(unittest.TestCase):
    def test_given_real_model_when_exported_then_png_written_and_model_unchanged(self):
        model = WORTEL / "architecture/model/model.archimate"
        voor = hashlib.sha256(model.read_bytes()).hexdigest()
        with tempfile.TemporaryDirectory() as map_:
            doel = Path(map_) / "plaat.png"
            code = ep.main(["--model", str(model), "--view", "OKx hoofdplaat v1.7<concept> (zonder context applicaties)", "--uit", str(doel)])
            self.assertEqual(code, 0)
            self.assertTrue(doel.exists() and doel.stat().st_size > 10000)
            self.assertEqual(doel.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(voor, hashlib.sha256(model.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
