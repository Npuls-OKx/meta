## Bijdragen aan OKx-meta

Deze repository is een knowledge base die team OKx maintaint. Leveranciers, instellingen en geinteresseerden kunnen 24/7 federatief en asynchroon bijdragen via issues en pull requests (PR's).

### Governance

- Iedereen mag issues openen en PR's indienen.
- Alleen OKx-teamleden mergen PR's.
- Team OKx begeleidt de uitbouw en bewaakt samenhang en richting.
- Een kerngroep OKx komt periodiek bij elkaar om prioriteiten en richting te geven aan verander-initiatieven op basis van GitHub issues, milestones en PR's (milestones worden handmatig beheerd).

### Wat hoort waar

- ArchiMate model: `architecture/model/model.archimate`
- ADR's (decision records): `architecture/dr/`
- Meetings (notulen + optioneel transcript): `architecture/meetings/`
- OKx context: `doc/` en `img/`
- OKE uitwerkingen: `OKE/`
- MOKA template (onderdeel van OKx): `moka-koppelvlakspecificaties/`

### Workflow (kort)

1. Start met een issue (vraag, voorstel, meeting follow-up, ADR-voorstel).
2. Werk het uit in een PR met concrete wijzigingen.
3. Link in de PR naar het issue (Fixes #123 / See also #456).
4. Als het een architectuurbesluit is: voeg of wijzig een ADR in `architecture/dr/` en link naar notulen/issues.

### Meetings vastleggen

We werken federatief en asynchroon. Meetings worden daarom vastgelegd in de repo:

1. Vastleggen: opname en/of ruwe aantekeningen.
2. Transcriberen: optioneel transcript opslaan in `architecture/meetings/YYYY/YYYY-MM-DD-onderwerp-transcript.md`.
3. Samenvatten: notulen opslaan in `architecture/meetings/YYYY/YYYY-MM-DD-onderwerp.md` met links naar issues/ADR's.

### Templates

- Issue templates: `.github/ISSUE_TEMPLATE/`
- PR template: `.github/PULL_REQUEST_TEMPLATE.md`
- ADR template: `architecture/dr/template.md`
- Notulen template: `architecture/meetings/template-notulen.md`

