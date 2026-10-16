# Signaleringen en openstaande punten

Een signalering vraagt een besluit voordat een eenheid vastligt. De rij zegt wat er is aangetroffen en welk besluit dat vraagt; de eenheid waar zij valt staat in de [interactieketenspecificatie](README.md).

| Nr | Signalering | Besluit |
|---|---|---|
| S1 | Beeld F4-09 laat Jochems verbintenissen op de geroosterde gelegenheden in de kernregistratie landen, en hoofdplaat v1.7 draagt daarvoor de stroom `Ontsluiten planninggroepen met studenten` van het roostersysteem naar de kernregistratie. De sectorarchitect zegt dat de kernregistratie niets van het rooster hoeft te weten | of die stroom van de plaat af gaat. Deze keten laat de geroosterde verbintenis in het studentkeuzesysteem landen (IS-SI-05), waarvoor v1.7 een eigen stroom draagt |

## Wat buiten deze keten valt

| Wat | Waarom |
|---|---|
| Hoe een student zich bij de voorziening voor centraal aanmelden meldt (F3-03) | AII beschrijft dat deel |
| Het intakesysteem, en daarmee de beelden F3-05 en F3-06 | Buiten scope. Dat een aanmelding een inschrijving wordt is een toestandswijziging binnen de kernregistratie en geen koppeling. Het component draagt op v1.7 dan ook geen enkele stroom |
| De inrichting van het studentkeuzesysteem: `Onderwijsprogramma aanbod` vanuit de catalogus, `Onsluiten geplande leergelegenheden (capaciteit)` vanuit het planningssysteem en `Ontsluiten van geroosterde leergelegenheden (detail en capaciteit)` vanuit het roostersysteem | Drie stromen die het studentkeuzesysteem inrichten voordat een student kiest. Zij zijn voorwaarde voor deze keten en landen als eenheid in de keuzedeelketen |
| De stroom van het studentkeuzesysteem terug naar de kernregistratie, met `Student Opleidingprogramma verbintenis (type: keuzedeel/credential)` | Komt aan de orde bij de keuzedeelketen; hier kiest de student nog niets |

## Verder open

| Punt | Stand |
|---|---|
| Beeld F4-11 laat de verbintenissen op alle niveaus in het studentvolgsysteem landen; v1.7 draagt daarvoor een stroom van het studentkeuzesysteem naar het studentvolgsysteem | Die stroom hoort bij de keuzedeelketen. Langs welke weg de verbintenis in dit traject het studentvolgsysteem bereikt, staat open |
| Het studentkeuzesysteem ontvangt in deze keten verbintenissen en een rooster, terwijl zijn naam naar keuzes verwijst | De keuzedeelketen werkt met hetzelfde component; daar hoort de vraag of die naam de lading dekt |
| De vier bevindingen van de tegenlezing die de bronvraag betwisten (F3-05, F3-07, F3-08, F4-05) | F3-05 en F3-07 raken de intake en vallen daarmee buiten scope; F3-08 en F4-05 komen terug bij IS-SI-02 |
| Zes van de zes stromen die deze keten draagt, staan op v1.7 zonder koppelingspecificatie | Deze keten is daarmee geheel voorstel, anders dan de keten onderwijsaanbod waar OC-P&R, OC-SIS en OC-LMS al vastlagen |
