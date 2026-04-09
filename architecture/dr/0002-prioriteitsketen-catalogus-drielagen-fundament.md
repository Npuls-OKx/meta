## Prioriteitsketen curriculumontwerp–onderwijscatalogus en drieledig architectuurfundament

Status: Voorstel

Datum: 2026-03-25

### Context

OKx moet **gestandaardiseerde koppelvlakken** concreet maken terwijl **sectorbrede streefarchitectuur** (o.a. Platform 3 / Mosa–Hosa, volledige MOKA-uitwerkingen per koppelvlak) **ontbreekt of achterloopt**. Tegelijkertijd is er geen zinvolle uitspraak te doen over **downstream**-koppelvlakken (planning, SVS, LMS, enz.) zonder zicht op **hoe** onderwijsaanbod tot stand komt en **wat** in de **onderwijscatalogus** als bron voor de keten landt.

In de SI-afstemming (maart 2024) is benadrukt dat de **eerste technische focus** ligt op de stroom **curriculumontwerp → onderwijscatalogus** (catalogus als **bronsysteem**), en dat OKx **drie architectuurproducten** uitwerkt: verdieping op het **MORA-procesbeeld**, **MOKA-koppelvlakspecificatie-views**, en het **MOKA-koppelvlak-informatiemodel** — als **werkbaar minimum** naast sectorale kaders.

**Samenhang:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md) beschrijft **waar en hoe** dit wordt vastgelegd. [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) beschrijft **domeinprincipes** (student kiest, leeruitkomsten) die deze keten inrichten.

### Beslissing (concept)

1. **Prioriteitsketen:** De **eerste diepgaande technische uitwerking** richt zich op het **formeel uitgewerkte aanbod tussen curriculumontwerp en onderwijscatalogus** — omdat zonder dit zicht geen **valide** koppelvlakken richting de rest van het landschap zijn te specificeren.
2. **Drielagen-fundament** (minimaal pakket zolang sectorbrede streeflevering ontbreekt): parallel aan MORA/MOKA-kaders werkt OKx aan **(a)** verdieping op het **MORA-procesbeeld**, **(b)** **MOKA-koppelvlakspecificatie-views**, en **(c)** het **MOKA-koppelvlak-informatiemodel** — als **gedeeld referentiekader** voor technische werkgroep en leveranciers, **niet** als vervanging van de sectorarchitectuur.
3. **Koppelvlakken** verderop in de keten (o.a. catalogus–planning, catalogus–SVS) worden **opgebouwd** in samenhang met dit fundament en **traceerbaar** gemaakt naar de MOKA-specificatielijn.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Wachten** op volledige Mosa/Hosa-streefarchitectuur Platform 3 en volledige MOKA-sectoruitwerking | Sterke normatieve dekking | **Stagnatie**; **eilandoplossingen** blijven ontstaan |
| **B. Willekeurige koppelvlak** eerst (bijv. alleen planning–SVS) | Snelle “demo” | **Fundering** ontbreekt; **hoge rework** |
| **C. Alleen leveranciers laten specificeren** zonder centraal procesbeeld | Commerciële snelheid | **Lokale optima**, **niet-componerbare** interfaces |
| **D. (Gekozen richting)** Keten curriculum–catalogus eerst + drie architectuurproducten | **Bestuurbare scope**, **gedeeld beeld** | **Capaciteitsdruk**; **afhankelijkheid** van MORA/MOKA-evolutie sector |

### Consequenties

- **Stakeholders:** Leveranciers krijgen **één** door de sector gedragen **richting** voor de eerste diepe uitwerking; instellingen kunnen **eisen** aan onderwijsaanbod en catalogus **koppelen** aan specificaties.
- **Werk:** Substantiële **modelleer- en specificatie-inspanning**; **werkgroep Techniek** en leverancierssessies bouwen hier op voort (zoals in notulen genoemd).
- **Risico’s:** **Afstemming** met MORA/MOKA-bezitters blijft nodig; **scope creep** als downstream te vroeg wordt opgepakt zonder stabiel fundament.

### Impact op `architecture/model/model.archimate`

- **Views:** Het model moet de **prioriteitsketen** (curriculumontwerp ↔ onderwijscatalogus) en de daaruit voortvloeiende **proces- en informatieobjecten** tonen in **dedicated views** (proces, applicatie, informatie), consistent met MOKA/MORA waar die bestaan.
- **Koppelvlakken:** Uitwerkingen richting **planning**, **SVS**, **LMS** en vergelijkbare componenten moeten **traceerbaar** linken aan de **MOKA-koppelvlakspecificatie**-lijn en het **informatiemodel** — zodat discussies in issues/PR’s op het model terug te voeren zijn.
- **Niet in dit ADR:** het **PR-proces** zelf — zie [0001](0001-publieke-repo-en-samenwerkingsmodel.md).

### Relaties en links

- **Gerelateerde ADR’s:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md) (repo en workflow), [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (domeinprincipes)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `doc/meetings kernteam/okx_si_team_afstemming_josvdarend_240326/okx_si_team_afstemming_josvdarend_aanhaken_voortgang_okx_240326_summary.md`
  - `doc/meetings kernteam/okx_si_team_afstemming_josvdarend_240326/okx_si_team_afstemming_josvdarend_aanhaken_voortgang_okx_240326_transcript.md`
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md`
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: [`architecture/docs/principes/doc/principes.md`](../docs/principes/doc/principes.md), [`doc/OKx_Projectoverzicht.md`](../../doc/OKx_Projectoverzicht.md)

### Vervangt (optioneel)

- Vervangt het eerdere gecombineerde voorstel `0001-centrale-repo-keten-catalogus-en-drielagen-fundament.md` (opgesplitst in 0001–0003).
