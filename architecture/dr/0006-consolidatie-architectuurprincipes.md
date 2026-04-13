## Consolidatie en review architectuurprincipes OKx (AP01–AP17 → AP01–AP13)

Status: Voorstel

Datum: 2026-04-09

### Context

Na opname van de [MOSA-visie](../docs/principes/doc/MOSA-Visiedocument.md) en de [MOSA vs OKx analyse](../docs/principes/doc/MOSA_vs_OKx_analyse.md) bevatte [`principes.md`](../docs/principes/doc/principes.md) **17 architectuurprincipes** (AP01–AP17). Vijf daarvan (AP13–AP17) waren rechtstreeks afgeleid uit de MOSA-visie.

Een kritische review bracht de volgende bevindingen naar voren:

1. **Te veel principes** — 17 principes zijn moeilijk te onthouden en te communiceren naar de bredere doelgroep (instellingen, leveranciers, beleidsmakers), die vaak niet technisch van aard is.
2. **Overlap** — Meerdere principes dekten hetzelfde thema:
   - AP07 (dataminimalisatie) en AP08 (privacy & security by design) delen het thema gegevensbescherming.
   - AP09 (transparantie besluitvorming) en AP10 (traceerbaarheid naar model) overlappen op navolgbaarheid.
   - AP13 (leveranciersonafhankelijkheid) overlapt met AP04 (OEAPI, tenzij) en AP05 (componentgrenzen).
   - AP15 (open standaarden/open source) overlapt met AP04 en is deels een werkafspraak (tooling).
3. **Dunne rationale** — AP03 (AMIGO) miste de verbinding met de projectdoelstelling en Edustandaard als beheersorgaan.
4. **Applicatiedenken** — AP05 benoemde componentgrenzen, maar maakte onvoldoende expliciet *waarom* referentiecomponenten loskomen van applicaties.
5. **Te smalle scope AP16** — Alleen "student centraal" terwijl ook onderwijsprofessionals (docenten, coaches, planners, ondersteunend personeel) geraakt worden door ketenwijzigingen.
6. **Vaag toekomstperspectief** — AP14 (data-soevereiniteit) mengde concrete huidige acties (consent, doelbinding) met toekomstige richting (wallets, SSI) zonder onderscheid.
7. **Zwakste principe** — AP17 (duurzaam API-ontwerp) had een dunne koppeling naar MOSA-principe 6 (milieu) en was beter te plaatsen als best practice bij AP10 (robuust in de praktijk).

### Beslissing

We consolideren van **17 naar 13 principes**. De oorspronkelijke 17 worden teruggebracht naar 12 door samenvoeging en integratie. Daarnaast is **AP13** (source system ownership) toegevoegd als nieuw principe afgeleid uit de MOSA-analyse (§6: IAM-domein) en de praktijkervaring met koppelvlakspecificaties. Onderstaande tabel beschrijft per principe de afweging en het besluit.

#### Principes die (nagenoeg) ongewijzigd blijven

| Principe | Beoordeling | Besluit |
|----------|-------------|---------|
| **AP01 — Keten vóór koppelvlak** | Sterk en helder. Rationale was duidelijk; MOSA §4.4 onderbouwing goed. | Behouden, lichte redactionele aanscherping. |
| **AP02 — Semantiek vóór techniek** | Kernprincipe, helder geformuleerd. | Behouden ongewijzigd. |
| **AP06 — Contracten zijn versieerbaar en evolueerbaar** | Goede stelling. De bullet "foutpaden (errors/retries)" is echter een operational-readiness concern en hoort bij AP12 (nu AP10). | Behouden; foutpaden-bullet verplaatst naar AP10. |
| **AP11 — Meervoudige implementatie richting standaard** | Sterk: de >1 instelling + >1 leverancier eis is concreet en toetsbaar. | Behouden, hernummerd naar **AP09**. |
| **AP12 — Robuust in de praktijk** | Sterk concept, maar implicaties waren te technisch. | Behouden, hernummerd naar **AP10**. Verrijkt met een niet-technische implicatie (impact op planning, docenten), foutpaden-bullet uit AP06, en efficiënt-API-content uit AP17. |

#### Principes die versterkt worden

