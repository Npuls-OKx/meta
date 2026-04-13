# Architectuur- en ontwerpprincipes (OKx-meta)

**Status:** Voorstel
**Datum:** 2026-04-09
**Consolidatie:** Zie [ADR 0006](../../../dr/0006-consolidatie-architectuurprincipes.md) voor de afwegingen en besluiten achter deze principes.

Dit document beschrijft de **architectuurprincipes** en **uitgangspunten** voor uitwerkingen in deze knowledge base (documentatie, koppelvlakspecificaties, modellen). Het is geen vervanging van concrete ADR's; bij twijfel of uitzondering leg je een besluit vast in `architecture/dr/`.

**Onderscheid principes en uitgangspunten:**

- **Principes** zijn abstracte, stabiele richtlijnen die niet snel wijzigen. Ze beschrijven *waarom* we dingen op een bepaalde manier doen.
- **Uitgangspunten** zijn gefundeerde besluiten om blocking issues te voorkomen. Ze zijn concreter, kunnen evolueren met voortschrijdend inzicht, en beschrijven *wat* we aannemen en *hoe* we werken.

Beide worden gevoed door de [MOSA-visie op sectorvoorzieningen](MOSA-Visiedocument.md), de [MOSA vs OKx analyse](MOSA_vs_OKx_analyse.md), en de praktijkervaring van het OKx-kernteam.

---

## OKx-uitgangspunten

Onderstaande uitgangspunten gelden voor iedereen die bijdraagt aan OKx. Ze zijn geen architectuurprincipes maar vormen de gefundeerde basis waarop we werken. Uitgangspunten kunnen wijzigen via **pull request** en, indien nodig, **ADR**.

### Technologie en standaarden

