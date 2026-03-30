# Changelog

Alle belangrijke wijzigingen in deze repository worden hier beschreven.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.1.0/),
en dit project volgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.1] — 2026-03-30

Eerste **getagde baseline** van de OKx-meta **publieke knowledge base**: documentatie, ADR’s, ArchiMate-model, meetings en koppelvlakartefacten. Geen “afgerond product”; wel een reproduceerbare snapshot voor sector en leveranciers. Als input voor de leveranciersbrief in de week van 30-03-26.

### Toegevoegd

- **ADR’s (Architecture Decision Records)** in `architecture/dr/`: o.a. publieke repo en samenwerkingsmodel, prioriteitsketen curriculum–onderwijscatalogus en drielagen-fundament, domeinprincipes student kiest en leeruitkomsten, leeruitkomsten met SBU/EC als logistieke containergrootte, Student Keuze Systeem (SKS) als zelfstandige referentiecomponent.
- **Documentatie** in `doc/`: o.a. projectoverzicht met hoofdplaat informatiestromen, ketenconcept informatiestromen, ArchiMate/MOKA-view uitleg, architectuurbesluiten en impact, bijdragen voor beginners, privacy bij meetings.
- **Meetings** onder `architecture/meetings/`: o.a. kernteam (o.a. voorbereiding leverancierssessie, student kiest/flexibel), SI-afstemming, BPMN uit architectuurmapping-sessies.
- **Koppelvlak- en standaard-artefacten**: MOKA/OKE-uitwerkingen, definitiemapping MORA–OEAPI (Excel/documentatie), product-/PDF-omschrijving waar van toepassing.
- **Cursor-commands** onder `.cursor/commands/` (o.a. ADR opstellen, release notes, commit message).

### Gewijzigd

- **README** en **CONTRIBUTING**: welkom-sectie “waar we nu mee bezig zijn”, keten- en MOKA-context, links naar hoofdplaat en ADR’s.
- **ArchiMate-model** (`architecture/model/model.archimate`): opschoning en structuur (o.a. data-objecten, functies, services in modelboom), views en objecten bijgewerkt in lijn met review en issues.
- **Governance**: workflow en repo-indeling verduidelijkt; verwijzingen naar issues en PR’s.

### Technische en overige notities

- Diverse **merge commits** van community-PR’s (GitHub); details staan in de git-historie en gekoppelde issues.

[Unreleased]: https://github.com/Npuls-OKx/meta/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/Npuls-OKx/meta/releases/tag/v0.0.1