| Principe | Afweging | Besluit |
|----------|----------|---------|
| **AP03 — AMIGO als standaardiseringsroute** | Rationale was te dun: "sectorbreed patroon" is geen overtuigend argument. De werkelijke reden is de projectdoelstelling *"Komen tot gezamenlijke taal en standaarden voor gegevensuitwisseling die een scala aan flexibilisering mogelijk maken"* en het feit dat **Edustandaard** — het orgaan dat de OKE-standaard beheert — de AMIGO-aanpak draagt. Door via AMIGO te werken, valt OKx automatisch onder de governance van standaardisering en architectuur in de sector. | Rationale versterkt met projectdoelstelling, Edustandaard als borger, en implicatie "werken onder standaarden en architectuur". |
| **AP04 — Koppelvlakken als open, gestandaardiseerde contracten** | Oorspronkelijk te smal als technologiekeuze ("OEAPI, tenzij"). Feedback: het fundamentelere punt ontbrak dat het koppelvlak zelf het gestandaardiseerde contract is dat modulariteit mogelijk maakt en lock-in reduceert. Elementen van AP13 (leveranciersonafhankelijkheid) en AP15 (open standaarden) versterken het. "OEAPI, tenzij" en "open-source-tooling" zijn geen abstracte principes maar concrete keuzes. | Herformuleerd: het koppelvlak als open, gestandaardiseerd contract centraal. Componentvervanging zonder ketenimpact als expliciete implicatie. AP13/AP15-elementen geïntegreerd. **"OEAPI, tenzij"** verplaatst naar OKx-uitgangspunten; open-source-tooling eveneens naar uitgangspunten. |
| **AP05 — Referentiecomponenten als gedeeld referentiekader** | Oorspronkelijk als "referentiecomponenten boven applicatiedenken" — te scherp: het suggereert dat OKx applicaties terzijde schuift. De werkelijke intentie is dat referentiecomponenten een **gedeeld vocabulaire** bieden voor functie en gedrag, zodat applicaties van verschillende leveranciers vergelijkbaar worden op koppelvlakniveau. OKx gaat uitsluitend over koppelvlakinteractie; leveranciers behouden volledige soevereiniteit over hun applicatie-inrichting. | Herformuleerd naar **"Referentiecomponenten als gedeeld referentiekader"**. Leverancierssoevereiniteit expliciet benoemd. OKx-scope beperkt tot koppelvlakinteractie, niet tot applicatiefunctionaliteit. |

#### Samenvoegingen

| Oud | Nieuw | Motivatie |
|-----|-------|-----------|
| **AP07** (dataminimalisatie) + **AP08** (privacy & security by design) | **AP07 — Dataminimalisatie, privacy en security by design** | Beide gaan over gegevensbescherming; scheiden voegt geen onderscheidend vermogen toe. Samengevoegd tot één principe met duidelijke stelling en gecombineerde implicaties. |
| **AP09** (transparantie besluitvorming) + **AP10** (traceerbaar naar model) | **AP08 — Transparantie, traceerbaarheid en navolgbaarheid** | AP09 ging over besluitvorming (issues/PR's/ADR's), AP10 over traceerbaarheid naar artefacten. Samen vormen ze één coherent principe over navolgbaarheid op alle niveaus. |

#### Principes die geherformuleerd worden

| Principe | Afweging | Besluit |
|----------|----------|---------|
| **AP14 — Data-soevereiniteit van de student** | Waardevol en vooruitkijkend, maar mengde concrete verplichtingen (consent, doelbinding) met toekomstige technologieën (wallets, SSI). De sector moet begrijpen wat *nu* geldt en wat *toekomstrichting* is. **Edu-V principe D** ("Regie op gegevens": de onderwijsorganisatie bepaalt welke gegevenssoorten uitgewisseld worden) is een direct relevant kader. | Behouden als **AP11 — Regie op gegevens en data-soevereiniteit**. Gesplitst in *huidige verplichtingen* (consent, doelbinding, Edu-V D-alignment) en *toekomstrichting* (wallets, verifiable credentials, SSI). |
| **AP16 — Student centraal in ketenoptimalisatie** | Sympathiek maar te smal. Flexibilisering raakt niet alleen de student maar ook de **onderwijsprofessional**: docenten, coaches/begeleiders, planners, ondersteunend personeel. De student journey is de basis, maar de impact op professionals die het moeten realiseren moet ook meegewogen worden. | Herformuleerd naar **AP12 — Gebruiker centraal in ketenoptimalisatie**. Stelling en implicaties verbreed naar alle betrokken rollen. |

#### Principes die als zelfstandig principe vervallen

