# Sjabloon interactieketen

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een interactieketen: welke diensten elkaar in welke volgorde aanroepen om een keten af te maken, en welke afspraken elke dienst nakomt. Dit is de laag onder het kaderscenario en boven de endpoints |
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want de keten raakt de koppelvlakken |
| Voorbeelduitwerking | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review als pull request 373 |
| Inleveren | terug naar OKx SI als Word-bestand |


## Vaste koppen

De koppen in dit document blijven staan zoals zij hier staan. In het agent-harnas komt een lezer (parser) die een ingevuld document per kop terugvertaalt naar de kennisbank; een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt dus zijn kop, met de reden eronder.

## De grootst gemene deler

Tussen de inbreng van instellingen en leveranciers en dit document zit een analysestap. Houd daarbij drie dingen uit elkaar: wat een product vandaag doet, wat een component moet kunnen, en wat OKx als grootst gemene deler vastlegt.

Een leverancier spreekt voor zijn product en niet voor de sector. Dat een product een aanroep vandaag niet kent, is een implementatiefeit en geen ontwerpargument; dat het die wel kent, maakt hem nog niet tot afspraak.

## Wat deze keten afmaakt

Welke keten dit is en wat er aan het eind klaar is, in twee zinnen. Een keten zonder eindpunt is een opsomming van aanroepen.

## Informatiestromen

Welke stromen uit het kaderscenario deze keten realiseert, met hun nummer uit dat scenario. Een keten vindt geen stromen uit: zij implementeert de stromen die het scenario heeft benoemd.

| Nummer | Van | Naar | Welke informatie |
|---|---|---|---|

## Gegevensoorsprong

Per gegeven welk systeem de bron is, en welk systeem het alleen doorgeeft. Dit hoofdstuk voorkomt dat twee systemen zich later eigenaar noemen van hetzelfde gegeven.

| Gegeven | Bronsysteem | Wie neemt het over |
|---|---|---|

## Diensten

Per dienst een naam en een versie, en wie hem aanbiedt tegenover wie hem afneemt. Aanbieder en afnemer zijn twee diensten met elk een eigen naam en versie; trek ze niet samen tot een rol.

| Dienst | Versie | Aanbieder | Afnemer | Wat de dienst doet |
|---|---|---|---|---|

## Afspraken per dienst

Wat elke dienst nakomt, ongeacht wie hem bouwt: wanneer hij antwoordt, wat hij doet bij een herhaalde aanroep, en wat er gebeurt wanneer hij niet beschikbaar is. Vaktermen op protocolniveau blijven onvertaald.

## De keten

De volgorde van de aanroepen, als diagram of als genummerde lijst. Volledig, dus met de terugweg en met het foutpad: een keten die alleen het goede verloop toont, is niet te bouwen.

## Afwijkingen per instelling

Waar een instelling of een leverancier de keten anders loopt dan hierboven staat, per regel met de naam erbij. Zet hier ook wat een product vandaag niet kan, zodat het als implementatiefeit bewaard blijft en niet als ontwerpargument meegaat.

## Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag de dienst of de stroom waar het om gaat.
