# De opleiding van Jochem in het informatiemodel

Relateert aan: het kaderscenario leerroute 1 (persona Jochem, Apothekersassistent, cohort 2026) en het [informatiemodel OKx](informatiemodel.md). Gegenereerd uit `voorbeeld-lr1-regels.json`; gecontroleerd tegen `informatiemodel.json` op commit 0cf6e29 en `begrippen.json` op commit 8ebfaca.

## Leeswijzer

Dit document loopt stap voor stap door de instellingsreis van het kaderscenario en toont per stap wat er in het informatiemodel ontstaat en wat er tussen systemen beweegt, met de waarde voor Jochem erin. Het is een leeshulp op conceptueel niveau (MIM 1 en 2): geen payloads, geen endpoints, geen diensten. Eén instantie per objecttype toont het type, niet het aantal.

Vier termen, overal gelijk:

| Term | Betekenis |
|---|---|
| Objecttype | Element van de informatiemodelplaat (ArchiMate business object), met de plaatnaam letterlijk |
| Instantie | De waarde voor Jochem: een leesbare naam |
| Applicatiedienst | De ArchiMate-applicatiedienst op de hoofdplaat en in MORA; alleen context |
| Koppeling | Een pijl op hoofdplaat v1.7 tussen twee componenten; met de koppeling-ID uit Public waar die er is |

Twee soorten regels, in de vormtaal van de plaat:

- **Ontstaat**: een rol (geel, rolicoon) voert een processtap uit (geel, procesicoon) en daaruit ontstaan objecttypen (geel, objecticoon) met Jochems waarde. "Bestaat uit" is nesting; een relatielabel van de plaat staat tussen twee objecten of als verwijzing op een object dat aan een eerdere stap hangt. Een gestippelde rand is een aanname; grijs is een objecttype dat de plaat buiten de uitwisseling zet en dit voorbeeld toch meeneemt.
- **Stroomt** (blauwe rand): van welk systeem naar welk systeem gaat welk object, met de koppeling-ID of "zonder koppelingspecificatie", en de processtap waarna het gebeurt.

Koppeling-ID's op hoofdplaat v1.7: OC-P&R is Onderwijscatalogus naar Planningssysteem; OC-P&R is Planningssysteem naar Onderwijscatalogus; OC-SIS is Onderwijscatalogus naar Kernregistratie systeem studenten (KRS); OC-SIS is Onderwijscatalogus naar Student volg systeem (SVS); OC-LMS is Onderwijscatalogus naar Leer management systeem (LMS). Een pijl die op de hoofdplaat staat maar geen koppelingspecificatie heeft, staat als "zonder koppelingspecificatie"; een stroom uit het kaderscenario zonder pijl op de hoofdplaat staat als "geen pijl op de hoofdplaat".

De fasenamen zijn de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario. Het kaderscenario noemt fase 3 in de fasenlijst "Instroom, afstemming en plaatsing" en in de sectiekop "Instroom, intake en plaatsing"; hier geldt de sectiekop.

Wat hier staat is feedback, geen commitment: het voorbeeld beslist niets over het model. Per objecttype staan in de bijlage twee lege kolommen, "heet bij u" en "hangt bij u onder", voor wie het naast het eigen model legt.
## Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen

**Ontstaat:** `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces`, `Leeruitkomst`, `Opleiding specificatie`, `Opleidingsprogramma specificatie`, `Onderwijseenheid specificatie`, `Keuzedeelruimte`, `Keuzedeel`, `Student keuze regelset`, `Toetsonderdeel specificatie`, `Examenonderdeelspecificatie`. **MORA-hoofdproces:** Ontwikkelen.

Regels volgen na 30 september.

## Fase 2: Publiceren en planbaar maken

**Ontstaat:** `Verzoek tot Aanbod / Intekening op specificatie`, `Opleidingsaanbod van Instelling`, `Opleidingaanbod`, `Opleidingsprogramma aanbod`, `Cohort / periode`, `Onderwijseenheid aanbod`, `Leergelegenheid`, `Toetsgelegenheid`. **Stroomt:** Onderwijscatalogus naar Planningssysteem; Planningssysteem naar Onderwijscatalogus. **MORA-hoofdproces:** Plannen en roosteren.

![stroomt: Specificatie publiceren en planopgave doen](img/regels/f2-01-specificatie-publiceren-en-planopgave-doen.svg)

