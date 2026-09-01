#!/usr/bin/env python3
"""Houdt het platenmanifest van de presentaties actueel.

Een deck wordt beter van een bestaande architectuurplaat dan van een zelf
getekend diagram. Maar die platen leven verspreid over twee repositories, ze
hebben versies, en een afgeleide plaat kan op een oudere versie stoelen dan de
plaat die inmiddels leidend is. Dat zie je niet aan de bestandsnaam.

Dit script vergelijkt het manifest met wat er werkelijk staat en meldt:

  ONTBREEKT    het manifest noemt een bron die niet bestaat
  GEWIJZIGD    de bron is veranderd sinds hij in het manifest werd opgenomen
  NIEUWERE     er staat een hogere versie naast de versie in het manifest
  ONBEKEND     er staat een plaat die het manifest niet noemt
  KOPIE OUD    de kopie in presentaties/src/public/platen wijkt af van de bron
  KOPIE LOS    er ligt een kopie die geen enkele manifestregel opeist

Gebruik:
    python3 scripts/platen-inventariseren.py              # controleren
    python3 scripts/platen-inventariseren.py --bijwerken  # hashes bijwerken
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REPOS = {
    "Npuls-OKx/meta": Path("/workspaces/OKx/OKx-meta"),
    "Npuls-OKx/Public": Path("/workspaces/OKx/Public"),
}
MANIFEST = Path(__file__).resolve().parent.parent / "presentaties" / "platen.json"
# Slidev serveert alleen bestanden onder public/; een slide kan niet buiten het
# project wijzen. Een gebruikte plaat is dus altijd een kopie, en een kopie kan
# achterlopen op zijn bron zonder dat iemand het merkt.
KOPIEEN = MANIFEST.parent / "src" / "public" / "platen"
BEELD = {".jpg", ".jpeg", ".png", ".svg"}
# Mappen die geen bronmateriaal zijn: de kopieën in het presentatieproject zelf,
# afhankelijkheden en de huisstijl-assets.
NEGEER = ("node_modules", "presentaties/src/public", ".git", "/export/", ".agents/skills")


def hash_van(pad: Path) -> str:
    return hashlib.sha256(pad.read_bytes()).hexdigest()[:16]


def beelden_in(wortel: Path) -> list[Path]:
    uit = []
    for p in wortel.rglob("*"):
        if p.suffix.lower() not in BEELD or not p.is_file():
            continue
        rel = str(p.relative_to(wortel))
        if any(n.strip("/") in rel for n in NEGEER):
            continue
        uit.append(p)
    return sorted(uit)


VERSIE = re.compile(r"(?<![\d.])(\d+)\.(\d+)([a-z]?)(?![\d.])")


def patroon_naar_regex(patroon: str) -> re.Pattern[str]:
    """Vertaalt een glob naar een regex die vanaf de repositorywortel matcht.

    Niet PurePath.match gebruiken: die matcht van rechts af, waardoor een
    patroon als 'img/*' ook platen in elke geneste img-map zou afdekken. Zo
    verdwijnt materiaal ongemerkt uit de controle.

    '*' loopt niet over een mapgrens heen, '**' wel.
    """
    uit = []
    i = 0
    while i < len(patroon):
        if patroon.startswith("**/", i):
            uit.append("(?:.*/)?")   # nul of meer tussenliggende mappen
            i += 3
        elif patroon.startswith("**", i):
            uit.append(".*")
            i += 2
        elif patroon[i] == "*":
            uit.append("[^/]*")
            i += 1
        elif patroon[i] == "?":
            uit.append("[^/]")
            i += 1
        else:
            uit.append(re.escape(patroon[i]))
            i += 1
    return re.compile("".join(uit) + r"\Z")


def nieuwere_versie(pad: Path, wortel: Path) -> str | None:
    """Bestaat er naast dit pad een map met een hoger versienummer?

    De hoofdplaat leeft in mappen als '1.6' en '1.7'. Een manifest dat naar 1.6
    wijst terwijl 1.7 er staat, laat een verouderde plaat in een deck belanden.
    """
    for ouder in pad.parents:
        if ouder == wortel:
            break
        m = VERSIE.fullmatch(ouder.name)
        if not m:
            continue
        huidig = (int(m.group(1)), int(m.group(2)), m.group(3))
        hoger = []
        for zus in ouder.parent.iterdir():
            if not zus.is_dir():
                continue
            mz = VERSIE.fullmatch(zus.name)
            if mz:
                kandidaat = (int(mz.group(1)), int(mz.group(2)), mz.group(3))
                if kandidaat > huidig:
                    hoger.append(zus.name)
        if hoger:
            return f"{ouder.name} -> {max(hoger)}"
    return None


def controleer(manifest: dict) -> tuple[list[str], dict]:
    meldingen: list[str] = []
    genoemd: set[tuple[str, str]] = set()
    nieuwe_hashes: dict[str, str] = {}

    # Een plaat komt vaak in een familie: acht uitsneden van dezelfde
    # informatiestroom, vijf koppelvlakviews. Het manifest beschrijft de familie
    # een keer en dekt de rest met een patroon af, anders verdrinkt een echt
    # nieuwe plaat in de meldingen over varianten.
    patronen: list[tuple[str, re.Pattern[str]]] = []
    for plaat in manifest["platen"]:
        for p in plaat.get("varianten", []):
            patronen.append((plaat["bron"], patroon_naar_regex(p)))
    for regel in manifest.get("overslaan", []):
        patronen.append((regel["bron"], patroon_naar_regex(regel["patroon"])))

    def gedekt(repo: str, rel: str) -> bool:
        return any(r == repo and p.match(rel) for r, p in patronen)

    for plaat in manifest["platen"]:
        repo, rel = plaat["bron"], plaat["pad"]
        wortel = REPOS.get(repo)
        if wortel is None:
            meldingen.append(f"ONBEKENDE REPO  {plaat['naam']}: {repo}")
            continue
        pad = wortel / rel
        genoemd.add((repo, rel))

        if not pad.exists():
            meldingen.append(f"ONTBREEKT       {plaat['naam']}\n                {repo}: {rel}")
            continue

        h = hash_van(pad)
        nieuwe_hashes[plaat["naam"]] = h
        if plaat.get("hash") and plaat["hash"] != h:
            meldingen.append(
                f"GEWIJZIGD       {plaat['naam']}\n"
                f"                de bron is veranderd; controleer of de plaat nog klopt in lopende decks"
            )

        nieuwer = nieuwere_versie(pad, wortel)
        if nieuwer:
            meldingen.append(
                f"NIEUWERE        {plaat['naam']}\n"
                f"                er staat een hogere versie: {nieuwer}"
            )

    # De kopieën in public/platen tegen hun bron houden. Zonder deze controle
    # blijft een deck een oude plaat tonen terwijl de bron al bijgetekend is,
    # en meldt het manifest netjes dat alles klopt.
    opgeeist: set[str] = set()
    for plaat in manifest["platen"]:
        naam = plaat.get("kopie")
        if not naam:
            continue
        opgeeist.add(naam)
        kopie = KOPIEEN / naam
        bron = REPOS[plaat["bron"]] / plaat["pad"]
        if not kopie.exists():
            continue   # nog niet in gebruik; dat is geen fout
        if bron.exists() and hash_van(kopie) != hash_van(bron):
            meldingen.append(
                f"KOPIE OUD       {naam}\n"
                f"                wijkt af van {plaat['naam']}; opnieuw kopiëren uit {plaat['bron']}"
            )

    if KOPIEEN.is_dir():
        for kopie in sorted(KOPIEEN.iterdir()):
            if kopie.is_file() and kopie.name not in opgeeist:
                meldingen.append(
                    f"KOPIE LOS       {kopie.name}\n"
                    f"                geen manifestregel claimt deze kopie; veld 'kopie' invullen of het bestand weghalen"
                )

    for repo, wortel in REPOS.items():
        for pad in beelden_in(wortel):
            rel = str(pad.relative_to(wortel))
            if (repo, rel) not in genoemd and not gedekt(repo, rel):
                meldingen.append(
                    f"ONBEKEND        {repo}: {rel}\n"
                    f"                opnemen in platen[], of afdekken via 'varianten' of 'overslaan'"
                )

    return meldingen, nieuwe_hashes


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--bijwerken", action="store_true", help="hashes in het manifest bijwerken")
    a = p.parse_args()

    if not MANIFEST.exists():
        print(f"Geen manifest gevonden op {MANIFEST}")
        return 1
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    meldingen, hashes = controleer(manifest)

    if a.bijwerken:
        for plaat in manifest["platen"]:
            if plaat["naam"] in hashes:
                plaat["hash"] = hashes[plaat["naam"]]
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Hashes bijgewerkt voor {len(hashes)} platen.")
        return 0

    if not meldingen:
        print(f"SCHOON - {len(manifest['platen'])} platen in het manifest, alles actueel.")
        return 0

    for m in meldingen:
        print(m)
    onbekend = sum(1 for m in meldingen if m.startswith("ONBEKEND "))
    print(f"\n{len(meldingen)} melding(en), waarvan {onbekend} nog niet in het manifest.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
