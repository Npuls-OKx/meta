# Leesroute voor een architect die nieuw op OKx is

Tien stappen door de twee OKx-repositories, samen ongeveer twee uur. Na deze route is de keten te overzien, is duidelijk welke keuzes vastliggen en welke nog voorstel zijn, en is te zeggen waar de volgende stap van het project ligt.

De route is geschreven voor de lezer in [`domeinarchitect-npuls.md`](../.agents/personas/domeinarchitect-npuls.md): een architect die architectuurtaal vanzelf leest, de onderwijslogistieke keten nog niet kent, en het beeld dat hij hier opdoet verder draagt naar anderen. Voor een informatiemanager, een leverancier of een nieuw kernteamlid gelden andere documenten, een andere volgorde en een kortere route.

**Deze route draagt zelf geen stand van zaken.** Per stap staat waar de status van het materiaal te lezen is, niet welke status dat vandaag is. Een route die statuslabels overschrijft veroudert sneller dan de documenten waarnaar zij wijst, en een verouderd overzicht is schadelijker dan geen overzicht.

De leestijd is de woordtelling gedeeld door honderdtachtig woorden per minuut, afgerond op hele minuten. Zo is zij navolgbaar en niet geschat.

## De route in een oogopslag

| # | Document | Repo | Min |
|---|---|---|---|
| 1 | De verhouding tussen de twee repositories | Public | 2 |
| 2 | De architectuurprincipes | Public | 12 |
| 3 | De architectuurbesluiten, met vier aangewezen besluiten | Public | 16 |
| 4 | De requirementsboom | Public | 8 |
| 5 | Het kaderscenario van de reguliere leerroute, in uitsnede | Public | 34 |
| 6 | Het informatiemodel | Public | 15 |
| 7 | De hoofdplaat informatiestromen | meta | 5 |
| 8 | De koppelvlakspecificatie en haar uitgangspunten | Public | 11 |
| 9 | De interactieketenspecificatie onderwijsaanbod | meta | 11 |
| 10 | Release en beheer, met de stand van het werk | beide | 6 |

Samen honderdtwintig minuten. Stap 1 tot 4 leggen het kader, stap 5 tot 7 de keten en de taal, stap 8 tot 10 het eindproduct en wie het draagt.

## 1. De verhouding tussen de twee repositories

[`README.md` in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/README.md)

- **Vraag** Welke repository draagt wat, en welke kopie van een document is leidend wanneer er twee zijn.
- **Overslaan** Niets; het document is kort.
- **Status** De repository-indeling staat in dit document zelf beschreven.
- **Omvang** 343 woorden, 2 minuten.

Het werk van OKx staat in twee repositories. `Npuls-OKx/meta` is de kennisbank waar de kaderstelling ontstaat; `Npuls-OKx/Public` draagt de releaseartefacten waarmee een instelling of leverancier bouwt. Rijpt iets in meta tot een releasebaar artefact, dan verhuist het naar Public. Daardoor bestaat een document soms in twee versies: de werkversie in meta en de vastgelegde versie in Public. Voor een uitspraak naar buiten geldt de versie in Public.

## 2. De architectuurprincipes

[`Referentiemateriaal/principes/principes.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md), met de [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/uitgangspunten.md) ernaast

- **Vraag** Welke richting ligt onder alle uitwerkingen, en welke standaardiseringsroute volgt het project.
- **Overslaan** De toelichting per principe bij eerste lezing; de titels dragen de lijn.
- **Status** De `Status`-regel boven het document.
- **Omvang** 2112 woorden, 12 minuten.

De principes zijn abstract en stabiel en beschrijven het waarom; de uitgangspunten ernaast zijn concreter en bewegen mee. Het principe over de standaardiseringsroute bepaalt hoe een afspraak van een idee naar een vastgelegde standaard loopt, en verklaart de volgorde van het werk in de rest van deze route.

## 3. De architectuurbesluiten

[`Referentiemateriaal/adr/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/README.md), met deze vier besluiten voluit:

| Besluit | Waarom dit besluit |
|---|---|
| [Afbakening: planning eerst, intra-instelling](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md) | Bepaalt wat binnen en buiten bereik valt, en waarom federatie later komt |
| [Conceptuele gelaagdheid tegenover ROSA en het Kernmodel Onderwijsinformatie](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0019-conceptuele-gelaagdheid-kwalificatie-specificatie-aanbod-rosa-koi.md) | Legt de verhouding met de bestaande referentiekaders vast |
| [Resultaatbegrippen conform ROSA en het Kernmodel Onderwijsinformatie](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md) | Hetzelfde, voor de resultaatkant van de keten |
| [De leeruitkomst als verbindende sleutel](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md) | Het scharnier van het hele informatiemodel |

