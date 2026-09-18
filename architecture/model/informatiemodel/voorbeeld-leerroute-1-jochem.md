# De opleiding van Jochem in het informatiemodel

Relateert aan: het [kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md) (persona Jochem, Apothekersassistent, cohort 2026), het architectuurkader van OKx, en het [informatiemodel OKx](informatiemodel.md). Gegenereerd uit `voorbeeld-lr1-regels.json`; gecontroleerd tegen `informatiemodel.json` op commit 0cf6e29 en `begrippen.json` op commit 8ebfaca.

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

Een **verdieping** (zelfde rol en stap, met "verdieping" op de processtap) zoomt in op een regel erboven. Een verdieping met een gestippelde rand en de chip "conceptplaat: Informatiemodel Onderwijsontwerp" put uit de conceptplaat in het ArchiMate-model: zij laat zien waar de informatiemodelplaat kan groeien en telt niet mee in de bijlage en het invulblad.

Koppeling-ID's op hoofdplaat v1.7: OC-P&R is Onderwijscatalogus naar Planningssysteem; OC-P&R is Planningssysteem naar Onderwijscatalogus; OC-SIS is Onderwijscatalogus naar Kernregistratie systeem studenten (KRS); OC-SIS is Onderwijscatalogus naar Student volg systeem (SVS); OC-LMS is Onderwijscatalogus naar Leer management systeem (LMS). Een pijl die op de hoofdplaat staat maar geen koppelingspecificatie heeft, staat als "zonder koppelingspecificatie"; een stroom uit het kaderscenario zonder pijl op de hoofdplaat staat als "geen pijl op de hoofdplaat".

De fasenamen zijn de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario. Het kaderscenario noemt fase 3 in de fasenlijst "Instroom, afstemming en plaatsing" en in de sectiekop "Instroom, intake en plaatsing"; hier geldt de sectiekop.

Wat hier staat is feedback, geen commitment: het voorbeeld beslist niets over het model. Per objecttype staan in de bijlage twee lege kolommen, "heet bij u" en "hangt bij u onder", voor wie het naast het eigen model legt.
## Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen

De fase in detail: [kaderscenario leerroute 1, fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen).

**Ontstaat:** `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces`, `Examenplan`, `Summatieve resultaat structuur`, `Cohort / periode`, `Leeruitkomst`, `Competenties / Skills`, `Vaardigheid`, `Kennis`, `Inzicht`, `Opleiding specificatie`, `Opleidingsprogramma specificatie`, `Onderwijseenheid specificatie`, `Leeronderdeel specificatie`, `Keuzedeelruimte`, `Keuzedeel`, `Student keuze regelset`, `Toetsonderdeel specificatie`, `Examenonderdeelspecificatie`, `Examenonderdeel weging`, `Summatief Afrondingscriterium`. **Stroomt:** Curriculum ontwerptool naar Onderwijscatalogus. **MORA-hoofdproces:** Ontwikkelen.

![ontstaat: Kwalificatiedossier analyseren](img/regels/f1-01-kwalificatiedossier-analyseren.svg)

![ontstaat: Examenplan vaststellen](img/regels/f1-02-examenplan-vaststellen.svg)

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten](img/regels/f1-03-kwalificatiedossier-vertalen-naar-leeruitkomsten.svg)

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: kerntaak onderwijskundig vertaald](img/regels/f1-04-kwalificatiedossier-vertalen-naar-leeruitkomsten-verdieping.svg)

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: leeruitkomst naar skills](img/regels/f1-05-kwalificatiedossier-vertalen-naar-leeruitkomsten-verdieping.svg)

![ontstaat: Opleidingsspecificatie met programma en eenheden beschrijven](img/regels/f1-06-opleidingsspecificatie-met-programma-en-eenheden-beschrijven.svg)

![ontstaat: Toetsonderdelen en resultaatstructuur uit het examenplan afleiden](img/regels/f1-07-toetsonderdelen-en-resultaatstructuur-uit-het-examenplan-afleiden.svg)

![stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus](img/regels/f1-08-grofmazig-resultaat-publiceren-naar-de-onderwijscatalogus.svg)

## Fase 2: Publiceren en planbaar maken

De fase in detail: [kaderscenario leerroute 1, fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken).

