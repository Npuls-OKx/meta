# AGENTS.md

Basisdocument voor AI-agents (Cursor, Claude Code, Codex en vergelijkbaar) die in deze repository werken. Lees dit eerst; de details staan achter de links.

## Wat is deze repository

OKx-meta is de **publieke kennisbank** van OKx (Npuls, pijler Leren Zonder Drempels): gedeelde kennis, afspraken en conceptuitwerkingen rond **gestandaardiseerde koppelvlakken voor onderwijslogistiek**. Dit is een documentatierepository, geen codebase. Scope start bij mbo (leerroutes 1-3 eerst), hoger onderwijs volgt. Volledige introductie: [README.md](README.md) en [doc/OKx_Projectoverzicht.md](doc/OKx_Projectoverzicht.md).

## Principes en werkafspraken

De architectuurprincipes van OKx staan in [Referentiemateriaal/principes in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md) (OKx-AP01 tot en met AP13; AMIGO als standaardiseringsroute is AP03), naast de [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md). Eisen komen vóór de techniekkeuze: een eis sneuvelt nooit omdat OEAPI of een andere technische standaard hem niet toestaat; zo'n mismatch is een signalering richting de standaard (uitgangspunt-voorstel voor Public in voorbereiding, relateert aan #139).

Voor het werk in deze repository gelden vier werkafspraken:

