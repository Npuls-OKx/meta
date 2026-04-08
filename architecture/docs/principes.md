# Architectuur- en ontwerpprincipes (OKx-meta)

## Algemene principes

Dit document vat **richtinggevende principes** samen voor uitwerkingen in deze knowledge base (documentatie, koppelvlakspecificaties, modellen). Het is geen vervanging van concrete ADR’s; bij twijfel of uitzondering leg je een besluit vast in `architecture/dr/`.

---

## 1. Design first

- We **ontwerpen en beschrijven** koppelvlakken en informatiestromen **voordat** we ze als “af” beschouwen voor implementatie door leveranciers.
- Uitwerkingen zijn **iteratief**: concept → review (issues/PR’s) → verfijning.
- De projectaanpak (begrijpen → ontwerpen → realiseren) uit [`doc/OKx_Projectoverzicht.md`](../../doc/OKx_Projectoverzicht.md) sluit hierbij aan. Net als de gekozen [AMIGO aanpak](https://www.edustandaard.nl/amigo/) tot het komen van standaarden onder de vlag van edustandaard.

---

## 2. OEAPI als voorkeur — tenzij strategisch anders

**Uitgangspunt**: wat de **Open Onderwijs API (OEAPI)** kan uitdrukken of bedienen, modelleren en specificeren we **zoveel mogelijk op basis van OEAPI** (profielen, extensies, bestaande patronen).

- Raadpleeg de officiële documentatie: [Open Onderwijs API](https://openonderwijsapi.nl/) en bijvoorbeeld [OEAPI v6.0](https://openonderwijsapi.nl/v6.0/).
- **Waarom**: hergebruik van een brede sectorstandaard vermindert maatwerk, vergroot interoperabiliteit en sluit aan op bestaande implementaties en kennis in het veld.

**Uitzondering (“tenzij strategie”)**: als OEAPI **niet** past of **onvoldoende** is voor een gegeven use case (bijv. domeinspecifieke semantiek, wettelijke eisen, performance of ketenafspraken buiten het OEAPI-model), dan:

1. Beschrijf **waarom** OEAPI onvoldoende is (in issue, PR of ADR).
2. Leg een **bewuste keuze** vast — bij voorkeur als **ADR** in `architecture/dr/`.
3. Houd de oplossing **zo dicht mogelijk bij** bredere afspraken (MOKA, BOPSI, andere erkende kaders) en documenteer impact op keten en leveranciers.

---

## 3. Machine-interpreteerbare formaten en AI-ondersteuning

We streven ernaar om uitwerkingen **zoveel mogelijk machine-interpreteerbaar** te houden (bijv. **gestructureerde Markdown**, **JSON**-informatiemodellen, tabellen met duidelijke koppen, waar mogelijk schema’s en valideerbare definities).

**Waarom**

- **Automatisering**: consistente validatie, generatie van documentatie en koppeling tussen artefacten.
- **AI-agents en assistentie**: voorspelbare structuur maakt het veiliger en nuttiger om hulpmiddelen (zoals editors met AI) in te zetten voor review, consistentie en doorlinking — **zonder** de inhoudelijke verantwoordelijkheid van mensen te vervangen.

**Afspraken**

- Publiceer **geen** strikt vertrouwelijke of persoonsgevoelige gegevens in deze repo; zie [`doc/Privacy-meetings-en-transcriptie.md`](../../doc/Privacy-meetings-en-transcriptie.md) (o.a. meetings, transcriptie, publiek karakter van de knowledge base).
- Waar “menselijke” tekst onvermijdelijk is (notulen, toelichting), combineren we die met **gestructureerde** artefacten waar dat de kwaliteit verhoogt.

---

## 4. Show don't tell (diagram-first)

- Liever **inzichtelijk maken met weinig woorden**: **diagrammen** (bijv. Mermaid), **tabellen**, **schema’s** en korte bullets — in plaats van lange lappen tekst waar hetzelfde helder kan.
- **Waarom**: sneller te begrijpen, beter te reviewen, en beter te gebruiken door mens én tooling (AI-agents).
- Zie [`doc/Bijdragen-voor-beginners.md`](../../doc/Bijdragen-voor-beginners.md) voor voorbeelden (Git-flow, Cursor-workflow). PlantUML kan als teamkeuze; Mermaid heeft brede ondersteuning op GitHub.

---

## 5. Uitbreidbaarheid

- Principes hier zijn **levend**: ze mogen worden aangescherpt naarmate OKx volwassener wordt.
- Wijzigingen in deze principes gaan via **pull request** en, indien nodig, **ADR**.

---

## 6. Gerelateerde documenten

- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) — workflow en governance
- [`doc/Bijdragen-voor-beginners.md`](../../doc/Bijdragen-voor-beginners.md) — praktische gids voor bijdragen
- [`architecture/agent-artifacts/README.md`](../agent-artifacts/README.md) — opslag en frontmatter voor agent-gegenereerde plannen en ontwerpen
- [`doc/Privacy-meetings-en-transcriptie.md`](../../doc/Privacy-meetings-en-transcriptie.md) — opname/transcriptie, AVG en waarschuwing rond niet-publieke informatie
- [`architecture/dr/`](../dr/) — Architecture Decision Records

---

## 7. OKx architectuurprincipes

**Status:** Voorstel  
**Datum:** 2026-04-08

Onderstaande principes hebben een korte **stelling**, **rationale** en **implicaties**. Waar een principe tot concrete keuzes leidt, leggen we dat vast als **ADR**.

### OKx-AP01 — Keten vóór koppelvlak

- **Stelling**: We optimaliseren voor de **hele keten**, niet voor één los koppelvlak.
- **Rationale**: Dit voorkomt lokale maxima en helpt een gedeeld minimum aan afspraken te bereiken.
- **Implicaties**:
  - Elke koppelvlakspecificatie moet expliciet beschrijven **welke ketenstappen/stromen** ze ondersteunt.
  - Wijzigingen worden beoordeeld op **downstream impact** (planning, SVS, LMS, examen/resultaten, etc.).

### OKx-AP02 — Semantiek vóór techniek

- **Stelling**: Eerst semantische overeenstemming, daarna technische interfaces.
- **Rationale**: Interoperabiliteit faalt meestal op betekenisverschillen, niet op endpoint-syntax.
- **Implicaties**:
  - Geen “API-first” zonder voorafgaande keten- en informatiemodelcontext (AMIGO stappen 1–3).
  - Objecten/definities zijn traceerbaar naar MORA/MOKA waar beschikbaar.

### OKx-AP03 — AMIGO als standaardiseringsroute

- **Stelling**: OKx standaardiseert via de **AMIGO-aanpak**.
- **Rationale**: AMIGO biedt een sectorbreed patroon van scenario → gegevens → interactie → techniek.
- **Implicaties**:
  - Een technische uitwerking bevat altijd verwijzing naar scenario-, gegevens- en interactieanalyse (minimaal).
  - Zie ook: `https://www.edustandaard.nl/amigo/aanpak/`.

### OKx-AP04 — OEAPI, tenzij

- **Stelling**: Technologiekeuze is **OEAPI**, tenzij OEAPI aantoonbaar niet past.
- **Rationale**: Hergebruik van een brede sectorstandaard vergroot interoperabiliteit en herbruikbaarheid.
- **Implicaties**:
  - Afwijkingen bevatten een korte “tenzij”-onderbouwing (wat past niet, trade-offs, impact).
  - Bij structurele afwijking: leg vast als ADR.

### OKx-AP05 — Heldere componentgrenzen

- **Stelling**: Referentiecomponenten blijven herkenbaar en hebben expliciete verantwoordelijkheden.
- **Rationale**: Zonder heldere grenzen ontstaan dubbelingen en verborgen koppellogica.
- **Implicaties**:
  - Componenten zoals Onderwijscatalogus, SKS, SVS, KRS, LMS worden niet stilzwijgend samengevoegd.
  - Wijzigingen aan componentafbakening: ADR + migratiepad.

### OKx-AP06 — Contracten zijn versieerbaar en evolueerbaar

- **Stelling**: Koppelvlakken zijn publieke contracten die gecontroleerd kunnen evolueren.
- **Rationale**: Leveranciers en instellingen moeten veilig kunnen implementeren en upgraden.
- **Implicaties**:
  - Versioning, compatibiliteit en deprecatie zijn onderdeel van de specificatie.
  - Foutpaden (errors/retries) zijn expliciet beschreven.

### OKx-AP07 — Dataminimalisatie en doelbinding

- **Stelling**: Deel zo min mogelijk data, passend bij het ketendoel.
- **Rationale**: Minimalisatie verlaagt privacyrisico’s en integratiecomplexiteit.
- **Implicaties**:
  - Elk attribuut heeft een expliciete reden (ketendoel, processtap, actor).
  - Vermijd “datadumps”; kies voor doelgerichte resources.

### OKx-AP08 — Privacy & security by design

- **Stelling**: Privacy en security zijn ontwerpcriteria, geen nabehandeling.
- **Rationale**: Onderwijsdata is gevoelig; fouten zijn kostbaar en moeilijk te herstellen.
- **Implicaties**:
  - Scopes/authorisatieprincipes zijn expliciet (waar passend).
  - Scheid waar mogelijk anonieme/pseudonieme fase van persoonsgebonden fase.
  - Maak gebruik van bestaande en state-of-the-art standaarden.

### OKx-AP09 — Transparantie en traceerbaarheid

- **Stelling**: Besluiten en wijzigingen zijn publiek, navolgbaar en herleidbaar.
- **Rationale**: Dit is een federatieve, asynchrone knowledge base.
- **Implicaties**:
  - Alles via issues/PR’s; richtinggevende keuzes via ADR.
  - Link altijd naar relevante notulen en modelimpact.

### OKx-AP10 — Traceerbaar naar model en deliverables

- **Stelling**: Elke uitwerking is traceerbaar naar ArchiMate/MOKA-artefacten én naar technische deliverables.
- **Rationale**: Dit maakt review en consistentie over stromen en specificaties mogelijk.
- **Implicaties**:
  - Per koppelvlak: ketencontext, informatiemodel/klassediagram, interactie, technische specs (OAS/endpoint) + cross-links.

### OKx-AP11 — Meervoudige implementatie richting standaard

- **Stelling**: Sectorstandaard vereist breder draagvlak dan één-op-één implementatie.
- **Rationale**: Anders ontstaan leveranciers-/instellingsspecifieke afspraken die niet generiek zijn.
- **Implicaties**:
  - Richting standaard/afsprakenstelsel: **meer dan 1 instelling én meer dan 1 leverancier** aangehaakt (minimaal 2+2).
  - Kleinere initiatieven kunnen via MOKA starten (AMIGO + OEAPI, tenzij), zonder op OKx-kern te wachten.

### OKx-AP12 — Robuust in de praktijk (operational readiness)

- **Stelling**: De “niet-happy-flow” is onderdeel van de standaard.
- **Rationale**: Interoperabiliteit faalt vaak op randgevallen: fouten, timing, volgorde.
- **Implicaties**:
  - Afspraken over idempotentie, retries, timeouts, en berichtvolgorde waar relevant.
  - Test- en validatieaanpak (pilots) expliciet bij oplevering.
