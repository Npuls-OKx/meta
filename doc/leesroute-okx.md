# Leesroute OKx

Tien stappen door de twee OKx-repositories, samen ongeveer twee uur. De route is bedoeld voor een architect die OKx nog niet kent en wel in architectuurtaal leest: de lezer in [`domeinarchitect-npuls.md`](../.agents/personas/domeinarchitect-npuls.md). Wie wil bouwen tegen een koppelvlak begint aan de andere kant, bij de koppelvlakspecificaties in Public.

De leestijd is de woordtelling gedeeld door honderdtachtig woorden per minuut, afgerond op hele minuten. Zo is zij navolgbaar en niet geschat.

Per stap staat de **stand**: hoe hard het materiaal is, en welke wijziging erop in behandeling is, met de pull request erbij. De route noemt zelf geen statuslabel en geen versienummer; een overzicht dat die overschrijft veroudert sneller dan de bron.

## Vier vragen die de route beantwoordt

1. **Wat wil OKx bereiken**, en welk probleem lost dat op.
2. **Waar gaat het wel en niet over**, en welke keuzes liggen daarover vast.
3. **Wat levert OKx op**, in welke vorm, en hoe hard is dat vandaag.
4. **Hoe komt een afspraak tot stand**, en wie draagt hem daarna.

Wie deze vier na de route kan beantwoorden, kan over de inhoud meespreken. Lukt een van de vier niet, dan is dat een tekortkoming van de route; die hoort als issue in deze repository, niet als vraag aan een collega.

| Vraag | Stappen | Minuten |
|---|---|---|
| 1. Wat wil OKx bereiken | 1 en 2 | 14 |
| 2. Waar gaat het wel en niet over | 3 en 4 | 50 |
| 3. Wat levert OKx op | 5 tot 8 | 42 |
| 4. Hoe komt een afspraak tot stand | 9 en 10 | 14 |

## Vraag 1: wat wil OKx bereiken

### 1. De twee repositories

[`README.md` in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/README.md)

- **Beantwoordt** Welke repository draagt wat, en welke kopie van een document is leidend wanneer er twee zijn.
- **Overslaan** Niets; het document is kort.
- **Stand** De indeling staat in dit document beschreven en beweegt niet.
- **Omvang** 343 woorden, 2 minuten.

De kaderstelling ontstaat in `Npuls-OKx/meta`; `Npuls-OKx/Public` draagt de releaseartefacten waarmee een instelling of leverancier bouwt. Bestaat een document in beide, dan geldt voor een uitspraak naar buiten de versie in Public.

### 2. De principes en de uitgangspunten

[`Referentiemateriaal/principes/principes.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md), met de [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/uitgangspunten.md) ernaast

- **Beantwoordt** Welke richting ligt onder alle uitwerkingen, en welke standaardiseringsroute volgt het project.
- **Overslaan** De toelichting per principe bij eerste lezing; de titels dragen de lijn.
- **Stand** Vastgelegd in Public. De besluiten die de principes aanhalen dragen de status voorstel. In behandeling: [Public PR 71](https://github.com/Npuls-OKx/Public/pull/71), dat een principe toevoegt waarmee een eis vóór de techniekkeuze komt; de review-instructie staat in die pull request.
- **Omvang** 2112 woorden, 12 minuten.

De principes zijn abstract en stabiel en beschrijven het waarom; de uitgangspunten ernaast zijn concreter en bewegen mee.

## Vraag 2: waar gaat het wel en niet over

### 3. De architectuurbesluiten

[`Referentiemateriaal/adr/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/README.md), met deze vier besluiten voluit:

| Besluit | Waarom dit besluit |
|---|---|
| [Afbakening: planning eerst, intra-instelling](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md) | Bepaalt wat binnen en buiten bereik valt, en waarom federatie later komt |
| [Conceptuele gelaagdheid tegenover ROSA en het Kernmodel Onderwijsinformatie](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0019-conceptuele-gelaagdheid-kwalificatie-specificatie-aanbod-rosa-koi.md) | Legt de verhouding met de bestaande referentiekaders vast |
| [Resultaatbegrippen conform ROSA en het Kernmodel Onderwijsinformatie](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) | Hetzelfde, voor de resultaatkant van de keten |
| [De leeruitkomst als verbindende sleutel](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md) | Het scharnier van het hele informatiemodel |