**Ontstaat:** `Opleidingsprogramma specificatie`, `Verzoek tot Aanbod / Intekening op specificatie`, `Opleidingsaanbod van Instelling`, `Opleidingaanbod`, `Opleidingsprogramma aanbod`, `Onderwijseenheid aanbod`, `Leergelegenheid`, `Toetsgelegenheid`. **Stroomt:** Onderwijscatalogus naar Planningssysteem; Planningssysteem naar Onderwijscatalogus. **MORA-hoofdproces:** Plannen en roosteren.

![ontstaat: Specificatie aanvullen tot planbare specificatie](img/regels/f2-09-specificatie-aanvullen-tot-planbare-specificatie.svg)

![ontstaat: Planningssysteem verzoeken om onderwijsaanbod](img/regels/f2-10-planningssysteem-verzoeken-om-onderwijsaanbod.svg)

![stroomt: Planningssysteem verzoeken om onderwijsaanbod](img/regels/f2-11-planningssysteem-verzoeken-om-onderwijsaanbod.svg)

![ontstaat: Haalbaarheid bepalen en aanbod plannen](img/regels/f2-12-haalbaarheid-bepalen-en-aanbod-plannen.svg)

![stroomt: Gepland aanbod terugleveren aan de onderwijscatalogus](img/regels/f2-13-gepland-aanbod-terugleveren-aan-de-onderwijscatalogus.svg)

## Fase 3: Instroom, intake en plaatsing

De fase in detail: [kaderscenario leerroute 1, fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing).

**Ontstaat:** `Persoon`, `Aanmelding`, `Student`, `Opleiding aanbod verbintenis`, `Opleidingsprogramma aanbod verbintenis`, `Plaatsingsgroep`, `Inschrijving`. **Stroomt:** Onderwijscatalogus naar Voorziening Centraal Aanmelden (CAMBO); Voorziening Centraal Aanmelden (CAMBO) naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Informeren, aanmelden, intake en plaatsen.

![stroomt: Orienteren op het gepubliceerde aanbod](img/regels/f3-14-orienteren-op-het-gepubliceerde-aanbod.svg)

![ontstaat: Aanmelden via het intakesysteem](img/regels/f3-15-aanmelden-via-het-intakesysteem.svg)

![stroomt: Aanmelden via het intakesysteem](img/regels/f3-16-aanmelden-via-het-intakesysteem.svg)

![ontstaat: Intake doorlopen en plaatsen](img/regels/f3-17-intake-doorlopen-en-plaatsen.svg)

![ontstaat: Persoon en verbintenissen vastleggen in de kernregistratie](img/regels/f3-18-persoon-en-verbintenissen-vastleggen-in-de-kernregistratie.svg)

## Fase 4: Detailleren, roosteren en inschrijven

De fase in detail: [kaderscenario leerroute 1, fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven).

**Ontstaat:** `Leeronderdeel specificatie`, `Les specificatie`, `Leergelegenheid`, `Lesgelegenheid`, `Medewerker`, `Onderwijseenheid aanbod verbintenis`, `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis`, `Opleidingsprogramma aanbod verbintenis`. **Stroomt:** Onderwijscatalogus naar Leer management systeem (LMS); Onderwijscatalogus naar Student volg systeem (SVS); Kernregistratie systeem studenten (KRS) naar Planningssysteem; Planningssysteem naar Roostersysteem; Roostersysteem naar Kernregistratie systeem studenten (KRS); Kernregistratie systeem studenten (KRS) naar Leer management systeem (LMS). **MORA-hoofdproces:** Plannen en roosteren.

![ontstaat: Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken](img/regels/f4-19-leeronderdeel-en-toetsonderdeelspecificaties-fijnmazig-uitwerken.svg)

![stroomt: Detailspecificaties leveren aan het LMS](img/regels/f4-20-detailspecificaties-leveren-aan-het-lms.svg)

![stroomt: Detailspecificaties leveren aan het LMS](img/regels/f4-21-detailspecificaties-leveren-aan-het-lms.svg)

![stroomt: Plaatsings- en planninggroepen definieren en aan personen koppelen](img/regels/f4-22-plaatsings-en-planninggroepen-definieren-en-aan-personen-koppelen.svg)

![stroomt: Te roosteren specificaties aan het roostersysteem geven](img/regels/f4-23-te-roosteren-specificaties-aan-het-roostersysteem-geven.svg)

