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


def zichtbare_tekst(slide):
    """Wat de zaal leest: zonder sprekersnotitie, HTML-tags, attributen en iconen."""
    tekst = re.sub(r"<!--.*?-->", " ", slide, flags=re.S)          # sprekersnotities
    tekst = re.sub(r"<(carbon|mdi)-[a-z0-9-]+[^>]*/?>", " ", tekst)  # pictogrammen
    tekst = re.sub(r"<[^>]+>", " ", tekst)                          # overige tags
    tekst = re.sub(r"&[a-z]+;", " ", tekst)                         # entiteiten
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


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("deck", nargs="+", type=pathlib.Path)
    parser.add_argument("--budget", type=int, default=BUDGET)
    parser.add_argument("--grens", type=int, default=GRENS, help="hierboven is het een bevinding")
    args = parser.parse_args(argv)
    fout = False
    for pad in args.deck:
        if not pad.exists():
            print(f"deck niet gevonden: {pad}", file=sys.stderr)
            fout = True
            continue
        print(f"{pad}")
        for nummer, aantal in tel(pad):
            merk = "" if aantal <= args.budget else ("  let op" if aantal <= args.grens else "  te veel tekst")
            print(f"  slide {nummer}: {aantal} woorden{merk}")
            if aantal > args.grens:
                fout = True
    if fout:
        print(f"\nEen slide boven {args.grens} woorden leest niemand. Maak er steekwoorden van met een "
              f"drager: pictogram, kaart, pijplijn of plaat.", file=sys.stderr)
    return 1 if fout else 0


if __name__ == "__main__":
    raise SystemExit(main())
