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

&middot; een twee drie &#8594;
"""


CODEDECK = """---
title: x
---

# Kop met code

<code>GET /onderwijsaanbod/{id}</code>

<pre>{
  "naam": "Apothekersassistent",
  "status": "gepland"
}</pre>
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
        self.assertEqual(uit[1], (2, 5))          # kop (2) plus drie woorden, entiteiten tellen niet

    def test_given_frontmatter_when_counted_then_it_is_not_a_slide(self):
        self.assertEqual(len(self.tel()), 2)

    def test_given_deck_above_the_limit_when_run_then_exit_code_one(self):
        lang = "---\ntitle: x\n---\n\n# " + " ".join(["woord"] * 70) + "\n"
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "deck.md"
            pad.write_text(lang, encoding="utf-8")
            self.assertEqual(tw.main([str(pad)]), 1)
            self.assertEqual(tw.main([str(pad), "--grens", "100"]), 0)


BEELDDECK = """---
title: x
---

# Kop met diagram

<style scoped>
.mermaid svg { max-width: 100%; height: auto; }
</style>

```mermaid
sequenceDiagram
    P->>OC: melding
```
"""


class CodeTests(unittest.TestCase):
    """Code op een slide is een beeld: buiten het woordbudget, met een eigen maat."""

    def schrijf(self, bron):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        pad = Path(tmp.name) / "deck.md"
        pad.write_text(bron, encoding="utf-8")
        return pad

    def test_given_slide_with_code_when_counted_then_code_is_not_a_word(self):
        self.assertEqual(tw.tel(self.schrijf(CODEDECK)), [(1, 3)])   # alleen de kop

    def test_given_slide_with_code_when_counted_then_its_lines_are_reported(self):
        self.assertEqual(tw.tel_code(self.schrijf(CODEDECK)), [(1, 4)])

    def test_given_slide_with_style_block_when_counted_then_css_is_not_text(self):
        self.assertEqual(tw.tel(self.schrijf(BEELDDECK)), [(1, 3)])   # alleen de kop

    def test_given_mermaid_block_when_counted_then_it_is_a_plate_not_code(self):
        self.assertEqual(tw.tel_code(self.schrijf(BEELDDECK)), [(1, 0)])

    def test_given_long_fragment_when_run_then_exit_code_one(self):
        pad = self.schrijf(CODEDECK)
        self.assertEqual(tw.main([str(pad)]), 0)
        self.assertEqual(tw.main([str(pad), "--coderegels", "3"]), 1)


if __name__ == "__main__":
    unittest.main()
