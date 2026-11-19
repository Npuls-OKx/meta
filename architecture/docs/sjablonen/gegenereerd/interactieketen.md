# Sjabloon interactieketen

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een interactieketen: welke diensten elkaar in welke volgorde aanroepen om een keten af te maken, en welke afspraken elke dienst nakomt |
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want de keten raakt de koppelvlakken |
| Voorbeeld | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review als pull request 373 |
| Inleveren | terug naar OKx SI als Word-bestand |

## Werkwijze

Elk hoofdstuk opent met een blok van vier regels. Dat blok zegt wat er van dit hoofdstuk wordt verwacht, en het blijft staan: het is de opdracht en niet de uitwerking.

| Regel | Wat erin staat |
|---|------------------------------------------------|
| Voorbeeld | de plek in de voorbeelduitwerking waar hetzelfde hoofdstuk al is ingevuld |
| Verwacht | het artefact dat hier hoort, afgeleid uit wat de voorbeelduitwerking daar levert |
| User stories | de nummers uit het pakket van eisen die dit hoofdstuk verwezenlijkt |
| Klaar wanneer | het acceptatiecriterium waaraan de uitwerking voldoet |

De koppen blijven staan zoals zij hier staan. In het agent-harnas komt een lezer (parser) die een ingevuld document per kop terugvertaalt naar de kennisbank; een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt dus zijn kop, met de reden eronder.

## Van user story naar requirement

Een hoofdstuk is pas af wanneer het aanwijsbaar is welke user stories het verwezenlijkt. Die stories komen uit de gedeelde analyse van alles wat scholen als input hebben geleverd, geinventariseerd in de PoC-sessies met de koploperscholen en samengebracht tot het pakket van eisen. De grootst gemene deler daaruit is wat OKx vastlegt.

Elke story gaat daarna door drie lagen. Een voorbeeld, zodat de vorm vastligt:

| Laag | Voorbeeld |
|---|------------------------------------------------|
| User story | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het keuzedeel, de periode en de locatie |
| Technical requirement | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de user stories in; de drie requirementlagen volgen daarna in een eigen ronde, met dit document als bron.

## De grootst gemene deler

Tussen de inbreng van instellingen en leveranciers en dit document zit een analysestap. Houd daarbij drie dingen uit elkaar: wat een product vandaag doet, wat een component moet kunnen, en wat OKx als grootst gemene deler vastlegt. Een leverancier spreekt voor zijn product en niet voor de sector.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

## 1 De informatiestromen

**Voorbeeld** [Keten onderwijsaanbod, De informatiestromen](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#1-de-informatiestromen)

**Verwacht** een beeld, een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

*Beeld ontbreekt in de bron: De zeven informatiestromen van deze keten, uitgelicht op de informatiestromen-hoofdplaat v1.7.*

| Nr | Naam | Van | Naar | Wat erover gaat | Stand |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Schrijf hier de uitwerking.*

### 1.1 IS-XX-01 Ontwerp naar de catalogus

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-01 Ontwerp naar de catalogus](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-01-ontwerp-naar-de-catalogus)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F1-12: de opleidingsspecificatie met haar programma's, eenheden, leeronderdelen, keuzedeelruimte en summatieve resultaatstructuur, alles verwijzend naar leeruitkomsten, naar de onderwijscatalogus.*

*Schrijf hier de uitwerking.*

### 1.2 IS-XX-02 Onderwijsontwerp naar de catalogus

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-02 Onderwijsontwerp naar de catalogus](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-02-onderwijsontwerp-naar-de-catalogus)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F1-13: vorm, leeromgeving, docent- en examinatorprofiel, studiebelasting en toetsvorm als verdieping op de specificatiestructuur, van de conceptplaat Onderwijsontwerp.*

*Schrijf hier de uitwerking.*

### 1.3 IS-XX-03 Verzoek om aanbod naar planning

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-03 Verzoek om aanbod naar planning](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-03-verzoek-om-aanbod-naar-planning)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F2-03: het verzoek tot aanbod met de specificatiestructuur en de planbare waarden per eenheid, van de onderwijscatalogus naar het planningssysteem.*

