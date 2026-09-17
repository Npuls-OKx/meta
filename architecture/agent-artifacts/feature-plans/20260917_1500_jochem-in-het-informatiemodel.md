# Jochem in het informatiemodel: featureplan en implementatieplan

Relateert aan: [Public #106](https://github.com/Npuls-OKx/Public/issues/106) (het deliverable), #237 (analyse, mock-up, PoC en de tegenlezingen op dit plan), #234 en #235 (open modelvragen), [Public #105](https://github.com/Npuls-OKx/Public/issues/105) en [Public #107](https://github.com/Npuls-OKx/Public/issues/107). Bronnen: de mock-up `research/20260916_1300_voorbeelduitwerking-leerroute-1/mockup-eindproduct.html` (versie 4), de PoC-renderers in `poc/`, en de drie tegenlezingen op versie 1 van dit plan in dezelfde map (`tegenlezing-plan-tester.md`, `tegenlezing-plan-projectmanager.md`, `tegenlezing-plan-informatiearchitect-kerngroep.md`). Versie 2, 17 september 2026, na verwerking van die tegenlezingen; ter goedkeuring door de modelleur. Na akkoord worden de werkpakketten sub-issues onder Public #106.

## 1. Doel en toets

Op woensdag 30 september 2026 toont OKx de kerngroep techniek de opleiding van Jochem (kaderscenario leerroute 1, Apothekersassistent, cohort 2026) stap voor stap in het informatiemodel, op conceptueel niveau (MIM 1 en 2), zodat elk lid het naast het eigen model kan leggen en per regel kan zeggen: herken ik dit, heet het bij mij anders, hangt het bij mij anders, of ontbreekt het.

Het doel is gehaald als:

1. de fasen 2, 3 en 4 van de instellingsreis als regels op tafel liggen (ontstaat en stroomt), de andere fasen als chips met de verwachte objecttypen en de zin "regels volgen na 30 september";
2. elk objecttype binnen scope dat in fase 2 tot 4 voor het eerst verschijnt één ontstaat-regel heeft, met aannames gemarkeerd en de plaatnaam letterlijk;
3. de bijlage van zes pagina's uiterlijk vrijdag 25 september bij de agenda zit, en het deck dezelfde zes pagina's is;
4. de vragenpagina hoogstens zeven vragen draagt die de regels van fase 2 tot 4 zelf oproepen, met een antwoordvorm per regel (invulblad) en per objecttype (kolommen "heet bij u" en "hangt bij u onder");
5. de uitkomst van de sessie binnen twee werkdagen als comment onder Public #106 staat: per regel per aanwezig lid een van de vier antwoorden.

Niet het doel: alle acht fasen, een perfecte hoofdplaat-render, publicatie in Public vóór de sessie, of besluiten over de open modelvragen. Dat volgt na 30 september.

## 2. Vaste woorden en vaste keuzes

Vier termen, overal gelijk in plan, schema, leeswijzer en tabellen:

| Term | Betekenis |
|---|---|
| Objecttype | Element van de informatiemodelplaat (ArchiMate business object, MIM-niveau 2), met de plaatnaam letterlijk; "informatieobject" alleen als synoniem in de eerste zin van de leeswijzer |
| Instantie | De waarde voor Jochem: een leesbare naam, geen veldwaarde; één per objecttype, toont het type en niet het aantal |
| Applicatiedienst | De ArchiMate-applicatiedienst op hoofdplaat v1.7 en in MORA (bijvoorbeeld Jaarplanning); alleen context, nooit een regel. De koppelvlakdienst uit Public is laag 3 en komt in het document niet voor |
| Koppeling | Een pijl op hoofdplaat v1.7 tussen twee componenten, met de koppeling-ID uit Public waar die er is (OC-P&R, OC-SIS, OC-LMS) |

Keuzes die in de tegenlezingen open bleken en hier vastliggen:

- **Relaties, geen labels.** De controle toetst het drietal (soort, van, naar) tegen `informatiemodel.json`; nesting op een aggregatie of compositie van ouder naar kind, ongeacht label; het label wordt getoond als de plaat het heeft. Een relatie die de plaat niet kent wordt geen regel maar een vraag.
- **Toestand.** Een objecttype ontstaat één keer; een latere verschijning (planbaar naar geroosterd, aangemeld naar ingeschreven) is een regel met soort `verandert` en een veld `toestand` met de stadia uit het kaderscenario. Dekking telt op de eerste verschijning.
- **Rollen en componenten.** Een ontstaat-regel draagt een rol uit een gesloten lijst uit het kaderscenario (onderwijsontwerper, onderwijsontwikkelaar, planner, roosteraar, SLB'er, docent, examinator, examencommissie, student); een stroomt-regel draagt de componentnamen letterlijk uit v1.7 en de uiteinden heten `van` en `naar`. Eigenaarschap (U3) staat één keer per objecttype in de familietabel, niet op de regel.
- **Pijlidentiteit.** Een pijl is (van, naar) op v1.7 na het oplossen van junctions; `stromen.json` uit de export is de enige bron. Geen nummers, geen terugval op de tabel v20260317. "Geen pijl op de hoofdplaat" is een geldige lege regel die de controle rapporteert.
- **Koppeling-ID's.** In de leeswijzer een mappingregel: OC-P&R is OC naar Planningssysteem en terug; OC-SIS is OC naar KRS en OC naar SVS; OC-LMS is OC naar LMS. Andere pijlen: "pijl zonder koppeling".
- **Leslaag.** De modelleur heeft besloten de leslaag (Les specificatie, Lesgelegenheid, Lesgelegenheid verbintenis, Lesgelegenheid resultaat) mee te nemen. Dat is een herziening van ontwerpkeuze 8 en hoort met motivering in de eerstvolgende modelronde (feature 8, na 30 september). Tot die tijd draagt de regeltabel een scope-uitzondering voor die vier objecttypen, met de bron "besluit modelleur 17 september, ontwerpkeuze 8 wordt herzien", en de spanning (v1.7 wisselt Lesgelegenheid uit van Rooster naar KRS) staat op de vragenpagina.
- **Fase-indeling.** De fasenamen letterlijk uit de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario; roosteren en de groepen horen in fase 4, niet in fase 2 (de mock-up wordt daarop gecorrigeerd). De verwachting welk objecttype in welke fase voor het eerst verschijnt komt uit de alinea "Wat licht op in de plaat" per fase en de laag-1-analyse, en wordt op 18 september vastgesteld.
- **Namen.** De weergavenaam op een regel is de plaatnaam letterlijk; de controle normaliseert alleen witruimte (`Opleiding aanbod  verbintenis` met dubbele spatie geldt als gelijk aan de naam met één spatie). Een aanname geldt voor de instantie, nooit voor het objecttype: een objecttype dat niet op de plaat staat wordt geweigerd.
- **Versiepin.** De regeltabel draagt de commit van `informatiemodel.json` en `begrippen.json` waartegen is gecontroleerd; de controle waarschuwt bij afwijking.
- **Bronnen.** Kaderscenario, scenario 1.1, persona en de voorbeeldpayloads mogen bron zijn (het veld `bron` verwijst); de instantietekst is een leesbare naam, geen veldwaarde.

## 3. Eisen en acceptatiecriteria

| Eis | Wat | Acceptatiecriterium |
|---|---|---|
| R1 Regeltabel als bron | `architecture/model/informatiemodel/voorbeeld-lr1-regels.json` met kop (model-commit, fasenlijst met stappen en bron, rollenlijst, scope-uitzonderingen, koppeling-ID-mapping) en per regel: fase, stap, soort (ontstaat, verandert, stroomt), wie of van en naar, objecttype, instantie, toestand, relatie als drietal, aanname, bron, zin | Valideert tegen een JSON-schema (eigen validatie in stdlib, geen afhankelijkheid); elke objecttypenaam bestaat in `informatiemodel.json` na witruimtenormalisatie; elke relatie bestaat als (soort, van, naar); nesting alleen op aggregatie of compositie; elke rol staat in de rollenlijst; elke stroomt-regel wijst naar een (van, naar) in `stromen.json` of draagt de markering "geen pijl op de hoofdplaat"; elke stap staat in de fasenlijst |
| R2 Dekking | Elk objecttype binnen scope (inclusief de scope-uitzonderingen) heeft minstens één ontstaat-regel, in de fase van de verwachting | De controle meldt per fase de ontbrekende objecttypen en faalt bij een objecttype buiten scope met een regel; voor 30 september is de lijst leeg voor fase 2 tot 4 |
| R3 Regelrenderer | Per regel een SVG in ArchiMate-vormtaal: geel voor rol en objecttype, blauw voor component, icoon per type, nesting bij aggregatie, gestippeld bij aanname, grijs bij scope-uitzondering, `van` en `naar` op de stroomt-regel met de processtap als klein label; geen externe fonts, geen scripts | Tests uit `tegenlezing-plan-tester.md` (positief per soort, faalgevallen, randgevallen, byte-gelijke uitvoer); welgevormde en zelfdragende SVG; een schermafbeelding van de render op de PR-branch in de PR-beschrijving |
| R4a Export stromen | `stromen.json` uit de view "OKx hoofdplaat v1.7<concept>" in `model.archimate`, alleen lezen: per flow van, naar (na junction-resolutie), relatietype, label uit de labelexpressie of de relatienaam, koppeling-ID uit de mapping | Precies één regel per flow; test op junction-resolutie met een fixture; het modelbestand is voor en na byte-gelijk |
| R4b Render hoofdplaat | Dezelfde view als SVG: posities en knikpunten uit Archi (knikpunt is het gemiddelde van bronmidden plus startoffset en doelmidden plus eindoffset), labels uit `labelExpression` op connecties en groepen, eindpunten van geneste elementen op het geneste element, kleur en icoon per ArchiMate-type, lijnkleur uit de connectie | Telbaar: aantal elementen en connecties gelijk aan de view (49 en 43 voor de view zonder context), nul namen breder dan hun vak, nul labels die een elementvak overlappen; daarna het oordeel van de modelleur naast de JPG. Terugval bij rood: de JPG in het document, `stromen.json` blijft de bron |
| R5 Document | `voorbeeld-leerroute-1-jochem.md` uit de regeltabel: leeswijzer (definitieblok, legenda, mappingregel koppeling-ID's, de zin "een instantie toont het type, niet het aantal", noot over de fasenamen), per fase chips (objecttypen, stromen, MORA-hoofdproces) en regels als SVG, een tabel per familie, de vragenpagina | Tests uit de tegenlezing (secties, SVG-verwijzingen lossen op, familietabellen dekken de scope, stub-fase toont chips en de vaste zin, geen streepjes, byte-gelijk); `validate-docs.py` groen; familietabel met de kolommen objecttype, instantie, fase, toestand, aanname, bron, bezitter (U3), begrip en definitiestatus, entiteit in Public en OEAPI-object (links), heet bij u, hangt bij u onder |
| R6 Bijlage en deck | Zes pagina's: 1 de vraag aan de kerngroep en de legenda, 2 tot 4 een pagina per fase (chips plus regels; past fase 4 niet, dan alleen chips), 5 de plaat, 6 de vragen met invulblad. Het deck is dezelfde zes pagina's als slides, uit dezelfde SVG's | Pdf in `presentaties/export/`; verstuurd aan de agenda-eigenaar uiterlijk 25 september met bevestiging van ontvangst; reserve-verzender benoemd; doorloop van dertig minuten op 24 september |
| R7 Vragenpagina | Hoogstens zeven vragen die de regels van fase 2 tot 4 oproepen, elk met de regel waar de vraag zichtbaar wordt, de consequentie voor het model en de antwoordvorm; één regel die de laag-3-vragen (patroon, schema's, toetslijst, profielselectie) doorverwijst naar het spoor koppelvlakspecificatie | Kandidaten, te bevestigen op 22 september: cohort als sleutel of object (ontwerpkeuze 17); verzoek tot aanbod als planopgave of intekening (13); aanmelding, inschrijving en verbintenis als subtype of toestand (13); stamgroep, lesgroep en planninggroep tegenover Plaatsingsgroep (15, #235); rijping van aanbod als toestand of eigen objecttypen (13); de leslaag op de pijl Rooster naar KRS tegenover ontwerpkeuze 8; welke bestaande structuur bij de instelling aanmelding, inschrijving en cohort draagt. Elke vraag verwijst naar minstens één regel of objecttype in het document |
| R8 Acceptatietest 30 september | Per regel van fase 2 tot 4 per aanwezig lid een van vier antwoorden: herken, heet anders (met de term), hangt anders (met de plek), ontbreekt; het invulblad is het formulier, vooraf ingevuld telt mee | Geslaagd als elke regel minstens één antwoord heeft en elke vraag minstens één reactie; de uitkomst staat binnen twee werkdagen als comment onder Public #106, met de termen van de leden per objecttype |
| R9 Publicatie (na de sessie) | Document en SVG's via `scripts/publiceer-informatiemodel.py` naar het pakket in Public, `release.json` bijgewerkt, meta blijft bron | Public-controles groen; draft-PR gestapeld op Public PR 104; geen voorwaarde voor 30 september |
| R10 Modelronde (na de sessie) | In Archi door de modelleur: ontwerpkeuze 8 herzien met motivering, de dubbele spatie, de plaatkoppen, en de objecttypen aan de flows van v1.7 (als naam of, bij voorkeur, als business object aan de flow) | `validate-archimate.py` groen; `informatiemodel.json` en begrippenlijst opnieuw gegenereerd; de scope-uitzondering in de regeltabel vervalt |
| R11 Reviews | Tester (eis voor eis met de testgevallen), informatiearchitect, lid kerngroep techniek (per fase de vier antwoorden als checklist) en schrijfstijl, in verse contexten, op fase 2 en 3 plus de vragenpagina op 23 september; fase 4 op 24 september | Rapporten als agent-rapport in de PR-beschrijving; hoogstens drie iteraties; rood op 24 september: de modelleur beslist welke bevindingen als "bewust open" meegaan |

## 4. Features, in implementatievolgorde

Basis: `informatiemodel.json`, `begrippen.json`, de generatorscripts, `tests/` en het publiceerscript bestaan alleen op branch `89-informatiemodel-en-begrippenkader` (PR 225, open; PR 233 is daarin gemerged), niet op `dev`. Keuze voor de modelleur op 18 september: A, de lopende modelronde committen en PR 225 mergen, daarna alle branches vanaf `dev` (aanbeveling: één dagdeel, schone basis); B, alle branches vanaf `origin/89-...` aftakken en pas na PR 225 mergen (start direct, rebases bij elke wijziging op 89). Het model is tijdens de sprint bevroren: geen Archi-werk tot na 30 september behalve het committen van de lopende ronde.

### 1. Regeltabel, schema, fasenlijst en controle (meta, agent, 18 september)

- **Wat:** het schema en het bronbestand met kop (fasenlijst met stappen en bron, verwachting objecttype per fase, rollenlijst, scope-uitzonderingen, koppeling-ID-mapping, model-commit) en `scripts/controleer-voorbeeldregels.py` dat R1 en R2 afdwingt.
- **Hangt af van:** de basis; feature 3a voor de stroomt-controle (zelfde dag).
- **Levert op:** schema, kop gevuld, controle met de testgevallen uit de tegenlezing, README-regel in `architecture/model/README.md`.
- **Sluit uit:** de regels zelf (feature 4) en het tekenen (feature 2).

### 2. Regelrenderer (meta, agent, 18 september)

- **Wat:** `poc/blok.py` wordt `scripts/teken-voorbeeldregels.py`: leest de regeltabel, schrijft per regel een SVG naar `architecture/model/informatiemodel/img/regels/`, met de vormregels uit sectie 2 en R3.
- **Hangt af van:** feature 1 (schema).
- **Levert op:** script, tests, voorbeeld-SVG's, schermafbeelding op de branch.
- **Sluit uit:** de hoofdplaat (feature 3) en het document (feature 5).

### 3a. Export van de hoofdplaat als stromen.json (meta, agent, 18 september)

- **Wat:** `scripts/exporteer-archimate-view.py`: leest de view alleen, lost junctions op, schrijft `stromen.json` (R4a). Geen layout.
- **Hangt af van:** geen.
- **Levert op:** script, tests (junction-resolutie, byte-gelijk modelbestand, onbekende view), `stromen.json`.
- **Sluit uit:** tekenen (3b).

### 3b. Render van de hoofdplaat herstellen (meta, agent, 21 september, één dag, optioneel)

- **Wat:** `poc/hoofdplaat.py` wordt `scripts/teken-archimate-view.py` met de herstelpunten uit R4b: labelexpressies, knikpuntgemiddelde, geneste eindpunten, tekst zonder verlies, labels op het langste segment met witte achtergrond, lijnkleur.
- **Hangt af van:** 3a (gedeelde inlezer).
- **Levert op:** script, tests, render van beide v1.7-views, telbare controle.
- **Sluit uit:** een generieke Archi-vervanger. Terugval: de JPG.

### 4. Regels vullen voor fase 2 tot 4 (meta, agent met de modelleur, 21 tot 23 september)

- **Wat:** ontstaat-, verandert- en stroomt-regels uit kaderscenario, scenario 1.1, persona en payloads; één instantie per objecttype; aannames gemarkeerd met bron of "geen bron, keuze van het voorbeeld"; de drie relatiefouten uit de mock-up gecorrigeerd (cohort zonder relatie wordt vraag; `middels` vanaf Aanmelding; Onderwijseenheid aanbod onder Opleidingsprogramma aanbod).
- **Hangt af van:** features 1, 2 en 3a.
- **Levert op:** fase 2 op 21 september (eerste render), fase 3 op 22 september (stopmoment), fase 4 op 23 september (asynchroon akkoord via comment).
- **Sluit uit:** nieuwe objecttypen of relaties; fase 1 en 5 tot 8 (sub-issue 9).

### 5. Documentgenerator en document (meta, agent, 23 september)

- **Wat:** `scripts/genereer-voorbeeld-lr1.py` bouwt het document uit R5.
- **Hangt af van:** features 1, 2 en 4; 3b voor de plaat als beeld, met de JPG als terugval.
- **Levert op:** script, tests, het document met fase 2 tot 4 gevuld en de andere fasen als stub.
- **Sluit uit:** payloads, diensten, berichtstromen; laag 3 en 4 zijn links in de familietabel.

### 6. Bijlage en deck (meta, agent, 24 september; verzending modelleur, 25 september)

- **Wat:** de zes pagina's uit R6 als markdown-bijlage (pdf) en als Slidev-deck `presentaties/src/260930_kerngroep_techniek_jochem.md` uit dezelfde SVG's; het invulblad; de mailtekst; de doorloop.
- **Hangt af van:** feature 5 (fase 2 en 3 minimaal).
- **Levert op:** pdf en pptx in `presentaties/export/`, mail verstuurd, ontvangst bevestigd.
- **Sluit uit:** het versioneringsdeel en de bouwblokken van Garik.

### 7. Publicatie naar Public (7a meta-script, 7b Public-PR; agent; 1 tot 3 oktober)

- **Wat:** publiceerscript uitbreiden met document en `img/regels/`, `release.json`, draft-PR in Public gestapeld op PR 104.
- **Hangt af van:** feature 5; branch 232 in `dev`.
- **Sluit uit:** wijzigingen aan de bestaande documenten in het pakket.

### 8. Modelronde (modelleur, na 30 september)

- **Wat:** R10.
- **Hangt af van:** de bevindingen van de kerngroep; het model bevroren tot dan.

### 9. Regels voor fase 1 en 5 tot 8 (meta, agent, 1 tot 3 oktober)

- **Wat:** de overige fasen, met de termen van de kerngroep uit R8 in de kolommen "heet bij u".

## 5. Dwarsdoorsnijdend

- **Tests volgens de testpersona.** `tests/test_<script>.py`, stdlib `unittest`, given-when-then, verwachtingen uit eigen fixtures; de tabellen per script staan in `tegenlezing-plan-tester.md` en komen letterlijk in de sub-issues.
- **Schrijfstijl.** Geen streepjes, geen nadruk-accenten, geen tweede persoon; regels dragen zinnen uit het kaderscenario. Mechanische controle in de generatortest.
- **Werkafspraken.** Eén issue, één branch, één pull request per feature. Mergestrategie, keuze voor de modelleur: A, een integratiebranch `106-jochem` vanaf `dev` waarin de agent de sub-branches na hun reviews samenvoegt en één PR naar `dev` na 30 september (aanbeveling; vraagt expliciet akkoord omdat het samenvoegen dan niet door het OKx-team gebeurt); B, dagelijkse merge van afgeronde sub-PR's naar `dev` door de modelleur (een kwartier per PR).
- **Milestone.** Keuze voor de modelleur: A, alles onder meta-milestone 7 en Public-milestone 5 laten (geen werk, sprint onzichtbaar tussen 19 issues); C, een eigen milestone "Voorbeelduitwerking Jochem, kerngroep 30 september" in meta en Public met einddatum 3 oktober, herleidbaar naar epic-0001 (aanbeveling, een kwartier).
- **Publieke repositories.** Geen namen of citaten van leveranciers in regels, tabellen, README of deck.
- **Zelfdragende sub-issues.** Elke sub-issue is zonder deze sessie op te pakken: taak, eigenaar, datum, afhankelijkheid, klaar-criterium met R-nummers, testgevallen, stopmoment.

## 6. Implementatieplan op werkdagen

| Dag | Wat | Wie | Stopmoment |
|---|---|---|---|
| do 17 sep | Plan versie 2, tweede tegenlezing, akkoord; sub-issues en milestone aanmaken | agent, modelleur | Akkoord op het plan en op de drie keuzes (basis, merge, milestone) |
| vr 18 sep | Basis (keuze A of B); features 1, 2, 3a; fasenlijst, verwachting per fase, rollenlijst; pdf-export proefdraaien op een bestaand deck; agendaslot en reserve-verzender bevestigen | agent; modelleur (één dagdeel) | Einde dag, asynchroon: fasenlijst, verwachting per fase, testgevallen |
| ma 21 sep | Feature 4 fase 2, eerste render; feature 3b (één dag, optioneel) | agent | |
| di 22 sep | Feature 4 fase 3; vragenpagina in concept | agent; modelleur (één dagdeel) | Inhoud fase 2 en 3, aannames, de zeven vragen, hoofdplaat-render of JPG |
| wo 23 sep | Feature 4 fase 4; feature 5; reviews op fase 2 en 3 en de vragenpagina | agent | Fase 4 asynchroon via comment |
| do 24 sep | Iteratie; feature 6 (bijlage, deck, invulblad); doorloop dertig minuten | agent; modelleur (één dagdeel) | Document fase 2 tot 4, deck, invulblad |
| vr 25 sep | Verzending, ochtend als buffer | modelleur (half dagdeel); reserve-verzender | Verzonden en bevestigd |
| wo 30 sep | Kerngroep techniek; invulbladen | modelleur | |
| do 1 tot za 3 okt | Uitkomst als comment (R8); features 7, 8 en 9; PR's mergen | agent, modelleur | |

Capaciteit modelleur: drie en een half dagdeel van de zes tot 25 september; reserve voor uitloop. Terugvalvolgorde bij uitloop: eerst feature 3b (JPG als plaat), dan fase 4 alleen als chips, dan de leslaag als grijze chips; nooit `stromen.json`, de vragenpagina, het invulblad of de verzenddatum.

## 7. Risico's en faalpaden

| Risico of faalpad | Gevolg | Maatregel of uitkomst |
|---|---|---|
| Basis niet op tijd (PR 225 niet gemerged) | Feature 1 wacht | Keuze B: aftakken van `origin/89`, mergen na PR 225 |
| Modelnamen schuiven tijdens de sprint | R1 breekt | Model bevroren; versiepin in de regeltabel; de controle waarschuwt |
| Feature 3b loopt uit (Archi-bijzonderheden) | Geen render | Eén dag gebudgetteerd; JPG in het document; `stromen.json` blijft |
| Fase 3 raakt de open vragen over aanmelding, inschrijving en verbintenis | Discussie in plaats van herkenning | Eén instantie, aanname gemarkeerd, de vraag op de vragenpagina; geen akkoord op 22 september betekent: elke omstreden regel wordt een aanname met vraag en blijft staan |
| Reviews rood na drie iteraties | Geen tijd voor een vierde | De modelleur beslist op 24 september welke bevindingen als "bewust open" meegaan |
| `validate-docs.py` of de generatortest rood | Document niet leverbaar | Generator herstellen, nooit het document met de hand |
| Pdf-export rood | Geen bijlage | Proefdraai op 18 september; terugval browserafdruk van de markdown-bijlage |
| Modelleur valt uit op 25 september | Geen verzending | Reserve-verzender benoemd op 18 september; bijlage staat op 24 september klaar op de branch |
| Agendaslot niet bevestigd | Geen tijd op 30 september | Eigenaar, lengte en mailingdatum op 18 september bevestigen |
| Het document groeit voorbij de zes pagina's | Niemand leest het | Zes pagina's is een harde grens in feature 5 en 6; fase 4 dan alleen chips; het volledige document is naslag |
| De kerngroep leest de bijlage niet vooraf | Sessie zonder herkenning | Pagina 1 opent met de vraag; het invulblad werkt ook live |

## 8. Sub-issues onder Public #106 (aan te maken na akkoord)

| Nr | Titel | Repo | Eigenaar | Uiterlijk | Hangt af van | Klaar als |
|---|---|---|---|---|---|---|
| 1 | Regeltabel, schema, fasenlijst en dekkingscontrole | meta | agent | 18 sep | basis | R1 en R2 tests groen; fasenlijst, verwachting per fase en rollenlijst akkoord (stopmoment 18 sep) |
| 2 | Regelrenderer: van regel naar SVG in ArchiMate-vormtaal | meta | agent | 18 sep | 1 | R3 tests groen; schermafbeelding op de branch |
| 3a | Hoofdplaat v1.7 als stromen.json (alleen lezen, junction-resolutie) | meta | agent | 18 sep | geen | R4a tests groen; modelbestand byte-gelijk |
| 3b | Hoofdplaat-render herstellen: labelexpressies, knikpunten, geneste eindpunten | meta | agent | 21 sep (één dag) | 3a | R4b telbaar groen of terugval JPG vastgelegd |
| 4 | Regels fase 2 tot 4 (Jochems eerste periode) | meta | agent, modelleur | 23 sep | 1, 2, 3a | R2 leeg voor fase 2 tot 4; stopmoment 22 sep akkoord; fase 4 asynchroon akkoord |
| 5 | Documentgenerator en voorbeeld-leerroute-1-jochem.md | meta | agent | 23 sep | 1, 2, 4 | R5 tests en validate-docs groen; reviews R11 gestart |
| 6 | Bijlage en deck kerngroep 30 september, invulblad, verzending | meta | agent; modelleur verzendt | 24 sep, verzending 25 sep | 5 | R6: pdf en pptx in export, doorloop gedaan, mail verstuurd en bevestigd |
| 7a | Publiceerscript: document en SVG's naar het pakket | meta | agent | 3 okt | 5, branch 232 in dev | R9 test groen |
| 7b | Draft-PR voorbeelduitwerking in Public | Public | agent | 3 okt | 7a, PR 104 | Public-controles groen, PR op draft |
| 8 | Modelronde: ontwerpkeuze 8 herzien, dubbele spatie, plaatkoppen, objecttypen aan de flows van v1.7 | meta | modelleur | 3 okt | uitkomst 30 sep | R10; scope-uitzondering vervalt |
| 9 | Regels fase 1 en 5 tot 8, met de termen van de kerngroep | meta | agent | 3 okt | 4, 8 | R2 leeg voor alle fasen |
| 10 | Acceptatietest 30 september en uitkomst onder Public #106 | Public | modelleur, agent | 2 okt | 6 | R8: comment met per regel de antwoorden en per objecttype de termen |

Sub-issues in meta hangen via de sub-issue-koppeling onder Public #106; lukt dat niet over repositories heen, dan via een takenlijst in het issue. Elke sub-issue krijgt de testgevallentabel voor zijn script en de vaste velden uit sectie 5.

## Open voor vervolg

- De drie keuzes voor de modelleur: basis (A of B), mergestrategie (A of B), milestone (A of C).
- Reserve-verzender en agenda-eigenaar voor 25 september.
- Of de objecttypen op v1.7 als naam op de flow komen of als business object aan de flow (R10); de tweede verdient de voorkeur zodra de controle op id's gaat werken.
