# Softwarearchitect bij een applicatieleverancier

## Rol

Softwarearchitect bij een leverancier van applicaties binnen het onderwijsecosysteem. Die applicaties zijn vaak ontwikkeld en beheerd los van de referentiearchitectuur, met eigen grenzen en een eigen datamodel. Ontwerpt hoe de koppeling in dat landschap landt en bepaalt wat het bouwen kost.

## Kennis en vaardigheden

Ontwerpt API's en integraties: REST en OpenAPI, meldpatronen met gebeurtenissen (events en webhooks), herhaalbaarheid zonder neveneffect (idempotentie), herstel na een gemist bericht, en versionering met behoud van compatibiliteit. Kent authenticatie met OAuth 2.0 client credentials en de eisen die Edukoppeling daaraan stelt. Kent de eigen applicatiearchitectuur en het datamodel door en door, inclusief de historie van keuzes die niemand meer terugdraait. Kent OEAPI mogelijk gedeeltelijk, afhankelijk van eerdere trajecten. Het onderwijsdomein kent hij functioneel, niet als vakgebied.

## Afstand tot OKx en de kennisbank

Kent OKx vanaf de rand: hij weet dat het over gestandaardiseerde koppelvlakken gaat en waarom, maar is niet intrinsiek bekend met de begrippen en de leerroutes. Leest de koppelvlakspecificaties, de interactiepatronen, de datamodelschema's en de endpointtabellen bij de applicatiecomponenten. De requirementsboom raadpleegt hij hooguit om te begrijpen waarom een eis bestaat.

## Leesdoel

Wat moet ik bouwen: welke endpoints, welke payload, welke volgorde, welke foutafhandeling en welke versies moet ik ondersteunen.

## Afhaakpunten

- Een begrip dat zonder definitie wordt gebruikt, zoals cohort of leergelegenheid.
- Een indeling in referentiecomponenten die niet op zijn applicatiegrenzen te leggen is, zonder dat de vertaalslag ergens staat.
- Een eis zonder bijbehorende interactie, of een interactie zonder endpoint.
- Een schema zonder voorbeeldpayload.
- Impliciete aannames over volgorde, gelijktijdigheid of herhaling.
- Ontbrekende foutpaden: alleen het nominale verloop beschreven.
