---
name: okx-oeapi-scenario-uitwerking
description: >-
  Schrijft en scherpt kaderstellende scenario's voor de OKx leerroute-uitwerking af:
  Npuls-leerroutes, multi-actor (student + instelling), MORA- en
  architectuurlagen, begrippenkader (specificatie / aanbod / verbintenis /
  resultaat), AMIGO-volgorde en verwijzing naar het specificatiedocument.
  Gebruik bij scenario-analyse, §3.x scenario-uitwerkingen, leerroute 1–9,
  happy flow en incidentele tempo-varianten, of wanneer de gebruiker OKx,
  OC, leerroute-uitwerking of Npuls-leerroutes in scenario-vorm wil
  uitwerken.
---

# OKx scenario-uitwerking (leerroute-uitwerking)

## Bron van waarheid

- Primair document: `architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md`.
- Werk **binnen** de definities en nummering van dat document; verzin geen parallelle begrippenlijst naast OKx/OEAPI/MORA.
- **OEAPI-kern** wijzigen doet het profiel niet: gaps → signalering / change request (zoals in §1.4 van het profiel).

## Keuzedelen

- Verplicht onderdeel van mbo; afgesloten met examen.
- Voor **niveau 4**: **720 SBU** keuzedeelruimte (verwijs naar S-BB waar relevant).
- **Geprioriteerde voorkeurslijst** met (periode, locatie); maximaal **één actieve inschrijving** per keuzedeelruimte in het onderwijsprogramma.
- Geen passend aanbod → ruimte kan **leeg** blijven → actieve signalering (studievertraging).
- Drie instellingsbeleidsvarianten voor het moment van aanmelding: uiterlijk periode *t* vóór de ruimte; definitief bij intake; voorlopig bij intake (met loop 8f).

## Taal en toon

- **Nederlands**; volledige zinnen; toegankelijk voor bestuurders en onderwijskundigen, precies genoeg voor API- en ketenspecialisten.
- **Niet te technisch:** schrijf voor onderwijsprofessionals én bouwers; introduceer termen als CSP of NP-Hard alleen als **verdieping**, nooit als ingang.
- **Concept-eerst, verdieping daarna:** hoofdtekst conceptueel; technische details in expliciete *voor wie dieper wil*-blokken.
- **Onderwijsplannen** (canonieke formulering): *een invulling van alle open vragen waarbij alle regels tegelijk kloppen*.
- **Leesregel planproces:** *goed beschrijven → goed plannen → goed instelling-breed plannen → goed roosteren*.
- Onderscheid bewust:
  - *Student journey* (oriënteren → aanmelden → intake → inschrijven → volgen → toetsen → kwalificeren).
  - *Instellings journey* (ontwerp, publicatie, planbaar en geroosterd aanbod, intake/plaatsing, uitvoering, examinering, diplomering).
- Gebruik **vaste sectortermen**: kwalificatiekader, onderwijsspecificatie, onderwijsaanbod, onderwijsverbintenis, onderwijsresultaat (zoals de vlakken-/ankertabel in het document).
- Vermijd testjargon als hoofdlijn (“Given/When/Then” alleen als interne structuur, niet als dominante koppen tenzij de gebruiker dat expliciet wil).

## MORA en architectuurkaders

