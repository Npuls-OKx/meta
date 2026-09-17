# Tegenlezing featureplan "Jochem in het informatiemodel" (projectmanager en testcoördinator)

Gelezen: het featureplan `architecture/agent-artifacts/feature-plans/20260917_1500_jochem-in-het-informatiemodel.md`, de mock-up en README onder `research/20260916_1300_voorbeelduitwerking-leerroute-1/`, `plan.md` in die map, `AGENTS.md`, de skills `okx-product-flow` en `okx-test-persona`, en (alleen lezend) de issues Public #106, meta #237, #234 en #235, de open PR's en de milestones. Aangenomen persona's: de projectmanager en de testcoördinator uit `.agents/personas/`. De totstandkoming van het plan is niet bekend; beoordeeld is wat er staat.

## Feiten waarop de beoordeling leunt

| Feit | Gevolg voor het plan |
|---|---|
| 17 september is een donderdag; 19 en 20 september vallen in het weekend. Tot en met 25 september zijn er zes werkdagen (18, 21, 22, 23, 24, 25); tot en met 30 september negen | "Dertien dagen" zijn zes werkdagen tot de bijlage. De modelleur heeft in die periode zes dagdelen |
| `informatiemodel.json`, `genereer-informatiemodel-doc.py`, `genereer-begrippenlijst.py` en de map `tests/` bestaan alleen op branch `89-informatiemodel-en-begrippenkader` (PR 225, open) en branch `232-publiceer-informatiemodel-naar-public` (nog geen PR); niet op `dev`. `publiceer-informatiemodel.py` bestaat alleen op branch 232 | Feature 1, 4, 5 en 6 hebben op `dev` geen bron om op te bouwen; "hangt af van: geen" klopt niet |
| Public PR 104 (informatiemodel als laag 1 en 2 in het pakket) staat open op `feature/restructure-and-versioning`, niet op `dev` | Feature 6 stapelt op een PR die zelf op een featurebranch stapelt |
| `model.archimate` heeft op branch 89 ongecommitte wijzigingen (de modelronde loopt); ArchiMate-bestanden zijn niet mergebaar (harde regel 1, ADR 0010) | Feature 8 "parallel" is alleen veilig na het afronden van branch 89 |
| Hoofdplaat v1.7 telt 33 flows (28 zonder context), geen enkele met een naam. De pijlnummertabel in het projectoverzicht telt 17 pijlen van de oudere plaat v20260317; de mock-up gebruikt de nummers 2, 8, 10 en 13, waarvan 8, 10 en 13 in die tabel op andere pijlen slaan (8: OC naar rooster in de tabel, rooster naar KRS in de mock-up; 10: SKS naar SVS tegenover CAMBO naar KRS; 13: SVS naar examenafname tegenover KRS naar LMS) | De pijlnummers hebben nog geen bron; de terugvaloptie "tabel in het projectoverzicht" past niet op v1.7 |
| Public #106 hangt onder Public-milestone 5 (epic-0002, koppelingspecificatiestructuur); #237, #234 en #235 onder meta-milestone 7 (epic-0001, 19 open issues) | De milestone die het plan noemt (epic gezamenlijke taal) is niet die van het bovenliggende issue |
| De "zeven vragen" staan in `plan.md` sectie 7 als (a) tot (g); c, e en f gaan over interactiepatronen, governance van de toetslijst en de profielselectie op een endpoint (laag 3 en 4) | Drie van de zeven vragen vallen buiten de scope MIM 1 en 2 die het plan zelf kiest |
| De mock-up zet "Periode 1 roosteren" in fase 2; `plan.md` en de samenvatting onder Public #106 zetten roosteren in fase 4 (S4) | De fase-indeling en de stappen per fase liggen niet vast |
| Slidev-export (pdf via playwright-chromium, pptx via LibreOffice) is ingericht en eerder gebruikt (`export/260915_kerngroep_techniek`) | Exportrisico is klein, mits de toolchain in de gebruikte worktree op tijd draait |

## Bevindingen projectmanager

### PM1. Sectie 3 (feature 1, 4, 5, 6) en sectie 5: de bronbestanden bestaan niet op de basisbranch

