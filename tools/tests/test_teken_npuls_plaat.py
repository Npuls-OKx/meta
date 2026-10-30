"""Testgevallen voor tools/scripts/teken-npuls-plaat.py, de aanduidingen bij ladder en stappen.

De terugloop is de uitspraak van de statusplaat: werk dat een hogere trede haalde en na een
onbeantwoorde vraag opnieuw begint. Zij moet in de goot links lopen, want een hogere trede
springt naar rechts in en laat daar geen ruimte over. Dezelfde goot draagt de band die een
reeks treden beugelt. Een trede die producten draagt groeit mee met het aantal rijen chips,
anders loopt zij over de volgende heen. De lus doet hetzelfde onder een rij stappen.
"""

import importlib.util
import re
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("npuls", WORTEL / "tools/scripts/teken-npuls-plaat.py")
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


class ItemTests(unittest.TestCase):
    def test_given_a_trede_with_items_when_drawn_then_every_item_is_on_the_plaat(self):
        blok = {"soort": "ladder", "treden": [
            {"nummer": 1, "naam": "Vraag", "items": ["Begrippenlijst", "Hoofdplaat"]}]}
        svg, _ = npuls.blok_ladder(blok, 40, 100, 1000, PALET, {"iconen": {}})
        self.assertIn("Begrippenlijst", svg)
        self.assertIn("Hoofdplaat", svg)

    def test_given_many_items_when_drawn_then_the_trede_grows_beyond_the_basis(self):
        veel = [f"Product {n}" for n in range(14)]
        blok = {"soort": "ladder", "treden": [{"nummer": 1, "naam": "Vraag", "items": veel}]}
        _, met = npuls.blok_ladder(blok, 40, 100, 1000, PALET, {"iconen": {}})
        _, zonder = npuls.blok_ladder(
            {"soort": "ladder", "treden": [{"nummer": 1, "naam": "Vraag"}]},
            40, 100, 1000, PALET, {"iconen": {}})
        self.assertGreater(met, zonder)


class BandTests(unittest.TestCase):
    def test_given_a_band_when_drawn_then_the_label_is_turned_upright(self):
        svg, _ = ladder()
        self.assertNotIn("hier beweegt het werk", svg)
        blok = dict(LADDER, band={"boven": 2, "onder": 1, "tekst": "hier beweegt het werk"})
        svg, _ = npuls.blok_ladder(blok, 40, 100, 1000, PALET, {"iconen": {}})
        self.assertIn("hier beweegt het werk", svg)
        self.assertRegex(svg, r'transform="rotate\(-90 ')

    def test_given_a_band_and_a_terugloop_when_drawn_then_both_fit_in_the_goot(self):
        blok = dict(LADDER, band={"boven": 2, "onder": 1}, terugloop={"van": 3, "naar": 1})
        met, _ = npuls.blok_ladder(blok, 40, 100, 1000, PALET, {"iconen": {}})
        alleen, _ = ladder({"van": 3, "naar": 1})
        self.assertGreater(min(linkerranden(met)), min(linkerranden(alleen)))


class LusTests(unittest.TestCase):
    def stappen(self, lus=None):
        blok = {"soort": "stappen", "stappen": [
            {"naam": f"Stap {n}"} for n in range(1, 5)]}
        if lus:
            blok["lus"] = lus
        return npuls.blok_stappen(blok, 40, 100, 1000, PALET, {"iconen": {}})

    def test_given_a_row_without_lus_when_drawn_then_the_height_is_the_card_height(self):
        _, hoog = self.stappen()
        self.assertEqual(hoog, 96)

    def test_given_a_lus_when_drawn_then_the_row_reserves_room_underneath(self):
        _, zonder = self.stappen()
        _, met = self.stappen({"van": 4, "naar": 2, "tekst": "opnieuw"})
        self.assertGreater(met, zonder)
        svg, _ = self.stappen({"van": 4, "naar": 2, "tekst": "opnieuw"})
        self.assertIn("opnieuw", svg)

    def test_given_a_lus_to_a_missing_stap_when_drawn_then_it_stops_with_a_message(self):
        with self.assertRaises(SystemExit) as gevangen:
            self.stappen({"van": 9, "naar": 1})
        self.assertIn("stap 9", str(gevangen.exception))


class NetwerkTests(unittest.TestCase):
    def paneel(self, vorm, aantal=4):
        return {"soort": "netwerk", "panelen": [{
            "titel": "Een school", "vorm": vorm, "midden": "OKx-koppelvlak",
            "knopen": [{"naam": f"Systeem {n}"} for n in range(aantal)]}]}

    def test_given_knopen_onderling_when_drawn_then_every_pair_has_a_line(self):
        svg, _ = npuls.blok_netwerk(self.paneel("onderling", 4), 40, 100, 1000, PALET, {"iconen": {}})
        self.assertEqual(svg.count('stroke-opacity="0.75"'), 6)

    def test_given_knopen_via_a_midden_when_drawn_then_there_is_a_line_per_knoop(self):
        svg, _ = npuls.blok_netwerk(self.paneel("via", 4), 40, 100, 1000, PALET, {"iconen": {}})
        self.assertEqual(svg.count('stroke-width="2"'), 4)
        self.assertIn("OKx-koppelvlak", svg)

    def test_given_a_paneel_when_drawn_then_every_knoop_carries_its_name(self):
        svg, _ = npuls.blok_netwerk(self.paneel("via", 4), 40, 100, 1000, PALET, {"iconen": {}})
        for n in range(4):
            self.assertIn(f"Systeem {n}", svg)


class VersieTests(unittest.TestCase):
    def plaat(self, **extra):
        sel = {"titel": "Proef", "breedte": 800, "voet": "een voetregel",
               "blokken": [{"soort": "tekst", "tekst": "inhoud"}]}
        sel.update(extra)
        return npuls.teken(sel)

    def test_given_a_selectie_with_a_versie_when_drawn_then_it_stands_in_the_voetregel(self):
        self.assertIn(">v0.2.0<", self.plaat(versie="0.2.0"))

    def test_given_a_selectie_without_a_versie_when_drawn_then_no_version_is_shown(self):
        self.assertNotRegex(self.plaat(), r">v\d")

    def test_given_only_a_versie_when_drawn_then_the_voetregel_still_appears(self):
        svg = npuls.teken({"titel": "Proef", "breedte": 800, "versie": "1.0.0",
                           "blokken": [{"soort": "tekst", "tekst": "inhoud"}]})
        self.assertIn(">v1.0.0<", svg)


if __name__ == "__main__":
    unittest.main()
