"""Testgevallen voor presentaties/tel-woorden.py.

De teller moet tellen wat de zaal leest: geen sprekersnotities, geen HTML,
geen pictogramtags en geen frontmatter.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("tel_woorden", WORTEL / "presentaties/tel-woorden.py")
tw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tw)

DECK = """---
theme: default
title: "Titel met vier woorden hier"
---

# Kop van de slide

<div class="np-card accent-blue" style="font-size: 1rem;">
  <carbon-user-multiple style="font-size: 2rem;" />
  <strong>Drie korte woorden</strong>
</div>

<!--
Deze sprekersnotitie bevat veel woorden die de zaal nooit ziet en dus niet meetellen
in het budget van de slide zelf.
-->

---

# Tweede slide

&middot; een twee drie
"""


class TelWoordenTests(unittest.TestCase):
    def tel(self, bron=DECK):
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "deck.md"
            pad.write_text(bron, encoding="utf-8")
            return tw.tel(pad)

    def test_given_slide_with_notes_and_html_when_counted_then_only_visible_words(self):
        uit = self.tel()
        self.assertEqual(uit[0], (1, 7))          # kop (4) plus de kaart (3), niets uit de notitie
        self.assertEqual(uit[1], (2, 5))          # kop (2) plus drie woorden

    def test_given_frontmatter_when_counted_then_it_is_not_a_slide(self):
        self.assertEqual(len(self.tel()), 2)

    def test_given_deck_above_the_limit_when_run_then_exit_code_one(self):
        lang = "---\ntitle: x\n---\n\n# " + " ".join(["woord"] * 70) + "\n"
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "deck.md"
            pad.write_text(lang, encoding="utf-8")
            self.assertEqual(tw.main([str(pad)]), 1)
            self.assertEqual(tw.main([str(pad), "--grens", "100"]), 0)


if __name__ == "__main__":
    unittest.main()
