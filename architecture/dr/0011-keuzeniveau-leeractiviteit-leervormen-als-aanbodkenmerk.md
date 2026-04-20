## Student kiest op leeractiviteitniveau; leervormen als aanbodkenmerk

Status: Voorstel

Datum: 2026-04-13

### Context

[0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) benoemt **leeruitkomsten** als sleutel en [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) beschrijft **trechterparameters** (ofwel queryparameters op de aanbodquery) waarmee een student aanbod filtert. Onduidelijk was echter op **welk granulariteitsniveau** de student concreet kiest binnen een instelling — en of **leervormen** (WPV, fysiek op school, online) een **apart keuzemoment** in het proces vormen of simpelweg **kenmerken** van het aanbod zijn.

In het kernteamoverleg **inhoud uitwerken StudentKiest** (13 april 2026) is door Niek, Niels, Mark en Alda geconcludeerd dat de **leeractiviteit** het juiste keuzeniveau is. Een leeractiviteit is een **collectie van leeropdrachten** met bijbehorende **lesuitkomsten** — grof genoeg voor een studentkeuze, fijn genoeg om personalisatie mogelijk te maken. Diepere niveaus (individuele leeropdrachten, lesvorm per les) zijn **te fijnmazig** voor de voorkant en vallen in het LMS-domein.

Tegelijkertijd is vastgesteld dat **leervormen geen apart keuzemoment** zijn in het proces, maar **kenmerken van het aanbod** in de onderwijscatalogus. De student kiest uit het beschikbare aanbod; als dat aanbod verschillende leervormen kent, zijn die zichtbaar als **queryparameters op de aanbodquery** (trechterparameters conform [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)), niet als een afzonderlijke processtap.

### Beslissing (concept)

1. **Keuzeniveau:** de student kiest in het StudentKiest-proces op het niveau van de **leeractiviteit** — een collectie van leeropdrachten en bijbehorende lesuitkomsten. Dit is het laagste niveau waarop het SKS keuze-articulatie ondersteunt; fijnere granulariteit (individuele lesopdrachten, differentiatie binnen leeractiviteiten) valt onder **LMS/uitvoeringsdomein**.
2. **Leervormen als kenmerk:** leervormen (WPV, fysiek, online, etc.) worden in de **onderwijscatalogus** opgenomen als **metadata van het aanbod**, niet als apart keuzemoment in het StudentKiest-proces. De student filtert op leervormen als **queryparameter op de koppelvlakken** naar de onderwijscatalogus, net als op andere trechterparameters ([0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)).
3. **Informatiemodel:** de hiërarchie programma → leertaak (per opleidingsonderdeel) → leeractiviteit (collectie leeropdrachten + lesuitkomsten) → lesopdracht wordt in het informatiemodel **herkenbaar** gemaakt, zodat het keuzeniveau **traceerbaar** is naar de catalogusstructuur en de onderwijskundige eenheden.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Student kiest op leertaakniveau** (per opleidingsonderdeel) | Eenvoudiger UI, minder keuzes | **Te grof** voor personalisatie; student kan niet differentiëren binnen een opleidingsonderdeel |
| **B. Student kiest op lesopdrachtniveau** | Maximale flexibiliteit | **Te fijnmazig**: onbeheerbaar voor student (zeker MBO niveau 1-3), te complex voor catalogus en planning |
| **C. Leervormen als apart keuzemoment** in het proces | Expliciete processtap voor leervormkeuze | **Functionele overlap** met leervorm als queryparameter op de aanbodquery ([0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)): de student filtert het catalogusaanbod al op leervorm via trechterparameters (potentiële queryparameters op koppelvlakken), waarna een apart keuzemoment in het proces dezelfde keuze **nogmaals** afdwingt. Daarnaast is het **overbodig** wanneer het geselecteerde aanbod de leervorm al determineert (bijv. een leeractiviteit die uitsluitend als WPV wordt aangeboden heeft geen tweede keuzemoment nodig). |
| **D. (Gekozen richting)** **Leeractiviteit als keuzeniveau + leervormen als aanbodkenmerk** | Balans granulariteit/beheersbaarheid; consistent met informatiemodel | **Afstemming** nodig met instellingen over hoe leeractiviteiten worden samengesteld en gepubliceerd |

### Consequenties

- **Catalogusbeheerders** moeten aanbod publiceren op leeractiviteitniveau met leervorm als metadata-attribuut.
- **SKS-specificaties** beschrijven keuze-interactie op leeractiviteitniveau; **LMS-koppelvlakken** nemen het over voor fijnere differentiatie.
- **Stakeholders MBO niveau 1-3:** bij nominale routes is de leeractiviteitkeuze vaak al ingevuld; het systeem moet dit transparant maken zonder de student te overweldigen.

### Impact op `architecture/model/model.archimate`

- **Informatie-elementen:** de hiërarchie programma → leertaak → leeractiviteit → lesopdracht moet in het informatiemodel **expliciet** zijn, met leeractiviteit als het **keuzeniveau** gemarkeerd.
- **Data-objecten:** leervorm als **attribuut** van aanbod/leeractiviteit in catalogusstructuur, niet als aparte entiteit in het keuzeproces.
- **Views:** MOKA-koppelvlakspecificatie-views en StudentKiest-procesviews moeten **leeractiviteit** als keuzegranulariteit tonen.

### Relaties en links

- **Gerelateerde ADR's:** [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (leeruitkomsten als sleutel), [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) (SBU/EC als logistieke maat), [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) (SKS als component), [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) (trechterparameters), [0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) (SKS/SVS-verdeling)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_20260413/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`

### Vervangt (optioneel)

- —
