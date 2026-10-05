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
import math
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


def _verdeel(wit, hoogte, baan, n):
    """n banen proberen: per grens de witregel die het dichtst bij de gelijke verdeling ligt.

    Geeft (snedes, knelpunt). Een knelpunt is het bereik waar geen witregel ligt; is er geen knelpunt
    en toch geen uitkomst, dan zijn er meer banen nodig.
    """
    uit, start = [], 0.0
    for i in range(1, n):
        doel = hoogte * i / n
        grens = min(start + baan, hoogte)
        kandidaten = [g for g in wit if start < (g[0] + g[1]) / 2 <= grens]
        if not kandidaten:
            return None, (start, grens)
        a, b = min(kandidaten, key=lambda g: abs((g[0] + g[1]) / 2 - doel))
        uit.append((a + b) / 2)
        start = uit[-1]
    if hoogte - start > baan:
        return None, None
    return uit, None


def _snedes(svg, baan):
    """De y-waarden waarop het beeld wordt gesneden, en de reden als het niet lukt.

    De banen worden verdeeld in plaats van volgemaakt: eerst het aantal banen dat nodig is, dan per
    grens de witregel die het dichtst bij de gelijke verdeling ligt. Past de laatste baan niet, dan
    gaat er een baan bij; zo lijken de banen in hoogte op elkaar en blijft elke snede in witruimte.
    """
    _, _, _, hoogte = doek(svg)
    if hoogte <= baan:
        return [], None
    wit = gaten(bezet(svg, hoogte), hoogte)
    knel = None
    for n in range(math.ceil(hoogte / baan), math.ceil(hoogte / GAT) + 1):
        snedes_, knel = _verdeel(wit, hoogte, baan, n)
        if snedes_ is not None:
            return snedes_, None
        if knel:
            break
    van, tot = knel if knel else (0.0, hoogte)
    return [], (f"geen witregel van {GAT:g} punten tussen y={van:g} en y={tot:g}; "
                f"het beeld staat daar vol en past niet in een baan van {baan:g}")


def snedes(svg, baan):
    """De y-waarden waarop het beeld wordt gesneden, altijd in een witregel."""
    return _snedes(svg, baan)[0]


def knelpunt(svg, baan=None):
    """De reden waarom een beeld niet te snijden is, of None als het wel lukt."""
    _, _, breedte, _ = doek(svg)
    return _snedes(svg, baan or breedte * VERHOUDING)[1]


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
    reden = knelpunt(svg, a.baan)
    delen = banen(svg, a.baan, a.marge)
    if reden:
        print(f"{bron.name}: niet te snijden, {reden}", file=sys.stderr)
        return 1
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
