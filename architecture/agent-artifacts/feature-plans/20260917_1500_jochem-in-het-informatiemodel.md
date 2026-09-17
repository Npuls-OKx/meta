# Jochem in het informatiemodel: featureplan en implementatieplan

Relateert aan: [Public #106](https://github.com/Npuls-OKx/Public/issues/106) (het deliverable), #237 (analyse, mock-up en PoC), #234 en #235 (open modelvragen), [Public #105](https://github.com/Npuls-OKx/Public/issues/105) en [Public #107](https://github.com/Npuls-OKx/Public/issues/107). Bronnen: de mock-up `research/20260916_1300_voorbeelduitwerking-leerroute-1/mockup-eindproduct.html` en de PoC-renderers in `poc/` op dezelfde plek. Concept ter goedkeuring; na akkoord worden de werkpakketten sub-issues onder Public #106.

## 1. Doel en toets

Op 30 september 2026 toont OKx de kerngroep techniek de opleiding van Jochem (kaderscenario leerroute 1, Apothekersassistent, cohort 2026) stap voor stap in het informatiemodel, op conceptueel niveau (MIM 1 en 2), zodat elk lid het naast het eigen model kan leggen en kan zeggen wat bij hem anders heet of anders hangt.

Het doel is gehaald als op 30 september:

1. de fasen 2, 3 en 4 van de instellingsreis volledig als regels op tafel liggen (ontstaat en stroomt), de andere fasen als samenvatting in chips;
2. elk objecttype van de plaat dat in die fasen ontstaat één instantie voor Jochem heeft, met aannames gemarkeerd;
3. de kerngroep de bijlage vóór de sessie heeft ontvangen (uiterlijk 25 september bij de agenda) en er niet meer dan zes pagina's voor hoeft te lezen;
4. de zeven vragen aan de kerngroep op één pagina staan, en het antwoord op de vraag "wat heet bij u anders" per regel kan worden genoteerd.

Niet het doel: het volledige document voor alle acht fasen, een perfecte hoofdplaat-render, of besluiten over de open modelvragen. Dat volgt na de sessie.

## 2. Eisen en acceptatiecriteria

| Eis | Wat | Acceptatiecriterium |
|---|---|---|
| R1 Regeltabel als bron | Eén machineleesbaar bestand met per regel: fase, stap, soort (ontstaat of stroomt), wie, objecttype, instantie, relatie, aanname, bron | Het bestand valideert tegen een JSON-schema; elke objecttypenaam bestaat in `informatiemodel.json`; elk relatielabel bestaat op de plaat; elke stroomt-regel wijst naar een bestaande pijl van de hoofdplaat |
| R2 Dekking | Elk objecttype binnen scope dat in een fase ontstaat heeft daar één regel | De controle faalt met een lijst van ontbrekende objecttypen; voor 30 september is de lijst leeg voor fase 2 tot 4 |
| R3 Regelrenderer | Een script tekent elke regel als SVG in ArchiMate-vormtaal (kleur per laag, icoon per type, nesting bij "bestaat uit", gestippeld bij aanname), zonder externe fonts | Tests: één positief geval per regelsoort, faalgevallen (onbekend objecttype, leeg relatielabel, ontbrekende instantie); de SVG's renderen op GitHub in markdown |
| R4 Hoofdplaat-renderer | Een script rendert de view "OKx hoofdplaat v1.7" uit `model.archimate` (alleen lezen) als SVG: posities, knikpunten en namen zoals in Archi, ArchiMate-kleuren en -iconen, de informatieobjecten als label op de pijlen | De knikpunten volgen Archi's conventie (relatief aan het midden van bron en doel); geen naam valt weg; de render is door de modelleur naast de JPG gelegd en akkoord bevonden; tests voor de knikpuntvertaling en het inlezen van een view; export van `stromen.json` (bron, doel, informatieobject, pijlnummer) |
| R5 Documentgenerator | Een script bouwt `voorbeeld-leerroute-1-jochem.md` uit de regeltabel: leeswijzer met legenda, per fase chips en regels als SVG, een tabel per familie, één pagina vragen | `python3 scripts/validate-docs.py` groen; acht fasesecties aanwezig; elke SVG-verwijzing lost op; de familietabellen dekken alle objecttypen binnen scope (leeg gemarkeerd waar nog geen regel is) |
| R6 Publicatie | Het document en de SVG's landen in het pakket informatie- en gegevensmodellen in Public via het bestaande publiceerscript; meta blijft bron | Public-controles groen (`check-conventies.py`, `check-links.py`, `build-release.py --alleen-controle`); pull request in Public op draft tot na de sessie |
| R7 Bijlage kerngroep | Een deck van hoogstens zes inhoudelijke slides plus de regels van fase 2 tot 4, geëxporteerd als pdf, bij de agenda van 30 september | Uiterlijk 25 september verstuurd; het deck opent met wat de kerngroep wordt gevraagd (herken het, zeg wat anders heet) |
| R8 Vragenpagina | De zeven vragen uit het plan onder Public #106 op één pagina, met per vraag de consequentie voor het model | In het document en in het deck; geen besluit gevraagd, wel input |
| R9 Modelhuiswerk | In Archi: de leslaag (Les specificatie, Lesgelegenheid, Lesgelegenheid verbintenis, Lesgelegenheid resultaat) binnen scope, de informatieobjecten als naam op de flows van hoofdplaat v1.7, en de pijlnummers | `validate-archimate.py` groen; `informatiemodel.json` opnieuw gegenereerd toont de leslaag binnen scope; de labeltabel van de renderer vervalt zodra de flows namen dragen |
| R10 Reviews | Tester (eis voor eis), specialist (informatiearchitect, lid kerngroep techniek) en schrijfstijl in verse contexten vóór de pull request | Reviewrapporten in de PR-beschrijving als agent-rapport; hoogstens drie iteraties |

## 3. Features, in implementatievolgorde

### 1. Regeltabel, schema en dekkingscontrole (meta)

- **Wat:** het bronbestand `architecture/model/informatiemodel/voorbeeld-lr1-regels.json` met JSON-schema, en `scripts/controleer-voorbeeldregels.py` dat R1 en R2 afdwingt tegen `informatiemodel.json`, `begrippen.json` en `stromen.json`.
- **Hangt af van:** geen; werkt op de huidige `informatiemodel.json` (leslaag nog buiten scope, zie feature 8).
- **Levert op:** schema, leeg gevuld bestand met de acht fasen en hun stappen, controlescript met tests, README-regel in `architecture/model/README.md`.
- **Sluit uit:** de inhoud van de regels (feature 4) en het tekenen (feature 2).

### 2. Regelrenderer (meta)

- **Wat:** `poc/blok.py` wordt `scripts/teken-voorbeeldregels.py`: leest de regeltabel, schrijft per regel een SVG naar `architecture/model/informatiemodel/img/regels/`. Tekstbreedte per teken gekalibreerd op Arial, zodat namen niet in het icoon lopen.
- **Hangt af van:** feature 1 (het schema).
- **Levert op:** script, tests (positief per regelsoort, faalgevallen, randgeval lange naam), voorbeeld-SVG's.
- **Sluit uit:** de hoofdplaat (feature 3) en het document (feature 5).

### 3. Hoofdplaat-renderer herstellen (meta)

- **Wat:** `poc/hoofdplaat.py` wordt `scripts/teken-archimate-view.py`. Te herstellen: de knikpuntvertaling (Archi slaat een bendpoint op als offset ten opzichte van het midden van bron én doel; de PoC gebruikt alleen de bronoffset, waardoor pijlen scheef of recht lopen), tekst die wegvalt (regelafbreking en verticale uitlijning per elementtype), labels die over elementen vallen (plaatsing op het langste segment, met witte achtergrond), en de export van `stromen.json`.
- **Hangt af van:** geen; alleen-lezen op `model.archimate`.
- **Levert op:** script, tests (knikpuntvertaling met een bekend voorbeeld, view inlezen, geneste elementen, label uit flow-naam of tabel), render van v1.7 en v1.7 zonder context als SVG, `stromen.json`.
- **Sluit uit:** wijzigingen in het model (feature 8) en een generieke Archi-vervanger: alleen wat de hoofdplaat en de informatiemodelview nodig hebben.

### 4. Regels vullen: fase 2 tot 4, daarna 1 en 5 tot 8 (meta, met de modelleur)

- **Wat:** de regeltabel vullen uit het kaderscenario, scenario 1.1, de persona en de voorbeeldpayloads; één instantie per objecttype; waar de bronnen niets geven een aanname; per fase de stroomt-regels op de pijlen van de hoofdplaat.
- **Hangt af van:** feature 1; feature 3 voor de pijlnummers (tot die tijd de nummering uit de tabel in het projectoverzicht).
- **Levert op:** gevulde tabel voor fase 2 tot 4 (stopmoment met de modelleur na de eerste render van fase 2), daarna de overige fasen.
- **Sluit uit:** nieuwe objecttypen of relaties; wat op de plaat ontbreekt wordt een vraag, geen regel.

### 5. Documentgenerator en het document (meta)

- **Wat:** `scripts/genereer-voorbeeld-lr1.py` bouwt `architecture/model/informatiemodel/voorbeeld-leerroute-1-jochem.md`: leeswijzer met legenda en de plaat als beeld, per fase de chips en de regels, een tabel per familie, de vragenpagina.
- **Hangt af van:** features 1, 2 en 4.
- **Levert op:** script, tests (secties aanwezig, verwijzingen lossen op, familietabellen dekkend), het document.
- **Sluit uit:** payloads, diensten, berichtstromen; de koppeling naar laag 3 en 4 is één verwijzing in de leeswijzer.

### 6. Publicatie naar Public

- **Wat:** `scripts/publiceer-informatiemodel.py` levert het document en `img/regels/` mee aan `Informatie-en-gegevensmodellen/`, met de linktabel en de gepinde meta-commit; `release.json` krijgt de sectie.
- **Hangt af van:** feature 5.
- **Levert op:** uitgebreid publiceerscript met test, pull request in Public gestapeld op PR 104, op draft tot na 30 september.
- **Sluit uit:** wijzigingen aan de bestaande documenten in het pakket.

### 7. Bijlage en deck voor 30 september (meta)

- **Wat:** Slidev-deck `presentaties/src/260930_kerngroep_techniek_jochem.md`: de vraag aan de kerngroep, de legenda, fase 2 tot 4 als regels, de vragenpagina, het vervolg. Export pdf en pptx.
- **Hangt af van:** features 2, 4 en 5 voor fase 2 tot 4.
- **Levert op:** deck en exports, mailtekst voor de agenda.
- **Sluit uit:** het versioneringsdeel en de bouwblokken van Garik (eigen agenda-onderdeel).

### 8. Modelhuiswerk in Archi (modelleur)

- **Wat:** de leslaag binnen scope zetten, de informatieobjecten als naam op de flows van hoofdplaat v1.7, de pijlnummers vastleggen (tabel in het projectoverzicht of een nummering op v1.7), de plaatkoppen en de dubbele spatie in `Opleiding aanbod  verbintenis` opschonen.
- **Hangt af van:** geen; loopt parallel.
- **Levert op:** bijgewerkt `model.archimate` (alleen door de modelleur), `validate-archimate.py` groen, opnieuw gegenereerde `informatiemodel.json` en begrippenlijst.
- **Sluit uit:** de open modelvragen uit #234 en #235; die blijven vragen.

## 4. Dwarsdoorsnijdende aandachtspunten

- **Eén bron per laag.** De regeltabel verwijst naar bronnen en kopieert geen waarden uit de payloads; de plaat komt uit Archi; namen uit de begrippenlijst. In feature 1 en 3 verwerkt.
- **Tests volgens de testpersona.** `tests/test_<script>.py`, stdlib `unittest`, given-when-then, geen momentopnames van de repo-inhoud. In elke scriptfeature verwerkt.
- **Schrijfstijl.** Geen streepjes, geen nadruk-accenten, geen tweede persoon; de regels dragen zinnen uit het kaderscenario, niet uit het transcript. In feature 4 en 5 verwerkt.
- **Werkafspraken.** Eén issue, één branch, één pull request per feature; features 1 tot 7 onder een milestone die naar de requirementsboom herleidt (epic gezamenlijke taal en standaard).
- **Publieke repositories.** Geen namen of citaten van leveranciers in regels, README of deck.

## 5. Implementatieplan tot 30 september

| Wanneer | Wat | Wie | Stopmoment |
|---|---|---|---|
| 17 september | Dit plan tegengelezen (tester, projectmanager en testcoördinator, informatiearchitect en lid kerngroep techniek) en goedgekeurd; sub-issues aangemaakt | agent, modelleur | Akkoord op het plan |
| 18 september | Feature 1 (schema, lege tabel, controle) en feature 2 (renderer naar scripts, tests); start feature 8 | agent; modelleur | |
| 19 tot 22 september | Feature 3 (hoofdplaat herstel); feature 4 fase 2, eerste render | agent; modelleur toetst | Akkoord op fase 2 als vorm, en op de hoofdplaat-render naast de JPG |
| 22 tot 23 september | Feature 4 fase 3 en 4; feature 5 generator en document met stubs voor de andere fasen | agent | |
| 23 september | Reviews in verse contexten: tester, informatiearchitect, lid kerngroep techniek, schrijfstijl; iteratie | agent | |
| 24 september | Feature 6 (publicatie, draft PR in Public); feature 7 (deck en exports) | agent | Akkoord op document fase 2 tot 4 en op het deck |
| 25 september | Bijlage bij de agenda | modelleur | Verzonden |
| 30 september | Kerngroep techniek | | |
| 1 tot 3 oktober | Feature 4 fase 1 en 5 tot 8; bevindingen verwerkt; pull requests mergen | agent, modelleur | |

Capaciteit: de modelleur ongeveer een dagdeel per dag voor stopmomenten en feature 8; de rest is agentwerk in deze sessie. Bij uitloop valt eerst feature 3 terug (de JPG van de modelleur als plaat, labels alleen in de stroomt-regels), dan fase 4 (alleen fase 2 en 3 op tafel), nooit de vragenpagina of de bijlagedatum.

## 6. Risico's

| Risico | Gevolg | Maatregel |
|---|---|---|
| De knikpuntvertaling van Archi blijkt ingewikkelder (verschillende bendpoint-varianten per Archi-versie) | Feature 3 loopt uit | Twee dagen gebudgetteerd; terugval op de JPG; de stromen-export blijft (die heeft geen layout nodig) |
| Fase 3 raakt de open vragen over aanmelding, inschrijving en verbintenis (#234, ontwerpkeuze 13) | Discussie in plaats van herkenning | Eén instantie kiezen, aanname markeren, de vraag op de vragenpagina; niet in de regel zelf |
| Het modelhuiswerk (leslaag, flow-namen) is niet op tijd | Leslaag grijs op de kaart; labeltabel blijft | De renderer werkt met en zonder flow-namen; de leslaag krijgt regels met de markering "buiten scope tot modelronde" |
| De kerngroep leest de bijlage niet | Sessie zonder herkenning | Bijlage hoogstens zes pagina's, opent met de vraag; de regels zijn plaatjes, geen tekst |
| Het document groeit naar de omvang van de leerroute-uitwerking | Niemand leest het | Chips per fase, regels als beeld, één zin per regel; de familietabellen als bijlage |

## 7. Sub-issues onder Public #106 (concept, na akkoord aan te maken)

| Nr | Titel | Repository | Feature | Taak in één zin |
|---|---|---|---|---|
| 1 | Regeltabel en dekkingscontrole voor de voorbeelduitwerking | meta | 1 | Schema en bronbestand met de acht fasen, controle op objecttypen, relatielabels en pijlen, met tests |
| 2 | Regelrenderer: van regel naar SVG in ArchiMate-vormtaal | meta | 2 | PoC naar `scripts/`, tekstbreedte kalibreren, tests, voorbeeld-SVG's |
| 3 | Hoofdplaat-renderer: knikpunten, namen en labels herstellen | meta | 3 | Archi-view alleen-lezen naar SVG die naast de JPG standhoudt; export `stromen.json`; tests |
| 4 | Regels vullen voor fase 2 tot 4 (Jochems eerste periode) | meta | 4 | Ontstaat- en stroomt-regels uit kaderscenario, scenario 1.1, persona en payloads; aannames gemarkeerd; stopmoment na fase 2 |
| 5 | Documentgenerator en `voorbeeld-leerroute-1-jochem.md` | meta | 5 | Leeswijzer, fasen met chips en regels, familietabellen, vragenpagina; tests; validate-docs groen |
| 6 | Publicatie van de voorbeelduitwerking naar het pakket | Public | 6 | Publiceerscript uitbreiden, release.json, draft PR gestapeld op PR 104, Public-controles groen |
| 7 | Bijlage en deck kerngroep techniek 30 september | meta | 7 | Deck met de vraag, legenda, fase 2 tot 4 en de vragenpagina; pdf en pptx; bij de agenda op 25 september |
| 8 | Modelhuiswerk: leslaag binnen scope, flow-namen en pijlnummers op hoofdplaat v1.7 | meta | 8 | Door de modelleur in Archi; validate-archimate groen; informatiemodel.json en begrippenlijst opnieuw gegenereerd |
| 9 | Regels vullen voor fase 1 en 5 tot 8 | meta | 4 | Na 30 september, met de bevindingen van de kerngroep |

Sub-issues in meta worden via de GitHub-sub-issue-koppeling aan Public #106 gehangen; lukt dat niet over repositories heen, dan met een takenlijst in het issue.

## Open voor vervolg

- Pijlnummers: de tabel in het projectoverzicht (v20260317, 1 tot 17) of een nummering op v1.7; keuze van de modelleur bij feature 8.
- Sub-issues over twee repositories: te toetsen bij het aanmaken.
- Het cohortobject: één instantie "2026" in de regels; de vraag of het een sleutel of een object is blijft op de vragenpagina.
