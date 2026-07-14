## Microcredentials buiten scope OKx-definitie; credentialcontrole bij intake

Status: Voorstel

Datum: 2026-04-13

### Context

In het kernteamoverleg **inhoud uitwerken StudentKiest** (13 april 2026) kwam de rol van **microcredentials** aan de orde in twee contexten: (1) wie definieert wat een leeruitkomst/microcredential is en wie geeft deze uit, en (2) wanneer worden behaalde credentials relevant in het StudentKiest-proces?

[0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) benoemt leeruitkomsten als **sleutel** en de ontwikkelingswallet als randvoorwaarde. [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) definieert SBU/EC als logistieke maatstaf. Geen van de bestaande ADR's spreekt zich uit over de **scope-afbakening** van OKx ten aanzien van de **definitie** van microcredentials, noch over het moment waarop **behaalde credentials** als **toelatingsvoorwaarde** worden gecontroleerd.

In de meeting was consensus: OKx hoeft **niet** te bepalen wat precies een leeruitkomst of microcredential is — dat is aan de **sector** en de **instellingen**. Wat OKx wél moet faciliteren is dat credentials **uitgewisseld** kunnen worden en dat ze bij de **intake** worden **gecontroleerd** als toelatingsvoorwaarde. Alda en Niek bevestigden: de **instelling** is de issuer; **Edubadges.nl** is het register. Mark en Niek concludeerden dat microcredentials in de **huidige fase** (keuzemoment, vóór toetsing) nog niet relevant zijn — behalve bij intake, waar eerder behaalde credentials bepalen of een student **mag** inschrijven.

### Beslissing (concept)

1. **Definitie microcredential buiten scope OKx:** OKx neemt **geen** positie in over de precieze definitie van een microcredential of leeruitkomst (bijv. of aanwezigheid volstaat, of een summatieve toets vereist is). Dit is een **sectorale** en **instellingsbeslissing**. OKx gaat uit van het bestaan van leeruitkomsten als **feit** en beschrijft de **interfaces** waarmee ze worden uitgewisseld.
2. **Issuer = instelling:** in het OKx-ketenmodel is de **instelling** de issuer van microcredentials. Het register is **Edubadges.nl** (of equivalent). OKx-koppelvlakken moeten **issuer** en **registratie** als attributen kunnen dragen, maar schrijven niet voor welk platform wordt gebruikt.
3. **Credentialcontrole bij intake:** bij de intake (onderdeel van het StudentKiest-proces, na oriëntatie en vóór plaatsing) worden **behaalde credentials** uit de ontwikkelingswallet gecontroleerd als **toelatingsvoorwaarde**. Dit is een **expliciete processtap** die in het procesmodel en de koppelvlakken herkenbaar moet zijn.
4. **Credentials lezen vanuit wallet:** de controle haalt credentials op uit de **ontwikkelingswallet** ([0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md)). Alle instellingen schrijven resultaten **naar** en lezen **uit** dezelfde walletstructuur, zodat cross-instelling credentialcontrole mogelijk is.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. OKx definieert microcredentials** volledig | Uniformiteit in de keten | **Buiten mandaat** OKx; sector en OCW zijn aan zet; risico op vertraging |
| **B. Geen credentialcontrole in het proces** | Eenvoudiger procesmodel | **Geen instroomborging**; studenten kunnen zich inschrijven zonder vereiste voorkennis |
| **C. Credentials alleen bij toetsing** (einde traject) | Minder processtappen vooraf | **Te laat**: instelling ontdekt pas achteraf dat student niet kwalificeert |
| **D. (Gekozen richting)** **Definitie bij sector + controle bij intake via wallet** | Duidelijke scope OKx; intake geborgd; flexibel naar sectorontwikkelingen | **Afhankelijkheid** van walletinfrastructuur en sectorale standaardisatie van credentials |

### Consequenties

- **OKx-specificaties** beschrijven **interfaces** voor het ophalen en controleren van credentials, maar schrijven **niet** voor wat de credentials inhoudelijk bevatten.
- **Processontwerp:** de intake krijgt een expliciete stap **"controleer behaalde credentials"** vóór plaatsing/inschrijving.
- **Stakeholders:** instellingen behouden autonomie over de definitie van microcredentials; leveranciers krijgen een **helder** koppelpunt (wallet → intake) zonder dat OKx de inhoud dicteert.
- **Empos-programma's** en OCW-richtlijnen (benoemd door Niek in het overleg) evolueren onafhankelijk; OKx-koppelvlakken moeten **forward-compatible** zijn met veranderende definities.

### Impact op `architecture/model/model.archimate`

- **Processen:** een **controlestap** voor credentials in het intakeproces, gekoppeld aan de ontwikkelingswallet als databron.
- **Informatie-objecten:** credential/microcredential als entiteit met attributen **issuer**, **register**, **leeruitkomstreferentie**, **behaaldatum**; de **inhoudelijke** structuur (wat maakt het een credential) wordt **niet** door OKx vastgelegd.
- **Relaties:** wallet ↔ intake (lezen credentials), instelling → wallet (schrijven credentials na beoordeling), Edubadges.nl als extern register.

### Relaties en links

- **Gerelateerde ADR's:** [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (wallet, leeruitkomsten als sleutel), [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) (SBU/EC), [0006](0006-studentorientatie-trechter-ketenfase.md) (oriëntatiefase → intake), [0012](0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md) (intake en keuzegate)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings: `architecture/meetings/20260413_okx_kernteam_inhoud_uitwerken_studentkiest/summary.md`, `.../transcript.md`
- ArchiMate: `architecture/model/model.archimate`

### Vervangt (optioneel)

- —
