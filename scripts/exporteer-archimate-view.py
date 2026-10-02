#!/usr/bin/env python3
"""De stromen van een ArchiMate-view als machineleesbare lijst schrijven.

Waarom dit script bestaat: de hoofdplaat informatiestromen leeft als view in het
ArchiMate-model, maar een regeltabel die naar een pijl wil verwijzen heeft een
stabiele sleutel nodig. Dit script leest een view alleen en schrijft per flow de
relatie-id uit Archi, de componenten aan beide kanten (junctions opgelost), het
relatietype, het label uit de labelexpressie of de relatienaam, en de koppeling-ID
uit een mapping. Geen layout; dat doet teken-archimate-view.py.

    python3 scripts/exporteer-archimate-view.py [--model PAD] [--view NAAM]
        [--mapping PAD] [--uit PAD]

Het model wordt alleen gelezen, nooit geschreven.
"""

import argparse
import json
import pathlib
import sys
import xml.etree.ElementTree as ET

XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
MODEL = pathlib.Path("architecture/model/model.archimate")
UIT = pathlib.Path("architecture/model/informatiemodel/stromen.json")
VIEW = "OKx hoofdplaat v1.7<concept> (zonder context applicaties)"
ZONDER = "zonder koppelingspecificatie"
CONTAINERS = {"ApplicationComponent", "BusinessActor", "BusinessRole", "Node", "Grouping", "Group"}


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
                             "doel": el.get("target"), "naam": el.get("name") or ""}
        elif soort != "ArchimateDiagramModel":
            elementen[eid] = {"soort": soort, "naam": el.get("name") or ""}
    return wortel, elementen, relaties


def views(wortel):
    return {el.get("name"): el for el in wortel.iter("element")
            if el.get(XSI, "").endswith("ArchimateDiagramModel")}


def labelexpressie(knoop):
    for feature in knoop.findall("feature"):
        if feature.get("name") == "labelExpression":
            return " ".join(feature.get("value", "").split())
    return ""


def lees_view(view, elementen):
    """Per diagramobject: element-id, soort, naam en de ouder-component; per connectie de bron en doel."""
    objecten, connecties = {}, []

    def loop(knoop, ouder_component):
        ref = knoop.get("archimateElement")
        el = elementen.get(ref, {"soort": knoop.get(XSI, "").replace("archimate:", ""), "naam": knoop.get("name") or ""})
        eigen = knoop.get("id")
        component = eigen if el["soort"] in CONTAINERS else ouder_component
        objecten[eigen] = {"element": ref, "soort": el["soort"], "naam": el["naam"], "component": component}
        for conn in knoop.findall("sourceConnection"):
            connecties.append({"bron": eigen, "doel": conn.get("target"),
                               "relatie": conn.get("archimateRelationship"), "label": labelexpressie(conn)})
        for kind in knoop.findall("child"):
            loop(kind, component)

    for kind in view.findall("child"):
        loop(kind, None)
    return objecten, connecties


def componentnaam(objecten, obj_id):
    obj = objecten.get(obj_id)
    if obj is None:
        return None
    houder = objecten.get(obj["component"]) if obj["component"] else None
    return " ".join((houder or obj)["naam"].split())


def stromen(objecten, connecties, relaties, mapping):
    """Flows tussen componenten; een junction wordt opgelost naar de uiteinden erachter."""
    uitgaand = {}
    for conn in connecties:
        uitgaand.setdefault(conn["bron"], []).append(conn)

    def doelen(conn, bezocht):
        doel = objecten.get(conn["doel"])
        if doel is None:
            return []
        if doel["soort"] == "Junction":
            if conn["doel"] in bezocht:
                return []
            uit = []
            for volgende in uitgaand.get(conn["doel"], []):
                uit.extend(doelen(volgende, bezocht | {conn["doel"]}))
            return uit
        return [(conn, doel)]

    uit = []
    for conn in connecties:
        rel = relaties.get(conn["relatie"])
        if rel is None or rel["soort"] != "Flow":
            continue
        bron = objecten.get(conn["bron"])
        if bron is None or bron["soort"] == "Junction":
            continue
        van = componentnaam(objecten, conn["bron"])
        for laatste, doel in doelen(conn, set()):
            naar = componentnaam(objecten, laatste["doel"])
            laatste_rel = relaties.get(laatste["relatie"], rel)
            label = conn["label"] or laatste["label"] or rel["naam"] or laatste_rel["naam"]
            uit.append({"id": conn["relatie"], "van": van, "naar": naar, "soort": "Flow",
                        "label": label, "koppeling": mapping.get(f"{van} > {naar}", ZONDER)})
    uit.sort(key=lambda s: (s["van"], s["naar"], s["label"], s["id"]))
    return uit


def exporteer(model=MODEL, viewnaam=VIEW, mapping=None):
    wortel, elementen, relaties = lees_model(model)
    alle = views(wortel)
    if viewnaam not in alle:
        sys.exit("view niet gevonden: " + viewnaam + "\nbeschikbaar:\n  " + "\n  ".join(sorted(alle)))
    objecten, connecties = lees_view(alle[viewnaam], elementen)
    return {"view": viewnaam, "model": str(model), "stromen": stromen(objecten, connecties, relaties, mapping or {})}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--view", default=VIEW)
    parser.add_argument("--mapping", type=pathlib.Path, help="JSON: {\"Van > Naar\": \"OC-P&R\", ...}")
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    args = parser.parse_args(argv)
    mapping = json.loads(args.mapping.read_text(encoding="utf-8")) if args.mapping else {}
    if not args.model.exists():
        print(f"model niet gevonden: {args.model}", file=sys.stderr)
        return 2
    uitkomst = exporteer(args.model, args.view, mapping)
    args.uit.parent.mkdir(parents=True, exist_ok=True)
    args.uit.write_text(json.dumps(uitkomst, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(uitkomst['stromen'])} stromen geschreven naar {args.uit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
