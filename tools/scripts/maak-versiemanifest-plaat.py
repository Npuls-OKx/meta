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
    python3 tools/scripts/maak-versiemanifest-plaat.py                      # controleren
    python3 tools/scripts/maak-versiemanifest-plaat.py --schrijf --versie 1.7.1
    python3 tools/scripts/maak-versiemanifest-plaat.py --retrofit           # de historie aanvullen

De controle hangt in `tools/tests/test_maak-versiemanifest-plaat.py` en loopt dus mee in CI.
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
MANIFEST = PLATEN / "versiemanifest.json"
MODELPAD = "architecture/model/model.archimate"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"

# De viewnaam zoals die toen heette, per uitgebrachte versie. De namen dragen sinds
# november 2026 geen versie meer; voor de historie is de oude naam de enige ingang.
# Per uitgebrachte versie de viewnaam zoals die toen heette. De viewnamen dragen sinds
# november 2026 geen versie meer; voor de historie is de oude naam de enige ingang. De
# commit is de LAATSTE waarin die view nog bestond, want een view die later hernoemd is
# bestaat op de commit van de afbeelding niet meer onder die naam.
HISTORIE = {
    "1.3": ("OKx hoofdplaat v1.3", "665c7a00a79f57eefcbca333a71e4e4f72987ce6"),
    "1.4": ("OKx hoofdplaat v1.4 <concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
    "1.6.1": ("OKx hoofdplaat v1.6a<concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
    "1.6.2": ("OKx hoofdplaat v1.6b<concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
    "1.7": ("OKx hoofdplaat v1.7<concept>", "a65979b48ae32c730f60cc909aa43c8b00d045ba"),
}

# Versie 1.1 en 1.2 hebben nooit een view in het model gehad. De eerste hoofdplaatview is
# `OKx hoofdplaat v1.3` en verscheen op 1 april 2026; het model zelf kwam op 18 maart in
# de repository. Hun afbeelding is er wel, en die geldt als release.
ZONDER_MODELSTAAT = ("1.1", "1.2")

# Hoe de afbeelding gemaakt is. Tot en met 1.7 handmatig, uit de lokale Archi van de
# modelleur; daarom is een uitgebrachte plaat niet uit haar modelstaat te herbouwen.
# Gemeten op 17 november 2026: hoofdplaat 1.7 is 2267 bij 861, en een export uit precies
# die modelstaat geeft 2276 bij 1113 voor de volle view en 2241 bij 873 voor de view
# zonder contextapplicaties. Vanaf 1.7.1 komt de export uit het gecommitte model.
HANDMATIG_TOT_EN_MET = "1.7"


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
    """Het geexporteerde beeld in de versiemap, relatief aan de platenmap.

    Een map draagt precies een beeld, want een map is een versie. Toen `1.6a` en `1.6b`
    samen in de map `1.6` stonden, koos dit de eerste op alfabet en bleef `1.6b` stil
    buiten het manifest: een uitgebrachte plaat die nergens stond. Daarom faalt dit nu
    in plaats van te kiezen.
    """
    map_ = PLATEN / versie
    if not map_.is_dir():
        return None
    beelden = [p for p in sorted(map_.iterdir())
               if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".svg"}]
    if len(beelden) > 1:
        raise SystemExit(f"map {versie} draagt {len(beelden)} beelden: "
                         + ", ".join(p.name for p in beelden)
                         + "\neen map is een versie, dus geef elke plaat haar eigen map")
    return f"{versie}/{beelden[0].name}" if beelden else None


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


def _beeld_bron(versie):
    """Hoe de afbeelding van deze versie gemaakt is, en of zij te herbouwen valt."""
    if versie <= HANDMATIG_TOT_EN_MET:
        return ("handmatige export uit de lokale Archi van de modelleur", False)
    return ("exporteer-archimate-platen.py uit het gecommitte model", True)


def retrofit(m):
    """Vult de historie aan voor versies die al uitgebracht zijn.

    Een uitgebrachte plaat blijft staan zoals zij is uitgebracht. Dit vult alleen de
    verwijzing naar de modelstaat erachter, zodat navolgbaar is waar de bron zit.
    """
    # Een versie waarvan de map verdwenen is, hoort niet in het manifest te blijven staan.
    # Dat gebeurde toen `1.6` werd gesplitst in `1.6.1` en `1.6.2`: de oude regel bleef
    # en wees naar een beeld dat er niet meer was.
    mappen = sorted(p.name for p in PLATEN.iterdir() if p.is_dir())
    m["versies"] = [v for v in m["versies"] if v["versie"] in mappen]
    for versie in mappen:
        v = item(m, versie)
        if v.get("model_herkomst") == "vastgelegd bij export":
            continue
        pad = export_van(versie)
        v["export"] = pad
        v["beeld_bron"], v["reproduceerbaar"] = _beeld_bron(versie)
        v["beeld_commit"] = volledige_commit(f"{PLATEN.relative_to(WORTEL)}/{pad}") if pad else None
        if versie in ZONDER_MODELSTAAT:
            v["view"], v["model_commit"], v["viewhash"] = None, None, None
            v["model_herkomst"] = ("geen: deze versie heeft nooit een view in het model gehad, "
                                   "de eerste hoofdplaatview verscheen op 1 april 2026")
            continue
        naam, commit = HISTORIE.get(versie, (None, None))
        h = viewhash_op_commit(commit, naam) if (naam and commit) else None
        v["view"], v["model_commit"], v["viewhash"] = naam, commit, h
        v["model_herkomst"] = ("nagemeten: de view bestond onder deze naam op deze commit"
                               if h else "geen: viewnaam of commit onbekend")
    ORDE = ["versie", "export", "beeld_bron", "beeld_commit", "reproduceerbaar",
            "view", "model_commit", "viewhash", "model_herkomst"]
    for i, v in enumerate(m["versies"]):
        m["versies"][i] = {k: v[k] for k in ORDE if k in v}
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
            print(f"  {v['versie']:7s} {v.get('model_herkomst','')[:58]}")
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
        bron, reproduceerbaar = _beeld_bron(versie)
        v.update({"export": pad, "beeld_bron": bron, "reproduceerbaar": reproduceerbaar,
                  "beeld_commit": volledige_commit(f"{PLATEN.relative_to(WORTEL)}/{pad}"),
                  "view": naam, "viewhash": nu,
                  "model_commit": volledige_commit(MODELPAD),
                  "model_herkomst": "vastgelegd bij export"})
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
        print("  python3 tools/scripts/maak-versiemanifest-plaat.py --schrijf --versie <versie>")
        return 1
    print("\ngelijk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
