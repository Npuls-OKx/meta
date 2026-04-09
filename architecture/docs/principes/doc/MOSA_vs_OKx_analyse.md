# MOSA-visie en OKx-projectscope — Analyse en afleidbare principes

**Status:** Voorstel
**Datum:** 2026-04-09

---

## 1. Inleiding

Het [MOSA-Visiedocument](MOSA-Visiedocument.md) (versie 1.0, januari 2025) beschrijft de doelarchitectuur voor **sectorvoorzieningen** in het mbo: een bestemmingsplan voor vijf tot tien jaar, opgesteld door de MOSA-werkgroep van MBO Digitaal in opdracht van de CIO Raad.

**Project OKx** opereert binnen datzelfde NPuls-kader en richt zich op de **essentiële kern van onderwijslogistiek**: het specificeren van gestandaardiseerde koppelvlakken (interfaces) tussen referentiecomponenten in de onderwijsketen — primair MBO, later HO. OKx levert MOKA-koppelvlakspecificaties, informatiemodellen en OEAPI-uitwerkingen.

**Uitgangspunt van deze analyse:** de MOSA beschrijft architectuurprincipes die recht doen aan de scoping van OKx met **autonomie**, **interoperabiliteit** en **standaarden** in het bijzonder. We nemen alle relevante principes en af te leiden principes over vanuit het MOSA-visiedocument.

---

## 2. Overlap tussen MOSA en OKx

De volgende thema's komen in beide terug:

| Thema | MOSA | OKx |
|-------|------|-----|
| **Interoperabiliteit** | Kernthema: technische, semantische en procesinteroperabiliteit als voorwaarde voor samenwerking (§4.4) | Primair doel: koppelvlakken standaardiseren zodat systemen interoperabel worden |
| **Standaardisering** | Open standaarden, API-strategie, afsprakenstelsels (principes 3, 4; §4.4) | AMIGO-aanpak, OEAPI als voorkeurstandaard ("OEAPI, tenzij"), MOKA-templates |
| **Autonomie** | Instellingen behouden keuzes over intern applicatielandschap; MOSA dingt niet af op autonomie (§4.4) | OKx specificeert de buitenkant (interface), niet de binnenkant; referentiecomponenten boven applicatiedenken (AP05) |
| **Flexibilisering** | Modulair onderwijs, persoonlijke leerroute, instellingsoverstijgend aanbod (§1.1, §5.3) | Informatiestromen rond curriculum, catalogus, planning en student-keuze ondersteunen flexibilisering |
| **Leven Lang Ontwikkelen** | Laagdrempelige, leven-lang-toegang tot onderwijs en portfolio (§1.1, §5) | Referentiecomponenten (SKS, SVS, KRS) faciliteren leven-lang-keuzes en resultaatopbouw |
| **Keten eerst** | Samenwerking in de hele keten; voorkomen van versnippering (§1.1) | AP01: keten vóór koppelvlak; optimaliseren voor de hele keten |
| **Privacy en beveiliging** | Principes 8, 9: AVG-conformiteit, vertrouwelijkheid, integriteit, transparantie | AP07: dataminimalisatie, privacy en security by design |
| **Wendbare componenten** | Principe 3: onafhankelijk, schaalbaar, koppelbaar/ontkoppelbaar | AP05: referentiecomponenten boven applicatiedenken; AP06: versieerbare contracten |
| **Publieke waarden en ethiek** | Principes 2, 4: Ethics by Design, WaardenWijzer, openheid | AP08: transparantie, traceerbaarheid en navolgbaarheid |
| **Platform als concept** | MOSA = sectorbreed platform met services, portalen, aansluitpartijen | OKx draagt bij als specificeerder van koppelvlakken die het platform voedt |

---

## 3. Verschillen