- **Vraag** Welke keuzes liggen vast, met welke onderbouwing, en hoe verhoudt OKx zich tot de bestaande referentiekaders.
- **Overslaan** De overige besluiten, tot er een op een eigen vraag drukt. De index noemt ze alle met hun onderwerp.
- **Status** De `Status`-regel in elk besluit, en de inleiding van de index die over de reeks als geheel spreekt. Een besluit kan ook vervangen zijn; dat staat dan op die regel, met het vervangende besluit erbij.
- **Omvang** 2920 woorden, 16 minuten.

Deze stap staat met opzet vooraan. Zonder te weten welke keuzes vastliggen en met welke status, leest de rest van de route als een reeks feiten terwijl een deel voorstel is.

## 4. De requirementsboom

[`Referentiemateriaal/requirementsboom/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md), met [`opdracht.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/opdracht.md) en [`epics.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/epics.md)

- **Vraag** Waar hangt elk stuk werk aan: van opdracht naar epic, feature en story.
- **Overslaan** `features.md` en `stories.md`; naslag zodra een concrete eis aan de orde is.
- **Status** De inleiding van de README benoemt de laag en de bronplicht per laag.
- **Omvang** 1440 woorden, 8 minuten.

De boom is de verbinding tussen de opdracht en het technische werk. Elk issue in beide repositories hangt via een milestone aan deze boom, dus wie de boom kent kan elk stuk werk plaatsen.

## 5. Het kaderscenario van de reguliere leerroute

[`Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md)

Van dit document vier secties, in deze volgorde:

1. De opening tot en met de leeswijzer.
2. *De procesbeleving achter 'regulier' onderwijs van een Instelling.*
3. *Betrokken informatie bij proces.*
4. *Procesfasen, interacties op de plaat en informatie.*
5. *Componenten en hun doel, wat hoort hier wel en niet thuis.*

- **Vraag** Wat gebeurt er in de keten, welke informatie ontstaat waar, en welke componenten dragen welke rol.
- **Overslaan** De studentreis en de keuzedelen in detail, de gegevensoverzichten, de anti-patronen en het concept-informatiemodel. Het laatste komt in stap 6 in zijn vastgelegde vorm terug.
- **Status** De sectie *Waarvoor dit document dient* zegt wat het document wel en niet vastlegt.
- **Omvang** 6030 van 15679 woorden, 34 minuten. Voluit is het document 87 minuten.

Dit is de enige plek waar de keten als geheel staat, met een student als rode draad. De volledige lezing is de moeite waard zodra een vraag over de keten zelf opkomt.

## 6. Het informatiemodel

[`Informatie-en-gegevensmodellen/informatiemodel.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/informatiemodel.md), met [`begrippen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/begrippen.md) als naslag

- **Vraag** Welke objecttypen kent de keten, hoe hangen zij samen, en welke begrippenfamilies delen haar in.
- **Overslaan** De ontwerpkeuzes die nog voorstel zijn, bij eerste lezing. De plaat en de begrippenfamilies dragen het beeld.
- **Status** De kop van het document voor het model als geheel, de `versie` in `release.json` van het pakket, en per ontwerpkeuze de aanduiding bij die keuze.
- **Omvang** 2741 woorden, 15 minuten.

Dit is de vastgelegde kopie. In meta leeft onder `architecture/model/informatiemodel/` een werkversie die verder kan zijn; die wordt via een pull request naar Public gebracht. Voor een uitspraak naar buiten geldt de kopie in Public.

## 7. De hoofdplaat informatiestromen

De hoogste versiemap onder [`architecture/model/informatiestromen hoofdplaat OKx/`](../architecture/model/)

- **Vraag** Welke informatiestromen lopen tussen welke componenten, en welke daarvan zijn nog niet beschreven.
- **Overslaan** De eerdere versiemappen; die staan er voor de historie.
- **Status** De legenda op de plaat zelf, en de README in de versiemap.
- **Omvang** Een plaat met haar leeswijzer, 5 minuten.

De plaat is het werkbeeld van het project: elke stroom erop is een kandidaat voor een koppelingspecificatie. Het ArchiMate-model waaruit de plaat komt blijft hier buiten beeld; dat opent alleen in Archi, en de platen dragen de inhoud.

## 8. De koppelvlakspecificatie en haar uitgangspunten

[`Koppelvlakspecificaties/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md) met [`uitgangspunten.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md)

- **Vraag** Wat bevat een afgeronde beschrijving, en wat is het verschil tussen een koppeling en een koppelvlak.
- **Overslaan** De uitgangspunten die niet op een eigen vraag drukken; de README wijst de leesvolgorde.
- **Status** Het veld `versie` in `release.json` van het pakket, en de uitgangspunten zelf benoemen de status van de besluiten die zij aanhalen.
- **Omvang** 1998 woorden, 11 minuten.

Een koppeling is de informatiestroom tussen twee componenten; een koppelvlak is de verzameling koppelingen van precies een component. Dat onderscheid draagt de hele indeling van het pakket. Wie wil zien hoe ver een uitwerking gaat, opent daarna een applicatiecomponent met zijn interactiepatroon en een datamodelschema.