![ontstaat: Leer-, les- en toetsgelegenheden roosteren](img/regels/f4-24-leer-les-en-toetsgelegenheden-roosteren.svg)

![stroomt: Leer-, les- en toetsgelegenheden roosteren](img/regels/f4-25-leer-les-en-toetsgelegenheden-roosteren.svg)

![ontstaat: Verwachte deelnemers delen en toegang geven](img/regels/f4-26-verwachte-deelnemers-delen-en-toegang-geven.svg)

![stroomt: Verwachte deelnemers delen en toegang geven](img/regels/f4-27-verwachte-deelnemers-delen-en-toegang-geven.svg)

## Fase 5: Onderwijs uitvoeren en voortgang begeleiden

De fase in detail: [kaderscenario leerroute 1, fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden).

**Ontstaat:** `Lesgelegenheid verbintenis`, `Aanwezigheid`, `Lesgelegenheid resultaat`, `Toetsgelegenheid verbintenis`, `Formatieve resultaat structuur`, `Toetsonderdeel weging`, `Toetsgelegenheid resultaat`, `Formatief resultaat`, `Formatieve beoordeling`, `Persoonlijke ontwikkeling`, `Leergelegenheid resultaat`, `Onderwijseenheid resultaat`. **Stroomt:** Leer management systeem (LMS) naar Student volg systeem (SVS). **MORA-hoofdproces:** Verzorgen en begeleiden.

![ontstaat: Onderwijs verzorgen](img/regels/f5-28-onderwijs-verzorgen.svg)

![ontstaat: Toetsmomenten plannen tijdens lessen](img/regels/f5-29-toetsmomenten-plannen-tijdens-lessen.svg)

![ontstaat: Formatieve voortgang bijhouden](img/regels/f5-30-formatieve-voortgang-bijhouden.svg)

![stroomt: Formatieve voortgang bijhouden](img/regels/f5-31-formatieve-voortgang-bijhouden.svg)

![ontstaat: Studiebeeld volgen in het studentvolgsysteem](img/regels/f5-32-studiebeeld-volgen-in-het-studentvolgsysteem.svg)

## Fase 6: Organiseren van keuzemomenten

De fase in detail: [kaderscenario leerroute 1, fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten).

**Ontstaat:** `Keuzedeelaanbod`, `Keuzedeel aanbod verbintenis`. **Stroomt:** Onderwijscatalogus naar Student Keuze Systeem (SKS); Student Keuze Systeem (SKS) naar Planningssysteem; Planningssysteem naar Onderwijscatalogus; Student Keuze Systeem (SKS) naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Plannen en roosteren.

![ontstaat: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem](img/regels/f6-33-keuzedeelaanbod-ontsluiten-naar-het-studentkeuzesysteem.svg)

![stroomt: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem](img/regels/f6-34-keuzedeelaanbod-ontsluiten-naar-het-studentkeuzesysteem.svg)

![ontstaat: Voorkeurslijst samenstellen in het studentkeuzesysteem](img/regels/f6-35-voorkeurslijst-samenstellen-in-het-studentkeuzesysteem.svg)

![stroomt: Voorkeurslijst samenstellen in het studentkeuzesysteem](img/regels/f6-36-voorkeurslijst-samenstellen-in-het-studentkeuzesysteem.svg)

![ontstaat: Definitieve keuzes verwerken naar groepen en capaciteit](img/regels/f6-37-definitieve-keuzes-verwerken-naar-groepen-en-capaciteit.svg)

![stroomt: Planbaar aanbod actualiseren](img/regels/f6-38-planbaar-aanbod-actualiseren.svg)

![ontstaat: Keuzedeel formeel inschrijven](img/regels/f6-39-keuzedeel-formeel-inschrijven.svg)

![stroomt: Keuzedeel formeel inschrijven](img/regels/f6-40-keuzedeel-formeel-inschrijven.svg)

## Fase 7: Bijsturen planning en aanbod

De fase in detail: [kaderscenario leerroute 1, fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod).

**Ontstaat:** `Plaatsingsgroep`, `Onderwijseenheid aanbod verbintenis`, `Onderwijseenheid aanbod`. **Stroomt:** Kernregistratie systeem studenten (KRS) naar Planningssysteem; Planningssysteem naar Onderwijscatalogus; Planningssysteem naar Roostersysteem. **MORA-hoofdproces:** Plannen en roosteren.

