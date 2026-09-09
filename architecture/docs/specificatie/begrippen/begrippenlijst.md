# Begrippenlijst OKx

## Context

De koppelvlakken van OKx wisselen informatie uit tussen instellingen en tussen systemen. Dat werkt alleen als een term aan beide kanten hetzelfde betekent.

## Inleiding

Deze lijst geeft per begrip de vastgestelde schrijfwijze, een definitie en de vindplaats van die definitie. Een begrip zonder vindplaats staat er als gat in, niet als dichtgeschreven aanname.

## Doel

Vaststellen wat OKx onder een term verstaat, zodat een lezer van een specificatie niet hoeft te raden. De lijst is de toetssteen voor naamgeving in het informatiemodel, de koppelvlakspecificaties en de reviews.

## Scope

De objecttypen en begrippen van het informatiemodel OKx. Termen uit de rest van de documentatie staan nog niet in deze lijst; de extractie in begrippen-extractie.json houdt bij hoeveel dat er zijn.

## Stand van zaken

| | |
|---|---|
| Begrippen in deze versie | 69 |
| Met definitie en vindplaats | 17 |
| Nog te definieren | 52 |
| Waarvan met alleen een doelomschrijving | 10 |
| Kandidaat-begrippen uit meta en Public buiten deze versie | 776 |

## Begrippen

De begrippen delen de keten in. Ze zijn niveau 1 in het [Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/); de objecttypen eronder zijn niveau 2.

