# Stories

Laag 4 van de [requirementsboom](README.md): toetsbare wensen van één actor, per uitgewerkte [epic](epics.md). De kolom Koppelvlak noemt de interactie en het systeem dat eigenaar wordt van de bijbehorende endpoint-set: wie de featureset wil ondersteunen, wordt eigenaar van die endpoints. Relateert aan: #130.

## Onderwijsaanbod specificeren en ontsluiten

| Story | Feature | Bron | Koppelvlak |
|---|---|---|---|
| Als onderwijsontwerper wil ik dat de keten bij publicatie valideert dat de studielast (SBU/EC) van onderliggende delen optelt naar het bovenliggende niveau, zodat een aggregatiefout tot terugdraaien (rollback) leidt. | Hiërarchische, refereerbare specificatiestructuur | [ADR 0017](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md) | geen |
| Als planner wil ik dat bij een specificatie-update de vorige versie actief blijft voor lopend aanbod en de nieuwe alleen op nieuw aanbod geldt, zodat lopende planningen niet breken. | Stabiele identiteit en versionering van specificaties | [Consumer-profiel §19, F10](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | I4, eigenaar OC ([OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md)) |
| Als onderwijsontwikkelaar wil ik dat het leermanagementsysteem de gelegde leermiddelkoppeling als eigen resource terugmeldt, zodat de catalogus die kan ophalen en tonen bij het aanbod. | Leeromgeving inrichten op de specificatie | [Koppelingspecificatie OC-LMS, §2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-lms/koppelingspecificatie-oc-lms.md) | L4 en L5, eigenaar LMS ([OC-LMS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-lms/koppelingspecificatie-oc-lms.md)) |

## Student kiest onderwijsspecificaties

| Story | Feature | Bron | Koppelvlak |
|---|---|---|---|
| Als student wil ik dezelfde opleiding by design in een lager tempo kunnen volgen, bijvoorbeeld vier in plaats van drie jaar, zodat ik studeren met werk en gezin kan combineren. | Kiesbaarheid bepalen | [Consumer-profiel §3.4.5](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | geen |
| Als student wil ik eerst de door mijn instelling voorgesorteerde keuzedelen zien, zodat ik gericht kan kiezen binnen mijn leerroute en keuzedeelruimte. | Kiesbaarheid bepalen | [Persona Jochem, kiezen keuzedelen](../specificatie/okx-oeapi-consumer-profiel/doc/persona_jochem.md) | geen |
| Als student wil ik alleen keuzedelen als kiesbaar zien wanneer ze op mijn locatie en in mijn periode beschikbaar zijn, zodat ik geen onhaalbare keuze maak. | Kiesbaarheid bepalen | [PR 120, R3 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |
| Als planner wil ik dezelfde voorwaarde-regel gebruiken die het keuzemoment stuurde, zodat keuze en rooster niet uiteenlopen. | Regelsets los van items, met min/max-keuzeregels | [PR 120, R8 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |
| Als instelling wil ik naast algemene en beroepsspecifieke keuzedelen eigen kiesbaarheidsklassen kunnen toevoegen, zodat de indeling niet vastligt. | Regelsets los van items, met min/max-keuzeregels | [PR 120, R10 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |

## Aanbod plannen en roosteren

| Story | Feature | Bron | Koppelvlak |
|---|---|---|---|
| Als planner wil ik dat de catalogus een planbaar geworden specificatie met een dun event (id en versie) meldt en ik de structuur of delta kan ophalen, zodat ik er opleidingsaanbod van kan maken. | Geldig, gefaseerd aanbod afleiden | [Koppelingspecificatie OC-P&R, §3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) | I1 en I2, eigenaar OC ([OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md)) |
| Als onderwijsontwikkelaar wil ik dat planning en roostering de verwerkingsstatus met referentie naar het opleidingsaanbod terugmeldt, zodat de catalogus weet of de specificatie planbaar bleek. | Geldig, gefaseerd aanbod afleiden | [Koppelingspecificatie OC-P&R, §3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) | I3, eigenaar P&R ([OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md)) |
| Als planner wil ik de groep herkennen die hoort bij de combinatie keuzedeel, locatie en periode, zodat keuzes stabiel tussen systemen uitwisselbaar zijn. | Geldig, gefaseerd aanbod afleiden | [PR 120, R4 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |
| Als roosteraar wil ik geroosterd aanbod per periode publiceren en beschikbaar stellen aan student en docent, zodat latere perioden planbaar blijven. | Drie stadia van onderwijsaanbod | [Consumer-profiel §3.4.1](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | geen |
| Als student wil ik voor de start van het onderwijs toegang tot het leermanagementsysteem en mijn periode-rooster krijgen, zodat ik op de eerste lesdag kan beginnen. | Drie stadia van onderwijsaanbod | [Consumer-profiel §3.4.1](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | geen |
| Als onderwijsontwerper wil ik dat het planningssysteem mijn concept-programma met een snelle toets (quick scan) op realiseerbaarheid beoordeelt, zodat ik het ontwerp vóór publicatie kan aanpassen. | Haalbaarheid van keuze en ontwerp toetsen | [Consumer-profiel §19, F3](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | geen |

## Voortgang en resultaat op leeruitkomsten

| Story | Feature | Bron | Koppelvlak |
|---|---|---|---|
| Als docent wil ik tijdens de uitvoering per les de verbintenistoestand (Association.state) van studenten muteren en resultaten vastleggen, zodat voortgang en resultaat herleidbaar zijn. | Resultaatstructuur inrichten en resultaten registreren | [Consumer-profiel §3.4.1](../specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | geen |
| Als student wil ik vrijstellingen kunnen aanvragen op basis van eerder behaalde resultaten of aangetoonde competenties, zodat ik mijn opleiding versneld kan afronden. | Toetsing zodra leeruitkomsten gedekt zijn | [Persona Linda, examineren](../specificatie/okx-oeapi-consumer-profiel/doc/persona_linda.md) | geen |