![ontstaat: Afwijkingen verzamelen in een planninggroep](img/regels/f7-41-afwijkingen-verzamelen-in-een-planninggroep.svg)

![ontstaat: Bestaande verbintenissen annuleren](img/regels/f7-42-bestaande-verbintenissen-annuleren.svg)

![stroomt: Bestaande verbintenissen annuleren](img/regels/f7-43-bestaande-verbintenissen-annuleren.svg)

![ontstaat: Nieuw aanbod maken en publiceren](img/regels/f7-44-nieuw-aanbod-maken-en-publiceren.svg)

![stroomt: Nieuw aanbod maken en publiceren](img/regels/f7-45-nieuw-aanbod-maken-en-publiceren.svg)

![stroomt: Nieuw aanbod maken en publiceren](img/regels/f7-46-nieuw-aanbod-maken-en-publiceren.svg)

## Fase 8: Examineren, vaststellen en diplomeren

De fase in detail: [kaderscenario leerroute 1, fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren).

**Ontstaat:** `Examengelegenheid`, `Examengelegenheid verbintenis`, `Examengelegenheid resultaat`, `Summatief resultaat`, `Summatieve beoordeling`, `Opleidingsprogramma resultaat`, `Keuzedeel resultaat`, `Opleiding aanbod resultaat`, `Waarde document (diploma / certificaat)`. **Stroomt:** Toets- en examen afname systeem naar Student volg systeem (SVS); Student volg systeem (SVS) naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Examens uitvoeren en vaststellen; diplomeren.

![ontstaat: Examenspecificaties omzetten in examengelegenheden](img/regels/f8-47-examenspecificaties-omzetten-in-examengelegenheden.svg)

![ontstaat: Kandidatenlijsten samenstellen](img/regels/f8-48-kandidatenlijsten-samenstellen.svg)

![ontstaat: Zitting uitvoeren en resultaten doorgeven](img/regels/f8-49-zitting-uitvoeren-en-resultaten-doorgeven.svg)

![stroomt: Zitting uitvoeren en resultaten doorgeven](img/regels/f8-50-zitting-uitvoeren-en-resultaten-doorgeven.svg)

![ontstaat: Summatief vaststellen](img/regels/f8-51-summatief-vaststellen.svg)

![stroomt: Summatief vaststellen](img/regels/f8-52-summatief-vaststellen.svg)

![ontstaat: Kwalificering en diplomering registreren](img/regels/f8-53-kwalificering-en-diplomering-registreren.svg)

## Bijlage: alle objecttypen per begrippenfamilie

Per objecttype de instantie voor Jochem, de fase waarin hij verschijnt, de status van de definitie in de begrippenlijst en het OEAPI-object uit de mapping. De laatste twee kolommen zijn voor de lezer.

### Kwalificatiekader mbo

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Kerntaak | B1-K1 Biedt farmaceutische patiëntenzorg | 1 |  | ja | geen equivalent | | |
| Kwalificatie | Apothekersassistent, 27141 | 1 |  | ja | geen equivalent | | |
| Kwalificatie dossier | Apothekersassistent, crebo 23450 | 1 |  | ja | geen equivalent | | |
| Werkproces | B1-K1-W1 Neemt de zorg-/adviesvraag in behandeling | 1 |  | ja | geen equivalent | | |

### Onderwijskundig kader instelling

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Competenties / Skills | Vaardigheden bij deze leeruitkomst (CompetentNL) | 1 | ja | nog te definieren | geen equivalent | | |
| Inzicht | Werking en risico van een geneesmiddel bij de vraag aan de balie | 1 | ja | nog te definieren | geen equivalent | | |
| Kennis | Farmacie (CompetentNL kennisgebied op ISCED-F 0916) | 1 | ja | nog te definieren | geen equivalent | | |
| Leeruitkomst | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving (kerntaakniveau) | 1 | ja | ja | LearningOutcome | | |
| Vaardigheid | Communicatieve vaardigheden (CompetentNL laag 2) | 1 | ja | nog te definieren | geen equivalent | | |

