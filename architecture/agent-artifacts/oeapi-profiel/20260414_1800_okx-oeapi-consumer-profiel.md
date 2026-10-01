---
created: "2026-04-14T18:00:00+02:00"
updated: "2026-04-14T18:45:00+02:00"
human_authors:
  - "Niek Derksen (Architect OKx)"
human_reviewers: []
agent_command: "maak-plan"
agent_model: ""
related_issues: []
source_paths:
  - "meta/architecture/agent-artifacts/project-requests/20260414_1500_okx-oeapi-consumer-profiel.md"
notes: "Human-in-the-loop: auteurs zijn verantwoordelijk voor merge naar de officiële werklijn."
---

# OKx OEAPI Consumer Profiel — Featureplan

## Overzicht

Dit plan ontbindt het OKx OEAPI consumer profiel (`consumerKey: "okx"`) in **12 features**, geordend op afhankelijkheid over drie fasen. De kern van de volgorde: eerst het **gedeelde vocabulaire** (enumeraties, specificatie-objecten), dan de **entiteit-extensies** per OEAPI-laag (Programme → Course → Component → Outcome), dan de **afnemer-specifieke verrijkingen** (SKS-trechters, planningsattributen), en tot slot **cross-instelling validatie** en **signaleringen** richting OEAPI-werkgroep.

Elke feature levert een concrete set YAML-bestanden in `source/consumers/OKx/V1/` en/of documentatie-artefacten. Er wordt **geen** OEAPI-kernspecificatie aangepast — alleen consumer-extensies en signaleringsdocumenten.

## Features (in implementatievolgorde)

### 1. OKx enumeraties en gedeelde typen

- **Wat:** Definieer alle OKx-specifieke enumeratiewaarden en herbruikbare subschema's die in meerdere entiteiten terugkomen. Dit is het vocabulaire dat alle volgende features gebruiken.
- **Hangt af van:** Geen
- **Levert op:**
  - `source/consumers/OKx/V1/enumerations/` — YAML-bestanden voor:
    - `leervormType` (simulatie, klassikaal, werkplekleren, projectonderwijs, zelfstudie_begeleid, stage, onderzoek, co_teaching, blended)
    - `ruimteType` (praktijkruimte_simulatie, collegezaal, werkplaats, lab, online, externe_werkplek, examenzaal, hybride)
    - `hierarchieNiveau` (leeractiviteit, lesopdracht)
    - `hierarchieNiveauLO` (leeruitkomst, lesuitkomst)
    - `waardeDocumentType` (diploma, certificaat, mbo_certificaat, deelkwalificatie, microcredential, badge)
    - `curriculumType` (nominaal, flexibel, hybride)
    - `keuzegateType` (nominaal, maatwerk, continu)
    - `leerrouteType` (regulier, versneld, temporiserend, personalisatie_intra, personalisatie_sector, personalisatie_cross_sector, vrije_keuze, bundelen, stapelen)
    - `toetsNiveau` (formatief, summatief)
    - `deelnameVereistenType` (afgerond, gelijktijdig)
    - `standaardisatieStatus` (concept, afgestemd, vastgesteld, verouderd)
  - Gedeelde subschema's (herbruikbaar via `$ref`):
    - `OnderwijsSpecificatie.yaml` — het specificatie-object (leervorm, tijdsbesteding, ruimte, expertise, leermiddelen)
    - `WaardeDocument.yaml` — `{ type, register }`
    - `KwalificatieRef.yaml` — `{ dossier, kwalificatie, kerntaak, werkproces }`
    - `Tijdsbesteding.yaml` — `{ bot, oot, eenheid, spreidingspatroon }`
    - `DeelnameVereiste.yaml` — `{ referentieId, type }`
- **Sluit uit:** Koppeling aan specifieke OEAPI-entiteiten (dat is feature 2-6). Geen enum-waarden voor fase 2/3-specifieke attributen (die worden in feature 8 en 10 toegevoegd).

---

### 2. Programme-extensie (curriculum- en kwalificatielaag)

