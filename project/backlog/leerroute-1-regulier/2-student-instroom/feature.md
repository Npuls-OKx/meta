---
type: Feature
titel: "Interactieketen student-instroom: van aanmelding tot klaar voor de start"
ouder: ../epic.md
bestaand-issue: https://github.com/Npuls-OKx/meta/issues/386
schatting: 4 FTE-weken
streefdatum: 29 januari 2027
---

# Interactieketen student-instroom: van aanmelding tot klaar voor de start

## Waarde

Op de eerste lesdag is de student ingeschreven, geplaatst en geroosterd, en kennen studentkeuzesysteem, leeromgeving en studentvolgsysteem hem. Fase 3 en 4.

## Informatiestromen

- centraal aanmelden → kernregistratie: aanmelding en verbintenissen
- kernregistratie → studentkeuzesysteem en leeromgeving: verbintenis
- kernregistratie → planningssysteem: plaatsingsgroepen
- planningssysteem → roostersysteem → studentkeuzesysteem: leergelegenheden en rooster
- onderwijscatalogus → studentvolgsysteem: resultaatstructuur

## Gereed als

- [ ] elke stroom van deze keten in de regeltabel hoort bij een interactie, of staat met reden buiten scope
- [ ] de bevindingen uit de reviewsessies voor deze keten zijn verwerkt
- [ ] elke stroom heeft een koppelingspecificatie in Public; nu missen zes van de zeven die
- [ ] de koppelvlakspecificatie is uitgebracht met een eigen versie

## Draagt bij aan

- [feature-0030 Verbintenis als toestandsmachine per niveau](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0030)
- [feature-0033 Resultaatstructuur inrichten en resultaten registreren](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0033)

## Stories

1. [Besluit: plaatsingsgroep, planninggroep en lesgroep](01-besluit-plaatsingsgroep-planninggroep-en-lesgroep.md)
2. [Besluit: is het studentinformatiesysteem de orchestrator richting de leeromgeving](02-besluit-is-het-studentinformatiesysteem-de-orchestrator.md)
3. [Fase 3: aanmelding en inschrijving als status op een verbintenis](03-fase-3-aanmelding-en-inschrijving-als-status-op-een.md)
4. [Fase 3: lege plaatsingsgroepen vlak na de ontsluiting naar planning](04-fase-3-lege-plaatsingsgroepen-vlak-na-de-ontsluiting-naar.md)
5. [Fase 4: de resultaatstructuur gaat naar het studentvolgsysteem](05-fase-4-de-resultaatstructuur-gaat-naar-het.md)
6. [Fase 4: de lesgroep loopt via het studentkeuzesysteem naar de leeromgeving](06-fase-4-de-lesgroep-loopt-via-het-studentkeuzesysteem-naar.md)
7. [Signaleringen uit het concept besluiten](07-signaleringen-uit-het-concept-besluiten.md)
8. [De aanmelding de instelling in](08-de-aanmelding-de-instelling-in.md)
9. [De verbintenis naar het studentkeuzesysteem](09-de-verbintenis-naar-het-studentkeuzesysteem.md)
10. [Plaatsingsgroepen naar planning](10-plaatsingsgroepen-naar-planning.md)
11. [Roosteren van de leergelegenheden](11-roosteren-van-de-leergelegenheden.md)
12. [Het rooster naar het studentkeuzesysteem](12-het-rooster-naar-het-studentkeuzesysteem.md)
13. [De verbintenis naar de leeromgeving](13-de-verbintenis-naar-de-leeromgeving.md)
14. [De resultaatstructuur naar het studentvolgsysteem](14-de-resultaatstructuur-naar-het-studentvolgsysteem.md)
15. [Koppelvlakdiensten en applicatiecomponenten bijwerken](15-koppelvlakdiensten-en-applicatiecomponenten-bijwerken.md)
16. [Release: review en eerste versie uitbrengen](16-release-review-en-eerste-versie-uitbrengen.md)

## Bron

- [meta #386](https://github.com/Npuls-OKx/meta/issues/386)
- [Concept](https://github.com/Npuls-OKx/meta/pull/387)
- [Concept op de branch](https://github.com/Npuls-OKx/meta/blob/386-interactieketen-aanmelden-tot-start/architecture/docs/specificatie/interactieketen-student-instroom/README.md)
- [Regeltabel leerroute 1](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md)
