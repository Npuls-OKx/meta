# Release notes (GitHub-tag)

Maak **release notes** in Markdown voor een GitHub **Release** bij een nieuwe **git-tag** (SemVer), bijvoorbeeld `v0.0.1`.

## Aanpak

1. **Versie:** gebruik de tag die de gebruiker noemt (of `$ARGUMENTS`), anders **`v0.0.1`** als voorbeeld. Noem de tag exact zoals op GitHub (meestal met `v`-prefix).
2. **Feiten verzamelen** (repo lokaal):
   - `git tag -l` — welke tags bestaan er al?
   - Als er een **vorige tag** is: `git log <vorige-tag>..HEAD --oneline` (en eventueel `--no-merges`).
   - Als dit de **eerste tag** is: `git log --oneline` met redelijke limiet, of commits sinds een afgesproken startpunt.
   - Optioneel: `git shortlog` of diff-stat voor grotere wijzigingen.
3. **Scope OKx-meta:** groepeer onder duidelijke kopjes, bijvoorbeeld:
   - **Documentatie** (`doc/`, `README.md`, `CONTRIBUTING.md`)
   - **Architectuur** (`architecture/dr/`, `architecture/model/model.archimate`, meetings)
   - **Governance / bijdragen** (ADR’s, principes)
   - **Overig** (OKE, MOKA-templates, `.cursor`, CI)
4. **Toon:** helder, **Nederlands** (tenzij de gebruiker Engels vraagt), volledige zinnen. Geen overdreven hype; wel concreet wat er voor stakeholders verandert.
5. **Eerste release (0.0.x):** vermeld kort dat dit een **vroege** / **baseline**-release kan zijn en wat gebruikers mogen verwachten (kennisbasis, geen “afgerond product”).

## Output

Lever **alleen** (of primair):

1. Een **tekstblok Markdown** geschikt om te **plakken in GitHub → Releases → Create a new release** (veld *Release notes*).
2. Onderaan, optioneel: **korte instructies** voor de gebruiker:
   - `git tag -a v0.0.1 -m "Release v0.0.1"`
   - `git push origin v0.0.1`
   - (of het aanmaken van de release via GitHub UI na push)

Als de gebruiker **ook** een bestand `CHANGELOG.md` wil: voeg een sectie **`## [v0.0.1] — YYYY-MM-DD`** toe volgens [Keep a Changelog](https://keepachangelog.com/)-stijl — **alleen** als de gebruiker dat expliciet vraagt.

## Niet doen

- Geen fictieve commits of issues verzinnen; alleen wat uit `git` of expliciete context van de gebruiker volgt.
- Geen grote refactors of andere bestanden wijzigen tenzij de gebruiker `CHANGELOG.md` wil.