*Schrijf hier de uitwerking.*

### 1.4 IS-XX-04 Gepland aanbod naar de catalogus

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-04 Gepland aanbod naar de catalogus](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-04-gepland-aanbod-naar-de-catalogus)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F2-07: het geplande aanbod in de lagen opleiding, programma, eenheid en gelegenheid, elk verwijzend naar specificatie en verzoek, terug naar de onderwijscatalogus.*

*Schrijf hier de uitwerking.*

### 1.5 IS-XX-05 Aanmeldbaar aanbod naar de kernregistratie

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-05 Aanmeldbaar aanbod naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-05-aanmeldbaar-aanbod-naar-de-kernregistratie)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F3-01: het aanmeldbare opleidingsprogramma-aanbod van de onderwijscatalogus naar de kernregistratie.*

*Schrijf hier de uitwerking.*

### 1.6 IS-XX-06 Aanmeldbaar aanbod naar centraal aanmelden

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-06 Aanmeldbaar aanbod naar centraal aanmelden](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-06-aanmeldbaar-aanbod-naar-centraal-aanmelden)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F3-02: hetzelfde aanmeldbare aanbod van de kernregistratie naar AII, de voorziening voor centraal aanmelden.*

*Schrijf hier de uitwerking.*

### 1.7 IS-XX-07 Specificaties naar het leermanagementsysteem

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-07 Specificaties naar het leermanagementsysteem](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-07-specificaties-naar-het-leermanagementsysteem)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Beeld F4-02: de detailspecificaties van de onderwijscatalogus naar het leermanagementsysteem, ter inrichting van de leeromgeving.*

*Schrijf hier de uitwerking.*

## 2 Opbrengst van de keten

**Voorbeeld** [Keten onderwijsaanbod, Opbrengst van de keten](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#2-wat-deze-keten-oplevert)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Partij | Waarvoor deze keten dient |
|---|---|
| | |
| | |
| | |
| | |

| Wat hierop bouwt | Wat die keten eraan heeft |
|---|---|
| | |
| | |
| | |

*Schrijf hier de uitwerking.*

## 3 Gegevensoorsprong en bronsysteem

**Voorbeeld** [Keten onderwijsaanbod, Gegevensoorsprong en bronsysteem](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#3-gegevensoorsprong-en-bronsysteem)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

*Beeld ontbreekt in de bron: Per applicatiecomponent de objecttypen die daar ontstaan, gegroepeerd naar de interactiespecificatie die ze ontsluit.*

*Schrijf hier de uitwerking.*

## 4 Koppelvlakdiensten

**Voorbeeld** [Keten onderwijsaanbod, Koppelvlakdiensten](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#4-koppelvlakdiensten)

**Verwacht** een beeld, een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

*Beeld ontbreekt in de bron: Wie biedt en wie neemt welke koppelvlakdienst af, per applicatiecomponent.*

| Component | Dienst | Endpoints en meldingen | Eenheid | Stand |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

## 5 Afspraken per dienst

**Voorbeeld** [Keten onderwijsaanbod, Afspraken per dienst](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#5-afspraken-die-elke-dienst-nakomt)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Afspraak | Wat zij de implementator oplegt | Waar zij staat | Stand in deze keten |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

## 6 De interactieketen

**Voorbeeld** [Keten onderwijsaanbod, De interactieketen](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#6-de-interactieketen)

**Verwacht** een procesdiagram (BPMN, mermaid, UML of vergelijkbaar)

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt

*Schrijf hier de uitwerking.*

## 7 De interactiespecificaties

**Voorbeeld** [Keten onderwijsaanbod, De interactiespecificaties](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#7-de-interactiespecificaties)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Nr | Naam | Wat erover gaat | Operaties |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

## Afwijkingen per instelling

Wat bij een instelling anders gaat dan hierboven staat, per regel met de instelling erbij. Dit is geen restcategorie: hier staat het materiaal waaruit blijkt of de grootst gemene deler houdbaar is.

| Instelling | Hoofdstuk | Wat daar anders gaat |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

## Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het speelt.

| Nummer | Hoofdstuk | Vraag |
|---|---|------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
