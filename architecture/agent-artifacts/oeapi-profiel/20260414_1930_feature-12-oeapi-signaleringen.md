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
| `onderwijsSpecificatie` | `educationSpecification` |
| `leervorm` | `deliveryForm` |
| `waardeDocument` | `credentialDocument` |
| `deelnameVereisten` | `participationRequirements` |
| `simulatie` | `simulation` |
| `zelfstudie_begeleid` | `guided_self_study` |
| `stage` | `internship` |
| `deelkwalificatie` | `partial_qualification` |
| `mbo_certificaat` | `mbo_certificate` |

# Feature 12 — OEAPI signaleringen en change requests

## 1. Probleem en doel

Het OKx-profiel gebruikt consumer-extensies als **workaround** voor zes tekortkomingen in de OEAPI-kern. Deze signaleringen moeten geformaliseerd worden als **concrete change request-voorstellen** zodat het kernteam ze kan indienen bij de OEAPI-werkgroep. Daarnaast moet `consumerKey: "okx"` worden geregistreerd.

**Succescriterium:** Zes change request-concepten, elk met probleembeschrijving, impact, oplossingsvoorstel en alternatieven. Plus een registratieverzoek voor de consumerKey.

## 2. Scope

| Binnen scope | Buiten scope |
|-------------|-------------|
| 6 change request-concepten als markdown | Indiening bij OEAPI-werkgroep (governance-actie) |
| `consumerKey: "okx"` registratieverzoek | Implementatie van de wijzigingen in OEAPI-kern |

## 3. Referenties

Projectaanvraag §9 (signaleringen). Alle feature-ontwerpdocumenten (1-11) waar workarounds zijn beschreven.

## 4. Data en validatie

Geen nieuwe schema-bestanden. Dit is documentatie.

## 5. Happy-path narratief

Niet van toepassing — dit is een documentatiefeature.

## 6. Feature-specifieke diepte

### Signalering 1: `studyLoad` op LearningComponent / TestComponent

| Aspect | Inhoud |
|--------|--------|
| **Probleem** | `studyLoad` (StudyLoadDescriptor) bestaat op `Programme` en `Course` maar niet op `LearningComponent` of `TestComponent`. OKx heeft de bottom-up aggregatie-invariant `SOM(components) = course` nodig (ADR 0004). |
| **Impact** | Zonder studyLoad op component-niveau kan de aggregatie niet in de kern worden afgedwongen. Consumer-extensie `componentStudyLoad` (feature 4) is de workaround. |
| **Oplossingsvoorstel** | Voeg `studyLoad` (array StudyLoadDescriptor) toe aan `LearningComponent` en `TestComponent` als optioneel kernveld, identiek aan de bestaande implementatie op `Course`. |
| **Alternatieven** | (a) Alleen via consumer-extensie (huidige workaround). (b) Via `duration` met conversielogica — verworpen: `duration` is kalendermatig, niet inspanningsmatig. |

### Signalering 2: Uitbreiding `modesOfDelivery` extensible-enum

| Aspect | Inhoud |
|--------|--------|
| **Probleem** | OKx-leervormen (simulation, guided_self_study) zijn niet uitdrukbaar in de bestaande `modeOfDelivery`-waarden. De OKx-extensie `educationSpecification.deliveryForm` is de workaround (feature 1). |
| **Impact** | Systemen die alleen kern `modesOfDelivery` lezen missen OKx-leervorminformatie. |
| **Oplossingsvoorstel** | Voeg OKx-waarden toe aan `x-ooapi-extensible-enum` op `modeOfDelivery`: `x-simulation`, `x-guided_self_study`, `x-internship`, `x-co_teaching`. |
| **Alternatieven** | (a) Alleen via consumer-extensie (huidige workaround). (b) Mapping-tabel in documentatie — reeds opgenomen in feature 1. |

### Signalering 3: `prerequisiteIds` op Course / LearningComponent

| Aspect | Inhoud |
|--------|--------|
| **Probleem** | OEAPI heeft geen mechanisme om volgordelijkheid (prerequisites) uit te drukken. OKx `participationRequirements` (feature 3, 4) is de workaround. |
| **Impact** | Cross-instelling prerequisite-ketens zijn niet interoperabel zonder een kernmechanisme. |
| **Oplossingsvoorstel** | Voeg `prerequisiteIds` toe als optioneel veld op `Course` en `LearningComponent`: `type: array, items: { $ref: './Identifier.yaml' }`. Met een `prerequisiteType` enum: `completed`, `concurrent`. |
| **Alternatieven** | (a) Alleen via consumer-extensie. (b) Via `Association`-entiteit — verworpen: verkeerd semantisch niveau. |

