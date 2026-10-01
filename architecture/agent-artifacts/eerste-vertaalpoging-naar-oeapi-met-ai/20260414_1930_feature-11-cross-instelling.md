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
  - "meta/architecture/agent-artifacts/design-docs/20260414_1930_feature-7-aggregatie-validatie.md"
notes: "Human-in-the-loop: auteurs zijn verantwoordelijk voor juistheid vóór PR/merge."
---

## NL → UK English mapping

| NL (oud) | EN (nieuw) |
|----------|-----------|
| `waardeDocument` | `credentialDocument` |
| `keuzeMogelijk` | `choiceAvailable` |
| `onderwijsSpecificatie` | `educationSpecification` |
| `leervorm` | `deliveryForm` |
| `tijdsbesteding` | `timeAllocation` |
| `kwalificatieRef` | `qualificationReference` |
| `deelnameVereisten` | `participationRequirements` |
| `hierarchieNiveau` | `hierarchyLevel` |
| `beschikbaarheidsType` | `availabilityType` |
| `budgetIndicatie` | `budgetIndication` |
| `standaardisatieStatus` | `standardisationStatus` |
| `kerntaak` | `coreTask` |
| `werkproces` | `workProcess` |
| `bot` | `supervisedHours` |
| `oot` | `unsupervisedHours` |
| `eenheid` | `unit` |
| `certificaat` | `certificate` |
| `klassikaal` | `classroom` |

# Feature 11 — Cross-instelling interoperabiliteitsdocumentatie

## 1. Probleem en doel

OKx moet niet alleen **binnen** een instelling werken, maar ook **ertussen**: instelling B ontsluit aanbod dat instelling A opneemt in haar programma (ADR 0012: leerroute als instellingsonafhankelijke entiteit). Daarvoor is een contract nodig: welke OKx-attributen zijn **verplicht** voor cross-instelling, welke **optioneel**, en hoe verloopt de uitwisseling via Sector Edubroker?

**Succescriterium:** Een helder document dat twee instellingen kunnen gebruiken als referentie voor het delen van aanbod via het OKx-profiel.

## 2. Scope

| Binnen scope | Buiten scope |
|-------------|-------------|
| Verplichte vs. optionele attributen per entiteit voor cross-instelling | Implementatie van Edubroker-koppeling |
| Mapping `qualificationReference` ↔ SBB/CROHO | Governance-afspraken (dat is een ADR) |
| Erkenningsprotocol: `credentialDocument` + `learningOutcomes` → vrijstelling | Authenticatie/autorisatie tussen instellingen |
| Macca-scenario volledig uitgewerkt | Wijzigingen aan OEAPI-kern |

## 3. Referenties