- **OEAPI, tenzij** — Technologiekeuze voor koppelvlakken is **[OEAPI](https://openonderwijsapi.nl/)**, tenzij OEAPI aantoonbaar niet past. Afwijkingen bevatten een korte "tenzij"-onderbouwing (wat past niet, trade-offs, impact). Bij structurele afwijking: leg vast als ADR. Geen vendor-specifieke extensies zonder ADR. Dit uitgangspunt ondersteunt AP04 (koppelvlakken als open, gestandaardiseerde contracten).
- **Open-source tooling voorkeur** — Tooling voor specificatie, validatie en generatie is bij voorkeur open source. Specificaties worden in open formaten opgeleverd (OpenAPI/Swagger, JSON Schema, Markdown). Geen verplichte afhankelijkheid van propriëtaire specificatietools.
- **Machine-interpreteerbare formaten** — Uitwerkingen zijn zoveel mogelijk gestructureerd (Markdown, JSON-informatiemodellen, tabellen, schema's). Dit maakt automatisering, AI-assistentie en consistente validatie mogelijk. Publiceer geen vertrouwelijke of persoonsgevoelige gegevens; zie [`doc/Privacy-meetings-en-transcriptie.md`](../../../../doc/Privacy-meetings-en-transcriptie.md).

### Randvoorwaardelijke domeinen

- **IDM en provisioning als randvoorwaarde** — Identity Management en provisioning vallen buiten OKx-scope, maar zijn een **kritische randvoorwaarde** voor correcte werking van koppelvlakken. Zonder helder bronsysteem voor persoonsattributen ontstaat het risico dat functionele componenten onbedoeld identiteitsdata gaan distribueren (zie [AP13](#okx-ap13--source-system-ownership-en-doelbinding-per-referentiecomponent)). OKx benoemt IDM/provisioning expliciet als randvoorwaarde in koppelvlakspecificaties, maar schrijft de oplossing niet voor.

### Kwaliteit en verificatie

- **Test-driven op berichtniveau** — Koppelvlakspecificaties worden bij voorkeur test-driven ontwikkeld: beschrijf eerst de **testcase** (given-when-then), ga daarna bouwen. Door op berichtniveau te testen wordt de interoperabiliteit concreet verifieerbaar vóórdat implementaties worden opgeleverd. Dit versnelt validatie bij leveranciers en voorkomt late integratieproblemen.

### Afstemming en beschrijvingswijze

- **Afstemming met referentiearchitecturen** — OKx stemt de beschrijvingswijze af op de aanpak binnen **MORA** (mbo), **HORA** (ho) en **FORA** (federatief), maar blijft **pragmatisch**: het snijvlak is dat we iets moeten realiseren én tegelijkertijd de keten voldoende beschrijven — maar niet zo veel dat we in een ivoren toren belanden. Voldoende beschrijven, niet overbeschrijven.
- **Show don't tell — praktische voorbeelden zo dicht mogelijk bij het eindresultaat** — Liever OEAPI-profielen, API-specs, mockups, diagrammen (Mermaid, ArchiMate) en korte bullets dan lange lappen tekst. Hoe dichter het artefact bij het eindresultaat, hoe sneller adoptie in diverse gremia verloopt. Zie [`doc/Bijdragen-voor-beginners.md`](../../../../doc/Bijdragen-voor-beginners.md) voor voorbeelden.

### Adoptie en transitie

- **BOPSI-aanpak voor adoptie** — OKx bouwt niet alleen een oplossing maar helpt ook bij het adoptieproces. Via de **BOPSI-aanpak** (Beleid, Organisatie, Proces, Systeem, Informatie) kijken we samen met instellingen waar de huidige situatie (IST) moet veranderen per BOPSI-aspect om toe te groeien naar de streefarchitectuur (SOLL) die we nu uitzetten. Architecture-based designs worden vertaald naar concrete transitiepaden per instelling.
- **Borging in lijnorganisaties** — OKx is een programma/project met een einddatum. Dragen we actief bij aan de vorming van nieuwe of ondersteuning van bestaande **lijnorganisaties** die beoogde deliverables in beheer gaan nemen. Borgingsaspecten (eigenaarschap, governance, financiering, competenties) worden expliciet meegenomen in het ontwerp, niet pas bedacht bij oplevering.

### Samenwerking en openheid

- **Samen ontwerpen — open boek** — Het domein is te groot en te complex voor één team. OKx werkt als open boek: zoek de fouten, deel ze, en doe constructieve verbetervoorstellen. Iedereen — leveranciers, instellingen, architecten, docenten — is welkom om mee te denken en bij te dragen. Alles via issues en PR's.
- **Levend document** — Uitgangspunten mogen worden aangescherpt naarmate OKx volwassener wordt. Wijzigingen gaan via **pull request** en, indien nodig, **ADR**.

### Gerelateerde documenten

- [`CONTRIBUTING.md`](../../../../CONTRIBUTING.md) — workflow en governance
- [`doc/Bijdragen-voor-beginners.md`](../../../../doc/Bijdragen-voor-beginners.md) — praktische gids voor bijdragen
- [`architecture/agent-artifacts/README.md`](../../../agent-artifacts/README.md) — opslag voor agent-gegenereerde plannen en ontwerpen
- [`doc/Privacy-meetings-en-transcriptie.md`](../../../../doc/Privacy-meetings-en-transcriptie.md) — opname/transcriptie, AVG
- [`architecture/dr/`](../../../dr/) — Architecture Decision Records
- [MOSA-Visiedocument](MOSA-Visiedocument.md) — sectorarchitectuur voor sectorvoorzieningen in het mbo
- [MOSA vs OKx analyse](MOSA_vs_OKx_analyse.md) — overlap, verschillen en afleidbare principes
- [ADR 0006 — Consolidatie architectuurprincipes](../../../dr/0006-consolidatie-architectuurprincipes.md) — afwegingen achter de consolidatie en uitgangspunten
- [Edu-V Architectuurprincipes](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes) — referentiekader (met name principe D: Regie op gegevens)

---

## OKx architectuurprincipes

Onderstaande principes zijn abstract en stabiel. Ze hebben een korte **stelling**, **rationale** en **implicaties**. Waar een principe tot concrete keuzes leidt, leggen we dat vast als **ADR**.

### OKx-AP01 — Keten vóór koppelvlak

- **Stelling**: We optimaliseren voor de **hele keten**, niet voor één los koppelvlak.
- **Rationale**: Een koppelvlak dat voor één systeem optimaal is, kan elders in de keten een bottleneck worden. Door eerst de keten te begrijpen — welke stromen er zijn, wie er aan raakt — voorkomen we lokale maxima en bereiken we een gedeeld minimum aan afspraken. De projectaanpak (begrijpen → ontwerpen → realiseren) uit [`doc/OKx_Projectoverzicht.md`](../../../../doc/OKx_Projectoverzicht.md) sluit hierbij aan. MOSA §4.4 onderbouwt dat interoperabiliteit de sleutel is om autonomie te behouden bij ketenoptimalisatie.
- **Implicaties**:
  - Elke koppelvlakspecificatie beschrijft expliciet **welke ketenstappen en stromen** ze ondersteunt.
  - Wijzigingen worden beoordeeld op **downstream impact** (planning, SVS, LMS, examen/resultaten, etc.).
  - Uitwerkingen zijn iteratief: concept → review (issues/PR's) → verfijning.

### OKx-AP02 — Semantiek vóór techniek

- **Stelling**: Eerst semantische overeenstemming, daarna technische interfaces.
- **Rationale**: Interoperabiliteit faalt meestal op betekenisverschillen, niet op endpoint-syntax. Als de ene partij "vak" bedoelt en de andere "module", helpt geen API dat te overbruggen. Dit geldt op alle drie de lagen die MOSA onderscheidt: technische, semantische én procesinteroperabiliteit (MOSA §4.4).
- **Implicaties**:
  - Geen "API-first" zonder voorafgaande keten- en informatiemodelcontext (AMIGO stappen 1–3).
  - Objecten en definities zijn traceerbaar naar MORA/MOKA waar beschikbaar.

### OKx-AP03 — AMIGO als standaardiseringsroute

- **Stelling**: OKx standaardiseert via de **[AMIGO-aanpak](https://www.edustandaard.nl/amigo/aanpak/)**.
- **Rationale**: Een van de kerndoelstellingen van project OKx is: *"Komen tot gezamenlijke taal en standaarden voor gegevensuitwisseling die een scala aan flexibilisering mogelijk maken."* De AMIGO-aanpak (scenario → gegevens → interactie → technologie → bericht → interface) is het door **[Edustandaard](https://www.edustandaard.nl/)** erkende raamwerk waarmee de sector gezamenlijk tot standaarden komt. Edustandaard beheert reeds de OKE-standaard en is het orgaan dat standaarden borgt binnen de educatieve sector. Door AMIGO te volgen, valt OKx-werk automatisch onder de governance van standaardisering en architectuur in de sector.
- **Implicaties**:
  - Een technische uitwerking bevat altijd verwijzing naar de bijbehorende scenario-, gegevens- en interactieanalyse.
  - OKx werkt onder de standaarden en architectuur van Edustandaard; uitwerkingen moeten daar in passen of een expliciet wijzigingsverzoek bevatten.

### OKx-AP04 — Koppelvlakken als open, gestandaardiseerde contracten

- **Stelling**: Elk koppelvlak fungeert als een **open, gestandaardiseerd contract** tussen referentiecomponenten. Het doel is **modulariteit vergroten** en **lock-in reduceren**: instellingen kunnen componenten onafhankelijk van elkaar vervangen zolang het contract wordt nageleefd.
- **Rationale**: Zonder gestandaardiseerde contracten zijn instellingen afhankelijk van bilaterale, leverancier-specifieke integraties. Elke leverancierswissel vereist dan herontwerp van alle koppelingen. Door het koppelvlak zelf als het bindende, open contract te behandelen — niet de applicatie of de leveranciersrelatie — ontstaat echte modulariteit: een instelling kan een LMS of SVS vervangen zonder dat de rest van de keten breekt. MOSA-principe 4 (open ecosysteem, internationale open standaarden) en MOSA-principe 1 (leveranciersonafhankelijkheid) versterken dit. De concrete technologiekeuze (OEAPI, tenzij) is vastgelegd als [uitgangspunt](#technologie-en-standaarden).
- **Implicaties**:
  - Het koppelvlak is het **contractpunt**: wat niet in de koppelvlakspecificatie staat, kan niet worden afgedwongen tussen ketenpartijen. Dit dwingt expliciete, volledige specificatie af.
  - Specificaties zijn implementeerbaar met gangbare technologiestacks; vermijd afhankelijkheden van specifieke cloudplatformen of propriëtaire tooling.
  - Geen vendor-specifieke extensies zonder ADR.
  - Houd de oplossing zo dicht mogelijk bij bredere afspraken (MOKA, BOPSI, andere erkende kaders).
  - De gestandaardiseerde contracten ondersteunen **componentsgewijze vervanging**: een instelling moet een referentiecomponent kunnen vervangen door een ander product dat hetzelfde contract implementeert, zonder impact op de rest van de keten.

### OKx-AP05 — Referentiecomponenten als gedeeld referentiekader

- **Stelling**: OKx beschrijft koppelvlakken in termen van **referentiecomponenten** — een gedeeld referentiekader voor functie en gedrag. Leveranciers behouden volledige **soevereiniteit** over de inrichting van hun applicaties.
- **Rationale**: Applicatie A is niet rechtstreeks vergelijkbaar met applicatie B: elke leverancier biedt een eigen combinatie van functies, onder eigen naamgeving en met eigen grenzen. Zonder gedeeld vocabulaire voor functie en gedrag is semantische overeenstemming op koppelvlakken onbereikbaar. Referentiecomponenten (Onderwijscatalogus, SKS, SVS, KRS, LMS, etc.) bieden dat vocabulaire: ze beschrijven **wat** een component doet en **hoe** het zich gedraagt in de keten, onafhankelijk van welke leverancier het invult. OKx gaat uitsluitend over de **koppelvlakinteractie** tussen die referentiecomponenten — niet over wat er achter het koppelvlak gebeurt. Leveranciers hebben volledige vrijheid in hoe zij hun applicatie(s) inrichten, welke functies zij combineren, en hoe zij de referentiecomponent(en) die zij bedienen intern realiseren. MOSA-principe 3 stelt dat componenten onafhankelijk, schaalbaar en ontkoppelbaar moeten zijn; dit principe vult aan dat die onafhankelijkheid ook de **leveranciersvrijheid** aan de applicatiekant omvat.
- **Implicaties**:
  - Koppelvlakken worden gespecificeerd op referentiecomponentniveau, niet op applicatieniveau. Dit is een **taalafspraak** voor standaardisering, geen beperking van applicatiefunctionaliteit.
  - Leveranciers mappen zelf hun applicatie(s) op één of meer referentiecomponenten. Hoe zij dat intern organiseren is hun eigen keuze.
  - OKx schrijft niet voor welke functionaliteit een applicatie wel of niet mag bevatten — alleen welk gedrag zichtbaar moet zijn op het koppelvlak.
  - Componentafbakening in de referentiearchitectuur wijzigt alleen via ADR + migratiepad; dit raakt de koppelvlakdefinitie, niet de applicatie-inrichting van leveranciers.
  - Elk koppelvlak beschrijft welke referentiecomponenten betrokken zijn en welke verantwoordelijkheid bij welk component hoort.

### OKx-AP06 — Contracten zijn versieerbaar en evolueerbaar

- **Stelling**: Koppelvlakken zijn publieke contracten die gecontroleerd kunnen evolueren.
- **Rationale**: Leveranciers en instellingen moeten veilig kunnen implementeren en upgraden. Dit omvat ook een wendbare exit-strategie: MOSA-principe 3 adviseert exit-plannen in contracten, zodat overstappen geen onoverkomelijke drempel is.
- **Implicaties**:
  - Versioning, compatibiliteit en deprecatie zijn onderdeel van de specificatie.
  - Deprecatiepaden en migratiegidsen bij majorversies.
  - Exit-strategie: leveranciers kunnen zonder onredelijke drempels overstappen.

### OKx-AP07 — Dataminimalisatie, privacy en security by design

- **Stelling**: Deel zo min mogelijk data, passend bij het ketendoel. Privacy en security zijn ontwerpcriteria, geen nabehandeling.
- **Rationale**: Onderwijsdata is gevoelig; fouten zijn kostbaar en moeilijk te herstellen. Dataminimalisatie verlaagt zowel privacyrisico's als integratiecomplexiteit. MOSA-principes 8 en 9 vereisen AVG-conformiteit, vertrouwelijkheid en integriteit van gegevens.
- **Implicaties**:
  - Elk attribuut heeft een expliciete reden (ketendoel, processtap, actor).
  - Vermijd "alles ophalen" als standaardpatroon; kies voor doelgerichte resources.
  - Scopes en autorisatieprincipes zijn expliciet beschreven waar passend.
  - Scheid waar mogelijk een anonieme/pseudonieme fase van een persoonsgebonden fase.
  - Maak gebruik van state-of-the-art beveiligingsstandaarden.

### OKx-AP08 — Transparantie, traceerbaarheid en navolgbaarheid

- **Stelling**: Besluiten, wijzigingen én uitwerkingen zijn publiek, navolgbaar en herleidbaar.
- **Rationale**: Dit is een federatieve, asynchrone knowledge base. Elke keuze moet achteraf begrijpelijk zijn — niet alleen voor het kernteam, maar ook voor nieuwe bijdragers en architectuurgremia. MOSA-principe 9 vereist dat systeemwerking inzichtelijk is; OKx vult dit aan met transparantie over zowel besluitvorming als technische artefacten.
- **Implicaties**:
  - Alles via issues en PR's; richtinggevende keuzes via ADR.
  - Link altijd naar relevante notulen en modelimpact.
  - Elke uitwerking is traceerbaar naar ArchiMate/MOKA-artefacten én naar technische deliverables.
  - Per koppelvlak: ketencontext, informatiemodel/klassendiagram, interactie, technische specs (OAS/endpoint) + cross-links.

### OKx-AP09 — Meervoudige implementatie richting standaard

- **Stelling**: Sectorstandaard vereist breder draagvlak dan één-op-één implementatie.
- **Rationale**: Afspraken die slechts door één leverancier en één instelling worden gedragen, zijn per definitie niet generiek. MOSA-principes 1 en 4 benadrukken leveranciersonafhankelijkheid en openheid.
- **Implicaties**:
  - Richting standaard/afsprakenstelsel: **meer dan 1 instelling én meer dan 1 leverancier** aangehaakt (minimaal 2+2).
  - Kleinere initiatieven kunnen via MOKA starten (AMIGO + OEAPI, tenzij), zonder op de OKx-kern te wachten.

### OKx-AP10 — Robuust in de praktijk (operational readiness)

- **Stelling**: De "niet-happy-flow" is onderdeel van de standaard.
- **Rationale**: Interoperabiliteit faalt vaak op randgevallen: fouten, timing, volgorde, onverwachte volumes. MOSA-principe 7 vereist dat continuïteit van onderwijs en bedrijfsvoering geborgd is. Dit geldt niet alleen technisch maar ook organisatorisch: als er iets misgaat, moet duidelijk zijn wie wat doet en hoe het proces doorgaat.
- **Implicaties**:
  - Foutpaden (errors, retries, timeouts) en berichtvolgorde zijn expliciet beschreven.
  - Afspraken over idempotentie en retries waar relevant.
  - Efficiënt API-ontwerp: vermijd onnodige polling; gebruik webhooks of event-driven patronen waar passend.
  - Hergebruik bestaande specificaties en patronen boven nieuwe uitvindingen.
  - Test- en validatieaanpak (pilots) expliciet bij oplevering.
  - Beschrijf de impact op niet-technische stakeholders (planners, ondersteunend personeel) bij faalscenario's.

### OKx-AP11 — Regie op gegevens en data-soevereiniteit

- **Stelling**: De onderwijsorganisatie en de student hebben regie over hun gegevens: wie mag wat inzien, en met welk doel.
- **Rationale**: [Edu-V principe D (Regie op gegevens)](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes) stelt dat de onderwijsorganisatie bepaalt welke gegevenssoorten er tussen leveranciers uitgewisseld mogen worden. MOSA §4.4 en §6 breiden dit uit naar de student: self-sovereign identity (SSI), wallets en verifiable credentials als richting. OKx neemt beide perspectieven mee: de student is niet slechts onderwerp van gegevensuitwisseling, maar actor met regie. Dit versterkt AP07 (dataminimalisatie).
- **Huidige verplichtingen**:
  - Koppelvlakken houden rekening met consent-mechanismen en doelbinding.
  - Instellingen kunnen bepalen welke gegevenssoorten uitgewisseld worden (in lijn met Edu-V D).
  - Gegevensuitwisseling vindt plaats op basis van een expliciete grondslag (toestemming, overeenkomst, wettelijke verplichting).
- **Toekomstrichting** *(OKx faciliteert, maar verplicht nog niet)*:
  - Datastructuren worden waar relevant "credential-ready" ontworpen: resultaten, inschrijvingen en voortgang als potentieel verifiable credentials.
  - Toekomstige wallet-integratie (eduID, EUDI Wallet) wordt niet geblokkeerd door huidige ontwerpkeuzes.
  - SSI-principes (issuer/holder/verifier) worden meegenomen als richtinggevend model bij identiteitsgerelateerde stromen.

### OKx-AP12 — Gebruiker centraal in ketenoptimalisatie

- **Stelling**: De ervaring van **alle betrokken gebruikers** — student, onderwijsprofessional en ondersteunend personeel — is toetssteen bij ketenoptimalisatie.
- **Rationale**: MOSA-principe 1 stelt de student (de lerende) centraal in het ecosysteem. Maar flexibilisering raakt niet alleen de student: docenten, coaches, begeleiders, planners en ondersteunend personeel moeten de wijzigingen in hun dagelijks werk kunnen realiseren. OKx optimaliseert informatiestromen in de keten; de impact op alle betrokkenen moet expliciet worden meegewogen, ook als zij geen directe actor zijn in een specifiek koppelvlak.
- **Implicaties**:
  - Bij het ontwerp van stromen die gebruikers raken: beschrijf de impact op de **student-ervaring** (student journey als basis).
  - Beschrijf ook hoe de **onderwijskundige, planner, coach/begeleider/docent** en **ondersteunend personeel** de wijziging ervaart.
  - Voorzieningen voor Leven Lang Ontwikkelen (LLO) en flexibel onderwijs zijn toetscriteria voor ketenontwerp.

### OKx-AP13 — Source system ownership en doelbinding per referentiecomponent

- **Stelling**: Elk koppelvlak maakt expliciet welk referentiecomponent de **bron** is van welke data. Een component draagt uitsluitend data die bij zijn eigen functie hoort.
- **Rationale**: In een keten van referentiecomponenten ontstaat het risico dat het eerste component dat een associatie legt (bijv. SKS koppelt een student aan een LMS) onbedoeld verantwoordelijk wordt voor het doorleveren van persoonsattributen die het downstream systeem nodig heeft. Maar SKS is geen bronsysteem voor persoonsdata — dat is het IDM/provisioningsdomein. Zonder expliciete bronverantwoordelijkheid per attribuut verwatert dataminimalisatie (AP07), worden componentgrenzen (AP05) ondermijnd, en ontstaan schaduw-kopieën van identiteitsdata in systemen die daar niet voor bedoeld zijn. MOSA §6 adresseert IAM als apart domein; OKx maakt dit concreet per koppelvlak.
- **Implicaties**:
  - Elke koppelvlakspecificatie bevat een **data-ownership-tabel**: per attribuut of attribuutgroep is aangegeven welk referentiecomponent de bron is (owner), welke consumenten er zijn, en op welke grondslag.
  - **Associaties boven attributen**: waar een koppelsleutel (pseudoniem, opaque identifier) volstaat om een relatie te leggen, worden geen volledige persoonsattributen meegegeven. Vraag: heeft een toets-/examenafnamesysteem de volledige naam en het BSN nodig, of is een associatie genoeg?
  - **IDM en provisioning als voorwaardelijk kader**: OKx neemt IDM/provisioning niet in scope, maar benoemt het als **randvoorwaarde** in koppelvlakspecificaties. Koppelvlakken mogen niet impliciet de rol van identiteitsdistributie overnemen.
  - Functionele componenten (SKS, SVS, LMS, toetssysteem, etc.) zijn **geen doorgeefluik** voor persoonsdata van andere componenten. Als een LMS persoonsattributen nodig heeft, haalt het die uit het IDM — niet uit het SKS-koppelvlak waarmee de leerroute-associatie is gelegd.
  - Bij afwijking van dit principe (bijv. performance, offline scenario): leg vast als **ADR** met expliciete risico-afweging.
