`<w:p><w:r><w:br w:type="page"/></w:r></w:p>`{=openxml}

# Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een interactieketen: welke diensten elkaar in welke volgorde aanroepen om een keten af te maken, en welke afspraken elke dienst nakomt |
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want de keten raakt de koppelvlakken |
| Voorbeeld | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review als pull request 373 |
| Inleveren | terug naar OKx SI als Word-bestand |

Elk hoofdstuk opent met een blok dat zegt wat er van dat hoofdstuk wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

# Van user story naar eis

Het pakket van eisen komt uit de gedeelde analyse van alles wat scholen hebben ingebracht, geinventariseerd in de PoC-sessies met de koploperscholen. De grootst gemene deler daaruit is wat OKx vastlegt.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort.

| Laag | Waar die ontstaat | Voorbeeld |
|---|---|------------------------------------|
| User story | in een journey of een scenario | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | in een procesbeschrijving | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | in een gegevens- of systeemhoofdstuk | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technical requirement | in een interactiehoofdstuk | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de laag in die boven het hoofdstuk staat. De lagen eronder volgen in een eigen ronde, met dit document als bron.

# De grootst gemene deler

Tussen de inbreng van instellingen en leveranciers en dit document zit een analysestap. Houd daarbij drie dingen uit elkaar: wat een product vandaag doet, wat een component moet kunnen, en wat OKx als grootst gemene deler vastlegt. Een leverancier spreekt voor zijn product en niet voor de sector.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

# De informatiestromen

**Voorbeeld** [Keten onderwijsaanbod, De informatiestromen](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#1-de-informatiestromen)

**Acceptatiecriteria** een beeld, een ingevulde tabel, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

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

## IS-XX-01 Ontwerp naar de catalogus

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-01 Ontwerp naar de catalogus](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-01-ontwerp-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F1-12: de opleidingsspecificatie met haar programma's, eenheden, leeronderdelen, keuzedeelruimte en summatieve resultaatstructuur, alles verwijzend naar leeruitkomsten, naar de onderwijscatalogus.*

*Schrijf hier de uitwerking.*

## IS-XX-02 Onderwijsontwerp naar de catalogus

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-02 Onderwijsontwerp naar de catalogus](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-02-onderwijsontwerp-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F1-13: vorm, leeromgeving, docent- en examinatorprofiel, studiebelasting en toetsvorm als verdieping op de specificatiestructuur, van de conceptplaat Onderwijsontwerp.*

*Schrijf hier de uitwerking.*

## IS-XX-03 Verzoek om aanbod naar planning

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-03 Verzoek om aanbod naar planning](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-03-verzoek-om-aanbod-naar-planning)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F2-03: het verzoek tot aanbod met de specificatiestructuur en de planbare waarden per eenheid, van de onderwijscatalogus naar het planningssysteem.*

*Schrijf hier de uitwerking.*

## IS-XX-04 Gepland aanbod naar de catalogus

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-04 Gepland aanbod naar de catalogus](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-04-gepland-aanbod-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F2-07: het geplande aanbod in de lagen opleiding, programma, eenheid en gelegenheid, elk verwijzend naar specificatie en verzoek, terug naar de onderwijscatalogus.*

*Schrijf hier de uitwerking.*

## IS-XX-05 Aanmeldbaar aanbod naar de kernregistratie

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-05 Aanmeldbaar aanbod naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-05-aanmeldbaar-aanbod-naar-de-kernregistratie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F3-01: het aanmeldbare opleidingsprogramma-aanbod van de onderwijscatalogus naar de kernregistratie.*

*Schrijf hier de uitwerking.*

## IS-XX-06 Aanmeldbaar aanbod naar centraal aanmelden

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-06 Aanmeldbaar aanbod naar centraal aanmelden](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-06-aanmeldbaar-aanbod-naar-centraal-aanmelden)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F3-02: hetzelfde aanmeldbare aanbod van de kernregistratie naar AII, de voorziening voor centraal aanmelden.*

*Schrijf hier de uitwerking.*

## IS-XX-07 Specificaties naar het leermanagementsysteem

**Voorbeeld** [Keten onderwijsaanbod, IS-XX-07 Specificaties naar het leermanagementsysteem](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-07-specificaties-naar-het-leermanagementsysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Beeld F4-02: de detailspecificaties van de onderwijscatalogus naar het leermanagementsysteem, ter inrichting van de leeromgeving.*

*Schrijf hier de uitwerking.*

# Opbrengst van de keten

**Voorbeeld** [Keten onderwijsaanbod, Opbrengst van de keten](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#2-wat-deze-keten-oplevert)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

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

# Gegevensoorsprong en bronsysteem

**Voorbeeld** [Keten onderwijsaanbod, Gegevensoorsprong en bronsysteem](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#3-gegevensoorsprong-en-bronsysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Beeld ontbreekt in de bron: Per applicatiecomponent de objecttypen die daar ontstaan, gegroepeerd naar de interactiespecificatie die ze ontsluit.*

*Schrijf hier de uitwerking.*

# Koppelvlakdiensten

**Voorbeeld** [Keten onderwijsaanbod, Koppelvlakdiensten](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#4-koppelvlakdiensten)

**Acceptatiecriteria** een beeld, een ingevulde tabel, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

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

# Afspraken per dienst

**Voorbeeld** [Keten onderwijsaanbod, Afspraken per dienst](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#5-afspraken-die-elke-dienst-nakomt)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

| Afspraak | Wat zij de implementator oplegt | Waar zij staat | Stand in deze keten |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

# De interactieketen

**Voorbeeld** [Keten onderwijsaanbod, De interactieketen](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#6-de-interactieketen)

**Acceptatiecriteria** een procesplaat in mermaid, BPMN, UML of vergelijkbaar, en het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

# De interactiespecificaties

**Voorbeeld** [Keten onderwijsaanbod, De interactiespecificaties](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#7-de-interactiespecificaties)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Technical requirements** *wat er over het koppelvlak gaat en in welke vorm; verwijs naar het nummer van de story*

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

# Afwijkingen per instelling

Wat bij een instelling anders gaat dan hierboven staat, per regel met de instelling erbij. Dit is geen restcategorie: hier staat het materiaal waaruit blijkt of de grootst gemene deler houdbaar is.

| Instelling | Hoofdstuk | Wat daar anders gaat |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

# Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het speelt.

| Nummer | Hoofdstuk | Vraag |
|---|---|------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
