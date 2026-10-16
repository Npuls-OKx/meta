# Signaleringen en openstaande punten

Drie signaleringen vragen een besluit voordat een eenheid vastligt. Elke rij zegt wat er is aangetroffen en welk besluit dat vraagt; de eenheid waar zij valt staat in de [interactieketenspecificatie](README.md).

| Nr | Signalering | Besluit |
|---|---|---|
| S1 | Het `Intake systeem` staat in [componenten.json](../../../model/informatiemodel/componenten.json) en draagt op hoofdplaat v1.7 geen enkele stroom, terwijl de beelden F3-05, F3-06 en F3-07 erop leunen: de intake kent de student aan een plaatsingsgroep toe en maakt van een aanmelding een inschrijving | of de intake een eigen component is met eigen koppelvlakdiensten, of een functie binnen de kernregistratie. Bevinding F3-07 betwist de intake als bron |
| S2 | Hoofdplaat v1.7 draagt geen stroom van de kernregistratie naar het studentvolgsysteem, terwijl de beelden F3-08 en F4-11 die nodig hebben: de verbintenissen op alle niveaus en de behaalde leeruitkomsten moeten daar landen | of die stroom erbij komt, en of de kernregistratie en het studentvolgsysteem los te zien zijn. Bevinding F4-05 zegt dat dat in de huidige situatie lastig is |
| S3 | Hoofdplaat v1.7 draagt de stroom `Ontsluiten planninggroepen met studenten` van het roostersysteem naar de kernregistratie, en beeld F4-09 laat Jochems verbintenissen op de geroosterde gelegenheden daar landen. De sectorarchitect zegt dat de kernregistratie niets van het rooster hoeft te weten. De stroom valt daarmee buiten deze keten | waar de verbintenis op een geroosterde gelegenheid dan leeft. Op v1.7 gaat `Student Opleidingprogramma- en onderwijseenheid verbintenis` van het roostersysteem naar het studentkeuzesysteem, en beeld F4-11 laat de verbintenissen naar het studentvolgsysteem gaan |

Verder open:

| Punt | Stand |
|---|---|
| De stroom van de kernregistratie naar het leermanagementsysteem staat op hoofdplaat v1.7, maar `teken-hoofdplaat-ruim.py` kan het pad niet volgen en tekent haar gestippeld | Een junctie die de padzoeker niet aankan; de stroom bestaat wel. Punt voor het plaatgereedschap, niet voor deze keten |
| Vijf van de zes stromen die deze keten draagt, staan op v1.7 als `zonder koppelingspecificatie` | Deze keten is daarmee grotendeels voorstel, anders dan de keten onderwijsaanbod waar OC-P&R, OC-SIS en OC-LMS al vastlagen |
| De vier bevindingen van de tegenlezing die de bronvraag betwisten (F3-05, F3-07, F3-08, F4-05) | Komen per eenheid terug waar zij die eenheid raken |
