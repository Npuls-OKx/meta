## Studentkeuzecriteria als queryparameters: SKS vertaalt leervraag naar OC-interpreteerbare queries

Status: Voorstel

Datum: 2026-03-31

### Context

Zonder **afbakening** van queryparameters op de aanbodquery raken studenten en systemen **overweldigd** door schaal van modulair aanbod; tegelijk moet de keten **voldoende structuur** bieden om aanbod te matchen op **leeruitkomsten**, **planning** en **kwalificatie/instroom** (transcript 31 maart 2026).

In hetzelfde overleg zijn **trechters** expliciet benoemd, o.a.: **geografische** reikwijdte (bijv. regio), **bekostiging/budget**, **tijd en planningshorizon** (beschikbaarheid, doorlooptijd), **kwalificatie/instroomeisen** en **uitstroomniveau** / type leeruitkomsten. Optioneel kwam **contenttype** (bijv. fysiek vs. digitale vorm) aan bod. Deze criteria vormen de **brug** tussen de in [0006](0006-studentorientatie-trechter-ketenfase.md) beschreven **oriëntatie** en de **onderwijscatalogus** als bron.

**Randvoorwaarde:** uniforme **leeruitkomstdefinities** over instellingen heen blijft een **kritische** factor voor automatisering (samenvatting meeting); dit ADR gaat uit van voortschrijdende **standaardisatie** en verwijst naar [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) voor **studielast** als logistieke maat.

### Beslissing (concept)

1. OKx-specificaties en het informatiemodel **moeten** de genoemde **categorieën keuzecriteria** kunnen dragen als **gestructureerde parameters** op de **aanbodquery** (niet alleen vrije tekst), met **minimumset** die in MVP’s afsprakelijk wordt.
2. **Trechters** zijn **componerbaar**: meerdere queryparameters tegelijk (bijv. geo **en** horizon **en** instroom) — exacte cardinaliteit en defaults in technische uitwerking van koppelvlakken.
3. **Mapping naar onderwijsbeschrijving:** criteria worden **traceerbaar** gemaakt naar wat in **catalogusmetadata** en **leeruitkomst-uitwerking** beschikbaar moet zijn ([0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md)).
4. **Rol van SKS:** het **Student Keuze Systeem (SKS)** is de primaire ketenbouwsteen die de (vaak vage) **leervraag** uit studentoriëntatie **vertaalt** naar **OC-interpreteerbare queryparameters** op de aanbodquery. Het SKS orkestreert daarmee de trechter(s) richting de onderwijscatalogus, zonder de onderwijscatalogus zelf te belasten met keuze-interactie of niet-gestandaardiseerde leervraaginterpretatie (zie ook [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) en [0006](0006-studentorientatie-trechter-ketenfase.md)).

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Alleen full-text zoeken in catalogus** | Eenvoudig te bouwen | **Geen** betrouwbare logistiek/planning; geen instroomborging |
| **B. Vaste vaste menu’s per instelling zonder sectorale afspraak** | Snel lokaal | **Geen uitwisselbaarheid** tussen ketenpartijen |
| **C. (Gekozen richting)** **Gestandaardiseerde trechterparameters als queryparameters op koppelvlakken** + koppeling catalogus | Ondersteunt [0006](0006-studentorientatie-trechter-ketenfase.md) en sectoraggregatie (o.a. Edibroker-discussie in meeting) | **Datakwaliteit** en **ontbrekende metadata** bij aanbod blijven risico |

### Consequenties

- **Catalogusbeheerders** moeten **metadata** leveren die de queryparameters op koppelvlakken ondersteunen; **OKx** beschrijft de **minimumset** queryparameters in koppelvlakspecificaties.
- **Stakeholders:** werkgevers-/UWV-koppeling (in meeting genoemd) blijft **optioneel** en **buiten scope** van dit ADR behalve waar het leeruitkomsten-sets raakt.

### Impact op `architecture/model/model.archimate`

- **Data-objecten / informatie-elementen** voor **queryparameters**, **aanbodquery**, en relatie met **aanbod** / **curriculum-onderdeel** / **leeruitkomst** (namen volgens jullie modelleerconventie).
- **Services/API’s** in applicatielaag waar **SKS** / catalogus-query’s spelen: relaties expliciet maken ([0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md)).

### Relaties en links

- **Gerelateerde ADR’s:** [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md), [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md), [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md), [0006](0006-studentorientatie-trechter-ketenfase.md), [0008](0008-scope-planning-eerst-intra-instelling.md)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria_20260331/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: [`doc/OKx_Projectoverzicht.md`](../../doc/OKx_Projectoverzicht.md)

### Vervangt (optioneel)

- —
