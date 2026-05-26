---
created: "2026-04-29T17:10:00+02:00"
source_qualification_dossier: "meta/architecture/docs/kwalificatiedossier/Apothekersassistent-2.md"
purpose: "Voorbeeld-uitwerkingen kwalificatiedossier → kerntaak/werkproces → leeruitkomsten → OEAPI-objecten incl. aanbod/verbintenis/resultaat (vlaksmodel)."
notes:
  - "Deze voorbeelden zijn **richtsnoer** (pseudo-data), geen normatieve schema’s."
  - "Identifiers zijn illustratief; de kern is de **traceerbaarheid** en **kolom-/rij-discipline** uit §12.0."
---

# Voorbeeld-uitwerkingen — Apothekersassistent → OEAPI (OKx-profiel)

## Canonieke kwalificatiekaderverwijzing (voor deze voorbeelden)

```yaml
qualificationReference:
  scheme: "crebo"
  dossier: "23450"        # Crebo dossier (kwalificatiedossier)
  qualification: "27141"  # Crebo kwalificatie
```

## Voorbeeld 1 — Werkproces B1-K1-W1 → LO-set → Course/LC/TC (+ offering/association/result)

### Bron (kwalificatiedossier)

- **Werkproces**: `B1-K1-W1` — “Neemt de zorg-/adviesvraag in behandeling”
- **Kerntaak**: `B1-K1` — “Biedt farmaceutische patiëntenzorg”

### Beoogde leeruitkomsten (kolom: Beoogde leeruitkomst)

**Summatieve LearningOutcome (root)**

```yaml
learningOutcome:
  id: "lo-apoth-b1-k1-w1-001"
  name: "Neemt de zorg-/adviesvraag in behandeling"
  hierarchyLevel: "learning_outcome"       # OKx: leeruitkomst (summatief)
  standardisationStatus: "concept"
  qualificationReference:
    scheme: "crebo"
    dossier: "23450"
    qualification: "27141"
    coreTask: "B1-K1"
    workProcess: "B1-K1-W1"
```

**Formatieve LessonOutcomes (children in OEAPI LearningOutcome-DAG)**

```yaml
learningOutcomes:
  - id: "lo-apoth-b1-k1-w1-001a"
    name: "Stelt gerichte vragen en verzamelt patiëntinformatie"
    hierarchyLevel: "lesson_outcome"
    parentIds: ["lo-apoth-b1-k1-w1-001"]
    qualificationReference:
      scheme: "crebo"
      dossier: "23450"
      qualification: "27141"
      coreTask: "B1-K1"
      workProcess: "B1-K1-W1"
  - id: "lo-apoth-b1-k1-w1-001b"
    name: "Bepaalt passende vervolgstap en stemt af met patiënt/naastbetrokkenen"
    hierarchyLevel: "lesson_outcome"
    parentIds: ["lo-apoth-b1-k1-w1-001"]
    qualificationReference:
      scheme: "crebo"
      dossier: "23450"
      qualification: "27141"
      coreTask: "B1-K1"
      workProcess: "B1-K1-W1"
```

### Onderwijsspecificatie (kolom: Onderwijsspecificatie → OEAPI entiteiten)

**Programme (kwalificatie)**

```yaml
programme:
  id: "prog-apoth"
  name: "Apothekersassistent"
  programmeType: "programme"
  learningOutcomeIds:
    - "lo-apoth-b1-k1-w1-001"
    # ... plus alle overige werkproces-LO's ...
  consumer:
    okx:
      qualificationReference:
        scheme: "crebo"
        dossier: "23450"
        qualification: "27141"
```

**Course (onderwijseenheid/leeronderdeel)**

```yaml
course:
  id: "course-balie-intake"
  name: "Balie: zorg-/adviesvraag"
  learningOutcomeIds:
    - "lo-apoth-b1-k1-w1-001"
  consumer:
    okx:
      educationSpecification:
        deliveryForm: "simulation"
        timeAllocation: { bot: 40, oot: 20, unit: "sbu" }
        roomType: "simulation_practice_room"
        expertiseProfiles: ["pharmaceutical_assistant_coach", "roleplay_training"]
        learningResourceGroups: ["simulation_material", "digital_workstation"]
      credentialDocument: { type: "microcredential", register: "edubadges.nl" }
```

**LearningComponent (leeractiviteit + lesopdrachten)**