1. **Design first**: ontwerpen en reviewen vóór "af"; iteratief via issues en PR's.
2. **Machine-interpreteerbaar**: gestructureerde markdown, JSON, valideerbare definities.
3. **Show don't tell**: diagrammen (mermaid), tabellen en voorbeelden boven lange tekst.
4. **Milestone-gedreven**: een grotere klus krijgt een GitHub-milestone die herleidbaar is naar de [requirementsboom](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md) (doel, epic of feature); elk issue hangt onder een milestone. Bij een los idee zonder milestone-context vraagt de agent de indiener door tot het grotere plaatje duidelijk is, en stelt dan een bestaande of nieuwe milestone voor (issue #179).

De werkafspraken zijn levend; wijzigen via PR.

## Aannames en kaders

- **Scenario's**: leerroutes 1-3 met de persona's uit de [leerroute-uitwerking](architecture/docs/specificatie/leerroute-uitwerking/README.md); latere leerroutes als delta.
- **Intra-instelling eerst**, federatie gefaseerd (ADR 0008).
- **Taal**: Nederlands, IT-vaktermen tussen haakjes. Stijl: [.cursor/rules/schrijfstijl.mdc](.cursor/rules/schrijfstijl.mdc).
- **Semantiek**: de zes begrippenfamilies uit de ankertabel in het [begrippenkader van de leerroute-uitwerking](architecture/docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) (kwalificatiekader, beoogde leeruitkomst, onderwijsspecificatie, onderwijsaanbod, onderwijsverbintenis, onderwijsresultaat); de leeruitkomst is de sleutel, onderwijsresultaten hangen aan leeruitkomsten. Subtypen voluit met backquotes; geen verzonnen termen. Een koppeling is de informatiestroom tussen twee componenten; een koppelvlak is de verzameling koppelingen van één component.
- **Geen metadatakop (frontmatter)** in deliverables en agent-artifacten: GitHub (git-historie, issues, PR's) is de bron voor auteurschap, datums en traceerbaarheid; verwijs in de tekst ("Relateert aan: #12"). Uitzondering: `SKILL.md`-bestanden en `.mdc`-rules houden hun verplichte metadatakop (naam, beschrijving, `alwaysApply`).

## Harde regels

1. **Raak nooit een `*.archimate`-bestand aan.** Nooit tekstueel mergen; zie [architecture/model/README.md](architecture/model/README.md) en ADR 0010. Vóór elke model-commit: `python3 scripts/validate-archimate.py`.
2. **Installaties alleen in de dev-container**, nooit op de host ([.cursor/rules/dev-omgeving.mdc](.cursor/rules/dev-omgeving.mdc); een controlescript (hook) bewaakt dit).
3. **1 issue = 1 branch = 1 PR**, feature-branches vanaf `dev`, alleen het OKx-team merget ([CONTRIBUTING.md](CONTRIBUTING.md)).
4. **Deliverables volgen de product-flow** (requirements, uitwerking, onafhankelijke review; zie hieronder).
5. Markdown-deliverables halen de voorcontrole: `python3 scripts/validate-docs.py <pad>`.

## Waar vind ik wat

| Wat | Waar |
|---|---|
| Projectcontext, hoofdplaat informatiestromen | [doc/](doc/) |
| Requirementsboom (opdracht, epics, features, stories) | [Referentiemateriaal/requirementsboom in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md) |
| Architectuurbesluiten (ADR's) | [Referentiemateriaal/adr in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr) |
| ArchiMate-model (niet aanraken) | [architecture/model/](architecture/model/) |
| Meetingverslagen | [architecture/meetings/](architecture/meetings/) |
| Specificaties (leerroute-uitwerking, persona's) | [architecture/docs/specificatie/](architecture/docs/specificatie/) |
| Agent-artifacten (ontwerpen, plannen) | [architecture/agent-artifacts/](architecture/agent-artifacts/) |
| OKE-subdomein en MOKA-templates | [OKE/](OKE/), [moka-koppelvlakspecificaties/](moka-koppelvlakspecificaties/) |
| Presentaties (Slidev, Npuls huisstijl) | [presentaties/](presentaties/) |
| Validatiescripts | [scripts/](scripts/) |

De koppelingspecificaties per koppeling (OC-P&R, OC-SIS, OC-LMS) leven als interactiepatronen met datamodelschema's in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties); de [keuze-requirements met regelset-payload](architecture/docs/specificatie/student-keuze/keuze-requirements.md) staan onder `architecture/docs/specificatie/student-keuze/`.

## Agent-omgeving

- **Skills** (canoniek [.agents/skills/](.agents/skills/); `.cursor/skills` en `.claude/skills` zijn symbolische links (symlinks)): het overzicht met doel en herkomst staat in het manifest [.agents/skills.json](.agents/skills.json). OKx-specifieke skills en extern gevendorde skills (via `npx skills`) staan gescheiden beschreven; externe skills nooit rechtstreeks bewerken, aanpassingen via een adaptatie-wrapper. Werkwijze: [.agents/README.md](.agents/README.md).
- **Commands** (canoniek [.cursor/commands/](.cursor/commands/); `.claude/commands` is een symbolische link (symlink), zodat zowel Cursor als Claude Code ze vindt): herbruikbare opdrachten, o.a. `adr-opstellen`, `ontwerp-document`, `meeting-notulen-nl`, `release-notes`, `product-flow` en `presentatie`.
- **Rules** ([.cursor/rules/](.cursor/rules/)): altijd geldend: `okx-governance`, `dev-omgeving`, `schrijfstijl`, `product-flow`; gebonden aan bestandstype: `docs-style` (`**/*.md`), `architecture-artifacts` (`architecture/**/*.md`).
- **Hooks** ([.cursor/hooks/](.cursor/hooks/)): installatie-guard richting de dev-container.

### Product-flow (samenvatting)

Elk deliverable doorloopt de keten uit [.agents/skills/okx-product-flow/SKILL.md](.agents/skills/okx-product-flow/SKILL.md): **requirements** opstellen met de business-analyse-persona, **uitwerken** met de specialist-skill, **onafhankelijke review** door tester en specialist in verse subagent-contexten, **itereren** tot beide reviews slagen, en afsluiten met een kort **agent-rapport** in de PR-beschrijving. Start via het command `product-flow`.

## Skills toevoegen of bijwerken

In de dev-container: `npx skills find "<zoekterm>"`, dan `npx skills add <owner/repo> -s <skill> -a cursor -y --copy`. Provenance staat in [skills-lock.json](skills-lock.json) (CLI-formaat); vul daarna het manifest [.agents/skills.json](.agents/skills.json) aan met doel, type en eventuele adaptatie. Bijwerken: `npx skills update`.