- **Beantwoordt** Welke keuzes liggen vast, met welke onderbouwing, en hoe verhoudt OKx zich tot de bestaande referentiekaders.
- **Overslaan** De overige besluiten, tot er een op een eigen vraag drukt. De index noemt ze alle met hun onderwerp.
- **Stand** Alle besluiten dragen de status voorstel; de `Status`-regel in het besluit zelf is leidend, en kan ook zeggen dat een besluit is vervangen. In behandeling: [Public PR 71](https://github.com/Npuls-OKx/Public/pull/71) en [72](https://github.com/Npuls-OKx/Public/pull/72).
- **Omvang** 2920 woorden, 16 minuten.

Deze stap staat met opzet vooraan in vraag 2. Zonder te weten welke keuzes vastliggen, leest de rest van de route als een reeks feiten terwijl een deel voorstel is.

### 4. Het kaderscenario van de reguliere leerroute

[`Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md)

Van dit document vier secties, in deze volgorde: de opening tot en met de leeswijzer, *De procesbeleving achter 'regulier' onderwijs van een Instelling*, *Betrokken informatie bij proces*, *Procesfasen, interacties op de plaat en informatie*, en *Componenten en hun doel, wat hoort hier wel en niet thuis*.

- **Beantwoordt** Wat gebeurt er in de keten, welke informatie ontstaat waar, en welke componenten dragen welke rol.
- **Overslaan** De studentreis en de keuzedelen in detail, de gegevensoverzichten, de anti-patronen en het concept-informatiemodel. Dat laatste komt in stap 5 in zijn vastgelegde vorm terug.
- **Stand** Kaderstellend voor de reguliere leerroute; de andere leerroutes worden als verschil daarop beschreven en volgen nog. In behandeling: [meta PR 144](https://github.com/Npuls-OKx/meta/pull/144), dat de leerroute-uitwerking herstructureert en aan de requirementsboom verbindt.
- **Omvang** 6030 van 15679 woorden, 34 minuten. Voluit is het document 87 minuten.

Dit is de enige plek waar de keten als geheel staat, met een student als rode draad.

## Vraag 3: wat levert OKx op

### 5. Het informatiemodel

[`Informatie-en-gegevensmodellen/informatiemodel.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/informatiemodel.md), met [`begrippen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/begrippen.md) als naslag

- **Beantwoordt** Welke objecttypen kent de keten, hoe hangen zij samen, en welke begrippenfamilies delen haar in.
- **Overslaan** De ontwerpkeuzes die nog voorstel zijn, bij eerste lezing. De plaat en de begrippenfamilies dragen het beeld.
- **Stand** Laag 1 en 2 zijn vastgelegd in Public, met per ontwerpkeuze de aanduiding erbij. In behandeling: [Public PR 131](https://github.com/Npuls-OKx/Public/pull/131) brengt de modelronde van oktober naar het pakket, met de review-instructie in die pull request; [meta PR 391](https://github.com/Npuls-OKx/meta/pull/391) raakt het kwalificatiekader en [meta PR 410](https://github.com/Npuls-OKx/meta/pull/410) de resultaatkant. Zolang PR 131 openstaat loopt de werkversie in meta voor op de vastgelegde kopie.
- **Omvang** 2741 woorden, 15 minuten.

### 6. De hoofdplaat informatiestromen

De hoogste versiemap onder [`architecture/model/informatiestromen hoofdplaat OKx/`](../architecture/model/)

- **Beantwoordt** Welke informatiestromen lopen tussen welke componenten, en welke daarvan zijn nog niet beschreven.
- **Overslaan** De eerdere versiemappen; die staan er voor de historie.
- **Stand** Werkbeeld van het project: elke stroom erop is een kandidaat voor een koppelingspecificatie. In behandeling: [meta PR 412](https://github.com/Npuls-OKx/meta/pull/412) en [Public PR 133](https://github.com/Npuls-OKx/Public/pull/133), die de plaat bijwerken en een ontbrekende stroom herstellen.
- **Omvang** Een plaat met haar leeswijzer, 5 minuten.

Het ArchiMate-model waaruit de plaat komt blijft hier buiten beeld: dat opent alleen in Archi, en de platen dragen de inhoud.

### 7. De koppelvlakspecificatie

[`Koppelvlakspecificaties/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md) met [`uitgangspunten.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md)

- **Beantwoordt** Wat bevat een afgeronde beschrijving, en wat is het verschil tussen een koppeling en een koppelvlak.
- **Overslaan** De uitgangspunten die niet op een eigen vraag drukken; de README wijst de leesvolgorde.
- **Stand** Het eerste pakket is uitgebracht en wordt nu herzien, zie stap 8. In behandeling: [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt een laag applicatiediensten tussen component en endpoint, met de review-instructie in die pull request.
- **Omvang** 1998 woorden, 11 minuten.

Een koppeling is de informatiestroom tussen twee componenten; een koppelvlak is de verzameling koppelingen van precies een component. Dat onderscheid draagt de hele indeling van het pakket. Wie wil zien hoe ver een uitwerking gaat, opent daarna een applicatiecomponent met zijn interactiepatroon en een datamodelschema.

### 8. De herziening naar interactieketens

De interactieketens in behandeling: [meta PR 373](https://github.com/Npuls-OKx/meta/pull/373) onderwijsaanbod, [387](https://github.com/Npuls-OKx/meta/pull/387) student-instroom, [364](https://github.com/Npuls-OKx/meta/pull/364) keuzedelen, en [377](https://github.com/Npuls-OKx/meta/pull/377) voor de OpenAPI per component

- **Beantwoordt** Waar werkt het project nu aan, en hoe ziet een keten eruit die van de waarde voor student en instelling tot een machineleesbaar contract is doorgetrokken.
- **Overslaan** De onderliggende stroomdocumenten en de OpenAPI-documenten, tenzij een vraag daarop uitkomt. Lees van elke pull request de review-instructie en de eerste plaat.
- **Stand** Nog niet op de ontwikkellijn. Dit is de herziening van de koppelvlakspecificaties: waar het eerste pakket per component begon, beginnen de interactieketens bij de waarde voor student en instelling en trekken die door naar de koppelingen eronder. [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt daar de dienstlaag onder. De vormen moeten nog samenkomen.
- **Omvang** 1975 woorden voor de ketenbeschrijving van het onderwijsaanbod, 11 minuten.

Dit is de voorhoede van het werk en daarmee de beste plek om te zien waar OKx naartoe beweegt.

## Vraag 4: hoe komt een afspraak tot stand

### 9. De requirementsboom

[`Referentiemateriaal/requirementsboom/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md), met [`opdracht.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/opdracht.md) en [`epics.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/epics.md)

- **Beantwoordt** Hoe hangt een stuk werk aan de opdracht: van opdracht naar epic, feature en story.
- **Overslaan** `features.md` en `stories.md`; de vorm blijkt al uit de bovenste lagen.
- **Stand** Vroeg concept. De huidige boom demonstreert de vorm van een uiteindelijke uitwerking van de verzamelde requirements-analyse en is in geen enkele vorm een weergave van de werkelijke breakdown. Die breakdown ontstaat in de proefopstellingen die Niels van Duin uitvoert, en loopt voorlopig buiten de boom om.
- **Omvang** 1440 woorden, 8 minuten.

Lees de boom dus om de bedoelde vorm te zien, en niet om te weten wat er gebouwd wordt. Dat laatste staat in de milestones en de pull requests.

### 10. Release en beheer

[`Algemeen/release-management/Release-management-algemeen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Algemeen/release-management/Release-management-algemeen.md), met de milestones van [meta](https://github.com/Npuls-OKx/meta/milestones) en [Public](https://github.com/Npuls-OKx/Public/milestones) en het [wijzigingenoverzicht van meta](../CHANGELOG.md)

- **Beantwoordt** Wie draagt het resultaat, hoe komt een versie tot stand, en wat staat er vandaag open.
- **Overslaan** Niets; dit is de kortste stap met het grootste bereik.
- **Stand** Elk pakket in Public draagt een eigen versielijn met een manifest. In behandeling: [Public PR 82](https://github.com/Npuls-OKx/Public/pull/82) voor de volgende momentopname.
- **Omvang** 1109 woorden en twee milestonelijsten, 6 minuten.

Een versielabel zegt wat vastligt en wat nog beweegt. Zolang een pakket zijn eerste stabiele versie niet heeft bereikt, kan elk onderdeel eraan wijzigen, ook wanneer het document zelf afgerond leest.