```yaml
learningComponents:
  - id: "lc-balie-simulatie"
    name: "Leeractiviteit: intake zorg-/adviesvraag (simulatie)"
    learningComponentType: "practical"
    learningOutcomeIds:
      - "lo-apoth-b1-k1-w1-001"
    consumer:
      okx:
        hierarchyLevel: "learning_activity"
        educationSpecification:
          deliveryForm: "simulation"
          timeAllocation: { bot: 30, oot: 10, unit: "sbu", spreadPattern: "2x per week, 4 weken" }
          roomType: "simulation_practice_room"
          roomRequirements: "balie, wachtruimte, kassasysteem (simulatie)"
          expertiseProfiles: ["roleplay_training"]
          learningResourceGroups: ["simulation_material"]

  - id: "lc-balie-les-1"
    parentId: "lc-balie-simulatie"
    name: "Lesopdracht: vragenstellen en informatie verzamelen"
    learningComponentType: "assignment"
    learningOutcomeIds:
      - "lo-apoth-b1-k1-w1-001a"
    consumer:
      okx:
        hierarchyLevel: "lesson_assignment"
        educationSpecification:
          deliveryForm: "simulation"
          timeAllocation: { bot: 10, oot: 5, unit: "sbu" }
          roomType: "simulation_practice_room"
          expertiseProfiles: ["roleplay_training"]
          learningResourceGroups: ["simulation_material"]
```

**TestComponent (summatief)**

```yaml
testComponent:
  id: "tc-balie-praktijk"
  name: "Praktijktoets: intake zorg-/adviesvraag"
  testComponentType: "practical_exam"
  learningOutcomeIds:
    - "lo-apoth-b1-k1-w1-001"
  consumer:
    okx:
      assessmentLevel: "summative"
      qualificationReference:
        scheme: "crebo"
        dossier: "23450"
        qualification: "27141"
        coreTask: "B1-K1"
        workProcess: "B1-K1-W1"
      educationSpecification:
        roomType: "simulation_practice_room"
        expertiseProfiles: ["assessor_pharmaceutical"]
        timeAllocation: { bot: 2, oot: 0, unit: "sbu" }
```

### Aanbod/verbintenis/resultaat (kolommen: Aanbod → Verbintenis → Resultaat)

```yaml
courseOffering:
  id: "courseOff-balie-intake-2026p1"
  courseId: "course-balie-intake"
  startDateTime: "2026-09-01T09:00:00+02:00"
  endDateTime: "2026-10-01T17:00:00+02:00"
  maxNumberStudents: 24

association:
  id: "assoc-student-123-courseOff-balie-intake-2026p1"
  role: "student"
  state: "enrolled"

result:
  minimal: "association.state -> completed/failed/withdrawn"
  evidence:
    learningOutcomeId: "lo-apoth-b1-k1-w1-001"
    judgement: "passed"
```

## Voorbeeld 2 — Werkproces B1-K2-W2 → LO-set → Course/LC (+ planning-impact)

### Bron (kwalificatiedossier)

- **Werkproces**: `B1-K2-W2` — “Houdt de voorraad bij”
- **Kerntaak**: `B1-K2` — “Voert logistieke taken uit in de apotheek”

### Beoogde leeruitkomsten

```yaml
learningOutcome:
  id: "lo-apoth-b1-k2-w2-001"
  name: "Houdt de voorraad bij (bewaken, bestellen, registreren)"
  hierarchyLevel: "learning_outcome"
  standardisationStatus: "concept"
  qualificationReference:
    scheme: "crebo"
    dossier: "23450"
    qualification: "27141"
    coreTask: "B1-K2"
    workProcess: "B1-K2-W2"
```

### Onderwijsspecificatie (resource-dominant; sterk relevant voor CSP)

```yaml
course:
  id: "course-voorraadbeheer"
  name: "Voorraadbeheer en distributieketen"
  learningOutcomeIds: ["lo-apoth-b1-k2-w2-001"]
  consumer:
    okx:
      educationSpecification:
        deliveryForm: "classroom"
        timeAllocation: { bot: 20, oot: 20, unit: "sbu" }
        roomType: "general_classroom"
        expertiseProfiles: ["pharmacy_logistics"]
        learningResourceGroups: ["digital_workstation", "inventory_system_training"]

learningComponent:
  id: "lc-voorraadbeheer-practicum"
  name: "Leeractiviteit: voorraadcontrole en bestelcyclus (practicum)"
  learningOutcomeIds: ["lo-apoth-b1-k2-w2-001"]
  consumer:
    okx:
      hierarchyLevel: "learning_activity"
      educationSpecification:
        deliveryForm: "simulation"
        timeAllocation: { bot: 10, oot: 5, unit: "sbu" }
        roomType: "workshop"
        roomRequirements: "oefenvoorraad + barcodescanner + trainingsomgeving voorraadbeheersysteem"
        expertiseProfiles: ["pharmacy_logistics", "digital_skills_coach"]
        learningResourceGroups: ["simulation_material", "digital_workstation"]
```

