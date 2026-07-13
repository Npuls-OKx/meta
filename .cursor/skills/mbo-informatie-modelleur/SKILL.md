---
name: mbo-informatie-modelleur
description: >-
  Modelleert het concept-informatiemodel van mbo-onderwijs binnen het OKx OEAPI
  consumer-profiel: gefaseerde, geneste onderwijsspecificaties (opleiding ->
  programma -> onderwijseenheid -> leeronderdeel -> lessenreeks -> les) in
  ASCII-boomvorm, met Nederlandse concept-attributen, keuzedelen als zelfstandig
  programma, en delta-modellering voor leerroute 2-9 t.o.v. de reguliere
  baseline. Gebruik bij informatiemodellering, gegevensanalyse, attribuut- en
  entiteituitwerking, ankertabel (§3.2.6) of specificatie-catalogus (§12.5), en
  als AMIGO-substap (gegevensanalyse -> berichtspecificatie).
disable-model-invocation: true
---

# MBO informatie modelleur

Vertaalt een kwalificatiedossier + scenario naar een **concept-informatiemodel**:
een gefaseerde, geneste **onderwijsspecificatie** in ASCII-boomvorm, met
attributen op elk niveau. Dit is de **gegevensanalyse-stap** die de
**berichtspecificatie** voedt.

## Positie in de AMIGO-harness

Substap van de [AMIGO-aanpak](../amigo-aanpak/SKILL.md) (Edustandaard). In de
OKx-nummering is dit **stap 2 (gegevensanalyse)**; het levert het
informatiemodel dat de latere **berichtspecificatie** (stap 5) concreet maakt.

- **Input:** scenario-uitwerking uit [`okx-oeapi-scenario-uitwerking`](../okx-oeapi-scenario-uitwerking/SKILL.md) (stap 1), kwalificatiedossier, ankertabel.
- **Output:** geneste onderwijsspecificatie (entiteiten + attributen) als leg-up naar **koppelingen** (gestandaardiseerde informatiestromen) en uiteindelijk **koppelvlakken** (endpoints in spec).
- Blijf op **model-/kaderniveau**: geen volledige OEAPI-payloads, endpoints of stack-keuzes tenzij expliciet gevraagd.

## Informatiestroom → koppeling → koppelvlak

Het informatiemodel beschrijft **wat** er in een informatiestroom zit (entiteiten + attributen). Dat is nog geen koppeling of koppelvlak:

- **Informatiestroom** — welke objecten bewegen tussen welke ketenpartners (conceptueel).
- **Koppeling** — gestandaardiseerde realisatie van die stroom (berichten + interactie; AMIGO stap 3–5).
- **Koppelvlak** — technische endpoint-set in de spec-repo (AMIGO stap 6).

