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

    def test_given_beeld_id_when_drawn_then_id_before_title_and_first_in_filename(self):
        r = regels()
        for x in r["regels"][:3]:
            x["beeld_id"], x["beeld"] = "F2-01", "Het aanbod gemaakt"
        blok = [b for b in self.blokken(r) if b.get("beeld")][0]
        self.assertEqual(tv.beeldtitel(blok), "F2-01 - Het aanbod gemaakt")
        self.assertEqual(tv.bestandsnaam(blok), "f2-01-het-aanbod-gemaakt.svg")
        self.assertIn("F2-01 - Het aanbod gemaakt", teksten(tv.regel_ontstaat(blok, set())))

    def test_given_specialization_when_nested_then_child_lands_in_the_specialization(self):
        r = {"scope_uitzonderingen": [], "regels": [
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Keuzedeel", "instantie": "K0262", "bron": "b",
             "relatie": {"soort": "Specialization", "van": "Keuzedeel", "naar": "Opleidingsprogramma specificatie"}},
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Onderwijseenheid specificatie", "instantie": "D1-K1", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie", "naar": "Onderwijseenheid specificatie", "nesting": True}},
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Onderwijseenheid specificatie", "instantie": "D1-K2", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie", "naar": "Onderwijseenheid specificatie", "nesting": True}},
            {"beeld_id": "F1-01", "beeld": "Keuzedeel", "fase": 1, "stap": "Aanbod maken", "soort": "ontstaat", "wie": "planner",
             "objecttype": "Leeronderdeel specificatie", "instantie": "D1-K2-W1", "bron": "b",
             "relatie": {"soort": "Aggregation", "van": "Onderwijseenheid specificatie", "naar": "Leeronderdeel specificatie", "nesting": True}}]}
        blok = self.blokken(r)[0]
        keuzedeel = blok["objecten"][0]
        self.assertEqual(keuzedeel["type"], "Keuzedeel")
        eenheden = keuzedeel["kinderen"]
        self.assertEqual([k["instantie"] for k in eenheden], ["D1-K1", "D1-K2"])
        # het leeronderdeel hangt onder de laatst getoonde eenheid, niet onder de eerste
        self.assertEqual([k["instantie"] for k in eenheden[1]["kinderen"]], ["D1-K2-W1"])
        self.assertNotIn("kinderen", eenheden[0])

    def test_given_state_on_a_created_object_when_drawn_then_state_is_shown(self):
        r = regels()
        r["regels"][0]["toestand"] = "intentie"
        blok = [b for b in self.blokken(r) if b["stap"] == "Aanbod maken"][0]
        self.assertEqual(blok["objecten"][0]["toestand"], "intentie")
        self.assertIn("toestand: intentie", teksten(tv.regel_ontstaat(blok, set())))

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