- **Bevinding.** Het plan bouwt op `informatiemodel.json`, `begrippen.json`, de generatorscripts en het publiceerscript als bestaand. Op `dev` bestaan ze niet; ze leven op de open branches 89 en 232 en in Public op PR 104. Feature 1 begint dus op 18 september met een keuze die het plan niet noemt.
- **Ernst.** Blokkerend.
- **Wat anders moet.** De basis voor de start vastleggen. A: PR 225 (branch 89) op 17 of 18 september mergen naar `dev`, branch 232 als PR erachteraan; kost de modelleur een dagdeel review op dag één, daarna schone featurebranches vanaf `dev`; scope ongewijzigd. B: alle sub-issues vertakken vanaf branch 89; start direct, maar elke wijziging op 89 dwingt rebases af en de PR's kunnen pas na 225 mergen; scope ongewijzigd, doorlooptijd na 30 september langer. C: de gegenereerde `informatiemodel.json` kopiëren naar de featurebranch; snelste start, maar breekt "één bron per laag" en levert een tweede waarheid op die later moet worden opgeruimd. Aanbeveling: A, en het dagdeel van de modelleur op 17 of 18 september daaraan besteden.

### PM2. Sectie 5: het schema rekent met kalenderdagen en heeft geen buffer

- **Bevinding.** "19 tot 22 september" voor feature 3 en fase 2 bevat een weekend; netto twee werkdagen. Op 24 september staan feature 6, feature 7 en het akkoord op document en deck op één dag; 25 september is tegelijk de enige reservedag en de verzenddag. Eén mislukte reviewronde op 23 september schuift de bijlage voorbij de agendadatum.
- **Ernst.** Blokkerend.
- **Wat anders moet.** Herplannen op werkdagen: 18 september feature 1 en 2 en de vaststellingen uit TC1 tot TC3; 21 september feature 3 (beperkt, zie PM8) en fase 2; 22 september fase 3 en 4 met stopmoment; 23 september feature 5 en het deck (feature 7) in eerste versie plus reviews; 24 september iteratie en akkoord; 25 september verzending, met de ochtend als buffer. Feature 6 uit het kritieke pad (zie PM8).

### PM3. Sectie 5: de stopmomenten zitten op het verkeerde onderwerp en missen de product-flow

