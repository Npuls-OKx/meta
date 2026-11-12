---
type: Feature
titel: "Interactieketen keuzedelen: kiezen en verwerken"
ouder: ../epic.md
bestaand-issue: https://github.com/Npuls-OKx/meta/issues/363
schatting: 4 FTE-weken
streefdatum:
---

# Interactieketen keuzedelen: kiezen en verwerken

## Waarde

De student kiest alleen wat voor hem kiesbaar is, met de reden bij wat afvalt. Zijn keuze landt als inschrijving bij planning, kernregistratie en catalogus. Fase 6.

## Informatiestromen

- kiesbaarheid, concept in meta PR #364: onderwijscatalogus, kernregistratie en studentvolgsysteem → studentkeuzesysteem, en de verwerkingsuitkomst terug naar de catalogus
- verwerking, zonder concept: studentkeuzesysteem → planningssysteem, planningssysteem → onderwijscatalogus en studentkeuzesysteem → kernregistratie
- variant capaciteitsgestuurd: planningssysteem → studentkeuzesysteem
- het verzoek tot aanbod voor een keuzedeel loopt via de keten onderwijsaanbod; een keuzedeel wordt behandeld als een opleiding

## Gereed als

- [ ] elke stroom van deze keten in de regeltabel hoort bij een interactie, of staat met reden buiten scope
- [ ] de bevindingen uit de reviewsessies voor deze keten zijn verwerkt
- [ ] kiesbaarheid en verwerking zijn allebei gespecificeerd
- [ ] de koppelvlakspecificatie is uitgebracht met een eigen versie

## Draagt bij aan

- [feature-0015 Haalbaarheid van keuze en ontwerp toetsen](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0015)
- [feature-0024 Kiesbaarheid bepalen](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0024)
- [feature-0025 Keuzecriteria als queryparameters op de aanbodquery](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0025)
- [feature-0026 Regelsets los van items, met min/max-keuzeregels](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0026)
- [feature-0027 Leeruitkomst-id's als verbindende sleutels in keuzeregels](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0027)
- [feature-0028 Regelsets versioneren voor verantwoording](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0028)
- [feature-0031 Keuze gescheiden van inschrijving en resultaat](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/features.md#feature-0031)

## Stories

1. [Besluit: de plek van het vastgestelde roostermoment](01-besluit-de-plek-van-het-vastgestelde-roostermoment.md)
2. [Besluit: de plek van de keuzeregelset](02-besluit-de-plek-van-de-keuzeregelset.md)
3. [Besluit: welk systeem het keuzemoment van een student start](03-besluit-welk-systeem-het-keuzemoment-van-een-student-start.md)
4. [Besluit: waarop de keuzeruimte wordt begrensd](04-besluit-waarop-de-keuzeruimte-wordt-begrensd.md)
5. [Fase 6: het keuzedeel als eigen specificatie in elke stap](05-fase-6-het-keuzedeel-als-eigen-specificatie-in-elke-stap.md)
6. [Specificatiestructuur, keuzeregelset en kiesbaar aanbod naar het studentkeuzesysteem](06-specificatiestructuur-keuzeregelset-en-kiesbaar-aanbod-naar.md)
7. [Studentcontext naar het studentkeuzesysteem](07-studentcontext-naar-het-studentkeuzesysteem.md)
8. [Behaalde leeruitkomsten naar het studentkeuzesysteem](08-behaalde-leeruitkomsten-naar-het-studentkeuzesysteem.md)
9. [Verwerkingsuitkomst terug naar de catalogus](09-verwerkingsuitkomst-terug-naar-de-catalogus.md)
10. [Keuzestelling naar planning](10-keuzestelling-naar-planning.md)
11. [Geactualiseerd aanbod naar de catalogus](11-geactualiseerd-aanbod-naar-de-catalogus.md)
12. [Keuzedeelverbintenis naar de kernregistratie](12-keuzedeelverbintenis-naar-de-kernregistratie.md)
13. [Variant capaciteitsgestuurd: geplande leergelegenheid naar het studentkeuzesysteem](13-variant-capaciteitsgestuurd-geplande-leergelegenheid-naar.md)
14. [Koppelvlakdiensten en applicatiecomponenten bijwerken](14-koppelvlakdiensten-en-applicatiecomponenten-bijwerken.md)
15. [Release: review en eerste versie uitbrengen](15-release-review-en-eerste-versie-uitbrengen.md)

## Bron

- [meta #363](https://github.com/Npuls-OKx/meta/issues/363)
- [Concept kiesbaarheid](https://github.com/Npuls-OKx/meta/pull/364)
- [Concept op de branch](https://github.com/Npuls-OKx/meta/blob/363-koppelvlak-keuzedeel-kiesbaar/architecture/docs/specificatie/koppelvlak-keuzedeel-kiesbaar/README.md)
- [Regeltabel leerroute 1](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md)
