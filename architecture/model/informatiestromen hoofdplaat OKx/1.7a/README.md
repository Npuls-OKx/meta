# Versie 1.7a

![OKx hoofdplaat v1.7a](<OKx hoofdplaat v1.7a.png>)

Export uit de view `OKx hoofdplaat v1.7a` in [`model.archimate`](../../model.archimate), als PNG met schaal 100% en marge 10. De legenda op de plaat draagt nog de status concept.

Wat er ten opzichte van [1.7](../1.7/README.md) is veranderd:

| Wijziging | Waarom |
|---|---|
| De stroom van het studentvolgsysteem (SVS) naar het studentkeuzesysteem (SKS), die meldt dat een opleidingsprogramma of onderwijseenheid van de student voltooid is: gevolgd en afgerond | Een onderdeel dat de student al heeft gevolgd en afgerond, is niet meer te kiezen. Uit een proefimplementatie bij mboRijnland (meta #393, Npuls-OKx/Public#110) |
| De stroom staat ook op de koppelvlakviews SIS en SKS | Het koppelvlak van een component is de optelsom van zijn stromen |
| Drie notities verwijderd van de hoofdplaat (eduhub-aanbod, externe student journey, inrichtingsprincipes SIS) | Keuze van de modelleur |
| De viewnamen zonder `<concept>` en `:`, volgens de [conventie](../../README.md#viewnamen) | Een viewnaam wordt een bestandsnaam (#405) |
| In het koppelvlak van het leermanagementsysteem loopt "Student, opleidingprogramma verbintenis, relevante groepen" weer van de kernregistratie (KRS) naar het LMS | De view liep tegen de hoofdplaat in (#397) |
