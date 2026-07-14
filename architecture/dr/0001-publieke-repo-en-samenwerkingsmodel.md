## Publieke repository als single source of truth en samenwerkingsmodel

Status: Voorstel

Datum: 2026-03-25

### Context

OKx heeft behoefte aan **traceerbare besluitvorming**, **versionering** van kennis en modellen, en **gedeeld eigenaarschap** tussen instellingen, leveranciers en het kernteam. Zonder centrale plek dreigen **versnippering**, **niet terug te voeren besluiten** en **lokale optima** (oplossingen die elders in de keten problemen geven).

In de SI-afstemming met Jos van den Arend (maart 2024) is de **centrale GitHub-repository** benadrukt als **openbare kennisbank** voor modellen en specificaties, met **pull requests** en **review** door het kernteam. In het kernteamoverleg (maart 2026) wordt **GitHub als backlog** voor technische behoeften en issues expliciet genoemd.

**Samenhang:** Deze beslissing gaat over **hoe** we vastleggen en wijzigen. **Wat** we eerst inhoudelijk uitwerken staat in [0002-prioriteitsketen-catalogus-drielagen-fundament.md](0002-prioriteitsketen-catalogus-drielagen-fundament.md); **domeinprincipes** (student kiest, leeruitkomsten) in [0003-student-kiest-leeruitkomsten-domeinprincipes.md](0003-student-kiest-leeruitkomsten-domeinprincipes.md).

### Beslissing (concept)

1. De **publieke GitHub-repository** is de **primaire bron** (“single source of truth”) voor OKx-kennis die onder versiebeheer hoort: o.a. ArchiMate-model, koppelvlakrichting, proces- en informatie-inzichten, ADR’s en relevante documentatie.
2. **Wijzigingen** aan die artefacten verlopen via **pull requests** en worden beoordeeld door het **kernteam** (en waar afgesproken: kerngroep techniek), conform [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
3. **Issues** worden gebruikt voor vragen, backlog, onduidelijkheden en koppeling aan leveranciers-/instellingsfeedback (o.a. “barrières” en vervolgstappen).
4. **Geen stille grootschalige wijzigingen** aan het hoofdmodel zonder review: wijzigingen moeten **navolgbaar** zijn (PR, eventueel release notes / changelog waar het team dat hanteert).

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Wiki of losse documenten** zonder strikte review | Snel schrijven | **Geen** eenduidige versionering; moeilijk **traceerbaar** besluit |
| **B. Alleen interne (niet-publieke) repo** | Meer vrijheid | Minder **transparantie** voor sector; haakt af bij OKx-open-kennisprincipes |
| **C. (Gekozen richting)** Publieke repo + PR + issues + kernteam-merge | **Traceerbaarheid**, **gedeeld beeld**, **bestuurbare** wijzigingen | **Proceslast**; deelnemers moeten **Git/GitHub** begrijpen of begeleid worden |

### Consequenties

- **Stakeholders:** Instellingen en leveranciers kunnen **issues** indienen; **kernteam** behoudt **regie** op wat in de “officiële” lijn wordt gemerged.
- **Werk:** Documentatie voor **toegang en bijdrage** (`doc/Bijdragen-voor-beginners.md`); bewaking **begrijpbaarheid** voor niet-architecten.
- **Risico:** **Frustratie** als de repo “te vaak” wijzigt zonder duidelijke **releases** — mitigatie: heldere **main/dev**-branchstrategie en waar nodig **release notes** (zie bijdragenhandleiding).

### Impact op `architecture/model/model.archimate`

- **Wijzigingsbeheer:** Wijzigingen aan het ArchiMate-model lopen via hetzelfde **PR-/reviewproces** als andere kernartefacten; geen **stille** wijzigingen zonder vastlegging.
- **Navolgbaarheid:** PR’s en eventuele **ADR’s** (bij inhoudelijk grote wijzigingen) moeten **waarom** en **wat** mutatie uitleggen.

### Relaties en links

- **Gerelateerde ADR’s:** [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md) (scope keten en fundament), [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (domeinprincipes)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/20260324_okx_si_team_afstemming_josvdarend/okx_si_team_afstemming_josvdarend_aanhaken_voortgang_okx_240326_summary.md`
  - `architecture/meetings/20260324_okx_si_team_afstemming_josvdarend/okx_si_team_afstemming_josvdarend_aanhaken_voortgang_okx_240326_transcript.md`
  - `architecture/meetings/20260325_okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst/summary.md`
- ArchiMate: `architecture/model/model.archimate`
- Governance: [`CONTRIBUTING.md`](../../CONTRIBUTING.md), [`doc/Bijdragen-voor-beginners.md`](../../doc/Bijdragen-voor-beginners.md)

### Vervangt (optioneel)

- Vervangt het eerdere gecombineerde voorstel `0001-centrale-repo-keten-catalogus-en-drielagen-fundament.md` (opgesplitst in 0001–0003).
