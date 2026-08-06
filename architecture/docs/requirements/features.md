# Features

Laag 3 van de [requirementsboom](README.md): afgebakend gedrag per [epic](epics.md). De ouder staat in de sectiekop. Relateert aan: #130.

## Onderwijsaanbod specificeren en ontsluiten

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Catalogus vullen vanuit curriculumontwerp | De onderwijscatalogus wordt als bronsysteem voor de keten gevuld met het formeel uitgewerkte aanbod vanuit de curriculumontwerptool. | uitgewerkt | [ADR 0002](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0002-prioriteitsketen-catalogus-drielagen-fundament.md) | |
| Hiërarchische, refereerbare onderwijsspecificatiestructuur | De onderwijsspecificatie is een hiërarchische structuur met unieke specificatie- en ouder-id's, leerwegen, doelgroepvarianten en relationeel hergebruik van gedeelde onderdelen. | uitgewerkt | [Meetingverslag 10 juli](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#besluiten) | [Payload onderwijsspecificatie](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/payload-onderwijsspecificatie.md) |
| Stabiele identiteit en versionering van specificaties | Het id van een specificatie verandert nooit door een inhoudelijke wijziging; alleen de versie wijzigt, zodat verwijzingen van afnemers geldig blijven. | uitgewerkt | [Lifecycle en versionering](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/lifecycle-en-versionering.md) | |
| Leeromgeving inrichten op de specificatie | Het leermanagementsysteem richt de leeromgeving in tot op leeronderdeelniveau en vult het lesniveau daaronder zelf in, buiten de catalogus. | uitgewerkt | [Koppelingspecificatie OC-LMS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-lms/koppelingspecificatie-oc-lms.md) | |

