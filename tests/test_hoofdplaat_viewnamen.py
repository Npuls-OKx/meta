"""Testgevallen voor de viewnamen waarmee de scripts de hoofdplaat in het model zoeken.

De scripts zoeken een view op naam. Deze gevallen toetsen daarom tegen het echte
model in de repository: hernoemt de modelleur een view in Archi, dan valt dat hier
direct op (#393).
"""

import importlib.util
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"


def laad(naam, bestand):
    spec = importlib.util.spec_from_file_location(naam, WORTEL / "scripts" / bestand)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def viewnamen():
    return {e.get("name") for e in ET.parse(MODEL).getroot().iter("element")
            if e.get(XSI) == "archimate:ArchimateDiagramModel"}


class ViewnaamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.views = viewnamen()

    def gevonden(self, naam, bestand):
        view = laad(naam, bestand).VIEW
        self.assertTrue(view in self.views, f"view niet in het model: {view}")

    def test_given_model_when_default_view_of_exporteer_archimate_view_then_found(self):
        self.gevonden("exporteer_archimate_view", "exporteer-archimate-view.py")

    def test_given_model_when_default_view_of_teken_hoofdplaat_highlight_then_found(self):
        self.gevonden("teken_hoofdplaat_highlight", "teken-hoofdplaat-highlight.py")

    def test_given_model_when_default_view_of_teken_hoofdplaat_ruim_then_found(self):
        self.gevonden("teken_hoofdplaat_ruim", "teken-hoofdplaat-ruim.py")

    def test_given_model_when_hoofdplaat_views_listed_then_none_left_on_1_7(self):
        oud = sorted(v for v in self.views if "v1.7<" in v or "obv 1.7)" in v)
        self.assertEqual(oud, [])


class StroomSvsSksTests(unittest.TestCase):
    def test_given_model_when_hoofdplaat_exported_then_flow_svs_to_sks_present(self):
        ex = laad("exporteer_archimate_view", "exporteer-archimate-view.py")
        stromen = ex.exporteer(MODEL, ex.VIEW)["stromen"]
        self.assertIn(("Student volg systeem (SVS)", "Student Keuze Systeem (SKS)"),
                      {(s["van"], s["naar"]) for s in stromen})


if __name__ == "__main__":
    unittest.main()
