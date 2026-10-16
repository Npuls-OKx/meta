# Signaleringen en openstaande punten

Twee signaleringen vragen een besluit voordat een eenheid vastligt. Elke rij zegt wat er is aangetroffen en welk besluit dat vraagt; de eenheid waar zij valt staat in de [interactieketenspecificatie](README.md).

| Nr | Signalering | Besluit |
|---|---|---|
| S1 | Beeld F7-02 zegt dat annuleren per niveau een andere impact heeft, en breekt daar af. Een verbintenis op onderwijseenheidniveau annuleren laat de verbintenis op programmaniveau staan; een annulering op programmaniveau raakt alles eronder. Welke reeks toestanden een verbintenis kent en wat een annulering op elk niveau doet, is nergens vastgelegd | de toestanden van een verbintenis en hun overgangen, met per niveau wat een annulering meeneemt |
| S2 | Het informatiemodel kent `Plaatsingsgroep` en geen `Planninggroep`, terwijl hoofdplaat v1.7 een stroom `Ontsluiten planninggroepen met studenten` draagt en beeld F7-04 over de planninggroep spreekt. Beeld F7-03 zegt daarbij dat groepen die in de kernregistratie ontstaan per definitie plaatsingsgroepen zijn | of planninggroep een eigen objecttype is of een andere naam voor dezelfde zaak; in het laatste geval volgt een hernoeming op de plaat |

## Wat buiten deze keten valt

| Wat | Waarom |
|---|---|
| De aanleiding voor het bijsturen: aanwezigheid, lesresultaat en formatieve voortgang (F5-01 tot en met F5-03) | Dat ontstaat binnen het leermanagementsysteem. De bron zegt bij F5-01 dat de registratie van aanwezigheid zelf buiten OKx valt |
| Het studiebeeld dat de begeleider naast de nominale route legt (F5-05) | Een beeld dat uit bestaande gegevens wordt samengesteld, geen koppeling |
| Het formatieve resultaat dat naar het studentvolgsysteem gaat (F5-04) | Hoort bij de keten resultaten, samen met de examenresultaten uit F8 |

## Verder open

| Punt | Stand |
|---|---|
| Vier van de vijf koppelingen in deze keten zijn al gespecificeerd in de ketens [onderwijsaanbod](../interactieketen-onderwijsaanbod/README.md) en [student instroom](../interactieketen-student-instroom/README.md) | Deze keten beschrijft wat een wijziging anders maakt dan een eerste levering, en wijst voor het contract naar de eenheid die het droeg |
| De stroom `Verzoek tot bijwerken onderwijspecificaties` staat op v1.7 zonder koppelingspecificatie, en de plaatmarkering kan haar pad niet volgen omdat het planningssysteem en de catalogus twee lijnen delen | De stroom bestaat; dit is een punt voor het plaatgereedschap |
