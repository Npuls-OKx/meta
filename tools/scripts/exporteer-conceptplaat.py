#!/usr/bin/env python3
"""De objecttypen en relaties van een concept-view als machineleesbare lijst schrijven.

Waarom dit script bestaat: de voorbeelduitwerking van Jochem wordt gecontroleerd tegen
de informatiemodelplaat (MIM 1 en 2). Een verdieping mag putten uit een conceptplaat
zoals "Informatiemodel Onderwijsontwerp", maar alleen met objecttypen en relaties die
daar echt op staan. Dit script leest zo'n view alleen en schrijft de objecttypen (met
de groep waarin ze staan) en de relaties die op de view getekend zijn, in dezelfde vorm
als informatiemodel.json, zodat controleer-voorbeeldregels.py er zonder omweg mee werkt.

    python3 scripts/exporteer-conceptplaat.py [--model PAD] [--view NAAM] [--uit PAD]

Het model wordt alleen gelezen, nooit geschreven.
"""

import argparse
import json
import pathlib
import sys
import xml.etree.ElementTree as ET

XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
MODEL = pathlib.Path("architecture/model/model.archimate")
UIT = pathlib.Path("architecture/model/informatiemodel/conceptplaat-onderwijsontwerp.json")
VIEW = "Informatiemodel Onderwijsontwerp"
GROEPEN = {"Grouping", "Group"}
GEEN_OBJECT = GROEPEN | {"Note", "DiagramModelReference", "DiagramModelNote"}


def norm(naam):
    return " ".join((naam or "").split())


def lees_model(pad):
    try:
        wortel = ET.parse(pad).getroot()
    except (OSError, ET.ParseError) as fout:
        sys.exit(f"model niet leesbaar: {pad} ({fout})")
    elementen, relaties = {}, {}
    for el in wortel.iter("element"):
        soort = el.get(XSI, "").replace("archimate:", "")
        eid = el.get("id")
        if not eid or not soort:
            continue
        if soort.endswith("Relationship"):
            relaties[eid] = {"soort": soort.replace("Relationship", ""), "bron": el.get("source"),
                             "doel": el.get("target"), "label": norm(el.get("name")) or None}
        elif soort != "ArchimateDiagramModel":
            elementen[eid] = {"soort": soort, "naam": norm(el.get("name"))}
    return wortel, elementen, relaties


def views(wortel):
    return {el.get("name"): el for el in wortel.iter("element")
            if el.get(XSI, "").endswith("ArchimateDiagramModel")}


def lees_view(view, elementen):
    """Objecttypen op de view met hun groep (de buitenste grouping), en de relatie-id's van de connecties."""
    objecttypen, relatie_ids = {}, []

    def loop(knoop, groep):
        ref = knoop.get("archimateElement")
        el = elementen.get(ref, {"soort": knoop.get(XSI, "").replace("archimate:", ""), "naam": norm(knoop.get("name"))})
        eigen_groep = groep
        if el["soort"] in GROEPEN:
            eigen_groep = groep or el["naam"] or None
        elif el["soort"] not in GEEN_OBJECT and el["naam"]:
            objecttypen.setdefault(el["naam"], {"naam": el["naam"], "soort": el["soort"], "groep": groep})
        for conn in knoop.findall("sourceConnection"):
            if conn.get("archimateRelationship"):
                relatie_ids.append(conn.get("archimateRelationship"))
        for kind in knoop.findall("child"):
            loop(kind, eigen_groep)

    for kind in view.findall("child"):
        loop(kind, None)
    return objecttypen, relatie_ids


def exporteer(model=MODEL, viewnaam=VIEW):
    wortel, elementen, relaties = lees_model(model)
    alle = views(wortel)
    if viewnaam not in alle:
        sys.exit("view niet gevonden: " + viewnaam + "\nbeschikbaar:\n  " + "\n  ".join(sorted(alle)))
    objecttypen, relatie_ids = lees_view(alle[viewnaam], elementen)
    uit_relaties, gezien = [], set()
    for rid in relatie_ids:
        rel = relaties.get(rid)
        if rel is None:
            continue
        van, naar = elementen.get(rel["bron"]), elementen.get(rel["doel"])
        if not van or not naar or van["soort"] in GEEN_OBJECT or naar["soort"] in GEEN_OBJECT:
            continue
        sleutel = (rel["soort"], van["naam"], naar["naam"], rel["label"])
        if sleutel in gezien:
            continue
        gezien.add(sleutel)
        uit_relaties.append({"soort": rel["soort"], "van": van["naam"], "naar": naar["naam"], "label": rel["label"]})
    return {"bron": {"model": str(model), "view": viewnaam},
            "objecttypen": [objecttypen[n] for n in sorted(objecttypen)],
            "relaties": sorted(uit_relaties, key=lambda r: (r["soort"], r["van"], r["naar"], r["label"] or ""))}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--view", default=VIEW)
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    args = parser.parse_args(argv)
    if not args.model.exists():
        print(f"model niet gevonden: {args.model}", file=sys.stderr)
        return 2
    uitkomst = exporteer(args.model, args.view)
    args.uit.parent.mkdir(parents=True, exist_ok=True)
    args.uit.write_text(json.dumps(uitkomst, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(uitkomst['objecttypen'])} objecttypen en {len(uitkomst['relaties'])} relaties geschreven naar {args.uit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
