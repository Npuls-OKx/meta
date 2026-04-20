## Werkafspraken: ArchiMate-model en MOKA-koppelvlakspecificatie (concurrent editing en sync)

Status: Voorstel

Datum: 2026-03-31

### Context

Het bestand `architecture/model/model.archimate` is de **centrale** architectuurvoorstelling voor OKx en groeit mee met **MOKA-koppelvlakspecificatie-views** en het **informatiemodel**. In het overleg **kaderstelling studentkeuze en criteria** (31 maart 2026) is afgesproken dat **Niek** en **Niels van Duin** het **informatiemodel** (in relatie tot de MOKA-view) verder **bijwerken** en dat **gelijktijdige** wijzigingen aan `model.archimate` **technische corruptie en merge-conflicten** riskeren — daarom moeten **werkafspraken** gelden voor **branches** en **timing** (samenvatting en transcript).

Dit ADR is **primair proces-/workflow** en staat naast inhoudelijke ADR’s [0001](0001-publieke-repo-en-samenwerkingsmodel.md) (PR’s) en [0006](0006-studentorientatie-trechter-ketenfase.md)–[0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) (inhoud keten).

### Beslissing (concept)

1. **Geen gelijktijdige** ongecoördineerde edits op `model.archimate` in **dezelfde of verschillende** feature branches zonder voorafgaande **afstemming** tussen de model-eigenaren (zoals besproken: Niek/Niels-kern).
2. **Wijzigingen** lopen via **pull request** met **review** en bij voorkeur **kleine, reviewbare** commits (consistent met [0001](0001-publieke-repo-en-samenwerkingsmodel.md)).
3. **MOKA-informatiemodel** en **data-objecten** onder de koppelvlakspecificatie-view worden **gesynchroniseerd** met proceswijzigingen uit o.a. [0006](0006-studentorientatie-trechter-ketenfase.md) en [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) in een **aparte sessie** (zoals gepland in het overleg), vastgelegd via PR met link naar dit ADR.

### Alternatieven


| Optie                                                                      | Voordeel                      | Nadeel / risico                                               |
| -------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| **A. Vrij editen zonder afspraken**                                        | Maximale snelheid individueel | **Merge-conflicten**, **corrupt XML**, verlies reviewbaarheid |
| **B. Alleen één persoon mag het model wijzigen**                           | Geen conflict                 | **Knelpunt** en single point of failure                       |
| **C. (Gekozen richting)** **Coördinatie + PR** + geen parallel zonder sync | Balans snelheid/kwaliteit     | **Discipline** nodig; agenda voor model-sessies               |


### Consequenties

- **Kernteam:** korte **sync** voor model-werk (stand-up of async “lock” afspraak in issue/PR).
- **Contributors buiten kernteam:** grote model-PR’s **vroeg** melden; bij twijfel **issue** voor afstemming.

### Impact op `architecture/model/model.archimate`

- **Direct:** geen inhoudelijke wijziging door dit ADR alleen — wel **governance** op **hoe** gewijzigd wordt.
- **Indirect:** voorspelbare **evolutie** van views en data-objecten voor studentoriëntatie, trechters en SKS/SVS-splitsing.

### Relaties en links

- **Gerelateerde ADR’s:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md), [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria_20260331/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md](../../doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md)`

### Vervangt (optioneel)

- —

