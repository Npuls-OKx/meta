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
