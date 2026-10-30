# De schema's van deze interactieketen

| Schema | Nederlandse naam | Stand | Interactiespecificaties | Wat het in Public toevoegt of wijzigt |
|---|---|---|---|---|
| `arrangement-status.json` | Inrichtingsstatus | voorstel | IS-OA-05 | Nieuw. Het vult de rij `inrichtingsstatus` die de dienstpagina al aankondigt zonder schema |
| `education-design.json` | Onderwijsontwerp | voorstel | IS-OA-02 | Nieuw. Met `allOf` gecomponeerd in de twee dragende schema's, dus additief |
| `education-offering.json` | Onderwijsaanbod | vastgelegd | IS-OA-04 | De statuswaarde `aanmeldbaar` in de gesloten lijst: MAJOR voor wie erop valideert |
| `education-offering-delta.json` | Onderwijsaanbod-delta | voorstel | IS-OA-05 | Nieuw, naar het model van `education-specification-delta.json` |
| `education-specification.json` | Onderwijsspecificatie | vastgelegd | IS-OA-01 tot en met IS-OA-03 | De ontwerpvelden van IS-OA-02 erin met `allOf`, dus additief |
| `expertise-profile.json` | Expertise- of functieprofiel | voorstel | IS-OA-02 | Nieuw, met `organisationUnitId` op `organisation-unit.json` |
| `intake-finding.json` | Innamebevinding | voorstel | IS-OA-01 | Nieuw, met de codelijst in `regels.md` naast die van `bottleneck.json` |
| `intake-outcome.json` | Innameuitkomst | voorstel | IS-OA-01 | Nieuw naast `processing-status.json`, of de sleutels `deliveryId` en `findings` daarin. Die sleutels daar voorwaardelijk maken is MAJOR |
| `intake-rejection.json` | Innameafkeuring | voorstel | IS-OA-01 | Nieuw, als antwoordlichaam bij 400 en 409, met die 409 erbij op de componentpagina's |
| `learning-resource-group.json` | Leermiddelgroep | voorstel | IS-OA-02 | Nieuw, met de leermiddelkoppeling in `gebruiksprofielen.md` erop |
| `offering-open-for-application.json` | Aanmeldbaar aanbod | voorstel | IS-OA-05, IS-OA-06 | Nieuw, als gebruiksprofiel van `education-offering.json`, met een profiel per afnemer |
| `offering-processing-status.json` | Verwerkingsstatus van aanbod | voorstel | IS-OA-06 | Nieuw naast `processing-status.json`, met het aanbod als onderwerp |
| `offering-reference.json` | Aanbod-referentie | voorstel | IS-OA-05, IS-OA-06 | Nieuw. Het vervangt de inline vorm in `offering-processing-status.json`: MAJOR voor wie daarop valideert |
| `offering-request.json` | Verzoek tot aanbod | voorstel | IS-OA-03 | Nieuw naast `specification-reference.json`, dat ongewijzigd blijft |
| `offering-status-changed.json` | Aanbod-status-gewijzigd | voorstel | IS-OA-05, IS-OA-06 | Nieuw, met de meldingssoort per koppeling op de componentpagina |
| `processing-status.json` | Verwerkingsstatus | vastgelegd | IS-OA-02, IS-OA-04 | De sleutels van de inname erin of ernaast |
| `result-structure.json` | Resultaatstructuur en examenplan | vastgelegd | IS-OA-01, IS-OA-02 | De formatieve wortel als enumwaarde erbij, dus additief |
| `room-type.json` | Onderwijslocatie type | voorstel | IS-OA-02 | Nieuw, met `locationIds` op `location.json` |
| `specification-reference.json` | Specificatie-referentie | vastgelegd | IS-OA-03 | Kopmetadata in de respons erbij, dus additief |
| `student-choice-rule.json` | Student keuze regel | voorstel | IS-OA-01, IS-OA-03 | Nieuw, in `rules` van `rule-set.json`: MINOR naast de vrije vorm en MAJOR bij dichtzetten |

`vastgelegd` staat voor een schema dat [Public](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen/schemas) draagt met het label alfa, `voorstel` voor een schema in deze map met een `$id` op `/voorstel`. Een voorstel wordt vastgelegd door het in Public op te nemen: de `$id` wisselt naar `/alfa` en de verwijzingen worden bestandsrelatief, wat additief is en daarmee MINOR ([versionering](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/regels.md)).

Een schema zonder eigen payload draagt de objecten waarnaar een ander schema wijst, en komt mee in diens validatie.

## Wat er naast de schema's bij komt

| Wat | Waar | Versie-impact |
|---|---|---|
| De paden en meldingen uit [de koppelvlakdiensten](../README.md#4-koppelvlakdiensten), met hun parameters en statuscodes | de componentpagina's, plus een nieuwe voor centraal aanmelden | Nieuwe endpoints |
| De meldingssoorten `ontwerp-gereed`, `aanbod-aanmeldbaar`, `aanmeldbaar-aanbod-beschikbaar` en `inrichtingsstatus` | de gesloten lijst `events` in `subscription.json` | MAJOR voor wie op die lijst valideert |
| Een stabiel `eventId` op elke melding, dat [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) voor herhaalbare verwerking vraagt | de eventschema's in Public | Optioneel MINOR, verplicht MAJOR |
| De diensten voor de inname en voor aanmeldbaar aanbod, met het gebruiksprofiel per koppeling eronder | de dienstenlijst en `gebruiksprofielen.md` | Nieuwe dienstpagina's |
| De Nederlandse naam per nieuwe sleutel, en het begrip levering als eenheid van aanname | `mapping.md` en de begrippenlijst | Geen schemawijziging |
| Een objecttype per verwijzing uit [S19](../signaleringen.md), met een definitie erbij | het informatiemodel en de begrippenlijst | Geen schemawijziging |

## Hoe een payload tegen haar schema loopt

Elke voorbeeldpayload in een interactiespecificatie noemt achter haar taalaanduiding de schema's waartegen zij valideert, zoals `schema=intake-outcome`. Twee namen achter elkaar staan voor een dragend schema met een overlay erop; de payload gaat dan tegen beide.

```bash
python3 tools/scripts/controleer-interactiespec.py
```

Dat haalt elke payload langs haar schema's en meldt elke sleutel die geen schema verklaart.
