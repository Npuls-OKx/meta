## Conceptuele gelaagdheid: kwalificatiekader, onderwijsspecificatie en onderwijsaanbod (uitlijning ROSA/KOOI)

Status: Voorstel

Datum: 2026-05-01

### Context

In het overleg **NDE/NVD — informatiestromen en hoofdplaat** (1 mei 2026) is het informatiemodel verder uitgewerkt om **semantische consistentie** te bereiken en discussies met externe architecten (o.a. MORA-verwijzing) te vermijden. Kernpunten uit transcript en samenvatting:

- **Strikte kolommen:** (1) kwalificatiekader / kwalificatiedossier, (2) **onderwijsspecificatie** (het ontwerp), (3) **onderwijsaanbod** (de realisatie), met daaronder toets- en resultaatsporen zoals in de tabel besproken.
- **Leeruitkomsten los van kwalificatiekader:** op kwalificatie- en dossierniveau worden geen directe leeruitkomsten gemodelleerd zoals in sommige MORA-voorstellen; op **kerntaak** worden leeruitkomsten als **aggregatie van op werkprocesniveau gedefinieerde** leeruitkomsten gezien; op **lesniveau** gaat het om lesdoelen / beoogde resultaten — dit corrigeert een **onderwijskundige oversimplificatie** (“alles = beloofde leeruitkomsten op dossierniveau”).
- **Structuur als DAG:** het model wordt als **directed acyclic graph** (geen cyclische redenering) beschouwd; informeel ook “boomstructuur” genoemd.
- **Terminologie:** onderwijsspecificatie uitgelijnd met **ROSA** en **KOOI** (Kernonderwijsinformatiemodel); aanbodterminologie sluit daarop aan met o.a. **leergelegenheid** (vs. afwijkende Engelse “assessment”-hallucinaties in conceptdiagrammen die nog hersteld moeten worden).

In het eerdere overleg **OKx NDE/NVD — SKS, examens en resultaatstructuren** (28 april 2026) speelt dezelfde spanning: **examen als abstracte container**, **exameninstrument**, **resultaatstructuur** en de verwarring tussen **opleidingsonderdeel, onderwijseenheid, leeronderdeel en leeractiviteit** (alignment MORA/HORA). Dat overleg benadrukt bovendien dat **leeruitkomsten** en **onderwijsspecificaties** inhoudelijk verschillende rollen hebben (“wat” vs “hoe”), met **ECTS/SBU** als brug — wat dit ADR niet herdefinieert maar wel **plaatst** in de gelaagdheid.

### Beslissing (concept)

1. OKx hanteert in domein- en koppelvlakbeschrijvingen **drie hoofdlagen** tussen kwalificatie en uitvoering: **kwalificatiekader** → **onderwijsspecificatie** → **onderwijsaanbod** (inclusief verbintenissen en resultaten op de in ROSA/KOOI passende granulariteit).
2. **Leeruitkomsten** worden **niet** primair op dossier-/kwalificatieniveau “opgeplakt”; aggregatie loopt **van werkproces naar kerntaak**; lesniveau gebruikt **lesdoelen / beoogde uitkomsten** als aparte semantiek.
3. **Naamgeving** van specificatie- en aanbodobjecten volgt **ROSA/KOOI** waar sectorstandaarden dat voorschrijven; afwijkingen (bijv. leergelegenheid) worden **expliciet** gedocumenteerd met rationale.
4. De **technische hiërarchie** (macro → micro, aggregatie SBU/EC) blijft gelden zoals in [0017](0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md); dit ADR voegt de **semantische scheiding kader/spec/aanbod** en **LO-plaatsingsregels** toe.

### Uitwerking - informatiemodel (6 kolommen × 6 rijen + toetsrij)

Dit model verduidelijkt de onderliggende **informatiestapeling** die we in OKx overal gebruiken. Je kunt het lezen als: *per kwalificatiekader-niveau (rij) hebben we een beoogde uitkomst, een specificatie, een aanbod-instantie, een verbintenis (association) en uiteindelijk een resultaat*.

#### Toelichting Kolommen (objectfamilies)