## Student kiest onderwijsspecificaties

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Kiesbaarheid bepalen | Per student is bepaalbaar welke onderwijsspecificaties hij op elk niveau mag kiezen (eligibility). | uitgewerkt | [PR 120, R1 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | |
| Keuzecriteria als queryparameters op de aanbodquery | Het studentkeuzesysteem vertaalt de leervraag naar gestructureerde, componeerbare keuzecriteria die de onderwijscatalogus als queryparameters draagt. | uitgewerkt | [ADR 0007](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) | |
| Regelsets los van items, met min/max-keuzeregels | Keuzeregels staan als regelsets los van de items waarop ze werken en dragen vormen als "kies minimaal x en maximaal y uit een set". | uitgewerkt | [PR 120, R2 en R5 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | |
| Leeruitkomst-id's als opaque sleutels in keuzeregels | Systemen evalueren keuzeregels met alleen leeruitkomst-id's en behaald-status, zonder de inhoud van de leeruitkomst te kennen. | uitgewerkt | [ADR 0023](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) | [Koppelingspecificatie OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) |
| Regelsets versioneren voor verantwoording | Regelsets kennen eigen versionering; achteraf is vaststelbaar welke regelversie gold bij een keuze, onder meer voor de diplomaverantwoording. | uitgewerkt | [PR 120, R17 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | |

## Aanbod plannen en roosteren

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Drie stadia van onderwijsaanbod | Aanbod kent drie stadia: specificatie, planbaar aanbod (perioden en capaciteit) en geroosterd aanbod (concrete tijdsloten en resource-instanties). | uitgewerkt | [Consumer-profiel §3.2.3](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#323-stadia-van-onderwijsaanbod--specificatie--planbaar--geroosterd) | |
| Planbaarheid als rijpheidskenmerk | De catalogus draagt planbaarheid als rijpheidskenmerk van de specificatie, met studielast, expertise, volgorde, toetsvorm, capaciteit en tijdvensters zonder giswerk. | uitgewerkt | [Kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario%27s/leerroute-1-regulier.md) | |
| Geldig, gefaseerd aanbod afleiden | Planning en roostering leidt uit de onderwijsspecificatiestructuur, de regels en de vereiste leeruitkomsten geldig, in de tijd gefaseerd aanbod af. | uitgewerkt | [PR 120, R9 en R11 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | [Koppelingspecificatie OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) |
| Eigenaarschap van het aanbodobject | Planning en roostering is eigenaar van het aanbodobject met uitsluitend planningsrelevante gegevens en een referentie naar de specificatie. | uitgewerkt | [Meetingverslag 10 juli](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#besluiten) | [Payload onderwijsaanbod](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/payload-onderwijsaanbod.md) |
| Haalbaarheid van keuze en ontwerp toetsen | Een expliciete haalbaarheidstoets (request for offering) beoordeelt een studentkeuze en koppelt minimaal acceptatie, afwijzing of een alternatief terug. | uitgewerkt | [ADR 0015](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md) | |

## Keuze en verbintenis vastleggen

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Verbintenis als toestandsmachine per niveau | De onderwijsverbintenis bestaat op elk niveau (programma, eenheid, leergelegenheid, toets) en wordt per niveau als eigen toestandsmachine (state machine) bijgehouden. | nog niet uitgewerkt | [Consumer-profiel §3.2.4](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#324-stadia-van-onderwijsverbintenis--aangemeld--ingeschreven--bezig--afgerond) | |
| Keuze gescheiden van inschrijving en resultaat | Formele inschrijving en onderwijskundige keuze zijn gescheiden processtappen, belegd bij studentinformatiesysteem respectievelijk studentkeuzesysteem, met gescheiden interfaces. | nog niet uitgewerkt | [ADR 0009](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) | |
| Examenplanwijzigingen alleen na impactanalyse | Wijzigingen aan het examenplan worden alleen na expliciete impactanalyse en besluitvorming verwerkt, zodat lopende verbintenissen niet ongecontroleerd geraakt worden. | nog niet uitgewerkt | [Lifecycle en versionering](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/lifecycle-en-versionering.md) | |

## Voortgang en resultaat op leeruitkomsten

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Resultaatstructuur inrichten en resultaten registreren | Het studentinformatiesysteem richt met de specificatie- en resultaatstructuur het nominale sjabloon in en registreert onderwijsresultaten gewogen op leeruitkomsten. | uitgewerkt | [ADR 0022](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) | [Koppelingspecificatie OC-SIS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-sis-krs-svs/koppelingspecificatie-oc-sis.md) |
| Voorwaarden vooraf in behaalde leeruitkomsten | Een voorwaarde vooraf wordt uitgedrukt in behaalde leeruitkomsten, niet in doorlopen onderwijsspecificaties. | uitgewerkt | [PR 120, R7 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | |
| Aanvullend resultaat-koppelvlak voor bewijsvoering | Naast de verbintenistoestand biedt de keten een aanvullend resultaat-koppelvlak voor rijkere bewijsvoering op leeruitkomstniveau. | uitgewerkt | [Consumer-profiel §3.2.4](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#324-stadia-van-onderwijsverbintenis--aangemeld--ingeschreven--bezig--afgerond) | |
| Toetsing zodra leeruitkomsten gedekt zijn | Een toetsmoment is mogelijk zodra de leeruitkomsten gedekt zijn, ook als de student niet alle leergelegenheden heeft bijgewoond. | uitgewerkt | [Consumer-profiel §3.4.9](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#349-scenario-31--versnellen-by-design-anker-lr3) | |

## Gezamenlijke taal en standaard

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Formele begrippenlijst als artefact | De standaard bevat een formele begrippenlijst als artefact, bron voor alle termen in informatiemodellen en data, conform Edustandaard en de AMIGO-aanpak. | nog niet uitgewerkt | [Sparsessie 5 augustus](../../agent-artifacts/research/20260806_0837_requirementsboom-extractie.md#meetingbronnen-die-alleen-extern-zijn-vastgelegd) | |
| Uitlijning met ROSA en KOI | De terminologie van de standaard is uitgelijnd met landelijke referentiemodellen zoals ROSA (Referentie Onderwijs Sector Architectuur) en KOI (Kernmodel Onderwijsinformatie). | nog niet uitgewerkt | [Meetingverslag 30 april](../../meetings/20260430_nde_nvd_klus53_allignment_OKx_referentiekader/summary.md#executive-summary) | |
| N:M-cardinaliteit en prerequisite-relaties | De standaard hanteert de normatieve N:M-cardinaliteit tussen leeruitkomsten en onderdelen en drukt voorwaarderelaties (prerequisites) uit. | nog niet uitgewerkt | [Consumer-profiel §3.2.6](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#326-het-vlaks-model-als-ankertabel--6-niveaus--6-families) | |
| Eenduidige regelevaluatie (conformance) | Een keuzeregel is zo eenduidig dat elk systeem dezelfde uitkomst berekent; voorwaarde voor conformance-toetsing. | nog niet uitgewerkt | [PR 120, R6 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | |
| Koppeling versus koppelvlak als vaste terminologie | Elke koppeling is een gestandaardiseerde informatiestroom tussen twee referentiecomponenten; het koppelvlak per component is de optelsom daarvan. | nog niet uitgewerkt | [Uitgangspunt U2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) | |

## Betrouwbare en vervangbare koppelingen

| Feature | Doel | Status | Bron | Verwijzing |
|---|---|---|---|---|
| Betrouwbaar berichtenverkeer | Mutaties gaan via dunne events met referentie waarna de consument zelf ophaalt; elk kanaal levert gegarandeerde aflevering, idempotentie en volgorde per sleutel. | nog niet uitgewerkt | [Uitgangspunten U4 en U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) | |
| Authenticatie via OAuth 2.0 Client Credentials | Elke consument authenticeert zich conform het Edukoppeling REST-profiel niveau 1; elk systeem dat endpoints serveert beheert zijn eigen token-endpoint. | nog niet uitgewerkt | [Public PR 9 (in review)](https://github.com/Npuls-OKx/Public/pull/9) | |
| Maximaal twee actieve major versies | De standaard ondersteunt maximaal twee major versies actief (de nieuwste en de voorlaatste), zodat afnemers tijd hebben om over te stappen. | nog niet uitgewerkt | [Meetingverslag 14 juli](../../meetings/20260714_SI_afstemming_PR_specificatie_uitwerking_P_en_R/summary.md#progress) | |
| Intra-instelling eerst, federatie gefaseerd | Koppelingen worden eerst binnen een instelling werkend gemaakt; federatie en cross-instelling volgen gefaseerd. | nog niet uitgewerkt | [Uitgangspunt U10](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) | |

## Standaard piloteren en adopteren

Nog geen features. Deze epic is toegevoegd bij de review van het boom-concept (6 augustus 2026); kandidaten volgen in de volgende uitwerkingsronde, onder meer uit de [adoptiestrategie van 17 april](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md).
