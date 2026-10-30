"""Testgevallen voor tools/scripts/validate-docs.py.

De voorcontrole bewaakt markdown-deliverables. Wat zij meldt moet kloppen: een melding die
onterecht is leert mensen om de uitkomst te negeren.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("validate_docs", WORTEL / "tools/scripts/validate-docs.py")
vd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vd)


class DodeLinks(unittest.TestCase):

    def map_met(self, *bestanden):
        """Een tijdelijke map met de genoemde bestanden, en het pad naar het eerste."""
        d = Path(tempfile.mkdtemp())
        for naam in bestanden:
            (d / naam).parent.mkdir(parents=True, exist_ok=True)
            (d / naam).write_text("x", encoding="utf-8")
        return d

    def controleer(self, map_, inhoud):
        doc = map_ / "doc.md"
        doc.write_text(inhoud, encoding="utf-8")
        return vd.check_file(doc)

    def test_given_a_link_to_a_name_with_a_space_when_checked_then_no_finding(self):
        d = self.map_met("img/MOKA voorblad.png")
        meldingen = self.controleer(d, "![plaat](img/MOKA%20voorblad.png)\n")
        self.assertEqual([m for m in meldingen if "dode link" in m], [])

    def test_given_a_link_to_a_missing_file_when_checked_then_a_finding(self):
        d = self.map_met("img/bestaat.png")
        meldingen = self.controleer(d, "![plaat](img/bestaat%20niet.png)\n")
        self.assertTrue([m for m in meldingen if "dode link" in m])

    def test_given_a_link_without_escapes_when_checked_then_still_resolved(self):
        d = self.map_met("doc/ander.md")
        meldingen = self.controleer(d, "[ander](doc/ander.md)\n")
        self.assertEqual([m for m in meldingen if "dode link" in m], [])


if __name__ == "__main__":
    unittest.main()
