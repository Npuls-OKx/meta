# Leesroute OKx

| Deel | De vraag | Kern | Verdieping |
|---|---|---|---|
| [1 Context](#deel-1-context) | Waarvoor bestaat OKx | 5 min | optioneel, 12 min |
| [2 Historisch overzicht](#deel-2-historisch-overzicht) | Hoe is het zo gelopen | | optioneel, 10 min |
| [3 Scope](#deel-3-scope) | Waar houdt het op | 10 min | optioneel, 50 min |
| [4 Deliverables](#deel-4-deliverables) | Wat komt eruit | 18 min | optioneel, 65 min |
| [5 Architectuurbesluiten](#deel-5-architectuurbesluiten) | Waarop steunt dat | 6 min | optioneel, 23 min |
| [6 Release en beheer](#deel-6-release-en-beheer) | Hoe blijft het in leven | 4 min | optioneel, 9 min |
| [7 Wat nu](#deel-7-wat-nu) | Waar stap ik in | 2 min | |

Kern: 45 minuten. Alles: ongeveer drie uur.

Wat hier staat is grotendeels **concept** en **voorstel**: een uitwerking om op te schieten. Niets is bekrachtigd door de sector, en release 0.0.1 van augustus 2026 kreeg geen review. Per stap hieronder zegt de statusregel waar dat deel op staat.

![De producten van OKx op de statusladder, met het werk dat beweegt tussen status 1 en 4](img/visueel/status-nu.svg)

Leestijd is de woordtelling gedeeld door honderdtwintig woorden per minuut, het tempo waarop architectuurmateriaal leest dat een lezer moet kunnen navertellen. Per stap staat de status van het materiaal met de lopende pull request erbij; de route schrijft geen statuswaarde over.

## Deel 1, context

**Waarvoor bestaat OKx, en waarom lost het bestaande dat niet op?**

![Keuzemogelijkheden ontleed: vier niveaus van binnen de eigen opleiding tot over sectoren heen, met de leerroutetekeningen van Npuls erbij](img/visueel/keuzeniveaus.svg)

*De negen leerroutetekeningen van Npuls, voluit en op formaat: [de leerroutes met hun keten](../architecture/docs/specificatie/leerroute-uitwerking/img/README.md).*

De sector vraagt om meer keuze. Elk niveau hoger brengt partijen buiten de eigen muren in beeld, en vraagt daarmee meer afspraken, meer uitwisseling en meer beschrijflast. Een instelling kiest zelf welk niveau bij haar past.

![Voorschrijven met een voorwaarde: de redenering van ambitie naar systemen, de waarde voor drie groepen, de tegenvraag van een leverancier en de uitdaging voor OKx](img/visueel/aanleiding.svg)

De afspraak die daarbij hoort draagt een voorwaarde, en levert waarde voor de student, de instelling en de leverancier tegelijk. Voluit staat die redenering in [de aanleiding](context.md#aanleiding).

OKx legt gestandaardiseerde koppelingen vast voor de onderwijslogistiek, zodat een student binnen en later buiten de eigen instelling onderwijs kan kiezen en volgen terwijl de administratie meebeweegt. Het project valt onder de transformatiehub Wendbaar georganiseerd onderwijs van Npuls, in samenwerking met Digitale sectorvoorzieningen.

De kaderstelling ontstaat in `Npuls-OKx/meta`; `Npuls-OKx/Public` draagt de releaseartefacten. Bestaat een document in beide, dan geldt voor een uitspraak naar buiten de versie in Public.

Kern: de [managementsamenvatting](context.md#managementsamenvatting), 5 minuten.

### Verdieping: het projectplan

[Projectplan OKx](projectdocumentatie/projectplan-okx.md)

| | |
|---|---|
| Beantwoordt | Wie de opdrachtgever is, hoe het project bestuurd wordt, welke risico's zijn benoemd en welke alternatieven zijn afgewogen |
| Overslaan | Het conceptcommunicatieplan, tenzij je over de uitdracht gaat |
| Status | Bevroren bron, versie 2.1 van 19 november 2024, bijgewerkt 4 juni 2025. De secties 2 tot en met 8 zijn nog niet overgenomen; de inzet van mensen en middelen blijft eruit |
| Omvang | 909 woorden, 8 minuten |

### Verdieping: het contextdocument

[OKx in context](context.md)

| | |
|---|---|
| Beantwoordt | Wat de opdracht is, welke resultaten die draagt, met welke initiatieven OKx raakvlakken heeft, wie wat beslist, en welke uitdagingen eronder liggen |
| Overslaan | Niets bij eerste lezing; wie haast heeft leest de managementsamenvatting |
| Status | Concept. Samengesteld uit het projectplan en de platen van het programma. Elke sectie draagt haar herkomst, zodat een uitspraak uit het plan te onderscheiden is van een afleiding |
| Omvang | 1388 woorden, 12 minuten |

## Deel 2, historisch overzicht

**Hoe is het zo gelopen?**

### Verdieping: het historisch overzicht

[Detaillering van de OKx-tijdlijn](historie.md)

| | |
|---|---|
| Beantwoordt | Welke keerpunten het project doorliep sinds november 2024, en waarom de vorm van de oplevering nog beweegt |
| Overslaan | De bronnen achter elk keerpunt; die zijn er voor wie wil doorklikken |
| Status | Concept. De periode voor maart 2026 steunt op het projectplan en het geheugen van het team |
| Omvang | Een pagina met veertien keerpunten, 10 minuten |

## Deel 3, scope

**Waar acteert OKx, en waar houdt het op?**

OKE begon op de examenketen. OKx acteert op de processen daaromheen.

![Hoofdprocesmodel MORA, met de processen van OKx in goud en die van OKE in groen](img/mora-hoofdprocesmodel-okx-en-oke-20261027.webp)

*Hoofdprocesmodel [MORA](https://mora.mbodigitaal.nl/index.php/Hoofdpagina). Goud omlijnd: de processen waarop OKx acteert. Groen omlijnd: waar OKE begon.*

De integratie van die ketens over de studentreizen heen heet in het kaderscenario de **instellingsreis**. Dat is waar de koppelingen van OKx ontstaan.

De grens die daarbij hoort:

| Onderdeel | Hoort bij |
|---|---|
| De applicatie | De leverancier |
| Les en didactiek | De instelling, vastgelegd in de specificatie |
| De landelijke voorzieningen | Hun eigen pijler |

Welke leerroutes eerst aan bod komen, staat in de [basisuitgangspunten](context.md#basisuitgangspunten): prioriteit bij 1, 2, 3, 4 en 7. De [negen leerroutes van Npuls](../architecture/docs/specificatie/leerroute-uitwerking/img/README.md) staan als tekening bij elkaar, met per route de keten van persona, uitwerking, scenario's en modeldoorloop.

### Verdieping: het kaderscenario

[`leerroute-1-regulier.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), vier secties: de opening tot en met de leeswijzer, *De procesbeleving achter 'regulier' onderwijs van een Instelling*, *Betrokken informatie bij proces*, *Procesfasen, interacties op de plaat en informatie*, en *Componenten en hun doel*.

| | |
|---|---|
| Beantwoordt | Wat er in de keten gebeurt, welke informatie waar ontstaat, en welke componenten welke rol dragen |
| Overslaan | De studentreis, de keuzedelen in detail, de gegevensoverzichten, de anti-patronen, en het informatiemodel dat in deel 4 uitgebreider terugkomt |
| Status | Concept. Kaderstellend voor de reguliere leerroute; de andere leerroutes volgen als verschil daarop. [meta PR 144](https://github.com/Npuls-OKx/meta/pull/144) herstructureert de uitwerking |
| Omvang | 6030 van 15679 woorden, 50 minuten. Voluit ruim twee uur |

## Deel 4, deliverables

**Wat komt eruit, en hoe ontstaat dat?**

![Hoe ziet onze specificatie eruit: wat er in concept ligt tegenover wat open staat](img/visueel/specificatie-hoofdvraag.svg)

OKx levert een set specificaties van de koppelingen tussen de componenten in de onderwijsketen. Die set dient als functioneel ontwerp voor een implementatie, bij voorkeur als [OEAPI-profiel](https://oeapi.eu/v6.0/#/technical/consumers-and-profiles/profiling-guidelines). Valt een eis buiten de profielvorm, dan komt een andere generieke standaard in beeld. Het uitgangspunt is OEAPI tenzij.

![De route van userstories naar de koppelvlakspecificatie](img/route-naar-eindproduct-20261027.png)

Die route volgt de [AMIGO-aanpak](https://www.edustandaard.nl/amigo/aanpak/) van Edustandaard:

| AMIGO-stap | In de route naar het eindproduct |
|---|---|
| Scenario-analyse | Userstories, op de leerroute en het kaderscenario |
| Gegevensanalyse | Bouwblokken, begrippen en het informatiemodel |
| Interactieanalyse | Informatiestromen tussen applicatiecomponenten |
| Technologiekeuze | OEAPI tenzij; de keuze ligt bij OKx, in afstemming met de sector via de kerngroep techniek en de adviesgroep |
| Berichtspecificatie | Datamodelschema's, payloads en berichtstromen |
| Interfacespecificatie | Endpoints, operaties, antwoorden en voorbeelden |
| Afsprakenset | De koppelvlakspecificatie als geheel, met authenticatie en het inrichten van toegang erbij |

Drie lagen dragen de uitwerking. Een **informatiestroom** is de beweging van gegevens tussen twee componenten. Een **koppeling** is de gestandaardiseerde realisatie daarvan. Een **koppelvlak** is de verzameling koppelingen van precies een component.

Elke specificatie begint bij een wens in de student- en instellingsreis en sluit de cirkel bij de drie resultaten.

```mermaid
flowchart LR
  V["Student- en<br/>instellingsvraag"] --> L["Leerroute"]
  L --> A["Architectuur:<br/>proces, informatiemodel, SOLL ecosysteem"]
  A --> K["Koppelvlakspecificatie<br/>functioneel ontwerp van koppelingen"]
  K --> P["Technische specificatie van<br/>OKx-profiel<br/>binnen OEAPI"]
  P --> IM["Implementatie<br/>bij de instelling,<br/>met adoptie ondersteuning door OKx"]
  IM --> D["De drie resultaten"]
  D -.->|"volgende wens"| V
```

### Productopdeling

De opdeling van de volledige set staat als concept in [#396](https://github.com/Npuls-OKx/meta/issues/396), met de instellingsspecificatie als nieuw product tussen de leerroutes en de koppelvlakspecificatie.

```mermaid
flowchart TB
  V["Student- en instellingsvraag"] --> K
  subgraph K["1. Kaderstelling, per leerroute"]
    direction TB
    BV["Businesswaarde"] --> LR["Leerroute"]
    LR --> OI["Organisatie-inrichting"]
    LR --> BE["Beleid"]
    LR --> PM["SOLL procesmodel"]
    LR --> IM["SOLL informatiemodel"]
    AL["SOLL applicatielandschap<br/>hoofdplaat informatiestromen"] --> IM
  end
  K --> G["OKx: governance orgaan,<br/>projectleiding, adviesgroep"]
  G --> S
  subgraph S["2. Interactieketenspecificatie, per leerroute"]
    direction TB
    KS["Ketensequentie"] --> IS
    subgraph IS["Interactiespecificaties"]
      direction LR
      D1["Interactiediensten en<br/>koppelvlakdiensten"]
      D2["Operaties en methodes"]
      D3["Datamodel"]
      D4["Endpoints"]
      D5["Interactiesequentiediagram"]
    end
    IS --- PR["Provisioning"]
    IS --- AU["Authenticatie"]
    IS --- CT["Conformiteitstoets"]
  end
  S --> P
  subgraph P["3. OKx OEAPI-profiel"]
    direction TB
    GW["Governance orgaan,<br/>werkwijze, issue raising"]
    BP["Profiel en consumers bouwen:<br/>OAS, OEAPI-consumer, besluiten"]
  end
  P --> A
  subgraph A["4. Adoptie via BOPSI, per leerroute"]
    direction LR
    A1["Beleid"]
    A2["Organisatie"]
    A3["Proces"]
    A4["Systeem"]
    A5["Informatie"]
    A6["Techniek"]
    A7["Architectuur"]
    A8["Projecttemplate"]
  end
  A --> E(["Geimplementeerde koppelingen<br/>en koppelingketens"])
```

Per laag een dragende partij:

| Laag | Draagt het | Toetst het |
|---|---|---|
| Kaderstelling | Het programma met de instelling, vanuit de instellingsreis van vandaag | Adviesgroep |
| Interactieketenspecificatie | De solution architecten van OKx | Kerngroep techniek |
| OEAPI-profiel en consumers | OKx met de leveranciers | Kerngroep techniek en de werkgroep van de standaard |
| Adoptie | BOPSI, met de instelling | Governance orgaan |

### Status van de route

De opdeling hierboven is een concept, en de route eromheen wordt aangescherpt. Wat er ligt, wat nu bepaald wordt en waar het naartoe gaat staat in [de status van het werk](context.md#status-van-het-werk). De laag die het langst openstaat is die van de instelling: wat een instelling doet, in welke volgorde, en welke informatie daarbij beweegt. Zolang dat beeld ontbreekt laat de set koppelingen zich niet afbakenen, en laat de vorm waarin zij uitkomt zich niet kiezen. Het vastzetten van de specificatie- en releasestructuur staat daarom stil tot dat beeld er is ([#424](https://github.com/Npuls-OKx/meta/issues/424)).

Het werk loopt nu via de reis van een instelling, per leerroute, in drie lagen.

| Laag | Wat het vastlegt | Voor leerroute 1 |
|---|---|---|
| Persona | De lerende, en wat zijn situatie van de instelling vraagt | [`persona_jochem.md`](../architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| Leerroutedocument | Wat de instelling doet per fase, met de componenten en objecttypen die daarbij oplichten | [kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md) |
| OKx modeldoorloop | Per doorloopstap welke objecten ontstaan, veranderen en stromen, met de bron erbij | [`modeldoorloop-leerroute-1-jochem.md`](../architecture/model/informatiemodel/modeldoorloop-leerroute-1-jochem.md) |

Leerroute 1 draagt die drie lagen. Leerroute 2 en 3 staan in de milestone [Instellingsreizen per leerroute](https://github.com/Npuls-OKx/meta/milestone/24). De maat: een instelling herkent zich voor ongeveer tachtig procent in zo'n beschrijving, en de rest is lokale variant die als variant wordt vastgelegd.

Daarnaast loopt een tweede lijn: de capabilities van de voorziening, oftewel wat een functiegebied moet kunnen, los van het product waarin dat landt. De informatiemodel-voorbeelden verbinden die twee lijnen, want daar staat per stap welke objecten bewegen. Het onderzoek naar die verhouding staat in [#422](https://github.com/Npuls-OKx/meta/issues/422).

### Verdieping: het informatiemodel

[`informatiemodel.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/informatiemodel.md) met [`begrippen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/begrippen.md) als naslag

| | |
|---|---|
| Beantwoordt | Welke objecttypen de keten kent, hoe die samenhangen, en welke begrippenfamilies haar indelen |
| Overslaan | De ontwerpkeuzes met de status voorstel |
| Status | Voorstel, gepubliceerd op `dev` in Public met de modelronde van oktober erin ([Public PR 131](https://github.com/Npuls-OKx/Public/pull/131)). Lopend: [meta PR 391](https://github.com/Npuls-OKx/meta/pull/391) raakt het kwalificatiekader, [410](https://github.com/Npuls-OKx/meta/pull/410) de resultaatkant |
| Omvang | 2741 woorden, 23 minuten |

### Verdieping: de hoofdplaat informatiestromen

De hoogste versiemap onder [`architecture/model/informatiestromen hoofdplaat OKx/`](../architecture/model/)

| | |
|---|---|
| Beantwoordt | Welke stromen tussen welke componenten lopen, en welke nog een beschrijving vragen |
| Overslaan | De eerdere versiemappen, die de historie dragen |
| Status | Concept. Elke stroom is een kandidaat voor een koppelingspecificatie. [meta PR 412](https://github.com/Npuls-OKx/meta/pull/412) en [Public PR 133](https://github.com/Npuls-OKx/Public/pull/133) werken de plaat bij |
| Omvang | Een plaat met leeswijzer, 10 minuten |

Het ArchiMate-model achter de plaat opent in Archi; de platen in dit deel dragen de inhoud.

### Verdieping: de koppelvlakspecificatie

[`Koppelvlakspecificaties/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md) met [`uitgangspunten.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md)

| | |
|---|---|
| Beantwoordt | Wat een afgeronde beschrijving bevat, en hoe koppeling en koppelvlak zich verhouden |
| Overslaan | De uitgangspunten buiten de eigen vraag; de README wijst de leesvolgorde |
| Status | Gereleased als 0.0.1 in augustus 2026, zonder review en uit gebruik; concept voor de herziening naar interactieketens: [meta PR 373](https://github.com/Npuls-OKx/meta/pull/373) onderwijsaanbod en [387](https://github.com/Npuls-OKx/meta/pull/387) student-instroom, zie de interactieketens hieronder. [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt een laag applicatiediensten tussen component en endpoint |
| Omvang | 1998 woorden, 17 minuten |

Wie verder wil, opent een applicatiecomponent met zijn interactiepatroon en een datamodelschema.

### Verdieping: de interactieketens

[meta PR 373](https://github.com/Npuls-OKx/meta/pull/373) onderwijsaanbod, [387](https://github.com/Npuls-OKx/meta/pull/387) student-instroom, [364](https://github.com/Npuls-OKx/meta/pull/364) keuzedelen, [377](https://github.com/Npuls-OKx/meta/pull/377) OpenAPI per component

| | |
|---|---|
| Beantwoordt | Hoe een keten loopt van de waarde voor student en instelling tot een machineleesbaar contract |
| Overslaan | De stroomdocumenten en de OpenAPI-documenten; lees per pull request de review-instructie en de eerste plaat |
| Status | Voorstel, nog op een branch. Dit is de herziening van de koppelvlakspecificaties: de keten begint bij de waarde en trekt die door naar de koppelingen. [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt de dienstlaag eronder. De twee vormen komen nog samen |
| Omvang | 1975 woorden voor de keten onderwijsaanbod, 17 minuten |

![Van beeld naar bericht: dezelfde stap als interactie, voorbeeldbericht en endpoint](img/van-beeld-naar-bericht-20261027.png)

*Wat een specificatie uiteindelijk oplevert: de interactie, het bericht en het endpoint. Het bericht ligt vast, de techniek is een keuze.*

## Deel 5, architectuurbesluiten

**Waarop steunen die keuzes?**

![De architectuurbesluiten die de rest van het werk dragen](img/visueel/besluiten.svg)

| Vraag | Besluit | Laag |
|---|---|---|
| Waar ligt de grens | [0008](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md) eerst intra-instelling, federatie gefaseerd | kern |
| Wat is het ordenend principe | [0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md) de leeruitkomst als verbindende sleutel | kern |
| Hoe verhoudt OKx zich tot de sectorarchitectuur | [0019](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0019-conceptuele-gelaagdheid-kwalificatie-specificatie-aanbod-rosa-koi.md) gelaagdheid en [0022](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) resultaatbegrippen | verdieping |
| Welke verdieping vraagt OKx in MORA | [0005](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) het studentkeuzesysteem als zelfstandige referentiecomponent | verdieping |
| Welke taal dragen de producten | [0021](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0021-koppeling-versus-koppelvlak-terminologie.md) koppeling tegenover koppelvlak | verdieping |

### Verdieping: de overige besluiten

[`adr/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/README.md) met 0019, 0022, 0005 en 0021

| | |
|---|---|
| Beantwoordt | Hoe OKx zich tot ROSA en het Kernmodel Onderwijsinformatie verhoudt, welke verdieping het in MORA vraagt, en welke taal de producten dragen |
| Overslaan | De overige besluiten, tot er een op een eigen vraag drukt |
| Status | Voorstel. Alle 26 besluiten staan op `Voorstel` en leggen herleidbaar vast wat het team koos; de `Status`-regel in elk besluit is leidend, en een besluit kan vervangen zijn. Het onderscheid uit 0021 is in beweging: het kan opgaan in de interactieketen en de interactiespecificatie |
| Omvang | 2731 woorden, 23 minuten |

Verder lezen: 0003 en 0004 onder de leeruitkomst, 0009 en 0014 voor de rolverdeling tussen studentkeuzesysteem en studentvolgsysteem, en 0018 voor de messaging-patronen.

## Deel 6, release en beheer

**Hoe blijft dit in leven?**

![De fasen van OKx: specificatie, bouw, implementatie en adoptie, borging, met 2032 als eindpunt](img/visueel/fasen.svg)

Elk pakket in Public draagt een eigen versielijn met een manifest. Tot een pakket zijn eerste stabiele versie bereikt, kan elk onderdeel eraan wijzigen.

Wie iets wil toevoegen of corrigeren, opent een issue of een pull request; de werkwijze staat in [`CONTRIBUTING.md`](../CONTRIBUTING.md).

### Verdieping: release-management

[`Release-management-algemeen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Algemeen/release-management/Release-management-algemeen.md), met de milestones van [meta](https://github.com/Npuls-OKx/meta/milestones) en [Public](https://github.com/Npuls-OKx/Public/milestones) en het [wijzigingenoverzicht](../CHANGELOG.md)

| | |
|---|---|
| Beantwoordt | Wie het resultaat draagt, hoe een versie tot stand komt, en wat vandaag openstaat |
| Overslaan | Niets |
| Status | Concept, gepubliceerd op `dev` in Public en in gebruik door het team: elk pakket draagt een eigen versielijn met een manifest. De vorm van een uitgave ligt zelf nog open, en dat is waarom er sinds augustus 2026 geen nieuwe is. [Public PR 82](https://github.com/Npuls-OKx/Public/pull/82) brengt de volgende momentopname |
| Omvang | 1109 woorden en twee milestonelijsten, 9 minuten |

## Deel 7, wat nu

Drie uur lezen levert weinig op als er daarna niets te doen valt. Dit is wat er openstaat en waar een lezer binnenkomt.

| Wat | Waar |
|---|---|
| Een vraag stellen of meedenken | [Discussions](https://github.com/Npuls-OKx/meta/discussions), of een issue met het label `question` |
| Een fout melden in wat hier staat | Een issue via de sjabloon correctie-documentatie |
| Meelezen op wat nu loopt | De open pull requests, elk met een review-instructie bovenaan |
| Zien waar het werk aan toe is | De [milestones](https://github.com/Npuls-OKx/meta/milestones), elk met de vraag die zij beantwoordt |
| Bijdragen | [`CONTRIBUTING.md`](../CONTRIBUTING.md) voor de werkwijze, [Bijdragen voor beginners](bijdragen-voor-beginners.md) voor de eerste stappen |

De vragen waar OKx zelf het meeste aan heeft staan in de platen hierboven met een vraagteken erbij. Wie daar een antwoord op heeft, of een reden waarom de vraag verkeerd staat, is precies wie we zoeken.
