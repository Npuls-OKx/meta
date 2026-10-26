"""Testgevallen voor scripts/teken-fasenplaten.py.

De fasenplaten komen uit het model en niet over een rasterrender heen (#407). De gevallen die
de vorm raken draaien op een fixture; de gevallen die de plaat zelf raken draaien op het echte
model in de repository, want daar gaat het mis zodra de view wijzigt.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("teken_fasenplaten", WORTEL / "scripts/teken-fasenplaten.py")
tf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tf)

REGELS = WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json"


def fixture():
    return {
        "fasen": [{"nummer": 1, "naam": "Kwalificatiekader analyseren en grofmazig ontwerpen"}],
        "regels": [
            {"fase": 1, "soort": "stroomt", "beeld_id": "F1-01", "van": "Onderwijscatalogus",
             "naar": "Planningssysteem", "pijl": "id-1"},
            {"fase": 1, "soort": "stroomt", "beeld_id": "F1-02", "van": "Onderwijscatalogus",
             "naar": "Planningssysteem", "pijl": tf.hoog.GEEN_PIJL},
            {"fase": 1, "soort": "ontstaat", "beeld_id": "F1-03", "objecttype": "Leeruitkomst"},
        ],
    }


class DeVormVanEenMarkering(unittest.TestCase):

    def test_given_a_rule_table_when_phase_names_are_read_then_each_number_carries_its_name(self):
        self.assertEqual(tf.fasenamen(fixture())[1], "Kwalificatiekader analyseren en grofmazig ontwerpen")

    def test_given_a_flow_with_an_arrow_when_marked_then_it_carries_the_flow_id(self):
        stromen = tf.hoog.stromen_per_fase(fixture())[1]
        markering = next(m for m in tf.markeringen_van(stromen) if m["label"] == "F1-01")
        self.assertTrue(markering["op_de_plaat"])
        self.assertEqual(markering["stroom"], "id-1")

    def test_given_a_flow_without_an_arrow_when_marked_then_it_is_not_on_the_plate(self):
        stromen = tf.hoog.stromen_per_fase(fixture())[1]
        markering = next(m for m in tf.markeringen_van(stromen) if m["label"] == "F1-02")
        self.assertFalse(markering["op_de_plaat"])
        self.assertEqual(markering["stroom"], "")

    def test_given_a_rule_that_does_not_flow_when_marked_then_it_is_left_out(self):
        stromen = tf.hoog.stromen_per_fase(fixture())[1]
        self.assertNotIn("F1-03", [m["label"] for m in tf.markeringen_van(stromen)])


class DePlaatUitHetModel(unittest.TestCase):
    """Deze gevallen tekenen de plaat uit het model in de repository."""

    @classmethod
    def setUpClass(cls):
        cls.map_ = Path(tempfile.mkdtemp())
        tf.main(["--regels", str(REGELS), "--uit", str(cls.map_), "--fasen", "1"])
        cls.svg = (cls.map_ / "f1.svg").read_text(encoding="utf-8")

    def test_given_the_rule_table_when_phase_one_is_drawn_then_only_its_own_images_are_marked(self):
        regels = json.loads(REGELS.read_text(encoding="utf-8"))
        eigen = {r["beeld_id"] for r in regels["regels"]
                 if r["soort"] == "stroomt" and r["fase"] == 1 and r.get("beeld_id")}
        vreemd = {r["beeld_id"] for r in regels["regels"]
                  if r["soort"] == "stroomt" and r["fase"] != 1 and r.get("beeld_id")}
        self.assertTrue(eigen & set(self.svg.split()) or any(b in self.svg for b in eigen))
        self.assertFalse([b for b in vreemd if f">{b}<" in self.svg])

    def test_given_a_drawn_plate_when_read_then_it_is_vector_without_an_embedded_render(self):
        self.assertIn("<svg", self.svg)
        self.assertNotIn("data:image/jpeg", self.svg)
        self.assertNotIn("data:image/png", self.svg)

    def test_given_the_same_rule_table_when_drawn_twice_then_the_plate_is_byte_equal(self):
        tweede = Path(tempfile.mkdtemp())
        tf.main(["--regels", str(REGELS), "--uit", str(tweede), "--fasen", "1"])
        self.assertEqual(self.svg, (tweede / "f1.svg").read_text(encoding="utf-8"))

    def test_given_the_overview_when_drawn_then_it_carries_no_marking(self):
        kaart = (self.map_ / tf.OVERZICHT).read_text(encoding="utf-8")
        self.assertIn("<svg", kaart)
        self.assertNotIn("markeerpunt", kaart)


if __name__ == "__main__":
    unittest.main()
