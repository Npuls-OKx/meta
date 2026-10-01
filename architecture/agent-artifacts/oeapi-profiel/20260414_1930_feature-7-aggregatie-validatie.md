---
created: "2026-04-14T19:30:00+02:00"
updated: "2026-04-14T20:00:00+02:00"
human_authors:
  - "Niek Derksen (Architect OKx)"
human_reviewers: []
agent_command: "ontwerp-document"
agent_model: ""
related_issues: []
source_paths:
  - "meta/architecture/agent-artifacts/feature-plans/20260414_1800_okx-oeapi-consumer-profiel.md"
  - "meta/architecture/agent-artifacts/project-requests/20260414_1500_okx-oeapi-consumer-profiel.md"
  - "meta/architecture/agent-artifacts/design-docs/20260414_1900_feature-1-enumeraties-en-gedeelde-typen.md"
  - "meta/architecture/agent-artifacts/design-docs/20260414_1930_feature-2-programme-extensie.md"
  - "meta/architecture/agent-artifacts/design-docs/20260414_1930_feature-3-course-extensie.md"
  - "meta/architecture/agent-artifacts/design-docs/20260414_1930_feature-4-lc-tc-extensie.md"
  - "meta/architecture/agent-artifacts/design-docs/20260414_1930_feature-6-learningoutcome-extensie.md"
notes: "Human-in-the-loop: auteurs zijn verantwoordelijk voor juistheid vóór PR/merge."
---

## NL → UK English mapping

| NL (oud) | EN (nieuw) |
|----------|-----------|
| `waardeDocument` | `credentialDocument` |
| `kwalificatieRef` | `qualificationReference` |
| `kerntaak` | `coreTask` |
| `keuzeMogelijk` | `choiceAvailable` |
| `onderwijsSpecificatie` | `educationSpecification` |
| `hierarchieNiveau` | `hierarchyLevel` |
| `eenheid` | `unit` |
| `bot` | `supervisedHours` |
| `oot` | `unsupervisedHours` |
| `leeractiviteit` | `learning_activity` |
| `lesopdracht` | `lesson_assignment` |
| `leeruitkomst` | `learning_outcome` |
| `lesuitkomst` | `lesson_outcome` |
| `regulier` | `regular` |
| `versneld` | `accelerated` |
| `summatief` | `summative` |
| `certificaat` | `certificate` |
| `microcredential` | `micro_credential` |
| `deelkwalificatie` | `partial_qualification` |
| `mbo_certificaat` | `mbo_certificate` |

# Feature 7 — Aggregatie-validatie en voorbeeldscenario's

## 1. Probleem en doel

Features 1-6 definiëren het OKx-profiel per entiteit. Feature 7 bewijst dat ze **samen een werkend geheel vormen** door end-to-end scenario's uit te werken en de aggregatie-invariant (`SOM(children) = parent`) formeel te documenteren. Dit is het **kritieke integratieijkpunt** vóór fase 2/3.

**Succescriterium:** Drie complete voorbeeldscenario's als OEAPI-responses met OKx-extensies, plus formele aggregatieregels die als validatiecriteria dienen voor voorbeeldbestanden.

## 2. Scope

| Binnen scope | Buiten scope |
|-------------|-------------|
| Aggregatie-invarianten documenteren | Implementatie van validatietooling (CI-pipeline) |
| 3 scenario's: regulier, modulair, cross-instelling | YAML-wijzigingen aan features 1-6 |
| Validatiecriteria als checklijst | Fase 2/3 attributen |

## 3. Referenties