- **Bevinding.** Het stopmoment van 19 tot 22 september vraagt akkoord op "fase 2 als vorm", terwijl de vorm al in vier ronden is gekozen (comment onder #237). Wat ontbreekt is een stopmoment op de inhoud van fase 3, de omstreden fase (aanmelding, inschrijving, verbintenis; #234). Daarnaast eist de product-flow per deliverable een akkoord van de mens op acceptatiecriteria en testgevallen voor de uitwerking; met zeven features zijn dat zeven touchpoints die niet in het schema staan.
- **Ernst.** Moet.
- **Wat anders moet.** Drie stopmomenten met een vaste inhoud: 18 september (dit plan als requirements-document voor alle features, inclusief de testgevallentabellen uit TC5, plus de vaststellingen uit TC1 tot TC3); 22 september (inhoud fase 2 en 3, aannames en de hoofdplaat-render of de terugval); 24 september (document fase 2 tot 4, deck, invulblad). Fase 4 asynchroon via een comment in het sub-issue. Zo blijft de modelleur binnen zijn dagdelen.

### PM4. Sectie 4 (werkafspraken) en sectie 7: de milestone is niet benoemd en past niet op het bovenliggende issue

- **Bevinding.** Het plan zegt "onder een milestone die naar de requirementsboom herleidt (epic gezamenlijke taal en standaard)". Dat is meta-milestone 7 met 19 open issues; het bovenliggende Public #106 hangt onder Public-milestone 5 (epic-0002). De projectmanager kan de voortgang van deze klus zo niet volgen en de herleidbaarheid is gesplitst.
- **Ernst.** Moet.
- **Wat anders moet.** A: alles onder meta-milestone 7 en Public #106 laten staan; geen werk, maar de sprint verdwijnt tussen 19 andere issues en de herleidbaarheid van #106 klopt niet. B: Public #106 verhuizen naar een Public-milestone onder epic-0001; klein, maar de sprint blijft onzichtbaar. C: een eigen milestone "Voorbeelduitwerking Jochem, kerngroep 30 september" in meta en in Public, herleidbaar naar epic-0001 (feature-0001 en feature-0002), met einddatum 30 september; kost een kwartier en geeft één voortgangsbeeld met einddatum. Aanbeveling: C.

### PM5. Sectie 7: de sub-issues zijn niet zonder navraag op te pakken

- **Bevinding.** Elke rij heeft een titel en een taak in één zin, maar geen eigenaar (agent of modelleur), geen klaar-criterium (de R-nummers uit sectie 2 worden niet aangehaald), geen datum en geen afhankelijkheid. Sub-issue 6 heet Public maar bevat een meta-script (breekt 1 issue, 1 branch, 1 PR). Sub-issue 8 begint met een open keuze (pijlnummering) die het plan bij de uitvoerder legt. Sub-issue 4 noemt een stopmoment zonder te zeggen wie beslist. Sub-issue 9 heeft geen datum.
- **Ernst.** Moet.
- **Wat anders moet.** Elke sub-issue in vaste vorm: taak, eigenaar, uiterste datum, hangt af van (sub-issue en branch), klaar als (R-nummers met de meetbare toets), stopmoment (wie, wanneer, waarop). Sub-issue 6 splitsen in 6a (meta: publiceerscript, test) en 6b (Public: draft PR); beide na 30 september. Sub-issue 8 de keuze uit "Open voor vervolg" meegeven als eerste taak met datum 18 september. Sub-issue 9 onder dezelfde milestone met einddatum 3 oktober.

### PM6. Feature 8 en harde regel 1: "loopt parallel" is onveilig voor het model

- **Bevinding.** De modelronde op branch 89 is niet afgerond (ongecommitte wijzigingen in `model.archimate`). Een tweede branch voor feature 8 op hetzelfde bestand is niet te mergen. Het plan noemt dit niet.
- **Ernst.** Moet.
- **Wat anders moet.** Serialiseren: eerst branch 89 committen en mergen (PM1, optie A), dan feature 8 op een eigen branch vanaf `dev`, door dezelfde persoon, en geen ander Archi-werk tot die is gemerged. In het sub-issue vastleggen dat het model tijdens de sprint bevroren is behalve voor feature 8.

### PM7. Sectie 5 (capaciteit): de dagdelen van de modelleur tellen niet op

- **Bevinding.** Beschikbaar: zes dagdelen tot 25 september. Gevraagd: akkoord op het plan (17 september, een dagdeel), review en merge van PR 225 (een dagdeel), feature 8 in volle omvang (33 flows benoemen, leslaag binnen scope, nummering, plaatkoppen en dubbele spaties opschonen: twee tot drie dagdelen), twee stopmomenten (twee dagdelen), verzending (een half dagdeel). Dat zijn zeven tot acht dagdelen.
- **Ernst.** Moet.
- **Wat anders moet.** Feature 8 inkrimpen tot wat fase 2 tot 4 nodig heeft: de nummering vastleggen en alleen de pijlen die in de stroomt-regels van fase 2 tot 4 voorkomen (circa acht) een naam geven; leslaag binnen scope alleen als dat één vlag in Archi is; plaatkoppen en dubbele spaties na 30 september. Dat scheelt een tot twee dagdelen en houdt de zes dagdelen sluitend met een halve dag reserve.

### PM8. Sectie 5 (terugvalvolgorde): feature 6 ontbreekt en feature 3 is als eerste terugval de verkeerde

- **Bevinding.** De volgorde is feature 3, dan fase 4, nooit de vragenpagina of de bijlagedatum. Feature 6 (publicatie naar Public, draft PR) staat niet in de rij, terwijl geen enkel doel van 30 september ervan afhangt. Feature 3 als eerste terugval botst met R1: de controle "wijst naar een bestaande pijl" leunt op `stromen.json` uit feature 3, en de terugval "nummering uit het projectoverzicht" past niet op v1.7 (zie TC1).
- **Ernst.** Moet.
- **Wat anders moet.** Feature 6 uit het kritieke pad naar 1 tot 3 oktober. Feature 3 vooraf splitsen: de export van `stromen.json` (bron, doel, informatieobject, nummer; geen layout nodig) hoort bij feature 1 en is verplicht; de layoutreparatie (knikpunten, tekst, labels) is optioneel met de bestaande `OKx hoofdplaat 1.7.jpg` als plaat. Terugvalvolgorde wordt dan: layout van feature 3, dan fase 4, dan de leslaag, nooit `stromen.json`, de vragenpagina of de bijlagedatum.

### PM9. Sectie 6: risico's die het plan mist

- **Bevinding.** Niet benoemd: de afhankelijkheid van drie open PR's (meta 225, branch 232, Public 104); het verschuiven van modelnamen tijdens de sprint (de modelronde voegde aanmelding, inschrijving en cohort net toe; een naamswijziging breekt R1); de modelleur als enig persoon voor stopmomenten en verzending zonder vervanger; de agenda van 30 september (wie is eigenaar, hoeveel minuten krijgt dit onderdeel naast het versioneringsdeel, is 25 september de bevestigde mailingdatum); het plan dat "in deze sessie" wordt uitgevoerd, waardoor een verloren sessie de voortgang meeneemt; de exporttoolchain die pas op 24 september in de worktree draait.
- **Ernst.** Moet.
- **Wat anders moet.** Zes rijen toevoegen met maatregel: basis vastzetten (PM1); modelnamen pinnen op de commit van `informatiemodel.json` en de pin in de leeswijzer noemen; een vervanger voor de verzending aanwijzen; het agendaslot (eigenaar, lengte, mailingdatum) op 18 september bevestigen; elke sub-issue zelfdragend formuleren zodat elke agentsessie hem kan oppakken; de pdf-export op 18 september proefdraaien op een bestaand deck.

### PM10. Sectie 1 (doel 3) tegenover R7: zes pagina's tegenover zes slides plus regels

- **Bevinding.** Doel 3 belooft hoogstens zes pagina's leeswerk; R7 staat zes inhoudelijke slides plus de regels van fase 2 tot 4 toe. Fase 2 en 3 tellen in de mock-up al negen regels; met fase 4 zijn het er circa vijftien, dus vijf tot acht extra slides. De kerngroep krijgt dan elf tot veertien pagina's.
- **Ernst.** Kan.
- **Wat anders moet.** A: zes pagina's in totaal, regels drie per pagina en fase 4 als chips; minste leestijd, scope van de bijlage kleiner, sessie doet fase 4 live. B: zes inhoudelijke pagina's plus een bijlage met alle regels, doel 3 aangepast naar "zes pagina's kern"; meer leeswerk, geen scopeverlies. C: alleen de zes pagina's en een link naar het document; minste werk, maar de regels bereiken alleen wie doorklikt. Aanbeveling: B, met de kernpagina's vooraan en de vraag aan de kerngroep op pagina één.

### PM11. Sectie 5 (1 tot 3 oktober) en de werkafspraak "alleen het OKx-team merget": geen mergestrategie voor de stapel

- **Bevinding.** Feature 2 hangt op 1, 4 op 1 en 3, 5 op 1, 2 en 4, 7 op 2, 4 en 5. Met één branch per feature en merges pas na 30 september ontstaat een stapel van vijf branches die elkaar bij elke wijziging tot rebasen dwingen.
- **Ernst.** Kan.
- **Wat anders moet.** A: een integratiebranch `106-jochem` vanaf `dev`, waarin de agent de sub-branches na hun reviews samenvoegt, en één PR naar `dev` na 30 september; kost niets extra, maar vraagt op 17 september expliciet akkoord omdat het samenvoegen niet door het OKx-team gebeurt. B: dagelijkse merge van afgeronde sub-PR's naar `dev` door de modelleur; conform de werkafspraak, kost een kwartier per PR uit zijn dagdeel. C: alles op één branch en één PR; snelst, breekt de werkafspraak. Aanbeveling: A met expliciet akkoord.

## Bevindingen testcoördinator

### TC1. R1, R4 en feature 4: de pijlnummers hebben geen bron, dus is R1 niet toetsbaar

- **Bevinding.** R1 eist dat elke stroomt-regel naar een bestaande pijl van de hoofdplaat wijst. Op v1.7 dragen de 33 flows geen naam of nummer; de terugvaltabel in het projectoverzicht beschrijft 17 pijlen van de plaat v20260317; de mock-up gebruikt nummers die op andere pijlen slaan dan die tabel. Tot de nummering vaststaat kan de tester geen enkele stroomt-regel goed- of afkeuren, en zal de controle alles of niets goedkeuren.
- **Ernst.** Blokkerend.
- **Wat anders moet.** De keuze uit "Open voor vervolg" naar 18 september halen: nummering op v1.7 (aanbeveling, want de stroomt-regels citeren v1.7). `stromen.json` in feature 1 uit `model.archimate` genereren zonder layout (bron, doel, relatietype, nummer, naam of leeg), zodat R1 vanaf dag één een bron heeft en niet van feature 3 afhangt. Testgeval: een stroomt-regel met een nummer dat niet in `stromen.json` staat faalt met een melding die het nummer en de regel noemt.

### TC2. R2 (dekking): "ontstaat in een fase" heeft geen definitie

- **Bevinding.** R2 eist dat elk objecttype dat in een fase ontstaat daar één regel heeft, en dat de lijst voor fase 2 tot 4 leeg is. Welk objecttype in welke fase ontstaat staat nergens: niet in `informatiemodel.json`, niet in het plan. Zonder die toewijzing kan de controle een ontbrekend objecttype niet aan fase 2 tot 4 of aan fase 5 tot 8 toerekenen, en zijn ook de chips van doel 1 voor de andere fasen niet te maken.
- **Ernst.** Blokkerend.
- **Wat anders moet.** Een lijst objecttype per fase (verwachte fase van ontstaan) als onderdeel van feature 1, afgeleid uit de laag-5-analyse, vastgesteld op 18 september. De controle krijgt een fasefilter en meldt per fase de ontbrekende objecttypen. Testgevallen: een objecttype met fase 3 zonder regel in fase 3 faalt; een objecttype met fase 6 zonder regel slaagt met filter fase 2 tot 4; een regel voor een objecttype buiten scope faalt.

### TC3. Feature 1 en doel 1: de fase-indeling en de stappen liggen niet vast

- **Bevinding.** Doel 1 is pas waarneembaar als bekend is welke stappen in fase 2, 3 en 4 horen. De mock-up zet roosteren in fase 2, `plan.md` en Public #106 in fase 4. Feature 1 belooft een "leeg gevuld bestand met de acht fasen en hun stappen" zonder te zeggen wie de stappenlijst vaststelt.
- **Ernst.** Moet.
- **Wat anders moet.** De acht fasen met hun stappen als tabel in het plan of in sub-issue 1, met de bron per stap (kaderscenario, scenario 1.1) en akkoord op 18 september. Roosteren eenduidig plaatsen. Testgeval: het schema wijst een regel met een stap die niet in de fasetabel staat af.

### TC4. R8: "de zeven vragen" zijn niet benoemd en passen deels niet in de scope

- **Bevinding.** R8 verwijst naar "de zeven vragen uit het plan onder Public #106". De vragen (a) tot (g) in `plan.md` sectie 7 zijn de enige zeven; c (request-reply of notificatie), e (governance van de toetslijst) en f (profielselectie op een endpoint) zijn laag 3 en 4, terwijl feature 5 payloads, diensten en berichtstromen uitsluit. De tester kan niet vaststellen of de vragenpagina compleet is, en de kerngroep krijgt vragen over iets wat het document niet toont.
- **Ernst.** Moet.
- **Wat anders moet.** De zeven vragen in het plan opsommen, elk op MIM 1 en 2 (kandidaten uit `plan.md` sectie 6: cohort als sleutel of object; aanmelding en inschrijving naast de verbintenis; verzoek tot aanbod als één of twee dingen; welke groep bron is van de plaatsingsgroep; de plaats van het toetsonderdeel; de drager van aanwezigheid; keuzedeel op specificatie of aanbod), elk met de consequentie voor het model en een antwoordvorm. Testgeval: de vragenpagina telt precies zeven vragen en elke vraag verwijst naar minstens één regel of objecttype in het document.

### TC5. Sectie 2 en R10: acceptatiecriteria zonder testgevallen

- **Bevinding.** De testpersona eist per criterium een tabel (methode, given, then) voor de uitwerking; de tester in R10 loopt die "geval voor geval" af. Het plan heeft criteria, geen testgevallen. De reviews op 23 september hebben dan geen lijst om tegen te toetsen en worden interpretatie.
- **Ernst.** Moet.
- **Wat anders moet.** Per scriptfeature (1, 2, 3, 5, 6) een testgevallentabel in het sub-issue, opgesteld bij de start van de sub-issue; het akkoord van de modelleur asynchroon via een comment. Voor het document en het deck een checklist per doel uit sectie 1 (vier regels) en per R5 tot R8.

### TC6. R4: "naast de JPG gelegd en akkoord bevonden" is niet telbaar

- **Bevinding.** Het criterium is een oordeel zonder maat. Bij een afwijking is niet te zeggen of de render faalt of de smaak verschilt.
- **Ernst.** Moet.
- **Wat anders moet.** Telbaar maken voor het oordeel: aantal elementen en verbindingen gelijk aan de view in Archi (67 en 66 voor v1.7; 49 en 43 zonder context); nul namen langer dan hun vak (test op tekstbreedte); nul labels die een elementvak overlappen (test op begrenzingsvakken); daarna het visuele oordeel van de modelleur als laatste stap. Faalpad: bij rood op een van de drie tellingen gaat de JPG 1.7 in het document en blijft `stromen.json` (TC1) de bron.

### TC7. R7 en feature 7: "verstuurd" is waarneembaar, de rest niet

- **Bevinding.** Onbenoemd: aan wie (agenda-eigenaar), door wie, en wat er gebeurt als de modelleur op 25 september uitvalt. Geen generale repetitie; geen invulblad, terwijl doel 4 eist dat "wat heet bij u anders" per regel kan worden genoteerd.
- **Ernst.** Moet.
- **Wat anders moet.** Ontvanger en reserve-verzender in sub-issue 7; een doorloop van dertig minuten op 24 september met de modelleur in de rol van kerngroeplid (herkent hij per regel het objecttype en de pijl zonder uitleg); een invulblad per regel met vier kolommen (herken, heet anders, hangt anders, ontbreekt) als laatste pagina van de bijlage. Klaar als: pdf in `presentaties/export/`, mail met bijlage en invulblad verstuurd aan de agenda-eigenaar, bevestiging van ontvangst.

### TC8. Sectie 6: faalpaden die ontbreken

- **Bevinding.** Benoemd zijn de render die niet klopt (JPG) en het modelhuiswerk dat te laat is (labeltabel, leslaag grijs). Niet benoemd: reviews die na drie iteraties niet slagen (de product-flow escaleert naar de mens, maar er is geen dag voor); fase 3 zonder akkoord op 22 september; een rode `validate-docs` op het gegenereerde document; rode Public-controles bij feature 6; een mislukte pdf-export.
- **Ernst.** Moet.
- **Wat anders moet.** Per faalpad de uitkomst en wie beslist: reviews rood op 24 september, de modelleur beslist welke bevindingen als "bewust open" in de bijlage meegaan; fase 3 zonder akkoord, elke omstreden regel wordt een aanname met de vraag op de vragenpagina en de regel blijft; `validate-docs` rood, generator herstellen, nooit het document met de hand; Public-controles rood, de draft-PR blijft draft en is geen voorwaarde voor 30 september; export rood, pdf via de browserafdruk van het markdown-document.

### TC9. Sectie 1 en het geheel: de acceptatietest voor 30 september is deels af te leiden

- **Bevinding.** De vier doelen zijn waarneembaar (regels op tafel, één instantie per objecttype, bijlage op tijd, vragen op één pagina). Wat ontbreekt is de uitkomst van de sessie zelf: wanneer is de kerngroep "geslaagd" en waar landt het antwoord. Zonder dat is de sessie een presentatie, geen toets.
- **Ernst.** Moet.
- **Wat anders moet.** De acceptatietest in het plan opnemen, in termen die de kerngroep herkent: per regel van fase 2 tot 4 (circa vijftien) noteert de begeleider per aanwezig lid een van vier antwoorden (herken, heet anders met de term, hangt anders met de plek, ontbreekt); geslaagd als elke regel minstens één antwoord heeft, elke van de zeven vragen minstens één reactie, en de uitkomst binnen twee werkdagen als comment onder Public #106 staat met de instanties waar de kerngroep een andere term gebruikt. Het invulblad (TC7) is het testformulier; wie de bijlage vooraf invult, telt mee.

### TC10. R3 en R5: bewijs van "rendert op GitHub" en van de stubs

- **Bevinding.** R3 eist dat de SVG's op GitHub renderen; dat is alleen op een gepushte branch waarneembaar. R5 eist acht fasesecties terwijl alleen 2 tot 4 gevuld zijn; het plan zegt niet hoe een stub eruitziet.
- **Ernst.** Kan.
- **Wat anders moet.** R3: de controle op de PR-branch vastleggen met een schermafbeelding in de PR-beschrijving. R5: een stub-fase toont de chips uit de objecttype-per-fase-lijst (TC2) en de zin "regels volgen na 30 september"; testgeval: een fase zonder regels levert die zin en geen lege sectie.

### TC11. R9 en feature 3: gedrag van de renderer bij flow-naam én tabel

- **Bevinding.** "De labeltabel vervalt zodra de flows namen dragen" laat open wat de renderer doet als beide bestaan of elkaar tegenspreken.
- **Ernst.** Kan.
- **Wat anders moet.** Regel vastleggen: de naam in Archi wint; een tabelregel zonder naam in Archi geeft een waarschuwing; een tegenspraak faalt. Drie testgevallen.

## Oordeel

Uitvoerbaar in dertien dagen: nee in de huidige vorm (feature 3 volledig, feature 6, feature 8 in volle omvang en de product-flow per feature passen niet in zes werkdagen met zes dagdelen modelleur), ja in de afgeslankte vorm met deze drie aanpassingen:

1. **Basis en bronnen op dag één vastzetten.** PR 225 mergen zodat `informatiemodel.json` op `dev` staat (PM1); op 18 september de pijlnummering op v1.7, de fase- en stappenlijst en de lijst objecttype per fase vaststellen, en `stromen.json` zonder layout uit feature 1 laten komen (TC1 tot TC3).
2. **Kritieke pad afslanken en op werkdagen plannen.** Feature 6 en het volledige modelhuiswerk (leslaag, opschonen) naar 1 tot 3 oktober; feature 3 beperkt tot de export, de layoutreparatie optioneel met de JPG 1.7 als plaat; feature 8 beperkt tot de nummering en de pijlen van fase 2 tot 4; deck op 23 september, iteratie en akkoord op 24 september, 25 september verzending met buffer (PM2, PM7, PM8).
3. **Sub-issues en toetsing aanscherpen.** Per sub-issue eigenaar, datum, afhankelijkheid, klaar-criterium met R-nummers en een testgevallentabel; R8 met de zeven vragen bij naam op MIM 1 en 2; een invulblad en een acceptatietest voor 30 september met de uitkomst onder Public #106; een eigen milestone met einddatum (PM4, PM5, TC4, TC5, TC7, TC9).

## Samenvatting

Het plan is inhoudelijk scherp maar rekent met kalenderdagen, bouwt op bestanden die alleen op open branches bestaan en laat de pijlnummering en de fase-indeling open, waardoor R1 en R2 niet toetsbaar zijn. Modelleur-capaciteit komt een tot twee dagdelen tekort zolang feature 8 volledig en feature 6 in het kritieke pad staan. Sub-issues missen eigenaar, datum en klaar-criterium; de reviews missen testgevallen; de sessie van 30 september mist een acceptatietest en een invulblad. Met de basis op dag één vastgezet, het kritieke pad afgeslankt en de sub-issues aangescherpt is 25 september haalbaar.
