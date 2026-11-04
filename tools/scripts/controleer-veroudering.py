#!/usr/bin/env python3
"""Beweringen opsporen die stil verouderen: een plaatversie, een fase, een vervangen naam.

Waarom dit script bestaat: documenten verouderen zonder dat iemand het merkt. Bij de leesroute
van #415 wezen drie van de negen stappen naar materiaal met een uitspraak die niet meer klopte,
en het concept-plan voor die route verouderde binnen zijn eigen tekst op vier punten. Beide
keren viel dat bij toeval op, doordat een tegenlezer de bron ernaast legde.

Drie veroudergangen zijn machinaal te zien, en alle drie zijn ze werkelijk aangetroffen:

    plaatversie      een verwijzing naar een versie van de hoofdplaat die niet de hoogste is
    fasebewering     een zin over de fase of de stand van het project
    vervangen naam   een componentnaam die door een architectuurbesluit is vervangen

Dit script meldt en herstelt niets. Of een oude versie bewust wordt aangehaald is een
inhoudelijke vraag, en die beantwoordt een mens. Een document dat een oude stand bewust
vastlegt draagt daarom een uitzondering met de reden erbij:

    <!-- veroudering-uitzondering: dit verslag legt de stand van juni 2026 vast -->

Een uitzondering zonder reden telt niet; die wordt zelf gemeld.

    python3 tools/scripts/controleer-veroudering.py              de hele werkmap
    python3 tools/scripts/controleer-veroudering.py <pad> ...    losse bestanden of mappen

Het script leest alleen, draait zonder netwerk, en werkt in beide repositories: wat het niet
vindt slaat het over.
"""

import argparse
import json
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent
STROMEN = WORTEL / "architecture/model/informatiemodel/stromen.json"

# Mappen die per definitie een oude stand vastleggen; hun README zegt dat ook. Een uitzondering
# per bestand zou daar honderden regels opleveren zonder iets toe te voegen.
HISTORISCH = ("archief/", "architecture/meetings/", "architecture/agent-artifacts/",
              "presentaties/src/")

UITZONDERING = re.compile(r"<!--\s*veroudering-uitzondering:?(.*?)-->", re.I | re.S)

# Een versie van de hoofdplaat, zoals die in een zin wordt aangehaald.
PLAATVERSIE = re.compile(r"hoofdplaat[^.\n]{0,60}?v\s?(\d+\.\d+[a-z]?)", re.I)

# Zinswendingen die een stand van het project beweren. Uitbreidbaar: zet er een bij zodra je er
# een tegenkomt die verouderd bleek.
FASEBEWERINGEN = (
    "bevindt zich nu in de fase",
    "bevindt zich in de fase",
    "momenteel in de fase",
    "op dit moment in fase",
    "de huidige fase van het project",
    "het project bevindt zich",
    "we zitten nu in fase",
)

# Namen die een besluit heeft vervangen, met dat besluit erbij.
VERVANGEN = {
    "Student Kiest": "studentkeuzesysteem (SKS), vervangen in ADR 0005",
    "Student Kiest Systeem": "studentkeuzesysteem (SKS), vervangen in ADR 0005",
    "voorbeeldregels": "OKx modeldoorloop met doorloopstappen, hernoemd in meta#415",
}


def hoogste_plaatversie(stromen=STROMEN):
    """De versie die het model zelf draagt; die is de maat, niet een map of een bestandsnaam."""
    if not stromen.exists():
        return None
    view = json.loads(stromen.read_text(encoding="utf-8")).get("view", "")
    merk = re.search(r"v(\d+\.\d+[a-z]?)", view)
    return merk.group(1) if merk else None


def historisch(pad, wortel):
    rel = str(pad.relative_to(wortel)).replace("\\", "/")
    return any(rel.startswith(m) for m in HISTORISCH)


def uitzondering(tekst):
    """(draagt een uitzondering, reden). Een reden van niets telt niet als reden."""
    merk = UITZONDERING.search(tekst)
    if not merk:
        return False, None
    return True, " ".join(merk.group(1).split()) or None


def bevindingen_in(tekst, pad, hoogste):
    uit = []
    for nr, regel in enumerate(tekst.splitlines(), 1):
        for merk in PLAATVERSIE.finditer(regel):
            if hoogste and merk.group(1).lower() != hoogste.lower():
                uit.append((nr, f"verwijst naar hoofdplaat v{merk.group(1)} en de hoogste is v{hoogste}"))
        laag = regel.lower()
        for zin in FASEBEWERINGEN:
            if zin in laag:
                uit.append((nr, f"bewering over de stand van het project: {zin!r}"))
        for naam, besluit in VERVANGEN.items():
            if re.search(rf"\b{re.escape(naam)}\b", regel):
                uit.append((nr, f"vervangen naam {naam!r}: {besluit}"))
    return uit


NIET_GEGEVEN = object()


def controleer(paden, wortel=WORTEL, hoogste=NIET_GEGEVEN):
    # None betekent hier: er is geen hoogste versie bekend, dus die controle vervalt. Dat is iets
    # anders dan de versie niet meegeven, en daarom staat er een eigen waarde voor.
    hoogste = hoogste_plaatversie() if hoogste is NIET_GEGEVEN else hoogste
    meldingen, bekeken, overgeslagen = [], 0, 0
    bestanden = []
    for p in paden:
        p = pathlib.Path(p)
        bestanden += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    for pad in bestanden:
        try:
            rel = pad.relative_to(wortel)
        except ValueError:
            rel = pad
        if historisch(pad, wortel) if pad.is_absolute() else False:
            overgeslagen += 1
            continue
        tekst = pad.read_text(encoding="utf-8")
        draagt, reden = uitzondering(tekst)
        if draagt and not reden:
            meldingen.append(f"{rel}: een uitzondering zonder reden telt niet; zeg waarom deze "
                             f"bewering mag blijven staan")
            continue
        if draagt:
            overgeslagen += 1
            continue
        bekeken += 1
        for nr, wat in bevindingen_in(tekst, pad, hoogste):
            meldingen.append(f"{rel}:{nr}: {wat}")
    return meldingen, bekeken, overgeslagen


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("paden", nargs="*", default=[str(WORTEL)],
                   help="bestanden of mappen; standaard de hele werkmap")
    p.add_argument("--wortel", default=str(WORTEL))
    args = p.parse_args()
    meldingen, bekeken, overgeslagen = controleer(args.paden or [args.wortel],
                                                  pathlib.Path(args.wortel))
    for m in meldingen:
        print(m)
    hoogste = hoogste_plaatversie()
    print(f"{bekeken} bestanden gecontroleerd, {overgeslagen} overgeslagen, "
          f"{len(meldingen)} meldingen; hoogste hoofdplaat v{hoogste}")
    return 1 if meldingen else 0


if __name__ == "__main__":
    sys.exit(main())
