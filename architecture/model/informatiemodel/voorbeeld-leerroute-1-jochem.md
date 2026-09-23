# De opleiding van Jochem in het informatiemodel

Relateert aan: het [kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md) (persona Jochem, Apothekersassistent, cohort 2026), het architectuurkader van OKx, en het [informatiemodel OKx](informatiemodel.md). Gegenereerd uit `voorbeeld-lr1-regels.json`; gecontroleerd tegen `informatiemodel.json` op commit 0cf6e29 en `begrippen.json` op commit 8ebfaca.

## Leeswijzer

Dit document loopt stap voor stap door de instellingsreis van het kaderscenario en toont per stap wat er in het informatiemodel ontstaat en wat er tussen systemen beweegt, met de waarde voor Jochem erin. Het is een leeshulp op conceptueel niveau (MIM 1 en 2): geen payloads, geen endpoints, geen diensten. Eén instantie per objecttype toont het type, niet het aantal.

Elk beeld heeft een ID en een titel die zegt wat het toont: F1-02 is het tweede beeld van fase 1. Beide staan in het beeld zelf, als kop erboven (met een eigen anker in dit document) en in het regelregister achterin; de bijlage en het invulblad noemen het ID. Verwijs naar een beeld met zijn ID, en naar een regel met dat ID en het objecttype.

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

Waar de herkomst loopt: het kwalificatiedossier, de kwalificatie, de kerntaken en de werkprocessen staan in het eerste beeld van fase 1, en het derde beeld vertaalt ze naar leeruitkomsten. Daarna verwijzen specificaties, toets- en examenonderdelen, aanbod, verbintenissen en resultaten naar de leeruitkomst; de plaat kent buiten die route alleen een directe verwijzing vanuit het examenplan en de OER. Een dossiercode in een instantienaam (B1-K1, B1-K1-W1) is daarom een leeshulp die zegt over welk deel van het dossier het gaat, en geen relatie. Op de conceptplaat loopt daarnaast een eigen pad binnen de instelling: de kerntaak wordt daar onderwijskundig vertaald tot een leerdoel.

Een **verdieping** (zelfde rol en stap, met "verdieping" op de processtap) zoomt in op een regel erboven. Een paars objecttype komt van de conceptplaat "Informatiemodel Onderwijsontwerp" in het ArchiMate-model (een verdieping daaruit heeft ook een gestippelde rand en een chip): het laat zien waar de informatiemodelplaat kan groeien en telt niet mee in de bijlage en het invulblad.

Koppeling-ID's op hoofdplaat v1.7: OC-P&R is Onderwijscatalogus naar Planningssysteem; OC-P&R is Planningssysteem naar Onderwijscatalogus; OC-SIS is Onderwijscatalogus naar Kernregistratie systeem studenten (KRS); OC-SIS is Onderwijscatalogus naar Student volg systeem (SVS); OC-LMS is Onderwijscatalogus naar Leer management systeem (LMS). Een pijl die op de hoofdplaat staat maar geen koppelingspecificatie heeft, staat als "zonder koppelingspecificatie"; een stroom uit het kaderscenario zonder pijl op de hoofdplaat staat als "geen pijl op de hoofdplaat".

De fasenamen zijn de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario. Het kaderscenario noemt fase 3 in de fasenlijst "Instroom, afstemming en plaatsing" en in de sectiekop "Instroom, intake en plaatsing"; hier geldt de sectiekop.

Wat hier staat is feedback, geen commitment: het voorbeeld beslist niets over het model. Per objecttype staan in de bijlage twee lege kolommen, "heet bij u" en "hangt bij u onder", voor wie het naast het eigen model legt.
## De hoofdplaat als kaart

De beelden met een blauwe rand tonen een stroom tussen twee componenten. Die componenten en pijlen komen van hoofdplaat v1.7; de plaat hieronder is de kaart waarop die lijnen te vinden zijn.

![Hoofdplaat OKx informatiestromen v1.7](<../informatiestromen hoofdplaat OKx/1.7/OKx hoofdplaat 1.7.jpg>)

Alle stromen die dit voorbeeld gebruikt, met de beelden waarin ze voorkomen:

| Van | Naar | Op de hoofdplaat | Beelden |
|---|---|---|---|
| Curriculum ontwerptool | Onderwijscatalogus | geen pijl op de hoofdplaat | F1-11, F1-12 |
| Onderwijscatalogus | Planningssysteem | OC-P&R | F2-03 |
| Planningssysteem | Onderwijscatalogus | OC-P&R | F2-07, F6-06, F7-05 |
| Onderwijscatalogus | Kernregistratie systeem studenten (KRS) | OC-SIS | F3-01, F4-05 |
| Kernregistratie systeem studenten (KRS) | AII (centraal aanmelden) | geen pijl op de hoofdplaat | F3-02 |
| AII (centraal aanmelden) | Intake systeem | geen pijl op de hoofdplaat | F3-04 |
| Intake systeem | Student Keuze Systeem (SKS) | geen pijl op de hoofdplaat | F3-06 |
| Intake systeem | Kernregistratie systeem studenten (KRS) | geen pijl op de hoofdplaat | F3-08 |
| Onderwijscatalogus | Leer management systeem (LMS) | OC-LMS | F4-02, F4-03 |
| Onderwijscatalogus | Student volg systeem (SVS) | OC-SIS | F4-04 |
| Kernregistratie systeem studenten (KRS) | Planningssysteem | zonder koppelingspecificatie | F4-06, F7-03 |
| Planningssysteem | Roostersysteem | zonder koppelingspecificatie | F4-07, F7-06 |
| Kernregistratie systeem studenten (KRS) | Leer management systeem (LMS) | zonder koppelingspecificatie | F4-10 |
| Kernregistratie systeem studenten (KRS) | Student volg systeem (SVS) | geen pijl op de hoofdplaat | F4-11 |
| Leer management systeem (LMS) | Student volg systeem (SVS) | zonder koppelingspecificatie | F5-04 |
| Onderwijscatalogus | Student Keuze Systeem (SKS) | zonder koppelingspecificatie | F6-02 |
| Student Keuze Systeem (SKS) | Planningssysteem | zonder koppelingspecificatie | F6-04 |
| Student Keuze Systeem (SKS) | Kernregistratie systeem studenten (KRS) | zonder koppelingspecificatie | F6-08 |
| Toets- en examen afname systeem | Student volg systeem (SVS) | geen pijl op de hoofdplaat | F8-04 |
| Student volg systeem (SVS) | Kernregistratie systeem studenten (KRS) | geen pijl op de hoofdplaat | F8-06 |

Een stroom die het kaderscenario noemt en die de plaat nog niet kent, staat als "geen pijl op de hoofdplaat": dat is een signalering voor de plaat, geen omweg in het voorbeeld.

## De systemen en wat zij doen

De componenten in de stroombeelden komen uit het ArchiMate-model, dat de beschrijvingen van MORA draagt. Per systeem staat hieronder wat het doet en welke applicatiediensten het levert; zo is te zien waarom een stroom loopt zoals zij loopt.

| Systeem | Wat het doet | Applicatiediensten |
|---|---|---|
| AII (centraal aanmelden) | nog geen beschrijving in het model | nog geen diensten in het model |
| Curriculum ontwerptool | Een systeem ter ondersteuning van het ontwerp- en planningsproces van het curriculum (de samenhangende structuur) van een opleiding. Dit omvat onder andere de opbouw in opleidingsonderdelen met hun onderlinge afhankelijkheden, logsche volgorde, relatie met leerdoelen, kerntaken en werkprocessen en de omvang in studiebelasting. Daarnaast omvat dit ook het in de tijd plannen van het curriculum. Dit is een tijdplanning, hoe de opleidingsonderdelen ten opzichte van elkaar in onderwijsperiodes gepland kunnen worden zodat het qua belasting een studeerbaar en organiseerbaar geheel is. | Curriculum ontwerp, Curriculum planning |
| Intake systeem | Een systeem voor het plannen, inschrijven, afhandelen, verslagleggen en beoordelen van de intake van studenten. Dit zowel voor initiele aanmeldingen als voor tussentijdse loopbaanadviestrajecten | Intake dienst |
| Kernregistratie systeem studenten (KRS) | Een systeem voor het beheren van gegevens van studenten zoals in- en uitschrijvingsgegevens, BPV-contractgegevens, bekostigingsgegevens, studieresultaten, diploma's, studentbegeleidingsgegevens, studievoortganggegevens Bijvoorbeeld: Eduarte Osiris Magister TP Ellucian (Sungard/SCT) Banner Student Oracle Peopelsoft Campus Solutions | BPV overeenkomst beheer, Doorstroomdossier beheer, Inschijving op opleidingsprogramma, Inschrijvingen beheer, Kwalificering, Onderwijskosten facturering, Student gegevens beheer, Studentgegevens uitwisseling, Uitschrijvingen beheer, Uitwisseling BRON |
| Leer management systeem (LMS) | Systeem ten behoeve van het aanbieden en gebruiken van leermateriaal, de ondersteuning van het leerproces en de interactie tussen student en docent. | Communicatie en samenwerking, Leercontent gebruik, Onderwijs begeleiding ondersteuning, Overhandiging opdrachten, Studieroute beheer |
| Onderwijscatalogus | Een systeem voor het beheren en publiceren van het onderwijsaanbod, zoals dat is opgebouwd uit de onderwijsprogramma's, opleidingsonderdelen en leeractiviteiten en alle metadata die daarbij relevant is. Deze metadata omvat bijvoorbeeld de leerdoelen, kerntaken, werkprocessen, studiebelastingsuren etc. Het onderwijsaanbod omvat ook per onderwijsprogramma de bijbehorende standaard leerroutes en eventuele keuzemogelijkheden. De publicatie van het onderwijsaanbod kan in verschillende vormen plaatsvinden, bijvoorbeeld in de vorm van een Onderwijs en Examenreglement (OER) of een studiegids. | Onderwijs aanbod publicatie, Onderwijs beheer |
| Planningssysteem | nog geen beschrijving in het model | Jaar planning, Meerjaren planning |
| Roostersysteem | Een systeem dat het maken van roosters ondersteunt op basis van beschikbaarheid van mensen en middelen en de leerroutes van de studenten. Bijvoorbeeld: GPUntis Xedule | Aanmelding rooster activiteit, Groepen beheer, Rooster constructie, Rooster wijziging |
| Student Keuze Systeem (SKS) | nog geen beschrijving in het model | Accorderen van keuzes, Keuze op leergelegenheid |
| Student volg systeem (SVS) | Een systeem voor het registreren en meten van de studievoortgang en resultaten van een student. | Formatief resultaten beheer, Persoonlijke leerroute beheer, Studie voortgang bepaling, Summatief resultaten beheer |
| Toets- en examen afname systeem | Systeem voor het afnemen van toetsen en examens, denk aan een veilige afnameomgeving (BLDC - bootable lock down client) Bijvoorbeeld: * Safetyboot * Facet * QMP | Toets of examen afname |

Zonder beschrijving in het model: AII (centraal aanmelden), Planningssysteem, Student Keuze Systeem (SKS). Dat is een signalering voor het model, geen keuze van dit voorbeeld.

## Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen

De fase in detail: [kaderscenario leerroute 1, fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen).

**Ontstaat:** `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces`, `Examenplan`, `Summatieve resultaat structuur`, `Cohort / periode`, `Leeruitkomst`, `Competenties / Skills`, `Vaardigheid`, `Kennis`, `Inzicht`, `Onderwijseenheid specificatie`, `Leeronderdeel specificatie`, `Opleiding specificatie`, `Opleidingsprogramma specificatie`, `Keuzedeelruimte`, `Student keuze regelset`, `Keuzedeel`, `Toetsonderdeel specificatie`, `Examenonderdeelspecificatie`, `Examenonderdeel weging`, `Summatief Afrondingscriterium`. **Stroomt:** Curriculum ontwerptool naar Onderwijscatalogus. **MORA-hoofdproces:** Ontwikkelen.

![Hoofdplaat v1.7 met de stromen van fase 1 gemarkeerd](img/hoofdplaat/f1.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F1-01 - Het kwalificatiedossier ontleed

![ontstaat: Kwalificatiedossier analyseren](img/regels/f1-01-het-kwalificatiedossier-ontleed.svg)

### F1-02 - Examenplan, eerste resultaatstructuur en cohort

![ontstaat: Examenplan vaststellen](img/regels/f1-02-examenplan-eerste-resultaatstructuur-en-cohort.svg)

### F1-03 - Leeruitkomsten uit het dossier, in de stem van de instelling

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten](img/regels/f1-03-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.svg)

### F1-04 - De leeruitkomst in CompetentNL-skills

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: leeruitkomst naar skills](img/regels/f1-04-de-leeruitkomst-in-competentnl-skills.svg)

### F1-05 - De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: van kerntaak naar eenheid en leeronderdelen](img/regels/f1-05-de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten.svg)

### F1-06 - De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: onderwijsontwerp met ruimte en middelen](img/regels/f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen.svg)

### F1-07 - De opleidingsspecificatie met programma, eenheden en keuzedeelruimte

![ontstaat: Opleidingsspecificatie met programma en eenheden beschrijven](img/regels/f1-07-de-opleidingsspecificatie-met-programma-eenheden-en-keuzedeelruimte.svg)

### F1-08 - Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen

![ontstaat: Keuzedeelprogramma als eigen specificatie vormgeven](img/regels/f1-08-het-keuzedeel-als-eigen-programmaspecificatie-met-kerntaken-en-werkprocessen.svg)

### F1-09 - Toetsonderdelen, wegingen en afrondingscriterium

![ontstaat: Toetsonderdelen en resultaatstructuur uit het examenplan afleiden](img/regels/f1-09-toetsonderdelen-wegingen-en-afrondingscriterium.svg)

### F1-10 - De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte

![ontstaat: Exameninstrumenten bepalen, inkopen of construeren, verdieping: examenvorm, instrument en beoordelaar](img/regels/f1-10-de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte.svg)

### F1-11 - De opleiding zoals ontworpen naar de catalogus

![stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus](img/regels/f1-11-de-opleiding-zoals-ontworpen-naar-de-catalogus.svg)

**Interactie:** Curriculum ontwerptool naar Onderwijscatalogus, geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F1-11.

### F1-12 - Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)

![stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus](img/regels/f1-12-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat.svg)

**Interactie:** Curriculum ontwerptool naar Onderwijscatalogus, geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F1-12.

## Fase 2: Publiceren en planbaar maken

De fase in detail: [kaderscenario leerroute 1, fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken).

**Ontstaat:** `Opleidingsprogramma specificatie`, `Onderwijseenheid specificatie`, `Leeronderdeel specificatie`, `Verzoek tot Aanbod / Intekening op specificatie`, `Opleidingsaanbod van Instelling`, `Opleidingaanbod`, `Opleidingsprogramma aanbod`, `Onderwijseenheid aanbod`, `Leergelegenheid`, `Toetsgelegenheid`. **Stroomt:** Onderwijscatalogus naar Planningssysteem; Planningssysteem naar Onderwijscatalogus. **MORA-hoofdproces:** Plannen en roosteren.

