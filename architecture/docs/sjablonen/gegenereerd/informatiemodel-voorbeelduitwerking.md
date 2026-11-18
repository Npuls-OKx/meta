# Sjabloon informatiemodel-voorbeelduitwerking

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een voorbeelduitwerking: een persona stap voor stap in het informatiemodel, zodat zichtbaar wordt of het model de werkelijkheid draagt |
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers vullen de regels, de business analisten leggen ze naast het model |
| Voorbeelduitwerking | [de opleiding van Jochem in het informatiemodel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Vaste koppen

De koppen in dit document blijven staan zoals zij hier staan. In het agent-harnas komt een lezer (parser) die een ingevuld document per kop terugvertaalt naar de kennisbank; een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt dus zijn kop, met de reden eronder.

Dit sjabloon is afgeleid uit [de opleiding van Jochem in het informatiemodel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md), dus het draagt elke kop en elke tabel van die uitwerking. Wat daar algemeen was staat er nog. Wat daar aan die ene uitwerking hing, staat er als ingesprongen citaat, met *Schrijf hier de uitwerking.* eronder: daar hoort de eigen uitwerking. Een lege tabel heeft evenveel rijen als de uitwerking had, zodat zichtbaar is hoeveel er wordt verwacht.

## De grootst gemene deler

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier sterker dan elders, omdat een voorbeeld overtuigt: een regel die uit een enkele instelling komt en hier als voorbeeld staat, leest als sectorpraktijk.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

> De uitwerking van Jochem schrijft hier: Relateert aan: het kaderscenario leerroute 1 (persona Jochem, Apothekersassistent, cohort 2026), het architectuurkader van OKx, en het informatiemodel OKx.

*Schrijf hier de uitwerking.*

## Leeswijzer

> De uitwerking van Jochem schrijft hier: Dit document loopt stap voor stap door de instellingsreis van het kaderscenario en toont per stap wat er in het informatiemodel ontstaat en wat er tussen systemen beweegt, met de waarde voor Jochem erin.

Elk beeld heeft een ID en een titel die zegt wat het toont: F1-02 is het tweede beeld van fase 1. Beide staan in het beeld zelf, als kop erboven (met een eigen anker in dit document) en in het regelregister achterin; de bijlage noemt het ID. Verwijs naar een beeld met zijn ID, en naar een regel met dat ID en het objecttype.

Vier termen, overal gelijk:

| Term | Betekenis |
|---|---|
| | |
| | |
| | |
| | |

Vier lagen waarin hetzelfde onderwijs steeds concreter wordt. Dit onderscheid draagt het hele document, en
elk beeld staat in een van deze lagen:

| Laag | Wat het is | In dit voorbeeld |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

Een specificatie bestaat dus zonder dat er iemand voor kiest, een aanbod zonder dat er iemand op zit, en een
verbintenis zonder dat er al een resultaat is. Dezelfde naam komt in meer lagen voor: `Opleidingaanbod` is het
aanbod, `Opleiding aanbod verbintenis` de inschrijving daarop.

Een specialisatie op de plaat (open pijlpunt) zegt dat het ene objecttype de structuur van het andere overneemt
en er eigen eigenschappen bij krijgt. Het keuzedeel is daarvan het duidelijkste voorbeeld, en het loopt door
alle vier de lagen heen:

| Laag | Algemeen | Specialisatie |
|---|---|---|
| Specificatie | `Opleidingsprogramma specificatie` | `Keuzedeel`, `Keuzedeelruimte` |
| Aanbod | `Opleidingsprogramma aanbod` | `Keuzedeel aanbod` |
| Verbintenis | `Opleidingsprogramma aanbod verbintenis` | `Keuzedeel aanbod verbintenis` |
| Resultaat | `Opleidingsprogramma resultaat` | `Keuzedeel resultaat` |

Een keuzedeel is daarmee in opbouw bijna hetzelfde als een programma: het erft die opbouw en vult hem aan. Wat
het eigen heeft komt in het logisch gegevensmodel erbij. Het algemene begrip staat dus al op de plaat, en het
keuzedeel is de invulling die het mbo eraan geeft.

Twee soorten regels, in de vormtaal van de plaat:

> Ontstaat: een rol (geel, rolicoon) voert een processtap uit (geel, procesicoon) en daaruit ontstaan objecttypen (geel, objecticoon) met Jochems waarde.

Waar de herkomst loopt: het kwalificatiedossier, de kwalificatie, de kerntaken en de werkprocessen staan in het eerste beeld van fase 1, en het derde beeld vertaalt ze naar leeruitkomsten. Daarna verwijzen specificaties, toets- en examenonderdelen, aanbod, verbintenissen en resultaten naar de leeruitkomst; de plaat kent buiten die route alleen een directe verwijzing vanuit het examenplan en de OER. Een dossiercode in een instantienaam (B1-K1, B1-K1-W1) is daarom een leeshulp die zegt over welk deel van het dossier het gaat, en geen relatie. Op de conceptplaat loopt daarnaast een eigen pad binnen de instelling: de kerntaak wordt daar onderwijskundig vertaald tot een leerdoel.

Een **verdieping** (zelfde rol en stap, met "verdieping" op de processtap) zoomt in op een regel erboven. Een paars objecttype komt van de conceptplaat "Informatiemodel Onderwijsontwerp" in het ArchiMate-model (een verdieping daaruit heeft ook een gestippelde rand en een chip): het laat zien waar de informatiemodelplaat kan groeien en telt niet mee in de bijlage.

Koppeling-ID's op hoofdplaat v1.7a: OC-P&R is Onderwijscatalogus naar Planningssysteem; OC-P&R is Planningssysteem naar Onderwijscatalogus; OC-KRS is Onderwijscatalogus naar Kernregistratie systeem studenten (KRS); OC-SVS is Onderwijscatalogus naar Student volg systeem (SVS); OC-LMS is Onderwijscatalogus naar Leer management systeem (LMS). Een pijl die op de hoofdplaat staat maar geen koppelingspecificatie heeft, staat als "zonder koppelingspecificatie"; een stroom uit het kaderscenario zonder pijl op de hoofdplaat staat als "geen pijl op de hoofdplaat".

De fasenamen zijn de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario. Het kaderscenario noemt fase 3 in de fasenlijst "Instroom, afstemming en plaatsing" en in de sectiekop "Instroom, intake en plaatsing"; hier geldt de sectiekop.

Wat hier staat is feedback, geen commitment: het voorbeeld beslist niets over het model. Per objecttype staan in de bijlage twee lege kolommen, "heet bij u" en "hangt bij u onder", voor wie het naast het eigen model legt.

*Schrijf hier de uitwerking.*

## De hoofdplaat als kaart

De beelden met een blauwe rand tonen een stroom tussen twee componenten. Die componenten en pijlen komen van de hoofdplaat informatiestromen; de plaat hieronder is de kaart waarop die lijnen te vinden zijn, getekend uit het model.

*Beeld: De hoofdplaat informatiestromen van OKx, getekend uit het model. Voeg hier het beeld in.*

Alle stromen die dit voorbeeld gebruikt, met de beelden waarin ze voorkomen:

| Van | Naar | Op de hoofdplaat | Beelden |
|---|---|---|---|
| Curriculum ontwerptool | Onderwijscatalogus | geen pijl op de hoofdplaat | F1-12, F1-13 |
| Onderwijscatalogus | Planningssysteem | OC-P&R | F2-03 |
| Planningssysteem | Onderwijscatalogus | OC-P&R | F2-04, F2-09, F6-06, F7-05 |
| Onderwijscatalogus | Kernregistratie systeem studenten (KRS) | OC-KRS | F3-01, F4-05 |
| Kernregistratie systeem studenten (KRS) | AII (centraal aanmelden) | geen pijl op de hoofdplaat | F3-02 |
| AII (centraal aanmelden) | Intake systeem | geen pijl op de hoofdplaat | F3-04 |
| Voorziening Centraal Aanmelden (CAMBO) | Kernregistratie systeem studenten (KRS) | zonder koppelingspecificatie | F3-07 |
| Kernregistratie systeem studenten (KRS) | Student Keuze Systeem (SKS) | zonder koppelingspecificatie | F3-08 |
| Onderwijscatalogus | Leer management systeem (LMS) | OC-LMS | F4-02, F4-03 |
| Onderwijscatalogus | Student volg systeem (SVS) | OC-SVS | F4-04 |
| Kernregistratie systeem studenten (KRS) | Planningssysteem | zonder koppelingspecificatie | F4-06, F7-03 |
| Planningssysteem | Roostersysteem | zonder koppelingspecificatie | F4-07, F7-06 |
| Roostersysteem | Leer management systeem (LMS) | zonder koppelingspecificatie | F4-10 |
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
| Voorziening Centraal Aanmelden (CAMBO) | Een landelijk digitaal portaal voor het mbo waar een aspirant-student zich voor een opleiding kan aanmelden. Het is een generieke voorziening, dus niet instellingsspecifiek. Afkorting CAMBO | nog geen diensten in het model |

Zonder beschrijving in het model: AII (centraal aanmelden), Planningssysteem, Student Keuze Systeem (SKS). Dat is een signalering voor het model, geen keuze van dit voorbeeld.

## Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 1.

> Ontstaat: `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces`, `Examenplan`, `Summatieve resultaat structuur`, `Cohort / periode`, `Leeruitkomst`, `Onderwijskundige taxonomie`, `Competenties / Skills`, `Vaardigheid`, `Kennis`, `Inzicht`, `Onderwijseenheid specificatie`, `Leeronderdeel specificatie` ...

*Beeld: De hoofdplaat met de stromen van fase 1 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F1-01 - Het kwalificatiedossier ontleed

*Beeld: ontstaat: Kwalificatiedossier analyseren. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-02 - Examenplan, eerste resultaatstructuur en cohort

*Beeld: ontstaat: Examenplan opstellen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-03 - Leeruitkomsten uit het dossier, in de stem van de instelling

*Beeld: ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-04 - De leeruitkomst in CompetentNL-skills

*Beeld: ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: leeruitkomst naar skills. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-05 - De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten

*Beeld: ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: van kerntaak naar eenheid en leeronderdelen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-06 - De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen

*Beeld: ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: onderwijsontwerp met ruimte en middelen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-07 - De opleidingsspecificatie met programma, eenheden en keuzedeelruimte

*Beeld: ontstaat: Opleidingsspecificatie met programma en eenheden beschrijven. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-08 - Kiesbaar onderwijsprogrammaonderdeel: keuzedelen en minor

*Beeld: ontstaat: Keuzedeelprogramma als eigen specificatie vormgeven. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-09 - Toetsonderdelen, wegingen en afrondingscriterium

*Beeld: ontstaat: Toetsonderdelen en resultaatstructuur uit het examenplan afleiden. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-10 - De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte

*Beeld: ontstaat: Exameninstrumenten bepalen, inkopen of construeren, verdieping: examenvorm, instrument en beoordelaar. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-11 - Het examenplan vastgesteld

*Beeld: ontstaat: Examenplan vaststellen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F1-12 - De opleiding zoals ontworpen naar de catalogus

*Beeld: stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Curriculum ontwerptool naar Onderwijscatalogus, geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

### F1-13 - Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)

*Beeld: stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Curriculum ontwerptool naar Onderwijscatalogus, geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

## Fase 2: Publiceren en planbaar maken

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 2.

> Ontstaat: `Opleidingsprogramma specificatie`, `Onderwijseenheid specificatie`, `Leeronderdeel specificatie`, `Verzoek tot Aanbod / Intekening op specificatie`, `Opleidingsaanbod van Instelling`, `Opleiding aanbod`, `Opleidingsprogramma aanbod`, `Onderwijseenheid aanbod`, `Leergelegenheid`, `Toetsgelegenheid`.

*Beeld: De hoofdplaat met de stromen van fase 2 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F2-01 - De specificatie planbaar gemaakt

*Beeld: ontstaat: Specificatie aanvullen tot planbare specificatie. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F2-02 - Het verzoek om onderwijsaanbod

*Beeld: ontstaat: Planningssysteem verzoeken om onderwijsaanbod. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning

*Beeld: stroomt: Planningssysteem verzoeken om onderwijsaanbod. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Planningssysteem, OC-P&R.

*Schrijf hier de uitwerking.*

### F2-04 - De specificatie op haalbaarheid getoetst

*Beeld: stroomt: Specificatie op haalbaarheid toetsen. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Onderwijscatalogus, OC-P&R.

*Schrijf hier de uitwerking.*

### F2-05 - De aanbodvraag naast de schaarste van ruimtes en mensen (conceptplaat)

*Beeld: ontstaat: Aanbodvraag per opleiding bepalen, verdieping: ruimtes en mensen op de specificatie. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F2-06 - De jaarplanning op instellingsniveau (conceptplaat)

*Beeld: ontstaat: Jaarplanning op instellingsniveau vaststellen, verdieping: jaarplanning op instellingsniveau. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F2-07 - Examenbehoefte uit de resultaatstructuur (conceptplaat)

*Beeld: ontstaat: Jaarplanning op instellingsniveau vaststellen, verdieping: examenplanning uit de resultaatstructuur. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F2-08 - Het aanbod gepland: opleiding, programma, eenheid, gelegenheid

*Beeld: ontstaat: Aanbod plannen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F2-09 - Het geplande aanbod terug naar de catalogus

*Beeld: stroomt: Gepland aanbod terugleveren aan de onderwijscatalogus. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Onderwijscatalogus, OC-P&R.

*Schrijf hier de uitwerking.*

### Variant capaciteitsgestuurd

> De uitwerking van Jochem schrijft hier: Het kaderscenario beschrijft vraaggestuurd plannen: de planner vormt groepen nadat de studenten hebben gekozen.

*Schrijf hier de uitwerking.*

#### F2-C01 - Keuzedeel K0037 vooraf gepland op capaciteit

*Beeld: ontstaat: Keuzedeelaanbod plannen op inzetbare capaciteit en prognose. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

#### F2-C02 - Geplande keuzedeelgroepen naar de catalogus

*Beeld: stroomt: Gepland keuzedeelaanbod terugleveren aan de onderwijscatalogus. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Onderwijscatalogus, OC-P&R.

*Schrijf hier de uitwerking.*

## Fase 3: Instroom, intake en plaatsing

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 3.

> Ontstaat: `Persoon`, `Aanmelding`, `Opleiding aanbod verbintenis`, `Opleidingsprogramma aanbod verbintenis`, `Student`, `Plaatsingsgroep`, `Inschrijving`.

*Beeld: De hoofdplaat met de stromen van fase 3 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F3-01 - Aanmeldbaar aanbod naar de kernregistratie

*Beeld: stroomt: Orienteren op het gepubliceerde aanbod. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Kernregistratie systeem studenten (KRS), OC-KRS.

*Schrijf hier de uitwerking.*

### F3-02 - Aanmeldbaar aanbod van de kernregistratie naar AII

*Beeld: stroomt: Orienteren op het gepubliceerde aanbod. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Kernregistratie systeem studenten (KRS) naar AII (centraal aanmelden), geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

### F3-03 - <student> meldt zich aan: aanmelding en verbintenissen

*Beeld: ontstaat: Aanmelden via het intakesysteem. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F3-04 - De aanmelding van de voorziening naar het intakesysteem

*Beeld: stroomt: Aanmelden via het intakesysteem. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: AII (centraal aanmelden) naar Intake systeem, geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

### F3-05 - Intake: student en plaatsingsgroep

*Beeld: ontstaat: Intake doorlopen en plaatsen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F3-06 - Inschrijving: van aangemeld naar ingeschreven

*Beeld: ontstaat: Persoon en verbintenissen vastleggen in de kernregistratie. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F3-07 - Inschrijving en verbintenissen naar de kernregistratie

*Beeld: stroomt: Persoon en verbintenissen vastleggen in de kernregistratie. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Voorziening Centraal Aanmelden (CAMBO) naar Kernregistratie systeem studenten (KRS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F3-08 - Student, verbintenis, groep en behaalde leeruitkomsten naar het studentkeuzesysteem

*Beeld: stroomt: Persoon en verbintenissen vastleggen in de kernregistratie. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Kernregistratie systeem studenten (KRS) naar Student Keuze Systeem (SKS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

## Fase 4: Detailleren, roosteren en inschrijven

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 4.

> Ontstaat: `Leeronderdeel specificatie`, `Les specificatie`, `Leergelegenheid`, `Lesgelegenheid`, `Medewerker`, `Onderwijseenheid aanbod verbintenis`, `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis`, `Opleidingsprogramma aanbod verbintenis`.

*Beeld: De hoofdplaat met de stromen van fase 4 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F4-01 - Het leeronderdeel fijnmazig: lessenreeks en les

*Beeld: ontstaat: Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F4-02 - Detailspecificaties naar het LMS

*Beeld: stroomt: Detailspecificaties leveren aan het LMS. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Leer management systeem (LMS), OC-LMS.

*Schrijf hier de uitwerking.*

### F4-03 - De les en de toets van binnen, elk met hun eigen onderdelen (conceptplaat)

*Beeld: stroomt: Detailspecificaties leveren aan het LMS. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Leer management systeem (LMS), OC-LMS.

*Schrijf hier de uitwerking.*

### F4-04 - Summatieve resultaatstructuur naar het studentvolgsysteem

*Beeld: stroomt: Detailspecificaties leveren aan het LMS. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Student volg systeem (SVS), OC-SVS.

*Schrijf hier de uitwerking.*

### F4-05 - Summatieve resultaatstructuur naar de kernregistratie

*Beeld: stroomt: Detailspecificaties leveren aan het LMS. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Kernregistratie systeem studenten (KRS), OC-KRS.

*Schrijf hier de uitwerking.*

### F4-06 - Plaatsingsgroepen naar planning

*Beeld: stroomt: Plaatsings- en planninggroepen definieren en aan personen koppelen. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Kernregistratie systeem studenten (KRS) naar Planningssysteem, zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F4-07 - Te roosteren leergelegenheden naar het roostersysteem

*Beeld: stroomt: Te roosteren specificaties aan het roostersysteem geven. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Roostersysteem, zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F4-08 - Roosteren: lesgelegenheid, lokaal en docent

*Beeld: ontstaat: Leer-, les- en toetsgelegenheden roosteren. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F4-09 - <student>s verbintenissen op de geroosterde gelegenheden

*Beeld: ontstaat: Verwachte deelnemers delen en toegang geven. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F4-10 - Student, verbintenissen en groep naar het LMS

*Beeld: stroomt: Verwachte deelnemers delen en toegang geven. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Roostersysteem naar Leer management systeem (LMS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F4-11 - Verbintenissen op alle niveaus naar het studentvolgsysteem

*Beeld: stroomt: Verwachte deelnemers delen en toegang geven. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Kernregistratie systeem studenten (KRS) naar Student volg systeem (SVS), geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

### Variant capaciteitsgestuurd

> De uitwerking van Jochem schrijft hier: Het keuzedeel wordt pas geroosterd na de toewijzing in fase 6;

> Hieraan gaan vooraf: F2-C01.

*Schrijf hier de uitwerking.*

#### F4-C01 - Na de toewijzing: de keuzedeelgroep met vaste capaciteit naar het roostersysteem

*Beeld: stroomt: Keuzedeelgroep met vaste capaciteit aan het roostersysteem geven. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Roostersysteem, zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

## Fase 5: Onderwijs uitvoeren en voortgang begeleiden

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 5.

> Ontstaat: `Lesgelegenheid verbintenis`, `Aanwezigheid`, `Lesgelegenheid resultaat`, `Toetsgelegenheid verbintenis`, `Formatieve resultaat structuur`, `Toetsonderdeel weging`, `Toetsgelegenheid resultaat`, `Formatief resultaat`, `Formatieve beoordeling`, `Persoonlijke ontwikkeling`, `Leergelegenheid resultaat` ...

*Beeld: De hoofdplaat met de stromen van fase 5 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F5-01 - Les gevolgd: aanwezigheid en lesresultaat

*Beeld: ontstaat: Onderwijs verzorgen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F5-02 - De verbintenis op de toetsgelegenheid: geplaatst of zelf gekozen

*Beeld: ontstaat: Toetsmomenten plannen tijdens lessen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F5-03 - Formatieve voortgang: structuur, resultaten en beoordeling

*Beeld: ontstaat: Formatieve voortgang bijhouden. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F5-04 - Formatieve resultaten van het LMS naar het studentvolgsysteem

*Beeld: stroomt: Formatieve voortgang bijhouden. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Leer management systeem (LMS) naar Student volg systeem (SVS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F5-05 - Studiebeeld: de nominale route naast wat <student> heeft behaald

*Beeld: ontstaat: Studiebeeld volgen in het studentvolgsysteem. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

## Fase 6: Organiseren van keuzemomenten

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 6.

> Ontstaat: `Keuzedeel aanbod`, `Aanmelding`, `Keuzedeel aanbod verbintenis`, `Inschrijving`.

*Beeld: De hoofdplaat met de stromen van fase 6 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F6-01 - Keuzedeelaanbod ontsloten

*Beeld: ontstaat: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F6-02 - Keuzedeelaanbod, specificatie en regels naar het studentkeuzesysteem

*Beeld: stroomt: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Onderwijscatalogus naar Student Keuze Systeem (SKS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F6-03 - <student>s aanmelding op het keuzedeelaanbod, met zijn voorkeurslijst

*Beeld: ontstaat: Voorkeurslijst samenstellen in het studentkeuzesysteem. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F6-04 - Keuzestelling naar planning

*Beeld: stroomt: Voorkeurslijst samenstellen in het studentkeuzesysteem. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Student Keuze Systeem (SKS) naar Planningssysteem, zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F6-05 - Definitieve keuzes verwerkt naar groepen en capaciteit

*Beeld: ontstaat: Definitieve keuzes verwerken naar groepen en capaciteit. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F6-06 - Geactualiseerd keuzedeelaanbod terug naar de catalogus

*Beeld: stroomt: Planbaar aanbod actualiseren. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Onderwijscatalogus, OC-P&R.

*Schrijf hier de uitwerking.*

### F6-07 - De aanmelding wordt een inschrijving op het keuzedeel

*Beeld: ontstaat: Keuzedeel formeel inschrijven. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F6-08 - Keuzedeelverbintenis naar de kernregistratie

*Beeld: stroomt: Keuzedeel formeel inschrijven. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Student Keuze Systeem (SKS) naar Kernregistratie systeem studenten (KRS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### Variant capaciteitsgestuurd

> De uitwerking van Jochem schrijft hier: In deze vorm kiest de student op een geplande leergelegenheid.

> Hieraan gaan vooraf: F6-01, F6-02, F6-03, F6-04.

> Vervalt in deze vorm of schuift hierheen: F6-05, F6-07.

*Schrijf hier de uitwerking.*

#### F6-C01 - Capaciteit vastgesteld na de animo

*Beeld: ontstaat: Capaciteit vaststellen na de animo. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

#### F6-C02 - Geplande leergelegenheid naar het studentkeuzesysteem

*Beeld: stroomt: Geplande leergelegenheden ontsluiten naar het studentkeuzesysteem. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Student Keuze Systeem (SKS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

#### F6-C03 - <student> kiest een plek op de geplande leergelegenheid

*Beeld: ontstaat: Plek kiezen op een geplande leergelegenheid. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

#### F6-C04 - Toegewezen binnen de capaciteit: inschrijving op het keuzedeel

*Beeld: ontstaat: Toewijzen binnen de capaciteit. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

## Fase 7: Bijsturen planning en aanbod

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 7.

> Ontstaat: `Plaatsingsgroep`, `Onderwijseenheid aanbod verbintenis`, `Onderwijseenheid aanbod`.

*Beeld: De hoofdplaat met de stromen van fase 7 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F7-01 - Afwijkingen verzameld in een plaatsingsgroep

*Beeld: ontstaat: Afwijkingen verzamelen in een planninggroep. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F7-02 - Onderwijseenheid-aanbodverbintenis geannuleerd

*Beeld: ontstaat: Bestaande verbintenissen annuleren. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F7-03 - Plaatsingsgroep van de kernregistratie naar planning

*Beeld: stroomt: Bestaande verbintenissen annuleren. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Kernregistratie systeem studenten (KRS) naar Planningssysteem, zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### F7-04 - Nieuw aanbod voor de plaatsingsgroep

*Beeld: ontstaat: Nieuw aanbod maken en publiceren. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F7-05 - Bijgestuurd aanbod naar de catalogus

*Beeld: stroomt: Nieuw aanbod maken en publiceren. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Onderwijscatalogus, OC-P&R.

*Schrijf hier de uitwerking.*

### F7-06 - Nieuwe leergelegenheden naar het roostersysteem

*Beeld: stroomt: Nieuw aanbod maken en publiceren. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Roostersysteem, zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

### Variant capaciteitsgestuurd

> De uitwerking van Jochem schrijft hier: Bij bijsturen blijft de bestaande planninggroep staan: een plek die vrijkomt, gaat binnen de capaciteit terug naar het studentkeuzesysteem.

*Schrijf hier de uitwerking.*

#### F7-C01 - Een plek komt vrij binnen de capaciteit

*Beeld: ontstaat: Vrijgekomen plek binnen de capaciteit verwerken. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

#### F7-C02 - De vrije plek terug naar het studentkeuzesysteem

*Beeld: stroomt: Vrije plek ontsluiten naar het studentkeuzesysteem. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Planningssysteem naar Student Keuze Systeem (SKS), zonder koppelingspecificatie.

*Schrijf hier de uitwerking.*

## Fase 8: Examineren, vaststellen en diplomeren

> De uitwerking van Jochem schrijft hier: De fase in detail: kaderscenario leerroute 1, fase 8.

> Ontstaat: `Examengelegenheid`, `Examengelegenheid verbintenis`, `Examengelegenheid resultaat`, `Zitting`, `Zittingsrapport`, `Examendossier`, `Summatief resultaat`, `Summatieve beoordeling`, `Opleidingsprogramma resultaat`, `Keuzedeel resultaat`, `Opleiding resultaat`, `Waarde document (diploma / certificaat)`.

*Beeld: De hoofdplaat met de stromen van fase 8 gemarkeerd. Voeg hier het beeld in.*

> De gemarkeerde lijnen zijn de stromen die deze fase raakt, met het beeld waarin ze staan;

*Schrijf hier de uitwerking.*

### F8-01 - Examengelegenheid uit de examenspecificatie

*Beeld: ontstaat: Examenspecificaties omzetten in examengelegenheden. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F8-02 - Kandidatenlijst: verbintenis op de examengelegenheid

*Beeld: ontstaat: Kandidatenlijsten samenstellen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F8-03 - Afname en beoordeling: de proeve individueel, een centraal examen in een zitting

*Beeld: ontstaat: Zitting uitvoeren en resultaten doorgeven. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F8-04 - Examenresultaat naar het studentvolgsysteem

*Beeld: stroomt: Zitting uitvoeren en resultaten doorgeven. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Toets- en examen afname systeem naar Student volg systeem (SVS), geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

### F8-05 - Summatief vastgesteld: resultaten en beoordeling

*Beeld: ontstaat: Summatief vaststellen. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

### F8-06 - Vaststelling naar de kernregistratie

*Beeld: stroomt: Summatief vaststellen. Voeg hier het beeld in.*

> De uitwerking van Jochem schrijft hier: Interactie: Student volg systeem (SVS) naar Kernregistratie systeem studenten (KRS), geen pijl op de hoofdplaat.

*Schrijf hier de uitwerking.*

### F8-07 - Gediplomeerd: opleidingsresultaat en diploma

*Beeld: ontstaat: Kwalificering en diplomering registreren. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

## Bijlage: alle objecttypen per begrippenfamilie

> De uitwerking van Jochem schrijft hier: Per objecttype het beeld waarin hij verschijnt (het ID uit de kop), de instantie voor Jochem, de fase, de status van de definitie in de begrippenlijst en het OEAPI-object uit de mapping.

*Schrijf hier de uitwerking.*

### Kwalificatiekader

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Onderwijskundig kader instelling

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Onderwijsspecificatie

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Onderwijsaanbod

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Onderwijsverbintenis

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Onderwijsresultaat

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Resultaatstructuur

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Buiten de kolommen (persoon, groep, cohort, verzoek)

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

## Vragen aan de kerngroep

> De uitwerking van Jochem schrijft hier: De vragen die de regels zelf oproepen, met de regel waar de vraag zichtbaar wordt.

> 1. Het cohort hangt op de plaat aan de student (Student heeft toegang tot Cohort / periode), terwijl een student meerdere verbintenissen kan hebben die elk op een eigen moment starten.

*Schrijf hier de uitwerking.*

### Vragen, vervolg (2 van 3)

> De uitwerking van Jochem schrijft hier: 8. De conceptplaat noemt hier Examenmoment, Examen instrument en Examen.

*Schrijf hier de uitwerking.*

### Vragen, vervolg (3 van 3)

> De uitwerking van Jochem schrijft hier: 15. Welk systeem start het keuzemoment van een student? Planning is het enige systeem met een notie van onderwijsperiode, het keuzesysteem beheert de regels, en de SLB'er heeft in de praktijk een evaluatierol.

> De eerste 7 vragen gaan als ronde mee naar de kerngroep; dat is wat een sessie kan wegen.

> Vragen over patronen, schema's, de toetslijst en endpoints horen bij de koppelvlakspecificatie en staan hier niet.

*Schrijf hier de uitwerking.*

## Regelregister

> De uitwerking van Jochem schrijft hier: Elke regel onder het ID en de titel van haar beeld (fase, stap, bestand) met de bron.

> F1-01 - Het kwalificatiedossier ontleed (fase 1, Kwalificatiedossier analyseren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F1-02 - Examenplan, eerste resultaatstructuur en cohort (fase 1, Examenplan opstellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F1-03 - Leeruitkomsten uit het dossier, in de stem van de instelling (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F1-04 - De leeruitkomst in CompetentNL-skills (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-05 - De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-06 - De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen (fase 1, Kwalificatiedossier vertalen naar leeruitkomsten;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-07 - De opleidingsspecificatie met programma, eenheden en keuzedeelruimte (fase 1, Opleidingsspecificatie met programma en eenheden beschrijven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-08 - Kiesbaar onderwijsprogrammaonderdeel: keuzedelen en minor (fase 1, Keuzedeelprogramma als eigen specificatie vormgeven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-09 - Toetsonderdelen, wegingen en afrondingscriterium (fase 1, Toetsonderdelen en resultaatstructuur uit het examenplan afleiden;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-10 - De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte (fase 1, Exameninstrumenten bepalen, inkopen of construeren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-11 - Het examenplan vastgesteld (fase 1, Examenplan vaststellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

> F1-12 - De opleiding zoals ontworpen naar de catalogus (fase 1, Grofmazig resultaat publiceren naar de onderwijscatalogus;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F1-13 - Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat) (fase 1, Grofmazig resultaat publiceren naar de onderwijscatalogus;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F2-01 - De specificatie planbaar gemaakt (fase 2, Specificatie aanvullen tot planbare specificatie;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F2-02 - Het verzoek om onderwijsaanbod (fase 2, Planningssysteem verzoeken om onderwijsaanbod;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning (fase 2, Planningssysteem verzoeken om onderwijsaanbod;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F2-04 - De specificatie op haalbaarheid getoetst (fase 2, Specificatie op haalbaarheid toetsen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

> F2-05 - De aanbodvraag naast de schaarste van ruimtes en mensen (conceptplaat) (fase 2, Aanbodvraag per opleiding bepalen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F2-06 - De jaarplanning op instellingsniveau (conceptplaat) (fase 2, Jaarplanning op instellingsniveau vaststellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F2-07 - Examenbehoefte uit de resultaatstructuur (conceptplaat) (fase 2, Jaarplanning op instellingsniveau vaststellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F2-08 - Het aanbod gepland: opleiding, programma, eenheid, gelegenheid (fase 2, Aanbod plannen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F2-09 - Het geplande aanbod terug naar de catalogus (fase 2, Gepland aanbod terugleveren aan de onderwijscatalogus;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F3-01 - Aanmeldbaar aanbod naar de kernregistratie (fase 3, Orienteren op het gepubliceerde aanbod;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F3-02 - Aanmeldbaar aanbod van de kernregistratie naar AII (fase 3, Orienteren op het gepubliceerde aanbod;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F3-03 - Jochem meldt zich aan: aanmelding en verbintenissen (fase 3, Aanmelden via het intakesysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F3-04 - De aanmelding van de voorziening naar het intakesysteem (fase 3, Aanmelden via het intakesysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F3-05 - Intake: student en plaatsingsgroep (fase 3, Intake doorlopen en plaatsen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

> F3-06 - Inschrijving: van aangemeld naar ingeschreven (fase 3, Persoon en verbintenissen vastleggen in de kernregistratie;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F3-07 - Inschrijving en verbintenissen naar de kernregistratie (fase 3, Persoon en verbintenissen vastleggen in de kernregistratie;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F3-08 - Student, verbintenis, groep en behaalde leeruitkomsten naar het studentkeuzesysteem (fase 3, Persoon en verbintenissen vastleggen in de kernregistratie;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F4-01 - Het leeronderdeel fijnmazig: lessenreeks en les (fase 4, Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F4-02 - Detailspecificaties naar het LMS (fase 4, Detailspecificaties leveren aan het LMS;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F4-03 - De les en de toets van binnen, elk met hun eigen onderdelen (conceptplaat) (fase 4, Detailspecificaties leveren aan het LMS;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F4-04 - Summatieve resultaatstructuur naar het studentvolgsysteem (fase 4, Detailspecificaties leveren aan het LMS;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F4-05 - Summatieve resultaatstructuur naar de kernregistratie (fase 4, Detailspecificaties leveren aan het LMS;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F4-06 - Plaatsingsgroepen naar planning (fase 4, Plaatsings- en planninggroepen definieren en aan personen koppelen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F4-07 - Te roosteren leergelegenheden naar het roostersysteem (fase 4, Te roosteren specificaties aan het roostersysteem geven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F4-08 - Roosteren: lesgelegenheid, lokaal en docent (fase 4, Leer-, les- en toetsgelegenheden roosteren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F4-09 - Jochems verbintenissen op de geroosterde gelegenheden (fase 4, Verwachte deelnemers delen en toegang geven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F4-10 - Student, verbintenissen en groep naar het LMS (fase 4, Verwachte deelnemers delen en toegang geven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F4-11 - Verbintenissen op alle niveaus naar het studentvolgsysteem (fase 4, Verwachte deelnemers delen en toegang geven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F5-01 - Les gevolgd: aanwezigheid en lesresultaat (fase 5, Onderwijs verzorgen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F5-02 - De verbintenis op de toetsgelegenheid: geplaatst of zelf gekozen (fase 5, Toetsmomenten plannen tijdens lessen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F5-03 - Formatieve voortgang: structuur, resultaten en beoordeling (fase 5, Formatieve voortgang bijhouden;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F5-04 - Formatieve resultaten van het LMS naar het studentvolgsysteem (fase 5, Formatieve voortgang bijhouden;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

> F5-05 - Studiebeeld: de nominale route naast wat Jochem heeft behaald (fase 5, Studiebeeld volgen in het studentvolgsysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F6-01 - Keuzedeelaanbod ontsloten (fase 6, Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F6-02 - Keuzedeelaanbod, specificatie en regels naar het studentkeuzesysteem (fase 6, Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F6-03 - Jochems aanmelding op het keuzedeelaanbod, met zijn voorkeurslijst (fase 6, Voorkeurslijst samenstellen in het studentkeuzesysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

> F6-04 - Keuzestelling naar planning (fase 6, Voorkeurslijst samenstellen in het studentkeuzesysteem;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F6-05 - Definitieve keuzes verwerkt naar groepen en capaciteit (fase 6, Definitieve keuzes verwerken naar groepen en capaciteit;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F6-06 - Geactualiseerd keuzedeelaanbod terug naar de catalogus (fase 6, Planbaar aanbod actualiseren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F6-07 - De aanmelding wordt een inschrijving op het keuzedeel (fase 6, Keuzedeel formeel inschrijven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

> F6-08 - Keuzedeelverbintenis naar de kernregistratie (fase 6, Keuzedeel formeel inschrijven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F7-01 - Afwijkingen verzameld in een plaatsingsgroep (fase 7, Afwijkingen verzamelen in een planninggroep;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F7-02 - Onderwijseenheid-aanbodverbintenis geannuleerd (fase 7, Bestaande verbintenissen annuleren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F7-03 - Plaatsingsgroep van de kernregistratie naar planning (fase 7, Bestaande verbintenissen annuleren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F7-04 - Nieuw aanbod voor de plaatsingsgroep (fase 7, Nieuw aanbod maken en publiceren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F7-05 - Bijgestuurd aanbod naar de catalogus (fase 7, Nieuw aanbod maken en publiceren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F7-06 - Nieuwe leergelegenheden naar het roostersysteem (fase 7, Nieuw aanbod maken en publiceren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F8-01 - Examengelegenheid uit de examenspecificatie (fase 8, Examenspecificaties omzetten in examengelegenheden;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F8-02 - Kandidatenlijst: verbintenis op de examengelegenheid (fase 8, Kandidatenlijsten samenstellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F8-03 - Afname en beoordeling: de proeve individueel, een centraal examen in een zitting (fase 8, Zitting uitvoeren en resultaten doorgeven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> F8-04 - Examenresultaat naar het studentvolgsysteem (fase 8, Zitting uitvoeren en resultaten doorgeven;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

> F8-05 - Summatief vastgesteld: resultaten en beoordeling (fase 8, Summatief vaststellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

> F8-06 - Vaststelling naar de kernregistratie (fase 8, Summatief vaststellen;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> F8-07 - Gediplomeerd: opleidingsresultaat en diploma (fase 8, Kwalificering en diplomering registreren;

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

## Afwijkingen per instelling

Wat bij een instelling anders gaat dan hierboven staat, per regel met de instelling erbij. Dit is geen restcategorie: hier staat het materiaal waaruit blijkt of de grootst gemene deler houdbaar is.

| Instelling | Hoofdstuk | Wat daar anders gaat |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

## Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het speelt.

| Nummer | Hoofdstuk | Vraag |
|---|---|------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
