# Sjabloon interactieketen

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een interactieketen: welke diensten elkaar in welke volgorde aanroepen om een keten af te maken, en welke afspraken elke dienst nakomt |
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want de keten raakt de koppelvlakken |
| Voorbeelduitwerking | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review als pull request 373 |
| Inleveren | terug naar OKx SI als Word-bestand |

## Vaste koppen

De koppen in dit document blijven staan zoals zij hier staan. In het agent-harnas komt een lezer (parser) die een ingevuld document per kop terugvertaalt naar de kennisbank; een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt dus zijn kop, met de reden eronder.

Dit sjabloon is afgeleid uit [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review als pull request 373, dus het draagt elke kop en elke tabel van die uitwerking. Wat daar algemeen was staat er nog. Wat daar aan die ene uitwerking hing, staat er als ingesprongen citaat, met *Schrijf hier de uitwerking.* eronder: daar hoort de eigen uitwerking. Een lege tabel heeft evenveel rijen als de uitwerking had, zodat zichtbaar is hoeveel er wordt verwacht.

## De grootst gemene deler

Tussen de inbreng van instellingen en leveranciers en dit document zit een analysestap. Houd daarbij drie dingen uit elkaar: wat een product vandaag doet, wat een component moet kunnen, en wat OKx als grootst gemene deler vastlegt. Een leverancier spreekt voor zijn product en niet voor de sector.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

| | |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |

## Leeswijzer

| Deel | Inhoud |
|---|---|
| [1 De informatiestromen](#1-de-informatiestromen) | Welke informatie waarheen gaat, met per stroom het beeld van wat erover gaat |
| [2 Wat deze keten oplevert](#2-wat-deze-keten-oplevert) | Waarvoor deze keten dient, per partij, en wat erop bouwt |
| [3 Gegevensoorsprong en bronsysteem](#3-gegevensoorsprong-en-bronsysteem) | Per applicatiecomponent de gegevens die daar ontstaan |
| [4 Koppelvlakdiensten](#4-koppelvlakdiensten) | Per component de diensten met hun endpoints en meldingen |
| [5 Afspraken die elke dienst nakomt](#5-afspraken-die-elke-dienst-nakomt) | Wat voor elke dienst in deze keten geldt, waar elke interactiespecificatie naar wijst |
| [6 De interactieketen](#6-de-interactieketen) | De volgorde over alle zeven de interactiespecificaties |
| [7 De interactiespecificaties](#7-de-interactiespecificaties) | Per stroom het contract: operaties, berichten, voorbeeldpayload |
| [schemas/](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/schemas/README.md) | De twintig schema's van deze keten, met hun stand |
| [signaleringen.md](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/signaleringen.md) | Achtentwintig punten die een besluit vragen |

Elk objecttype en elke instantie hier komt uit het [informatiemodel OKx](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/model/informatiemodel/informatiemodel.md) en de [voorbeelduitwerking van leerroute 1](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/model/informatiemodel/voorbeeld-leerroute-1-jochem.md). Dit document herhaalt die niet, het verwijst erheen waar een stroom valt.

## 1. De informatiestromen

*Beeld: De zeven informatiestromen van deze keten, uitgelicht op de informatiestromen-hoofdplaat v1.7. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: De componenten die meedoen zijn omlijnd en bij elke stroom staat wat er overheen gaat.

| Nr | Naam | Van | Naar | Wat erover gaat | Stand |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

> Een instelling wijst hier aan welke interactiespecificatie zij uitvraagt;

*Schrijf hier de uitwerking.*

### IS-XX-01 Ontwerp naar de catalogus

*Beeld: Beeld F1-12: de opleidingsspecificatie met haar programma's, eenheden, leeronderdelen, keuzedeelruimte en summatieve resultaatstructuur, alles verwijzend naar leeruitkomsten, naar de onderwijscatalogus. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: Links staat wat de ontwerper bouwde, rechts de catalogus die het opneemt.

> Ontstaan in F1-02 tot en met F1-11, van het ontleden van het dossier tot het vaststellen van het examenplan.

*Schrijf hier de uitwerking.*

### IS-XX-02 Onderwijsontwerp naar de catalogus

*Beeld: Beeld F1-13: vorm, leeromgeving, docent- en examinatorprofiel, studiebelasting en toetsvorm als verdieping op de specificatiestructuur, van de conceptplaat Onderwijsontwerp. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: De blokken hangen onder de typen van IS-OA-01 en vormen geen eigen resource.

> Ontstaan in F1-06 en F1-10.

*Schrijf hier de uitwerking.*

### IS-XX-03 Verzoek om aanbod naar planning

*Beeld: Beeld F2-03: het verzoek tot aanbod met de specificatiestructuur en de planbare waarden per eenheid, van de onderwijscatalogus naar het planningssysteem. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: Het `Verzoek tot Aanbod` staat op de grens tussen specificatie en aanbod:

> Ontstaan in F1-05 tot en met F1-10 en F2-01 en F2-02.

*Schrijf hier de uitwerking.*

### IS-XX-04 Gepland aanbod naar de catalogus

*Beeld: Beeld F2-07: het geplande aanbod in de lagen opleiding, programma, eenheid en gelegenheid, elk verwijzend naar specificatie en verzoek, terug naar de onderwijscatalogus. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: Elke aanbodlaag draagt twee verwijzingen: naar de specificatie waaruit zij volgt en naar het verzoek waarop zij antwoordt.

> Ontstaan in F2-04, waar de planner het aanbod in zijn vier lagen plant.

*Schrijf hier de uitwerking.*

### IS-XX-05 Aanmeldbaar aanbod naar de kernregistratie

*Beeld: Beeld F3-01: het aanmeldbare opleidingsprogramma-aanbod van de onderwijscatalogus naar de kernregistratie. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: Alleen het `Opleidingsprogramma aanbod` gaat mee, met zijn `Opleiding aanbod` erboven, en niet de lagen eronder.

> Ontstaan in F2-04, dezelfde planning die IS-OA-04 terugleverde.

*Schrijf hier de uitwerking.*

### IS-XX-06 Aanmeldbaar aanbod naar centraal aanmelden

*Beeld: Beeld F3-02: hetzelfde aanmeldbare aanbod van de kernregistratie naar AII, de voorziening voor centraal aanmelden. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: De vorm is die van IS-OA-05, met de kernregistratie nu als bezitter.

> Ontstaan in F2-04, via IS-OA-05 een schakel eerder.

*Schrijf hier de uitwerking.*

### IS-XX-07 Specificaties naar het leermanagementsysteem

*Beeld: Beeld F4-02: de detailspecificaties van de onderwijscatalogus naar het leermanagementsysteem, ter inrichting van de leeromgeving. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: De leeromgeving krijgt de volledige specificatieboom plus de formatieve resultaatstructuur, en richt zich in tot op leeronderdeelniveau.

> Ontstaan in F1-05 tot en met F1-09 en F2-04.

*Schrijf hier de uitwerking.*

## 2. Wat deze keten oplevert

| Partij | Waarvoor deze keten dient |
|---|---|
| | |
| | |
| | |
| | |

> De keten onderwijsaanbod schrijft hier: De catalogus publiceert een keer, en een groep systemen neemt af:

| Wat hierop bouwt | Wat die keten eraan heeft |
|---|---|
| | |
| | |
| | |

*Schrijf hier de uitwerking.*

## 3. Gegevensoorsprong en bronsysteem

*Beeld: Per applicatiecomponent de objecttypen die daar ontstaan, gegroepeerd naar de interactiespecificatie die ze ontsluit. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: Een component bezit hier het objecttype waarvan hij in de voorbeelduitwerking het bronsysteem is, en dat is de enige bron ervan (U3).

> De plaat komt uit voorbeeld-lr1-regels.json, getekend met `python3 tools/scripts/teken-gegevens-per-component.py`.

*Schrijf hier de uitwerking.*

## 4. Koppelvlakdiensten

*Beeld: Wie biedt en wie neemt welke koppelvlakdienst af, per applicatiecomponent. Voeg hier het beeld in.*

> De keten onderwijsaanbod schrijft hier: Een dienst zegt wat er over een koppeling moet kunnen, en elk component kan hem claimen;

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

> De dienstnamen komen uit de dienstenlijst op commit d0c20d99;

> `/aanmeldbaar-aanbod` komt tweemaal voor, bij de catalogus en bij de kernregistratie, met dezelfde parameters en statuscodes.

*Schrijf hier de uitwerking.*

## 5. Afspraken die elke dienst nakomt

> De keten onderwijsaanbod schrijft hier: Deze afspraken komen uit Npuls-OKx/Public en gelden voor elke interactie.

| Afspraak | Wat zij de implementator oplegt | Waar zij staat | Stand in deze keten |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> Een enum leeft in het schema dat het veld draagt. De interactiespecificatie zegt per waarde wat zij de ontvanger oplegt.

*Schrijf hier de uitwerking.*

## 6. De interactieketen

*Diagram: de bron tekent hier een sequenceDiagram. Voeg hier het diagram in.*

> De keten onderwijsaanbod schrijft hier: Elk gekleurd kader is een interactiespecificatie, met haar aanduiding erboven.

*Schrijf hier de uitwerking.*

## 7. De interactiespecificaties

| Nr | Naam | Wat erover gaat | Operaties |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> De keten onderwijsaanbod schrijft hier: Elke interactiespecificatie draagt hetzelfde: het contract per koppelvlakdienst, de volgorde als sequentiediagram, de berichten veld voor veld met hun ERD, en een voorbeeldpayload die valideert.

> De voorbeeldpayloads gebruiken de vaste identificaties uit casus.md, zodat dezelfde opleiding door de hele keten dezelfde uuid draagt.

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
