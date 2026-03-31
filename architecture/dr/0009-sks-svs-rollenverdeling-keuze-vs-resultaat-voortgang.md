## Rollenverdeling SKS en SVS: keuze-interactie versus resultaatstructuren en LMS-voortgang

Status: Voorstel

Datum: 2026-03-31

### Context

[0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) benoemt het **Student Keuze Systeem (SKS)** als **eigen referentiecomponent** en de bewuste relatie met **SVS**. In het overleg **kaderstelling studentkeuze en criteria** (31 maart 2026) is een **nadere functionele splitsing** besproken (o.a. Niels en Niek): **SKS** richting **alle student-keuze-interacties**; **SVS** gebruikt de **catalogus** vooral om te bepalen **welke resultaatstructuren** nodig zijn en haalt **resultaten en voortgang** uit het **LMS** — terwijl overige “student kiest”-interacties **niet** in het SVS hoeven te landen.

Dit ADR **verfijnt** de architectuurgrens **zonder** [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) te vervangen: het vult **gedrag** en **datastromen** aan waar het kernteam technische **corruptie van verantwoordelijkheden** wil vermijden (keuze-flexibiliteit versus volg-/resultaatlogica).

### Beslissing (concept)

1. **SKS** is het **primaire** component voor **keuzemomenten** en **articulatie** van de leervraag richting **aanbod** (inclusief iteratieve keuze na inschrijving waar het proces dat vraagt — zoals in de samenvatting: recursief aanbod ophalen).
2. **SVS** focust op **volgsysteemkern**: o.a. **resultaatstructuren** afgeleid van/catalogus-koppeling en **voortgang/resultaat** uit **LMS**; **niet** alle niet-keuze functionaliteit hoeft in SVS te zitten, maar **wel** duidelijke **grenzen** in koppelvlakbeschrijvingen.
3. **Overlap vermijden:** waar leveranciers één product voor beide gebruiken, blijven **externe interfaces** (API/bericht) **scheiden** volgens deze rollen — implementatie mag gecombineerd zijn, **referentiecomponenten** niet door elkaar halen in specificaties.

### Alternatieven


| Optie                                                                   | Voordeel                          | Nadeel / risico                                                         |
| ----------------------------------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------- |
| **A. SVS als alles-voor-student** inclusief alle keuze-UI               | Eén systeem bij kleine instelling | **Wrijving** met flexibele keuze en keten naar catalogus/SKS            |
| **B. Geen onderscheid in specs**                                        | Minder tekst                      | **Integratiefouten** en dubbele bron van waarheid                       |
| **C. (Gekozen richting)** **Heldere rollen** SKS vs SVS zoals hierboven | Sluit aan op discussie 31 maart   | **Afstemming** met bestaande installaties; migratiepaden per instelling |


### Consequenties

- **Specificaties** voor stromen **catalogus–SVS**, **SKS–SVS**, **SVS–LMS** worden **reviewed** op consistentie met deze verdeling.
- **Stakeholders:** leveranciers van SVS en SKS krijgen **duidelijker** welke **events** en **data** waar thuishoren.

### Impact op `architecture/model/model.archimate`

- **Applicatie-/serviceschets:** relaties **SKS** ↔ **Onderwijscatalogus**, **SKS** ↔ **SVS**, **SVS** ↔ **LMS** expliciet; **geen** impliciete “alles gaat via SVS” zonder relatie-label.
- **Herziening bestaande views** waar SKS en SVS nog **samengevallen** zijn — via PR met verwijzing naar dit ADR.

### Relaties en links

- **Gerelateerde ADR’s:** [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) (SKS als component); projectoverzicht voor **SVS**-stromen: `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)`
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria_20260331/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Informatiesstromen.md](../../doc/OKx_Informatiesstromen.md)`

### Vervangt (optioneel)

- — *(verfijnt [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md), vervangt niet)*

