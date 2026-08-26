#!/usr/bin/env python3
"""Testgevallen voor validate-boom.py (issue #171).

Elk geval draait het script tegen een verse kopie van de boom in een
tijdelijke map, met precies een geinjecteerde breuk, en toetst exitcode
en foutmelding. P-gevallen zijn positief (schoon), N-gevallen negatief
(moeten falen met de juiste melding), R-gevallen toetsen randgedrag.
Zo is per testgeval naloopbaar wat er gedraaid is en wat het resultaat
was (werkafspraak 26 augustus, issue #172).

Gebruik: python3 scripts/test-validate-boom.py
Exitcodes: 0 = alle gevallen geslaagd, 1 = minstens een geval gefaald.
"""
import os
import shutil
import subprocess
import sys
import tempfile

BRON = "architecture/docs/requirements"
SCRIPT = "scripts/validate-boom.py"
PUBLIC = os.path.join(os.getcwd(), "..", "Public")
PUBLIC_AANWEZIG = os.path.isdir(os.path.join(PUBLIC, ".git"))

# (id, omschrijving, bestand, oud, nieuw, verwachte exit, verwacht fragment)
GEVALLEN = [
    ("P1", "ongewijzigde boom is schoon", None, None, None, 0, "0 problemen"),
    ("N1", "verwijderd anker (story-0002)", "stories.md",
     '<a id="story-0002"></a>story-0002', "story-0002", 1, "zonder anker"),
    ("N2", "dubbel anker (story-0002 2x)", "stories.md",
     '<a id="story-0003"></a>', '<a id="story-0002"></a>', 1, "dubbel anker"),
    ("N3", "epic weg uit Van-doel-naar-epic (vooruit-richting)", "opdracht.md",
     "[epic-0003 Aanbod plannen en roosteren](epics.md#epic-0003); ", "", 1,
     "doel<->epic"),
    ("N4", "Draagt-bij-aan gewijzigd (terug-richting)", "epics.md",
     "[doel-0003](opdracht.md#doel-0003)", "[doel-0002](opdracht.md#doel-0002)",
     1, "doel<->epic"),
    ("N5", "Epic-cel wijst naar verkeerde epic", "features.md",
     "| [epic-0002](epics.md#epic-0002) | geen |",
     "| [epic-0003](epics.md#epic-0003) | geen |", 1, "Epic-cel"),
    ("N6", "story uit Stories-cel verwijderd", "features.md",
     "[story-0001](stories.md#story-0001)", "geen", 1, "feature<->story"),
    ("N7", "Features-cel linkt verkeerde sectiekop", "epics.md",
     "[features](features.md#gezamenlijke-taal-en-standaard)",
     "[features](features.md#aanbod-plannen-en-roosteren)", 1, "epic<->feature"),
    ("N8", "dode functionele-eis-link (0004 -> 9999)", "stories.md",
     "planning-en-roostering.md#functionele-eis-0004",
     "planning-en-roostering.md#functionele-eis-9999", 1, "zonder anker"),
    ("N9", "anker schendt id-conventie (feature-99)", "features.md",
     '<a id="feature-0009"></a>feature-0009', '<a id="feature-99"></a>feature-99',
     1, "volgt de id-conventie niet"),
]


def draai(boommap: str, public: str) -> tuple[int, str]:
    uit = subprocess.run([sys.executable, SCRIPT, boommap, public],
                         capture_output=True, text=True)
    return uit.returncode, uit.stdout + uit.stderr


def main() -> int:
    fouten = 0
    for gid, oms, bestand, oud, nieuw, verwacht_exit, fragment in GEVALLEN:
        if gid == "N8" and not PUBLIC_AANWEZIG:
            print(f"SKIP {gid}: {oms} (geen Public-checkout)")
            continue
        with tempfile.TemporaryDirectory() as tmp:
            kopie = os.path.join(tmp, "req")
            shutil.copytree(BRON, kopie)
            if bestand:
                pad = os.path.join(kopie, bestand)
                t = open(pad, encoding="utf-8").read()
                if oud not in t:
                    print(f"FAIL {gid}: {oms} - mutatiedoel niet gevonden")
                    fouten += 1
                    continue
                open(pad, "w", encoding="utf-8").write(t.replace(oud, nieuw, 1))
            code, uitvoer = draai(kopie, PUBLIC)
            ok = code == verwacht_exit and fragment in uitvoer
            regel = next((r for r in uitvoer.splitlines() if fragment in r), "")
            print(f"{'PASS' if ok else 'FAIL'} {gid}: {oms} -> exit {code} "
                  f"(verwacht {verwacht_exit}); {regel[:90]}")
            fouten += 0 if ok else 1

    # R1: pad niet gevonden -> exit 2
    code, uitvoer = draai("/pad/dat/niet/bestaat", PUBLIC)
    ok = code == 2
    print(f"{'PASS' if ok else 'FAIL'} R1: onbestaand pad -> exit {code} (verwacht 2)")
    fouten += 0 if ok else 1

    # R2: geen Public-checkout -> waarschuwing, geen fout
    with tempfile.TemporaryDirectory() as tmp:
        code, uitvoer = draai(BRON, os.path.join(tmp, "leeg"))
        ok = code == 0 and "waarschuwing" in uitvoer
        print(f"{'PASS' if ok else 'FAIL'} R2: geen Public-checkout -> exit {code} "
              f"(verwacht 0) met waarschuwing")
        fouten += 0 if ok else 1

    print(f"testgevallen: {len(GEVALLEN) + 2} totaal, {fouten} gefaald"
          + ("" if PUBLIC_AANWEZIG else " (N8 overgeslagen)"))
    return 1 if fouten else 0


if __name__ == "__main__":
    sys.exit(main())
