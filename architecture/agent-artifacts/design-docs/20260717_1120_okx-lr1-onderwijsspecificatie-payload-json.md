---
created: "2026-07-17T11:20:30+00:00"
updated: "2026-07-20T09:38:15+00:00"
human_authors:
  - "Niek Derksen (architect, OKx)"
human_reviewers: []
agent_command: "ontwerp-document"
agent_model: "Claude Opus 4.8 (Claude Code)"
related_issues: ["#119", "#105", "#84", "#120", "#110"]
source_paths:
  - "architecture/docs/specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md"
  - "architecture/docs/kwalificatiedossier/Apothekersassistent-2.md"
  - ".cursor/skills/mbo-informatie-modelleur/SKILL.md"
  - "architecture/agent-artifacts/design-docs/20260716_1414_okx-lr1-keuzedelen-requirements-voorstel.md"
  - "architecture/dr/0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md"
  - "architecture/dr/0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md"
  - "doc/OKx_PDCA cyclus onderwijsontwerp.md"
notes: "Async sessies: bij elke bewerking 'updated' bijwerken en auteurs aanvullen indien meerdere mensen betrokken. Concept-payload (grofmazig, fase 1-2); attribuutwaarden indicatief. Regels staan los van de onderwijsspecificatie (zie #84/#120). Enums zijn concept en te bevestigen. OEAPI-binding is signalering."
---

# Onderwijsspecificatie als JSON-payload (OC naar P)

Context: koppeling OC naar P (onderwijscatalogus naar planning), vroege processtap "kwalificatiekader analyseren". Scenario: LR1 (Apothekersassistent, Crebo-dossier 23450, kwalificatie 27141). Niveau: concept-payload, grofmazig (fase 1-2). Status: concept. Relateert aan: #119, #105, #84, #120.

## Inhoudsopgave

