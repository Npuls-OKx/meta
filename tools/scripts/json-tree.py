#!/usr/bin/env python3
"""Genereert schema- en instantiebomen bij de JSON-payloads in de koppelingspecificaties.

De payloads gebruiken platte arrays met een zelfverwijzende ouder-pointer. Daardoor is
de boomstructuur in de JSON zelf onzichtbaar: je kunt hem alleen reconstrueren door
uuid's met de hand te matchen. Dit script rendert die boom voor, als ASCII in een
```text-blok tussen HTML-comment-markers, zodat de weergave leesbaar blijft op GitHub
en in een PDF-export.

Markers in het document:

    <!-- json-tree:begin kind=schema -->
    <!-- json-tree:begin kind=instance array=aanbodInstanties id=id
         parent=bovenliggendAanbodId label=naam type=aanbodType attrs=versie,status -->
    ...gegenereerde inhoud...
    <!-- json-tree:end -->

Voor kind=instance zijn array, id, parent en label verplicht; type en attrs optioneel.
Het schemablok wordt herkend aan de sleutel "$schema".

Exitcodes: 0 schoon, 1 probleem gevonden, 2 bestand niet gevonden.
"""

import argparse
import json
import pathlib
import re
import sys

BEGIN = re.compile(r"<!--\s*json-tree:begin\s+(?P<args>.*?)\s*-->", re.DOTALL)
EIND = "<!-- json-tree:end -->"
JSONBLOK = re.compile(r"```json\n(.*?)\n```", re.DOTALL)

KORT = 8  # aantal tekens van een uuid in de boom


def parse_args_marker(tekst):
    """Zet 'kind=instance array=x id=y' om in een dict."""
    return dict(deel.split("=", 1) for deel in tekst.split() if "=" in deel)


def json_blokken(inhoud):
    """Alle JSON-blokken uit een markdown-document, gesplitst in schema en voorbeelden.

    Voorbeelden dragen hun startpositie mee, zodat een marker het dichtstbijzijnde
    voorafgaande blok kan kiezen in plaats van simpelweg het eerste.
    """
    schema, voorbeelden = None, []
    for m in JSONBLOK.finditer(inhoud):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and "$schema" in data:
            schema = data
        else:
            voorbeelden.append((m.start(), data))
    return schema, voorbeelden


# --- instantieboom ------------------------------------------------------------------

def bouw_boom(objecten, id_veld, ouder_veld):
    """Geeft (kinderen-per-ouder, roots, problemen)."""
    per_id = {}
    problemen = []
    for o in objecten:
        sleutel = o.get(id_veld)
        if sleutel is None:
            problemen.append(f"object zonder {id_veld}: {list(o)[:3]}")
            continue
        if sleutel in per_id:
            problemen.append(f"dubbele {id_veld}: {sleutel}")
        per_id[sleutel] = o

    kinderen, roots = {}, []
    for o in objecten:
        ouder = o.get(ouder_veld)
        if ouder is None:
            roots.append(o)
        elif ouder not in per_id:
            problemen.append(f"dode verwijzing {ouder_veld}={ouder} op object {o.get(id_veld)}")
            roots.append(o)
        else:
            kinderen.setdefault(ouder, []).append(o)

    # cykels opsporen
    for o in objecten:
        gezien, huidig = set(), o
        while huidig is not None:
            sleutel = huidig.get(id_veld)
            if sleutel in gezien:
                problemen.append(f"cykel via {ouder_veld} rond object {sleutel}")
                break
            gezien.add(sleutel)
            huidig = per_id.get(huidig.get(ouder_veld))
    return kinderen, roots, problemen


def entiteitnaam(obj, type_veld, vast=None):
    if type_veld and obj.get(type_veld):
        return str(obj[type_veld]).upper()
    return (vast or "object").upper()


