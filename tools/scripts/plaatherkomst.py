#!/usr/bin/env python3
"""Legt vast uit welke modelstaat een geexporteerde plaat komt.

Waarom dit script bestaat: de viewnamen in het ArchiMate-model dragen geen versie
meer. De versie hoort bij de **export**, want dat is wat Public aanhaalt: daar staat
`hoofdplaat v1.7` in de tekst en `informatiestromen_hoofdplaat_v1_7.png` in de
bestandsnamen, en nergens een viewnaam. Zonder vastlegging is die versie daarmee
een etiket zonder verwijzing: niemand kan nalopen uit welke modelstaat de plaat komt,
en een plaat die achterloopt op het model is niet van een actuele te onderscheiden.

Twee dingen leggen we per versie vast:

  viewhash   sha256 over de **inhoud van de view**, niet over het hele modelbestand.
             Dat is met opzet: een wijziging in een MOKA-view of in het informatiemodel
             raakt de hoofdplaat niet, en zou met een bestandshash wel een nieuwe
             export afdwingen. De hash dekt de elementen, de relaties, de geometrie
             en de vulkleuren, dus precies wat de plaat laat zien.
  commit     de **volledige** veertigtekenhash. Een afkorting is een prefix waarvan
             de uniciteit alleen geldt op het moment van schrijven; git schaalt zijn
             afkortlengte mee met het aantal objecten in de repository (hier al acht
             tekens in plaats van zeven). Een verwijzing die jaren mee moet, slaat
             daarom de volle hash op.

Daarnaast zegt elk item met `herkomst` hoe hard de verwijzing is:

  vastgelegd bij export   op het moment van exporteren geschreven; dit is het echte werk
  nagemeten               achteraf gereconstrueerd uit de modelstaat van die commit
  onbekend                geen modelstaat te vinden; alleen de afbeelding bestaat

Gebruik:
    python3 tools/scripts/plaatherkomst.py                      # controleren
    python3 tools/scripts/plaatherkomst.py --schrijf --versie 1.7.1
    python3 tools/scripts/plaatherkomst.py --retrofit           # de historie aanvullen

De controle hangt in `tools/tests/test_plaatherkomst.py` en loopt dus mee in CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
PLATEN = WORTEL / "architecture/model/informatiestromen hoofdplaat OKx"
MANIFEST = PLATEN / "herkomst.json"
MODELPAD = "architecture/model/model.archimate"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"

# De viewnaam zoals die toen heette, per uitgebrachte versie. De namen dragen sinds
# november 2026 geen versie meer; voor de historie is de oude naam de enige ingang.
HISTORIE = {
    "1.4": "OKx hoofdplaat v1.4 <concept>",
    "1.6": "OKx hoofdplaat v1.6a<concept>",
    "1.7": "OKx hoofdplaat v1.7<concept>",
}


def view_element(wortel, naam):
    for el in wortel.iter("element"):
        if el.get(XSI) == "archimate:ArchimateDiagramModel" and el.get("name") == naam:
            return el
    return None


def _hash_van_view(el):
    regels = []
    for kind in el.iter():
        if kind is el:
            continue
        ae, ar = kind.get("archimateElement"), kind.get("archimateRelationship")
        b = kind.find("bounds")
        knikpunten = kind.findall("bendpoint")
        # Alles wat op de plaat staat telt mee, niet alleen de ArchiMate-elementen:
        # een groep, een notitie of een los label is net zo zichtbaar, en een
        # verschoven groep verandert de plaat net zo goed.
        if not (ae or ar or b is not None or knikpunten):
            continue
        vak = (f"{b.get('x')},{b.get('y')},{b.get('width')},{b.get('height')}"
               if b is not None else "")
        knik = ";".join(f"{q.get('startX')},{q.get('startY')},{q.get('endX')},{q.get('endY')}"
                        for q in knikpunten)
        regels.append("|".join([kind.get("id") or "", ae or "", ar or "", vak, knik,
                                kind.get("fillColor") or "", kind.get("font") or "",
                                kind.get("name") or "", (kind.get("content") or "").strip()]))
    return "sha256:" + hashlib.sha256("\n".join(sorted(regels)).encode("utf-8")).hexdigest()


def viewhash(pad, naam):
    """sha256 over de inhoud van een view in een modelbestand, of None."""
    el = view_element(ET.parse(pad).getroot(), naam)
    return _hash_van_view(el) if el is not None else None


def viewhash_op_commit(commit, naam):
    """Dezelfde hash, maar over het model zoals het op die commit stond."""
    uit = subprocess.run(["git", "show", f"{commit}:{MODELPAD}"],
                         cwd=WORTEL, capture_output=True, text=True)
    if uit.returncode != 0:
        return None
    el = view_element(ET.fromstring(uit.stdout), naam)
    return _hash_van_view(el) if el is not None else None


def volledige_commit(pad):
    """De volledige veertigtekenhash van de commit die dit bestand toevoegde."""
    uit = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "-1", "--", pad],
                         cwd=WORTEL, capture_output=True, text=True)
    h = uit.stdout.strip()
    return h if len(h) == 40 else None


def export_van(versie):
    """Het geexporteerde beeld in de versiemap, relatief aan de platenmap."""
    map_ = PLATEN / versie
    if not map_.is_dir():
        return None
    for p in sorted(map_.iterdir()):
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".svg"}:
            return f"{versie}/{p.name}"
    return None


def lees():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"view": "OKx hoofdplaat", "huidig": None, "versies": []}


def schrijf(m):
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def item(m, versie):
    for v in m["versies"]:
        if v["versie"] == versie:
            return v
    nieuw = {"versie": versie}
    m["versies"].append(nieuw)
    return nieuw


def retrofit(m):
    """Vult de historie aan voor versies die al uitgebracht zijn."""
    gevonden = sorted(p.name for p in PLATEN.iterdir() if p.is_dir())
    for versie in gevonden:
        v = item(m, versie)
        if v.get("herkomst") == "vastgelegd bij export":
            continue
        pad = export_van(versie)
        v["export"] = pad
        v["commit"] = volledige_commit(f"{PLATEN.relative_to(WORTEL)}/{pad}") if pad else None
        naam = HISTORIE.get(versie)
        h = viewhash_op_commit(v["commit"], naam) if (naam and v["commit"]) else None
        v["view"] = naam
        v["viewhash"] = h
        v["herkomst"] = ("nagemeten" if h else
                         "onbekend, geen view met deze naam in het model van die commit")
    m["versies"].sort(key=lambda v: [int(x) for x in v["versie"].split(".")])
    return m


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--schrijf", action="store_true", help="de huidige versie vastleggen")
    p.add_argument("--versie", help="de versie van deze export, bijvoorbeeld 1.7.1")
    p.add_argument("--retrofit", action="store_true", help="de historie aanvullen")
    p.add_argument("--model", default=str(MODEL))
    args = p.parse_args(argv)

    m = lees()
    naam = m.get("view", "OKx hoofdplaat")

    if args.retrofit:
        schrijf(retrofit(m))
        print(f"historie aangevuld: {len(m['versies'])} versies in {MANIFEST.name}")
        for v in m["versies"]:
            print(f"  {v['versie']:7s} {v.get('herkomst','')}")
        return 0

    nu = viewhash(args.model, naam)
    if nu is None:
        print(f"view niet gevonden: {naam}")
        return 1

    if args.schrijf:
        versie = args.versie or m.get("huidig")
        if not versie:
            print("geef de versie mee: --versie 1.7.1")
            return 1
        pad = export_van(versie)
        if pad is None:
            print(f"geen export gevonden in {PLATEN.name}/{versie}; exporteer de plaat eerst")
            return 1
        v = item(m, versie)
        v.update({"view": naam, "viewhash": nu, "export": pad,
                  "commit": volledige_commit(f"{PLATEN.relative_to(WORTEL)}/{pad}"),
                  "herkomst": "vastgelegd bij export"})
        m["huidig"] = versie
        schrijf(m)
        print(f"vastgelegd: versie {versie}, {nu[:22]}...")
        return 0

    huidig = m.get("huidig")
    v = item(m, huidig) if huidig else None
    print(f"view        {naam}")
    print(f"huidig      {huidig or '(nog niet vastgelegd)'}")
    print(f"nu          {nu}")
    print(f"vastgelegd  {(v or {}).get('viewhash') or '(nog niet vastgelegd)'}")
    if not v or v.get("viewhash") != nu:
        print("\nDe view wijkt af van wat er is geexporteerd. Exporteer de plaat opnieuw en draai:")
        print("  python3 tools/scripts/plaatherkomst.py --schrijf --versie <versie>")
        return 1
    print("\ngelijk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
