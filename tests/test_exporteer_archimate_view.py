"""Testgevallen voor scripts/exporteer-archimate-view.py.

Elke verwachting komt uit het fixture-model in de test zelf, niet uit het
model in de repository. Het echte model wordt alleen gebruikt om te toetsen
dat het script het niet wijzigt.
"""

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("exporteer_archimate_view", WORTEL / "scripts/exporteer-archimate-view.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

XSI = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate"'


def model_xml(elementen, relaties, view_kinderen, viewnaam="Testview"):
    """Een minimaal Archi-bestand. elementen: [(id, soort, naam)], relaties: [(id, soort, bron, doel, naam)]."""
    e = "".join(f'<element xsi:type="archimate:{s}" name="{n}" id="{i}"/>' for i, s, n in elementen)
    r = "".join(f'<element xsi:type="archimate:{s}Relationship" id="{i}" source="{b}" target="{d}"{" name=%s" % json.dumps(n) if n else ""}/>'
                for i, s, b, d, n in relaties)
    return (f'<?xml version="1.0" encoding="UTF-8"?><archimate:model {XSI} name="t" id="m" version="5.0.0">'
            f'<folder name="Business" id="f1" type="business">{e}</folder>'
            f'<folder name="Relations" id="f2" type="relations">{r}</folder>'
            f'<folder name="Views" id="f3" type="diagrams"><element xsi:type="archimate:ArchimateDiagramModel" name="{viewnaam}" id="v1">'
            f'{view_kinderen}</element></folder></archimate:model>')


def obj(oid, element, soort="DiagramObject", conns="", kinderen="", x=0, y=0):
    return (f'<child xsi:type="archimate:{soort}" id="{oid}" archimateElement="{element}">'
            f'<bounds x="{x}" y="{y}" width="120" height="55"/>{conns}{kinderen}</child>')


def conn(cid, doel, relatie, label=None):
    feature = f'<feature name="labelExpression" value="{label}"/>' if label else ""
    return f'<sourceConnection xsi:type="archimate:Connection" id="{cid}" source="x" target="{doel}" archimateRelationship="{relatie}">{feature}</sourceConnection>'


class Fixture:
    """Een tijdelijk modelbestand dat aan het einde van de test wordt opgeruimd."""

    def __init__(self, xml, test):
        self.map = tempfile.TemporaryDirectory()
        test.addCleanup(self.map.cleanup)
        self.pad = Path(self.map.name) / "model.archimate"
        self.pad.write_text(xml, encoding="utf-8")


class ExporteerTests(unittest.TestCase):
    def basis(self):
        elementen = [("A", "ApplicationComponent", "Systeem A"), ("B", "ApplicationComponent", "Systeem B"),
                     ("C", "ApplicationComponent", "Systeem C"), ("J", "Junction", "Junction")]
        relaties = [("rAB", "Flow", "A", "B", ""), ("rAB2", "Flow", "A", "B", "Tweede"),
                    ("rAJ", "Flow", "A", "J", ""), ("rJB", "Flow", "J", "B", ""), ("rJC", "Flow", "J", "C", ""),
                    ("rAC", "Serving", "A", "C", "")]
        return elementen, relaties

    def test_given_view_with_n_flows_when_exported_then_n_entries(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB", "Eerste") + conn("c2", "oB", "rAB2")) + obj("oB", "B") + obj("oC", "C")
        f = Fixture(model_xml(elementen, relaties, view), self)
        uit = ex.exporteer(f.pad, "Testview")["stromen"]
        self.assertEqual(len(uit), 2)
        self.assertEqual({s["id"] for s in uit}, {"rAB", "rAB2"})
        self.assertTrue(all(s["van"] == "Systeem A" and s["naar"] == "Systeem B" for s in uit))

    def test_given_flow_via_junction_when_exported_then_resolved_to_components(self):
        elementen, relaties = self.basis()
        view = (obj("oA", "A", conns=conn("c1", "oJ", "rAJ")) + obj("oB", "B") + obj("oC", "C")
                + obj("oJ", "J", soort="DiagramObject", conns=conn("c2", "oB", "rJB") + conn("c3", "oC", "rJC")))
        f = Fixture(model_xml(elementen, relaties, view), self)
        uit = ex.exporteer(f.pad, "Testview")["stromen"]
        self.assertEqual({(s["van"], s["naar"]) for s in uit}, {("Systeem A", "Systeem B"), ("Systeem A", "Systeem C")})
        self.assertTrue(all(s["id"] == "rAJ" for s in uit))

    def test_given_two_flows_same_van_naar_when_exported_then_two_entries_with_labels(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB", "Eerste") + conn("c2", "oB", "rAB2")) + obj("oB", "B")
        f = Fixture(model_xml(elementen, relaties, view), self)
        uit = ex.exporteer(f.pad, "Testview")["stromen"]
        self.assertEqual(sorted(s["label"] for s in uit), ["Eerste", "Tweede"])
        self.assertEqual(len({s["id"] for s in uit}), 2)

    def test_given_label_expression_when_exported_then_label_from_feature_without_linebreaks(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB", "Regel een&#xD;&#xA;regel twee")) + obj("oB", "B")
        f = Fixture(model_xml(elementen, relaties, view), self)
        uit = ex.exporteer(f.pad, "Testview")["stromen"]
        self.assertEqual(uit[0]["label"], "Regel een regel twee")

    def test_given_no_label_when_exported_then_relation_name_or_empty(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB") + conn("c2", "oB", "rAB2")) + obj("oB", "B")
        f = Fixture(model_xml(elementen, relaties, view), self)
        labels = {s["id"]: s["label"] for s in ex.exporteer(f.pad, "Testview")["stromen"]}
        self.assertEqual(labels, {"rAB": "", "rAB2": "Tweede"})

    def test_given_mapping_when_exported_then_koppeling_id_filled(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB") + conn("c2", "oC", "rAC")) + obj("oB", "B") + obj("oC", "C")
        f = Fixture(model_xml(elementen, relaties, view), self)
        uit = ex.exporteer(f.pad, "Testview", {"Systeem A > Systeem B": "A-B"})["stromen"]
        self.assertEqual([s["koppeling"] for s in uit], ["A-B"])

    def test_given_serving_relation_when_exported_then_not_a_flow(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oC", "rAC")) + obj("oC", "C")
        f = Fixture(model_xml(elementen, relaties, view), self)
        self.assertEqual(ex.exporteer(f.pad, "Testview")["stromen"], [])

    def test_given_nested_service_when_exported_then_parent_component_name(self):
        elementen = [("A", "ApplicationComponent", "Systeem A"), ("S", "ApplicationService", "Dienst S"),
                     ("B", "ApplicationComponent", "Systeem B")]
        relaties = [("rSB", "Flow", "S", "B", "")]
        view = obj("oA", "A", kinderen=obj("oS", "S", conns=conn("c1", "oB", "rSB"))) + obj("oB", "B")
        f = Fixture(model_xml(elementen, relaties, view), self)
        uit = ex.exporteer(f.pad, "Testview")["stromen"]
        self.assertEqual((uit[0]["van"], uit[0]["naar"]), ("Systeem A", "Systeem B"))

    def test_given_unknown_view_when_exported_then_exit_lists_views(self):
        elementen, relaties = self.basis()
        f = Fixture(model_xml(elementen, relaties, obj("oA", "A")), self)
        with self.assertRaises(SystemExit) as fout:
            ex.exporteer(f.pad, "Bestaat niet")
        self.assertIn("Testview", str(fout.exception))

    def test_given_missing_model_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            code = ex.main(["--model", str(Path(map_) / "geen.archimate"), "--uit", str(Path(map_) / "uit.json")])
        self.assertEqual(code, 2)

    def test_given_model_when_exported_then_model_file_unchanged(self):
        pad = WORTEL / "architecture/model/model.archimate"
        voor = hashlib.sha256(pad.read_bytes()).hexdigest()
        with tempfile.TemporaryDirectory() as map_:
            ex.main(["--uit", str(Path(map_) / "uit.json")])
        self.assertEqual(voor, hashlib.sha256(pad.read_bytes()).hexdigest())

    def test_given_same_model_twice_when_exported_then_identical_output(self):
        elementen, relaties = self.basis()
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB", "Eerste") + conn("c2", "oB", "rAB2")) + obj("oB", "B")
        f = Fixture(model_xml(elementen, relaties, view), self)
        a = json.dumps(ex.exporteer(f.pad, "Testview"), sort_keys=True)
        b = json.dumps(ex.exporteer(f.pad, "Testview"), sort_keys=True)
        self.assertEqual(a, b)


class AanvullingTests(unittest.TestCase):
    """Een stroom die een nieuwere hoofdplaat kent en de gepubliceerde view nog niet. Het model wijzigt
    alleen de modelleur, dus zo'n stroom komt uit een eigen bestand en overleeft een nieuwe export."""

    def aanvulling(self, test, **velden):
        inhoud = {"id": "aanvulling-a-naar-b", "van": "Systeem A", "naar": "Systeem B", "soort": "Flow",
                  "label": "Nieuwe lijn", "herkomst": "hoofdplaat 1.7a", "status": "nog niet gepubliceerd",
                  "bron": "https://github.com/x/y/pull/252#discussion_r1"}
        inhoud.update(velden)
        map_ = tempfile.TemporaryDirectory()
        test.addCleanup(map_.cleanup)
        pad = Path(map_.name) / "aanvullingen.json"
        pad.write_text(json.dumps({"aanvullingen": [inhoud]}), encoding="utf-8")
        return pad

    def basis(self):
        elementen = [("A", "ApplicationComponent", "Systeem A"), ("B", "ApplicationComponent", "Systeem B")]
        relaties = [("rAB", "Flow", "A", "B", "")]
        view = obj("oA", "A", conns=conn("c1", "oB", "rAB", "Bestaande lijn")) + obj("oB", "B")
        return Fixture(model_xml(elementen, relaties, view), self)

    def test_given_an_addition_when_exported_then_it_stands_beside_the_view_flows(self):
        f = self.basis()
        uit = ex.exporteer(f.pad, "Testview", aanvullingen=self.aanvulling(self))
        self.assertEqual(len(uit["stromen"]), 2)
        extra = [s for s in uit["stromen"] if s["id"].startswith("aanvulling-")]
        self.assertEqual(len(extra), 1)
        self.assertEqual(extra[0]["herkomst"], "hoofdplaat 1.7a")
        self.assertEqual(extra[0]["status"], "nog niet gepubliceerd")
        self.assertEqual(extra[0]["koppeling"], ex.ZONDER)

    def test_given_no_additions_file_when_exported_then_the_output_is_exactly_the_view(self):
        f = self.basis()
        self.assertEqual(len(ex.exporteer(f.pad, "Testview", aanvullingen=Path("bestaat-niet.json"))["stromen"]), 1)

    def test_given_an_addition_without_herkomst_when_exported_then_it_stops_and_names_the_field(self):
        f = self.basis()
        pad = self.aanvulling(self, herkomst="")
        with self.assertRaises(SystemExit) as fout:
            ex.exporteer(f.pad, "Testview", aanvullingen=pad)
        self.assertIn("herkomst", str(fout.exception))

    def test_given_an_addition_whose_id_lacks_the_prefix_when_exported_then_it_stops(self):
        f = self.basis()
        pad = self.aanvulling(self, id="id-865f297e")
        with self.assertRaises(SystemExit) as fout:
            ex.exporteer(f.pad, "Testview", aanvullingen=pad)
        self.assertIn("aanvulling-", str(fout.exception))

    def test_given_an_addition_that_the_view_already_carries_when_exported_then_it_stops(self):
        """Zodra de modelleur de stroom opneemt hoort de aanvulling te vervallen."""
        f = self.basis()
        pad = self.aanvulling(self, label="Bestaande lijn")
        with self.assertRaises(SystemExit) as fout:
            ex.exporteer(f.pad, "Testview", aanvullingen=pad)
        self.assertIn("staat al als stroom in de view", str(fout.exception))

    def test_given_the_export_when_run_twice_then_the_addition_survives(self):
        f = self.basis()
        pad = self.aanvulling(self)
        with tempfile.TemporaryDirectory() as map_:
            uit = Path(map_) / "uit.json"
            for _ in range(2):
                ex.main(["--model", str(f.pad), "--view", "Testview", "--aanvullingen", str(pad), "--uit", str(uit)])
            inhoud = json.loads(uit.read_text(encoding="utf-8"))
        self.assertEqual([s["id"] for s in inhoud["stromen"] if s["id"].startswith("aanvulling-")],
                         ["aanvulling-a-naar-b"])
        self.assertIn("aanvulling-", inhoud["toelichting"])

    def test_given_the_real_export_when_read_then_the_svs_to_sks_flow_stands_there(self):
        inhoud = json.loads((WORTEL / "architecture/model/informatiemodel/stromen.json").read_text(encoding="utf-8"))
        stroom = [s for s in inhoud["stromen"]
                  if s["van"] == "Student volg systeem (SVS)" and s["naar"] == "Student Keuze Systeem (SKS)"]
        self.assertEqual(len(stroom), 1)
        self.assertEqual(stroom[0]["objecten"],
                         ["Opleidingsprogramma aanbod verbintenis", "Onderwijseenheid aanbod verbintenis"])
        self.assertIn("voltooid", stroom[0]["aanleiding"])
        self.assertEqual(stroom[0]["herkomst"], "OKx hoofdplaat 1.7a")
        self.assertEqual(stroom[0]["status"], "nog niet gepubliceerd")
        self.assertTrue(stroom[0]["bron"].startswith("https://github.com/Npuls-OKx/meta/pull/252#discussion_r"))

    def test_given_the_real_export_when_read_then_it_says_how_it_relates_to_the_published_plate(self):
        inhoud = json.loads((WORTEL / "architecture/model/informatiemodel/stromen.json").read_text(encoding="utf-8"))
        self.assertIn("nog niet op de gepubliceerde hoofdplaat", inhoud["toelichting"])


if __name__ == "__main__":
    unittest.main()
