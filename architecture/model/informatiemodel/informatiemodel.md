# Informatiemodel OKx

## Context

OKx maakt gestandaardiseerde koppelvlakken voor onderwijslogistiek. Die koppelvlakken wisselen informatie uit, en die informatie moet aan beide kanten hetzelfde betekenen.

## Inleiding

Dit document zet het informatiemodel van OKx uiteen: welke objecttypen de keten van kwalificatiekader tot resultaat kent, hoe ze samenhangen, en welke begrippen die keten indelen. De plaat is de weergave, dit document geeft de conventies en de keuzes erachter. Versie v0.2, concept; ter bekrachtiging door de kerngroep techniek.

## Doel

Het uiteenzetten van de informatiearchitectuur van de belangrijkste informatieobjecten binnen het OKx-ecosysteem, als gedeelde grondslag voor de koppelvlakspecificaties. Na bekrachtiging is het model de gedeelde grondslag waaraan de datamodelschema's en de koppelvlakspecificatie zich houden.

## Scope

De scope volgt de beschouwingsniveaus van het [Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/mim/).

| | Niveau | Waar het staat |
|---|---|---|
| Uitsnede | [1, model van begrippen](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-1-model-van-begrippen) | Het [begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) en de [begrippenlijst](../../docs/specificatie/begrippen/begrippenlijst.md). De plaat toont daarvan een uitsnede: de zeven begrippenfamilies als kolommen |
| Dit document | [2, conceptueel informatiemodel](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-2-conceptueel-informatiemodel) | De objecttypen en hun relaties, binnen een instelling: de plaat. Attribuutsoorten en multipliciteit horen ook bij dit niveau en staan er nog niet; de plaat draagt één cardinaliteit (`Minimaal 1`) en het begrippenkader de normatieve cardinaliteiten |
| Buiten scope | [3, logisch informatiemodel](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-3-logisch-informatie-of-gegevensmodel) | De entiteiten met hun velden en relaties per begrippenfamilie, in een eigen gegevensmodeldocument |
| Buiten scope | [4, technisch datamodel](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-4-fysiek-of-technisch-gegevens-of-datamodel) | De JSON Schema's en de endpoints in de koppelvlakspecificatie, in een eigen gegevensmodeldocument |

Verder buiten scope: applicatiecomponenten, techniekkeuzes en federatie tussen instellingen. Welke component welk objecttype bezit staat in [uitgangspunt U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap) van de koppelvlakspecificatie. Een conceptueel informatiemodel is volgens MIM onafhankelijk van standaarden voor gegevensuitwisseling; de verhouding tot de Open Education API (OEAPI) staat daarom in een [apart document](informatiemodel-oeapi-mapping.md).

![Informatiemodel OKx, versie v0.2 van 19 oktober 2026](<OKx informatiemodel v0.2.jpg>)

## Lezers en detailniveau

| | |
|---|---|
| **Voor wie** | Kerngroep techniek, implementerende partijen, informatiemanagers en enterprise-architecten van instellingen |
| **Detailniveau** | MIM-niveau 2: objecttypen en hun relaties, met de begrippenfamilies als indeling. Geen attributen en geen datatypes |

## Begrippenfamilies

De kolommen op de plaat zijn de begrippenfamilies waarin OKx de keten indeelt. Ze zijn een uitsnede van het model van begrippen (MIM-niveau 1); de objecttypen binnen de kolommen zijn het conceptuele informatiemodel (niveau 2). Het volledige model van begrippen staat in het [begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) en de [begrippenlijst](../../docs/specificatie/begrippen/begrippenlijst.md); daar staat per begrip de definitie met bron.

Dit model volgt het begrippenkader op en wijzigt het op twee punten. De familie *beoogde leeruitkomst* heet hier `Onderwijskundig kader instelling`: de invulling door de instelling van de beoogde leeruitkomsten uit het kwalificatiekader. En `Resultaatstructuur` is een zevende familie, omdat de samenstelling en weging van resultaten een eigen objecttype vragen dat in geen van de zes families past.