| Principe | Reden | Waar de inhoud landt |
|----------|-------|----------------------|
| **AP13 — Leveranciersonafhankelijkheid en platformneutraliteit** | Overlapt grotendeels met AP04 (koppelvlakken als contracten) en AP05 (referentiekader). "Geen vendor-specifieke extensies" is een implicatie, geen zelfstandig principe. | Elementen opgenomen in **AP04** (gestandaardiseerde contracten, componentvervanging, geen vendor-lock-in) en **AP05** (gedeeld referentiekader met behoud van leveranciersvrijheid). |
| **AP15 — Open standaarden en open-source voorkeur** | "Open standaarden" is al verankerd in AP04 (koppelvlakken als open contracten); "OEAPI, tenzij" en "open-source tooling" zijn concrete keuzes, geen abstracte principes. | Open-standaarden-aspect in **AP04**; "OEAPI, tenzij" en open-source-tooling in **OKx-uitgangspunten**. |
| **AP17 — Duurzaam en efficiënt API-ontwerp** | Zwakste principe: de link naar MOSA-principe 6 (milieu) was geforceerd. De kern (efficiënte payloads, geen onnodige polling, hergebruik patronen) is beter geplaatst als operational best practice. | Efficiëntie-implicaties in **AP10** (robuust in de praktijk). Doelgerichte payloads al geborgd via **AP07** (dataminimalisatie). |

#### Nieuw principe (niet uit consolidatie, maar aanvullend afgeleid)

| Principe | Afweging | Besluit |
|----------|----------|---------|
| **AP13 — Source system ownership en doelbinding per referentiecomponent** | Bij het specificeren van koppelvlakken bleek dat zonder expliciete bronverantwoordelijkheid per attribuut het risico ontstaat dat functionele componenten (bijv. SKS) onbedoeld identiteitsdata gaan distribueren naar downstream systemen (bijv. LMS). IDM en provisioning vallen buiten OKx-scope maar zijn voorwaardelijk. MOSA §6 adresseert IAM als apart domein; MOSA principes 8/9 vereisen doelbinding en AVG-conformiteit. Bestaande principes (AP05 componentgrenzen, AP07 dataminimalisatie) dekken dit onvoldoende af: ze zeggen *wat* je niet moet delen en *dat* componenten gescheiden zijn, maar niet *wie de bron is* van welke data en wat er gebeurt als een associatie-leggend component onbedoeld doorgeefluik wordt. | Opgenomen als **nieuw zelfstandig principe AP13**. Impliceert data-ownership-tabel per koppelvlak, associaties boven attributen, en IDM/provisioning als expliciet voorwaardelijk kader. |

#### Resulterende structuur (AP01–AP13)

| Nr | Titel | Kern |
|----|-------|------|
| AP01 | Keten vóór koppelvlak | Optimaliseer voor de hele keten |
| AP02 | Semantiek vóór techniek | Eerst semantische overeenstemming |
| AP03 | AMIGO als standaardiseringsroute | Edustandaard-governance, gezamenlijke taal |
| AP04 | Koppelvlakken als open, gestandaardiseerde contracten | Modulariteit, geen lock-in; technologiekeuze in uitgangspunten |
| AP05 | Referentiecomponenten als gedeeld referentiekader | Gedeeld vocabulaire; leveranciersvrijheid blijft |
| AP06 | Contracten zijn versieerbaar en evolueerbaar | Migratie, deprecatie, exit-strategie |
| AP07 | Dataminimalisatie, privacy en security by design | Gegevensbescherming als ontwerpcriteria |
| AP08 | Transparantie, traceerbaarheid en navolgbaarheid | Besluiten én artefacten navolgbaar |
| AP09 | Meervoudige implementatie richting standaard | >1 instelling + >1 leverancier |
| AP10 | Robuust in de praktijk | Niet-happy-flow, efficiënt, operationeel |
| AP11 | Regie op gegevens en data-soevereiniteit | Consent nu; SSI/wallets als toekomstrichting |
| AP12 | Gebruiker centraal in ketenoptimalisatie | Student + professional + planner + coach |
| AP13 | Source system ownership en doelbinding | Bronsysteem per attribuut; IDM als randvoorwaarde |

### Alternatieven

