"""Testgevallen die de versie op elke plaat en elke uitsnede afdwingen.

Waarom dit een testgeval is en geen losse controle: de werkstroom in CI draait de
testgevallen, dus een selectiebestand zonder versie laat de pull request falen. Een beeld dat
onder een issue hangt of in een deck staat, moet zelf zeggen welke versie het is; anders is na
een ronde niet te zien of iemand naar de vorige of de huidige kijkt.

De regel staat in .cursor/rules/architecture-artifacts.mdc: een eerste beeld begint op 0.1.0,
nieuwe inhoud verhoogt de minor, een correctie de patch, en een beeld dat iets anders zegt dan
de vorige versie de major.
"""

import json
import re
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

MAPPEN = (
    ("project/img/visueel", {"iconen.json"}),
    ("architecture/model/informatiemodel/uitsneden", set()),
)


def selecties():
    """Elk selectiebestand van een plaat, met de bestanden die geen plaat zijn eraf."""
    for map_, overslaan in MAPPEN:
        for pad in sorted((WORTEL / map_).glob("*.json")):
            if pad.name not in overslaan:
                yield pad


class PlaatversieTests(unittest.TestCase):
    def test_given_the_selection_files_when_read_then_there_is_at_least_one(self):
        self.assertGreater(len(list(selecties())), 0, "geen selectiebestanden gevonden")

    def test_given_every_selection_when_read_then_it_carries_a_versie(self):
        zonder = [p.name for p in selecties()
                  if "versie" not in json.loads(p.read_text(encoding="utf-8"))]
        self.assertEqual(zonder, [], f"selectie zonder veld versie: {zonder}")

    def test_given_every_versie_when_read_then_it_follows_semver(self):
        fout = []
        for pad in selecties():
            versie = json.loads(pad.read_text(encoding="utf-8")).get("versie", "")
            if not SEMVER.match(str(versie)):
                fout.append(f"{pad.name}: {versie!r}")
        self.assertEqual(fout, [], f"versie volgt MAJOR.MINOR.PATCH niet: {fout}")

    def test_given_a_drawn_plaat_when_read_then_the_versie_stands_on_it(self):
        for pad in sorted((WORTEL / "project/img/visueel").glob("*.svg")):
            bron = pad.with_suffix(".json")
            if not bron.exists():
                continue
            versie = json.loads(bron.read_text(encoding="utf-8"))["versie"]
            self.assertIn(f">v{versie}<", pad.read_text(encoding="utf-8"),
                          f"{pad.name} draagt versie {versie} niet; teken hem opnieuw")


if __name__ == "__main__":
    unittest.main()
