#!/usr/bin/env python3
"""Vergelijk twee versies van een ArchiMate-model en meld wat eruit verdween.

Waarom dit script bestaat: `validate-archimate.py` vangt een model dat intern niet meer
klopt, met views die naar niets verwijzen. Een regelgebaseerde merge die alleen invoegt
levert een bestand op dat wel klopt en toch minder draagt dan de versie ervoor. Dat is
precies wat in juli 2026 gebeurde: 276 elementdefinities verdwenen. Deze controle kijkt
daarom niet naar de staat van een bestand maar naar het verschil met de versie ervoor.

    python3 scripts/controleer-modelverlies.py <oud>.archimate <nieuw>.archimate
    python3 scripts/controleer-modelverlies.py --git <basis-ref> <pad>

Exitcode 0 = niets verdwenen, 1 = er ging iets weg.

Verdwijnen mag, zolang het met opzet gebeurt. Wie elementen weghaalt, zet `--toegestaan`
met het aantal dat mag verdwijnen; de controle meldt dan nog steeds wat weg is, maar
faalt pas boven dat aantal.
"""

import argparse
import pathlib
import re
import subprocess
import sys

RE_ELEMENT = re.compile(r'<(element|archimate:model)\b[^>]*\bid="([^"]+)"')
RE_NAAM = re.compile(r'\bname="([^"]*)"')


def elementen(inhoud: str) -> dict[str, str]:
    """De elementdefinities per id, met hun naam; diagramobjecten tellen niet mee.

    Alleen `<element>` draagt een concept. Een `<child>` of `<sourceConnection>` is een
    weergave daarvan op een view; die mag verdwijnen zonder dat er iets verloren gaat.
    """
    uit = {}
    for m in re.finditer(r"<element\b[^>]*>", inhoud):
        tag = m.group(0)
        mid = re.search(r'\bid="([^"]+)"', tag)
        if mid:
            naam = RE_NAAM.search(tag)
            uit[mid.group(1)] = naam.group(1) if naam else ""
    return uit


def uit_git(ref: str, pad: str) -> str:
    """Het bestand zoals het op die ref staat; lege tekst als het er niet was."""
    r = subprocess.run(["git", "show", f"{ref}:{pad}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def verschil(oud: str, nieuw: str) -> list[tuple[str, str]]:
    """De elementen die in oud stonden en in nieuw ontbreken, als (id, naam)."""
    a, b = elementen(oud), elementen(nieuw)
    return sorted(((i, a[i]) for i in a if i not in b), key=lambda p: p[1].lower())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("oud", help="het oude bestand, of de git-ref bij --git")
    ap.add_argument("nieuw", help="het nieuwe bestand, of het pad bij --git")
    ap.add_argument("--git", action="store_true",
                    help="lees het oude bestand uit git: <ref> <pad>")
    ap.add_argument("--toegestaan", type=int, default=0,
                    help="zoveel verdwenen elementen zijn met opzet; standaard geen")
    a = ap.parse_args()

    if a.git:
        oud, nieuw = uit_git(a.oud, a.nieuw), pathlib.Path(a.nieuw).read_text(encoding="utf-8")
        waar = f"{a.oud}:{a.nieuw}"
    else:
        oud = pathlib.Path(a.oud).read_text(encoding="utf-8")
        nieuw = pathlib.Path(a.nieuw).read_text(encoding="utf-8")
        waar = a.oud

    if not oud:
        print(f"SCHOON - geen eerdere versie op {waar}, niets te vergelijken.")
        return 0

    weg = verschil(oud, nieuw)
    totaal = len(elementen(oud))
    if not weg:
        print(f"SCHOON - alle {totaal} elementen uit {waar} staan er nog.")
        return 0

    print(f"{len(weg)} van de {totaal} elementen uit {waar} staan niet meer in het model:")
    for i, naam in weg[:40]:
        print(f"  {naam or '(zonder naam)'}  [{i}]")
    if len(weg) > 40:
        print(f"  ... en nog {len(weg) - 40}")
    if len(weg) <= a.toegestaan:
        print(f"Toegestaan: er mochten er {a.toegestaan} weg.")
        return 0
    print("\nVerdwenen elementen wijzen meestal op een regelgebaseerde merge; zie harde regel 1 "
          "en ADR 0010. Is het met opzet, draai dan met --toegestaan.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
