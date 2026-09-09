#!/usr/bin/env python3
"""Controleert begrippen.json en genereert de leesbare begrippenlijst eruit.

De controles zijn de kern: een definitie zonder werkende vindplaats komt er niet
door, een objecttype van het informatiemodel kan niet stilletjes ontbreken, en
een negeerregel die nergens op slaat wordt opgeruimd.

Gebruik:
    python3 scripts/genereer-begrippenlijst.py [--controleer]
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
MAP = WORTEL / "architecture/docs/specificatie/begrippen"
BEGRIPPEN = MAP / "begrippen.json"
EXTRACTIE = MAP / "begrippen-extractie.json"
INFORMATIEMODEL = WORTEL / "architecture/model/informatiemodel/informatiemodel.json"
DOEL = MAP / "begrippenlijst.md"

KOP = """# Begrippenlijst OKx

## Context

De koppelvlakken van OKx wisselen informatie uit tussen instellingen en tussen systemen. Dat werkt alleen als een term aan beide kanten hetzelfde betekent.

## Inleiding

Deze lijst geeft per begrip de vastgestelde schrijfwijze, een definitie en de vindplaats van die definitie. Een begrip zonder vindplaats staat er als gat in, niet als dichtgeschreven aanname.

## Doel

Vaststellen wat OKx onder een term verstaat, zodat een lezer van een specificatie niet hoeft te raden. De lijst is de toetssteen voor naamgeving in het informatiemodel, de koppelvlakspecificaties en de reviews.

## Scope