Alle ontwerpdocumenten van features 1-6. Projectaanvraag §4.3 (scenario's A-E). ADR 0004 (SBU/EC), ADR 0012 (leerroutes).

## 4. Data en validatie

### Aggregatie-invarianten

| Regel | Formule | Geldt voor |
|-------|---------|-----------|
| **R1** Studielast Programme ↔ Courses | `Programme.studyLoad[unit=X].value = SOM(courses.studyLoad[unit=X].value)` waarbij courses = alle Courses met `programmeId = programme.programmeId` | Elke Programme (root en track) |
| **R2** Studielast Course ↔ Components | `Course.studyLoad[unit=X].value ≈ SOM(LearningComponents.componentStudyLoad[supervisedHours+unsupervisedHours])` | Elke Course |
| **R3** Studielast Component ↔ Children | `LC.componentStudyLoad[supervisedHours+unsupervisedHours] = SOM(children.componentStudyLoad[supervisedHours+unsupervisedHours])` als children bestaan | LearningComponent met children |
| **R4** LO-dekking | Elke `learningOutcomeId` op Programme-niveau moet ook voorkomen op minstens één child Course of LearningComponent | Programme |
| **R5** `credentialDocument`-cascade | `diploma` alleen op root Programme; `certificate`/`micro_credential` alleen op Course/LC; `badge` alleen op LC (kind) | Alle entiteiten met `credentialDocument` |
| **R6** `qualificationReference`-tracering | Root Programme met `qualificationReference.dossier` → elke coreTask in dat dossier is gedekt door minstens één Course/LO met bijbehorende `qualificationReference.coreTask` | Root Programme |

**Tolerantie R2:** De som hoeft niet exact te zijn vanwege afrondingen en overlappende activiteiten. Afwijking ≤ 5% is acceptabel.

### Geen nieuwe schema-bestanden

Feature 7 levert documentatie en voorbeeldbestanden, geen nieuwe YAML-schema's.

## 5. Happy-path narratief

Drie scenario's conform projectaanvraag §5:

### Scenario A: Jochem — Regulier voltijd (leerroute 1)

```
Programme "Apothekersassistent" (4800 SBU, diploma)
├── Programme "Track: Regulier" (track, 4800 SBU, regular)
│   ├── Course "Baliegesprekken" (240 SBU, micro_credential)
│   │   ├── LC "Gespreksvoering simulatie" (learning_activity, 120 SBU)
│   │   │   ├── LC "Les: Emotionele cliënt" (lesson_assignment, 30 SBU, badge)
│   │   │   ├── LC "Les: Medicatie-info" (lesson_assignment, 30 SBU, badge)
│   │   │   └── LC "Les: Culturele sensitiviteit" (lesson_assignment, 30 SBU, badge)
│   │   │   [SOM = 90 ≈ 120? → overige uren = voorbereiding/reflectie]
│   │   ├── LC "Farmaceutische theorie" (learning_activity, 80 SBU)
│   │   └── TC "Praktijkexamen" (summative, 4 SBU)
│   │   [SOM LCs = 120+80 = 200, TC = 4 → totaal 204 ≈ 240]
│   ├── Course "Farmaceutische kennis" (360 SBU, certificate)
│   ├── Course "BPV" (1200 SBU, certificate)
│   └── ... (overige courses tot SOM = 4800)
└── Programme "Track: Versneld" (track, 3600 SBU, accelerated)
    └── ... (subset courses, gedeeld via programmeIds)
```

**Perspectief student:** Jochem kiest bij intake het reguliere track. Het SKS toont het volledige programma als boom. Jochem volgt de voorgeschreven volgorde.

**Perspectief planner:** De planner ziet 4800 SBU met per course de BOT/OOT-verdeling, ruimte-eisen en expertiseprofielen. Kan roosteren op basis van `educationSpecification`.

**Perspectief ontwerper:** De curriculum-ontwerper publiceert het volledige programma naar de OC. Aggregatie klopt top-down (kwalificatiedossier → kerntaken → LO's → courses) en bottom-up (lessen → activiteiten → courses → programme).

### Scenario B: Sinead — Modulair studeren (leerroute 7)

```
Geen Programme-parent!
Course "Baliegesprekken" (240 SBU, micro_credential, choiceAvailable: true)
Course "Farmaceutische kennis" (360 SBU, micro_credential, choiceAvailable: true)
Course "Data-analyse gezondheidszorg" (180 SBU, micro_credential, choiceAvailable: true)
  └── (van een andere instelling, via Edubroker)
```

**Perspectief student:** Sinead kiest losse courses uit de catalogus, elk met `choiceAvailable: true`. Er is geen overkoepelend Programme — ze studeert modulair. Elk afgerond course levert een microcredential.

**Perspectief planner:** Planningssysteem ontvangt CourseOfferings met OKx-extensies. Geen programme-context, maar per course is de `educationSpecification` compleet.

### Scenario C: Macca — Cross-instelling (leerroute 5)

```
Instelling A:
Programme "Verpleegkundig specialist" (root, 7200 SBU, diploma)
├── Programme "Track: Personalisatie sector" (track, 7200 SBU)
│   ├── Course "Klinische vaardigheden A" (600 SBU) — instelling A
│   ├── Course "Ethiek in de zorg" (300 SBU) — instelling B (cross!)
│   │   └── consumer: [{consumerKey: okx, ...}, {consumerKey: eduxchange, alliances: [...]}]
│   └── ... overige courses

Instelling B:
Course "Ethiek in de zorg" (300 SBU, certificate)
  └── consumer: [{consumerKey: okx, choiceAvailable: true, ...}]
```

**Cross-instelling contract:** Course "Ethiek in de zorg" is gepubliceerd door instelling B met OKx-extensies. Instelling A neemt het op in haar track via `programmeIds`. De Course heeft **twee** consumer-objecten: OKx en EduXchange. Het SKS van instelling A toont de Course met de OKx-educationSpecification; het EduXchange-profiel faciliteert de inschrijving.

## 6. Feature-specifieke diepte

### 6.1 Validatiecriteria (testbaar)

```
VOOR ELK Programme P (root of track):
  1. SOM(courses_in_P.studyLoad[unit].value) = P.studyLoad[unit].value
     TOLERANTIE: ±5%
  2. VOOR ELKE Course C in P:
     SOM(LCs_in_C.componentStudyLoad.supervisedHours + unsupervisedHours) ≈ C.studyLoad[unit].value
     TOLERANTIE: ±10% (vanwege toetsen, overhead)
  3. P.credentialDocument.type IN {diploma, partial_qualification} als P.programmeType = programme
  4. C.credentialDocument.type IN {certificate, micro_credential, mbo_certificate}
  5. LC.credentialDocument.type IN {micro_credential, badge} of null

VOOR ELKE LearningOutcome LO met hierarchyLevel = learning_outcome:
  6. LO.parentIds is null of leeg
  7. Er bestaat minstens 1 Course of LC met learningOutcomeIds die LO.learningOutcomeId bevat

VOOR ELKE LearningOutcome LO met hierarchyLevel = lesson_outcome:
  8. LO.parentIds bevat minstens 1 UUID
```

### 6.2 Cross-instelling interoperabiliteitscheck

Voor scenario C geldt aanvullend:
- Course "Ethiek in de zorg" van instelling B moet **dezelfde OEAPI-structuur** hebben als courses van instelling A.
- `qualificationReference` referereert naar hetzelfde SBB-dossier (of is null als cross-sector).
- `educationSpecification` is ingevuld zodat het planningssysteem van instelling A de BOT/OOT kan interpreteren.

## 7. Faalpad

**Scenario:** Voorbeeldbestand `scenario-regulier.yaml` heeft een Programme met `studyLoad: 4800 SBU`, maar de som van de courses is 4200 SBU (er ontbreekt een course).

**Impact:** Het voorbeeldbestand valideert niet tegen regel R1. Dit signaleert een fout in de voorbeelden, niet in het schema.

**Mitigatie:** Validatiecriteria §6.1 worden handmatig of via script gecontroleerd. Feature 12 kan optioneel een CI-validatiescript bevatten.

## 8. Ontwerpkeuzes

| # | Keuze | Motivatie | Afgewogen alternatief |
|---|-------|-----------|----------------------|
| 1 | Tolerantie op aggregatie (±5%/±10%) | Exacte aggregatie is onrealistisch: toetsen, overhead, afronding. | Exacte match — verworpen: breekt bij elk reëel voorbeeld. |
| 2 | Drie scenario's (niet vijf) | Regulier, modulair, cross-instelling dekken de belangrijkste patronen. Overige Npuls-routes zijn variaties. | Vijf scenario's — overweeg in iteratie 2 als kernteam meer routes wil valideren. |
| 3 | Validatiecriteria als checklist, niet als executable script | Een script is een feature-12 concern (tooling). Dit document definieert *wat* gevalideerd moet worden. | Script nu schrijven — verworpen: buiten scope. |

## 9. Signaleringen

Geen nieuwe signaleringen. Feature 7 bevestigt of de workarounds uit features 1-6 werken.

## 10. Verificatie

- [ ] Scenario A: alle aggregatieregels R1-R8 kloppen
- [ ] Scenario B: courses zonder Programme-parent; `choiceAvailable: true`
- [ ] Scenario C: Course van instelling B in Programme van instelling A; dubbel consumer-profiel
- [ ] Alle voorbeelden bevatten geldige OKx-extensies conform features 2-6
- [ ] Scope niet overschreden: geen YAML-wijzigingen aan features 1-6
