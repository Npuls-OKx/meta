"""Testgevallen voor de viewnamen in het model.

De scripts zoeken een view op naam. Deze gevallen toetsen daarom tegen het echte
model in de repository: hernoemt de modelleur een view in Archi, dan valt dat hier
direct op (#393). Een viewnaam wordt ook een bestandsnaam, bij de export uit Archi
en bij de platen in de repository; daarom draagt hij alleen tekens die dat overal
kunnen (#405, de conventie staat in architecture/model/README.md).
"""

import importlib.util
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
# letters, cijfers, spatie, punt, haakjes, koppelteken en &: geldig als bestandsnaam op Windows, macOS
# en Linux, en zonder aanhalingstekens bruikbaar op de commandoregel
CONVENTIE = re.compile(r"[A-Za-z0-9 .()&-]+")
# oude views die buiten de conventie vallen en met opzet zo blijven, op id zodat een hernoeming ze niet raakt
UITGEZONDERD = {"id-140ced0690894291acfbd86453fa6e57": "oude MOKA-view in Views > Koppelvlakken > OKE, uitgezonderd door de modelleur (#405)"}


def laad(naam, bestand):
    spec = importlib.util.spec_from_file_location(naam, WORTEL / "tools" / "scripts" / bestand)
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


class NaamconventieTests(unittest.TestCase):
    def test_given_model_when_every_view_name_checked_then_only_allowed_characters(self):
        views = [e for e in ET.parse(MODEL).getroot().iter("element") if e.get(XSI) == "archimate:ArchimateDiagramModel"]
        fout = sorted(e.get("name") for e in views
                      if e.get("id") not in UITGEZONDERD and not CONVENTIE.fullmatch(e.get("name") or ""))
        self.assertEqual(fout, [], "viewnamen buiten de conventie in architecture/model/README.md")

    def test_given_exception_list_when_checked_then_each_id_still_in_the_model(self):
        ids = {e.get("id") for e in ET.parse(MODEL).getroot().iter("element") if e.get(XSI) == "archimate:ArchimateDiagramModel"}
        self.assertEqual(set(UITGEZONDERD) - ids, set())

    def test_given_names_that_break_a_file_name_when_checked_then_rejected(self):
        for naam in ("OKx hoofdplaat v1.7a<concept>", "Koppelvlak: SKS", "a/b", 'a"b', "a|b", "a?b", "a*b", "a,b", "a+b"):
            self.assertIsNone(CONVENTIE.fullmatch(naam), naam)
        self.assertIsNotNone(CONVENTIE.fullmatch("Koppelvlak SIS (KRS-SVS) (obv 1.7a)"))


class StroomSvsSksTests(unittest.TestCase):
    def test_given_model_when_hoofdplaat_exported_then_flow_svs_to_sks_present(self):
        ex = laad("exporteer_archimate_view", "exporteer-archimate-view.py")
        stromen = ex.exporteer(MODEL, ex.VIEW)["stromen"]
        self.assertIn(("Student volg systeem (SVS)", "Student Keuze Systeem (SKS)"),
                      {(s["van"], s["naar"]) for s in stromen})


if __name__ == "__main__":
    unittest.main()
