#!/usr/bin/env python3
"""Oogst elke term tussen backquotes uit de markdown van OKx-meta en Public.

Het script levert per schrijfwijze wat er in de markdown staat, met aantal
voorkomens en vindplaatsen. Wat daarvan een begrip is, bepaalt een mens: de
indeling in begrip, veldnaam, pad, commando, uitdrukking en ruis is een voorstel.

De map met de begrippenlijst zelf blijft buiten de oogst. Anders zou elk begrip
zichzelf bewijzen zodra het in de lijst staat.

Gebruik:
    python3 scripts/extraheer-begrippen.py [--oeapi <pad naar de OpenAPI-JSON>]
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
REPOS = {
    "meta": WORTEL,
    "public": WORTEL.parent / "Public",
}
UITVOER = "architecture/docs/specificatie/begrippen/begrippen-extractie.json"

# Paden binnen een repository die niet meetellen, als voorvoegsel.
UITGESLOTEN_PADEN = ("architecture/docs/specificatie/begrippen",)
UITGESLOTEN_MAPPEN = {
    ".git", "node_modules", ".venv", "venv", "dist", ".next", "build",
    ".obsidian", ".pytest_cache", "__pycache__",
}

# Afgebakende codeblokken (fenced code blocks) en HTML-commentaar bevatten code,
# geen begrip.
FENCE = re.compile(r"^\s*(```|~~~)")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
# Code in de regel (inline code): een of meer backquotes, niet-gulzig.
INLINE = re.compile(r"(?<!`)(`+)(?!`)([^\n]+?)(?<!`)\1(?!`)")

PAD_ACHTERVOEGSELS = (
    ".md", ".json", ".py", ".yml", ".yaml", ".archimate", ".mdc", ".jpg",
    ".png", ".svg", ".html", ".css", ".ts", ".js", ".sh", ".txt", ".pptx",
    ".pdf", ".xml", ".csv",
)
COMMANDO_STARTS = (
    "python3", "python", "npx", "npm", "git ", "gh ", "cd ", "ls ", "make ",
    "./", "pip ", "docker", "soffice", "bash", "grep", "sed ", "curl",
)
HTTP_STARTS = ("GET ", "POST ", "PUT ", "PATCH ", "DELETE ", "HEAD ")
# Cardinaliteiten, pijlen en toekenningen zijn uitdrukkingen over begrippen.
EXPRESSIE = re.compile(r"\(\s*\d\s*\.\.|→|->|⇒|=|\bt/m\b|…")


def markdown_bestanden(repos, uitgesloten_paden=UITGESLOTEN_PADEN):
    for repo, wortel in sorted(repos.items()):
        if not Path(wortel).is_dir():
            print(f"waarschuwing: {wortel} bestaat niet, overgeslagen", file=sys.stderr)
            continue
        for pad in sorted(Path(wortel).rglob("*.md")):
            rel = pad.relative_to(wortel)
            if UITGESLOTEN_MAPPEN & set(rel.parts):
                continue
            if any(rel.as_posix().startswith(p) for p in uitgesloten_paden):
                continue
            yield repo, Path(wortel), pad


def regels_zonder_code(tekst):
    """Geef (regelnummer, regel) voor regels buiten afgebakende codeblokken."""
    tekst = HTML_COMMENT.sub("", tekst)
    binnen = False
    for nr, regel in enumerate(tekst.splitlines(), start=1):
        if FENCE.match(regel):
            binnen = not binnen
            continue
        if not binnen:
            yield nr, regel


def normaliseer(term):
    """Sleutel waaronder schrijfwijzevarianten van hetzelfde begrip samenvallen.

    Koppeltekens, lage streepjes en spaties tellen niet mee, zodat
    'Onderwijseenheid-specificatie', 'Onderwijseenheid specificatie' en
    'onderwijseenheidspecificatie' dezelfde sleutel krijgen.
    """
    kern = term.strip().strip(".,;:!?")
    kern = kern.replace("-", " ").replace("_", " ").replace("/", " / ")
    kern = re.sub(r"\s+", "", kern)
    return kern.lower()


def classificeer(term, oeapi_schemas=frozenset(), oeapi_velden=frozenset()):
    """Voorstel voor de indeling."""
    kaal = term.strip()
    if not kaal:
        return "leeg"
    if kaal in oeapi_schemas:
        return "oeapi-schema"
    if kaal in oeapi_velden:
        return "oeapi-veld"
    if kaal.startswith(HTTP_STARTS) or EXPRESSIE.search(kaal):
        return "expressie"
    if kaal.startswith(COMMANDO_STARTS) or " --" in kaal or kaal.startswith("-"):
        return "commando"
    if "/" in kaal and " " not in kaal:
        return "pad"
    if kaal.lower().endswith(PAD_ACHTERVOEGSELS):
        return "pad"
    if re.fullmatch(r"[A-Za-z0-9_]*_[A-Za-z0-9_]*", kaal):
        return "veldnaam"
    if re.fullmatch(r"[a-z]+([A-Z][A-Za-z0-9]*)+", kaal):
        return "veldnaam"
    if re.fullmatch(r"[A-Z][A-Za-z0-9]*", kaal) and re.search(r"[a-z][A-Z]", kaal):
        return "veldnaam"
    if re.fullmatch(r"\d[\d.\-]*", kaal):
        return "getal"
    if re.fullmatch(r"#[A-Fa-f0-9]{3,8}", kaal):
        return "ruis"
    if len(kaal) > 80:
        return "ruis"
    if re.search(r"[A-Za-z]", kaal):
        return "kandidaat-begrip"
    return "ruis"


def oeapi_namen(pad):
    """Schema- en veldnamen uit de OEAPI OpenAPI-specificatie."""
    spec = json.loads(Path(pad).read_text(encoding="utf-8"))
    schemas = spec.get("components", {}).get("schemas", {})
    velden = set()

    def loop(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "properties" and isinstance(v, dict):
                    velden.update(v)
                loop(v)
        elif isinstance(o, list):
            for x in o:
                loop(x)

    loop(schemas)
    return set(schemas), velden - set(schemas)


def extraheer(repos, oeapi_schemas=frozenset(), oeapi_velden=frozenset(),
              max_vindplaatsen=6, uitgesloten_paden=UITGESLOTEN_PADEN):
    varianten = defaultdict(lambda: defaultdict(lambda: {"aantal": 0, "vindplaatsen": []}))
    bestanden = 0
    weggelaten = 0
    for repo, wortel, pad in markdown_bestanden(repos, uitgesloten_paden):
        bestanden += 1
        try:
            tekst = pad.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = f"{repo}:{pad.relative_to(wortel)}"
        for nr, regel in regels_zonder_code(tekst):
            for m in INLINE.finditer(regel):
                term = m.group(2).strip()
                sleutel = normaliseer(term) if term else ""
                if not sleutel:
                    continue
                item = varianten[sleutel][term]
                item["aantal"] += 1
                if len(item["vindplaatsen"]) < max_vindplaatsen:
                    item["vindplaatsen"].append(f"{rel}:{nr}")
                else:
                    weggelaten += 1

    termen = []
    for sleutel in sorted(varianten):
        schrijfwijzen = varianten[sleutel]
        gekozen = max(schrijfwijzen.items(), key=lambda kv: (kv[1]["aantal"], kv[0]))[0]
        termen.append({
            "sleutel": sleutel,
            "aantal": sum(v["aantal"] for v in schrijfwijzen.values()),
            "indeling": classificeer(gekozen, oeapi_schemas, oeapi_velden),
            "schrijfwijzen": [
                {"schrijfwijze": s, "aantal": d["aantal"], "vindplaatsen": d["vindplaatsen"]}
                for s, d in sorted(schrijfwijzen.items(), key=lambda kv: -kv[1]["aantal"])
            ],
        })
    return termen, bestanden, weggelaten


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json", default=UITVOER)
    p.add_argument("--vindplaatsen", type=int, default=6,
                   help="maximaal aantal bewaarde vindplaatsen per schrijfwijze")
    p.add_argument("--oeapi", default=None,
                   help="pad naar de OEAPI OpenAPI-specificatie (JSON); zonder dit "
                        "argument worden OEAPI-namen niet herkend")
    args = p.parse_args()

    schemas, velden = (oeapi_namen(args.oeapi) if args.oeapi else (set(), set()))
    termen, bestanden, weggelaten = extraheer(
        REPOS, schemas, velden, args.vindplaatsen)

    uitvoer = {
        "bron": {
            "repositories": {k: str(v) for k, v in REPOS.items()},
            "uitgesloten_paden": list(UITGESLOTEN_PADEN),
            "markdownbestanden": bestanden,
            "vindplaatsen_per_schrijfwijze": args.vindplaatsen,
            "vindplaatsen_weggelaten": weggelaten,
            "oeapi_specificatie": args.oeapi,
            "oeapi_schemas": len(schemas),
            "oeapi_velden": len(velden),
            "commando": ("python3 scripts/extraheer-begrippen.py"
                         + (f" --oeapi {args.oeapi}" if args.oeapi else "")),
        },
        "termen": termen,
    }
    doel = Path(args.json)
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_text(json.dumps(uitvoer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    per_indeling = defaultdict(int)
    for t in termen:
        per_indeling[t["indeling"]] += 1
    meervoudig = sum(1 for t in termen if len(t["schrijfwijzen"]) > 1)

    print(f"{bestanden} markdownbestanden gelezen")
    print(f"{len(termen)} termen na ontdubbeling van schrijfwijzen")
    for indeling, n in sorted(per_indeling.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {indeling}")
    print(f"{meervoudig} termen met meer dan één schrijfwijze")
    print(f"{weggelaten} vindplaatsen niet bewaard door de cap van {args.vindplaatsen}")
    print(f"geschreven naar {doel}")


if __name__ == "__main__":
    main()
