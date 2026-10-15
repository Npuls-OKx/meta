# Wat deze snede aan Npuls-OKx/Public teruggeeft

Twintig schema's dragen de berichten van deze snede, waarvan dertien een voorstel. Dit bestand zegt per schema wat er in Public moet landen en wat dat kost, en daaronder wat er naast de schema's bij komt. De verdieping per stroom draagt de werkbrief zelf, met haar volledige tekst.

## De schema's per eenheid

| Schema | Nederlandse naam | Status | Eenheden | Werkbrief en afwijking |
|---|---|---|---|---|
| `arrangement-status.json` | Inrichtingsstatus | voorstel | IS-OA-05 | W4: het schema vult de rij `inrichtingsstatus` die de dienstpagina aankondigt |
| `education-design.json` | Onderwijsontwerp | voorstel | IS-OA-02 | WB-01 tot en met WB-08: met `allOf` gecomponeerd in de twee dragende schema's |
| `education-offering.json` | Onderwijsaanbod | vastgelegd | IS-OA-04 | W1 van IS-OA-06: de statuswaarde `aanmeldbaar` in de gesloten lijst is MAJOR |
| `education-offering-delta.json` | Onderwijsaanbod-delta | voorstel | IS-OA-05 | W7, naar het model van education-specification-delta.json |
| `education-specification.json` | Onderwijsspecificatie | vastgelegd | IS-OA-01 tot en met IS-OA-03 | WB-01 van IS-OA-02: de ontwerpvelden erin met `allOf` |
| `expertise-profile.json` | Expertise- of functieprofiel | voorstel | IS-OA-02 | WB-03, met `organisationUnitId` op organisation-unit.json |
| `intake-finding.json` | Innamebevinding | voorstel | IS-OA-01 | W15, met de codelijst in regels.md naast die van bottleneck.json |
| `intake-outcome.json` | Innameuitkomst | voorstel | IS-OA-01 | W14: naast processing-status.json, of de sleutels `deliveryId` en `findings` daarin. `specificationReference` daar voorwaardelijk maken is MAJOR |
| `intake-rejection.json` | Innameafkeuring | voorstel | IS-OA-01 | W16: als antwoordlichaam bij 400 en 409, met die 409 erbij op de componentpagina's |
| `learning-resource-group.json` | Leermiddelgroep | voorstel | IS-OA-02 | WB-06, met de leermiddelkoppeling in gebruiksprofielen.md erop |
| `offering-open-for-application.json` | Aanmeldbaar aanbod | voorstel | IS-OA-05, IS-OA-06 | W2 en W11: als gebruiksprofiel van education-offering.json, met een profiel per afnemer |
| `offering-processing-status.json` | Verwerkingsstatus van aanbod | voorstel | IS-OA-06 | W6, naast processing-status.json met het aanbod als onderwerp |
| `offering-reference.json` | Aanbod-referentie | voorstel | IS-OA-05, IS-OA-06 | W8: het vervangt de inline vorm in offering-processing-status.json, MAJOR voor wie daarop valideert |
| `offering-request.json` | Verzoek tot aanbod | voorstel | IS-OA-03 | W1 van IS-OA-03: naast specification-reference.json, dat in interactie I7 en in processing-status.json ongewijzigd blijft |
| `offering-status-changed.json` | Aanbod-status-gewijzigd | voorstel | IS-OA-05, IS-OA-06 | W1 en W5, met de meldingssoort per koppeling op de componentpagina |
| `processing-status.json` | Verwerkingsstatus | vastgelegd | IS-OA-02, IS-OA-04 | W14 van IS-OA-01: de sleutels van de inname erin of ernaast |
| `result-structure.json` | Resultaatstructuur en examenplan | vastgelegd | IS-OA-01, IS-OA-02 | W7 van IS-OA-01: de formatieve wortel als enumwaarde erbij |
| `room-type.json` | Onderwijslocatie type | voorstel | IS-OA-02 | WB-02, met `locationIds` op location.json |
| `specification-reference.json` | Specificatie-referentie | vastgelegd | IS-OA-03 | W3 van IS-OA-01: kopmetadata in de respons erbij |
| `student-choice-rule.json` | Student keuze regel | voorstel | IS-OA-01, IS-OA-03 | W9: in `rules` van rule-set.json, MINOR naast de vrije vorm en MAJOR bij dichtzetten |

Een schema zonder eigen payload draagt de losse objecten waarnaar een ander schema wijst, en komt mee in diens validatie.

Wat er naast de schema's landt:

| Wat erbij komt | Waar | Versie-impact |
|---|---|---|
| De paden en meldingen uit [paragraaf 5 van de interactiespecificatie](README.md#5-elk-endpoint-staat-bij-zijn-bezitter), met hun parameters en statuscodes | de componentpagina's, plus een nieuwe voor centraal aanmelden | Nieuwe endpoints |
| De meldingssoorten `ontwerp-gereed`, `aanbod-aanmeldbaar`, `aanmeldbaar-aanbod-beschikbaar` en `inrichtingsstatus` | de gesloten lijst `events` in subscription.json | MAJOR voor wie op die lijst valideert |
| Een stabiel `eventId` op elke melding, dat U5 voor herhaalbare verwerking vraagt | de eventschema's in Public | Optioneel MINOR, verplicht MAJOR |
| De diensten voor de inname en voor aanmeldbaar aanbod, met het gebruiksprofiel per koppeling eronder | de dienstenlijst en gebruiksprofielen.md | Nieuwe dienstpagina's |
| De Nederlandse naam per nieuwe sleutel, en het begrip levering als eenheid van aanname | mapping.md en de begrippenlijst | Geen schemawijziging |
| Een objecttype per verwijzing uit [S19](signaleringen.md), met een definitie erbij | het informatiemodel en de begrippenlijst | Geen schemawijziging |

`vastgelegd` staat voor een schema dat [Public](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen/schemas) draagt met het label alfa, `voorstel` voor een schema uit [schemas/](schemas/) met een `$id` op `/voorstel`. Een voorstel landt door het daar op te nemen: de `$id` wisselt naar `/alfa` en de verwijzingen worden bestandsrelatief, wat additief is en daarmee MINOR ([versionering](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/regels.md)).

Elke voorbeeldpayload noemt achter haar taalaanduiding de schema's waartegen zij valideert, zoals `schema=intake-outcome`; twee namen staan voor een dragend schema met een overlay. `python3 scripts/controleer-interactiespec.py` haalt elke payload erlangs en meldt elke sleutel die geen schema verklaart. Een schema zonder eigen payload draagt de objecten waarnaar een ander wijst.
