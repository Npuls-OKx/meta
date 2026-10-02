# Tegenlezing plan voorbeelduitwerking: softwarearchitect bij een leverancier van planning en rooster

Gelezen als de architect die tegen dit voorbeeld een planningssysteem (P) moet aansluiten. Verwijzingen: "plan rNN" is het regelnummer in `plan-voorbeelduitwerking.md`; Public-bestanden staan met eigen regelnummer. Ernst: blokkerend (kan er niet tegen bouwen), moet (voor 30 september herstellen), kan (later).

## 1. De vijf regels per stap (plan sectie 3 punt 1, r26)

| Bevinding | Ernst | Wat anders |
|---|---|---|
| Regel 3 noemt berichtstroom en patroon, geen bericht en geen endpoint. In Public hangen endpoints aan de dienst (OC-P&R r81-86 verwijst per endpoint naar de dienstpagina); de kaart laat mij dus opnieuw drie documenten openen om te zien welke webhook ik moet serveren | Moet | Zesde regel: bericht en endpoint (webhook-naam of GET-pad) met de status van de naam; `verwerkingsstatus` en `specificatie-planbaar` zijn voorstel, niet vastgesteld (verwerkingsuitkomst-afnemer.md r22, onderwijsspecificatiestructuur-afnemer.md r25) |
| Geen regel voor het foutpad. Elk sequentiediagram in Public heeft alt-takken (afgekeurd, niet gelukt, niet ingericht: OC-P&R r98-112, OC-SIS r94-98), de vijf regels tonen alleen het nominale verloop | Moet | Regel: terminale uitkomsten per bericht en wie daarna aan zet is (asynchronous-request-reply.md r44-46) |
| Geen regel voor versie. Er bestaan nu vier identifiers die niet aan elkaar hangen: berichtstroom 1.0 (OC-P&R r79), pakket koppelvlakspecificatie 0.0.1 en gegevensmodellen 0.1.0 (release.json), schema `$id` op `/alfa` zonder nummer | Moet | Regel: versie als feit per kaart (stroom, schema-`$id`, pakket); geen eigen versies verzinnen, wat plan r92 al wil |
| Regel 2 (aanbieder of afnemer) is de dienstrichting, niet wie de bron van het gegeven is (U3). De kaart zegt niet wie de payload bezit | Moet | Per payload de bezitter noemen; zie sectie 4 over de dubbele claim op de specificatie en het planbaar aanbod |
| Regel 5 kan het OEAPI-object gratis dragen: de mapping per objecttype bestaat (informatiemodel-oeapi-mapping.md r37-74) en plan r60 belooft hem op slide 3, terwijl plan r86 "de OEAPI-tegenhanger per endpoint" uitsluit | Kan | In regel 5 het OEAPI-object per objecttype opnemen; per endpoint buiten scope laten en dat onderscheid benoemen |
| Schrappen: niets. Het MORA-hoofdproces in regel 1 heeft voor mij geen functie, maar stoort niet als hij achteraan staat | Kan | Regel 1 in onderwijstaal laten, de vijf technische regels eerst op de kaart |

## 2. Instantiebestand en hergebruik van de payloads (plan sectie 3 punt 2 en 3, r27-28; stap 1, r54)

| Bevinding | Ernst | Wat anders |
|---|---|---|
| De voorbeeldpayloads dragen Nederlandse veldnamen, de schema's Engelse met `DutchName` als annotatie (mapping.md r3-5). Wie code genereert uit het schema (leverancier A, 15 september) kan het voorbeeld niet inlezen. Het plan zegt niet welke namen over de lijn gaan | Blokkerend | Het voorbeeld voor S2 en S4 in de veldnamen van het schema, of een expliciete zin dat de Engelse naam het contract is en de Nederlandse de leesvorm |
| Twee waarheden: `instanties.json` per objecttype en de payloads per schema. De controle (r27) faalt op ontbrekende objecttypen, lege relatiekanten en afwijkende namen, maar kruist de id's niet met de payloads | Moet | Controle: elk id in `instanties.json` komt voor in een payloadblok, en omgekeerd |
| De controle noemt geen schemavalidatie en geen oplossing van verwijzingen (`bovenliggendSpecificatieId`, `leeruitkomstId`, `specificatieVerwijzing`, `beoordeelt`, `geldtVoor`), terwijl r28 belooft dat de voorbeelden "voortaan valideren". Laag 4 sectie 6 punt 3 beschrijft precies die controle; het plan neemt alleen het dekkingsdeel over | Moet | Vertaling via `DutchName`, validatie met jsonschema en referentiecontrole in dezelfde controle |
| De controle komt in meta (r54), document en payloads in Public (r55, r58). De controle draait dan niet waar de data leeft; Public kent nog geen schemavalidatie | Moet | Controle in `Public/scripts` naast `check-conventies.py` |
| Delta 4 (cohort en startdatum van specificatie naar aanbod, r28, r70) wijzigt het voorbeeld, niet het schema: `education-specification.json` houdt `cohort` en `startDate`. Het contract blijft dubbelzinnig | Moet | Ook in het schema (schrappen of als verouderd markeren), of het voorbeeld draagt de aanname zichtbaar |
| `leeruitkomstId` is nergens verplicht (education-specification.json required-lijst) terwijl de leeruitkomst de sleutel is; een lege relatiekant in `instanties.json` vangt dat in de payload niet | Kan | Verplichte velden per profiel in de controle opnemen |

