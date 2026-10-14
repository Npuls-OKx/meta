#!/usr/bin/env python3
"""Keurt leeruitkomsten op de vorm die de NLQF-handleiding voorschrijft.

Waarom dit script bestaat: een leeruitkomst leest bijna altijd als een nette zin, ook als
een van de vijf plekken uit het tuning model ontbreekt. Wat eruit valt merkt niemand bij het
lezen, maar wel bij het toetsen: zonder standaard is er geen criterium, zonder context geen
omgeving waarin het bewijs geldt. Dit script meet de vorm, zodat die aan een poort hangt en
niet aan oplettendheid.

De handleiding telt tien controlevragen. Vier daarvan zijn machinaal te toetsen en staan
hieronder; de zes die een menselijk oordeel vragen staan in de skill okx-leeruitkomst-formuleren.

Wat er gemeld wordt:

  STANDAARD   de zin draagt geen herkenbare standaard
  CONTEXT     de zin draagt geen herkenbare context
  WERKWOORDEN de zin draagt meer dan een handeling
  TAXONOMIE   er is geen taxonomiecode, of zij past niet bij het NLQF-niveau

Bron: Handleiding Formuleren leeruitkomsten, NCP NLQF, december 2020, paragraaf 2.3 en 2.6.
"""

import argparse
import json
import pathlib
import re
import sys

# de signaalwoorden waarmee de handleiding een standaard en een context aankondigt, zoals
# teruggevonden in de bestaande leeruitkomsten van de voorbeelduitwerking
STANDAARD_WOORDEN = ("volgens", "aan de hand van", "toetsbaar aan", "op basis van",
                     "conform", "onderbouwd met", "geverifieerd bij", "met navolgbare",
                     "uit het hoofd", "met een onderbouwd")
CONTEXT_WOORDEN = (" in ", " bij ", " op de ", " op een ", " onder begeleiding", " in een ")

# Een tweede handeling kondigt zich aan met "en" gevolgd door een vervoegd werkwoord. In het
# Nederlands eindigt dat in de derde persoon op een t. Zelfstandige naamwoorden op -en vallen
# daarmee af, en de korte woorden op -t die geen werkwoord zijn staan in de uitzonderingen
NIET_EEN_WERKWOORD = {"het", "dat", "wat", "niet", "met", "tot", "want", "want", "recht",
                      "licht", "zicht", "gedrag", "inzicht", "overleg", "advies"}
TWEEDE_HANDELING = re.compile(r",?\s+en\s+([a-z]{5,}t)\b", re.IGNORECASE)

ROMISZOWSKI = {"Ff", "Fp", "Bb", "Bp", "Rc", "Rpm", "Rr", "Ri", "Pc", "Ppm", "Pr", "Pi"}
SOLO = {"solo0", "solo1", "solo2", "solo3", "solo4"}
NLQF = re.compile(r"NLQF\s*(?:niveau\s*)?(\d)", re.IGNORECASE)


class Bevinding:
    def __init__(self, code, zin, uitleg):
        self.code, self.zin, self.uitleg = code, zin, uitleg

    def __str__(self):
        return f"  {self.code:<11} {self.zin[:46]:<48} {self.uitleg}"


def niveau_van(zin):
    """Het NLQF-niveau zoals de zin het vermeldt, of None."""
    m = NLQF.search(zin)
    return int(m.group(1)) if m else None


def keur(zin, taxonomie=None):
    """Alle bevindingen op een leeruitkomst. Een lege lijst betekent dat de vorm klopt."""
    uit = []
    laag = zin.lower()
    if not any(w in laag for w in STANDAARD_WOORDEN):
        uit.append(Bevinding("STANDAARD", zin, "geen signaalwoord als volgens of aan de hand van"))
    if not any(w in laag for w in CONTEXT_WOORDEN):
        uit.append(Bevinding("CONTEXT", zin, "geen omgeving waarin het wordt getoond"))
    for tweede in TWEEDE_HANDELING.finditer(zin):
        woord = tweede.group(1)
        if woord.lower() not in NIET_EEN_WERKWOORD:
            uit.append(Bevinding("WERKWOORDEN", zin, f"tweede handeling: {woord}"))
            break
    niveau = niveau_van(zin)
    if taxonomie is None:
        uit.append(Bevinding("TAXONOMIE", zin, "geen taxonomiecode vastgelegd"))
    elif niveau is not None:
        hoort = ROMISZOWSKI if niveau <= 4 else SOLO
        if taxonomie not in hoort:
            welke = "Romiszowski" if niveau <= 4 else "SOLO"
            uit.append(Bevinding("TAXONOMIE", zin, f"{taxonomie} past niet bij NLQF {niveau}, verwacht {welke}"))
    return uit


def leeruitkomsten_uit(pad):
    """De geformuleerde leeruitkomsten uit een regeltabel, als paren van zin en taxonomiecode.

    Alleen regels waarin een leeruitkomst ontstaat tellen mee. In een regel die stroomt is de
    leeruitkomst lading: daar staat welke waarde er over de koppeling gaat, en dat is geen
    formulering. "Al behaald door Jochem: geen" hoort dus niet gekeurd te worden."""
    model = json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    uit, gezien = [], set()
    for regel in model.get("regels", []):
        if regel.get("objecttype") != "Leeruitkomst" or regel.get("soort") != "ontstaat":
            continue
        zin = regel.get("instantie", "")
        if zin and zin not in gezien:
            gezien.add(zin)
            uit.append((zin, regel.get("taxonomie")))
    return uit


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("paden", nargs="+", help="regeltabellen in JSON, of tekstbestanden met een leeruitkomst per regel")
    p.add_argument("--stil", action="store_true", help="meld alleen de bestanden met bevindingen")
    args = p.parse_args()

    gezakt = 0
    for pad in args.paden:
        if pad.endswith(".json"):
            stel = leeruitkomsten_uit(pad)
        else:
            stel = [(r.strip(), None) for r in pathlib.Path(pad).read_text(encoding="utf-8").splitlines() if r.strip()]
        bevindingen = [b for zin, tax in stel for b in keur(zin, tax)]
        if bevindingen or not args.stil:
            print(f"{pad}: {len(stel)} leeruitkomsten")
        for b in bevindingen:
            print(b)
        if bevindingen:
            gezakt += 1
            print(f"  AFGEKEURD {len(bevindingen)} bevindingen op {len(stel)} leeruitkomsten")
        elif not args.stil:
            print("  GOEDGEKEURD")
    return 1 if gezakt else 0


if __name__ == "__main__":
    sys.exit(main())