class BeeldIsBestandTests(unittest.TestCase):
    """Een beeld is een bestand. Viel een beeld in twee blokken, dan overschreef het tweede het eerste
    en toonde het beeld minder dan de tabel zegt."""

    def beeld_regels(self):
        r = regels()
        for x in r["regels"][:3]:
            x["beeld_id"], x["beeld"] = "F2-01", "Het aanbod gemaakt"
        r["regels"][2]["wie"] = "onderwijsontwerper"
        return r

    def test_given_an_image_whose_rules_change_role_when_grouped_then_one_block_with_both_roles(self):
        blokken = [b for b in tv.groepeer(self.beeld_regels()) if b.get("beeld")]
        self.assertEqual(len(blokken), 1)
        self.assertEqual(blokken[0]["rollen"], ["planner", "onderwijsontwerper"])
        self.assertEqual(blokken[0]["wie"], "planner, onderwijsontwerper")
        def tel(items):
            return sum(1 + tel(o.get("kinderen", [])) for o in items if "type" in o)
        self.assertEqual(tel(blokken[0]["objecten"]), 3)   # de genestte blijft meetellen

    def test_given_an_image_with_two_roles_when_drawn_then_both_stand_in_the_header(self):
        blok = [b for b in tv.groepeer(self.beeld_regels()) if b.get("beeld")][0]
        self.assertIn("planner, onderwijsontwerper", teksten(tv.regel_ontstaat(blok, set())))

    def test_given_rules_without_an_image_when_grouped_then_the_role_still_separates_blocks(self):
        r = regels()
        r["regels"][2]["wie"] = "onderwijsontwerper"
        rollen = [b.get("wie") for b in tv.groepeer(r) if b["soort"] == "ontstaat" and b["stap"] == "Aanbod maken"]
        self.assertEqual(rollen, ["planner", "onderwijsontwerper"])

    def test_given_two_blocks_with_the_same_filename_when_drawn_then_it_stops_and_names_both(self):
        r = regels()
        for x in r["regels"][:3]:
            x["beeld_id"], x["beeld"] = "F2-01", "Het aanbod gemaakt"
        r["regels"][1]["stap"] = "Aanbod publiceren"   # eigen blok, zelfde beeld en dus zelfde naam
        with tempfile.TemporaryDirectory() as map_:
            with self.assertRaises(SystemExit) as fout:
                tv.teken(r, Path(map_))
        self.assertIn("f2-01-het-aanbod-gemaakt.svg", str(fout.exception))
        self.assertIn("een beeld is een bestand", str(fout.exception))

    def test_given_the_real_table_when_drawn_then_every_block_gets_its_own_file(self):
        tabel = json.loads((WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as map_:
            uit = tv.teken(tabel, Path(map_))
            self.assertEqual(len(uit), len({n for n, _ in uit}))
            self.assertEqual(len(uit), len(list(Path(map_).glob("*.svg"))))


class OpruimenTests(unittest.TestCase):
    def test_given_a_renamed_image_when_drawn_then_the_old_file_is_gone(self):
        with tempfile.TemporaryDirectory() as map_:
            tv.teken(regels(), Path(map_))
            (Path(map_) / "f9-99-oude-naam.svg").write_text("<svg/>", encoding="utf-8")
            tv.teken(regels(), Path(map_), opruimen=True)
            self.assertFalse((Path(map_) / "f9-99-oude-naam.svg").exists())

    def test_given_the_keep_switch_when_drawn_then_the_orphan_stays(self):
        with tempfile.TemporaryDirectory() as map_:
            tv.teken(regels(), Path(map_))
            (Path(map_) / "f9-99-oude-naam.svg").write_text("<svg/>", encoding="utf-8")
            tv.teken(regels(), Path(map_), opruimen=False)
            self.assertTrue((Path(map_) / "f9-99-oude-naam.svg").exists())


class MatenTests(unittest.TestCase):
    """De uitvoer noemt per beeld de hoogte en de banen, zodat een onleesbaar beeld opvalt."""

    def test_given_a_run_when_it_reports_then_each_image_carries_its_size_and_bands(self):
        import contextlib, io
        with tempfile.TemporaryDirectory() as map_:
            m = Path(map_)
            (m / "r.json").write_text(json.dumps(regels()), encoding="utf-8")
            uit = io.StringIO()
            with contextlib.redirect_stdout(uit):
                code = tv.main(["--regels", str(m / "r.json"), "--uit", str(m / "beelden")])
            tekst = uit.getvalue()
        self.assertEqual(code, 0)
        self.assertRegex(tekst, r"\.svg: \d+ bij \d+, \d+ ba")
        self.assertIn("beelden getekend naar", tekst.splitlines()[-1])

    def test_given_no_band_when_measured_then_none_is_taller_than_the_slide_allows(self):
        """Over alle beelden van de echte tabel: een baan blijft binnen de verhouding die een slide toelaat."""
        snijd = tv._snijd()
        map_ = WORTEL / "architecture/model/informatiemodel/img/regels"
        for naam, breedte, _, hoogtes, reden in tv.maten(map_, sorted(p.name for p in map_.glob("*.svg"))):
            if reden:
                continue
            for h in hoogtes:
                self.assertLessEqual(h, breedte * snijd.VERHOUDING + 1, naam)

    def test_given_an_image_that_cannot_be_cut_when_measured_then_the_reason_comes_along(self):
        map_ = WORTEL / "architecture/model/informatiemodel/img/regels"
        redenen = {naam: reden for naam, _, _, _, reden in
                   tv.maten(map_, sorted(p.name for p in map_.glob("*.svg"))) if reden}
        # F1-08 is in #283 ingekort en past nu in drie banen; F2-07 wacht op #284
        self.assertEqual(sorted(redenen), ["f2-07-het-geplande-aanbod-terug-naar-de-catalogus.svg"])
        for reden in redenen.values():
            self.assertIn("geen witregel", reden)


if __name__ == "__main__":
    unittest.main()
