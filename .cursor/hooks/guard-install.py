#!/usr/bin/env python3
"""Cursor hook: gate package installs zodat agents niet ad-hoc op de host installeren.

Draait op `beforeShellExecution`. Detecteert installatie-commando's van gangbare
package managers en zet ze op "ask", zodat de mens bewust moet goedkeuren.
Werk in de Dev Container (.devcontainer/) en voeg dependencies daar toe.

Stdin: JSON met o.a. {"command": "..."}.
Stdout: JSON met {"permission": "allow" | "ask" | "deny", ...}.

Let op: deze hook faalt 'open' (allow) bij onverwachte fouten, behalve wanneer
in hooks.json `failClosed: true` staat. Wil je een keiharde blokkade i.p.v. een
bevestigingsvraag, vervang dan "ask" door "deny" hieronder.
"""
import sys
import json
import re

INSTALL_PATTERNS = [
    r"\bpip3?\s+install\b",
    r"\bpython3?\s+-m\s+pip\s+install\b",
    r"\bpipx\s+install\b",
    r"\buv\s+(pip\s+install|add)\b",
    r"\bconda\s+install\b",
    r"\bpoetry\s+add\b",
    r"\beasy_install\b",
    r"\bnpm\s+(install|i|add|ci)\b",
    r"\bpnpm\s+(install|i|add)\b",
    r"\byarn\s+(add|global\s+add)\b",
]

AGENT_MSG = (
    "Geblokkeerd door projecthook: installeer geen pakketten op de host. "
    "Werk in de Dev Container (.devcontainer/, 'Reopen in Container'). "
    "Nieuwe dependency nodig? Voeg die toe aan .devcontainer/requirements.txt "
    "(Python), .devcontainer/Dockerfile (systeem/CLI) of postCreateCommand in "
    ".devcontainer/devcontainer.json (Node) en rebuild de container."
)
USER_MSG = (
    "Pakket-installatie gedetecteerd. Alleen toestaan als dit IN de Dev Container "
    "draait; draait dit op je host, weiger het dan."
)


def main() -> None:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
        command = str(data.get("command") or "")
    except Exception:
        print(json.dumps({"permission": "allow"}))
        return

    if any(re.search(p, command) for p in INSTALL_PATTERNS):
        print(json.dumps({
            "permission": "ask",
            "user_message": USER_MSG,
            "agent_message": AGENT_MSG,
        }))
        return

    print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