Feature 7 (scenario C: Macca), ADR 0012, projectaanvraag §5 (scenario's D en E).

## 4. Data en validatie

### Verplichte OKx-attributen voor cross-instelling uitwisseling

| Entiteit | Verplicht (cross-instelling) | Optioneel |
|----------|------------------------------|-----------|
| **Course** | `credentialDocument`, `choiceAvailable`, `educationSpecification.deliveryForm`, `educationSpecification.timeAllocation` | `qualificationReference`, `participationRequirements` |
| **LearningComponent** | `hierarchyLevel`, `componentStudyLoad` | `educationSpecification` (volledig), `credentialDocument` |
| **LearningOutcome** | `hierarchyLevel`, `qualificationReference` (als summatief) | `competentNlRefs`, `standardisationStatus` |
| **CourseOffering** | Kern: `startDateTime`, `endDateTime`, `state` | `availabilityType`, `budgetIndication` |

**Motivatie:** De ontvangende instelling moet minimaal weten: *wat* wordt er geleerd (LO's), *hoeveel* inspanning (studyLoad, BOT/OOT), *welke* credential (`credentialDocument`), en *wanneer* beschikbaar (offering dates). Alles erboven is verrijking.

### Mapping qualificationReference cross-sector

| Sector | Veld in `QualificationReference` | Bron |
|--------|---------------------------|------|
| MBO | `dossier` + `qualification` + `coreTask` + `workProcess` | SBB |
| HBO | `crohoCode` | CROHO/DUO |
| Cross-sector (mbo → hbo of v.v.) | Beide ingevuld waar van toepassing; `coreTask`/`workProcess` null bij hbo | Instelling |

### Erkenningsprotocol

```
Instelling B publiceert:
  Course "Ethiek in de zorg" (300 SBU, certificate)
    + learningOutcomeIds: [LO-ETH-001, LO-ETH-002]
    + qualificationReference: { dossier: null, crohoCode: "34560" }

Instelling A ontvangt via OC (of Edubroker):
  1. Matcht LO-ETH-001/002 op eigen kwalificatieraamwerk
  2. Bepaalt: "Deze LO's dekken kerntaak X in ons programma"
  3. Kent vrijstelling toe voor Course "Ethiek" in eigen track
  4. CredentialDocument van instelling B wordt erkend als certificate
```

## 5. Happy-path narratief

```mermaid
sequenceDiagram
    participant B_OC as OC instelling B
    participant Edu as Sector Edubroker
    participant A_OC as OC instelling A
    participant A_SKS as SKS instelling A

    B_OC->>Edu: Publiceert Course +<br>OKx-extensies +<br>LearningOutcomes
    Edu->>A_OC: Beschikbaar aanbod<br>(alle leergelegenheden i.r.t. LO's)
    A_SKS->>A_OC: GET /courses?<br>fieldsOfStudy=0916<br>&consumer=okx
    A_OC-->>A_SKS: Courses incl.<br>instelling-B aanbod
    Note over A_SKS: Student kiest Course<br>van instelling B,<br>SKS checkt LO-matching<br>en qualificationReference
```

## 6. Feature-specifieke diepte

### 6.1 Dubbel consumer-profiel

Een Course die cross-instelling wordt gedeeld draagt meerdere consumer-objecten:

```yaml
consumer:
  - consumerKey: okx
    credentialDocument:
      type: certificate
      register: DUO
    choiceAvailable: true
    educationSpecification:
      deliveryForm: classroom
      timeAllocation:
        supervisedHours: 200
        unsupervisedHours: 100
        unit: sbu
  - consumerKey: eduxchange
    alliances:
      - name: ewuu
        visibleForOwnStudents: false
```

### 6.2 LO-matching cross-instelling

Wanneer twee instellingen dezelfde CompetentNL-referenties gebruiken op hun LearningOutcomes, is automatisch zichtbaar welke overlap er is:

```
Instelling A LO: competentNlRefs: ["cnl:skill/specifiek/mondelinge-communicatie"]
Instelling B LO: competentNlRefs: ["cnl:skill/specifiek/mondelinge-communicatie"]
→ Match! Dezelfde skill wordt afgedekt → potentiële vrijstelling
```

Dit is de kracht van CompetentNL als gedeelde taal (feature 6).

## 7. Faalpad

**Scenario:** Instelling B publiceert een Course zonder `qualificationReference`. Instelling A kan niet bepalen of de LO's matchen met haar kwalificatiedossier.

**Impact:** Geen automatische matching; handmatige beoordeling nodig.

**Mitigatie:** `qualificationReference` is optioneel maar **sterk aanbevolen** voor cross-instelling. Het protocol beschrijft dat zonder `qualificationReference` de matching via `learningOutcomeIds` + `competentNlRefs` moet lopen.

## 8. Ontwerpkeuzes

| # | Keuze | Motivatie | Alternatief |
|---|-------|-----------|-------------|
| 1 | Minimumset verplichte attributen (niet alles verplicht) | Lage drempel voor deelname; meer attributen = betere matching maar hogere datakwaliteitseis. | Alles verplicht — verworpen: zou instellingen afschrikken. |
| 2 | CompetentNL als primaire matching-taal cross-instelling | Nationaal gestandaardiseerd; koppelt LO's aan arbeidsmarkt en kwalificaties. | Alleen ISCED-F `fieldsOfStudy` — te grof voor matching op vaardigheidsniveau. |

## 9. Signaleringen

| # | Probleem | Workaround | Aanbeveling |
|---|---------|-----------|-------------|
| 1 | Geen keuze-/plaatsingsobject in OEAPI | Cross-instelling plaatsing loopt buiten OEAPI om (bijv. via `Association`) | OEAPI change request: keuze-/plaatsingsentiteit (signalering 5 uit projectaanvraag) |

## 10. Verificatie

- [ ] Verplichte attributen-tabel is compleet voor alle entiteiten
- [ ] Mapping `qualificationReference` mbo ↔ hbo is beschreven
- [ ] Erkenningsprotocol is helder (stap-voor-stap)
- [ ] Macca-scenario is volledig uitgewerkt met dubbel consumer-profiel
- [ ] CompetentNL-matching voorbeeld aanwezig
- [ ] Geen governance-afspraken in dit document (scope-check)