Milestone 3 ([OC P afgerond](https://github.com/Npuls-OKx/meta/milestone/3)) levert in meta **`v0.1.0`**: informatiemodellen en eerste gestandaardiseerde koppelingen voor OC P (LR1–LR3); volledige koppelvlakken volgen bij **`v1.0.0`**. Zie [`doc/OKx_Release-management-en-versionering.md`](../../../doc/OKx_Release-management-en-versionering.md) §8.

## Bron van waarheid

- Primair document: `architecture/docs/specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md`.
- **Ankertabel** (§3.2.6): 6 niveaus × 6 families is de normatieve verankering van entiteiten en cardinaliteiten.
- **Specificatie-catalogus** (§12.5): attributen per specificatie-object (Engelse, OEAPI-nabije namen).
- **OEAPI-mapping** (§5): recursief datamodel `Programme` / `Course` / `LearningComponent` / `TestComponent`.
- Werk **binnen** de definities en nummering; verzin geen parallelle begrippenlijst. Gaps → signalering / change request (§1.4, §9).

## Entiteiten (ankertabel §3.2.6)

Gebruik consequent deze niveaus en hun OEAPI-mapping:

| Niveau (rij)         | Concept-entiteit (specificatie)  | OEAPI-mapping                          |
| -------------------- | -------------------------------- | -------------------------------------- |
| Kwalificatiedossier  | `Opleidingsspecificatie`         | `Programme` (root)                     |
| Kwalificatie         | `Opleidingsprogramma-specificatie` | `Programme` (track)                  |
| Kerntaak             | `Onderwijseenheid-specificatie`  | `Course`                               |
| Werkproces           | `Leeronderdeel-specificatie`     | `LearningComponent` (learning_activity)|
| (lessenreeks)        | geneste `Leeronderdeel`/reeks    | `LearningComponent` (learning_activity)|
| Lesdoel/Lesuitkomst  | `Lesspecificatie`                | `LearningComponent` (lesson_assignment)|
| Toets (cross-cutting)| `Toetsonderdeel-specificatie`    | `TestComponent`                        |

Hulpspecificaties (§12.5.7–12.5.10): `Lesplan`, `Leertaak-specificatie`, `LesmateriaalSpecificaties`, `Leervormspecificatie`.

## Modelleerregels (normatief)

1. **Faseren volgens de instellingsjourney.**
   - **Fase 1–2 (grofmazig ontwerp → publiceerbaar/planbaar):** opleidingsspecificatie → opleidingsprogramma's (leerwegen) → onderwijseenheden (kerntaken) → leeronderdelen (werkprocessen), met organiseerbaarheids-waarden (BOT/OOT, BPV, ruimtetype, expertiseprofiel). Rol: **onderwijsontwerper**.
   - **Fase 4 (detaillering):** lessenreeksen en lessen met lesplan, werkinstructie (leertaak), leermateriaal, lesdoel/lesuitkomst en toetsonderdeel. Rol: **onderwijsontwikkelaar**. Houd dit **indicatief**, niet uitputtend.
2. **Keuzedelen = zelfstandig programma.** Modelleer keuzedelen **niet** als onderwijseenheid binnen een diplomaprogramma, maar als een **eigen `opleidingsprogramma-specificatie`** met de losse keuzedelen als `onderwijseenheid-specificaties` eronder. **N:M-gekoppeld** aan de diplomaprogramma's (herbruikbaar over BOL/BBL/leerwegen, en potentieel over opleidingen/instellingen). Zie §17.3. Generieke onderdelen blijven wél onder het diplomaprogramma.
3. **Nederlandse concept-attributen.** Gebruik de Nederlandse labels uit de woordenlijst hieronder. Houd **OEAPI-entiteitnamen** (Programme/Course/LearningComponent/TestComponent) en `Association.state` **wel** in het Engels — dat zijn standaardnamen, geen concept-attributen.
4. **Delta t.o.v. de baseline (leerroute 2–9).** Beschrijf niet-reguliere leerroutes als **verschil** t.o.v. leerroute 1. De **boomstructuur en semantiek blijven gelijk**; markeer gewijzigde attributen met `Δ`. Wat verschuift zit in sturing en een handvol attributen (bv. `spreidingspatroon`, `bereik`, `alternatieveGelegenheden`, `thuisorganisatie`/`gastorganisatie`).
5. **Aggregatie-invariant.** Studielast telt bottom-up op: `SOM(leeronderdelen) = onderwijseenheid`, `SOM(onderwijseenheden) = programma` (§5.3).
6. **Stadia scheiden.** Specificatie ≠ planbaar aanbod ≠ geroosterd aanbod (§3.2.3). In fase 2 krijgen eenheden `spreidingspatroon` + capaciteit; resources blijven **profielen** (ruimtetype/expertiseprofielen), nog geen instanties. Verbintenis/resultaat = kolom 5–6 (`Association.state`).

## Woordenlijst — Nederlands concept-label ↔ §12.5 (OEAPI-nabij)

| Nederlands              | §12.5 / OEAPI-nabij        |
| ----------------------- | -------------------------- |
| `kwalificatieverwijzing`| `qualificationReference`   |
| `curriculumtype`        | `curriculumType`           |
| `status`                | `status`                   |
| `versie`                | `version`                  |
| `waardedocument`        | `credentialDocument`       |
| `studielast`            | `studyLoad`                |
| `tijdmodel`             | `timeModel`                |
| `programmastructuur`    | `programmeStructure`       |
| `programmatype`         | `programmeType`            |
| `leerroutetype`         | `learningRouteType`        |
| `dektLeeruitkomsten`    | `targetsLearningOutcomes`  |
| `dektLesuitkomsten`     | `targetsLessonOutcomes`    |
| `leervorm`              | `deliveryForm`             |
| `tijdsverdeling`        | `timeAllocation` (BOT/OOT) |
| `spreidingspatroon`     | `spreadPattern`            |
| `ruimtetype`            | `roomType`                 |
| `ruimtevereisten`       | `roomRequirements`         |
| `expertiseprofielen`    | `expertiseProfiles`        |
| `leermiddelengroepen`   | `learningResourceGroups`   |
| `deelnamevereisten`     | `participationRequirements`|
| `lesplanverwijzing`     | `lessonPlanRef`            |
| `leertaken`             | `learningTasks`            |
| `leermaterialen`        | `learningMaterials`        |
| `taakomschrijving`      | `taskDescription`          |
| `opleverproducten`      | `deliverables`             |
| `acceptatiecriteria`    | `acceptanceCriteria`       |
| `toetsniveau`           | `assessmentLevel`          |
| `toetsbereik`           | `assessmentScope`          |
| `werkprocescodes`       | `workProcessCodes`         |
| `toetsvorm`             | `testForm`                 |
| `resultaatmodel`        | `resultModel`              |
| `schaal`                | `scale`                    |
| `fasen`                 | `phases`                   |
| `formatieveControles`   | `formativeChecks`          |
| `bereik`                | `scope`                    |
| `alternatieveGelegenheden` | `alternativeOccasionRefs`|
| `thuisorganisatie`      | `homeOrganisation`         |
| `gastorganisatie`       | `hostOrganisation`         |
| `locatieverwijzing`     | `locationRef`              |
| `keuzeruimte`           | keuzedeelruimte (SBU)      |
| `keuzeBeschikbaar`      | `choiceAvailable`          |

Nieuwe attributen die (nog) niet in §12.5 staan: registreer als **signalering** (§9), verzin geen OEAPI-kernwijziging.

## ASCII-conventies

- Wikkel de boom in een ` ```text ` code fence; blanco regels rondom de fence.
- **Pure ASCII** boom-connectors: `+--` (tak), `` `-- `` (laatste tak), `|` (verticale lijn), inspringen met spaties.
- Entiteit in HOOFDLETTERS; instantie met `=`; niveau-/mapping-annotatie tussen haakjes: `(rij: Kerntaak | OEAPI: Course)`.
- Attributen als `label: waarde`, met `|` als scheider op één regel.
- Delta t.o.v. baseline: prefix `Δ` met tussen haakjes de oude waarde: `Δ curriculumtype: hybride  (LR1: nominaal)`.
- Markeer verzonnen invulling met `(indicatief)`.

## Skabloon (structuur)

```text
OPLEIDINGSSPECIFICATIE                 (rij: Kwalificatiedossier | OEAPI: Programme[root])
= <opleiding>  -  Crebo-dossier <nr>
  kwalificatieverwijzing: {...} | curriculumtype: <...> | status: <...> | versie: <...>
|
+-- OPLEIDINGSPROGRAMMA-SPECIFICATIE   (rij: Kwalificatie | OEAPI: Programme[track])
|   = <leerweg>  (diplomaprogramma)
|   +-- ONDERWIJSEENHEID-SPECIFICATIE  (rij: Kerntaak | OEAPI: Course)
|   |   +-- LEERONDERDEEL-SPECIFICATIE (rij: Werkproces | OEAPI: LearningComponent[learning_activity])
|   `-- keuzeruimte: <SBU> -> ingevuld vanuit het programma "Keuzedelen"
|
+-- OPLEIDINGSPROGRAMMA-SPECIFICATIE = Keuzedelen  (zelfstandig programma | OEAPI: Programme)
      koppeling: N:M-gekoppeld aan de diplomaprogramma's (§17.3)
      +-- ONDERWIJSEENHEID-SPECIFICATIE = Keuzedeel "<...>"
```

Fase 4 zoomt in op één werkproces → LESSENREEKS → LESSPECIFICATIE met
`lesplanverwijzing` → LESPLAN, `leertaken` → LEERTAAK-SPECIFICATIE,
`leermaterialen` → LESMATERIAALSPECIFICATIES, plus TOETSONDERDEEL-SPECIFICATIE.

## Checklist vóór afronden

- [ ] Entiteiten en cardinaliteiten conform ankertabel (§3.2.6); OEAPI-mapping (§5) klopt.
- [ ] Attributen in het **Nederlands** (woordenlijst); OEAPI-entiteitnamen/`Association.state` in Engels.
- [ ] **Keuzedelen** als zelfstandig programma met onderwijseenheden eronder (N:M, §17.3).
- [ ] Gefaseerd: fase 1–2 grofmazig + fase 4 detaillering (indicatief).
- [ ] Leerroute 2–9 als **delta** (`Δ`) t.o.v. leerroute 1; structuur/semantiek ongewijzigd.
- [ ] Aggregatie-invariant en stadia (specificatie/planbaar/geroosterd) gerespecteerd.
- [ ] Nieuwe/ontbrekende attributen als **signalering** (§9), geen OEAPI-kernwijziging.
- [ ] ASCII-conventies (pure ASCII, `text`-fence, `Δ`, `(indicatief)`).
- [ ] Leg-up naar berichtspecificatie leesbaar; geen verzonnen payloads/koppelvlakken.

## Governance

OKx-meta: issues en PR's; **alleen OKx-team merge**; link PR aan issues
(`Fixes #…` / `See also #…`). Zie `.cursor/rules/okx-governance.mdc`.
