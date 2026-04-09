# Architectuur- en ontwerpprincipes (OKx-meta)

**Status:** Voorstel
**Datum:** 2026-04-09
**Consolidatie:** Zie [ADR 0006](../../../dr/0006-consolidatie-architectuurprincipes.md) voor de afwegingen en besluiten achter deze principes.

Dit document vat **richtinggevende principes** samen voor uitwerkingen in deze knowledge base (documentatie, koppelvlakspecificaties, modellen). Het is geen vervanging van concrete ADR's; bij twijfel of uitzondering leg je een besluit vast in `architecture/dr/`.

De principes zijn geformuleerd in stelling, rationale, implicaties en worden gevoed door de [MOSA-visie op sectorvoorzieningen](MOSA-Visiedocument.md), de [MOSA vs OKx analyse](MOSA_vs_OKx_analyse.md), en de praktijkervaring van het OKx-kernteam.

---

## Werkafspraken voor de knowledge base

Onderstaande werkafspraken gelden voor iedereen die bijdraagt aan deze repo. Ze zijn niet genummerd als architectuurprincipe, maar vormen de operationele basis.

- **Machine-interpreteerbare formaten** — Uitwerkingen zijn zoveel mogelijk gestructureerd (Markdown, JSON-informatiemodellen, tabellen, schema's). Dit maakt automatisering, AI-assistentie en consistente validatie mogelijk. Publiceer geen vertrouwelijke of persoonsgevoelige gegevens; zie [`doc/Privacy-meetings-en-transcriptie.md`](../../../../doc/Privacy-meetings-en-transcriptie.md).
- **Show don't tell (diagram-first)** — Liever diagrammen (Mermaid, ArchiMate), tabellen en korte bullets dan lange lappen tekst. Zie [`doc/Bijdragen-voor-beginners.md`](../../../../doc/Bijdragen-voor-beginners.md) voor voorbeelden.
- **Levend document** — Deze principes mogen worden aangescherpt naarmate OKx volwassener wordt. Wijzigingen gaan via **pull request** en, indien nodig, **ADR**.
- **Open-source tooling voorkeur** — Tooling voor specificatie, validatie en generatie is bij voorkeur open source. Specificaties worden in open formaten opgeleverd (OpenAPI/Swagger, JSON Schema, Markdown). Geen verplichte afhankelijkheid van propriëtaire specificatietools.

### Gerelateerde documenten

- [`CONTRIBUTING.md`](../../../../CONTRIBUTING.md) — workflow en governance
- [`doc/Bijdragen-voor-beginners.md`](../../../../doc/Bijdragen-voor-beginners.md) — praktische gids voor bijdragen
- [`architecture/agent-artifacts/README.md`](../../../agent-artifacts/README.md) — opslag voor agent-gegenereerde plannen en ontwerpen
- [`doc/Privacy-meetings-en-transcriptie.md`](../../../../doc/Privacy-meetings-en-transcriptie.md) — opname/transcriptie, AVG
- [`architecture/dr/`](../../../dr/) — Architecture Decision Records
- [MOSA-Visiedocument](MOSA-Visiedocument.md) — sectorarchitectuur voor sectorvoorzieningen in het mbo
- [MOSA vs OKx analyse](MOSA_vs_OKx_analyse.md) — overlap, verschillen en afleidbare principes
- [ADR 0006 — Consolidatie architectuurprincipes](../../../dr/0006-consolidatie-architectuurprincipes.md) — afwegingen achter de consolidatie van 17 naar 12 principes
- [Edu-V Architectuurprincipes](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes) — referentiekader (met name principe D: Regie op gegevens)

---

## OKx architectuurprincipes

Onderstaande principes hebben een korte **stelling**, **rationale** en **implicaties**. Waar een principe tot concrete keuzes leidt, leggen we dat vast als **ADR**.

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

### OKx-AP04 — OEAPI, tenzij — open en leverancierneutraal

- **Stelling**: Technologiekeuze is **[OEAPI](https://openonderwijsapi.nl/)**, tenzij OEAPI aantoonbaar niet past. Specificaties zijn **leverancierneutraal** en creëren geen lock-in.
- **Rationale**: Hergebruik van een brede, open sectorstandaard vermindert maatwerk en vergroot interoperabiliteit. MOSA-principe 4 (open ecosysteem, internationale open standaarden) en MOSA-principe 1 (leveranciersonafhankelijkheid) versterken dit. Specificaties moeten door willekeurige leveranciers implementeerbaar zijn, ongeacht hun technologiestack.
- **Implicaties**:
  - Afwijkingen bevatten een korte "tenzij"-onderbouwing (wat past niet, trade-offs, impact).
  - Bij structurele afwijking: leg vast als ADR.
  - Geen vendor-specifieke extensies zonder ADR.
  - Specificaties zijn implementeerbaar met gangbare technologiestacks; vermijd afhankelijkheden van specifieke cloudplatformen of propriëtaire tooling.
  - Houd de oplossing zo dicht mogelijk bij bredere afspraken (MOKA, BOPSI, andere erkende kaders).

### OKx-AP05 — Referentiecomponenten boven applicatiedenken

- **Stelling**: OKx beschrijft koppelvlakken tussen **referentiecomponenten**, niet tussen applicaties.
- **Rationale**: Instellingen denken vaak in applicaties: een systeem dat door één leverancier geleverd wordt en meerdere functies bevat. Die applicatiegrens verschilt per leverancier — de ene noemt iets een "vak", de andere een "module". Zolang we in applicaties denken, is semantische overeenstemming onbereikbaar. Referentiecomponenten (Onderwijscatalogus, SKS, SVS, KRS, LMS, etc.) maken de **functie** expliciet, onafhankelijk van de leverancier die ze invult. MOSA-principe 3 stelt dat componenten onafhankelijk, schaalbaar en ontkoppelbaar moeten zijn.
- **Implicaties**:
  - Koppelvlakken worden gespecificeerd op referentiecomponentniveau, niet op applicatieniveau.
  - Leveranciers mappen zelf hun applicatie(s) op één of meer referentiecomponenten.
  - Componenten worden niet stilzwijgend samengevoegd; wijzigingen aan componentafbakening vereisen een ADR + migratiepad.
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
