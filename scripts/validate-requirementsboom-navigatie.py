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
Testgevallen: python3 -m unittest discover -s tests -v.
"""
import os
import re
import sys
import urllib.parse

KINDS = ("doel", "epic", "feature", "story")
ID_RE = re.compile(r"^(?:%s)-\d{4}$" % "|".join(KINDS))
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')


def slug(text: str) -> str:
    """GitHub-kopslug van platte koptekst (linkmarkup al gestript)."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def cells(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def read_text(path: str) -> str:
    return open(path, encoding="utf-8").read()


def main() -> int:
    tree_dir = sys.argv[1] if len(sys.argv) > 1 else "architecture/docs/requirements"
    public_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.getcwd(), "..", "Public")
    if not os.path.isdir(tree_dir):
        print(f"pad niet gevonden: {tree_dir}", file=sys.stderr)
        return 2
    problems: list[str] = []
    texts = {name: read_text(os.path.join(tree_dir, name))
             for name in os.listdir(tree_dir) if name.endswith(".md")}

    # 1. Ankers verzamelen: uniek en conform id-conventie
    anchors: dict[str, set[str]] = {}
    for name, content in texts.items():
        seen = anchors[name] = set()
        for anchor in ANCHOR_RE.findall(content):
            if anchor in seen:
                problems.append(f"{name}: dubbel anker {anchor}")
            seen.add(anchor)
            if not ID_RE.match(anchor):
                problems.append(f"{name}: anker {anchor} volgt de id-conventie niet")
    # 1b. Interne fragmentlinks naar boom-id's resolven
    for name, content in texts.items():
        for target_file, fragment in re.findall(r"\]\((?:([\w.-]+\.md))?#([\w\-]+)\)", content):
            if not ID_RE.match(fragment):
                continue  # kopsluglinks toetst punt 3
            target_name = target_file or name
            if fragment not in anchors.get(target_name, set()):
                problems.append(f"{name}: link #{fragment} zonder anker in {target_name}")

    # 2. doel <-> epic
    forward: dict[str, set[str]] = {}
    for row in texts["opdracht.md"].splitlines():
        m = re.match(r"\| \[(doel-\d{4})\]\(#\1\) \| (.*) \|$", row)
        if m:
            forward[m.group(1)] = set(re.findall(r"\[(epic-\d{4}) ", m.group(2)))
    backward: dict[str, set[str]] = {}
    epic_features_cell: dict[str, str] = {}
    for row in texts["epics.md"].splitlines():
        m = re.match(r'\| <a id="(epic-\d{4})"></a>\1 \|', row)
        if m:
            c = cells(row)
            goals = re.findall(r"\[(doel-\d{4})\]\(opdracht\.md#\1\)", c[3])
            if len(goals) != 1:
                problems.append(f"epics.md: {m.group(1)} zonder eenduidige Draagt-bij-aan-cel")
                continue
            backward.setdefault(goals[0], set()).add(m.group(1))
            epic_features_cell[m.group(1)] = c[5]
    for goal in sorted(set(forward) | set(backward)):
        if forward.get(goal, set()) != backward.get(goal, set()):
            problems.append(
                f"doel<->epic: {goal} vooruit {sorted(forward.get(goal, []))} "
                f"!= terug {sorted(backward.get(goal, []))}")

    # 3. epic <-> feature (secties) en 4. feature <-> story
    section_epic: dict[str, str] = {}
    feature_stories: dict[str, set[str]] = {}
    current_epic = None
    for row in texts["features.md"].splitlines():
        heading = re.match(r"## \[(.+)\]\(epics\.md#(epic-\d{4})\)\s*$", row)
        if heading:
            current_epic = heading.group(2)
            if current_epic in section_epic.values():
                problems.append(f"features.md: tweede sectie voor {current_epic}")
            section_epic[slug(heading.group(1))] = current_epic
            continue
        m = re.match(r'\| <a id="(feature-\d{4})"></a>\1 \|', row)
        if m:
            c = cells(row)
            epics_in_cell = re.findall(r"\[(epic-\d{4})\]\(epics\.md#\1\)", c[4])
            if epics_in_cell != ([current_epic] if current_epic else []):
                problems.append(
                    f"features.md: {m.group(1)} Epic-cel {epics_in_cell} "
                    f"!= sectie-epic {current_epic}")
            stories = re.findall(r"\[(story-\d{4})\]\(stories\.md#\1\)", c[5])
            if not stories and c[5] != "geen":
                problems.append(f"features.md: {m.group(1)} Stories-cel noch links noch \"geen\"")
            feature_stories[m.group(1)] = set(stories)
    for epic, cell in epic_features_cell.items():
        m = re.match(r"\[features\]\(features\.md#([\w\-]+)\)$", cell)
        if not m:
            problems.append(f"epics.md: {epic} Features-cel geen sectielink: {cell}")
        elif section_epic.get(m.group(1)) != epic:
            problems.append(f"epic<->feature: {epic} linkt #{m.group(1)}, "
                            f"maar die sectie hoort bij {section_epic.get(m.group(1))}")
    for section, epic in section_epic.items():
        if epic not in epic_features_cell:
            problems.append(f"epic<->feature: sectie #{section} wijst naar onbekende epic {epic}")

    story_feature: dict[str, str] = {}
    requirement_links: list[tuple[str, str, str]] = []
    for row in texts["stories.md"].splitlines():
        m = re.match(r'\| <a id="(story-\d{4})"></a>\1 \|', row)
        if m:
            c = cells(row)
            features = re.findall(r"\[(feature-\d{4}) [^\]]*\]\(features\.md#\1\)", c[2])
            if len(features) != 1:
                problems.append(f"stories.md: {m.group(1)} zonder eenduidige featurecel")
                continue
            story_feature[m.group(1)] = features[0]
            for url, fragment in re.findall(
                    r"\[functionele-eis-\d{4}\]\((https://github\.com/Npuls-OKx/Public/"
                    r"blob/dev/[^)#]+)#(functionele-eis-\d{4})\)", c[4]):
                requirement_links.append((m.group(1), url, fragment))
            if not re.search(r"functionele-eis-\d{4}", c[4]) and c[4] != "geen":
                problems.append(f"stories.md: {m.group(1)} Functionele-eisen-cel "
                                f"noch eis-link noch \"geen\"")
    stories_backward: dict[str, set[str]] = {}
    for story, feature in story_feature.items():
        stories_backward.setdefault(feature, set()).add(story)
        if feature not in feature_stories:
            problems.append(f"feature<->story: {story} wijst naar onbekende {feature}")
    for feature in sorted(set(feature_stories) | set(stories_backward)):
        if feature_stories.get(feature, set()) != stories_backward.get(feature, set()):
            problems.append(
                f"feature<->story: {feature} Stories-cel "
                f"{sorted(feature_stories.get(feature, []))} "
                f"!= terugwijzend {sorted(stories_backward.get(feature, []))}")

    # 5. story -> functionele eis. De links wijzen naar blob/dev op GitHub,
    # dus de referentie is origin/dev van de Public-checkout, niet de
    # werkkopie (die kan op een andere branch staan of achterlopen).
    if os.path.isdir(os.path.join(public_dir, ".git")):
        import subprocess
        cache: dict[str, str | None] = {}
        for story, url, fragment in requirement_links:
            rel_path = urllib.parse.unquote(url.split("/blob/dev/", 1)[1])
            if rel_path not in cache:
                proc = subprocess.run(
                    ["git", "-C", public_dir, "show", f"origin/dev:{rel_path}"],
                    capture_output=True, text=True)
                cache[rel_path] = proc.stdout if proc.returncode == 0 else None
            if cache[rel_path] is None:
                problems.append(f"stories.md: {story} linkt {rel_path}, "
                                f"niet aanwezig op Public origin/dev")
            elif f'<a id="{fragment}"></a>' not in cache[rel_path]:
                problems.append(f"stories.md: {story} linkt {fragment} zonder anker in {rel_path}")
    else:
        print(f"waarschuwing: Public-checkout niet gevonden ({public_dir}); "
              f"functionele-eis-ankers niet gecontroleerd")

    for problem in problems:
        print(problem)
    print(f"boomcontrole: {len(texts)} bestanden, {len(story_feature)} stories, "
          f"{len(feature_stories)} features, {len(epic_features_cell)} epics, "
          f"{len(forward)} doelen, {len(requirement_links)} eis-links, "
          f"{len(problems)} problemen.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