| Kolom                     | Betekenis                                                        | OEAPI-haak                                                                                    |
| ------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Kwalificatiekader**     | Normatief kader uit SBB/CROHO dat bepaalt *wat* geldig is        | `qualificationReference` (OKx) + `levelOfQualification`, `fieldsOfStudy`                      |
| **Beoogde leeruitkomst**  | Inhoudelijke uitkomsten die *gedekt moeten worden* op dit niveau | `LearningOutcome` (OEAPI) + OKx `hierarchyLevel`                                              |
| **Onderwijsspecificatie** | Ontwerp-/sjabloonvorm: *wat gaan we organiseren*                 | `Programme` / `Course` / `LearningComponent` / `TestComponent` + OKx `educationSpecification` |
| **Onderwijsaanbod**       | Concrete instantie in tijd/capaciteit                            | `*Offering` + `OfferingProperties`                                                            |
| **Onderwijsverbintenis**  | Relatie student ↔ aanbod (intekening/inschrijving)               | `Association` + `AssociationProperties`                                                       |
| **Onderwijsresultaat**    | Resultaat/aanwezigheid/afronding op die verbintenis              | `Association.state` + result-attributen op Offering (OEAPI)                                   |


Allignment met klus 53 Alignment MORA <> HORA MBO digitaal Architectuurberaad, en ROSA terminologie.

#### Informatiemodel en referemtiearchitectuur terminologie


