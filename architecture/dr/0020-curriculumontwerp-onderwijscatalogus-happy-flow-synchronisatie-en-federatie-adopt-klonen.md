## Curriculumontwerp en onderwijscatalogus: happy flow, synchronisatie (UUID, pub/sub) en federatie (adopteren vs klonen)

Status: Voorstel

Datum: 2026-05-01

### Context

In **NDE/NVD — informatiestromen en hoofdplaat** (1 mei 2026) is de **happy flow** tussen **Curriculumontwerptool (CO)** en **Onderwijscatalogus (OC)** doorgesproken, naast eerdere lijnen uit **OKx NDE/NVD — SKS, examens en resultaatstructuren** (28 april 2026) over **request-for-offering** en planning.

Kern uit het transcript:

- **Hergebruik:** CO bevraagt OC op basis van **leeruitkomsten** op welke **bestaande onderwijsspecificaties** (education specifications) beschikbaar zijn; antwoord o.a. als **set UUID’s**; CO wil niet “blind” alles fijnmazig binnenhalen maar wel **referentie + voldoende metadata** (titels, studielast, menselijk herkenbare info) om te kiezen.
- **Geen vrij posten van eigen LO’s door docenten in deze flow:** nieuwe of ontbrekende uitwerking gaat via **Request for (detailed) specification** binnen OC; **fijnmazige uitwerking en validatie** (sommen, consistentie) is **interne logica van OC**, niet van CO.
- **Publicatie:** **OC beslist** of iets publiceerbaar is (geen halffabrikaten, tenzij beleid dat toestaat); CO hoeft niet de “publicatiemanager” te zijn, maar heeft wél **statusfeedback** nodig (o.a. na publicatie / na uitwerking).
- **Synchronisatie bij wijzigingen:** voor **mutaties** op specificaties in OC is **point-to-point pull “on demand” onvoldoende**; gewenst patroon is **pub/sub** (publisher → **topic** op een **message bus** / servicebus → subscribers), zodat CO en andere deelnemers **events** krijgen wanneer relevante **UUID’s** in hun programma’s wijzigen. Cross-instelling via broker wordt genoemd als verlengstuk.
- **Federatie extern aanbod:** twee scenario’s: **adopteren** (eigen lifecycle volgt bron/release) versus **klonen** (eigen lifecycle, meer controle) — klonen opent het risico op **datawildgroei** en vergt **ID-mapping** (“schaduwboekhouding”) voor o.a. EduBroker-achtige federatie.

Daarnaast: om **attribuutniveau** en OEAPI-consequentie te borgen, wordt in hetzelfde overleg overwogen de **volledige OEAPI-specificatie** in de ontwikkelcontext (repo/skill/context) beschikbaar te hebben — dat is een **werkwijze/tooling-besluit**, geen ketenstandaard op zich.

### Beslissing (concept)

1. **Ontwerp–catalogus happy flow:** CO → OC: query op **leeruitkomsten** (niet primair op kwalificatiedossier-sleutel als proxy) → OC retourneert **herbruikbare specificaties** o.a. via **UUID’s** en **kopmetadata** → voor ontbrekende stukken: **aanmaken + Request for detailed specification** in OC → na interne uitwerking: **callback/status** richting CO; **publicatie** is **uitsluitend** volgens **OC-regels**.
2. **Wijzigingssync:** voor **updates** op education specifications (en vergelijkbare OC-kernobjecten) wordt het **doelarchitectuurpatroon** **event-gedreven synchronisatie** (pub/sub op bus), niet uitsluitend pull, met expliciete aansluiting op ketenbrede messaging-eisen ([0018](0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md)).
3. **Federatie:** specificaties **adopteren** of **klonen** zijn beide toegestane **modellen**; de gekozen modus moet **traceerbaar** zijn (bron-ID, lokale ID, versie/release-afhankelijkheid). **Klonen** wordt gekoppeld aan **governance** (wildgroei, reconciliatie).
4. **Aansluiting planning:** na publicatie sluit de keten aan op **Request for Offering** / haalbaarheid richting planning ([0015](0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md)) — buiten de scope van deze happy flow, maar **volgorde** is: specificatie gereed → publicatie OC → **dan** RFO-achtige stappen.

### Alternatieven


