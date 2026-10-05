#!/usr/bin/env python3
"""De stromen van een ArchiMate-view als machineleesbare lijst schrijven.

Waarom dit script bestaat: de hoofdplaat informatiestromen leeft als view in het
ArchiMate-model, maar een regeltabel die naar een pijl wil verwijzen heeft een
stabiele sleutel nodig. Dit script leest een view alleen en schrijft per flow de
relatie-id uit Archi, de componenten aan beide kanten (junctions opgelost), het
relatietype, het label uit de labelexpressie of de relatienaam, en de koppeling-ID
uit een mapping. Geen layout; dat doet teken-archimate-view.py.

    python3 scripts/exporteer-archimate-view.py [--model PAD] [--view NAAM]
        [--mapping PAD] [--aanvullingen PAD] [--uit PAD]

Het model wordt alleen gelezen, nooit geschreven.

Naast de view schrijft dit script de aanvullingen mee: stromen die een nieuwere versie van de
hoofdplaat kent en de gepubliceerde versie nog niet. Die bestaan niet als relatie in het model, want
dat wijzigt alleen de modelleur in Archi. Zonder die aanvullingen zou een voorbeeld dat zo'n stroom
nodig heeft hem met de hand in de uitvoer moeten zetten, en dan verdwijnt hij bij de volgende export.
Een aanvulling draagt daarom haar herkomst, haar status en de bron waaruit zij komt, en haar id begint
met "aanvulling-" zodat zij zich onderscheidt van een relatie-id uit Archi.
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
AANVULLINGEN = pathlib.Path("architecture/model/informatiemodel/stromen-aanvullingen.json")
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


def lees_aanvullingen(pad):
    """De stromen die een nieuwere hoofdplaat kent en de gepubliceerde view nog niet.

    Elke aanvulling draagt een eigen id dat met "aanvulling-" begint, plus herkomst, status en bron.
    Ontbreekt het bestand, dan levert dit niets op: de export blijft dan precies de view.
    """
    if pad is None or not pathlib.Path(pad).exists():
        return []
    inhoud = json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    uit = []
    for a in inhoud.get("aanvullingen", []):
        ontbreekt = [v for v in ("id", "van", "naar", "label", "herkomst", "status", "bron") if not a.get(v)]
        if ontbreekt:
            sys.exit(f"aanvulling {a.get('id', '(zonder id)')!r} mist {', '.join(ontbreekt)}")
        if not a["id"].startswith("aanvulling-"):
            sys.exit(f"aanvulling {a['id']!r} hoort een id te dragen dat met 'aanvulling-' begint, "
                     f"zodat zij zich onderscheidt van een relatie-id uit Archi")
        uit.append(dict(a, soort=a.get("soort", "Flow"), koppeling=a.get("koppeling", ZONDER)))
    return uit


TOELICHTING = ("De stromen van de genoemde view, plus de aanvullingen uit stromen-aanvullingen.json. "
               "Een stroom met een id dat met 'aanvulling-' begint staat nog niet op de gepubliceerde "
               "hoofdplaat; haar herkomst en status zeggen uit welke versie zij komt. Wie de plaat "
               "gebruikt om iets te verantwoorden kijkt dus naar de view; wie een voorbeeld leest ziet "
               "aan de aanvulling dat die lijn nog in aanbouw is.")


def exporteer(model=MODEL, viewnaam=VIEW, mapping=None, aanvullingen=None):
    """De view als lijst stromen. Zonder aanvullingen is de uitkomst precies de view; main() geeft het
    pad naar de aanvullingen mee, zodat de uitvoer van het script ze wel draagt."""
    wortel, elementen, relaties = lees_model(model)
    alle = views(wortel)
    if viewnaam not in alle:
        sys.exit("view niet gevonden: " + viewnaam + "\nbeschikbaar:\n  " + "\n  ".join(sorted(alle)))
    objecten, connecties = lees_view(alle[viewnaam], elementen)
    uit = stromen(objecten, connecties, relaties, mapping or {})
    extra = lees_aanvullingen(aanvullingen)
    bekend = {(s["van"], s["naar"], s["label"]) for s in uit}
    for a in extra:
        if (a["van"], a["naar"], a["label"]) in bekend:
            sys.exit(f"aanvulling {a['id']!r} staat al als stroom in de view; haal haar uit "
                     f"stromen-aanvullingen.json")
    uit += extra
    uit.sort(key=lambda s: (s["van"], s["naar"], s["label"], s["id"]))
    return {"view": viewnaam, "model": str(model), "toelichting": TOELICHTING,
            "aanvullingen_uit": str(aanvullingen) if extra else None, "stromen": uit}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--view", default=VIEW)
    parser.add_argument("--mapping", type=pathlib.Path, help="JSON: {\"Van > Naar\": \"OC-P&R\", ...}")
    parser.add_argument("--aanvullingen", type=pathlib.Path, default=AANVULLINGEN,
                        help="stromen die een nieuwere hoofdplaat kent en de view nog niet")
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    args = parser.parse_args(argv)
    mapping = json.loads(args.mapping.read_text(encoding="utf-8")) if args.mapping else {}
    if not args.model.exists():
        print(f"model niet gevonden: {args.model}", file=sys.stderr)
        return 2
    uitkomst = exporteer(args.model, args.view, mapping, args.aanvullingen)
    args.uit.parent.mkdir(parents=True, exist_ok=True)
    args.uit.write_text(json.dumps(uitkomst, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    extra = [s for s in uitkomst["stromen"] if s["id"].startswith("aanvulling-")]
    staart = f", waarvan {len(extra)} uit de aanvullingen" if extra else ""
    print(f"{len(uitkomst['stromen'])} stromen geschreven naar {args.uit}{staart}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