def render_knoop(obj, kinderen, opts, prefix, is_laatste, is_root, regels):
    id_veld, label_veld = opts["id"], opts["label"]
    type_veld = opts.get("type")
    attrs = [a for a in opts.get("attrs", "").split(",") if a]

    kort = str(obj.get(id_veld, ""))[:KORT]
    naam = entiteitnaam(obj, type_veld, opts.get("entity"))

    if is_root:
        tak, vervolg = "", ""
    else:
        tak = "`-- " if is_laatste else "+-- "
        vervolg = "    " if is_laatste else "|   "

    kop = f"{prefix}{tak}{naam}"
    regels.append(f"{kop.ljust(62)}{kort}")

    binnen = prefix + vervolg
    label = obj.get(label_veld)
    if label:
        regels.append(f"{binnen}= {label}")
    waarden = []
    for a in attrs:
        w = obj.get(a)
        if isinstance(w, dict):
            w = "{" + ", ".join(f"{k}: {v}" for k, v in w.items()) + "}"
        elif isinstance(w, list):
            w = f"[{len(w)}]" if w else None
        if w not in (None, ""):
            waarden.append(f"{a}: {w}")
    if waarden:
        regels.append(f"{binnen}  " + " | ".join(waarden))

    kids = kinderen.get(obj.get(id_veld), [])
    if kids:
        regels.append(f"{binnen}|")
    for i, kind in enumerate(kids):
        render_knoop(kind, kinderen, opts, binnen, i == len(kids) - 1, False, regels)


def render_instantieboom(data, opts):
    array = opts["array"]
    objecten = data.get(array)
    if not isinstance(objecten, list):
        return None, [f"array '{array}' niet gevonden of geen lijst"], {}

    kinderen, roots, problemen = bouw_boom(objecten, opts["id"], opts["parent"])
    regels = [f"{array}  ({len(objecten)} objecten, {len(roots)} root"
              f"{'s' if len(roots) != 1 else ''}, boom via {opts['parent']})", ""]
    for i, root in enumerate(roots):
        if i:
            regels.append("")
        render_knoop(root, kinderen, opts, "", True, True, regels)

    def diepte(obj, d=1):
        kids = kinderen.get(obj.get(opts["id"]), [])
        return max([diepte(k, d + 1) for k in kids], default=d)

    stats = {"objecten": len(objecten), "roots": len(roots),
             "diepte": max([diepte(r) for r in roots], default=0)}
    return "\n".join(regels), problemen, stats


# --- schemaboom ---------------------------------------------------------------------

def typenaam(schema, breedte=78):
    """Geeft het type als tekst. Enums geven hun waarden, desnoods over meerdere regels."""
    if "enum" in schema:
        regels, huidig = [], ""
        for w in (str(x) for x in schema["enum"]):
            kandidaat = f"{huidig} | {w}" if huidig else w
            if len(kandidaat) > breedte and huidig:
                regels.append(huidig)
                huidig = w
            else:
                huidig = kandidaat
        regels.append(huidig)
        return "\n".join(regels)
    t = schema.get("type")
    if isinstance(t, list):
        return " of ".join(t)
    if t == "string" and schema.get("format") == "uuid":
        return "uuid"
    return t or "any"


def render_eigenschappen(schema, prefix, regels):
    props = schema.get("properties", {})
    verplicht = set(schema.get("required", []))
    namen = list(props)
    for i, naam in enumerate(namen):
        deel = props[naam]
        laatste = i == len(namen) - 1
        tak = "`-- " if laatste else "+-- "
        vervolg = "    " if laatste else "|   "

        if deel.get("type") == "array":
            items = deel.get("items", {})
            label = f"{naam}[]"
            toel = "verplicht" if naam in verplicht else "optioneel"
            regels.append(f"{prefix}{tak}{label.ljust(34)}{toel}")
            if items.get("properties"):
                render_eigenschappen(items, prefix + vervolg, regels)
            elif items:
                regels.append(f"{prefix}{vervolg}  ({typenaam(items)})")
        elif deel.get("properties"):
            toel = "verplicht" if naam in verplicht else "optioneel"
            regels.append(f"{prefix}{tak}{naam.ljust(34)}{toel}, object")
            render_eigenschappen(deel, prefix + vervolg, regels)
        else:
            toel = typenaam(deel) + ("" if naam in verplicht else ", optioneel")
            kop, *vervolgregels = toel.split("\n")
            regels.append(f"{prefix}{tak}{naam.ljust(34)}{kop}")
            for extra in vervolgregels:
                regels.append(f"{prefix}{vervolg}{' ' * 34}{extra}")


def render_schemaboom(schema):
    if not schema:
        return None, ["geen JSON Schema-blok gevonden (verwacht een blok met \"$schema\")"]
    titel = schema.get("title", "payload")
    regels = [f"{titel}  ({schema.get('$comment', 'schema')})", "", "{root}"]
    render_eigenschappen(schema, "", regels)
    return "\n".join(regels), []


# --- markers verwerken --------------------------------------------------------------