![ontstaat: Specificatie publiceren en planopgave doen](img/regels/f2-02-specificatie-publiceren-en-planopgave-doen.svg)

![ontstaat: Opleidingsaanbod maken](img/regels/f2-03-opleidingsaanbod-maken.svg)

![ontstaat: Onderwijseenheden en leergelegenheden plannen](img/regels/f2-04-onderwijseenheden-en-leergelegenheden-plannen.svg)

![stroomt: Aanbod publiceren](img/regels/f2-05-aanbod-publiceren.svg)

## Fase 3: Instroom, intake en plaatsing

**Ontstaat:** `Persoon`, `Aanmelding`, `Student`, `Opleiding aanbod verbintenis`, `Opleidingsprogramma aanbod verbintenis`, `Plaatsingsgroep`, `Inschrijving`. **Stroomt:** Onderwijscatalogus naar Voorziening Centraal Aanmelden (CAMBO); Voorziening Centraal Aanmelden (CAMBO) naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Informeren, aanmelden, intake en plaatsen.

![stroomt: Orienteren en aanmelden](img/regels/f3-06-orienteren-en-aanmelden.svg)

![ontstaat: Orienteren en aanmelden](img/regels/f3-07-orienteren-en-aanmelden.svg)

![stroomt: Orienteren en aanmelden](img/regels/f3-08-orienteren-en-aanmelden.svg)

![ontstaat: Intake en plaatsen](img/regels/f3-09-intake-en-plaatsen.svg)

![ontstaat: Inschrijving bevestigen](img/regels/f3-10-inschrijving-bevestigen.svg)

## Fase 4: Detailleren, roosteren en inschrijven

**Ontstaat:** `Leeronderdeel specificatie`, `Les specificatie`, `Summatieve resultaat structuur`, `Examenonderdeel weging`, `Summatief Afrondingscriterium`, `Leergelegenheid`, `Lesgelegenheid`, `Medewerker`, `Onderwijseenheid aanbod verbintenis`, `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis`, `Opleidingsprogramma aanbod verbintenis`. **Stroomt:** Onderwijscatalogus naar Leer management systeem (LMS); Onderwijscatalogus naar Student volg systeem (SVS); Kernregistratie systeem studenten (KRS) naar Planningssysteem; Planningssysteem naar Roostersysteem; Roostersysteem naar Kernregistratie systeem studenten (KRS); Kernregistratie systeem studenten (KRS) naar Leer management systeem (LMS). **MORA-hoofdproces:** Plannen en roosteren.

![ontstaat: Leeronderdelen detailleren](img/regels/f4-11-leeronderdelen-detailleren.svg)

![stroomt: LMS inrichten](img/regels/f4-12-lms-inrichten.svg)

![ontstaat: Resultaatstructuur inrichten](img/regels/f4-13-resultaatstructuur-inrichten.svg)

![stroomt: Resultaatstructuur inrichten](img/regels/f4-14-resultaatstructuur-inrichten.svg)

![stroomt: Groepen definieren](img/regels/f4-15-groepen-definieren.svg)

![stroomt: Periode 1 roosteren](img/regels/f4-16-periode-1-roosteren.svg)

![ontstaat: Periode 1 roosteren](img/regels/f4-17-periode-1-roosteren.svg)

![stroomt: Periode 1 roosteren](img/regels/f4-18-periode-1-roosteren.svg)

![ontstaat: Inschrijven op gelegenheden](img/regels/f4-19-inschrijven-op-gelegenheden.svg)

![stroomt: Inschrijven op gelegenheden](img/regels/f4-20-inschrijven-op-gelegenheden.svg)

## Fase 5: Onderwijs uitvoeren en voortgang begeleiden

**Ontstaat:** `Aanwezigheid`, `Lesgelegenheid resultaat`, `Leergelegenheid resultaat`, `Toetsgelegenheid verbintenis`, `Toetsgelegenheid resultaat`, `Formatief resultaat`, `Formatieve beoordeling`, `Formatieve resultaat structuur`, `Toetsonderdeel weging`, `Persoonlijke ontwikkeling`, `Onderwijseenheid resultaat`. **MORA-hoofdproces:** Verzorgen en begeleiden.

Regels volgen na 30 september.

## Fase 6: Organiseren van keuzemomenten

**Ontstaat:** `Keuzedeelaanbod`, `Keuzedeel aanbod verbintenis`, `Keuzedeel resultaat`. **MORA-hoofdproces:** Plannen en roosteren.

