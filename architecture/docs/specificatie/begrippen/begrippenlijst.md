# Begrippenlijst OKx

## Context

De koppelvlakken van OKx wisselen informatie uit tussen instellingen en tussen systemen. Dat werkt alleen als een term aan beide kanten hetzelfde betekent.

## Inleiding

Deze lijst geeft per begrip de schrijfwijze, een definitie en de vindplaats van die definitie, en legt elk begrip naast de referentiearchitecturen: de mbo-referentiearchitectuur (MORA), het Kernmodel Onderwijsinformatie (KOI) binnen de Referentiearchitectuur Onderwijs (ROSA), en de referentiearchitectuur van het hoger onderwijs (HORA). Een begrip zonder vindplaats staat er als open post in.

## Doel

Vaststellen wat OKx onder een term verstaat, zodat een lezer van een specificatie niet hoeft te raden. De lijst is de toetssteen voor naamgeving in het informatiemodel, de koppelvlakspecificaties en de reviews.

## Scope

De objecttypen en begrippen van het informatiemodel OKx, elk eerst gelegd naast MORA en het Kernmodel Onderwijsinformatie binnen ROSA. HORA is nog niet onderzocht. Termen uit de rest van de documentatie vallen buiten deze versie.

Gezocht in de volledige lijst van het MORA-informatiemodel (81 informatieobjecten, https://mora.mbodigitaal.nl/index.php/Informatiemodel) en in het volledige overzicht van het Kernmodel Onderwijsinformatie (https://rosa.wikixl.nl/index.php/Kernmodel_Onderwijsinformatie), opgehaald op 9 september 2026 en opnieuw op 14 september 2026. Een begrip dat in beide lijsten ontbreekt staat als 'geen tegenhanger gevonden'.

## Dekking

Versie v0.2, concept. De kaders zijn geraadpleegd op 2026-09-14.

| | |
|---|---|
| Begrippen en objecttypen | 69 |
| Met een definitie uit een referentiekader | 18 |
| Met een definitie uit een OKx-document | 18 |
| Zonder definitie | 33 |

## Begrippenfamilies

De begrippenfamilies delen de keten in; het zijn de kolommen op de plaat van het [informatiemodel](../../../model/informatiemodel/informatiemodel.md#begrippenfamilies). De objecttypen eronder zijn het conceptuele informatiemodel.

| Begrip | Definitie | Herkomst | Bron |
|---|---|---|---|
| `Kwalificatiekader mbo` | Het geheel van landelijk vastgestelde eisen waaraan een opleiding moet voldoen. Vastgesteld en beheerd buiten OKx | nieuw voor OKx | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippenfamilies) |
| `Onderwijskundig kader instelling` | De invulling door de instelling van de beoogde leeruitkomsten uit het kwalificatiekader | nieuw voor OKx | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippenfamilies) |
| `Onderwijsspecificatie` | Het herbruikbare ontwerp van een onderwijsonderdeel, los van wanneer het draait en wie eraan meedoet | verbijzondering van `onderwijsaanbod (koi)` (ROSA-KOI) | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippenfamilies) |
| `Onderwijsaanbod` | Een specificatie die is ingepland: een periode, een capaciteit en waar van toepassing concrete plek, docent en tijd | verbijzondering van `onderwijsaanbod (koi)` (ROSA-KOI) | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippenfamilies) |
| `Onderwijsverbintenis` | Een afspraak voor het gaan volgen, volgen en hebben gevolgd van onderwijs. | overgenomen uit ROSA-KOI | [onderwijsdeelname (koi)](https://rosa.wikixl.nl/index.php/Id-ec977035c9be4b01bb1c14a5950a1799) |
| `Onderwijsresultaat` | Vastgelegde en geformaliseerde beoordeling op basis van een of meer leerresultaten. | overgenomen uit ROSA-KOI | [onderwijsresultaat (koi)](https://rosa.wikixl.nl/index.php/Id-e5d21e5384c0482ba4a501571e69927a) |
| `Resultaatstructuur` | De samenstelling en weging waarmee losse resultaten optellen tot een uitspraak over de beoogde leeruitkomsten, en daarmee over een kwalificatie of certificaat | nieuw voor OKx | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippenfamilies) |

## Objecttypen met een definitie

Bij een verbijzondering gaat OKx verder dan het kader; de reden staat in de laatste kolom. Een noot geeft aan waar een citaat een oudere naam of schrijfwijze gebruikt.

| Objecttype | Begrip | Definitie | Herkomst | Bron | Reden of noot |
|---|---|---|---|---|---|
| `Examenplan` | Buiten de kolommen | Het examenplan geeft per kwalificatie een overzicht van de examenonderdelen en examens die een mbo-school inzet voor de examinering (kwalificerende beoordeling). Het examenplan geeft inzicht in de onderdelen die een student met een voldoende moet afsluiten om in aanmerking te komen voor een diploma. In het examenplan staat binnen welke omgeving (mbo-school of beroepspraktijk) de examens plaatsvinden. Hierbij houdt de school rekening met de praktische haalbaarheid van de examinering binnen de praktijksituatie en de afspraken in het sectoraal examenprofiel. In een examenplan staan de examenonderdelen en examens voor de beroepsgerichte eisen en de generieke taal- en rekeneisen. Ook de wijze waarop een school deze onderdelen examineert, staat in het examenplan. | overgenomen uit MORA | [Examenplan](https://mora.mbodigitaal.nl/index.php/Id-913bf380-1288-8a49-0bca-906d8b112e8f) |  |
| `Medewerker` | Buiten de kolommen | Een natuurlijk persoon die op grond van een overeenkomst werkzaam is voor een onderwijsorganisatie. | overgenomen uit ROSA-KOI | [onderwijsmedewerker (koi)](https://rosa.wikixl.nl/index.php/Id-5ea4d7d18cbc4f8eb3aea997a4d9b35d) |  |
| `Student` | Buiten de kolommen | Een persoon die aan onderwijsactiviteiten deelneemt of dat wil gaan doen. Dit omvat ingeschreven studenten, potentiële studenten en alumni | overgenomen uit MORA | [Student](https://mora.mbodigitaal.nl/index.php/Id-c7c163ee-2fa5-5b58-bc08-f401d0350c3a) |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | Buiten de kolommen | Het `Verzoek tot Aanbod / Intekening op specificatie` is een verzoek om aanbod te maken voor een specificatie. Het heeft specificaties als input en leidt tot aanbod; of intekenen op bestaand aanbod hetzelfde is, is nog niet vastgesteld. | verbijzondering van `Leervraag` (MORA) | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#ontwerpkeuzes) | MORA kent de leervraag als de vraag van de student wat hij wil leren. OKx verbijzondert die tot een uitwisselbaar verzoek dat leidt tot aanbod. De aanmelding (het verzoek om toegelaten te worden tot een opleiding) blijft, net als de inschrijving, bij het studentinformatiesysteem. |
| `Waarde document (diploma / certificaat)` | Buiten de kolommen | Het bewijsstuk van een eindoordeel over het voltooien van een opleiding, keuzedeel, deelkwalificatie of module door een onderwijsaanbieder. | overgenomen uit MORA | [Waarde document (diploma / certificaat)](https://mora.mbodigitaal.nl/index.php/Id-8647eba0-e31d-5bcf-c12a-4d477069943c) |  |
| `Kerntaak` | Kwalificatiekader mbo | Een kerntaak is een substantieel deel van de beroepsuitoefening naar belang omvang (tijdsbeslag of frequentie) of beide. Een kerntaak bestaat uit een geheel van inhoudelijk met elkaar samenhangende werkprocessen kenmerkend voor de beroepsuitoefening. Een kwalificatiedossier heeft een beperkt aantal kerntaken. Alle kerntaken samen beschrijven de essentie van de beroepsuitoefening van de betreffende beroepengroep. | overgenomen uit MORA | [Kerntaak](https://mora.mbodigitaal.nl/index.php/Id-99ef9489-49b3-4a3b-7a89-08ae36a3255e) |  |
| `Kwalificatie` | Kwalificatiekader mbo | De kwalificatie is de combinatie van het basis- en profieldeel uit het kwalificatiedossier. De kwalificatie omvat wat de beginnend beroepsbeoefenaar moet kennen en kunnen als hij gediplomeerd is en start op de arbeidsmarkt | overgenomen uit MORA | [Kwalificatie](https://mora.mbodigitaal.nl/index.php/Id-f54b73a9-9562-2b28-deca-724e992bbcdb) |  |
| `Kwalificatie dossier` | Kwalificatiekader mbo | Het kwalificatiedossier beschrijft de eisen waaraan een student moet voldoen om zijn diploma te behalen. Elk dossier bevat een of meer kwalificaties en iedere kwalificatie leidt tot een diploma. Alle kwalificatiedossiers samen, aangevuld met de keuzedelen, vormen de kwalificatiestructuur. Een kwalificatiedossier bestaat uit een basisdeel en een of meer profieldelen. Het basisdeel bevat de generieke onderdelen Nederlandse taal, rekenen, loopbaan en burgerschap en Engels (uitsluitend voor niveau 4). Verder bevat het gemeenschappelijke elementen, die gelden voor alle kwalificaties in het dossier: kerntaken, werkprocessen, vakkennis, vaardigheden en houdingsaspecten. Het profieldeel beschrijft de specifieke onderdelen. Keuzedelen zijn een plus op de kwalificatie en maken de opleiding compleet. | overgenomen uit MORA | [Kwalificatie dossier](https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762) |  |
| `Werkproces` | Kwalificatiekader mbo | Een werkproces is een afgebakend geheel van beroepshandelingen binnen een kerntaak. Het werkproces kent een begin en een eind heeft een resultaat en wordt als kenmerkend herkend in de beroepspraktijk. Een werkproces bestaat dus nooit uit één handeling of gedraging. Meerdere werkprocessen kunnen gelijktijdig lopen. Dat ze een begin en eind hebben wil niet per se zeggen dat ze na elkaar komen maar dat ze duidelijk te onderscheiden zijn van andere werkprocessen. | overgenomen uit MORA | [Werkproces](https://mora.mbodigitaal.nl/index.php/Id-9cf4d404-b06c-473f-57d9-3945af33cfa8) |  |
| `Examengelegenheid` | Onderwijsaanbod | Het georganiseerde aanbod van een examenmoment: planning, locatie, surveillant-capaciteit en kandidaten, gekoppeld aan precies één `Examenspecificatie`. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | Het citaat noemt `Examenspecificatie`; in het informatiemodel heet dat objecttype `Examenonderdeelspecificatie`. |
| `Opleidingaanbod` | Onderwijsaanbod | Een opleidingseenheid die door een onderwijsaanbieder aangeboden wordt in een bepaalde vorm, al dan niet op een bepaalde onderwijslocatie, waarop een onderwijsvolger zich kan inschrijven | overgenomen uit MORA | [Aangeboden opleiding](https://mora.mbodigitaal.nl/index.php/Id-e723f9e6-adfc-40a1-0527-ee1b75b380dc) |  |
| `Opleidingsaanbod van Instelling` | Onderwijsaanbod | Het geheel van opleiding dat door de instelling wordt aangeboden | overgenomen uit MORA | [Opleidingen overzicht](https://mora.mbodigitaal.nl/index.php/Id-9a23241c-a60e-6623-e13a-d945a761ab17) |  |
| `Toetsgelegenheid` | Onderwijsaanbod | Het georganiseerde aanbod van een toetsmoment: wanneer, waar en onder welke condities een toetsonderdeel wordt afgenomen, gekoppeld aan precies één `Toetsonderdeel-specificatie`. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | Het citaat schrijft `Toetsonderdeel-specificatie` met koppelteken, de oudere schrijfwijze van `Toetsonderdeel specificatie`. |
| `Leeruitkomst` | Onderwijskundig kader instelling | Een leeruitkomst is de invulling door de instelling van wat het kwalificatiekader beoogt: wat een student moet kennen en kunnen, zo geformuleerd dat specificaties ernaar kunnen verwijzen en dat behaalde toets- en examenresultaten er het bewijs voor leveren. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#ontwerpkeuzes) |  |
| `Formatief resultaat` | Onderwijsresultaat | Een waardering die de student informatie geeft over de kwaliteit en voortgang van zijn of haar leren, maar niet meetelt voor de uiteindelijke kwalificering. Formatieve resultaten worden vastgelegd conform de formatieve resultaatstructuur. Formatieve resultaten worden ook wel toetsresultaten genoemd | overgenomen uit MORA | [Formatief resultaat](https://mora.mbodigitaal.nl/index.php/Id-2bd2c72b-08d2-169d-9ed1-f4868ad34f5c) |  |
| `Formatieve beoordeling` | Onderwijsresultaat | Een beoordeling, veelal van een toets, die niet meetelt voor de uiteindelijke kwalificering, maar de lerende informatie geeft over de kwaliteit van zijn of haar leren | overgenomen uit MORA | [Formatieve beoordeling](https://mora.mbodigitaal.nl/index.php/Id-26fa321c-d407-817f-68c5-5509997d821b) |  |
| `Summatief resultaat` | Onderwijsresultaat | Een formele, door de instelling geregistreerde waardering voor summatief gemaakt werk (zoals een examen of BPV-beoordeling) die meetelt voor de uiteindelijke kwalificering. Summatieve resultaten worden vastgelegd conform de summatieve resultaatstructuur. Summatieve resultaten worden ook wel examenresultaten genoemd | overgenomen uit MORA | [Summatief resultaat](https://mora.mbodigitaal.nl/index.php/Id-beaf106a-f329-b3ed-e513-6814b1fd65fa) |  |
| `Summatieve beoordeling` | Onderwijsresultaat | De beoordeling van summatief gemaakt werk, zoals de beoordeling van een examen of een BPV-beoordeling | overgenomen uit MORA | [Summatieve beoordeling](https://mora.mbodigitaal.nl/index.php/Id-0a14e5af-bf2e-2584-3320-095341367128) |  |
| `Examenonderdeelspecificatie` | Onderwijsspecificatie | De specificatie van een summatief examen (opstelling, instrumenten, beoordelingskader) zoals vastgesteld door de examencommissie, gekoppeld aan te behalen leeruitkomsten of werkprocessen. | verbijzondering van `Examen` (MORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | MORA beschrijft het examen als onderzoek naar kennis, inzicht, houding en vaardigheden. OKx specificeert het examenonderdeel apart van de examengelegenheid waarop het wordt afgenomen. De bron schrijft `Examenspecificatie`; op de plaat heet het objecttype `Examenonderdeelspecificatie` (ontwerpkeuze 9: een examenonderdeel is een specialisatie van een toetsonderdeel). |
| `Keuzedeelruimte` | Onderwijsspecificatie | Een keuzedeelruimte is een oningevuld keuzedeel: onderwijskundig vrijgemaakte ruimte van een bepaalde omvang waarin een student een keuzedeel kiest. | nieuw voor OKx | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#ontwerpkeuzes) |  |
| `Leeronderdeel specificatie` | Onderwijsspecificatie | De specificatie van het deel van de onderwijseenheid (onder meer bestaande uit lesstof en opdrachten) waarin de student competenties kan verwerven. | afgeleid uit klus 53 (alignment MORA en HORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | MORA beschrijft de leertaak als lesstof en opdrachten. OKx maakt daar een herbruikbare specificatie van, binnen de onderwijseenheid. |
| `Les specificatie` | Onderwijsspecificatie | De specificatie van het kleinste geplande leermoment binnen een leeronderdeel: welke lesinhoud, leeractiviteit of toetsactiviteit in dat moment wordt aangeboden. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |  |
| `Onderwijseenheid specificatie` | Onderwijsspecificatie | De specificatie van de fundamentele eenheid waarin onderwijs wordt ontworpen en aangeboden, in de vorm van een samenhangend stelsel van één of meer (beoogde) leeruitkomsten, leeronderdelen en/of toetsonderdelen. (NB: Leeruitkomsten omvat o.a. kennis, inzicht en vaardigheden.) | afgeleid uit klus 53 (alignment MORA en HORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | KOI beschrijft de onderwijseenheid als samenhangend geheel met een leerdoel. OKx specificeert die eenheid met leeruitkomsten, leeronderdelen en toetsonderdelen, los van de inplanning. |
| `Opleidingsprogramma specificatie` | Onderwijsspecificatie | Een samenhangende verzameling van één of meer (deel)programma's, onderwijseenheden, of leeruitkomsten die kunnen leiden tot een kwalificatie. | afgeleid uit klus 53 (alignment MORA en HORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | De specificatiekant van het MORA-begrip onderwijs programma. MORA beschrijft het programma inclusief de planbaarheid; OKx scheidt de specificatie van het aanbod. |
| `Toetsonderdeel specificatie` | Onderwijsspecificatie | De specificatie van het deel van de onderwijseenheid (bestaand uit een onderzoek naar kennis, inzicht, houding en vaardigheden van de student), waarmee wordt vastgesteld over welke competenties de student beschikt, leidend tot een formatieve of summatieve beoordeling. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |  |
| `Examengelegenheid verbintenis` | Onderwijsverbintenis | De relatie tussen kandidaat en `Examengelegenheid`: inschrijving op en deelname aan de examenafname. | verbijzondering van `Examen deelname` (MORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) | MORA registreert de examensessie waarin een examen wordt afgenomen. OKx legt de relatie vast tussen de kandidaat en de examengelegenheid, met dezelfde informatiestructuur als de toetsgelegenheidverbintenis. |
| `Toetsgelegenheid verbintenis` | Onderwijsverbintenis | De relatie tussen een persoon en een `Toetsgelegenheid`: de feitelijke (voorbereide of lopende) deelname aan dat toetsmoment. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |  |
| `Formatieve resultaat structuur` | Resultaatstructuur | Structuur voor de geordende vastlegging van formatieve resultaten bij een opleidingsonderdeel. Per opleidingsonderdeel kunnen één of meerdere resultaatstructuren worden gemaakt. Een formatieve resultaatstructuur bestaat uit een aantal toetsen waarvan de formatieve resultaten kunnen vastgelegd en een berekeningswijze om tot een eindresultaat voor het opleidingsonderdeel als geheel te komen | overgenomen uit MORA | [Formatieve resultaat structuur](https://mora.mbodigitaal.nl/index.php/Id-a5f45830-ae81-5110-df27-b47e642a54a3) |  |
| `Summatieve resultaat structuur` | Resultaatstructuur | Structuur voor de geordende vastlegging van summatieve resultaten bij een onderwijsprogramma. Een summatieve resultaatstructuur bestaat uit een aantal examens of examenonderdelen waarvan de summatieve resultaten kunnen worden vastgelegd en een berekeningswijze om tot een eindresultaat voor het onderwijsprogramma als geheel te komen | overgenomen uit MORA | [Summatieve resultaat structuur](https://mora.mbodigitaal.nl/index.php/Id-a3020bda-2b3d-d3ac-ea08-a5be84de56cc) |  |

## Objecttypen zonder definitie

Deze objecttypen staan op de plaat maar hebben nog geen definitie. Waar een kader een tegenhanger kent is dat een verbijzondering waarvan de eigen definitie nog ontbreekt; de mapping hieronder toont de tegenhanger en de reden.

| Begrip | Objecttypen |
|---|---|
| Buiten de kolommen | `Persoon`, `Plaatsingsgroep` |
| Onderwijsaanbod | `Keuzedeelaanbod`, `Leergelegenheid`, `Lesgelegenheid`, `Onderwijseenheid aanbod`, `Opleidingsprogramma aanbod` |
| Onderwijskundig kader instelling | `Competenties / Skills`, `Inzicht`, `Kennis`, `Vaardigheid` |
| Onderwijsresultaat | `Aanwezigheid`, `Examengelegenheid resultaat`, `Keuzedeel resultaat`, `Leergelegenheid resultaat`, `Lesgelegenheid resultaat`, `Onderwijseenheid resultaat`, `Opleiding aanbod resultaat`, `Opleidingsprogramma resultaat`, `Toetsgelegenheid resultaat` |
| Onderwijsspecificatie | `Keuzedeel`, `Opleiding specificatie`, `Student keuze regelset` |
| Onderwijsverbintenis | `Keuzedeel aanbod verbintenis`, `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis`, `Onderwijseenheid aanbod verbintenis`, `Opleiding aanbod  verbintenis`, `Opleidingsprogramma aanbod verbintenis` |
| Resultaatstructuur | `Examenonderdeel weging`, `Persoonlijke ontwikkeling`, `Summatief Afrondingscriterium`, `Toetsonderdeel weging` |

## Mapping naar de referentiekaders

Per kader een van drie uitkomsten: een tegenhanger met link, `geen tegenhanger gevonden`, of `nog niet onderzocht`. Bij een verbijzondering staat de reden erbij.

| Begrip of objecttype | ROSA-KOI | MORA | HORA | Reden bij verbijzondering |
|---|---|---|---|---|
| `Kwalificatiekader mbo` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Onderwijsaanbod` | [`onderwijsaanbod (koi)`](https://rosa.wikixl.nl/index.php/Id-6d1ed39571de4ee5b1aefcf051991478) (verbijzondering) | geen tegenhanger gevonden | nog niet onderzocht | KOI vat ontwerp en uitvoering samen in een begrip. OKx splitst dat in de onderwijsspecificatie, het herbruikbare ontwerp, en het onderwijsaanbod, de ingeplande uitvoering. |
| `Onderwijskundig kader instelling` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Onderwijsresultaat` | [`onderwijsresultaat (koi)`](https://rosa.wikixl.nl/index.php/Id-e5d21e5384c0482ba4a501571e69927a) | [`Summatief resultaat`](https://mora.mbodigitaal.nl/index.php/Id-beaf106a-f329-b3ed-e513-6814b1fd65fa) (verbijzondering) | nog niet onderzocht | MORA scheidt het summatieve en het formatieve resultaat. OKx gebruikt onderwijsresultaat als de overkoepelende term van KOI en houdt het onderscheid in de resultaatstructuur. |
| `Onderwijsspecificatie` | [`onderwijsaanbod (koi)`](https://rosa.wikixl.nl/index.php/Id-6d1ed39571de4ee5b1aefcf051991478) (verbijzondering) | geen tegenhanger gevonden | nog niet onderzocht | De ontwerpkant van het KOI-begrip onderwijsaanbod, losgemaakt van de inplanning omdat een specificatie herbruikbaar is over meerdere aanbodmomenten. |
| `Onderwijsverbintenis` | [`onderwijsdeelname (koi)`](https://rosa.wikixl.nl/index.php/Id-ec977035c9be4b01bb1c14a5950a1799) | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Resultaatstructuur` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Examenplan` | geen tegenhanger gevonden | [`Examenplan`](https://mora.mbodigitaal.nl/index.php/Id-913bf380-1288-8a49-0bca-906d8b112e8f) | nog niet onderzocht |  |
| `Medewerker` | [`onderwijsmedewerker (koi)`](https://rosa.wikixl.nl/index.php/Id-5ea4d7d18cbc4f8eb3aea997a4d9b35d) | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Persoon` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Plaatsingsgroep` | geen tegenhanger gevonden | [`Cohort / periode`](https://mora.mbodigitaal.nl/index.php/Id-67cf6837-c59e-52aa-47e6-006c572259e1) (verbijzondering) | nog niet onderzocht | MORA groepeert studenten per cohort onder hetzelfde reglement. OKx gebruikt de plaatsingsgroep om verbintenissen op elk aanbodniveau te bundelen. |
| `Student` | [`onderwijsdeelnemer (koi)`](https://rosa.wikixl.nl/index.php/Id-ca1e8048bd094f02a348cf843fa07ae7) | [`Student`](https://mora.mbodigitaal.nl/index.php/Id-c7c163ee-2fa5-5b58-bc08-f401d0350c3a) | nog niet onderzocht |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | geen tegenhanger gevonden | [`Leervraag`](https://mora.mbodigitaal.nl/index.php/Id-306e945a-d2ff-000e-f950-f1acaa91a0bc) (verbijzondering) | nog niet onderzocht | MORA kent de leervraag als de vraag van de student wat hij wil leren. OKx verbijzondert die tot een uitwisselbaar verzoek dat leidt tot aanbod. De aanmelding (het verzoek om toegelaten te worden tot een opleiding) blijft, net als de inschrijving, bij het studentinformatiesysteem. |
| `Waarde document (diploma / certificaat)` | geen tegenhanger gevonden | [`Waarde document (diploma / certificaat)`](https://mora.mbodigitaal.nl/index.php/Id-8647eba0-e31d-5bcf-c12a-4d477069943c) | nog niet onderzocht |  |
| `Kerntaak` | geen tegenhanger gevonden | [`Kerntaak`](https://mora.mbodigitaal.nl/index.php/Id-99ef9489-49b3-4a3b-7a89-08ae36a3255e) | nog niet onderzocht |  |
| `Kwalificatie` | geen tegenhanger gevonden | [`Kwalificatie`](https://mora.mbodigitaal.nl/index.php/Id-f54b73a9-9562-2b28-deca-724e992bbcdb) | nog niet onderzocht |  |
| `Kwalificatie dossier` | geen tegenhanger gevonden | [`Kwalificatie dossier`](https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762) | nog niet onderzocht |  |
| `Werkproces` | geen tegenhanger gevonden | [`Werkproces`](https://mora.mbodigitaal.nl/index.php/Id-9cf4d404-b06c-473f-57d9-3945af33cfa8) | nog niet onderzocht |  |
| `Examengelegenheid` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Keuzedeelaanbod` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Leergelegenheid` | geen tegenhanger gevonden | [`Leeractiviteit`](https://mora.mbodigitaal.nl/index.php/Id-b25709e2-388a-d36b-696b-b82fd908f076) (verbijzondering) | nog niet onderzocht | De ingeplande kant van de MORA-leeractiviteit, op het niveau van een groep lessen. |
| `Lesgelegenheid` | geen tegenhanger gevonden | [`Leeractiviteit`](https://mora.mbodigitaal.nl/index.php/Id-b25709e2-388a-d36b-696b-b82fd908f076) (verbijzondering) | nog niet onderzocht | De ingeplande kant van de MORA-leeractiviteit, op het niveau van een enkele les. |
| `Onderwijseenheid aanbod` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Opleidingaanbod` | geen tegenhanger gevonden | [`Aangeboden opleiding`](https://mora.mbodigitaal.nl/index.php/Id-e723f9e6-adfc-40a1-0527-ee1b75b380dc) | nog niet onderzocht |  |
| `Opleidingsaanbod van Instelling` | geen tegenhanger gevonden | [`Opleidingen overzicht`](https://mora.mbodigitaal.nl/index.php/Id-9a23241c-a60e-6623-e13a-d945a761ab17) | nog niet onderzocht |  |
| `Opleidingsprogramma aanbod` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Toetsgelegenheid` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Competenties / Skills` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Inzicht` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Kennis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Leeruitkomst` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Vaardigheid` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Aanwezigheid` | geen tegenhanger gevonden | [`Aan- en afwezigheid`](https://mora.mbodigitaal.nl/index.php/Id-64aa6ac8-d531-7df9-8bcd-c5e09d4c15e9) (verbijzondering) | nog niet onderzocht | OKx legt alleen de aanwezigheid vast, als resultaat op een lesgelegenheid. |
| `Examengelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Formatief resultaat` | geen tegenhanger gevonden | [`Formatief resultaat`](https://mora.mbodigitaal.nl/index.php/Id-2bd2c72b-08d2-169d-9ed1-f4868ad34f5c) | nog niet onderzocht |  |
| `Formatieve beoordeling` | geen tegenhanger gevonden | [`Formatieve beoordeling`](https://mora.mbodigitaal.nl/index.php/Id-26fa321c-d407-817f-68c5-5509997d821b) | nog niet onderzocht |  |
| `Keuzedeel resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Leergelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Lesgelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Onderwijseenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Opleiding aanbod resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Opleidingsprogramma resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Summatief resultaat` | geen tegenhanger gevonden | [`Summatief resultaat`](https://mora.mbodigitaal.nl/index.php/Id-beaf106a-f329-b3ed-e513-6814b1fd65fa) | nog niet onderzocht |  |
| `Summatieve beoordeling` | geen tegenhanger gevonden | [`Summatieve beoordeling`](https://mora.mbodigitaal.nl/index.php/Id-0a14e5af-bf2e-2584-3320-095341367128) | nog niet onderzocht |  |
| `Toetsgelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Examenonderdeelspecificatie` | geen tegenhanger gevonden | [`Examen`](https://mora.mbodigitaal.nl/index.php/Id-9c12b2e2-2413-3a7b-ac80-bd44f5e381a5) (verbijzondering) | nog niet onderzocht | MORA beschrijft het examen als onderzoek naar kennis, inzicht, houding en vaardigheden. OKx specificeert het examenonderdeel apart van de examengelegenheid waarop het wordt afgenomen. |
| `Keuzedeel` | geen tegenhanger gevonden | [`Keuzedeel`](https://mora.mbodigitaal.nl/index.php/Id-018c4a8c-4129-ce3e-66a6-55ad855f7661) (verbijzondering) | nog niet onderzocht | In MORA hangt het keuzedeel in de kwalificatiestructuur, naast het kwalificatiedossier. In OKx is het keuzedeel een specialisatie van de opleidingsprogrammaspecificatie: het ontwerp waarmee een instelling het landelijke keuzedeel aanbiedt. Dezelfde naam, een andere plek. |
| `Keuzedeelruimte` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Leeronderdeel specificatie` | geen tegenhanger gevonden | [`Leertaak`](https://mora.mbodigitaal.nl/index.php/Id-be2dc6b8-cf25-4bd4-2950-2a4c2e4f2ffa) (verbijzondering) | nog niet onderzocht | MORA beschrijft de leertaak als lesstof en opdrachten. OKx maakt daar een herbruikbare specificatie van, binnen de onderwijseenheid. |
| `Les specificatie` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Onderwijseenheid specificatie` | [`onderwijseenheid (koi)`](https://rosa.wikixl.nl/index.php/Id-c74c161c6f1f4690933a31ce4d11f3b8) (verbijzondering) | [`Opleidings-onderdeel`](https://mora.mbodigitaal.nl/index.php/Id-17db36ca-368f-450e-cbfe-604b2fafee6e) (verbijzondering) | nog niet onderzocht | KOI beschrijft de onderwijseenheid als samenhangend geheel met een leerdoel. OKx specificeert die eenheid met leeruitkomsten, leeronderdelen en toetsonderdelen, los van de inplanning. |
| `Opleiding specificatie` | geen tegenhanger gevonden | [`Opleidings eenheid`](https://mora.mbodigitaal.nl/index.php/Id-422e89b9-f9e3-a3ae-56f7-25855f01d433) (verbijzondering) | nog niet onderzocht | MORA beschrijft de opleidingseenheid naar het waardedocument dat volgt. OKx gebruikt de specificatie als de instellingseigen beschrijving van die eenheid. |
| `Opleidingsprogramma specificatie` | geen tegenhanger gevonden | [`Onderwijs programma`](https://mora.mbodigitaal.nl/index.php/Id-3a7bb8e1-5748-3381-24f6-43c98479fe35) (verbijzondering) | nog niet onderzocht | De specificatiekant van het MORA-begrip onderwijs programma. MORA beschrijft het programma inclusief de planbaarheid; OKx scheidt de specificatie van het aanbod. |
| `Student keuze regelset` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Toetsonderdeel specificatie` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Examengelegenheid verbintenis` | geen tegenhanger gevonden | [`Examen deelname`](https://mora.mbodigitaal.nl/index.php/Id-abbf4971-fe71-2b56-20f1-6135b4a1eb82) (verbijzondering) | nog niet onderzocht | MORA registreert de examensessie waarin een examen wordt afgenomen. OKx legt de relatie vast tussen de kandidaat en de examengelegenheid, met dezelfde informatiestructuur als de toetsgelegenheidverbintenis. |
| `Keuzedeel aanbod verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Leergelegenheid verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Lesgelegenheid verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Onderwijseenheid aanbod verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Opleiding aanbod  verbintenis` | geen tegenhanger gevonden | [`Plaatsing`](https://mora.mbodigitaal.nl/index.php/Id-871a4ac0-e5e2-242d-7204-976fdc5cd613) (verbijzondering) | nog niet onderzocht | MORA kent de plaatsing als de deelname van een student aan een opleiding, en de inschrijving als de overeenkomst met rechten en plichten. OKx legt de verbintenis vast op een concreet opleidingaanbod; de overeenkomst blijft bij het studentinformatiesysteem. |
| `Opleidingsprogramma aanbod verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Toetsgelegenheid verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Examenonderdeel weging` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Formatieve resultaat structuur` | geen tegenhanger gevonden | [`Formatieve resultaat structuur`](https://mora.mbodigitaal.nl/index.php/Id-a5f45830-ae81-5110-df27-b47e642a54a3) | nog niet onderzocht |  |
| `Persoonlijke ontwikkeling` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Summatief Afrondingscriterium` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |
| `Summatieve resultaat structuur` | geen tegenhanger gevonden | [`Summatieve resultaat structuur`](https://mora.mbodigitaal.nl/index.php/Id-a3020bda-2b3d-d3ac-ea08-a5be84de56cc) | nog niet onderzocht |  |
| `Toetsonderdeel weging` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |  |

## Objecten uit de kaders zonder OKx-objecttype

De omgekeerde dekking: objecten uit MORA en KOI die bij het zoeken naar tegenhangers zijn opgehaald (35 van de 81 MORA-informatieobjecten en alle 13 KOI-begrippen) en die in de lijst niet als tegenhanger voorkomen. De overige MORA-objecten zijn nog niet beoordeeld en staan hier niet. Voor de vertaling van een eigen doelarchitectuur naar OKx zegt dit waar OKx niets over uitwisselt.

| Kader | Object | Definitie |
|---|---|---|
| MORA | [`Aanmelding`](https://mora.mbodigitaal.nl/index.php/Id-666a838e-d9bd-c5fd-ad85-545ec69f1566) | Het schriftelijke verzoek om een student toe te laten tot een school en/of een specifieke opleiding |
| MORA | [`Certificaat`](https://mora.mbodigitaal.nl/index.php/Id-4b956a9f-0487-7d1f-d915-5c887b43d41f) | Een mbo-certificaat bevat een deel van de kwalificatie-eisen van een mbo-opleiding. Dit kan gaan om keuzedelen of beroepsgerichte onderdelen. De minister van OCW stelt met een regeling vast aan welke onderdelen van een mbo-opleiding een mbo-certificaat wordt verbonden. Een door de student behaald mbo-certificaat wordt geregistreerd in het diplomaregister van DUO |
| MORA | [`Diploma`](https://mora.mbodigitaal.nl/index.php/Id-39568458-7a8e-36ed-9ec1-971592a7e099) | Waardedocument dat de student behaalt nadat aan alle eisen is voldaan die beschreven zijn in de kwalificatie |
| MORA | [`Generiek examenonderdeel`](https://mora.mbodigitaal.nl/index.php/Id-da9eca0c-230d-ff88-be08-fa6224c28f48) | De examenonderdelen uit het kwalificatiedossier die binnen het basisdeel vallen. Het basisdeel bevat de generieke onderdelen Nederlandse taal, rekenen, loopbaan en burgerschap en Engels (uitsluitend voor niveau 4) |
| MORA | [`Inschrijving`](https://mora.mbodigitaal.nl/index.php/Id-b329667d-f273-4c9c-2866-73ccce570d18) | Een overeenkomst tussen de onderwijsaanbieder en de student waar de rechten en plichten van onderwijsaanbieder en student in staan. Deze overeenkomst bevat ook voorwaarden waarin o.a. is opgenomen dat de student (en bij minderjarigen de ouders) akkoord gaan met alle voor het onderwijs relevante onderdelen zoals de BPV |
| MORA | [`Onderwijs aanbieder`](https://mora.mbodigitaal.nl/index.php/Id-64f8ba53-233e-46fe-6581-1b8148927876) | Een organisatie die door een bevoegd gezag is ingesteld voor het verzorgen van onderwijs |
| MORA | [`Onderwijsplan`](https://mora.mbodigitaal.nl/index.php/Id-8e2d0035-fb6e-8666-381b-d6d235b79b85) | Het onderwijsplan beschrijft per aangeboden opleiding het onderwijsprogramma inclusief de opleidingsonderdelen en standaard leerroute(s). Het onderwijsplan bevat daarnaast o.a. een globale beschrijving van de leeractiviteiten en leertaken en kan aanvullende informatie omvatten, zoals de doelen van de opleiding, de leerinhoud, toetsen, didactische principes en/of de wijze en het tijdstip waarop dit aangeboden wordt. In het onderwijsplan staat binnen welke omgeving (mbo-school, zelfstudie of beroepspraktijk) het onderwijs plaatsvindt. Hierbij houdt de school rekening met de praktische haalbaarheid en de doelgroep |
| MORA | [`Persoonlijke leerroute`](https://mora.mbodigitaal.nl/index.php/Id-24c6cb1f-773c-ce02-b525-053322772250) | Een planbaar geheel van opleidingsonderdelen dat is afgestemd op de leervraag van de student. De standaard leerroutes uit het onderwijsprogramma staan hier model voor. Afwijken van de standaard leerroute kan met begeleiding en binnen de keuzevrijheid die het onderwijsprogramma biedt |
| ROSA-KOI | [`leerresultaat (koi)`](https://rosa.wikixl.nl/index.php/Id-943051f7f72246b0a3d3656c8e0b75cd) | Vastgelegde uitkomst van een door een onderwijsdeelnemer uitgevoerde leeractiviteit. |
| ROSA-KOI | [`onderwijsactiviteit (koi)`](https://rosa.wikixl.nl/index.php/Id-a5b4e50fc6eb4e7186d4b7e5ec62f3c7) | Het aanleren van kennis, vaardigheden en attitudes om vooraf vastgelegde doelen na te streven. |
| ROSA-KOI | [`onderwijslocatie (koi)`](https://rosa.wikixl.nl/index.php/Id-4255ee059f4448279eaeff1f151ebbd6) | Een plek waar onderwijs wordt gegeven. |
| ROSA-KOI | [`onderwijsmateriaal (koi)`](https://rosa.wikixl.nl/index.php/Id-d79862549a824a3ca72a7df50489bdee) | Content en (fysieke) benodigdheden bestemd voor gebruik binnen onderwijsactiviteiten. |
| ROSA-KOI | [`onderwijsondersteuning (koi)`](https://rosa.wikixl.nl/index.php/Id-223e100616a846aaac245ccc9023a328) | Alle activiteiten die nodig zijn om de deelname aan het onderwijs mogelijk te maken. |
| ROSA-KOI | [`onderwijsontwikkeling (koi)`](https://rosa.wikixl.nl/index.php/Id-13d010dc71ff492f86a1fa6ea9e46d7c) | Het samenstellen van onderwijsprogramma's, curricula en/of leerlijnen en het variëren en arrangeren in het beschikbare onderwijsaanbod en/of het ontwikkelen van onderwijsmateriaal gebruikmakend van beschikbare onderwijsmaterialen. |
| ROSA-KOI | [`onderwijsorganisatie (koi)`](https://rosa.wikixl.nl/index.php/Id-25e646d0ef8b4cc298d0976f745869b0) | Een organisatie die onderwijs aanbiedt en verzorgt en regelt dat aan de gestelde randvoorwaarden wordt voldaan. |


## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md) | De objecttypen en hun samenhang; deze lijst geeft er de definities bij |
| [Begrippenkader leerroute-uitwerking](../leerroute-uitwerking/doc/begrippenkader.md) | De families, de niveaus en de stadia |
| [`begrippen.json`](begrippen.json) | Deze lijst machineleesbaar; dit document wordt eruit gegenereerd |
| [`begrippen-extractie.json`](begrippen-extractie.json) | Elke term tussen backquotes in meta en Public, met vindplaatsen |
| [`referentiekaders.json`](referentiekaders.json) | De letterlijk overgenomen definities uit MORA en KOI, met bron-URL en ophaaldatum |
| [MORA-definitiemapping v0.4](../../definitie_mapping_MORA_OEAPI_excel/) | Eerdere mapping van MORA-objecten op OEAPI, als werkblad; deze lijst vervangt hem niet en verwijst ernaar waar de keuzes verschillen |
