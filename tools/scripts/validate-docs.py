#!/usr/bin/env python3
"""Deterministische voorcontrole voor markdown-documenten (OKx-meta).

Controleert per opgegeven bestand of map (recursief, alleen .md):
1. Relatieve markdown-links verwijzen naar bestaande bestanden.
2. ```json-blokken zijn parsebaar.
3. Code-fences zijn sluitend; mermaid-blokken bevatten geen puntkomma's
   (mermaid leest ; als statement-scheider en breekt op GitHub).

Dit is uitsluitend de mechanische voorcontrole uit de product-flow
(.agents/skills/okx-requirements-tester); het inhoudelijke oordeel blijft
bij de reviewende persona's.

Gebruik: python3 tools/scripts/validate-docs.py [pad ...]   (standaard: repo-root)
Exitcodes: 0 = schoon, 1 = problemen gevonden, 2 = pad niet gevonden.
"""
import json
import os
import urllib.parse
import re
import sys

# Slidev geeft een mermaid-blok opties mee achter de taal: ```mermaid {theme: 'base'}.
# Zonder die staart leest de controle de sluitende fence als een nieuwe opening.
FENCE = re.compile(r"^```(\w+)?(?:\s.*)?$")
MDLINK = re.compile(r"\]\((?!https?://|mailto:|#)([^)#\s]+?\.(?:md|json|py|png|jpg|jpeg))(?:#[^)]*)?\)")

# Een kop is een label en geen zin (.cursor/rules/schrijfstijl.mdc). Een kop die opent met een
# vraagwoord of met een persoonsvorm is een zin: hij vertelt in plaats van te benoemen. De controle
# vangt de openers die in de praktijk misgaan; subtielere gevallen blijven mensenwerk.
KOP = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
VRAAGWOORD = re.compile(r"^(wat|hoe|waarom|wanneer|waar|wie|welke)\b", re.I)
PERSOONSVORM = re.compile(r"^(dit|dat|deze|die|er|het|zo)\s+(is|zijn|staat|staan|hoort|horen|werkt|werken|gaat|gaan|komt|komen|doet|doen|heeft|hebben)\b", re.I)


# De kopcontrole geldt voor de pagina's waar een lezer binnenkomt. De skills, de templates en het
# oudere materiaal dragen nog zinkoppen; die gaan mee zodra dat materiaal wordt herzien.
LEZERSPAGINAS = ("README.md", "project/leesroute.md", "project/context.md",
                 "project/historie.md", "project/status.md", "project/README.md")


def kopprobleem(tekst: str) -> str | None:
    """De reden waarom een kop een zin is, of None als hij een label is."""
    kaal = re.sub(r"^\s*\d+(\.\d+)*\.?\s+", "", tekst).strip()
    kaal = re.sub(r"[`*_\[\]]", "", kaal)
    if VRAAGWOORD.match(kaal):
        return "opent met een vraagwoord"
    if PERSOONSVORM.match(kaal):
        return "opent met een persoonsvorm"
    return None


def check_file(path: str) -> list[str]:
    problems = []
    text = open(path, encoding="utf-8").read()
    base = os.path.dirname(path) or "."

    lang = None
    body: list[str] = []
    for nr, line in enumerate(text.splitlines(), 1):
        m = FENCE.match(line)
        if m and lang is None:
            lang, body = m.group(1) or "", []
            continue
        if line.strip() == "```" and lang is not None:
            if lang == "json":
                # Een fragment met een beletselteken is bewust ingekort en hoort niet te parsen.
                ingekort = any(r.strip() in {"\u2026", "..."} or r.strip().endswith("\u2026") for r in body)
                if not ingekort:
                    try:
                        json.loads("\n".join(body))
                    except json.JSONDecodeError as e:
                        problems.append(f"{path}:{nr}: json-blok niet parsebaar: {e}")
            lang = None
            continue
        if lang is not None:
            body.append(line)
            if lang == "mermaid" and ";" in line:
                problems.append(f"{path}:{nr}: puntkomma in mermaid (breekt rendering)")
        else:
            km = KOP.match(line)
            if km and os.path.normpath(path) in LEZERSPAGINAS:
                reden = kopprobleem(km.group(2))
                if reden:
                    problems.append(f"{path}:{nr}: kop {km.group(2)!r} {reden}; een kop is een label")
            for lm in MDLINK.finditer(line):
                # een pad met spaties staat in markdown met procentcodes; zonder decoderen
                # meldt de controle een bestand als dood terwijl het er gewoon staat
                target = os.path.normpath(os.path.join(base, urllib.parse.unquote(lm.group(1))))
                if not os.path.exists(target):
                    problems.append(f"{path}:{nr}: dode link: {lm.group(1)}")
    if lang is not None:
        problems.append(f"{path}: code-fence niet gesloten (```{lang})")
    return problems

def collect(paths: list[str]) -> list[str]:
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
                files += [os.path.join(root, n) for n in names if n.endswith(".md")]
        elif os.path.isfile(p):
            files.append(p)
        else:
            print(f"pad niet gevonden: {p}", file=sys.stderr)
            sys.exit(2)
    return sorted(set(files))

def main() -> int:
    paths = sys.argv[1:] or ["."]
    problems = []
    files = collect(paths)
    for f in files:
        problems += check_file(f)
    for p in problems:
        print(p)
    print(f"{len(files)} bestanden gecontroleerd, {len(problems)} problemen.")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