1. [Inleiding](#1-inleiding)
2. [Doel](#2-doel)
3. [Scope](#3-scope)
4. [Context](#4-context)
5. [Voorstel: hoe drukken we de gelaagdheid uit in JSON?](#5-voorstel-hoe-drukken-we-de-gelaagdheid-uit-in-json)
6. [Enumeraties (concept)](#6-enumeraties-concept)
7. [Uitwerking van de payload](#7-uitwerking-van-de-payload)
8. [Onderwijsspecificatie lifecycle (versionering en manifest)](#8-onderwijsspecificatie-lifecycle-versionering-en-manifest)
9. [Open vragen en signaleringen](#9-open-vragen-en-signaleringen)

## 1. Inleiding

Issue #119 vraagt een eerste payload-uitwerking in JSON van de onderwijsspecificatie-boom voor LR1-3, zodat we kunnen toetsen of die vorm in latere versies overeind blijft. Dit document geeft die vorm en de ontwerpkeuze eronder: hoe leg je de gelaagdheid (de geneste specificatie) generiek vast in JSON.

De ArchiMate-view "01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model" gebruikt nog niet het huidige begrippenkader (opleidingsspecificatie, programmaspecificatie, enzovoort). We gebruiken de ankertabel (§3.2.6) uit het OKx OEAPI consumer-profiel, het kwalificatiedossier Apothekersassistent, en de datamodel-schets uit #119.

## 2. Doel

- Een eerste, toetsbare JSON-vorm van de onderwijsspecificatie-boom voor LR1-3.
- Een generieke en herbruikbare ontwerpkeuze voor gelaagdheid en voor keuzeregels.
- Invoer voor de berichtspecificatie (AMIGO-stap 5) en het OEAPI-profiel.

Buiten scope: definitieve OEAPI-binding, endpoints, het aanbod (planbaar of geroosterd resultaat), en de interne structuur van de ruleset (die staat in #84 en #120).

## 3. Scope

- Koppeling: OC naar P, vroege processtap "kwalificatiekader analyseren".
- Leerroutes: LR1 uitgewerkt. LR2 en LR3 volgen als verschil (delta); boomstructuur gelijk, een handvol attributen wijzigt.
- Diepte: `opleidingsspecificatie`, `opleidingsprogrammaspecificatie`, `onderwijseenheidspecificatie`, `leeronderdeelspecificatie`. Geen harde grens. De `lesspecificatie` valt buiten scope; PMO realiseert dat niet.
- Fase: grofmazig ontwerp (fase 1-2). Waarden zijn indicatief. Generieke onderdelen (taal, rekenen, burgerschap, Engels) vallen buiten deze payload.

## 4. Context

Ankertabel (§3.2.6), specificatie-kolom. Conceptniveaus, bron in het kwalificatiekader en OEAPI-mapping:

| Conceptniveau (`educationSpecificationType`) | Bron in kwalificatiekader | OEAPI-mapping (indicatief) |
|---|---|---|
| `opleidingsspecificatie` | Kwalificatiedossier | EducationSpecification (program) |
| `opleidingsprogrammaspecificatie` | Kwalificatie | Programme |
| `onderwijseenheidspecificatie` | Kerntaak | Course |
| `leeronderdeelspecificatie` | Werkproces | LearningComponent |
| `keuzedeelruimtespecificatie` | ruimte binnen kwalificatie | (afgeleid, geen 1:1 OEAPI-object) |
| `toetsonderdeelspecificatie` | toetsing | TestComponent |
| `examenplanspecificatie` | OER, summatieve resultaatstructuur | (aparte uitwerking) |
| `lesspecificatie` (buiten scope) | beleid instelling | LearningComponent (lesson) |

Belangrijke correctie ten opzichte van de vorige versie: de **kwalificatie ligt niet op root-niveau**. De opleiding draagt het kwalificatiedossier als leeruitkomst (`type: kwalificatiedossier`, code 23450). De kwalificatie (27141) hoort op programma-niveau (`type: kwalificatie`).

Vier eigenschappen die de gelaagdheid bepalen:

- Recursie: elk niveau is hetzelfde type object en verwijst naar zijn ouder (`parent`).
- Twee programma-lagen, beide een `opleidingsprogrammaspecificatie`: t.b.v. leerweg (BOL, BBL) en daaronder t.b.v. doelgroep (regulier, zijinstromer, hybride, of organisatiespecifiek zoals een ziekenhuis-BBL). De kwalificatie-inhoud (kerntaken, werkprocessen) hangt onder de doelgroep-laag.
- Keuzeruimte is een eigen, herbruikbare `keuzedeelruimtespecificatie`, geen los veld.
- Regels staan los van de specificatie. Een specificatie verwijst via `ruleSetRefs` naar een of meer rulesets. De ruleset bepaalt welke keuzedelen kiesbaar zijn. Zie #84 en #120.

```mermaid
flowchart TD
    OPL["opleidingsspecificatie<br/>Apothekersassistent (dossier 23450)"]
    PBOL["opleidingsprogrammaspecificatie<br/>leerweg BOL"]
    PBBL["opleidingsprogrammaspecificatie<br/>leerweg BBL"]
    G1["opleidingsprogrammaspecificatie<br/>doelgroep Regulier BOL"]
    G2["opleidingsprogrammaspecificatie<br/>doelgroep Zijstroom / Hybride"]
    G4["opleidingsprogrammaspecificatie<br/>doelgroep BBL Ziekenhuis 12"]
    OE["onderwijseenheidspecificatie<br/>Kerntaak B1-K1"]
    LO["leeronderdeelspecificatie<br/>Werkproces B1-K1-W1"]
    KR["keuzedeelruimtespecificatie<br/>720 SBU"]
    RS["ruleSet<br/>welke keuzedelen kiesbaar"]
    KD1["opleidingsprogrammaspecificatie<br/>keuzedeelprogramma Ondernemerschap"]
    KD2["opleidingsprogrammaspecificatie<br/>keuzedeelprogramma Ruimtelijk inzicht"]
    OPL --> PBOL
    OPL --> PBBL
    PBOL --> G1
    PBOL --> G2
    PBBL --> G4
    G1 --> OE
    OE --> LO
    G1 --> KR
    KR -. ruleSetRefs .-> RS
    RS -. verwijst naar .-> KD1
    RS -. verwijst naar .-> KD2
    KD2 --> KDOE["onderwijseenheidspecificatie"]
    KDOE --> KDLO["leeronderdeelspecificatie"]
```

## 5. Voorstel: hoe drukken we de gelaagdheid uit in JSON?

| Optie | Vorm | Voordeel | Nadeel |
|---|---|---|---|
| A. Pure nesting | children-arrays, alles inline | Simpel | Hergebruik wordt gedupliceerd |
| B. Nesting + referenties | genest, hergebruik via uuid | Minder duplicatie | Twee relatievormen door elkaar |
| C. Recursief plat + parent | uniforme lijst, relatie via `parent` | Elk object gelijk, generiek, herbruikbaar, uitlijnbaar met OEAPI `EducationSpecification.parent` | Boom minder direct leesbaar |

Voorstel: optie C.

Ontwerpkeuzes:

- Eén uniform type. Alle specificaties staan in een platte lijst `educationSpecifications`. Elke specificatie heeft een `parent` (uuid; `null` op de root). De boom reconstrueer je door `parent` te volgen; een geneste weergave is daaruit af te leiden.
- Discriminator `educationSpecificationType` bepaalt het niveau.
- Verankering via leeruitkomst (vervangt `primaryCode`). Elke specificatie verwijst naar een leeruitkomst met een `type`. Nu de kwalificatiekader-typen (kwalificatiedossier, kwalificatie, kerntaak, werkproces, keuzedeel); later uitbreidbaar met een leeruitkomst-standaard zoals CompetentNL (ADR 0003, 0004).
- Id's zijn UUID's.
- Versionering per specificatie met semver (`MAJOR.MINOR.PATCH`). MAJOR = wijziging die betekenis of uitkomst raakt (leeruitkomsten, structuur, studielast), MINOR = additief zonder bestaande betekenis te breken, PATCH = correctie. Temporele geldigheid apart via `validFrom`/`validTo` en cohort, niet als versienummer.
- Identiteit los van versie (uitgangspunt, memo PR #110). `educationSpecificationId` is stabiel; `version` verandert bij een wijziging binnen dezelfde identiteit. Een fundamentele wijziging (nieuw kwalificatiedossier, nieuwe wettelijke eisen) is een nieuwe specificatie met een nieuw id, niet alleen een MAJOR-bump.
- Kwalificatie op programma-niveau, dossier op opleiding-niveau (zie §4).
- `programmaLaag` onderscheidt leerweg- en doelgroep-programma. Beide zijn `programma`.
- `parent` draagt twee betekenissen: onderdeel-van (additief, bv. kerntaak onder programma) en variant-van (alternatief, bv. doelgroep onder leerweg). De aggregatie-invariant geldt alleen voor onderdeel-van.
- Niveau, leeruitkomsten en leerroute zijn afleidbaar uit de boomstructuur, niet als losse specificatie-velden. Het NLQF-niveau hangt aan de leeruitkomst. Wie een bepaalde set kerntaken en werkprocessen heeft afgerond, voldoet aan de kwalificatie. Leerroute-typen zijn indicatief voor wat mogelijk wordt en horen niet in het datamodel. Leeruitkomsten worden naar verwachting later flexibeler (ADR 0003, 0004).
- Keuzeruimte is een eigen specificatie (`keuzedeelruimte`) met studielast, herbruikbaar.
- Regels los van de onderwijsspecificatie. `ruleSetRefs` op een specificatie verwijst naar losse `ruleSets`. De ruleset draagt de kiesbaarheid (welke keuzedelen) en de voorwaarde vooraf (prerequisite). Interne structuur van de ruleset: #84 en #120.
- Elke specificatie kan `ruleSetRefs` hebben (generiek), niet alleen de keuzeruimte.
- Keuzedelen zijn zelfstandige programma-specificaties (`parent: null`), zelf opgebouwd als programma naar onderwijseenheid naar leeronderdeel. Herbruikbaar over opleidingen (N:M via ruleset-referenties).
- Aggregatie-invariant: `studyLoad` telt bottom-up op binnen onderdeel-van (SOM children = ouder). Niet over varianten (leerweg, doelgroep).

## 6. Enumeraties (concept)

Concept en te bevestigen. Open sets zijn als zodanig gemarkeerd.

| Veld | Toegestane waarden |
|---|---|
| `educationSpecificationType` | `opleidingsspecificatie`, `opleidingsprogrammaspecificatie`, `onderwijseenheidspecificatie`, `leeronderdeelspecificatie`, `keuzedeelruimtespecificatie`, `toetsonderdeelspecificatie` (examinering/toetsing, OEAPI TestComponent), `examenplanspecificatie` en `resultaateenheidspecificatie` (resultaatstructuur, aparte uitwerking) |
| `manifest[].relatie` | `onderdeel` (additief), `variant` (alternatief), `referentie` (gepinde verwijzing) |
| `status` | `concept`, `vastgesteld`, `gepubliceerd`, `gedeactiveerd`, `vervallen`, `gearchiveerd` |
| `version` | semver `MAJOR.MINOR.PATCH` (bv. `0.1.0`) |
| `validFrom` / `validTo` | datum; geldigheidsperiode. Meerdere versies kunnen gelijktijdig actief zijn |
| `curriculumType` | `nominaal`, `hybride`, `flexibel` |
| `programmeType` | `diplomaprogramma`, `keuzedeelprogramma`, `certificaatprogramma` (open) |
| `programmaLaag` | `leerweg`, `doelgroep` |
| `leerweg` | `BOL`, `BBL` |
| `doelgroep` | `regulier`, `zijinstromer`, `hybride`, `organisatiespecifiek` (open) || `timeAllocation` (tijdsverdeling) | `BOT` (begeleide onderwijstijd), `OOT` (onbegeleide onderwijstijd) |
| `studyLoad.unit` | `SBU`, `EC` |
| `leeruitkomst.type` | `kwalificatiedossier`, `kwalificatie`, `kerntaak`, `werkproces`, `keuzedeel` (open, uitbreidbaar met een leeruitkomst-standaard zoals CompetentNL) |
| `keuzedeelKlasse` | `algemeen-verbredend`, `beroepsspecifiek-verdiepend` (open, uitbreidbaar; #84 R10) |
| `leeruitkomst.nlqfNiveau` | `1` t/m `8` (NLQF, geldt voor alle sectoren) |

## 7. Uitwerking van de payload

Grofmazig, LR1, indicatief. `studyLoad` telt bottom-up op binnen onderdeel-van (kerntaken 2000 + 1200 + 880 = 4080; plus keuzeruimte 720 = 4800 onder Regulier BOL). Programma-varianten (leerweg BOL/BBL, doelgroep regulier/zijinstromer/hybride) zijn alternatieven, geen optelling. De inhoud hangt hier onder één doelgroep (Regulier BOL); de andere varianten zijn leeg (illustratief). Keuzedelen zijn illustratief (de prerequisite Wiskunde 1 voor Ruimtelijk inzicht komt uit #84).

### 7.1 Boomstructuur met attributen (ERD)

Alle objecten zijn hetzelfde type (`EducationSpecification`), gespecialiseerd via `educationSpecificationType`. Hieronder per laag getoond met de belangrijkste attributen. `onderdeel_van` = additief (studielast telt op), `variant_van` = alternatief. Elke entiteit draagt daarnaast `version` (semver); voor de leesbaarheid niet in elke box herhaald.

```mermaid
erDiagram
    OPLEIDINGSSPECIFICATIE ||--o{ OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG : variant_van
    OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG ||--o{ OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP : variant_van
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP ||--o{ ONDERWIJSEENHEIDSPECIFICATIE : onderdeel_van
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP ||--|| KEUZEDEELRUIMTESPECIFICATIE : bevat
    ONDERWIJSEENHEIDSPECIFICATIE ||--o{ LEERONDERDEELSPECIFICATIE : onderdeel_van
    KEUZEDEELRUIMTESPECIFICATIE }o--o{ RULESET : ruleSetRefs
    RULESET }o--o{ KEUZEDEELPROGRAMMASPECIFICATIE : kiesbaar
    KEUZEDEELPROGRAMMASPECIFICATIE ||--o{ ONDERWIJSEENHEIDSPECIFICATIE : onderdeel_van

    OPLEIDINGSSPECIFICATIE {
        uuid educationSpecificationId PK
        string educationSpecificationType "opleidingsspecificatie"
        uuid parent "null"
        object leeruitkomst "type=kwalificatiedossier, code=23450, nlqfNiveau=4"
        string name
        string curriculumType
        string version
        date validFrom
        date validTo
        object studyLoad "waarde + SBU"
        array manifest "pins: id + version + relatie"
        string status
    }
    OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG {
        uuid educationSpecificationId PK
        string educationSpecificationType "opleidingsprogrammaspecificatie"
        uuid parent FK "opleiding"
        object leeruitkomst "type=kwalificatie, code=27141"
        string programmaLaag "leerweg"
        string leerweg "BOL of BBL"
        string programmeType "diplomaprogramma"
        object studyLoad
    }
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP {
        uuid educationSpecificationId PK
        string educationSpecificationType "opleidingsprogrammaspecificatie"
        uuid parent FK "leerweg-programma"
        string programmaLaag "doelgroep"
        string doelgroep "regulier, zijinstromer, hybride, organisatiespecifiek"
        string leerweg
        string curriculumType
        object organisatie "optioneel, bv. Ziekenhuis 12"
        string cohort
        date startdatum
        date validFrom
        date validTo
        object studyLoad
        array manifest "pins: id + version + relatie"
    }
    ONDERWIJSEENHEIDSPECIFICATIE {
        uuid educationSpecificationId PK
        string educationSpecificationType "onderwijseenheidspecificatie"
        uuid parent FK "programma of keuzedeelprogramma"
        object leeruitkomst "type=kerntaak"
        string name
        object studyLoad
    }
    LEERONDERDEELSPECIFICATIE {
        uuid educationSpecificationId PK
        string educationSpecificationType "leeronderdeelspecificatie"
        uuid parent FK "onderwijseenheid"
        object leeruitkomst "type=werkproces"
        string name
        string timeAllocation "BOT of OOT"
        object studyLoad
    }
    KEUZEDEELRUIMTESPECIFICATIE {
        uuid educationSpecificationId PK
        string educationSpecificationType "keuzedeelruimtespecificatie"
        uuid parent FK "doelgroep-programma"
        object studyLoad "keuzeruimte in SBU"
        array ruleSetRefs FK "naar RULESET"
    }
    KEUZEDEELPROGRAMMASPECIFICATIE {
        uuid educationSpecificationId PK
        string educationSpecificationType "opleidingsprogrammaspecificatie"
        uuid parent "null, zelfstandig"
        object leeruitkomst "type=keuzedeel"
        string programmeType "keuzedeelprogramma"
        string keuzedeelKlasse "algemeen-verbredend of beroepsspecifiek-verdiepend"
        object studyLoad
    }
    RULESET {
        uuid ruleSetId PK
        string name
        uuid appliesTo FK "keuzedeelruimte"
        array regels "kiesbaar + voorwaardeVooraf (prerequisite)"
    }
```

### 7.2 Payload (JSON)

```json
{
  "educationSpecifications": [
    {
      "educationSpecificationId": "79736830-1c5c-470f-b2c2-005029c96733",
      "educationSpecificationType": "opleidingsspecificatie",
      "version": "0.1.0",
      "parent": null,
      "leeruitkomst": { "type": "kwalificatiedossier", "code": "23450", "nlqfNiveau": 4 },
      "name": "Apothekersassistent",
      "description": "Opleiding tot apothekersassistent. Domein Zorg en welzijn.",
      "curriculumType": "nominaal",
      "status": "concept",
      "validFrom": "2026-08-01",
      "validTo": null,
      "studyLoad": { "value": 4800, "unit": "SBU" },
      "manifest": [
        { "educationSpecificationId": "5ef37812-ae0f-4232-904f-451b9928e45e", "version": "0.1.0", "relatie": "variant" },
        { "educationSpecificationId": "93f3c239-5baa-4d96-a56f-728c09d7fefe", "version": "0.1.0", "relatie": "variant" }
      ]
    },
    {
      "educationSpecificationId": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "79736830-1c5c-470f-b2c2-005029c96733",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "Apothekersassistent, leerweg BOL",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "leerweg",
      "leerweg": "BOL",
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "93f3c239-5baa-4d96-a56f-728c09d7fefe",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "79736830-1c5c-470f-b2c2-005029c96733",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "Apothekersassistent, leerweg BBL",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "leerweg",
      "leerweg": "BBL",
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "Regulier BOL",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "doelgroep",
      "doelgroep": "regulier",
      "leerweg": "BOL",
      "curriculumType": "nominaal",
      "cohort": "2026",
      "startdatum": "2026-09-01",
      "validFrom": "2026-09-01",
      "validTo": null,
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" },
      "manifest": [
        { "educationSpecificationId": "402c2342-d897-4df4-a667-7fc5bd930944", "version": "0.1.0", "relatie": "onderdeel" },
        { "educationSpecificationId": "aa0a8af1-d383-4981-8a0f-6ec2ba4e6283", "version": "0.1.0", "relatie": "onderdeel" },
        { "educationSpecificationId": "f686a286-d555-4eda-bd22-001c5b60e4dc", "version": "0.1.0", "relatie": "onderdeel" },
        { "educationSpecificationId": "fb5be5ae-faa0-4b4b-8085-474fce9aae08", "version": "0.1.0", "relatie": "onderdeel" }
      ]
    },
    {
      "educationSpecificationId": "82de8b94-8a43-4ccf-8114-043f8f9bc2f8",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "Zijstroom/LLO BOL (illustratief)",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "doelgroep",
      "doelgroep": "zijinstromer",
      "leerweg": "BOL",
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "685dc983-1597-46d5-9935-001d7e3715ca",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "Hybride BOL (illustratief)",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "doelgroep",
      "doelgroep": "hybride",
      "leerweg": "BOL",
      "curriculumType": "hybride",
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "23d18a33-dafc-47e7-a60e-84cd31d27613",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "93f3c239-5baa-4d96-a56f-728c09d7fefe",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "Regulier BBL (illustratief)",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "doelgroep",
      "doelgroep": "regulier",
      "leerweg": "BBL",
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "c295478c-c1c1-4647-9550-dc728aff1a7c",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": "93f3c239-5baa-4d96-a56f-728c09d7fefe",
      "leeruitkomst": { "type": "kwalificatie", "code": "27141" },
      "name": "BBL Ziekenhuis 12 (illustratief)",
      "programmeType": "diplomaprogramma",
      "programmaLaag": "doelgroep",
      "doelgroep": "organisatiespecifiek",
      "organisatie": { "naam": "Ziekenhuis 12" },
      "leerweg": "BBL",
      "toelichting": "BBL-variant, 4 dagen werken en 1 dag school.",
      "status": "concept",
      "studyLoad": { "value": 4800, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "402c2342-d897-4df4-a667-7fc5bd930944",
      "educationSpecificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parent": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "leeruitkomst": { "type": "kerntaak", "code": "B1-K1" },
      "name": "Biedt farmaceutische patiëntenzorg",
      "studyLoad": { "value": 2000, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "aa0a8af1-d383-4981-8a0f-6ec2ba4e6283",
      "educationSpecificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parent": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "leeruitkomst": { "type": "kerntaak", "code": "B1-K2" },
      "name": "Voert logistieke taken uit in de apotheek",
      "studyLoad": { "value": 1200, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "f686a286-d555-4eda-bd22-001c5b60e4dc",
      "educationSpecificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parent": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "leeruitkomst": { "type": "kerntaak", "code": "B1-K3" },
      "name": "Werkt mee aan kwaliteit en deskundigheid",
      "studyLoad": { "value": 880, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "327c8263-3516-4b5a-8d57-c16241ec008d",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "402c2342-d897-4df4-a667-7fc5bd930944",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K1-W1" },
      "name": "Neemt de zorg-/adviesvraag in behandeling",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 600, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "29522e42-fb32-46d2-a504-0869831f941f",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "402c2342-d897-4df4-a667-7fc5bd930944",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K1-W2" },
      "name": "Voert medicatiebewaking uit",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 500, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "db4ae6c8-7dda-45ef-953e-a4e8bfc557f8",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "402c2342-d897-4df4-a667-7fc5bd930944",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K1-W3" },
      "name": "Verstrekt (zelfzorg)medicijnen en/of hulpmiddelen",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 500, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "2a4e31d4-2b27-401f-a28c-f152b0d502db",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "402c2342-d897-4df4-a667-7fc5bd930944",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K1-W4" },
      "name": "Geeft informatie en advies over medicijngebruik, gezondheid en leefstijl",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 400, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "c36d635f-7b1c-4459-a035-adfca96768da",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "aa0a8af1-d383-4981-8a0f-6ec2ba4e6283",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K2-W1" },
      "name": "Maakt medicijnen klaar voor gebruik en/of aflevering",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 700, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "c5262133-0873-44a7-9b54-d15004c9d940",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "aa0a8af1-d383-4981-8a0f-6ec2ba4e6283",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K2-W2" },
      "name": "Houdt de voorraad bij",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 500, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "f956bad0-f49c-4b5c-a040-c084229b23e0",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "f686a286-d555-4eda-bd22-001c5b60e4dc",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K3-W1" },
      "name": "Draagt bij aan sociaal veilige werkomgeving",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 280, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "6d5b468e-ceac-47df-b221-d09dce4cce3c",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "f686a286-d555-4eda-bd22-001c5b60e4dc",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K3-W2" },
      "name": "Evalueert de werkzaamheden en ontwikkelt zichzelf als professional",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 300, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "90245c2e-2f2d-4d58-b770-24427e717f97",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "f686a286-d555-4eda-bd22-001c5b60e4dc",
      "leeruitkomst": { "type": "werkproces", "code": "B1-K3-W3" },
      "name": "Stemt de farmaceutische zorgverlening af",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 300, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "educationSpecificationType": "keuzedeelruimtespecificatie",
      "version": "0.1.0",
      "parent": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "name": "Keuzedeelruimte",
      "description": "Ruimte binnen de kwalificatie die met keuzedelen wordt ingevuld.",
      "studyLoad": { "value": 720, "unit": "SBU" },
      "ruleSetRefs": ["e4037953-17d6-40a4-9e59-92ec1f9c19a8"],
      "manifest": [
        { "educationSpecificationId": "6a5ec549-da21-4034-b0cd-a709731de2eb", "version": "0.1.0", "relatie": "referentie" },
        { "educationSpecificationId": "ecf4a1ce-8fe4-4ed2-82d4-6c743862094e", "version": "0.1.0", "relatie": "referentie" },
        { "educationSpecificationId": "65342d39-7716-4d33-a5cd-a255cc1a2feb", "version": "0.1.0", "relatie": "referentie" }
      ]
    },
    {
      "educationSpecificationId": "6a5ec549-da21-4034-b0cd-a709731de2eb",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": null,
      "leeruitkomst": { "type": "keuzedeel", "code": "K0072" },
      "name": "Keuzedeel Ondernemerschap",
      "programmeType": "keuzedeelprogramma",
      "keuzedeelKlasse": "algemeen-verbredend",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "7d4d9a10-bb71-4d05-9b30-0b79d7144be1",
      "educationSpecificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parent": "6a5ec549-da21-4034-b0cd-a709731de2eb",
      "leeruitkomst": { "type": "kerntaak", "code": "K0072-K1" },
      "name": "Zet een onderneming op in de zorg (indicatief)",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "b4ec6046-fae8-442e-91df-163c5e9e72f2",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "7d4d9a10-bb71-4d05-9b30-0b79d7144be1",
      "leeruitkomst": { "type": "werkproces", "code": "K0072-K1-W1" },
      "name": "Stelt een ondernemingsplan op (indicatief)",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "ecf4a1ce-8fe4-4ed2-82d4-6c743862094e",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": null,
      "leeruitkomst": { "type": "keuzedeel", "code": "K0000-ri" },
      "name": "Keuzedeel Ruimtelijk inzicht (illustratief)",
      "programmeType": "keuzedeelprogramma",
      "keuzedeelKlasse": "beroepsspecifiek-verdiepend",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "20f1099a-949f-40b8-b893-1aa5bfea3f4c",
      "educationSpecificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parent": "ecf4a1ce-8fe4-4ed2-82d4-6c743862094e",
      "leeruitkomst": { "type": "kerntaak", "code": "K0000-ri-K1" },
      "name": "Past ruimtelijk inzicht toe (illustratief)",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "9e74eb44-1155-4882-8eb4-24e58a9146b2",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "20f1099a-949f-40b8-b893-1aa5bfea3f4c",
      "leeruitkomst": { "type": "werkproces", "code": "K0000-ri-K1-W1" },
      "name": "Interpreteert ruimtelijke figuren (illustratief)",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "65342d39-7716-4d33-a5cd-a255cc1a2feb",
      "educationSpecificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parent": null,
      "leeruitkomst": { "type": "keuzedeel", "code": "K0000-w1" },
      "name": "Keuzedeel Wiskunde 1 (illustratief)",
      "programmeType": "keuzedeelprogramma",
      "keuzedeelKlasse": "beroepsspecifiek-verdiepend",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "729972d9-b83a-418f-91ec-10db1ecb56da",
      "educationSpecificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parent": "65342d39-7716-4d33-a5cd-a255cc1a2feb",
      "leeruitkomst": { "type": "kerntaak", "code": "K0000-w1-K1" },
      "name": "Beheerst basale wiskunde (illustratief)",
      "studyLoad": { "value": 240, "unit": "SBU" }
    },
    {
      "educationSpecificationId": "6952e0af-eca5-422e-aa6a-69cfd38f97c9",
      "educationSpecificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parent": "729972d9-b83a-418f-91ec-10db1ecb56da",
      "leeruitkomst": { "type": "werkproces", "code": "K0000-w1-K1-W1" },
      "name": "Rekent met verhoudingen en formules (illustratief)",
      "timeAllocation": "BOT",
      "studyLoad": { "value": 240, "unit": "SBU" }
    }
  ],
  "ruleSets": [
    {
      "ruleSetId": "e4037953-17d6-40a4-9e59-92ec1f9c19a8",
      "version": "0.1.0",
      "name": "Kiesbare keuzedelen voor Apothekersassistent (LR1)",
      "description": "Bepaalt welke keuzedelen in de keuzedeelruimte kiesbaar zijn. Regelstructuur wordt uitgewerkt in #84 en #120; onderstaande regels zijn indicatief.",
      "appliesTo": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "regels": [
        { "type": "kiesbaar", "bereik": "alle keuzedelen met keuzedeelKlasse algemeen-verbredend" },
        { "type": "kiesbaar", "keuzedeel": "ecf4a1ce-8fe4-4ed2-82d4-6c743862094e",
          "voorwaardeVooraf": [ { "vereist": "65342d39-7716-4d33-a5cd-a255cc1a2feb", "status": "afgerond" } ] }
      ]
    }
  ]
}
```

De voorwaarde vooraf (Ruimtelijk inzicht vereist Wiskunde 1) staat nu in de ruleset, niet in de specificatie. Zo blijft de regel los van het item, conform #84 R2 en #120.

## 8. Onderwijsspecificatie lifecycle (versionering en manifest)

De volledige lifecycle (classificatie van wijzigingen, acceptatie, deactiveren, migratie) staat in de aparte uitwerking [lifecycle en versionering](20260720_0832_okx-lr1-lifecycle-versionering.md). Hier alleen de mechaniek die de payload zelf raakt.

**Snapshot als manifest.** De payload zoals geleverd is een snapshot: elke specificatie staat erin met haar `version`. De versie van de `opleidingsspecificatie` is de manifest- of release-versie; de versies van de onderdelen staan inline. Een geleverde payload pint zo precies één samenhangende set (id, version).

**Manifest op elk niveau.** Niet alleen de `opleidingsspecificatie`. Elk niveau met onderdelen is een manifest voor die onderdelen; dezelfde logica geldt recursief: een `opleidingsprogrammaspecificatie` pint haar `onderwijseenheidspecificatie`s, een `onderwijseenheidspecificatie` pint haar `leeronderdeelspecificatie`s.

**Afgeleide versie, impact-gedreven propagatie.** Een niveau versioneert wanneer zijn samenstelling wijzigt of een onderliggende wijziging zijn afhankelijkheid breekt (leeruitkomsten, weging, diploma-eligibility). Een child-bump propageert dus niet automatisch omhoog.

**Voorbeeld.** Uitgangspunt: de `opleidingsprogrammaspecificatie` (doelgroep Regulier BOL) `2.1` pint `onderwijseenheidspecificatie` A `1.1` en B `1.2`. A wijzigt naar `2.0` (MAJOR op A):

| Breekt A de `opleidingsprogrammaspecificatie`? | `opleidingsprogrammaspecificatie` | Manifest pint |
|---|---|---|
| Ja (leeruitkomst, weging of diploma-eligibility) | `2.1` naar `3.0` (MAJOR) | A `2.0`, B `1.2` |
| Nee (interne herstructurering van A) | `2.1` naar `2.2` (MINOR) | A `2.0`, B `1.2` |

B blijft in beide gevallen `1.2`. Dezelfde afweging geldt een niveau hoger richting de `opleidingsspecificatie`.

**Manifest payload.** Elke specificatie met onderdelen, varianten of gepinde verwijzingen draagt een `manifest`: een lijst van (id, versie, relatie). Daarmee is de pin expliciet in plaats van impliciet.

| Veld | Betekenis |
|---|---|
| `educationSpecificationId` | de gepinde specificatie |
| `version` | de exacte versie die deze release vastlegt |
| `relatie` | `onderdeel` (additief, telt mee in de studielast), `variant` (alternatief), `referentie` (gepinde verwijzing, bv. naar een keuzedeelprogramma) |

```json
{
  "educationSpecificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
  "educationSpecificationType": "opleidingsprogrammaspecificatie",
  "version": "0.1.0",
  "manifest": [
    { "educationSpecificationId": "402c2342-d897-4df4-a667-7fc5bd930944", "version": "0.1.0", "relatie": "onderdeel" },
    { "educationSpecificationId": "fb5be5ae-faa0-4b4b-8085-474fce9aae08", "version": "0.1.0", "relatie": "onderdeel" }
  ]
}
```

In §7.2 staat het manifest uitgewerkt op drie niveaus: de `opleidingsspecificatie` (pint de leerweg-varianten), de `opleidingsprogrammaspecificatie` Regulier BOL (pint haar `onderwijseenheidspecificatie`s en de `keuzedeelruimtespecificatie`), en de `keuzedeelruimtespecificatie` (pint de keuzedeelprogramma's als referentie). Voor de leesbaarheid niet op elk niveau herhaald; in een volledige payload draagt elke specificatie met onderdelen een manifest.

## 9. Open vragen en signaleringen

- OEAPI-binding van `educationSpecificationType`. De OEAPI-enum (program, cluster, course) mapt niet 1:1 op onze conceptniveaus. Binding vaststellen in de gegevensanalyse. Signalering; geen OEAPI-kernwijziging.
- Interne structuur van de ruleset (regeltypes, parameters, evaluatie). Wordt uitgewerkt in #84 en #120. Hier alleen de referentie (`ruleSetRefs`) en indicatieve regels.
- Parent versus children. Gekozen: `parent` (recursief, plat). Een geneste weergave is afleidbaar. Te bevestigen.
- Dubbele betekenis van `parent`: onderdeel-van versus variant-van. Overwegen dit expliciet te maken (bv. veld `parentRelatie`).
- Hergebruik van kwalificatie-inhoud over doelgroep-varianten. Nu hangt de inhoud onder één doelgroep (Regulier BOL); de andere varianten zijn leeg. Bepalen: inhoud herhalen of refereren.
- `startdatum` en `cohort` raken het cohort- en planbaar-stadium, niet de pure specificatie. Plaatsing te bevestigen.
- Lifecycle en versionering (apart voorstel, zie Gerelateerde uitwerkingen). De `opleidingsspecificatie` heeft een eigen versie die tevens als manifest de versies van onderliggende onderdelen vastpint (bv. opleiding 2.1 pint onderwijseenheid A 1.1 en B 1.2). Een MAJOR-bump van een onderdeel propageert niet automatisch naar de opleiding; alleen als de afhankelijkheid breekt (leeruitkomsten, weging, diploma-eligibility).
- Examenplan en resultaatstructuur (aparte uitwerking, zie Gerelateerde uitwerkingen). Het examenplan (OER) is een parallelle boom die via leeruitkomsten aan de onderwijsspecificatie hangt en de weging en indeling van toets- en examenspecificaties richting het diploma draagt (summatief en formatief). Hier alleen als specificatietype opgenomen.
- Deactiveren, niet verwijderen. Specificaties met aanbod worden gedeactiveerd (`status: gedeactiveerd`); meerdere versies kunnen gelijktijdig actief zijn (`validFrom`/`validTo`). Memo PR #110.
- Versie-pins bij verwijzingen zijn nu belegd in het `manifest` (`relatie: referentie`). Open blijft of `ruleSetRefs` daarnaast een eigen pin krijgt, of altijd via het manifest loopt.

## Gerelateerde uitwerkingen

Achterliggende uitwerkingen die de keuzes in deze payload toelichten:

- [Resultaatstructuur en examenplan](20260720_0831_okx-lr1-resultaatstructuur-examenplan.md): het examenplan (OER) en de summatieve/formatieve resultaatstructuur.
- [Lifecycle en versionering](20260720_0832_okx-lr1-lifecycle-versionering.md): semver, identiteit versus versie, manifest en propagatie.
- Memo "Onderwijs PDCA-cyclus" van Niels: `doc/OKx_PDCA cyclus onderwijsontwerp.md` (PR #110).
- `name` en `description` als string versus meertalig (OEAPI `LanguageTypedString[]`). Nu string, conform de stub in #119.
- Leeruitkomst enkelvoud versus meervoud. Nu één primaire leeruitkomst per specificatie (verving `primaryCode`). Een specificatie kan meerdere leeruitkomsten dekken; een array-vorm is een latere uitbreiding.
- Uitbreiding leeruitkomst-standaard. `leeruitkomst.type` is open; koppeling aan CompetentNL (of vergelijkbaar) vaststellen wanneer die standaard beschikbaar is.
- Enums in §6 zijn concept. Vaststellen welke waarden per veld gelden.
- LR2 en LR3 als delta: welke attributen wijzigen (bv. `spreidingspatroon`, `bereik`, `thuisOrganisatie`, `gastheerOrganisatie`).
