# Sjabloon informatiemodel viewpoint

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een viewpoint op het informatiemodel: welke objecttypen er zijn, hoe zij samenhangen, en voor welke lezer deze plaat bedoeld is |
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want het viewpoint hangt aan het ArchiMate-model |
| Voorbeeld | [informatiemodel OKx](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md) |
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

Tussen de inbreng van instellingen en dit document zit een analysestap. Een objecttype hoort hier wanneer meerdere instellingen het nodig hebben, niet wanneer een instelling het zo genoemd heeft. Hoe een instelling haar onderwijs inricht blijft haar keuze: OKx legt alleen de vorm van de uitwisseling vast.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

## 1 Informatiemodel OKx

**Voorbeeld** [Informatiemodel OKx, Informatiemodel OKx](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#informatiemodel-okx)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 1.1 Context

**Voorbeeld** [Informatiemodel OKx, Context](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#context)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 1.2 Inleiding

**Voorbeeld** [Informatiemodel OKx, Inleiding](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#inleiding)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 1.3 Doel

**Voorbeeld** [Informatiemodel OKx, Doel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#doel)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 1.4 Scope

**Voorbeeld** [Informatiemodel OKx, Scope](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#scope)

**Verwacht** een beeld, een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

| | Niveau | Waar het staat |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

![Informatiemodel OKx, versie v0.2 van 14 oktober 2026](<img/informatiemodel-viewpoint/OKx informatiemodel v0.2.jpg>)

*Schrijf hier de uitwerking.*

### 1.5 Lezers en detailniveau

**Voorbeeld** [Informatiemodel OKx, Lezers en detailniveau](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#lezers-en-detailniveau)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| | |
|---|---|
| | |
| | |

*Schrijf hier de uitwerking.*

### 1.6 Begrippenfamilies

**Voorbeeld** [Informatiemodel OKx, Begrippenfamilies](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#begrippenfamilies)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Begrip | Wat het is | Beantwoordt de vraag |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

*Schrijf hier de uitwerking.*

### 1.7 Notatie

**Voorbeeld** [Informatiemodel OKx, Notatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#notatie)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| | Relatie | Betekenis in dit model |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

*Schrijf hier de uitwerking.*

### 1.8 Ontwerpkeuzes

**Voorbeeld** [Informatiemodel OKx, Ontwerpkeuzes](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#ontwerpkeuzes)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 1.9 Verwante documenten

**Voorbeeld** [Informatiemodel OKx, Verwante documenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#verwante-documenten)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Document | Verhouding |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |

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
