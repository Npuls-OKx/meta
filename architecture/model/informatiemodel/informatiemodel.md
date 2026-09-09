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
| Onderwijskundig kader instelling | De vertaling van het kwalificatiekader naar beoogde leeruitkomsten, gemaakt door de instelling zelf | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Het herbruikbare ontwerp van een onderwijsonderdeel, los van wanneer het draait en wie eraan meedoet | Wat wordt georganiseerd |
| Onderwijsaanbod | Een specificatie die is ingepland: een periode, een capaciteit en waar van toepassing concrete plek, docent en tijd | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | De relatie tussen een student en een aanbod, van aangemeld tot afgerond | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat een student op een verbintenis heeft behaald, uitgedrukt in leeruitkomsten | Wat is er behaald |
| Resultaatstructuur | De samenstelling en weging waarmee losse resultaten optellen tot een uitspraak over de beoogde leeruitkomsten, en daarmee over een kwalificatie of certificaat | Hoe telt dat op tot een uitspraak over de kwalificatie |

Objecttypen buiten de kolommen raken de hele keten: `Persoon`, `Student`, `Medewerker` en `Plaatsingsgroep`, het `Verzoek tot Aanbod / Intekening op specificatie` als brug van specificatie naar aanbod, en `Examenplan` en `Waarde document (diploma / certificaat)` die buiten scope staan.

## Notatie

**Kleur.** Geel is het OKx-referentiekader, afgestemd op MORA en HORA via klus 53. Grijs staat als erkend begrip in het model maar valt buiten de scope van OKx: de leslaag, het examenplan als document, en de onderwijskundige begrippen `Competenties / Skills`, `Kennis`, `Vaardigheid` en `Inzicht`. Blauw is OEAPI v6 en komt alleen voor op de [mapping](informatiemodel-oeapi-mapping.md).

**Relatiesoorten**, in ArchiMate-notatie.

| | Relatie | Betekenis in dit model |
|---|---|---|
| `──▷` | Specialisatie (specialization) | Een bijzonder geval van het algemenere type, met dezelfde informatiestructuur |
| `◇──` | Aggregatie (aggregation) | Het geheel bestaat uit deze delen; een deel kan ook zonder het geheel bestaan |
| `───` | Associatie (association) | Inhoudelijke samenhang zonder eigenaarschap of samenstelling |
| `╌╌▷` | Toegang (access) | Een persoon gebruikt of wijzigt dit objecttype, als student of als medewerker |

Waar de betekenis niet uit de twee objecttypen volgt, draagt de associatie een label. Dat label hoort bij het model en niet bij de plaat: `Wordt vertaald naar`, `voorwaarde op`, `bestaat uit`, `bevat`, `conform`.

## Ontwerpkeuzes

1. **De leeruitkomst is de sleutel die specificaties en resultaatstructuur verbindt.** Elke specificatie wijst naar leeruitkomsten en de summatieve resultaatstructuur ook; daarmee is de leeruitkomst het enige objecttype dat over de begrippen heen loopt. Een leeruitkomst kan subleeruitkomsten bevatten.
2. **Het kwalificatiekader wordt vertaald naar leeruitkomsten, niet gespecialiseerd.** Kwalificatiedossier, kwalificatie, kerntaak en werkproces stellen vast wat normatief geldig is; de instelling vertaalt dat naar leeruitkomsten, vanuit haar onderwijskundige vrijheid. Een leeruitkomst is dus geen bijzonder geval van een werkproces. Een instelling die geen eigen leeruitkomsten formuleert kan die vertaling een op een maken, waarbij de leeruitkomst met het werkproces samenvalt.
3. **Uitwisseling tussen instellingen vraagt landelijk gestandaardiseerde leeruitkomsten.** Die standaardisatie en dat beheer bestaan nog niet; er loopt een apart traject voor, waarvan OKx de aanjager is. Zonder dat blijft een leeruitkomst instellingseigen en is aanbod van verschillende instellingen niet te vergelijken.
4. **Het niveau waarop iets gespecificeerd wordt ligt niet vast.** Een `Onderwijseenheid specificatie` kan op kerntaakniveau liggen of op een ander niveau dat de instelling kiest. De koppeling loopt via de leeruitkomst, en daarom is het niveau geen eigenschap van de objecttypen.
5. **Een specificatie kan zelfstandig bestaan.** Specificaties onder de `Opleiding specificatie` kunnen onderdeel zijn van een bovenliggende specificatie, maar hoeven dat niet. Een `Opleidingsprogramma specificatie` zonder bovenliggende `Opleiding specificatie` is geldig.
6. **De student kiest uit specificaties, niet uit leeruitkomsten.** De `Student keuze regelset` wijst naar de specificatietypen waaruit gekozen kan worden. Leeruitkomsten komen erin voor als voorwaarde op die keuze, bijvoorbeeld dat de gekozen specificatie een bepaald type leeruitkomst afdekt. Een student kiest daarmee altijd onderwijs dat een instelling ook daadwerkelijk vormgeeft.
7. **De leslaag valt buiten de uitwisseling.** `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan in het model zodat een latere behoefte om tot op lesniveau te beschrijven niet geblokkeerd wordt.
8. **Een examenonderdeel is een specialisatie van een toetsonderdeel.** Beide delen dezelfde informatiestructuur; hun totstandkoming is strikt gescheiden, want een examenonderdeel wordt vastgesteld door de examencommissie en een toetsonderdeel volgt instellingsbeleid. De summatieve resultaatstructuur is samengesteld uit toetsonderdelen, zodat een instelling ook een formatief toetsonderdeel summatief kan laten meetellen. Wordt een toetsonderdeel op die manier opgenomen, dan volgt het vanaf dat moment de examenketen.
9. **Het examenplan berust op de summatieve resultaatstructuur.** OKx wisselt de `Summatieve resultaat structuur` uit: de examenonderdelen met hun wegingen en het afrondingscriterium dat de zak-slaagregeling draagt. Het examenplan als document valt buiten de uitwisseling.
10. **Een verbintenis loopt bij voorkeur via een groep.** `Plaatsingsgroep` maakt regulier onderwijs makkelijker te plannen en te roosteren en geldt voor alle acht verbintenistypen. Het model sluit individuele verbintenissen niet uit.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Mapping naar OEAPI v6](informatiemodel-oeapi-mapping.md) | Dezelfde objecttypen met de Open Onderwijs API ernaast |
| [Begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) | Werkt de begrippen en hun subtypen verder uit |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken deze objecttypen uit tot velden en datatypes |
| [`informatiemodel.json`](informatiemodel.json) | Dit model machineleesbaar, gegenereerd uit `model.archimate` |
