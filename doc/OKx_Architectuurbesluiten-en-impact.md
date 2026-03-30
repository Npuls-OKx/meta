# OKx: architectuurbesluiten en impact

Dit document **vat samen** welke architectuurrichting uit **Architecture Decision Records (ADR’s)** en uit **kernteam- en SI-afstemming** volgt, en wat dat betekent voor **documentatie**, **informatiestromen** en het **ArchiMate-model**. Het vervangt geen ADR: voor de volledige onderbouwing en status per besluit gelden de bestanden in [`architecture/dr/`](../architecture/dr/).

**Status:** de onderliggende ADR’s staan als *Voorstel*; deze pagina is eveneens **concept** en wordt mee bijgewerkt als ADR’s worden geaccepteerd of vervangen.

## Bronnen

### ADR’s (canonical)

| ADR | Onderwerp |
|-----|-----------|
| [0001 – Publieke repo en samenwerkingsmodel](../architecture/dr/0001-publieke-repo-en-samenwerkingsmodel.md) | Single source of truth, issues, pull requests, review |
| [0002 – Prioriteitsketen en drielagen-fundament](../architecture/dr/0002-prioriteitsketen-catalogus-drielagen-fundament.md) | Keten curriculumontwerp–onderwijscatalogus; MORA/MOKA-fundament |
| [0003 – Student kiest en leeruitkomsten](../architecture/dr/0003-student-kiest-leeruitkomsten-domeinprincipes.md) | Domeinprincipes flexibilisering |
| [0004 – Leeruitkomsten en SBU/EC](../architecture/dr/0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) | Inhoud (LO) + studielast als logistieke maat |

### Meetings (context en onderbouwing)

- `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md` (en transcript in dezelfde map)
- `architecture/meetings/OKx_kernteam_inhoud_voorbereidingleveranciersessie_20260327/summary.md` (en transcript in dezelfde map)
- `doc/meetings kernteam/okx_si_team_afstemming_josvdarend_240326/okx_si_team_afstemming_josvdarend_aanhaken_voortgang_okx_240326_summary.md` (en transcript in dezelfde map)

## Samenvatting per thema

### 1. Publieke repository en samenwerking

- De **GitHub-repository** is de primaire plek voor **versioneerbare** OKx-kennis: o.a. [`architecture/model/model.archimate`](../architecture/model/model.archimate), koppelvlakrichting, ADR’s en kern-documentatie.
- **Wijzigingen** lopen via **pull requests** en **review** door het kernteam (zie [`CONTRIBUTING.md`](../CONTRIBUTING.md)).
- **Issues** houden backlog, vragen en externe feedback vast (o.a. leveranciers/instellingen).

**Impact:** besluiten en modelwijzigingen blijven **traceerbaar**; er is een gedeelde basis om **lokale optima** (eilandoplossingen) te vermijden.

### 2. Prioriteitsketen en drielagen-fundament

- De **eerste diepgaande technische uitwerking** richt zich op het **uitgewerkte aanbod tussen curriculumontwerp en onderwijscatalogus** — de **onderwijscatalogus** geldt als **bronsysteem** voor veel vervolgstromen.
- Zolang sectorbrede streeflevering (o.a. volledige MOKA-sectoruitwerking) achterloopt, werkt OKx aan een **minimaal pakket**: verdieping op het **MORA-procesbeeld**, **MOKA-koppelvlakspecificatie-views** en het **MOKA-koppelvlak-informatiemodel** — als **referentiekader**, niet als vervanging van sectorarchitectuur.

**Impact op informatiestromen (zie [OKx_Projectoverzicht](OKx_Projectoverzicht.md)):**

- **Stroom 1** (Curriculum ontwerptool → Onderwijscatalogus, *Uitgewerkt aanbod*) is de **basislijn** waaraan latere stromen (2, 3, …) inhoudelijk hangen.
- Stromen **2 en 3** zijn **direct downstream** van de catalogus in de prioritering; zonder helder beeld op stroom 1 zijn specs daar lastig te verdedigen.

### 3. Student kiest, leeruitkomsten en onderwijskundige laag

- **Student kiest** en **leeruitkomsten** vormen **domeinprincipes**: koppelvlakken moeten **onderwijskundige** en **logistieke** informatie **samen** ondersteunen.
- **Student journeys**, mockups en scenario’s zijn bewust onderdeel van de aanpak om **draagvlak** te creëren naast technische platen.

**Impact:** het ArchiMate-model en MOKA-views moeten **concepten** (o.a. leeruitkomsten, keuzes) **herkenbaar** houden, niet alleen technische interfaces.

### 4. Leeruitkomsten en SBU/EC als logistieke containergrootte

- **Leeruitkomsten** blijven de **inhoudelijke** kern; **SBU (mbo)** en **EC (hbo)** zijn de **genormeerde maat** voor de **logistieke grootte** van programma-onderdelen in koppelvlakken (planning, aggregatie, vergelijking tussen aanbieders).
- **Wettelijke/bekostigingscontainers** (bijv. ROD) kunnen **aanvullend** zijn en worden **gemapt**, niet zonder besluit gelijkgesteld aan deze logistieke maatstaf (zie [0004](../architecture/dr/0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md)).

**Impact:** het informatiemodel en API-profielen moeten **studielast per sector** en **koppeling aan leeruitkomsten** kunnen dragen.

## Impact op `architecture/model/model.archimate`

Samengevat (detail per ADR):

- **0001:** wijzigingen aan het model via **PR/review**; geen grote stille wijzigingen zonder vastlegging.
- **0002:** **views** en elementen voor de **prioriteitsketen** en **MOKA-koppelvlaklijn**; traceerbaarheid naar specificaties.
- **0003:** **domeinconcepten** (rollen, leeruitkomsten, keuze) zichtbaar of traceerbaar in relevante views.
- **0004:** **studielast** (SBU/EC) en **relatie leeruitkomst ↔ aanbodsonderdeel** in relevante informatie- en ketenviews.

**Let op:** het bestand `model.archimate` wordt **alleen** gewijzigd via het afgesproken repo-proces (geen directe ongecontroleerde edits).

## Zie ook

- [OKx Informatiestromen](OKx_Informatiesstromen.md) — overzicht stromen en specs
- [Informatiestromen, ArchiMate en MOKA-view](OKx_Informatiestromen-ArchiMate-en-MOKA-view.md) — **hoe** je stromen terugvindt in het model
- [OKx Projectoverzicht](OKx_Projectoverzicht.md) — hoofdplaat en interpretatietabel
