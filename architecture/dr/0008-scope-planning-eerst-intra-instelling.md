## Scope: eerst planning en keten binnen één instelling; sector-orchestratie gefaseerd

Status: Voorstel

Datum: 2026-03-31

### Context

OKx moet **haalbare** koppelvlakken en processen opleveren. In het overleg **kaderstelling studentkeuze en criteria** (31 maart 2026) is expliciet benadrukt om **planning en context binnen één instelling** als **startpunt** te nemen: zelfs tussen **opleidingsdomeinen** binnen dezelfde instelling bestaat al spanning op **planningsdomeinen** en **leeruitkomsten** — voordat sectorbrede **orchestratie** (in het gesprek o.a. **Edu Exchange**, **Edibroker**, multi-institutionele aggregatie) volledig wordt ingevuld.

Dit raakt de **volgorde van uitwerking** en de **grenzen van MVP’s**: [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md) kiest al voor een **eerste diepgaande keten** rond curriculum–catalogus; deze ADR **verankert** de bredere strategische lijn dat **intra-institutionele** logistieke haalbaarheid **voorrang** heeft op **federatieve** schaal over meerdere aanbieders.

### Beslissing (concept)

1. **Fasering:** OKx prioriteert **uitwerking en validatie** van **planning en onderwijslogistiek binnen één instelling** (één organisatorische context) vóór het normeren van **ketenoverschrijdende** scenario’s waarbij aanbod van **meerdere** instellingen tegelijk wordt gecombineerd.
2. **Sector-artefacten** (aggregators, broker-concepten, landelijke wallets) worden **niet** als vervanging van deze basis gezien; ze worden **gefaseerd** aangesloten zodra **data- en procesfundament** (o.a. leeruitkomsten, catalogusmetadata, trechters — [0006](0006-studentorientatie-trechter-ketenfase.md), [0007](0007-keuzecriteria-trechters-onderwijscatalogus.md)) voldoende zijn.
3. **Transparantie naar stakeholders:** documentatie en roadmap benoemen **bewust** wat **in scope** is per fase, om **verwachtingen** over “landelijke etalage” te managen.

### Alternatieven


| Optie                                                                  | Voordeel                                          | Nadeel / risico                                                                    |
| ---------------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **A. Direct federatief maximum** (multi-instelling eerst)              | Visie maximaal zichtbaar                          | **Niet uitvoerbaar** zonder standaardisatie en metadata (zie meeting-samenvatting) |
| **B. Alleen technische POC** zonder domeinafbakening                   | Snelle demo                                       | **Geen** bestuurbare keten bij planners/docenten                                   |
| **C. (Gekozen richting)** **Intra-instelling eerst**, daarna federatie | Beheerste complexiteit; aansluiting op transcript | **Politieke druk** op snelle sector-hub; mitigatie via roadmap en ADR’s            |


### Consequenties

- **Backlog:** issues rond **regionale hubs** en **arbeidsmarkt-koppeling** worden **gelaagd** naast MVP intra-instelling.
- **Afstemming Npuls:** samenvatting noemt afstemming **tussen pijlers** (o.a. vóór 22 april 2026); dit ADR ondersteunt die planning als **architectuurrichting**.

### Impact op `architecture/model/model.archimate`

- **Views:** scenario’s in het model **labelen** (of taggen) als **intra-instelling** vs **multi-instelling** waar dat helpt bij review.
- **Geen verplichte wijziging** aan bestaande elementen; wel **discipline** in nieuwe views: eerst **enkele** organisatie-context tenzij expliciet anders besloten.

### Relaties en links

- **Gerelateerde ADR’s:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md), [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md), [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md), [0006](0006-studentorientatie-trechter-ketenfase.md), [0007](0007-keuzecriteria-trechters-onderwijscatalogus.md)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria_20260331/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)`

### Vervangt (optioneel)

- —