| Optie | Voordeel | Nadeel |
|-------|----------|--------|
| **A. 17 principes behouden** | Geen hernummering, geen risico op informatieverlies | Te veel om te communiceren; overlap verwaart |
| **B. Radicaal terugbrengen naar 6–8** | Zeer beknopt, makkelijk te onthouden | Verlies van waardevolle nuance (data-soevereiniteit, meervoudige implementatie) |
| **C. (Gekozen) Consolidatie naar 12 + 1 nieuw (AP13)** | Balans: compact genoeg om te communiceren, rijk genoeg om richtinggevend te zijn; AP13 adresseert een gat dat bij koppelvlakspecificatie zichtbaar werd | Hernummering vereist update van verwijzingen |

### Introductie OKx-uitgangspunten (naast principes)

Naast de architectuurprincipes introduceert `principes.md` een sectie **OKx-uitgangspunten**. Het onderscheid:

- **Principes** zijn abstract en stabiel — ze beschrijven *waarom* we dingen op een bepaalde manier doen en wijzigen niet snel.
- **Uitgangspunten** zijn gefundeerde besluiten om blocking issues te voorkomen — ze zijn concreter, kunnen evolueren, en beschrijven *wat* we aannemen en *hoe* we werken.

De voormalige "werkafspraken" sectie is hernoemd naar uitgangspunten en uitgebreid met:

| Uitgangspunt | Toelichting |
|---|---|
| **OEAPI, tenzij** | Verplaatst vanuit AP04: de concrete technologiekeuze is een uitgangspunt, niet een abstract principe. AP04 behoudt de contractfocus. |
| **IDM en provisioning als randvoorwaarde** | Buiten scope maar kritisch; verwijzing naar AP13 (source system ownership). |
| **Test-driven op berichtniveau** | Given-when-then testcases vóór implementatie; verifieerbare interoperabiliteit. |
| **Afstemming met referentiearchitecturen** | MORA/HORA/FORA als referentie, maar pragmatisch: voldoende beschrijven, niet overbeschrijven. |
| **Show don't tell** | Praktische voorbeelden (OEAPI-profielen, API-specs, mockups) zo dicht mogelijk bij het eindresultaat. |
| **BOPSI-aanpak voor adoptie** | IST→SOLL per aspect (Beleid, Organisatie, Proces, Systeem, Informatie) samen met instellingen. |
| **Borging in lijnorganisaties** | Actief vormgeven van beheerorganisaties die deliverables overnemen na programma-einde. |
| **Samen ontwerpen — open boek** | Domein te complex voor één team; constructieve verbetervoorstellen via issues/PR's. |

### Consequenties

- **`principes.md`** wordt herschreven met AP01–AP13 en een nieuwe sectie OKx-uitgangspunten. Oude nummering en "werkafspraken" vervallen.
- **`MOSA_vs_OKx_analyse.md`** wordt bijgewerkt met verwijzingen naar de nieuwe nummering en het nieuwe thema source system ownership.
- **OEAPI, tenzij** verhuist van AP04 (principe) naar uitgangspunten; AP04 behoudt de abstracte contractfocus.
- **Toekomstige ADR's en documenten** refereren aan AP01–AP13 (principes) en aan uitgangspunten waar relevant.
- **Edu-V alignment**: AP11 refereert expliciet aan [Edu-V principe D (Regie op gegevens)](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes).
- **IDM/provisioning als randvoorwaarde**: AP13 benoemt IDM/provisioning expliciet als buiten OKx-scope maar voorwaardelijk. Dit wordt versterkt door het uitgangspunt "IDM en provisioning als randvoorwaarde".
- **Adoptie**: de BOPSI-aanpak en borging in lijnorganisaties zijn als uitgangspunten vastgelegd, niet als principes — ze zijn concreet en evolueren met de projectfase.
- **Doelgroep**: formuleringen worden waar mogelijk niet-technisch gehouden; bij onvermijdelijke technische termen volgt een korte toelichting.

### Relaties en links

- ADR's: [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (student kiest), [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) (SKS), [0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) (SKS/SVS-rollenverdeling — context voor AP13: componentgrenzen en dataverantwoordelijkheid)
- Docs:
  - [`architecture/docs/principes/doc/principes.md`](../docs/principes/doc/principes.md)
  - [`architecture/docs/principes/doc/MOSA_vs_OKx_analyse.md`](../docs/principes/doc/MOSA_vs_OKx_analyse.md)
  - [`architecture/docs/principes/doc/MOSA-Visiedocument.md`](../docs/principes/doc/MOSA-Visiedocument.md)
- Extern: [Edu-V Architectuurprincipes](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes)
- ArchiMate: `architecture/model/model.archimate` — geen directe modelimpact; principes zijn richtinggevend voor toekomstige views.
