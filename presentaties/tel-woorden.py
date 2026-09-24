#!/usr/bin/env python3
"""De zichtbare woorden per slide tellen en melden welke slide over het budget gaat.

Waarom dit script bestaat: de presentatieskill schrijft rond de veertig zichtbare
woorden per slide voor, en dat blijft anders een voornemen. Dit telt wat er op de
slide staat: koppen, kaarten en bijschriften, zonder sprekersnotities, zonder HTML
en zonder de frontmatter. Een slide boven het budget draagt te veel tekst en vraagt
om steekwoorden met een drager.

    python3 presentaties/tel-woorden.py presentaties/src/260929_werkgroep_okx_voortgang.md

Exitcode 0: alle slides binnen het budget; 1: een of meer slides erboven.
"""

import argparse
import pathlib
import re
import sys

BUDGET = 40
GRENS = 60


CODEREGELS = 12


def zonder_code(slide):
    """Code en payloads eruit: die zijn een beeld, geen leestekst.

    Een endpoint of een voorbeeldbericht op een slide wordt herkend, niet gelezen,
    net als een plaat of een pictogram. Daarom telt het niet mee in het woordbudget.
    Wel geldt een eigen maat: coderegels() bewaakt dat het fragment kort blijft.
    """
    tekst = re.sub(r"```.*?```", " ", slide, flags=re.S)            # gemarkeerde codeblokken
    tekst = re.sub(r"<pre[^>]*>.*?</pre>", " ", tekst, flags=re.S)  # voorbeeldberichten
    return re.sub(r"<code[^>]*>.*?</code>", " ", tekst, flags=re.S)  # endpoints in de tekst


def coderegels(slide):
    """Het aantal regels code op de slide: de maat voor een fragment als beeld.

    Een mermaid-blok telt niet mee: dat rendert tot een diagram, en een diagram is
    een plaat. De regels eronder ziet de zaal nooit.
    """
    blokken = [b for b in re.findall(r"```.*?```", slide, flags=re.S) if not b.startswith("```mermaid")]
    blokken += re.findall(r"<pre[^>]*>.*?</pre>", slide, flags=re.S)
    return sum(len([r for r in blok.splitlines() if r.strip()]) for blok in blokken)


def zichtbare_tekst(slide):
    """Wat de zaal leest: zonder sprekersnotitie, code, HTML-tags, attributen en iconen."""
    tekst = re.sub(r"<!--.*?-->", " ", zonder_code(slide), flags=re.S)  # sprekersnotities
    tekst = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", tekst, flags=re.S)  # opmaak en gedrag
    tekst = re.sub(r"<(carbon|mdi)-[a-z0-9-]+[^>]*/?>", " ", tekst)  # pictogrammen
    tekst = re.sub(r"<[^>]+>", " ", tekst)                          # overige tags
    tekst = re.sub(r"&#?[a-z0-9]+;", " ", tekst)                    # entiteiten, ook pijlen als &#8594;
    tekst = re.sub(r"[#*`|]", " ", tekst)                           # markdown-tekens
    return tekst


def tel(pad):
    bron = pathlib.Path(pad).read_text(encoding="utf-8")
    if bron.startswith("---"):
        bron = bron.split("\n---\n", 1)[-1]                         # frontmatter eraf
    uit = []
    for nummer, slide in enumerate(bron.split("\n---\n"), 1):
        woorden = [w for w in zichtbare_tekst(slide).split() if any(c.isalnum() for c in w)]
        uit.append((nummer, len(woorden)))
    return uit


def tel_code(pad):
    """Per slide het aantal coderegels, in dezelfde volgorde als tel()."""
    bron = pathlib.Path(pad).read_text(encoding="utf-8")
    if bron.startswith("---"):
        bron = bron.split("\n---\n", 1)[-1]
    return [(nummer, coderegels(slide)) for nummer, slide in enumerate(bron.split("\n---\n"), 1)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("deck", nargs="+", type=pathlib.Path)
    parser.add_argument("--budget", type=int, default=BUDGET)
    parser.add_argument("--grens", type=int, default=GRENS, help="hierboven is het een bevinding")
    parser.add_argument("--coderegels", type=int, default=CODEREGELS, help="maximaal aantal regels code per slide")
    args = parser.parse_args(argv)
    fout = False
    for pad in args.deck:
        if not pad.exists():
            print(f"deck niet gevonden: {pad}", file=sys.stderr)
            fout = True
            continue
        print(f"{pad}")
        code = dict(tel_code(pad))
        for nummer, aantal in tel(pad):
            merk = "" if aantal <= args.budget else ("  let op" if aantal <= args.grens else "  te veel tekst")
            regels = code.get(nummer, 0)
            erbij = f", {regels} coderegels" if regels else ""
            if regels > args.coderegels:
                erbij += "  te lang fragment"
                fout = True
            print(f"  slide {nummer}: {aantal} woorden{erbij}{merk}")
            if aantal > args.grens:
                fout = True
    if fout:
        print(f"\nEen slide boven {args.grens} woorden leest niemand, en een fragment boven "
              f"{args.coderegels} regels ook niet. Maak er steekwoorden van met een drager: "
              f"pictogram, kaart, pijplijn, plaat of een kort voorbeeldbericht.", file=sys.stderr)
    return 1 if fout else 0


if __name__ == "__main__":
    raise SystemExit(main())