### Signalering 4: `credentialDocument` als kern-attribuut

| Aspect | Inhoud |
|--------|--------|
| **Probleem** | `formalDocument` op `Programme` is beperkt (6 waarden, geen `register`-veld). OKx `credentialDocument` (feature 1) voegt badge, partial_qualification, mbo_certificate toe. |
| **Impact** | De credentialing-cascade (badge → micro_credential → certificate → diploma) is niet in de kern uitdrukbaar. |
| **Oplossingsvoorstel** | (a) Uitbreiden `formalDocument` extensible-enum met: `x-badge`, `x-partial_qualification`, `x-mbo_certificate`. (b) Overweeg een `credentialRegister`-veld naast `formalDocument`. |
| **Alternatieven** | Alleen via consumer-extensie (huidige workaround). |

### Signalering 5: Keuze-/plaatsingsobject (SKS ↔ SVS)

| Aspect | Inhoud |
|--------|--------|
| **Probleem** | OEAPI heeft `Association` voor student-offering relaties, maar geen concept voor een **keuze** die nog niet tot inschrijving heeft geleid. Het SKS heeft een "concept-leerroute" nodig die naar SVS wordt gestuurd. |
| **Impact** | De stap "Student kiest → intekening" (ArchiMate stap 5) is niet in OEAPI te modelleren. |
| **Oplossingsvoorstel** | Een nieuw entiteitstype `Choice` of `Placement` met: studentId, offeringIds, status (concept/definitief), learningOutcomeIds. |
| **Alternatieven** | (a) Gebruik `Association` met status-extensie. (b) Buiten OEAPI om (custom API). De keuze is complex en vereist verdere discussie in de OEAPI-werkgroep. |

### Signalering 6: Recurrence-model voor roostering

| Aspect | Inhoud |
|--------|--------|
| **Probleem** | OEAPI heeft geen recurrence-patroon op offerings. "Elke dinsdag 10:00-12:00 gedurende 8 weken" vereist nu 8 aparte `LearningComponentOffering`-objecten. |
| **Impact** | Schaalprobleem: 1 leeractiviteit × 32 weken = 32 offerings i.p.v. 1 offering met recurrence. |
| **Oplossingsvoorstel** | Een `recurrence`-object op offerings: `{ frequency: string, interval: integer, count: integer, daysOfWeek: array }` gebaseerd op RFC 5545 (iCalendar RRULE). |
| **Alternatieven** | (a) Meerdere offerings (huidige workaround). (b) Via `duration` + `startDateTime` + conventie — fragiel en niet machine-interpreteerbaar. |

### ConsumerKey-registratie

| Aspect | Inhoud |
|--------|--------|
| **Actie** | Registreer `consumerKey: "okx"` bij de OEAPI-werkgroep conform de [consumer registry](https://openonderwijsapi.nl/v6.0/#/technical/consumers-and-profiles/) procedure. |
| **Eigenaar** | OKx-kernteam |
| **Informatie** | Naam: "Open Ketenstandaard (OKx)". Versie: V1. Doel: verrijking van onderwijscatalogus met flexibel-onderwijs-specificaties. |

## 7. Faalpad

**Scenario:** De OEAPI-werkgroep wijst een change request af.

**Mitigatie:** De consumer-extensie workaround blijft functioneel. Het OKx-profiel is ontworpen om zelfstandig te werken; kernwijzigingen zijn wenselijk maar niet blokkerend.

## 8. Ontwerpkeuzes

| # | Keuze | Motivatie | Alternatief |
|---|-------|-----------|-------------|
| 1 | Alle 6 signaleringen als change request-concept (niet als issue-draft) | Geeft het kernteam een compleet, gereviewd document om mee naar de werkgroep te gaan. | GitHub issue-drafts — sneller maar minder gedetailleerd; overweeg als follow-up. |
| 2 | Prioriteitsvolgorde: S1 > S3 > S4 > S2 > S6 > S5 | S1 (studyLoad op component) blokkeert de aggregatie-invariant het meest; S5 (keuze-object) is het meest complex en vereist het langste traject. | Geen prioritering — verworpen: OEAPI-werkgroep heeft beperkte capaciteit. |

## 9. Signaleringen

N.v.t. — dit document **is** de signaleringenverzameling.

## 10. Verificatie

- [ ] Alle 6 signaleringen uit projectaanvraag §9 zijn uitgewerkt
- [ ] Elke signalering heeft: probleem, impact, oplossingsvoorstel, alternatieven
- [ ] ConsumerKey-registratieverzoek is beschreven
- [ ] Prioriteitsvolgorde is vastgesteld
- [ ] Geen implementatiewerk in dit document (scope-check)