| Begrip | Wat het is | Beantwoordt de vraag |
|---|---|---|
| Kwalificatiekader | Het geheel van landelijk vastgestelde eisen waaraan een opleiding moet voldoen, voor het middelbaar en het hoger onderwijs. Vastgesteld en beheerd buiten OKx | Wat is normatief geldig |
| Onderwijskundig kader instelling | De invulling door de instelling van de beoogde leeruitkomsten uit het kwalificatiekader | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Het herbruikbare ontwerp van een onderwijsonderdeel, los van wanneer het draait en wie eraan meedoet | Wat wordt georganiseerd |
| Onderwijsaanbod | Een specificatie die is ingepland: een periode, een capaciteit en waar van toepassing concrete plek, docent en tijd | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | Een afspraak voor het gaan volgen, volgen en hebben gevolgd van onderwijs | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Vastgelegde en geformaliseerde beoordeling op basis van een of meer leerresultaten | Wat is er behaald op een verbintenis |
| Resultaatstructuur | De samenstelling en weging waarmee losse resultaten optellen tot een uitspraak over de beoogde leeruitkomsten, en daarmee over een kwalificatie of certificaat | Hoe telt dat op tot bewijs voor een leeruitkomst |

Objecttypen buiten de kolommen raken de hele keten, en staan er vaak omdat zij twee families verbinden: `Persoon` met de rollen `Student` en `Medewerker`, `Plaatsingsgroep` en `Cohort / periode`, het `Verzoek tot Aanbod / Intekening op specificatie` als brug van specificatie naar aanbod (`Input voor`, `Leidt tot`), de `Aanmelding` op dat aanbod, `Waarde document (diploma / certificaat)`, en aan de uitvoerende kant `Organisatie-eenheid`, `Expertise of functieprofiel` en `Onderwijslocatie vlekkenplan`. `Examenplan` en `OER` staan buiten scope.

## Notatie

**Kleur.** Geel is het OKx-referentiekader. Het sluit aan op de mbo-referentiearchitectuur (MORA) en, via het lopende initiatief klus 53 (Alignment MORA en HORA, MBO Digitaal), op de referentiearchitectuur van het hoger onderwijs (HORA). Grijs staat als erkend begrip in het model maar valt buiten de scope van OKx: `Les specificatie`, `Leergelegenheid resultaat`, `Aanwezigheid`, het examenplan en de `OER` als document, en de onderwijskundige begrippen `Competenties / Skills`, `Kennis`, `Vaardigheid` en `Inzicht`. Blauw is OEAPI v6 en komt alleen voor op de [mapping](informatiemodel-oeapi-mapping.md).

**Relatiesoorten**, in ArchiMate-notatie.

| | Relatie | Betekenis in dit model |
|---|---|---|
| `──▷` | Specialisatie (specialization) | Een bijzonder geval van het algemenere type, met dezelfde informatiestructuur |
| `◇──` | Aggregatie (aggregation) | Het geheel bestaat uit deze delen; een deel kan ook zonder het geheel bestaan |
| `───` | Associatie (association) | Inhoudelijke samenhang zonder eigenaarschap of samenstelling |
| `╌╌>` | Toegang (access) | `Persoon` gebruikt of wijzigt dit objecttype: het verzoek, de aanmelding en de resultaten; `Student` het cohort. Aanbod en verbintenis bereikt een persoon via de aanmelding |

Waar de betekenis niet uit de twee objecttypen volgt, draagt de relatie een label. Op associaties staan `Wordt vertaald naar`, `voorwaarde op`, `Input voor`, `Leidt tot`, `Op basis van`, `middels`, `conform`, `kent`, `met`, `Worden gegroepeerd via`, `Groepeert Studenten op toepasbare`, `wordt uitgewerkt in`, `staat beschreven in` en de cardinaliteit `Minimaal 1`; op aggregaties `bestaat uit` en `bevat`; op de specialisatie van `Aanmelding` naar `Inschrijving` staat `wordt`. De labels staan op de plaat.

## Ontwerpkeuzes

