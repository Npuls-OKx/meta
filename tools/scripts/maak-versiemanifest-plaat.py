#!/usr/bin/env python3
"""Legt per uitgebrachte plaat vast uit welke modelstaat zij komt.

Waarom dit script bestaat: de viewnamen in het ArchiMate-model dragen geen versie meer.
De versie hoort bij de **export**, want dat is wat [Npuls-OKx/Public] aanhaalt: daar staat
`hoofdplaat v1.7` in de tekst en `informatiestromen_hoofdplaat_v1_7.png` in bestandsnamen,
en nergens een viewnaam. Zo neemt een versieophoging ook geen scriptwijziging mee. Zonder
vastlegging is die versie daarmee een etiket zonder verwijzing: niemand kan nalopen uit
welke modelstaat de plaat komt, en een plaat die achterloopt op het model is niet van een
actuele te onderscheiden.

Per versie leggen we vast:

  viewhash   sha256 over de **inhoud van de view**, niet over het hele modelbestand. Een
             wijziging in een MOKA-view raakt de hoofdplaat niet en zou met een
             bestandshash wel een export afdwingen. De hash dekt de elementen, de
             relaties, de geometrie, de vulkleuren en de labels; dus precies wat de plaat
             laat zien.
  commit     de **volledige** veertigtekenhash. Een afkorting is een prefix waarvan de
             uniciteit alleen geldt op het moment van schrijven; git schaalt zijn
             afkortlengte mee met het aantal objecten in de repository.
  beeld_bron hoe de afbeelding gemaakt is, en of zij uit haar modelstaat te herbouwen is.

Gebruik:
    python3 tools/scripts/maak-versiemanifest-plaat.py                       # controleren
    python3 tools/scripts/maak-versiemanifest-plaat.py --plaat hoofdplaat --schrijf --versie 1.7.2
    python3 tools/scripts/maak-versiemanifest-plaat.py --retrofit            # historie aanvullen

De controle hangt in `tools/tests/test_maak_versiemanifest_plaat.py` en loopt mee in CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
# In bron/ en niet in gegenereerd/: de regels die met --schrijf zijn vastgelegd dragen
# de viewhash van het moment van exporteren, en die is niet opnieuw te berekenen zodra
# het model verder is. Dit bestand is dus data die bewaard moet blijven.
MANIFEST = WORTEL / "architecture/model/bron/versiemanifest.json"
MODELPAD = "architecture/model/model.archimate"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

# De platen die wij uitbrengen. Twee vormen, omdat zij historisch verschillen:
#   map-per-versie     elke versie is een map met een beeld; zo staat de hoofdplaat
#   bestand-per-versie elke versie is een bestand met de versie in de naam
PLATEN = {
    "hoofdplaat": {
        "view": "OKx hoofdplaat",
        "map": "architecture/model/informatiestromen hoofdplaat OKx",
        "vorm": "map-per-versie",
        "handmatig_tot_en_met": "1.7.0",
        # Per versie de viewnaam zoals die toen heette en de LAATSTE commit waarin die
        # view nog bestond. De namen dragen sinds november 2026 geen versie meer; voor de
        # historie is de oude naam de enige ingang.
        "historie": {
            "1.3.0": ("OKx hoofdplaat v1.3", "665c7a00a79f57eefcbca333a71e4e4f72987ce6"),
            "1.4.0": ("OKx hoofdplaat v1.4 <concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
            "1.6.1": ("OKx hoofdplaat v1.6a<concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
            "1.6.2": ("OKx hoofdplaat v1.6b<concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
            "1.7.0": ("OKx hoofdplaat v1.7<concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
        },
        # Versie 1.1.0 en 1.2.0 hebben nooit een view gehad: de eerste hoofdplaatview is
        # `OKx hoofdplaat v1.3` en verscheen op 1 april 2026, en het model zelf kwam op
        # 18 maart in de repository. Hun afbeelding geldt wel als release.
        "zonder_modelstaat": ("1.1.0", "1.2.0"),
    },
    "informatiemodel": {
        "view": "OKx informatiemodel",
        "map": "architecture/model/informatiemodel",
        "vorm": "bestand-per-versie",
        "patroon": "OKx informatiemodel v{versie}.jpg",
        "handmatig_tot_en_met": "0.2.0",
        "historie": {},
        "zonder_modelstaat": ("0.1.0", "0.2.0"),
    },
    "informatiemodel-oeapi": {
        "view": "OKx informatiemodel en mapping OEAPI",
        "map": "architecture/model/informatiemodel",
        "vorm": "bestand-per-versie",
        "patroon": "OKx informatiemodel en mapping OEAPI v{versie}.jpg",
        "handmatig_tot_en_met": "0.2.0",
        "historie": {},
        "zonder_modelstaat": ("0.1.0", "0.2.0"),
    },
}
BEELD = {".jpg", ".jpeg", ".png", ".svg"}


def getal(v):
    return tuple(int(x) for x in v.split("."))


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
        # Alles wat op de plaat staat telt mee, niet alleen de ArchiMate-elementen: een
        # groep, een notitie of een los label is net zo zichtbaar.
        if not (ae or ar or b is not None or knikpunten):
            continue
        vak = (f"{b.get('x')},{b.get('y')},{b.get('width')},{b.get('height')}"
               if b is not None else "")
        knik = ";".join(f"{q.get('startX')},{q.get('startY')},{q.get('endX')},{q.get('endY')}"
                        for q in knikpunten)
        label = ""
        for f in kind.findall("feature"):
            if f.get("name") == "labelExpression":
                label = " ".join((f.get("value") or "").split())
        regels.append("|".join([kind.get("id") or "", ae or "", ar or "", vak, knik,
                                kind.get("fillColor") or "", kind.get("font") or "",
                                kind.get("name") or "", label,
                                (kind.get("content") or "").strip()]))
    return "sha256:" + hashlib.sha256("\n".join(sorted(regels)).encode("utf-8")).hexdigest()


def viewhash(pad, naam):
    """sha256 over de inhoud van een view in een modelbestand, of None."""
    el = view_element(ET.parse(pad).getroot(), naam)
    return _hash_van_view(el) if el is not None else None


def viewhash_op_commit(commit, naam):
    """Dezelfde hash, over het model zoals het op die commit stond."""
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


def model_commit_bij(beeld_commit):
    """De laatste commit die het model raakte, op of voor de commit van de export.

    Niet `volledige_commit(MODELPAD)`: die geeft de commit die het modelbestand ooit
    toevoegde, en zette elke versie op dezelfde commit uit maart 2026.
    """
    if not beeld_commit:
        return None
    uit = subprocess.run(["git", "log", "-1", "--format=%H", beeld_commit, "--", MODELPAD],
                         cwd=WORTEL, capture_output=True, text=True)
    h = uit.stdout.strip()
    return h if len(h) == 40 else None


def model_gecommit():
    """Waar als het model in de werkmap gelijk is aan HEAD."""
    return subprocess.run(["git", "diff", "--quiet", "HEAD", "--", MODELPAD], cwd=WORTEL).returncode == 0


def versies_op_schijf(plaat):
    """De uitgebrachte versies van deze plaat, met hun beeld relatief aan de wortel.

    Een versie draagt precies een beeld. Toen `1.6a` en `1.6b` samen in de map `1.6`
    stonden koos dit de eerste op alfabet, en bleef `1.6b` stil buiten het manifest.
    """
    map_ = WORTEL / plaat["map"]
    uit = {}
    if plaat["vorm"] == "map-per-versie":
        for d in sorted(p for p in map_.iterdir() if p.is_dir()):
            beelden = [b for b in sorted(d.iterdir()) if b.suffix.lower() in BEELD]
            if len(beelden) > 1:
                raise SystemExit(f"map {d.name} draagt {len(beelden)} beelden: "
                                 + ", ".join(b.name for b in beelden)
                                 + "\neen map is een versie, dus geef elke plaat haar eigen map")
            if beelden:
                uit[d.name] = str(beelden[0].relative_to(WORTEL))
        return uit
    patroon = plaat["patroon"]
    voor, na = patroon.split("{versie}")
    for b in sorted(map_.iterdir()):
        if b.name.startswith(voor) and b.name.endswith(na):
            uit[b.name[len(voor):len(b.name) - len(na)]] = str(b.relative_to(WORTEL))
    return uit


def lees():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"platen": {}}


def schrijf(m):
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def blok(m, naam):
    plaat = PLATEN[naam]
    b = m["platen"].setdefault(naam, {})
    b.update({"view": plaat["view"], "map": plaat["map"], "vorm": plaat["vorm"]})
    b.setdefault("huidig", None)
    b.setdefault("versies", [])
    return b


def item(b, versie):
    for v in b["versies"]:
        if v["versie"] == versie:
            return v
    nieuw = {"versie": versie}
    b["versies"].append(nieuw)
    return nieuw


ORDE = ["versie", "export", "beeld_bron", "beeld_commit", "reproduceerbaar",
        "view", "model_commit", "viewhash", "model_herkomst"]


def opschonen(b):
    for i, v in enumerate(b["versies"]):
        b["versies"][i] = {k: v[k] for k in ORDE if k in v}
    b["versies"].sort(key=lambda v: getal(v["versie"]))


def beeld_bron(plaat, versie):
    """Hoe de afbeelding gemaakt is, en of zij uit haar modelstaat te herbouwen is."""
    if getal(versie) <= getal(plaat["handmatig_tot_en_met"]):
        return ("handmatige export uit de lokale Archi van de modelleur", False)
    return ("exporteer-archimate-platen.py uit het gecommitte model", True)


def retrofit(m, naam):
    """Vult de historie aan. Een uitgebrachte plaat blijft zoals zij is uitgebracht."""
    plaat, b = PLATEN[naam], blok(m, naam)
    op_schijf = versies_op_schijf(plaat)
    # Een versie waarvan het beeld verdwenen is, hoort niet in het manifest te blijven.
    b["versies"] = [v for v in b["versies"] if v["versie"] in op_schijf]
    for versie, pad in sorted(op_schijf.items(), key=lambda kv: getal(kv[0])):
        v = item(b, versie)
        if v.get("model_herkomst") == "vastgelegd bij export":
            continue
        v["export"] = pad
        v["beeld_bron"], v["reproduceerbaar"] = beeld_bron(plaat, versie)
        v["beeld_commit"] = volledige_commit(pad)
        if versie in plaat["zonder_modelstaat"]:
            v["view"], v["model_commit"], v["viewhash"] = None, None, None
            v["model_herkomst"] = ("geen: deze versie is uitgebracht zonder dat de modelstaat "
                                   "erachter is vastgelegd")
            continue
        viewnaam, commit = plaat["historie"].get(versie, (None, None))
        h = viewhash_op_commit(commit, viewnaam) if (viewnaam and commit) else None
        v["view"], v["model_commit"], v["viewhash"] = viewnaam, commit, h
        v["model_herkomst"] = ("nagemeten: de view bestond onder deze naam op deze commit"
                               if h else "geen: viewnaam of commit onbekend")
    opschonen(b)
    return b


def vastleggen(m, naam, versie, model):
    plaat, b = PLATEN[naam], blok(m, naam)
    nu = viewhash(model, plaat["view"])
    if nu is None:
        raise SystemExit(f"view niet gevonden: {plaat['view']}")
    if not SEMVER.match(versie):
        raise SystemExit(f"versie {versie} is geen MAJOR.MINOR.PATCH")
    # Een gewijzigde plaat krijgt een nieuw nummer. Zonder deze regel kun je het beeld
    # van de huidige versie overschrijven en dezelfde versie opnieuw vastleggen; de hash
    # klopt dan weer en de controle zwijgt, terwijl een afnemer iets anders geleverd krijgt
    # onder hetzelfde nummer.
    huidig = b.get("huidig")
    if huidig:
        vorige = next((x for x in b["versies"] if x["versie"] == huidig), None)
        if vorige and vorige.get("viewhash") != nu and getal(versie) <= getal(huidig):
            raise SystemExit(f"de view wijkt af van versie {huidig}, dus {versie} is te laag; "
                             f"hoog het nummer op")
    op_schijf = versies_op_schijf(plaat)
    if versie not in op_schijf:
        raise SystemExit(f"geen beeld gevonden voor versie {versie} in {plaat['map']}; "
                         "exporteer de plaat eerst")
    if not model_gecommit():
        raise SystemExit("het model heeft wijzigingen die niet gecommit zijn; commit het model eerst")
    v = item(b, versie)
    bron, reproduceerbaar = beeld_bron(plaat, versie)
    beeld_commit = volledige_commit(op_schijf[versie])
    v.update({"export": op_schijf[versie], "beeld_bron": bron,
              "reproduceerbaar": reproduceerbaar,
              "beeld_commit": beeld_commit,
              "view": plaat["view"], "model_commit": model_commit_bij(beeld_commit),
              "viewhash": nu, "model_herkomst": "vastgelegd bij export"})
    b["huidig"] = versie
    opschonen(b)
    return nu


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--plaat", choices=sorted(PLATEN), help="welke plaat; standaard alle")
    p.add_argument("--schrijf", action="store_true", help="deze versie vastleggen")
    p.add_argument("--versie", help="de versie van deze export, bijvoorbeeld 1.7.2")
    p.add_argument("--retrofit", action="store_true", help="de historie aanvullen")
    p.add_argument("--model", default=str(MODEL))
    args = p.parse_args(argv)

    m = lees()
    m.setdefault("platen", {})
    namen = [args.plaat] if args.plaat else sorted(PLATEN)

    if args.retrofit:
        for naam in namen:
            b = retrofit(m, naam)
            print(f"{naam}: {len(b['versies'])} versies")
            for v in b["versies"]:
                print(f"  {v['versie']:7s} {v['model_herkomst'][:56]}")
        schrijf(m)
        return 0

    if args.schrijf:
        if not args.plaat or not args.versie:
            raise SystemExit("geef de plaat en de versie mee: --plaat <naam> --versie <v>")
        nu = vastleggen(m, args.plaat, args.versie, args.model)
        schrijf(m)
        print(f"vastgelegd: {args.plaat} {args.versie}, {nu[:22]}...")
        return 0

    fout = 0
    for naam in namen:
        plaat = PLATEN[naam]
        b = m["platen"].get(naam, {})
        nu = viewhash(args.model, plaat["view"])
        huidig = b.get("huidig")
        v = next((x for x in b.get("versies", []) if x["versie"] == huidig), None) if huidig else None
        gelijk = v is not None and v.get("viewhash") == nu
        print(f"{naam:22s} view {plaat['view']!r}")
        print(f"  huidig      {huidig or '(nog niet vastgelegd)'}")
        print(f"  {'gelijk' if gelijk else 'WIJKT AF van de vastgelegde versie'}")
        if not gelijk:
            fout = 1
            print(f"  exporteer de plaat opnieuw en draai:")
            print(f"    python3 tools/scripts/maak-versiemanifest-plaat.py "
                  f"--plaat {naam} --schrijf --versie <hoger dan {huidig or '0.0.0'}>")
    return fout


if __name__ == "__main__":
    sys.exit(main())
