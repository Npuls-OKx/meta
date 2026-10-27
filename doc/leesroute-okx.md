# Leesroute OKx

## 1. Inleiding

### 1.1 Context

Het werk van OKx staat verdeeld over twee repositories en ruim tweehonderd documenten. Deze route wijst een leesvolgorde aan: tien stappen, samen ongeveer twee uur, voor wie architectuur leest en OKx nog niet kent.

### 1.2 Doel

Na de route zijn vier vragen te beantwoorden.

```mermaid
flowchart LR
  V1["1. Doel<br/>welk probleem OKx oplost<br/>stap 1 en 2, 14 min"] --> V2["2. Scope<br/>waarover OKx afspraken maakt<br/>stap 3 en 4, 50 min"]
  V2 --> V3["3. Deliverables<br/>wat OKx oplevert<br/>stap 5 tot 8, 42 min"]
  V3 --> V4["4. Totstandkoming<br/>hoe een afspraak ontstaat<br/>stap 9 en 10, 14 min"]
```

Blijft een van de vier onbeantwoord, dan hoort dat als issue in deze repository.

### 1.3 Scope

In scope: de kaderstelling, de scope van OKx, de deliverables en de werkwijze waarmee die tot stand komen.

Het bouwen tegen een koppelvlak begint bij de [koppelvlakspecificaties in Public](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md), die daar hun eigen leesvolgorde dragen. De werkwijze voor een bijdrage staat in [`CONTRIBUTING.md`](../CONTRIBUTING.md), de werkwijze voor agents in [`AGENTS.md`](../AGENTS.md). Al het overige valt buiten deze route.

### 1.4 Leeswijzer

| Veld per stap | Betekenis |
|---|---|
| Beantwoordt | De vraag die het document oplost |
| Overslaan | Wat bij eerste lezing buiten de route blijft |
| Stand | Hoe hard het materiaal is, met de pull request die eraan werkt |
| Omvang | Woordtelling en leestijd bij honderdtachtig woorden per minuut |

Statuslabels en versienummers staan in de bron, niet in deze route.

## 2. Doel: welk probleem OKx oplost

### Stap 1. De twee repositories

[`README.md` in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/README.md)

| | |
|---|---|
| Beantwoordt | Welke repository draagt wat, en welke kopie van een document is leidend |
| Overslaan | Niets |
| Stand | De indeling staat in het document beschreven |
| Omvang | 343 woorden, 2 minuten |

De kaderstelling ontstaat in `Npuls-OKx/meta`. `Npuls-OKx/Public` draagt de releaseartefacten. Voor een uitspraak naar buiten geldt de versie in Public.

### Stap 2. De principes en de uitgangspunten

[`principes.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md) met de [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/uitgangspunten.md)

| | |
|---|---|
| Beantwoordt | Welke richting onder alle uitwerkingen ligt, en welke standaardiseringsroute het project volgt |
| Overslaan | De toelichting per principe |
| Stand | Vastgelegd in Public. [Public PR 71](https://github.com/Npuls-OKx/Public/pull/71) voegt een principe toe dat eisen voor de techniekkeuze plaatst |
| Omvang | 2112 woorden, 12 minuten |

## 3. Scope: waarover OKx afspraken maakt

### Stap 3. De architectuurbesluiten

[`adr/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/README.md), met vier besluiten voluit:

| Besluit | Draagt |
|---|---|
| [0008 afbakening](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md) | Wat binnen bereik valt, en waarom federatie later komt |
| [0019 gelaagdheid](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0019-conceptuele-gelaagdheid-kwalificatie-specificatie-aanbod-rosa-koi.md) | De verhouding met ROSA en het Kernmodel Onderwijsinformatie |
| [0022 resultaatbegrippen](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) | Hetzelfde, voor de resultaatkant van de keten |
| [0026 leeruitkomst](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md) | Het scharnier van het informatiemodel |

