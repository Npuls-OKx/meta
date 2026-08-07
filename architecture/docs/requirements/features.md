# Features

Laag 3 van de [requirementsboom](README.md): afgebakend gedrag per [epic](epics.md). De ouder staat in de sectiekop. Relateert aan: #130.

## Onderwijsaanbod specificeren en ontsluiten

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F1.1 | Catalogus vullen vanuit curriculumontwerp | Alle ketenpartijen vertrouwen op één actuele, formeel vastgestelde bron voor de onderwijsspecificaties. | [ADR 0002](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0002-prioriteitsketen-catalogus-drielagen-fundament.md) |  |
| F1.2 | Hiërarchische, refereerbare onderwijsspecificatiestructuur | Elk onderdeel van de onderwijsspecificatie is eenduidig herleidbaar en herbruikbaar, ook over leerwegen en doelgroepvarianten heen. | [Meetingverslag 10 juli, besluiten](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#besluiten) en [technische details](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#technische--implementatiedetails) | [Payload onderwijsspecificatie](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/payload-onderwijsspecificatie.md) |
| F1.3 | Stabiele identiteit en versionering van specificaties | Verwijzingen van afnemers naar een specificatie blijven geldig, ook na inhoudelijke wijzigingen. | [Lifecycle en versionering](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/lifecycle-en-versionering.md) |  |
| F1.4 | Leeromgeving inrichten op de specificatie | De leeromgeving is altijd inhoudelijk consistent met de specificatie, met ruimte voor eigen invulling op lesniveau. | [Koppelingspecificatie OC-LMS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-lms/koppelingspecificatie-oc-lms.md) |  |

## Student kiest onderwijsspecificaties

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F2.1 | Kiesbaarheid bepalen | Voor elke student staat op elk niveau vast welke onderwijsspecificaties hij mag kiezen (eligibility). | [PR 120, R1 (in review)](https://github.com/Npuls-OKx/meta/pull/120) |  |
| F2.2 | Keuzecriteria als queryparameters op de aanbodquery | Systemen doorzoeken het onderwijsaanbod met precieze, herbruikbare criteria die rechtstreeks uit de leervraag volgen. | [ADR 0007](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) |  |
| F2.3 | Regelsets los van items, met min/max-keuzeregels | Beheerders wijzigen regelsets los van catalogusitems en drukken keuzevormen met een minimum en maximum uit. | [PR 120, R2 en R5 (in review)](https://github.com/Npuls-OKx/meta/pull/120) |  |
| F2.4 | Leeruitkomst-id's als opaque sleutels in keuzeregels | Systemen wisselen keuzegegevens uit zonder de inhoud van leeruitkomsten te hoeven delen. | [ADR 0023](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) | [Koppelingspecificatie OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) |
| F2.5 | Regelsets versioneren voor verantwoording | Achteraf staat vast welke regelversie gold bij een keuze, nodig voor de diplomaverantwoording. | [PR 120, R17 (in review)](https://github.com/Npuls-OKx/meta/pull/120) |  |

## Aanbod plannen en roosteren

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F3.1 | Drie stadia van onderwijsaanbod | Systemen onderscheiden betrouwbaar in welke fase het aanbod verkeert, van specificatie tot concreet rooster. | [Consumer-profiel §3.2.3](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#323-stadia-van-onderwijsaanbod--specificatie--planbaar--geroosterd) |  |
| F3.2 | Planbaarheid als rijpheidskenmerk | Planners plannen aanbod zonder giswerk; alle benodigde gegevens liggen vooraf vast in de specificatie. | [Kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario%27s/leerroute-1-regulier.md) |  |
| F3.3 | Geldig, gefaseerd aanbod afleiden | Het geplande aanbod is altijd geldig en sluit in de tijd logisch aan op de vereiste leeruitkomsten. | [PR 120, R9 en R11 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | [Koppelingspecificatie OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) |
| F3.4 | Eigenaarschap van het aanbodobject | Planninggegevens en specificatie-inhoud blijven gescheiden; het aanbodobject bevat geen dubbele of verouderde specificatiegegevens. | [Meetingverslag 10 juli](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#besluiten) | [Payload onderwijsaanbod](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/payload-onderwijsaanbod.md) |
| F3.5 | Haalbaarheid van keuze en ontwerp toetsen | De student weet vóór bevestiging of zijn keuze haalbaar is, via acceptatie, afwijzing of een alternatief. | [ADR 0015](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md) |  |

## Keuze en verbintenis vastleggen

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F4.1 | Verbintenis als toestandsmachine per niveau | Systemen en actoren stellen op elk niveau, van programma tot toets, de actuele status van de verbintenis vast. | [Consumer-profiel §3.2.4](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#324-stadia-van-onderwijsverbintenis--aangemeld--ingeschreven--bezig--afgerond) |  |
| F4.2 | Keuze gescheiden van inschrijving en resultaat | Studentkeuze staat als eigen verantwoordelijkheid los van de formele inschrijving en van resultaat en voortgang. | [ADR 0014](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md) en [ADR 0009](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) |  |
| F4.3 | Examenplanwijzigingen alleen na impactanalyse | Een wijziging in het examenplan raakt lopende verbintenissen nooit ongecontroleerd. | [Lifecycle en versionering](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/lifecycle-en-versionering.md) |  |

## Voortgang en resultaat op leeruitkomsten

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F5.1 | Resultaatstructuur inrichten en resultaten registreren | Elk onderwijsresultaat koppelt gewogen en herleidbaar aan de behaalde leeruitkomsten van de student. | [ADR 0022](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) | [Koppelingspecificatie OC-SIS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-sis-krs-svs/koppelingspecificatie-oc-sis.md) |
| F5.2 | Voorwaarden vooraf in behaalde leeruitkomsten | Een student voldoet aan een voorwaarde vooraf zodra hij de leeruitkomst behaalt, ongeacht de gevolgde specificatie. | [PR 120, R7 (in review)](https://github.com/Npuls-OKx/meta/pull/120) |  |
| F5.3 | Aanvullend resultaat-koppelvlak voor bewijsvoering | Afnemers beschikken naast de verbintenisstatus over rijkere bewijsvoering van resultaten op leeruitkomstniveau. | [Consumer-profiel §3.2.4](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#324-stadia-van-onderwijsverbintenis--aangemeld--ingeschreven--bezig--afgerond) |  |
| F5.4 | Toetsing zodra leeruitkomsten gedekt zijn | De student kan toetsen zodra de leeruitkomsten gedekt zijn, ook zonder elke leergelegenheid te hebben bijgewoond. | [Consumer-profiel §3.4.9](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md#349-scenario-31--versnellen-by-design-anker-lr3) |  |

## Gezamenlijke taal en standaard

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F6.1 | Formele begrippenlijst als artefact | Alle informatiemodellen en data gebruiken eenduidige termen, herleidbaar tot één vastgestelde begrippenlijst. | [Sparsessie 5 augustus](../../agent-artifacts/research/20260806_0837_requirementsboom-extractie.md#meetingbronnen-die-alleen-extern-zijn-vastgelegd) |  |
| F6.2 | Uitlijning met ROSA en KOI | Instellingen en landelijke systemen herkennen dezelfde begrippen, zonder eigen vertaalslag naar ROSA (Referentie Onderwijs Sector Architectuur) of KOI (Kernmodel Onderwijsinformatie). | [Meetingverslag 30 april](../../meetings/20260430_nde_nvd_klus53_allignment_OKx_referentiekader/summary.md#executive-summary) |  |
| F6.3 | N:M-cardinaliteit en prerequisite-relaties | Systemen leggen relaties tussen leeruitkomsten, onderdelen en voorwaarden (prerequisites) eenduidig vast, ook waar één leeruitkomst meerdere onderdelen raakt. | [Payload onderwijsspecificatie, §3.2 Ontwerpkeuzes](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/payload-onderwijsspecificatie.md#32-ontwerpkeuzes) |  |
| F6.4 | Eenduidige regelevaluatie (conformance) | Elk systeem berekent voor dezelfde keuzeregel dezelfde uitkomst, een voorwaarde voor conformance-toetsing. | [PR 120, R6 (in review)](https://github.com/Npuls-OKx/meta/pull/120) |  |
| F6.5 | Koppeling versus koppelvlak als vaste terminologie | Alle betrokkenen gebruiken de termen koppeling en koppelvlak eenduidig en zonder onderlinge verwarring. | [Uitgangspunt U2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |  |

## Betrouwbare en vervangbare koppelingen

| Id | Feature | Doel | Bron | Verwijzing |
|---|---|---|---|---|
| F7.1 | Betrouwbaar berichtenverkeer | Consumenten missen nooit een mutatie en verwerken elk bericht eenmalig en in de juiste volgorde. | [Uitgangspunten U4 en U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |  |
| F7.2 | Authenticatie via OAuth 2.0 Client Credentials | Alleen geautoriseerde consumenten krijgen toegang tot endpoints, conform het Edukoppeling REST-profiel. | [Public PR 9 (in review)](https://github.com/Npuls-OKx/Public/pull/9) |  |
| F7.3 | Maximaal twee actieve major versies | Afnemers hebben altijd voldoende tijd om over te stappen naar een nieuwe major versie. | [Meetingverslag 14 juli](../../meetings/20260714_SI_afstemming_PR_specificatie_uitwerking_P_en_R/summary.md#progress) |  |
| F7.4 | Intra-instelling eerst, federatie gefaseerd | Instellingen gebruiken koppelingen eerst betrouwbaar binnen de eigen instelling, vóór cross-instelling uitbreiding nodig is. | [Uitgangspunt U10](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |  |

## Standaard piloteren en adopteren

Nog geen features. Deze epic is toegevoegd bij de review van het boom-concept (6 augustus 2026); kandidaten volgen in de volgende uitwerkingsronde, onder meer uit de [adoptiestrategie van 17 april](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#stakeholdermanagement-en-adoptiestrategie).
