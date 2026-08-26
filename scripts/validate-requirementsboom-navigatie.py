#!/usr/bin/env python3
"""Navigatiecontrole van de requirementsboom (OKx-meta, issue #171).

Controleert de laagverwijzingen in architecture/docs/requirements/:
1. Ankerintegriteit en id-conventie: elke fragmentlink naar een boom-id
   resolvet naar een bestaand <a id>-anker; ankers zijn uniek; id's volgen
   de conventie (plat per soort, voluit, vier cijfers).
2. doel <-> epic: "Draagt bij aan" (epics.md) en "Van doel naar epic"
   (opdracht.md) beschrijven exact dezelfde relatie (set-gelijkheid).
3. epic <-> feature: elke sectiekop in features.md linkt naar precies een
   epic, elke epic heeft precies een sectie, en de Features-cel van de epic
   linkt naar de kop van die sectie.
4. feature <-> story: de Epic-cel van elke featurerij komt overeen met de
   sectie waarin de rij staat; de Stories-cel bevat exact de stories die
   met hun featurecel terugwijzen (of "geen").
5. story -> functionele eis: elke functionele-eis-link resolvet naar een
   rij-anker in de Public-checkout naast deze repository; ontbreekt die
   checkout, dan wordt dit punt met een waarschuwing overgeslagen.

Bekende grenzen: alleen inline-links ([tekst](bestand#anker)) worden
gecontroleerd, referentiestijl-links niet (komen in de boom niet voor);
anker-achtige tekst in codeblokken telt mee als anker (faalt naar de
veilige kant); de featurecel vereist id en naam als linktekst, conform
het tabelformat in de skill okx-requirements-boom.

Gebruik: python3 scripts/validate-requirementsboom-navigatie.py [requirements-map] [public-map]
Standaard: architecture/docs/requirements en ../Public naast de repo-root.
Exitcodes: 0 = schoon, 1 = problemen gevonden, 2 = pad niet gevonden.
Testgevallen: python3 scripts/test-validate-requirementsboom-navigatie.py.
"""
import os
import re
import sys
import urllib.parse

SOORTEN = ("doel", "epic", "feature", "story")
ID_RE = re.compile(r"^(?:%s)-\d{4}$" % "|".join(SOORTEN))
ANKER_RE = re.compile(r'<a id="([^"]+)"></a>')


def slug(tekst: str) -> str:
    """GitHub-kopslug van platte koptekst (linkmarkup al gestript)."""
    s = tekst.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def cellen(regel: str) -> list[str]:
    return [c.strip() for c in regel.strip().strip("|").split("|")]


def lees(pad: str) -> str:
    return open(pad, encoding="utf-8").read()


