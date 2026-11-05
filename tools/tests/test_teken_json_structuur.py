"""Testgevallen voor tools/scripts/teken-json-structuur.py.

De plaat toont de indeling van een bericht dat van buiten komt. Twee dingen moeten daarom
kloppen: wat erop staat is wat er in het bericht staat, en wat er niet op hoort te staan komt
er ook niet op. Dat laatste is de reden dat waarden standaard uit staan.
"""

import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("jsonstructuur",
                                              WORTEL / "tools/scripts/teken-json-structuur.py")
js = importlib.util.module_from_spec(spec)
spec.loader.exec_module(js)

BERICHT = {
    "bestandstype": "SBIS",
    "opleidingseenheid": {
        "opleidingscode": "DV125960",
        "niveau": 2,
        "onderdelen": [{"code": "a", "naam": "een", "sbu": None},
                       {"code": "b", "naam": "twee", "sbu": 40}],
        "leeg": [],
    },
}


def regels(diepte=3, waarden_tot=-1, merk=()):
    return js.regels_van(BERICHT, diepte, waarden_tot, set(merk))


class SoortnaamTests(unittest.TestCase):
    def test_given_an_object_when_named_then_it_counts_its_keys(self):
        self.assertEqual(js.soortnaam({"a": 1, "b": 2}), "{ 2 sleutels }")

    def test_given_an_object_with_one_key_when_named_then_the_word_is_singular(self):
        self.assertEqual(js.soortnaam({"a": 1}), "{ 1 sleutel }")

    def test_given_a_list_of_objects_when_named_then_it_counts_and_types_them(self):
        self.assertEqual(js.soortnaam([{"a": 1}, {"a": 2}]), "[ 2 x object ]")

    def test_given_an_empty_list_when_named_then_it_says_so(self):
        self.assertEqual(js.soortnaam([]), "[ leeg ]")

    def test_given_a_null_when_named_then_it_says_leeg(self):
        self.assertEqual(js.soortnaam(None), "leeg")

    def test_given_a_boolean_when_named_then_it_is_not_a_getal(self):
        self.assertEqual(js.soortnaam(True), "ja of nee")


class SleutelvormTests(unittest.TestCase):
    def test_given_a_list_of_objects_when_asked_then_it_gives_the_keys_of_the_first(self):
        self.assertEqual(js.sleutelvorm([{"code": 1, "naam": 2}]), "code, naam")

    def test_given_more_keys_than_fit_when_asked_then_it_says_how_many_are_left(self):
        knoop = {f"k{i}": i for i in range(js.MAX_VORMSLEUTELS + 3)}
        self.assertTrue(js.sleutelvorm(knoop).endswith(f"en nog 3"))

    def test_given_a_list_of_values_when_asked_then_there_is_no_vorm(self):
        self.assertIsNone(js.sleutelvorm([1, 2, 3]))


class RegelsTests(unittest.TestCase):
    def test_given_a_depth_when_walked_then_nothing_deeper_is_drawn(self):
        self.assertEqual(max(n for n, *_ in regels(diepte=2)), 2)

    def test_given_a_list_when_walked_then_its_first_element_is_the_shape(self):
        namen = [s for _, s, *_ in regels(diepte=3)]
        self.assertIn("elk element", namen)

    def test_given_no_waarden_when_walked_then_no_value_is_drawn(self):
        self.assertTrue(all(w is None for *_, w, _, _ in regels()))

    def test_given_waarden_when_walked_then_the_value_is_drawn(self):
        gevonden = {s: w for _, s, _, w, _, _ in regels(waarden_tot=2)}
        self.assertEqual(gevonden["bestandstype"], '"SBIS"')
        self.assertEqual(gevonden["niveau"], "2")

    def test_given_waarden_tot_when_walked_then_deeper_values_stay_off(self):
        gevonden = {s: w for _, s, _, w, _, _ in regels(waarden_tot=1)}
        self.assertEqual(gevonden["bestandstype"], '"SBIS"')
        self.assertIsNone(gevonden["opleidingscode"])

    def test_given_a_merk_when_walked_then_that_key_is_marked(self):
        gemerkt = {s for _, s, _, _, _, g in regels(merk=["onderdelen"]) if g}
        self.assertEqual(gemerkt, {"onderdelen"})


class TekenTests(unittest.TestCase):
    def plaat(self, diepte=3, waarden_tot=-1):
        return js.teken(regels(diepte, waarden_tot), "Titel", "Herkomst", "0.1.0", "bericht.json")

    def test_given_a_message_when_drawn_then_every_key_stands_on_the_plaat(self):
        svg = self.plaat()
        for sleutel in ("bestandstype", "opleidingseenheid", "onderdelen", "leeg"):
            self.assertIn(sleutel, svg)

    def test_given_no_waarden_when_drawn_then_the_content_stays_off(self):
        self.assertNotIn("DV125960", self.plaat())

    def test_given_waarden_when_drawn_then_the_content_is_on_it(self):
        self.assertIn("DV125960", self.plaat(waarden_tot=2))

    def test_given_a_drawing_when_made_then_the_canvas_holds_the_widest_line(self):
        svg = self.plaat(waarden_tot=2)
        breed = int(svg.split('width="')[1].split('"')[0])
        langste = max(js.breedte(str(s)) for _, s, *_ in regels())
        self.assertGreater(breed, langste)

    def test_given_too_many_rows_when_drawn_then_it_stops(self):
        groot = {f"k{i}": i for i in range(js.MAX_REGELS + 1)}
        with self.assertRaises(SystemExit) as gevangen:
            js.teken(js.regels_van(groot, 2, -1, set()), "T", "H", "", "x.json")
        self.assertIn("hoogstens", str(gevangen.exception))
