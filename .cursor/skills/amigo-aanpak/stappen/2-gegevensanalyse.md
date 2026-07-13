# AMIGO stap 2 — Gegevensanalyse (informatiemodellering)

**Doel:** van proces/scenario naar de bijpassende **gegevens**: welke informatie-objecten bewegen, met welke attributen, semantiek en referenties — richting producerend → consumerend.

**Levert (afsprakenset):** informatiemodel dat de **berichtspecificatie** (stap 5) en daarmee **koppelingen** (gestandaardiseerde informatiestromen) voedt.

**Input:** scenariobeschrijving (stap 1) — inclusief benoemde **informatiestromen** —, kwalificatiedossier, ankertabel (§3.2.6), specificatie-catalogus (§12.5).

**Output:** gefaseerde, geneste onderwijsspecificatie (entiteiten + Nederlandse concept-attributen) in ASCII-boomvorm; keuzedelen als zelfstandig programma; delta-modellering voor leerroute 2–9.

**Uitgewerkt in:** skill [`mbo-informatie-modelleur`](../../mbo-informatie-modelleur/SKILL.md).

**Aandachtspunten:**

- Entiteiten/cardinaliteiten conform ankertabel; OEAPI-mapping (§5).
- Semantiek die niet mag vervagen: `specificatie → aanbod → verbintenis → resultaat`.
- Nieuwe/ontbrekende attributen → signalering (§9), geen OEAPI-kernwijziging.

**Status:** uitgewerkt (eigen skill).
