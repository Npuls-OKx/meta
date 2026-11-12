#!/usr/bin/env python3
"""Legt vast uit welke modelstaat een geexporteerde plaat komt.

Waarom dit script bestaat: de viewnamen in het ArchiMate-model dragen geen versie
meer. De versie hoort bij de **export**, want dat is wat Public aanhaalt: daar staat
`hoofdplaat v1.7` in de tekst en `informatiestromen_hoofdplaat_v1_7.png` in de
bestandsnamen, en nergens een viewnaam. Zonder vastlegging is die versie daarmee
een etiket zonder verwijzing: niemand kan nalopen uit welke modelstaat de plaat komt,
en een plaat die achterloopt op het model is niet van een actuele te onderscheiden.

Dit script berekent een hash over de **inhoud van de view zelf**, niet over het hele
modelbestand. Dat is met opzet: een wijziging in een MOKA-view of in het
informatiemodel raakt de hoofdplaat niet, en zou met een hash over het hele bestand
wel een nieuwe export afdwingen. De hash dekt de elementen, de relaties en de
geometrie van de view, dus precies wat de plaat laat zien.

    python3 tools/scripts/plaatherkomst.py             # tonen en vergelijken
    python3 tools/scripts/plaatherkomst.py --schrijf    # het manifest bijwerken

De controle hangt in `tools/tests/test_plaatherkomst.py` en loopt dus mee in CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
MANIFEST = WORTEL / "architecture/model/informatiestromen hoofdplaat OKx/herkomst.json"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"


def view_element(wortel, naam):
    """De view met deze naam, of None."""
    for el in wortel.iter("element"):
        if el.get(XSI) == "archimate:ArchimateDiagramModel" and el.get("name") == naam:
            return el
    return None


def viewhash(pad, naam):
    """sha256 over de inhoud van een view: elementen, relaties en geometrie.

    Niet over het hele modelbestand, zodat een wijziging elders geen export afdwingt.
    De uitvoer is genormaliseerd en gesorteerd, zodat de volgorde waarin Archi
    schrijft de hash niet verandert.
    """
    el = view_element(ET.parse(pad).getroot(), naam)
    if el is None:
        return None
    regels = []
    for kind in el.iter():
        if kind is el:
            continue
        ae = kind.get("archimateElement")
        ar = kind.get("archimateRelationship")
        if not (ae or ar):
            continue
        b = kind.find("bounds")
        vak = (f"{b.get('x')},{b.get('y')},{b.get('width')},{b.get('height')}"
               if b is not None else "")
        knik = ";".join(f"{p.get('startX')},{p.get('startY')},{p.get('endX')},{p.get('endY')}"
                        for p in kind.findall("bendpoint"))
        regels.append("|".join([ae or "", ar or "", vak, knik,
                                kind.get("fillColor") or "", kind.get("name") or ""]))
    tekst = "\n".join(sorted(regels))
    return "sha256:" + hashlib.sha256(tekst.encode("utf-8")).hexdigest()


def lees_manifest():
    if not MANIFEST.exists():
        return None
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--schrijf", action="store_true",
                   help="het manifest bijwerken met de huidige hash")
    p.add_argument("--versie", help="de versie van deze export, bijvoorbeeld 1.7.1")
    p.add_argument("--model", default=str(MODEL))
    args = p.parse_args(argv)

    manifest = lees_manifest() or {"view": "OKx hoofdplaat", "versie": None, "export": None}
    naam = manifest.get("view", "OKx hoofdplaat")
    nu = viewhash(args.model, naam)

    if nu is None:
        print(f"view niet gevonden: {naam}")
        return 1

    if args.schrijf:
        if args.versie:
            manifest["versie"] = args.versie
        if not manifest.get("versie"):
            print("geef bij de eerste keer een versie mee: --versie 1.7.1")
            return 1
        v = manifest["versie"]
        manifest["viewhash"] = nu
        manifest["export"] = f"{v}/OKx hoofdplaat {v}.jpg"
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
        print(f"manifest bijgewerkt: versie {v}, {nu[:22]}...")
        return 0

    print(f"view        {naam}")
    print(f"versie      {manifest.get('versie') or '(nog niet vastgelegd)'}")
    print(f"nu          {nu}")
    print(f"vastgelegd  {manifest.get('viewhash') or '(nog niet vastgelegd)'}")
    if manifest.get("viewhash") != nu:
        print("\nDe view wijkt af van wat er is geexporteerd. Exporteer de plaat opnieuw en draai:")
        print("  python3 tools/scripts/plaatherkomst.py --schrijf")
        return 1
    print("\ngelijk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