Regels volgen na 30 september.

## Fase 7: Bijsturen planning en aanbod

**Ontstaat:** geen nieuwe objecttypen; deze fase raakt bestaande objecttypen. **MORA-hoofdproces:** Plannen en roosteren.

Regels volgen na 30 september.

## Fase 8: Examineren, vaststellen en diplomeren

**Ontstaat:** `Examengelegenheid`, `Examengelegenheid verbintenis`, `Examengelegenheid resultaat`, `Summatief resultaat`, `Summatieve beoordeling`, `Opleidingsprogramma resultaat`, `Opleiding aanbod resultaat`, `Waarde document (diploma / certificaat)`. **MORA-hoofdproces:** Examens uitvoeren en vaststellen; diplomeren.

Regels volgen na 30 september.

## Bijlage: alle objecttypen per begrippenfamilie

Per objecttype de instantie voor Jochem, de fase waarin hij verschijnt, de status van de definitie in de begrippenlijst en het OEAPI-object uit de mapping. De laatste twee kolommen zijn voor de lezer.

### Kwalificatiekader mbo

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Kerntaak | regels volgen na 30 september | 1 |  | ja | geen equivalent | | |
| Kwalificatie | regels volgen na 30 september | 1 |  | ja | geen equivalent | | |
| Kwalificatie dossier | regels volgen na 30 september | 1 |  | ja | geen equivalent | | |
| Werkproces | regels volgen na 30 september | 1 |  | ja | geen equivalent | | |

### Onderwijskundig kader instelling

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Leeruitkomst | regels volgen na 30 september | 1 |  | ja | LearningOutcome | | |

### Onderwijsspecificatie

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examenonderdeelspecificatie | regels volgen na 30 september | 1 |  | ja | TestComponent | | |
| Keuzedeel | regels volgen na 30 september | 1 |  | nog te definieren | Programme | | |
| Keuzedeelruimte | regels volgen na 30 september | 1 |  | ja | Programme | | |
| Leeronderdeel specificatie | B1-K1-W1 Neemt de zorg-/adviesvraag in behandeling, lessenreeks Baliegesprek en triage | 4 |  | ja | LearningComponent | | |
| Les specificatie | Les 1 Introductie WHAM-vragen en triage, werkcollege, 2 uur | 4 |  | ja | LearningComponent | | |
| Onderwijseenheid specificatie | regels volgen na 30 september | 1 |  | ja | Course | | |
| Opleiding specificatie | regels volgen na 30 september | 1 |  | nog te definieren | Programme | | |
| Opleidingsprogramma specificatie | regels volgen na 30 september | 1 |  | ja | Programme | | |
| Student keuze regelset | regels volgen na 30 september | 1 |  | nog te definieren | geen equivalent | | |
| Toetsonderdeel specificatie | regels volgen na 30 september | 1 |  | ja | TestComponent | | |

### Onderwijsaanbod

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examengelegenheid | regels volgen na 30 september | 8 |  | ja | TestComponentOffering | | |
| Keuzedeelaanbod | regels volgen na 30 september | 6 |  | nog te definieren | ProgrammeOffering | | |
| Leergelegenheid | B1-K1-W1 Neemt de zorg-/adviesvraag in behandeling, periode 1 | 2 |  | nog te definieren | LearningComponentOffering | | |
| Lesgelegenheid | Les 1, maandag 1 september 09:00, simulatieruimte 2.14 | 4 |  | nog te definieren | LearningComponentOffering | | |
| Onderwijseenheid aanbod | B1-K1 Biedt farmaceutische patiëntenzorg, leerjaar 1 | 2 |  | nog te definieren | CourseOffering | | |
| Opleidingaanbod | Apothekersassistent 2026 | 2 |  | ja | ProgrammeOffering | | |
| Opleidingsaanbod van Instelling | ROC Het Voorbeeld | 2 | ja | ja | geen equivalent | | |
| Opleidingsprogramma aanbod | Regulier BOL 2026, 18 tot 120 studenten | 2 |  | nog te definieren | ProgrammeOffering | | |
| Toetsgelegenheid | Praktijktoets baliegesprek (OSCE), einde periode 1 | 2 |  | ja | TestComponentOffering | | |

