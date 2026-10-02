# Tegenlezing plan voorbeelduitwerking (Public #106), lid kerngroep techniek bij een SIS-leverancier

Gelezen als degene die op 15 september om dit voorbeeld vroeg; mijn product is in OKx-taal SIS, dus KRS plus SVS. Regelnummers (r) verwijzen naar `plan-voorbeelduitwerking.md`; T is de sessie van 15 september; P is Public (`public-wt-102`). Ernst: blokkerend, moet, kan.

## 1. Beantwoordt het plan wat de kerngroep vroeg

| Bevinding | Waar | Ernst |
|---|---|---|
| De vraag was "een opleiding helemaal uitdrukken in dit model" (casus-context r3). Het plan maakt er in r7 een lijn over zes lagen van; dat is wat ik als leverancier wil, maar het is een andere, grotere opdracht dan gesteld, en r20 geeft toe dat voor alles na 1 september de specificatie niets draagt. "Helemaal" wordt dus niet gehaald; zeg dat in de eerste zin van het deliverable, niet pas in de conclusie. | r7, r20 | moet |
| Te veel: acht kaarten met vijf regels (r55), zeven instantietabellen (r27), diagrammen per fase, leemtelijst, toetslijst, en een generator met tests (r54). Voor 30 september volstaan de stappentabel (r36-45), kaart S2 en kaart S4; de rest is naslag na de sessie. r95 zegt dat zelf ("het deck draagt de kern") maar r54-55 bouwen toch alles. | r27, r54-55, r95 | moet |
| Te weinig: "implementatie" is voor mij endpoint, schema en OEAPI-tegenhanger. r86 zet de OEAPI-tegenhanger per endpoint buiten scope; alleen slide 3 (r60) noemt een OEAPI-object, en alleen voor de specificatiefamilie. De objecttype-mapping bestaat al (`informatiemodel-oeapi-mapping.md`, 36 rijen); neem per kaart een kolom OEAPI op, ook als daar "nog niet gemapt" staat. | r60, r86 | moet |
| "Of iedereen het over hetzelfde heeft" toetst het plan alleen tussen documenten (bronnen tegen model), niet tussen leveranciers. Nergens een kolom "uw term" of de vraag "herkent u deze instantie in uw product". Laag 6 §4 stelde die kolom voor; r27 en r56 nemen hem niet over. | r27, r56 | moet |
| Voor SIS dekt de casus precies een berichtstroom (S4, OC-SIS) plus een structuur zonder stroom (S8). Dat is eerlijk opgeschreven in r14 en r45, maar de tabel in r36-45 heeft geen kolom per component; ik moet zelf uitzoeken welke rijen mij raken. | r36-45 | kan |

## 2. Begint het bij het koppelvlak, is het eerste rode pijltje herkenbaar

| Bevinding | Waar | Ernst |
|---|---|---|
| Het eerste rode pijltje (S2, OC-P&R "Opleidingsaanbod aanmaken", r39, slide 1 r60) is herkenbaar en klopt met de uitsnede van de hoofdplaat v1.7. Maar het is niet mijn pijltje: voor een SIS is dat OC-SIS "Nominaal template en resultaatstructuur inrichten" (S4). Slide 1 toont alleen S2; op 30 september zie ik mijn koppeling dus op geen slide. Zet S2 en S4 naast elkaar, of kleur slide 2 per component. | r39, r47, r60 | moet |
| Elke kaart opent met regel 1, de processtap (r26). Dat is opnieuw beginnen bij hoe een school werkt (T,). Open de kaart met de pijl op de plaat en regel 2 en 3 (koppeling, dienst met richting, bericht, patroon); regel 1 als context eronder. | r26 | moet |
| De kolom "Component en dienst" noemt bij S4 "OC-LMS en OC-SIS diensten" en bij S8 "resultaatstructuur (OC-SIS)" zonder dienstnaam en richting. Wat mijn component moet claimen staat alleen in P `studentinformatiesysteem.md` r15-17 (`onderwijsspecificatiestructuur-afnemer`, `resultaatstructuur-afnemer`, `verwerkingsuitkomst-aanbieder`). Die drie namen horen letterlijk in de stappentabel, niet pas in de toetslijst van 24 september (r56). | r41, r45, r56 | moet |
| Het plan schrijft overal SIS; het kaderscenario laat KRS (inschrijven, S3) en SVS (voortgang, S5) apart handelen (laag 1 §2, laag 2 §1). Zonder KRS en SVS in de tabel kan ik S3 en S5 niet op mijn product leggen. | r40, r42 | moet |

