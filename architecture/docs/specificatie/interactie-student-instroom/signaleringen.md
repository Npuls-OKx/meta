# Signaleringen en openstaande punten

Twee signaleringen vragen een besluit voordat een eenheid vastligt. Elke rij zegt wat er is aangetroffen en welk besluit dat vraagt; de eenheid waar zij valt staat in de [interactieketenspecificatie](README.md).

| Nr | Signalering | Besluit |
|---|---|---|
| S1 | Het `Intake systeem` staat in [componenten.json](../../../model/informatiemodel/componenten.json) en draagt op hoofdplaat v1.7 geen enkele stroom, terwijl de beelden F3-05, F3-06 en F3-07 erop leunen: de intake kent de student aan een plaatsingsgroep toe en maakt van een aanmelding een inschrijving | of de intake een eigen applicatiecomponent is met eigen koppelvlakdiensten, of een functie binnen de kernregistratie. Bevinding F3-07 van de tegenlezing betwist de intake als bron |
| S2 | Beeld F4-09 laat Jochems verbintenissen op de geroosterde gelegenheden in de kernregistratie landen, en v1.7 draagt daarvoor de stroom `Ontsluiten planninggroepen met studenten` van het roostersysteem naar de kernregistratie. De sectorarchitect zegt dat de kernregistratie niets van het rooster hoeft te weten | of die stroom van de plaat af gaat. Deze keten laat de geroosterde verbintenis in het studentkeuzesysteem landen (IS-SI-06), waarvoor v1.7 een eigen stroom draagt |

Verder open:

| Punt | Stand |
|---|---|
| Het studentkeuzesysteem kan de verbintenis uit IS-SI-03 pas plaatsen als het het aanbod kent. Hoofdplaat v1.7 draagt daarvoor `Onderwijsprogramma aanbod` van de onderwijscatalogus naar het studentkeuzesysteem, en daarnaast `Onsluiten geplande leergelegenheden (capaciteit)` vanuit het planningssysteem en `Ontsluiten van geroosterde leergelegenheden (detail en capaciteit)` vanuit het roostersysteem | Drie stromen die het studentkeuzesysteem inrichten voordat een student kiest. Besloten: zij landen als eenheid in de keuzedeelketen, want het studentkeuzesysteem bestaat om de student te laten kiezen en deze drie zijn zijn inrichting daarvoor. Deze keten noemt ze als voorwaarde |
| Beeld F4-11 laat de verbintenissen op alle niveaus in het studentvolgsysteem landen; v1.7 draagt daarvoor een stroom van het studentkeuzesysteem naar het studentvolgsysteem | Die stroom hoort bij de keuzedeelketen, waar de student zelf kiest. Langs welke weg de verbintenis in dit traject het studentvolgsysteem bereikt, staat open |
| De stroom van het studentkeuzesysteem terug naar de kernregistratie, met `Student Opleidingprogramma verbintenis (type: keuzedeel/credential)` | Komt pas aan de orde bij de keuzedeelketen; hier kiest de student nog niets |
| Het studentkeuzesysteem ontvangt in deze keten verbintenissen en een rooster, terwijl zijn naam naar keuzes verwijst | De keuzedeelketen werkt met hetzelfde component; daar hoort de vraag of die naam de lading dekt |
| De vier bevindingen van de tegenlezing die de bronvraag betwisten (F3-05, F3-07, F3-08, F4-05) | Komen per eenheid terug waar zij die eenheid raken |
| Zes van de zes stromen die deze keten draagt, staan op v1.7 zonder koppelingspecificatie | Deze keten is daarmee geheel voorstel, anders dan de keten onderwijsaanbod waar OC-P&R, OC-SIS en OC-LMS al vastlagen |
