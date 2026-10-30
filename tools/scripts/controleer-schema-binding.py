#!/usr/bin/env python3
"""De binding tussen de schema's en het informatiemodel toetsen.

Waarom dit bestand bestaat: 23 van de 24 schema's in Npuls-OKx/Public dragen een naam die
geen objecttype in het informatiemodel is, en de vertaling ertussen werd tot nu toe per
veldrij in een interactiespecificatie met de hand gelegd. Van de 276 rijen droegen er 69
proza en 17 een naam die het model niet kent. Zolang die binding niet ergens vastligt, blijft
elke afgeleide plaat zo volledig als de tabel eronder. Relateert aan: Npuls-OKx/meta#385.

    python3 tools/scripts/controleer-schema-binding.py [--binding PAD] [--kort]

Wat het bestand draagt
----------------------

| Deel | Wat erin staat |
|---|---|
| `schemas` | Per schema of het een begrip draagt of vervoer is, en welke objecttypen het draagt |
| `objecttypen` | Per objecttype zijn attribuutsoorten, elk met datatype, kardinaliteit, rol en bron |

Drie soorten schema, met de toets erbij waarmee zij uit elkaar te houden zijn.

| Soort | Wat het is | De toets |
|---|---|---|
| `begrip` | Het draagt objecttypen uit het informatiemodel | Het heeft een eigen identiteit: een `id`, of een `code` met een `name` |
| `waardeobject` | Een genest object zonder eigen identiteit, waarvan de velden attribuutsoort worden van het objecttype dat het houdt | Geen eigen identiteit, en het wordt door een ander schema aangehaald |
| `vervoer` | Het richt het kanaal in, of draagt een verwijzing, een delta of een gebeurtenis | Geen eigen onderwerp: de velden wijzen naar iets anders |

Die grens werd eerst per schema beslist in plaats van met een regel, en liep daardoor uiteen:
`manifest-item.json` stond als vervoer terwijl zes gelijkvormige waardeobjecten als begrip
stonden, en `learning-resource-group.json` stond als vervoer terwijl het een eigen identiteit
draagt. De toets hierboven trekt die grens wel.

Een begripsschema waarvan het model het objecttype mist, draagt dat gat in `mist_objecttype`.
Dat is een uitkomst en geen fout: het benoemt wat het model nog niet kent.

De bron per attribuutsoort
--------------------------
Elke attribuutsoort draagt waar hij vandaan komt, of de vaststelling dat er geen bron is. Dat
laatste is een uitkomst en geen fout: een gat dat benoemd staat, is te dichten.

Dit bestand is een voorstel en geen model. [#369](https://github.com/Npuls-OKx/meta/issues/369)
legt de route vast waarlangs attribuutsoorten als properties in Archi landen, waarna
`genereer-informatiemodel-doc.py` ze meeneemt. Tot die tijd staat hier wat de specificaties
nodig hebben, met de herkomst erbij.

Exitcodes
---------
0: elke binding sluit aan; 1: er is iets dat niet aansluit; 2: de invoer is niet bruikbaar.
"""

import argparse
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent
BINDING = "architecture/model/informatiemodel/schema-binding.json"
MODEL = "architecture/model/informatiemodel/informatiemodel.json"
SCHEMAMAPPEN = [
    "../Public/Informatie-en-gegevensmodellen/schemas",
    "architecture/docs/specificatie/interactieketen-onderwijsaanbod/schemas",
]
SOORTEN = ("begrip", "waardeobject", "vervoer")
VELDEN = ("naam", "datatype", "kardinaliteit", "bron")


class Bevinding:
    def __init__(self, waar, wat):
        self.waar, self.wat = waar, wat

    def __str__(self):
        return f"{self.waar}: {self.wat}"


def schemabestanden(mappen):
    """Elke schemanaam die in een van de meegegeven mappen staat."""
    gevonden = {}
    for map_ in mappen:
        if map_.is_dir():
            for bestand in map_.glob("*.json"):
                gevonden.setdefault(bestand.name, bestand)
    return gevonden