| Aspect | MOSA | OKx |
|--------|------|-----|
| **Scope** | Sector-breed: alle sectorvoorzieningen (presentatie, platform services, aangesloten partijen) | Gericht: essentiële kern van onderwijslogistiek-koppelvlakken |
| **Granulariteit** | Visieniveau: services op hoofdlijnen, scenario's en use cases | Specificatieniveau: berichtspecificaties, klassendiagrammen, API-endpoints |
| **Horizon** | 5–10 jaar doelarchitectuur | Iteratief: begrijpen → ontwerpen → realiseren, met direct bruikbare deliverables |
| **Domeinen** | Onderwijs en Flexibilisering, IAM, Onderzoek | Primair Proces Onderwijs en Flexibilisering (keten curriculum → student) |
| **Technologiekeuze** | API-strategie (niet specifiek OEAPI) | OEAPI als voorkeur ("tenzij"), MOKA-metamodel |
| **Governance** | Signaleert governance-uitdagingen; geen uitspraken over inrichting | Governance via federatief werken: issues, PR's, ADR's, reviewcycli |
| **Identiteit / IAM** | Uitgebreid domein: eduID, SSI, wallets, verifiable credentials, ECK iD | Niet in primaire scope; raakvlak bij toekomstige inschrijvingsstromen |
| **Onderzoek** | Domeinarchitectuur Onderzoek voorzien (valorisatie) | Buiten scope |
| **AI** | Expliciet geadresseerd als aandachtspunt bij realisatie | Operationeel ingezet (Cursor AI-agents), geen architectureel principe |

---

## 4. Afleidbare architectuurprincipes voor OKx

Onderstaande principes zijn **af te leiden uit de MOSA-visie** en relevant voor de OKx-scope. Waar ze overlappen met bestaande OKx-AP's, versterken ze de onderbouwing. Waar ze nieuw zijn, verdienen ze opname.

### 4.1 Principes die bestaande OKx-AP's versterken

| MOSA-principe | Versterkt OKx-AP | Toelichting |
|---|---|---|
| §4.4 Autonomie + interoperabiliteit | **AP01** (Keten vóór koppelvlak) | MOSA onderbouwt dat interoperabiliteit de sleutel is om autonomie te behouden bij ketenoptimalisatie |
| §4.4 Technische + semantische + procesinteroperabiliteit | **AP02** (Semantiek vóór techniek) | MOSA benoemt drie lagen van interoperabiliteit; OKx AP02 focust op semantiek-eerst, volledig aligned |
| Principe 3: wendbare componenten, API-strategie | **AP05** (Referentiecomponenten boven applicatiedenken) | MOSA onderbouwt dat componenten onafhankelijk, schaalbaar en ontkoppelbaar moeten zijn |
| Principe 4: open, delen als norm, open standaarden | **AP04** (OEAPI, tenzij) | MOSA-openheid versterkt de keuze voor open standaarden (OEAPI) |
| Principe 7: robuust, continuïteit | **AP10** (Robuust in de praktijk) | MOSA en OKx eisen beide dat niet-happy-flow onderdeel is van de standaard |
| Principe 8: beveiligd, AVG | **AP07** (Dataminimalisatie, privacy en security by design) | Directe overlap |
| Principe 9: transparant | **AP08** (Transparantie, traceerbaarheid en navolgbaarheid) | MOSA-transparantie gaat over systeemwerking; OKx AP08 over besluitvorming — complementair |

### 4.2 Nieuwe of aanvullende principes af te leiden uit MOSA

