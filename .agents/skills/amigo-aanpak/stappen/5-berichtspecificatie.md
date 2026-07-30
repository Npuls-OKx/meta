# AMIGO stap 5 — Berichtspecificatie

**Doel:** vastleggen **welke gegevens** worden uitgewisseld — structuur, constraints, syntax — plus de te hanteren **vocabulaire/waardenlijsten**.

**Levert (afsprakenset):** berichtspecificatie + vocabulairespecificatie/-selectie; maakt een **koppeling** (gestandaardiseerde informatiestroom) berichtbaar.

**Input:** informatiemodel (stap 2), interactie-analyse (stap 3), technologiekeuze (stap 4).

**Output:** concrete berichtdefinities per koppeling (bv. OEAPI/OOAPI-profiel: `Programme`, `Course`, `LearningComponent`, `TestComponent`, `Association`) met OKx-extensies en waardenlijsten. Endpoints (= koppelvlak) volgen in stap 6.

**Uitgewerkt in:** bouwt direct voort op de skill [`mbo-informatie-modelleur`](../../mbo-informatie-modelleur/SKILL.md) (stap 2). De Nederlandse concept-attributen mappen via de woordenlijst naar §12.5 (OEAPI-nabije namen) en vandaar naar het OEAPI-profiel.

**Aandachtspunten:**

- Concept-attributen (NL) → §12.5 (EN) → OEAPI-payload: houd de mapping traceerbaar.
- OEAPI-kern niet ter plekke oplossen; gaps → signalering (§9) / change request.
- Zie profiel §6 (naamgeving/extensies) en §12.2/§12.5.

**Status:** kader (TO-DO) — leunt op stap 2, uit te werken tot volwaardige berichtspecificatie.