### Onderwijsspecificatie

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examenonderdeelspecificatie | Proeve van bekwaamheid B1-K1 | 1 | ja | ja | TestComponent | | |
| Keuzedeel | Ondernemerschap in de zorg | 1 |  | nog te definieren | Programme | | |
| Keuzedeelruimte | 720 SBU, mbo-4 | 1 |  | ja | Programme | | |
| Leeronderdeel specificatie | B1-K1-W1 Baliegesprek en triage: simulatie in de leerapotheek, theorie ondersteunend, grofmazig | 1 |  | ja | LearningComponent | | |
| Les specificatie | Les 1 Introductie WHAM-vragen en triage, werkcollege, 2 uur | 4 |  | ja | LearningComponent | | |
| Onderwijseenheid specificatie | Blok B1-K1 Biedt farmaceutische patiëntenzorg | 1 |  | ja | Course | | |
| Opleiding specificatie | Apothekersassistent, versie 2026.1 | 1 |  | nog te definieren | Programme | | |
| Opleidingsprogramma specificatie | BOL voltijd, diplomaprogramma | 1 |  | ja | Programme | | |
| Student keuze regelset | Kiesbare keuzedelen voor Apothekersassistent | 1 |  | nog te definieren | geen equivalent | | |
| Toetsonderdeel specificatie | Praktijktoets baliegesprek (OSCE), summatief | 1 |  | ja | TestComponent | | |

### Onderwijsaanbod

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examengelegenheid | Proeve van bekwaamheid B1-K1, periode 12 | 8 | ja | ja | TestComponentOffering | | |
| Keuzedeelaanbod | Ondernemerschap in de zorg, periode 7, locatie A | 6 | ja | nog te definieren | ProgrammeOffering | | |
| Leergelegenheid | B1-K1-W1, periode 1, planbaar | 2 |  | nog te definieren | LearningComponentOffering | | |
| Lesgelegenheid | Les 1, maandag 1 september 09:00, simulatieruimte 2.14 | 4 |  | nog te definieren | LearningComponentOffering | | |
| Onderwijseenheid aanbod | B1-K1, leerjaar 1 | 2 |  | nog te definieren | CourseOffering | | |
| Opleidingaanbod | Apothekersassistent 2026 | 2 |  | ja | ProgrammeOffering | | |
| Opleidingsaanbod van Instelling | ROC Het Voorbeeld | 2 | ja | ja | geen equivalent | | |
| Opleidingsprogramma aanbod | Regulier BOL 2026, 18 tot 120 studenten | 2 |  | nog te definieren | ProgrammeOffering | | |
| Toetsgelegenheid | Praktijktoets baliegesprek (OSCE), einde periode 1, planbaar | 2 |  | ja | TestComponentOffering | | |

### Onderwijsverbintenis

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examengelegenheid verbintenis | Jochem op de proeve, periode 12 | 8 |  | ja | TestComponentOfferingAssociation | | |
| Inschrijving | Juni 2026 | 3 |  | ja | geen equivalent | | |
| Keuzedeel aanbod verbintenis | Jochem op Ondernemerschap in de zorg, periode 7 (voorkeur 1) | 6 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Leergelegenheid verbintenis | Jochem op B1-K1-W1, periode 1 | 4 |  | nog te definieren | LearningComponentOfferingAssociation | | |
| Lesgelegenheid verbintenis | Jochem op les 1, 1 september 09:00 | 4 |  | nog te definieren | LearningComponentOfferingAssociation | | |
| Onderwijseenheid aanbod verbintenis | Jochem op B1-K1, leerjaar 1 | 4 |  | nog te definieren | CourseOfferingAssociation | | |
| Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026, aangemeld | 3 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026, aangemeld | 3 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Toetsgelegenheid verbintenis | Jochem op de OSCE, einde periode 1 | 5 |  | ja | TestComponentOfferingAssociation | | |

