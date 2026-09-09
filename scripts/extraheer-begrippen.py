#!/usr/bin/env python3
"""Oogst elke term tussen backquotes uit de markdown van OKx-meta en Public.

De extractie gaat vooraf aan de interpretatie: dit script beslist niet wat een
begrip is, het levert per constructie de volledige lijst van wat er feitelijk
staat, met aantal voorkomens en vindplaatsen. De indeling in begrip, veldnaam
en ruis is een voorstel dat een mens bevestigt of verwerpt.

Gebruik:
    python3 scripts/extraheer-begrippen.py [--json <pad>]
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPOS = {
    "meta": Path("/workspaces/OKx/OKx-meta"),
    "public": Path("/workspaces/OKx/Public"),
}

UITGESLOTEN_MAPPEN = {
    ".git", "node_modules", ".venv", "venv", "dist", ".next", "build",
    ".obsidian", ".pytest_cache", "__pycache__",
}

# Fenced blocks (```/~~~) en HTML-commentaar tellen niet mee: daarin staat code,
# geen begrip.
FENCE = re.compile(r"^\s*(```|~~~)")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
# Inline code: een of meer backquotes, niet-gulzig, zonder aangrenzende backquote.
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
# Cardinaliteiten, pijlen en toekenningen zijn uitdrukkingen over begrippen,
# geen begrippen. Ze worden apart gezet zodat ze de lijst niet vervuilen.
EXPRESSIE = re.compile(r"\(\s*\d\s*\.\.|\u2192|->|\u21d2|=|\bt/m\b|\u2026")


def markdown_bestanden():
    for repo, wortel in REPOS.items():
        if not wortel.is_dir():
            print(f"waarschuwing: {wortel} bestaat niet, overgeslagen", file=sys.stderr)
            continue
        for pad in sorted(wortel.rglob("*.md")):
            if UITGESLOTEN_MAPPEN & set(pad.relative_to(wortel).parts):
                continue
            yield repo, wortel, pad


def regels_zonder_code(tekst):
    """Geef (regelnummer, regel) terug voor regels buiten fenced code blocks."""
    tekst = HTML_COMMENT.sub("", tekst)
    binnen = False
    for nr, regel in enumerate(tekst.splitlines(), start=1):
        if FENCE.match(regel):
            binnen = not binnen
            continue
        if not binnen:
            yield nr, regel


def normaliseer(term):
    """Sleutel waaronder schrijfwijzevarianten van hetzelfde begrip samenvallen."""
    kern = term.strip().strip(".,;:!?")
    kern = kern.replace("-", " ").replace("_", " ").replace("/", " / ")
    kern = re.sub(r"\s+", " ", kern)
    return kern.lower()


def classificeer(term, oeapi_schemas=frozenset(), oeapi_velden=frozenset()):
    """Voorstel voor de indeling. Een mens bevestigt of verwerpt."""
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
    if re.fullmatch(r"[#A-Fa-f0-9]{4,9}", kaal) and kaal.startswith("#"):
        return "ruis"
    if len(kaal) > 80:
        return "ruis"
    if re.search(r"[A-Za-z]", kaal):
        return "kandidaat-begrip"
    return "ruis"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json", default="architecture/docs/specificatie/begrippen/begrippen-extractie.json")
    p.add_argument("--vindplaatsen", type=int, default=6,
                   help="maximaal aantal bewaarde vindplaatsen per schrijfwijze")
    p.add_argument("--oeapi", default=None,
                   help="pad naar de OEAPI OpenAPI-specificatie (JSON); zonder dit "
                        "argument worden OEAPI-namen niet herkend")
    args = p.parse_args()

    oeapi_schemas, oeapi_velden = set(), set()
    if args.oeapi:
        spec = json.loads(Path(args.oeapi).read_text(encoding="utf-8"))
        schemas = spec.get("components", {}).get("schemas", {})
        oeapi_schemas = set(schemas)

        def loop(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "properties" and isinstance(v, dict):
                        oeapi_velden.update(v)
                    loop(v)
            elif isinstance(o, list):
                for x in o:
                    loop(x)

        loop(schemas)
        oeapi_velden -= oeapi_schemas

    # sleutel -> schrijfwijze -> {aantal, vindplaatsen}
    varianten = defaultdict(lambda: defaultdict(lambda: {"aantal": 0, "vindplaatsen": []}))
    bestanden = 0

    for repo, wortel, pad in markdown_bestanden():
        bestanden += 1
        try:
            tekst = pad.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = f"{repo}:{pad.relative_to(wortel)}"
        for nr, regel in regels_zonder_code(tekst):
            for m in INLINE.finditer(regel):
                term = m.group(2).strip()
                if not term:
                    continue
                sleutel = normaliseer(term)
                if not sleutel:
                    continue
                item = varianten[sleutel][term]
                item["aantal"] += 1
                if len(item["vindplaatsen"]) < args.vindplaatsen:
                    item["vindplaatsen"].append(f"{rel}:{nr}")

    termen = []
    for sleutel in sorted(varianten):
        schrijfwijzen = varianten[sleutel]
        totaal = sum(v["aantal"] for v in schrijfwijzen.values())
        gekozen = max(schrijfwijzen.items(), key=lambda kv: (kv[1]["aantal"], kv[0]))[0]
        termen.append({
            "sleutel": sleutel,
            "aantal": totaal,
            "indeling": classificeer(gekozen, oeapi_schemas, oeapi_velden),
            "schrijfwijzen": [
                {"schrijfwijze": s, "aantal": d["aantal"], "vindplaatsen": d["vindplaatsen"]}
                for s, d in sorted(schrijfwijzen.items(), key=lambda kv: -kv[1]["aantal"])
            ],
        })

    uitvoer = {
        "bron": {
            "repositories": {k: str(v) for k, v in REPOS.items()},
            "markdownbestanden": bestanden,
        },
        "termen": termen,
    }
    doel = Path(args.json)
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_text(json.dumps(uitvoer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    per_indeling = defaultdict(int)
    for t in termen:
        per_indeling[t["indeling"]] += 1
    meervoudig = [t for t in termen if len(t["schrijfwijzen"]) > 1]

    print(f"{bestanden} markdownbestanden gelezen")
    print(f"{len(termen)} termen na ontdubbeling van schrijfwijzen")
    for indeling, aantal in sorted(per_indeling.items(), key=lambda kv: -kv[1]):
        print(f"  {aantal:5d}  {indeling}")
    print(f"{len(meervoudig)} termen met meer dan een schrijfwijze")
    print(f"geschreven naar {doel}")


if __name__ == "__main__":
    main()