## 3. Stappentabel S2 en S4 tegen OC-P&R, OC-SIS en OC-LMS (plan sectie 4, r39 en r41)

| Rij | Wat het plan zegt | Wat Public zegt | Ernst |
|---|---|---|---|
| S2 dienst | "OC aanbieder, planning afnemer, verwerkingsuitkomst" | Klopt alleen voor onderwijsspecificatiestructuur. Bij planbaar-onderwijsaanbod en verwerkingsuitkomst is P aanbieder en OC afnemer (OC-P&R r31-36); de stroom zet vier diensten in (r79), de tabel noemt er drie zonder richting | Moet |
| S2 payload | education-specification, education-offering, processing-status | `specification-reference.json` ontbreekt: dat is de webhook `specificatie-planbaar` die ik moet serveren (onderwijsspecificatiestructuur-afnemer.md r21). `subscription.json` (voorwaarde Abonnement registreren, r264) ontbreekt | Moet |
| S2 dekking | "Volledig" | Het foutpad niet: "afgekeurd met foutmodel" (r111) en "niet gelukt met reden" (verwerkingsuitkomst-aanbieder.md r12) hebben geen veld in `processing-status.json` (alleen `status`, `programmeOfferingId`, `specificationReference`); knelpunten zitten in `education-offering.bottlenecks` en zijn alleen via de optionele GET te halen. De webhooknamen zijn voorstel (r22, r25) | Moet: "nominaal volledig, foutpad zonder schema, namen voorstel" |
| S2 trigger | Opleiding specificatie tot Opleidingaanbod en Opleidingsprogramma aanbod | Trigger r75 zegt "onderwijsspecificatie gepubliceerd", diagram r94 "opleidingsprogrammaspecificatie"; `programmeOfferingId` heet `opleidingsaanbodId`. Welke instantie ik terugmeld is niet eenduidig | Kan |
| S4 stroom | "Leeromgeving inrichten" | Heet "Leeromgeving inrichten en leermiddelkoppeling melden" (OC-LMS r65); de weggelaten helft is de terugstroom met twee berichten zonder schema (r78-79) | Kan |
| S4 payload | ... result-structure, group | Geen bericht in S4 draagt `group.json`; hij reist alleen genest in `education-offering` (S2). Rooster heeft geen endpoints (roostersysteem.md r13). Dit is datamodel zonder berichtstroom in regel 4 | Moet |
| S4 dekking | "Twee koppelingen volledig" | OC-SIS: 2 van 4 endpoints zonder schema (webhook beschikbaar: resultaatstructuur-afnemer.md r19 "nog niet uitgewerkt"; `inrichtingsstatus`: verwerkingsuitkomst-afnemer.md r22). OC-LMS: 3 van 5 (`inrichtingsstatus`, `leermiddelkoppeling-beschikbaar`, `GET /leermiddelkoppelingen/{id}` r19). Plan r15 zegt zelf "vier berichten hebben nog geen schema"; de tabel spreekt de analyse tegen | Moet |
| S4 afleveradres | Niet genoemd | OC-SIS r34 en OC-LMS r34 kennen geen afleverabonnement; `subscription.json` kent alleen de vier P&R-events. Voor S4 moet ik het webhook-adres buiten de specificatie om afspreken | Moet: als leemte in de rij |
| S4 volgorde | Niet genoemd | OC-SIS vuurt pas als specificatie en examenplanspecificatie beide gepubliceerd zijn (r67); scenario 1.1 kent die tweede publicatie niet. S2 en S4 vuren op dezelfde trigger naar drie afnemers zonder uitspraak over onderlinge afhankelijkheid, en de verfijning van leeronderdelen na publicatie zou herplannen en bijwerken laten vuren (S7 zet dat als "niet in de happy flow") | Moet: aanname "eenmalige publicatie, drie onafhankelijke afnemers" expliciet |

