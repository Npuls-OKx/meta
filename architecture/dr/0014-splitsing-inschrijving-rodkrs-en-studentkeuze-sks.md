## Splitsing: inschrijving (ROD/KRS) en onderwijskundige keuze (SKS)

Status: Voorstel

Datum: 2026-04-20

### Context

In het overleg over **student keuzecriteria en plaatsing** is herbevestigd dat de keten een **duidelijk onderscheid** moet maken tussen:

- **Formele inschrijving** (o.a. voor ROD-bewijs/administratieve borging), en
- **Onderwijskundige keuze en samenstelling** van het leertraject (incl. LLO/maatwerk versus programma-student).

Zonder deze scheiding ontstaat een ontwerp waarin keuze-interactie, administratieve bewijsvoering en logistieke plaatsing door elkaar gaan lopen, met als gevolg onduidelijke verantwoordelijkheden tussen referentiecomponenten (met name rond SKS, KRS en eventuele intake/plaatsing-stappen).

Bron: `architecture/meetings/okx_kernteam_inhoud_verdiepen_student_keuze_criteria_en_plaatsing_20260409/summary.md`.

### Beslissing

We leggen vast dat het OKx-proces en de koppelvlakspecificaties **inschrijving** en **onderwijskundige keuze** als **onderscheiden processtappen** behandelen, met elk een eigen set informatie en verantwoordelijkheden:

1. **Inschrijving (ROD/KRS)** is primair een administratieve stap om de student formeel te registreren (incl. bewijsvoering/ROD-koppeling waar relevant).
2. **Studentkeuze (SKS)** is de stap (en iteratieve interactie) waarin de student leervraag/leerroute concretiseert naar keuzes op het afgesproken keuzeniveau (zie [0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md)) en waarin differentiatie plaatsvindt tussen typen trajecten (LLO/maatwerk/programma) zoals besproken in de meeting.
3. Implementaties mogen deze stappen in de praktijk combineren in één product of UI, maar in de referentiearchitectuur en interfaces blijven het **afzonderlijke verantwoordelijkheden** met **traceerbare** datastromen.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Keuze onderdeel van inschrijving** | Minder processtappen in één flow | Vermengt bewijsvoering/administratie met keuze-interactie; hogere kans op onduidelijke bron van waarheid en rework bij wijzigende keuzes |
| **B. Keuze vóór inschrijving als harde voorwaarde** | Dwingt vroeg richting/commitment af | Past slecht bij iteratief keuzeproces en intake/plaatsing; kan drempels verhogen in LLO/maatwerk |
| **C. (Gekozen richting)** **Strikte scheiding: inschrijving (ROD/KRS) en keuze (SKS)** | Heldere verantwoordelijkheden; beter te modelleren en te specificeren; ondersteunt iteratieve keuze na inschrijving | Vereist expliciete koppelvlakken/overdracht van minimale context tussen stappen |

### Consequenties

- **Procesontwerp:** het procesmodel moet expliciet laten zien dat na de formele inschrijving een trajectkeuze/uitwerking volgt (incl. vervolgkeuzegate nominale route vs maatwerk zoals in [0012](0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md)).
- **Koppelvlakscope:** specificaties rond studentkeuze hoeven niet “ROD-proof” te zijn; omgekeerd hoeft inschrijving niet alle keuze-interacties te bevatten.
- **Datadeling:** alleen de noodzakelijke “sleutel”/context (student-id/inschrijfcontext) gaat van inschrijving naar studentkeuze; de keuze-inhoud (leerroute/leertraject) blijft primair in de keuze-scope.

### Relaties en links

- **Gerelateerde ADR’s:**
  - [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) — SKS als zelfstandige referentiecomponent
  - [0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) — rollenverdeling SKS/SVS
  - [0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md) — leeractiviteit als keuzeniveau
  - [0012](0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md) — keuzegate nominaal/maatwerk, leerroute vs leertraject
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_verdiepen_student_keuze_criteria_en_plaatsing_20260409/summary.md`
- ArchiMate model: `architecture/model/model.archimate` (splits processtappen en relaties tussen KRS/inschrijving en SKS/studentkeuze expliciet in relevante views)

