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
- **GitHub CLI (`gh`)** (via devcontainer-feature) - zie hieronder.
- `imagemagick`, `graphviz`, `pandoc`, `chromium`.

## GitHub vanuit de container (eenmalig inloggen)

Zonder login kan de container **niet pushen** (`could not read Username for 'https://github.com'`)
en kunnen agents geen PR's openen of reviewen. Log daarom na de eerste build eenmalig in:

```bash
gh auth login        # kies: GitHub.com -> HTTPS -> login met browser/device code
gh auth setup-git    # maakt gh de git credential helper, zodat ook `git push` werkt
```

Controleren:

```bash
gh auth status
git push --dry-run   # moet nu slagen zonder om een gebruikersnaam te vragen
```

De login wordt bewaard in een **named volume** (`okx-meta-gh-config`, gemount op
`~/.config/gh`), dus je hoeft dit **niet** te herhalen na een `Rebuild Container`.

Daarmee kunnen mens en agent hetzelfde: committen, pushen, PR's openen (`gh pr create`),
reviewen en mergen - allemaal **binnen** de container, conform
[`dev-omgeving.mdc`](../.cursor/rules/dev-omgeving.mdc).

## Extra tooling toevoegen (reproduceerbaar voor het team)

Installeer **niet** ad-hoc; voeg het toe aan de juiste plek en rebuild:

| Type | Waar toevoegen |
|------|----------------|
| Python-pakket | [`requirements.txt`](requirements.txt) |
| Systeem/CLI-tool | [`Dockerfile`](Dockerfile) |
| Node-tool (globaal) | `postCreateCommand` in [`devcontainer.json`](devcontainer.json) |
| CLI met eigen feature (bv. `gh`) | `features` in [`devcontainer.json`](devcontainer.json) |

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
