# Sjabloon leerroute-kaderscenario

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een kaderscenario: een leerroute uitgewerkt tot het punt waarop duidelijk is welke informatie waarheen moet. Het is kaderstellend, dus geen anekdote en geen instellingsontwerp |
| Wie dit invult | de adviesgroep. Suggestie: de BOP-adviseurs en de business analisten samen, met de onderwijskundige kant bij de adviesgroep zelf |
| Voorbeelduitwerking | [kaderscenario leerroute 1](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Vaste koppen

De koppen in dit document blijven staan zoals zij hier staan. In het agent-harnas komt een lezer (parser) die een ingevuld document per kop terugvertaalt naar de kennisbank; een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt dus zijn kop, met de reden eronder.

Dit sjabloon is afgeleid uit [kaderscenario leerroute 1](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md), dus het draagt elke kop en elke tabel van die uitwerking. Wat daar algemeen was staat er nog. Wat daar aan die ene uitwerking hing, staat er als ingesprongen citaat, met *Schrijf hier de uitwerking.* eronder: daar hoort de eigen uitwerking. Een lege tabel heeft evenveel rijen als de uitwerking had, zodat zichtbaar is hoeveel er wordt verwacht.

## De grootst gemene deler

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier dubbel, want een kaderscenario is wat OKx als afspraak vastlegt: een procesgewoonte van een instelling die hier als kader belandt, wordt een eis aan elke leverancier.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

## Inleiding

**Doel.** De leerroute-uitwerking van OKx volgens de [AMIGO-aanpak](https://www.edustandaard.nl/amigo/aanpak/), stap 1 tot en met 3 (scenario-analyse, gegevensanalyse en interactie-analyse): per Npuls-leerroute vastleggen wat de keten moet kunnen, in begrippen, actoren, betrokken systemen en informatiestromen. Dit is de kaderstelling waar de requirementsboom en de koppelingspecificaties op bouwen. Het document heette eerder "OKx OEAPI consumer-profiel"; die naam dekte de lading niet en zette de techniekkeuze voorop.

> Leerroute 1 schrijft hier: Scope. Leerroute 1 (regulier) is volledig uitgewerkt en vormt de basis;

**Verhouding tot de scenario-uitwerkingen.** Dit document beschrijft het kader per leerroute: wat de keten moet kunnen. De [scenario-uitwerkingen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/README.md) maken dat kader concreet en toetsbaar met één persona die de keten doorloopt, als opstapje naar testgedreven ontwikkeling (test driven development).

> Leeswijzer. Het begrippenkader met de ankertabel definieert de zes begrippenfamilies, de niveaus en de stadia;

**Voor wie.** Kernteam OKx, kerngroep techniek, architecten, leveranciers en professionals van instellingen.

*Schrijf hier de uitwerking.*

## 1. Wat is OKx en wat wil het bereiken?

### 1.1 Wat is OKx?

OKx is een afspraakstelsel, leunend op een gegevensstandaard om onderwijs op de lange termijn **flexibeler** te maken, zonder dat iedere instelling en leverancier opnieuw dezelfde vertaalslag hoeft te doen. De kern is dat studenten onderwijs op verschillende manieren moeten kunnen volgen en combineren, terwijl instellingen het onderwijs nog steeds **organiseerbaar** moeten houden.

De Npuls-leerroutes (zie [§3.5](#35-scenario-analyse--start) en [§3.2.1](#321-de-npuls-leerroutes)) maken dit concreet. Ze beschrijven varianten zoals regulier, versneld (bijv. met vrijstellingen/EVC), personaliseren binnen de instelling, personaliseren over de instellingsgrens (binnen sector) en modulair studeren (vrije keuze, bundelen, stapelen).

### 1.2 Wat wil OKx bereiken?

In alle leerroutes komt dezelfde ketenvraag terug:

- Hoe vindt een student passend onderwijsaanbod?
- Hoe maken we zichtbaar *wat* het onderwijs is én *hoe* het georganiseerd wordt (tijd, leervorm, ruimte, expertise, middelen)?
- Hoe kunnen planning en roostering bepalen of het uitvoerbaar is (capaciteit, mensen en middelen)?
- Hoe leggen we keuze/intekening/inschrijving en voortgang vast, zodat het herleidbaar en overdraagbaar blijft?

OKx werkt toe naar de volgende resultaten (bron: projectplan OKx v202506):

1. Komen tot **gezamenlijke taal** en **standaarden** voor gegevensuitwisseling die een **scala aan flexibilisering** mogelijk maken.
2. Komen tot **functionele** en **technische gegevensuitwisseling** voor het mbo, hbo en wo die **studentmobiliteit** ondersteunen.
3. Pilot studentmobiliteit starten bij mbo: **implementatie en realisatie van de digitale koppelingen**, eventueel met gebruik van bestaande SURF-diensten.

### 1.3 Scope

Dit profiel is in eerste instantie gericht op het **mbo**, omdat het direct aansluit op het werk van OKx in de mbo-keten en omdat de use-cases rond keuze, planning, roostering en modulair aanbod daar het meest urgent en concreet zijn. Tegelijk moet het profiel op termijn **sector-overstijgend** en **nationaal** kunnen werken, zodat onderwijsaanbod en leerresultaten uitwisselbaar worden over instellingen en (waar passend) over sectoren heen.

OKx sluit aan op het lopende initiatief **Klus 53** (MBO-Digitaal): alignment van **MORA** en **HORA** als basis voor het informatiemodel in dit profiel (zie ook §3.3.1.2.5).

### 1.4 Koppelvlakken als doel én als middel

Koppelvlakken maken het mogelijk dat systemen in de keten dezelfde kerninformatie **op dezelfde manier** uitwisselen. Daarmee kan een onderwijscatalogus aanbod vindbaar en vergelijkbaar maken, kan een planningssysteem haalbaarheid berekenen en capaciteit terugkoppelen, kan een roostersysteem het onderwijs in tijdsloten, en worden studenten o.b.v. inschrijvingen en keuzes geroosterd en aan de bijbehorende cursussen in het leermanagement systeem gekoppeld.

Zonder deze afspraken blijft flexibilisering beperkt tot losse pilots en lokale interpretaties. Vanuit OKx wordt geïnventariseerd welke interactiepatronen en scenario's er mogelijk dienen te zijn; de specificatie toetst daaraan. Dit kan resulteren in ketenscenario's die een school samen met leveranciers kan implementeren. **Hoe** scholen en leveranciers koppelvlakken inzetten (met of zonder integratielaag) wordt niet voorgeschreven. OKx neemt daarin een **adviserende** rol. De route van kader naar implementatie loopt via de [projectdeliverables](#2-hoe-okx-dat-bereikt-projectdeliverables) in §2.

## 2. Hoe OKx dat bereikt: projectdeliverables

### 2.1 Deliverable-keten

OKx levert een samenhangende keten van **projectdeliverables** — van kaderstelling tot borging in de sector. Het volgende diagram geeft deze deliverables en de volgordelijkheid hiervan weer:

**Leeswijzer.** De [deliverable-keten en versionering](https://github.com/Npuls-OKx/meta/blob/dev/../doc/
OKx_Release-management-en-versionering.md#1-doel-en-scope) staan in het release-document; 
[ketenplaat, BOPSI en projectfase](https://github.com/Npuls-OKx/meta/blob/dev/project/projectdocumentatie/projectplan-okx.md) in het 
projectplan.

Het diagram leest **van boven naar beneden**: **meta** (kaderstelling) bovenaan, **spec**, adoptie 
en borging onderaan. Onder het diagram: terugkoppeling van **wijzigingsverzoeken**.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Nummering vanaf §3.2.1 (scenario-uitwerkingen) volgt nog een oudere indeling en wordt in een 
volgende pass opgeschoond.*

| Stap | Deliverable | Korte omschrijving |
|------|-------------|-------------------|
| 1 | **Referentiekader / business architectuur** | Begrippenkader, sectorarchitecturen, procesbeeld (scenario's, persona's), informatiemodellen, informatiestromen, interactieanalyse |
| 2 | **Specificatiedocument** (dit document) | Data-uitwisselingstandaard op businesslaag: endpoints, interactiepatronen, sequentiediagrammen, datamodel, security |
| 3 | **OEAPI OpenAPI** (spec-repo) | Technische implementatie — bouwbaar en testbaar koppelvlak |
| 4 | **Instelling acceptatie-pilots** | Instellingen en leveranciers toetsen de standaard in de praktijk |
| 5 | **Adoptie via BOPSI** | Business architectuur en datamodel mappen; koppelingen met instellingssystemen activeren |
| 6 | **Borging** | Overdracht naar lijnorganisaties na afloop Npuls |

### 2.2 Repositories meta en spec

| Repository | Scope | Rol |
|------------|-------|-----|
| [**meta**](https://github.com/Npuls-OKx/meta) | **Kaderstelling** t/m **specificatiedocument** (businesslaag) | *Wat* de standaard betekent en *hoe* uitwisseling conceptueel is afgesproken |
| **OEAPI-profiel** | **OEAPI OpenAPI** | Overlay op een vastgezette OEAPI-versie, als submodule |

Versiebeheer en releases: [OKx Release management en versionering](https://github.com/Npuls-OKx/meta/blob/dev/project/release-management-en-versionering.md).

### 2.3 Terugkoppeling

Vanaf **OEAPI OpenAPI**, **instelling acceptatie-pilots**, **adoptie via BOPSI** en **borging** kunnen **wijzigingsverzoeken** terug naar **kaderstelling** in meta (zie diagram onder de inleiding). Daar worden ze verwerkt in nieuwe meta-/spec-releases. De eerste reviewbare kaderrelease (`v0.1.0`) wordt ter beoordeling aan de **kerngroep techniek** voorgelegd voordat de spec-implementatie start.

### 2.4 Werkwijze: AMIGO

Om van kaderstelling naar een bouwbare afsprakenset te komen hanteren we de **AMIGO-aanpak**, zoals beschreven door Edustandaard. Zie [AMIGO aanpak](https://www.edustandaard.nl/amigo/aanpak/).

AMIGO leidt stapsgewijs tot een **afsprakenset** (bouwbare uitwisselspecificatie), door scenario's te verhelderen en die te vertalen naar gegevens, interacties en uiteindelijk bericht- en interfacespecificaties. De stappen worden soms iteratief doorlopen: keuzes in bericht of interface kunnen aanleiding zijn om scenario, gegevens of interacties aan te scherpen. De referentiekader-deliverables (§2.1 stap 1) voeden de scenario- en analysefase; dit specificatiedocument (stap 2) en de OpenAPI-spec (stap 3) zijn het resultaat op business- respectievelijk technische laag.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

### 2.5 Werken onder architectuur

De projectdoelstellingen (§1.2) brengen twee implicaties met zich mee:

1. **Werken onder architectuur**: we sluiten aan op (sectorale en nationale) architectuurkaders, zodat afspraken herbruikbaar en uitlegbaar blijven.
2. **Werken met en streven naar sectorstandaarden**: we gebruiken waar mogelijk bestaande standaarden en brengen gaps terug als change requests (in plaats van lokale varianten te "verharden").

Dit sluit aan op de deliverable **sectorarchitecturen** (MOSA, HOSA, ROSA, MORA, HORA). Onderstaande schets toont ROSA als knooppunt van architectuurkennis, met sectorale referentiearchitecturen (waaronder MORA voor het mbo).

*Beeld: De ROSA als knooppunt van architectuurkennis. Voeg hier het beeld in.*

## 3. Dit document in de keten

### 3.1 Wat is dit document?

Een OEAPI **consumer profiel** (`consumerKey: "okx"`) waarmee de **Onderwijscatalogus (OC)** — als centrale referentiecomponent — haar informatiestromen verrijkt met een **complete onderwijsspecificatie**. Niet alleen *wat* er geleerd wordt, maar ook *hoe*, *waarmee*, *door wie*, *waar* en *hoe lang* — op elk niveau van de hiërarchie.

Dit profiel maakt maximaal gebruik van het **recursieve OEAPI-datamodel** en voegt een gestructureerd specificatie-object toe waar de kern onvoldoende is. Het resultaat is bruikbaar voor:

- **Studenten** die top-down (nominaal programma) of bottom-up (zelf samenstellen) kiezen
- **Planners** die moeten bepalen of de instelling een onderwijswens kan realiseren
- **Onderwijs ontwerpers** die opleidingen en gerelateerde onderwijsprogramma's als curriculum ontwerpen en verdieping vragen binnen de Onderwijscatalogus
- **Onderwijsontwikkelaars** die grofmazige onderwijsspecificaties binnen een curriculum specificeren tot planbare en uitvoerbare onderwijsspecificaties voor onderwijsprofessionals
- **Andere instellingen** die aanbod willen ontvangen en verwerken (interoperabiliteit)

### 3.2 Wat levert dit document op?

Onderstaande tabel koppelt deliverables uit de keten (§2) aan de plek waar ze nu leven: dit document, de bestanden ernaast, de koppelingspecificaties in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) of het [archief](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md) (oudere top-down concepten, niet normatief).

| Deliverable | Waar |
|-------------|----------------------|
| Begrippenkader | [begrippenkader.md](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) met de ankertabel en de stadia |
| Sectorarchitecturen | §2.5, MORA/HORA in §3.3.1.2.5 |
| OKx principes en uitgangspunten | [architectuurprincipes](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md) en [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) in Public |
| Procesbeeld · scenario's · persona's | §3.5, §3.2.1 en verder, [scenario-uitwerkingen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/README.md) |
| Informatiemodellen | conceptmodellen in het [archief](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md); terugkoppeling volgt uit de payload-specificaties (Public) |
| Informatiestromen | de informatiestromenplaat en het blok "Betrokken systemen bij gegevensuitwisseling" in de leerroute-1-uitwerking; [hoofdplaat](https://github.com/Npuls-OKx/meta/blob/dev/README.md) |
| Interactieanalyse | het blok "Applicatiecomponenten op de plaat" in de leerroute-1-uitwerking; oudere interactiepatronen in het [archief](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md) |
| Endpointbeschrijvingen | koppelingspecificaties en endpoint-sets in Public |
| Interactiepatronen | patroonsecties van de koppelingspecificaties in Public |
| Sequentiediagrammen | koppelingspecificaties in Public; oudere versies in het [archief](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md) |
| Datamodel | payload-specificaties in Public, bottom-up en endpoint-gedreven |
| Requirementsboom (opdracht, epics, features, stories) | [requirementsboom](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md); elk scenario benoemt in zijn veld Verantwoordt de stories die eruit volgen, en elke story wijst met zijn bron terug naar de passage hier |
| Security | uitwerking volgt; oudere ontwerpkeuzes in het [archief](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md) |
| OEAPI OpenAPI (profiel) | *Buiten dit document*: een overlay op de OEAPI-specificatie, als submodule |
| Pilots · BOPSI · borging | [projectplan](https://github.com/Npuls-OKx/meta/blob/dev/project/projectdocumentatie/projectplan-okx.md), [release-doc §1](https://github.com/Npuls-OKx/meta/blob/dev/project/release-management-en-versionering.md#1-doel-en-scope) |

### 3.3 OEAPI-broncode en signaleringen

**OEAPI-broncode wordt niet aangepast.** Signaleringen uit deze uitwerking leiden tot OEAPI change requests (zie het [archief](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/archief-conceptmodellen.md), §9).

### 3.4 Npuls-programmacontext

*Beeld: Een wendbaar georganiseerd onderwijssysteem (tekening). Voeg hier het beeld in.*

We kennen nu al de gangbare groene route. Hiermee kun je als student van het mbo naar het hbo, en van het hbo naar het wo bewegen, of direct vanuit het mbo, hbo of wo naar het werkveld.

Maar naast de bestaande groene route maken we in het vervolgonderwijs meer mogelijk: leerroutes die dwars door het mbo, hbo en wo gaan, waarbij de lerende — zowel de initiële student als de leven lang lerende — regie heeft op haar eigen leerroute.

Die leerroutes zijn divers en kwalitatief van aard, waarbij de lerende een drempelvrij traject heeft. Dat kan op eigen tempo, gepersonaliseerd (binnen de instelling, buiten de instelling of over de sectoren heen) en modulair — een leven lang.

### 3.5 Scenario-analyse — start

In deze paragraaf werken we de 9 leerroutes uit als **kaderstellende scenario's**: ze vormen de basis voor de concrete scenario's en procesbeschrijvingen die we later verder detailleren. Dit is de deliverable **procesbeeld a.d.h.v. scenario's en persona's** uit de keten (§2.1).

Npuls beschrijft de leerroutes primair vanuit het (eerste) studentenperspectief. Voor implementatie binnen het onderwijskundige en onderwijslogistieke domein is dat niet voldoende: om een leerroute te realiseren zijn ook onderwijskundige beschrijvingen, toetsing en onderwijslogistiek nodig. Daarom koppelen we per leerroute expliciet:

- **Wat** wordt geleerd (kwalificatiekader / beoogde leeruitkomsten)
- **Hoe** het wordt aangeleerd: (leervorm, begeleiding, studielast i.d.v. Studie Belastingsuren (SBU) Begeleidde onderwijstijd (BOT), Onbegeleidde onderwijstijd (OOT) en Flexibele uren, onderwijsspecificaties op werkproces- en lesniveau)
- **Hoe** toetsing en bewijsvoering werken (toets-/examenvorm en scope)

Deze zaken refereren aan **Onderwijsspecificatie**.

- **Hoe** de onderwijsspecificatie organiseerbaar is (planning/roostering binnen beperkte tijd en **mensen en middelen**)

Dit concept refereert aan **Onderwijsaanbod**.

- **Hoe** het geplande aanbod door studenten en instellingsmedewerkers daadwerkelijk gevolgd, beoordeeld en geadministreerd wordt.

Dit concept refereert aan **Onderwijsaanbod verbintenis**.

De uitwerking per leerroute volgt in [§3.2.1](#321-de-npuls-leerroutes) en verderop in dit hoofdstuk.

## Kaderstellende specificatie (vervolg)

### 3.2.1 De Npuls Leerroutes

*Beeld: De leerroutes — een overzicht. Voeg hier het beeld in.*

De 9 leerroutes zijn:

- **Standaard route**: [(1) Regulier](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md), [(2) Temporiseren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_larissa.md), [(3) Versnellen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_linda.md)
- **Personaliseren diplomaroute**: (4) Binnen de instelling, (5) Buiten de instelling, binnen de sector, (6) Buiten de instelling, over sectoren heen
- **Modulair studeren**: (7) Vrije keuze, (8) Bundelen, (9) Stapelen

*Met sector bedoelen we hier de volgende onderwijssectoren: het mbo, hbo en wo.*

#### 3.2.1.1 Leerroute <nummer> — <naam van de route>

*Beeld: Conceptbeeld leerroute <nummer> - regulier studeren in samenhang. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: Persona — Jochem (rode draad voor leerroute 1). In de uitwerkingen hieronder volgen we Jochem (17, na het vmbo):

*Schrijf hier de uitwerking.*

#### 3.2.1.1 Wat betekent “<de route in twee woorden>”?

##### 3.2.1.1 De student beleving - De Student Journey

> Leerroute 1 schrijft hier: Vignet — Jochem (oriëntatie en aanmelding). Op de website van de mbo-instelling ziet Jochem de opleiding Apothekersassistent — regulier met start in september, BPV in een openbare apotheek en het gepubliceerde keuzedeelaanbod.

> Vanuit studentperspectief lijkt regulier studeren eenvoudig:

*Schrijf hier de uitwerking.*

##### Keuzedelen

> Leerroute 1 schrijft hier: Vignet — Jochem (keuzedeel-voorkeuren). Jochem stelt een geprioriteerde voorkeurslijst samen met Ondernemerschap in de zorg op plaats 1 (semester 2, locatie A), gevolgd door alternatieven op lagere prioriteit — zoals in de tabel hieronder.

> De keuzedelen worden van te voren als beschikbaar aanbod gepubliceerd en getoond aan de student tijdens zijn/haar aanbod oriëntatie.

> Hieruit volgt story-0013: de student ziet eerst de keuzedelen die de instelling heeft voorgesorteerd.

> Naarmate de student zijn route aflegt, wordt de voortgang van de student gemonitord en de keuze van keuzedelen gefaciliteerd.

> De student meldt zich vervolgens aan op een keuzedeel. Bij deze aanmelding legt de student per keuzedeelprioriteit de voorkeur(s) voor de periode in zijn of haar onderwijsprogramma vast.

> Voorbeeld keuzedeel prioriteitenlijst:

| Voorkeur  | Keuzedeel                            | Onderwijsperiode   | Onderwijslocatie         |
|-----------|--------------------------------------|--------------------|--------------------------|
| | | | |
| | | | |
| | | | |

> In deze lijst geeft de student aan dat 'Ondernemerschap in de zorg' het meest gewenste keuzedeel is, gevolgd door 'Duurzame technologie', enzovoorts.

> Wanneer de student niet het gewenste keuzedeel op de voorkeurs onderwijslocatie en/of voorkeurs onderwijsperiode, dan moet de student op een andere onderwijslocatie kunnen oriënteren op meer passende keuzedelen.

> Als er geen passend aanbod (combinatie keuzedeel en/of onderwijsperiode en/of onderwijslocatie) is voor de student, dan blijft de geplande keuzedeelruimte mogelijk oningevuld.

> Wanneer een passende combinatie van keuzedeel en/of onderwijsperiode en/of onderwijslocatie, voor de student gevonden kan worden, wordt de keuzedeel aanmelding een intekening.

*Schrijf hier de uitwerking.*

##### Wanneer kiest een student keuzedelen?

> Leerroute 1 schrijft hier: De aanmelding voor keuzedelen wordt vast gelegd naarmate de in het onderwijsprogramma geplande keuzdeelruimte dichterbij komt.

> Vignet — Jochem Jochems instelling legt de keuzedeel-aanmelding 1 periode voorafgaande aan de keuzedeelruimte vast.

> Leeswijzer diagram. Rechthoeken zijn processtappen; ruiten zijn beslismomenten;

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

> Figuur - Student Journey Regulier - Proces studentbeleving regulier studeren*

> Wanneer wordt aanmelding een inschrijving?

| Moment | Van (aanmelding) | Naar (inschrijving) | Voorwaarde |
| --- | --- | --- | --- |
| | | | |
| | | | |

> Vignet — Jochem (twee stappen naar inschrijving). Eerst wordt Jochems aanmelding opleiding na positieve plaatsing een inschrijving opleiding en opleidingsprogramma.

*Schrijf hier de uitwerking.*

##### <student>'s onderwijsperiode start

> Leerroute 1 schrijft hier: Jochem het bericht dat zijn 1e keuze voor Ondernemerschap in de zorg is geaccepteerd.

*Schrijf hier de uitwerking.*

##### 3.3.1.2 De Instellingsbeleving - De Instellingsjourney

> Leerroute 1 schrijft hier: Vanuit organisatieperspectief is regulier studeren juist een gecoordineerde ketenprestatie van meerdere actoren.

*Schrijf hier de uitwerking.*

##### De onderwijsinstelling

> Leerroute 1 schrijft hier: Daarom staan we stil bij de organisatie inrichting achter deze leerroute en haar actoren.

> Figuur - Organogram en actoren van een onderwijsinstelling binnen de context van 'regulier' studeren*

> Vignet — Jochem (actoren). In de praktijk ontmoet Jochem zijn SLB'er (instroom en route), vakdocenten (o.a.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

> Eén vorm, vele varianten. Dit organogram toont één veelvoorkomende vorm:

*Schrijf hier de uitwerking.*

##### De procesbeleving achter '<naam van de route>' onderwijs van een Instelling

> Leerroute 1 schrijft hier: Zoals de MORA - de referentiearchitectuur voor het mbo laat zien, is "regulier onderwijs verzorgen" niet één los proces maar een samenhang van hoofdprocessen die samen een school laten werken.

> Figuur - Hoofdprocesmodel MORA 2.6 - 12-05-26*

*Beeld: MORA Hoofdprocesmodel. Voeg hier het beeld in.*

> Hier sluit §2.5 implicatie 1 - werken onder architectuur direct op aan.

> Welke processen moet een onderwijsinstelling faciliteren om 'regulier' studeren te realiseren? Procesketen 3, Onderwijsuitvoering en begeleiding:

*Beeld: MORA Hoofdprocesmodel. Voeg hier het beeld in.*

> Procesketen 4, Onderwijslogistiek:

*Beeld: MORA Hoofdprocesmodel. Voeg hier het beeld in.*

> Procesketen 6, onderwijsontwikkeling:

*Beeld: MORA Hoofdprocesmodel. Voeg hier het beeld in.*

> De Instellingsjourney De MORA beschrijft dus betrokken procesketens, maar het complete proces vergt integratie van de losse ketens.

> In verhalende vorm ziet die instellingsjourney er als volgt uit.

> Vanaf dat moment verschuift de aandacht van ontwerp naar uitvoering.

> Instellings Journey in fasen 1. Kwalificatiekader analyseren en grofmazig ontwerpen:

> Vignet — Jochem door de 8 fasen. (1) De onderwijsontwerper vertaalt Jochems kwalificatiedossier naar een grofmazig programma met keuzedeelruimte.

> Onderstaand figuur is een conceptuele model weergave van de door OKx geobserveerde IST situatie van dit proces.

> Leeswijzer diagram. Fasen 1–5 vormen de lineaire keten van ontwerp tot start uitvoering;

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

> Voetnoot: Het plan en rooster proces is hier bewust conceptueel (vereenvoudigd) weergegeven.

*Schrijf hier de uitwerking.*

##### Scenario's binnen deze leerroute

> Leerroute 1 schrijft hier: Binnen deze leerroute speelt zich niet maar één scenario af.

> De belangrijkste scenario's binnen deze leerroute zijn:

> Happy flow / nominaal verloop: alles gaat goed. De student volgt het programma zoals ontworpen en gepland.

> Incidenteel temporiseren: de student loopt tijdelijk achter door een gebeurtenis in de uitvoering.

> De `happy flow` en de incidentele varianten van temporiseren, versnellen en hybride voortgang zijn niet uniek voor leerroute 1.

*Schrijf hier de uitwerking.*

##### Overige scenario's specifiek voor leerroute <nummer>

> Leerroute 1 schrijft hier: Wisselen van opleiding en behaalde resultaten meenemen: een student volgt eerst een deel van de reguliere route, besluit daarna over te stappen naar een andere opleiding of een ander regulier programma, en wil eerder behaalde resultaten meenemen.

*Schrijf hier de uitwerking.*

##### Switch <naam van de route> onderwijs ↔ set certificaten

> Leerroute 1 schrijft hier: Trigger. Een student wil tussentijds het opleidingsprogramma loslaten en alleen nog certificaten halen (of omgekeerd:

> Actorflow (hoofdlijnen). SLB signaleert de wens → onderwijsontwikkelaar/team beoordeelt haalbaarheid en herontwerp → planner en roosteraar hergroeperen aanbod en capaciteit → KRS/SVS (en aanverwante registratie) moeten verbintenissen, rechtmatigheid en bekostiging actualiseren.

> Informatiestromen-delta t.o.v. reguliere baseline.

| Aspect | Regulier | Switch naar certificaten (of terug) |
| --- | --- | --- |
| | | |
| | | |
| | | |

> KRS/SVS-knelpunten. Systemen zijn ingericht op één doorlopende opleidingsverbintenis;

> Randvoorwaarden (kern).

| Dimensie | Wat moet vastliggen |
| --- | --- |
| | |
| | |
| | |
| | |

> Vervolguitwerking (volledige scenario, negenvlak, interfaces):

> Deze leerroute volgt een sterk aanbod-gestuurd model met hybride kenmerken:

> Alle mbo-instellingen hanteren in de praktijk dit aanbod-gestuurde grondmodel;

| Leerroute | Happy / nominaal | Incidenteel Temporiseren | Incidenteel Versnellen | Incidenteel Hybride | Route-specifiek (voorbeeld) |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

> De uitwerking en specificatie van de scenario's volgt in `HOOFDSTUK X`.

*Schrijf hier de uitwerking.*

##### Betrokken informatie bij proces

> Leerroute 1 schrijft hier: De begrippen in onderstaande tabel vullen het begrippenkader uit paragraaf 2.1 aan.

> Samengevat:

| Vraag                                        | Concept                | Doel/toelichting                                                                                                   |
|----------------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------|
| | | |
| | | |
| | | |
| | | |
| | | |

> De volgende tabel is daarmee de brug tussen het begrippenkader en het gegevensmodel.

| **1. Kwalificatiekader** | **2. Onderwijsspecificatie** | **3. Onderwijsaanbod** | **4. Onderwijsverbintenis** | **5. Onderwijsresultaat** |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

> Voetnoot: Examenonderdelen zijn `speciale` instanties van toetsonderdelen.

> Conceptdefinities per object in het vlakkenmodel (normatieve kern;

| Informatie-object | Conceptdefinitie |
| --- | --- |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

> Cardinaliteit (normatief voor dit profiel):

> `Kwalificatiedossier (1..) Kwalificatie` `Kwalificatie (1..) Kerntaak` `Kerntaak (1..) Werkproces` `Werkproces (1..) Leeruitkomst` (summatief) `Leeruitkomst (0..) Onderwijseenheid` / `Leeronderdeel` / `Toetsonderdeel` (dezelfde LO kan over meerdere onderdelen verdeeld zijn;

> Bovenstaande tabel alligned hiermee met het lopende initiatief onder Klus 53 (MBO-Digitaal), van het architectuurgremia:

*Beeld: Informatiemodel visual — Klus 53 allignment MORA-HORA. Voeg hier het beeld in.*

> De tabel is daarmee niet bedoeld als extra abstractielaag naast de scenario's, maar juist als hun vaste referentiepunt.

> Voetnoot. OKx richt zich in dit profiel primair tot de diepte van het beschrijven van de werkproceslaag.

*Schrijf hier de uitwerking.*

##### Het plan en rooster proces

> Leerroute 1 schrijft hier: `TO-DO`

> Plannen en roosteren brengen het onderwijsontwerp en de werkelijkheid van de instelling samen.

> In de instellingsjourney wordt `onderwijsspecificatie` eerst planbaar gemaakt en daarna als `onderwijsaanbod` aanmeldbaar en inschrijfbaar.

*Schrijf hier de uitwerking.*

##### Plannen is cyclisch

> Leerroute 1 schrijft hier: Voor de student er is (instellingsjourney-fasen 1–2): de planner start op een grofmazige planbare `onderwijsspecificatie` en maakt een grove tactisch jaarplanning met perioden, capaciteit en instroom.

> Bij start onderwijsuitvoering (fasen 4–5): planbaar aanbod wordt geroosterd aanbod;

> Tijdens het jaar (fasen 6–7): keuzemomenten, incidenteel versnellen of temporiseren, hybride trajecten, overstap naar een set certificaten en 720 SBU keuzedeelruimte (niveau 4) vullen de planner met afwijkingen.

> Jochem. Hij versnelt op theorie en temporiseert op BPV. Zijn keuzedeel vult de helft van zijn 720 SBU keuzedeelruimte en moet alsnog passen in een lopend rooster van ruim 2.000 studenten — typisch voor de complexiteit van fase 6 en 7.

> Voordat de planner begint, moet de keten planbaarheidsgegevens leveren (zie paragraaf Planbare onderwijsspecificaties en §3.3.1.2.5).

*Schrijf hier de uitwerking.*

##### Voor wie dieper wil: CSP, NP-Hard en controle

> Leerroute 1 schrijft hier: Onderwijsplannen is in essentie een invulling van alle open vragen waarbij alle regels tegelijk kloppen.

> Voordat de planner begint, leveren specificatie, inschrijvingen, groepen, capaciteit en beleid die regels (zie ook de informatietabel Persoon, groep en constraint).

*Schrijf hier de uitwerking.*

##### Voorbeeld van groeperingen en plannen en roosteren

> Leerroute 1 schrijft hier: Jochem. Zijn persoonlijke programma = het nominale apothekersassistent-programma plus het gekozen keuzedeel Ondernemerschap in de zorg.

> Hieruit volgt story-0008: de planner herkent de groep aan het gekozen keuzedeel en de periode.

> Verschil tussen nominaal en persoonlijk programma in deze leerroute.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

#### Planbare onderwijsspecificaties

> Leerroute 1 schrijft hier: Wanneer wordt een `onderwijsspecificatie` planbaar? Een `onderwijsspecificatie` begint grofmazig:

> Minimaal benodigde gegevens (conceptueel). Onderstaande velden maken de overgang van grofmazig naar planbaar expliciet.

| Gegevensdimensie | Wat de planner nodig heeft | Voorbeeld (generiek) |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

> Grofmazig vs gedetailleerd planbaar is een rijpheidscontinuüm, geen twee strakke stadia.

> Voorbeeld — Jochem, leeronderdeel Medicatiebewaking (`B1-K1-W2`).

| Gegevensdimensie | Invulling voor <student>s cohort |
| --- | --- |
| | |
| | |
| | |
| | |
| | |

> Van planbare specificatie naar `onderwijsaanbod`. Zodra de specificatie planbaar is, instantieert de planner `onderwijsaanbod`.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

##### Persoon, groep en constraint — informatie-overzicht

> Leerroute 1 schrijft hier: Het cyclische plandiagram en de instellingsjourney groeperen keteninvoer in vier bronnen.

| **Bron (keten)** | **Primair inzicht** | **`Persoon` (student / medewerker)** | **Groep / cluster / populatie** | **Constraintdimensie (voorbeelden)** |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

> Denkraam: persoon, rollen en skills. Naast de onderwijsdata die elders in dit document wordt gemodelleerd, is voor planning en roostering een complementair denkpatroon nodig dat direct met mensen en wat zij kunnen en willen werkt.

> Skill-vraag en skill-aanbod. Groepen zijn in dit denkpatroon clusters van personen die qua skill-vector op elkaar lijken of dezelfde aan te bieden onderwijs- of begeleidingsbehoefte delen.

> Reële wereld en strategie. Daarbovenop liggen constraints die niet “in het hoofd” van één persoon zitten maar de realiteit van de instelling vormen:

> Planning en roostering. Binnen die totale constraintset voeren planning en roostering het zoeken naar haalbare toewijzingen uit (zie Voor wie dieper wil:

| **Hoofdtype `Persoon`** | **Rol of functietitel (voorbeelden; koppelbaar aan HR)** | **Skills-profiel** (vaardigheden, kennis, inzichten; bevoegdheden waar van toepassing) | **Als constraint geformuleerd** (skill-vraag / skill-aanbod; typisch plan vs rooster) |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| **Reële-wereldvlak** | **Voorbeelden van constraints** | **Meest zichtbaar in** |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

> Leeswijzer. De eerste tabel koppelt diagramblokken aan informatie-inzicht over personen, groepen en constraints.

*Schrijf hier de uitwerking.*

##### Conceptueel gegevensoverzicht

> Leerroute 1 schrijft hier: Onderstaande tabel vult het vlakkenmodel hierboven aan met doel, conceptuele inhoud en voorbeeldattributen per gegevensgroep.

| **Gegevensgroep / informatie-object** | **Vlak** | **Doel en conceptuele inhoud** | **Voorbeeld attributen** (niet exhaustief) | **Conceptdefinitie** |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

> Disclaimer.* In deze fase blijven we bewust op conceptueel niveau.

*Schrijf hier de uitwerking.*

##### Betrokken systemen bij gegevensuitwisseling

> Leerroute 1 schrijft hier: Jochem op de plaat (leeswijzer). De onderstaande informatiestromenplaat is geen Jochem-specifiek diagram:

*Beeld: OKx informatiestromen Leerroute <nummer> - Regulier. Voeg hier het beeld in.*

*Schrijf hier de uitwerking.*

##### Applicatiecomponenten op de plaat — doelen, gegevens en interacties

> Leerroute 1 schrijft hier: Doel. Dit blok start de gegevensanalyse en de interactieanalyse voor Leerroute 1 — regulier, geen inhoudelijke keuze op kaderniveau.

> Leeswijzer op de plaat. De plaat (`OKx_LR1_informatiestromen_v20260526.jpg`) kent twee delen:

> Labels op de pijlen volgen het vlakkenmodel (zie anker-tabel Betrokken informatie bij proces):

> Student Keuze Systeem (SKS) staat op deze plaat als duidelijk gescopeerde applicatiecomponent:

*Schrijf hier de uitwerking.*

##### Componenten en hun doel — wat hoort hier wel en niet thuis

| Component (zoals op plaat) | Hoofddoel in dit scenario | Wat dit systeem **niet** doet (rolafbakening) | Welke informatie hier ontstaat of leeft (conceptueel) |
| --- | --- | --- | --- |
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

> Leerroute 1 schrijft hier: Jochem — één feit, één bron. Zijn opleidingsspecificatie ontstaat in de curriculumtool en wordt via OC gelezen door planning, LMS en SVS — niet opnieuw vastgelegd in het LMS.

*Schrijf hier de uitwerking.*

##### Bron-, lees- en bewerkrollen t.o.v. informatie-objecten

> Leerroute 1 schrijft hier: De vorige tabel beschrijft doelen en rolafbakening. Hieronder staat dezelfde set systemen in termen van het vlakkenmodel uit §3.2:

| Systeem | Bron van waarheid voor (informatie-objecten) | Leest (consumeert) | Bewerkt / schrijft |
| --- | --- | --- | --- |
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

> Implementatienuance.* De exacte splitsing tussen KRS en SVS voor grensgevallen (bijv.

*Schrijf hier de uitwerking.*

##### Anti-patronen tussen systemen — tegengestelde doelen om te voorkomen

> Leerroute 1 schrijft hier: Doel hier is dat de semantische consistentie uit §3.2 ook bij implementatie behouden blijft:

> OC vs LMS — OC is de enige bron van de onderwijsspecificatie;

*Schrijf hier de uitwerking.*

##### Procesfasen ↔ interacties op de plaat ↔ informatie

> Leerroute 1 schrijft hier: Hier komt alles samen. Per fase van de instellingsjourney (zie De procesbeleving achter 'regulier' onderwijs van een Instelling, fasen 1–8) lopen we de informatiestromenplaat voor leerroute 1 verhalend door.

> Jochem (student) — happy flow. Hoe ervaart hij deze fase als reguliere mbo-student? De instelling — journey fase N.

> Bij fase 5, 6 en 7 is dit verhaal niet af zonder de variaties incidenteel temporiseren, incidenteel versnellen en hybride:

> Leesregel op de plaat. De linkerhelft is Onderwijsontwikkeling (fasen 1–2:

*Schrijf hier de uitwerking.*

###### Fase 1 — Kwalificatiekader analyseren en grofmazig ontwerpen

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 1. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: De instelling — journey fase 1. Een onderwijsontwerper vertaalt het `kwalificatiedossier` (CREBO, kerntaken, werkprocessen, keuzedeelruimte) naar een `opleidingsspecificatie` met onderliggende `opleidingsprogramma-` en `onderwijseenheid-specificaties`, eerste toetsvormen en een initieel examenplan.

> Jochem — happy flow. Voor Jochem nog onzichtbaar; deze fase voltooit zich vóórdat hij zich oriënteert.

> Wat licht op in de plaat. Curriculum-ontwerptool → OC met `opleidingsspecificatie`, `opleidingsprogramma-specificatie`, `onderwijseenheid-specificatie`, `toetsonderdeel-specificatie` en initieel `examenonderdeel-specificatie` — alles op grofmazig niveau.

*Schrijf hier de uitwerking.*

###### Fase 2 — Publiceren en planbaar maken

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 2. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: De instelling — journey fase 2. De grofmazige specificaties zijn aangevuld tot planbare specificatie (tijdvensters, capaciteit, expertise, faciliteit).

> Hieruit volgen story-0007 (de verwerkingsstatus met referentie terugmelden) en story-0009 (de haalbaarheidstoets op het concept vóór publicatie).

> Jochem — happy flow. Nog steeds onzichtbaar, maar deze fase bepaalt of zijn opleiding in september start en met welke capaciteit.

> Wat licht op in de plaat. OC → Planningssysteem (`opleidingsspecificatie` als planopgave);

*Schrijf hier de uitwerking.*

###### Fase 3 — Instroom, intake en plaatsing

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 3. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: Jochem — happy flow. Jochem ziet het gepubliceerde aanbod (vanuit OC) en herkent Apothekersassistent — regulier met start in september.

> De instelling — journey fase 3. Vanaf nu bestaat Jochem als formele student in de keten met een inschrijving op opleiding, programma en (waar van toepassing) initiële `plaatsingsgroep`.

> Wat licht op in de plaat.: OC → Intakesysteem (aanbod om op te oriënteren);

*Schrijf hier de uitwerking.*

###### Fase 4 — Detailleren, roosteren en inschrijven

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 4. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: De instelling — journey fase 4. Onderwijsontwikkelaars werken `leeronderdeel-` en `toetsonderdeel-specificaties` (en waar nodig `lesspecificatie`) fijnmazig uit;

> Jochem — happy flow. Jochem ontvangt zijn eerste rooster en krijgt toegang tot het LMS voor periode 1.

> Hieruit volgen story-0004 (geroosterd aanbod per periode publiceren) en story-0005 (vóór de start toegang tot leeromgeving en rooster).

> Wat licht op in de plaat. OC → LMS (`leeronderdeel-specificaties` ter detaillering);

*Schrijf hier de uitwerking.*

###### Fase 5 — Onderwijs uitvoeren en voortgang begeleiden

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 5. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: Jochem — happy flow. Jochem volgt zijn lessen, BPV in de apotheek en formatieve toetsen (student-journey-stappen 5–7).

> De instelling — journey fase 5. Docenten verzorgen onderwijs, plannen toetsmomenten tijdens lessen en houden formatieve voortgang bij.

> Hieruit volgt story-0021: de docent legt tijdens de uitvoering voortgang en resultaat per les vast.

> Jochem — variaties.

> Incidenteel temporiseren: Jochem mist BPV-weken door ziekte;

> In alle drie blijft de leerroute regulier; deze signalen uit fase 5 voeden direct fase 7 (bijsturen).

> Wat licht op in de plaat. OC → LMS en OC → SVS (specificatie als referentiekader);

*Schrijf hier de uitwerking.*

###### Fase 6 — Organiseren van keuzemomenten

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 6. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: Jochem — happy flow. De keuzedeelruimte nadert; Jochem stelt zijn geprioriteerde voorkeurslijst samen in het SKS (zie Wanneer kiest een student keuzedelen?).

> Hieruit volgt story-0014: een keuzedeel is alleen kiesbaar wanneer locatie en periode passen.

> De instelling — journey fase 6. De planner verwerkt definitieve keuzes periodiek naar groepen en capaciteit, actualiseert het planbare aanbod in OC en het rooster volgt.

> Jochem — variaties. Past zijn eerste voorkeur niet, dan oriënteert hij op een andere locatie (gate 9a) of een ander keuzedeel;

> Wat licht op in de plaat. OC → SKS (`opleidingsprogramma-aanbod` type keuzedeel + `opleidingsprogramma-specificatie`);

*Schrijf hier de uitwerking.*

###### Fase 7 — Bijsturen planning en aanbod

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 7. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: De instelling — journey fase 7 (IST situatie is grotendeels handmatig).

> Jochem — variaties.

> Temporiseren: zijn gemiste praktijkles-weken voor medicatieherkenning worden door de planner samengevoegd met andere achterlopers tot een nieuwe `planningsgroeping` i.r.t.

> Wat licht op in de plaat. SVS als bron van individuele voortgang (`onderwijsverbintenis resultaten`);

*Schrijf hier de uitwerking.*

###### Fase 8 — Examineren, vaststellen en diplomeren

*Beeld: OKx informatiestromen Leerroute <nummer> — highlight Procesfase 8. Voeg hier het beeld in.*

> Leerroute 1 schrijft hier: De instelling — journey fase 8. Op basis van het examenplan uit fase 1 worden `examenspecificaties` getransformeerd tot `examengelegenheden`.

> Jochem — happy flow. Jochem legt examens af, ontvangt zijn formele beoordeling en uiteindelijk zijn diploma — het eindpunt van dezelfde keten die hij als reguliere route ervoer.

> Wat licht op in de plaat. Toets-/examenplanning ↔ Toets-/examenafname;

> Aansluiting op de informatiestromenplaat. De Informatiestromenplaat hierboven toont dezelfde stromen in begrippen uit het begrippenkader en informatiemodel;

*Schrijf hier de uitwerking.*

##### Concept informatiemodel — geneste onderwijsspecificatie (<student>, Apothekersassistent)

> Leerroute 1 schrijft hier: Om de begrippen uit het begrippenkader en de ankertabel tastbaar te maken, werken we hieronder de onderwijsspecificatie voor Jochems opleiding Apothekersassistent (Crebo-dossier 23450, kwalificatie 27141) volledig genest uit — als ASCII-boom.

> Fase 1–2 — grofmazig onderwijsontwerp: publiceerbaar en planbaar.

*Voorbeeld: de bron toont hier een fragment. Voeg hier het eigen fragment in.*

> Keuzedelen als zelfstandig programma. Keuzedelen worden hier niet als onderwijseenheid binnen een diplomaprogramma gemodelleerd, maar als een eigen `opleidingsprogramma-specificatie` met daaronder de losse keuzedelen als `onderwijseenheid-specificaties`.

> Aggregatie-invariant. De studielast telt bottom-up op: `SOM(leeronderdelen) = onderwijseenheid` en `SOM(onderwijseenheden) = programma` (archief, §5.3).

> Fase 4 — detaillering: lessenreeksen en lessen. De onderwijsontwikkelaar werkt de grofmazige leeronderdelen fijnmazig uit tot lessenreeksen en lessen, met lesplannen, werkinstructies (leertaken), leermaterialen en lesdoelen (lesuitkomsten).

*Voorbeeld: de bron toont hier een fragment. Voeg hier het eigen fragment in.*

> Van detail naar uitvoering. Deze detailspecificaties voeden OC → LMS ter inrichting (fase 4;

> <!-- Probleemstelling van IST situatie: In de IST-situatie werkt een instelling weliswaar onder een gezamenlijk bestuurlijk en organisatorisch dak, maar beschrijven domeinen en onderliggende onderwijsteams hun onderwijsspecificaties nog ieder op hun eigen manier.

> Het gevolg is dat onderwijsspecificaties van team A niet vanzelf begrijpelijk of herbruikbaar zijn voor team B, ook al werken beide teams binnen dezelfde instelling.

> Onderstaand organogram maakt zichtbaar dat dit probleem niet alleen tussen domeinen speelt, maar ook raakt aan de afstemming tussen onderwijsteams en de ondersteunende teams voor logistiek en begeleiding.

> <!-- Actor(en) — wie maakt regulier studeren mogelijk? Student:

> Wat moet er minimaal beschreven en uitwisselbaar zijn om dit mogelijk te maken? Onderwijskundige beschrijving:

> Scenario-set (aanbod-gestuurd, primair) 1. Onderwijsontwerp en publicatie (onderwijsspecificaties beschikbaar maken).

*Schrijf hier de uitwerking.*

#### 3.3.2 Leerroute 2 — Temporiseren (en personaliseren) by design

> Leerroute 1 schrijft hier: Anker-persona: Larissa — topsporter (kans op Olympische Spelen 2028) die de mbo-4-opleiding Software Developer (BOL) wil halen, maar met structureel beperkte en deels onvoorspelbare beschikbaarheid:

> Kern. De student volgt dezelfde kwalificatie en in essentie dezelfde `onderwijsspecificatie` als in leerroute 1, maar het persoonlijke programma wijkt structureel af van het nominale programma:

> Hieruit volgt story-0012: dezelfde opleiding by design in een lager tempo volgen.

> Leeswijzer. Deze paragraaf is opgebouwd zoals leerroute 1: eerst de delta t.o.v.

*Schrijf hier de uitwerking.*

##### 3.3.2.1 Delta t.o.v. leerroute <nummer> (<naam van de route>)

> Leerroute 1 schrijft hier: De winst van leerroute 1 als baseline is dat we alleen het verschil hoeven te beschrijven.

| Dimensie | Leerroute <nummer> — regulier (<student>) | Leerroute 2 — temporiseren/personaliseren by design (<student>) |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

> Voor wie dieper wil — sturingsmodel. Leerroute 2 verlaat het aanbod-gestuurde model niet volledig.

*Schrijf hier de uitwerking.*

##### 3.3.2.2 De studentbeleving — <student> (student journey)

> Leerroute 1 schrijft hier: Voor de volledige verhaallijn: zie persona Larissa. Hieronder de stappen die de leerroute-2-delta dragen;

> Oriënteren & aanmelden. Larissa kiest bewust niet het op topsport afgestemde Sport & Bewegen, maar ICT/Software Developer.

*Schrijf hier de uitwerking.*

##### 3.3.2.3 De instellingsbeleving — wat de instelling extra moet organiseren

> Leerroute 1 schrijft hier: Voor de instelling is leerroute 2 dezelfde instellingsjourney (fasen 1–8) als bij leerroute 1, maar met zwaartepunt in fase 5–7 (uitvoeren, keuzemomenten, bijsturen).

> Deelname-flexibiliteit per `lesgelegenheid` (in-/uitschrijven, alternatieve slots) in plaats van alleen een vaste groepsplaatsing.

> Dat dit organisatorisch kan, hangt sterk af van hoe de instelling geografisch en organisatorisch is ingericht.

> Sterk aanbod-gestuurd onderwijsaanbodmodel met hybride kenmerken:

*Schrijf hier de uitwerking.*

##### 3.3.2.4 Organisatorische en geografische complexiteit van instellingen

> Leerroute 1 schrijft hier: In leerroute 1 spraken we impliciet over de onderwijsinstelling als één organisatie op één locatie (zie het organogram).

> Het reductie-principe. De complexiteit blijft beheersbaar door alle varianten terug te brengen tot twee scoping-vragen op elk informatie-object:

> 1. Wie is eigenaar/aanbieder? — de organisatie (rechtspersoon/BRIN) die het object bezit, publiceert of erkent.

> Zolang elk object deze twee dimensies expliciet draagt (zie de attributen in §3.3.2.6), kan dezelfde keten — met de Onderwijscatalogus (OC) als distributiepunt — alle organisatievormen bedienen.

> Vier organisatievormen. Onderstaande tabel beschrijft per vorm wat er verandert;

| Organisatievorm | Kenmerk | Grens van OC / publicatie | Grens van planning & rooster | Grens van verbintenis & erkenning | Koppelvlak-implicatie |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

> Larissa op de organisatiekaart. Haar Engels-bij-Technicus Engineering is in vorm A/B een interne cross-opleiding plaatsing (zelfde rechtspersoon, mogelijk andere locatie → `locationRef`).

> Hoe blijft de koppeling werken over alle dimensies? Vier ontwerpregels, alle terug te voeren op bestaande secties:

> 1. Eén distributiepunt per scope. De OC blijft de plek waar specificatie en (planbaar/geroosterd) aanbod worden gepubliceerd en consistent gehouden (archief, §4.1).

*Schrijf hier de uitwerking.*

##### 3.3.2.5 Het plan- en rooster proces onder locatie- en organisatiecomplexiteit

> Leerroute 1 schrijft hier: Dit is de aangekondigde uitbreiding van Het plan en rooster proces.

> Wat verandert er in de constraint-set? In leerroute 1 leverde de keten al `Persoon`, `groep` en `constraint` aan de planner (zie de informatietabel Persoon, groep en constraint en §3.3.1.2.5).

| Constraint-categorie | In leerroute <nummer> (impliciet) | In leerroute 2 (expliciet) |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |

> Twee planlagen, expliciet gescheiden. Onder organisatiecomplexiteit valt het plan uiteen in:

> Instellingsbreed (tactisch) jaarplan — over alle opleidingen en locaties van één organisatie.

> Bij samenwerkende instellingen (vorm C/D) is er geen gedeelde rooster-master.

> Voor wie dieper wil — CSP met locatie/organisatie. In de CSP-termen uit Voor wie dieper wil:

*Schrijf hier de uitwerking.*

##### 3.3.2.6 Per processtap: data-objecten en attributen richting koppelvlak

> Leerroute 1 schrijft hier: Doel van deze sectie is de aankondiging uit de inleiding waarmaken:

> Notatie en grenzen. We hanteren de notatie van §12.5 (gegevensgroep → attributen → verwijzing) en blijven conceptueel:

> Stap 0 — Organisatie- en locatiecontext (geldt op álle objecten).

| Gegevensgroep | Attributen (minimaal) | Toelichting |
| --- | --- | --- |
| | | |
| | | |
| | | |

> Stap 1 — Specificatie (fase 1): standaardiseren op leeruitkomsten.

> 1. Uitwisselingsprobleem — structuur en betekenis sluiten niet op elkaar aan;

> De oplossing voor beide is dezelfde lingua franca: gestandaardiseerde leeruitkomsten (bij voorkeur in een sectoroverstijgende skillstaxonomie als CompetentNL, zie hoofdstuk 4 en §5.4).

> Onderstaand het begrippenkader uit Betrokken informatie bij proces, hier uitgebreid met een expliciete kolom 2.

| **1. Kwalificatiekader** | **2. Leeruitkomsten** | **3. Onderwijsspecificatie** | **4. Onderwijsaanbod** | **5. Onderwijsverbintenis** | **6. Onderwijsresultaat** |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

> De `Leeruitkomst` (summatief, op werkproces-niveau) en `Lesuitkomst` (formatief, op les-niveau) zijn het canonieke vertrekpunt;

> Probleem 1 — uitwisseling. Wanneer elk team zijn eigen uitwerking hanteert, loopt zelfs de interne uitwisseling al vast:

*Diagram: de bron tekent hier een sequenceDiagram. Voeg hier het diagram in.*

> Probleem 2 — vindbaarheid. Hetzelfde gebrek aan gedeelde betekenis maakt aanbod ook onvindbaar op inhoud.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

> De vereiste standaard schaalt mee met het scenario. Hoe groter de organisatorische en geografische reikwijdte (§3.3.2.4), hoe hoger het noodzakelijke standaardisatieniveau van leeruitkomsten.

| Scenario (§3.3.2.4) | Benodigd standaardisatieniveau leeruitkomsten | Zonder die standaard |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

> Kortom: leeruitkomsten zijn zowel de uitwisselsleutel (probleem 1) als de zoeksleutel (probleem 2) van de keten.

> Stap 2 — Planbaar aanbod (fase 2). Hier ontstaat het eerste object dat §12.5 nog niet op attribuutniveau gaf.

| Gegevensgroep | Attributen (minimaal) | Toelichting |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |

> Stap 3 — Geroosterd aanbod: `leergelegenheid` / `lesgelegenheid` (fase 4).

| Gegevensgroep | Attributen (minimaal) | Toelichting |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |

> Stap 4 — Verbintenis: aanmelding → inschrijving (fasen 3, 6).

| Gegevensgroep | Attributen (minimaal) | Toelichting |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |

> Stap 5 — Resultaat: `onderwijsverbintenis-resultaat` (fasen 5, 8).

| Gegevensgroep | Attributen (minimaal) | Toelichting |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

> Traceerbaarheid. Deze vijf stappen vormen samen de attribuutketen `specificatie → planbaar aanbod → geroosterd aanbod → verbintenis → resultaat`, telkens met de organisatie/locatie-scoping uit stap 0.

*Schrijf hier de uitwerking.*

##### 3.3.2.7 Randvoorwaarden — negen concern-dimensies

> Leerroute 1 schrijft hier: Per dimensie kort wat besloten, geregeld of beschikbaar moet zijn voordat leerroute 2 (met locatie-/organisatiecomplexiteit) uitvoerbaar is.

| Dimensie | Randvoorwaarde voor leerroute 2 |
| --- | --- |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

*Schrijf hier de uitwerking.*

##### 3.3.2.8 Informatiestromen en AMIGO-voorloper

> Leerroute 1 schrijft hier: Beeld/verwijzing. Het procesbeeld staat in de ArchiMate-view Onderwijsvisie vertalen naar onderwijsaanbod;

> Gegevensanalyse (kader). Producerend → consumerend, met de minimale referenties uit §3.3.2.6:

> Interactieanalyse (kader). Nieuw t.o.v. de route-1-baseline zijn:

> Doorverwijzing AMIGO. Deze gegevens- en interactieanalyse voedt in een volgende iteratie technologiekeuze → berichtspecificatie → interfacespecificatie → afsprakenset.

*Schrijf hier de uitwerking.*

##### 3.3.2.9 Concept informatiemodel — geneste onderwijsspecificatie (delta t.o.v. LR1)

> Leerroute 1 schrijft hier: Larissa volgt Software Developer (BOL, mbo-4, indicatief) en temporiseert by design.

> Fase 1–2 — delta in het grofmazige ontwerp. De temporiseer-variant komt als track naast het reguliere programma;

*Voorbeeld: de bron toont hier een fragment. Voeg hier het eigen fragment in.*

> Fase 4 — delta in de detaillering. De specificatie van lessenreeks en les verandert niet;

*Voorbeeld: de bron toont hier een fragment. Voeg hier het eigen fragment in.*

> Kernpunt (skill-conform). De structuur en semantiek van de onderwijsspecificatie veranderen niet t.o.v.

*Schrijf hier de uitwerking.*

#### 3.3.3 Leerroute 3 — Versnellen (standaard route) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student rondt sneller af door vrijstellingen/EVC, hogere intensiteit of het overslaan van onderdelen.

> Hieruit volgt story-0024: vrijstellingen aanvragen op eerder behaalde resultaten of aangetoonde competenties.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

#### 3.3.4 Leerroute 4 — Binnen de instelling (personaliseren diplomaroute) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student personaliseert binnen één instelling (combineren/overlap tussen opleidingen of trajecten).

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Diagram: de bron tekent hier een sequenceDiagram. Voeg hier het diagram in.*

> SOLL situatie: Delta: leeruitkomsten sectoroversteigend gestandaardiseerd.

> `TO-DO: Rapport van Hans Kok op ontsluiten onderwijs aanbod rapportage benoemen en meenemen en principes mappen op ons document en voorgestelde aanpak`.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

##### Persoon, rollen en skills als denkraam voor constraints

> Leerroute 1 schrijft hier: Naast de onderwijsdata die elders in dit document wordt gemodelleerd, is voor planning en roostering (§ Het plan en rooster proces) een complementair denkpatroon nodig dat direct met mensen en wat zij kunnen en willen werkt.

> Skill-vraag en skill-aanbod. Groepen zijn in dit denkpatroon clusters van personen die qua skill-vector op elkaar lijken of dezelfde aan te bieden onderwijs- of begeleidingsbehoefte delen.

> Reële wereld en strategie. Daarbovenop liggen constraints die niet “in het hoofd” van één persoon zitten maar de realiteit van de instelling vormen:

> Planning en roostering. Binnen die totale constraintset voeren planning en roostering het zoeken naar haalbare toewijzingen uit (zie Voor wie dieper wil:

| **Hoofdtype `Persoon`** | **Rol of functietitel (voorbeelden; koppelbaar aan HR)** | **Skills-profiel** (vaardigheden, kennis, inzichten; bevoegdheden waar van toepassing) | **Als constraint geformuleerd** (skill-vraag / skill-aanbod; typisch plan vs rooster) |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| **Reële-wereldvlak** | **Voorbeelden van constraints** | **Meest zichtbaar in** |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

> Leeswijzer. Dit blok vervangt geen gegevensmodel uit §3.3.1.2.5:

*Schrijf hier de uitwerking.*

#### 3.3.5 Leerroute 5 — Buiten de instelling, binnen de sector (personaliseren diplomaroute) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student volgt onderdelen bij een andere instelling binnen dezelfde sector.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

#### 3.3.6 Leerroute 6 — Buiten de instelling, over sectoren heen (personaliseren diplomaroute) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student volgt onderdelen over sectoren heen (mbo/hbo/wo).

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

#### 3.3.7 Leerroute 7 — Vrije keuze (modulair studeren) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student kiest losse onderdelen voor ontwikkeling/bijscholing;

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

#### 3.3.8 Leerroute 8 — Bundelen (modulair studeren) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student bundelt losse onderdelen tot een samenhangend pakket rond een thema/rol.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

#### 3.3.9 Leerroute 9 — Stapelen (modulair studeren) (TO-DO)

> Leerroute 1 schrijft hier: Kern: de student stapelt onderdelen richting een formeel eindresultaat (bijv.

*Diagram: de bron tekent hier een flowchart. Voeg hier het diagram in.*

*Schrijf hier de uitwerking.*

### 3.4 Scenario-uitwerkingen

> Leerroute 1 schrijft hier: De concrete gebruikersscenario's staan per scenario in een eigen document in de map scenario-uitwerkingen;

*Schrijf hier de uitwerking.*

## Begrippenkader en archief

> Leerroute 1 schrijft hier: Het begrippenkader met de zes niveaus, de stadia en de ankertabel staat in begrippenkader.md.

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
