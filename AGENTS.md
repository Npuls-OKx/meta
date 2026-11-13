# AGENTS.md

Basisdocument voor AI-agents (Cursor, Claude Code, Codex en vergelijkbaar) die in deze repository werken. Lees dit eerst; de details staan achter de links.

## Wat is deze repository

OKx-meta is de **publieke kennisbank** van OKx (Npuls, pijler Leren Zonder Drempels): gedeelde kennis, afspraken en conceptuitwerkingen rond **gestandaardiseerde koppelvlakken voor onderwijslogistiek**. Dit is een documentatierepository, geen codebase. Scope start bij mbo (leerroutes 1-3 eerst), hoger onderwijs volgt. Volledige introductie: [README.md](README.md) en [project/](project/).

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
- **Semantiek**: de zeven begrippenfamilies uit het [informatiemodel OKx](architecture/model/informatiemodel/informatiemodel.md) (kwalificatiekader, onderwijskundig kader instelling, onderwijsspecificatie, onderwijsaanbod, onderwijsverbintenis, onderwijsresultaat, resultaatstructuur), met de definities per begrip in de [begrippenlijst](architecture/docs/specificatie/begrippen/begrippenlijst.md); het [begrippenkader van de leerroute-uitwerking](architecture/docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) is de voorloper. De leeruitkomst is de sleutel: specificaties en de resultaatstructuur verwijzen ernaar; resultaten ontstaan op de verbintenis en vormen via de resultaatstructuur het bewijs voor een leeruitkomst. Subtypen voluit met backquotes; geen verzonnen termen. Een koppeling is de informatiestroom tussen twee componenten; een koppelvlak is de verzameling koppelingen van één component.
- **Geen metadatakop (frontmatter)** in deliverables en agent-artifacten: GitHub (git-historie, issues, PR's) is de bron voor auteurschap, datums en traceerbaarheid; verwijs in de tekst ("Relateert aan: #12"). Uitzondering: `SKILL.md`-bestanden en `.mdc`-rules houden hun verplichte metadatakop (naam, beschrijving, `alwaysApply`).

## Harde regels

1. **Raak nooit een `*.archimate`-bestand aan.** Nooit tekstueel mergen; zie [architecture/model/README.md](architecture/model/README.md) en ADR 0010. Een lijn of een wijziging die nog geen besluit is gaat niet het model in maar komt als voorstel op de plaat; zie [okx-voorstel-op-de-hoofdplaat](.agents/skills/okx-voorstel-op-de-hoofdplaat/SKILL.md). Vóór elke model-commit: `python3 tools/scripts/validate-archimate.py`.
2. **Installaties alleen in de dev-container**, nooit op de host ([.cursor/rules/dev-omgeving.mdc](.cursor/rules/dev-omgeving.mdc); een controlescript (hook) bewaakt dit).
3. **1 issue = 1 branch = 1 PR**, feature-branches vanaf `dev`, alleen het OKx-team merget ([CONTRIBUTING.md](CONTRIBUTING.md)).
4. **Een agent merget nooit zelfstandig, en op `Npuls-OKx/Public` merget een agent nooit.** Zie [Mergen](#mergen).
5. **Deliverables volgen de product-flow**: story met gebruiker en waarde, acceptatiecriteria in het issue, plan met tegenlezing, uitwerking met onafhankelijke review, waardevalidatie. Twee stopmomenten, beide bij de opdrachtgever: akkoord op de criteria, en groen licht op het plan. Zie [hieronder](#product-flow-samenvatting).
6. Markdown-deliverables halen de voorcontrole: `python3 tools/scripts/validate-docs.py <pad>`.
7. **Specificeren bovenop OEAPI gaat via een submodule, nooit via een fork.** De OEAPI-specificatie komt binnen als git-submodule op een vastgezet versielabel; het OKx-werk ligt daar als overlay bovenop. Zie [Specificeren bovenop OEAPI](#specificeren-bovenop-oeapi).

## Mergen

Een merge is het moment waarop werk van een voorstel een feit wordt. Vanaf dat moment bouwt een afnemer ertegen, en een fout erin is niet meer terug te nemen zonder dat iemand anders het al heeft gezien.

| Repository | Wat een agent doet |
|---|---|
| `Npuls-OKx/Public` | **Nooit mergen.** Ook niet op verzoek, ook niet met groen licht in een gesprek, ook niet wanneer alle controles slagen. Een agent opent de pull request, zet de review-instructie erin en meldt dat zij klaarstaat |
| `Npuls-OKx/meta` | Alleen mergen wanneer het OKx-team daar in de pull request zelf om vraagt. Uit zichzelf nooit |

Dit geldt ongeacht de rechten die de agent toevallig heeft. Een beveiligingsregel op een branch die een goedkeuring eist, wordt nooit omzeild met een adminsleutel, een geforceerde push of het tijdelijk versoepelen van de regel. Blokkeert zo'n regel de merge, dan is dat de uitkomst: de agent meldt wat er blokkeert en wie het kan oplossen.

Public draagt het releasepakket. Wat daar op `dev` staat is gepubliceerd en leidend, en dat is precies waarom het laatste oordeel bij een mens ligt.

## Specificeren bovenop OEAPI

OKx bouwt voort op de [Open Education API](https://github.com/open-education-api/specification). Dat gebeurt met een **git-submodule op een vastgezet versielabel**, en niet met een fork. Een fork kan de specificatie aanpassen en gaat daarmee uit de pas lopen met de standaard; dat is precies wat OKx wil voorkomen.

De vorm staat in [oeapi-profile-example](https://github.com/open-education-api/oeapi-profile-example) van OEAPI zelf:

```text
OEAPI base specification
+ profile overlay
+ consumer overlay
= gegenereerde OpenAPI-specificatie
```

De basis komt binnen als submodule, met een label in plaats van een branch:

```text
[submodule "base/oeapi"]
	path = base/oeapi
	url = https://github.com/open-education-api/specification.git
```

| | |
|---|---|
| Vastzetten | De submodule staat op een versielabel, bijvoorbeeld `v6.0-rc.3`, zodat de basis niet onder het werk verschuift |
| Meebewegen | Overgaan naar een volgende OEAPI-versie betekent de submodule naar dat nieuwe label verzetten, waarna de overlay opnieuw wordt samengevoegd |
| Samenvoegen | De overlay gaat over de basis heen met `overlay-merger.js`; het resultaat komt in `generated/` en wordt niet met de hand bijgewerkt |
| Afwijken | Een verschil tussen een OKx-eis en wat OEAPI toestaat blijft een signalering richting de standaard, en wordt geen aanpassing in de basis |

De mappenindeling die OEAPI aanraadt:

```text
<profiel-repository>/
├── base/oeapi/source/        de submodule, alleen-lezen
└── <profiel>/
    ├── profile.yaml
    ├── source/
    │   ├── spec.yaml
    │   ├── paths/ schemas/
    │   └── consumers/<consumer>/
    └── generated/
```

Dit vervangt de fork `Npuls-OKx/specification`, die op verzoek van de OEAPI-beheerder is opgeheven. Het werk dat daarin stond is bewaard in `architecture/agent-artifacts/eerste-vertaalpoging-naar-oeapi-met-ai/`, met een leeswijzer die de status erbij zegt.

## Waar vind ik wat

| Wat | Waar |
|---|---|
| Projectcontext, hoofdplaat informatiestromen | [project/](project/) |
| Bronstukken, zoals het projectplan | [project/projectdocumentatie/](project/projectdocumentatie/) |
| Sectorketen: wie maakt wat, van kader tot implementatie | [project/sectorketen-viewpoint.md](project/sectorketen-viewpoint.md) |
| Requirementsboom (opdracht, epics, features, stories) | [Referentiemateriaal/requirementsboom in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md) |
| Architectuurbesluiten (ADR's) | [Referentiemateriaal/adr in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr) |
| ArchiMate-model (niet aanraken) | [architecture/model/](architecture/model/) |
| Een JSON-bericht van buiten in beeld: payload, exportbestand, voorbeeldbericht | skill [okx-json-bericht-in-beeld](.agents/skills/okx-json-bericht-in-beeld/SKILL.md), via `tools/scripts/teken-json-structuur.py` |
| Voorstellen op de hoofdplaat, voor een concept of een sparvraag | [architecture/model/informatiemodel/voorstellen/](architecture/model/informatiemodel/voorstellen/), skill [okx-voorstel-op-de-hoofdplaat](.agents/skills/okx-voorstel-op-de-hoofdplaat/SKILL.md) |
| Meetingverslagen | [architecture/meetings/](architecture/meetings/) |
| Specificaties (leerroute-uitwerking, persona's) | [architecture/docs/specificatie/](architecture/docs/specificatie/) |
| Agent-artifacten (ontwerpen, plannen) | [architecture/agent-artifacts/](architecture/agent-artifacts/) |
| Onderzoek van het team zelf | [architecture/docs/onderzoek/](architecture/docs/onderzoek/) |
| MOKA-sjabloon en de uitwerking erop, gearchiveerd | [archief/MOKA/](archief/MOKA/) |
| Presentaties (Slidev, Npuls huisstijl) | [presentaties/](presentaties/) |
| Validatiescripts en testgevallen | [tools/scripts/](tools/scripts/), [tools/tests/](tools/tests/) |

### Mapindeling

Een map vertelt een nieuwkomer waar hij moet beginnen. Daarom draagt de hoofdmap van een documentmap alleen wat een mens leest, en staat de rest eronder:

| Plek | Wat er staat |
|---|---|
| de hoofdmap | `README.md` als leeswijzer, en de documenten die een mens leest, ook wanneer een script ze schreef |
| `bron/` | wat een mens bewerkt en wat een script leest: regeltabellen, schemas, selectiebestanden |
| `gegenereerd/` | wat een script schrijft, beelden daaronder in `gegenereerd/img/`; hier bewerkt niemand iets met de hand |

Drie keuzes die hierin vastliggen. Het gaat om de **lezer en niet om de maker**: een gegenereerd document dat gelezen wordt staat in de hoofdmap, een gegenereerd gegeven dat niemand opent niet. De naam `gegenereerd` is de **waarschuwing**: wie daar met de hand iets wijzigt, verliest het bij de volgende ronde, en dat is de fout die #411 beschrijft. En **scripts verhuizen niet mee**: zij blijven in [tools/scripts/](tools/scripts/) en [tools/tests/](tools/tests/), zoals #464 ze daar bracht. Een script dat bij een document hoort, wordt in dat document met zijn pad genoemd.

De maat staat in [.cursor/rules/mapindeling.mdc](.cursor/rules/mapindeling.mdc) en wordt afgedwongen door `tools/tests/test_mapindeling.py`. Die test draagt een lijst uitzonderingen in twee soorten: blijvend, met de reden erbij, en wachtend op werk, met het issuenummer erbij. Een uitzondering die wacht op werk en inmiddels voldoet laat de test ook falen, zodat de lijst niet blijft staan nadat het werk gedaan is.

De koppelingspecificaties per koppeling (OC-P&R, OC-SIS, OC-LMS) leven als interactiepatronen met datamodelschema's in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties); de [keuze-requirements met regelset-payload](architecture/docs/specificatie/student-keuze/keuze-requirements.md) staan onder `architecture/docs/specificatie/student-keuze/`.

## Agent-omgeving

- **Skills** (canoniek [.agents/skills/](.agents/skills/); `.cursor/skills` en `.claude/skills` zijn symbolische links (symlinks)): het overzicht met doel en herkomst staat in het manifest [.agents/skills.json](.agents/skills.json). OKx-specifieke skills en extern gevendorde skills (via `npx skills`) staan gescheiden beschreven; externe skills nooit rechtstreeks bewerken, aanpassingen via een adaptatie-wrapper. Werkwijze: [.agents/README.md](.agents/README.md).
- **Commands** (canoniek [.cursor/commands/](.cursor/commands/); `.claude/commands` is een symbolische link (symlink), zodat zowel Cursor als Claude Code ze vindt): herbruikbare opdrachten, o.a. `adr-opstellen`, `ontwerp-document`, `meeting-notulen-nl`, `release-notes`, `product-flow` en `presentatie`.
- **Rules** ([.cursor/rules/](.cursor/rules/)): altijd geldend: `okx-governance`, `dev-omgeving`, `schrijfstijl`, `product-flow`, `vragen-nummeren`, `mapindeling`; gebonden aan bestandstype: `docs-style` (`**/*.md`), `architecture-artifacts` (`architecture/**/*.md`).
- **Hooks** ([.cursor/hooks/](.cursor/hooks/)): installatie-guard richting de dev-container.

### Product-flow (samenvatting)

Elk deliverable doorloopt de keten uit [.agents/skills/okx-product-flow/SKILL.md](.agents/skills/okx-product-flow/SKILL.md). Elke iteratie begint bij waarde voor een benoemde gebruiker en eindigt met de controle of die waarde geleverd is; het doel is een eerste iteratie die waarde levert, niet een volmaakt resultaat.

| Stap | Wat er gebeurt |
|---|---|
| 0 | **Story**: als `<gebruiker>` wil ik `<X>` met als doel dat `<waarde>`. Zonder benoemde gebruiker en waarde begint het werk niet |
| 1 | **Acceptatiecriteria** in gesprek scherp gemaakt en vastgelegd in het issue, met per criterium een testgeval. *Stopmoment: akkoord van de opdrachtgever* |
| 2 | **Implementatieplan**, autonoom |
| 3 | **Tegenlezing van het plan** door een onafhankelijke agent in een verse context, die afkeurt op vier gronden en niet op volledigheid of smaak |
| 4 | *Stopmoment: groen licht van de opdrachtgever* |
| 5 | **Uitwerken** met de specialist-skill, daarna onafhankelijke review door tester, specialist en schrijfstijl in verse subagent-contexten |
| 6 | **Waardevalidatie**: levert het geleverde de waarde uit de story. Vervolgpunten worden kleine iteraties |

Een ultracode-sessie of een workflow is uitwerking en geen verkenning: stopmoment 1 geldt daar onverkort, dus eerst sparren over de stories en de criteria. Ook een verkennende workflow legt zijn vraag eerst voor, er start geen tweede workflow op hetzelfde onderwerp voordat de eerste gelezen is, en voor een fan-out staat vast welke branch of structuur normatief is. De lus is begrensd op drie ronden per poort; daarna escaleert de agent met de openstaande bevindingen. Het verloop staat in het issue of in het **agent-rapport** in de PR-beschrijving.

Een titel van een issue of pull request opent met het gebied, dan het onderdeel, dan het object dat verandert met de bewerking erbij: `Informatiemodel voorbeeld, fase 3: onderwijslocatie object met aanbodgedreven onderwijsmodel voorbeeldvariant toegevoegd`. Het gebied is een naam die in de repository terugkomt, geen scriptnaam; het derde deel noemt het object en wat ermee gebeurde, en niet het gevolg. Korter is beter; tachtig tekens is de richting en niet de grens.

Elke PR-beschrijving opent met een samenvatting van hoogstens vijftien zinnen: het sluitwoord `Closes #123` als context, een genummerde lijst van wat er is opgeleverd met per regel een link naar het document of de plaat zelf, en of de product-flow is doorlopen. Heeft de oplevering structuur, dan hoort daar een visuele uitsplitsing bij (mermaid of ascii), volgens werkafspraak 3. Daaronder een genummerde **review-instructie** die zegt wat van dat werk een mens moet beoordelen, in welke volgorde, en welk bronmateriaal hij kan overslaan. Daaronder de acceptatiecriteria met hun testuitkomst, de openstaande vragen en gevonden fouten, en de issues die daaruit zijn aangemaakt. Een agent mag zelf een issue aanmaken voor wat hij vindt, uitsluitend in `Npuls-OKx/meta` en altijd met het label `gevondenDoorAI`. Een opmerking uit een reviewronde wordt daarentegen altijd twee issues: de interactie in het repository waar de reviewer meeleest, met de opmerking letterlijk erin en de inbrenger getagd, en de werkbrief in meta. Dat interactie-issue draagt vijf koppen van een woord (aanleiding, inbreng, observaties, actiepunten, vervolg), is geschreven in de ik-vorm, en krijgt alleen een story wanneer de inbrenger een concrete wijziging vraagt met een rol die bestaat. Een leverancier spreekt voor zijn product en niet voor de sector: houd uit elkaar wat een product vandaag doet, wat een component moet kunnen, en wat OKx als grootst gemene deler vastlegt. Een applicatie is daarbij geen applicatiecomponent, en een implementatiefeit geen ontwerpargument. Daarna kan de pull request sluiten. Zo'n issue kent drie uitgangen: de inbrenger sluit hem omdat het antwoord volstaat, hij gaat met het label `agenda kerngroep techniek` naar een sessie, of OKx sluit hem met de reden erbij. Het antwoord komt altijd onder het issue te staan, ook als het al in de pull request stond, en het issue gaat op naam van de inbrenger. Een label per sessie komt er niet: dat label is stabiel en de datum staat in de comment. De vorm staat in [.agents/skills/okx-product-flow/SKILL.md](.agents/skills/okx-product-flow/SKILL.md). Een werkwijze-issue draagt wel een story en krijgt geen plek in de requirementsboom. Start via het command `product-flow`.

## Skills toevoegen of bijwerken

In de dev-container: `npx skills find "<zoekterm>"`, dan `npx skills add <owner/repo> -s <skill> -a cursor -y --copy`. Provenance staat in [skills-lock.json](skills-lock.json) (CLI-formaat); vul daarna het manifest [.agents/skills.json](.agents/skills.json) aan met doel, type en eventuele adaptatie. Bijwerken: `npx skills update`.
