# Requirements voor de requirementsboom (PoC)

Relateert aan: #130. Opgesteld met de persona [`business-analyse-okx`](../../../.agents/skills/business-analyse-okx/SKILL.md); de vormconventies staan in [`okx-requirements-boom`](../../../.agents/skills/okx-requirements-boom/SKILL.md).

## Context

De sparsessie van 5 augustus 2026 (commentaar bij #130) koos de requirementsboom als de getoonde koppeling tussen business en techniek: opdracht, epics, features, stories, met onderaan de aansluiting op de koppelingspecificaties. Dit document stelt de eisen aan die boom vast, zodat de uitwerking en de onafhankelijke reviews (product-flow stap 2 en 3) een toetsbaar kader hebben.

## Wat er al ligt en wat ontbreekt

- Aanwezig: doelen en scope (consumer-profiel §1, projectoverzicht), scenario's en persona's (LR1 tot en met LR3), keuze-requirements R1 tot en met R17 ([PR 120](https://github.com/Npuls-OKx/meta/pull/120), in review), uitgangspunten en interacties in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public).
- Ontbreekt: een gelaagde, leesbare ingang die dit materiaal van opdracht tot techniek ordent. Dat is het deliverable.

## Doel

Een proof of concept (PoC) van de boom die drie vragen beantwoordt: wat moet de keten kunnen en waarom (bovenste twee lagen, voor de product owner), hoe hangt bestaand materiaal daaraan (bron per rij), en waar raakt een story de techniek (koppelvlakverwijzing). Geslaagd wanneer beide reviews uit de product-flow slagen en de acceptatiecriteria hieronder aantoonbaar zijn.

## Scope

De zes documenten onder `architecture/docs/requirements/`, het extractie-artifact met parkeerlijst, en de indexregels in bestaande README's. Al het overige valt buiten scope.

## Eisen

| Eis | Omschrijving | Acceptatiecriterium |
|---|---|---|
| R1 Vier lagen, zes bestanden | De boom bestaat uit opdracht, epics, features en stories, elk in één document, plus index en leeswijzer. Geen tussenlagen. | `architecture/docs/requirements/` bevat exact `README.md`, `opdracht.md`, `epics.md`, `features.md`, `stories.md`, `leeswijzer.md`. |
| R2 Herleidbaar tot de opdracht | Elke epic verwijst naar een doel, elke feature naar een epic, elke story naar een feature. Voorbeeld: de story over Jochems keuzedeel is via feature en epic te volgen tot "Leren zonder Drempels". | Geen rij zonder ouder (kolom of sectiekop); het pad opdracht, epic, feature, story is voor de PoC-epic aanwijsbaar. |
| R3 Bronplicht | Elke rij draagt een bron volgens de bronhierarchie uit de skill; wat niet herleidbaar is staat op de parkeerlijst, niet in de boom. | 100% gevulde bronkolommen (telbaar); parkeerlijst aanwezig in het extractie-artifact. |
| R4 PoC-diepte | Drie epics zijn doorgewerkt tot stories: onderwijsaanbod specificeren en ontsluiten, student kiest onderwijsspecificaties, en aanbod plannen en roosteren. Voortgang en resultaat op leeruitkomsten krijgt een eerste opzet: features, en stories alleen waar de bron hard is. Overige epics dragen "nog niet uitgewerkt" zonder verzonnen invulling. | `stories.md` bevat uitsluitend stories van deze vier epics; elke andere epic heeft de status "nog niet uitgewerkt". |
| R5 Koppelvlakverwijzing | Wanneer een story een interactie tussen systemen raakt, dan noemt de rij de interactie en het systeem dat eigenaar wordt van de endpoint-set; anders staat er "geen". Voorbeeld: `I1, eigenaar OC`. | Geen lege koppelvlakcellen in `stories.md`. |
| R6 Overzicht boven volledigheid | De omvangslimieten uit de skill zijn hard: onder andere maximaal 7 epics, 15 stories, en de regellimieten per bestand. | `wc -l` per bestand binnen de limiet; tellingen epics en stories binnen het maximum. |
| R7 Leesbaar voor de product owner | `opdracht.md` en `epics.md` zijn zelfstandig leesbaar zonder technische voorkennis; afkortingen voluit bij eerste gebruik. | De tester begrijpt beide documenten zonder een verwijzing te hoeven volgen; geen onverklaarde afkorting. |
| R8 Vertaalbaar naar issues | De tabellen volgen exact de kolomformats uit de skill, zodat de boom later mechanisch naar milestones en issues is om te zetten. | Kolomkoppen per laag identiek aan de skill. |
| R9 Leeswijzer verwijst, dupliceert niet | De leeswijzer wijst bestaande documenten en secties aan en neemt geen inhoud over. | Geen inhoudelijke passages die ook in het brondocument staan (steekproef door de reviewer). |
| R10 Achtergrondmechaniek buiten de boom | Geen eis-ID-notatie of uitvoerbare scenario's (Gherkin) in de boomdocumenten; de index verwijst voor die mechaniek naar het ADR en #135. | `grep` op `req~`, `Covers:` en `Functionaliteit:` in `architecture/docs/requirements/` levert niets op. |
| R11 Mechanisch schoon | Validatie en indexplicht gelden zoals overal in de repo. | `python3 scripts/validate-docs.py architecture/docs/requirements` slaagt; nieuwe bestanden staan in de README-indexen. |
| R12 Plaat en tabel vertellen hetzelfde | De mermaid-plaat in de index toont dezelfde epics en features als de tabellen. | Elke node in de plaat staat in de tabellen en omgekeerd (stories als verzamelnode). |

Het pad dat R2 en R5 samen toetsen, als voorbeeld uit leerroute 1:

```mermaid
flowchart LR
  O["Opdracht: Leren zonder Drempels"] --> E["Epic: Student kiest onderwijsspecificaties"]
  E --> F["Feature: kiesbaarheid bepalen"]
  F --> S["Story: Jochem kiest een keuzedeel"]
  S --> K["Koppelvlak: interactie, eigenaar OC of SKS"]
```

## Open vragen

| Vraag | Vervolgstap |
|---|---|
| Wie onderhoudt de boom na de PoC, en kan de business de doorverwijzingen (interacties, later eis-ID's uit #135) zelf definiëren en bijhouden? | Voorstel (5 augustus): de boom in git blijft de bron; een agent-command zet de vastgestelde boom idempotent om naar milestones en issues in Npuls-OKx/Public (epic wordt milestone, feature en story worden issues met terugverwijzing). Uitwerken in de beheerparagraaf van het ADR-concept en als vervolgissue. |
| Is de werkindeling in zes epics de juiste snede? | Vaststellen bij het boom-concept (stopmoment na de eerste opzet), vóór leeswijzer en reviews. |
| Wanneer verhuist de boom, of een release-weergave ervan, naar Npuls-OKx/Public? | Vervolgissue na de PoC-review. |

## Vaststelling

Niek stelt deze eisen vast vóór de uitwerking start (product-flow stap 1); Garik reviewt het geheel via PR 131.