- **Wat:** Definieer de OKx consumer-extensie voor `Programme`. Dit is de zwaarste entiteit: kwalificatiereferentie, leerroutetype, curriculumtype, keuzegate, waardeDocument en de overkoepelende onderwijsspecificatie.
- **Hangt af van:** 1 (enumeraties en gedeelde typen)
- **Levert op:**
  - `source/consumers/OKx/V1/Programme.yaml` — schema met alle fase-1 attributen:
    - `curriculumType`, `keuzegateType`, `leerrouteType`
    - `waardeDocument` (→ `$ref WaardeDocument.yaml`)
    - `kwalificatieRef` (→ `$ref KwalificatieRef.yaml`)
    - `leeruitkomstDekking`
    - `onderwijsSpecificatie` (→ `$ref OnderwijsSpecificatie.yaml`)
  - `source/consumers/OKx/V1/examples/Programme.yaml` — voorbeeldinstantie (Apothekersassistent met tracks)
- **Sluit uit:** Fase 2 attributen op Programme (`instroomEisen`, `uitstroomProfiel`, `regioAanbod`). Offering-extensies (die zijn feature 5).

---

### 3. Course-extensie (opleidingsonderdeel / leertaak)

- **Wat:** Definieer de OKx consumer-extensie voor `Course`. Bevat de onderwijsspecificatie op cursusniveau, waardeDocument, deelnamevereisten en kwalificatiereferentie.
- **Hangt af van:** 1 (gedeelde typen)
- **Levert op:**
  - `source/consumers/OKx/V1/Course.yaml` — schema met:
    - `onderwijsSpecificatie` (→ `$ref`)
    - `waardeDocument` (→ `$ref`)
    - `keuzeMogelijk` (boolean)
    - `deelnameVereisten` (array van `$ref DeelnameVereiste.yaml` met `courseId`)
    - `kwalificatieRef` (→ `$ref`)
  - `source/consumers/OKx/V1/examples/Course.yaml` — voorbeeld (Baliegesprekken, BPV)
- **Sluit uit:** LearningComponent/TestComponent extensies (feature 4). Offering-extensies (feature 5).

---

### 4. LearningComponent- en TestComponent-extensie (leeractiviteit / lesopdracht / toets)

- **Wat:** Definieer OKx consumer-extensies voor `LearningComponent` en `TestComponent`. Dit is waar de onderwijsspecificatie het meest concreet is: BOT/OOT per les, ruimte-eisen, expertiseprofiel, leermiddelen, spreidingspatroon.
- **Hangt af van:** 1 (gedeelde typen)
- **Levert op:**
  - `source/consumers/OKx/V1/LearningComponent.yaml` — schema met:
    - `hierarchieNiveau` (leeractiviteit / lesopdracht)
    - `onderwijsSpecificatie` (→ `$ref` — hier het meest gedetailleerd)
    - `waardeDocument` (→ `$ref`)
    - `componentStudyLoad` (→ `$ref Tijdsbesteding.yaml` met BOT/OOT)
    - `deelnameVereisten` (array met `learningComponentId`)
  - `source/consumers/OKx/V1/TestComponent.yaml` — schema met:
    - `toetsNiveau` (formatief / summatief)
    - `onderwijsSpecificatie` (subset: ruimte, expertise, tijdsbesteding)
    - `kwalificatieRef` (→ `$ref`)
  - `source/consumers/OKx/V1/examples/LearningComponent.yaml`
  - `source/consumers/OKx/V1/examples/TestComponent.yaml`
- **Sluit uit:** Offering-extensies. LearningOutcome-extensie (feature 6).

---

### 5. Offering-extensies (aanbod-/planningslaag)

- **Wat:** Definieer OKx consumer-extensies voor `ProgrammeOffering`, `CourseOffering` en `LearningComponentOffering`. Deze laag verbindt de catalogusspecificatie met de concrete uitvoering in tijd en capaciteit.
- **Hangt af van:** 2, 3, 4 (de bovenliggende entiteit-extensies moeten bestaan)
- **Levert op:**
  - `source/consumers/OKx/V1/ProgrammeOffering.yaml` — `cohortGrootte`, `doorlooptijdWeken`
  - `source/consumers/OKx/V1/CourseOffering.yaml` — `planningHorizon`, `minimaalAantalDeelnemers`, `parallelGroepen`
  - `source/consumers/OKx/V1/LearningComponentOffering.yaml` — (voorbereid, initieel leeg of minimaal — de `onderwijsSpecificatie` op de bovenliggende LearningComponent bevat al het meeste)
  - Voorbeeldbestanden per offering
- **Sluit uit:** Fase 2 offering-attributen (beschikbarePlaatsen, instroomMomenten, budgetIndicatie) — die worden in feature 9 toegevoegd.

