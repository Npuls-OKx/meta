# Informatiemodel OKx

Het conceptuele informatiemodel van OKx: welke informatieobjecten de keten van kwalificatiekader tot resultaat kent, hoe ze zich tot elkaar verhouden, en waar de OKx-scope ophoudt. Doel: een ontwerp dat de kerngroep techniek kan bekrachtigen, zodat de koppelingspecificaties erop kunnen bouwen. Wat de standaard OEAPI hiervan wel en niet dekt staat in de [mapping](informatiemodel-oeapi-mapping.md).

![Informatiemodel OKx](<OKx informatiemodel v0.1.jpg>)

## Viewpoint

| | |
|---|---|
| **Voor wie** | Kerngroep techniek, leveranciers, informatiemanagers en enterprise-architecten van instellingen |
| **Doel** | Ontwerpen en besluiten. De kerngroep techniek bekrachtigt dit model; daarna is het de bron voor de koppelingspecificaties |
| **Vraag die het beantwoordt** | Welke informatieobjecten onderscheidt OKx, hoe hangen ze samen, en wat legt OKx bewust niet vast |
| **Scope** | Businesslaag, informatieaspect, binnen een instelling. Geen applicatiecomponenten, geen techniek, geen federatie |
| **Detailniveau** | Objecttypen en hun samenhang. Geen attributen en geen datatypes; die staan in de payload-specificaties |

## Notatieconventies

**De kolommen zijn begrippen.** Ze delen de keten in naar de vraag die ze beantwoorden, en vormen daarmee het model van begrippen: niveau 1 in het [Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/). De objecttypen binnen die kolommen zijn het conceptuele informatiemodel, MIM-niveau 2. De payload-specificaties in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) vormen het logische niveau, MIM-niveau 3.

| Kolom | Beantwoordt de vraag |
|---|---|
| Kwalificatiekader MBO | Wat is normatief geldig |
| Onderwijskundigkader instelling | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Wat gaan we organiseren |
| Onderwijsaanbod | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat is er behaald |
| Resultaatstructuur | Hoe telt dat op tot een uitspraak over de kwalificatie |

Objecttypen die geen kolom hebben raken de hele keten: `Persoon`, `Plaatsingsgroep`, en `Verzoek tot Aanbod / Intekening op specificatie` als brug van specificatie naar aanbod.

**Kleur is scope.** Geel legt OKx vast, uitgelijnd met MORA en HORA via klus 53. Grijs erkent OKx wel maar legt het niet vast.

**Vier relatiesoorten**, in ArchiMate-notatie.

| | Relatie | Betekenis in dit model |
|---|---|---|
| `──▷` | Specialisatie | Een bijzonder geval van het algemenere type, met dezelfde informatiestructuur |
| `◇──` | Aggregatie | Het geheel bestaat uit deze delen; een deel kan ook zonder het geheel bestaan |
| `───` | Associatie | Inhoudelijke samenhang zonder eigenaarschap of samenstelling |
| `╌╌▷` | Toegang | Een persoon raakt dit objecttype, als student of als medewerker |

## Ontwerpkeuzes

**De leeruitkomst is de sleutel, en OKx legt hem niet vast.** Leeruitkomsten zijn landelijk gestandaardiseerd en in beheer. Instellingen vertalen kwalificatiekaders zelf, vanuit hun onderwijskundige vrijheid. OKx gebruikt de leeruitkomst om specificatie, aanbod, verbintenis en resultaat aan elkaar te knopen en schrijft de vorm ervan niet voor.

**Het niveau waarop iets gespecificeerd wordt ligt niet vast.** Een `Onderwijseenheid specificatie` kan op kerntaakniveau worden gespecificeerd, en veel instellingen zullen dat doen, maar dat hoeft niet zo te blijven. De koppeling loopt via de leeruitkomst; op welk niveau een instelling haar specificaties formuleert is haar keuze. Daarom staat het niveau niet als eigenschap bij de objecttypen.

**De les-laag valt buiten de uitwisseling.** `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan in het model zodat een latere behoefte om tot op lesniveau te beschrijven niet geblokkeerd wordt. Er lopen geen uitwisselingen tussen applicatiecomponenten over.

**Een examenonderdeel is een specialisatie van een toetsonderdeel.** Instellingen kunnen formatieve toetsen laten meetellen in de summatieve structuur. Om dat te faciliteren delen beide dezelfde informatiestructuur, terwijl hun totstandkoming strikt gescheiden is: een examenonderdeel wordt vastgesteld door de examencommissie, een toetsonderdeel volgt instellingsbeleid.

**Het examenplan is bekend op de werkvloer, maar niet wat er uitgewisseld wordt.** OKx wisselt naar alle waarschijnlijkheid het document niet uit, maar de `Summatieve resultaat structuur` waarop het berust: de examenonderdelen met hun wegingen, en het afrondingscriterium dat de zak-slaagregeling draagt.

**Een verbintenis loopt bij voorkeur via een groep.** `Plaatsingsgroep` maakt regulier onderwijs makkelijker te plannen en te roosteren. Individuele verbintenissen moeten in de toekomst ook mogelijk zijn; het model sluit ze niet uit.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Mapping naar OEAPI v6](informatiemodel-oeapi-mapping.md) | Dezelfde objecttypen met de standaard ernaast |
| [Begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) | Levert de definities bij de kolommen en de objecttypen |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken deze objecttypen uit tot velden en datatypes |
| [`informatiemodel.json`](informatiemodel.json) | Dit model machineleesbaar, gegenereerd uit de bron |
