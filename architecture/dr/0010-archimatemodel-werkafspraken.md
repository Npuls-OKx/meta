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
4. **`*.archimate` wordt NOOIT regelgebaseerd gemerged** — niet door git, niet met de hand. Bij een conflict geldt de **merge-procedure** hieronder. Dit is technisch afgedwongen via `-merge` in `.gitattributes`.
5. **Valideren vóór commit**: `python3 scripts/validate-archimate.py architecture/model/model.archimate` moet **schoon** zijn (0 dode referenties, 0 dubbele id's, welgevormde XML).

### Merge-procedure bij een conflict op `model.archimate`

Het model is **één XML-boom** waarin views via **ID's** verwijzen naar elementen elders in het bestand. Een regelgebaseerde merge kan element-definities laten wegvallen terwijl de views blijven staan. Het resultaat is **geldige XML met dode verwijzingen** — een reviewer ziet dat niet in een diff van 5 MB, en **Archi gooit die objecten bij de eerstvolgende save stilzwijgend weg**. Daarmee wordt herstelbaar verlies definitief verlies.

Bij een conflict:

1. **Kies één kant wholesale.** Nooit handmatig samenvoegen.
   `git checkout --theirs -- architecture/model/model.archimate` (of `--ours`).
2. **Breng de andere kant terug via Archi**, niet via git — Archi merget op **ID-niveau**:
   zet de andere versie als los bestand klaar (`git show <ref>:architecture/model/model.archimate > architecture/model/_import_<naam>.archimate`, wordt genegeerd door `.gitignore`) en gebruik in Archi **File → Import → Another model into the selected model**. Zet daarbij het **vervangen/updaten van bestaande objecten UIT**: alleen nieuwe objecten toevoegen.
3. **Valideer** met `scripts/validate-archimate.py` en **open het model in Archi** om te bevestigen dat de views renderen. Pas dan committen.
4. Ruim het tijdelijke `_import_*.archimate`-bestand op.

**Let op:** het automatische `.bak`-bestand van Archi is **geen** herstelpad bij een merge-conflict. Het bevat de staat van de vorige lokale save en mist doorgaans het werk van de andere branch. De betrouwbare bronnen zijn de **commits zelf** (`HEAD` en `MERGE_HEAD`), die onveranderlijk in de historie liggen.

**Aanleiding (juli 2026):** bij een handmatige merge van `dev` in een feature branch vielen **276 element-definities** weg terwijl alle views bleven staan; dat leverde **295 dode verwijzingen** op, verspreid over 9 views — waaronder hoofdplaat 1.7, alle vijf de koppelvlak-views en de `Definitiemapping OEAPI vs OKx` (97% dood). Precies het risico dat dit ADR in maart 2026 benoemde. Het is hersteld door dev wholesale te nemen en de eigen view via Archi te importeren.

### Alternatieven


| Optie                                                                      | Voordeel                      | Nadeel / risico                                               |
| -------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| **A. Vrij editen zonder afspraken**                                        | Maximale snelheid individueel | **Merge-conflicten**, **corrupt XML**, verlies reviewbaarheid |
| **B. Alleen één persoon mag het model wijzigen**                           | Geen conflict                 | **Knelpunt** en single point of failure                       |
| **C. (Gekozen richting)** **Coördinatie + PR** + geen parallel zonder sync | Balans snelheid/kwaliteit     | **Discipline** nodig; agenda voor model-sessies               |


### Consequenties

- **Kernteam:** korte **sync** voor model-werk (stand-up of async “lock” afspraak in issue/PR).
- **Contributors buiten kernteam:** grote model-PR’s **vroeg** melden; bij twijfel **issue** voor afstemming.
- **Technisch afgedwongen:** `.gitattributes` bevat `architecture/model/*.archimate -merge`. Git **weigert** het bestand samen te voegen en dwingt een expliciete keuze voor één kant. De afspraak is daarmee geen discipline-kwestie meer.
- **Rebase/merge kost tijd:** wie lang op een branch doorwerkt met modelwijzigingen, moet de andere kant handmatig via Archi terugbrengen. Dat is een reden om model-werk **kort en gecoördineerd** te houden — precies wat beslissing 1 beoogt.

### Impact op `architecture/model/model.archimate`

- **Direct:** geen inhoudelijke wijziging door dit ADR alleen — wel **governance** op **hoe** gewijzigd wordt.
- **Indirect:** voorspelbare **evolutie** van views en data-objecten voor studentoriëntatie, trechters en SKS/SVS-splitsing.

### Relaties en links

- **Gerelateerde ADR’s:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md), [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/20260331_okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md](../../doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md)`

### Vervangt (optioneel)

- —

