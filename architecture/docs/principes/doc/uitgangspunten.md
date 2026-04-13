# OKx-uitgangspunten

**Status:** Voorstel
**Datum:** 2026-04-13

Uitgangspunten zijn **gefundeerde besluiten** om blocking issues te voorkomen. Ze zijn concreter dan [architectuurprincipes](principes.md), kunnen evolueren met voortschrijdend inzicht, en beschrijven *wat* we aannemen en *hoe* we werken. Principes beschrijven *waarom*; uitgangspunten beschrijven *wat* en *hoe*.

Uitgangspunten gelden voor iedereen die bijdraagt aan OKx. Ze kunnen wijzigen via **pull request** en, indien nodig, **ADR**.

Zie [ADR 0006](../../../dr/0006-consolidatie-architectuurprincipes.md) voor de afwegingen achter de introductie van uitgangspunten naast principes.

---

## Technologie en standaarden

- **OEAPI, tenzij** — Technologiekeuze voor koppelvlakken is **[OEAPI](https://openonderwijsapi.nl/)**, tenzij OEAPI aantoonbaar niet past. Afwijkingen bevatten een korte "tenzij"-onderbouwing (wat past niet, trade-offs, impact). Bij structurele afwijking: leg vast als ADR. Geen vendor-specifieke extensies zonder ADR. Dit uitgangspunt ondersteunt [AP04 — Koppelvlakken als open, gestandaardiseerde contracten](principes.md#okx-ap04--koppelvlakken-als-open-gestandaardiseerde-contracten).
- **Open-source tooling voorkeur** — Tooling voor specificatie, validatie en generatie is bij voorkeur open source. Specificaties worden in open formaten opgeleverd (OpenAPI/Swagger, JSON Schema, Markdown). Geen verplichte afhankelijkheid van propriëtaire specificatietools.
- **Machine-interpreteerbare formaten** — Uitwerkingen zijn zoveel mogelijk gestructureerd (Markdown, JSON-informatiemodellen, tabellen, schema's). Dit maakt automatisering, AI-assistentie en consistente validatie mogelijk. Publiceer geen vertrouwelijke of persoonsgevoelige gegevens; zie [`doc/Privacy-meetings-en-transcriptie.md`](../../../../doc/Privacy-meetings-en-transcriptie.md).

## Randvoorwaardelijke domeinen

- **IDM en provisioning als randvoorwaarde** — Identity Management en provisioning vallen buiten OKx-scope, maar zijn een **kritische randvoorwaarde** voor correcte werking van koppelvlakken. Zonder helder bronsysteem voor persoonsattributen ontstaat het risico dat functionele componenten onbedoeld identiteitsdata gaan distribueren (zie [AP13 — Source system ownership](principes.md#okx-ap13--source-system-ownership-en-doelbinding-per-referentiecomponent)). OKx benoemt IDM/provisioning expliciet als randvoorwaarde in koppelvlakspecificaties, maar schrijft de oplossing niet voor.

## Kwaliteit en verificatie

- **Test-driven op berichtniveau** — Koppelvlakspecificaties worden bij voorkeur test-driven ontwikkeld: beschrijf eerst de **testcase** (given-when-then), ga daarna bouwen. Door op berichtniveau te testen wordt de interoperabiliteit concreet verifieerbaar vóórdat implementaties worden opgeleverd. Dit versnelt validatie bij leveranciers en voorkomt late integratieproblemen.

## Afstemming en beschrijvingswijze

- **Afstemming met referentiearchitecturen** — OKx stemt de beschrijvingswijze af op de aanpak binnen **MORA** (mbo), **HORA** (ho) en **FORA** (federatief), maar blijft **pragmatisch**: het snijvlak is dat we iets moeten realiseren én tegelijkertijd de keten voldoende beschrijven — maar niet zo veel dat we in een ivoren toren belanden. Voldoende beschrijven, niet overbeschrijven.
- **Show don't tell — praktische voorbeelden zo dicht mogelijk bij het eindresultaat** — Liever OEAPI-profielen, API-specs, mockups, diagrammen (Mermaid, ArchiMate) en korte bullets dan lange lappen tekst. Hoe dichter het artefact bij het eindresultaat, hoe sneller adoptie in diverse gremia verloopt. Zie [`doc/Bijdragen-voor-beginners.md`](../../../../doc/Bijdragen-voor-beginners.md) voor voorbeelden.

## Adoptie en transitie

- **BOPSI-aanpak voor adoptie** — OKx bouwt niet alleen een oplossing maar helpt ook bij het adoptieproces. Via de **BOPSI-aanpak** (Beleid, Organisatie, Proces, Systeem, Informatie) kijken we samen met instellingen waar de huidige situatie (IST) moet veranderen per BOPSI-aspect om toe te groeien naar de streefarchitectuur (SOLL) die we nu uitzetten. Architecture-based designs worden vertaald naar concrete transitiepaden per instelling.
- **Borging in lijnorganisaties** — OKx is een programma/project met een einddatum. Dragen we actief bij aan de vorming van nieuwe of ondersteuning van bestaande **lijnorganisaties** die beoogde deliverables in beheer gaan nemen. Borgingsaspecten (eigenaarschap, governance, financiering, competenties) worden expliciet meegenomen in het ontwerp, niet pas bedacht bij oplevering.

## Samenwerking en openheid

- **Samen ontwerpen — open boek** — Het domein is te groot en te complex voor één team. OKx werkt als open boek: zoek de fouten, deel ze, en doe constructieve verbetervoorstellen. Iedereen — leveranciers, instellingen, architecten, docenten — is welkom om mee te denken en bij te dragen. Alles via issues en PR's.
- **Levend document** — Uitgangspunten mogen worden aangescherpt naarmate OKx volwassener wordt. Wijzigingen gaan via **pull request** en, indien nodig, **ADR**.

---

## Gerelateerde documenten

- [Architectuurprincipes (AP01–AP13)](principes.md) — de stabiele, abstracte principes die richting geven
- [`CONTRIBUTING.md`](../../../../CONTRIBUTING.md) — workflow en governance
- [`doc/Bijdragen-voor-beginners.md`](../../../../doc/Bijdragen-voor-beginners.md) — praktische gids voor bijdragen
- [`architecture/agent-artifacts/README.md`](../../../agent-artifacts/README.md) — opslag voor agent-gegenereerde plannen en ontwerpen
- [`doc/Privacy-meetings-en-transcriptie.md`](../../../../doc/Privacy-meetings-en-transcriptie.md) — opname/transcriptie, AVG
- [`architecture/dr/`](../../../dr/) — Architecture Decision Records
- [MOSA-Visiedocument](MOSA-Visiedocument.md) — sectorarchitectuur voor sectorvoorzieningen in het mbo
- [MOSA vs OKx analyse](MOSA_vs_OKx_analyse.md) — overlap, verschillen en afleidbare principes
- [ADR 0006 — Consolidatie architectuurprincipes](../../../dr/0006-consolidatie-architectuurprincipes.md) — afwegingen achter de consolidatie en uitgangspunten
- [Edu-V Architectuurprincipes](https://edu-v.atlassian.net/wiki/spaces/AFSPRAKENS/pages/2031619/Architectuurprincipes) — referentiekader (met name principe D: Regie op gegevens)
