# Tegenlezing enterprise architect van een instelling: plan voorbeelduitwerking Jochem

Gelezen: de persona, het plan (r1-97), de zes laaganalyses, casus-context, de begrippenlijst en informatiemodel.md (ontwerpkeuzes 1-17, brugtabel) in meta, het kaderscenario leerroute 1 (r289-330, r850-868) in Public en de MORA-definities uit de cache. Ernst: blokkerend, moet, kan. Verwijzingen zijn naar sectie en regel van het plan.

## 1. Semantiek

| # | Bevinding | Plek | Ernst |
|---|---|---|---|
| 1.1 | Het plan gebruikt zelf beide namen voor de dienstlaag: "koppelvlakdienst" (r7, r14, r26) en "applicatiedienst" (r79, r92). r79 maakt de begrippenlijst leidend, maar die dekt alleen objecttypen van het informatiemodel (begrippenlijst r15-17: termen uit de rest van de documentatie vallen buiten deze versie). De bron waarop de keuze steunt kent de term niet. | §3.5 r30, §6 r79 | moet |
| 1.2 | Aanbieder en afnemer verschuiven van dienstrichting naar componentrol: S2 zegt "OC aanbieder, planning afnemer, verwerkingsuitkomst", terwijl planning aanbieder is van planbaar-onderwijsaanbod en verwerkingsuitkomst en OC daarvan afnemer (laag 2, dienstenkaart). r30 belooft precies dit onderscheid. | §4 r39 | moet |
| 1.3 | Drie naamstelsels in een tabel: ankertabel ("Opleidingsverbintenis", r40), plaat ("Opleidingaanbod", "Opleidingsprogramma aanbod", r39) en laag 4 ("education-specification"). r30 zegt: de naam uit de begrippenlijst; die schrijft `Opleiding aanbod  verbintenis`. | §4 r39-45 | moet |
| 1.4 | `Verzoek tot Aanbod` verschuift van betekenis: op de plaat is het de brug van elke specificatie naar aanbod (ontwerpkeuze 13; `Input voor` en `Leidt tot` op acht specificatietypen), dus S2; het plan zet het alleen in S6 als intekening door de student. Laag 3 §5 noemt het event `specificatie-planbaar` in S2 het impliciete verzoek. Een objecttype, twee stappen, geen zin die ze verbindt. | §4 r39, r43 | moet |
| 1.5 | `Inschrijving` staat in S3 naast `Opleidingsverbintenis` als tweede objecttype, terwijl ontwerpkeuze 13 zegt "inschrijven is de verbintenis" en de begrippenlijst `Opleiding aanbod  verbintenis` op MORA `Plaatsing` legt en `Inschrijving` op MORA `Inschrijving` (de overeenkomst, blijft bij het SIS). Twee objecten of twee namen: het plan zegt het niet. | §4 r40 | moet |
| 1.6 | Cohort in drie betekenissen: het MORA-object `Cohort / periode` (studenten onder dezelfde OER), de tekenreeks "2026" op het aanbod (r70) en "cohort 120" als capaciteit (scenario 1.1). "Periode 1" en "periode 7" zijn planningsperioden van tien weken zonder objecttype (#234 punt 19), niet de periode uit `Cohort / periode`. r16 noemt "cohort als object" een leemte, r28 maakt er een tekenreeks van. | §2 r16, §3.3 r28, §4 r34, §6 r70, r75 | moet |
| 1.7 | `Plaatsingsgroep` wordt in S4 gelijkgesteld aan de payload `group`, terwijl de brugtabel zegt: dezelfde rol, niet dezelfde inhoud (naam met capaciteit tegenover verzameling personen). Stamgroep, lesgroep, planninggroep en BPV-cluster (r75) worden tot een instantie samengetrokken. | §4 r41, §6 r75 | moet |
| 1.8 | Resultaat en beoordeling: r69 en r84 laten "kennisexamen behaald" en de OSCE op de verbintenis landen zonder te zeggen of `Summatief resultaat` of `Summatieve beoordeling` wordt geïnstantieerd; de begrippenlijst (r71-72) scheidt ze naar MORA, de casus niet (#234 punt 12). De aanname "alleen resultaat" uit laag 5 staat niet in §6. | §6 r69, r73; §7 r84 | kan |
| 1.9 | "SIS" verbergt de knip die het kaderscenario maakt: KRS is bron van persoon en verbintenis (LR1 r884), SVS van resultaat en voortgang (r890). Voor S3, S5 en S8 is dat de vraag welke bronregistratie levert; het plan noemt KRS en SVS nergens. | §4 r40-45 | moet |

## 2. Koppeling aan MORA

Regel 1 met alleen het MORA-hoofdproces (r26) volstaat niet: het hoofdproces zegt welke keten, niet welk bedrijfsproces, welk informatieobject en welke referentiecomponent. Zonder die drie maakt elke instelling de vertaling zelf, en dus anders.

| Wat erbij moet | Waar | Uit de MORA-cache | Ernst |
|---|---|---|---|
| MORA-bedrijfsproces per stap, naast het hoofdproces | regel 1, r26 | S1 Definieren onderwijs-programma, Definiëren opleidings onderdelen; S2 Vertalen onderwijsvisie naar onderwijsaanbod, Vaststellen opleidingen aanbod; S3 Aanmelden, Intake en plaatsen, Plaatsen student; S4 Clusteren leeractiviteiten; S6 Formuleren leervraag, Aanmelden keuzedelen; S8 Opstellen examen plan, Uitvoeren examen, Beheren summatieve resultaat structuur | moet |
| MORA-informatieobject per instantierij, uit de mapping in de begrippenlijst (r104-177), ook "geen tegenhanger" | instanties.json, r27 | Aanmelding, Inschrijving, Plaatsing (bij `Opleiding aanbod  verbintenis`), Cohort / periode, Leervraag (bij `Verzoek`), Aangeboden opleiding, Leeractiviteit, Examen deelname; `Plaatsingsgroep`: geen | moet |
| MORA-referentiecomponent naast elke OKx-component | regel 2, r26 | OC = Onderwijscatalogus; R = Roostersysteem; SIS = Kernregistratie systeem studenten (KRS) en Student volg systeem (SVS), apart; intake = Intake systeem en Aanmeld systeem; examen = Toets- en examenplanning- en inschrijfsysteem, Toets- en examen afname systeem; P, CO en SKS: tegenhanger te toetsen (hoofdplaat: SKS "nog niet in MORA") | moet |
| Ketenpartijen die MORA kent en het plan niet: CAMBO (aanmelding, persona r14), RIO, ROD, SBB (BPV), als kolom "buiten OKx, wel in de keten" | §4 r40, r45 | Koppelvlak CAMBO aggregeert Aanmelding en Plaatsing; Koppelvlak RIO aggregeert Aangeboden opleiding | kan |
| De MORA-versie noemen (kaderscenario r295: hoofdprocesmodel 2.6 van 12-05-26) en klus 53 als brug naar HORA | leeswijzer, r55 | | kan |

## 3. Nieuwe objecttypen tegenover bestaande structuren

| Objecttype | In mijn architectuur gedragen door | Vraag die het voorbeeld moet stellen in plaats van de aanname in §6 | Ernst |
|---|---|---|---|
| `Aanmelding` | Bestaand: MORA Aanmelding in intake en KRS, via CAMBO | Is de aanmelding keuzedeel (LR1 r861: SKS is bron) dezelfde structuur als de aanmelding opleiding, of een verbintenistoestand op keuzedeelaanbod? r43 zet haar onder `Verzoek tot Aanbod`. | moet |
| `Inschrijving` | Bestaand: de overeenkomst in KRS; niet uitgewisseld, wel de plaatsing die eruit volgt | Wisselt OKx de inschrijving uit of alleen de verbintenistoestand (MORA Plaatsing)? Zo alleen de toestand: waarom een eigen objecttype in de familie verbintenis, en waarom als specialisatie (`wordt`) van `Aanmelding` in plaats van een toestand? | moet |
| `Verzoek tot Aanbod / Intekening op specificatie` | De planopgave van OC naar planning is in mijn integratielaag een event (`specificatie-planbaar`), geen object; de intekening van de student is MORA Leervraag en Persoonlijke leerroute in het SVS | Is het verzoek een object met sleutel en toestand, of het startevent van aanbod maken; en is de planopgave hetzelfde object als de studentintekening? Twee dingen onder een schuine streep. | moet |
| `Plaatsingsgroep` | Drie bestaande structuren met drie eigenaren: stamgroep (KRS), planninggroep (planning), lesgroep (rooster) | Welke groep is bron van welke registratie, en wisselt OKx lidmaatschap uit of alleen capaciteit (payload `group`)? Dat is meta #235; r75 neemt "een plaatsingsgroep" aan en verbergt de vraag. | moet |
| `Cohort / periode` | Bestaand: cohortjaar als attribuut van de inschrijving in KRS plus de OER-versie; geen eigen object | Is cohort een sleutel op aanbod en verbintenis of een object; en is de versie van de resultaatstructuur niet al de sleutel die MORA via de OER legt (ontwerpkeuze 17)? r16 en r28 spreken elkaar tegen. | moet |

## 4. Generaliseerbaarheid

| Bevinding | Plek | Ernst |
|---|---|---|
| Het plan noemt hbo, HORA en klus 53 nergens; de begrippenlijst zegt "HORA nog niet onderzocht" (r17). De vraag of het model buiten het mbo werkt krijgt geen antwoord, ook geen "nog niet". | §1-8 | moet |
| Drie lagen lopen door elkaar zonder markering: model (families, leeruitkomst als sleutel, resultaatstructuur), mbo-sectorkader (kwalificatiedossier, kerntaak, werkproces, keuzedeel, keuzedeelruimte, BPV, examenplan, OER, BOL en BBL als opsomming in laag 4) en instellingsinrichting (cohort 2026, vier perioden van tien weken, keuzedeel elke derde periode, eenheid gelijk aan kerntaakblok terwijl ontwerpkeuze 4 het niveau vrijlaat, leeruitkomst een op een per werkproces, OSCE weging 1, 120 studenten, lokaal 2.14). De aanname-markering (r29) onderscheidt die drie niet. | §3.4 r29, §4 r34, §6 r68, r73, r75 | moet |
| instanties.json (r27) krijgt objecttype, instantie, bron, aanname en oordeel. Voeg het veld "laag" toe (model, sectorkader, inrichting) en laat de generator per laag een tabel maken; dan is zichtbaar dat de uitsnede geen model is. | §3.2 r27, §5 r54 | moet |
| Leeruitkomst een op een per werkproces (r68) is mbo-inrichting: in het hbo komen leeruitkomsten uit een opleidingsprofiel zonder werkprocessen. Als aanname goed; als "vertaling van het kwalificatiekader" bakt het de mbo-structuur in ontwerpkeuze 2. | §6 r68 | kan |
| Keuzedeel en keuzedeelruimte als specialisatie van de programmaspecificatie (ontwerpkeuze 12) hebben in het hbo een tegenhanger (minor, vrije keuzeruimte) met andere regels; het tweede blad (r34, r74) moet die als vraag meenemen, niet als mbo-model. | §4 r34, §6 r74 | kan |

## 5. Onderhoudslast en herleidbaarheid

| Bevinding | Plek | Ernst |
|---|---|---|
| instanties.json herhaalt waarden die al in voorbeeldpayloads.md staan (r28: de payloads zijn al Jochems opleiding, id 79736830 en verder). Twee plekken voor een instantie is de derde bron van waarheid die r27 zegt te vermijden. Laat instanties.json alleen verwijzen: objecttype naar (bestand, id of JSON-pointer) in de payloads of (bestand, regel) in het kaderscenario; de generator lost op en kopieert niet. | §3.2 r27, §3.3 r28 | moet |
| Bron in meta (r54), gegenereerd document in Public (r55): generatie over twee repositories heen, terwijl de Public-scripts (build-release, check-conventies) instanties.json niet kennen. Public draagt al kopieën van informatiemodel.md en begrippen.md (laag 4 §4); dit wordt de derde. Leg vast welk bestand bron is, welk afgeleide, en waar de generator draait. | §5 r54-55, r58 | moet |
| Geen eigenaar en geen vastgezette versie (versie-pin) na 30 september: r94 zegt de versie van het model te noemen, niet dat de controle faalt zodra informatiemodel.json, begrippen.json of release.json wijzigt. Zonder pin veroudert het voorbeeld stil, terwijl #234 (26 punten) en #235 open staan. | §8 r94 | moet |
| Minimale controleset, grotendeels al voorgesteld in laag 4 §6 en laag 5 §6: (1) elk objecttype binnen scope uit informatiemodel.json heeft precies een rij of een gemarkeerde leemte; (2) elke naam en familie komt uit begrippen.json; (3) elke verwijzing lost op: id in de payloads na vertaling via DutchName en validatie tegen schemas/, regel in het kaderscenario met de geciteerde term; (4) relaties met twee instanties worden getekend en het aantal lege kanten is een vaste verwachting (nu 32), zodat drift zichtbaar wordt; (5) versie-pin op de drie bronnen. Meer niet; een aparte diagramgenerator per fase (r54) is een tweede generator en dus tweede onderhoud. | §5 r54 | kan |
| Delta 4 (r28: cohort en startdatum van specificatie naar aanbod) wijzigt een voorbeeld in Public op een punt waar laag 3 (entiteit `..._DOELGROEP`, velden cohort en startdatum) nog anders zegt. r86 belooft niet te specificeren door voorbeeld; dit is het wel. Markeer de delta als signalering naar #234 punt 6 en #105, niet als stille wijziging. | §3.3 r28, §5 r58, §7 r86 | moet |

## 6. Afhaakpunten uit de persona

| Afhaakpunt | Raakt het plan | Waar | Wat anders moet | Ernst |
|---|---|---|---|---|
| Koppelvlak zonder afbakening van componenten en verantwoordelijkheid | Ja: eigenaarschap van de specificatie als aanname (OC bezitter per U3) terwijl LR1 r857 en r878 CO als bron zetten en OC als "deelt en verwijst"; SIS zonder KRS/SVS-knip; intake en examenafname geen component | §6 r78; §4 r40, r45 | Per stap een kolom "bronregistratie volgens LR1 r872-890" naast de U3-bezitter; waar ze verschillen een vraag, geen aanname | moet |
| Aannames over de inrichting van een instelling | Ja: een OC, een planning, een SIS, een plaatsingsgroep, een cohort; delta 3 laat de organisatie-eenheid weg, het enige handvat voor meerdere locaties (LR1 r289: "een vorm, vele varianten") | §3.3 r28, §6 r75 | Zin in de leeswijzer: een exemplaar per referentiecomponent is een aanname van de uitsnede, geen modelregel; organisatie-eenheid aanvullen, niet weglaten | moet |
| Geen relatie met MORA of MOSA | Ja, zie 2: alleen het hoofdproces; MOSA komt nergens voor | §3.1 r26 | Drie MORA-kolommen | moet |
| Begrip dat per document verschuift | Ja, zie 1.1 tot 1.7: vijf begrippen verschuiven binnen de tabel van §4 zelf | §4, §6 | Naamkwesties beslissen voorafgaand aan het voorbeeld, niet erin; de tabel in §4 eerst op een naamstelsel zetten | blokkerend |
| Model dat alleen binnen het mbo werkt | Ja, zie 4 | §4, §6 | Laagmarkering en een HORA-kolom "nog niet onderzocht" | moet |
| Nieuw objecttype waar een structuur volstond | Ja, zie 3: Inschrijving, Verzoek, Plaatsingsgroep, Cohort | §6 r75, r79; §4 r40, r43 | De vier vragen stellen, de aannames schrappen | moet |
| Onderhoudslast zonder drager | Ja, zie 5 | §5, §8 | Eigenaar, versie-pin, verwijzen in plaats van kopiëren | moet |
| Besluit zonder onderbouwing | Ja: OSCE weging 1 (r73) zonder bron voor de weging; een plaatsingsgroep (r75) zonder bron; begrippenlijst "leidend" (r79) terwijl die v0.2 concept is en het informatiemodel "ter bekrachtiging" | §6 r73, r75, r79 | Per aanname de bron, of "geen bron, keuze van het voorbeeld" | kan |

## Oordeel

Nee, in deze vorm is het voorbeeld niet als toetssteen te verdedigen in mijn architectuurraad. Na drie ingrepen wel, en dan is het een bruikbare toetssteen omdat de leemtes eerlijk zichtbaar blijven (r29, r86).

1. MORA in de instantietabellen: bedrijfsproces per stap, informatieobject per rij, referentiecomponent per OKx-component, met KRS en SVS apart. Zonder dat blijft de vertaling naar de eigen doelarchitectuur bij de lezer en oordeelt elke raad over een ander plaatje.
2. Begrippen vastzetten voorafgaand aan het voorbeeld en het plan er zelf aan houden: een naam voor de dienstlaag; `Opleiding aanbod  verbintenis` tegenover `Inschrijving` en MORA `Plaatsing`; `Verzoek tot Aanbod` als event of als object, en in welke stap; cohort in een betekenis. Nu verschuiven vijf begrippen binnen de tabel van §4.
3. Drie lagen markeren (model, mbo-sectorkader, instellingsinrichting) in instanties.json, met eigenaar, versie-pin en verwijzen in plaats van kopiëren. Anders wordt de uitsnede van Jochem het model, en groeit naast begrippen.json en informatiemodel.json een derde bron die niemand draagt.