def main() -> int:
    boommap = sys.argv[1] if len(sys.argv) > 1 else "architecture/docs/requirements"
    public = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.getcwd(), "..", "Public")
    if not os.path.isdir(boommap):
        print(f"pad niet gevonden: {boommap}", file=sys.stderr)
        return 2
    problemen: list[str] = []
    tekst = {n: lees(os.path.join(boommap, n))
             for n in os.listdir(boommap) if n.endswith(".md")}

    # 1. Ankers verzamelen: uniek en conform id-conventie
    ankers: dict[str, set[str]] = {}
    for naam, inhoud in tekst.items():
        gezien = ankers[naam] = set()
        for a in ANKER_RE.findall(inhoud):
            if a in gezien:
                problemen.append(f"{naam}: dubbel anker {a}")
            gezien.add(a)
            if not ID_RE.match(a):
                problemen.append(f"{naam}: anker {a} volgt de id-conventie niet")
    # 1b. Interne fragmentlinks naar boom-id's resolven
    for naam, inhoud in tekst.items():
        for doelbestand, frag in re.findall(r"\]\((?:([\w.-]+\.md))?#([\w\-]+)\)", inhoud):
            if not ID_RE.match(frag):
                continue  # kopsluglinks toetst punt 3
            doelnaam = doelbestand or naam
            if frag not in ankers.get(doelnaam, set()):
                problemen.append(f"{naam}: link #{frag} zonder anker in {doelnaam}")

    # 2. doel <-> epic
    vooruit: dict[str, set[str]] = {}
    for regel in tekst["opdracht.md"].splitlines():
        m = re.match(r"\| \[(doel-\d{4})\]\(#\1\) \| (.*) \|$", regel)
        if m:
            vooruit[m.group(1)] = set(re.findall(r"\[(epic-\d{4}) ", m.group(2)))
    terug: dict[str, set[str]] = {}
    epic_features_cel: dict[str, str] = {}
    for regel in tekst["epics.md"].splitlines():
        m = re.match(r'\| <a id="(epic-\d{4})"></a>\1 \|', regel)
        if m:
            c = cellen(regel)
            doelen = re.findall(r"\[(doel-\d{4})\]\(opdracht\.md#\1\)", c[3])
            if len(doelen) != 1:
                problemen.append(f"epics.md: {m.group(1)} zonder eenduidige Draagt-bij-aan-cel")
                continue
            terug.setdefault(doelen[0], set()).add(m.group(1))
            epic_features_cel[m.group(1)] = c[5]
    for d in sorted(set(vooruit) | set(terug)):
        if vooruit.get(d, set()) != terug.get(d, set()):
            problemen.append(
                f"doel<->epic: {d} vooruit {sorted(vooruit.get(d, []))} "
                f"!= terug {sorted(terug.get(d, []))}")

    # 3. epic <-> feature (secties) en 4. feature <-> story
    sectie_epic: dict[str, str] = {}
    feature_stories: dict[str, set[str]] = {}
    huidige = None
    for regel in tekst["features.md"].splitlines():
        kop = re.match(r"## \[(.+)\]\(epics\.md#(epic-\d{4})\)\s*$", regel)
        if kop:
            huidige = kop.group(2)
            if huidige in sectie_epic.values():
                problemen.append(f"features.md: tweede sectie voor {huidige}")
            sectie_epic[slug(kop.group(1))] = huidige
            continue
        m = re.match(r'\| <a id="(feature-\d{4})"></a>\1 \|', regel)
        if m:
            c = cellen(regel)
            epics_in_cel = re.findall(r"\[(epic-\d{4})\]\(epics\.md#\1\)", c[4])
            if epics_in_cel != ([huidige] if huidige else []):
                problemen.append(
                    f"features.md: {m.group(1)} Epic-cel {epics_in_cel} "
                    f"!= sectie-epic {huidige}")
            stories = re.findall(r"\[(story-\d{4})\]\(stories\.md#\1\)", c[5])
            if not stories and c[5] != "geen":
                problemen.append(f"features.md: {m.group(1)} Stories-cel noch links noch \"geen\"")
            feature_stories[m.group(1)] = set(stories)
    for epic, cel in epic_features_cel.items():
        m = re.match(r"\[features\]\(features\.md#([\w\-]+)\)$", cel)
        if not m:
            problemen.append(f"epics.md: {epic} Features-cel geen sectielink: {cel}")
        elif sectie_epic.get(m.group(1)) != epic:
            problemen.append(f"epic<->feature: {epic} linkt #{m.group(1)}, "
                             f"maar die sectie hoort bij {sectie_epic.get(m.group(1))}")
    for s, e in sectie_epic.items():
        if e not in epic_features_cel:
            problemen.append(f"epic<->feature: sectie #{s} wijst naar onbekende epic {e}")

    story_feature: dict[str, str] = {}
    eis_links: list[tuple[str, str, str]] = []
    for regel in tekst["stories.md"].splitlines():
        m = re.match(r'\| <a id="(story-\d{4})"></a>\1 \|', regel)
        if m:
            c = cellen(regel)
            feats = re.findall(r"\[(feature-\d{4}) [^\]]*\]\(features\.md#\1\)", c[2])
            if len(feats) != 1:
                problemen.append(f"stories.md: {m.group(1)} zonder eenduidige featurecel")
                continue
            story_feature[m.group(1)] = feats[0]
            for url, frag in re.findall(
                    r"\[functionele-eis-\d{4}\]\((https://github\.com/Npuls-OKx/Public/"
                    r"blob/dev/[^)#]+)#(functionele-eis-\d{4})\)", c[4]):
                eis_links.append((m.group(1), url, frag))
            if not re.search(r"functionele-eis-\d{4}", c[4]) and c[4] != "geen":
                problemen.append(f"stories.md: {m.group(1)} Functionele-eisen-cel "
                                 f"noch eis-link noch \"geen\"")
    terug_fs: dict[str, set[str]] = {}
    for s, f in story_feature.items():
        terug_fs.setdefault(f, set()).add(s)
        if f not in feature_stories:
            problemen.append(f"feature<->story: {s} wijst naar onbekende {f}")
    for f in sorted(set(feature_stories) | set(terug_fs)):
        if feature_stories.get(f, set()) != terug_fs.get(f, set()):
            problemen.append(
                f"feature<->story: {f} Stories-cel {sorted(feature_stories.get(f, []))} "
                f"!= terugwijzend {sorted(terug_fs.get(f, []))}")

    # 5. story -> functionele eis. De links wijzen naar blob/dev op GitHub,
    # dus de referentie is origin/dev van de Public-checkout, niet de
    # werkkopie (die kan op een andere branch staan of achterlopen).
    if os.path.isdir(os.path.join(public, ".git")):
        import subprocess
        cache: dict[str, str | None] = {}
        for story, url, frag in eis_links:
            rel = urllib.parse.unquote(url.split("/blob/dev/", 1)[1])
            if rel not in cache:
                uit = subprocess.run(
                    ["git", "-C", public, "show", f"origin/dev:{rel}"],
                    capture_output=True, text=True)
                cache[rel] = uit.stdout if uit.returncode == 0 else None
            if cache[rel] is None:
                problemen.append(f"stories.md: {story} linkt {rel}, "
                                 f"niet aanwezig op Public origin/dev")
            elif f'<a id="{frag}"></a>' not in cache[rel]:
                problemen.append(f"stories.md: {story} linkt {frag} zonder anker in {rel}")
    else:
        print(f"waarschuwing: Public-checkout niet gevonden ({public}); "
              f"functionele-eis-ankers niet gecontroleerd")

    for p in problemen:
        print(p)
    print(f"boomcontrole: {len(tekst)} bestanden, {len(story_feature)} stories, "
          f"{len(feature_stories)} features, {len(epic_features_cel)} epics, "
          f"{len(vooruit)} doelen, {len(eis_links)} eis-links, "
          f"{len(problemen)} problemen.")
    return 1 if problemen else 0


if __name__ == "__main__":
    sys.exit(main())