def controleer(binding, objecttypen, schemas):
    """Elke regel van de binding langs het model en de schemamappen."""
    bevindingen = []
    bronsoorten = set(binding.get("bronsoorten") or {})
    if not bronsoorten:
        bevindingen.append(Bevinding("bronsoorten", "het bestand verklaart geen enkele bronsoort"))

    for naam, gegeven in (binding.get("schemas") or {}).items():
        waar = f"schemas/{naam}"
        if naam not in schemas:
            bevindingen.append(Bevinding(waar, "dit schema staat in geen van de schemamappen"))
        soort = gegeven.get("soort")
        if soort not in SOORTEN:
            bevindingen.append(Bevinding(waar, f"soort is {soort!r} en niet een van {SOORTEN}"))
        draagt = gegeven.get("draagt") or []
        landt_op = gegeven.get("landt_op") or []
        mist = gegeven.get("mist_objecttype") or []
        if soort == "vervoer" and (draagt or landt_op):
            bevindingen.append(Bevinding(waar, "een vervoersschema draagt geen objecttype"))
        if soort in ("vervoer", "waardeobject") and not gegeven.get("reden"):
            bevindingen.append(Bevinding(waar, f"een {soort}schema zegt waarom het er een is"))
        if soort == "waardeobject" and draagt:
            bevindingen.append(Bevinding(
                waar, "een waardeobject draagt geen objecttype maar landt erop; gebruik landt_op"))
        if soort == "waardeobject" and not landt_op:
            bevindingen.append(Bevinding(waar, "een waardeobject noemt de objecttypen waarop het landt"))
        if soort == "begrip" and not draagt and not mist:
            bevindingen.append(Bevinding(
                waar, "een begripsschema noemt de objecttypen die het draagt, of het gat in mist_objecttype"))
        if mist and not gegeven.get("reden"):
            bevindingen.append(Bevinding(waar, "een ontbrekend objecttype gaat met de reden erbij"))
        for objecttype in list(draagt) + list(landt_op):
            if objecttype not in objecttypen:
                bevindingen.append(Bevinding(waar, f"{objecttype!r} is geen objecttype in het model"))
        for sleutel, waarde in (gegeven.get("discriminator") or {}).get("waarden", {}).items():
            if waarde not in objecttypen:
                bevindingen.append(Bevinding(
                    f"{waar}, discriminator {sleutel}", f"{waarde!r} is geen objecttype in het model"))

    for naam, gegeven in (binding.get("objecttypen") or {}).items():
        waar = f"objecttypen/{naam}"
        if naam not in objecttypen:
            bevindingen.append(Bevinding(waar, "dit objecttype staat niet in het informatiemodel"))
        gezien = set()
        for attribuut in gegeven.get("attributen") or []:
            for veld in VELDEN:
                if not attribuut.get(veld):
                    bevindingen.append(Bevinding(
                        f"{waar}, {attribuut.get('naam', 'naamloos')}", f"{veld} ontbreekt"))
            bron = (attribuut.get("bron") or "").split(",")[0].split(" ")[0]
            if bron and bron not in bronsoorten:
                bevindingen.append(Bevinding(
                    f"{waar}, {attribuut.get('naam')}", f"bronsoort {bron!r} is niet verklaard"))
            if attribuut.get("naam") in gezien:
                bevindingen.append(Bevinding(
                    f"{waar}, {attribuut['naam']}", "deze attribuutsoort staat er twee keer"))
            gezien.add(attribuut.get("naam"))
    return bevindingen


def tellingen(binding):
    """Wat er in het bestand staat, zodat de uitvoer de omvang toont."""
    schemas = binding.get("schemas") or {}
    objecttypen = binding.get("objecttypen") or {}
    attributen = [a for g in objecttypen.values() for a in (g.get("attributen") or [])]
    per_bron = {}
    for a in attributen:
        soort = (a.get("bron") or "?").split(",")[0].split(" ")[0]
        per_bron[soort] = per_bron.get(soort, 0) + 1
    return {
        "schemas": len(schemas),
        "per_soort": {s: sum(1 for g in schemas.values() if g.get("soort") == s) for s in SOORTEN},
        "objecttypen": len(objecttypen),
        "attribuutsoorten": len(attributen),
        "per_bron": per_bron,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--binding", default=None, help="het bindingsbestand")
    parser.add_argument("--model", default=None, help="het informatiemodel")
    parser.add_argument("--kort", action="store_true", help="alleen de tellingen en de bevindingen")
    args = parser.parse_args(argv)

    binding_pad = pathlib.Path(args.binding) if args.binding else WORTEL / BINDING
    model_pad = pathlib.Path(args.model) if args.model else WORTEL / MODEL
    for pad in (binding_pad, model_pad):
        if not pad.is_file():
            print(f"Het bestand {pad} bestaat niet.", file=sys.stderr)
            return 2
    try:
        binding = json.loads(binding_pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError as fout:
        print(f"{binding_pad.name} is geen geldige json: {fout}", file=sys.stderr)
        return 2

    objecttypen = {o["naam"] for o in json.loads(model_pad.read_text(encoding="utf-8"))["objecttypen"]}
    schemas = schemabestanden([WORTEL / m for m in SCHEMAMAPPEN])
    bevindingen = controleer(binding, objecttypen, schemas)

    t = tellingen(binding)
    soorten = ", ".join(f"{n} {s}" for s, n in t["per_soort"].items() if n)
    print(f"{t['schemas']} schema's ({soorten}), "
          f"{t['objecttypen']} objecttypen, {t['attribuutsoorten']} attribuutsoorten")
    if not args.kort and t["per_bron"]:
        for soort, n in sorted(t["per_bron"].items(), key=lambda p: -p[1]):
            print(f"  {soort:18} {n}")
    for b in bevindingen:
        print(f"  sluit niet aan: {b}")
    print(f"\n{len(bevindingen)} bindingen die niet aansluiten.")
    return 1 if bevindingen else 0


if __name__ == "__main__":
    sys.exit(main())
