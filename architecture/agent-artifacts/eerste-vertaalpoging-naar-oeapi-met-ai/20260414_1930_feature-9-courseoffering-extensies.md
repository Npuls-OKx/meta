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
  - "meta/architecture/agent-artifacts/design-docs/20260414_1930_feature-5-offering-extensies.md"
notes: "Human-in-the-loop: auteurs zijn verantwoordelijk voor juistheid vóór PR/merge."
---

## NL → UK English mapping

| NL (oud) | EN (nieuw) |
|----------|-----------|
| `beschikbaarheidsType` | `availabilityType` |
| `budgetIndicatie` | `budgetIndication` |
| `doorlopend` | `continuous` |
| `periodiek` | `periodic` |
| `eenmalig` | `one_time` |
| `bedrag` | `amount` |
| `valuta` | `currency` |
| `collegegeld` | `tuition_fee` |
| `cursusgeld` | `course_fee` |
| `materiaalkosten` | `material_costs` |
| `minimaalAantalDeelnemers` | `minimumParticipants` |
| `parallelGroepen` | `parallelGroups` |

# Feature 9 — Fase 2 CourseOffering-extensies (beschikbaarheid en budget)

## 1. Probleem en doel

Het SKS filtert niet alleen op programmaniveau (feature 8) maar ook op **course-niveau**: "Is deze course doorlopend of periodiek beschikbaar? Wat kost het?" De OEAPI-kern biedt `priceInformation` maar geen gestructureerd beschikbaarheidstype of budgetindicatie op OKx-niveau.

**Succescriterium:** `CourseOffering.yaml` wordt uitgebreid met `availabilityType` en `budgetIndication`.

## 2. Scope

| Binnen scope | Buiten scope |
|-------------|-------------|
| `availabilityType` en `budgetIndication` op CourseOffering | Budgetberekeningen, bekostigingslogica |
| | Roostering/recurrence (signalering, geen feature) |

## 3. Referenties

Feature 5 ontwerp, ADR 0007 (trechterparameters), OEAPI `CourseOffering.yaml`.

## 4. Data en validatie

### Uitbreiding CourseOffering

| Attribuut | Type | Beschrijving |
|-----------|------|-------------|
| `availabilityType` | enum | `continuous` (instroom op elk moment), `periodic` (vaste startmomenten), `one_time` (eenmalige uitvoering) |
| `budgetIndication` | object (nullable) | `{ amount: number, currency: string, type: enum }`. Type: `tuition_fee`, `course_fee`, `material_costs`. |

```yaml
# Toevoeging aan source/consumers/OKx/V1/CourseOffering.yaml
  availabilityType:
    type:
      - string
      - "null"
    description: |
      - continuous: entry possible at any time
      - periodic: fixed start moments (see core flexibleEntryPeriod)
      - one_time: single execution
    enum:
      - continuous
      - periodic
      - one_time
  budgetIndication:
    type:
      - object
      - "null"
    properties:
      amount:
        type: number
        description: Indicative amount.
        minimum: 0
      currency:
        type: string
        description: ISO 4217 currency code.
        example: EUR
      type:
        type: string
        enum:
          - tuition_fee
          - course_fee
          - material_costs
```

### Validatie

1. `availabilityType = continuous` → kern `flexibleEntryPeriodStartDateTime` mag gevuld zijn.
2. `budgetIndication.currency` conform ISO 4217.

## 5. Happy-path narratief

Student zoekt betaalbare cursussen. SKS queriet `GET /course-offerings?consumer=okx&availabilityType=continuous`. OC retourneert offerings met budgetindicatie zodat SKS een kostenfilter kan toepassen.

## 6. Feature-specifieke diepte

### Voorbeeld-YAML

```yaml
# Toevoeging aan examples/CourseOffering.yaml
- consumerKey: okx
  planningHorizon: "continuous"
  minimumParticipants: 8
  parallelGroups: 1
  availabilityType: continuous
  budgetIndication:
    amount: 250
    currency: EUR
    type: course_fee
```

### Relatie met OEAPI `priceInformation`

OEAPI-kern heeft `priceInformation` (array van `Cost`-objecten). OKx `budgetIndication` is een vereenvoudigde weergave voor trechterfiltering. Bij gedetailleerde kosteninfo: gebruik kern `priceInformation`.

## 7. Faalpad

**Scenario:** `budgetIndication` toont €250 maar kern `priceInformation` toont €500 (inclusief boeken).

**Mitigatie:** `budgetIndication.type` maakt expliciet welk kostentype het betreft. De student ziet beide bronnen; SKS kan de OKx-budgetindicatie gebruiken voor filtering en kern `priceInformation` voor detail.

## 8. Ontwerpkeuzes

| # | Keuze | Motivatie | Alternatief |
|---|-------|-----------|-------------|
| 1 | Eigen `budgetIndication` naast kern `priceInformation` | `priceInformation` is een complex object (Cost-array). OKx wil een eenvoudige indicatie voor filtering. | Alleen kern `priceInformation` — onvoldoende gestructureerd voor snelle trechterfiltering. |
| 2 | `availabilityType` als 3-waarden enum | Dekt de drie patronen die instellingen kennen. Uitbreidbaar via `x-`-prefix indien nodig. | Meer waarden — te vroeg zonder pilotvalidatie. |

## 9. Signaleringen

Geen nieuwe.

## 10. Verificatie

- [ ] Uitbreiding `CourseOffering.yaml` backward compatible
- [ ] `availabilityType` enum-waarden gedocumenteerd
- [ ] `budgetIndication` voorbeeld met `currency: EUR`
- [ ] Geen conflict met kern `priceInformation`
