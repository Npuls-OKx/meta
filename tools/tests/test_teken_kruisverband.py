"""Testgevallen voor tools/scripts/teken-kruisverband.py.

De matrix bestaat om te laten zien dat een bericht dat eruitziet als een boom er geen is.
Dat werkt alleen als de kruisjes staan waar het bericht ze zet, en als een rij of kolom die
niets raakt zichtbaar leeg blijft in plaats van weg te vallen.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("kruisverband",
                                              WORTEL / "tools/scripts/teken-kruisverband.py")
kv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kv)

BERICHT = {
    "envelop": {
        "eenheden": [
            {"code": "LE-01", "naam": "Een", "delen": ["D-01-a", "D-02-a"]},
            {"code": "LE-02", "naam": "Twee", "delen": ["D-01-b"]},
            {"code": "LE-03", "naam": "Drie", "delen": []},
        ],
        "onderdelen": [
            {"code": "D-01", "naam": "Eerste", "delen": [{"code": "D-01-a"}, {"code": "D-01-b"}]},
            {"code": "D-02", "naam": "Tweede", "delen": [{"code": "D-02-a"}]},
            {"code": "D-03", "naam": "Derde", "delen": [{"code": "D-03-a"}]},
        ],
    }
}

SELECTIE = {
    "titel": "Proef", "herkomst": "testgeval", "versie": "0.1.0", "bron": "bericht.json",
    "rijen": {"pad": "envelop.eenheden", "verwijst_naar": "delen"},
    "kolommen": {"pad": "envelop.onderdelen", "bevat": "delen"},
}


def lees(selectie=None, bericht=None):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "bericht.json").write_text(json.dumps(bericht or BERICHT), encoding="utf-8")
        pad = tmp / "selectie.json"
        pad.write_text(json.dumps(selectie or SELECTIE), encoding="utf-8")
        return kv.lees(pad)


class VoorvoegselTests(unittest.TestCase):
    def test_given_codes_with_a_shared_head_when_asked_then_it_is_returned(self):
        self.assertEqual(kv.gemeen_voorvoegsel(["DV12705801", "DV12705802"]), "DV1270580")

    def test_given_codes_without_a_shared_head_when_asked_then_it_is_empty(self):
        self.assertEqual(kv.gemeen_voorvoegsel(["abc", "xyz"]), "")

    def test_given_one_code_when_asked_then_nothing_is_stripped(self):
        self.assertEqual(kv.gemeen_voorvoegsel(["DV12705801"]), "")

    def test_given_a_prefix_when_shortening_then_only_the_tail_remains(self):
        self.assertEqual(kv.kort("DV12705801", "DV127058"), "01")

    def test_given_no_prefix_when_shortening_then_the_code_stays_whole(self):
        self.assertEqual(kv.kort("LE-01", ""), "LE-01")


class LeesTests(unittest.TestCase):
    def test_given_a_message_when_read_then_the_pairs_follow_the_references(self):
        _, rijen, kolommen, paren = lees()
        self.assertEqual(paren, {("LE-01", "D-01"), ("LE-01", "D-02"), ("LE-02", "D-01")})

    def test_given_a_row_without_references_when_read_then_it_stays_in_the_rows(self):
        _, rijen, _, _ = lees()
        self.assertIn("LE-03", [r["code"] for r in rijen])

    def test_given_a_column_nobody_points_at_when_read_then_it_stays_in_the_columns(self):
        _, _, kolommen, paren = lees()
        self.assertIn("D-03", [k["code"] for k in kolommen])
        self.assertNotIn("D-03", {p[1] for p in paren})

    def test_given_a_selectie_without_herkomst_when_read_then_it_stops(self):
        sel = dict(SELECTIE)
        del sel["herkomst"]
        with self.assertRaises(SystemExit) as gevangen:
            lees(sel)
        self.assertIn("herkomst", str(gevangen.exception))

    def test_given_more_rows_than_fit_when_read_then_it_stops(self):
        bericht = {"envelop": {
            "eenheden": [{"code": f"LE-{i}", "delen": []} for i in range(kv.MAX_RIJEN + 1)],
            "onderdelen": [{"code": "D-01", "delen": []}]}}
        with self.assertRaises(SystemExit) as gevangen:
            lees(bericht=bericht)
        self.assertIn("hoogstens", str(gevangen.exception))


class TekenTests(unittest.TestCase):
    def plaat(self):
        return kv.teken(*lees())

    def test_given_a_matrix_when_drawn_then_it_counts_the_pairs(self):
        _, n, meer, leeg = self.plaat()
        self.assertEqual((n, meer, leeg), (3, 1, 1))

    def test_given_a_row_with_more_than_one_column_when_drawn_then_it_is_marked(self):
        svg, *_ = self.plaat()
        self.assertIn(kv.ACCENT, svg)

    def test_given_a_matrix_when_drawn_then_every_row_name_is_on_it(self):
        svg, *_ = self.plaat()
        for naam in ("Een", "Twee", "Drie"):
            self.assertIn(naam, svg)

    def test_given_a_matrix_when_drawn_then_the_canvas_holds_every_column(self):
        svg, *_ = self.plaat()
        breed = int(svg.split('width="')[1].split('"')[0])
        _, _, kolommen, _ = lees()
        self.assertGreater(breed, kv.MARGE + kv.RIJLABEL + len(kolommen) * kv.CEL)