| Optie                                                                                                                     | Voordeel                                              | Nadeel / risico                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **A. Alleen REST pull door CO**                                                                                           | Eenvoudig                                             | Missed updates; race conditions; onduidelijke integriteit bij langlopende curriculumprojecten                               |
| **B. CO beheert publicatierechten**                                                                                       | Minder stappen in diagram                             | Wrijving met catalogus als bron van waarheid; inconsistente “halffabrikaat”-publicatie                                      |
| **C. Geen expliciet adopt/clone-model**                                                                                   | Minder documentatie                                   | Onduidelijkheid bij federatief hergebruik en lifecycle                                                                      |
| **D. (Gekozen richting)** **UUID-gedreven happy flow + OC-eigenaarschap + pub/sub voor mutaties + adopt/clone expliciet** | Sluit aan bij besproken integriteit en schaalbaarheid | Vereist bus/topics, idempotentie, monitoring ([0018](0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md)) |


### Consequenties

- **Koppelvlakspecificaties** moeten endpoints/events onderscheiden voor **create**, **uitwerken**, **publiceren** en **wijzigen**, met duidelijke **idempotency**- en **ordering**-overwegingen waar van toepassing.
- **Leveranciers** van CO en OC krijgen een referentieproces voor **POC’s** (happy flow eerst intra-instelling, zie [0008](0008-scope-planning-eerst-intra-instelling.md)).
- **OEAPI:** mapping van de flow naar bestaande OEAPI-concepten blijft verplicht uitgangspunt ([0017](0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md) en `[architecture/docs/principes.md](../docs/principes.md)`); tooling om de volledige spec te laden is een **implementatiehulp** voor auteurs.

### Overlap en relatie met bestaande ADR’s (expliciet)

- **[0018](0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md)** — **0020** is een **toepassing** van die patronen op **CO↔OC synchronisatie**; geen conflict: **0020** maakt het domeinspecifiek.
- **[0015](0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md)** — **0020** behandelt het **ontwerp–catalogus**-gedeelte **vóór** RFO; samen de keten **ontwerp → publicatie → haalbaarheid**.
- **[0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)** — zelfde idee “**catalogus bevragen op gestructureerde criteria**”, maar met actor **SKS** en focus **studentaanbod**; **0020** betreft **CO** en **curriculumhergebruik** — pattern overlap, ander **bounded context**.
- **[0017](0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md)** — hergebruik van blokken en aggregatie; **0020** beschrijft het **interactiepatroon** tussen tools.
- **[0008](0008-scope-planning-eerst-intra-instelling.md)** — pub/sub intra-ecosysteem sluit aan bij gefaseerde scope; federatie-adopt/clone is **complexer** en vraagt broker/ID-afspraken.
- **[0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md)** / meeting 28 april — resultaatstructuren en exameninstrumenten blijven **SVS/SKS-kant**; **0020** voedt de **catalogus-specificaties** waar die keten op leunt.
- **[0019](0019-conceptuele-gelaagdheid-kwalificatie-specificatie-aanbod-rosa-kooi.md)** — de objecten die CO en OC uitwisselen moeten de **specificatie- vs aanbodlaag** respecteren.

### Relaties en links

- Meetings:
  - `architecture/meetings/20260501_nde_nvd_informatie_stromen_hoofdplaat/summary.md`
  - `architecture/meetings/20260501_nde_nvd_informatie_stromen_hoofdplaat/transcript.md`
  - `architecture/meetings/20260428_okx_nde_nvd_sks_examens_resultaat_structuren/summary.md` (keten richting RFO/planning, modulaire examenopbouw)
- ArchiMate model: `architecture/model/model.archimate` — **impact (conceptueel, geen modelwijziging in deze PR):** uitbreiden/verscherpen van **interacties** tussen **Curriculumontwerp** en **Onderwijscatalogus** (sequenties, data-objecten voor UUID-sets, status terug naar CO); toevoegen of labelen van **integration/messaging** (topic/subscription) voor **specification update events**; **federatie**-relaties (broker) voor adopt/clone met traceerbaarheid. Raadpleeg [0010](0010-archimate-moka-informatiemodel-werkafspraken.md).
- OKx docs: `[doc/Projectoverzicht.md](../../doc/Projectoverzicht.md)`, `[doc/Informatiesstromen.md](../../doc/Informatiesstromen.md)`

### Vervangt (optioneel)

- —

