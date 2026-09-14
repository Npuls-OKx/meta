# Informatiemodel OKx naast OEAPI v6

## Context

OKx sluit voor de technische uitwerking zoveel mogelijk aan op de Open Education API (OEAPI), versie 6. Dat kan alleen waar de standaard de begrippen van OKx ook kan dragen.

## Inleiding

Dit document legt het [informatiemodel](informatiemodel.md) naast OEAPI v6 en laat zien waar de standaard het model dekt, waar hij te grof dekt, en waar hij niet dekt. Versie v0.1, concept; de oordelen per objecttype zijn voorlopig tot de kerngroep techniek ze bekrachtigt.

## Doel

Per objecttype vaststellen of de standaard volstaat, aangepast moet worden, of bewust niet gevolgd wordt. De uitkomst bepaalt welke signaleringen richting de standaard gaan.

## Scope

De objecttypen van het informatiemodel, [MIM-niveau 2](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-2-conceptueel-informatiemodel), naast de objecten van OEAPI v6. OEAPI is een standaard voor gegevensuitwisseling: het logische model ervan is [niveau 3](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-3-logisch-informatie-of-gegevensmodel), de JSON-vorm en de endpoints zijn [niveau 4](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-4-fysiek-of-technisch-gegevens-of-datamodel). Dit document is de brug tussen niveau 2 en die twee. Attributen, datatypes en multipliciteit vallen hier buiten; die staan in het [logisch gegevensmodel en de schema's](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen) in Public.

![Informatiemodel OKx naast de mapping op OEAPI v6, versie v0.1 van 14 september 2026](<OKx informatiemodel en mapping OEAPI v0.1.jpg>)

## Notatie

De blauwe objecten zijn OEAPI v6 en staan als data-object in het model. Van de OKx-objecttypen zijn er 59 bedrijfsobject en 3 bedrijfsactor: `Persoon`, `Student` en `Medewerker`. Draagt één OEAPI-object meerdere OKx-objecttypen, dan staat het op de plaat bij elk van die objecttypen apart. De relatie is realisatie: het data-object is de vorm waarin een OKx-objecttype wordt uitgewisseld. Realisatie overbrugt lagen en komt daarom alleen hier voor. `Persoon` naar `Person` is de uitzondering, en dat volgt uit die typering: realisatie loopt naar een bedrijfsobject, niet naar een bedrijfsactor, dus daar is de relatie een associatie (association).

## Dekking door OEAPI v6

**Een OEAPI-object draagt vaak meerdere OKx-objecttypen.** `Programme` draagt vier specificatietypen, `ProgrammeOffering` drie aanbodtypen en `Result` zeven objecttypen binnen scope in de kolom Onderwijsresultaat (acht met `Lesgelegenheid resultaat`, dat buiten scope valt). De vijf andere objecttypen in die kolom hebben geen equivalent: `Aanwezigheid`, en de vier objecttypen voor formatieve en summatieve resultaten en beoordelingen. Het onderscheid tussen die OKx-objecttypen ligt dan in een typeveld van OEAPI waar dat uitbreidbaar is (`programmeType` en `associationState` zijn uitbreidbare opsommingen met het voorvoegsel `x-`), en anders buiten de standaard, in het logisch gegevensmodel en de schema's van OKx. `Result` is in OEAPI geen eigen resource maar een deel van een association of een attempt; een resultaat wordt dus via de verbintenis ontsloten.

**Voor het kwalificatiekader is nog geen equivalent geïdentificeerd.** Kwalificatiedossier, kwalificatie, kerntaak en werkproces zijn in de OpenAPI-specificatie van OEAPI v6 niet als object gevonden; de vraag hoe OEAPI een kwalificatiekader draagt ligt bij de kerngroep techniek. De leeruitkomst zelf heeft wel een equivalent: `LearningOutcome`, met eigen endpoints.

**De resultaatstructuur is nog niet op OEAPI gemapt.** OEAPI kent `weight` per resultaat, niet per specificatie; op het toetsonderdeel draagt het wel `passFrom` (cesuur), `resultValueType` (schaal), `attempts` en `parent` en `children` voor samengestelde toetsen, en op het resultaat `final` (vastgesteld door de examencommissie). Het afrondingscriterium over onderdelen heen bestaat er alleen als vrije tekst in `qualificationRequirements`. Wat ontbreekt is de weging per specificatie en de aggregatieregel; of de samenstelling van een summatieve structuur daarmee in OEAPI is uit te drukken is nog niet vastgesteld. OKx legt hem wel machineleesbaar vast, in [`result-structure.json`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/result-structure.json).

### Mapping per objecttype

Uit `informatiemodel.json`: de 35 realisaties en de associatie van `Persoon` naar `Person` op de plaat. Het oordeel is voorlopig en telt alleen objecttypen binnen scope: *volstaat* waar een OEAPI-object precies één OKx-objecttype binnen scope draagt, *te grof* waar het er meer draagt. De leslaag staat op de plaat maar valt buiten de uitwisseling; die rijen tellen niet mee.

| OKx-objecttype | Begrippenfamilie | OEAPI-object | Voorlopig oordeel |
|---|---|---|---|
| `Examengelegenheid` | Onderwijsaanbod | `TestComponentOffering` | te grof: draagt 2 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Examengelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Examengelegenheid verbintenis` | Onderwijsverbintenis | `TestComponentOfferingAssociation` | te grof: draagt 2 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Examenonderdeelspecificatie` | Onderwijsspecificatie | `TestComponent` | te grof: draagt 2 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Keuzedeel` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Keuzedeel aanbod verbintenis` | Onderwijsverbintenis | `ProgrammeOfferingAssociation` | te grof: draagt 3 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Keuzedeel resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Keuzedeelaanbod` | Onderwijsaanbod | `ProgrammeOffering` | te grof: draagt 3 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Keuzedeelruimte` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Leergelegenheid` | Onderwijsaanbod | `LearningComponentOffering` | volstaat |
| `Leergelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Leergelegenheid verbintenis` | Onderwijsverbintenis | `LearningComponentOfferingAssociation` | volstaat |
| `Leeronderdeel specificatie` | Onderwijsspecificatie | `LearningComponent` | volstaat |
| `Leeruitkomst` | Onderwijskundig kader instelling | `LearningOutcome` | volstaat |
| `Les specificatie` | Onderwijsspecificatie | `LearningComponent` | buiten scope: de leslaag valt buiten de uitwisseling |
| `Lesgelegenheid` | Onderwijsaanbod | `LearningComponentOffering` | buiten scope: de leslaag valt buiten de uitwisseling |
| `Lesgelegenheid resultaat` | Onderwijsresultaat | `Result` | buiten scope: de leslaag valt buiten de uitwisseling |
| `Lesgelegenheid verbintenis` | Onderwijsverbintenis | `LearningComponentOfferingAssociation` | buiten scope: de leslaag valt buiten de uitwisseling |
| `Onderwijseenheid aanbod` | Onderwijsaanbod | `CourseOffering` | volstaat |
| `Onderwijseenheid aanbod verbintenis` | Onderwijsverbintenis | `CourseOfferingAssociation` | volstaat |
| `Onderwijseenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Onderwijseenheid specificatie` | Onderwijsspecificatie | `Course` | volstaat |
| `Opleiding aanbod  verbintenis` | Onderwijsverbintenis | `ProgrammeOfferingAssociation` | te grof: draagt 3 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleiding aanbod resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleiding specificatie` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleidingaanbod` | Onderwijsaanbod | `ProgrammeOffering` | te grof: draagt 3 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma aanbod` | Onderwijsaanbod | `ProgrammeOffering` | te grof: draagt 3 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma aanbod verbintenis` | Onderwijsverbintenis | `ProgrammeOfferingAssociation` | te grof: draagt 3 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Opleidingsprogramma specificatie` | Onderwijsspecificatie | `Programme` | te grof: draagt 4 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Persoon` | buiten de kolommen | `Person` | volstaat |
| `Plaatsingsgroep` | buiten de kolommen | `Group` | volstaat |
| `Toetsgelegenheid` | Onderwijsaanbod | `TestComponentOffering` | te grof: draagt 2 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Toetsgelegenheid resultaat` | Onderwijsresultaat | `Result` | te grof: draagt 7 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Toetsgelegenheid verbintenis` | Onderwijsverbintenis | `TestComponentOfferingAssociation` | te grof: draagt 2 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |
| `Toetsonderdeel specificatie` | Onderwijsspecificatie | `TestComponent` | te grof: draagt 2 OKx-objecttypen binnen scope, het onderscheid ligt buiten de standaard |

### OKx-objecttypen zonder OEAPI-equivalent

Voor deze 21 objecttypen binnen scope is nog geen equivalent in OEAPI v6 geïdentificeerd. Per groep staat waarom, en wat het besluit vraagt: een signalering richting de standaard, of een bewuste afwijking.

| Groep | Objecttypen | Waarom geen equivalent | Besluit |
|---|---|---|---|
| Kwalificatiekader | `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces` | Nationale kaderstelling is in OEAPI geen object; de vraag hoe OEAPI een kwalificatiekader draagt ligt bij de kerngroep techniek | open |
| Resultaatstructuur | `Summatieve resultaat structuur`, `Formatieve resultaat structuur`, `Examenonderdeel weging`, `Toetsonderdeel weging`, `Summatief Afrondingscriterium` | OEAPI kent `weight` per resultaat en het afrondingscriterium alleen als vrije tekst; OKx legt de structuur vast in [`result-structure.json`](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/result-structure.json) | open |
| Onderwijsresultaat | `Summatief resultaat`, `Formatief resultaat`, `Summatieve beoordeling`, `Formatieve beoordeling` | `Result` in OEAPI hangt aan een association of attempt en heeft `final`, `pass`, `score` en `assessor` als velden; het onderscheid formatief of summatief en de beoordeling als eigen object kent OEAPI niet | open |
| Rollen | `Student`, `Medewerker` | OEAPI kent ze niet als object maar als `affiliations` op `Person` | open: rol als attribuut van `Person` volstaat mogelijk |
| Aanwezigheid | `Aanwezigheid` | OEAPI kent aanwezigheid alleen als attribuut op een association, niet als eigen object | open |
| Keuze en verzoek | `Student keuze regelset`, `Verzoek tot Aanbod / Intekening op specificatie` | Geen object in OEAPI voor de regelset (OKx legt die vast in `rule-set.json`) en voor het verzoek om nieuw aanbod te maken. Intekenen op bestaand aanbod kent OEAPI wel: een association met `state` `pending` of `queued` | open |
| Overig | `Opleidingsaanbod van Instelling`, `Waarde document (diploma / certificaat)`, `Persoonlijke ontwikkeling` | Geen object in OEAPI gevonden | open |

### OEAPI-objecten zonder OKx-objecttype

De omgekeerde dekking: objecten die OEAPI v6 wel kent en die op de plaat geen objecttype hebben. Per object of het bewust buiten scope valt of nog niet is gemodelleerd.

| OEAPI-object | Wat het draagt | Stand op de plaat |
|---|---|---|
| `Organisation` | De onderwijsaanbieder en zijn organisatie-eenheden, met `parent` en `root` | Nog niet gemodelleerd; ook in het logisch gegevensmodel alleen als `ORGANISATIE_EENHEID` |
| `AcademicSession` | Schooljaar en periode, waar een offering aan hangt | Nog niet gemodelleerd; de periode is op de plaat een kenmerk van het aanbod |
| `Group` en `Membership` | Een groep met leden, rol en status | `Plaatsingsgroep` is op `Group` gemapt; het lidmaatschap als eigen object ontbreekt |
| `TestComponentOfferingAssociationAttempt` | Een poging op een toetsonderdeel, met `attempt`, `opportunity`, `attendance` en een eigen `result` | Nog niet gemodelleerd: de plaat kent geen poging of herkansing als objecttype |

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](informatiemodel.md) | Het model zelf, zonder de standaard ernaast |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken de mapping uit tot attribuutniveau |
| [`informatiemodel.json`](informatiemodel.json) | De mapping machineleesbaar, gegenereerd uit `model.archimate` |
