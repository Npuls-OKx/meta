"""Testgevallen voor scripts/teken-voorbeeldregels.py.

Elke verwachting volgt uit een fixture-regeltabel in de test; de SVG wordt als XML
geparst en op inhoud en geometrie getoetst, niet op een momentopname.
"""

import importlib.util
import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("teken_voorbeeldregels", WORTEL / "scripts/teken-voorbeeldregels.py")
tv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tv)

SVG = "{http://www.w3.org/2000/svg}"


def regels(extra=None):
    basis = {"scope_uitzonderingen": [{"objecttype": "Lesgelegenheid", "motivering": "besluit"}],
             "regels": [
                 {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "b", "zin": "De planner maakt aanbod."},
                 {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Opleidingsprogramma aanbod", "instantie": "Regulier BOL 2026", "bron": "b",
                  "relatie": {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Opleidingsprogramma aanbod", "nesting": True}},
                 {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Cohort / periode", "instantie": "2026", "bron": "b", "aanname": True,
                  "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Cohort / periode", "label": "Op basis van"}},
                 {"fase": 2, "stap": "Aanbod publiceren", "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1", "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "b", "zin": "Terug naar de catalogus."},
                 {"fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "roosteraar", "objecttype": "Lesgelegenheid", "instantie": "ma 09:00", "bron": "b"},
                 {"fase": 4, "stap": "Roosteren", "soort": "verandert", "wie": "roosteraar", "objecttype": "Leergelegenheid", "instantie": "B1-K1-W1", "toestand": "geroosterd", "bron": "b"}]}
    if extra:
        basis["regels"] += extra
    return basis


def teksten(svg):
    return [t.text or "" for t in ET.fromstring(svg).iter(f"{SVG}text")]


def rects(svg):
    return [dict(r.attrib) for r in ET.fromstring(svg).iter(f"{SVG}rect")]


class TekenTests(unittest.TestCase):
    def blokken(self, r=None):
        return tv.groepeer(r or regels())

    def test_given_rules_same_step_when_grouped_then_one_block_with_role_once(self):
        b = self.blokken()
        ontstaat = [x for x in b if x["soort"] == "ontstaat" and x["stap"] == "Aanbod maken"]
        self.assertEqual(len(ontstaat), 1)
        self.assertEqual(ontstaat[0]["wie"], "planner")

    def test_given_verdieping_in_same_step_when_grouped_then_own_block_named_and_drawn_with_it(self):
        extra = [{"fase": 2, "stap": "Aanbod maken", "verdieping": "aanbod naar skills", "soort": "verandert", "wie": "planner",
                  "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "toestand": "verdiept", "bron": "b"}]
        b = [x for x in self.blokken(regels(extra)) if x["soort"] == "ontstaat" and x["stap"] == "Aanbod maken"]
        self.assertEqual([x.get("verdieping") for x in b], [None, "aanbod naar skills"])
        self.assertTrue(tv.bestandsnaam(b[1], 2).endswith("-aanbod-maken-verdieping.svg"))
        self.assertFalse(tv.bestandsnaam(b[0], 1).endswith("-verdieping.svg"))
        self.assertEqual(tv.bestandsnaam({"fase": 1, "beeld": "Leeruitkomsten uit het dossier, in de stem van de instelling"}), "f1-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.svg")
        self.assertIn("verdieping: aanbod naar skills", teksten(tv.regel_ontstaat(b[1], set())))
        self.assertNotIn("verdieping: aanbod naar skills", teksten(tv.regel_ontstaat(b[0], set())))

    def test_given_relation_to_non_adjacent_object_when_grouped_then_reference_not_line(self):
        r = regels()
        r["regels"].insert(3, {"fase": 2, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner", "objecttype": "Student keuze regelset", "instantie": "Regels", "bron": "b",
                               "relatie": {"soort": "Association", "van": "Opleidingaanbod", "naar": "Student keuze regelset"}})
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        laatste = blok["objecten"][-1]
        self.assertEqual(laatste["type"], "Student keuze regelset")
        self.assertEqual(laatste["verwijzing"], "Opleidingaanbod hangt aan")
        self.assertNotIn("relatie", blok["objecten"][-2])

    def test_given_concept_block_when_drawn_then_chip_and_dashed_frame(self):
        extra = [{"fase": 2, "stap": "Aanbod maken", "verdieping": "kader", "plaat": "onderwijsontwerp", "soort": "ontstaat", "wie": "planner",
                  "objecttype": "Leervormstrategie", "instantie": "Leren door te doen", "bron": "c"}]
        blokken = [b for b in self.blokken(regels(extra)) if b["stap"] == "Aanbod maken"]
        self.assertEqual([b.get("plaat") for b in blokken], ["informatiemodel", "onderwijsontwerp"])
        svg = tv.regel_ontstaat(blokken[1], set())
        self.assertIn("conceptplaat: Informatiemodel Onderwijsontwerp", teksten(svg))
        self.assertIn("6 4", rects(svg)[0].get("stroke-dasharray", ""))
        self.assertNotIn("stroke-dasharray", rects(tv.regel_ontstaat(blokken[0], set()))[0])

    def test_given_beeld_title_when_grouped_then_own_block_titled_and_filename_from_title(self):
        r = regels()
        for x in r["regels"][:2]:
            x["beeld"] = "Het aanbod gemaakt: opleiding en programma"
        r["regels"][2]["beeld"] = "Het cohort erbij"
        blokken = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"]
        self.assertEqual([b.get("beeld") for b in blokken], ["Het aanbod gemaakt: opleiding en programma", "Het cohort erbij"])
        self.assertEqual(tv.bestandsnaam(blokken[0]), "f2-het-aanbod-gemaakt-opleiding-en-programma.svg")
        svg = tv.regel_ontstaat(blokken[0], set())
        self.assertIn("Het aanbod gemaakt: opleiding en programma", teksten(svg))
        self.assertNotIn("Het cohort erbij", teksten(svg))

    def test_given_extra_relations_when_grouped_then_each_a_reference_with_instance_and_stacked(self):
        r = regels()
        r["regels"][3]["relaties"] = [{"soort": "Association", "van": "Opleidingaanbod", "naar": "Leeruitkomst", "instantie": "Baliegesprek"},
                                      {"soort": "Association", "van": "Toetsonderdeel specificatie", "naar": "Opleidingaanbod", "label": "toetst"}]
        blok = [b for b in self.blokken(r) if b["soort"] == "stroomt"][0]
        self.assertEqual(blok["objecten"][0]["verwijzingen"], ["hangt aan Leeruitkomst: Baliegesprek", "Toetsonderdeel specificatie toetst"])
        svg = tv.regel_stroomt(blok, set())
        ys = {x.text: float(x.get("y")) for x in ET.fromstring(svg).iter(f"{SVG}text") if x.text in ("hangt aan Leeruitkomst: Baliegesprek", "Toetsonderdeel specificatie toetst")}
        self.assertEqual(len(ys), 2)
        self.assertNotEqual(*ys.values())

    def test_given_ontstaat_rule_when_drawn_then_svg_contains_role_step_and_each_instance(self):
        blok = self.blokken()[0]
        svg = tv.regel_ontstaat(blok, {"Lesgelegenheid"})
        t = teksten(svg)
        for s in ("planner", "Aanbod maken", "Apothekersassistent 2026", "Regulier BOL 2026", "2026"):
            self.assertIn(s, t)
        self.assertEqual(svg.count(tv.ICONS["proces"]), 1)

    def test_given_nested_objects_when_drawn_then_child_rect_within_parent_rect(self):
        blok = self.blokken()[0]
        svg = tv.regel_ontstaat(blok, set())
        rs = [r for r in rects(svg) if r.get("fill") == tv.BUS and r.get("rx", "0") == "0"]
        rs = sorted(rs, key=lambda r: float(r["width"]), reverse=True)
        ouder, kind = rs[0], next(r for r in rs[1:] if float(r["x"]) > float(rs[0]["x"]))
        self.assertGreaterEqual(float(kind["x"]), float(ouder["x"]))
        self.assertLessEqual(float(kind["x"]) + float(kind["width"]), float(ouder["x"]) + float(ouder["width"]))
        self.assertLessEqual(float(kind["y"]) + float(kind["height"]), float(ouder["y"]) + float(ouder["height"]))

    def test_given_container_with_toestand_when_drawn_then_toestand_shown_above_children(self):
        extra = [{"fase": 4, "stap": "Roosteren", "soort": "verandert", "wie": "roosteraar", "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "toestand": "geroosterd", "bron": "b"},
                 {"fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "roosteraar", "objecttype": "Onderwijseenheid aanbod", "instantie": "Blok 1", "bron": "b",
                  "relatie": {"soort": "Aggregation", "van": "Opleidingaanbod", "naar": "Onderwijseenheid aanbod", "nesting": True}}]
        blok = [b for b in self.blokken(regels(extra)) if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, set())
        ts = {t.text: (float(t.get("x")), float(t.get("y"))) for t in ET.fromstring(svg).iter(f"{SVG}text") if t.text}
        self.assertIn("toestand: geroosterd", ts)
        self.assertLess(ts["toestand: geroosterd"][1], ts["Blok 1"][1])
        self.assertIn(("AA 2026"), ts)

    def test_given_wide_row_of_children_when_drawn_then_stacked_within_parent(self):
        lang = "Een heel lange instantienaam die de rij van kinderen ver voorbij de maximale breedte duwt"
        extra = [{"fase": 4, "stap": "Roosteren", "soort": "ontstaat", "wie": "roosteraar", "objecttype": f"Kind {i}", "instantie": lang, "bron": "b",
                  "relatie": {"soort": "Aggregation", "van": "Lesgelegenheid", "naar": f"Kind {i}", "nesting": True}} for i in range(3)]
        blok = [b for b in self.blokken(regels(extra)) if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, set())
        ys = {t.text: float(t.get("y")) for t in ET.fromstring(svg).iter(f"{SVG}text") if t.text and t.text.startswith("Kind ")}
        self.assertEqual(len(ys), 3)
        self.assertEqual(len(set(ys.values())), 3)
        self.assertLess(float(ET.fromstring(svg).get("width")), 1500)

    def test_given_assumption_when_drawn_then_rect_has_dasharray(self):
        blok = self.blokken()[0]
        svg = tv.regel_ontstaat(blok, set())
        gestippeld = [r for r in rects(svg) if r.get("stroke-dasharray") == "5 3"]
        self.assertEqual(len(gestippeld), 1)

    def test_given_relation_label_when_drawn_then_label_between_objects(self):
        svg = tv.regel_ontstaat(self.blokken()[0], set())
        self.assertIn("Op basis van", teksten(svg))

    def test_given_scope_exception_when_drawn_then_grey_fill(self):
        blok = [b for b in self.blokken() if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, {"Lesgelegenheid"})
        self.assertTrue(any(r.get("fill") == tv.GRIJS for r in rects(svg)))

    def test_given_verandert_rule_when_drawn_then_toestand_shown(self):
        blok = [b for b in self.blokken() if b["stap"] == "Roosteren"][0]
        svg = tv.regel_ontstaat(blok, set())
        self.assertIn("toestand: geroosterd", teksten(svg))

    def test_given_stroomt_rule_when_drawn_then_van_naar_object_id_and_step(self):
        blok = [b for b in self.blokken() if b["soort"] == "stroomt"][0]
        svg = tv.regel_stroomt(blok, set())
        t = teksten(svg)
        for s in ("Planningssysteem", "Onderwijscatalogus", "Opleidingaanbod", "OC-P&R", "na: Aanbod publiceren"):
            self.assertIn(s, t)
        self.assertTrue(any(r.get("fill") == tv.APP for r in rects(svg)))

    def test_given_first_stroomt_object_with_relation_when_grouped_then_reference_shown(self):
        r = regels()
        r["regels"][3]["relatie"] = {"soort": "Specialization", "van": "Opleidingaanbod", "naar": "Opleidingsaanbod van Instelling"}
        blok = [b for b in self.blokken(r) if b["soort"] == "stroomt"][0]
        self.assertEqual(blok["objecten"][0]["verwijzing"], "is een Opleidingsaanbod van Instelling")

    def test_given_stroomt_without_koppeling_when_drawn_then_marked(self):
        blok = [b for b in self.blokken() if b["soort"] == "stroomt"][0]
        blok["koppeling"] = None
        svg = tv.regel_stroomt(blok, set())
        self.assertIn("zonder koppelingspecificatie", teksten(svg))

    def test_given_stroomt_without_arrow_on_hoofdplaat_when_drawn_then_marked_as_such(self):
        extra = [{"fase": 2, "stap": "Aanbod publiceren", "soort": "stroomt", "van": "Curriculum ontwerptool", "naar": "Onderwijscatalogus",
                  "pijl": "geen pijl op de hoofdplaat", "koppeling": None, "objecttype": "Opleidingaanbod", "instantie": "AA 2026", "bron": "b"}]
        blok = [b for b in self.blokken(regels(extra)) if b["soort"] == "stroomt" and b["van"] == "Curriculum ontwerptool"][0]
        svg = tv.regel_stroomt(blok, set())
        self.assertIn("geen pijl op de hoofdplaat", teksten(svg))
        self.assertNotIn("zonder koppelingspecificatie", teksten(svg))

    def test_given_any_rule_when_drawn_then_svg_wellformed_and_self_contained(self):
        for blok in self.blokken():
            svg = tv.regel_stroomt(blok, set()) if blok["soort"] == "stroomt" else tv.regel_ontstaat(blok, set())
            ET.fromstring(svg)
            for verboden in ("<link", "@import", "url(", "<script", "<foreignObject"):
                self.assertNotIn(verboden, svg)

    def test_given_long_instance_name_when_drawn_then_text_fits_box(self):
        naam = "x" * 60
        s, w, h = tv.element(0, 0, "object", "Objecttype", naam)
        self.assertGreaterEqual(w, tv.tw(naam, 13, True) + 42)

    def test_given_special_characters_when_drawn_then_escaped(self):
        r = regels(); r["regels"][0]["instantie"] = "A & <B> 'C'"
        svg = tv.regel_ontstaat(tv.groepeer(r)[0], set())
        ET.fromstring(svg)

    def test_given_empty_relation_label_when_validated_then_exit(self):
        r = regels(); r["regels"][2]["relatie"]["label"] = ""
        with self.assertRaises(SystemExit):
            tv.valideer(r)

    def test_given_missing_instance_when_validated_then_exit_names_type(self):
        r = regels(); r["regels"][0]["instantie"] = ""
        with self.assertRaises(SystemExit) as fout:
            tv.valideer(r)
        self.assertIn("Opleidingaanbod", str(fout.exception))

    def test_given_unknown_kind_when_validated_then_exit(self):
        r = regels(); r["regels"][0]["soort"] = "verdwijnt"
        with self.assertRaises(SystemExit):
            tv.valideer(r)

    def test_given_table_when_drawn_then_one_file_per_block_with_deterministic_names(self):
        with tempfile.TemporaryDirectory() as map_:
            uit = tv.teken(regels(), map_)
            self.assertEqual(len(uit), len(tv.groepeer(regels())))
            self.assertEqual(len(list(Path(map_).glob("*.svg"))), len(uit))
            self.assertTrue(all(n.startswith("f") and n.endswith(".svg") for n, _ in uit))

    def test_given_same_input_twice_when_drawn_then_identical_output(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            tv.teken(regels(), a); tv.teken(regels(), b)
            for p in Path(a).glob("*.svg"):
                self.assertEqual(p.read_bytes(), (Path(b) / p.name).read_bytes())

    def test_given_missing_table_when_run_then_exit_two(self):
        with tempfile.TemporaryDirectory() as map_:
            self.assertEqual(tv.main(["--regels", str(Path(map_) / "geen.json"), "--uit", map_]), 2)


if __name__ == "__main__":
    unittest.main()
