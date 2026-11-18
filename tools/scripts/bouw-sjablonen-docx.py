#!/usr/bin/env python3
"""Bouwt de Word-sjablonen voor de adviesgroep uit de markdown-skeletten.

Markdown is de bron; de .docx is wat de adviesgroep opent. Beide staan in
versiebeheer, zodat niemand iets hoeft te bouwen om het sjabloon te kunnen
invullen, en een sjabloon dat achterloopt opnieuw te bouwen is.

    python3 tools/scripts/bouw-sjablonen-docx.py
    python3 tools/scripts/bouw-sjablonen-docx.py --controleer

Relateert aan: #554
"""

import argparse
import json
import pathlib
import shutil
import subprocess
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
MAP = WORTEL / "architecture/docs/sjablonen"
GEGENEREERD = MAP / "gegenereerd"
BRON = GEGENEREERD          # de skeletten komen uit maak-sjabloon-uit-document.py
CONFIG = MAP / "bron/sjablonen.json"
REFERENTIE = GEGENEREERD / "npuls-referentie.docx"


def sjablonen() -> dict[str, str]:
    """De vijf producten, met de bestandsnaam die de adviesgroep ziet."""
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    return {naam: cfg["bestand"] for naam, cfg in config.items()}


SJABLONEN = sjablonen()


def eis_pandoc() -> str:
    pad = shutil.which("pandoc")
    if not pad:
        raise SystemExit("pandoc ontbreekt; installeer hem in de dev-container "
                         "en nooit op de host")
    return pad


def bouw_een(naam: str, uit: pathlib.Path, referentie: pathlib.Path) -> None:
    bron = BRON / f"{naam}.md"
    if not bron.exists():
        raise SystemExit(
            f"het skelet {kort(bron)} bestaat niet; genereer het met "
            "tools/scripts/maak-sjabloon-uit-document.py")
    subprocess.run(
        [eis_pandoc(), str(bron), "--from", "gfm", "--to", "docx",
         "--reference-doc", str(referentie), "--output", str(uit)],
        check=True, capture_output=True,
    )


def kort(pad: pathlib.Path) -> str:
    """Het pad vanaf de wortel, en anders voluit; een pad in een testmap valt buiten."""
    try:
        return str(pad.relative_to(WORTEL))
    except ValueError:
        return str(pad)


def bouw(doel: pathlib.Path, referentie: pathlib.Path,
         controleer: bool = False) -> int:
    if not referentie.exists():
        raise SystemExit(
            f"de referentie {kort(referentie)} ontbreekt; "
            "bouw hem met tools/scripts/bouw-sjabloon-referentie.py")
    ontbreekt = []
    for naam, bestand in SJABLONEN.items():
        uit = doel / bestand
        if controleer:
            if not uit.exists():
                ontbreekt.append(bestand)
            continue
        bouw_een(naam, uit, referentie)
        print(f"  {bestand}  ({uit.stat().st_size} bytes)")
    if ontbreekt:
        print("deze sjablonen staan niet in versiebeheer:", file=sys.stderr)
        for b in ontbreekt:
            print(f"  {b}", file=sys.stderr)
        return 1
    if controleer:
        print(f"  alle {len(SJABLONEN)} sjablonen staan er")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--doel", type=pathlib.Path, default=MAP)
    p.add_argument("--referentie", type=pathlib.Path, default=REFERENTIE)
    p.add_argument("--controleer", action="store_true",
                   help="schrijft niets; faalt wanneer een sjabloon ontbreekt")
    a = p.parse_args(argv)
    return bouw(a.doel, a.referentie, a.controleer)


if __name__ == "__main__":
    sys.exit(main())
