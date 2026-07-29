# Lifecycle en versionering van onderwijsspecificaties

Context: achterliggende uitwerking bij de [onderwijsspecificatie-payload](20260717_1120_okx-lr1-onderwijsspecificatie-payload-json.md). Status: skeleton (nog uit te werken).

## Inhoudsopgave

1. [Inleiding](#1-inleiding)
2. [Doel](#2-doel)
3. [Scope](#3-scope)
4. [Context (memo van Niels)](#4-context-memo-van-niels)
5. [Voorstel (richting)](#5-voorstel-richting)
6. [Classificatie van wijzigingen](#6-classificatie-van-wijzigingen)
7. [Open vragen en TODO](#7-open-vragen-en-todo)
8. [Relaties](#8-relaties)

## 1. Inleiding

De payload zet `version` (semver) op elk niveau en houdt `educationSpecificationId` (identiteit) los van de versie. Dat roept een lifecycle-vraag op: heeft de `opleidingsspecificatie` een eigen versie, en hoe werkt propagatie van wijzigingen? Dit document licht die keuzes toe en schetst de richting.

Context voor de nieuwkomer: dit is een gedeelde uitwerking bij de centrale [onderwijsspecificatie-payload](20260717_1120_okx-lr1-onderwijsspecificatie-payload-json.md); zie de [instap in de README](../README.md#context) voor de keten, de begrippen en de actuele hoofdplaat v1.7. Scenario LR1-3.

Aanleiding is de memo **"Onderwijs PDCA-cyclus" van Niels** (PR #110, `doc/OKx_PDCA cyclus onderwijsontwerp.md`).

## 2. Doel

- De lifecycle van onderwijsspecificaties beschrijven, met concrete versioneringsvoorbeelden.
- Vastleggen wanneer een wijziging leidt tot een nieuwe specificatie, een nieuwe versie, of een niet-brekende aanpassing.
- Het release-/manifest-mechanisme beschrijven waar consumenten (planning, SVS) tegenaan werken.

## 3. Scope

- LR1-3. Conceptueel; techniek volgt in de berichtspecificatie.
- Aansluiting op releasemanagement (`doc/OKx_Release-management-en-versionering.md`).

## 4. Context (memo van Niels)

Uitgangspunten uit de memo:

- Onderdelen hebben een eigen lifecycle. Een minor update op een `onderwijseenheidspecificatie` hoeft de `opleidingsspecificatie` niet te wijzigen.
- Identificerende codering en versionering strikt scheiden.
- Specificaties met aanbod worden gedeactiveerd, niet verwijderd. Meerdere versies kunnen gelijktijdig actief zijn.
- Het examenplan/OER heeft de strengste acceptatieregels (contractueel).
- De onderwijscatalogus is verantwoordelijk voor versionering en releasemanagement.

## 5. Voorstel (richting)

> Skeleton. Concept-richting, nog uit te werken.

De payload-facing mechaniek (snapshot-als-manifest) en een uitgewerkt voorbeeld staan in het hoofdstuk *Onderwijsspecificatie lifecycle* van de [payload](20260717_1120_okx-lr1-onderwijsspecificatie-payload-json.md). Dit document werkt de bredere lifecycle en het beleid uit.

- **Semver per node** (`MAJOR.MINOR.PATCH`). MAJOR = brekend binnen dezelfde identiteit; MINOR = additief; PATCH = correctie.
- **Identiteit los van versie**. Een fundamentele wijziging (nieuw dossier, nieuwe wettelijke eisen) is een **nieuwe specificatie** met een nieuw `educationSpecificationId`, niet alleen een MAJOR-bump.
- **Versie als manifest, op elk niveau**. Elke specificatie met onderdelen pint de versies daarvan via `manifest` (id, versie, relatie). Formaat en voorbeeld: hoofdstuk *Onderwijsspecificatie lifecycle* van de payload.
- **Impact-gedreven propagatie**. Een MAJOR-bump van een onderdeel propageert niet automatisch naar de opleiding; alleen als de afhankelijkheid breekt (leeruitkomsten, weging, diploma-eligibility). Anders is het een nieuw pin in het manifest.
- **Status-lifecycle**: `concept` → `vastgesteld` → `gepubliceerd` → `gedeactiveerd` → `gearchiveerd`. `vervallen` waar van toepassing.
- **Geldigheid**: `validFrom`/`validTo` maken meerdere gelijktijdig actieve versies mogelijk (oude versie voor lopende studenten, nieuwe voor nieuwe instroom).

- **TODO**: meer versioneringsvoorbeelden, bovenop het basisvoorbeeld in de payload (o.a. gelijktijdig actieve versies over cohorten heen).
- **TODO**: hoe legt de onderwijscatalogus een release vast (publicatiegebeurtenis) bovenop de manifests.
- **TODO**: migratie van achterblijvende studenten (Jochem LR1 → Michelle LR9); grotendeels buiten OKx-scope, afhankelijk van applicatielandschap.

## 6. Classificatie van wijzigingen

Overgenomen en vertaald uit de memo van Niels, gekoppeld aan semver en identiteit:

| Type wijziging | Casus | Gevolg |
|---|---|---|
| Fundamenteel | Nieuw kwalificatiedossier, gewijzigde wettelijke eisen, nieuwe onderwijsvisie | Nieuwe specificatie (nieuw id); meestal alleen nieuwe instroom |
| Examenplan/OER | Aanpassing summatieve resultaatstructuur | Alleen na expliciete impactanalyse en besluit (strengste) |
| Onderdeel | Update `onderwijseenheidspecificatie` of `leeronderdeelspecificatie` | Nieuwe versie van het onderdeel (semver); bovenliggende specificatie alleen bij brekende afhankelijkheid |
| Niet-brekend | Actualisatie lessen, materiaal, uitvoeringsvorm | PATCH/MINOR binnen dezelfde lifecycle |
| Na planning/roostering | Wijziging nadat aanbod of rooster is gepubliceerd | Alleen bij uitzondering en na ketenafstemming |

## 7. Open vragen en TODO

- Het manifest pint exacte versies. Open blijft of daarnaast een "laatst-compatibele" verwijzing nodig is voor herbruikbare onderdelen.
- Hoe bepaalt de onderwijscatalogus of ontwerptool of een wijziging brekend is (impactanalyse)?
- Release-/snapshot-gebeurtenis: hoe publiceert OC een samenhangende versie van de boom?
- Tot welk moment worden wijzigingen geaccepteerd t.o.v. planning en roostering (beleid).

## 8. Relaties

- Payload: [onderwijsspecificatie-payload](20260717_1120_okx-lr1-onderwijsspecificatie-payload-json.md).
- Resultaatstructuur: [resultaatstructuur en examenplan](../oc-sis-krs-svs/20260720_0831_okx-lr1-resultaatstructuur-examenplan.md).
- Memo van Niels: `doc/OKx_PDCA cyclus onderwijsontwerp.md` (PR #110).
- Releasemanagement: `doc/OKx_Release-management-en-versionering.md`.
- ADR 0020 (CO-OC synchronisatie, adopt vs klonen, UUID-referentie).