## 3. Mijn afhaakpunten langs het plan

| Afhaakpunt | Raakt het plan waar | Wat moet anders | Ernst |
|---|---|---|---|
| Begrippen niet vast vóór de specificatie | 33 objecttypen zonder definitie (r17); het voorbeeld instantieert ze toch (verbintenissen, resultaten in r40, r42, r45) | Per rij markeren "objecttype zonder definitie"; de instantie is dan een vraag, geen aanname (r29 kent alleen aanname, leemte, geparkeerd) | moet |
| Structuur die per document verschilt | Vijf vaste regels per kaart (r26) is goed; het document landt in het pakket informatie- en gegevensmodellen (r55) terwijl de kaarten de koppelingsstructuur volgen | Plek kiezen en in de leeswijzer verantwoorden; ik zoek het naast de koppelingspecificaties | kan |
| Gegevensset zonder verankering | Regel 4 en 5 met gebruiksprofiel (r26) dekken dit; S4 noemt `group` tegen `Plaatsingsgroep` en S8 examenplan als wortel tegen de plaat (r41, r45), beide gemarkeerd in r72, r75 | Volstaat, mits de markering op de kaart staat en niet alleen in sectie 6 | kan |
| Besluit dat alleen in een vergadering leeft | "Geparkeerd op 15 september" (r74) en "afstemmen met Garik en Niels" (r53) verwijzen naar gesprekken | Verwijs naar deck-slide of issue; de uitkomst van 17 september in het issue vóór stap 1 start | moet |
| Story over applicatiefunctionaliteit of schoolbeleid | Regel 1 draagt fase, MORA-proces en journeystap (r26): schoolproces | Regel 1 labelen als context, geen eis; geen story-tekst op de kaart | kan |
| Meerdere koppelvlakken in een review | Drie koppelingen plus vijf leemtegebieden in een document (r36-45); leverancier D vroeg een koppelvlak tegelijk (T) | Een leesroute per component (filter op de stappentabel) en de toetslijst per component als ingang voor leveranciers | moet |
| Nieuwe term zonder uitleg | Leeswijzer en legenda (r55); "aanbieder en afnemer als dienstrichting" (r30) staat in P alleen in `onderwijsspecificatie-inname-afnemer.md` r3 | Die zin op de eerste kaart, niet alleen in de legenda | kan |
| Wat een akkoord betekent | Toetslijst vraagt "welke diensten in aanbieder- of afnemervorm" per component (r56): dat is de claimlijst van leverancier A (T) vóór Ruud en Hans de governance hebben (r96) | Vraag "welke herkent u, wat ontbreekt", niet "welke claimt u"; anders vul ik hem niet in | blokkerend |
| Alleen notificatie waar de praktijk een transactie vraagt | r15 signaleert twee acceptatietoetsen als transactie in notificatievorm; de examenplan-acceptatietoets is OC-SIS, maar verdwijnt in S7 als variant (r44) en staat niet bij de drie vragen (r84) | Als vierde vraag opnemen: transactie (request-reply) of notificatie voor beide acceptatietoetsen | moet |
| Reviewvraag boven de inzet zonder dat iemand het benoemt | r95 benoemt het; de reviews van r57 zijn persona-reviews, de kerngroep krijgt PR en deck pas 26-29 september (r58) | Zie sectie 6 | moet |
| Referentiecomponent niet op mijn product zonder vertaalslag | SIS overal; KRS en SVS nergens (r40, r42) | KRS of SVS noemen met "in Public: SIS" | moet |
| Aanname dat elk component een apart systeem is | S1 "CO naar OC" (r38) en r78 gaan uit van zeven losse componenten; bij mijn klanten zit het curriculum vaak in SIS of LMS | In de leeswijzer: de dienst is de eenheid van claim, niet het component (P Applicatiediensten README r3 zegt dat al) | kan |
| OKx-begrip zonder brug naar mijn termen | `instanties.json` kent objecttype, instantie, bron, aanname, oordeel (r27); geen OEAPI-object, geen kolom eigen term | Beide kolommen toevoegen; de eigen term leeg laten voor de leverancier | moet |
| Afspraak die inperkt zonder winst in beheerlast | Cohort en startdatum van specificatie naar aanbod (r28, r70) | Zie sectie 4 | blokkerend |
| Tempo van wijzigen zonder overzicht per versie | Vijf bewegende bronnen (PR 100 draft, PR 104 open, #234, #235, #105; r92-94) | Eén versieregel bovenaan: pakket 0.0.1, gegevensmodel 0.1.0, model v0.1, PR-stand op datum | kan |
| Zelf administreren zonder dat het mij iets oplevert | Toetslijst (r56) zegt niet wat de kerngroep met de antwoorden doet | Benoemen: input voor het claimmechanisme dat Garik bouwt (T) | kan |
| Vrijheid die er niet is | Alleen GET-endpoints dragen "(optioneel)" (laag 2 §5); de kaart toont per dienst niet verplicht of optioneel voor deze stroom | Kolom verplicht/optioneel per dienst en endpoint op de kaart | moet |
| Zelfde dienstnaam, andere gegevensset | Profielen per koppeling op regel 4 (r26, r41) dekken dit; maar S4 heet "twee koppelingen volledig" (r41) terwijl het eerste bericht van OC-SIS (`specificatie-en-resultaatstructuur-beschikbaar`) en de terugmelding `inrichtingsstatus` geen schema hebben (P `onderwijsspecificatiestructuur-afnemer.md` r25, laag 3 §1) | Dekking S4 voor OC-SIS op "deels" zetten; dat is mijn koppeling | moet |
| Versies per interactie en partij in plaats van per koppeling | Alle elf stromen "1.0" bij pakket 0.0.1 (laag 3 §4); r86 zet versionering buiten scope | Geen stroomversie op de kaart zolang PR 100 draft is; alleen de pakketversie | kan |

## 4. Besluiten en aannames in sectie 6

| Punt (r) | Accepteer ik als aanname | Waarom | Ernst |
|---|---|---|---|
| Cohort en startdatum naar het aanbod (r70) | Nee | Mijn SIS richt het nominale template per cohort in uit de specificatiepayload (P `gebruiksprofielen.md` r17); staat het cohort alleen op het aanbod, dan moet SIS `planbaar-onderwijsaanbod-afnemer` gaan claimen, wat het nu niet doet (P `studentinformatiesysteem.md` r15-17). Dat is een wijziging van OC-SIS, geen delta op een voorbeeld; als vraag stellen met die consequentie erbij | blokkerend |
| Examenplan-wortel presenteren als summatieve resultaatstructuur (r71) | Nee | Ik genereer code uit `result-structure.json`; daar heet de wortel examenplanspecificatie. Het voorbeeld moet het schema volgen en de plaatnaam ernaast zetten, niet andersom | moet |
| OSCE als summatief toetsonderdeel met weging 1 (r73) | Nee | `regels.md` r13 legt weging op de resultaateenheid, het schema op het toetsonderdeel (laag 4 §5.5); welke weging mijn SVS moet aggregeren is een vraag, geen aanname | moet |
| Resultaten op de verbintenis, structuur als vertaaltabel (r69) | Ja, gemarkeerd | Dit is hoe een SVS werkt; maar noem dat de examenverbintenis geen entiteit heeft (#105) en of de structuur per cohort of per student is (#234 punt 4), anders is de aanname half | kan |
| Leeruitkomst een op een per werkproces (r68) | Ja | Mits erbij staat dat dit alleen geldt zolang de instelling geen eigen leeruitkomsten formuleert | kan |
| Een plaatsingsgroep en een cohort (r75) | Ja, gemarkeerd | Voor KRS is de plaatsingsgroep de stamgroep, `GROEP` in het aanbod is een planninggroep; verwijs naar #235 op de kaart | kan |
| Ontbrekende vraag: sleutels | | Welke identificatie reist over de koppeling voor Jochem (specificatie-id plus versie, crebo 23450, kwalificatie 27141) en waaraan hangt KRS de inschrijving; #105.2 noemt het, sectie 6 niet | moet |
| Ontbrekende vraag: verplicht of optioneel | | Per dienst en endpoint in de casus; zonder die markering leest de toetslijst als "alles" | moet |
| Ontbrekende vraag: transactie of notificatie | | Beide acceptatietoetsen (OC-P&R r181, OC-SIS r101); zie sectie 3 | moet |

## 5. De drie vragen in sectie 7

| Vraag | Oordeel | Ernst |
|---|---|---|
| (a) Keuzedeel op specificatie of aanbod, en dus specificatie-id of aanbod-id uit het SKS | Dit is de vraag; KRS registreert de keuzedeelinschrijving op aanbod. Houden | kan |
| (b) Waar landen kennisexamen en onderwijstijd; is aanwezigheid een resultaat binnen scope | De eerste helft raakt SVS direct. De tweede helft is een modelvraag; als koppelvlakvraag stellen: wisselt OKx aanwezigheid uit, of blijft dat intern (aanwezigheidsregistratie is geen component, r14) | kan |
| (c) Welke groepen, en BPV met leerbedrijf en praktijkovereenkomst | Scope-vraag, geen casusvraag; BPV en POK zijn kern in KRS, dus wel stellen, maar apart van de groepen | kan |
| Wat mist | De vraag die ik zou stellen: "wordt de toetslijst de vorm waarin ik opgeef wat ik ondersteun, en wat betekent dat" (T,). En: "is OC-SIS voor Jochems eerste periode compleet, gezien twee berichten zonder schema". Beide belangrijker dan (c) | moet |

## 6. Plan van aanpak in sectie 5: haalbaar vóór 30 september, en lees ik het op tijd

| Stap | Bevinding | Ernst |
|---|---|---|
| 0 (17 september) | Naamkeuze en besluiten in een dag met Garik en Niels; Garik zei dat de namen nog bediscussieerd worden (T). Terugvaloptie (begrippenlijst leidend, r79) is goed; leg die vooraf vast in het issue | kan |
| 1 en 2 (18 tot 24 september) | Generator, controle, tests, acht kaarten, zeven instantietabellen en diagrammen in vijf werkdagen; haalbaar voor de stappentabel, S2 en S4, niet voor het geheel. Minimum vastleggen, rest na 30 september | moet |
| 4 (25 en 26 september) | De reviews zijn persona-subagents, niet de kerngroep; de kerngroep leest niets vóór de PR | moet |
| 5 (26 tot 29 september) | Een PR gestapeld op PR 104, die zelf op PR 100 (draft) staat: drie open PR's in de week vóór de sessie. Dat lees ik niet op tijd. Deck plus kaart S2 en S4 uiterlijk 25 september als losse bijlage bij de agenda; de PR na 30 september | blokkerend |
| Vier delta's op de voorbeeldpayloads (r58, r70) | Onduidelijk of het schema meebeweegt (cohort op de specificatie leeg laten is een voorbeeldwijziging; het veld schrappen is een schemawijziging). Voor code uit schema's is dat het verschil tussen niets doen en een release | kan |

## Oordeel

Neem ik dit voorbeeld mee naar mijn collega's: ja, maar alleen kaart S4 (OC-SIS) met de drie dienstnamen, de stappentabel en de leemtelijst; niet het volledige document, en niet de toetslijst in de vorm van r56. De drie belangrijkste punten:

1. De toetslijst is een claimlijst vóór de governance bestaat (r56 tegen r96). Vragen naar herkennen, niet naar claimen; anders blijft hij bij ons leeg.
2. Twee aannames zijn wijzigingen in mijn koppeling: cohort en startdatum naar het aanbod (r70) en de wortel van de resultaatstructuur hernoemen (r71). Als vraag stellen, met de consequentie voor OC-SIS erbij; en S4 eerlijk op "deels" zetten zolang twee OC-SIS-berichten geen schema hebben.
3. Timing en ingang: deck plus S2 en S4 uiterlijk 25 september los van de gestapelde PR's; in de stappentabel KRS en SVS, dienstnaam met richting, verplicht of optioneel, en een OEAPI-kolom, zodat ik zonder de koppelingspecificatie te openen zie wat mijn product moet doen.
