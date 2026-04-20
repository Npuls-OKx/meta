## Studentoriëntatie als expliciete ketenfase met trechter naar leeruitkomsten

Status: Voorstel

Datum: 2026-03-31

### Context

[0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) benadrukt **student kiest** en **leeruitkomsten** als sleutel. Zonder een **bewuste stap vóór** brede query op onderwijsaanbod lopen student en keten vast op **onbeheersbare** catalogusresultaten (o.a. “tienduizenden modules”) en op **vage leervragen** die niet matchbaar zijn met gestandaardiseerd aanbod.

In het kernteamoverleg **kaderstelling studentkeuze en criteria** (31 maart 2026) is de **studentoriëntatie** benoemd als fase waarin de student (in beginsel met **anonieme context**) een **leervraag articuleert** en die **vertaalt** naar **leeruitkomsten** en parameters die het onderwijs kan verwerken — niet door de student **vrij te laten definiëren** in eigen taal zonder vertaling, maar door te **destilleren** naar termen die in sector en catalogus voorkomen. De oriëntatiestap moet een **trechterfunctie** op de aanbodquery geven: de vertaalde leervraag resulteert in **queryparameters** die op de koppelvlakken naar de onderwijscatalogus worden meegegeven (samenvatting en transcript).

**Samenhang:** [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) positioneert het **SKS**; deze ADR beschrijft het **procespatroon** (oriëntatie → keuze → inschrijving/planning) dat in het model en in koppelvlakken **herkenbaar** moet zijn.

### Beslissing (concept)

1. **Studentoriëntatie** wordt in OKx als **expliciete ketenfase** vastgehouden: vóór inschrijving en vóór brede **aanbodquery** op de onderwijscatalogus wordt de **leervraag** vertaald naar **gestandaardiseerde leeruitkomsten** en **randvoorwaarden** (o.a. geografische reikwijdte, tijd/planningshorizon, beschikbaarheid, instroom/kwalificatie). Deze vertaling levert **queryparameters** op die als trechter fungeren op de koppelvlakken naar de catalogus ([0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)).
2. De student laat **geen eigen ad-hoc leeruitkomsten** als enige bron gelden: het systeem/keten helpt met **mapping** naar het **gedeelde begrippenkader** van instellingen (aansluiting bij [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) voor omvang/SBU/EC waar van toepassing).
3. **Privacy-scheiding:** in de oriëntatiefase kan **anonieme studentcontext** worden gehanteerd; koppeling aan persoon volgt in latere stappen (wallet/intake/SKS) — detailuitwerking in specs, niet in dit ADR.

### Alternatieven


| Optie                                                                                           | Voordeel                                     | Nadeel / risico                                                                                                                                          |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A. Geen aparte oriëntatiefase** — direct globale catalogusquery                               | Minder stappen in UI                         | **Overload** en **geen** vertaling vage vraag → standaard                                                                                                |
| **B. Alleen marketing/UX** zonder ketenmodel                                                    | Snel te communiceren                         | **Geen** afdwingbare **interoperabiliteit** tussen instellingen                                                                                          |
| **C. (Gekozen richting)** Oriëntatie als **gemodelleerde fase** met trechter (queryparameters) naar LO + criteria | Sluit aan bij Npuls/OKx-doelen en transcript | **Afstemming** met **sectorstandaard** leeruitkomsten blijft **randvoorwaarde** (zie ook [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md)) |


### Consequenties

- **Stakeholders:** **Instellingen** moeten **articulatie** en **queryparameters** op de koppelvlakken (zie [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)) op elkaar afstemmen; **leveranciers** krijgen duidelijke **grenzen** tussen oriëntatie-, keuze- en inschrijfstromen.
- **Werk:** BPMN/procesdiagrammen en MOKA-views moeten de fase **naamgeving en volgorde** consistent houden met deze ADR.

### Impact op `architecture/model/model.archimate`

- **Processen / samenwerkingspunten:** Een expliciet **proces** of **fase** voor **studentoriëntatie** (of equivalent in jullie ArchiMate-conventie) met uitgaande relaties naar **aanbodquery** (incl. queryparameters) en **leeruitkomsten**.
- **Informatie:** Objecten voor **leervraag**, **gemapte leeruitkomsten**, **queryparameters** (als output van de oriëntatie), **oriëntatiecontext** (anoniem/pseudoniem) waar passend.
- **Views:** MOKA-koppelvlakspecificatie-views en ketenviews worden bijgewerkt in **samenspraak** (zie [0010](0010-archimate-moka-informatiemodel-werkafspraken.md)).

### Relaties en links

- **Gerelateerde ADR’s:** [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md), [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md), [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md), [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md), [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria_20260331/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)`

### Vervangt (optioneel)

- —