| | |
|---|---|
| Beantwoordt | Welke keuzes vastliggen, met welke onderbouwing |
| Overslaan | De overige besluiten, tot er een op een eigen vraag drukt |
| Stand | Alle besluiten dragen de status voorstel; de `Status`-regel in het besluit is leidend. [Public PR 71](https://github.com/Npuls-OKx/Public/pull/71) en [72](https://github.com/Npuls-OKx/Public/pull/72) voegen besluiten toe |
| Omvang | 2920 woorden, 16 minuten |

### Stap 4. Het kaderscenario van de reguliere leerroute

[`leerroute-1-regulier.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), vier secties: de opening tot en met de leeswijzer, *De procesbeleving achter 'regulier' onderwijs van een Instelling*, *Betrokken informatie bij proces*, *Procesfasen, interacties op de plaat en informatie*, en *Componenten en hun doel*.

| | |
|---|---|
| Beantwoordt | Wat er in de keten gebeurt, welke informatie waar ontstaat, en welke componenten welke rol dragen |
| Overslaan | De studentreis, de keuzedelen in detail, de gegevensoverzichten, de anti-patronen, en het concept-informatiemodel dat in stap 5 vastgelegd terugkomt |
| Stand | Kaderstellend voor de reguliere leerroute; de andere leerroutes volgen als verschil daarop. [meta PR 144](https://github.com/Npuls-OKx/meta/pull/144) herstructureert de leerroute-uitwerking |
| Omvang | 6030 van 15679 woorden, 34 minuten. Voluit 87 minuten |

## 4. Deliverables: wat OKx oplevert

De vier deliverables hangen aan elkaar: het model levert de taal, de plaat de stromen, de specificatie het contract, en de interactieketen verbindt de waarde met dat contract.

```mermaid
flowchart TB
  M["Informatiemodel<br/>de taal van de keten"] --> H["Hoofdplaat<br/>de informatiestromen"]
  H --> K["Koppelvlakspecificatie<br/>koppelingen per component"]
  I["Interactieketen<br/>waarde voor student en instelling"] --> K
  M --> I
```

Drie lagen dragen die samenhang. Een **informatiestroom** is de beweging van gegevens tussen twee componenten. Een **koppeling** is de gestandaardiseerde realisatie daarvan. Een **koppelvlak** is de verzameling koppelingen van precies een component.

### Stap 5. Het informatiemodel

[`informatiemodel.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/informatiemodel.md) met [`begrippen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/begrippen.md) als naslag

| | |
|---|---|
| Beantwoordt | Welke objecttypen de keten kent, hoe die samenhangen, en welke begrippenfamilies haar indelen |
| Overslaan | De ontwerpkeuzes met de status voorstel |
| Stand | Laag 1 en 2 vastgelegd in Public. [Public PR 131](https://github.com/Npuls-OKx/Public/pull/131) brengt de modelronde van oktober, met de review-instructie daarin; [meta PR 391](https://github.com/Npuls-OKx/meta/pull/391) raakt het kwalificatiekader, [410](https://github.com/Npuls-OKx/meta/pull/410) de resultaatkant |
| Omvang | 2741 woorden, 15 minuten |

### Stap 6. De hoofdplaat informatiestromen

De hoogste versiemap onder [`architecture/model/informatiestromen hoofdplaat OKx/`](../architecture/model/)

| | |
|---|---|
| Beantwoordt | Welke stromen tussen welke componenten lopen, en welke nog een beschrijving vragen |
| Overslaan | De eerdere versiemappen, die de historie dragen |
| Stand | Werkbeeld: elke stroom is een kandidaat voor een koppelingspecificatie. [meta PR 412](https://github.com/Npuls-OKx/meta/pull/412) en [Public PR 133](https://github.com/Npuls-OKx/Public/pull/133) werken de plaat bij |
| Omvang | Een plaat met leeswijzer, 5 minuten |

Het ArchiMate-model achter de plaat opent in Archi; de platen in stap 5, 6 en 8 dragen de inhoud.

### Stap 7. De koppelvlakspecificatie

[`Koppelvlakspecificaties/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md) met [`uitgangspunten.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md)

| | |
|---|---|
| Beantwoordt | Wat een afgeronde beschrijving bevat, en hoe koppeling en koppelvlak zich verhouden |
| Overslaan | De uitgangspunten buiten de eigen vraag; de README wijst de leesvolgorde |
| Stand | Het eerste pakket is uitgebracht en wordt herzien, zie stap 8. [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt een laag applicatiediensten tussen component en endpoint |
| Omvang | 1998 woorden, 11 minuten |

Wie verder wil, opent een applicatiecomponent met zijn interactiepatroon en een datamodelschema.

### Stap 8. De interactieketens

[meta PR 373](https://github.com/Npuls-OKx/meta/pull/373) onderwijsaanbod, [387](https://github.com/Npuls-OKx/meta/pull/387) student-instroom, [364](https://github.com/Npuls-OKx/meta/pull/364) keuzedelen, [377](https://github.com/Npuls-OKx/meta/pull/377) OpenAPI per component

| | |
|---|---|
| Beantwoordt | Hoe een keten loopt van de waarde voor student en instelling tot een machineleesbaar contract |
| Overslaan | De stroomdocumenten en de OpenAPI-documenten; lees per pull request de review-instructie en de eerste plaat |
| Stand | Nog op een branch. Dit is de herziening van de koppelvlakspecificaties: de keten begint bij de waarde en trekt die door naar de koppelingen. [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt de dienstlaag eronder. De twee vormen komen nog samen |
| Omvang | 1975 woorden voor de keten onderwijsaanbod, 11 minuten |

## 5. Totstandkoming: hoe een afspraak ontstaat

De route van een vraag naar een vastgelegde afspraak volgt AMIGO, met de product-flow per deliverable eromheen.

```mermaid
flowchart LR
  S["Scenario<br/>analyse"] --> G["Gegevens en<br/>interactie"]
  G --> T["Technologie<br/>keuze"]
  T --> B["Bericht<br/>specificatie"]
  B --> I["Interface<br/>specificatie"]
  I --> A["Afspraken<br/>set"]
```

### Stap 9. De requirementsboom

[`requirementsboom/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md) met [`opdracht.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/opdracht.md) en [`epics.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/epics.md)

| | |
|---|---|
| Beantwoordt | Hoe een stuk werk aan de opdracht hangt: opdracht, epic, feature, story |
| Overslaan | `features.md` en `stories.md`; de bovenste lagen tonen de vorm |
| Stand | Vroeg concept. De boom demonstreert de vorm van een uiteindelijke uitwerking van de verzamelde requirements-analyse. De werkelijke breakdown ontstaat in de proefopstellingen die Niels van Duin uitvoert, en loopt voorlopig buiten de boom om |
| Omvang | 1440 woorden, 8 minuten |

Wat er gebouwd wordt staat in de milestones en de pull requests.

### Stap 10. Release en beheer

[`Release-management-algemeen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Algemeen/release-management/Release-management-algemeen.md), met de milestones van [meta](https://github.com/Npuls-OKx/meta/milestones) en [Public](https://github.com/Npuls-OKx/Public/milestones) en het [wijzigingenoverzicht](../CHANGELOG.md)

| | |
|---|---|
| Beantwoordt | Wie het resultaat draagt, hoe een versie tot stand komt, en wat vandaag openstaat |
| Overslaan | Niets |
| Stand | Elk pakket in Public draagt een eigen versielijn met een manifest. [Public PR 82](https://github.com/Npuls-OKx/Public/pull/82) brengt de volgende momentopname |
| Omvang | 1109 woorden en twee milestonelijsten, 6 minuten |

Zolang een pakket zijn eerste stabiele versie nog bereikt, kan elk onderdeel eraan wijzigen.
