#!/usr/bin/env python3
"""Een hoog beeld in leesbare banen snijden voor een slide.

Waarom dit script bestaat: een regelbeeld van de voorbeelduitwerking kan hoger zijn dan een
slide breed is. Op een slide geschaald wordt de tekst dan onleesbaar. De oplossing is het beeld
in banen tonen, gesneden in een witregel zodat geen vak doormidden gaat. Dat is eerder met de
hand gedaan; zodra het beeld verandert klopt de snede niet meer. Dit script leidt de snede af
uit het beeld zelf.

De maat is een verhouding, geen hoogte: een brede plaat wordt op een slide vanzelf laag en hoeft
niet gesneden te worden. Gesneden wordt zodra de hoogte meer is dan de breedte maal de verhouding
die de slide toelaat.

    python3 scripts/snijd-beeld.py <beeld>.svg [--uit MAP] [--baan HOOGTE] [--marge 8]

De banen komen als <naam>-deel1.svg, -deel2.svg naast elkaar te staan; elke baan draagt dezelfde
tekening met een eigen viewBox, dus zonder de inhoud te kopieren. Een beeld dat in een baan past
levert niets op en meldt dat.
"""

import argparse
import re
import sys
from pathlib import Path

VERHOUDING = 0.42   # hoogte gedeeld door breedte die een slide toelaat; hoger wordt te klein geschaald
MARGE = 8       # wat er boven en onder een baan mee mag, zodat een rand niet afsnijdt
GAT = 6         # een witregel telt vanaf deze hoogte als snijplek


def doek(svg):
    """De breedte en hoogte uit de viewBox; die is leidend boven width en height."""
    m = re.search(r'viewBox="([\d.\-]+) ([\d.\-]+) ([\d.]+) ([\d.]+)"', svg)
    if not m:
        raise ValueError("geen viewBox gevonden")
    return [float(g) for g in m.groups()]


GETAL = re.compile(r"-?\d+(?:\.\d+)?")


def bezet(svg, hoogte):
    """De y-intervallen waar iets getekend staat, zonder het omhullende kader.

    De icoongroepen staan in een eigen coordinatenstelsel (translate) en zitten altijd binnen
    een vak dat al meetelt; die gaan er eerst uit, zodat hun y-waarden niet meerekenen. Lijnen
    tellen ook niet mee: een verbinding die over de hele hoogte loopt zou anders elke snede
    blokkeren, en door een lijn snijden leest prima.
    """
    svg = re.sub(r"<g\s+transform=\"translate\([^)]*\)\".*?</g>", "", svg, flags=re.S)
    uit = []
    for y, h in re.findall(r'<rect[^>]*\sy="([\d.]+)"[^>]*\sheight="([\d.]+)"', svg):
        y, h = float(y), float(h)
        if h < hoogte * 0.9:                      # het kader zelf telt niet mee
            uit.append((y, y + h))
    for y in re.findall(r'<text[^>]*\sy="([\d.]+)"', svg):
        uit.append((float(y) - 12, float(y) + 5))
    return sorted(uit)


def gaten(intervallen, hoogte):
    """De witregels tussen de getekende delen, elk als (van, tot)."""
    uit, tot_nu = [], 0.0
    for a, b in intervallen:
        if a - tot_nu >= GAT:
            uit.append((tot_nu, a))
        tot_nu = max(tot_nu, b)
    if hoogte - tot_nu >= GAT:
        uit.append((tot_nu, hoogte))
    return uit


def snedes(svg, baan):
    """De y-waarden waarop het beeld wordt gesneden, altijd in een witregel."""
    _, _, _, hoogte = doek(svg)
    if hoogte <= baan:
        return []
    wit = gaten(bezet(svg, hoogte), hoogte)
    uit, start = [], 0.0
    while hoogte - start > baan:
        kandidaten = [g for g in wit if start + baan * 0.45 < (g[0] + g[1]) / 2 <= start + baan]
        if not kandidaten:
            break
        a, b = max(kandidaten, key=lambda g: ((g[0] + g[1]) / 2, g[1] - g[0]))
        snede = (a + b) / 2
        uit.append(snede)
        start = snede
    return uit


def banen(svg, baan=None, marge=MARGE):
    """Het beeld als reeks viewBox-vensters; elk venster is dezelfde tekening."""
    x, y0, breedte, hoogte = doek(svg)
    baan = baan or breedte * VERHOUDING
    grenzen = [0.0] + snedes(svg, baan) + [hoogte]
    uit = []
    for i in range(len(grenzen) - 1):
        boven = max(0.0, grenzen[i] - (marge if i else 0))
        onder = min(hoogte, grenzen[i + 1] + (marge if i + 1 < len(grenzen) - 1 else 0))
        h = onder - boven
        deel = re.sub(r'viewBox="[^"]*"', f'viewBox="{x:g} {boven:g} {breedte:g} {h:g}"', svg, count=1)
        deel = re.sub(r'\swidth="[\d.]+"\sheight="[\d.]+"',
                      f' width="{breedte:g}" height="{h:g}"', deel, count=1)
        uit.append(deel)
    return uit


def main():
    p = argparse.ArgumentParser()
    p.add_argument("beeld")
    p.add_argument("--uit", default=None, help="map voor de banen; standaard naast het beeld")
    p.add_argument("--baan", type=float, default=None,
                   help="bandhoogte; standaard de breedte maal %.2f" % VERHOUDING)
    p.add_argument("--marge", type=float, default=MARGE)
    a = p.parse_args()
    bron = Path(a.beeld)
    svg = bron.read_text(encoding="utf-8")
    delen = banen(svg, a.baan, a.marge)
    if len(delen) == 1:
        print(f"{bron.name}: past in een baan, niets gesneden")
        return 0
    map_ = Path(a.uit) if a.uit else bron.parent
    map_.mkdir(parents=True, exist_ok=True)
    for i, deel in enumerate(delen, 1):
        pad = map_ / f"{bron.stem}-deel{i}.svg"
        pad.write_text(deel, encoding="utf-8")
    print(f"{bron.name}: {len(delen)} banen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
