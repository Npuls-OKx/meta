# Features

Laag 3 van de [requirementsboom](README.md): afgebakend gedrag per [epic](epics.md). De ouder staat in de sectiekop.

## [Gezamenlijke taal en standaard](epics.md#epic-0001)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0001"></a>feature-0001 | Formele begrippenlijst als artefact | Alle informatiemodellen en data gebruiken eenduidige termen, herleidbaar tot één vastgestelde begrippenlijst. | [Sparsessie 5 augustus](../../agent-artifacts/research/20260806_0837_requirementsboom-extractie.md#meetingbronnen-die-alleen-extern-zijn-vastgelegd) |  |
| <a id="feature-0002"></a>feature-0002 | Uitlijning met ROSA en KOI | Instellingen en landelijke systemen herkennen dezelfde begrippen, zonder eigen vertaalslag naar ROSA (Referentie Onderwijs Sector Architectuur) of KOI (Kernmodel Onderwijsinformatie). | [Meetingverslag 30 april](../../meetings/20260430_nde_nvd_klus53_allignment_OKx_referentiekader/summary.md#executive-summary) |  |
| <a id="feature-0003"></a>feature-0003 | N:M-cardinaliteit en prerequisite-relaties | Systemen leggen relaties tussen leeruitkomsten, onderdelen en voorwaarden (prerequisites) eenduidig vast, ook waar één leeruitkomst meerdere onderdelen raakt. | [Datamodelschema's, regels bij de schema's](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/README.md#regels-bij-de-schemas) |  |
| <a id="feature-0004"></a>feature-0004 | Eenduidige regelevaluatie (conformance) | Elk systeem berekent voor dezelfde keuzeregel dezelfde uitkomst, een voorwaarde voor conformance-toetsing. | [Keuze-requirements R6](../specificatie/student-keuze/keuze-requirements.md#6-requirements) |  |
| <a id="feature-0005"></a>feature-0005 | Koppeling versus koppelvlak als vaste terminologie | Alle betrokkenen gebruiken de termen koppeling en koppelvlak eenduidig en zonder onderlinge verwarring. | [Uitgangspunt U2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |  |
| <a id="feature-0006"></a>feature-0006 | Engelse veldnamen met Nederlandse mapping | Systemen gebruiken Engelstalige veldnamen die eenduidig terugvoeren op de eerdere Nederlandse veldnamen. | [Mapping veldnamen](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/mapping.md) |  |

## [Onderwijsaanbod specificeren en ontsluiten](epics.md#epic-0002)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0007"></a>feature-0007 | Catalogus vullen vanuit curriculumontwerp | Alle ketenpartijen vertrouwen op één actuele, formeel vastgestelde bron voor de onderwijsspecificaties. | [ADR 0002](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0002-prioriteitsketen-catalogus-drielagen-fundament.md) |  |
| <a id="feature-0008"></a>feature-0008 | Hiërarchische, refereerbare onderwijsspecificatiestructuur | Elk onderdeel van de onderwijsspecificatie is eenduidig herleidbaar en herbruikbaar, ook over leerwegen en doelgroepvarianten heen. | [Meetingverslag 10 juli, besluiten](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#besluiten) en [technische details](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#technische--implementatiedetails) | [Datamodelschema's, onderwijsspecificatie](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/README.md#onderwijsspecificatie) |
| <a id="feature-0009"></a>feature-0009 | Stabiele identiteit en versionering van specificaties | Verwijzingen van afnemers naar een specificatie blijven geldig, ook na inhoudelijke wijzigingen. | [Regels bij de schema's](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/README.md#regels-bij-de-schemas) |  |
| <a id="feature-0010"></a>feature-0010 | Leeromgeving inrichten op de specificatie | De leeromgeving is altijd inhoudelijk consistent met de specificatie, met ruimte voor eigen invulling op lesniveau. | [Interactiepatroon OC-LMS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md) |  |

## [Aanbod plannen en roosteren](epics.md#epic-0003)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0011"></a>feature-0011 | Drie stadia van onderwijsaanbod | Systemen onderscheiden betrouwbaar in welke fase het aanbod verkeert, van specificatie tot concreet rooster. | [Begrippenkader, stadia van onderwijsaanbod](../specificatie/leerroute-uitwerking/doc/begrippenkader.md#stadia-van-onderwijsaanbod-specificatie-planbaar-geroosterd) |  |
| <a id="feature-0012"></a>feature-0012 | Planbaarheid als rijpheidskenmerk | Planners plannen aanbod zonder giswerk; alle benodigde gegevens liggen vooraf vast in de specificatie. | [Kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario%27s/leerroute-1-regulier.md) |  |
| <a id="feature-0013"></a>feature-0013 | Geldig, gefaseerd aanbod afleiden | Het geplande aanbod is altijd geldig en sluit in de tijd logisch aan op de vereiste leeruitkomsten. | [Keuze-requirements R9 en R11](../specificatie/student-keuze/keuze-requirements.md#6-requirements) | [Interactiepatroon OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md) |
| <a id="feature-0014"></a>feature-0014 | Eigenaarschap van het aanbodobject | Planninggegevens en specificatie-inhoud blijven gescheiden; het aanbodobject bevat geen dubbele of verouderde specificatiegegevens. | [Meetingverslag 10 juli](../../meetings/20260710_okx_kernteam_inhoud_specificatie_uitwerken_OC_P/summary.md#besluiten) | [Datamodelschema's, onderwijsaanbod](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/README.md#onderwijsaanbod) |
| <a id="feature-0015"></a>feature-0015 | Haalbaarheid van keuze en ontwerp toetsen | De student weet vóór bevestiging of zijn keuze haalbaar is, via acceptatie, afwijzing of een alternatief. | [ADR 0015](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md) |  |

## [Betrouwbare en vervangbare koppelingen](epics.md#epic-0004)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0016"></a>feature-0016 | Betrouwbaar berichtenverkeer | Consumenten missen nooit een mutatie en verwerken elk bericht eenmalig en in de juiste volgorde. | [Uitgangspunten U4 en U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |  |
| <a id="feature-0017"></a>feature-0017 | Authenticatie via OAuth 2.0 Client Credentials | Alleen geautoriseerde consumenten krijgen toegang tot endpoints, via één gedeeld mechanisme voor alle koppelvlakken. | [Auth-standaard](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/auth-standaard.md) |  |
| <a id="feature-0018"></a>feature-0018 | Maximaal twee actieve major versies | Afnemers hebben altijd voldoende tijd om over te stappen naar een nieuwe major versie. | [Meetingverslag 14 juli](../../meetings/20260714_SI_afstemming_PR_specificatie_uitwerking_P_en_R/summary.md#progress) |  |
| <a id="feature-0019"></a>feature-0019 | Intra-instelling eerst, federatie gefaseerd | Instellingen gebruiken koppelingen eerst betrouwbaar binnen de eigen instelling, vóór cross-instelling uitbreiding nodig is. | [Uitgangspunt U10](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |  |

## [Standaard beproeven en adopteren](epics.md#epic-0005)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0020"></a>feature-0020 | Standaard beproeven met pilotscholen | De standaard is bij pilotinstellingen in de praktijk beproefd voordat bredere adoptie start. | [Meetingverslag 17 april, POC-scholen](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#voortgang-en-selectie-van-de-poc-scholen) |  |
| <a id="feature-0021"></a>feature-0021 | Kennisopbouw bij instellingen | Instellingen beschikken over de kennis om de standaard en de onderliggende referentiearchitectuur toe te passen. | [Meetingverslag 17 april, MORA en kennisoverdracht](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#uitdagingen-rondom-de-mora-en-kennisoverdracht) |  |
| <a id="feature-0022"></a>feature-0022 | Leveranciersafspraken borgen via richtlijnen | Afspraken met leveranciers zijn geborgd zodat implementaties de standaard blijven volgen. | [Meetingverslag 17 april, EduV en borging](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#status-van-eduv-en-potentiële-borging-integratiestandaarden) |  |
| <a id="feature-0023"></a>feature-0023 | Feedbackloop met leveranciers en scholen | Specificaties zijn aangescherpt op basis van praktijkervaring van leveranciers en scholen. | [Meetingverslag 17 april, adoptiestrategie](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#stakeholdermanagement-en-adoptiestrategie) |  |

## [Student kiest onderwijsspecificaties](epics.md#epic-0006)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0024"></a>feature-0024 | Kiesbaarheid bepalen | Voor elke student staat op elk niveau vast welke onderwijsspecificaties hij mag kiezen (eligibility). | [Keuze-requirements R1](../specificatie/student-keuze/keuze-requirements.md#6-requirements) |  |
| <a id="feature-0025"></a>feature-0025 | Keuzecriteria als queryparameters op de aanbodquery | Systemen doorzoeken het onderwijsaanbod met precieze, herbruikbare criteria die rechtstreeks uit de leervraag volgen. | [ADR 0007](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) |  |
| <a id="feature-0026"></a>feature-0026 | Regelsets los van items, met min/max-keuzeregels | Beheerders wijzigen regelsets los van catalogusitems en drukken keuzevormen met een minimum en maximum uit. | [Keuze-requirements R2 en R5](../specificatie/student-keuze/keuze-requirements.md#6-requirements) |  |
| <a id="feature-0027"></a>feature-0027 | Leeruitkomst-id's als verbindende sleutels in keuzeregels | Systemen wisselen keuzegegevens uit zonder de inhoud van leeruitkomsten te hoeven delen. | [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md) en [Keuze-requirements R14 en R15](../specificatie/student-keuze/keuze-requirements.md#6-requirements) | [Interactiepatroon OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md) |
| <a id="feature-0028"></a>feature-0028 | Regelsets versioneren voor verantwoording | Achteraf staat vast welke regelversie gold bij een keuze, nodig voor de diplomaverantwoording. | [Keuze-requirements R17](../specificatie/student-keuze/keuze-requirements.md#6-requirements) |  |
| <a id="feature-0029"></a>feature-0029 | Bottom-up en top-down samenstellen | Een opleiding is van bovenaf en van onderop samen te stellen, met dezelfde onderliggende onderdelen als uitkomst. | [Keuze-requirements R13](../specificatie/student-keuze/keuze-requirements.md#6-requirements) |  |

## [Keuze en verbintenis vastleggen](epics.md#epic-0007)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0030"></a>feature-0030 | Verbintenis als toestandsmachine per niveau | Systemen en actoren stellen op elk niveau, van programma tot toets, de actuele status van de verbintenis vast. | [Begrippenkader, stadia van onderwijsverbintenis](../specificatie/leerroute-uitwerking/doc/begrippenkader.md#stadia-van-onderwijsverbintenis-aangemeld-ingeschreven-deelnemend-afgerond) |  |
| <a id="feature-0031"></a>feature-0031 | Keuze gescheiden van inschrijving en resultaat | Studentkeuze staat als eigen verantwoordelijkheid los van de formele inschrijving en van resultaat en voortgang. | [ADR 0014](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md) en [ADR 0009](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) |  |
| <a id="feature-0032"></a>feature-0032 | Examenplanwijzigingen alleen na impactanalyse | Een wijziging in het examenplan raakt lopende verbintenissen nooit ongecontroleerd. | [Interactiepatroon OC-SIS, acceptatietoets](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#acceptatietoets-bij-wijziging-examenplan) |  |

## [Voortgang en resultaat op leeruitkomsten](epics.md#epic-0008)

| Id | Feature | Omschrijving | Bron | Verwijzing |
|---|---|---|---|---|
| <a id="feature-0033"></a>feature-0033 | Resultaatstructuur inrichten en resultaten registreren | Elk onderwijsresultaat koppelt gewogen en herleidbaar aan de behaalde leeruitkomsten van de student. | [ADR 0022](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) | [Interactiepatroon OC-SIS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md) |
| <a id="feature-0034"></a>feature-0034 | Voorwaarden vooraf uitgedrukt in behaalde leeruitkomsten | Een voorwaarde vooraf (prerequisite) is uitgedrukt in behaalde leeruitkomsten, niet in doorlopen specificaties; via welke route de student de leeruitkomst behaalde doet er niet toe. | [Keuze-requirements R7](../specificatie/student-keuze/keuze-requirements.md#6-requirements) |  |
| <a id="feature-0035"></a>feature-0035 | Aanvullend resultaat-koppelvlak voor bewijsvoering | Afnemers beschikken naast de verbintenisstatus over rijkere bewijsvoering van resultaten op leeruitkomstniveau. | [Begrippenkader, stadia van onderwijsverbintenis](../specificatie/leerroute-uitwerking/doc/begrippenkader.md#stadia-van-onderwijsverbintenis-aangemeld-ingeschreven-deelnemend-afgerond) |  |
| <a id="feature-0036"></a>feature-0036 | Toetsing zodra leeruitkomsten gedekt zijn | De student kan toetsen zodra de leeruitkomsten gedekt zijn, ook zonder elke leergelegenheid te hebben bijgewoond. | [Scenario 3.1](../specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-3.1-versnellen-by-design.md) |  |