![Hoofdplaat v1.7 met de stromen van fase 2 gemarkeerd](img/hoofdplaat/f2.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F2-01 - De specificatie planbaar gemaakt

![ontstaat: Specificatie aanvullen tot planbare specificatie](img/regels/f2-01-de-specificatie-planbaar-gemaakt.svg)

### F2-02 - Het verzoek om onderwijsaanbod

![ontstaat: Planningssysteem verzoeken om onderwijsaanbod](img/regels/f2-02-het-verzoek-om-onderwijsaanbod.svg)

### F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning

![stroomt: Planningssysteem verzoeken om onderwijsaanbod](img/regels/f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.svg)

**Interactie:** Onderwijscatalogus naar Planningssysteem, OC-P&R. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F2-03.

### F2-04 - Het aanbod gepland: opleiding, programma, eenheid, gelegenheid

![ontstaat: Haalbaarheid bepalen en aanbod plannen](img/regels/f2-04-het-aanbod-gepland-opleiding-programma-eenheid-gelegenheid.svg)

### F2-05 - Ruimtes en mensen op de specificatie (conceptplaat)

![ontstaat: Haalbaarheid bepalen en aanbod plannen, verdieping: ruimtes en mensen op de specificatie](img/regels/f2-05-ruimtes-en-mensen-op-de-specificatie-conceptplaat.svg)

### F2-06 - Examenplanning uit de resultaatstructuur (conceptplaat)

![ontstaat: Haalbaarheid bepalen en aanbod plannen, verdieping: examenplanning uit de resultaatstructuur](img/regels/f2-06-examenplanning-uit-de-resultaatstructuur-conceptplaat.svg)

### F2-07 - Het geplande aanbod terug naar de catalogus

![stroomt: Gepland aanbod terugleveren aan de onderwijscatalogus](img/regels/f2-07-het-geplande-aanbod-terug-naar-de-catalogus.svg)

**Interactie:** Planningssysteem naar Onderwijscatalogus, OC-P&R. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F2-07.

## Fase 3: Instroom, intake en plaatsing

De fase in detail: [kaderscenario leerroute 1, fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing).

**Ontstaat:** `Persoon`, `Aanmelding`, `Opleiding aanbod verbintenis`, `Opleidingsprogramma aanbod verbintenis`, `Student`, `Plaatsingsgroep`, `Verzoek tot Aanbod / Intekening op specificatie`, `Inschrijving`. **Stroomt:** Onderwijscatalogus naar Kernregistratie systeem studenten (KRS); Kernregistratie systeem studenten (KRS) naar AII (centraal aanmelden); AII (centraal aanmelden) naar Intake systeem; Intake systeem naar Student Keuze Systeem (SKS); Intake systeem naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Informeren, aanmelden, intake en plaatsen.

![Hoofdplaat v1.7 met de stromen van fase 3 gemarkeerd](img/hoofdplaat/f3.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F3-01 - Aanmeldbaar aanbod naar de kernregistratie

![stroomt: Orienteren op het gepubliceerde aanbod](img/regels/f3-01-aanmeldbaar-aanbod-naar-de-kernregistratie.svg)

**Interactie:** Onderwijscatalogus naar Kernregistratie systeem studenten (KRS), OC-SIS. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F3-01.

### F3-02 - Aanmeldbaar aanbod van de kernregistratie naar AII

![stroomt: Orienteren op het gepubliceerde aanbod](img/regels/f3-02-aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii.svg)

**Interactie:** Kernregistratie systeem studenten (KRS) naar AII (centraal aanmelden), geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F3-02.

### F3-03 - Jochem meldt zich aan: aanmelding en verbintenissen

![ontstaat: Aanmelden via het intakesysteem](img/regels/f3-03-jochem-meldt-zich-aan-aanmelding-en-verbintenissen.svg)

### F3-04 - De aanmelding van de voorziening naar het intakesysteem

![stroomt: Aanmelden via het intakesysteem](img/regels/f3-04-de-aanmelding-van-de-voorziening-naar-het-intakesysteem.svg)

**Interactie:** AII (centraal aanmelden) naar Intake systeem, geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F3-04.

### F3-05 - Intake: student, plaatsingsgroep en eerste keuzedeelvoorkeur

![ontstaat: Intake doorlopen en plaatsen](img/regels/f3-05-intake-student-plaatsingsgroep-en-eerste-keuzedeelvoorkeur.svg)

### F3-06 - De eerste keuzedeelvoorkeur naar het studentkeuzesysteem

![stroomt: Intake doorlopen en plaatsen](img/regels/f3-06-de-eerste-keuzedeelvoorkeur-naar-het-studentkeuzesysteem.svg)

**Interactie:** Intake systeem naar Student Keuze Systeem (SKS), geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F3-06.

### F3-07 - Inschrijving: van aangemeld naar ingeschreven

![ontstaat: Persoon en verbintenissen vastleggen in de kernregistratie](img/regels/f3-07-inschrijving-van-aangemeld-naar-ingeschreven.svg)

### F3-08 - De inschrijving van het intakesysteem naar de kernregistratie

![stroomt: Persoon en verbintenissen vastleggen in de kernregistratie](img/regels/f3-08-de-inschrijving-van-het-intakesysteem-naar-de-kernregistratie.svg)

**Interactie:** Intake systeem naar Kernregistratie systeem studenten (KRS), geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F3-08.

## Fase 4: Detailleren, roosteren en inschrijven

De fase in detail: [kaderscenario leerroute 1, fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven).

**Ontstaat:** `Leeronderdeel specificatie`, `Les specificatie`, `Leergelegenheid`, `Lesgelegenheid`, `Medewerker`, `Onderwijseenheid aanbod verbintenis`, `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis`, `Opleidingsprogramma aanbod verbintenis`. **Stroomt:** Onderwijscatalogus naar Leer management systeem (LMS); Onderwijscatalogus naar Student volg systeem (SVS); Onderwijscatalogus naar Kernregistratie systeem studenten (KRS); Kernregistratie systeem studenten (KRS) naar Planningssysteem; Planningssysteem naar Roostersysteem; Kernregistratie systeem studenten (KRS) naar Leer management systeem (LMS); Kernregistratie systeem studenten (KRS) naar Student volg systeem (SVS). **MORA-hoofdproces:** Plannen en roosteren.

![Hoofdplaat v1.7 met de stromen van fase 4 gemarkeerd](img/hoofdplaat/f4.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F4-01 - Het leeronderdeel fijnmazig: lessenreeks en les

![ontstaat: Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken](img/regels/f4-01-het-leeronderdeel-fijnmazig-lessenreeks-en-les.svg)

### F4-02 - Detailspecificaties naar het LMS

![stroomt: Detailspecificaties leveren aan het LMS](img/regels/f4-02-detailspecificaties-naar-het-lms.svg)

**Interactie:** Onderwijscatalogus naar Leer management systeem (LMS), OC-LMS. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-02.

### F4-03 - De les en de toets van binnen, elk met hun eigen onderdelen (conceptplaat)

![stroomt: Detailspecificaties leveren aan het LMS](img/regels/f4-03-de-les-en-de-toets-van-binnen-elk-met-hun-eigen-onderdelen-conceptplaat.svg)

**Interactie:** Onderwijscatalogus naar Leer management systeem (LMS), OC-LMS. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-03.

### F4-04 - Resultaatstructuur naar het studentvolgsysteem

![stroomt: Detailspecificaties leveren aan het LMS](img/regels/f4-04-resultaatstructuur-naar-het-studentvolgsysteem.svg)

**Interactie:** Onderwijscatalogus naar Student volg systeem (SVS), OC-SIS. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-04.

### F4-05 - Resultaatstructuur naar de kernregistratie

![stroomt: Detailspecificaties leveren aan het LMS](img/regels/f4-05-resultaatstructuur-naar-de-kernregistratie.svg)

**Interactie:** Onderwijscatalogus naar Kernregistratie systeem studenten (KRS), OC-SIS. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-05.

### F4-06 - Plaatsingsgroepen naar planning

![stroomt: Plaatsings- en planninggroepen definieren en aan personen koppelen](img/regels/f4-06-plaatsingsgroepen-naar-planning.svg)

**Interactie:** Kernregistratie systeem studenten (KRS) naar Planningssysteem, zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-06.

### F4-07 - Te roosteren leergelegenheden naar het roostersysteem

![stroomt: Te roosteren specificaties aan het roostersysteem geven](img/regels/f4-07-te-roosteren-leergelegenheden-naar-het-roostersysteem.svg)

**Interactie:** Planningssysteem naar Roostersysteem, zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-07.

### F4-08 - Roosteren: lesgelegenheid, lokaal en docent

![ontstaat: Leer-, les- en toetsgelegenheden roosteren](img/regels/f4-08-roosteren-lesgelegenheid-lokaal-en-docent.svg)

### F4-09 - Jochems verbintenissen op de geroosterde gelegenheden

![ontstaat: Verwachte deelnemers delen en toegang geven](img/regels/f4-09-jochems-verbintenissen-op-de-geroosterde-gelegenheden.svg)

### F4-10 - Student, verbintenissen en groep naar het LMS

![stroomt: Verwachte deelnemers delen en toegang geven](img/regels/f4-10-student-verbintenissen-en-groep-naar-het-lms.svg)

**Interactie:** Kernregistratie systeem studenten (KRS) naar Leer management systeem (LMS), zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-10.

### F4-11 - Verbintenissen op alle niveaus naar het studentvolgsysteem

![stroomt: Verwachte deelnemers delen en toegang geven](img/regels/f4-11-verbintenissen-op-alle-niveaus-naar-het-studentvolgsysteem.svg)

**Interactie:** Kernregistratie systeem studenten (KRS) naar Student volg systeem (SVS), geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F4-11.

## Fase 5: Onderwijs uitvoeren en voortgang begeleiden

De fase in detail: [kaderscenario leerroute 1, fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden).

**Ontstaat:** `Lesgelegenheid verbintenis`, `Aanwezigheid`, `Lesgelegenheid resultaat`, `Toetsgelegenheid verbintenis`, `Formatieve resultaat structuur`, `Toetsonderdeel weging`, `Toetsgelegenheid resultaat`, `Formatief resultaat`, `Formatieve beoordeling`, `Persoonlijke ontwikkeling`, `Leergelegenheid resultaat`, `Onderwijseenheid resultaat`, `Onderwijseenheid aanbod`, `Summatieve resultaat structuur`. **Stroomt:** Leer management systeem (LMS) naar Student volg systeem (SVS). **MORA-hoofdproces:** Verzorgen en begeleiden.

![Hoofdplaat v1.7 met de stromen van fase 5 gemarkeerd](img/hoofdplaat/f5.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F5-01 - Les gevolgd: aanwezigheid en lesresultaat

![ontstaat: Onderwijs verzorgen](img/regels/f5-01-les-gevolgd-aanwezigheid-en-lesresultaat.svg)

### F5-02 - De verbintenis op de toetsgelegenheid: geplaatst of zelf gekozen

![ontstaat: Toetsmomenten plannen tijdens lessen](img/regels/f5-02-de-verbintenis-op-de-toetsgelegenheid-geplaatst-of-zelf-gekozen.svg)

### F5-03 - Formatieve voortgang: structuur, resultaten en beoordeling

![ontstaat: Formatieve voortgang bijhouden](img/regels/f5-03-formatieve-voortgang-structuur-resultaten-en-beoordeling.svg)

### F5-04 - Formatieve resultaten van het LMS naar het studentvolgsysteem

![stroomt: Formatieve voortgang bijhouden](img/regels/f5-04-formatieve-resultaten-van-het-lms-naar-het-studentvolgsysteem.svg)

**Interactie:** Leer management systeem (LMS) naar Student volg systeem (SVS), zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F5-04.

### F5-05 - Studiebeeld: de nominale route naast wat Jochem heeft behaald

![ontstaat: Studiebeeld volgen in het studentvolgsysteem](img/regels/f5-05-studiebeeld-de-nominale-route-naast-wat-jochem-heeft-behaald.svg)

## Fase 6: Organiseren van keuzemomenten

De fase in detail: [kaderscenario leerroute 1, fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten).

**Ontstaat:** `Keuzedeelaanbod`, `Keuzedeel aanbod verbintenis`. **Stroomt:** Onderwijscatalogus naar Student Keuze Systeem (SKS); Student Keuze Systeem (SKS) naar Planningssysteem; Planningssysteem naar Onderwijscatalogus; Student Keuze Systeem (SKS) naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Plannen en roosteren.

![Hoofdplaat v1.7 met de stromen van fase 6 gemarkeerd](img/hoofdplaat/f6.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F6-01 - Keuzedeelaanbod ontsloten

![ontstaat: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem](img/regels/f6-01-keuzedeelaanbod-ontsloten.svg)

### F6-02 - Keuzedeelaanbod, specificatie en regels naar het studentkeuzesysteem

![stroomt: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem](img/regels/f6-02-keuzedeelaanbod-specificatie-en-regels-naar-het-studentkeuzesysteem.svg)

**Interactie:** Onderwijscatalogus naar Student Keuze Systeem (SKS), zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F6-02.

### F6-03 - Jochems voorkeur: verbintenis op het keuzedeelaanbod

![ontstaat: Voorkeurslijst samenstellen in het studentkeuzesysteem](img/regels/f6-03-jochems-voorkeur-verbintenis-op-het-keuzedeelaanbod.svg)

### F6-04 - Keuzestelling naar planning

![stroomt: Voorkeurslijst samenstellen in het studentkeuzesysteem](img/regels/f6-04-keuzestelling-naar-planning.svg)

**Interactie:** Student Keuze Systeem (SKS) naar Planningssysteem, zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F6-04.

### F6-05 - Definitieve keuzes verwerkt naar groepen en capaciteit

![ontstaat: Definitieve keuzes verwerken naar groepen en capaciteit](img/regels/f6-05-definitieve-keuzes-verwerkt-naar-groepen-en-capaciteit.svg)

### F6-06 - Geactualiseerd keuzedeelaanbod terug naar de catalogus

![stroomt: Planbaar aanbod actualiseren](img/regels/f6-06-geactualiseerd-keuzedeelaanbod-terug-naar-de-catalogus.svg)

**Interactie:** Planningssysteem naar Onderwijscatalogus, OC-P&R. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F6-06.

### F6-07 - Formele inschrijving op het keuzedeel

![ontstaat: Keuzedeel formeel inschrijven](img/regels/f6-07-formele-inschrijving-op-het-keuzedeel.svg)

### F6-08 - Keuzedeelverbintenis naar de kernregistratie

![stroomt: Keuzedeel formeel inschrijven](img/regels/f6-08-keuzedeelverbintenis-naar-de-kernregistratie.svg)

**Interactie:** Student Keuze Systeem (SKS) naar Kernregistratie systeem studenten (KRS), zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F6-08.

## Fase 7: Bijsturen planning en aanbod

De fase in detail: [kaderscenario leerroute 1, fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod).

**Ontstaat:** `Plaatsingsgroep`, `Onderwijseenheid aanbod verbintenis`, `Onderwijseenheid aanbod`. **Stroomt:** Kernregistratie systeem studenten (KRS) naar Planningssysteem; Planningssysteem naar Onderwijscatalogus; Planningssysteem naar Roostersysteem. **MORA-hoofdproces:** Plannen en roosteren.

![Hoofdplaat v1.7 met de stromen van fase 7 gemarkeerd](img/hoofdplaat/f7.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F7-01 - Afwijkingen verzameld in een planninggroep

![ontstaat: Afwijkingen verzamelen in een planninggroep](img/regels/f7-01-afwijkingen-verzameld-in-een-planninggroep.svg)

### F7-02 - Bestaande verbintenis geannuleerd

![ontstaat: Bestaande verbintenissen annuleren](img/regels/f7-02-bestaande-verbintenis-geannuleerd.svg)

### F7-03 - Planninggroep van de kernregistratie naar planning

![stroomt: Bestaande verbintenissen annuleren](img/regels/f7-03-planninggroep-van-de-kernregistratie-naar-planning.svg)

**Interactie:** Kernregistratie systeem studenten (KRS) naar Planningssysteem, zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F7-03.

### F7-04 - Nieuw aanbod voor de planninggroep

![ontstaat: Nieuw aanbod maken en publiceren](img/regels/f7-04-nieuw-aanbod-voor-de-planninggroep.svg)

### F7-05 - Bijgestuurd aanbod naar de catalogus

![stroomt: Nieuw aanbod maken en publiceren](img/regels/f7-05-bijgestuurd-aanbod-naar-de-catalogus.svg)

**Interactie:** Planningssysteem naar Onderwijscatalogus, OC-P&R. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F7-05.

### F7-06 - Nieuwe leergelegenheden naar het roostersysteem

![stroomt: Nieuw aanbod maken en publiceren](img/regels/f7-06-nieuwe-leergelegenheden-naar-het-roostersysteem.svg)

**Interactie:** Planningssysteem naar Roostersysteem, zonder koppelingspecificatie. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F7-06.

## Fase 8: Examineren, vaststellen en diplomeren

De fase in detail: [kaderscenario leerroute 1, fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren).

**Ontstaat:** `Examengelegenheid`, `Examengelegenheid verbintenis`, `Examengelegenheid resultaat`, `Summatief resultaat`, `Summatieve beoordeling`, `Opleidingsprogramma resultaat`, `Keuzedeel resultaat`, `Opleiding aanbod resultaat`, `Waarde document (diploma / certificaat)`. **Stroomt:** Toets- en examen afname systeem naar Student volg systeem (SVS); Student volg systeem (SVS) naar Kernregistratie systeem studenten (KRS). **MORA-hoofdproces:** Examens uitvoeren en vaststellen; diplomeren.

![Hoofdplaat v1.7 met de stromen van fase 8 gemarkeerd](img/hoofdplaat/f8.svg)

De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan; een gestippelde lijn is een stroom die de plaat nog niet kent.

### F8-01 - Examengelegenheid uit de examenspecificatie

![ontstaat: Examenspecificaties omzetten in examengelegenheden](img/regels/f8-01-examengelegenheid-uit-de-examenspecificatie.svg)

### F8-02 - Kandidatenlijst: verbintenis op de examengelegenheid

![ontstaat: Kandidatenlijsten samenstellen](img/regels/f8-02-kandidatenlijst-verbintenis-op-de-examengelegenheid.svg)

### F8-03 - Zitting: het examenresultaat

![ontstaat: Zitting uitvoeren en resultaten doorgeven](img/regels/f8-03-zitting-het-examenresultaat.svg)

### F8-04 - Examenresultaat naar het studentvolgsysteem

![stroomt: Zitting uitvoeren en resultaten doorgeven](img/regels/f8-04-examenresultaat-naar-het-studentvolgsysteem.svg)

**Interactie:** Toets- en examen afname systeem naar Student volg systeem (SVS), geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F8-04.

### F8-05 - Summatief vastgesteld: resultaten en beoordeling

![ontstaat: Summatief vaststellen](img/regels/f8-05-summatief-vastgesteld-resultaten-en-beoordeling.svg)

### F8-06 - Vaststelling naar de kernregistratie

![stroomt: Summatief vaststellen](img/regels/f8-06-vaststelling-naar-de-kernregistratie.svg)

**Interactie:** Student volg systeem (SVS) naar Kernregistratie systeem studenten (KRS), geen pijl op de hoofdplaat. Op de [hoofdplaat](#de-hoofdplaat-als-kaart) en in de faseplaat hierboven staat deze lijn gemarkeerd met F8-06.

### F8-07 - Gediplomeerd: opleidingsresultaat en diploma

![ontstaat: Kwalificering en diplomering registreren](img/regels/f8-07-gediplomeerd-opleidingsresultaat-en-diploma.svg)

## Bijlage: alle objecttypen per begrippenfamilie

Per objecttype het beeld waarin hij verschijnt (het ID uit de kop), de instantie voor Jochem, de fase, de status van de definitie in de begrippenlijst en het OEAPI-object uit de mapping. De laatste twee kolommen zijn voor de lezer.

### Kwalificatiekader mbo

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Kerntaak | F1-01 | B1-K1 Biedt farmaceutische patiëntenzorg | 1 |  | ja | geen equivalent | | |
| Kwalificatie | F1-01 | Apothekersassistent, 27141 | 1 |  | ja | geen equivalent | | |
| Kwalificatie dossier | F1-01 | Apothekersassistent, crebo 23450 | 1 |  | ja | geen equivalent | | |
| Werkproces | F1-01 | B1-K1-W1 Neemt de zorg-/adviesvraag in behandeling | 1 |  | ja | geen equivalent | | |

### Onderwijskundig kader instelling

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Competenties / Skills | F1-04 | Vaardigheden bij deze leeruitkomst (CompetentNL) | 1 | ja | nog te definieren | geen equivalent | | |
| Inzicht | F1-04 | Werking en risico van een geneesmiddel bij de vraag aan de balie | 1 | ja | nog te definieren | geen equivalent | | |
| Kennis | F1-04 | Farmacie (CompetentNL kennisgebied op ISCED-F 0916) | 1 | ja | nog te definieren | geen equivalent | | |
| Leeruitkomst | F1-03 | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving (kerntaakniveau) | 1 | ja | ja | LearningOutcome | | |
| Vaardigheid | F1-04 | Communicatieve vaardigheden (CompetentNL laag 2) | 1 | ja | nog te definieren | geen equivalent | | |

### Onderwijsspecificatie

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Examenonderdeelspecificatie | F1-09 | Proeve van bekwaamheid B1-K1 | 1 | ja | ja | TestComponent | | |
| Keuzedeel | F1-08 | K0262 ARBO, kwaliteitszorg en hulpverlening geschikt voor niveau 3 (240 SBU) | 1 |  | nog te definieren | Programme | | |
| Keuzedeelruimte | F1-07 | 720 SBU, mbo-4: te vullen met 480 SBU verdiepend en 240 SBU generiek | 1 |  | ja | Programme | | |
| Leeronderdeel specificatie | F1-05 | B1-K1-W1 Baliegesprek en triage | 1 |  | ja | LearningComponent | | |
| Les specificatie | F4-01 | Les 1 Introductie WHAM-vragen en triage | 4 |  | ja | LearningComponent | | |
| Onderwijseenheid specificatie | F1-05 | Blok B1-K1 Biedt farmaceutische patiëntenzorg | 1 |  | ja | Course | | |
| Opleiding specificatie | F1-07 | Apothekersassistent, versie 2026.1 | 1 |  | nog te definieren | Programme | | |
| Opleidingsprogramma specificatie | F1-07 | BOL voltijd, diplomaprogramma | 1 |  | ja | Programme | | |
| Student keuze regelset | F1-07 | Kiesbare keuzedelen: K0037 Farmaceutische Patientenzorg (480 SBU, verdiepend) of K0262 ARBO, kwaliteitszorg en hulpverlening (240 SBU, generiek) | 1 |  | nog te definieren | geen equivalent | | |
| Toetsonderdeel specificatie | F1-09 | Praktijktoets baliegesprek (OSCE), summatief | 1 |  | ja | TestComponent | | |

### Onderwijsaanbod

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Examengelegenheid | F8-01 | Proeve van bekwaamheid B1-K1, periode 12 | 8 | ja | ja | TestComponentOffering | | |
| Keuzedeelaanbod | F6-01 | K0037 Farmaceutische Patientenzorg, periode 7, locatie A | 6 | ja | nog te definieren | ProgrammeOffering | | |
| Leergelegenheid | F2-04 | B1-K1-W1, periode 1, twee groepen van 24 | 2 |  | nog te definieren | LearningComponentOffering | | |
| Lesgelegenheid | F4-08 | Les 1, maandag 1 september 09:00, simulatieruimte 2.14 | 4 |  | nog te definieren | LearningComponentOffering | | |
| Onderwijseenheid aanbod | F2-04 | B1-K1, leerjaar 1, periode 1 tot 4 | 2 |  | nog te definieren | CourseOffering | | |
| Opleidingaanbod | F2-04 | Apothekersassistent 2026: vier perioden, 120 plaatsen | 2 |  | ja | ProgrammeOffering | | |
| Opleidingsaanbod van Instelling | F2-04 | ROC Het Voorbeeld: ambitie en verwachte instroom voor cohort 2026 | 2 | ja | ja | geen equivalent | | |
| Opleidingsprogramma aanbod | F2-04 | Regulier BOL 2026: 18 tot 120 studenten | 2 |  | nog te definieren | ProgrammeOffering | | |
| Toetsgelegenheid | F2-04 | Praktijktoets baliegesprek (OSCE), einde periode 1 | 2 |  | ja | TestComponentOffering | | |

### Onderwijsverbintenis

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Examengelegenheid verbintenis | F8-02 | Jochem op de proeve, periode 12 | 8 |  | ja | TestComponentOfferingAssociation | | |
| Inschrijving | F3-07 | Juni 2026 | 3 |  | ja | geen equivalent | | |
| Keuzedeel aanbod verbintenis | F6-03 | Jochem op K0037 Farmaceutische Patientenzorg, periode 7 (voorkeur 1) | 6 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Leergelegenheid verbintenis | F4-09 | Jochem op B1-K1-W1, periode 1 | 4 |  | nog te definieren | LearningComponentOfferingAssociation | | |
| Lesgelegenheid verbintenis | F4-09 | Jochem op les 1, 1 september 09:00 | 4 |  | nog te definieren | LearningComponentOfferingAssociation | | |
| Onderwijseenheid aanbod verbintenis | F4-09 | Jochem op B1-K1, leerjaar 1 | 4 |  | nog te definieren | CourseOfferingAssociation | | |
| Opleiding aanbod verbintenis | F3-03 | Jochem op Apothekersassistent 2026, aangemeld | 3 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Opleidingsprogramma aanbod verbintenis | F3-03 | Jochem op Regulier BOL 2026, aangemeld | 3 |  | nog te definieren | ProgrammeOfferingAssociation | | |
| Toetsgelegenheid verbintenis | F5-02 | Jochem op de OSCE, einde periode 1, via zijn plaatsingsgroep | 5 |  | ja | TestComponentOfferingAssociation | | |

### Onderwijsresultaat

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Aanwezigheid | F5-01 | Aanwezig, les 1 | 5 |  | nog te definieren | geen equivalent | | |
| Examengelegenheid resultaat | F8-03 | Proeve B1-K1: voldoende | 8 |  | nog te definieren | Result | | |
| Formatief resultaat | F5-03 | Quiz WHAM-vragen: 8 van 10 | 5 | ja | ja | geen equivalent | | |
| Formatieve beoordeling | F5-03 | Op koers voor B1-K1-W1 | 5 | ja | ja | geen equivalent | | |
| Keuzedeel resultaat | F8-05 | K0037 Farmaceutische Patientenzorg: voldoende | 8 |  | nog te definieren | Result | | |
| Leergelegenheid resultaat | F5-03 | B1-K1-W1 afgerond, periode 1 | 5 |  | nog te definieren | Result | | |
| Lesgelegenheid resultaat | F5-01 | Les 1 gevolgd | 5 |  | nog te definieren | Result | | |
| Onderwijseenheid resultaat | F5-05 | B1-K1: in uitvoering, twee van vier leeronderdelen afgerond | 5 |  | nog te definieren | Result | | |
| Opleiding aanbod resultaat | F8-07 | Apothekersassistent 2026: gediplomeerd | 8 |  | nog te definieren | Result | | |
| Opleidingsprogramma resultaat | F8-05 | Regulier BOL 2026: alle kerntaken en keuzedelen voldoende | 8 |  | nog te definieren | Result | | |
| Summatief resultaat | F8-05 | B1-K1: voldoende, vastgesteld | 8 |  | ja | geen equivalent | | |
| Summatieve beoordeling | F8-05 | Examencommissie, juni 2029 | 8 | ja | ja | geen equivalent | | |
| Toetsgelegenheid resultaat | F5-03 | OSCE: voldoende | 5 |  | nog te definieren | Result | | |

### Resultaatstructuur

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Examenonderdeel weging | F1-09 | Proeve van bekwaamheid B1-K1: weging 2 | 1 | ja | nog te definieren | geen equivalent | | |
| Formatieve resultaat structuur | F5-03 | Voortgang B1-K1-W1: quiz WHAM-vragen, rollenspel | 5 | ja | ja | geen equivalent | | |
| Persoonlijke ontwikkeling | F5-03 | Jochems ontwikkeling in periode 1 | 5 | ja | nog te definieren | geen equivalent | | |
| Summatief Afrondingscriterium | F1-09 | Alle kerntaken en de keuzedelen voldoende | 1 |  | nog te definieren | geen equivalent | | |
| Summatieve resultaat structuur | F1-02 | Eerste opzet: kerntaken en keuzedelen, alle voldoende | 1 | ja | ja | geen equivalent | | |
| Toetsonderdeel weging | F5-03 | Quiz WHAM-vragen: weging 1 | 5 | ja | nog te definieren | geen equivalent | | |

### Buiten de kolommen (persoon, groep, cohort, verzoek)

| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| Aanmelding | F3-03 | April 2026, Apothekersassistent BOL | 3 |  | ja | geen equivalent | | |
| Cohort / periode | F1-02 | Cohort 2026 | 1 |  | ja | geen equivalent | | |
| Examenplan | F1-02 | Examenplan Apothekersassistent, cohort 2026 | 1 | ja | ja | geen equivalent | | |
| Medewerker | F4-08 | Docent, personeelsnummer 4711 | 4 |  | ja | geen equivalent | | |
| Persoon | F3-03 | Jochem, 17, na het vmbo | 3 |  | nog te definieren | Person | | |
| Plaatsingsgroep | F3-05 | APO26-1A | 3 | ja | nog te definieren | Group | | |
| Student | F3-05 | Jochem, cohort 2026 | 3 |  | ja | geen equivalent | | |
| Verzoek tot Aanbod / Intekening op specificatie | F2-02 | Planopgave Apothekersassistent, cohort 2026 | 2 | ja | ja | geen equivalent | | |
| Waarde document (diploma / certificaat) | F8-07 | Diploma Apothekersassistent, juli 2029 | 8 |  | ja | geen equivalent | | |

## Vragen aan de kerngroep

De vragen die de regels zelf oproepen, met de regel waar de vraag zichtbaar wordt. Feedback, geen commitment.

1. Het kaderscenario zet het examenplan in fase 1 en de resultaatstructuur pas in fase 4 bij OC-SIS. Ontstaat de summatieve resultaatstructuur in de curriculum-ontwerptool uit het examenplan, en gaat zij met de specificatie mee naar de catalogus? (F1-02, `Examenplan`)
2. Is het cohort een sleutel op aanbod en verbintenis, of een eigen object dat de toepasselijke resultaatstructuur draagt (ontwerpkeuze 17)? (F1-02, `Cohort / periode`)
3. CompetentNL legt vaardigheden gelaagd vast (skos:broader, drie lagen) en de leeruitkomst is op de plaat gelaagd; Vaardigheid is dat niet. Krijgt Vaardigheid een eigen aggregatie, zodat laag 2 onder laag 1 hangt zoals de leeruitkomst onder de leeruitkomst? (F1-04, `Vaardigheid`)
4. De conceptplaat kent leervormstrategie, leerdoel, onderwijsvorm, leeromgeving, docentprofiel, studiebelasting en leermiddelen, maar verbindt ze niet met de onderwijseenheid- of leeronderdeelspecificatie van het informatiemodel. Welke daarvan horen in de uitwisseling op de specificatie, en welke blijven binnen de instelling? (F1-06, `Onderwijseenheid specificatie`)
5. De gewenste leeromgeving is op de conceptplaat een onderwijsruimtetype en daarmee indirect een lokaal, terwijl de onderwijslocatie lokaaltypes aggregeert. Hoort er een relatie tussen onderwijsruimtetype en lokaaltype, zodat de voorsortering op locatie in een stap te leggen is? (F1-06, `Onderwijsruimte type`)
6. Onder een lokaaltype hoort welke faciliteiten en leermiddelen de ruimte biedt, zoals een servicebalie met een bepaalde capaciteit; MORA kent daarvoor faciliteiten. De conceptplaat koppelt leermiddelgroepen aan het leeronderdeel en aan de lesspecificatie, niet aan het lokaal of het lokaaltype. Hoort die koppeling er, zodat een ruimtevraag op faciliteiten te matchen is? (F1-06, `Lokaaltypes`)
7. Het gewenste medewerkercompetentieprofiel staat op de conceptplaat los van competenties, vaardigheden en kennis, terwijl de leeruitkomst die structuur wel kent. Hoort onder het docentprofiel dezelfde skills-structuur, zodat de gevraagde expertise in dezelfde termen staat als wat de student leert? (F1-06, `Gewenst medewerker competentieprofiel`)

Vragen over patronen, schema's, de toetslijst en endpoints horen bij de koppelvlakspecificatie en staan hier niet.

### Invulblad

Per regel één van vier antwoorden: herken ik dit; heet bij ons anders (welke term); hangt bij ons anders (waaronder); ontbreekt. De kolom Beeld draagt het beeld-ID uit de kop erboven.

| Fase | Beeld | Objecttype | Herken | Heet anders | Hangt anders | Ontbreekt |
|---|---|---|---|---|---|---|
| 1 | F1-01 | Kwalificatie dossier | | | | |
| 1 | F1-01 | Kwalificatie | | | | |
| 1 | F1-01 | Kerntaak | | | | |
| 1 | F1-01 | Werkproces | | | | |
| 1 | F1-02 | Examenplan | | | | |
| 1 | F1-02 | Summatieve resultaat structuur | | | | |
| 1 | F1-02 | Cohort / periode | | | | |
| 1 | F1-02 | Examenplan | | | | |
| 1 | F1-03 | Leeruitkomst | | | | |
| 1 | F1-03 | Leeruitkomst | | | | |
| 1 | F1-04 | Leeruitkomst | | | | |
| 1 | F1-04 | Leeruitkomst | | | | |
| 1 | F1-04 | Competenties / Skills | | | | |
| 1 | F1-04 | Vaardigheid | | | | |
| 1 | F1-04 | Kennis | | | | |
| 1 | F1-04 | Inzicht | | | | |
| 1 | F1-05 | Onderwijseenheid specificatie | | | | |
| 1 | F1-05 | Leeruitkomst | | | | |
| 1 | F1-05 | Leeruitkomst | | | | |
| 1 | F1-05 | Leeronderdeel specificatie | | | | |
| 1 | F1-05 | Leeruitkomst | | | | |
| 1 | F1-05 | Leeronderdeel specificatie | | | | |
| 1 | F1-06 | Onderwijseenheid specificatie | | | | |
| 1 | F1-07 | Opleiding specificatie | | | | |
| 1 | F1-07 | Opleidingsprogramma specificatie | | | | |
| 1 | F1-07 | Onderwijseenheid specificatie | | | | |
| 1 | F1-07 | Leeronderdeel specificatie | | | | |
| 1 | F1-07 | Keuzedeelruimte | | | | |
| 1 | F1-07 | Student keuze regelset | | | | |
| 1 | F1-08 | Leeruitkomst | | | | |
| 1 | F1-08 | Leeruitkomst | | | | |
| 1 | F1-08 | Keuzedeel | | | | |
| 1 | F1-08 | Onderwijseenheid specificatie | | | | |
| 1 | F1-08 | Leeronderdeel specificatie | | | | |
| 1 | F1-08 | Leeronderdeel specificatie | | | | |
| 1 | F1-08 | Onderwijseenheid specificatie | | | | |
| 1 | F1-08 | Leeronderdeel specificatie | | | | |
| 1 | F1-08 | Keuzedeel | | | | |
| 1 | F1-08 | Onderwijseenheid specificatie | | | | |
| 1 | F1-08 | Leeronderdeel specificatie | | | | |
| 1 | F1-08 | Leeronderdeel specificatie | | | | |
| 1 | F1-09 | Summatieve resultaat structuur | | | | |
| 1 | F1-09 | Toetsonderdeel specificatie | | | | |
| 1 | F1-09 | Examenonderdeelspecificatie | | | | |
| 1 | F1-09 | Examenonderdeel weging | | | | |
| 1 | F1-09 | Summatief Afrondingscriterium | | | | |
| 1 | F1-10 | Examenonderdeelspecificatie | | | | |
| 2 | F2-01 | Opleidingsprogramma specificatie | | | | |
| 2 | F2-01 | Onderwijseenheid specificatie | | | | |
| 2 | F2-01 | Leeronderdeel specificatie | | | | |
| 2 | F2-01 | Leeronderdeel specificatie | | | | |
| 2 | F2-02 | Verzoek tot Aanbod / Intekening op specificatie | | | | |
| 2 | F2-04 | Opleidingsaanbod van Instelling | | | | |
| 2 | F2-04 | Opleidingaanbod | | | | |
| 2 | F2-04 | Opleidingsprogramma aanbod | | | | |
| 2 | F2-04 | Onderwijseenheid aanbod | | | | |
| 2 | F2-04 | Leergelegenheid | | | | |
| 2 | F2-04 | Toetsgelegenheid | | | | |
| 3 | F3-03 | Persoon | | | | |
| 3 | F3-03 | Aanmelding | | | | |
| 3 | F3-03 | Opleiding aanbod verbintenis | | | | |
| 3 | F3-03 | Opleidingsprogramma aanbod verbintenis | | | | |
| 3 | F3-05 | Student | | | | |
| 3 | F3-05 | Plaatsingsgroep | | | | |
| 3 | F3-05 | Verzoek tot Aanbod / Intekening op specificatie | | | | |
| 3 | F3-07 | Inschrijving | | | | |
| 3 | F3-07 | Opleiding aanbod verbintenis | | | | |
| 3 | F3-07 | Opleidingsprogramma aanbod verbintenis | | | | |
| 4 | F4-01 | Leeronderdeel specificatie | | | | |
| 4 | F4-01 | Les specificatie | | | | |
| 4 | F4-01 | Les specificatie | | | | |
| 4 | F4-08 | Leergelegenheid | | | | |
| 4 | F4-08 | Lesgelegenheid | | | | |
| 4 | F4-08 | Medewerker | | | | |
| 4 | F4-09 | Onderwijseenheid aanbod verbintenis | | | | |
| 4 | F4-09 | Leergelegenheid verbintenis | | | | |
| 4 | F4-09 | Lesgelegenheid verbintenis | | | | |
| 4 | F4-09 | Opleidingsprogramma aanbod verbintenis | | | | |
| 5 | F5-01 | Lesgelegenheid verbintenis | | | | |
| 5 | F5-01 | Aanwezigheid | | | | |
| 5 | F5-01 | Lesgelegenheid resultaat | | | | |
| 5 | F5-02 | Toetsgelegenheid verbintenis | | | | |
| 5 | F5-02 | Toetsgelegenheid verbintenis | | | | |
| 5 | F5-03 | Formatieve resultaat structuur | | | | |
| 5 | F5-03 | Toetsonderdeel weging | | | | |
| 5 | F5-03 | Toetsgelegenheid resultaat | | | | |
| 5 | F5-03 | Formatief resultaat | | | | |
| 5 | F5-03 | Formatieve beoordeling | | | | |
| 5 | F5-03 | Persoonlijke ontwikkeling | | | | |
| 5 | F5-03 | Leergelegenheid resultaat | | | | |
| 5 | F5-05 | Onderwijseenheid resultaat | | | | |
| 5 | F5-05 | Onderwijseenheid aanbod | | | | |
| 5 | F5-05 | Summatieve resultaat structuur | | | | |
| 6 | F6-01 | Keuzedeelaanbod | | | | |
| 6 | F6-03 | Keuzedeel aanbod verbintenis | | | | |
| 6 | F6-05 | Keuzedeelaanbod | | | | |
| 6 | F6-07 | Keuzedeel aanbod verbintenis | | | | |
| 7 | F7-01 | Plaatsingsgroep | | | | |
| 7 | F7-02 | Onderwijseenheid aanbod verbintenis | | | | |
| 7 | F7-04 | Onderwijseenheid aanbod | | | | |
| 8 | F8-01 | Examengelegenheid | | | | |
| 8 | F8-02 | Examengelegenheid verbintenis | | | | |
| 8 | F8-03 | Examengelegenheid resultaat | | | | |
| 8 | F8-05 | Summatief resultaat | | | | |
| 8 | F8-05 | Summatieve beoordeling | | | | |
| 8 | F8-05 | Opleidingsprogramma resultaat | | | | |
| 8 | F8-05 | Keuzedeel resultaat | | | | |
| 8 | F8-07 | Opleiding aanbod resultaat | | | | |
| 8 | F8-07 | Waarde document (diploma / certificaat) | | | | |

## Regelregister

Elke regel onder het ID en de titel van haar beeld (fase, stap, bestand) met de bron. Verwijs naar een beeld met zijn ID en naar een regel met dat ID en het objecttype.

**F1-01 - Het kwalificatiedossier ontleed** (fase 1, Kwalificatiedossier analyseren; [f1-01-het-kwalificatiedossier-ontleed.svg](img/regels/f1-01-het-kwalificatiedossier-ontleed.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Kwalificatie dossier | Apothekersassistent, crebo 23450 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r52](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L52) en [r1026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1026) |
| ontstaat | Kwalificatie | Apothekersassistent, 27141 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r52](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L52) en [r1027](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1027) |
| ontstaat | Kerntaak | B1-K1 Biedt farmaceutische patiëntenzorg | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1038](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1038) |
| ontstaat | Werkproces | B1-K1-W1 Neemt de zorg-/adviesvraag in behandeling | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1045](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1045) |

**F1-02 - Examenplan, eerste resultaatstructuur en cohort** (fase 1, Examenplan vaststellen; [f1-02-examenplan-eerste-resultaatstructuur-en-cohort.svg](img/regels/f1-02-examenplan-eerste-resultaatstructuur-en-cohort.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Examenplan | Examenplan Apothekersassistent, cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): een initieel examenplan; [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): op basis van het examenplan uit fase 1 |
| ontstaat | Summatieve resultaat structuur | Eerste opzet: kerntaken en keuzedelen, alle voldoende | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), resultaatstructuur (08b4656d): aggregatie allenVoldoende |
| ontstaat | Cohort / periode | Cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken) en scenario: cohort 2026; ontwerpkeuze 17 |
| ontstaat | Examenplan | Keuzedeeleis: 720 SBU, waarvan een verdiepend keuzedeel | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r52](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L52) (720 SBU keuzedelen verplicht voor niveau 4); het examenplan staat buiten de uitwisseling, de eis erin is de aanleiding voor de latere keuzeregelset |

**F1-03 - Leeruitkomsten uit het dossier, in de stem van de instelling** (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten; [f1-03-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.svg](img/regels/f1-03-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Leeruitkomst | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving (kerntaakniveau) | [informatiemodel.md](informatiemodel.md), familie Onderwijskundig kader instelling: de invulling door de instelling van de beoogde leeruitkomsten; leerroute-1-regulier.md, [r1046](informatiemodel.md?plain=1#L1046) en [r1052](informatiemodel.md?plain=1#L1052) (leervorm simulatie, theorie) en [r1092](informatiemodel.md?plain=1#L1092) |
| ontstaat | Leeruitkomst | Voert baliegesprek en triage uit in de simulatieapotheek, onderbouwd met theorie (werkprocesniveau) | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r620](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L620) (Werkproces 1..* Leeruitkomst) en [r1092](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1092); [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1021) (onderwijseenheden corresponderen met kerntaken, leeronderdelen met werkprocessen) |

**F1-04 - De leeruitkomst in CompetentNL-skills** (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten; [f1-04-de-leeruitkomst-in-competentnl-skills.svg](img/regels/f1-04-de-leeruitkomst-in-competentnl-skills.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Leeruitkomst | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving (kerntaakniveau) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader, drie lagen (6 verzamelconcepten, 24 generieke, 128 specifieke vaardigheden); cnlo:EducationalNorm (Opleidingsnorm) schrijft vaardigheden voor (cnlo:prescribes); leerroute-1-regulier.md, r1092 |
| verandert | Leeruitkomst | Voert baliegesprek en triage uit in de simulatieapotheek, onderbouwd met theorie (werkprocesniveau) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader, drie lagen (6 verzamelconcepten, 24 generieke, 128 specifieke vaardigheden); cnlo:EducationalNorm (Opleidingsnorm) schrijft vaardigheden voor (cnlo:prescribes); leerroute-1-regulier.md, r1092 |
| ontstaat | Competenties / Skills | Vaardigheden bij deze leeruitkomst (CompetentNL) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader, drie lagen (6 verzamelconcepten, 24 generieke, 128 specifieke vaardigheden); cnlo:KnowledgeArea (Kennisgebied) met een ISCED-F detailed field als ouder; cnlo:EducationalNorm (Opleidingsnorm) schrijft vaardigheden en kennisgebieden voor (cnlo:prescribes) |
| ontstaat | Vaardigheid | Communicatieve vaardigheden (CompetentNL laag 2) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader, drie lagen (6 verzamelconcepten, 24 generieke, 128 specifieke vaardigheden); cnlo:KnowledgeArea (Kennisgebied) met een ISCED-F detailed field als ouder; cnlo:EducationalNorm (Opleidingsnorm) schrijft vaardigheden en kennisgebieden voor (cnlo:prescribes) |
| ontstaat | Kennis | Farmacie (CompetentNL kennisgebied op ISCED-F 0916) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader, drie lagen (6 verzamelconcepten, 24 generieke, 128 specifieke vaardigheden); cnlo:KnowledgeArea (Kennisgebied) met een ISCED-F detailed field als ouder; cnlo:EducationalNorm (Opleidingsnorm) schrijft vaardigheden en kennisgebieden voor (cnlo:prescribes); ISCED-F 2013, detailed field 0916 Pharmacy |
| ontstaat | Inzicht | Werking en risico van een geneesmiddel bij de vraag aan de balie | geen bron, keuze van het voorbeeld: de plaat kent inzicht als apart deel van competenties en skills, CompetentNL niet |

**F1-05 - De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten** (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten; [f1-05-de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten.svg](img/regels/f1-05-de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Onderwijseenheid specificatie | Blok B1-K1 Biedt farmaceutische patiëntenzorg | informatiemodel.json: Onderwijseenheid specificatie naar Leeruitkomst (associatie); leerroute-1-regulier.md, r576 en r1021 (onderwijseenheden corresponderen met kerntaken) |
| verandert | Leeruitkomst | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving (kerntaakniveau) | informatiemodel.json: Onderwijseenheid specificatie naar Leeruitkomst (associatie); leerroute-1-regulier.md, r621 |
| verandert | Leeruitkomst | Voert baliegesprek en triage uit in de simulatieapotheek, onderbouwd met theorie (werkprocesniveau) | informatiemodel.json: Leeruitkomst aggregeert Leeruitkomst, Leeronderdeel specificatie naar Leeruitkomst; leerroute-1-regulier.md, r620, r1021 en r1044 |
| verandert | Leeronderdeel specificatie | B1-K1-W1 Baliegesprek en triage | informatiemodel.json: Leeruitkomst aggregeert Leeruitkomst, Leeronderdeel specificatie naar Leeruitkomst; leerroute-1-regulier.md, r620, r1021 en r1044 |
| verandert | Leeruitkomst | Voert medicatiebewaking uit onder begeleiding in de leerapotheek (werkprocesniveau) | informatiemodel.json: Leeruitkomst aggregeert Leeruitkomst; leerroute-1-regulier.md, r1051 (werkproces B1-K1-W2) |
| verandert | Leeronderdeel specificatie | B1-K1-W2 Medicatiebewaking | informatiemodel.json: Onderwijseenheid specificatie aggregeert Leeronderdeel specificatie, Leeronderdeel specificatie naar Leeruitkomst; leerroute-1-regulier.md, r1051 |

**F1-06 - De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen** (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten; [f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen.svg](img/regels/f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Onderwijseenheid specificatie | Blok B1-K1, met vorm, ruimte, mensen en middelen | informatiemodel.json: Onderwijseenheid specificatie aggregeert Leeronderdeel specificatie en verwijst naar Leeruitkomst; leerroute-1-regulier.md, r1021 (op leeronderdeelniveau staan de organiseerbaarheidswaarden) |
| ontstaat (conceptplaat) | Leervormstrategie | Leren door te doen in een levensechte omgeving, theorie ondersteunend | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Strategisch kader instelling, Leervormstrategie naar Onderwijsvorm specificatie |
| ontstaat (conceptplaat) | Leerdoel | Zelfstandig farmaceutische patiëntenzorg bieden in een levensechte setting | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Kerntaak 'Word onderwijskundig vertaald tot' Leerdoel; leerroute-1-regulier.md, r1046 en r1052 |
| ontstaat (conceptplaat) | Onderwijsvorm specificatie | Simulatie in de leerapotheek, theorie ondersteunend | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Leeruitkomst naar Onderwijsvorm specificatie; leerroute-1-regulier.md, r1046 en r1052 |
| ontstaat (conceptplaat) | Gewenste Onderwijskundige Leeromgeving | Simulatiegeschikte praktijkruimte voor 24 studenten, balie-opstelling mogelijk | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Onderwijsvorm specificatie naar Gewenste Onderwijskundige Leeromgeving, Gewenste Onderwijskundige Leeromgeving is een Onderwijsruimte type; leerroute-1-regulier.md, r1048 |
| ontstaat (conceptplaat) | Onderwijsruimte type | Praktijkruimte met baliesimulatie | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Gewenste Onderwijskundige Leeromgeving is een Onderwijsruimte type, Onderwijsruimte type is een Lokaal |
| ontstaat (conceptplaat) | Onderwijs locatie | Vestiging Zuid | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Onderwijs locatie aggregeert Lokaaltypes |
| ontstaat (conceptplaat) | Lokaaltypes | Praktijklokalen met servicebalie, 24 plaatsen | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Onderwijs locatie aggregeert Lokaaltypes |
| ontstaat (conceptplaat) | Gewenst medewerker competentieprofiel | Apothekersassistent-docent: didactisch en communicatief (CompetentNL laag 2), farmacie (ISCED-F 0916) | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Gewenst medewerker competentieprofiel naar Onderwijsvorm specificatie; CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |
| ontstaat (conceptplaat) | Medewerker Type / Expertise Profiel | Docent farmacie met baliepraktijk (expertiseprofiel) | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Medewerker Type / Expertise Profiel 'Heeft meerdere' Gewenst medewerker competentieprofiel |
| ontstaat (conceptplaat) | Competenties / skills | Profiel docent farmacie: de skills die de instelling bij dit type verwacht | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Competenties / skills aggregeert Vaardigheid, Kennis en Inzicht; CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |
| ontstaat (conceptplaat) | Vaardigheid | Didactische en communicatieve vaardigheden (CompetentNL laag 2) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |
| ontstaat (conceptplaat) | Kennis | Farmacie (ISCED-F 0916) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |
| ontstaat (conceptplaat) | Collectie van Medewerkertypes | Docent farmacie en praktijkbegeleider | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Leeronderdeel / Leeractiviteit specificatie aggregeert Collectie van Medewerkertypes |
| ontstaat (conceptplaat) | Studiebelasting en begeleide onderwijstijd indicatie | BOT 50 / OOT 50 SBU | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Studiebelasting en begeleide onderwijstijd indicatie naar Onderwijsvorm specificatie; leerroute-1-regulier.md, r1052 |
| ontstaat (conceptplaat) | Collectie van Leermiddelgroepen | Leermiddelen voor de baliesimulatie | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Leeronderdeel / Leeractiviteit specificatie aggregeert Collectie van Leermiddelgroepen |
| ontstaat (conceptplaat) | Leermiddelgroep | Apotheekbalie-opstelling, receptenlijnsysteem, oefenmedicatie | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Collectie van Leermiddelgroepen aggregeert Leermiddelgroep |

**F1-07 - De opleidingsspecificatie met programma, eenheden en keuzedeelruimte** (fase 1, Opleidingsspecificatie met programma en eenheden beschrijven; [f1-07-de-opleidingsspecificatie-met-programma-eenheden-en-keuzedeelruimte.svg](img/regels/f1-07-de-opleidingsspecificatie-met-programma-eenheden-en-keuzedeelruimte.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Opleiding specificatie | Apothekersassistent, versie 2026.1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1024](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1024) tot [1030](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1030) |
| ontstaat | Opleidingsprogramma specificatie | BOL voltijd, diplomaprogramma | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1032](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1032) tot [1036](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1036) |
| ontstaat | Onderwijseenheid specificatie | Blok B1-K1 Biedt farmaceutische patiëntenzorg | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1038](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1038) tot [1043](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1043) |
| ontstaat | Leeronderdeel specificatie | B1-K1-W1 Baliegesprek en triage: simulatie in de leerapotheek, theorie ondersteunend, grofmazig | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1021) (organiseerbaarheidswaarden op leeronderdeelniveau), [r1045](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1045) tot [1052](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1052) (leervorm simulatie, ruimtetype balie-simulatie) |
| ontstaat | Keuzedeelruimte | 720 SBU, mbo-4: te vullen met 480 SBU verdiepend en 240 SBU generiek | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1059](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1059) en [r1072](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1072) |
| ontstaat | Student keuze regelset | Kiesbare keuzedelen: K0037 Farmaceutische Patientenzorg (480 SBU, verdiepend) of K0262 ARBO, kwaliteitszorg en hulpverlening (240 SBU, generiek) | K0037-farmaceutische-patientenzorg.md (keuzedeel mbo K0037, 480 SBU, aard verdiepend, gevalideerd 26-11-2015); leerroute-1-regulier.md, r52 (720 SBU keuzedelen verplicht voor niveau 4); de eis komt uit het examenplan (F1-02) |

**F1-08 - Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen** (fase 1, Keuzedeelprogramma als eigen specificatie vormgeven; [f1-08-het-keuzedeel-als-eigen-programmaspecificatie-met-kerntaken-en-werkprocessen.svg](img/regels/f1-08-het-keuzedeel-als-eigen-programmaspecificatie-met-kerntaken-en-werkprocessen.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Leeruitkomst | Draagt bij aan kwaliteitszorg en arbeidsomstandigheden op de eigen werkplek (kerntaakniveau, keuzedeel) | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Leeruitkomst | Levert een bijdrage aan de inrichting van het kwaliteitszorgsysteem (werkprocesniveau, keuzedeel) | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Keuzedeel | K0262 ARBO, kwaliteitszorg en hulpverlening geschikt voor niveau 3 (240 SBU) | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Onderwijseenheid specificatie | D1-K1 Draagt bij aan kwaliteitszorg en arbeidsomstandigheden | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Leeronderdeel specificatie | D1-K1-W1 Bijdrage aan de inrichting van het kwaliteitszorgsysteem | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Leeronderdeel specificatie | D1-K1-W2 Risico-inventarisatie en -evaluatie | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Onderwijseenheid specificatie | D1-K2 Verleent EHBO en BHV | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Leeronderdeel specificatie | D1-K2-W1 Hulp bij calamiteiten | K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md (keuzedeel mbo K0262, gevalideerd 10-11-2015); leerroute-1-regulier.md, r1072 tot 1080 |
| ontstaat | Keuzedeel | K0037 Farmaceutische Patientenzorg (480 SBU, verdiepend) | K0037-farmaceutische-patientenzorg.md (keuzedeel mbo K0037, 480 SBU, aard verdiepend, gevalideerd 26-11-2015) |
| ontstaat | Onderwijseenheid specificatie | D1-K1 Voert farmaceutische patientenzorg uit | K0037-farmaceutische-patientenzorg.md (keuzedeel mbo K0037, 480 SBU, aard verdiepend, gevalideerd 26-11-2015) |
| ontstaat | Leeronderdeel specificatie | D1-K1-W1 Medicatieoverzicht | K0037-farmaceutische-patientenzorg.md (keuzedeel mbo K0037, 480 SBU, aard verdiepend, gevalideerd 26-11-2015) |
| ontstaat | Leeronderdeel specificatie | D1-K1-W2 Zorg aan specifieke doelgroepen | K0037-farmaceutische-patientenzorg.md (keuzedeel mbo K0037, 480 SBU, aard verdiepend, gevalideerd 26-11-2015) |

**F1-09 - Toetsonderdelen, wegingen en afrondingscriterium** (fase 1, Toetsonderdelen en resultaatstructuur uit het examenplan afleiden; [f1-09-toetsonderdelen-wegingen-en-afrondingscriterium.svg](img/regels/f1-09-toetsonderdelen-wegingen-en-afrondingscriterium.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Summatieve resultaat structuur | Resultaatstructuur Apothekersassistent, alle onderdelen voldoende | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), resultaatstructuur (08b4656d): aggregatie allenVoldoende |
| ontstaat | Toetsonderdeel specificatie | Praktijktoets baliegesprek (OSCE), summatief | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1114](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1114) tot [1117](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1117) |
| ontstaat | Examenonderdeelspecificatie | Proeve van bekwaamheid B1-K1 | geen bron, keuze van het voorbeeld: het kaderscenario noemt een examenplan zonder onderdelen |
| ontstaat | Examenonderdeel weging | Proeve van bekwaamheid B1-K1: weging 2 | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), toetsonderdelen (941f180d): weging 2 |
| ontstaat | Summatief Afrondingscriterium | Alle kerntaken en de keuzedelen voldoende | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), resultaatstructuur: aggregatie allenVoldoende |

**F1-10 - De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte** (fase 1, Exameninstrumenten bepalen, inkopen of construeren; [f1-10-de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte.svg](img/regels/f1-10-de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Examenonderdeelspecificatie | Proeve van bekwaamheid B1-K1, met vorm, instrumenten en ruimte | informatiemodel.json: Examenonderdeelspecificatie naar Leeruitkomst, Examenonderdeelspecificatie is een Toetsonderdeel specificatie; leerroute-1-regulier.md, r416 tot r426 (de examencommissie bepaalt de benodigde instrumenten en het materiaal, besluit inkopen of construeren en stelt specificatie, materiaal en instrumenten vast) |
| ontstaat (conceptplaat) | Toetsvormspecificatie | Proeve van bekwaamheid in de simulatieapotheek | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Toetsvormspecificatie is een Onderwijsvorm specificatie en een Toetsvorm; leerroute-1-regulier.md, r416 tot r426 (de examencommissie stelt examenplan en examenspecificaties op, bepaalt de benodigde instrumenten en het materiaal, besluit inkopen of construeren, en stelt specificatie, materiaal en instrumenten vast) |
| ontstaat (conceptplaat) | Toetsvorm | Praktijkbeoordeling aan de balie, 45 minuten | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Toetsvormspecificatie is een Toetsvorm, Toetsvorm heeft een Toets en verwijst naar Toetsinstrument |
| ontstaat (conceptplaat) | Toetsinstrument | Beoordelingsformulier met rubric, ingekocht bij de branche | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Toetsvorm naar Toetsinstrument; Toetsinstrument is een Collectie van Leermiddelgroepen; leerroute-1-regulier.md, r416 tot r426 (de examencommissie stelt examenplan en examenspecificaties op, bepaalt de benodigde instrumenten en het materiaal, besluit inkopen of construeren, en stelt specificatie, materiaal en instrumenten vast) |
| ontstaat (conceptplaat) | Leermiddelgroep | Examenmateriaal: oefenrecepten, casuskaarten, baliemateriaal | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Collectie van Leermiddelgroepen aggregeert Leermiddelgroep; leerroute-1-regulier.md, r416 tot r426 (de examencommissie bepaalt de benodigde instrumenten en het materiaal, besluit inkopen of construeren en stelt specificatie, materiaal en instrumenten vast) |
| ontstaat (conceptplaat) | Onderwijsruimte type | Praktijkruimte met baliesimulatie, afsluitbaar voor examinering | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Onderwijsruimte type |
| ontstaat (conceptplaat) | Gewenst medewerker competentieprofiel | Examinator met baliepraktijk en toetsbekwaamheid | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Gewenst medewerker competentieprofiel naar Toetsvormspecificatie |
| ontstaat (conceptplaat) | Competenties / skills | Profiel examinator: de skills die de instelling bij dit type verwacht | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Competenties / skills aggregeert Vaardigheid, Kennis en Inzicht; CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |
| ontstaat (conceptplaat) | Vaardigheid | Beoordelen en feedback geven (CompetentNL laag 2) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |
| ontstaat (conceptplaat) | Kennis | Farmacie en toetsing (ISCED-F 0916) | CompetentNL ontologie 2.1.0 (competentnl.nl, TTL, gewijzigd 14 juli 2026): cnlo:HumanCapability (Vaardigheid) gelaagd via skos:broader; cnlo:KnowledgeArea (Kennisgebied) op ISCED-F |

**F1-11 - De opleiding zoals ontworpen naar de catalogus** (fase 1, Grofmazig resultaat publiceren naar de onderwijscatalogus; [f1-11-de-opleiding-zoals-ontworpen-naar-de-catalogus.svg](img/regels/f1-11-de-opleiding-zoals-ontworpen-naar-de-catalogus.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Leeruitkomst | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving (kerntaakniveau) | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): Curriculum-ontwerptool naar OC, alles op grofmazig niveau; AGENTS.md: de leeruitkomst is de sleutel, specificaties en de resultaatstructuur verwijzen ernaar |
| stroomt | Leeruitkomst | Voert baliegesprek en triage uit in de simulatieapotheek (werkprocesniveau) | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): Curriculum-ontwerptool naar OC, alles op grofmazig niveau |
| stroomt | Competenties / Skills | Vaardigheden bij de leeruitkomst (CompetentNL) | CompetentNL ontologie 2.1.0: cnlo:HumanCapability, cnlo:KnowledgeArea; informatiemodel.md: Leeruitkomst is een specialisatie van Competenties / Skills |
| stroomt | Vaardigheid | Communicatieve vaardigheden (laag 2) | CompetentNL ontologie 2.1.0: cnlo:HumanCapability, cnlo:KnowledgeArea; informatiemodel.md: Leeruitkomst is een specialisatie van Competenties / Skills |
| stroomt | Kennis | Farmacie (ISCED-F 0916) | CompetentNL ontologie 2.1.0: cnlo:HumanCapability, cnlo:KnowledgeArea; informatiemodel.md: Leeruitkomst is een specialisatie van Competenties / Skills |
| stroomt | Inzicht | Werking en risico van een geneesmiddel | geen bron, keuze van het voorbeeld |
| stroomt | Opleiding specificatie | Apothekersassistent, versie 2026.1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): Curriculum-ontwerptool naar OC, alles op grofmazig niveau |
| stroomt | Opleidingsprogramma specificatie | BOL voltijd | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): Curriculum-ontwerptool naar OC, alles op grofmazig niveau |
| stroomt | Onderwijseenheid specificatie | Blok B1-K1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): Curriculum-ontwerptool naar OC, alles op grofmazig niveau |
| stroomt | Leeronderdeel specificatie | B1-K1-W1, grofmazig | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): Curriculum-ontwerptool naar OC, alles op grofmazig niveau |
| stroomt | Keuzedeelruimte | 720 SBU, mbo-4 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1059](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1059) en [r1072](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1072) |
| stroomt | Student keuze regelset | Kiesbare keuzedelen voor Apothekersassistent | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), regelsets[0] (e4037953) |
| stroomt | Summatieve resultaat structuur | Resultaatstructuur Apothekersassistent | keuze van het voorbeeld: de resultaatstructuur ontstaat in de ontwerptool en gaat met de specificatie mee |
| stroomt | Toetsonderdeel specificatie | Praktijktoets baliegesprek (OSCE) | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen): toetsonderdeel-specificatie |
| stroomt | Examenonderdeelspecificatie | Proeve van bekwaamheid B1-K1 | geen bron, keuze van het voorbeeld |
| stroomt | Summatief Afrondingscriterium | Alle kerntaken en de keuzedelen voldoende | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), resultaatstructuur: aggregatie allenVoldoende |

**F1-12 - Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)** (fase 1, Grofmazig resultaat publiceren naar de onderwijscatalogus; [f1-12-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat.svg](img/regels/f1-12-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt (conceptplaat) | Onderwijsvorm specificatie | Simulatie in de leerapotheek, theorie ondersteunend | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Gewenste Onderwijskundige Leeromgeving | Balie-simulatie in het skillslab | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Gewenst medewerker competentieprofiel | Apothekersassistent-docent met baliepraktijk | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Studiebelasting en begeleide onderwijstijd indicatie | BOT 50 / OOT 50 SBU | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Toetsvormspecificatie | Proeve van bekwaamheid in de simulatieapotheek | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Toetsvormspecificatie is een Onderwijsvorm specificatie |
| stroomt (conceptplaat) | Toetsinstrument | Beoordelingsformulier met rubric | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Toetsvorm naar Toetsinstrument; Toetsinstrument is een Collectie van Leermiddelgroepen |
| stroomt (conceptplaat) | Gewenst medewerker competentieprofiel | Examinator met baliepraktijk en toetsbekwaamheid | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Gewenst medewerker competentieprofiel naar Toetsvormspecificatie |
| stroomt (conceptplaat) | Onderwijsvorm specificatie | Simulatie in de leerapotheek, theorie ondersteunend | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Gewenste Onderwijskundige Leeromgeving | Balie-simulatie in het skillslab | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Gewenst medewerker competentieprofiel | Apothekersassistent-docent met baliepraktijk | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Studiebelasting en begeleide onderwijstijd indicatie | BOT 50 / OOT 50 SBU | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |

**F2-01 - De specificatie planbaar gemaakt** (fase 2, Specificatie aanvullen tot planbare specificatie; [f2-01-de-specificatie-planbaar-gemaakt.svg](img/regels/f2-01-de-specificatie-planbaar-gemaakt.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Opleidingsprogramma specificatie | BOL voltijd, planbaar: tijdvensters en capaciteit | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken): aangevuld tot planbare specificatie |
| verandert | Onderwijseenheid specificatie | Blok B1-K1, leerjaar 1: plek in de opleidingsduur en groepsgrootte | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1021) (op leeronderdeelniveau staan de organiseerbaarheidswaarden: BOT/OOT, BPV, ruimtetype, expertiseprofiel) en [r713](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L713) (planbaar als rijpheidskenmerk van de specificatie) |
| verandert | Leeronderdeel specificatie | B1-K1-W1: BOT 50 / OOT 50 SBU, praktijkruimte, docent farmacie | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1021) (op leeronderdeelniveau staan de organiseerbaarheidswaarden: BOT/OOT, BPV, ruimtetype, expertiseprofiel) en [r713](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L713) (planbaar als rijpheidskenmerk van de specificatie) |
| verandert | Leeronderdeel specificatie | B1-K1-W2: BOT 30 / OOT 70 SBU, praktijkruimte, docent farmacie | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1021) (op leeronderdeelniveau staan de organiseerbaarheidswaarden: BOT/OOT, BPV, ruimtetype, expertiseprofiel) en [r713](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L713) (planbaar als rijpheidskenmerk van de specificatie) |

**F2-02 - Het verzoek om onderwijsaanbod** (fase 2, Planningssysteem verzoeken om onderwijsaanbod; [f2-02-het-verzoek-om-onderwijsaanbod.svg](img/regels/f2-02-het-verzoek-om-onderwijsaanbod.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Verzoek tot Aanbod / Intekening op specificatie | Planopgave Apothekersassistent, cohort 2026 | geen bron, keuze van het voorbeeld: op de plaat een objecttype, in het kaderscenario een handeling van OC |

**F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning** (fase 2, Planningssysteem verzoeken om onderwijsaanbod; [f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.svg](img/regels/f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Verzoek tot Aanbod / Intekening op specificatie | Planopgave Apothekersassistent, cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken): OC verzoekt het Planningssysteem |
| stroomt | Opleiding specificatie | Apothekersassistent, versie 2026.1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken) |
| stroomt | Opleidingsprogramma specificatie | BOL voltijd, planbaar | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken) |
| stroomt | Onderwijseenheid specificatie | Blok B1-K1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken) |
| stroomt | Leeronderdeel specificatie | B1-K1-W1 Baliegesprek en triage | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken) |
| stroomt | Leeronderdeel specificatie | B1-K1-W2 Medicatiebewaking | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken); leerroute-1-regulier.md, [r1051](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1051) (leeronderdeel B1-K1-W2) |
| stroomt (conceptplaat) | Onderwijsvorm specificatie | Simulatie in de leerapotheek, theorie ondersteunend | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Gewenste Onderwijskundige Leeromgeving | Balie-simulatie in het skillslab | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Gewenst medewerker competentieprofiel | Apothekersassistent-docent met baliepraktijk | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |
| stroomt (conceptplaat) | Studiebelasting en begeleide onderwijstijd indicatie | BOT 50 / OOT 50 SBU | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat) |

