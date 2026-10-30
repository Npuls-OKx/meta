#!/usr/bin/env python3
"""De applicatiecomponenten van de hoofdplaat uit het ArchiMate-model halen, met hun MORA-definitie
en de applicatiediensten die zij realiseren.

Waarom dit script bestaat: het voorbeeld en de koppelingspecificaties noemen systemen bij naam, maar
wat een systeem doet stond nergens machinaal vast. MORA beschrijft dat, en die beschrijving staat in
het model. Dit script haalt haar eruit, zodat de controle componentnamen kan toetsen en het document
kan tonen wat een systeem doet.

    python3 scripts/exporteer-componenten.py [--model PAD] [--uit PAD]

Het model wordt alleen gelezen; raak nooit een .archimate-bestand aan.
"""

import argparse
import collections
import json
import pathlib
import sys
import xml.etree.ElementTree as ET

MODEL = pathlib.Path("architecture/model/model.archimate")
STROMEN = pathlib.Path("architecture/model/informatiemodel/stromen.json")
UIT = pathlib.Path("architecture/model/informatiemodel/componenten.json")
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
COMPONENT = "archimate:ApplicationComponent"
DIENST = "archimate:ApplicationService"
REALISEERT = "archimate:RealizationRelationship"


def norm(s):
    return " ".join(str(s or "").split())


def lees_model(pad):
    try:
        return ET.parse(pad)
    except (OSError, ET.ParseError) as fout:
        sys.exit(f"model niet leesbaar: {pad}: {fout}")


def verzamel(boom, namen):
    """Per gevraagde componentnaam de documentatie en de diensten die hij realiseert."""
    elementen = {el.get("id"): el for el in boom.iter("element") if el.get("id")}
    naam = {i: norm(e.get("name")) for i, e in elementen.items()}
    soort = {i: e.get(XSI) or "" for i, e in elementen.items()}
    doc = {i: norm(e.findtext("documentation")) for i, e in elementen.items()}

    ids_van = collections.defaultdict(list)
    for i, n in naam.items():
        if soort[i] == COMPONENT and n in namen:
            ids_van[n].append(i)

    diensten = collections.defaultdict(list)
    for el in boom.iter("element"):
        if el.get(XSI) != REALISEERT:
            continue
        bron, doel = el.get("source"), el.get("target")
        if soort.get(doel) != DIENST:
            continue
        for n, ids in ids_van.items():
            if bron in ids:
                diensten[n].append({"naam": naam[doel], "definitie": doc.get(doel, "")})

    uit = []
    for n in sorted(namen):
        ids = ids_van.get(n) or []
        definitie = next((doc[i] for i in ids if doc.get(i)), "")
        rij = {"naam": n, "definitie": definitie,
               "diensten": sorted(diensten.get(n, []), key=lambda d: d["naam"])}
        if not ids:
            rij["opmerking"] = "staat niet als applicatiecomponent in het model"
        uit.append(rij)
    return uit


def componentnamen(stromen):
    namen = set()
    for s in stromen.get("stromen", []):
        namen.add(norm(s["van"]))
        namen.add(norm(s["naar"]))
    return namen


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--stromen", type=pathlib.Path, default=STROMEN)
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    parser.add_argument("--extra", nargs="*", default=[],
                        help="componentnamen buiten de hoofdplaat, bijvoorbeeld Intakesysteem")
    args = parser.parse_args(argv)

    try:
        stromen = json.loads(args.stromen.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"stromen niet gevonden: {args.stromen}")
    namen = componentnamen(stromen) | {norm(x) for x in args.extra}
    componenten = verzamel(lees_model(args.model), namen)
    args.uit.parent.mkdir(parents=True, exist_ok=True)
    args.uit.write_text(json.dumps({"componenten": componenten}, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    zonder = [c["naam"] for c in componenten if not c["definitie"]]
    print(f"{len(componenten)} componenten geschreven naar {args.uit}"
          + (f"; zonder definitie: {', '.join(zonder)}" if zonder else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
