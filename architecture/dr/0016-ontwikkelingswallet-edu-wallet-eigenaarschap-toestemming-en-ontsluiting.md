## Ontwikkelingswallet (EDU-wallet): eigenaarschap individu, toestemming en ontsluiting via EduID

Status: Voorstel

Datum: 2026-04-20

### Context

In het kernteamoverleg rond **StudentKiest** is een strategische visie besproken op een **Student Ontwikkelings Wallet** (EDU-wallet). Daarbij zijn drie richtinggevende principes benoemd:

1. De wallet is **eigendom van het individu**.
2. Instellingen (en andere partijen) vragen **expliciete toestemming** voor inzage.
3. Ontsluiting van context (leer-/zorg-/werkgeschiedenis) loopt via **EduID** en publieke standaarden.

Daarnaast komt de wallet in latere uitwerking terug als bron voor **credentialcontrole bij intake**: behaalde credentials worden bij intake geraadpleegd om te bepalen of de student aan toelatingsvoorwaarden voldoet (zie [0013](0013-microcredentials-scope-en-credentialcontrole-intake.md)).

Tot nu toe wordt de wallet in OKx wel genoemd als randvoorwaarde (o.a. [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md), [0013](0013-microcredentials-scope-en-credentialcontrole-intake.md)), maar er is nog geen expliciet ADR dat de wallet als **ketenvoorziening** positioneert met alternatieven, consequenties en impact op `architecture/model/model.archimate`.

Bronnen:
- `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md`
- `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_20260413/summary.md`

### Beslissing

We leggen vast dat OKx de **ontwikkelingswallet (EDU-wallet)** hanteert als ketenvoorziening met de volgende architectuurkeuzes:

1. **Eigenaarschap:** de wallet (en de daarin opgeslagen context/credentials) is primair **van het individu**; de wallet is geen instellingseigendom.
2. **Toestemming en inzage:** partijen vragen expliciet **toestemming** voor toegang/inzage in (delen van) de wallet.
3. **Ontsluiting via EduID:** identificatie/ontsluiting richting wallet gebeurt via **EduID** als broker/identity layer, met gebruik van publieke standaarden waar mogelijk.
4. **Ketenrol:** de wallet is een gedeelde bron voor o.a. intake/credentialcontrole en (in bredere keten) het beschikbaar stellen van context die nodig is voor studentkeuze en plaatsing, met respect voor toestemming/privacyscheiding.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Centraal register zonder individueel eigenaarschap** | Simpel governance-model voor aanbieders | Past niet bij uitgangspunt eigenaarschap individu; risico op trust- en privacyproblemen |
| **B. Alleen decentrale portfolio’s per instelling** | Sluit aan bij bestaande systemen | Geen ketenbrede mobiliteit; veel point-to-point; lastig voor intake bij andere instelling |
| **C. Wallet zonder expliciete toestemmingslaag** | Minder complex in implementatie | Niet acceptabel qua privacy/trust; frictie met publieke/sectorprincipes |
| **D. (Gekozen richting)** **Individuele wallet + expliciete toestemming + ontsluiting via EduID** | Ondersteunt mobiliteit en LLO; expliciete privacygovernance; sluit aan op besproken principes | Afhankelijkheid van identity/consent-infrastructuur; vereist scherpe scope in MVP |

### Consequenties

- **Procesontwerp:** intake bevat een expliciete stap voor het raadplegen/controleren van credentials vanuit de wallet (zie [0013](0013-microcredentials-scope-en-credentialcontrole-intake.md)).
- **Dataminimalisatie:** koppelvlakken moeten uitgaan van minimale gegevensdeling; alleen wat nodig is voor de processtap wordt opgevraagd met toestemming.
- **Ketenverantwoordelijkheden:** instellingen blijven issuer van bepaalde credentials (zoals besproken bij microcredentials), maar de wallet fungeert als gedeelde “read”-bron in ketenprocessen.
- **Architectuurafbakening:** OKx legt hier het **ketenpatroon** vast, niet de volledige product-/platformkeuze of operationele implementatie.

### Relaties en links

- **Gerelateerde ADR’s:**
  - [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) — wallet als randvoorwaarde in student kiest context
  - [0012](0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md) — leerroute als entiteit (kan wallet-relatie krijgen)
  - [0013](0013-microcredentials-scope-en-credentialcontrole-intake.md) — credentialcontrole bij intake (wallet als databron)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md`
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_20260413/summary.md`
- ArchiMate model: `architecture/model/model.archimate` (voeg EDU-wallet als ketenvoorziening toe; modelleer relaties met EduID, intake/credentialcontrole en relevante referentiecomponenten; benoem toestemming/consent als expliciet concept in views waar passend)

