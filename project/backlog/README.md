# Backlog leerroutes OKx

Werkvoorraad per leerroute: een epic per leerroute als paraplu voor alles wat die leerroute betreft, een feature per interactieketen en stories die een teamlid in één pull request oppakt. Een bevinding uit de regeltabel hoort bij de keten van de interactie die hij verandert. Werk dat de hele leerroute raakt, zoals de scenario's, hangt als story direct onder de epic. Een keten ontstaat in de eerste leerroute die hem nodig heeft; een latere leerroute vult hem aan met een eigen feature, die eindigt in een nieuwe versie van dezelfde koppelvlakspecificatie.

## Opbouw van de map

- Een map per epic en per feature. `epic.md` en `feature.md` beschrijven het item zelf; de genummerde bestanden ernaast zijn de stories eronder. Een story naast `epic.md` hangt direct onder de epic.
- De frontmatter draagt de velden voor GitHub: type, ouder, bestaand issue, schatting en streefdatum. Een item met een bestaand issue wordt naar de planningsrepository verplaatst, niet opnieuw aangemaakt.
- `Wacht op` wordt in GitHub de relatie blocked by; `Draagt bij aan` verwijst naar de features in de requirementsboom.

## Schatting

Volgens de [rekenregels van de product breakdown](https://github.com/Npuls-OKx/meta/blob/feature/product-breakdown/architecture/product-breakdown/README.md#rekenregels): 5 FTE-weken per scenario en 4 per keten tot specificatie; een keten aanvullen voor een volgende leerroute kost 0 tot 4. De rekenregels tellen daarnaast 10 FTE-weken voor het anker van een leerroute. Bij leerroute 1 is dat werk over de ketens verdeeld en zit het nog niet in hun schatting van 4 FTE-weken. Stories zonder schatting worden bij het oppakken geschat.

## Overzicht

### [Leerroute 1, regulier](leerroute-1-regulier/epic.md)

6 features met samen 72 stories, en 5 stories direct onder de epic. Van alle stories hebben er 20 al een issue in meta.

| Feature | Stories | Schatting | Streefdatum | Bestaand issue |
|---|---|---|---|---|
| [Interactieketen onderwijsaanbod: van ontwerp tot aanmeldbaar aanbod](leerroute-1-regulier/1-onderwijsaanbod/feature.md) | 16 | 4 FTE-weken | 15 januari 2027 | [meta #372](https://github.com/Npuls-OKx/meta/issues/372) |
| [Interactieketen student-instroom: van aanmelding tot klaar voor de start](leerroute-1-regulier/2-student-instroom/feature.md) | 16 | 4 FTE-weken | 29 januari 2027 | [meta #386](https://github.com/Npuls-OKx/meta/issues/386) |
| [Interactieketen voortgang: formatieve resultaten tijdens de uitvoering](leerroute-1-regulier/3-voortgang/feature.md) | 6 | 4 FTE-weken | – | – |
| [Interactieketen keuzedelen: kiezen en verwerken](leerroute-1-regulier/4-keuzedelen/feature.md) | 15 | 4 FTE-weken | – | [meta #363](https://github.com/Npuls-OKx/meta/issues/363) |
| [Interactieketen bijsturen: planning, aanbod en rooster tijdens de uitvoering](leerroute-1-regulier/5-bijsturen/feature.md) | 11 | 4 FTE-weken | 12 februari 2027 | [meta #389](https://github.com/Npuls-OKx/meta/issues/389) |
| [Interactieketen examineren: van examenresultaat tot diploma](leerroute-1-regulier/6-examineren/feature.md) | 8 | 4 FTE-weken | – | – |

Direct onder de epic:

- [Variant capaciteitsgestuurd plannen inschuiven](leerroute-1-regulier/01-variant-capaciteitsgestuurd-plannen-inschuiven.md)
- [Modelronde in Archi: planninggroep, lesgroep en de locatierelaties](leerroute-1-regulier/02-modelronde-in-archi-planninggroep-lesgroep-en-de.md)
- [Scenario 1.2: vertraging](leerroute-1-regulier/03-scenario-1-2-vertraging.md)
- [Scenario 1.3: versnelling](leerroute-1-regulier/04-scenario-1-3-versnelling.md)
- [Scenario 1.4: hybride](leerroute-1-regulier/05-scenario-1-4-hybride.md)

### [Leerroute 2, temporiseren](leerroute-2-temporiseren/epic.md)

6 features met samen 12 stories, en 5 stories direct onder de epic. Van alle stories hebben er 1 al een issue in meta.

| Feature | Stories | Schatting | Streefdatum | Bestaand issue |
|---|---|---|---|---|
| [Interactieketen onderwijsaanbod: aanvullen voor leerroute 2](leerroute-2-temporiseren/1-onderwijsaanbod/feature.md) | 2 | 0–4 FTE-weken | – | – |
| [Interactieketen student-instroom: aanvullen voor leerroute 2](leerroute-2-temporiseren/2-student-instroom/feature.md) | 2 | 0–4 FTE-weken | – | – |
| [Interactieketen voortgang: aanvullen voor leerroute 2](leerroute-2-temporiseren/3-voortgang/feature.md) | 2 | 0–4 FTE-weken | – | – |
| [Interactieketen keuzedelen: aanvullen voor leerroute 2](leerroute-2-temporiseren/4-keuzedelen/feature.md) | 2 | 0–4 FTE-weken | – | – |
| [Interactieketen bijsturen: aanvullen voor leerroute 2](leerroute-2-temporiseren/5-bijsturen/feature.md) | 2 | 0–4 FTE-weken | – | – |
| [Interactieketen examineren: aanvullen voor leerroute 2](leerroute-2-temporiseren/6-examineren/feature.md) | 2 | 0–4 FTE-weken | – | – |

Direct onder de epic:

- [Instellingsreis Larissa: leerroutedocument en voorbeeldregels per fase](leerroute-2-temporiseren/01-instellingsreis-larissa-leerroutedocument-en.md)
- [Fasen reviewen met instellingen](leerroute-2-temporiseren/02-fasen-reviewen-met-instellingen.md)
- [Scenario 2.2: temporiseren plus vertraging](leerroute-2-temporiseren/03-scenario-2-2-temporiseren-plus-vertraging.md)
- [Scenario 2.3: temporiseren plus versnelling](leerroute-2-temporiseren/04-scenario-2-3-temporiseren-plus-versnelling.md)
- [Scenario 2.4: temporiseren plus hybride](leerroute-2-temporiseren/05-scenario-2-4-temporiseren-plus-hybride.md)
