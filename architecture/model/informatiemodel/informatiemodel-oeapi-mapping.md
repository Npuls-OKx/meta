# Informatiemodel OKx naast OEAPI v6

**Status.** Concept, versie v0.1 (plaatversie 20260909). Ter review binnen het OKx-team; daarna richting kerngroep techniek.

**Doel.** Laten zien waar het [informatiemodel van OKx](informatiemodel.md) de standaard OEAPI v6 raakt, en waar niet. Dit document beschrijft de plaat [OKx informatiemodel en mapping OEAPI v0.1.jpg](<OKx informatiemodel en mapping OEAPI v0.1.jpg>).

**Waarom apart.** In [Public#89](https://github.com/Npuls-OKx/Public/issues/89) is afgesproken met twee platen te werken: het OKx-model op zichzelf, en apart waar dat model de standaard raakt. Dat scheidt twee vragen die anders door elkaar lopen: klopt het model, en waar sluit het aan op OEAPI.

**Bron.** De tabellen worden gegenereerd uit het ArchiMate-model, uit de view `OKx informatiemodel en mapping OEAPI`, met `python3 scripts/genereer-informatiemodel-doc.py`. Er is niets van de plaat overgetypt.

## Wat de mapping zegt

De relatie is `Realization`: het OEAPI-object realiseert het OKx-objecttype. Dat is een richting die telt. OKx beschrijft wat er nodig is, OEAPI is de vorm waarin dat over de lijn gaat. Waar een OKx-objecttype geen OEAPI-tegenhanger heeft, betekent dat niet dat het objecttype niet nodig is, maar dat de standaard er nu geen vorm voor heeft.

## De mapping

<!-- gegenereerd:mapping -->
36 koppelingen tussen 36 OKx-objecttypen en OEAPI v6.

| OKx-objecttype | OEAPI v6 | Relatie |
|---|---|---|
| `Aanwezigheid` | `Attendance` | Realization |
| `Examengelegenheid` | `TestComponentOffering` | Realization |
| `Examengelegenheid resultaat` | `Result` | Realization |
| `Examengelegenheid verbintenis` | `TestComponentOfferingAssociation` | Realization |
| `Examenonderdeelspecificatie` | `TestComponent` | Realization |
| `Keuzedeel` | `Programme` | Realization |
| `Keuzedeel aanbod verbintenis` | `ProgrammeOfferingAssociation` | Realization |
| `Keuzedeel resultaat` | `Result` | Realization |
| `Keuzedeelaanbod` | `ProgrammeOffering` | Realization |
| `Keuzedeelruimte` | `Programme` | Realization |
| `Leergelegenheid` | `LearningComponentOffering` | Realization |
| `Leergelegenheid resultaat` | `Result` | Realization |
| `Leergelegenheid verbintenis` | `ComponentOfferingAssociation` | Realization |
| `Les specificatie` | `LearningComponent` | Realization |
| `Lesgelegenheid` | `LearningComponentOffering` | Realization |
| `Lesgelegenheid resultaat` | `Result` | Realization |
| `Lesgelegenheid verbintenis` | `ComponentOfferingAssociation` | Realization |
| `Onderwijseenheid aanbod` | `CourseOffering` | Realization |
| `Onderwijseenheid aanbod verbintenis` | `CourseOfferingAssociation` | Realization |
| `Onderwijseenheid resultaat` | `Result` | Realization |
| `Onderwijseenheid specificatie` | `Course` | Realization |
| `Opleiding aanbod  verbintenis` | `ProgrammeOfferingAssociation` | Realization |
| `Opleiding aanbod resultaat` | `Result` | Realization |
| `Opleidingaanbod` | `ProgrammeOffering` | Realization |
| `Opleidingspecificatie` | `Programme` | Realization |
| `Opleidingsprogramma aanbod` | `ProgrammeOffering` | Realization |
| `Opleidingsprogramma aanbod verbintenis` | `ProgrammeOfferingAssociation` | Realization |
| `Opleidingsprogramma resultaat` | `Result` | Realization |
| `Opleidingsprogramma specificatie` | `Programme` | Realization |
| `Persoon` | `Person` | Association |
| `Plaatsingsgroep` | `Group` | Realization |
| `Toetsgelegenheid` | `TestComponentOffering` | Realization |
| `Toetsgelegenheid resultaat` | `Result` | Realization |
| `Toetsgelegenheid verbintenis` | `TestComponentOfferingAssociation` | Realization |
| `Toetsonderdeel specificatie` | `TestComponent` | Realization |
| `leeronderdeel specificatie` | `LearningComponent` | Realization |
<!-- /gegenereerd -->

## Waar meerdere OKx-objecttypen op hetzelfde OEAPI-object uitkomen

Dit is de kern van de signalering: OKx onderscheidt op verschillende plaatsen iets dat OEAPI in een object samenvat.

<!-- gegenereerd:meervoudig -->
| OEAPI v6 | OKx-objecttypen |
|---|---|
| `ComponentOfferingAssociation` | `Leergelegenheid verbintenis`, `Lesgelegenheid verbintenis` |
| `LearningComponent` | `Les specificatie`, `leeronderdeel specificatie` |
| `LearningComponentOffering` | `Leergelegenheid`, `Lesgelegenheid` |
| `Programme` | `Keuzedeel`, `Keuzedeelruimte`, `Opleidingspecificatie`, `Opleidingsprogramma specificatie` |
| `ProgrammeOffering` | `Keuzedeelaanbod`, `Opleidingaanbod`, `Opleidingsprogramma aanbod` |
| `ProgrammeOfferingAssociation` | `Keuzedeel aanbod verbintenis`, `Opleiding aanbod  verbintenis`, `Opleidingsprogramma aanbod verbintenis` |
| `Result` | `Examengelegenheid resultaat`, `Keuzedeel resultaat`, `Leergelegenheid resultaat`, `Lesgelegenheid resultaat`, `Onderwijseenheid resultaat`, `Opleiding aanbod resultaat`, `Opleidingsprogramma resultaat`, `Toetsgelegenheid resultaat` |
| `TestComponent` | `Examenonderdeelspecificatie`, `Toetsonderdeel specificatie` |
| `TestComponentOffering` | `Examengelegenheid`, `Toetsgelegenheid` |
| `TestComponentOfferingAssociation` | `Examengelegenheid verbintenis`, `Toetsgelegenheid verbintenis` |
<!-- /gegenereerd -->

`Programme` en `ProgrammeOffering` dragen bij OKx vier tot vijf verschillende objecttypen. `Result` draagt elk resultaat, ongeacht niveau. Dat is werkbaar zolang het onderscheid ergens anders is vastgelegd, en het is precies het risico dat op de risicoslide van de AI-houdbaarheidspresentatie staat: als de eis alleen in OEAPI-vorm bestaat, is het onderscheid weg.

## Wat geen tegenhanger heeft

<!-- gegenereerd:zonder-tegenhanger -->
26 van de 62 objecttypen hebben geen OEAPI-tegenhanger op deze plaat.

| OKx-objecttype zonder OEAPI-tegenhanger |
|---|
| `Competenties / Skills` |
| `Examenonderdeel weging` |
| `Examenplan` |
| `Formatief resultaat` |
| `Formatieve beoordeling` |
| `Formatieve resultaat structuur` |
| `Inzicht` |
| `Kennis` |
| `Kerntaak` |
| `Kwalificatie` |
| `Kwalificatie dossier` |
| `Leeruitkomst` |
| `Medewerker` |
| `Opleidingsaanbod van Instelling` |
| `Persoonlijke ontwikkeling` |
| `Student` |
| `Student keuze regelset` |
| `Summatief Afrondingscriterium` |
| `Summatief resultaat` |
| `Summatieve beoordeling` |
| `Summatieve resultaat structuur` |
| `Toetsonderdeel weging` |
| `Vaardigheid` |
| `Verzoek tot Aanbod / Intekening op specificatie` |
| `Waarde document (diploma / certificaat)` |
| `Werkproces` |
<!-- /gegenereerd -->

De objecttypen zonder tegenhanger vallen in twee groepen: het kwalificatiekader met de onderwijskundige begrippen, en de hele resultaatstructuur.

Dat de resultaatstructuur er niet in zit, sluit aan op wat een leverancier in [meta#89](https://github.com/Npuls-OKx/meta/issues/89) opmerkte: in OEAPI zijn geen wegingen of samengestelde rekenmethoden over een lijst toetsen uit te drukken. Het model laat nu zien hoeveel dat precies is.

## Openstaande punten

| Punt | Issue |
|---|---|
| De mapping is nog niet op attribuutniveau; hij gaat over objecten | nog aan te maken |
| Voor de objecttypen zonder tegenhanger is nog niet vastgelegd of dat een signalering richting OEAPI wordt of een bewuste afwijking | #218 |
| De mapping is nog niet getoetst tegen de payload-specificaties in Public, die het logische niveau vormen | nog aan te maken |

Relateert aan: #163, #218
