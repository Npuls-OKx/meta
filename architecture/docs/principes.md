# Architectuur- en ontwerpprincipes (OKx-meta)

Dit document vat **richtinggevende principes** samen voor uitwerkingen in deze knowledge base (documentatie, koppelvlakspecificaties, modellen). Het is geen vervanging van concrete ADR’s; bij twijfel of uitzondering leg je een besluit vast in [Referentiemateriaal/adr in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr).

---

## 1. Design first

- We **ontwerpen en beschrijven** koppelvlakken en informatiestromen **voordat** we ze als “af” beschouwen voor implementatie door leveranciers.
- Uitwerkingen zijn **iteratief**: concept → review (issues/PR’s) → verfijning.
- De projectaanpak (begrijpen → ontwerpen → realiseren) uit [`doc/OKx_Projectoverzicht.md`](../../doc/OKx_Projectoverzicht.md) sluit hierbij aan.

---

## 2. OEAPI als voorkeur — tenzij strategisch anders

**Uitgangspunt**: wat de **Open Onderwijs API (OEAPI)** kan uitdrukken of bedienen, modelleren en specificeren we **zoveel mogelijk op basis van OEAPI** (profielen, extensies, bestaande patronen).

- Raadpleeg de officiële documentatie: [Open Onderwijs API](https://openonderwijsapi.nl/) en bijvoorbeeld [OEAPI v6.0](https://openonderwijsapi.nl/v6.0/).
- **Waarom**: hergebruik van een brede sectorstandaard vermindert maatwerk, vergroot interoperabiliteit en sluit aan op bestaande implementaties en kennis in het veld.

**Uitzondering (“tenzij strategie”)**: als OEAPI **niet** past of **onvoldoende** is voor een gegeven use case (bijv. domeinspecifieke semantiek, wettelijke eisen, performance of ketenafspraken buiten het OEAPI-model), dan:

1. Beschrijf **waarom** OEAPI onvoldoende is (in issue, PR of ADR).
2. Leg een **bewuste keuze** vast — bij voorkeur als **ADR** in [Referentiemateriaal/adr in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr).
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
- [[Referentiemateriaal/adr in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr)](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr) — Architecture Decision Records