**F2-04 - Het aanbod gepland: opleiding, programma, eenheid, gelegenheid** (fase 2, Haalbaarheid bepalen en aanbod plannen; [f2-04-het-aanbod-gepland-opleiding-programma-eenheid-gelegenheid.svg](img/regels/f2-04-het-aanbod-gepland-opleiding-programma-eenheid-gelegenheid.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Opleidingsaanbod van Instelling | ROC Het Voorbeeld: ambitie en verwachte instroom voor cohort 2026 | geen bron, keuze van het voorbeeld: het objecttype heeft geen instantie in het kaderscenario; leerroute-1-regulier.md, r657 (drie stadia van onderwijsaanbod, parallel aan meerjaren-, jaar- en periodeplanning) |
| ontstaat | Opleidingaanbod | Apothekersassistent 2026: vier perioden, 120 plaatsen | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), aanbodInstanties[0] (7aa6609f); leerroute-1-regulier.md, [r738](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md?plain=1#L738) (aanbod is minimaal gepland zodra perioden en capaciteit vastliggen) en [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md?plain=1#L1021) (stadium 2a, nog zonder lokalen en docenten) |
| ontstaat | Opleidingsprogramma aanbod | Regulier BOL 2026: 18 tot 120 studenten | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), aanbodInstanties[1] (8c494250); leerroute-1-regulier.md, [r738](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md?plain=1#L738) (aanbod is minimaal gepland zodra perioden en capaciteit vastliggen) en [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md?plain=1#L1021) (stadium 2a, nog zonder lokalen en docenten) |
| ontstaat | Onderwijseenheid aanbod | B1-K1, leerjaar 1, periode 1 tot 4 | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), aanbodInstanties[2] (04af26e6); leerroute-1-regulier.md, [r738](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md?plain=1#L738) (aanbod is minimaal gepland zodra perioden en capaciteit vastliggen) en [r1021](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md?plain=1#L1021) (stadium 2a, nog zonder lokalen en docenten) |
| ontstaat | Leergelegenheid | B1-K1-W1, periode 1, twee groepen van 24 | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), aanbodInstanties[3] (04070a96) |
| ontstaat | Toetsgelegenheid | Praktijktoets baliegesprek (OSCE), einde periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1114](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1114) tot [1117](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1117) |