Elke keuze noemt zijn bron; staat er *voorstel*, dan is de keuze in dit model gemaakt en wacht hij op bekrachtiging.

1. **De leeruitkomst is de sleutel die specificaties en resultaatstructuur verbindt.** Zeven specificatietypen wijzen rechtstreeks naar leeruitkomsten, `Keuzedeel` en `Keuzedeelruimte` doen dat via specialisatie, en de summatieve resultaatstructuur wijst er ook naar. Een leeruitkomst kan subleeruitkomsten bevatten. Bron: [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md).
2. **Het kwalificatiekader wordt vertaald naar leeruitkomsten, niet gespecialiseerd.** Kwalificatiedossier, kwalificatie, kerntaak en werkproces stellen vast wat normatief geldig is. Een leeruitkomst is de invulling door de instelling van wat het kwalificatiekader beoogt: wat een student moet kennen en kunnen, zo geformuleerd dat specificaties ernaar kunnen verwijzen en dat behaalde toets- en examenresultaten er het bewijs voor leveren. Een leeruitkomst is dus geen bijzonder geval van een werkproces; een instelling die geen eigen leeruitkomsten formuleert kan de vertaling een op een maken. Voorstel.
3. **Randvoorwaarde: uitwisseling tussen instellingen vraagt landelijk gestandaardiseerde leeruitkomsten.** Zonder een landelijk beheerde set blijft een leeruitkomst instellingseigen en is aanbod van verschillende instellingen niet te vergelijken. Dit model gaat van die set uit; de onderwijskundige vrijheid van de instelling zit in de specificaties waarmee zij de leeruitkomsten bereikt. Randvoorwaarde voor een latere fase; federatie valt buiten dit model.
4. **Het niveau waarop iets gespecificeerd wordt ligt niet vast.** Een `Onderwijseenheid specificatie` kan op kerntaakniveau liggen of op een ander niveau dat de instelling kiest. De koppeling loopt via de leeruitkomst, en daarom is het niveau geen eigenschap van de objecttypen. Voorstel.
5. **Een specificatie kan zelfstandig bestaan.** Specificaties onder de `Opleiding specificatie` kunnen onderdeel zijn van een bovenliggende specificatie, maar hoeven dat niet. Een `Opleidingsprogramma specificatie` zonder bovenliggende `Opleiding specificatie` is geldig. Voorstel.
6. **De student kiest uit specificaties, de voorwaarde staat in behaalde leeruitkomsten.** De `Student keuze regelset` wijst naar de specificatietypen waaruit gekozen kan worden. Een voorwaarde vooraf in die regelset wordt uitgedrukt in behaalde leeruitkomsten en niet in doorlopen specificaties: deelname aan Ruimtelijk inzicht vereist dat de leeruitkomst van Wiskunde 1 behaald is, ongeacht via welke specificatie. Bron: [R7 in de keuze-requirements](../../docs/specificatie/student-keuze/keuze-requirements.md) en [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md).
7. **Resultaten hangen aan verbintenissen, niet rechtstreeks aan leeruitkomsten.** Een student toont een leeruitkomst aan door toetsen en examens af te ronden; die resultaten ontstaan op de verbintenis, via specificatie, aanbod en verbintenis. De summatieve resultaatstructuur wijst naar de leeruitkomsten en zegt welke resultaten samen het bewijs vormen, ook voor een leeruitkomstenregister, Edubadges of een eduwallet. Daarom heeft geen enkel resultaattype een eigen relatie met `Leeruitkomst`. Een resultaat ontstaat op elk niveau waarop een verbintenis bestaat: opleiding, opleidingsprogramma, onderwijseenheid, leergelegenheid, lesgelegenheid, toetsgelegenheid en examengelegenheid. `Leergelegenheid resultaat` en `Aanwezigheid` staan buiten scope van OKx; zij bestaan in het model omdat de keten ze kent. Voorstel; verfijnt [ADR 0022](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md), dat "behaald op leeruitkomsten" zegt zonder de weg via de structuur te noemen.
8. **De inhoud van een les valt buiten de uitwisseling, de les in het rooster niet.** `Les specificatie` blijft erbuiten: wat er in een les gebeurt is onderwijskundige vrijheid van de instelling. `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan binnen scope, want de les in het rooster, de deelname eraan en het resultaat erop zijn logistiek en worden uitgewisseld. Voorstel.
9. **Een examenonderdeel is een specialisatie van een toetsonderdeel, en formatief of summatief is een kenmerk van het resultaat.** Toetsonderdeel en examenonderdeel delen dezelfde informatiestructuur; hun totstandkoming verschilt: een examenonderdeel stelt de examencommissie vast, een toetsonderdeel volgt instellingsbeleid. De specificatie draagt in haar definitie of zij formatief of summatief is, en `Formatief resultaat` en `Summatief resultaat` hangen onder het toets- respectievelijk examenresultaat. Er zijn dus geen twee takken door het model. De summatieve resultaatstructuur is samengesteld uit toetsonderdelen, zodat een instelling een formatief toetsonderdeel summatief kan laten meetellen; vanaf dat moment volgt het de examenketen. De term examenonderdeel komt uit het mbo; het hoger onderwijs gebruikt haar anders, en het model legt daarom het onderscheid in de totstandkoming vast en niet in het woord. Voorstel.
10. **OKx wisselt de summatieve resultaatstructuur uit, niet het examenplan.** De `Summatieve resultaat structuur` draagt de examenonderdelen met hun wegingen en het afrondingscriterium dat de zak-slaagregeling draagt. Zij is onderdeel van een examenplan en verwijst daarnaar; het examenplan zelf, het document dat de examencommissie vaststelt, valt buiten de uitwisseling, net als de `OER` (onderwijs- en examenregeling) die het examenplan bevat en de kwalificatie beschrijft. Bron: MORA onderscheidt OER, examenplan en summatieve resultaatstructuur op dezelfde manier.
11. **Een leeruitkomst is een geformuleerde competentie, en draagt als enige een niveau.** `Leeruitkomst` specialiseert `Competenties / Skills`: dezelfde informatiestructuur, uitgedrukt op het niveau waarop de instelling formuleert. De onderliggende begrippen kennis, vaardigheid en inzicht staan in het model en vallen buiten de uitwisseling. Het niveau is NLQF, met EQF als Europese equivalent: mbo 1 tot 4 en hoger onderwijs 5 tot 8 op dezelfde lat. Kerntaak en werkproces zijn een vindplaats in het mbo-dossier en geen niveau. Een vaardigheid eronder draagt geen niveau; de [metadateringsmethodologie van CompetentNL](https://publications.tno.nl/publication/34645225/UfmHs0kr/competentNL-2025-metadatering.pdf) stelt dat het gevraagde niveau per context verschilt. Het objecttype dat die lat draagt staat nog niet in het model; een objecttype dat die lat draagt is in voorbereiding. Voorstel.
12. **Keuzedeel en minor zijn bijzondere gevallen van een opleidingsprogramma, en een ruimte is de oningevulde variant ervan.** Een keuzedeelruimte is onderwijskundig vrijgemaakte ruimte van een bepaalde omvang waarin een student een keuzedeel kiest; een minorruimte doet hetzelfde voor het hoger onderwijs. `Keuzedeel`, `Keuzedeelruimte`, `Minor` en `Minor ruimte` specialiseren alle `Opleidingsprogramma specificatie`, en de minor loopt door over aanbod, verbintenis en resultaat. Het keuzedeel is landelijk vastgesteld en valt daarmee ook onder het kwalificatiekader: `Kwalificatie dossier`, `Kwalificatie` en `Keuzedeel` specialiseren alle `Kwalificatiestructuur SBB`, het objecttype dat vastlegt wat S-BB landelijk vaststelt. Het keuzedeel blijft in de kolom onderwijsspecificatie staan en draagt de K-code als verwijzing naar het landelijke keuzedeel.
13. **Intekenen, aanmelden en inschrijven zijn drie stappen.** Het `Verzoek tot Aanbod / Intekening op specificatie` is een verzoek om aanbod te maken voor een specificatie. Het heeft specificaties als input en leidt tot aanbod; aanmelden gebeurt daarna op dat aanbod en inschrijven is de verbintenis. De `Aanmelding` gaat `Op basis van` een aanbod, in elke fase waarin dat aanbod zich bevindt, loopt `middels` een verbintenis en `wordt` een `Inschrijving`: de overeenkomst tussen instelling en student, die bij het studentinformatiesysteem blijft. Bron: de afstemming van 14 september 2026 met een planner en een instelling; aanbod rijpt van intentie via grofmazig gepland naar geroosterd, en intekenen kan op de specificatie en op aanbod in elke fase. Of die fasering een toestand op het aanbod is of eigen objecttypen vraagt, is open.
14. **Student en medewerker zijn rollen van een persoon.** `Student` en `Medewerker` specialiseren `Persoon`; een persoon kan beide tegelijk zijn. Toegang tot de objecttypen loopt via `Persoon`. Voorstel.
15. **Een verbintenis loopt bij voorkeur via een groep.** `Plaatsingsgroep` maakt regulier onderwijs makkelijker te plannen en te roosteren en geldt voor elk verbintenistype. Het model sluit individuele verbintenissen niet uit. Voorstel.
16. **Een specificatie draagt de wettelijke geldigheid, geen planning.** Een specificatie is los van wanneer het onderwijs draait, maar niet los van de tijd: het kwalificatiekader waarop zij is ontworpen bepaalt vanaf wanneer zij geldt, tot wanneer erop gediplomeerd of gecertificeerd mag worden en wanneer het aanbieden stopt, bijvoorbeeld omdat het crebo erachter verjaart. Die geldigheid ligt vast op de specificatie; wanneer een aanbod daadwerkelijk draait staat op het aanbod. Voorstel.
17. **Het cohort hangt aan de inschrijving en bepaalt welke resultaatstructuur van toepassing is.** `Cohort / periode` groepeert studenten die onder dezelfde onderwijs- en examenregeling vallen (MORA). Het hangt aan de `Inschrijving` en niet aan `Student`, want een persoon kan in meer dan een opleiding zitten en daarmee in meer dan een cohort: het cohort is een eigenschap van de deelname. Het cohort groepeert studenten op de `Summatieve resultaat structuur` die op hen van toepassing is en wordt uitgewerkt in de `OER`. Daarmee bepaalt het ook wie samen onderwijs kan volgen, want wie onder een andere structuur valt moet andere dingen doen. Voorstel.
18. **Waar onderwijs plaatsvindt en wie het uitvoert zijn eigen objecttypen.** `Onderwijsvorm` legt per leeronderdeel vast hoe het onderwijs gegeven wordt; daaruit volgt `Onderwijslocatie type`, het soort ruimte dat die vorm vraagt. `Onderwijslocatie` hangt aan het aanbod, want pas bij het plannen ligt de plek vast. `Organisatie-eenheid` voert de onderwijsspecificatie uit. Of zij als keuzebepalende factor in een keuzeregelset mogen staan, en op welk moment in het planproces de locatie vastligt, is open. Voorstel.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Mapping naar OEAPI v6](informatiemodel-oeapi-mapping.md) | Dezelfde objecttypen met de Open Education API ernaast |
| [Begrippenlijst OKx](../../docs/specificatie/begrippen/begrippenlijst.md) | Geeft per begrip de definitie, de bron en de mapping naar MORA en het Kernmodel Onderwijsinformatie |
| [Begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) | Werkt de begrippen, hun subtypen en de normatieve cardinaliteiten verder uit |
| Logisch gegevensmodel | Werkt deze objecttypen uit tot entiteiten met velden, op MIM-niveau 3; in uitwerking |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Welke applicatiedienst welk objecttype over welk endpoint uitwisselt |
| [`informatiemodel.json`](informatiemodel.json) | Dit model machineleesbaar, gegenereerd uit `model.archimate` |