| Begrip | Definitie | Vindplaats |
|---|---|---|
| `Onderwijsresultaat` | Wat een student op een verbintenis heeft behaald, uitgedrukt in leeruitkomsten | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijskundig kader instelling` | De vertaling van het kwalificatiekader naar beoogde leeruitkomsten, gemaakt door de instelling zelf | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijsaanbod` | Een specificatie die is ingepland: een periode, een capaciteit en waar van toepassing concrete plek, docent en tijd | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijsverbintenis` | De relatie tussen een student en een aanbod, van aangemeld tot afgerond | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |
| `Resultaatstructuur` | De samenstelling en weging waarmee losse resultaten optellen tot een uitspraak over de beoogde leeruitkomsten, en daarmee over een kwalificatie of certificaat | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |
| `Onderwijsspecificatie` | Het herbruikbare ontwerp van een onderwijsonderdeel, los van wanneer het draait en wie eraan meedoet | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |
| `Kwalificatiekader mbo` | Het geheel van landelijk vastgestelde eisen waaraan een opleiding moet voldoen. Vastgesteld en beheerd buiten OKx | [informatiemodel.md](../../../../architecture/model/informatiemodel/informatiemodel.md#begrippen) |

## Objecttypen met een definitie

| Objecttype | Begrip | Definitie | Vindplaats |
|---|---|---|---|
| `Examengelegenheid` | Onderwijsaanbod | Het georganiseerde aanbod van een examenmoment: planning, locatie, surveillant-capaciteit en kandidaten, gekoppeld aan precies één `Examenspecificatie`. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Toetsgelegenheid` | Onderwijsaanbod | Het georganiseerde aanbod van een toetsmoment: wanneer, waar en onder welke condities een toetsonderdeel wordt afgenomen, gekoppeld aan precies één `Toetsonderdeel-specificatie`. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Leeruitkomst` | Onderwijskundig kader instelling | Een concreet en observeerbaar resultaat van leren, dat beschrijft wat een student na het doorlopen van één of meer leertaken weet, begrijpt of kan toepassen, en dat als voorwaarde geldt om een opleidingsonderdeel succesvol af te ronden — de vertaling van leertaken in een breakdown door onderwijskundigen. Bij voorkeur uitgedrukt in een sectoroverstijgende, gestandaardiseerde skillstaxonomie (zoals CompetentNL), in dimensies kennis, inzicht en vaardigheden; zie hoofdstuk 4. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Leeronderdeel specificatie` | Onderwijsspecificatie | De specificatie van het deel van de onderwijseenheid (onder meer bestaande uit lesstof en opdrachten) waarin de student competenties kan verwerven. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Les specificatie` | Onderwijsspecificatie | De specificatie van het kleinste geplande leermoment binnen een leeronderdeel: welke lesinhoud, leeractiviteit of toetsactiviteit in dat moment wordt aangeboden. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Onderwijseenheid specificatie` | Onderwijsspecificatie | De specificatie van de fundamentele eenheid waarin onderwijs wordt ontworpen en aangeboden, in de vorm van een samenhangend stelsel van één of meer (beoogde) leeruitkomsten, leeronderdelen en/of toetsonderdelen. (NB: Leeruitkomsten omvat o.a. kennis, inzicht en vaardigheden.) | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Opleidingsprogramma specificatie` | Onderwijsspecificatie | Een samenhangende verzameling van één of meer (deel)programma's, onderwijseenheden, of leeruitkomsten die kunnen leiden tot een kwalificatie. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Toetsonderdeel specificatie` | Onderwijsspecificatie | De specificatie van het deel van de onderwijseenheid (bestaand uit een onderzoek naar kennis, inzicht, houding en vaardigheden van de student), waarmee wordt vastgesteld over welke competenties de student beschikt, leidend tot een formatieve of summatieve beoordeling. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Examengelegenheid verbintenis` | Onderwijsverbintenis | De relatie tussen kandidaat en `Examengelegenheid`: inschrijving op en deelname aan de examenafname. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |
| `Toetsgelegenheid verbintenis` | Onderwijsverbintenis | De relatie tussen een persoon en een `Toetsgelegenheid`: de feitelijke (voorbereide of lopende) deelname aan dat toetsmoment. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces) |

## Objecttypen met alleen een doelomschrijving

Hier staat wel wat het objecttype doet, maar niet wat het is. Een doelomschrijving is geen definitie; deze rijen wachten nog op een.

| Objecttype | Begrip | Doelomschrijving | Vindplaats |
|---|---|---|---|
| `Kerntaak` | Kwalificatiekader mbo | Een samenhangend geheel van werkprocessen waarmee een beroep wordt uitgeoefend en waarvan de beheersing het functioneren in een beroep mede bepaalt. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Kwalificatie` | Kwalificatiekader mbo | Beschrijft een kwalificatie als afgerond geheel binnen één kwalificatiedossier. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Kwalificatie dossier` | Kwalificatiekader mbo | Legt het sectorale referentiekader vast waartegen instellingen opleiden en examineren. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Werkproces` | Kwalificatiekader mbo | Een samenhangend geheel van taken die uitgevoerd worden binnen een beroep en die leiden tot een herkenbaar resultaat, waarmee de beginnend beroepsbeoefenaar aantoont het beroep te beheersen. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Leergelegenheid` | Onderwijsaanbod | Groepeert lessen tot een planbaar/geroosterd leermoment. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Lesgelegenheid` | Onderwijsaanbod | Concretiseert één les in tijd, ruimte en bemanning. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Onderwijseenheid aanbod` | Onderwijsaanbod | Plant en capaciteert een onderwijseenheid in de tijd. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Opleidingsprogramma aanbod` | Onderwijsaanbod | Biedt een concreet programma-instantie aan (cohort, variant). | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Leergelegenheid verbintenis` | Onderwijsverbintenis | Koppelt persoon aan leergelegenheid (incl. docent). | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |
| `Lesgelegenheid verbintenis` | Onderwijsverbintenis | Koppelt persoon aan concrete lesuitvoering. | [leerroute-uitwerking-lr1.md](../../../../architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht) |

## Objecttypen zonder bron

Deze objecttypen staan op de plaat maar zijn nergens beschreven. Elk is een gat, geen aanname.

| Begrip | Objecttypen |
|---|---|
| Buiten de kolommen | `Examenplan`, `Medewerker`, `Persoon`, `Plaatsingsgroep`, `Student`, `Verzoek tot Aanbod / Intekening op specificatie`, `Waarde document (diploma / certificaat)` |
| Onderwijsaanbod | `Keuzedeelaanbod`, `Opleidingaanbod`, `Opleidingsaanbod van Instelling` |
| Onderwijskundig kader instelling | `Competenties / Skills`, `Inzicht`, `Kennis`, `Vaardigheid` |
| Onderwijsresultaat | `Aanwezigheid`, `Examengelegenheid resultaat`, `Keuzedeel resultaat`, `Leergelegenheid resultaat`, `Lesgelegenheid resultaat`, `Onderwijseenheid resultaat`, `Opleiding aanbod resultaat`, `Opleidingsprogramma resultaat`, `Toetsgelegenheid resultaat` |
| Onderwijsspecificatie | `Examenonderdeelspecificatie`, `Keuzedeel`, `Keuzedeelruimte`, `Opleiding specificatie`, `Student keuze regelset` |
| Onderwijsverbintenis | `Keuzedeel aanbod verbintenis`, `Onderwijseenheid aanbod verbintenis`, `Opleiding aanbod  verbintenis`, `Opleidingsprogramma aanbod verbintenis` |
| Resultaatstructuur | `Examenonderdeel weging`, `Formatief resultaat`, `Formatieve beoordeling`, `Formatieve resultaat structuur`, `Persoonlijke ontwikkeling`, `Summatief Afrondingscriterium`, `Summatief resultaat`, `Summatieve beoordeling`, `Summatieve resultaat structuur`, `Toetsonderdeel weging` |

## Verwijzingen naar MORA

Deze verwijzingen staan in de bron waaruit deze lijst is opgebouwd. Ze zijn nog niet geopend en dus nog geen bewijs van herkomst.

| Objecttype | Verwijzing | Stand |
|---|---|---|
| `Kerntaak` | [mora.mbodigitaal.nl - Kerntaak](https://mora.mbodigitaal.nl/index.php/Id-99ef9489-49b3-4a3b-7a89-08ae36a3255e) | nog niet geopend |
| `Kwalificatie` | [mora.mbodigitaal.nl - Kwalificatie](https://mora.mbodigitaal.nl/index.php/Id-f54b73a9-9562-2b28-deca-724e992bbcdb) | nog niet geopend |
| `Kwalificatie dossier` | [mora.mbodigitaal.nl - Kwalificatiedossier](https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762) | nog niet geopend |
| `Werkproces` | [mora.mbodigitaal.nl - Werkproces](https://mora.mbodigitaal.nl/index.php/Id-9cf4d404-b06c-473f-57d9-3945af33cfa8) | nog niet geopend |

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
