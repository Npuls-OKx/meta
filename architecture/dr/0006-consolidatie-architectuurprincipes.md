## Consolidatie en review architectuurprincipes OKx (AP01–AP17 → AP01–AP12)

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

We consolideren van **17 naar 12 principes**. Onderstaande tabel beschrijft per principe de afweging en het besluit.

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
| **AP04 — OEAPI, tenzij** | Goed, maar elementen van AP13 (leveranciersonafhankelijkheid) en AP15 (open standaarden) versterken het. "Open-source-tooling" in de rationale was misplaatst (dat is een werkafspraak). | AP13-elementen (leverancierneutraliteit, geen vendor-lock-in) en AP15-elementen (open standaarden) geïntegreerd. Open-source-tooling verplaatst naar werkafspraken. |
| **AP05 — Heldere componentgrenzen** | Herkend als sterk, maar miste de kern van het probleem: **instellingen denken in applicaties, niet in referentiecomponenten**. Applicaties worden gebouwd door leveranciers en bevatten meerdere referentiecomponenten. De ene applicatie noemt iets een "vak", de andere een "module". Zonder helder onderscheid blokkeer je standaardisering en gegevensuitwisselingssemantiek. | Herformuleerd naar **"Referentiecomponenten boven applicatiedenken"**. Rationale expliciet over het verschil applicatie vs. referentiecomponent en de gevolgen voor semantiek en standaardisering. AP13-elementen (platformneutraliteit) geïntegreerd. |

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
| **AP13 — Leveranciersonafhankelijkheid en platformneutraliteit** | Overlapt grotendeels met AP04 (OEAPI, tenzij) en AP05 (componentgrenzen). "Geen vendor-specifieke extensies" is een implicatie, geen zelfstandig principe. | Elementen opgenomen in **AP04** (leverancierneutraliteit, geen vendor-lock-in) en **AP05** (platformneutraliteit, implementeerbaar met gangbare stacks). |
| **AP15 — Open standaarden en open-source voorkeur** | "Open standaarden" is al verankerd in AP04 (OEAPI is een open standaard); "open-source tooling" is een werkafspraak, geen architectuurprincipe. | Open-standaarden-aspect in **AP04**; open-source-tooling in **werkafspraken**. |
| **AP17 — Duurzaam en efficiënt API-ontwerp** | Zwakste principe: de link naar MOSA-principe 6 (milieu) was geforceerd. De kern (efficiënte payloads, geen onnodige polling, hergebruik patronen) is beter geplaatst als operational best practice. | Efficiëntie-implicaties in **AP10** (robuust in de praktijk). Doelgerichte payloads al geborgd via **AP07** (dataminimalisatie). |

#### Resulterende structuur (AP01–AP12)

| Nr | Titel | Kern |
|----|-------|------|
| AP01 | Keten vóór koppelvlak | Optimaliseer voor de hele keten |
| AP02 | Semantiek vóór techniek | Eerst semantische overeenstemming |
| AP03 | AMIGO als standaardiseringsroute | Edustandaard-governance, gezamenlijke taal |
| AP04 | OEAPI, tenzij — open en leverancierneutraal | Open standaarden, geen lock-in |
| AP05 | Referentiecomponenten boven applicatiedenken | Los van applicaties; helder semantisch |
| AP06 | Contracten zijn versieerbaar en evolueerbaar | Migratie, deprecatie, exit-strategie |
| AP07 | Dataminimalisatie, privacy en security by design | Gegevensbescherming als ontwerpcriteria |
| AP08 | Transparantie, traceerbaarheid en navolgbaarheid | Besluiten én artefacten navolgbaar |
| AP09 | Meervoudige implementatie richting standaard | >1 instelling + >1 leverancier |
| AP10 | Robuust in de praktijk | Niet-happy-flow, efficiënt, operationeel |
| AP11 | Regie op gegevens en data-soevereiniteit | Consent nu; SSI/wallets als toekomstrichting |
| AP12 | Gebruiker centraal in ketenoptimalisatie | Student + professional + planner + coach |

### Alternatieven

| Optie | Voordeel | Nadeel |
|-------|----------|--------|
| **A. 17 principes behouden** | Geen hernummering, geen risico op informatieverlies | Te veel om te communiceren; overlap verwaart |
| **B. Radicaal terugbrengen naar 6–8** | Zeer beknopt, makkelijk te onthouden | Verlies van waardevolle nuance (data-soevereiniteit, meervoudige implementatie) |
| **C. (Gekozen) Consolidatie naar 12** | Balans: compact genoeg om te communiceren, rijk genoeg om richtinggevend te zijn | Hernummering vereist update van verwijzingen |

### Consequenties

- **`principes.md`** wordt herschreven met AP01–AP12. Oude nummering vervalt.
- **`MOSA_vs_OKx_analyse.md`** wordt bijgewerkt met verwijzingen naar de nieuwe nummering.
- **Werkafspraken** worden aangevuld met "open-source tooling voorkeur" (uit voormalig AP15).
- **Toekomstige ADR's en documenten** refereren aan AP01–AP12.
- **Edu-V alignment**: AP11 refereert expliciet aan [Edu-V principe D (Regie op gegevens)](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes).
- **Doelgroep**: formuleringen worden waar mogelijk niet-technisch gehouden; bij onvermijdelijke technische termen volgt een korte toelichting.

### Relaties en links

- ADR's: [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (student kiest), [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) (SKS)
- Docs:
  - [`architecture/docs/principes/doc/principes.md`](../docs/principes/doc/principes.md)
  - [`architecture/docs/principes/doc/MOSA_vs_OKx_analyse.md`](../docs/principes/doc/MOSA_vs_OKx_analyse.md)
  - [`architecture/docs/principes/doc/MOSA-Visiedocument.md`](../docs/principes/doc/MOSA-Visiedocument.md)
- Extern: [Edu-V Architectuurprincipes](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes)
- ArchiMate: `architecture/model/model.archimate` — geen directe modelimpact; principes zijn richtinggevend voor toekomstige views.