## 9. De interactieketenspecificatie onderwijsaanbod

De interactieketenspecificatie onderwijsaanbod in [pull request 373 van Npuls-OKx/meta](https://github.com/Npuls-OKx/meta/pull/373)

- **Vraag** Waar werkt het project nu aan, en hoe ziet een keten eruit die van de business-waarde tot een machineleesbaar contract is doorgetrokken.
- **Overslaan** De onderliggende stroomdocumenten en de OpenAPI-documenten, tenzij een vraag daarop uitkomt.
- **Status** Deze specificatie staat nog in een open pull request en niet op de ontwikkellijn; de review-instructie in die pull request zegt wat er beoordeeld wordt. Per informatiestroom staat de stand in de kop van haar document.
- **Omvang** 1975 woorden, 11 minuten.

Dit is de voorhoede van het werk: de vorm waarin de rest van de keten gaat volgen. Het materiaal staat in meta en is daarmee kaderstelling, geen releaseartefact. Zodra de pull request landt, verhuist deze stap naar het document op de ontwikkellijn.

## 10. Release, beheer en de stand van het werk

[`Algemeen/release-management/Release-management-algemeen.md`](https://github.com/Npuls-OKx/Public/blob/dev/Algemeen/release-management/Release-management-algemeen.md), met de milestones van [meta](https://github.com/Npuls-OKx/meta/milestones) en [Public](https://github.com/Npuls-OKx/Public/milestones) en het [wijzigingenoverzicht van meta](../CHANGELOG.md)

- **Vraag** Wie draagt het resultaat, hoe komt een versie tot stand, en wat staat er vandaag open.
- **Overslaan** Niets; dit is de kortste stap met het grootste bereik.
- **Status** De `versie` in het release-manifest van elk pakket, en de milestones voor het lopende werk.
- **Omvang** 1109 woorden en twee milestonelijsten, 6 minuten.

Een versielabel zegt wat er vastligt en wat nog beweegt. Zolang een pakket zijn eerste stabiele versie niet heeft bereikt, is elk onderdeel eraan onderhevig aan wijziging, ook wanneer het document zelf afgerond leest.

## Na de route: drie vragen

Wie de route heeft gelopen kan deze drie vragen beantwoorden. Lukt dat niet, dan is dat een tekortkoming van de route en niet van de lezer; de vindplaats hoort in een issue.

1. Welke drie componenten dragen de stroom van een kwalificatiedossier naar een aanmeldbaar onderwijsaanbod, en welk begrip verbindt de specificatie met het resultaat?
2. Welke keuze in de afbakening verklaart waarom federatie tussen instellingen nog niet aan de orde is?
3. Welk deel van het werk ligt vast in een releasepakket, en welk deel is voorstel dat nog kan wijzigen?

## Wat deze route niet doet

De route leidt naar de kaderstelling en naar de vorm van het eindproduct, niet naar een bouwbaar contract. Wie een koppeling gaat bouwen begint bij de applicatiecomponenten, de interactiepatronen en de datamodelschema's in het pakket koppelvlakspecificatie, en gebruikt de kaderstelling als naslag. Die route is korter, en begint aan de andere kant.

De route noemt ook geen aantallen en geen versienummers. Wie de stand van het werk wil zien, volgt stap 10.

## Wie de route bijwerkt

De route hangt aan de persona in [`.agents/personas/domeinarchitect-npuls.md`](../.agents/personas/domeinarchitect-npuls.md). Verandert die persona, dan verandert de route mee. Verhuist of verdwijnt een document uit de route, dan meldt de voorcontrole op de verwijzingen dat; een verwijzing naar de andere repository valt daarbuiten en vraagt een eigen controle.

## Dekking van de persona

Elk leesdoel en elk afhaakpunt van de persona wordt door ten minste precies een stap gedekt, en elke stap dient ten minste precies een leesdoel.

| Uit de persona | Gedekt door |
|---|---|
| Wat is besloten en wat is nog voorstel | 3, en de statusregel bij elke stap |
| Waar raakt dit de landelijke voorzieningen en de andere projecten | 3 met de twee besluiten over de referentiekaders, en 8 |
| Wat wordt van hem gevraagd | 4 en 10 |
| Afhaakpunt: een document dat de stand beweert terwijl die is ingehaald | De regel dat deze route geen stand draagt, en stap 10 |
| Afhaakpunt: een concept dat als besluit leest | 3, 6 en 9, elk met de vindplaats van de status |
| Afhaakpunt: proza zonder te zeggen waar hij op mag rekenen | De selectie in 5, en stap 10 |
| Afhaakpunt: een toevoeging zonder benoemde beheerder | 10 |
| Afhaakpunt: een eigen begrippenstelsel naast de referentiekaders | 3 en 6 |

Relateert aan: de ingang van deze repository en de routes per lezersrol die daar komen.
