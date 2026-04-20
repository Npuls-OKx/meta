## Enterprise messaging patronen voor betrouwbare koppelvlakken (delivery, idempotentie, dead-letter, ordering)

Status: Voorstel

Datum: 2026-04-20

### Context

In het kernteamoverleg is expliciet besproken dat OKx-koppelvlakken niet alleen semantisch moeten kloppen, maar ook robuust moeten zijn in het geval van fouten, retries en asynchrone verwerking. Daarin zijn concrete **Enterprise Application Patterns** genoemd:

- **Guaranteed delivery**: berichten blijven persistent tot aflevering is bevestigd.
- **Dead Letter Channel**: mislukte berichten worden apart afgehandeld zonder het hoofdproces te blokkeren.
- **Idempotent receiver**: ontvangers kunnen dubbele berichten veilig verwerken.
- **Ordering (FIFO)**: strikte berichtvolgorde om synchronisatiefouten te voorkomen.

In [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) worden “enterprise messaging‑patronen” al benoemd als randvoorwaarde, maar er is nog geen afzonderlijk besluit vastgelegd dat deze patronen als **ketenbrede niet-functionele eis** positioneert met alternatieven, consequenties en impact op `architecture/model/model.archimate`.

Bron: `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md`.

### Beslissing

We leggen vast dat OKx-koppelvlakken (events en/of API-interacties waar asynchronie, retries of distributie optreedt) moeten voldoen aan een minimumset van enterprise messaging-eisen:

1. **Betrouwbare aflevering (guaranteed delivery)** voor ketenkritische berichten: verzending en ontvangst worden zodanig ingericht dat berichten niet “stil” verloren gaan.
2. **Idempotente verwerking** aan ontvangende kant: consumers moeten duplicates kunnen herkennen en veilig kunnen negeren/herhalen.
3. **Dead Letter afhandeling**: foutgevallen worden geïsoleerd met traceerbaarheid, zodat operationele issues het ketenproces niet onzichtbaar corrumperen.
4. **Berichtvolgorde (ordering/FIFO)** waar procesvolgorde semantisch relevant is (bijv. statusovergangen, mutaties op dezelfde entiteit/route/plaatsing).

Deze beslissing is technologie-agnostisch (broker, queue, eventbus, API met outbox, etc.), maar **niet** vrijblijvend: leveranciers/instellingen moeten in hun implementatie aantoonbaar aan deze eigenschappen voldoen voor de relevante stromen.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Best-effort berichtenverkeer** (geen delivery/ordering garanties) | Snel te implementeren | Onbetrouwbaar; fouten worden pas laat zichtbaar; hoge herstelkosten; niet geschikt voor ketenkritische processen |
| **B. Per koppelvlak ad hoc keuzes** (geen uniforme NFR’s) | Flexibel per leverancier | Fragmentatie; moeilijk te testen/interopereren; inconsistent gedrag in keten |
| **C. Alleen synchrone API’s, geen messaging-patronen** | Eenduidig request/response | Past niet bij processen met retries/asynchronie; verhoogt coupling; slechter schaalbaar |
| **D. (Gekozen richting)** **Uniforme messaging‑patronen als ketenbrede NFR** | Voorspelbaar gedrag; betere interoperabiliteit; sluit aan bij meeting en [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) | Vereist expliciete implementatierichtlijnen en testbare criteria per stroom |

### Consequenties

- **Specificaties:** koppelvlakspecificaties moeten per stroom expliciet benoemen of ordering vereist is en welke idempotency-key/entiteitssleutel geldt.
- **Operationeel:** implementaties hebben monitoring/traceerbaarheid nodig (o.a. DLQ management) om ketenissues te kunnen diagnosticeren.
- **Samenhang met proces:** deze eisen zijn vooral kritisch bij stromen die keuze, plaatsing, planning en voortgang raken (waarbij foutafhandeling anders direct inconsistenties introduceert).

### Relaties en links

- **Gerelateerde ADR’s:**
  - [0001](0001-publieke-repo-en-samenwerkingsmodel.md) — governance/traceerbaarheid via issues/PR’s (relevant voor wijziging van NFR’s)
  - [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) — messaging-patronen genoemd als randvoorwaarde
  - [0015](0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md) — RFO-stroom vereist robuuste foutafhandeling/ordering in iteratief proces
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md`
- ArchiMate model: `architecture/model/model.archimate` (leg messaging‑capabilities/NFR’s vast bij relevante interfaces/stromen; modelleer waar DLQ/monitoring conceptueel hoort in de technology/integration laag)

