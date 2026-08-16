# Stories

Laag 4 van de [requirementsboom](README.md): toetsbare wensen van één actor, per uitgewerkte [epic](epics.md). De kolom Koppeling noemt de interactie en het systeem dat eigenaar wordt van de bijbehorende endpoint-set: wie de featureset wil ondersteunen, wordt eigenaar van die endpoints. Relateert aan: #130.

## Onderwijsaanbod specificeren en ontsluiten

| Id | Story | Feature | Bron | Koppeling | Raakt ook |
|---|---|---|---|---|---|
| S1.1 | Als onderwijsontwerper wil ik dat de keten bij publicatie valideert dat de studielast (studiebelastingsuren en studiepunten, SBU/EC) van onderliggende delen optelt naar het bovenliggende niveau, zodat een aggregatiefout tot terugdraaien (rollback) leidt. | F1.2 Hiërarchische, refereerbare onderwijsspecificatiestructuur | [ADR 0017](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md) | geen | |
| S1.2 | Als planner wil ik dat bij een specificatie-update de vorige versie actief blijft voor lopend aanbod en de nieuwe alleen op nieuw aanbod geldt, zodat lopende planningen niet breken. | F1.3 Stabiele identiteit en versionering van specificaties | [Archief leerroute-uitwerking §19, F10](../specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md#19-faalmatrix--overzicht-ketenfaalmodi) | I4, eigenaar OC ([OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md)) | E3 |
| S1.3 | Als onderwijsontwikkelaar wil ik dat het leermanagementsysteem de gelegde leermiddelkoppeling als eigen resource terugmeldt, zodat de catalogus die kan ophalen en tonen bij het aanbod. | F1.4 Leeromgeving inrichten op de specificatie | [Koppelingspecificatie OC-LMS, §2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-lms/koppelingspecificatie-oc-lms.md) | L4 en L5, eigenaar LMS ([OC-LMS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-lms/koppelingspecificatie-oc-lms.md)) | |

## Student kiest onderwijsspecificaties

| Id | Story | Feature | Bron | Koppeling |
|---|---|---|---|---|
| S2.1 | Als student wil ik dezelfde opleiding by design in een lager tempo kunnen volgen, bijvoorbeeld vier in plaats van drie jaar, zodat ik studeren met werk en gezin kan combineren. | F2.1 Kiesbaarheid bepalen | [Scenario 2.1](../specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-2.1-temporiseren-by-design.md) | geen |
| S2.2 | Als student wil ik eerst de door mijn instelling voorgesorteerde keuzedelen zien, zodat ik gericht kan kiezen binnen mijn leerroute en keuzedeelruimte. | F2.1 Kiesbaarheid bepalen | [Persona Jochem, kiezen keuzedelen](../specificatie/leerroute-uitwerking/doc/persona_jochem.md#kiezen-keuzedelen) | geen |
| S2.3 | Als student wil ik alleen keuzedelen als kiesbaar zien wanneer ze op mijn locatie en in mijn periode beschikbaar zijn, zodat ik geen onhaalbare keuze maak. | F2.1 Kiesbaarheid bepalen | [PR 120, R3 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |
| S2.4 | Als planner wil ik dezelfde voorwaarde-regel gebruiken die het keuzemoment stuurde, zodat keuze en rooster niet uiteenlopen. | F2.3 Regelsets los van items, met min/max-keuzeregels | [PR 120, R8 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |
| S2.5 | Als instelling wil ik naast algemene en beroepsspecifieke keuzedelen eigen kiesbaarheidsklassen kunnen toevoegen, zodat de indeling niet vastligt. | F2.3 Regelsets los van items, met min/max-keuzeregels | [PR 120, R10 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |

## Aanbod plannen en roosteren

| Id | Story | Feature | Bron | Koppeling |
|---|---|---|---|---|
| S3.1 | Als planner wil ik dat de catalogus een planbaar geworden specificatie met een dun event (id en versie) meldt en ik de structuur of delta kan ophalen, zodat ik er opleidingsaanbod van kan maken. | F3.3 Geldig, gefaseerd aanbod afleiden | [Koppelingspecificatie OC-P&R, §3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) | I1 en I2, eigenaar OC ([OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md)) |
| S3.2 | Als onderwijsontwikkelaar wil ik dat planning en roostering de verwerkingsstatus met referentie naar het opleidingsaanbod terugmeldt, zodat de catalogus weet of de specificatie planbaar bleek. | F3.3 Geldig, gefaseerd aanbod afleiden | [Koppelingspecificatie OC-P&R, §3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md) | I3, eigenaar P&R ([OC-P&R](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md)) |
| S3.3 | Als planner wil ik de groep herkennen die hoort bij de combinatie keuzedeel, locatie en periode, zodat keuzes stabiel tussen systemen uitwisselbaar zijn. | F3.3 Geldig, gefaseerd aanbod afleiden | [PR 120, R4 (in review)](https://github.com/Npuls-OKx/meta/pull/120) | geen |
| S3.4 | Als roosteraar wil ik geroosterd aanbod per periode publiceren en beschikbaar stellen aan student en docent, zodat latere perioden planbaar blijven. | F3.1 Drie stadia van onderwijsaanbod | [Scenario 1.1](../specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md) | geen |
| S3.5 | Als student wil ik voor de start van het onderwijs toegang tot het leermanagementsysteem en mijn periode-rooster krijgen, zodat ik op de eerste lesdag kan beginnen. | F3.1 Drie stadia van onderwijsaanbod | [Scenario 1.1](../specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md) | geen |
| S3.6 | Als onderwijsontwerper wil ik dat het planningssysteem mijn concept-programma met een snelle toets (quick scan) op realiseerbaarheid beoordeelt, zodat ik het ontwerp vóór publicatie kan aanpassen. | F3.5 Haalbaarheid van keuze en ontwerp toetsen | [Archief leerroute-uitwerking §19, F3](../specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md#19-faalmatrix--overzicht-ketenfaalmodi) | geen |

## Voortgang en resultaat op leeruitkomsten

| Id | Story | Feature | Bron | Koppeling |
|---|---|---|---|---|
| S5.1 | Als docent wil ik tijdens de uitvoering per les de verbintenistoestand (Association.state) van studenten muteren en resultaten vastleggen, zodat voortgang en resultaat herleidbaar zijn. | F5.1 Resultaatstructuur inrichten en resultaten registreren | [Scenario 1.1](../specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md) | geen |
| S5.2 | Als student wil ik vrijstellingen kunnen aanvragen op basis van eerder behaalde resultaten of aangetoonde competenties, zodat ik mijn opleiding versneld kan afronden. | F5.4 Toetsing zodra leeruitkomsten gedekt zijn | [Persona Linda, examineren](../specificatie/leerroute-uitwerking/doc/persona_linda.md#examineren) | geen |