**F2-05 - Ruimtes en mensen op de specificatie (conceptplaat)** (fase 2, Haalbaarheid bepalen en aanbod plannen; [f2-05-ruimtes-en-mensen-op-de-specificatie-conceptplaat.svg](img/regels/f2-05-ruimtes-en-mensen-op-de-specificatie-conceptplaat.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat (conceptplaat) | Lokaaltypes | Balie-simulatie (skillslab), 24 plaatsen | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Lokaaltypes naar Schaarste van middelen; leerroute-1-regulier.md, r723 en r736 (simulatieruimte apotheekbalie, max. 24 studenten) |
| ontstaat (conceptplaat) | Schaarste van middelen | Twee simulatieruimtes voor drie cohorten | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Schaarste van middelen naar Onderwijsaanbod Model |
| ontstaat (conceptplaat) | Onderwijsaanbod Model | Jaarplan 2026-2027: vier perioden, groepen van 24 | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Planning bevat Onderwijsaanbod Model; leerroute-1-regulier.md, Fase 2: strategische jaarplanning |
| ontstaat (conceptplaat) | Schaartste van mensen | Drie apothekersassistent-docenten met baliepraktijk | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Schaartste van mensen naar Onderwijsaanbod Model (naam letterlijk van de conceptplaat) |
| ontstaat (conceptplaat) | Medewerker | Docent 4711, apothekersassistent-docent | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Medewerker naar Schaartste van mensen |

**F2-06 - Examenplanning uit de resultaatstructuur (conceptplaat)** (fase 2, Haalbaarheid bepalen en aanbod plannen; [f2-06-examenplanning-uit-de-resultaatstructuur-conceptplaat.svg](img/regels/f2-06-examenplanning-uit-de-resultaatstructuur-conceptplaat.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat (conceptplaat) | Jaarplanning | Jaarplanning 2026-2027 | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Planning bevat Jaarplanning; Jaarplanning naar Jaarplanning examens |
| ontstaat (conceptplaat) | Jaarplanning examens | Examenmomenten cohort 2026 | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Jaarplanning naar Jaarplanning examens |
| ontstaat (conceptplaat) | Examenmoment | Proeve van bekwaamheid B1-K1, periode 12 | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Jaarplanning examens 'bestaat uit' Examenmoment |
| ontstaat (conceptplaat) | Examen instrument | Beoordelingsformulier proeve B1-K1 | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Examenmoment 'Afgenomen tijdens' Examen instrument |
| ontstaat (conceptplaat) | Examen | Proeve van bekwaamheid B1-K1 | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Examen instrument 'Wordt afgenomen door middel van' Examen; Examen 'Functionele koppeling aan' Summatieve resultaat structuur; Examenplan 'is uitgewekt in' Examen (labels letterlijk van de conceptplaat) |

**F2-07 - Het geplande aanbod terug naar de catalogus** (fase 2, Gepland aanbod terugleveren aan de onderwijscatalogus; [f2-07-het-geplande-aanbod-terug-naar-de-catalogus.svg](img/regels/f2-07-het-geplande-aanbod-terug-naar-de-catalogus.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Opleidingsaanbod van Instelling | ROC Het Voorbeeld | informatiemodel.json: Opleidingsaanbod van Instelling aggregeert Opleidingaanbod; leerroute-1-regulier.md, r657 |
| stroomt | Opleidingaanbod | Apothekersassistent 2026: vier perioden, 120 plaatsen | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken): Planning naar OC (opleidingsaanbod als planbaar resultaat); informatiemodel.json: de specificatie is geassocieerd met haar aanbod; het verzoek leidt tot aanbod |
| stroomt | Opleidingsprogramma aanbod | Regulier BOL 2026: 18 tot 120 studenten | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken); informatiemodel.json: de specificatie is geassocieerd met haar aanbod; het verzoek leidt tot aanbod |
| stroomt | Onderwijseenheid aanbod | B1-K1, leerjaar 1, periode 1 tot 4 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken): planbaar aanbod, periode en capaciteit; informatiemodel.json: de specificatie is geassocieerd met haar aanbod; het verzoek leidt tot aanbod |
| stroomt | Leergelegenheid | B1-K1-W1, periode 1, twee groepen van 24 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken): planbaar aanbod; informatiemodel.json: de specificatie is geassocieerd met haar aanbod; het verzoek leidt tot aanbod |
| stroomt | Toetsgelegenheid | Praktijktoets baliegesprek (OSCE), einde periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 2](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-2--publiceren-en-planbaar-maken): planbaar aanbod; informatiemodel.json: de specificatie is geassocieerd met haar aanbod; het verzoek leidt tot aanbod |

**F3-01 - Aanmeldbaar aanbod naar de kernregistratie** (fase 3, Orienteren op het gepubliceerde aanbod; [f3-01-aanmeldbaar-aanbod-naar-de-kernregistratie.svg](img/regels/f3-01-aanmeldbaar-aanbod-naar-de-kernregistratie.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Opleidingsprogramma aanbod | Regulier BOL 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing): OC naar Intakesysteem (aanbod om op te orienteren) |

**F3-02 - Aanmeldbaar aanbod van de kernregistratie naar AII** (fase 3, Orienteren op het gepubliceerde aanbod; [f3-02-aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii.svg](img/regels/f3-02-aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Opleidingsprogramma aanbod | Regulier BOL 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing): OC naar Intakesysteem (aanbod om op te orienteren); persona_jochem.md, [r74](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L74) (aanmeldsysteem CAMBO/AII); keuze van de sectorarchitect: via de kernregistratie |

**F3-03 - Jochem meldt zich aan: aanmelding en verbintenissen** (fase 3, Aanmelden via het intakesysteem; [f3-03-jochem-meldt-zich-aan-aanmelding-en-verbintenissen.svg](img/regels/f3-03-jochem-meldt-zich-aan-aanmelding-en-verbintenissen.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Persoon | Jochem, 17, na het vmbo | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r52](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L52): Jochem, 17, na het vmbo |
| ontstaat | Aanmelding | April 2026, Apothekersassistent BOL | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing); persona_jochem.md, [r74](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L74) (aanmeldsysteem CAMBO/AII) |
| ontstaat | Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026, aangemeld | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing): opleidingsverbintenis in KRS |
| ontstaat | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026, aangemeld | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing): opleidingsprogramma-verbintenis in KRS |

**F3-04 - De aanmelding van de voorziening naar het intakesysteem** (fase 3, Aanmelden via het intakesysteem; [f3-04-de-aanmelding-van-de-voorziening-naar-het-intakesysteem.svg](img/regels/f3-04-de-aanmelding-van-de-voorziening-naar-het-intakesysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Persoon | Jochem, 17, na het vmbo | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing): naar KRS (opleidingsverbintenis, opleidingsprogramma-verbintenis en Persoon); v1.7 tekent deze pijl voor CAMBO; leerroute-1-regulier.md, [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Aanmelding | April 2026, Apothekersassistent BOL | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing); leerroute-1-regulier.md, [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026, aangemeld | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing); leerroute-1-regulier.md, [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026, aangemeld | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing); leerroute-1-regulier.md, [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |

**F3-05 - Intake: student, plaatsingsgroep en eerste keuzedeelvoorkeur** (fase 3, Intake doorlopen en plaatsen; [f3-05-intake-student-plaatsingsgroep-en-eerste-keuzedeelvoorkeur.svg](img/regels/f3-05-intake-student-plaatsingsgroep-en-eerste-keuzedeelvoorkeur.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Student | Jochem, cohort 2026 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r82](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L82): intake, plaatsing op het nominale programma |
| ontstaat | Plaatsingsgroep | APO26-1A | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), groepen (13cc9125); leerroute-1-regulier.md, Fase 3: initiele plaatsingsgroep |
| ontstaat | Verzoek tot Aanbod / Intekening op specificatie | Voorlopige keuzedeelvoorkeur: K0037 Farmaceutische Patientenzorg, top 3 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r128](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L128) (8e: aanmelding keuzedeel ver vooraf vastleggen, voorlopig); keuze van de sectorarchitect: bij de intake |

**F3-06 - De eerste keuzedeelvoorkeur naar het studentkeuzesysteem** (fase 3, Intake doorlopen en plaatsen; [f3-06-de-eerste-keuzedeelvoorkeur-naar-het-studentkeuzesysteem.svg](img/regels/f3-06-de-eerste-keuzedeelvoorkeur-naar-het-studentkeuzesysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Verzoek tot Aanbod / Intekening op specificatie | Voorlopige keuzedeelvoorkeur: K0037 Farmaceutische Patientenzorg, top 3 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) (het intakesysteem doet geen keuzedeelselectie, dat is het SKS), [r850](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L850) (het SKS is bron voor de geprioriteerde voorkeurslijst) en [r73](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L73) (de student stelt die lijst samen zodra de keuzedeelruimte dichterbij komt); dat de intake de eerste voorkeuren alvast meegeeft, is een keuze van het voorbeeld |

**F3-07 - Inschrijving: van aangemeld naar ingeschreven** (fase 3, Persoon en verbintenissen vastleggen in de kernregistratie; [f3-07-inschrijving-van-aangemeld-naar-ingeschreven.svg](img/regels/f3-07-inschrijving-van-aangemeld-naar-ingeschreven.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Inschrijving | Juni 2026 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r15](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L15): inschrijving in juni 2026 |
| verandert | Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing): inschrijving op opleiding en programma |
| verandert | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 3](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-3--instroom-intake-en-plaatsing) |

**F3-08 - De inschrijving van het intakesysteem naar de kernregistratie** (fase 3, Persoon en verbintenissen vastleggen in de kernregistratie; [f3-08-de-inschrijving-van-het-intakesysteem-naar-de-kernregistratie.svg](img/regels/f3-08-de-inschrijving-van-het-intakesysteem-naar-de-kernregistratie.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Inschrijving | Juni 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Persoon | Jochem, 17, na het vmbo | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Student | Jochem, cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Plaatsingsgroep | APO26-1A | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |
| stroomt | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r860](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L860) en [r882](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L882) (het intakesysteem verwerkt aanmelding en intake en draagt de positieve uitkomst over aan KRS), [r945](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L945) en [r949](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L949) |

**F4-01 - Het leeronderdeel fijnmazig: lessenreeks en les** (fase 4, Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken; [f4-01-het-leeronderdeel-fijnmazig-lessenreeks-en-les.svg](img/regels/f4-01-het-leeronderdeel-fijnmazig-lessenreeks-en-les.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Leeronderdeel specificatie | B1-K1-W1 Neemt de zorg-/adviesvraag in behandeling, lessenreeks Baliegesprek en triage | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1086](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1086) tot [1110](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1110): lessenreeks 6 weken x 1 dagdeel |
| ontstaat | Les specificatie | Les 1 Introductie WHAM-vragen en triage | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1094](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1094) tot [1100](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1100): lesspecificatie les 1 |
| ontstaat | Les specificatie | Les 2 Baliegesprek oefenen met rollenspel | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r626](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L626) (Leeronderdeel-specificatie 0..* Lesspecificatie) en [r604](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L604) (de lesspecificatie is het kleinste geplande leermoment binnen een leeronderdeel); de les blijft buiten de uitwisseling, ontwerpkeuze 8 |

**F4-02 - Detailspecificaties naar het LMS** (fase 4, Detailspecificaties leveren aan het LMS; [f4-02-detailspecificaties-naar-het-lms.svg](img/regels/f4-02-detailspecificaties-naar-het-lms.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Leeronderdeel specificatie | B1-K1-W1, lessenreeks Baliegesprek en triage | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): OC naar LMS (leeronderdeel-specificaties ter detaillering) |
| stroomt | Les specificatie | Les 1 Introductie WHAM-vragen en triage | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): detailspecificaties naar het LMS |
| stroomt | Les specificatie | Les 2 Baliegesprek oefenen met rollenspel | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r626](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L626) (Leeronderdeel-specificatie 0..* Lesspecificatie) en [r604](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L604) (de lesspecificatie is het kleinste geplande leermoment binnen een leeronderdeel); de les blijft buiten de uitwisseling, ontwerpkeuze 8 |
| stroomt | Toetsonderdeel specificatie | Formatieve check baliegesprek, les 1 | informatiemodel.json: Toetsonderdeel specificatie naar Leeruitkomst; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |

**F4-03 - De les en de toets van binnen, elk met hun eigen onderdelen (conceptplaat)** (fase 4, Detailspecificaties leveren aan het LMS; [f4-03-de-les-en-de-toets-van-binnen-elk-met-hun-eigen-onderdelen-conceptplaat.svg](img/regels/f4-03-de-les-en-de-toets-van-binnen-elk-met-hun-eigen-onderdelen-conceptplaat.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt (conceptplaat) | Les specificatie / toets specificatie | Les 1 Introductie WHAM-vragen en triage, en de formatieve check erbij | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Onderwijsplan aggregeert Les specificatie / toets specificatie; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | (Didactische) Leervorm | Instructie met rollenspel in tweetallen | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert (Didactische) Leervorm; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Lesplanning | 90 minuten, week 3, skillslab | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Lesplanning; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Lesleerdoel | De student stelt de WHAM-vragen in de juiste volgorde | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Lesleerdoel; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Werkinstructies | Rolkaarten balie, checklist triage | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Werkinstructies; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Toetsvorm | Formatieve check: observatie met rubric | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Toetsvorm; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Toetsinstrument | Observatieformulier WHAM-vragen | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Toetsinstrument; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Toetsmatrijs | Dekking van de lesleerdoelen over de observatiepunten | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Toetsmatrijs; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |
| stroomt (conceptplaat) | Lesuitkomst | Stelt de WHAM-vragen volledig en in volgorde | model.archimate, view Informatiemodel Onderwijsontwerp (conceptplaat): Les specificatie / toets specificatie aggregeert Lesuitkomst; leerroute-1-regulier.md, r886 (het LMS detailleert de leeronderdeelspecificatie en eventueel de lesspecificaties) en r955 |

**F4-04 - Resultaatstructuur naar het studentvolgsysteem** (fase 4, Detailspecificaties leveren aan het LMS; [f4-04-resultaatstructuur-naar-het-studentvolgsysteem.svg](img/regels/f4-04-resultaatstructuur-naar-het-studentvolgsysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Summatieve resultaat structuur | Resultaatstructuur Apothekersassistent | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): OC naar SVS (specificatie als referentiekader); koppelingspecificatie OC-SIS: resultaatstructuur |
| stroomt | Examenonderdeelspecificatie | Proeve van bekwaamheid B1-K1 | informatiemodel.json: Summatieve resultaat structuur aggregeert Toetsonderdeel specificatie, Examenonderdeelspecificatie is een Toetsonderdeel specificatie, Examenonderdeel weging naar Examenonderdeelspecificatie |
| stroomt | Examenonderdeel weging | Proeve van bekwaamheid B1-K1: weging 2 | informatiemodel.json: Summatieve resultaat structuur aggregeert Toetsonderdeel specificatie, Examenonderdeelspecificatie is een Toetsonderdeel specificatie, Examenonderdeel weging naar Examenonderdeelspecificatie |
| stroomt | Summatief Afrondingscriterium | Alle kerntaken en de keuzedelen voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): OC naar SVS |

**F4-05 - Resultaatstructuur naar de kernregistratie** (fase 4, Detailspecificaties leveren aan het LMS; [f4-05-resultaatstructuur-naar-de-kernregistratie.svg](img/regels/f4-05-resultaatstructuur-naar-de-kernregistratie.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Summatieve resultaat structuur | Resultaatstructuur Apothekersassistent | keuze van de sectorarchitect: de kernregistratie verantwoordt de studievoortgang aan RIO en heeft daarvoor de resultaatstructuur nodig |
| stroomt | Examenonderdeelspecificatie | Proeve van bekwaamheid B1-K1 | informatiemodel.json: Summatieve resultaat structuur aggregeert Toetsonderdeel specificatie, Examenonderdeelspecificatie is een Toetsonderdeel specificatie, Examenonderdeel weging naar Examenonderdeelspecificatie |
| stroomt | Examenonderdeel weging | Proeve van bekwaamheid B1-K1: weging 2 | informatiemodel.json: Summatieve resultaat structuur aggregeert Toetsonderdeel specificatie, Examenonderdeelspecificatie is een Toetsonderdeel specificatie, Examenonderdeel weging naar Examenonderdeelspecificatie |
| stroomt | Summatief Afrondingscriterium | Alle kerntaken en de keuzedelen voldoende | keuze van de sectorarchitect |

**F4-06 - Plaatsingsgroepen naar planning** (fase 4, Plaatsings- en planninggroepen definieren en aan personen koppelen; [f4-06-plaatsingsgroepen-naar-planning.svg](img/regels/f4-06-plaatsingsgroepen-naar-planning.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Plaatsingsgroep | APO26-1A | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): Planning en KRS (groepen en persoon) |
| stroomt | Student | Jochem, cohort 2026 | informatiemodel.json: Persoon naar Plaatsingsgroep (Worden gegroepeerd via), Student is een Persoon |
| stroomt | Student | 29 andere studenten in dezelfde groep | informatiemodel.json: Persoon naar Plaatsingsgroep (Worden gegroepeerd via), Student is een Persoon |

**F4-07 - Te roosteren leergelegenheden naar het roostersysteem** (fase 4, Te roosteren specificaties aan het roostersysteem geven; [f4-07-te-roosteren-leergelegenheden-naar-het-roostersysteem.svg](img/regels/f4-07-te-roosteren-leergelegenheden-naar-het-roostersysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Leergelegenheid | B1-K1-W1, periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): Planning naar Rooster (te roosteren specificaties) |

**F4-08 - Roosteren: lesgelegenheid, lokaal en docent** (fase 4, Leer-, les- en toetsgelegenheden roosteren; [f4-08-roosteren-lesgelegenheid-lokaal-en-docent.svg](img/regels/f4-08-roosteren-lesgelegenheid-lokaal-en-docent.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Leergelegenheid | B1-K1-W1, periode 1, docent 4711 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r80](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L80): roosteraar roostert alleen periode 1 |
| ontstaat | Lesgelegenheid | Les 1, maandag 1 september 09:00, simulatieruimte 2.14 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r80](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L80) en [r86](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L86): ma 09:00 tot [11](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L11):00, lokaal 2.14 |
| ontstaat | Medewerker | Docent, personeelsnummer 4711 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r80](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L80): docent personeelsnr 4711 |

**F4-09 - Jochems verbintenissen op de geroosterde gelegenheden** (fase 4, Verwachte deelnemers delen en toegang geven; [f4-09-jochems-verbintenissen-op-de-geroosterde-gelegenheden.svg](img/regels/f4-09-jochems-verbintenissen-op-de-geroosterde-gelegenheden.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Onderwijseenheid aanbod verbintenis | Jochem op B1-K1, leerjaar 1 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r96](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L96): enrolled op P1-eenheden |
| ontstaat | Leergelegenheid verbintenis | Jochem op B1-K1-W1, periode 1 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r97](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L97): Association.state enrolled op P1-leergelegenheden |
| ontstaat | Lesgelegenheid verbintenis | Jochem op les 1, 1 september 09:00 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r98](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L98): lesgelegenheden eerste week geroosterd |
| verandert | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026 | [scenario-1.1-regulier-happyflow.md](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md), [r95](../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md?plain=1#L95): enrolled op nominaal traject |

**F4-10 - Student, verbintenissen en groep naar het LMS** (fase 4, Verwachte deelnemers delen en toegang geven; [f4-10-student-verbintenissen-en-groep-naar-het-lms.svg](img/regels/f4-10-student-verbintenissen-en-groep-naar-het-lms.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Student | Jochem, cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): KRS naar LMS, student, verbintenis en relevante groepen |
| stroomt | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): KRS naar LMS (verbintenis en persoon voor rechtmatige toegang) |
| stroomt | Plaatsingsgroep | APO26-1A | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): relevante groepen |
| stroomt | Onderwijseenheid aanbod verbintenis | Jochem op B1-K1, leerjaar 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): verwachte deelnemers |
| stroomt | Leergelegenheid verbintenis | Jochem op B1-K1-W1, periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 4](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-4--detailleren-roosteren-en-inschrijven): verwachte deelnemers |

**F4-11 - Verbintenissen op alle niveaus naar het studentvolgsysteem** (fase 4, Verwachte deelnemers delen en toegang geven; [f4-11-verbintenissen-op-alle-niveaus-naar-het-studentvolgsysteem.svg](img/regels/f4-11-verbintenissen-op-alle-niveaus-naar-het-studentvolgsysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Student | Jochem, cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (behaalde resultaten worden in SVS bijgehouden tegen de specificatie uit de catalogus) |
| stroomt | Opleiding aanbod verbintenis | Jochem op Apothekersassistent 2026, ingeschreven | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (behaalde resultaten worden in SVS bijgehouden tegen de specificatie uit de catalogus) |
| stroomt | Opleidingsprogramma aanbod verbintenis | Jochem op Regulier BOL 2026, ingeschreven | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (behaalde resultaten worden in SVS bijgehouden tegen de specificatie uit de catalogus) |
| stroomt | Onderwijseenheid aanbod verbintenis | Jochem op B1-K1, leerjaar 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (behaalde resultaten worden in SVS bijgehouden tegen de specificatie uit de catalogus) |
| stroomt | Leergelegenheid verbintenis | Jochem op B1-K1-W1, periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (behaalde resultaten worden in SVS bijgehouden tegen de specificatie uit de catalogus) |

**F5-01 - Les gevolgd: aanwezigheid en lesresultaat** (fase 5, Onderwijs verzorgen; [f5-01-les-gevolgd-aanwezigheid-en-lesresultaat.svg](img/regels/f5-01-les-gevolgd-aanwezigheid-en-lesresultaat.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Lesgelegenheid verbintenis | Jochem op les 1, 1 september 09:00 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): docenten verzorgen onderwijs |
| ontstaat | Aanwezigheid | Aanwezig, les 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): aanwezigheid wordt geregistreerd |
| ontstaat | Lesgelegenheid resultaat | Les 1 gevolgd | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden) |

**F5-02 - De verbintenis op de toetsgelegenheid: geplaatst of zelf gekozen** (fase 5, Toetsmomenten plannen tijdens lessen; [f5-02-de-verbintenis-op-de-toetsgelegenheid-geplaatst-of-zelf-gekozen.svg](img/regels/f5-02-de-verbintenis-op-de-toetsgelegenheid-geplaatst-of-zelf-gekozen.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Toetsgelegenheid verbintenis | Jochem op de OSCE, einde periode 1, via zijn plaatsingsgroep | informatiemodel.json: Toetsgelegenheid naar Toetsgelegenheid verbintenis, Plaatsingsgroep naar Toetsgelegenheid verbintenis; componenten.json: het studentkeuzesysteem levert de diensten Keuze op leergelegenheid en Accorderen van keuzes, het roostersysteem de dienst Aanmelding rooster activiteit |
| ontstaat | Toetsgelegenheid verbintenis | Jochem op de herkansing OSCE, periode 2, zelf ingetekend | informatiemodel.json: Toetsgelegenheid naar Toetsgelegenheid verbintenis, Plaatsingsgroep naar Toetsgelegenheid verbintenis; componenten.json: het studentkeuzesysteem levert de diensten Keuze op leergelegenheid en Accorderen van keuzes, het roostersysteem de dienst Aanmelding rooster activiteit |

**F5-03 - Formatieve voortgang: structuur, resultaten en beoordeling** (fase 5, Formatieve voortgang bijhouden; [f5-03-formatieve-voortgang-structuur-resultaten-en-beoordeling.svg](img/regels/f5-03-formatieve-voortgang-structuur-resultaten-en-beoordeling.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Formatieve resultaat structuur | Voortgang B1-K1-W1: quiz WHAM-vragen, rollenspel | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1096](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1096) tot [1099](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1099): formatieve controles per les |
| ontstaat | Toetsonderdeel weging | Quiz WHAM-vragen: weging 1 | geen bron, keuze van het voorbeeld |
| ontstaat | Toetsgelegenheid resultaat | OSCE: voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r1117](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L1117): schaal onvoldoende, voldoende, goed |
| ontstaat | Formatief resultaat | Quiz WHAM-vragen: 8 van 10 | geen bron, keuze van het voorbeeld |
| ontstaat | Formatieve beoordeling | Op koers voor B1-K1-W1 | geen bron, keuze van het voorbeeld |
| ontstaat | Persoonlijke ontwikkeling | Jochems ontwikkeling in periode 1 | geen bron, keuze van het voorbeeld |
| ontstaat | Leergelegenheid resultaat | B1-K1-W1 afgerond, periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): SLB'ers volgen Jochems studiebeeld in SVS |

**F5-04 - Formatieve resultaten van het LMS naar het studentvolgsysteem** (fase 5, Formatieve voortgang bijhouden; [f5-04-formatieve-resultaten-van-het-lms-naar-het-studentvolgsysteem.svg](img/regels/f5-04-formatieve-resultaten-van-het-lms-naar-het-studentvolgsysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Toetsgelegenheid resultaat | OSCE: voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): LMS naar SVS (toetsgelegenheid-verbintenis resultaten, formatief) |
| stroomt | Formatief resultaat | Quiz WHAM-vragen: 8 van 10 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): LMS naar SVS, formatief |
| stroomt | Leergelegenheid resultaat | B1-K1-W1 afgerond, periode 1 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden): LMS naar SVS, leergelegenheid-verbintenis resultaten |

**F5-05 - Studiebeeld: de nominale route naast wat Jochem heeft behaald** (fase 5, Studiebeeld volgen in het studentvolgsysteem; [f5-05-studiebeeld-de-nominale-route-naast-wat-jochem-heeft-behaald.svg](img/regels/f5-05-studiebeeld-de-nominale-route-naast-wat-jochem-heeft-behaald.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Onderwijseenheid resultaat | B1-K1: in uitvoering, twee van vier leeronderdelen afgerond | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 5](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden) en 7: onderwijseenheid-verbintenis resultaten |
| ontstaat | Onderwijseenheid aanbod | B1-K1, leerjaar 1, periode 1 tot 4: de nominale route | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij tot kwalificering) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (resultaten worden bijgehouden tegen de specificatie uit de catalogus) |
| ontstaat | Summatieve resultaat structuur | Resultaatstructuur Apothekersassistent, cohort 2026 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r868](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L868) (het studentvolgsysteem legt onderwijsresultaten per onderwijsverbintenis vast en houdt de studiepadadministratie bij tot kwalificering) en [r870](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L870) (resultaten worden bijgehouden tegen de specificatie uit de catalogus) |

**F6-01 - Keuzedeelaanbod ontsloten** (fase 6, Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem; [f6-01-keuzedeelaanbod-ontsloten.svg](img/regels/f6-01-keuzedeelaanbod-ontsloten.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Keuzedeelaanbod | K0037 Farmaceutische Patientenzorg, periode 7, locatie A | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): OC naar SKS (opleidingsprogramma-aanbod type keuzedeel + opleidingsprogramma-specificatie); wanneer het keuzedeelaanbod planbaar wordt, zegt het kaderscenario niet |

**F6-02 - Keuzedeelaanbod, specificatie en regels naar het studentkeuzesysteem** (fase 6, Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem; [f6-02-keuzedeelaanbod-specificatie-en-regels-naar-het-studentkeuzesysteem.svg](img/regels/f6-02-keuzedeelaanbod-specificatie-en-regels-naar-het-studentkeuzesysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Keuzedeelaanbod | K0037 Farmaceutische Patientenzorg, periode 7, locatie A | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): OC naar SKS |
| stroomt | Keuzedeel | K0037 Farmaceutische Patientenzorg | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): OC naar SKS, opleidingsprogramma-specificatie |
| stroomt | Student keuze regelset | Kiesbare keuzedelen voor Apothekersassistent | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), regelsets[0] (e4037953); keuze-requirements.md |

**F6-03 - Jochems voorkeur: verbintenis op het keuzedeelaanbod** (fase 6, Voorkeurslijst samenstellen in het studentkeuzesysteem; [f6-03-jochems-voorkeur-verbintenis-op-het-keuzedeelaanbod.svg](img/regels/f6-03-jochems-voorkeur-verbintenis-op-het-keuzedeelaanbod.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Keuzedeel aanbod verbintenis | Jochem op K0037 Farmaceutische Patientenzorg, periode 7 (voorkeur 1) | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): Jochem stelt zijn geprioriteerde voorkeurslijst samen in het SKS; SKS naar Planning geeft zijn keuzestelling door als opleidingsprogramma-verbintenis op het gekozen opleidingsprogramma-aanbod |

**F6-04 - Keuzestelling naar planning** (fase 6, Voorkeurslijst samenstellen in het studentkeuzesysteem; [f6-04-keuzestelling-naar-planning.svg](img/regels/f6-04-keuzestelling-naar-planning.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Keuzedeel aanbod verbintenis | Jochem op K0037 Farmaceutische Patientenzorg, periode 7 (voorkeur 1) | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): SKS naar Planning (opleidingsprogramma-verbintenis op gekozen aanbod) |

**F6-05 - Definitieve keuzes verwerkt naar groepen en capaciteit** (fase 6, Definitieve keuzes verwerken naar groepen en capaciteit; [f6-05-definitieve-keuzes-verwerkt-naar-groepen-en-capaciteit.svg](img/regels/f6-05-definitieve-keuzes-verwerkt-naar-groepen-en-capaciteit.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Keuzedeelaanbod | K0037 Farmaceutische Patientenzorg, periode 7, locatie A: 1 groep, 24 plaatsen | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): de planner verwerkt definitieve keuzes periodiek naar groepen en capaciteit |

**F6-06 - Geactualiseerd keuzedeelaanbod terug naar de catalogus** (fase 6, Planbaar aanbod actualiseren; [f6-06-geactualiseerd-keuzedeelaanbod-terug-naar-de-catalogus.svg](img/regels/f6-06-geactualiseerd-keuzedeelaanbod-terug-naar-de-catalogus.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Keuzedeelaanbod | K0037 Farmaceutische Patientenzorg, periode 7, locatie A: 1 groep, 24 plaatsen | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): actualiseert het planbare aanbod in OC en het rooster volgt; Planning naar OC (geactualiseerd planbaar aanbod) |

**F6-07 - Formele inschrijving op het keuzedeel** (fase 6, Keuzedeel formeel inschrijven; [f6-07-formele-inschrijving-op-het-keuzedeel.svg](img/regels/f6-07-formele-inschrijving-op-het-keuzedeel.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Keuzedeel aanbod verbintenis | Jochem op K0037 Farmaceutische Patientenzorg, periode 7 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): bij passend aanbod levert Planning naar KRS de formele inschrijving op het keuzedeel |

**F6-08 - Keuzedeelverbintenis naar de kernregistratie** (fase 6, Keuzedeel formeel inschrijven; [f6-08-keuzedeelverbintenis-naar-de-kernregistratie.svg](img/regels/f6-08-keuzedeelverbintenis-naar-de-kernregistratie.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Keuzedeel aanbod verbintenis | Jochem op K0037 Farmaceutische Patientenzorg, periode 7 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 6](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-6--organiseren-van-keuzemomenten): Planning naar KRS (formele inschrijving keuzedeel); hoofdplaat v1.7 kent alleen SKS naar KRS |

**F7-01 - Afwijkingen verzameld in een planninggroep** (fase 7, Afwijkingen verzamelen in een planninggroep; [f7-01-afwijkingen-verzameld-in-een-planninggroep.svg](img/regels/f7-01-afwijkingen-verzameld-in-een-planninggroep.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Plaatsingsgroep | Planninggroep temporiseren B1-K2, periode 5 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod): de planner verzamelt vergelijkbare afwijkingen in een planninggroep |

**F7-02 - Bestaande verbintenis geannuleerd** (fase 7, Bestaande verbintenissen annuleren; [f7-02-bestaande-verbintenis-geannuleerd.svg](img/regels/f7-02-bestaande-verbintenis-geannuleerd.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Onderwijseenheid aanbod verbintenis | Jochem op B1-K2, periode 3 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod): bestaande onderwijseenheid-verbintenissen worden via KRS geannuleerd |

**F7-03 - Planninggroep van de kernregistratie naar planning** (fase 7, Bestaande verbintenissen annuleren; [f7-03-planninggroep-van-de-kernregistratie-naar-planning.svg](img/regels/f7-03-planninggroep-van-de-kernregistratie-naar-planning.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Plaatsingsgroep | Planninggroep temporiseren B1-K2, periode 5 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod): KRS naar Planning (gewijzigde populatie en plangroepen) |

**F7-04 - Nieuw aanbod voor de planninggroep** (fase 7, Nieuw aanbod maken en publiceren; [f7-04-nieuw-aanbod-voor-de-planninggroep.svg](img/regels/f7-04-nieuw-aanbod-voor-de-planninggroep.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| verandert | Onderwijseenheid aanbod | B1-K2, periode 5, planninggroep temporiseren | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod): nieuw onderwijsaanbod op basis van dezelfde opleidingsprogramma-specificatie |

**F7-05 - Bijgestuurd aanbod naar de catalogus** (fase 7, Nieuw aanbod maken en publiceren; [f7-05-bijgestuurd-aanbod-naar-de-catalogus.svg](img/regels/f7-05-bijgestuurd-aanbod-naar-de-catalogus.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Onderwijseenheid aanbod | B1-K2, periode 5, bijgestuurd | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod): Planning naar OC (mutaties planbaar aanbod) |

**F7-06 - Nieuwe leergelegenheden naar het roostersysteem** (fase 7, Nieuw aanbod maken en publiceren; [f7-06-nieuwe-leergelegenheden-naar-het-roostersysteem.svg](img/regels/f7-06-nieuwe-leergelegenheden-naar-het-roostersysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Leergelegenheid | B1-K2-W1, periode 5 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 7](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-7--bijsturen-planning-en-aanbod): Planning naar Rooster (nieuw rooster) |

**F8-01 - Examengelegenheid uit de examenspecificatie** (fase 8, Examenspecificaties omzetten in examengelegenheden; [f8-01-examengelegenheid-uit-de-examenspecificatie.svg](img/regels/f8-01-examengelegenheid-uit-de-examenspecificatie.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Examengelegenheid | Proeve van bekwaamheid B1-K1, periode 12 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): examenspecificaties getransformeerd tot examengelegenheden |

**F8-02 - Kandidatenlijst: verbintenis op de examengelegenheid** (fase 8, Kandidatenlijsten samenstellen; [f8-02-kandidatenlijst-verbintenis-op-de-examengelegenheid.svg](img/regels/f8-02-kandidatenlijst-verbintenis-op-de-examengelegenheid.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Examengelegenheid verbintenis | Jochem op de proeve, periode 12 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): toets- en examenplanning stelt kandidatenlijsten samen |

**F8-03 - Zitting: het examenresultaat** (fase 8, Zitting uitvoeren en resultaten doorgeven; [f8-03-zitting-het-examenresultaat.svg](img/regels/f8-03-zitting-het-examenresultaat.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Examengelegenheid resultaat | Proeve B1-K1: voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): afname levert examengelegenheid-verbintenis resultaten aan SVS |

**F8-04 - Examenresultaat naar het studentvolgsysteem** (fase 8, Zitting uitvoeren en resultaten doorgeven; [f8-04-examenresultaat-naar-het-studentvolgsysteem.svg](img/regels/f8-04-examenresultaat-naar-het-studentvolgsysteem.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Examengelegenheid resultaat | Proeve B1-K1: voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): Toets-/examenafname naar SVS; niet op de view zonder context van hoofdplaat v1.7 |

**F8-05 - Summatief vastgesteld: resultaten en beoordeling** (fase 8, Summatief vaststellen; [f8-05-summatief-vastgesteld-resultaten-en-beoordeling.svg](img/regels/f8-05-summatief-vastgesteld-resultaten-en-beoordeling.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Summatief resultaat | B1-K1: voldoende, vastgesteld | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): de examencommissie stelt summatief vast |
| ontstaat | Summatieve beoordeling | Examencommissie, juni 2029 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): binnen SVS |
| ontstaat | Opleidingsprogramma resultaat | Regulier BOL 2026: alle kerntaken en keuzedelen voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): kwalificering |
| ontstaat | Keuzedeel resultaat | K0037 Farmaceutische Patientenzorg: voldoende | [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md), resultaatstructuur: aggregatie allenVoldoende over kerntaken en keuzedelen; leerroute-1-regulier.md, Fase 8 |

**F8-06 - Vaststelling naar de kernregistratie** (fase 8, Summatief vaststellen; [f8-06-vaststelling-naar-de-kernregistratie.svg](img/regels/f8-06-vaststelling-naar-de-kernregistratie.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| stroomt | Summatief resultaat | B1-K1: voldoende, vastgesteld | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): de examencommissie stelt summatief vast; SVS en KRS |
| stroomt | Opleidingsprogramma resultaat | Regulier BOL 2026: alle kerntaken en keuzedelen voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): SVS en KRS (kwalificering en diplomering) |
| stroomt | Keuzedeel resultaat | K0037 Farmaceutische Patientenzorg: voldoende | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): SVS en KRS (kwalificering en diplomering) |

**F8-07 - Gediplomeerd: opleidingsresultaat en diploma** (fase 8, Kwalificering en diplomering registreren; [f8-07-gediplomeerd-opleidingsresultaat-en-diploma.svg](img/regels/f8-07-gediplomeerd-opleidingsresultaat-en-diploma.svg))

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| ontstaat | Opleiding aanbod resultaat | Apothekersassistent 2026: gediplomeerd | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): KRS registreert kwalificering en diplomering |
| ontstaat | Waarde document (diploma / certificaat) | Diploma Apothekersassistent, juli 2029 | [leerroute-1-regulier.md](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md), [r58](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md?plain=1#L58) en [Fase 8](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#fase-8--examineren-vaststellen-en-diplomeren): diplomering |

