#!/usr/bin/env python3
"""Valideer de integriteit van een Archi (.archimate) modelbestand.

Een .archimate is een XML-boom waarin views via ID's verwijzen naar elementen en
relaties elders in het bestand. Een regelgebaseerde merge (git of met de hand) kan
elementen laten wegvallen terwijl de views blijven staan. Het bestand blijft dan
geldige XML, maar de views verwijzen naar niets meer -- Archi laat die objecten
stilzwijgend vallen bij de eerstvolgende save, waarna het verlies definitief is.

Deze check vangt dat. Zie ADR 0010 (https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0010-archimatemodel-werkafspraken.md).

Gebruik:
    python3 scripts/validate-archimate.py architecture/model/model.archimate

Exitcode 0 = schoon, 1 = probleem gevonden.
"""

import argparse
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter

# Definities: elk object dat een id="..." draagt.
RE_ID = re.compile(r'\bid="([^"]+)"')
# Verwijzingen vanuit view-objecten naar model-elementen/relaties.
RE_REF = re.compile(r'archimate(?:Element|Relationship)="([^"]+)"')
# Views (diagrammen), om per view te kunnen rapporteren.
RE_VIEW = re.compile(
    r'<element[^>]*xsi:type="archimate:ArchimateDiagramModel"[^>]*name="([^"]*)"'
)


def validate(path: pathlib.Path) -> int:
    raw = path.read_text(encoding="utf-8", errors="replace")

    problems = []

    # 1. Welgevormde XML?
    try:
        ET.fromstring(raw)
        xml_ok = True
    except ET.ParseError as exc:
        xml_ok = False
        problems.append(f"XML is niet welgevormd: {exc}")

    ids = RE_ID.findall(raw)
    id_set = set(ids)
    refs = RE_REF.findall(raw)

    # 2. Dubbele id's -- Archi gaat hier onvoorspelbaar mee om.
    duplicates = [i for i, n in Counter(ids).items() if n > 1]
    if duplicates:
        problems.append(f"{len(duplicates)} dubbele id's")

    # 3. Dangling references: view verwijst naar een element dat niet bestaat.
    dangling = [r for r in refs if r not in id_set]
    if dangling:
        problems.append(f"{len(dangling)} dode referenties ({len(set(dangling))} uniek)")

    views = RE_VIEW.findall(raw)

    print(f"Bestand      : {path}")
    print(f"Grootte      : {path.stat().st_size / 1048576:.1f} MB")
    print(f"XML          : {'welgevormd' if xml_ok else 'STUK'}")
    print(f"Objecten     : {len(id_set)} unieke id's")
    print(f"Views        : {len(views)}")
    print(f"Verwijzingen : {len(refs)}")
    print(f"Dubbele id's : {len(duplicates)}")
    print(f"Dode refs    : {len(dangling)}")

    if dangling:
        # Per view rapporteren: welke views zijn beschadigd en hoe erg?
        per_view = []
        # Splits op view-grens zodat we refs aan de juiste view kunnen toewijzen.
        chunks = re.split(
            r'(?=<element[^>]*xsi:type="archimate:ArchimateDiagramModel")', raw
        )
        for chunk in chunks:
            m = RE_VIEW.search(chunk)
            if not m:
                continue
            crefs = RE_REF.findall(chunk)
            cbad = [r for r in crefs if r not in id_set]
            if cbad:
                per_view.append((len(cbad), len(crefs), m.group(1)))
        per_view.sort(reverse=True)

        print(f"\nBeschadigde views ({len(per_view)}):")
        print(f"  {'DOOD':>5} {'TOTAAL':>7}  VIEW")
        for bad, total, name in per_view:
            pct = 100 * bad / total if total else 0
            print(f"  {bad:>5} {total:>7}  {name}  ({pct:.0f}% dood)")

    if problems:
        print("\nNIET SCHOON:")
        for p in problems:
            print(f"  - {p}")
        print(
            "\nCommit dit model NIET. Een .archimate mag nooit regelgebaseerd worden\n"
            "gemerged: kies bij een conflict een kant wholesale en breng de andere kant\n"
            "terug via Archi (File > Import > Another model into the selected model).\n"
            "Zie https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0010-archimatemodel-werkafspraken.md"
        )
        return 1

    print("\nSCHOON - geen dode referenties, geen dubbele id's, welgevormde XML.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "model",
        nargs="?",
        default="architecture/model/model.archimate",
        type=pathlib.Path,
        help="pad naar het .archimate bestand",
    )
    args = ap.parse_args()

    if not args.model.is_file():
        print(f"Niet gevonden: {args.model}", file=sys.stderr)
        return 2

    return validate(args.model)


if __name__ == "__main__":
    sys.exit(main())
