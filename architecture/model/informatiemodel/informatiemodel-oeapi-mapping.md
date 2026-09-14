# Informatiemodel OKx naast OEAPI v6

## Context

OKx sluit voor de technische uitwerking zoveel mogelijk aan op de Open Onderwijs API (OEAPI). Dat kan alleen waar de standaard de begrippen van OKx ook kan dragen.

## Inleiding

Dit document legt het [informatiemodel](informatiemodel.md) naast OEAPI v6 en laat zien waar de standaard het model dekt, waar hij te grof dekt, en waar hij niet dekt.

## Doel

Per objecttype vaststellen of de standaard volstaat, aangepast moet worden, of bewust niet gevolgd wordt. De uitkomst bepaalt welke signaleringen richting de standaard gaan.

## Scope

De objecttypen van het informatiemodel, [MIM-niveau 2](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-2-conceptueel-informatiemodel), naast de objecten van OEAPI v6. OEAPI is een standaard voor gegevensuitwisseling en hoort daarmee op [niveau 3](https://docs.geostandaarden.nl/mim/mim/#beschouwingsniveau-3-logisch-informatie-of-gegevensmodel); dit document is de brug tussen die twee niveaus. Attributen, datatypes en multipliciteit vallen hier buiten; die staan in de [datamodelschema's](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties/Datamodelschema%27s) in Public.

![Informatiemodel OKx naast de mapping op OEAPI v6, versie v0.1 van 9 september 2026](<OKx informatiemodel en mapping OEAPI v0.1.jpg>)

## Notatie

De blauwe objecten zijn OEAPI v6 en staan als data-object in het model. Van de OKx-objecttypen zijn er 61 bedrijfsobject en 3 bedrijfsactor: `Persoon`, `Student` en `Medewerker`. De relatie is realisatie: het data-object is de vorm waarin een OKx-objecttype over de lijn gaat. Dat is ook de enige plek in dit model waar realisatie voorkomt, want realisatie overbrugt lagen en loopt niet tussen twee bedrijfsobjecten. `Persoon` naar `Person` is de uitzondering, en dat volgt uit die typering: realisatie loopt naar een bedrijfsobject, niet naar een bedrijfsactor, dus daar is de relatie een associatie.

## Dekking door OEAPI v6

**Een OEAPI-object draagt vaak meerdere OKx-objecttypen.** `Programme` draagt vier specificatietypen, `ProgrammeOffering` drie aanbodtypen en `Result` acht van de negen objecttypen in de kolom Onderwijsresultaat, alle behalve `Aanwezigheid`. OEAPI kent daarnaast wel niveau-specifieke varianten van `Result`, maar het onderscheid tussen de OKx-objecttypen moet buiten de standaard vastliggen.

**Voor het kwalificatiekader is nog geen equivalent geïdentificeerd.** Kwalificatiedossier, kwalificatie, kerntaak en werkproces zijn in de OpenAPI-specificatie van OEAPI v6 niet als object gevonden; de vraag hoe OEAPI een kwalificatiekader draagt ligt bij de kerngroep techniek. De leeruitkomst zelf heeft wel een equivalent: `LearningOutcome`, met eigen endpoints.

**De resultaatstructuur is nog niet op OEAPI gemapt.** OEAPI kent `weight` per resultaat, niet per specificatie, en het afrondingscriterium bestaat er alleen als vrije tekst in `qualificationRequirements`. Of de samenstelling van een summatieve structuur daarmee in OEAPI is uit te drukken is nog niet vastgesteld; op grond van deze twee punten lijkt het niet te kunnen. OKx legt hem wel machineleesbaar vast, in [`result-structure.json`](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties/Datamodelschema%27s).

### OKx-objecttypen zonder OEAPI-equivalent

Voor deze objecttypen binnen scope is nog geen equivalent in OEAPI v6 geïdentificeerd. Per objecttype volgt een besluit: een signalering richting de standaard, of een bewuste afwijking.

| OKx-objecttype |
|---|
| `Aanwezigheid` |
| `Examenonderdeel weging` |
| `Formatief resultaat` |
| `Formatieve beoordeling` |
| `Formatieve resultaat structuur` |
| `Kerntaak` |
| `Kwalificatie` |
| `Kwalificatie dossier` |
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
| `Verzoek tot Aanbod / Intekening op specificatie` |
| `Waarde document (diploma / certificaat)` |
| `Werkproces` |

`Aanwezigheid` staat hier omdat OEAPI aanwezigheid alleen als attribuut op een association kent en niet als eigen object.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](informatiemodel.md) | Het model zelf, zonder de standaard ernaast |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken de mapping uit tot attribuutniveau |
| [`informatiemodel.json`](informatiemodel.json) | De mapping machineleesbaar, gegenereerd uit `model.archimate` |
