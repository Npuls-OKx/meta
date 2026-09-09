# Informatiemodel OKx

## Context

OKx maakt gestandaardiseerde koppelvlakken voor onderwijslogistiek. Die koppelvlakken wisselen informatie uit, en die informatie moet aan beide kanten hetzelfde betekenen.

## Inleiding

Dit document zet het informatiemodel van OKx uiteen: welke objecttypen de keten van kwalificatiekader tot resultaat kent, hoe ze samenhangen, en welke begrippen die keten indelen. De plaat is de weergave, dit document geeft de conventies en de keuzes erachter.

## Doel

Het uiteenzetten van de informatiearchitectuur van de belangrijkste informatieobjecten binnen het OKx-ecosysteem, als gedeelde grondslag voor de koppelvlakspecificaties. Het model wordt bekrachtigd door de kerngroep techniek en is daarna de bron waaruit payloads en endpoints worden afgeleid.

## Scope

De businesslaag en het informatieaspect, binnen een instelling. Buiten scope: applicatiecomponenten, techniekkeuzes, federatie tussen instellingen, en de attributen en datatypes die in de payload-specificaties thuishoren.

![Informatiemodel OKx, versie v0.1 van 9 september 2026](<OKx informatiemodel v0.1.jpg>)

## Lezers en detailniveau

| | |
|---|---|
| **Voor wie** | Kerngroep techniek, implementerende partijen, informatiemanagers en enterprise-architecten van instellingen |
| **Detailniveau** | Objecttypen en hun samenhang. Geen attributen en geen datatypes |

## Begrippen

De kolommen op de plaat zijn de begrippen waarin OKx de keten indeelt. Ze vormen daarmee het model van begrippen, niveau 1 in het [Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/); de objecttypen binnen die kolommen zijn het conceptuele informatiemodel, MIM-niveau 2.

| Begrip | Wat het is | Beantwoordt de vraag |
|---|---|---|
| Kwalificatiekader mbo | Het geheel van landelijk vastgestelde eisen waaraan een opleiding moet voldoen. Vastgesteld en beheerd buiten OKx | Wat is normatief geldig |
| Onderwijskundig kader instelling | De vertaling van dat kwalificatiekader naar wat een student moet kennen en kunnen, gemaakt door de instelling zelf | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Het herbruikbare ontwerp van een onderwijsonderdeel, los van wanneer het draait en wie eraan meedoet | Wat wordt georganiseerd |
| Onderwijsaanbod | Een specificatie die is ingepland: een periode, een capaciteit en waar van toepassing concrete plek, docent en tijd | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | De relatie tussen een student en een aanbod, van aangemeld tot afgerond | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat een student op een verbintenis heeft behaald, uitgedrukt in leeruitkomsten | Wat is er behaald |
| Resultaatstructuur | De samenstelling en weging waarmee losse resultaten optellen tot een uitspraak over een kwalificatie of certificaat | Hoe telt dat op tot een uitspraak over de kwalificatie |

Objecttypen buiten de kolommen raken de hele keten: `Persoon`, `Student`, `Medewerker` en `Plaatsingsgroep`, het `Verzoek tot Aanbod / Intekening op specificatie` als brug van specificatie naar aanbod, en `Examenplan` en `Waarde document (diploma / certificaat)` die buiten scope staan.

## Notatie

**Kleur is scope.** Grijs staat als erkend begrip in het model, maar wordt door OKx niet vastgelegd.

**Relatiesoorten**, in ArchiMate-notatie.

| | Relatie | Betekenis in dit model |
|---|---|---|
| `──▷` | Specialisatie (specialization) | Een bijzonder geval van het algemenere type, met dezelfde informatiestructuur |
| `◇──` | Aggregatie (aggregation) | Het geheel bestaat uit deze delen; een deel kan ook zonder het geheel bestaan |
| `───` | Associatie (association) | Inhoudelijke samenhang zonder eigenaarschap of samenstelling |
| `╌╌▷` | Toegang (access) | Een persoon gebruikt of wijzigt dit objecttype, als student of als medewerker |

## Ontwerpkeuzes

1. **De leeruitkomst is de sleutel, en OKx legt hem niet vast.** Leeruitkomsten zijn landelijk gestandaardiseerd en in beheer, en instellingen vertalen kwalificatiekaders zelf vanuit hun onderwijskundige vrijheid. OKx gebruikt de leeruitkomst om specificatie, aanbod, verbintenis en resultaat aan elkaar te knopen.
2. **Het niveau waarop iets gespecificeerd wordt ligt niet vast.** Een `Onderwijseenheid specificatie` kan op kerntaakniveau liggen of op een ander niveau dat de instelling kiest. De koppeling loopt via de leeruitkomst, en daarom is het niveau geen eigenschap van de objecttypen.
3. **De leslaag valt buiten de uitwisseling.** `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan in het model zodat een latere behoefte om tot op lesniveau te beschrijven niet geblokkeerd wordt.
4. **Een examenonderdeel is een specialisatie van een toetsonderdeel.** Instellingen kunnen formatieve toetsen laten meetellen in de summatieve structuur. Daarom delen beide dezelfde informatiestructuur, terwijl hun totstandkoming strikt gescheiden is: een examenonderdeel wordt vastgesteld door de examencommissie, een toetsonderdeel volgt instellingsbeleid.
5. **Het examenplan berust op de summatieve resultaatstructuur.** OKx wisselt de `Summatieve resultaat structuur` uit: de examenonderdelen met hun wegingen en het afrondingscriterium dat de zak-slaagregeling draagt. Het examenplan als document valt buiten de uitwisseling.
6. **Een verbintenis loopt bij voorkeur via een groep.** `Plaatsingsgroep` maakt regulier onderwijs makkelijker te plannen en te roosteren. Het model sluit individuele verbintenissen niet uit.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Mapping naar OEAPI v6](informatiemodel-oeapi-mapping.md) | Dezelfde objecttypen met de Open Onderwijs API ernaast |
| [Begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) | Werkt de begrippen en hun subtypen verder uit |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken deze objecttypen uit tot velden en datatypes |
| [`informatiemodel.json`](informatiemodel.json) | Dit model machineleesbaar, gegenereerd uit `model.archimate` |
