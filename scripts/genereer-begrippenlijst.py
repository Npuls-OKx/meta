#!/usr/bin/env python3
"""Controleert begrippen.json en genereert de leesbare begrippenlijst eruit.

Controles: een definitie staat letterlijk in de sectie waar de vindplaats naar
wijst, elk objecttype van het informatiemodel staat in de lijst, elk begrip komt
ergens vandaan, en elke term uit het corpus staat in de lijst, op de negeerlijst
of in de werkvoorraad.

Gebruik:
    python3 scripts/genereer-begrippenlijst.py [--controleer]
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
DEELPAD = "architecture/docs/specificatie/begrippen"

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
| [`referentiekaders.json`](referentiekaders.json) | De letterlijk overgenomen definities uit MORA en KOI, met bron-URL en ophaaldatum |
"""


def anker(kop):
    s = re.sub(r"[^\w\s-]", "", kop.strip().lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", s).strip("-")


def sectie(pad, kopanker):
    """De regels onder een kop, tot de volgende kop van gelijk of hoger niveau.

    Geeft None als het bestand of de kop niet bestaat.
    """
    if not pad.is_file():
        return None
    regels = pad.read_text(encoding="utf-8").splitlines()
    if not kopanker:
        return regels
    start = niveau = None
    for i, r in enumerate(regels):
        if r.startswith("#"):
            n = len(r) - len(r.lstrip("#"))
            if start is None and anker(r.lstrip("#")) == kopanker:
                start, niveau = i + 1, n
            elif start is not None and n <= niveau:
                return regels[start:i]
    return None if start is None else regels[start:]


def namen_van(b):
    return [b.get("naam", "")] + list(b.get("varianten") or [])


UITKOMSTEN = ("tegenhanger", "geen tegenhanger gevonden", "nog niet onderzocht")


def controleer_kaders(b, naam, referentie):
    """Elk kader krijgt een van de drie uitkomsten; een tegenhanger draagt zijn bewijs."""
    fouten = []
    blok = b.get("kaders")
    if not isinstance(blok, dict):
        return [f"begrip zonder mapping naar de referentiekaders: {naam}"]
    for kader in referentie["kaders"]:
        k = blok.get(kader)
        if not k:
            fouten.append(f"kader {kader} ontbreekt in de mapping: {naam}")
            continue
        uitkomst = k.get("uitkomst")
        if uitkomst not in UITKOMSTEN:
            fouten.append(f"onbekende uitkomst bij {kader}: {naam} -> {uitkomst}")
        elif uitkomst == "geen tegenhanger gevonden" and not k.get("zoekterm"):
            fouten.append(f"geen tegenhanger gevonden zonder zoekterm bij {kader}: {naam}")
        elif uitkomst == "tegenhanger":
            gevonden = {x["naam"]: x for x in referentie["kaders"][kader]["begrippen"]}
            b2 = gevonden.get(k.get("begrip"))
            if b2 is None:
                fouten.append(f"tegenhanger bij {kader} staat niet in referentiekaders.json: "
                              f"{naam} -> {k.get('begrip')}")
            else:
                if k.get("citaat") != b2["definitie"]:
                    fouten.append(f"citaat bij {kader} wijkt af van de vastgelegde bron: {naam}")
                if k.get("url") != b2["url"]:
                    fouten.append(f"url bij {kader} wijkt af van de vastgelegde bron: {naam}")
    return fouten


def controleer(data, extractie, im, referentie, wortel=WORTEL):
    fouten = []
    namen = [b.get("naam") for b in data.get("begrippen", [])]
    for n in sorted({x for x in namen if namen.count(x) > 1}):
        fouten.append(f"begrip staat meer dan één keer in de lijst: {n}")

    corpus = {s["schrijfwijze"].lower()
              for t in extractie.get("termen", []) for s in t.get("schrijfwijzen", [])}
    in_model = {o["naam"] for o in im.get("objecttypen", [])}
    in_model |= {o["kolom"] for o in im.get("objecttypen", []) if o.get("kolom")}

    for b in data.get("begrippen", []):
        naam = b.get("naam")
        if not naam:
            fouten.append("begrip zonder naam in de lijst")
            continue
        fouten += controleer_kaders(b, naam, referentie)
        if b.get("niveau") not in (1, 2):
            fouten.append(f"begrip zonder geldig niveau (1 of 2): {naam}")
        if not any(n.lower() in corpus or n in in_model for n in namen_van(b)):
            fouten.append(f"begrip komt nergens voor, niet in de markdown en niet in het model: {naam}")

        status = b.get("status")
        if status == "gedefinieerd":
            if not b.get("definitie"):
                fouten.append(f"status gedefinieerd zonder definitie: {naam}")
            fouten += controleer_bron(b, naam, b.get("definitie"), b.get("vindplaats"), wortel)
        elif status == "nog te definieren":
            if b.get("definitie"):
                fouten.append(f"definitie bij status nog te definieren: {naam}")
            t = b.get("toelichting")
            if t:
                fouten += controleer_bron(b, naam, t.get("tekst"), t.get("vindplaats"), wortel,
                                          soort="toelichting")
            v = b.get("verwijzing_mora")
            if v and v.get("status") != "nog niet geopend" and not v.get("citaat"):
                fouten.append(f"verwijzing naar MORA zonder citaat terwijl de status zegt "
                              f"dat de bron geopend is: {naam}")
        else:
            fouten.append(f"onbekende status: {naam} -> {status}")

    for o in im.get("objecttypen", []):
        if o["naam"] not in namen:
            fouten.append(f"objecttype van het informatiemodel ontbreekt in de lijst: {o['naam']}")
    for k in sorted({o["kolom"] for o in im.get("objecttypen", []) if o.get("kolom")}):
        if k not in namen and not any(k in (b.get("varianten") or []) for b in data.get("begrippen", [])):
            fouten.append(f"kolom van het informatiemodel ontbreekt in de lijst: {k}")

    schrijfwijzen = {s["schrijfwijze"] for t in extractie.get("termen", [])
                     for s in t.get("schrijfwijzen", [])}
    for n in data.get("negeerlijst", []):
        term = n.get("term")
        if term is None:
            fouten.append("negeerlijstregel zonder term")
            continue
        if term not in schrijfwijzen:
            fouten.append(f"negeerlijst noemt een term die in geen enkel bestand voorkomt: {term}")
        if n.get("reden") not in data.get("indeling_negeerlijst", []):
            fouten.append(f"negeerlijst gebruikt een onbekende reden: {term} -> {n.get('reden')}")

    for t in nieuw_in_corpus(data, extractie):
        fouten.append(f"nieuwe term uit de markdown staat niet in de lijst, niet op de "
                      f"negeerlijst en niet in de werkvoorraad: {t}")
    return fouten


def controleer_bron(b, naam, tekst, vindplaats, wortel, soort="definitie"):
    """De tekst moet letterlijk staan in de sectie waar de vindplaats naar wijst,
    en de naam of een variant moet daar ook voorkomen."""
    if not vindplaats:
        return [f"status gedefinieerd zonder vindplaats: {naam}"] if soort == "definitie" \
            else [f"toelichting zonder vindplaats: {naam}"]
    if vindplaats.startswith("http"):
        # Een definitie uit een referentiekader; die wordt getoetst in controleer_kaders.
        return []
    bestand, _, kop = vindplaats.partition("#")
    pad = wortel / bestand
    if not pad.is_file():
        return [f"vindplaats verwijst naar een bestand dat niet bestaat: {naam} -> {bestand}"]
    regels = sectie(pad, kop)
    if regels is None:
        return [f"vindplaats verwijst naar een kop die niet bestaat: {naam} -> {vindplaats}"]
    blok = "\n".join(regels)
    fouten = []
    if tekst and tekst not in blok:
        fouten.append(f"{soort} staat niet letterlijk in de sectie van de vindplaats: {naam}")
    if not any(n and n in blok for n in namen_van(b)):
        fouten.append(f"naam noch variant komt voor in de sectie van de vindplaats: {naam}")
    return fouten


def nieuw_in_corpus(data, extractie):
    """Kandidaat-begrippen uit het corpus die nergens zijn afgedekt."""
    gedekt = {n.lower() for b in data.get("begrippen", []) for n in namen_van(b) if n}
    gedekt |= {n["term"].lower() for n in data.get("negeerlijst", []) if n.get("term")}
    werkvoorraad = {t.lower() for t in data.get("werkvoorraad", [])}
    nieuw = []
    for t in extractie.get("termen", []):
        if t.get("indeling") != "kandidaat-begrip":
            continue
        vormen = [s["schrijfwijze"] for s in t.get("schrijfwijzen", [])]
        if any(v.lower() in gedekt for v in vormen):
            continue
        if t["sleutel"].lower() in werkvoorraad:
            continue
        nieuw.append(vormen[0])
    return sorted(nieuw)


def voorkomens(b, extractie):
    """Aantal voorkomens in de markdown, berekend uit de extractie."""
    vormen = {n.lower() for n in namen_van(b) if n}
    n = 0
    for t in extractie.get("termen", []):
        for s in t.get("schrijfwijzen", []):
            if s["schrijfwijze"].lower() in vormen:
                n += s["aantal"]
    return n


def link(vindplaats, map_pad):
    bestand, _, kop = vindplaats.partition("#")
    rel = os.path.relpath(WORTEL / bestand, map_pad)
    return rel + (f"#{kop}" if kop else "")


def bronlink(vindplaats, map_pad):
    naam = vindplaats.split("#")[0].split("/")[-1]
    return f"[{naam}]({link(vindplaats, map_pad)})"


def bron(b, map_pad):
    """Verwijzing naar de bron van de definitie: een kaderpagina of een OKx-document."""
    vp = b.get("vindplaats")
    if not vp:
        return ""
    if vp.startswith("http"):
        for k in b.get("kaders", {}).values():
            if k.get("uitkomst") == "tegenhanger" and k.get("url") == vp:
                return f"[{k['begrip']}]({vp})"
        return f"[bron]({vp})"
    return bronlink(vp, map_pad)


def kadercel(k, map_pad):
    if not k:
        return ""
    if k["uitkomst"] == "tegenhanger":
        cel = f"[`{k['begrip']}`]({k['url']})"
        return cel + (" (verbijzondering)" if k.get("verbijzondering") else "")
    return k["uitkomst"]


def schrijf(data, referentie, doel):
    map_pad = doel.parent
    r = [KOP.rstrip("\n"), "", data["scope"], "", data["zoekmethode"], ""]
    begrippen = data["begrippen"]
    gedef = [b for b in begrippen if b["status"] == "gedefinieerd"]
    open_b = [b for b in begrippen if b["status"] != "gedefinieerd"]
    uit_kader = [b for b in gedef if b.get("bron_soort") == "referentiekader"]

    r += ["## Dekking", "",
          f"Versie {data['versie']}. De kaders zijn geraadpleegd op {referentie['opgehaald']}.", "",
          "| | |", "|---|---|",
          f"| Begrippen en objecttypen | {len(begrippen)} |",
          f"| Met een definitie uit een referentiekader | {len(uit_kader)} |",
          f"| Met een definitie uit een OKx-document | {len(gedef) - len(uit_kader)} |",
          f"| Zonder definitie | {len(open_b)} |",
          f"| Termen uit de markdown die nog wachten | {len(data.get('werkvoorraad', []))} |",
          ""]

    r += ["## Begrippen", "",
          "De begrippen delen de keten in. Ze zijn niveau 1 in het "
          "[Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/); "
          "de objecttypen eronder zijn niveau 2. De uitleg van die gelaagdheid staat in het "
          "[informatiemodel](../../../model/informatiemodel/informatiemodel.md#begrippen).", "",
          "| Begrip | Definitie | Herkomst | Bron |", "|---|---|---|---|"]
    for b in [x for x in begrippen if x["niveau"] == 1]:
        d = b["definitie"] or "*nog te definiëren*"
        r.append(f"| `{b['naam']}` | {d} | {b['herkomst']} | {bron(b, map_pad)} |")
    r.append("")

    r += ["## Objecttypen met een definitie", "",
          "| Objecttype | Begrip | Definitie | Herkomst | Bron |", "|---|---|---|---|---|"]
    for b in sorted([x for x in gedef if x["niveau"] == 2], key=lambda x: (x["familie"] or "", x["naam"])):
        r.append(f"| `{b['naam']}` | {b['familie'] or ''} | {b['definitie']} | {b['herkomst']} "
                 f"| {bron(b, map_pad)} |")
    r.append("")

    r += ["## Objecttypen zonder definitie", "",
          "Deze objecttypen staan op de plaat, hebben geen tegenhanger in MORA of KOI, en zijn "
          "binnen OKx nog niet gedefinieerd.", "",
          "| Begrip | Objecttypen |", "|---|---|"]
    per_familie = defaultdict(list)
    for b in [x for x in open_b if x["niveau"] == 2]:
        per_familie[b["familie"] or "Buiten de kolommen"].append(b["naam"])
    for familie in sorted(per_familie):
        r.append(f"| {familie} | " + ", ".join(f"`{n}`" for n in sorted(per_familie[familie])) + " |")
    r.append("")

    r += ["## Mapping naar de referentiekaders", "",
          "Per kader een van drie uitkomsten, nooit een lege cel: een tegenhanger met link, "
          "`geen tegenhanger gevonden`, of `nog niet onderzocht`. Bij een verbijzondering gaat OKx "
          "verder dan het kader; de reden staat in "
          "[`begrippen.json`](begrippen.json).", "",
          "| Begrip of objecttype | " + " | ".join(data["kaders"]) + " |",
          "|---" * (len(data["kaders"]) + 1) + "|"]
    for b in sorted(begrippen, key=lambda x: (x["niveau"], x["familie"] or "", x["naam"])):
        cellen = [kadercel(b.get("kaders", {}).get(k), map_pad) for k in data["kaders"]]
        r.append(f"| `{b['naam']}` | " + " | ".join(cellen) + " |")
    r.append("")

    r += ["## Negeerlijst", "",
          "Termen die tussen backquotes voorkomen maar geen begrip zijn.", "",
          "| Term | Reden |", "|---|---|"]
    for n in sorted(data["negeerlijst"], key=lambda n: (n["reden"], n["term"])):
        r.append(f"| `{n['term']}` | {n['reden']} |")

    r.append(VOET)
    doel.write_text("\n".join(r).rstrip("\n") + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--controleer", action="store_true", help="alleen controleren, niets schrijven")
    p.add_argument("--map", default=str(WORTEL / DEELPAD), help="map met begrippen.json")
    args = p.parse_args()

    kaart = Path(args.map)
    data = json.loads((kaart / "begrippen.json").read_text(encoding="utf-8"))
    extractie = json.loads((kaart / "begrippen-extractie.json").read_text(encoding="utf-8"))
    im = json.loads((WORTEL / "architecture/model/informatiemodel/informatiemodel.json")
                    .read_text(encoding="utf-8"))

    referentie = json.loads((kaart / "referentiekaders.json").read_text(encoding="utf-8"))
    fouten = controleer(data, extractie, im, referentie)
    if fouten:
        print(f"{len(fouten)} problemen:", file=sys.stderr)
        for f in fouten:
            print(f"  {f}", file=sys.stderr)
        sys.exit(1)

    gedef = sum(1 for b in data["begrippen"] if b["status"] == "gedefinieerd")
    print(f"controle geslaagd: {len(data['begrippen'])} begrippen, {gedef} met definitie en vindplaats")
    print(f"werkvoorraad buiten deze versie: {len(data.get('werkvoorraad', []))} termen")
    if not args.controleer:
        doel = kaart / "begrippenlijst.md"
        schrijf(data, referentie, doel)
        print(f"geschreven naar {doel}")


if __name__ == "__main__":
    main()