- **MORA** (mbo-referentiearchitectuur) is het proces- en sectorreferentiekader: [MORA Hoofdpagina](https://mora.mbodigitaal.nl/index.php/Hoofdpagina).
- Leg bij “wat doet de instelling?” expliciet de link met **MORA-hoofdprocessen / procesketens** (in het document o.a. keten 3 uitvoering & begeleiding, keten 4 onderwijslogistiek, keten 6 onderwijsontwikkeling). Doel: **§2.2 implicatie 1 — werken onder architectuur** invullen, geen school-eigen parallelle werkelijkheid.
- **ROSA** positioneren als nationaal architectuurknooppunt waar relevant; sector-RA’s (waaronder MORA) blijven de uitlegbaarheid dragen.

### Randvoorwaarden per scenario — negen concern-dimensies (EA / SA)

Het profiel gebruikt in §3.4.0 een vaste **checklist van negen randvoorwaarden** (in het sjabloon letterlijk: Business / Strategy / Motivation / Beleid / Organisatie / Proces / Informatie / Data / Systeem). Dat is **geen** vervanging van het **kern-laagmodel van ArchiMate** (Strategy, Business, Application, Technology — plus Motivation en Implementation & Migration als uitbreidingen). Het is wél **verenigbaar** met gangbare enterprise- en solution-architectuur als **stakeholder- en preconditie-dimensies**: van strategie en governance tot proces, informatie/data en inzetbare systemen.

Gebruik per dimensie **kort** wat al besloten, geregeld of beschikbaar moet zijn voordat het scenario uitvoerbaar is.

| Dimensie (profiel) | Plaatsing in gangbare EA / SA |
| --- | --- |
| **Business** | Business context: wie is de waarde-ontvanger, welke dienst/product, welke uitkomst (business outcome). |
| **Strategy** | Strategische keuzes en portfolio: welke richting, welke prioriteit t.o.v. andere initiatieven. |
| **Motivation** | Drivers, doelen, architecture principles, expliciete requirements (ArchiMate *Motivation*). |
| **Beleid** | Governance en normenkaders: regels, compliance, examen-/onderwijsbeleid waar het scenario aan moet voldoen. |
| **Organisatie** (in uitwerking ook *organisatie-inrichting*) | Operating model: rollen, verantwoordelijkheden, mandaten, capaciteit (organisatiearchitectuur). |
| **Proces** | Bedrijfsprocessen en samenhang (BPMN, MORA-ketens): wie doet wat, in welke volgorde, welke handover. |
| **Informatie** | Informatiearchitectuur op **betekenisniveau**: welke informatie-objecten, semantiek, kaders voor uitwisseling. |
| **Data** | Data-architectuur: identificatie, herkomst, kwaliteit, persistentie, integratie-afspraken (naast “betekenis”). |
| **Systeem** | Solution / technology: applicaties, koppelvlakken, infrastructuur, beschikbaarheid en non-functionals die de keten dragen. |

**Scheiding Informatie vs Data:** *Informatie* = wat betekent het voor de keten en de actor; *Data* = hoe wordt het technisch en beheerbaar vastgelegd en uitgewisseld. Die split komt overeen met veel EA-praktijk (conceptueel/logisch vs. fysiek en contracten).

**Solution architecture:** zoom bij **Systeem** (en waar nodig **Data**) in op concrete services, API’s en integratiepatronen — alleen voor zover het profiel of een gelinkte specificatie dat toestaat. Onderscheid **koppeling** (gestandaardiseerde stroom) en **koppelvlak** (endpoints); verzin geen koppelvlakdetails zonder vastgelegde koppeling.

## Informatiestromen, koppelingen en koppelvlakken

Drie lagen — van concept naar bouwbaar contract:

| Laag | Definitie | AMIGO-stap | Release-relevantie |
| --- | --- | --- | --- |
| **Informatiestroom** | Conceptuele gegevensbeweging tussen ketenpartners/systemen: wie levert welke informatie aan wie, en in welk processtadium. Zichtbaar op de OKx-informatiestromenplaat en in scenario-uitwerkingen. | Scenario-analyse (stap 1); input voor gegevens- en interactie-analyse | Milestone 3 dekt de OC P-stromen (CO→OC, OC↔planning, planning↔rooster) voor LR1–LR3. |
| **Koppeling** | Gestandaardiseerde **realisatie/implementatie** van één of meer informatiestromen: afspraken over berichten, interactiepatronen en semantiek — nog **zonder** de volledige endpoint-set. | Interactie-analyse + berichtspecificatie (stap 3–5) | Milestone 3 / meta **`v0.1.0`** levert eerste gestandaardiseerde koppelingen; zie [`doc/OKx_Release-management-en-versionering.md`](../../../doc/OKx_Release-management-en-versionering.md) §8. |
| **Koppelvlak** | Technische uitwerking van een koppeling: het geheel van **endpoints** waarmee de koppeling in software wordt gebouwd. Eén koppelvlak kan meerdere endpoints omvatten. | Interfacespecificatie (stap 6) in de **spec**-repo | Volgt **nadat** koppelingen gestandaardiseerd zijn; compleet bij meta **`v1.0.0`**. |

**Werkvolgorde:** informatiestromen beschrijven in scenario's → koppelingen standaardiseren → op basis daarvan koppelvlakken (endpoints) bouwen in spec. Verwijs in scenario's expliciet naar **welke informatiestroom** wordt geraakt; benoem nog geen endpoint-details tenzij de gebruiker om koppelvlakuitwerking vraagt.

## AMIGO en keten naar specificatie

- Volg de **AMIGO**-logica uit het profiel: na de scenario-analyse volgen **gegevensanalyse** en **interactieanalyse** (parallel of iteratief), daarna **technologiekeuze**, vervolgens **berichtspecificatie** en **interfacespecificatie**, tot een **afsprakenset**.
- **Informatiestromen** in een scenario zijn daarmee niet alleen een plaatje: ze vormen de **brug** naar die analyses. Wat je hier vastlegt (welke gegevens over welke lijn, welke interactie tussen welke partijen) is de **leg-up** voor latere technische detaillering — zonder nu al volledige payloads of stack-keuzes te hoeven vastleggen, tenzij de gebruiker dat expliciet vraagt.
- Scenario’s zijn **kaderstellend**: ze voeden informatiestromen, testideeën en interactiepatronen; ze zijn geen losse anekdotes.

## Npuls-leerroutes en scenario-taxonomie

- Negen leerroutes zoals Npuls: standaard (1 regulier, 2 temporiseren, 3 versnellen), personaliseren (4–6), modulair (7–9).
- **IST vs SOLL (organisatie-maturiteit, geen waardeoordeel):** voor veel instellingen vormen **leerroute 1–3** de herkenbare **IST**: grotendeels **sterk aanbod-gestuurd** onderwijs (vaste of duidelijk afgebakende trajecten en cohorten), met bij 2 en 3 vooral **tempo- en spreidingsvarianten** op hetzelfde type logistiek. **Leerroute 4–9** zijn voor diezelfde instellingen vaak **SOLL**: meer personalisatie, modulair samenstellen, grenzen over, of vraag-gestuurde aanvullingen — dat vraagt **andere processen, data en ketensamenwerking** dan “klassiek cohort + catalogus”.
- **Vergelijk altijd met de reguliere baseline:** beschrijf leerroute **2 t/m 9** expliciet **tegen** **leerroute 1 (regulier, sterk aanbod-gestuurd)** als referentie: wat blijft gelijk (specificatie, aanbodstadia, verbintenis, examenketen), wat wijzigt in **sturing**, **rollen**, **informatiestromen** en **randvoorwaarden**? Maak de *delta* begrijpelijk voor lezers die route 1 als norm hebben.
- Per leerroute minimaal onderscheiden:
  - **Happy flow / nominaal verloop** (alles volgens ontwerp).
  - **Incidenteel temporiseren, incidenteel versnellen, incidenteel hybride** — deze drie + happy flow zijn **herbruikbaar over alle leerroutes**; de leerroute blijft gelijk, de voortgang wijkt tijdelijk.
  - **Route-specifieke scenario’s** (bijv. leerroute 1: overstap met resultaten meenemen; andere routes: eigen lijst uit het document of issue).
- **Onderwijslogistiek / sturingsmodel** expliciet maken waar het scenario daar door beïnvloed wordt (niet elke leerroute is hetzelfde “aanbod-eerst”-plaatje):
  - **Sterk aanbod-gestuurd** (zoals bij leerroute 1 in het profiel): vooraf ontwikkeld en gepland aanbod; student kiest uit wat er is. **Hybride kenmerken**: bij uitzondering aanvullend aanbod op aanvraag, vaak **gepoold / gebatched** tot een drempel — individuele verzoeken zijn beperkt haalbaar.
  - **(Meer) vraaggestuurd**: leervraag of persoonlijk pad leidt; instelling reageert met (her)planning en aanbodcreatie. Relevanter voor **flexibelere leerroutes** (personaliseren 4–6, modulair 7–9, en route 2/3 waar maatwerk/tempo centraal staat). In het profiel komt dit o.a. terug bij **vraag-gestuurd aanbod** en de signalering rond `RequestForOffering` (geen volledige OEAPI-kern; wel keten-/koppelvlakdenken).
  - **Hybride**: bewuste mix — groot deel van het curriculum **aanbod-gestuurd** (cohorten, vaste perioden), met **vraag-gestuurde** aanvullingen waar flex of herstel dat vereist. Benoem welk deel van de keten welk sturingsprincipe volgt (ontwerp, planbaar aanbod, roostering, intake, herplanning).
  - Koppel waar passend aan **`curriculumType`** (`nominaal` / `flexibel` / `hybride` in het profiel): het beïnvloedt of tracks vast zijn of de student (binnen regels) combineert — relevant voor scenario’s op leerroute 4–9 en voor keuze-/trajectscenario’s.

## Actoren en organisatie

- Scenario’s zijn **multi-perspectief**: naast de student de rollen die de keten dragen — primair uit het profiel en de **Instellingsjourney**: onderwijsontwerper, onderwijsontwikkelaar, planner, roosteraar, coach/SLB’er, docent, examinator, examenbeoordelaar, examencommissie, BPV-/praktijkbegeleiders, surveillanten, en waar relevant **bestuur / strategie** (besluit opleiding aanbieden, portfoliokeuzes).
- **Keten en systemen** benoemen waar het scenario dat raakt (zoals in het profiel/ArchiMate-stromen): o.a. **Onderwijscatalogus (OC)** als distributiepunt, curriculum-ontwerptool, planningssysteem, rooster, **SKS/SVS** (aanbod–student–verbintenis), LMS, toets-/examenketen — zonder koppelvlakdetails te verzinnen die niet in het document staan.
- Gebruik het **organogram**-denkbeeld: instelling → domeinen → onderwijsteams (teamleider, docenten, ontwerpers, ontwikkelaars); daarnaast **team onderwijslogistiek** (planner, roosteraar), **team onderwijsbegeleiding** (coach, SLB’er), **team onderwijsondersteuning** (BPV, examinatoren, surveillanten), **examencommissie** (voorzitter, secretaris, leden uit opleidingsteams). Bij **SOLL-routes (4–9)** explicieter: wie krijgt **meer besluit- en afstemlast** (bijv. planning op deelnemer, modulebundels, externe partners)?
- **IST vs SOLL op de organisatiekaart:** bij scenario’s op **1–3** vooral aantonen dat bestaande rollen en MORA-ketens **ingezet worden zoals nu**; bij **4–9** ook welke **nieuwe of zwaardere samenwerkingspatronen** (tussen teams, met sector, met studentregie) nodig zijn om de SOLL te realiseren.

## Informatieobjecten (keten)

- **Doel:** scenario’s moeten bijdragen aan **semantische consistentie** in het hele profiel en in de keten: dezelfde begrippen, dezelfde objecten en dezelfde grenzen tussen *specificatie*, *aanbod*, *verbintenis* en *resultaat* — ongeacht leerroute of actorperspectief. Daarmee blijven informatiestromen, testcases en koppelvlakbesprekingen **onderling vergelijkbaar** en sluiten ze aan op MORA- en OEAPI-taal zonder team-eigen herinterpretatie.
- Hanteer de documentlogica:
  - **Wat / hoe / toetsing** → onderwijsspecificatie (inclusief leeruitkomsten, werkproces- en lesniveau).
  - **Organiseerbaarheid** → onderwijsaanbod (planbaar vs geroosterd waar het document dat onderscheidt).
  - **Deelname en administratie** → onderwijsverbintenis (OEAPI: `Association` / state waar het profiel dat zo noemt).
  - **Resultaat** → minimaal state; rijkere evidence/LO-bewijsvoering alleen binnen profielgrenzen of als expliciete extensie/koppelvlak zoals het document aangeeft.
- Gebruik de **ankertabel / cardinaliteiten** in het document als normatieve referentie bij “wat hoort op welk niveau?” — geen synoniemen voor dezelfde entiteit zonder expliciete koppeling aan het model.

### Cyclus van plannen

- **Strategisch jaarplan** (hele instelling) én **opleidingscurriculum** als template over de opleidingsduur; zodra de student leert, wijkt het persoonlijke plan af en moet het jaarplan meebewegen.
- Onderscheid **vóór** en **na** startweek: grof plan op grofmazige specificatie rijpt mee; na start lopen **keuzemomenten** (fase 6) en **bijsturen** (fase 7) met **cumulatieve trendlijnen** t.o.v. het initiële jaarplan.
- **Grofmazig vs gedetailleerd planbaar** is een rijpheidscontinuüm op `onderwijsspecificatie`, geen strak binaire stap.

## Uitwerkingssjabloon (inhoudelijk)

Werk een scenario uit met minimaal:

1. **Titel + leerroute** (Npuls-nummer en naam).
2. **Persona** (één doorlopende casus is voldoende tenzij anders gevraagd).
3. **Uitgangssituatie (“given”)**: cohort, track, reeds gepubliceerd aanbod, relevante constraints; bij leerroute **2–9** ook de **relatie tot de reguliere (route-1-)baseline** (IST/SOLL, sturingsmodel).
4. **Trigger (“when”)**: wat verandert er (moment, besluit, incident)?
5. **Actorflow**: wie doet wat in welke volgorde (student + instelling + systemen waar relevant).
6. **Eindbeeld voor deze paragraaf**: richt je op **start van onderwijsuitvoering** (of andere in het document vastgelegde mijlpaal), niet automatisch op “na drie jaar gediplomeerd” tenzij het scenario daar expliciet om vraagt.
7. **Randvoorwaarden — negen concern-dimensies** (profiel §3.4.0; zie hierboven voor EA/SA-lijntrekking): korte bullets per dimensie.
8. **Informatiestromen + AMIGO-voorloper** (leg-up voor technologiekeuze, berichtspecificatie en interfacespecificatie):
   - **Beeld / verwijzing**: placeholder of verwijzing naar hoofdplaat / latere figuur — geen verzonnen koppelvlakdetails die niet in het profiel staan.
   - **Gegevensanalyse** (kader, nog geen volledige berichtdefinitie): welke informatieobjecten (ankertabel, OEAPI-profieltermen) bewegen in dit scenario; richting **producerend → consumerend**; welke sleutels of referenties minimaal nodig zijn om het verhaal te laten kloppen; welke semantiek **niet** mag vervagen.
   - **Interactieanalyse** (kader, nog geen koppelvlak/endpoints): welke **actoren/systemen** welke **handelingen** uitwisselen; welke **koppelingen** (gestandaardiseerde realisaties van informatiestromen) ontstaan; **publish vs event vs pull** alleen benoemen als het scenario dat nodig heeft; welke koppelingen nieuw zijn t.o.v. de route-1-baseline.
   - **Doorverwijzing AMIGO:** deze analyses voeden **technologiekeuze** → **berichtspecificatie** (koppelingen) → **interfacespecificatie** (koppelvlakken/endpoints) → **afsprakenset**. Houd het scenario-document op **analyse-niveau**, tenzij het team expliciet om bericht-/interfacedetail vraagt.

## Governance (repository)

- OKx-meta: issues en PR’s; **alleen OKx-team merge**; link PR aan issues (`Fixes #…` / `See also #…`). Zie `.cursor/rules/okx-governance.mdc`.

## Visueel

- **Mermaid** mag voor processen, journeys en overzichten; houd ID’s onderhoudbaar (`camelCase` met betekenisvolle naam).
- Diagrammen **alleen** bij echte cyclische of complexe processen; informatiestructuur en scenario-taxonomie werken vaak **beter als tabel** (Npuls-routes × varianten).
- Diagrammen **niet herscheppen** als de gebruiker vraagt om “intact laten” — alleen labels/ID’s of tekst eromheen aanpassen.
- Als een mermaid op een breed scherm niet leesbaar is, **verkies tabel** boven een breder diagram.
- Kleurgebruik consistent met MORA-procesketens en ArchiMate-lagen waar het document dat al doet; **geen nieuwe expliciete `fill:`-styling** in mermaid tenzij het bestaande diagram dat al heeft (theme-default werkt ook in dark mode).

## Checklist vóór afronden

- [ ] **Bron en scope:** aansluiting op de leerroute-uitwerking en nummering; geen parallelle begrippenlijst naast OKx/OEAPI/MORA; OEAPI-kern niet ter plekke “oplossen” (gaps → signalering / change request).
- [ ] **Perspectieven:** *student journey* én *instellings journey* / multi-actor meegenomen waar het scenario dat raakt; relevante **ketenpartners en systemen** (o.a. OC, SKS/SVS, planning, rooster, LMS) alleen benoemd voor zover het profiel dat ondersteunt.
- [ ] **Informatieketen en semantiek:** specificatie ↔ aanbod ↔ verbintenis ↔ resultaat consequent volgens **ankertabel en cardinaliteiten**; geen synoniemen zonder expliciete mapping naar het model.
- [ ] **Scenario-taxonomie:** happy flow en incidentele varianten (temporiseren / versnellen / hybride) correct t.o.v. **route-specifieke** scenario’s.
- [ ] **Sturing en curriculum:** aanbod-gestuurd / vraaggestuurd / hybride benoemd waar relevant; **`curriculumType`** (`nominaal` / `flexibel` / `hybride`) alleen waar het scenario dat raakt.
- [ ] **IST / SOLL en baseline:** waar nuttig positionering (“veel instellingen”: **1–3** IST, **4–9** SOLL); voor leerroute **2–9** expliciete **delta t.o.v. route 1** (regulier, sterk aanbod-gestuurd) in keten, rollen, data en sturing.
- [ ] **MORA:** link met relevante **procesketens** waar “wat doet de instelling?” centraal staat (§2.2 — werken onder architectuur).
- [ ] **Negen concern-dimensies** (profiel §3.4.0): ingevuld als randvoorwaarden; **niet** verwarren met het **ArchiMate-kern-laagmodel** noch met het **andere negenvlaks-informatiemodel** (specificatie/aanbod/verbintenis) uit het profiel.
- [ ] **Informatiestromen → koppelingen → koppelvlakken:** benoemde stromen kloppen met de informatiestromenplaat; koppelingen als gestandaardiseerde realisaties; **geen** endpoint-/koppelvlakdetails tenzij expliciet gevraagd.
- [ ] **Informatiestromen + AMIGO-voorloper:** beeld of verwijzing + **gegevensanalyse** + **interactieanalyse** op kader-niveau; brug naar koppelingen en (later) koppelvlakken leesbaar.
- [ ] **Mijlpaal eindbeeld:** op de in het profiel bedoelde plek (bijv. **start onderwijsuitvoering**), niet ten onrechte einddiplomering.
- [ ] **Figuren:** Mermaid-ID’s onderhoudbaar (`camelCase`); bestaande diagrammen niet herscheppen tenzij de gebruiker dat vraagt.
- [ ] **Toon:** concept-eerst, technische diepte in *voor wie dieper wil*-blokken; geen mermaid die niet leesbaar is op een breed scherm.
- [ ] **Governance:** PR gekoppeld aan issues waar van toepassing (`.cursor/rules/okx-governance.mdc`).
- [ ] **Traceerbaarheid:** verwijzing naar relevante **§** of **issue** voor vervolgwerk.
