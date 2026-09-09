"""Tabellen in de informatiemodel-documentatie bijwerken vanuit het ArchiMate-model.

Waarom dit script bestaat: de objecttypen en relaties in de documentatie moeten
gelijk lopen met het model. Overtypen vanaf de plaat gaat een keer goed en
daarna niet meer. Dit script vervangt alleen de blokken tussen de markeringen
`<!-- gegenereerd:<naam> -->` en `<!-- /gegenereerd -->`; de tekst eromheen
blijft ongemoeid.

    python3 scripts/genereer-informatiemodel-doc.py

Het model wordt alleen gelezen, nooit geschreven.
"""

import collections
import pathlib
import re
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


def vervang(pad, naam, inhoud):
    tekst = pad.read_text(encoding="utf-8")
    patroon = re.compile(rf"(<!-- gegenereerd:{naam} -->\n)(.*?)(<!-- /gegenereerd -->)", re.S)
    if not patroon.search(tekst):
        sys.exit(f"markering ontbreekt in {pad}: {naam}")
    pad.write_text(patroon.sub(lambda m: m.group(1) + inhoud + "\n" + m.group(3), tekst), encoding="utf-8")


def main():
    wortel, elementen, relaties = lees_model()

    v = view(wortel, VIEW_IM)
    kolommen, buiten, kleur = {}, [], {}
    for kind in list(v):
        if kind.get(XSI) == "archimate:Group":
            if kind.get("name") != "Legenda":
                kolommen[kind.get("name")] = sorted(set(leden(kind, elementen)) - LEGENDA)
        elif kind.get("archimateElement"):
            buiten.append(elementen[kind.get("archimateElement")])
            buiten.extend(leden(kind, elementen))
    for kind in v.iter():
        ref = kind.get("archimateElement")
        if ref:
            kleur[elementen[ref]] = kind.get("fillColor") or "standaard"
    buiten = sorted(set(buiten) - LEGENDA)
    alle = sorted({n for leden_ in kolommen.values() for n in leden_} | set(buiten))

    def scope(n):
        k = kleur.get(n, "standaard")
        return "binnen scope" if k == "standaard" else f"buiten scope ({GRIJS.get(k, k)})"

    def tabel(namen):
        regels = ["| Objecttype | Scope |", "|---|---|"]
        regels += [f"| `{n}` | {scope(n)} |" for n in namen]
        return "\n".join(regels)

    blokken = []
    for kolom in KOLOMVOLGORDE:
        if kolom in kolommen:
            blokken.append(f"### {kolom}\n\n{tabel(kolommen[kolom])}")
    blokken.append(f"### Buiten de kolommen\n\n{tabel(buiten)}")
    vervang(MAP / "informatiemodel.md", "objecttypen",
            f"In totaal {len(alle)} objecttypen.\n\n" + "\n\n".join(blokken))

    rel_ids = {k.get("archimateRelationship") for k in v.iter() if k.get("archimateRelationship")}
    naam = lambda i: elementen.get(i, "?")
    per_soort = collections.defaultdict(set)
    for rid in rel_ids:
        if rid in relaties:
            soort, van, naar, label = relaties[rid]
            per_soort[soort].add((naam(van), naam(naar), label))
    uitleg = {
        "Specialization": "Het ene objecttype is een verbijzondering van het andere.",
        "Aggregation": "Het ene objecttype bestaat uit het andere. De recursieve varianten zijn bewust: structuren kunnen genest zijn.",
        "Association": "Een inhoudelijke samenhang zonder eigenaarschap of samenstelling.",
        "Access": "Een persoon raakt het objecttype, als student of als medewerker.",
    }
    stukken = []
    for soort in ("Specialization", "Aggregation", "Association", "Access"):
        rijen = sorted(per_soort.get(soort, []))
        kop = f"### {soort} ({len(rijen)})\n\n{uitleg[soort]}\n\n| Van | Naar | Label |\n|---|---|---|"
        stukken.append(kop + "\n" + "\n".join(f"| `{a}` | `{b}` | {c or ''} |" for a, b, c in rijen))
    vervang(MAP / "informatiemodel.md", "relaties", "\n\n".join(stukken))

    vm = view(wortel, VIEW_MAP)
    map_rels = {k.get("archimateRelationship") for k in vm.iter() if k.get("archimateRelationship")}
    paren = set()
    for rid in map_rels:
        if rid not in relaties:
            continue
        soort, van, naar, _ = relaties[rid]
        a, b = naam(van), naam(naar)
        if (a in OEAPI) != (b in OEAPI):
            paren.add((b, a, soort) if a in OEAPI else (a, b, soort))
    gemapt = {okx for okx, _, _ in paren}
    zonder = [n for n in alle if n not in gemapt]
    per_oeapi = collections.defaultdict(set)
    for okx, oeapi, _ in paren:
        per_oeapi[oeapi].add(okx)

    vervang(MAP / "informatiemodel-oeapi-mapping.md", "mapping",
            f"{len(paren)} koppelingen tussen {len(gemapt)} OKx-objecttypen en OEAPI v6.\n\n"
            "| OKx-objecttype | OEAPI v6 | Relatie |\n|---|---|---|\n"
            + "\n".join(f"| `{a}` | `{b}` | {s} |" for a, b, s in sorted(paren)))
    vervang(MAP / "informatiemodel-oeapi-mapping.md", "meervoudig",
            "| OEAPI v6 | OKx-objecttypen |\n|---|---|\n"
            + "\n".join(f"| `{o}` | {', '.join('`' + x + '`' for x in sorted(v_))} |"
                        for o, v_ in sorted(per_oeapi.items()) if len(v_) > 1))
    vervang(MAP / "informatiemodel-oeapi-mapping.md", "zonder-tegenhanger",
            f"{len(zonder)} van de {len(alle)} objecttypen hebben geen OEAPI-tegenhanger op deze plaat.\n\n"
            "| OKx-objecttype zonder OEAPI-tegenhanger |\n|---|\n"
            + "\n".join(f"| `{n}` |" for n in zonder))

    print(f"bijgewerkt: {len(alle)} objecttypen, "
          f"{sum(len(v_) for v_ in per_soort.values())} relaties, {len(paren)} OEAPI-koppelingen")


if __name__ == "__main__":
    main()