### Onderwijsresultaat

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Aanwezigheid | Aanwezig, les 1 | 5 |  | nog te definieren | geen equivalent | | |
| Examengelegenheid resultaat | Proeve B1-K1: voldoende | 8 |  | nog te definieren | Result | | |
| Formatief resultaat | Quiz WHAM-vragen: 8 van 10 | 5 | ja | ja | geen equivalent | | |
| Formatieve beoordeling | Op koers voor B1-K1-W1 | 5 | ja | ja | geen equivalent | | |
| Keuzedeel resultaat | Ondernemerschap in de zorg: voldoende | 8 |  | nog te definieren | Result | | |
| Leergelegenheid resultaat | B1-K1-W1 afgerond, periode 1 | 5 |  | nog te definieren | Result | | |
| Lesgelegenheid resultaat | Les 1 gevolgd | 5 |  | nog te definieren | Result | | |
| Onderwijseenheid resultaat | B1-K1: in uitvoering | 5 |  | nog te definieren | Result | | |
| Opleiding aanbod resultaat | Apothekersassistent 2026: gediplomeerd | 8 |  | nog te definieren | Result | | |
| Opleidingsprogramma resultaat | Regulier BOL 2026: alle kerntaken en keuzedelen voldoende | 8 |  | nog te definieren | Result | | |
| Summatief resultaat | B1-K1: voldoende, vastgesteld | 8 |  | ja | geen equivalent | | |
| Summatieve beoordeling | Examencommissie, juni 2029 | 8 | ja | ja | geen equivalent | | |
| Toetsgelegenheid resultaat | OSCE: voldoende | 5 |  | nog te definieren | Result | | |

### Resultaatstructuur

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Examenonderdeel weging | Proeve van bekwaamheid B1-K1: weging 2 | 1 | ja | nog te definieren | geen equivalent | | |
| Formatieve resultaat structuur | Voortgang B1-K1-W1: quiz WHAM-vragen, rollenspel | 5 | ja | ja | geen equivalent | | |
| Persoonlijke ontwikkeling | Jochems ontwikkeling in periode 1 | 5 | ja | nog te definieren | geen equivalent | | |
| Summatief Afrondingscriterium | Alle kerntaken en de keuzedelen voldoende | 1 |  | nog te definieren | geen equivalent | | |
| Summatieve resultaat structuur | Eerste opzet: kerntaken en keuzedelen, alle voldoende | 1 | ja | ja | geen equivalent | | |
| Toetsonderdeel weging | Quiz WHAM-vragen: weging 1 | 5 | ja | nog te definieren | geen equivalent | | |

### Buiten de kolommen (persoon, groep, cohort, verzoek)

| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|
| Aanmelding | April 2026, Apothekersassistent BOL | 3 |  | ja | geen equivalent | | |
| Cohort / periode | Cohort 2026 | 1 |  | ja | geen equivalent | | |
| Examenplan | Examenplan Apothekersassistent, cohort 2026 | 1 | ja | ja | geen equivalent | | |
| Medewerker | Docent, personeelsnummer 4711 | 4 |  | ja | geen equivalent | | |
| Persoon | Jochem, 17, na het vmbo | 3 |  | nog te definieren | Person | | |
| Plaatsingsgroep | APO26-1A | 3 | ja | nog te definieren | Group | | |
| Student | Jochem, cohort 2026 | 3 |  | ja | geen equivalent | | |
| Verzoek tot Aanbod / Intekening op specificatie | Planopgave Apothekersassistent, cohort 2026 | 2 | ja | ja | geen equivalent | | |
| Waarde document (diploma / certificaat) | Diploma Apothekersassistent, juli 2029 | 8 |  | ja | geen equivalent | | |

## Vragen aan de kerngroep

De vragen die de regels zelf oproepen, met de regel waar de vraag zichtbaar wordt. Feedback, geen commitment.