### Aanbod/verbintenis/resultaat

```yaml
learningComponentOffering:
  id: "lcOff-voorraadbeheer-practicum-2026w40"
  learningComponentId: "lc-voorraadbeheer-practicum"
  startDateTime: "2026-09-28T13:00:00+02:00"
  endDateTime: "2026-09-28T17:00:00+02:00"
  maxNumberStudents: 16

association:
  id: "assoc-student-123-lcOff-voorraadbeheer-practicum-2026w40"
  role: "student"
  state: "participating"
```

## Voorbeeld 3 — Werkproces B1-K3-W2 → LO-set → Course/LC/TC (+ reflectie/resultaat)

### Bron (kwalificatiedossier)

- **Werkproces**: `B1-K3-W2` — “Evalueert de werkzaamheden en ontwikkelt zichzelf als professional”
- **Kerntaak**: `B1-K3` — “Werkt mee aan kwaliteit en deskundigheid”

### Beoogde leeruitkomsten

```yaml
learningOutcome:
  id: "lo-apoth-b1-k3-w2-001"
  name: "Evalueert werkzaamheden en ontwikkelt zichzelf als professional"
  hierarchyLevel: "learning_outcome"
  standardisationStatus: "concept"
  qualificationReference:
    scheme: "crebo"
    dossier: "23450"
    qualification: "27141"
    coreTask: "B1-K3"
    workProcess: "B1-K3-W2"

learningOutcomes:
  - id: "lo-apoth-b1-k3-w2-001a"
    name: "Verzamelt feedback en vertaalt dit naar leerdoelen"
    hierarchyLevel: "lesson_outcome"
    parentIds: ["lo-apoth-b1-k3-w2-001"]
  - id: "lo-apoth-b1-k3-w2-001b"
    name: "Formuleert verbeterpunten en doet verbetervoorstellen"
    hierarchyLevel: "lesson_outcome"
    parentIds: ["lo-apoth-b1-k3-w2-001"]
```

### Onderwijsspecificatie (portfolio/reflectie-achtig; toetsing vaak formatief + summatief moment)

```yaml
course:
  id: "course-professionalisering"
  name: "Professionalisering en kwaliteitsontwikkeling"
  learningOutcomeIds: ["lo-apoth-b1-k3-w2-001"]
  consumer:
    okx:
      educationSpecification:
        deliveryForm: "guided_self_study"
        timeAllocation: { bot: 10, oot: 30, unit: "sbu" }
        roomType: "online"
        expertiseProfiles: ["coach_reflective_practice"]
        learningResourceGroups: ["e_learning_platform", "portfolio_tool"]

testComponent:
  id: "tc-portfolio-beoordeling"
  name: "Portfolio-beoordeling professionalisering"
  testComponentType: "portfolio_assessment"
  learningOutcomeIds: ["lo-apoth-b1-k3-w2-001"]
  consumer:
    okx:
      assessmentLevel: "summative"
      educationSpecification:
        deliveryForm: "online"
        expertiseProfiles: ["assessor_reflective_practice"]
        timeAllocation: { bot: 1, oot: 0, unit: "sbu" }
```

### Aanbod/verbintenis/resultaat

```yaml
testComponentOffering:
  id: "tcOff-portfolio-2027w10"
  testComponentId: "tc-portfolio-beoordeling"
  startDateTime: "2027-03-08T09:00:00+01:00"
  endDateTime: "2027-03-08T10:00:00+01:00"

association:
  id: "assoc-student-123-tcOff-portfolio-2027w10"
  role: "student"
  state: "completed"

result:
  minimal: "association.state + (eventueel) instelling-eigen result-record"
  evidence:
    learningOutcomeId: "lo-apoth-b1-k3-w2-001"
    judgement: "passed"
```