De leemtemarkering is eerlijk voor S1, S3, S5, S6 en S8. Voor S2 en S4 verbergt "volledig" de schemaloze berichten, het foutpad en het afleveradres; precies de rijen waar ik zou beginnen.

## 4. Besluiten en aannames (plan sectie 6)

| Aanname (plan) | Wat het verandert aan wat ik bouw | Ernst en status |
|---|---|---|
| Cohort en startdatum naar het aanbod (r70) | De planopgave. "Planning niet gelukt melden" spreekt van "een of meer cohorten" (OC-P&R r152); als de specificatie geen cohort en startdatum meer draagt, heeft mijn planproces geen input voor welk cohort het plant. `Verzoek tot Aanbod` heeft geen bericht | Moet: vraag, geen aanname; wie levert cohort, startdatum en aantal aan P |
| Examenplan als wortel, gepresenteerd als summatieve resultaatstructuur (r71) | Ik bouw tegen de enumwaarde `examenplanspecificatie` en `GET /examenplanspecificaties/{id}`; een hernoeming is brekend in schema en endpoint | Moet: vraag met versieconsequentie erbij |
| OC bezit, CO is bron (r78) | Bepaalt wie ik bevraag (OC) en wie planbaar aanbod ketenbreed levert: Public zegt P via `GET /onderwijsaanbod`, kaderscenario r880 zegt OC na publicatie (laag 2 sectie 1). Twee systemen claimen dezelfde waarheid | Moet: besluit of vraag, niet aanname |
| Een plaatsingsgroep en een cohort (r75) | Mijn planning maakt groepen (APO26-1A en 1B in het voorbeeld) met capaciteit; dat is niet de `Plaatsingsgroep` van de KRS (brugtabel r111, meta #235). De aanname verbergt dat het twee begrippen zijn | Kan: aanname houden, beide namen op de kaart |
| Toetsonderdeel eenmaal, in de resultaatstructuur (r72) | `education-specification.json` laat `toetsonderdeelspecificatie` ook in de specificatiepayload toe; het besluit bepaalt of P toetsonderdelen krijgt en toetsgelegenheden plant, en of de enumwaarde uit het specificatieschema gaat | Kan: de enumconsequentie bij de vraag zetten |
| Ontbreekt: patroon van de acceptatietoetsen (S7) | Transactie (request-reply) of notificatie plus status; staat niet in sectie 6 en niet in sectie 7 | Moet: vraag |
| Ontbreekt: een exemplaar per component per instelling; SIS als KRS plus SVS in een | Bij fusie of samenwerking meerdere P's of KRS'en op een OC; het abonnement (r264) veronderstelt een adres per partij | Kan: als bekende beperking noemen |

## 5. Afhaakpunten uit de persona

| Afhaakpunt | Waar het plan hem raakt | Ernst | Wat anders |
|---|---|---|---|
| Generiek endpoint zonder context | `GET /onderwijsspecificaties/{id}` is een endpoint voor drie gebruiksprofielen (gebruiksprofielen.md r9-29); geen parameter, header of dienstvariant selecteert het profiel; "een contract, ongeacht waarvoor" (onderwijsspecificatiestructuur-afnemer.md r3). Plan r26 regel 4 noemt het profiel, niet hoe het op het endpoint wordt gekozen. Als OC-bouwer weet ik niet wat ik aan wie serveer, als afnemer wat ik krijg; dit is het OKE-associatieprobleem | Blokkerend | Op de S2- en S4-kaart de profielselectie als leemte markeren en als vraag aan de kerngroep opnemen |
| Informeren of transactie per bericht | Regel 3 belooft het (r26), de tabel S1-S8 heeft de kolom niet. De acceptatietoetsen (OC-P&R r206-208, OC-SIS r126-128) zijn de enige transacties in het pakket en zijn als notificatie plus status gemodelleerd (laag 3 sectie 3); het plan zet ze als "varianten" (r44) en stelt geen patroonvraag (r84 heeft alleen a, b, c) | Moet | Kolom toevoegen; vraag d: patroon van de acceptatietoetsen |
| Schemaversies per endpoint zonder regel voor achterlopen | "Hoogstens twee major versies" per dienst (Applicatiediensten/README.md r32) zonder versie op enige dienst; schema op `/alfa`; stroom 1.0. Plan parkeert alles bij PR 100 (r86, r92) en bevriest zo "1.0" als contract | Moet | Stand van de identifiers als feit per kaart; het beleid als vraag |
| Datamodel los van de berichtstroom | Regel 4 hangt aan regel 3, goed. Maar stap 2 (r55) zet "de rest als tabel" en S4 noemt `group` zonder bericht | Kan | Elke rij zonder bericht draagt "geen bericht" |
| Begrip zonder definitie | 33 objecttypen zonder definitie (r17); S4 gebruikt `Leergelegenheid`, S3 `Plaatsingsgroep` | Moet | Regel 5 linkt de definitie of toont "geen definitie" |
| Interactie zonder endpoint | Het roostercontext-diagram (OC-P&R r293-310) heeft `GET opleidingsaanbod` en `GET rooster` zonder dienst; stap 2 (r55) hergebruikt sequentiediagrammen | Kan | Dit diagram alleen grijs, of niet hergebruiken |
| Ontbrekende foutpaden | Zie sectie 1 en S2-dekking in sectie 3 | Moet | Foutpad per kaart |
| Wijziging zonder overzicht | De vier delta's op de payloads (r28) landen gestapeld op PR 104 (r58) zonder wijzigingsoverzicht in `voorbeeldpayloads.md` | Kan | Sectie "gewijzigd ten opzichte van" bij de payloads |

## 6. Wat het voorbeeld niet oplost (plan sectie 7, r86)

| Afbakening | Oordeel | Ernst |
|---|---|---|
| Geen koppelingspecificaties voor S3, S5, S6, S8; geen entiteiten verbintenis en resultaat; geen besluit intekenen; geen brug tussen de platen | Eens; specificeren door voorbeeld is precies wat ik niet wil | |
| OEAPI-tegenhanger volledig buiten | Oneens voor het objecttype (mapping bestaat, slide 3 belooft hem); eens voor het endpoint | Kan |
| Versionering volledig buiten | Oneens: de bestaande identifiers zijn een feit dat op de kaart hoort; alleen het beleid is de vraag aan Garik | Moet |
| Ontbreekt vóór het bouwen | Profielselectie op het endpoint; patroon van de acceptatietoetsen; afleveradres voor OC-SIS en OC-LMS; reden en foutmodel in `processing-status.json`; input van het planproces na delta 4 | Moet |
| Toetslijst per referentiecomponent (r56) | Mijn product is planning en rooster samen; de lijst moet beginnen met "welke referentiecomponenten dekt uw product", anders leg ik SIS, P en R niet op mijn grenzen | Kan |

## Oordeel

Als leeswijzer voor de kerngroep is het plan bruikbaar: de vijf regels en de leemtemarkering voor S1, S3, S5, S6 en S8 geven mij zonder de stories te lezen het beeld waar de specificatie staat. Als bouwvoorbeeld is het nog niet bruikbaar: de twee stappen die "volledig" heten, dragen een generiek endpoint zonder profielselectie, berichten zonder schema, een foutpad zonder veld en een voorbeeld in veldnamen die niet over de lijn gaan. De drie belangrijkste punten:

1. S2 en S4 niet als "volledig" presenteren: per bericht de status (schema, naam voorstel, foutpad, afleveradres), anders leest een leverancier een bouwbelofte die het pakket niet draagt (sectie 3).
2. Twee vragen toevoegen aan sectie 7: hoe het gebruiksprofiel op `GET /onderwijsspecificaties/{id}` wordt geselecteerd, en of de acceptatietoetsen transactie of notificatie zijn (sectie 5); zonder antwoord bouw ik op een aanname.
3. Delta 4 (cohort naar het aanbod) en het eigenaarschap zijn besluiten die de input van mijn planproces bepalen, geen aannames (sectie 4); en de controle hoort in Public met schemavalidatie, referentiecontrole en het voorbeeld in de schema-veldnamen (sectie 2).
