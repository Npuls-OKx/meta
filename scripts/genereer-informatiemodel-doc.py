"""De machineleesbare weergave van het informatiemodel schrijven vanuit het ArchiMate-model.

Waarom dit script bestaat: de plaat is de leesbare weergave, maar een agent of
een validatiescript kan er niet mee werken. Dit script schrijft dezelfde inhoud
als `informatiemodel.json`: objecttypen met hun kolom en scope, de relaties, en
de mapping naar OEAPI. De prozadocumentatie blijft handwerk.

    python3 scripts/genereer-informatiemodel-doc.py

Het model wordt alleen gelezen, nooit geschreven.
"""

import json
import pathlib
import sys
import xml.etree.ElementTree as ET

XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
MODEL = pathlib.Path("architecture/model/model.archimate")
MAP = pathlib.Path("architecture/model/informatiemodel")
VIEW_IM = "OKx informatiemodel"
VIEW_MAP = "OKx informatiemodel en mapping OEAPI"
LEGENDA = {"Buiten scope binnen OKx", "OKx referentiekader alligned met MORA en HORA via klus 53",
           "OEAPI v6 Object of attribuut"}
GRIJS = {"#f2f2f2": "les-laag", "#e8e8e8": "landelijk belegd", "#e0e0e0": "instellingsartefact"}
OEAPI = {"Attendance", "ComponentOfferingAssociation", "Course", "CourseOffering",
         "CourseOfferingAssociation", "Group", "LearningComponent", "LearningComponentOffering",
         "Person", "Programme", "ProgrammeOffering", "ProgrammeOfferingAssociation", "Result",
         "TestComponent", "TestComponentOffering", "TestComponentOfferingAssociation"}
KOLOMVOLGORDE = ["Kwalificatiekader MBO", "Onderwijskundigkader instelling", "Onderwijsspecificatie",
                 "Onderwijsaanbod", "Onderwijsverbintenis", "Onderwijsresultaat", "Resultaatstructuur"]


def lees_model():
    wortel = ET.parse(MODEL).getroot()
    elementen, relaties = {}, {}
    for el in wortel.iter("element"):
        soort = el.get(XSI, "").replace("archimate:", "")
        eid = el.get("id")
        if not eid:
            continue
        if "Relationship" in soort:
            relaties[eid] = (soort.replace("Relationship", ""), el.get("source"),
                             el.get("target"), el.get("name", ""))
        else:
            elementen[eid] = el.get("name", "")
    return wortel, elementen, relaties


def view(wortel, naam):
    for el in wortel.iter("element"):
        if el.get("name") == naam and el.get(XSI, "").endswith("ArchimateDiagramModel"):
            return el
    sys.exit(f"view niet gevonden: {naam}")


def leden(knoop, elementen):
    uit = []
    for kind in knoop.iter():
        if kind is knoop:
            continue
        ref = kind.get("archimateElement")
        if ref:
            uit.append(elementen[ref])
    return uit


def main():
    wortel, elementen, relaties = lees_model()

    v = view(wortel, VIEW_IM)
    kolom_van, buiten, kleur = {}, [], {}
    for kind in list(v):
        if kind.get(XSI) == "archimate:Group":
            if kind.get("name") != "Legenda":
                for n in set(leden(kind, elementen)) - LEGENDA:
                    kolom_van[n] = kind.get("name")
        elif kind.get("archimateElement"):
            buiten.append(elementen[kind.get("archimateElement")])
            buiten.extend(leden(kind, elementen))
    for kind in v.iter():
        ref = kind.get("archimateElement")
        if ref:
            kleur[elementen[ref]] = kind.get("fillColor") or "standaard"
    for n in set(buiten) - LEGENDA:
        kolom_van.setdefault(n, None)

    objecttypen = []
    for n in sorted(kolom_van):
        k = kleur.get(n, "standaard")
        objecttypen.append({
            "naam": n,
            "kolom": kolom_van[n],
            "scope": "binnen" if k == "standaard" else "buiten",
            "reden_buiten_scope": None if k == "standaard" else GRIJS.get(k, k),
        })

    rel_ids = {k.get("archimateRelationship") for k in v.iter() if k.get("archimateRelationship")}
    naam = lambda i: elementen.get(i, "?")
    relatielijst = []
    for rid in sorted(rel_ids):
        if rid in relaties:
            soort, van, naar, label = relaties[rid]
            relatielijst.append({"soort": soort, "van": naam(van), "naar": naam(naar),
                                 "label": label or None})
    relatielijst.sort(key=lambda r: (r["soort"], r["van"], r["naar"]))

    vm = view(wortel, VIEW_MAP)
    map_rels = {k.get("archimateRelationship") for k in vm.iter() if k.get("archimateRelationship")}
    mapping = []
    for rid in sorted(map_rels):
        if rid not in relaties:
            continue
        soort, van, naar = relaties[rid][0], naam(relaties[rid][1]), naam(relaties[rid][2])
        if (van in OEAPI) != (naar in OEAPI):
            okx, oeapi = (naar, van) if van in OEAPI else (van, naar)
            mapping.append({"okx": okx, "oeapi": oeapi, "relatie": soort})
    mapping.sort(key=lambda m: (m["okx"], m["oeapi"]))
    gemapt = {m["okx"] for m in mapping}
    for o in objecttypen:
        o["oeapi"] = sorted({m["oeapi"] for m in mapping if m["okx"] == o["naam"]}) or None

    uit = {
        "bron": {"model": str(MODEL), "views": [VIEW_IM, VIEW_MAP]},
        "objecttypen": objecttypen,
        "relaties": relatielijst,
        "oeapi_mapping": mapping,
    }
    doel = MAP / "informatiemodel.json"
    doel.write_text(json.dumps(uit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    zonder = [o["naam"] for o in objecttypen if not o["oeapi"]]
    print(f"{doel}: {len(objecttypen)} objecttypen, {len(relatielijst)} relaties, "
          f"{len(mapping)} OEAPI-koppelingen, {len(zonder)} objecttypen zonder tegenhanger")


if __name__ == "__main__":
    main()
