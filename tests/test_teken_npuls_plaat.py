"""Testgevallen voor scripts/teken-npuls-plaat.py, blok ladder met terugloop.

De terugloop is de uitspraak van de rijpheidsplaat: werk dat een hogere trede haalde en na een
onbeantwoorde vraag opnieuw begint. Zij moet in de goot links lopen, want een hogere trede
springt naar rechts in en laat daar geen ruimte over. Deze gevallen bewaken die goot en de
melding bij een trede die de ladder niet kent.
"""

import importlib.util
import re
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("npuls", WORTEL / "scripts/teken-npuls-plaat.py")
npuls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(npuls)

PALET = npuls.palet()
LADDER = {
    "soort": "ladder",
    "treden": [
        {"nummer": 1, "naam": "Vraag", "kleur": "#DD784B"},
        {"nummer": 2, "naam": "Concept", "kleur": "#3D68EC"},
        {"nummer": 3, "naam": "Uitgebracht", "kleur": "#00AF81"},
    ],
}


def ladder(terugloop=None):
    blok = dict(LADDER)
    if terugloop:
        blok["terugloop"] = terugloop
    return npuls.blok_ladder(blok, 40, 100, 1000, PALET, {"iconen": {}})


def linkerranden(svg):
    """De x van elke trede, uit de rechthoeken die de kaarten tekenen."""
    return sorted(float(m) for m in re.findall(r'<rect x="(-?\d+)" y="\d+" width="\d+"', svg))


class TerugloopTests(unittest.TestCase):
    def test_given_a_ladder_without_terugloop_when_drawn_then_the_treden_start_at_the_block(self):
        svg, _ = ladder()
        self.assertEqual(min(linkerranden(svg)), 40)

    def test_given_a_terugloop_when_drawn_then_the_treden_shift_right_for_the_goot(self):
        zonder, _ = ladder()
        met, _ = ladder({"van": 3, "naar": 1})
        self.assertGreater(min(linkerranden(met)), min(linkerranden(zonder)))

    def test_given_a_terugloop_when_drawn_then_the_height_stays_the_same(self):
        _, zonder = ladder()
        _, met = ladder({"van": 3, "naar": 1})
        self.assertEqual(met, zonder)

    def test_given_a_terugloop_with_text_when_drawn_then_the_label_is_turned_upright(self):
        svg, _ = ladder({"van": 3, "naar": 1, "tekst": "de vraag kwam terug"})
        self.assertIn("de vraag kwam terug", svg)
        self.assertRegex(svg, r'transform="rotate\(-90 ')

    def test_given_a_terugloop_to_a_missing_trede_when_drawn_then_it_stops_with_a_message(self):
        with self.assertRaises(SystemExit) as gevangen:
            ladder({"van": 9, "naar": 1})
        self.assertIn("trede 9", str(gevangen.exception))


if __name__ == "__main__":
    unittest.main()
