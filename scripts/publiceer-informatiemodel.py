#!/usr/bin/env python3
"""Schrijft het informatiemodel en de begrippenlijst naar Public als release-variant.

Meta is de bron: het ArchiMate-model, de platen, begrippen.json en de generatoren staan
hier. Public draagt het releasepakket Informatie-en-gegevensmodellen; daar landen de drie
documenten als laag 1 (begrippen) en laag 2 (conceptueel informatiemodel), met de platen
in img/ en de JSON-bestanden ernaast.

Wat het script doet:

1. Verwijzingen omzetten. Elke verwijzing in de documenten staat in een expliciete tabel:
   naar een pad binnen Public, of naar meta gepind op een commit. Een verwijzing die niet
   in de tabel staat en niet binnen de pakketmap oplost, laat het script falen: liever
   een zichtbare fout dan een dode link in een gereleased document.
2. Platen hernoemen naar de Public-conventie (img/ naast het document, geen versie in de
   bestandsnaam).
3. Controleren dat de brug naar het logisch gegevensmodel klopt: elke entiteit in de
   brugtabel bestaat in logisch-gegevensmodel.md van Public, elk objecttype in
   informatiemodel.json.
4. Controleren dat elke definitie die naar het kaderscenario leerroute 1 verwijst daar
   letterlijk in staat, zodat de vindplaatsgarantie van de begrippenlijst de verhuizing
   overleeft.

Gebruik:
    python3 scripts/publiceer-informatiemodel.py --doel ../Public [--meta-commit <sha>]
    python3 scripts/publiceer-informatiemodel.py --doel ../Public --controleer

De meta-commit is de commit waarop de gepinde verwijzingen wijzen; standaard HEAD. Pin op
een commit die gepusht is, anders wijst de verwijzing in Public naar niets.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
MODELMAP = WORTEL / "architecture" / "model" / "informatiemodel"
BEGRIPPENMAP = WORTEL / "architecture" / "docs" / "specificatie" / "begrippen"
PAKKET = "Informatie-en-gegevensmodellen"
KADERSCENARIO = "../Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md"
ANKERTABEL = KADERSCENARIO + "#betrokken-informatie-bij-proces"
PUBLIC_DEV = "https://github.com/Npuls-OKx/Public/blob/dev/"
PUBLIC_DEV_TREE = "https://github.com/Npuls-OKx/Public/tree/dev/"
META_BLOB = "https://github.com/Npuls-OKx/meta/blob/{commit}/"
META_TREE = "https://github.com/Npuls-OKx/meta/tree/{commit}/"

# Bron in meta, doel in het pakket. Documenten worden herschreven, de rest gekopieerd.
DOCUMENTEN = {
    MODELMAP / "informatiemodel.md": "informatiemodel.md",
    MODELMAP / "informatiemodel-oeapi-mapping.md": "informatiemodel-oeapi-mapping.md",
    BEGRIPPENMAP / "begrippenlijst.md": "begrippen.md",
}
BESTANDEN = {
    MODELMAP / "OKx informatiemodel v0.1.jpg": "img/informatiemodel.jpg",
    MODELMAP / "OKx informatiemodel en mapping OEAPI v0.1.jpg": "img/informatiemodel-oeapi-mapping.jpg",
    BEGRIPPENMAP / "referentiekaders.json": "referentiekaders.json",
}
# informatiemodel.json en begrippen.json worden niet gekopieerd maar herschreven: de
# modelverwijzing gepind, de werkvoorraad en negeerlijst eruit, de vindplaatsen omgezet.
JSON_UITVOER = ("informatiemodel.json", "begrippen.json")

# Verwijzingen zoals ze in de meta-documenten staan, en waar ze in Public heen wijzen.
# {commit} wordt de gepinde meta-commit. Een pad met anchor houdt zijn anchor, tenzij
# het doel er zelf een draagt.
VERWIJZINGEN = {
    # informatiemodel.md en de mapping
    "../../docs/specificatie/begrippen/begrippenlijst.md": "begrippen.md",
    "../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md": ANKERTABEL,
    "../../docs/specificatie/student-keuze/keuze-requirements.md":
        META_BLOB + "architecture/docs/specificatie/student-keuze/keuze-requirements.md",
    "OKx informatiemodel v0.1.jpg": "img/informatiemodel.jpg",
    "OKx informatiemodel en mapping OEAPI v0.1.jpg": "img/informatiemodel-oeapi-mapping.jpg",
    PUBLIC_DEV + "Informatie-en-gegevensmodellen/logisch-gegevensmodel.md": "logisch-gegevensmodel.md",
    PUBLIC_DEV + "Informatie-en-gegevensmodellen/schemas/result-structure.json": "schemas/result-structure.json",
    PUBLIC_DEV_TREE + "Informatie-en-gegevensmodellen/schemas": "schemas/",
    PUBLIC_DEV_TREE + "Informatie-en-gegevensmodellen": "logisch-gegevensmodel.md",
    PUBLIC_DEV + "Koppelvlakspecificaties/uitgangspunten.md": "../Koppelvlakspecificaties/uitgangspunten.md",
    PUBLIC_DEV_TREE + "Koppelvlakspecificaties": "../Koppelvlakspecificaties/README.md",
    # begrippenlijst.md
    "../../../model/informatiemodel/informatiemodel.md": "informatiemodel.md",
    "../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md": KADERSCENARIO,
    "../leerroute-uitwerking/doc/begrippenkader.md": ANKERTABEL,
    "begrippen-extractie.json":
        META_BLOB + "architecture/docs/specificatie/begrippen/begrippen-extractie.json",
    "../../definitie_mapping_MORA_OEAPI_excel/":
        META_TREE + "architecture/docs/definitie_mapping_MORA_OEAPI_excel/",
}
# Een ADR-verwijzing naar Public dev wordt relatief; het bestand zelf blijft gelijk.
ADR_PREFIX = PUBLIC_DEV + "Referentiemateriaal/adr/"

# Linkteksten die de meta-bestandsnaam noemen krijgen de Public-naam.
LINKTEKSTEN = {"leerroute-uitwerking-lr1.md": "leerroute-1-regulier.md",
               "Begrippenkader leerroute-uitwerking": "Ankertabel kaderscenario leerroute 1"}

# Zinnen die alleen in meta kloppen. Per document: (meta-tekst, Public-tekst). Elke
# meta-tekst moet voorkomen, anders is het brondocument veranderd en faalt het script:
# liever dat dan een statuszin of een verkeerd perspectief in een gereleased document.
# Statuszinnen vervallen: U10 van de koppelvlakspecificatie laat geen statusaanduiding
# in de inhoud toe; de status staat in de pull request en de git-historie.
TEKSTEN = {
    "informatiemodel.md": [
        (" Versie v0.1, concept; ter bekrachtiging door de kerngroep techniek.", ""),
        (" in Public (MIM-niveau 3) zet", " (MIM-niveau 3) zet"),
        ("het [logisch gegevensmodel](logisch-gegevensmodel.md) in Public; de", "het [logisch gegevensmodel](logisch-gegevensmodel.md) in dit pakket; de"),
        ("gegenereerd uit `model.archimate`", "gegenereerd uit het ArchiMate-model in de meta-repository"),
    ],
    "informatiemodel-oeapi-mapping.md": [
        (" Versie v0.1, concept; de oordelen per objecttype zijn voorlopig tot de kerngroep techniek ze bekrachtigt.", ""),
        ("](logisch-gegevensmodel.md) in Public.", "](logisch-gegevensmodel.md) in dit pakket."),
        ("ligt bij de kerngroep techniek", "ligt bij de kerngroep techniek van OKx, het technisch overleg met instellingen en leveranciers"),
        ("gegenereerd uit `model.archimate`", "gegenereerd uit het ArchiMate-model in de meta-repository"),
    ],
    "begrippen.md": [
        ("Versie v0.2, concept. De kaders zijn geraadpleegd op 2026-09-14.", "De kaders zijn geraadpleegd op 14 september 2026."),
        ("Elke term tussen backquotes in meta en Public, met vindplaatsen", "Elke term tussen backquotes in de meta-repository en in dit repository, met vindplaatsen"),
    ],
}
# Sleutels in begrippen.json die bij het werkproces horen en niet mee naar Public gaan.
WERKPROCES_SLEUTELS = ("werkvoorraad", "negeerlijst", "indeling_negeerlijst")
VINDPLAATSEN = {
    "architecture/model/informatiemodel/informatiemodel.md": "informatiemodel.md",
    "architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md": KADERSCENARIO,
}

LINK = re.compile(r"(!?)\[([^\]]*)\]\(<?([^)>]+?)>?\)")
ENTITEIT = re.compile(r"^\s{4}([A-Z][A-Z0-9_]+)\s*\{", re.MULTILINE)
BACKQUOTE = re.compile(r"`([^`]+)`")


def meta_commit(opgegeven: str | None) -> str:
    if opgegeven:
        return opgegeven
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WORTEL, text=True).strip()


def herschrijf_verwijzing(doel: str, commit: str, pakketmap: Path, fouten: list, waar: str) -> str:
    """Eén verwijzingsdoel uit een meta-document naar zijn Public-vorm."""
    pad, _, anchor = doel.partition("#")
    nieuw = None
    if pad in VERWIJZINGEN:
        nieuw = VERWIJZINGEN[pad].format(commit=commit)
    elif pad.startswith(ADR_PREFIX):
        nieuw = "../Referentiemateriaal/adr/" + pad[len(ADR_PREFIX):]
    elif pad.startswith(("http://", "https://")):
        if "github.com/Npuls-OKx/" in pad:
            fouten.append(f"{waar}: verwijzing naar een OKx-repository zonder omzetting: {doel}")
        return doel
    elif pad == "":
        return doel  # anchor binnen hetzelfde document
    elif (pakketmap / pad).exists() or pad in DOCUMENTEN.values() or pad in BESTANDEN.values() or pad in JSON_UITVOER:
        return doel  # lost binnen het pakket op
    else:
        fouten.append(f"{waar}: onbekende verwijzing, niet in de tabel en niet in het pakket: {doel}")
        return doel
    if anchor and "#" not in nieuw:
        nieuw += "#" + anchor
    return nieuw


def herschrijf(inhoud: str, commit: str, pakketmap: Path, fouten: list, waar: str) -> str:
    def vervang(m):
        beeld, tekst, doel = m.group(1), m.group(2), m.group(3)
        nieuw = herschrijf_verwijzing(doel, commit, pakketmap, fouten, waar)
        haakjes = f"<{nieuw}>" if " " in nieuw else nieuw
        return f"{beeld}[{LINKTEKSTEN.get(tekst, tekst)}]({haakjes})"
    uit = LINK.sub(vervang, inhoud)
    for oud, nieuw in TEKSTEN.get(waar, []):
        if oud not in uit:
            fouten.append(f"{waar}: verwachte tekst niet gevonden, is de bron veranderd? {oud[:60]!r}")
        uit = uit.replace(oud, nieuw)
    return uit


def begrippen_voor_public(begrippen: dict, fouten: list) -> dict:
    """begrippen.json zonder werkvoorraad en negeerlijst, met vindplaatsen binnen Public."""
    uit = {k: v for k, v in begrippen.items() if k not in WERKPROCES_SLEUTELS}
    uit["begrippen"] = []
    def omgezet(v: str) -> str:
        if not v or v.startswith("http") or v.startswith("Npuls-OKx/"):
            return v
        pad, _, anchor = v.partition("#")
        if pad not in VINDPLAATSEN:
            fouten.append(f"begrippen.json: vindplaats zonder Public-tegenhanger: {v}")
            return v
        return VINDPLAATSEN[pad] + (f"#{anchor}" if anchor else "")

    for b in begrippen["begrippen"]:
        b = dict(b)
        b["vindplaats"] = omgezet(b.get("vindplaats"))
        for sleutel in ("afgeleid_van", "toelichting"):
            if isinstance(b.get(sleutel), dict) and b[sleutel].get("vindplaats"):
                b[sleutel] = dict(b[sleutel], vindplaats=omgezet(b[sleutel]["vindplaats"]))
        uit["begrippen"].append(b)
    return uit


def controleer_brug(informatiemodel_md: str, lgm: str, model: dict, fouten: list) -> None:
    """Elke entiteit in de brugtabel bestaat in het logisch gegevensmodel, elk objecttype
    in het informatiemodel."""
    kop = "## Naar het logisch gegevensmodel"
    if kop not in informatiemodel_md:
        fouten.append("informatiemodel.md: sectie 'Naar het logisch gegevensmodel' ontbreekt")
        return
    sectie = informatiemodel_md.split(kop, 1)[1].split("\n## ", 1)[0]
    entiteiten = set(ENTITEIT.findall(lgm))
    objecttypen = {o["naam"] for o in model["objecttypen"]}
    families = {"Onderwijsspecificatie", "Onderwijsaanbod", "Onderwijsverbintenis", "Onderwijsresultaat",
                "Resultaatstructuur", "Kwalificatiekader mbo", "Onderwijskundig kader instelling"}
    for regel in sectie.splitlines():
        if not regel.startswith("| `") or regel.startswith("| Entiteit"):
            continue
        cellen = [c.strip() for c in regel.strip("|").split("|")]
        for e in BACKQUOTE.findall(cellen[0]):
            if e not in entiteiten:
                fouten.append(f"brug: entiteit `{e}` staat niet in logisch-gegevensmodel.md")
        for o in BACKQUOTE.findall(cellen[1]):
            if o not in objecttypen and o not in families:
                fouten.append(f"brug: objecttype `{o}` staat niet in informatiemodel.json")
    ontbrekend = sorted(e for e in entiteiten if f"`{e}`" not in sectie)
    for e in ontbrekend:
        fouten.append(f"brug: entiteit `{e}` uit logisch-gegevensmodel.md staat niet in de brugtabel")


def controleer_vindplaatsen(begrippen: dict, kaderscenario: str, fouten: list) -> None:
    """Een definitie met vindplaats in de leerroute-uitwerking staat letterlijk in het
    kaderscenario van Public, want daar wijst de begrippenlijst straks heen."""
    plat = BACKQUOTE.sub(r"\1", kaderscenario)
    for b in begrippen["begrippen"]:
        v = b.get("vindplaats") or ""
        if "leerroute-uitwerking-lr1.md" not in v:
            continue
        definitie = BACKQUOTE.sub(r"\1", b["definitie"]).rstrip(".")
        if definitie not in plat:
            fouten.append(f"vindplaats: definitie van `{b['naam']}` staat niet in het kaderscenario leerroute 1")


def publiceer(doel: Path, commit: str, alleen_controle: bool) -> list:
    pakketmap = doel / PAKKET
    fouten: list = []
    if not (pakketmap / "release.json").exists():
        return [f"{pakketmap} is geen releasepakket (geen release.json)"]

    uitvoer = {}
    for bron, naam in DOCUMENTEN.items():
        inhoud = bron.read_text(encoding="utf-8")
        uitvoer[naam] = herschrijf(inhoud, commit, pakketmap, fouten, naam)

    model = json.loads((MODELMAP / "informatiemodel.json").read_text(encoding="utf-8"))
    lgm_pad = pakketmap / "logisch-gegevensmodel.md"
    if lgm_pad.exists():
        controleer_brug(uitvoer["informatiemodel.md"], lgm_pad.read_text(encoding="utf-8"), model, fouten)
    else:
        fouten.append(f"{lgm_pad} ontbreekt; is de worktree gestapeld op het pakket?")

    begrippen = json.loads((BEGRIPPENMAP / "begrippen.json").read_text(encoding="utf-8"))
    kaderscenario = (pakketmap / KADERSCENARIO).resolve()
    if kaderscenario.exists():
        controleer_vindplaatsen(begrippen, kaderscenario.read_text(encoding="utf-8"), fouten)
    else:
        fouten.append(f"{kaderscenario} ontbreekt")

    if fouten or alleen_controle:
        if alleen_controle and not fouten:
            for naam, inhoud in uitvoer.items():
                bestaand = pakketmap / naam
                if not bestaand.exists() or bestaand.read_text(encoding="utf-8") != inhoud:
                    fouten.append(f"{naam} in Public loopt uit de pas met de bron in meta")
        return fouten

    for naam, inhoud in uitvoer.items():
        (pakketmap / naam).write_text(inhoud, encoding="utf-8")
    for bron, naam in BESTANDEN.items():
        (pakketmap / naam).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(bron, pakketmap / naam)
    schrijf_json(pakketmap / "begrippen.json", begrippen_voor_public(begrippen, fouten))
    model["bron"]["model"] = META_BLOB.format(commit=commit) + "architecture/model/model.archimate"
    schrijf_json(pakketmap / "informatiemodel.json", model)
    return fouten


def schrijf_json(doel: Path, data: dict) -> None:
    tekst = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    json.loads(tekst)
    doel.write_text(tekst, encoding="utf-8")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--doel", required=True, type=Path, help="wortel van de Public-worktree")
    ap.add_argument("--meta-commit", help="commit waarop meta-verwijzingen worden gepind (standaard HEAD)")
    ap.add_argument("--controleer", action="store_true", help="schrijf niets; faal als Public afwijkt van meta")
    args = ap.parse_args(argv)

    commit = meta_commit(args.meta_commit)
    fouten = publiceer(args.doel.resolve(), commit, args.controleer)
    if fouten:
        print(f"{len(fouten)} problemen:", file=sys.stderr)
        for f in fouten:
            print(f"  {f}", file=sys.stderr)
        return 1
    print("OK" if args.controleer else f"geschreven naar {args.doel.resolve() / PAKKET}, meta gepind op {commit[:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
