#!/usr/bin/env python3
"""Keurt een gegenereerde architectuurplaat op de eigenschappen die haar leesbaar maken.

Waarom dit script bestaat: een plaat die uit het model wordt getekend ziet er in de terminal
altijd goed uit, want daar staat alleen een regel met een aantal. Wat een plaat onleesbaar
maakt zit in de SVG zelf: een lijn die schuin wegloopt, twee lijnen die over elkaar heen gaan,
een naam die uit het doek valt, of tekst die zo klein is dat zij op een slide verdwijnt. Dit
script meet dat, zodat de kwaliteit aan een poort hangt en niet aan oplettendheid.

Wat er gemeld wordt:

  SCHUIN      een segment loopt niet horizontaal en niet verticaal
  BUITEN      een tekst valt buiten het doek
  KLEIN       een tekst staat kleiner dan de ondergrens
  IJL         de tekst is te klein ten opzichte van de plaat om op een slide te lezen
  KRUISING    er gaan meer lijnen over elkaar heen dan afgesproken

De eerste vier zijn harde eisen: het script eindigt met een foutcode zodra er een staat.
Kruisingen horen erbij maar zijn niet altijd te vermijden; met `--max-kruisingen` legt een
plaat haar eigen bovengrens vast, zodat een latere wijziging het niet stilletjes erger maakt.

Gebruik:
    python3 scripts/keur-plaat.py <plaat>.svg [<plaat>.svg ...]
    python3 scripts/keur-plaat.py plaat.svg --max-kruisingen 14
    python3 scripts/keur-plaat.py platen/*.svg --stil        # alleen wat er mis is
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG = "{http://www.w3.org/2000/svg}"
RECHT = 0.5          # een verschil kleiner dan dit telt als nul
SCHEEF = 2.0         # zoveel mag een segment afwijken voordat het als schuin telt
SCHEEF_DEEL = 0.01   # of zoveel van zijn eigen lengte, wat van de twee het ruimst is
TEKEN = 0.55         # geschatte breedte van een teken ten opzichte van de lettermaat
MIN_LETTER = 9.0     # onder deze maat leest een tekst ook van dichtbij niet
MIN_VERHOUDING = 0.0035   # de gebruikelijke lettermaat gedeeld door de breedte van de plaat
GETAL = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
EENHEID = {"pt": 4 / 3, "pc": 16, "mm": 3.7795, "cm": 37.795, "in": 96, "px": 1, "": 1}
EEN = (1.0, 1.0, 0.0, 0.0)   # de transformatie die niets verandert


class Bevinding:
    def __init__(self, code, waar, wat):
        self.code, self.waar, self.wat = code, waar, wat

    def __str__(self):
        return f"  {self.code:<9} {self.waar:<22} {self.wat}"


# ------------------------------------------------------------------ inlezen --

def lengte(waarde, standaard=0.0):
    """Een SVG-lengte als getal in pixels; pt en de andere eenheden rekenen mee."""
    if waarde is None:
        return standaard
    tekst = str(waarde).strip()
    getal = GETAL.match(tekst)
    if not getal:
        return standaard
    return float(getal.group()) * EENHEID.get(tekst[getal.end():].strip().lower(), 1)


def eigenschap(el, naam):
    """De waarde van een eigenschap, of die nu als attribuut of in style staat."""
    if el.get(naam) is not None:
        return el.get(naam)
    gevonden = re.search(rf"(?:^|;)\s*{naam}\s*:\s*([^;]+)", el.get("style") or "")
    return gevonden.group(1).strip() if gevonden else None


def samen(buitenste, binnenste):
    """Twee transformaties na elkaar: eerst de binnenste, dan de buitenste."""
    if buitenste is None or binnenste is None:
        return None
    sx, sy, dx, dy = buitenste
    bx, by, bdx, bdy = binnenste
    return (sx * bx, sy * by, dx + sx * bdx, dy + sy * bdy)


def transformatie(el):
    """De transformatie van een element als schaal en verschuiving; None bij een draaiing.

    Een gedraaide of geschuinde groep valt buiten wat dit script narekent. Die inhoud telt wel
    mee in de aantallen, maar niet in de meting op plek en richting.
    """
    tekst = el.get("transform")
    if not tekst:
        return EEN
    uit = EEN
    for naam, argument in re.findall(r"([a-zA-Z]+)\s*\(([^)]*)\)", tekst):
        deel = [float(g) for g in GETAL.findall(argument)]
        if naam == "translate" and deel:
            stap = (1.0, 1.0, deel[0], deel[1] if len(deel) > 1 else 0.0)
        elif naam == "scale" and deel:
            stap = (deel[0], deel[1] if len(deel) > 1 else deel[0], 0.0, 0.0)
        elif naam == "matrix" and len(deel) == 6 and abs(deel[1]) < 1e-9 and abs(deel[2]) < 1e-9:
            stap = (deel[0], deel[3], deel[4], deel[5])
        else:
            return None
        uit = samen(uit, stap)
    return uit


def polylijn(d):
    """De punten van een pad dat alleen uit rechte stukken bestaat; None bij een kromme."""
    if re.search(r"[CcSsQqTtAa]", d):
        return None
    punten, hier = [], None
    for stuk in re.findall(r"[MmLlHhVvZz][^MmLlHhVvZz]*", d):
        bevel, deel = stuk[0], [float(g) for g in GETAL.findall(stuk[1:])]
        if bevel in "Zz":
            if punten:
                punten.append(punten[0])
        elif bevel in "Hh" and deel and hier:
            hier = (deel[-1] if bevel == "H" else hier[0] + deel[-1], hier[1])
            punten.append(hier)
        elif bevel in "Vv" and deel and hier:
            hier = (hier[0], deel[-1] if bevel == "V" else hier[1] + deel[-1])
            punten.append(hier)
        else:
            for i in range(0, len(deel) - 1, 2):
                x, y = deel[i], deel[i + 1]
                hier = (x, y) if bevel.isupper() or hier is None else (hier[0] + x, hier[1] + y)
                punten.append(hier)
    return punten


def ontleed(wortel):
    """De lijnen en de teksten van de plaat, met de verschuiving van hun groep erin verrekend.

    Een lijn staat er vaak twee keer: een witte onderlaag en de lijn zelf, met hetzelfde pad.
    Een pad dat al gezien is telt niet opnieuw mee. Wat in `defs` staat is een sjabloon voor
    een pijlpunt en hoort niet bij de tekening.
    """
    lijn, tekst, gezien = [], [], set()

    def loop(el, vorm, maat, anker):
        if el.tag == SVG + "defs":
            return
        vorm = samen(vorm, transformatie(el))
        maat = lengte(eigenschap(el, "font-size"), maat)
        anker = eigenschap(el, "text-anchor") or anker
        if el.tag == SVG + "path":
            d = el.get("d") or ""
            if d and d not in gezien and (eigenschap(el, "fill") or "none") == "none":
                gezien.add(d)
                punten = polylijn(d)
                if punten and len(punten) > 1 and vorm:
                    lijn.append([(p[0] * vorm[0] + vorm[2], p[1] * vorm[1] + vorm[3])
                                 for p in punten])
        elif el.tag == SVG + "text":
            inhoud = "".join(el.itertext()).strip()
            if inhoud:
                groot = maat * (abs(vorm[0]) if vorm else 1.0)
                breed = len(inhoud) * groot * TEKEN
                x, y = lengte(el.get("x")), lengte(el.get("y"))
                if vorm:
                    x, y = x * vorm[0] + vorm[2], y * vorm[1] + vorm[3]
                links = x - breed / 2 if anker == "middle" else (x - breed if anker == "end" else x)
                tekst.append(dict(tekst=inhoud, maat=groot, plaatsbaar=vorm is not None,
                                  doos=(links, y - groot, breed, groot * 1.25)))
            return
        for kind in el:
            loop(kind, vorm, maat, anker)

    loop(wortel, EEN, 0.0, "start")
    return lijn, tekst


def doek(wortel):
    """De maat van de plaat, uit de viewBox of anders uit breedte en hoogte."""
    kijk = wortel.get("viewBox")
    if kijk:
        deel = [float(g) for g in GETAL.findall(kijk)]
        if len(deel) == 4:
            return deel[2], deel[3]
    return lengte(wortel.get("width")), lengte(wortel.get("height"))


# -------------------------------------------------------------------- meten --

def segmenten(punten):
    return list(zip(punten, punten[1:]))


def schuin(lijnen):
    """De segmenten die noch horizontaal noch verticaal lopen.

    Een afronding van een pixel op een lang been maakt een lijn nog niet schuin; pas een
    afwijking die opvalt telt mee, en die schaalt mee met de lengte van het been.
    """
    uit = []
    for punten in lijnen:
        for (x1, y1), (x2, y2) in segmenten(punten):
            kort, lang = sorted((abs(x1 - x2), abs(y1 - y2)))
            if kort > max(SCHEEF, SCHEEF_DEEL * lang):
                uit.append(((x1, y1), (x2, y2)))
    return uit


def kruisingen(lijnen):
    """De plekken waar een liggend segment van de ene lijn een staand van de andere doorsnijdt."""
    liggend, staand = [], []
    for nummer, punten in enumerate(lijnen):
        for (x1, y1), (x2, y2) in segmenten(punten):
            if abs(y1 - y2) <= RECHT and abs(x1 - x2) > RECHT:
                liggend.append((y1, min(x1, x2), max(x1, x2), nummer))
            elif abs(x1 - x2) <= RECHT and abs(y1 - y2) > RECHT:
                staand.append((x1, min(y1, y2), max(y1, y2), nummer))
    return [(x, y) for y, van, tot, a in liggend for x, boven, onder, b in staand
            if a != b and van + RECHT < x < tot - RECHT and boven + RECHT < y < onder - RECHT]


def buiten(doos, breed, hoog, speling=1.0):
    """Of een omhullende over de rand van het doek hangt."""
    return (doos[0] < -speling or doos[1] < -speling
            or doos[0] + doos[2] > breed + speling or doos[1] + doos[3] > hoog + speling)


def keur(pad, min_letter=MIN_LETTER, min_verhouding=MIN_VERHOUDING, max_kruisingen=None):
    """De plaat nakijken; geeft de bevindingen en de gemeten waarden terug."""
    wortel = ET.parse(pad).getroot()
    breed, hoog = doek(wortel)
    lijn, tekst = ontleed(wortel)
    maten = sorted(t["maat"] for t in tekst if t["maat"] > 0)
    kruis = kruisingen(lijn)
    bevindingen = []

    for a, b in schuin(lijn):
        bevindingen.append(Bevinding("SCHUIN", f"{a[0]:.0f},{a[1]:.0f}",
                                     f"segment loopt naar {b[0]:.0f},{b[1]:.0f}"))
    for t in tekst:
        if t["plaatsbaar"] and buiten(t["doos"], breed, hoog):
            bevindingen.append(Bevinding("BUITEN", f"{t['doos'][0]:.0f},{t['doos'][1]:.0f}",
                                         f"tekst valt buiten het doek: {t['tekst'][:40]}"))
        if 0 < t["maat"] < min_letter:
            bevindingen.append(Bevinding("KLEIN", f"{t['maat']:.1f} px",
                                         f"onder de ondergrens {min_letter:g}: {t['tekst'][:40]}"))
    verhouding = (maten[len(maten) // 2] / breed) if maten and breed else 0
    if verhouding and verhouding < min_verhouding:
        bevindingen.append(Bevinding("IJL", f"{verhouding:.4f}",
                                     f"tekst te klein voor een plaat van {breed:.0f} breed, "
                                     f"ondergrens {min_verhouding:g}"))
    if max_kruisingen is not None and len(kruis) > max_kruisingen:
        bevindingen.append(Bevinding("KRUISING", f"{len(kruis)}",
                                     f"meer dan de afgesproken {max_kruisingen}"))
    return bevindingen, dict(breedte=breed, hoogte=hoog, lijnen=len(lijn), teksten=len(tekst),
                             kruisingen=len(kruis), verhouding=verhouding,
                             kleinste=maten[0] if maten else 0, grootste=maten[-1] if maten else 0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("platen", nargs="+", type=Path)
    p.add_argument("--min-letter", type=float, default=MIN_LETTER)
    p.add_argument("--min-verhouding", type=float, default=MIN_VERHOUDING)
    p.add_argument("--max-kruisingen", type=int, default=None)
    p.add_argument("--stil", action="store_true", help="alleen de platen met een bevinding tonen")
    p.add_argument("--hoogstens", type=int, default=8, help="zoveel bevindingen per code tonen")
    args = p.parse_args()

    gezakt = 0
    for plaat in args.platen:
        bevindingen, maat = keur(plaat, args.min_letter, args.min_verhouding, args.max_kruisingen)
        if bevindingen or not args.stil:
            print(f"{plaat}: {maat['breedte']:.0f} bij {maat['hoogte']:.0f}, "
                  f"{maat['lijnen']} lijnen, {maat['teksten']} teksten, "
                  f"{maat['kruisingen']} kruisingen, letter {maat['kleinste']:g} tot "
                  f"{maat['grootste']:g}, verhouding {maat['verhouding']:.4f}")
        per_code = {}
        for b in bevindingen:
            per_code[b.code] = per_code.get(b.code, 0) + 1
            if per_code[b.code] <= args.hoogstens:
                print(b)
        for code, aantal in per_code.items():
            if aantal > args.hoogstens:
                print(f"  {code:<9} {'':<22} en nog {aantal - args.hoogstens} keer")
        if bevindingen:
            gezakt += 1
            print(f"  AFGEKEURD {len(bevindingen)} bevindingen")
        elif not args.stil:
            print("  GOEDGEKEURD")
    return 1 if gezakt else 0


if __name__ == "__main__":
    sys.exit(main())
