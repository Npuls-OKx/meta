"""Testgevallen voor scripts/teken-hoofdplaat-highlight.py.

De groepering bepaalt wat er op de plaat komt: per fase de beelden, of per koppeling
de lijnen die zij gebruikt.
"""

import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("hoofdplaat", WORTEL / "scripts/teken-hoofdplaat-highlight.py")
hp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hp)

REGELS = {"regels": [
    {"soort": "stroomt", "fase": 2, "van": "Onderwijscatalogus", "naar": "Planningssysteem",
     "pijl": "id-1", "koppeling": "OC-P&R", "beeld_id": "F2-03"},
    {"soort": "stroomt", "fase": 2, "van": "Planningssysteem", "naar": "Onderwijscatalogus",
     "pijl": "id-2", "koppeling": "OC-P&R", "beeld_id": "F2-07"},
    {"soort": "stroomt", "fase": 4, "van": "Onderwijscatalogus", "naar": "Leer management systeem (LMS)",
     "pijl": "id-3", "koppeling": "OC-LMS", "beeld_id": "F4-02"},
    {"soort": "ontstaat", "fase": 1, "objecttype": "Leeruitkomst", "beeld_id": "F1-03"},
]}


class StromenPerKoppelingTests(unittest.TestCase):
    def test_given_koppelingen_when_grouped_then_only_their_flows(self):
        uit = hp.stromen_per_koppeling(REGELS, ["OC-LMS"])
        self.assertEqual(list(uit), [("Onderwijscatalogus", "Leer management systeem (LMS)", "id-3")])
        self.assertEqual(list(uit.values()), [["OC-LMS"]])

    def test_given_two_directions_when_grouped_then_both_lines_keep_the_name(self):
        uit = hp.stromen_per_koppeling(REGELS, ["OC-P&R"])
        self.assertEqual(len(uit), 2)
        self.assertTrue(all(v == ["OC-P&R"] for v in uit.values()))

    def test_given_unknown_koppeling_when_grouped_then_empty(self):
        self.assertEqual(hp.stromen_per_koppeling(REGELS, ["OC-SIS"]), {})

    def test_given_two_boxes_when_orthogonal_path_then_segments_are_axis_aligned(self):
        a = {"x": 0, "y": 0, "w": 100, "h": 60}
        rechts = {"x": 300, "y": 10, "w": 100, "h": 60}
        onder = {"x": 0, "y": 300, "w": 100, "h": 60}
        schuin = {"x": 400, "y": 400, "w": 100, "h": 60}
        for b in (rechts, onder, schuin):
            punten = hp.haaks_pad(a, b, {})
            for (x1, y1), (x2, y2) in zip(punten, punten[1:]):
                self.assertTrue(x1 == x2 or y1 == y2, f"segment niet haaks: {(x1, y1)} naar {(x2, y2)}")
        self.assertEqual(hp.haaks_pad(a, rechts, {}), [(100, 35.0), (300, 35.0)])

    def test_given_two_lines_on_the_same_side_when_drawn_then_they_do_not_overlap(self):
        a = {"x": 0, "y": 0, "w": 100, "h": 60}
        b = {"x": 300, "y": 0, "w": 100, "h": 60}
        c = {"x": 300, "y": 0, "w": 100, "h": 60}
        aanhecht = {}
        eerste = hp.haaks_pad(a, b, aanhecht)
        tweede = hp.haaks_pad(a, c, aanhecht)
        self.assertNotEqual(eerste[0][1], tweede[0][1])

class HaaksRouterTests(unittest.TestCase):
    """De router houdt de banen uit elkaar en uit de vakken; anders leest een volle plaat niet."""

    @staticmethod
    def _snijdt(punten, vak):
        x1, y1, x2, y2 = vak["x"], vak["y"], vak["x"] + vak["w"], vak["y"] + vak["h"]
        for (ax, ay), (bx, by) in zip(punten, punten[1:]):
            if min(ax, bx) < x2 and x1 < max(ax, bx) and min(ay, by) < y2 and y1 < max(ay, by):
                return True
        return False

    def test_given_two_flows_between_the_same_boxes_when_routed_then_they_run_beside_each_other(self):
        a = {"x": 0, "y": 0, "w": 120, "h": 60}
        b = {"x": 400, "y": 0, "w": 120, "h": 60}
        router = hp.Haaks([a, b])
        heen, terug = router.pad(a, b), router.pad(b, a)
        self.assertNotEqual(heen[0][1], terug[0][1])
        self.assertGreaterEqual(abs(heen[0][1] - terug[0][1]), hp.Haaks.KRAP)

    def test_given_a_box_in_between_when_routed_then_the_line_keeps_clear_of_it(self):
        a = {"x": 0, "y": 0, "w": 120, "h": 60}
        b = {"x": 0, "y": 300, "w": 120, "h": 60}
        dwars = {"x": 0, "y": 150, "w": 90, "h": 60}
        punten = hp.Haaks([a, b, dwars]).pad(a, b)
        self.assertFalse(self._snijdt(punten, dwars), f"lijn loopt door een vak: {punten}")
        for (x1, y1), (x2, y2) in zip(punten, punten[1:]):
            self.assertTrue(x1 == x2 or y1 == y2)


