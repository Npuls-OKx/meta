# Laag 6: de verbinding over de lagen heen en de vorm voor de kerngroep techniek

Analyse bij Public #106 (voorbeelduitwerking Jochem), 16 september 2026. Bronnen: de sessie van de kerngroep techniek van 15 september, het deck `presentaties/src/260915_kerngroep_techniek_afspraken.md` (slides op naam), de schets `platen/concept-uitleg-business-architectuur.png`, de persona's onder `.agents/personas/`, en de documenten in Public (worktree public-wt-102) en meta (worktree wt-232).

Bron van de uitspraken: de sessie van de kerngroep techniek van 15 september; deelnemers van leveranciers zijn geanonimiseerd als leverancier A tot D, de OKx-teamleden staan bij naam.

## 1. Lagenstapel en naden

| Laag | Draagt de laag | Naad naar de laag eronder: vastgelegd in | Wat ontbreekt |
|---|---|---|---|
| Proces: MORA-ketens, leerroute, studentreis, instellingsreis | Kaderscenario `leerroute-1-regulier.md` (MORA-hoofdprocesmodel r. 500-522; instellingsreis fasen 1-8 r. 291; studentreis r. 56); `persona_jochem.md` (studentjourney en instellingsjourney per stap) | Naar stories: kolom Bron in `stories.md` en `features.md` verwijst naar scenario 1.1-1.4, persona Jochem en het kaderscenario (bv. feature-0012, story-0004, story-0013). Naar de plaat: sectie "Procesfasen, interacties op de plaat, informatie" (r. 909) noemt per fase welke pijlen oplichten | Geen kolom fase of MORA-proces in de boom (MORA komt 1 keer voor in `features.md`, 0 keer in `stories.md` en `epics.md`). De fase-uitsneden gebruiken de plaat `OKx_LR1_informatiestromen_v20260526`, de koppelvlakspecificatie de hoofdplaat v1.7; nergens vastgelegd dat het dezelfde stromen zijn |
| Stories en features (requirementsboom) | `stories.md`, `features.md`, `epics.md`, ADR 0025 (besluit 3: stories eindigen bij de techniek) | Naar berichtstroom: kolom "Ingevuld door" in `stories.md`; terug: sectie "Stories" in elke koppelingspecificatie (OC-P&R r. 11-23) | 19 van de 32 stories dragen "geen" in Ingevuld door; de leveranciers lezen de rest als applicatiefunctionaliteit (deck slide "Review op v0.0.2") |
| Bouwsteen en koppelvlakdienst (schets Niels) | Alleen de png en de sessie; geen document in meta of Public | Schets: Userstories OKx naar PoC casus/Bouwsteen naar Koppelvlakdienst en Koppeling; Generieke userstories naar Features OKx. Niek noemt `onderwijsspecificatiestructuur-aanbieder` en `-afnemer` als voorbeeld van een koppelvlakdienst | De gelijkstelling koppelvlakdienst = applicatiedienst staat nergens; Garik noemt ze "applicatiediensten binnen het koppelvlak, niet op applicatieniveau zoals in het plaatje van Niels". "APP dienst", "Sector dienst" en "Informatiemodel flow" uit de schets hebben geen artefact |
| Applicatiecomponent | `Applicatiecomponenten/*.md` (7 componenten: CO, OC, planning, rooster, SIS, LMS, SKS) met koppelvlak-view op hoofdplaat v1.7 | Lijst "Applicatiediensten" en "Koppelingen" per component; tabel "Geïmplementeerd door" in de koppelingspecificatie (OC-P&R r. 25-38) | Intakesysteem, aanwezigheidsregistratie en toets-/examenafname uit de fasen 3, 4, 5 en 8 van het kaderscenario zijn geen component in Public; SIS is "KRS en SVS samen" (inleiding, afkortingen) terwijl het kaderscenario KRS en SVS apart laat bewegen |
| Koppelingspecificatie | `Koppelingspecificaties/*.md` (OC-P&R, OC-SIS, OC-LMS) | Secties Plek in de keten (uitsnede hoofdplaat), Stories, Applicatiediensten, Interactiepatronen, Procesbeeld, Berichtstromen | Geen kort ID (Public #107, leverancier A); geen verwijzing naar de fase van de instellingsreis; alleen drie van de stromen op de hoofdplaat zijn gespecificeerd |
| Berichtstroom | Sectie per stroom: Doel, Trigger, Initiator, tabel Versie / Interactiepatronen / Applicatiediensten, Endpoints, sequentiediagram (OC-P&R r. 73-113) | Naar dienst en patroon: de tabel; naar payload: de endpoint-lijst verwijst via de dienst naar het schema | Het onderscheid informeren versus transactie (leverancier A) staat niet per stroom; de versie per stroom (PR 100) is nog draft |
| Applicatiedienst | `Applicatiediensten/*.md` (28 pagina's, 14 paren aanbieder/afnemer) | Verplichtingen, endpointtabel met Request en Response naar `schemas/*.json`, Gebruikt in | README Koppelvlakspecificaties belooft "welk doel uit de requirementsboom dat bereikt"; de dienstpagina `onderwijsspecificatiestructuur-aanbieder.md` noemt geen feature of story |
| Interactiepatroon | `Interactiepatronen/*.md` in rollen bezitter en consument; U3 bepaalt de rol per resource | README: twee onderscheidingen (draagt het event genoeg; wie begint) | Geen leidraad per doel zoals leverancier C vraagt; U4 zet event notification onder "vrijwel elke uitwisseling" (inleiding, kernbegrippen), wat leverancier A als eenzijdig leest |
| Endpoint | Endpointtabel bij de dienst; `auth-standaard.md` | Response-kolom naar schema; statuscodes | Geen OEAPI-tegenhanger per endpoint (leverancier A; Niek "techniekagnostisch, we gaan mappen") |
| Datamodel laag 3 en 4 | `logisch-gegevensmodel.md` (secties Onderwijsspecificatie, Onderwijsaanbod, Resultaatstructuur en examenplan, plus een sectie per koppeling), `schemas/` (24 bestanden), `voorbeeldpayloads.md`, `gebruiksprofielen.md` | Naar laag 2: brugtabel "Naar het logisch gegevensmodel" in `informatiemodel.md`; naar koppeling: `gebruiksprofielen.md` per koppeling | Families verbintenis en resultaat, formatieve structuur, `Aanmelding`, `Inschrijving` en `Cohort` hebben geen entiteit (brugtabel, slotalinea); examenplan is in laag 3 nog de wortel van de resultaatstructuur, in laag 2 buiten scope (brugtabel, rij `EXAMENPLANSPECIFICATIE`) |
| Informatiemodel laag 1 en 2 | `informatiemodel.md` (7 families, 17 ontwerpkeuzes), `begrippen.md`, `informatiemodel.json` (66 objecttypen, 156 relaties), OEAPI-mapping | Naar proces: de tabel "Beantwoordt de vraag" per familie; de ankertabel in het kaderscenario (r. 556-600) per niveau van het kwalificatiekader | De ankertabel en de inleiding van de koppelvlakspecificatie kennen zes families ("beoogde leeruitkomst"), de plaat zeven (`Onderwijskundig kader instelling`, `Resultaatstructuur`); de labels in de fase-teksten (`opleidingsprogramma-verbintenis`) zijn niet gelijkgetrokken met de objecttypen op de plaat |

Drie naden dragen de casus en zijn het zwakst vastgelegd: proces naar story (geen fase in de boom), story naar bouwsteen naar dienst (alleen een schets met twee namen voor hetzelfde), en laag 2 naar laag 3 voor verbintenis en resultaat (geen entiteiten). De naden koppelingspecificatie naar berichtstroom naar dienst naar endpoint naar schema zijn wel vastgelegd, maar alleen voor de drie OC-koppelingen.

## 2. Wat de kerngroep nodig heeft om het te volgen

| Wie | Vraag of afhaakpunt | Minuut |
|---|---|---|
| leverancier A | "We zijn applicaties aan het beschrijven en geen koppelvlak"; wachten tot koppelingsniveau; hoeveel tijd in stories | |
| leverancier A | Wat betekent een PR goedkeuren; "veel sterkere mening als het puur over het koppelvlak gaat"; "we gaan te weinig naar het koppelvlak toe" | |
| leverancier A | Stories die het koppelvlak beschrijven, of stories over hoe de wereld eruit kan zien | |
| leverancier A | "Totdat we echt over de koppelvlakken praten blijft dit lastig"; "het eerste rode lijntje"; nieuwe terminologie toelichten | |
| leverancier A | Toetst berichtstroom aan eigen voorbeelden: "validatie van een keuzedeel", "vrijgeven van een opleiding" | |
| leverancier A | OKE-ervaring: het endpoint associatie "kon 200 dingen betekenen"; wil de dienst beperkt tot de context, niet het hele OEAPI-endpoint |- |
| leverancier A | Indruk dat leveranciers niet meebepalen; permanent of running target |, |
| leverancier A | "Wij zijn [product] en ondersteunen deze applicatiediensten in aanbieder- of afnemervorm, is dat de lijst?" | |
| leverancier A | Alleen event notification in de stories; functioneel: informeren (al gebeurd) versus transactie (controle of het kan); event-driven is duurder |, |
| leverancier A | Korte naam per koppelingspecificatie | |
| leverancier A | Versionering: "het werk is hetzelfde, het lijkt complexer"; per interactie en partij versies bijhouden; genereert code uit schema's; wil versie op koppelingsniveau, maximaal een achterlopen |- |
| leverancier A | Liften mee met OEAPI: die dicteert versies en endpoints; "je stelt dat het datamodel niet in OEAPI is uitgedrukt" |- |
| leverancier A | Informatiemodel: eerst vrijgeven om te bekijken, dan toelichting | |
| leverancier C | Waarom applicatie-eisen beschrijven; ontwikkeltijd; "impact veel te groot om je doel te bereiken" |- |
| leverancier C | Bottom-up vanuit bestaande koppelingen en top-down naar elkaar toe |- |
| leverancier C | Governance op papier; keuzedelen kiezen als eerste; "liever een manier die werkt dan de mooiste"; niet "te ver weg gefantaseerd" | |
| leverancier C | Ongemak: akkoord op PR of story wordt in de sector "dat moet gemaakt worden" | |
| leverancier C | Aanbieder versus afnemer: als de aanbieder iets niet ondersteunt staan afnemers stil; "die vrijheid is er niet"; "ja tegen 90% van jullie werk dat leidt tot 10% specificatie" |- |
| leverancier C | OKE-ervaring: besluiten genomen, buiten spel; dichter op de bal notificatie, verder weg ophalen en vergelijken; leidraad per doel |, |
| leverancier C | Scope: keuzedeel kiezen, OC-P&R en OC-SIS eerst; hoe groeit dat naar LMS; hoe gaat het verder met de feedback |, |
| leverancier D | Stories soms gedetailleerd soms algemeen; alle koppelvlakken tegelijk; eerst een koppelvlak; tijdsbesteding ver boven de afspraak | |
| leverancier D | "Hoe groot de broek"; verwachtingen dat het systeem dit moet kunnen; "wij waren koppelvlakken aan het neerzetten" | |
| leverancier D | Aansluiten op een koppelvlak dwingt geen werking van de applicatie af; wanneer zit iets in OKx als geen leverancier het wil; "losknip-actie" |- |
| leverancier D | Wat bedoel je met applicatiediensten; zijn endpoints de applicatiediensten; dienst is keuze uit endpoints; endpoints OKx-breed of per specificatie |,-, |
| leverancier D | Wat is een datamodel en hoe verhoudt het zich tot de berichtstroom; "een veldje erbij zit toch ook in de berichtstroom" |- |
| leverancier B | Leeswijzer bij de PR was prettig | |
| leverancier B | Beeldvorming bij scholen: "OKx-compliant, dus jij ondersteunt deze stories"; aanbesteding | |
| leverancier B | Commitment op een story is functionaliteit inbouwen; een story die zegt wat een school vindt is niet te reviewen |, |
| leverancier B | Zelfde dienst `onderwijsspecificatiestructuur-afnemer` voor P&R en KRS met een andere dataset "lijkt me ingewikkeld" |- |

Vertaald naar eisen aan de voorbeelduitwerking:

| Eis | Bron |
|---|---|
| E1 Begin bij de koppeling op de plaat, niet bij de story; het eerste rode pijltje is een pijl op de hoofdplaat, met de koppeling ernaast | leverancier A, leverancier D |
| E2 Een koppeling per stap zichtbaar, ook al volgt de leesroute de casus (Niels: "vanuit een casus", niet vanuit een koppelvlak) | leverancier D, Niels |
| E3 Per stap: component, dienst in aanbieder- of afnemervorm, bericht, patroon | leverancier A, leverancier D, leverancier B |
| E4 Elke term uitgelegd waar hij voor het eerst valt: koppelvlak, koppeling, berichtstroom, applicatiedienst, interactiepatroon, datamodel, objecttype | leverancier A, leverancier D, |
| E5 Per berichtstroom: informeren of transactie, en waarom dat patroon | leverancier A, leverancier C |
| E6 Scheiding tussen wat OKx vastlegt (de dienst op het koppelvlak) en wat de applicatie doet (context, geen eis) | leverancier D,; leverancier B; Niek |
| E7 De leverancierslijst: welke diensten claimt component X voor deze casus | leverancier A, Garik |
| E8 Per endpoint het OEAPI-object, of de markering "nog niet gemapt" | leverancier A,; Niek |
| E9 Per regel de status: vastgesteld, voorstel, leemte; niets impliciet permanent | leverancier A, Garik |
| E10 Kort ID per koppeling zodra #107 dat oplevert; tot dan de volledige naam | leverancier A |
| E11 Kort, een document, leeswijzer vooraan; de reviewlast ligt al boven de afspraak | leverancier D, leverancier B |
| E12 Het document vraagt feedback op de casus, geen akkoord op stories; wat "ja" betekent ligt bij Ruud en Hans | leverancier C, leverancier A, deck slide "Afspraken 15 september" |
| E13 Soll-min: alleen wat Jochem in leerroute 1 nu doorloopt; varianten (scenario 1.2-1.4) buiten de hoofdlijn | leverancier C, Niels |

## 3. Rode draad voor de casus Jochem: dezelfde vijf regels per stap

Voorstel: elke stap van Jochems traject toont dezelfde vijf regels. Regel 1 processtap (fase van de instellingsreis uit het kaderscenario, MORA-keten, journeystap van Jochem); regel 2 component en dienst (aanbieder of afnemer); regel 3 berichtstroom en patroon; regel 4 payload of entiteit (schema laag 4, entiteit laag 3, gebruiksprofiel); regel 5 objecttype op de plaat (familie). De fasen komen uit `leerroute-1-regulier.md` r. 909-1016, de journeystappen uit `persona_jochem.md`.

| Stap | Regel 1 proces | Regel 2 component en dienst | Regel 3 berichtstroom en patroon | Regel 4 payload of entiteit | Regel 5 objecttype | Leemte |
|---|---|---|---|---|---|---|
| S1 Fase 1 ontwerpen (onzichtbaar voor Jochem) | CO naar OC; MORA onderwijsontwikkeling | `onderwijsspecificatie-inname-aanbieder`/`-afnemer` bestaan | Geen koppelingspecificatie CO-OC | `education-specification.json`, `ONDERWIJSSPECIFICATIE`, `LEERUITKOMST` | `Kwalificatiedossier`, `Kwalificatie`, `Kerntaak`, `Werkproces`, `Leeruitkomst`, `Opleiding specificatie` tot `Toetsonderdeel specificatie`, `Keuzedeelruimte` | Regel 3 leeg; de geneste boom Apothekersassistent (kaderscenario r. 1017-1120) is herbruikbaar voor regel 5 |
| S2 Fase 2 publiceren en planbaar maken | OC naar planning; MORA onderwijslogistiek | OC `onderwijsspecificatiestructuur-aanbieder`, planning `-afnemer`, `planbaar-onderwijsaanbod-aanbieder`, OC `verwerkingsuitkomst-afnemer` | OC-P&R "Opleidingsaanbod aanmaken": Event Notification plus Asynchronous Request-Reply (r. 73-113) | `education-specification.json` (profiel OC-P&R: zonder leeruitkomsten), `education-offering.json`, `processing-status.json`; `AANBODINSTANTIE` | `Opleiding specificatie` naar `Opleidingaanbod`, `Opleidingsprogramma aanbod` | Alle vijf regels vulbaar |
| S3 Fase 3 orienteren, aanmelden, intake, plaatsing | OC naar intake, intake naar KRS; journeystappen Orienteren, Aanmelden, Inschrijven | Geen: intakesysteem is geen component; `verbintenistoestand-aanbieder`/`-afnemer` bestaan zonder koppeling | Geen | Geen entiteit voor `Aanmelding`, `Inschrijving`, verbintenis (brugtabel) | `Verzoek tot Aanbod`, `Aanmelding`, `Inschrijving`, `Opleidingsverbintenis`, `Persoon`, `Student`, `Plaatsingsgroep` | Regel 2, 3, 4 leeg; regel 5 raakt de geparkeerde intekenvraag (deck slides "Positionering intekenen" en "Verbintenissen bestaan alleen op aanbod") en #105, #235 |
| S4 Fase 4 detailleren, roosteren, eerste rooster en LMS-toegang | OC naar LMS, OC naar SIS, planning naar rooster, KRS naar LMS; journeystap Informeren | OC-LMS en OC-SIS: diensten per koppelingspecificatie; rooster draagt geen endpoints | OC-LMS "Leeromgeving inrichten en leermiddelkoppeling melden"; OC-SIS "Nominaal template en resultaatstructuur inrichten"; planning naar rooster alleen als context (OC-P&R r. 289) | `education-specification.json` (profielen OC-LMS, OC-SIS), `result-structure.json`, `GROEP` | `Leeronderdeel specificatie`, `Leergelegenheid`, `Plaatsingsgroep`, `Summatieve resultaat structuur` | Vulbaar voor OC-LMS en OC-SIS; groepen, rooster en toegang leeg; `GROEP` versus `Plaatsingsgroep` open (brugtabel) |
| S5 Fase 5 studeren, voortgang | LMS naar SVS (formatieve resultaten); journeystappen Studeren, BPV, Studievoortgang | `behaalde-leeruitkomst-aanbieder`/`-afnemer` bestaan zonder koppeling | Geen | `ONDERWIJSRESULTAAT` alleen in een koppelingsbeeld | `Leergelegenheid verbintenis`, `Leergelegenheid resultaat`, `Toetsgelegenheid verbintenis`, `Formatieve resultaat structuur` | Regel 3 en 4 leeg; BPV heeft geen objecttype (#105) |
| S6 Fase 6 keuzedelen kiezen | OC naar SKS, SKS naar planning, planning naar KRS; journeystap Kiezen keuzedelen | SKS-component bestaat; `keuzeregelset`, `kiesbaarheidsbepaling`, `onderwijsaanbod-zoekvraag`, `onderwijsaanbod-haalbaarheidstoets` bestaan | Geen koppelingspecificatie; ADR 0015 (request for offering) | `rule-set.json`, `REGELSET`; keuze-requirements in meta | `Keuzedeel`, `Keuzedeelruimte`, `Student keuze regelset`, `Verzoek tot Aanbod` (geparkeerd) | Regel 3 leeg; dit is de stap die leverancier C als eerste werkende manier wil |
| S7 Fase 7 bijsturen | KRS naar planning, planning naar OC en rooster | OC-P&R diensten | OC-P&R "Opleidingsaanbod herplannen", "Specificatiestatus gewijzigd melden", "Acceptatietoets bij late wijziging" | `education-specification-delta.json`, `specification-status-changed.json` | `Opleidingsprogramma aanbod` | Voor Jochem regulier (happy flow) niet aan de orde; hoort bij scenario 1.2-1.4 (E13) |
| S8 Fase 8 examineren, diplomeren | Examenafname naar SVS, SVS naar KRS; journeystappen Examineren, Uitstroom, Diploma | `resultaatstructuur-aanbieder`/`-afnemer` (OC-SIS) | OC-SIS "Acceptatietoets bij wijziging examenplan" raakt Jochem niet; resultaatregistratie en diplomering zonder koppeling | `result-structure.json` met examenplan als wortel (tegenspraak met laag 2) | `Examenonderdeel specificatie`, `Examengelegenheid`, `Examengelegenheid resultaat`, `Summatieve resultaat structuur`, `Waarde document` | Regel 3 leeg voor de registratie; regel 4 spreekt regel 5 tegen |

Volgorde. Begin bij S2: de uitsnede `highlight_oc_p_en_r_informatiestromen_hoofdplaat_v1_7.png` met de pijl "1: event specificatie planbaar" uit het procesbeeld (OC-P&R r. 56-66) is het eerste rode pijltje, en het is de enige stap waar alle vijf regels uit bestaande artefacten komen; het deck gebruikte dezelfde stroom als voorbeeld (slide "Voorbeeld uit de koppelvlakspecificatie"). Daarna S4 (twee koppelingen, zelfde patroon), dan S1 en S3 als "het model draagt het, de specificatie nog niet", dan S6 als de geparkeerde vraag, en S5, S7, S8 als leemtelijst. De chronologie van Jochem blijft de indeling van de stappentabel; de uitgewerkte kaarten volgen de volgorde van volledigheid.

## 4. Vormvoorstel

| Artefact | Inhoud | Leesvolgorde |
|---|---|---|
| A Leeswijzer met legenda | De vijf regels, de statuskleuren (vastgesteld, voorstel, leemte), de zeven termen op de plek waar ze eerst vallen (E4, E11) | 1 |
| B Document in Public naast `informatiemodel.md` (per #106: `Informatie-en-gegevensmodellen/`) | Casus in drie zinnen; de stappentabel S1-S8; per stap een kaart met de vijf regels; de leemtelijst; de toetslijst | 2 |
| C Ingevulde plaat | Geen bewerking van `model.archimate` (instanties zijn geen objecttypen; harde regel 1). Per fase een uitsnede als mermaid, gecontroleerd tegen `informatiemodel.json` zodat ongebruikte objecttypen zichtbaar worden (#106) | 3, per stap |
| D Sequentiediagrammen | Hergebruik uit OC-P&R, OC-SIS, OC-LMS (bv. OC-P&R r. 88-113); voor S1, S3, S5, S6, S8 geen nieuw diagram, want dat zou specificeren door voorbeeld (U1, leverancier C) | 3, per stap |
| E Instantietabel per familie (7) | Kolommen objecttype, instantie Jochem (Apothekersassistent, crebo 23450, kwalificatie 27141 uit kaderscenario r. 1019), entiteit laag 3, schema laag 4, OEAPI-object, status | 4 |
| F Toetslijst voor leveranciers | Per component (OC, planning, SIS, LMS, SKS) de diensten in aanbieder- of afnemervorm voor deze casus, de berichtstromen, de schemaversie; de drie vragen uit #106; en de zin dat een antwoord feedback is, geen commitment (E12) | 5 |

Deck 30 september, hoogstens vijf slides:

| Slide | Kern |
|---|---|
| 1 Het eerste rode pijltje | Uitsnede OC-P&R met fase 2 van Jochem; de vijf regels ingevuld voor die ene stap |
| 2 Acht stappen, een tabel | S1-S8 met kleur: vol, deels, alleen objecttype; zo ziet de kerngroep waar de specificatie staat |
| 3 Van objecttype naar instantie | Familie Onderwijsspecificatie met de boom Apothekersassistent en de brug naar entiteit, schema en OEAPI-object |
| 4 Wat het model niet draagt | Aanmelding en inschrijving zonder entiteit; examenplan versus summatieve structuur; plaatsingsgroep; verzoek tot aanbod geparkeerd; als vragen, geen aannames |
| 5 Gevraagd | De toetslijst per component; de drie vragen; wat "ja" hier betekent, met verwijzing naar Ruud en Hans |

Toets aan de persona's. Primaire lezer: `lid-kerngroep-techniek.md` met de accenten van `lid-technische-werkgroep-leverancier.md` (de vier sprekers zijn leveranciers; leverancier A "wij zijn [product]"). De README-regel "kies de lezer met de grootste afstand" wijst voor de toetslijst (F) naar `softwarearchitect-leverancier.md`; voor regel 1 leest de `bop-procesbespecialist.md` mee.

| Persona | Afhaakpunt uit het bestand | Wat de uitwerking daarop moet doen |
|---|---|---|
| Lid kerngroep techniek | "Gegevensset zonder verankering in de ankertabel"; "structuur die per document verschilt" | Zes versus zeven families expliciet maken (regel 5); dezelfde vijf regels in elke kaart |
| Lid technische werkgroep, leverancier | "Referentiecomponenten niet op zijn product te leggen"; "OKx-begrippen zonder brug naar zijn termen"; "aanname van precies een exemplaar" | SIS als KRS en SVS benoemen; kolom voor de eigen term open laten in tabel E; meta #80 als bekende beperking noemen |
| Softwarearchitect bij een leverancier | "Begrip zonder definitie"; "eis zonder interactie, interactie zonder endpoint"; "schema zonder voorbeeldpayload"; "ontbrekende foutpaden" | Link naar `begrippen.md` per objecttype; leemtes markeren in plaats van invullen; een ingevulde payload voor S2; foutpaden uitdrukkelijk buiten scope zetten |
| Enterprise architect van een instelling | "Geen relatie met MORA"; "begrip dat per document verschuift" | MORA-keten in regel 1 (het kaderscenario heeft hem, de boom niet); koppelvlakdienst en applicatiedienst als een term benoemen |
| Informatiearchitect | "Twee namen voor hetzelfde begrip" | `opleidingsprogramma-verbintenis` (ankertabel) tegenover `Opleidingsprogramma verbintenis` (plaat) zonder entiteit: in tabel E zichtbaar maken |
| Onderwijskundig procesbespecialist | "Systeemtaal in de verhaallijn" | Regel 1 in onderwijstaal houden; de andere vier regels zijn techniek en mogen dat zijn |

## 5. Persona-aanvullingen

| Persona | Rubriek | Aanvulling | Bron |
|---|---|---|---|
| Lid kerngroep techniek | Kennis | Kent OKE en OEAPI uit implementatie en toetst elke afspraak aan wat daar misging ("associatie kon 200 dingen betekenen"; "besluiten genomen, buiten spel") | leverancier A, leverancier C |
| Lid kerngroep techniek | Leesdoel | Welke diensten moet ik in aanbieder- of afnemervorm ondersteunen; is dit permanent of een running target | leverancier A, |
| Lid kerngroep techniek | Afhaakpunten | Story die applicatiefunctionaliteit of schoolbeleid beschrijft; meerdere koppelvlakken in een review; nieuwe term zonder uitleg; reviewlast boven de afspraak; onduidelijk wat een akkoord betekent | leverancier A, leverancier C, leverancier D, leverancier B, leverancier A, leverancier C |
| Lid kerngroep techniek | Belangen (rubriek ontbreekt nu) | Tempo tegenover zekerheid ("we willen door, maar willen weten of dit permanent is"); eerst een werkende manier voor keuzedelen kiezen | leverancier A, leverancier C |
| Lid technische werkgroep, leverancier | Belangen | Een akkoord op een story mag niet als functionaliteitsbelofte gaan gelden, ook niet in aanbestedingen; bottom-up vanuit bestaande koppelingen; liever werkend dan mooi | leverancier B,; leverancier C, |
| Lid technische werkgroep, leverancier | Kennis | Genereert code uit schema's, dus elke schemaversie ernaast kost code; kent de kosten van event-driven (timeouts, herstel) tegenover request-reply | leverancier A, |
| Lid technische werkgroep, leverancier | Afhaakpunten | Vrijheid die er niet is (dienst optioneel genoemd terwijl de tegenpartij hem nodig heeft); een dienstnaam met een andere dataset per afnemer; versies bijhouden per interactie en per partij; alleen event notification | leverancier C-; leverancier B; leverancier A, |
| Lid technische werkgroep, leverancier | Leesdoel | Welke van de 25 diensten claim ik en hoe geef ik dat op | leverancier A, Garik |
| Softwarearchitect bij een leverancier | Kennis | "Kent OEAPI mogelijk gedeeltelijk" klopt niet voor deze groep: zij verwachten dat OKx meelift op OEAPI en dat het datamodel erin is uitgedrukt | leverancier A- |
| Softwarearchitect bij een leverancier | Leesdoel | Per bericht: informeren of transactie; welk patroon is per doel geeigend | leverancier A, leverancier C |
| Softwarearchitect bij een leverancier | Afhaakpunten | Een generiek endpoint zonder beperking tot de context van de dienst; per endpoint bijhouden welke schemaversies hij ondersteunt; datamodel als los begrip zonder verhouding tot de berichtstroom | leverancier A-,; leverancier D |

Aparte persona "product owner leverancier": niet nu. De rol staat al als onderliggende rol in `lid-kerngroep-techniek.md` (tabel Onderliggende rollen) en in de rolbeschrijving van `lid-technische-werkgroep-leverancier.md`; wat op 15 september afwijkt zijn belangen (commitment, aanbesteding, roadmap: leverancier B,; leverancier C "of dat op roadmaps kan"), niet kennis of leesdoel. Die belangen passen in de aanvullingen hierboven. Heroverwegen zodra Ruud en Hans de governance-aanpak opleveren; dan krijgt "wat betekent ja" een eigen leesdoel.

Aparte persona "PoC-school": ja, maar niet voor 30 september. Niels maakt de PoC-scholen tot bron van stories en tot lezer van de generieke story en bouwsteen (-: zeven scholen, sessie met Ferda op 16 september; vertaling naar generieke story). Geen bestaande persona dekt het leesdoel "herken ik mijn casus en mijn applicatielandschap in de generieke story"; `vertegenwoordiger-instelling-werkgroep.md` (README-rij: "afspraken die bij de praktijk van zijn school passen") komt het dichtstbij en kan als basis dienen, met als afhaakpunten "OKx-compliant lezen als functionaliteitsbelofte" (leverancier B) en "een story zonder terugkoppeling of de leverancier hem haalbaar vindt" (Niels). De voorbeelduitwerking heeft deze persona niet nodig; het kaderscenario is een fictieve casus, geen school.

## 6. Risico's en aannames voor het plan

| Kan tot 30 september | Kan niet tot 30 september |
|---|---|
| Document B met stappentabel en leeswijzer; kaart S2 volledig; kaarten S4 en S7 op bestaande berichtstromen | Koppelingspecificaties voor intake, SKS, SVS en diplomering (S3, S5, S6, S8); sequentiediagrammen daarvoor |
| Instantietabellen voor de families specificatie, aanbod en resultaatstructuur (laag 3 en 4 bestaan); de boom Apothekersassistent hergebruiken uit kaderscenario r. 1017-1120 | Entiteiten voor verbintenis, resultaat, aanmelding (brugtabel: nog niet gebrugd) |
| Leemtelijst en toetslijst; OEAPI-kolom uit `informatiemodel-oeapi-mapping.md` per objecttype | OEAPI-mapping per endpoint; antwoord op versionering; koppeling-ID (#107: "kernteam werkt voorstel uit") |
| Vijf slides | Besluit over intekenen en verzoek tot aanbod; plaatsingsgroep (#235); examenplan in laag 3 ("vervanging in voorbereiding") |

| Afhankelijkheid | Risico | Beperking |
|---|---|---|
| Garik: PR 100 is draft; de namen berichtstroom, applicatiedienst, koppelingspecificatie "worden bediscussieerd"; versie per berichtstroom; versioneringsvoorbeeld op een associatie-endpoint (deck slide "Prioritering") | Regel 2 en 3 van het voorbeeld bevriezen namen die nog schuiven | Per kaart de stand van PR 100 op datum noemen; geen eigen namen introduceren |
| Niels: stories opnieuw ophalen bij zeven PoC-scholen, generieke stories, bouwstenen, MORA-koppeling per story-,; story of feature is pas af als de leverancier haalbaar zegt | Regel 1 (fase uit het kaderscenario) en Niels' bouwstenen lopen uiteen; stories in het voorbeeld ogen als af | Regel 1 op de fasen van het gereleasede kaderscenario; kolom bouwsteen leeg laten tot Niels levert; stories alleen via "Ingevuld door" |
| PoC-scholen: Jochem is een kaderpersona; de scholen brengen eigen casussen | Vraag "welke school is dit" | Casus als kaderscenario labelen, niet als school |
| Ruud en Hans: governance-aanpak na 30 september (deck slide "Afspraken 15 september") | Toetslijst wordt als commitmentvraag gelezen | Zin over feedback versus commitment in A en F; geen akkoordvraag in het deck |
| Kerngroep: reviewcapaciteit onder druk (leverancier D; leverancier A "september drukke maand"); PR 104 staat nog open | Het voorbeeld wordt niet gelezen voor 30 september; v0.1 van het model verschuift door #234 (26 punten), #235, #105 | Omvang begrenzen; het deck draagt de kern; versie van het model per kaart noemen |
| Twee plaatversies (kaderscenario 20260526 met fase-uitsneden f1-f8; koppelvlakspecificatie hoofdplaat v1.7 met koppeling-uitsneden) | Pijl op de ene plaat is niet herleidbaar op de andere | v1.7 kiezen (leidend per README) en per stap de fase-uitsnede als context, niet als bron |

Besluiten die de uitwerking niet kan omzeilen, met de stap waar ze vallen:

| Besluit | Stap | Stand |
|---|---|---|
| Intekenen op specificatie en het objecttype `Verzoek tot Aanbod` (ontwerpkeuze 13) | S3, S6 | Geparkeerd op 15 september; "komt terug met de voorbeelduitwerking" (deck slides 17a en 17a2). Het voorbeeld moet beide lezingen tonen of leemte markeren |
| Examenplan als wortel (laag 3) tegenover summatieve resultaatstructuur (laag 2, ontwerpkeuze 10) | S4, S8 | Brugtabel: "laag 2 en 3 spreken elkaar tegen" |
| `Plaatsingsgroep` tegenover `GROEP` | S3, S4 | Brugtabel: open; meta #235 |
| Lifecycle, sleutels en BPV van verbintenissen | S3, S5, S7 | Public #105 |
| Zes of zeven families in ankertabel en inleiding | Regel 5 overal | Niet geagendeerd; inleiding koppelvlakspecificatie zegt "zes begrippenfamilies" |
| Koppelvlakdienst (Niels) is applicatiedienst (Garik) | Regel 2 overal | Alleen in de sessie, |
| Informeren of transactie per berichtstroom | Regel 3 overal | U4 zet event notification als standaard; leverancier A vraagt het functionele onderscheid; het voorbeeld kan alleen signaleren waar een transactie waarschijnlijk is (haalbaarheidstoets, acceptatietoets) |
| OEAPI-tegenhanger per endpoint en versionering ten opzichte van OEAPI | Regel 4 overal | Niek: "we gaan dat mappen"; Garik: "die link moeten we nog leggen" |
| Kort ID per koppeling | Regel 3 overal | Public #107, voorstel in voorbereiding |