---

### 6. LearningOutcome-extensie (leeruitkomsten / lesuitkomsten + CompetentNL)

- **Wat:** Definieer de OKx consumer-extensie voor `LearningOutcome`. Voegt hiërarchie-label, standaardisatiestatus, kwalificatiereferentie en **CompetentNL-referenties** toe. CompetentNL (nationale standaard voor skills, SBB/UWV/TNO/CBS) levert de gedeelde taal waarmee leeruitkomsten matchbaar worden met beroepen, vacatures en kwalificaties cross-instelling.
- **Hangt af van:** 1 (gedeelde typen)
- **Levert op:**
  - `source/consumers/OKx/V1/LearningOutcome.yaml` — schema met:
    - `hierarchieNiveau` (leeruitkomst / lesuitkomst)
    - `standaardisatieStatus`
    - `kwalificatieRef` (→ `$ref` met dossier, kerntaak, werkproces)
    - `sectorReferentie`
    - `competentNlRefs` (array: `{ uri, type, label }` — referenties naar CompetentNL vaardigheden en kennisgebieden via Linked Data URI's)
    - `competentNlRelatieType` (enum: `primair`, `ondersteunend`)
  - Gedeeld subschema: `CompetentNlRef.yaml` — `{ uri: string, type: enum (vaardigheid_algemeen, vaardigheid_generiek, vaardigheid_specifiek, kennisgebied), label: string }`
  - `source/consumers/OKx/V1/examples/LearningOutcome.yaml` — uitgewerkte voorbeelden gebaseerd op de Apothekersassistent-casus (root-leeruitkomsten B1-K1, B1-K2, B1-K3 met geneste lesuitkomsten, DAG-structuur met gedeelde lesuitkomst, CompetentNL-referenties per niveau)
- **Sluit uit:** Inhoudelijke definitie van leeruitkomsten zelf (dat is domein van SBB/instelling, niet van het profiel). Validatie of CompetentNL-URI's actueel zijn (dat is een runtime-concern).

---

### 7. Aggregatie-validatie en voorbeeldscenario's

- **Wat:** Documenteer de bottom-up aggregatie-invariant (`SOM(children) = parent`) en werk minimaal drie complete voorbeeldscenario's uit als end-to-end OEAPI-responses met OKx-extensies. Dit valideert dat features 1-6 samen een werkend geheel vormen.
- **Hangt af van:** 2, 3, 4, 5, 6 (alle entiteit-extensies)
- **Levert op:**
  - `source/consumers/OKx/V1/examples/scenario-regulier.yaml` — Jochem (leerroute 1): volledig genest Programme met tracks, courses, components, outcomes, offerings
  - `source/consumers/OKx/V1/examples/scenario-modulair.yaml` — Sinead (leerroute 7): losse courses zonder programme-parent, met waardeDocumenten
  - `source/consumers/OKx/V1/examples/scenario-cross-instelling.yaml` — Macca (leerroute 5): course van instelling B in programme van instelling A
  - Documentatie: `meta/architecture/agent-artifacts/design-docs/` — aggregatie-regels en validatiecriteria
- **Sluit uit:** Implementatie van validatietooling (dat is feature 12). Geen YAML-wijzigingen aan features 1-6 — alleen voorbeelden en documentatie.

---

### 8. Fase 2 Programme-extensies (trechters en instroomeisen)

- **Wat:** Voeg de SKS-gerichte attributen toe aan `Programme` en `ProgrammeOffering` die de trechterlogica ondersteunen: gestructureerde instroomeisen, uitstroomprofiel en regio.
- **Hangt af van:** 2, 5 (Programme- en Offering-extensies)
- **Levert op:**
  - Uitbreiding van `source/consumers/OKx/V1/Programme.yaml` met:
    - `instroomEisen` (array: `{ type, referentie, niveau }`)
    - `uitstroomProfiel` (enum)
  - Uitbreiding van `source/consumers/OKx/V1/ProgrammeOffering.yaml` met:
    - `instroomMomenten`, `beschikbarePlaatsen`, `regioAanbod`
  - Bijbehorende enumeraties (indien nodig) in feature 1-bestanden of als aparte toevoeging
  - Voorbeeldupdate
- **Sluit uit:** CourseOffering-trechters (feature 9). Daadwerkelijke query-implementatie in SKS.

---

### 9. Fase 2 CourseOffering-extensies (beschikbaarheid en budget)

- **Wat:** Voeg SKS-trechterattributen toe op `CourseOffering` die filteren op beschikbaarheidstype en kosten mogelijk maken.
- **Hangt af van:** 5 (CourseOffering-extensie)
- **Levert op:**
  - Uitbreiding van `source/consumers/OKx/V1/CourseOffering.yaml` met:
    - `beschikbaarheidsType` (doorlopend, periodiek, eenmalig)
    - `budgetIndicatie` (`{ bedrag, valuta, type }`)
  - Voorbeeldupdate
- **Sluit uit:** Implementatie van budgetberekeningen. Roostering/recurrence.

---

### 10. Fase 3 planningsattributen op offerings

- **Wat:** Voeg capaciteits- en planningsattributen toe die het planningssysteem nodig heeft bovenop de `onderwijsSpecificatie` die al in fase 1 zit.
- **Hangt af van:** 5 (Offering-extensies), 7 (validatie dat fase 1 werkt)
- **Levert op:**
  - Updates aan offering-YAML's:
    - `ProgrammeOffering`: `cohortGrootte`, `doorlooptijdWeken` (indien niet al in feature 5)
    - `CourseOffering`: `planningHorizon`, `minimaalAantalDeelnemers`, `parallelGroepen`
  - Documentatie: mapping ArchiMate-flow "Opleidingseenheid specifieke planning" → OEAPI-attributen
- **Sluit uit:** Fijnmazige roostering (recurrence-model). Dat is een signalering, geen feature.

---

### 11. Cross-instelling interoperabiliteitsdocumentatie

- **Wat:** Documenteer wat gestandaardiseerd moet zijn voor cross-instelling uitwisseling en wat instelling-specifiek mag blijven. Dit is het "contract" dat twee instellingen nodig hebben om aanbod via Sector Edubroker te delen.
- **Hangt af van:** 7 (scenario's, met name scenario-cross-instelling)
- **Levert op:**
  - `meta/architecture/agent-artifacts/design-docs/` — ontwerpdocument met:
    - Verplichte vs. optionele attributen per entiteit voor cross-instelling
    - Mapping `kwalificatieRef` ↔ SBB-dossiers (mbo) en CROHO (hbo)
    - Erkenningsprotocol: hoe `waardeDocument` + `learningOutcomes` leiden tot vrijstelling
    - Voorbeeldflow: Macca-scenario volledig uitgewerkt als OEAPI-uitwisseling
- **Sluit uit:** Implementatie van Edubroker-koppeling. Governance-afspraken (dat is een ADR).

---

### 12. OEAPI signaleringen en change requests

- **Wat:** Formaliseer de zes signaleringen uit de projectaanvraag (§9) als concrete OEAPI change request-voorstellen, zodat het kernteam deze kan indienen bij de OEAPI-werkgroep.
- **Hangt af van:** 7 (validatie bevestigt welke workarounds nodig zijn)
- **Levert op:**
  - Per signalering een change request-concept (markdown in `meta/architecture/agent-artifacts/design-docs/` of als GitHub issue-draft):
    1. `studyLoad` op `LearningComponent`/`TestComponent`
    2. Uitbreiding `modesOfDelivery` extensible-enum met OKx-waarden
    3. `prerequisiteIds` op `Course`/`LearningComponent`
    4. `waardeDocument` als kern-attribuut
    5. Keuze/plaatsingsobject (SKS ↔ SVS koppelvlak)
    6. Recurrence-model voor roostering
  - Per change request: probleembeschrijving, impact, voorgestelde oplossing, alternatieven
- **Sluit uit:** Indiening bij OEAPI-werkgroep (dat is een governance-actie, geen feature).

---

## Dwarsdoorsnijdende aandachtspunten

| Punt | Verwerking |
|------|-----------|
| **Bottom-up aggregatie-invariant** | Gedefinieerd in feature 7; gevalideerd per voorbeeldscenario. Alle entiteit-features (2-6) moeten de `studyLoad`-keten respecteren. |
| **Backward compatibility met RIO/EduXchange** | Bij elke entiteit-feature (2-6): controleer dat OKx-attributen niet conflicteren met bestaande profielen. Documenteer in feature 11 waar overlap is. |
| **Naming conventions** | Feature 1 definieert alle naamgeving. Alle enums in snake_case, consistent met OEAPI-conventie. Nederlands voor OKx-specifieke termen, Engels waar OEAPI-kern al Engels gebruikt. |
| **`consumerKey` registratie** | Moet bij OEAPI-werkgroep worden aangemeld. Opnemen als actie bij feature 12. |
| **Privacy** | Geen persoonsgegevens in het profiel (publieke repo). Credentialing (waardeDocument) is altijd op aanbodniveau, niet op studentniveau. |

## Sequencing-advies

**Features 2, 3, 4 en 6 zijn onderling onafhankelijk** en kunnen parallel worden ontworpen na feature 1. Ze raken elk een andere OEAPI-entiteit. Feature 5 (Offerings) hangt er wél van af omdat offerings verwijzen naar hun bovenliggende entiteiten.

**Feature 7 is het kritieke integratieïjkpunt.** Doe dit vóór fase 2/3 features (8-10) om te bevestigen dat de fase-1 extensies een samenhangend geheel vormen. Dit is het moment om enum-waarden en objectstructuren bij te stellen op basis van scenario-uitwerking.

**Features 8 en 9 kunnen parallel**, net als **10 en 11**. Feature 12 (signaleringen) kan op elk moment na feature 7 starten — het is documentatie, geen YAML.

```
Feature 1 (enumeraties + gedeelde typen)
    │
    ├── Feature 2 (Programme) ─────┐
    ├── Feature 3 (Course) ────────┤
    ├── Feature 4 (LC + TC) ───────┼── Feature 5 (Offerings)
    └── Feature 6 (LO) ───────────┘         │
                                             │
                              Feature 7 (aggregatie + scenario's)
                                    │
                        ┌───────────┼───────────┐
                  Feature 8    Feature 9    Feature 10
                  (trechters   (beschikb.   (planning-
                   Programme)   Course)      attributen)
                        │           │            │
                        └───────────┼────────────┘
                                    │
                             Feature 11 (cross-instelling docs)
                                    │
                             Feature 12 (OEAPI signaleringen)
```

## Open vragen

- **Enum-waarden `leervormType` en `ruimteType`:** De projectaanvraag geeft een startset. Zijn deze volledig? Moeten pilotinstellingen (Amsterdam, Rijnland) eerst valideren voordat we fixeren?
- **`kwalificatieRef` voor hbo:** SBB-dossiers gelden voor mbo. Hoe verwijzen we naar CROHO/NVAO voor hbo? Is er een equivalent `kwalificatieRef`-structuur of moet die sectoraal verschillen?
- **`spreidingspatroon`:** Nu een vrije string ("2x per week, 8 weken"). Moet dit gestructureerd worden (e.g. `{ frequentie: 2, eenheid: "week", duur: 8 }`) voor machine-interpreteerbaarheid?
- **Retroactieve programme-samenstelling (stapelen, leerroute 9):** Hoe wordt een programme dat bottom-up ontstaat uit losse courses technisch gerepresenteerd? Wordt het een `Programme` dat achteraf wordt aangemaakt met `programmeIds` die naar de al-behaalde courses wijzen?
- **Relatie met EduXchange `alliances`:** Als een course via een alliantie (EWUU/LDE) wordt gedeeld, hoe verhoudt OKx `keuzeMogelijk` zich tot EduXchange `visibleForOwnStudents`?
- **Tooling voor aggregatie-validatie (feature 7):** Moet er een validatiescript komen (bijv. in de CI-pipeline) dat controleert of SOM-invariant klopt in voorbeeldbestanden?
- **CompetentNL-URI stabiliteit (feature 6):** CompetentNL is per september 2025 live. Hoe stabiel zijn de Linked Data URI's? Moet het OKx-profiel een `validFrom`/`validTo` op `competentNlRefs` ondersteunen voor als URI's veranderen? Moet er een fallback via `otherCodes` met `codeType: "competentnl-skill"` zijn?
- **CompetentNL hbo-uitbreiding:** CompetentNL dekt momenteel alleen mbo-kwalificaties. Uitbreiding naar hbo is aangekondigd voor 2026+. Hoe gaan we om met hbo-leeruitkomsten die nog geen CompetentNL-mapping hebben?

## Open voor vervolg

Na goedkeuring van dit plan: ontwerpdocumenten per feature via `/ontwerp-document`, te beginnen bij feature 1 (vocabulaire vaststellen). Feature 7 (scenario-validatie) is het eerste moment waarop het kernteam de complete structuur end-to-end kan reviewen.