"""

VOET = """
## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md) | De objecttypen en hun samenhang; deze lijst geeft er de definities bij |
| [Begrippenkader leerroute-uitwerking](../leerroute-uitwerking/doc/begrippenkader.md) | De families, de niveaus en de stadia |
| [`begrippen.json`](begrippen.json) | Deze lijst machineleesbaar; dit document wordt eruit gegenereerd |
| [`begrippen-extractie.json`](begrippen-extractie.json) | Elke term tussen backquotes in meta en Public, met vindplaatsen |
"""


def anker(kop):
    s = kop.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", "-", s).strip("-")


def ankers_van(pad):
    if not pad.is_file():
        return None
    return {anker(r.lstrip("#").strip()) for r in pad.read_text(encoding="utf-8").splitlines()
            if r.startswith("#")}


def controleer(data, extractie, im):
    fouten = []
    namen = [b["naam"] for b in data["begrippen"]]
    for n in {x for x in namen if namen.count(x) > 1}:
        fouten.append(f"begrip staat meer dan een keer in de lijst: {n}")

    for b in data["begrippen"]:
        if b["status"] == "gedefinieerd":
            if not b.get("definitie"):
                fouten.append(f"status gedefinieerd zonder definitie: {b['naam']}")
            vp = b.get("vindplaats")
            if not vp:
                fouten.append(f"status gedefinieerd zonder vindplaats: {b['naam']}")
                continue
            bestand, _, kop = vp.partition("#")
            pad = WORTEL / bestand
            aanwezig = ankers_van(pad)
            if aanwezig is None:
                fouten.append(f"vindplaats verwijst naar een bestand dat niet bestaat: {b['naam']} -> {bestand}")
            elif kop and kop not in aanwezig:
                fouten.append(f"vindplaats verwijst naar een kop die niet bestaat: {b['naam']} -> {vp}")
        elif b["status"] == "nog te definieren":
            if b.get("definitie"):
                fouten.append(f"definitie bij status nog te definieren: {b['naam']}")
            t = b.get("toelichting")
            if t and not t.get("vindplaats"):
                fouten.append(f"toelichting zonder vindplaats: {b['naam']}")
            v = b.get("verwijzing_mora")
            if v and v.get("status") != "nog niet geopend" and not v.get("citaat"):
                fouten.append(f"verwijzing naar MORA zonder citaat terwijl de bron geopend heet: {b['naam']}")
        else:
            fouten.append(f"onbekende status: {b['naam']} -> {b['status']}")

    # Volledigheid binnen de scope van deze versie: het informatiemodel.
    in_lijst = {b["naam"] for b in data["begrippen"]}
    kolommen = {o["kolom"] for o in im["objecttypen"] if o.get("kolom")}
    for o in im["objecttypen"]:
        if o["naam"] not in in_lijst:
            fouten.append(f"objecttype van het informatiemodel ontbreekt in de lijst: {o['naam']}")
    for k in kolommen:
        if k not in in_lijst and not any(k in b.get("varianten", []) for b in data["begrippen"]):
            fouten.append(f"kolom van het informatiemodel ontbreekt in de lijst: {k}")

    # Een negeerregel die nergens op slaat is dode ballast.
    alle_termen = {s["schrijfwijze"] for t in extractie["termen"] for s in t["schrijfwijzen"]}
    for n in data["negeerlijst"]:
        if n["term"] not in alle_termen:
            fouten.append(f"negeerlijst noemt een term die in geen enkel bestand voorkomt: {n['term']}")
        if n["reden"] not in data["indeling_negeerlijst"]:
            fouten.append(f"negeerlijst gebruikt een onbekende reden: {n['term']} -> {n['reden']}")
    return fouten


def backlog(data, extractie):
    """Kandidaat-begrippen uit het corpus die noch in de lijst noch op de negeerlijst staan."""
    gedekt = set()
    for b in data["begrippen"]:
        gedekt.add(b["naam"].lower())
        gedekt.update(v.lower() for v in b.get("varianten", []))
    gedekt.update(n["term"].lower() for n in data["negeerlijst"])
    open_termen = []
    for t in extractie["termen"]:
        if t["indeling"] != "kandidaat-begrip":
            continue
        if any(s["schrijfwijze"].lower() in gedekt for s in t["schrijfwijzen"]):
            continue
        open_termen.append(t)
    return sorted(open_termen, key=lambda t: -t["aantal"])


def schrijf(data, extractie, open_termen):
    r = [KOP.rstrip("\n"), "", data["scope"], ""]
    begrippen = data["begrippen"]
    gedef = [b for b in begrippen if b["status"] == "gedefinieerd"]
    open_b = [b for b in begrippen if b["status"] == "nog te definieren"]

    r += ["## Stand van zaken", "",
          "| | |", "|---|---|",
          f"| Begrippen in deze versie | {len(begrippen)} |",
          f"| Met definitie en vindplaats | {len(gedef)} |",
          f"| Nog te definieren | {len(open_b)} |",
          f"| Waarvan met alleen een doelomschrijving | {sum(1 for b in open_b if b.get('toelichting'))} |",
          f"| Kandidaat-begrippen uit meta en Public buiten deze versie | {len(open_termen)} |",
          ""]

    r += ["## Begrippen", "",
          "De begrippen delen de keten in. Ze zijn niveau 1 in het "
          "[Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/); "
          "de objecttypen eronder zijn niveau 2.", "",
          "| Begrip | Definitie | Vindplaats |", "|---|---|---|"]
    for b in [x for x in begrippen if x["niveau"] == 1]:
        d = b["definitie"] or "*nog te definieren*"
        v = f"[{b['vindplaats'].split('#')[0].split('/')[-1]}]({pad_naar(b['vindplaats'])})" if b.get("vindplaats") else ""
        r.append(f"| `{b['naam']}` | {d} | {v} |")
    r.append("")

    r += ["## Objecttypen met een definitie", "",
          "| Objecttype | Begrip | Definitie | Vindplaats |", "|---|---|---|---|"]
    for b in sorted([x for x in gedef if x["niveau"] == 2], key=lambda x: (x["familie"] or "", x["naam"])):
        v = f"[{b['vindplaats'].split('#')[0].split('/')[-1]}]({pad_naar(b['vindplaats'])})"
        r.append(f"| `{b['naam']}` | {b['familie'] or ''} | {b['definitie']} | {v} |")
    r.append("")

    met_doel = [x for x in open_b if x["niveau"] == 2 and x.get("toelichting")]
    if met_doel:
        r += ["## Objecttypen met alleen een doelomschrijving", "",
              "Hier staat wel wat het objecttype doet, maar niet wat het is. Een doelomschrijving is geen "
              "definitie; deze rijen wachten nog op een.", "",
              "| Objecttype | Begrip | Doelomschrijving | Vindplaats |", "|---|---|---|---|"]
        for b in sorted(met_doel, key=lambda x: (x["familie"] or "", x["naam"])):
            t = b["toelichting"]
            v = f"[{t['vindplaats'].split('#')[0].split('/')[-1]}]({pad_naar(t['vindplaats'])})"
            r.append(f"| `{b['naam']}` | {b['familie'] or ''} | {t['tekst']} | {v} |")
        r.append("")

    zonder = [x for x in open_b if x["niveau"] == 2 and not x.get("toelichting")]
    r += ["## Objecttypen zonder bron", "",
          "Deze objecttypen staan op de plaat maar zijn nergens beschreven. Elk is een gat, geen aanname.", ""]
    per_familie = defaultdict(list)
    for b in zonder:
        per_familie[b["familie"] or "Buiten de kolommen"].append(b["naam"])
    r += ["| Begrip | Objecttypen |", "|---|---|"]
    for familie in sorted(per_familie):
        r.append(f"| {familie} | " + ", ".join(f"`{n}`" for n in sorted(per_familie[familie])) + " |")
    r.append("")

    verwijzingen = [b for b in begrippen if b.get("verwijzing_mora")]
    if verwijzingen:
        r += ["## Verwijzingen naar MORA", "",
              "Deze verwijzingen staan in de bron waaruit deze lijst is opgebouwd. Ze zijn nog niet "
              "geopend en dus nog geen bewijs van herkomst.", "",
              "| Objecttype | Verwijzing | Stand |", "|---|---|---|"]
        for b in sorted(verwijzingen, key=lambda x: x["naam"]):
            v = b["verwijzing_mora"]
            r.append(f"| `{b['naam']}` | [{v['bron']}]({v['url']}) | {v['status']} |")
        r.append("")

    r += ["## Negeerlijst", "",
          "Termen die tussen backquotes voorkomen maar geen begrip zijn.", "",
          "| Term | Reden |", "|---|---|"]
    for n in sorted(data["negeerlijst"], key=lambda n: (n["reden"], n["term"])):
        r.append(f"| `{n['term']}` | {n['reden']} |")

    r.append(VOET)
    DOEL.write_text("\n".join(r).rstrip("\n") + "\n", encoding="utf-8")


def pad_naar(vindplaats):
    bestand, _, kop = vindplaats.partition("#")
    rel = Path(bestand)
    hier = MAP.relative_to(WORTEL)
    omhoog = "../" * len(hier.parts)
    return omhoog + str(rel) + (f"#{kop}" if kop else "")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--controleer", action="store_true",
                   help="alleen controleren, niets schrijven")
    args = p.parse_args()

    data = json.loads(BEGRIPPEN.read_text(encoding="utf-8"))
    extractie = json.loads(EXTRACTIE.read_text(encoding="utf-8"))
    im = json.loads(INFORMATIEMODEL.read_text(encoding="utf-8"))

    fouten = controleer(data, extractie, im)
    open_termen = backlog(data, extractie)

    if fouten:
        print(f"{len(fouten)} problemen:", file=sys.stderr)
        for f in fouten:
            print(f"  {f}", file=sys.stderr)
        sys.exit(1)

    gedef = sum(1 for b in data["begrippen"] if b["status"] == "gedefinieerd")
    print(f"controle geslaagd: {len(data['begrippen'])} begrippen, {gedef} met definitie en vindplaats")
    print(f"backlog buiten deze versie: {len(open_termen)} kandidaat-begrippen")
    if not args.controleer:
        schrijf(data, extractie, open_termen)
        print(f"geschreven naar {DOEL}")


if __name__ == "__main__":
    main()