### Onderwijsverbintenis

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examengelegenheid verbintenis | regels volgen na 30 september | 8 |  | ja | TestComponentOfferingAssociation | | |
| Inschrijving | Juni 2026 | 3 |  | ja | geen equivalent | | |
| Keuzedeel aanbod verbintenis | regels volgen na 30 september | 6 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Leergelegenheid verbintenis | Jochem op B1-K1-W1, periode 1 | 4 |  | nog te definieren | LearningComponentOfferingAssociation | | |
| Lesgelegenheid verbintenis | Jochem op les 1, 1 september 09:00 | 4 |  | nog te definieren | LearningComponentOfferingAssociation | | |
| Onderwijseenheid aanbod verbintenis | Jochem op B1-K1, leerjaar 1 | 4 |  | nog te definieren | CourseOfferingAssociation | | |
| Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026, aangemeld | 3 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026, aangemeld | 3 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Toetsgelegenheid verbintenis | regels volgen na 30 september | 5 |  | ja | TestComponentOfferingAssociation | | |

### Onderwijsresultaat

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Aanwezigheid | regels volgen na 30 september | 5 |  | nog te definieren | geen equivalent | | |
| Examengelegenheid resultaat | regels volgen na 30 september | 8 |  | nog te definieren | Result | | |
| Formatief resultaat | regels volgen na 30 september | 5 |  | ja | geen equivalent | | |
| Formatieve beoordeling | regels volgen na 30 september | 5 |  | ja | geen equivalent | | |
| Keuzedeel resultaat | regels volgen na 30 september | 6 |  | nog te definieren | Result | | |
| Leergelegenheid resultaat | regels volgen na 30 september | 5 |  | nog te definieren | Result | | |
| Lesgelegenheid resultaat | regels volgen na 30 september | 5 |  | nog te definieren | Result | | |
| Onderwijseenheid resultaat | regels volgen na 30 september | 5 |  | nog te definieren | Result | | |
| Opleiding aanbod resultaat | regels volgen na 30 september | 8 |  | nog te definieren | Result | | |
| Opleidingsprogramma resultaat | regels volgen na 30 september | 8 |  | nog te definieren | Result | | |
| Summatief resultaat | regels volgen na 30 september | 8 |  | ja | geen equivalent | | |
| Summatieve beoordeling | regels volgen na 30 september | 8 |  | ja | geen equivalent | | |
| Toetsgelegenheid resultaat | regels volgen na 30 september | 5 |  | nog te definieren | Result | | |

### Resultaatstructuur

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examenonderdeel weging | Proeve van bekwaamheid B1-K1: weging 2 | 4 | ja | nog te definieren | geen equivalent | | |
| Formatieve resultaat structuur | regels volgen na 30 september | 5 |  | ja | geen equivalent | | |
| Persoonlijke ontwikkeling | regels volgen na 30 september | 5 |  | nog te definieren | geen equivalent | | |
| Summatief Afrondingscriterium | Alle kerntaken en de keuzedelen voldoende | 4 |  | nog te definieren | geen equivalent | | |
| Summatieve resultaat structuur | Examenplan Apothekersassistent, alle onderdelen voldoende | 4 |  | ja | geen equivalent | | |
| Toetsonderdeel weging | regels volgen na 30 september | 5 |  | nog te definieren | geen equivalent | | |

### Buiten de kolommen (persoon, groep, cohort, verzoek)

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Aanmelding | April 2026, Apothekersassistent BOL | 3 |  | ja | geen equivalent | | |
| Cohort / periode | Cohort 2026 | 2 |  | ja | geen equivalent | | |
| Medewerker | Docent, personeelsnummer 4711 | 4 |  | ja | geen equivalent | | |
| Persoon | Jochem, 17, na het vmbo | 3 |  | nog te definieren | Person | | |
| Plaatsingsgroep | APO26-1A | 3 | ja | nog te definieren | Group | | |
| Student | Jochem, cohort 2026 | 3 |  | ja | geen equivalent | | |
| Verzoek tot Aanbod / Intekening op specificatie | Planopgave Apothekersassistent, cohort 2026 | 2 | ja | ja | geen equivalent | | |
| Waarde document (diploma / certificaat) | regels volgen na 30 september | 8 |  | ja | geen equivalent | | |

## Vragen aan de kerngroep

De vragen die de regels zelf oproepen, met de regel waar de vraag zichtbaar wordt. Feedback, geen commitment.

