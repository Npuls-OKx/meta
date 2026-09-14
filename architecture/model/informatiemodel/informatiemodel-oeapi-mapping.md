# Informatiemodel OKx naast OEAPI v6

## Context

OKx sluit voor de technische uitwerking zoveel mogelijk aan op de Open Education API (OEAPI), versie 6. Dat kan alleen waar de standaard de begrippen van OKx ook kan dragen.

## Inleiding

Dit document legt het [informatiemodel](informatiemodel.md) naast OEAPI v6 en laat zien waar de standaard het model dekt, waar hij te grof dekt, en waar hij niet dekt. Versie v0.1, concept; de oordelen per objecttype zijn voorlopig tot de kerngroep techniek ze bekrachtigt.

## Doel

Per objecttype vaststellen of de standaard volstaat, aangepast moet worden, of bewust niet gevolgd wordt. De uitkomst bepaalt welke signaleringen richting de standaard gaan.

## Scope

De objecttypen van het informatiemodel, [MIM-niveau 2](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-2-conceptueel-informatiemodel), naast de objecten van OEAPI v6. OEAPI is een standaard voor gegevensuitwisseling: het logische model ervan is [niveau 3](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-3-logisch-informatie-of-gegevensmodel), de JSON-vorm en de endpoints zijn [niveau 4](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-4-fysiek-of-technisch-gegevens-of-datamodel). Dit document is de brug tussen niveau 2 en die twee. Attributen, datatypes en multipliciteit vallen hier buiten; die staan in de [datamodelschema's](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties/Datamodelschema%27s) in Public.

![Informatiemodel OKx naast de mapping op OEAPI v6, versie v0.1 van 9 september 2026](<OKx informatiemodel en mapping OEAPI v0.1.jpg>)

## Notatie

De blauwe objecten zijn OEAPI v6 en staan als data-object in het model. Van de OKx-objecttypen zijn er 59 bedrijfsobject en 3 bedrijfsactor: `Persoon`, `Student` en `Medewerker`. Draagt één OEAPI-object meerdere OKx-objecttypen, dan staat het op de plaat bij elk van die objecttypen apart. De relatie is realisatie: het data-object is de vorm waarin een OKx-objecttype wordt uitgewisseld. Realisatie overbrugt lagen en komt daarom alleen hier voor. `Persoon` naar `Person` is de uitzondering, en dat volgt uit die typering: realisatie loopt naar een bedrijfsobject, niet naar een bedrijfsactor, dus daar is de relatie een associatie.

## Dekking door OEAPI v6

**Een OEAPI-object draagt vaak meerdere OKx-objecttypen.** `Programme` draagt vier specificatietypen, `ProgrammeOffering` drie aanbodtypen en `Result` acht van de negen objecttypen in de kolom Onderwijsresultaat, alle behalve `Aanwezigheid`. Het onderscheid tussen die OKx-objecttypen ligt dan buiten de standaard, in de datamodelschema's van OKx.

**Voor het kwalificatiekader is nog geen equivalent geïdentificeerd.** Kwalificatiedossier, kwalificatie, kerntaak en werkproces zijn in de OpenAPI-specificatie van OEAPI v6 niet als object gevonden; de vraag hoe OEAPI een kwalificatiekader draagt ligt bij de kerngroep techniek. De leeruitkomst zelf heeft wel een equivalent: `LearningOutcome`, met eigen endpoints.

**De resultaatstructuur is nog niet op OEAPI gemapt.** OEAPI kent `weight` per resultaat, niet per specificatie, en het afrondingscriterium bestaat er alleen als vrije tekst in `qualificationRequirements`. Of de samenstelling van een summatieve structuur daarmee in OEAPI is uit te drukken is nog niet vastgesteld; op grond van deze twee punten lijkt het niet te kunnen. OKx legt hem wel machineleesbaar vast, in [`result-structure.json`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/result-structure.json).

### Mapping per objecttype

Uit `informatiemodel.json`, de 36 realisaties op de plaat. Het oordeel is voorlopig: *volstaat* waar een OEAPI-object precies één OKx-objecttype draagt, *te grof* waar het er meer draagt.

| OKx-objecttype | Begrippenfamilie | OEAPI-object | Voorlopig oordeel |
|---|---|---|---|
| `Examengelegenheid` | Onderwijsaanbod | `TestComponentOffering` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Keuzedeelaanbod` | Onderwijsaanbod | `ProgrammeOffering` | te grof: draagt 3 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Leergelegenheid` | Onderwijsaanbod | `LearningComponentOffering` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Lesgelegenheid` | Onderwijsaanbod | `LearningComponentOffering` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Onderwijseenheid aanbod` | Onderwijsaanbod | `CourseOffering` | volstaat |
| `Opleidingaanbod` | Onderwijsaanbod | `ProgrammeOffering` | te grof: draagt 3 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma aanbod` | Onderwijsaanbod | `ProgrammeOffering` | te grof: draagt 3 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Toetsgelegenheid` | Onderwijsaanbod | `TestComponentOffering` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Leeruitkomst` | Onderwijskundigkader instelling | `LearningOutcome` | volstaat |
| `Examengelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Keuzedeel resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Leergelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Lesgelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Onderwijseenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Opleiding aanbod resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Toetsgelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 8 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Examenonderdeelspecificatie` | Onderwijsspecificatie | `TestComponent` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Keuzedeel` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Keuzedeelruimte` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Leeronderdeel specificatie` | Onderwijsspecificatie | `LearningComponent` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Les specificatie` | Onderwijsspecificatie | `LearningComponent` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Onderwijseenheid specificatie` | Onderwijsspecificatie | `Course` | volstaat |
| `Opleiding specificatie` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma specificatie` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Toetsonderdeel specificatie` | Onderwijsspecificatie | `TestComponent` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Examengelegenheid verbintenis` | Onderwijsverbintenis | `TestComponentOfferingAssociation` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Keuzedeel aanbod verbintenis` | Onderwijsverbintenis | `ProgrammeOfferingAssociation` | te grof: draagt 3 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Leergelegenheid verbintenis` | Onderwijsverbintenis | `LearningComponentOfferingAssociation` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Lesgelegenheid verbintenis` | Onderwijsverbintenis | `LearningComponentOfferingAssociation` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Onderwijseenheid aanbod verbintenis` | Onderwijsverbintenis | `CourseOfferingAssociation` | volstaat |
| `Opleiding aanbod  verbintenis` | Onderwijsverbintenis | `ProgrammeOfferingAssociation` | te grof: draagt 3 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma aanbod verbintenis` | Onderwijsverbintenis | `ProgrammeOfferingAssociation` | te grof: draagt 3 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Toetsgelegenheid verbintenis` | Onderwijsverbintenis | `TestComponentOfferingAssociation` | te grof: draagt 2 OKx-objecttypen, het onderscheid ligt buiten de standaard |
| `Persoon` | buiten de kolommen | `Person` | volstaat |
| `Plaatsingsgroep` | buiten de kolommen | `Group` | volstaat |

### OKx-objecttypen zonder OEAPI-equivalent

Voor deze 21 objecttypen binnen scope is nog geen equivalent in OEAPI v6 geïdentificeerd. Per groep staat waarom, en wat het besluit vraagt: een signalering richting de standaard, of een bewuste afwijking.

| Groep | Objecttypen | Waarom geen equivalent | Besluit |
|---|---|---|---|
| Kwalificatiekader | `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces` | Nationale kaderstelling is in OEAPI geen object; de vraag hoe OEAPI een kwalificatiekader draagt ligt bij de kerngroep techniek | open |
| Resultaatstructuur | `Summatieve resultaat structuur`, `Formatieve resultaat structuur`, `Examenonderdeel weging`, `Toetsonderdeel weging`, `Summatief Afrondingscriterium`, `Summatief resultaat`, `Formatief resultaat`, `Summatieve beoordeling`, `Formatieve beoordeling` | OEAPI kent `weight` per resultaat en het afrondingscriterium alleen als vrije tekst; OKx legt de structuur vast in [`result-structure.json`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/result-structure.json) | open |
| Rollen | `Student`, `Medewerker` | OEAPI kent ze niet als object maar als `affiliations` op `Person` | open: rol als attribuut van `Person` volstaat mogelijk |
| Aanwezigheid | `Aanwezigheid` | OEAPI kent aanwezigheid alleen als attribuut op een association, niet als eigen object | open |
| Keuze en verzoek | `Student keuze regelset`, `Verzoek tot Aanbod / Intekening op specificatie` | Geen object in OEAPI; OKx legt de regelset vast in `rule-set.json` | open |
| Overig | `Opleidingsaanbod van Instelling`, `Waarde document (diploma / certificaat)`, `Persoonlijke ontwikkeling` | Geen object in OEAPI gevonden | open |

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](informatiemodel.md) | Het model zelf, zonder de standaard ernaast |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken de mapping uit tot attribuutniveau |
| [`informatiemodel.json`](informatiemodel.json) | De mapping machineleesbaar, gegenereerd uit `model.archimate` |