| Kwalificatiekader                                                                            | Beoogde leeruitkomst                                                                                                                                                                    | Onderwijsspecificatie              | Onderwijsaanbod                                                                                                            | Onderwijsverbintenis                         | Onderwijsresultaat                                  |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| `Kwalificatiedossier`                                                                        | *n.v.t. op dit niveau*                                                                                                                                                                  | `Opleidingsspecificatie`           | `Opleidingsaanbod`                                                                                                         | `Opleidingsverbintenis`                      | `Opleidingsresultaat`                               |
| `Kwalificatie`                                                                               | *n.v.t. op dit niveau*                                                                                                                                                                  | `Opleidingsprogramma specificatie` | `Opleidingsprogramma aanbod`                                                                                               | `Opleidingsprogramma verbintenis`            | `Opleidingsprogramma resultaat`                     |
| `Kerntaak`                                                                                   | **Collectie van collecties van leeruitkomsten** (werkproces heeft meerdere leeruitkomsten, een kerntaak heeft meerdere werkprocessen, dus is een lijst, met lijsten van leeruitkomsten. | `Onderwijseenheid specificatie`    | `Onderwijseenheid aanbod`                                                                                                  | `Onderwijseenheid verbintenis`               | `Onderwijseenheid resultaat`                        |
| `Werkproces`                                                                                 | **Collectie leeruitkomsten** / collectie van een collectie van lesuitkomsten (bottom up)                                                                                                | `Leeronderdeel specificatie`       | **Leergelegenheid** = `LearningComponentOffering` waar `LearningComponent.consumer.okx.hierarchyLevel = learning_activity` | `Association` op `LearningComponentOffering` | `Association.state` (+ evt. resultaat-koppelvlak)   |
| *n.v.t. kwalificatiekader*                                                                   | `Lesdoel / Lesuitkomst`                                                                                                                                                                 | `Lesspecificatie`                  | **Lesgelegenheid** = `LearningComponentOffering` waar `LearningComponent.consumer.okx.hierarchyLevel = lesson_assignment`  | `Association` op `LearningComponentOffering` | `Association.state` (+ evt. aanwezigheid/resultaat) |
| Summatief: vaststelling Examencommissie t.o.v. leeruitkomsten / formatief: Instellingsbeleid | `Lesuitkomst`/set, `Leeruitkomst`/set, `Werkproces`/set, … (scope van toetsing)                                                                                                         | `Toetsonderdeel specificatie`      | `Toetsgelegenheid`                                                                                                         | `Toetsgelegenheid verbintenis`               | `Toetsresultaat / Aanwezigheid`                     |


Voetnoot: OKx richt zich in dit profiel primair op het beschrijven van de werkproceslaag. De entiteit ‘leergelegenheid’ (een groep van lessen) leidt uiteindelijk tot individueel geroosterde lessen. Binnen deze geroosterde lessen kunnen op hun beurt weer individuele (of geneste) lessen zitten; in de toekomst moeten ook deze recursief volgens het hierboven beschreven datamodel gemodelleerd kunnen worden. Dit geldt eveneens voor nog diepere sublagen, zoals bijvoorbeeld een ‘lessenreeks’ of specifieke leeractiviteiten binnen een les. Hiermee erkennen we expliciet dat er onder een “leergelegenheid” of “lessenreeks” nog een hiërarchie van leeronderdelen kan bestaan. Dit heeft directe impact op de wijze waarop bottom-up en top-down aggregatie van opleidingen en programma’s moet worden ontworpen en ondersteund in het datamodel.

**Cardinaliteit (normatief voor dit profiel):**

- `Kerntaak (1..*) Werkproces`
- `Werkrproces (1..*) Leeruitkomst` (summatief)
- `Leeruitkomst (0..*) Onderwijseenheid` / `Leeronderdeel` / `Toetsonderdeel` (dezelfde LO kan over meerdere onderdelen verdeeld zijn; onderdelen kunnen meerdere LO’s dekken)
- `Leeruitkomst (0..*) Lesuitkomst` (formatief; DAG/Boom-structuur)


### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. MORA-“alles is beloofde LO op dossier”** | Eenvoudig te tekenen in één blok | Conflicteert met onderwijskundige praktijk en met sectorstandaardterminologie; veroorzaakt debat met architecten |
| **B. Eigen OKx-woordenboek los van ROSA/KOOI** | Maximale vrijheid | Slechte interoperabiliteit; dubbele vertaalslagen naar OEAPI en landelijke kaders |
| **C. Alleen aanbod modelleren, specificatie impliciet** | Minder objecttypen | Geen heldere bron voor curriculumontwerp, examenstructuur en planning |
| **D. (Gekozen richting)** **Drielagen + ROSA/KOOI + expliciete LO-plaatsing** | Sluit aan bij standaarden en op 28 april besproken examen-/specificatie-onderscheid | Vereist zorgvuldige mapping naar OEAPI en voortdurende sync met standaardreleases |

### Consequenties

- **Specificatierepo en sequentiediagrammen** moeten termen uit deze gelaagdheid consequent gebruiken; inconsistente “test vs assessment”-splitsingen worden als **fout** in conceptmateriaal behandeld tot hersteld.
- **Stakeholders:** onderwijskundigen en examencommissies krijgen een expliciet kader waar **formatief/summatief** en **toetsing** in de matrix thuishoren (verdieping volgt in aparte uitwerkingen).
- **Samenhang met examen/resultaat:** de op 28 april beschreven keten **SKS → toetsinstrumenten → SVS resultaatstructuur** blijft functioneel onder [0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md); dit ADR positioneert de **data** waar die structuren op steunen in de **specificatie- en aanbodkolommen**.

### Overlap en relatie met bestaande ADR’s (expliciet)

- **[0017](0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md)** — zelfde hiërarchie- en aggregatiegedachte; **0019** verdiept **semantiek** (kader vs specificatie vs aanbod) en **waar** LO’s wel/niet gehangen worden. Geen vervanging: **aanvulling**.
- **[0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md)** — SBU/EC blijven de logistieke maat; **0019** beperkt zich niet tot maat maar tot **conceptuele lagen**.
- **[0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md)** — “student kiest op leeruitkomsten”; **0019** bewaakt dat **niet** alles een catalogus-LO op topniveau wordt.
- **[0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md)** — catalogusfundament; **0019** aligneert **begrippen** in die keten met ROSA/KOOI.
- **[0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md)** — keuzeniveau; **0019** raakt vooral **ontwerp- vs aanbodlaag**, niet het keuzeniveau zelf.

### Relaties en links

- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/20260501_nde_nvd_informatie_stromen_hoofdplaat/summary.md`
  - `architecture/meetings/20260501_nde_nvd_informatie_stromen_hoofdplaat/transcript.md`
  - `architecture/meetings/20260428_okx_nde_nvd_sks_examens_resultaat_structuren/summary.md` (examens, naamgevingsverwarring, LO vs specificatie)
- ArchiMate model: `architecture/model/model.archimate` — **impact (conceptueel, geen modelwijziging in deze PR):** views/diagrammen rond **informatiemodel / hoofdplaat / MOKA-IM** moeten de **drie kolommen** (kader, specificatie, aanbod) en **LO-aggregatie** visueel en in elementnamen weerspiegelen; relaties naar **EducationSpecification**-achtige objecten en **aanbod**-objecten aligneren met ROSA/KOOI-termen; cycli vermijden conform DAG-principe. Zie werkafspraken [0010](0010-archimate-moka-informatiemodel-werkafspraken.md).
- OKx docs: [`doc/Projectoverzicht.md`](../../doc/Projectoverzicht.md), [`doc/Informatiesstromen.md`](../../doc/Informatiesstromen.md), [`doc/Informatiestromen-ArchiMate-en-MOKA-view.md`](../../doc/Informatiestromen-ArchiMate-en-MOKA-view.md), [`architecture/docs/principes.md`](../docs/principes.md)
- [specificatie-repository > architecture/agent-artifacts/project-requests](https://github.com/Npuls-OKx/specification/blob/main/meta/architecture/agent-artifacts/project-requests/20260414_1500_okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md)

### Vervangt (optioneel)

- —
