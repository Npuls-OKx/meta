# Versie 1.7a

![OKx hoofdplaat v1.7a](<OKx hoofdplaat v1.7a.png>)

Export uit de view `OKx hoofdplaat v1.7a` in [`model.archimate`](../../model.archimate), als PNG met schaal 100% en marge 10. De legenda draagt de status concept.

Wat er ten opzichte van [1.7](../1.7/README.md) is veranderd:

| Wijziging | Waarom |
|---|---|
| Stroom van het studentvolgsysteem (SVS) naar het studentkeuzesysteem (SKS): opleidingsprogramma of onderwijseenheid voltooid | Een onderdeel dat de student heeft gevolgd en afgerond, hoort niet meer bij de keuzes. Casus ingebracht door mboRijnland in de POC-gesprekken (meta #393, Npuls-OKx/Public#110) |
| Dezelfde stroom op de koppelvlakplaten (views) van het studentinformatiesysteem (SIS) en het SKS | Het koppelvlak van een component is de optelsom van zijn stromen |
| Drie notities verwijderd van de hoofdplaat (eduhub-aanbod, externe student journey, inrichtingsprincipes SIS) | Keuze van de modelleur |
| De viewnamen zonder `<concept>` en `:`, volgens de [conventie](../../README.md#viewnamen) | Een viewnaam wordt een bestandsnaam (#405) |
| In het koppelvlak van het leermanagementsysteem (LMS) loopt `Student, opleidingprogramma verbintenis, relevante groepen` nu van het kernregistratiesysteem (KRS) naar het LMS | De view liep tegen de hoofdplaat in (#397) |
| In het koppelvlak van het SIS lopen `Student Opleidingprogramma verbintenis (type: keuzedeel/credential)` en `Student Opleidingprogramma- en onderwijseenheid verbintenis` nu van het SKS naar het SIS, en `Student, opleidingprogramma verbintenis, relevante groepen` van het SIS naar het SKS | Drie pijlen in de view liepen tegen de hoofdplaat in (#397) |
