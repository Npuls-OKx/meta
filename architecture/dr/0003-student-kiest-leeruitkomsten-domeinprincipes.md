## Domeinprincipes: student kiest, leeruitkomsten en onderwijskundige laag

Status: Voorstel

Datum: 2026-03-25

### Context

Flexibilisering en **“student kiest”** vereisen dat **onderwijskundige** en **logistieke** informatie **samen** worden ontworpen: alleen “stromen tussen systemen” volstaat niet voor **keuze-articulatie**, **LLO**, en **examen-/resultaatketens**. In het kernteamoverleg (maart 2026) wordt dit onder meer gekoppeld aan een **Student Ontwikkelingswallet (EDU-wallet)** (eigendom, toestemming, EduID), de noodzaak van een **Student Kiest Systeem (SKS)** en een **modulaire onderwijsovereenkomst**, aan **enterprise messaging-patronen** (o.a. guaranteed delivery, dead letter, idempotentie, berichtvolgorde), en aan **student journeys** bij pilotinstellingen en **mockups** om draagvlak te creëren.

**Samenhang:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md) beschrijft **waar** we dit vastleggen. [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md) beschrijft de **eerste technische keten en fundamenten** waarin deze principes **inhoudelijk** landen. [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) verankert **leeruitkomsten + SBU/EC** als maatstaf voor **logistieke containergrootte** in koppelvlakken.[0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) verankert het **Student Keuze Systeem (SKS)** als **zelfstandige referentiecomponent** in plaat en model.

### Beslissing (concept)

1. **Student kiest** is een **leidend uitgangspunt** voor OKx-uitwerking in het flexibele onderwijslandschap: architectuur en koppelvlakken moeten **keuze**, **personaliseren** en **ketenoverstijgende** routes **ondersteunen**, binnen wettelijke en kwaliteitskaders (niet: “alles vrij zonder onderwijskundige structuur”).
2. **Leeruitkomsten** worden als **sleutel** gebruikt om flexibel onderwijs **inhoudelijk** te ordenen en te koppelen aan **logistiek** (o.a. wat staat in de catalogus, wat wordt gepland, wat wordt getoetst) — consistent met de verdieping op curriculum en catalogus in [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md).
3. **Onderwijskundige** aspecten worden **expliciet** meegenomen naast **pure logistiek**; abstracte architectuur alleen is **onvoldoende** voor draagvlak bij instellingen en docent/planner-rollen.
4. **Tastbare communicatie** (o.a. **student journeys**, mockups, scenario’s in verschillende volwassenheidsgraden) is **bewust onderdeel** van de aanpak om **businesscase** en **begrip** te versterken — **parallel** aan technische specificatie, niet pas als “laatste stap”.
5. Randvoorwaarden (wallet, SKS, overeenkomst, berichtenpatronen) worden in specificaties en het model **herkenbaar** gemaakt waar ze de keten raken; **detail-uitwerking** kan in afzonderlijke documenten of latere ADR’s.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Alleen logistieke koppelvlakken** (rooster, inschrijving, cijfers) | Sneller te bouwen, minder discussie | **Mismatch** met flexibilisering en **LLO**; **keuze** en **kwaliteit** blijven onderbelicht |
| **B. Alleen onderwijskundige visiedocumenten** zonder technische binding | Breed draagvlak in het begin | **Geen** afdwingbare **interoperabiliteit** |
| **C. (Gekozen richting)** Gekoppelde onderwijskundige + logistische uitwerking met leeruitkomsten als sleutel | **Samenhang** tussen beleid, onderwijs en ICT | **Hoge complexiteit**; **afstemming** met examen-/kwaliteitsketen nodig |

### Consequenties

- **Stakeholders:** **Instellingen** moeten zowel **onderwijs** als **ICT** aan tafel hebben; **leveranciers** krijgen **duidelijkere** functionele kaders dan “alleen API’s”.
- **Werk:** Extra **scenario- en journey-werk**; **integratie** met bestaande kwalificatie- en examenstructuur (evolutionair, niet alles in één ADR).
- **Risico’s:** **Scope creep** door breedte “student kiest”; mitigatie via **mijlpalen** (pilots, journeys) en **backlog** in GitHub ([0001](0001-publieke-repo-en-samenwerkingsmodel.md)).

### Impact op `architecture/model/model.archimate`

- **Concepten:** Leeruitkomsten, keuze-momenten, en **rollen** (student, planner, docent, enz.) moeten in relevante views **herkenbaar** zijn of **traceerbaar** naar documentatie — niet alleen als technische interfaces.
- **Koppelvlakken:** Berichten- en integratiepatronen moeten **consistent** zijn met **foutafhandeling** en **procesvolgorde** (zoals in notulen genoemd); detail per koppelvlak volgt uit specifieke uitwerkingen.
- **Samenhang met [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md):** het **informatiemodel** rond catalogus en curriculum moet **leeruitkomsten** en onderwijsstructuur **kunnen** dragen, conform dit ADR.

### Relaties en links

- **Gerelateerde ADR’s:** [0001](0001-publieke-repo-en-samenwerkingsmodel.md) (repo en workflow), [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md) (keten en fundament), [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) (SBU/EC als logistieke grootte bij leeruitkomsten), [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) (SKS als referentiecomponent)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md`
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/transcript.md`
  - `doc/meetings kernteam/okx_si_team_afstemming_josvdarend_240326/okx_si_team_afstemming_josvdarend_aanhaken_voortgang_okx_240326_summary.md` (context bredere OKx-aanpak)
- ArchiMate: `architecture/model/model.archimate`
- Docs: [`doc/OKx_Projectoverzicht.md`](../../doc/OKx_Projectoverzicht.md), [`architecture/docs/principes.md`](../docs/principes.md)

### Vervangt (optioneel)

- Vervangt het eerdere gecombineerde voorstel `0001-centrale-repo-keten-catalogus-en-drielagen-fundament.md` (opgesplitst in 0001–0003).
