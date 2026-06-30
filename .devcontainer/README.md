# Dev container (geisoleerde dev-omgeving)

Deze map levert een **reproduceerbare, geisoleerde** ontwikkelomgeving via Docker.
Doel: (AI-)agents en mensen kunnen tooling installeren en scripts draaien **in de
container**, zonder de lokale machine (host) te vervuilen. Iedereen die de repo
cloont werkt na een paar klikken in **exact dezelfde** omgeving.

## Eenmalig: vereisten

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS) of Docker Engine (Linux), draaiend.
- In VS Code: extensie **Dev Containers** (`ms-vscode-remote.remote-containers`). Cursor heeft Dev Containers ingebouwd.

## Gebruiken

1. Open de repo-map in Cursor of VS Code.
2. Kies **"Reopen in Container"** (commandpalet: `Dev Containers: Reopen in Container`).
3. De container wordt 1x gebouwd. Daarna draaien terminal, agents en installaties **in de container**.

Controleren dat je in de container zit:

```bash
whoami          # -> vscode
cat /.dockerenv # bestaat -> je zit in een container
```

## Wat zit erin

- Python 3.12 + `pip` (zie [`requirements.txt`](requirements.txt), o.a. Pillow).
- Node.js LTS + `npm` (via devcontainer-feature) + `markdownlint-cli2` + `mermaid-cli`.
- `imagemagick`, `graphviz`, `pandoc`, `chromium`.

## Extra tooling toevoegen (reproduceerbaar voor het team)

Installeer **niet** ad-hoc; voeg het toe aan de juiste plek en rebuild:

| Type | Waar toevoegen |
|------|----------------|
| Python-pakket | [`requirements.txt`](requirements.txt) |
| Systeem/CLI-tool | [`Dockerfile`](Dockerfile) |
| Node-tool (globaal) | `postCreateCommand` in [`devcontainer.json`](devcontainer.json) |

Daarna: commandpalet -> **`Dev Containers: Rebuild Container`**.

## Afspraak voor agents

De regel [`.cursor/rules/dev-omgeving.mdc`](../.cursor/rules/dev-omgeving.mdc)
(altijd actief) verbiedt installaties op de host en verwijst naar deze container.

Daarbovenop onderschept de hook [`.cursor/hooks.json`](../.cursor/hooks.json)
(`beforeShellExecution` -> [`.cursor/hooks/guard-install.py`](../.cursor/hooks/guard-install.py))
pakket-installaties (`pip install`, `npm install`, enz.) en vraagt eerst om
bevestiging. De hook draait op de host via `python`; mac/Linux-collega's met enkel
`python3` passen het commando in `hooks.json` daarop aan. Wil je een keiharde
blokkade i.p.v. een vraag, zet dan `"ask"` op `"deny"` in `guard-install.py`.