1. Het kaderscenario zet het examenplan in fase 1 en de resultaatstructuur pas in fase 4 bij OC-SIS. Ontstaat de summatieve resultaatstructuur in de curriculum-ontwerptool uit het examenplan, en gaat zij met de specificatie mee naar de catalogus? (fase 1, Examenplan vaststellen, `Examenplan`)
2. Is het cohort een sleutel op aanbod en verbintenis, of een eigen object dat de toepasselijke resultaatstructuur draagt (ontwerpkeuze 17)? (fase 1, Examenplan vaststellen, `Cohort / periode`)
3. Het kader waarmee de instelling de kerntaak vormgeeft staat op de conceptplaat (leervormstrategie, leerdoel, onderwijsvorm specificatie, leeromgeving), niet op de informatiemodelplaat. Welke daarvan horen in de uitwisseling, bijvoorbeeld leervorm en leeromgeving op het leeronderdeel, en welke blijven binnen de instelling? (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten, `Onderwijsvorm specificatie`)
4. CompetentNL legt vaardigheden gelaagd vast (skos:broader, drie lagen) en de leeruitkomst is op de plaat gelaagd; Vaardigheid is dat niet. Krijgt Vaardigheid een eigen aggregatie, zodat laag 2 onder laag 1 hangt zoals de leeruitkomst onder de leeruitkomst? (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten, `Vaardigheid`)
5. Welke weging moet een studentvolgsysteem aggregeren: op het toetsonderdeel (schema) of op de resultaateenheid (regels)? Meta #234 punt 5. (fase 1, Toetsonderdelen en resultaatstructuur uit het examenplan afleiden, `Examenonderdeel weging`)
6. Is het verzoek tot aanbod een object met sleutel en toestand, of het startevent van aanbod maken? (fase 2, Planningssysteem verzoeken om onderwijsaanbod, `Verzoek tot Aanbod / Intekening op specificatie`)
7. Welke groep bij de instelling is de bron van de plaatsingsgroep: stamgroep (KRS), planninggroep of lesgroep (meta #235)? (fase 3, Intake doorlopen en plaatsen, `Plaatsingsgroep`)

Vragen over patronen, schema's, de toetslijst en endpoints horen bij de koppelvlakspecificatie en staan hier niet.

### Invulblad

Per regel één van vier antwoorden: herken ik dit; heet bij ons anders (welke term); hangt bij ons anders (waaronder); ontbreekt.

| Fase | Stap | Objecttype | Herken | Heet anders | Hangt anders | Ontbreekt |
|---|---|---|---|---|---|---|
| 1 | Kwalificatiedossier analyseren | Kwalificatie dossier | | | | |
| 1 | Kwalificatiedossier analyseren | Kwalificatie | | | | |
| 1 | Kwalificatiedossier analyseren | Kerntaak | | | | |
| 1 | Kwalificatiedossier analyseren | Werkproces | | | | |
| 1 | Examenplan vaststellen | Examenplan | | | | |
| 1 | Examenplan vaststellen | Summatieve resultaat structuur | | | | |
| 1 | Examenplan vaststellen | Cohort / periode | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Leeruitkomst | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Leeruitkomst | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Leeruitkomst | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Leeruitkomst | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Competenties / Skills | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Vaardigheid | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Kennis | | | | |
| 1 | Kwalificatiedossier vertalen naar leeruitkomsten | Inzicht | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Opleiding specificatie | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Opleidingsprogramma specificatie | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Onderwijseenheid specificatie | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Leeronderdeel specificatie | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Keuzedeelruimte | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Keuzedeel | | | | |
| 1 | Opleidingsspecificatie met programma en eenheden beschrijven | Student keuze regelset | | | | |
| 1 | Toetsonderdelen en resultaatstructuur uit het examenplan afleiden | Summatieve resultaat structuur | | | | |
| 1 | Toetsonderdelen en resultaatstructuur uit het examenplan afleiden | Toetsonderdeel specificatie | | | | |
| 1 | Toetsonderdelen en resultaatstructuur uit het examenplan afleiden | Examenonderdeelspecificatie | | | | |
| 1 | Toetsonderdelen en resultaatstructuur uit het examenplan afleiden | Examenonderdeel weging | | | | |
| 1 | Toetsonderdelen en resultaatstructuur uit het examenplan afleiden | Summatief Afrondingscriterium | | | | |
| 2 | Specificatie aanvullen tot planbare specificatie | Opleidingsprogramma specificatie | | | | |
| 2 | Planningssysteem verzoeken om onderwijsaanbod | Verzoek tot Aanbod / Intekening op specificatie | | | | |
| 2 | Haalbaarheid bepalen en aanbod plannen | Opleidingsaanbod van Instelling | | | | |
| 2 | Haalbaarheid bepalen en aanbod plannen | Opleidingaanbod | | | | |
| 2 | Haalbaarheid bepalen en aanbod plannen | Opleidingsprogramma aanbod | | | | |
| 2 | Haalbaarheid bepalen en aanbod plannen | Onderwijseenheid aanbod | | | | |
| 2 | Haalbaarheid bepalen en aanbod plannen | Leergelegenheid | | | | |
| 2 | Haalbaarheid bepalen en aanbod plannen | Toetsgelegenheid | | | | |
| 3 | Aanmelden via het intakesysteem | Persoon | | | | |
| 3 | Aanmelden via het intakesysteem | Aanmelding | | | | |
| 3 | Intake doorlopen en plaatsen | Student | | | | |
| 3 | Intake doorlopen en plaatsen | Opleiding aanbod verbintenis | | | | |
| 3 | Intake doorlopen en plaatsen | Opleidingsprogramma aanbod verbintenis | | | | |
| 3 | Intake doorlopen en plaatsen | Plaatsingsgroep | | | | |
| 3 | Persoon en verbintenissen vastleggen in de kernregistratie | Inschrijving | | | | |
| 4 | Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken | Leeronderdeel specificatie | | | | |
| 4 | Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken | Les specificatie | | | | |
| 4 | Leer-, les- en toetsgelegenheden roosteren | Leergelegenheid | | | | |
| 4 | Leer-, les- en toetsgelegenheden roosteren | Lesgelegenheid | | | | |
| 4 | Leer-, les- en toetsgelegenheden roosteren | Medewerker | | | | |
| 4 | Verwachte deelnemers delen en toegang geven | Onderwijseenheid aanbod verbintenis | | | | |
| 4 | Verwachte deelnemers delen en toegang geven | Leergelegenheid verbintenis | | | | |
| 4 | Verwachte deelnemers delen en toegang geven | Lesgelegenheid verbintenis | | | | |
| 4 | Verwachte deelnemers delen en toegang geven | Opleidingsprogramma aanbod verbintenis | | | | |
| 5 | Onderwijs verzorgen | Lesgelegenheid verbintenis | | | | |
| 5 | Onderwijs verzorgen | Aanwezigheid | | | | |
| 5 | Onderwijs verzorgen | Lesgelegenheid resultaat | | | | |
| 5 | Toetsmomenten plannen tijdens lessen | Toetsgelegenheid verbintenis | | | | |
| 5 | Formatieve voortgang bijhouden | Formatieve resultaat structuur | | | | |
| 5 | Formatieve voortgang bijhouden | Toetsonderdeel weging | | | | |
| 5 | Formatieve voortgang bijhouden | Toetsgelegenheid resultaat | | | | |
| 5 | Formatieve voortgang bijhouden | Formatief resultaat | | | | |
| 5 | Formatieve voortgang bijhouden | Formatieve beoordeling | | | | |
| 5 | Formatieve voortgang bijhouden | Persoonlijke ontwikkeling | | | | |
| 5 | Studiebeeld volgen in het studentvolgsysteem | Leergelegenheid resultaat | | | | |
| 5 | Studiebeeld volgen in het studentvolgsysteem | Onderwijseenheid resultaat | | | | |
| 6 | Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem | Keuzedeelaanbod | | | | |
| 6 | Voorkeurslijst samenstellen in het studentkeuzesysteem | Keuzedeel aanbod verbintenis | | | | |
| 6 | Definitieve keuzes verwerken naar groepen en capaciteit | Keuzedeelaanbod | | | | |
| 6 | Keuzedeel formeel inschrijven | Keuzedeel aanbod verbintenis | | | | |
| 7 | Afwijkingen verzamelen in een planninggroep | Plaatsingsgroep | | | | |
| 7 | Bestaande verbintenissen annuleren | Onderwijseenheid aanbod verbintenis | | | | |
| 7 | Nieuw aanbod maken en publiceren | Onderwijseenheid aanbod | | | | |
| 8 | Examenspecificaties omzetten in examengelegenheden | Examengelegenheid | | | | |
| 8 | Kandidatenlijsten samenstellen | Examengelegenheid verbintenis | | | | |
| 8 | Zitting uitvoeren en resultaten doorgeven | Examengelegenheid resultaat | | | | |
| 8 | Summatief vaststellen | Summatief resultaat | | | | |
| 8 | Summatief vaststellen | Summatieve beoordeling | | | | |
| 8 | Summatief vaststellen | Opleidingsprogramma resultaat | | | | |
| 8 | Summatief vaststellen | Keuzedeel resultaat | | | | |
| 8 | Kwalificering en diplomering registreren | Opleiding aanbod resultaat | | | | |
| 8 | Kwalificering en diplomering registreren | Waarde document (diploma / certificaat) | | | | |

