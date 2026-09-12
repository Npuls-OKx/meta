# Begrippenlijst OKx

## Context

De koppelvlakken van OKx wisselen informatie uit tussen instellingen en tussen systemen. Dat werkt alleen als een term aan beide kanten hetzelfde betekent.

## Inleiding

Deze lijst geeft per begrip de vastgestelde schrijfwijze, een definitie en de vindplaats van die definitie. Een begrip zonder vindplaats staat er als gat in, niet als dichtgeschreven aanname.

## Doel

Vaststellen wat OKx onder een term verstaat, zodat een lezer van een specificatie niet hoeft te raden. De lijst is de toetssteen voor naamgeving in het informatiemodel, de koppelvlakspecificaties en de reviews.

## Scope

De objecttypen en begrippen van het informatiemodel OKx, elk eerst gelegd naast MORA en het Kernmodel Onderwijsinformatie binnen ROSA. HORA is nog niet onderzocht. Termen uit de rest van de documentatie vallen buiten deze versie.

Gezocht in de volledige lijst van het MORA-informatiemodel (81 informatieobjecten, https://mora.mbodigitaal.nl/index.php/Informatiemodel) en in het volledige overzicht van het Kernmodel Onderwijsinformatie (https://rosa.wikixl.nl/index.php/Kernmodel_Onderwijsinformatie), opgehaald op 9 september 2026. Een begrip dat in beide lijsten ontbreekt staat als 'geen tegenhanger gevonden'.

## Dekking

Versie v0.2. De kaders zijn geraadpleegd op 2026-09-09.

| | |
|---|---|
| Begrippen en objecttypen | 69 |
| Met een definitie uit een referentiekader | 20 |
| Met een definitie uit een OKx-document | 14 |
| Zonder definitie | 35 |
| Termen uit de markdown die nog wachten | 782 |

## Begrippen

De begrippen delen de keten in. Ze zijn niveau 1 in het [Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/); de objecttypen eronder zijn niveau 2. De uitleg van die gelaagdheid staat in het [informatiemodel](../../../model/informatiemodel/informatiemodel.md#begrippen).

| Begrip | Definitie | Herkomst | Bron |
|---|---|---|---|
| `Kwalificatiekader mbo` | Het geheel van landelijk vastgestelde eisen waaraan een opleiding moet voldoen. Vastgesteld en beheerd buiten OKx | nieuw voor de solution-laag | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijskundig kader instelling` | De beoogde leeruitkomsten waartegen een instelling haar onderwijs specificeert. OKx gaat uit van landelijk gestandaardiseerde en beheerde leeruitkomsten; de onderwijskundige vrijheid van de instelling zit in de specificaties | nieuw voor de solution-laag | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijsspecificatie` | Het herbruikbare ontwerp van een onderwijsonderdeel, los van wanneer het draait en wie eraan meedoet | verbijzondering van `onderwijsaanbod (koi)` (ROSA-KOI) | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijsaanbod` | Een specificatie die is ingepland: een periode, een capaciteit en waar van toepassing concrete plek, docent en tijd | verbijzondering van `onderwijsaanbod (koi)` (ROSA-KOI) | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijsverbintenis` | Een afspraak voor het gaan volgen, volgen en hebben gevolgd van onderwijs. | overgenomen uit ROSA-KOI | [onderwijsdeelname (koi)](https://rosa.wikixl.nl/index.php/Id-ec977035c9be4b01bb1c14a5950a1799) |
| `Onderwijsresultaat` | Vastgelegde en geformaliseerde beoordeling op basis van een of meer leerresultaten. | overgenomen uit ROSA-KOI | [onderwijsresultaat (koi)](https://rosa.wikixl.nl/index.php/Id-e5d21e5384c0482ba4a501571e69927a) |
| `Resultaatstructuur` | De samenstelling en weging waarmee losse resultaten optellen tot een uitspraak over de beoogde leeruitkomsten, en daarmee over een kwalificatie of certificaat | nieuw voor de solution-laag | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md#begrippen) |

## Objecttypen met een definitie

| Objecttype | Begrip | Definitie | Herkomst | Bron |
|---|---|---|---|---|
| `Examenplan` |  | Het examenplan geeft per kwalificatie een overzicht van de examenonderdelen en examens die een mbo-school inzet voor de examinering (kwalificerende beoordeling). Het examenplan geeft inzicht in de onderdelen die een student met een voldoende moet afsluiten om in aanmerking te komen voor een diploma | overgenomen uit MORA | [Examenplan](https://mora.mbodigitaal.nl/index.php/Id-913bf380-1288-8a49-0bca-906d8b112e8f) |
| `Medewerker` |  | Een natuurlijk persoon die op grond van een overeenkomst werkzaam is voor een onderwijsorganisatie. | overgenomen uit ROSA-KOI | [onderwijsmedewerker (koi)](https://rosa.wikixl.nl/index.php/Id-5ea4d7d18cbc4f8eb3aea997a4d9b35d) |
| `Student` |  | Een persoon die aan onderwijsactiviteiten deelneemt of dat wil gaan doen. Dit omvat ingeschreven studenten, potentiële studenten en alumni | overgenomen uit MORA | [Student](https://mora.mbodigitaal.nl/index.php/Id-c7c163ee-2fa5-5b58-bc08-f401d0350c3a) |
| `Waarde document (diploma / certificaat)` |  | Het bewijsstuk van een eindoordeel over het voltooien van een opleiding, keuzedeel, deelkwalificatie of module | overgenomen uit MORA | [Waarde document (diploma / certificaat)](https://mora.mbodigitaal.nl/index.php/Id-8647eba0-e31d-5bcf-c12a-4d477069943c) |
| `Kerntaak` | Kwalificatiekader mbo | Een kerntaak is een substantieel deel van de beroepsuitoefening naar belang omvang (tijdsbeslag of frequentie) of beide. Een kerntaak bestaat uit een geheel van inhoudelijk met elkaar samenhangende werkprocessen kenmerkend voor de beroepsuitoefening. Een kwalificatiedossier heeft een beperkt aantal kerntaken | overgenomen uit MORA | [Kerntaak](https://mora.mbodigitaal.nl/index.php/Id-99ef9489-49b3-4a3b-7a89-08ae36a3255e) |
| `Kwalificatie` | Kwalificatiekader mbo | De kwalificatie is de combinatie van het basis- en profieldeel uit het kwalificatiedossier. De kwalificatie omvat wat de beginnend beroepsbeoefenaar moet kennen en kunnen als hij gediplomeerd is en start op de arbeidsmarkt | overgenomen uit MORA | [Kwalificatie](https://mora.mbodigitaal.nl/index.php/Id-f54b73a9-9562-2b28-deca-724e992bbcdb) |
| `Kwalificatie dossier` | Kwalificatiekader mbo | Het kwalificatiedossier beschrijft de eisen waaraan een student moet voldoen om zijn diploma te behalen. Elk dossier bevat een of meer kwalificaties en iedere kwalificatie leidt tot een diploma. Alle kwalificatiedossiers samen, aangevuld met de keuzedelen, vormen de kwalificatiestructuur. Een kwalificatiedossier bestaat uit een basisdeel en een of meer profieldelen | overgenomen uit MORA | [Kwalificatie dossier](https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762) |
| `Werkproces` | Kwalificatiekader mbo | Een werkproces is een afgebakend geheel van beroepshandelingen binnen een kerntaak. Het werkproces kent een begin en een eind heeft een resultaat en wordt als kenmerkend herkend in de beroepspraktijk | overgenomen uit MORA | [Werkproces](https://mora.mbodigitaal.nl/index.php/Id-9cf4d404-b06c-473f-57d9-3945af33cfa8) |
| `Examengelegenheid` | Onderwijsaanbod | Het georganiseerde aanbod van een examenmoment: planning, locatie, surveillant-capaciteit en kandidaten, gekoppeld aan precies één `Examenspecificatie`. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Opleidingaanbod` | Onderwijsaanbod | Een opleidingseenheid die door een onderwijsaanbieder aangeboden wordt in een bepaalde vorm, al dan niet op een bepaalde onderwijslocatie, waarop een onderwijsvolger zich kan inschrijven | overgenomen uit MORA | [Aangeboden opleiding](https://mora.mbodigitaal.nl/index.php/Id-e723f9e6-adfc-40a1-0527-ee1b75b380dc) |
| `Opleidingsaanbod van Instelling` | Onderwijsaanbod | Het geheel van opleiding dat door de instelling wordt aangeboden | overgenomen uit MORA | [Opleidingen overzicht](https://mora.mbodigitaal.nl/index.php/Id-9a23241c-a60e-6623-e13a-d945a761ab17) |
| `Toetsgelegenheid` | Onderwijsaanbod | Het georganiseerde aanbod van een toetsmoment: wanneer, waar en onder welke condities een toetsonderdeel wordt afgenomen, gekoppeld aan precies één `Toetsonderdeel-specificatie`. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Leeruitkomst` | Onderwijskundig kader instelling | Een concreet en observeerbaar resultaat van leren, dat beschrijft wat een student na het doorlopen van één of meer leertaken weet, begrijpt of kan toepassen, en dat als voorwaarde geldt om een opleidingsonderdeel succesvol af te ronden — de vertaling van leertaken in een breakdown door onderwijskundigen. Bij voorkeur uitgedrukt in een sectoroverstijgende, gestandaardiseerde skillstaxonomie (zoals CompetentNL), in dimensies kennis, inzicht en vaardigheden; zie hoofdstuk 4. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Keuzedeel` | Onderwijsspecificatie | Keuzedelen zijn een verrijking van de kwalificatie (basis- en profieldeel) en kunnen voor de student verbredend of verdiepend zijn of bijdragen aan een betere doorstroom naar een vervolgopleiding | overgenomen uit MORA | [Keuzedeel](https://mora.mbodigitaal.nl/index.php/Id-018c4a8c-4129-ce3e-66a6-55ad855f7661) |
| `Leeronderdeel specificatie` | Onderwijsspecificatie | De specificatie van het deel van de onderwijseenheid (onder meer bestaande uit lesstof en opdrachten) waarin de student competenties kan verwerven. | afgeleid uit klus 53 (alignment MORA en HORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Les specificatie` | Onderwijsspecificatie | De specificatie van het kleinste geplande leermoment binnen een leeronderdeel: welke lesinhoud, leeractiviteit of toetsactiviteit in dat moment wordt aangeboden. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Onderwijseenheid specificatie` | Onderwijsspecificatie | De specificatie van de fundamentele eenheid waarin onderwijs wordt ontworpen en aangeboden, in de vorm van een samenhangend stelsel van één of meer (beoogde) leeruitkomsten, leeronderdelen en/of toetsonderdelen. (NB: Leeruitkomsten omvat o.a. kennis, inzicht en vaardigheden.) | afgeleid uit klus 53 (alignment MORA en HORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Opleidingsprogramma specificatie` | Onderwijsspecificatie | Een samenhangende verzameling van één of meer (deel)programma's, onderwijseenheden, of leeruitkomsten die kunnen leiden tot een kwalificatie. | afgeleid uit klus 53 (alignment MORA en HORA) | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Toetsonderdeel specificatie` | Onderwijsspecificatie | De specificatie van het deel van de onderwijseenheid (bestaand uit een onderzoek naar kennis, inzicht, houding en vaardigheden van de student), waarmee wordt vastgesteld over welke competenties de student beschikt, leidend tot een formatieve of summatieve beoordeling. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Examengelegenheid verbintenis` | Onderwijsverbintenis | De registratie van een formele activiteit (lees examensessie) waarin een examen wordt afgenomen | overgenomen uit MORA | [Examen deelname](https://mora.mbodigitaal.nl/index.php/Id-abbf4971-fe71-2b56-20f1-6135b4a1eb82) |
| `Toetsgelegenheid verbintenis` | Onderwijsverbintenis | De relatie tussen een persoon en een `Toetsgelegenheid`: de feitelijke (voorbereide of lopende) deelname aan dat toetsmoment. | afgeleid uit het vlakkenmodel, afgestemd op klus 53 | [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Formatief resultaat` | Resultaatstructuur | Een waardering die de student informatie geeft over de kwaliteit en voortgang van zijn of haar leren, maar niet meetelt voor de uiteindelijke kwalificering. Formatieve resultaten worden vastgelegd conform de formatieve resultaatstructuur. Formatieve resultaten worden ook wel toetsresultaten genoemd | overgenomen uit MORA | [Formatief resultaat](https://mora.mbodigitaal.nl/index.php/Id-2bd2c72b-08d2-169d-9ed1-f4868ad34f5c) |
| `Formatieve beoordeling` | Resultaatstructuur | Een beoordeling, veelal van een toets, die niet meetelt voor de uiteindelijke kwalificering, maar de lerende informatie geeft over de kwaliteit van zijn of haar leren | overgenomen uit MORA | [Formatieve beoordeling](https://mora.mbodigitaal.nl/index.php/Id-26fa321c-d407-817f-68c5-5509997d821b) |
| `Formatieve resultaat structuur` | Resultaatstructuur | Structuur voor de geordende vastlegging van formatieve resultaten bij een opleidingsonderdeel. Per opleidingsonderdeel kunnen één of meerdere resultaatstructuren worden gemaakt. Een formatieve resultaatstructuur bestaat uit een aantal toetsen waarvan de formatieve resultaten kunnen vastgelegd en een berekeningswijze om tot een eindresultaat voor het opleidingsonderdeel als geheel te komen | overgenomen uit MORA | [Formatieve resultaat structuur](https://mora.mbodigitaal.nl/index.php/Id-a5f45830-ae81-5110-df27-b47e642a54a3) |
| `Summatief resultaat` | Resultaatstructuur | Een formele, door de instelling geregistreerde waardering voor summatief gemaakt werk (zoals een examen of BPV-beoordeling) die meetelt voor de uiteindelijke kwalificering. Summatieve resultaten worden vastgelegd conform de summatieve resultaatstructuur. Summatieve resultaten worden ook wel examenresultaten genoemd | overgenomen uit MORA | [Summatief resultaat](https://mora.mbodigitaal.nl/index.php/Id-beaf106a-f329-b3ed-e513-6814b1fd65fa) |
| `Summatieve beoordeling` | Resultaatstructuur | De beoordeling van summatief gemaakt werk, zoals de beoordeling van een examen of een BPV-beoordeling | overgenomen uit MORA | [Summatieve beoordeling](https://mora.mbodigitaal.nl/index.php/Id-0a14e5af-bf2e-2584-3320-095341367128) |
| `Summatieve resultaat structuur` | Resultaatstructuur | Structuur voor de geordende vastlegging van summatieve resultaten bij een onderwijsprogramma. Een summatieve resultaatstructuur bestaat uit een aantal examens of examenonderdelen waarvan de summatieve resultaten kunnen worden vastgelegd en een berekeningswijze om tot een eindresultaat voor het onderwijsprogramma als geheel te komen | overgenomen uit MORA | [Summatieve resultaat structuur](https://mora.mbodigitaal.nl/index.php/Id-a3020bda-2b3d-d3ac-ea08-a5be84de56cc) |

## Objecttypen zonder definitie

Deze objecttypen staan op de plaat, hebben geen tegenhanger in MORA of KOI, en zijn binnen OKx nog niet gedefinieerd.

| Begrip | Objecttypen |
|---|---|
| Buiten de kolommen | `Persoon`, `Plaatsingsgroep`, `Verzoek tot Aanbod / Intekening op specificatie` |
| Onderwijsaanbod | `Keuzedeelaanbod`, `Leergelegenheid`, `Lesgelegenheid`, `Onderwijseenheid aanbod`, `Opleidingsprogramma aanbod` |
| Onderwijskundig kader instelling | `Competenties / Skills`, `Inzicht`, `Kennis`, `Vaardigheid` |
| Onderwijsresultaat | `Aanwezigheid`, `Examengelegenheid resultaat`, `Keuzedeel resultaat`, `Leergelegenheid resultaat`, `Lesgelegenheid resultaat`, `Onderwijseenheid resultaat`, `Opleiding aanbod resultaat`, `Opleidingsprogramma resultaat`, `Toetsgelegenheid resultaat` |
| Onderwijsspecificatie | `Examenonderdeelspecificatie`, `Keuzedeelruimte`, `Opleiding specificatie`, `Student keuze regelset` |
| Onderwijsverbintenis | `Keuzedeel aanbod verbintenis`, `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis`, `Onderwijseenheid aanbod verbintenis`, `Opleiding aanbod  verbintenis`, `Opleidingsprogramma aanbod verbintenis` |
| Resultaatstructuur | `Examenonderdeel weging`, `Persoonlijke ontwikkeling`, `Summatief Afrondingscriterium`, `Toetsonderdeel weging` |

## Mapping naar de referentiekaders

Per kader een van drie uitkomsten, nooit een lege cel: een tegenhanger met link, `geen tegenhanger gevonden`, of `nog niet onderzocht`. Bij een verbijzondering gaat OKx verder dan het kader; de reden staat in [`begrippen.json`](begrippen.json).

| Begrip of objecttype | ROSA-KOI | MORA | HORA |
|---|---|---|---|
| `Kwalificatiekader mbo` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Onderwijsaanbod` | [`onderwijsaanbod (koi)`](https://rosa.wikixl.nl/index.php/Id-6d1ed39571de4ee5b1aefcf051991478) (verbijzondering) | geen tegenhanger gevonden | nog niet onderzocht |
| `Onderwijskundig kader instelling` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Onderwijsresultaat` | [`onderwijsresultaat (koi)`](https://rosa.wikixl.nl/index.php/Id-e5d21e5384c0482ba4a501571e69927a) | [`Summatief resultaat`](https://mora.mbodigitaal.nl/index.php/Id-beaf106a-f329-b3ed-e513-6814b1fd65fa) (verbijzondering) | nog niet onderzocht |
| `Onderwijsspecificatie` | [`onderwijsaanbod (koi)`](https://rosa.wikixl.nl/index.php/Id-6d1ed39571de4ee5b1aefcf051991478) (verbijzondering) | geen tegenhanger gevonden | nog niet onderzocht |
| `Onderwijsverbintenis` | [`onderwijsdeelname (koi)`](https://rosa.wikixl.nl/index.php/Id-ec977035c9be4b01bb1c14a5950a1799) | geen tegenhanger gevonden | nog niet onderzocht |
| `Resultaatstructuur` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Examenplan` | geen tegenhanger gevonden | [`Examenplan`](https://mora.mbodigitaal.nl/index.php/Id-913bf380-1288-8a49-0bca-906d8b112e8f) | nog niet onderzocht |
| `Medewerker` | [`onderwijsmedewerker (koi)`](https://rosa.wikixl.nl/index.php/Id-5ea4d7d18cbc4f8eb3aea997a4d9b35d) | geen tegenhanger gevonden | nog niet onderzocht |
| `Student` | [`onderwijsdeelnemer (koi)`](https://rosa.wikixl.nl/index.php/Id-ca1e8048bd094f02a348cf843fa07ae7) | [`Student`](https://mora.mbodigitaal.nl/index.php/Id-c7c163ee-2fa5-5b58-bc08-f401d0350c3a) | nog niet onderzocht |
| `Waarde document (diploma / certificaat)` | geen tegenhanger gevonden | [`Waarde document (diploma / certificaat)`](https://mora.mbodigitaal.nl/index.php/Id-8647eba0-e31d-5bcf-c12a-4d477069943c) | nog niet onderzocht |
| `Persoon` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Plaatsingsgroep` | geen tegenhanger gevonden | [`Cohort / periode`](https://mora.mbodigitaal.nl/index.php/Id-67cf6837-c59e-52aa-47e6-006c572259e1) (verbijzondering) | nog niet onderzocht |
| `Verzoek tot Aanbod / Intekening op specificatie` | geen tegenhanger gevonden | [`Leervraag`](https://mora.mbodigitaal.nl/index.php/Id-306e945a-d2ff-000e-f950-f1acaa91a0bc) (verbijzondering) | nog niet onderzocht |
| `Kerntaak` | geen tegenhanger gevonden | [`Kerntaak`](https://mora.mbodigitaal.nl/index.php/Id-99ef9489-49b3-4a3b-7a89-08ae36a3255e) | nog niet onderzocht |
| `Kwalificatie` | geen tegenhanger gevonden | [`Kwalificatie`](https://mora.mbodigitaal.nl/index.php/Id-f54b73a9-9562-2b28-deca-724e992bbcdb) | nog niet onderzocht |
| `Kwalificatie dossier` | geen tegenhanger gevonden | [`Kwalificatie dossier`](https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762) | nog niet onderzocht |
| `Werkproces` | geen tegenhanger gevonden | [`Werkproces`](https://mora.mbodigitaal.nl/index.php/Id-9cf4d404-b06c-473f-57d9-3945af33cfa8) | nog niet onderzocht |
| `Examengelegenheid` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Keuzedeelaanbod` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Leergelegenheid` | geen tegenhanger gevonden | [`Leeractiviteit`](https://mora.mbodigitaal.nl/index.php/Id-b25709e2-388a-d36b-696b-b82fd908f076) (verbijzondering) | nog niet onderzocht |
| `Lesgelegenheid` | geen tegenhanger gevonden | [`Leeractiviteit`](https://mora.mbodigitaal.nl/index.php/Id-b25709e2-388a-d36b-696b-b82fd908f076) (verbijzondering) | nog niet onderzocht |
| `Onderwijseenheid aanbod` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Opleidingaanbod` | geen tegenhanger gevonden | [`Aangeboden opleiding`](https://mora.mbodigitaal.nl/index.php/Id-e723f9e6-adfc-40a1-0527-ee1b75b380dc) | nog niet onderzocht |
| `Opleidingsaanbod van Instelling` | geen tegenhanger gevonden | [`Opleidingen overzicht`](https://mora.mbodigitaal.nl/index.php/Id-9a23241c-a60e-6623-e13a-d945a761ab17) | nog niet onderzocht |
| `Opleidingsprogramma aanbod` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Toetsgelegenheid` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Competenties / Skills` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Inzicht` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Kennis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Leeruitkomst` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Vaardigheid` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Aanwezigheid` | geen tegenhanger gevonden | [`Aan- en afwezigheid`](https://mora.mbodigitaal.nl/index.php/Id-64aa6ac8-d531-7df9-8bcd-c5e09d4c15e9) (verbijzondering) | nog niet onderzocht |
| `Examengelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Keuzedeel resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Leergelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Lesgelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Onderwijseenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Opleiding aanbod resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Opleidingsprogramma resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Toetsgelegenheid resultaat` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Examenonderdeelspecificatie` | geen tegenhanger gevonden | [`Examen`](https://mora.mbodigitaal.nl/index.php/Id-9c12b2e2-2413-3a7b-ac80-bd44f5e381a5) (verbijzondering) | nog niet onderzocht |
| `Keuzedeel` | geen tegenhanger gevonden | [`Keuzedeel`](https://mora.mbodigitaal.nl/index.php/Id-018c4a8c-4129-ce3e-66a6-55ad855f7661) | nog niet onderzocht |
| `Keuzedeelruimte` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Leeronderdeel specificatie` | geen tegenhanger gevonden | [`Leertaak`](https://mora.mbodigitaal.nl/index.php/Id-be2dc6b8-cf25-4bd4-2950-2a4c2e4f2ffa) (verbijzondering) | nog niet onderzocht |
| `Les specificatie` | geen tegenhanger gevonden | [`Leeractiviteit`](https://mora.mbodigitaal.nl/index.php/Id-b25709e2-388a-d36b-696b-b82fd908f076) (verbijzondering) | nog niet onderzocht |
| `Onderwijseenheid specificatie` | [`onderwijseenheid (koi)`](https://rosa.wikixl.nl/index.php/Id-c74c161c6f1f4690933a31ce4d11f3b8) (verbijzondering) | [`Opleidings-onderdeel`](https://mora.mbodigitaal.nl/index.php/Id-17db36ca-368f-450e-cbfe-604b2fafee6e) (verbijzondering) | nog niet onderzocht |
| `Opleiding specificatie` | geen tegenhanger gevonden | [`Opleidings eenheid`](https://mora.mbodigitaal.nl/index.php/Id-422e89b9-f9e3-a3ae-56f7-25855f01d433) (verbijzondering) | nog niet onderzocht |
| `Opleidingsprogramma specificatie` | geen tegenhanger gevonden | [`Onderwijs programma`](https://mora.mbodigitaal.nl/index.php/Id-3a7bb8e1-5748-3381-24f6-43c98479fe35) (verbijzondering) | nog niet onderzocht |
| `Student keuze regelset` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Toetsonderdeel specificatie` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Examengelegenheid verbintenis` | geen tegenhanger gevonden | [`Examen deelname`](https://mora.mbodigitaal.nl/index.php/Id-abbf4971-fe71-2b56-20f1-6135b4a1eb82) | nog niet onderzocht |
| `Keuzedeel aanbod verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Leergelegenheid verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Lesgelegenheid verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Onderwijseenheid aanbod verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Opleiding aanbod  verbintenis` | geen tegenhanger gevonden | [`Inschrijving`](https://mora.mbodigitaal.nl/index.php/Id-b329667d-f273-4c9c-2866-73ccce570d18) (verbijzondering) | nog niet onderzocht |
| `Opleidingsprogramma aanbod verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Toetsgelegenheid verbintenis` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Examenonderdeel weging` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Formatief resultaat` | geen tegenhanger gevonden | [`Formatief resultaat`](https://mora.mbodigitaal.nl/index.php/Id-2bd2c72b-08d2-169d-9ed1-f4868ad34f5c) | nog niet onderzocht |
| `Formatieve beoordeling` | geen tegenhanger gevonden | [`Formatieve beoordeling`](https://mora.mbodigitaal.nl/index.php/Id-26fa321c-d407-817f-68c5-5509997d821b) | nog niet onderzocht |
| `Formatieve resultaat structuur` | geen tegenhanger gevonden | [`Formatieve resultaat structuur`](https://mora.mbodigitaal.nl/index.php/Id-a5f45830-ae81-5110-df27-b47e642a54a3) | nog niet onderzocht |
| `Persoonlijke ontwikkeling` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Summatief Afrondingscriterium` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |
| `Summatief resultaat` | geen tegenhanger gevonden | [`Summatief resultaat`](https://mora.mbodigitaal.nl/index.php/Id-beaf106a-f329-b3ed-e513-6814b1fd65fa) | nog niet onderzocht |
| `Summatieve beoordeling` | geen tegenhanger gevonden | [`Summatieve beoordeling`](https://mora.mbodigitaal.nl/index.php/Id-0a14e5af-bf2e-2584-3320-095341367128) | nog niet onderzocht |
| `Summatieve resultaat structuur` | geen tegenhanger gevonden | [`Summatieve resultaat structuur`](https://mora.mbodigitaal.nl/index.php/Id-a3020bda-2b3d-d3ac-ea08-a5be84de56cc) | nog niet onderzocht |
| `Toetsonderdeel weging` | geen tegenhanger gevonden | geen tegenhanger gevonden | nog niet onderzocht |

## Negeerlijst

Termen die tussen backquotes voorkomen maar geen begrip zijn.

| Term | Reden |
|---|---|
| `.feature` | bestandsextensie |
| `clidev` | branchnaam |
| `dev` | branchnaam |
| `main` | branchnaam |
| `specificatie-gewijzigd` | naam van een gebeurtenis |
| `gepubliceerd` | statuswaarde |
| `id` | veldnaam |
| `inrichtingsstatus` | veldnaam |
| `status` | veldnaam |
| `versie` | veldnaam |
| `verwerkingsstatus` | veldnaam |
| `Association.state` | veldpad in OEAPI |
| `v0.1.0` | versienummer |
| `v1.0.0` | versienummer |

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md) | De objecttypen en hun samenhang; deze lijst geeft er de definities bij |
| [Begrippenkader leerroute-uitwerking](../leerroute-uitwerking/doc/begrippenkader.md) | De families, de niveaus en de stadia |
| [`begrippen.json`](begrippen.json) | Deze lijst machineleesbaar; dit document wordt eruit gegenereerd |
| [`begrippen-extractie.json`](begrippen-extractie.json) | Elke term tussen backquotes in meta en Public, met vindplaatsen |
| [`referentiekaders.json`](referentiekaders.json) | De letterlijk overgenomen definities uit MORA en KOI, met bron-URL en ophaaldatum |
