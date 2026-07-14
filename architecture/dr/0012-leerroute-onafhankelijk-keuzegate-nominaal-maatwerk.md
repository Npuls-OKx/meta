## Leerroute als instellingsonafhankelijke entiteit; keuzegate nominaal vs. maatwerk

Status: Voorstel

Datum: 2026-04-13

### Context

[0006](0006-studentorientatie-trechter-ketenfase.md) beschrijft de **oriëntatiefase** en [0008](0008-scope-planning-eerst-intra-instelling.md) benadrukt dat **intra-instelling** eerst wordt uitgewerkt. In het kernteamoverleg **inhoud uitwerken StudentKiest** (13 april 2026) zijn drie samenhangende besluiten genomen over de verhouding tussen de **globale leerroute** (cross-instelling), het **gedetailleerde leertraject** (binnen instelling) en de **keuzegate** waar de student kiest tussen nominaal en maatwerk.

**Leerroute als losse entiteit:** Mark Hoogenboom bracht in dat een student een **globaal uitgewerkte leerroute** moet kunnen hebben — mogelijk voor de rest van zijn leven — waarmee hij bij **meerdere scholen** kan rondkijken. De leerroute is daarmee een **entiteit die vóór inschrijving** bij een specifieke instelling bestaat. Het team stemde in: het procesmodel ondersteunt **meerdere parallelle trajecten** bij verschillende instellingen, elk gevoed vanuit dezelfde leerroute.

**Leertraject binnen instelling:** het **gedetailleerde leertraject** — welke dag, welke locatie, welke logistiek — wordt pas **binnen de instelling** uitgewerkt. De instelling kan pas op dat detailniveau plannen als de student "door de poort" is.

**Keuzegate:** bij de instelling volgt een **keuzegate**: neemt de student deel aan een **nominale** (voorontworpen) route, of wordt een **maatwerk**-leertraject samengesteld? Dit is primair een **systeem/proceskeuze**, geen onomkeerbare beslissing. Niels vergeleek het met een lego-plaat: nominaal krijg je een voorgeladen bouwplaat; maatwerk krijg je een lege plaat. Maar op **elk moment** kan de student switchen — "continuous change of state". Zelfs bij een nominale route kun je later verbreden, verdiepen of cherry-picken.

### Beslissing (concept)

1. **Leerroute als onafhankelijke entiteit:** de leerroute wordt in het informatiemodel en de procesarchitectuur behandeld als een **entiteit die onafhankelijk van een specifieke instelling kan bestaan**. Een student kan een leerroute opstellen en daarmee bij **één of meerdere instellingen** uitkomen. De leerroute bevat **globale leeruitkomsten**, **tijdshorizon** en **randvoorwaarden**, maar niet de logistieke details.
2. **Leertraject binnen instelling:** het **leertraject** (gedetailleerde planning, roostering, toewijzing van leeractiviteiten aan periodes en locaties) wordt pas uitgewerkt **na** inschrijving bij een instelling. Eén leerroute kan leiden tot **meerdere parallelle leertrajecten** bij verschillende instellingen.
3. **Keuzegate nominaal/maatwerk:** na intake bij een instelling volgt een **keuzegate**: nominale leerroute (voorgeladen curriculum met differentiatiemogelijkheden) of volledig maatwerk (zelf leeractiviteiten samenstellen). Deze keuze is **niet onomkeerbaar** — het systeem moet ondersteunen dat een student op elk moment kan overschakelen (continuous change of state).
4. **Onderscheid terminologie:** "leerroute" = globaal, cross-instelling; "leertraject" = gedetailleerd, binnen instelling. Deze termen worden in specs en model **consistent** gehanteerd.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Leerroute alleen na inschrijving** | Eenvoudiger procesmodel | Student kan niet **shoppen** over instellingen; cross-instelling onmogelijk |
| **B. Keuzegate als definitieve keuze** (nominaal OF maatwerk, niet meer switchen) | Minder complexiteit in systeem | **Strijdig** met flexibiliseringsgedachte; student zit vast |
| **C. Geen onderscheid leerroute/leertraject** | Eenvoudigere terminologie | **Verwarring** over wat cross-instelling kan en wat instelling-specifiek is |
| **D. (Gekozen richting)** **Leerroute onafhankelijk + keuzegate reversibel + leertraject binnen instelling** | Maximale flexibiliteit voor student; consistent met LLO-visie | **Complexer** informatiemodel; **afstemming** nodig over hoe leerroutes federatief worden gedeeld |

### Consequenties

- **Informatiemodel:** twee **onderscheiden entiteiten**: leerroute (globaal) en leertraject (instelling-specifiek), met een **1:N relatie** (één leerroute → meerdere leertrajecten).
- **Ontwikkelingswallet:** de leerroute sluit aan op de **wallet** als centrale plek waar leeruitkomsten en credentials worden bijgehouden ([0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md)).
- **SKS:** het SKS moet zowel de **globale leerroute-samenstelling** als de **keuzegate** binnen een instelling ondersteunen.
- **Stakeholders MBO niveau 1-3:** voor jonge studenten is de leerroute vaak impliciet (ouders/begeleider bepalen mee); het systeem moet **advisering** ondersteunen (benoemd door Mark in het overleg).

### Impact op `architecture/model/model.archimate`

- **Entiteiten:** **leerroute** en **leertraject** als onderscheiden informatie-objecten met expliciete relatie.
- **Processen:** de **keuzegate nominaal/maatwerk** als herkenbaar beslismoment in het StudentKiest-proces; de **reversibiliteit** (continuous change of state) moet in het procesmodel zichtbaar zijn (bijv. als terugkeerpad).
- **Views:** cross-instelling scenario's tonen de leerroute als entiteit die **buiten** individuele instellingscontext leeft; intra-instelling views tonen het leertraject.

### Relaties en links

- **Gerelateerde ADR's:** [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) (SKS als component), [0006](0006-studentorientatie-trechter-ketenfase.md) (oriëntatiefase), [0008](0008-scope-planning-eerst-intra-instelling.md) (intra-instelling eerst), [0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md) (keuzeniveau leeractiviteit)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/20260413_okx_kernteam_inhoud_uitwerken_studentkiest/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`

### Vervangt (optioneel)

- — *(verfijnt [0008](0008-scope-planning-eerst-intra-instelling.md) op het punt van leerroute vs. leertraject, vervangt niet)*