1. Is het verzoek tot aanbod een object met sleutel en toestand, of het startevent van aanbod maken? (fase 2, Specificatie publiceren en planopgave doen, `Verzoek tot Aanbod / Intekening op specificatie`)
2. Is het cohort een sleutel op aanbod en verbintenis, of een eigen object (ontwerpkeuze 17)? (fase 2, Opleidingsaanbod maken, `Cohort / periode`)
3. Welke groep bij de instelling is de bron van de plaatsingsgroep: stamgroep (KRS), planninggroep of lesgroep (meta #235)? (fase 3, Intake en plaatsen, `Plaatsingsgroep`)
4. Is de inschrijving een eigen object naast de verbintenis, of een toestand van de aanmelding (ontwerpkeuze 13)? (fase 3, Inschrijving bevestigen, `Inschrijving`)
5. Welke weging moet een studentvolgsysteem aggregeren: op het toetsonderdeel (schema) of op de resultaateenheid (regels)? Meta #234 punt 5. (fase 4, Resultaatstructuur inrichten, `Examenonderdeel weging`)
6. De hoofdplaat wisselt lesgelegenheden uit, ontwerpkeuze 8 zet de leslaag buiten de uitwisseling. Herkent de kerngroep deze stroom? (fase 4, Periode 1 roosteren, `Lesgelegenheid`)
7. Rijpt een verbintenis mee met het aanbod (planbaar naar geroosterd), of is de toestand van de verbintenis los van die van het aanbod (ontwerpkeuze 13)? (fase 4, Inschrijven op gelegenheden, `Opleidingsprogramma aanbod verbintenis`)

Vragen over patronen, schema's, de toetslijst en endpoints horen bij de koppelvlakspecificatie en staan hier niet.

### Invulblad

Per regel één van vier antwoorden: herken ik dit; heet bij ons anders (welke term); hangt bij ons anders (waaronder); ontbreekt.

| Fase | Stap | Objecttype | Herken | Heet anders | Hangt anders | Ontbreekt |
|---|---|---|---|---|---|---|
| 2 | Specificatie publiceren en planopgave doen | Verzoek tot Aanbod / Intekening op specificatie | | | | |
| 2 | Opleidingsaanbod maken | Opleidingsaanbod van Instelling | | | | |
| 2 | Opleidingsaanbod maken | Opleidingaanbod | | | | |
| 2 | Opleidingsaanbod maken | Opleidingsprogramma aanbod | | | | |
| 2 | Opleidingsaanbod maken | Cohort / periode | | | | |
| 2 | Onderwijseenheden en leergelegenheden plannen | Onderwijseenheid aanbod | | | | |
| 2 | Onderwijseenheden en leergelegenheden plannen | Leergelegenheid | | | | |
| 2 | Onderwijseenheden en leergelegenheden plannen | Toetsgelegenheid | | | | |
| 3 | Orienteren en aanmelden | Persoon | | | | |
| 3 | Orienteren en aanmelden | Aanmelding | | | | |
| 3 | Intake en plaatsen | Student | | | | |
| 3 | Intake en plaatsen | Opleiding aanbod verbintenis | | | | |
| 3 | Intake en plaatsen | Opleidingsprogramma aanbod verbintenis | | | | |
| 3 | Intake en plaatsen | Plaatsingsgroep | | | | |
| 3 | Inschrijving bevestigen | Inschrijving | | | | |
| 4 | Leeronderdelen detailleren | Leeronderdeel specificatie | | | | |
| 4 | Leeronderdelen detailleren | Les specificatie | | | | |
| 4 | Resultaatstructuur inrichten | Summatieve resultaat structuur | | | | |
| 4 | Resultaatstructuur inrichten | Examenonderdeel weging | | | | |
| 4 | Resultaatstructuur inrichten | Summatief Afrondingscriterium | | | | |
| 4 | Periode 1 roosteren | Leergelegenheid | | | | |
| 4 | Periode 1 roosteren | Lesgelegenheid | | | | |
| 4 | Periode 1 roosteren | Medewerker | | | | |
| 4 | Inschrijven op gelegenheden | Onderwijseenheid aanbod verbintenis | | | | |
| 4 | Inschrijven op gelegenheden | Leergelegenheid verbintenis | | | | |
| 4 | Inschrijven op gelegenheden | Lesgelegenheid verbintenis | | | | |
| 4 | Inschrijven op gelegenheden | Opleidingsprogramma aanbod verbintenis | | | | |

