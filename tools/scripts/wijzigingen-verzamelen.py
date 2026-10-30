#!/usr/bin/env python3
"""Verzamelt de wijzigingen uit beide OKx-repositories over een periode.

De grondstof voor een update-deck. OKx werkt met twee repositories, en een
update gaat over wat er in allebei is gebeurd:

    Npuls-OKx/meta     kaderstelling, model, notulen
    Npuls-OKx/Public   releaseartefacten

Het script leest ze naast elkaar uit de workspace. Staat er een niet lokaal,
dan valt het terug op de GitHub API via `gh`.

De uitvoer is bewust ruw: gemergde pull requests met hun beschrijving, en de
bestanden die zijn gewijzigd. Een deck maak je daar niet mechanisch van. Een
pull request-titel zegt *wat* er is veranderd; wat het betekent staat in de
beschrijving en in de documenten zelf. Lees die voordat je een slide schrijft.

Gebruik:
    python3 scripts/wijzigingen-verzamelen.py --sinds 2026-07-01
    python3 scripts/wijzigingen-verzamelen.py --sinds 2026-07-01 --formaat json
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPOS = {
    "Npuls-OKx/meta": Path("/workspaces/OKx/OKx-meta"),
    "Npuls-OKx/Public": Path("/workspaces/OKx/Public"),
}


def draai(argv: list[str], cwd: Path | None = None) -> str:
    klaar = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    if klaar.returncode != 0:
        return ""
    return klaar.stdout


def pull_requests(repo: str, sinds: str) -> list[dict]:
    """Gemergde pull requests sinds een datum, met beschrijving."""
    if not shutil.which("gh"):
        return []
    uit = draai([
        "gh", "pr", "list", "--repo", repo, "--state", "merged", "--limit", "100",
        "--json", "number,title,body,mergedAt,author,url",
    ])
    if not uit:
        return []
    prs = [p for p in json.loads(uit) if (p.get("mergedAt") or "") >= sinds]
    return sorted(prs, key=lambda p: p["mergedAt"])


def integratielijn(pad: Path) -> str | None:
    """De ref die de integratielijn draagt: lokale dev, anders die van een remote.

    Niet elke werkkopie heeft een lokale dev-branch; in Npuls-OKx/meta bestaat
    alleen de remote variant. Zonder deze terugval levert het script stilzwijgend
    nul bestanden op, wat eruitziet als "er is niets gebeurd".
    """
    if draai(["git", "rev-parse", "--verify", "--quiet", "dev"], cwd=pad).strip():
        return "dev"
    for remote in draai(["git", "remote"], cwd=pad).split():
        ref = f"{remote}/dev"
        if draai(["git", "rev-parse", "--verify", "--quiet", ref], cwd=pad).strip():
            return ref
    return None


def bestanden(pad: Path, sinds: str) -> dict[str, list[str]]:
    """Toegevoegde en gewijzigde bestanden sinds een datum."""
    if not (pad / ".git").exists():
        return {}
    branch = integratielijn(pad)
    if branch is None:
        return {}
    uit = draai(["git", "log", f"--since={sinds}", "--name-status",
                 "--pretty=format:", branch], cwd=pad)
    per_soort: dict[str, set[str]] = {"toegevoegd": set(), "gewijzigd": set(), "verwijderd": set()}
    for regel in uit.splitlines():
        if not regel.strip():
            continue
        deel = regel.split("\t")
        if len(deel) < 2:
            continue
        soort = {"A": "toegevoegd", "M": "gewijzigd", "D": "verwijderd"}.get(deel[0][0])
        if soort:
            per_soort[soort].add(deel[-1])
    return {k: sorted(v) for k, v in per_soort.items() if v}


def verzamel(sinds: str) -> dict:
    resultaat = {}
    for repo, pad in REPOS.items():
        lokaal = (pad / ".git").exists()
        resultaat[repo] = {
            "lokaal": lokaal,
            "pad": str(pad) if lokaal else None,
            "pull_requests": pull_requests(repo, sinds),
            "bestanden": bestanden(pad, sinds) if lokaal else {},
        }
    return resultaat


def toon(data: dict, sinds: str) -> None:
    print(f"Wijzigingen sinds {sinds}\n")
    for repo, d in data.items():
        prs = d["pull_requests"]
        print(f"{'=' * 72}\n{repo}{'' if d['lokaal'] else '   (niet lokaal; alleen pull requests)'}\n{'=' * 72}")
        if not prs:
            print("  geen gemergde pull requests in deze periode\n")
        for p in prs:
            print(f"\n  #{p['number']}  {p['title']}")
            print(f"    gemerged {p['mergedAt'][:10]} door {p['author'].get('login', '?')}")
            body = (p.get("body") or "").strip()
            if body:
                kern = [r for r in body.splitlines() if r.strip() and not r.startswith(("#", "|", "```"))][:3]
                for r in kern:
                    print(f"    | {r.strip()[:100]}")
        b = d["bestanden"]
        if b:
            print("\n  bestanden:")
            for soort, lijst in b.items():
                print(f"    {soort}: {len(lijst)}")
                for f in lijst[:8]:
                    print(f"      {f}")
                if len(lijst) > 8:
                    print(f"      ... en {len(lijst) - 8} meer")
        print()
    print("Lees de pull request-beschrijvingen en de gewijzigde documenten voordat je")
    print("een slide schrijft. Een titel zegt wat er is veranderd, niet wat het betekent.")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--sinds", required=True, help="datum als JJJJ-MM-DD")
    p.add_argument("--formaat", choices=["tekst", "json"], default="tekst")
    a = p.parse_args()

    data = verzamel(a.sinds)
    if a.formaat == "json":
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        toon(data, a.sinds)
    return 0


if __name__ == "__main__":
    sys.exit(main())