class AanhechtingTests(unittest.TestCase):
    """Twee lijnen uit hetzelfde vak hechten aan in de volgorde waarin hun overkanten liggen.

    Staan zij in de verkeerde volgorde, dan moeten die lijnen elkaar wel passeren; dat patroon
    leverde op de hoofdplaat het meeste kruiswerk op. En waar een route toch een lijn zou
    kruisen, wijkt zij liever een baan opzij.
    """

    def test_given_two_targets_when_planned_then_the_attachments_follow_their_order(self):
        vak = {"x": 0, "y": 0, "w": 200, "h": 60}
        links = {"x": -400, "y": 400, "w": 120, "h": 60}
        rechts = {"x": 500, "y": 400, "w": 120, "h": 60}
        # het vak naar rechts wordt als eerste aangeboden; de ligging beslist, niet de volgorde
        router = hp.Haaks([vak, links, rechts], [(vak, rechts), (vak, links)])
        self.assertLess(router.wensen[(id(vak), "x", id(links))],
                        router.wensen[(id(vak), "x", id(rechts))])
        self.assertLess(router.wensen[(id(vak), "y", id(links))],
                        router.wensen[(id(vak), "y", id(rechts))])

    def test_given_a_line_that_is_already_there_when_counted_then_a_crossing_shows_up(self):
        router = hp.Haaks()
        router._bezet([(0, 50), (200, 50)])
        self.assertEqual(router._kruisingen([(100, 0), (100, 100)]), 1)
        self.assertEqual(router._kruisingen([(300, 0), (300, 100)]), 0)

    def test_given_a_line_across_the_middle_when_routed_then_the_new_line_steps_aside(self):
        a = {"x": 0, "y": 0, "w": 160, "h": 60}
        b = {"x": 0, "y": 400, "w": 160, "h": 60}
        router = hp.Haaks([a, b])
        router._bezet([(-100, 200), (100, 200)])       # deze baan ligt dwars voor het midden
        self.assertGreater(router.pad(a, b)[0][0], 100)
        self.assertEqual(hp.Haaks([a, b]).pad(a, b)[0][0], 80)


if __name__ == "__main__":
    unittest.main()


class VensterTests(unittest.TestCase):
    """De uitsnede houdt de gemarkeerde vakken vast en blijft binnen de plaat."""

    KNOPEN = [dict(x=200, y=300, w=120, h=55), dict(x=500, y=400, w=120, h=55)]

    def test_given_marked_nodes_when_cropped_then_window_holds_them_with_air(self):
        x, y, w, h = hp.venster(self.KNOPEN, 0, 0, 2000, 1500, lucht=50)
        self.assertEqual((x, y), (150, 250))
        self.assertEqual((w, h), (520, 255))

    def test_given_air_beyond_the_plate_when_cropped_then_it_clips(self):
        x, y, w, h = hp.venster(self.KNOPEN, 0, 0, 640, 470, lucht=100)
        self.assertEqual((x, y), (100, 200))
        self.assertEqual((x + w, y + h), (640, 470))


class VensterBurenTests(unittest.TestCase):
    """Een vak op de rand komt er helemaal in, zonder dat het venster doorgroeit."""

    def test_given_node_on_the_edge_when_cropped_then_it_is_taken_in_whole(self):
        geraakt = [dict(x=300, y=300, w=100, h=50)]
        buur = dict(x=180, y=300, w=100, h=50)          # steekt net in het venster
        ver = dict(x=0, y=300, w=100, h=50)             # raakt het venster niet
        x, y, w, h = hp.venster(geraakt, 0, 0, 2000, 1500, lucht=50, buren=[buur, ver])
        self.assertEqual(x, 172)
        self.assertEqual(x + w, 450)