| Thema | Bron in MOSA | Relevantie voor OKx |
|---|---|---|
| **Data-soevereiniteit** | §4.4: "de student heeft zelf regie over welke informatie met wie gedeeld wordt"; §6: SSI, wallets, verifiable credentials | OKx-koppelvlakken moeten rekening houden met datasoevereiniteit van de student: consent-mechanismen, doelbinding, en toekomstige wallet-integratie |
| **Open standaarden en open source** | Principe 4: open ecosysteem, internationale open standaarden; §4.4: standaarden voor verbindingen en semantiek | Explicieter dan AP04: niet alleen OEAPI, maar ook een bredere voorkeur voor open standaarden en open-source-tooling in het specificatieproces |
| **Platformneutraliteit** | §4.3: "geen één groot centraal systeem"; §4.4: "interoperabiliteit bevordert autonomie" | OKx-specificaties mogen geen platformlock-in creëren; ze moeten implementeerbaar zijn door willekeurige leveranciers |
| **Leveranciersonafhankelijkheid** | Principe 1: onafhankelijkheid van leveranciers is geborgd | Koppelvlakspecificaties moeten leverancierneutraal zijn: geen vendor-specifieke extensies zonder ADR |
| **Doelmatig ecosysteem / student centraal** | Principe 1: student (de lerende) centraal | In ketenoptimalisatie de student-ervaring als toetssteen meenemen: stromen die de student raken moeten de student-centraalheid weerspiegelen |
| **Duurzaamheid** | Principe 6: milieu en omgeving zo min mogelijk belasten, hergebruik bevorderen | Relevant voor API-ontwerp: efficiënte payloads, vermijden van onnodige polling, hergebruik van bestaande specificaties |
| **Wendbaarheid via exit-strategie** | Principe 3: exit-plannen in contracten | OKx-koppelvlakken moeten migratie en versieovergang ondersteunen; deprecatie-paden expliciet beschrijven |
| **Verifiable Credentials / SSI** | §6.1: eduID, wallets, verifiable credentials driehoek (issuer/holder/verifier/registry) | Toekomstig raakvlak voor OKx: resultaten en inschrijvingsgegevens als credentials. Specificeer datastructuren credential-ready |

---

## 5. Samenvatting

```
MOSA-visie                              OKx-projectscope
──────────────────────                  ──────────────────────
Sector-breed platform                   Essentiële kern:
voor alle voorzieningen                 koppelvlakken voor
(5–10 jaar doelarchitectuur)            onderwijslogistiek
                                        (iteratief, deliverables)
        ╲                             ╱
         ╲     Gedeelde kern          ╱
          ╲                          ╱
           ╲  - Interoperabiliteit  ╱
            ╲ - Standaardisering   ╱
             ╲- Autonomie         ╱
              ╲- Keten eerst     ╱
               ╲- Privacy       ╱
                ╲- Openheid    ╱
                 ╲            ╱
```

De MOSA biedt OKx een **sector-strategische onderbouwing** voor architectuurprincipes die OKx al deels heeft geformuleerd. De analyse levert:

1. **Versterking** van 7 bestaande OKx-AP's met MOSA-onderbouwing.
2. **8 nieuwe/aanvullende thema's** die als OKx-principes opgenomen kunnen worden: data-soevereiniteit, open standaarden/open source, platformneutraliteit, leveranciersonafhankelijkheid, student centraal, duurzaamheid, wendbare exit-strategie, en credential-readiness.

Na review en consolidatie ([ADR 0006](../../../dr/0006-consolidatie-architectuurprincipes.md)) zijn deze thema's geïntegreerd in de bestaande principes (AP01–AP12) in [`principes.md`](principes.md). Sommige thema's zijn opgenomen als zelfstandig principe (data-soevereiniteit → AP11, gebruiker centraal → AP12), andere zijn verwerkt in bestaande principes (leveranciersonafhankelijkheid → AP04/AP05, open standaarden → AP04, duurzaamheid → AP10, exit-strategie → AP06, credential-readiness → AP11).

---

## Bronnen

- [MOSA-Visiedocument v1.0](MOSA-Visiedocument.md) (januari 2025)
- [OKx Projectoverzicht](../../../../doc/OKx_Projectoverzicht.md)
- [OKx Architectuurprincipes](principes.md)
- [MORA](https://mora.mbodigitaal.nl/)
- [AMIGO-aanpak](https://www.edustandaard.nl/amigo/aanpak/)
- [OEAPI](https://openonderwijsapi.nl/)
- [Edu-V Architectuurprincipes](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes)