def verwerk(pad, modus):
    p = pathlib.Path(pad)
    if not p.exists():
        print(f"Bestand niet gevonden: {p}", file=sys.stderr)
        return 2, None

    inhoud = p.read_text(encoding="utf-8")
    schema, voorbeelden = json_blokken(inhoud)
    problemen, meldingen, nieuw = [], [], inhoud
    verschoven = 0

    for m in list(BEGIN.finditer(inhoud)):
        opts = parse_args_marker(m.group("args"))
        soort = opts.get("kind", "instance")
        start = m.end()
        eind = inhoud.find(EIND, start)
        if eind == -1:
            problemen.append(f"marker zonder afsluitende {EIND}")
            continue

        if soort == "schema":
            blok, fout = render_schemaboom(schema)
            stats = {}
        else:
            ontbreekt = [k for k in ("array", "id", "parent", "label") if k not in opts]
            if ontbreekt:
                problemen.append(f"marker mist {', '.join(ontbreekt)}")
                continue
            kandidaten = [(pos, v) for pos, v in voorbeelden
                          if isinstance(v, dict) and isinstance(v.get(opts["array"]), list)]
            # het dichtstbijzijnde blok vóór de marker; anders het eerstvolgende erna
            ervoor = [k for k in kandidaten if k[0] < m.start()]
            bron = (ervoor[-1][1] if ervoor else kandidaten[0][1]) if kandidaten else None
            if bron is None:
                problemen.append(f"geen voorbeeldblok met array '{opts['array']}'")
                continue
            blok, fout, stats = render_instantieboom(bron, opts)

        problemen.extend(fout)
        if blok is None:
            continue
        if stats:
            meldingen.append(f"{opts.get('array', 'schema'):<28}: {stats['objecten']} objecten, "
                             f"{stats['roots']} root{'s' if stats['roots'] != 1 else ''}, "
                             f"diepte {stats['diepte']}")
        else:
            meldingen.append(f"{'schemaboom':<28}: gerenderd")

        vervanging = "\n```text\n" + blok + "\n```\n"
        oud = inhoud[start:eind]
        if modus == "check":
            if oud != vervanging:
                problemen.append(f"boom bij marker '{m.group('args')[:40]}' wijkt af van de JSON")
        elif modus == "write":
            a, b = start + verschoven, eind + verschoven
            nieuw = nieuw[:a] + vervanging + nieuw[b:]
            verschoven += len(vervanging) - len(oud)
        else:
            print(vervanging)

    if modus == "write" and nieuw != inhoud:
        p.write_text(nieuw, encoding="utf-8")

    # voorbeeld valideren tegen het schema
    if schema and voorbeelden:
        try:
            import jsonschema
        except ImportError:
            meldingen.append(f"{'schemavalidatie':<28}: OVERGESLAGEN, pakket jsonschema ontbreekt "
                             "(pip install -r .devcontainer/requirements.txt)")
        else:
            for i, (_, v) in enumerate(voorbeelden):
                try:
                    jsonschema.validate(v, schema)
                    meldingen.append(f"{'schemavalidatie':<28}: voorbeeld {i + 1} voldoet")
                except jsonschema.ValidationError as e:
                    pad_str = "/".join(str(x) for x in e.absolute_path) or "(root)"
                    problemen.append(f"voorbeeld {i + 1} voldoet niet aan het schema op {pad_str}: {e.message}")

    return (1 if problemen else 0), (meldingen, problemen)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("bestanden", nargs="+", type=pathlib.Path,
                    help="markdown-documenten met json-tree-markers")
    ap.add_argument("--write", action="store_true", help="bomen in het document bijwerken")
    ap.add_argument("--check", action="store_true", help="falen als een boom afwijkt van de JSON")
    args = ap.parse_args()

    modus = "write" if args.write else "check" if args.check else "print"
    hoogste, alle_problemen = 0, []

    for pad in args.bestanden:
        code, uitkomst = verwerk(pad, modus)
        hoogste = max(hoogste, code)
        if uitkomst is None:
            continue
        meldingen, problemen = uitkomst
        print(f"Bestand      : {pad}")
        for r in meldingen:
            print(f"  {r}")
        for r in problemen:
            print(f"  PROBLEEM: {r}")
            alle_problemen.append(f"{pad}: {r}")
        print()

    if hoogste == 2:
        return 2
    if alle_problemen:
        print(f"NIET SCHOON: {len(alle_problemen)} probleem(en) gevonden.")
        return 1
    print("SCHOON - bomen komen overeen met de JSON.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
