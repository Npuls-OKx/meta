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
import tempfile
import zipfile
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
MAP = WORTEL / "architecture/docs/sjablonen"
GEGENEREERD = MAP / "gegenereerd"
BRON = GEGENEREERD          # de skeletten komen uit maak-sjabloon-uit-document.py
CONFIG = MAP / "bron/sjablonen.json"
REFERENTIE = GEGENEREERD / "npuls-referentie.docx"


def titels() -> dict[str, str]:
    """De documenttitel per sjabloon; Word zet hem in de kop- en voettekst."""
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    return {naam: cfg["titel"] for naam, cfg in config.items()}


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


def bouw_een(naam: str, uit: pathlib.Path, referentie: pathlib.Path,
             titel: str = "") -> None:
    bron = BRON / f"{naam}.md"
    if not bron.exists():
        raise SystemExit(
            f"het skelet {kort(bron)} bestaat niet; genereer het met "
            "tools/scripts/maak-sjabloon-uit-document.py")
    # --resource-path wijst pandoc naar de beelden die de generator naast het
    # skelet heeft gezet, zodat zij in het Word-bestand zelf landen.
    klaar = subprocess.run(
        [eis_pandoc(), str(bron), "--from", "gfm+raw_attribute", "--to", "docx",
         "--reference-doc", str(referentie),
         "--resource-path", str(bron.parent),
         "--toc", "--toc-depth=3",
         "--metadata", f"title={titel}",
         "--metadata", "lang=nl-NL",
         "--metadata", "toc-title=Inhoudsopgave",
         "--output", str(uit)],
        capture_output=True, text=True,
    )
    if klaar.returncode:
        raise SystemExit(f"pandoc kon {kort(bron)} niet omzetten:\n"
                         f"{klaar.stderr.strip()}")
    if klaar.stderr.strip():
        for regel in klaar.stderr.strip().splitlines():
            print(f"    let op: {regel}")
    zet_titel_in_de_voettekst(uit, titel)


def zet_titel_in_de_voettekst(docx: pathlib.Path, titel: str) -> None:
    """Vult de plaatshouder die het Npuls-sjabloon in zijn voettekst draagt.

    Daar staat letterlijk [titel]; het is geen veld, dus Word vult hem nooit
    zelf en elk gebouwd sjabloon zou die plaatshouder blijven tonen.
    """
    if not titel:
        return
    with zipfile.ZipFile(docx) as z:
        onderdelen = {n: z.read(n) for n in z.namelist()}
    geraakt = False
    for naam, inhoud in onderdelen.items():
        if naam.startswith(("word/footer", "word/header")) and b"[titel]" in inhoud:
            onderdelen[naam] = inhoud.replace(b"[titel]", titel.encode("utf-8"))
            geraakt = True
    if not geraakt:
        return
    with tempfile.TemporaryDirectory() as tmp:
        tussen = pathlib.Path(tmp) / docx.name
        with zipfile.ZipFile(tussen, "w", zipfile.ZIP_DEFLATED) as z:
            for naam, inhoud in onderdelen.items():
                z.writestr(naam, inhoud)
        shutil.move(str(tussen), docx)


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
        bouw_een(naam, uit, referentie, titels().get(naam, ""))
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
