## Leeruitkomsten als opaque sleutels in de koppeling OC-P&R

Status: Voorstel

Datum: 2026-07-23

### Context

Regelset-voorwaarden zijn uitgedrukt in behaalde leeruitkomsten (ADR 0022): je moet bepaalde leeruitkomsten behaald hebben om deel te nemen aan bijvoorbeeld een keuzedeel. Het planningssysteem gebruikt die voorwaarden voor volgordebepaling (Wiskunde 1 vóór Ruimtelijk inzicht). De vraag was of planning daarvoor de leeruitkomst-objecten zelf nodig heeft.

### Beslissing

1. Binnen de koppeling OC-P&R zijn leeruitkomst-ids **opaque sleutels**: ze komen uitsluitend voor binnen regelset-voorwaarden (`voorwaardeVooraf`) en dienen alleen voor volgordebepaling en planvalidatie.
2. De `leeruitkomsten`-lijst (inhoud, aggregatie, `waardedocument`, `indicatieveOmvang`) wordt **niet** over deze koppeling meegeleverd. Het gebruiksprofiel van OC-P&R legt dit vast.
3. Betekenis van leeruitkomsten leeft bij de koppelingen die haar nodig hebben: OC-SIS (resultaatstructuur en onderwijsresultaten, ADR 0022) en OC-LMS (inhoudsvelden voor de leeromgeving).

### Alternatieven

- Optie A: volledige leeruitkomst-laag ook naar planning. Afgewezen: planning doet niets met de betekenis; meesturen vergroot de koppelvlakoppervlakte en de afhankelijkheid zonder functie (dataminimalisatie).
- Optie B: voorwaarden voor planning projecteren naar specificatie-verwijzingen (OC vertaalt). Afgewezen: introduceert een vertaalslag en een tweede waarheid over dezelfde regel; de regel blijft zo niet één bron (#84 R8, één regel met twee consumenten).

### Consequenties

- Het gebruiksprofiel OC-P&R (koppelingspecificatie §6.2) levert `onderwijsspecificaties` en `regelsets`, geen `leeruitkomsten`.
- Planning behandelt leeruitkomst-ids als betekenisloze identifiers; wijzigingen in leeruitkomst-inhoud raken de koppeling OC-P&R niet.
- Conformance-tests voor OC-P&R toetsen volgordebepaling zonder leeruitkomst-resolutie.

### Relaties en links

- Issues: #98, #119, #84
- ADR's: 0021 (gebruiksprofielen), 0022 (resultaatbegrippen conform ROSA KOI)
- Docs: `architecture/agent-artifacts/design-docs/koppelingspecificaties/`

### Vervangt (optioneel)

- Geen.
