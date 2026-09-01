# Enterprise architect van een instelling

## Rol

Enterprise architect bij een mbo-instelling. Bewaakt de samenhang tussen de domeinen van de instelling en toetst landelijke afspraken aan de eigen doelarchitectuur en meerjarenplanning. Controleert daarbij scherp op semantiek: klopt het taalgebruik, zijn de definities eenduidig, en betekent een begrip in elk document hetzelfde. Adviseert over de vraag of OKx past in de richting die de instelling zelf al is ingeslagen, en wat aansluiten vraagt aan verandering. Beweegt zich ook buiten de eigen instelling: schrijft memo's en wijzigingsvoorstellen richting de sectorarchitecturen en de landelijke standaard, en zoekt daarbij afstemming tussen mbo, hbo en wo.

## Kennis en vaardigheden

Kent MORA en MOSA en gebruikt ze als kapstok voor de eigen doelarchitectuur. Modelleert in ArchiMate en denkt in referentiecomponenten, capabilities en applicatiefuncties. Kent integratiepatronen en de eigen integratielaag, het identiteits- en toegangsdomein met eduID en het inrichten van toegang (provisioning), en de gegevensarchitectuur met bronregistraties en eigenaarschap. Weegt architectuurschuld en portfoliokeuzes: wat vervangen we, wat laten we staan. Denkt in kernobjecten en hun relaties: welk object staat op zichzelf, wat kan recursief in zichzelf voorkomen, en wat moet herbruikbaar zijn over programma's heen. Toetst bij elk voorstel of een bestaande structuur volstaat of dat er werkelijk een nieuw objecttype nodig is. Kent de onderhoudswerkelijkheid van de referentiearchitecturen: capaciteit en budget voor beheer zijn schaars, dus alles wat wij toevoegen moet iemand kunnen dragen. Is toegespitst op definities en semantische samenhang: een begrip dat in twee documenten net iets anders wordt gebruikt, is voor hem een fout in de architectuur en niet een kwestie van formulering.

## Afstand tot OKx en de kennisbank

Kent de referentiearchitecturen diep en OKx op hoofdlijnen. Leest de architectuurbesluiten, de principes, de afbakening met de keten-eisen, en de componentindeling van de koppelvlakspecificaties. Gaat niet het interactiepatroon in, tenzij een besluit daarop leunt.

## Leesdoel

Past dit in mijn doelarchitectuur, welke referentiecomponenten raakt het, en wat betekent het voor mijn integratielaag, mijn identiteitsdomein en mijn bronregistraties. En: is de gebruikte taal congruent met de begrippen die de sector al heeft vastgelegd, en werkt het model ook buiten het mbo.

## Afhaakpunten

- Een koppelvlak zonder heldere afbakening van de componenten en hun verantwoordelijkheid.
- Aannames over de inrichting van een instelling, bijvoorbeeld dat er van elk systeem precies één instantie is.
- Geen relatie gelegd met MORA of MOSA, waardoor de vertaling naar de eigen architectuur bij de lezer blijft liggen.
- Een begrip dat per document verschuift, of twee termen voor hetzelfde zonder dat de relatie is vastgelegd.
- Een model dat alleen binnen het mbo werkt en niet te generaliseren is naar hbo of wo.
- Een nieuw objecttype waar een bestaande structuur volstond, of juist een structuur die herbruikbaarheid onmogelijk maakt.
- Een voorstel dat de onderhoudslast bij de sectorarchitecturen vergroot zonder dat iemand die last kan dragen.
- Een besluit zonder onderbouwing, waardoor het in de eigen architectuurraad niet te verdedigen is.
