# Informatiemodel OKx naast OEAPI v6

## Context

OKx sluit voor de technische uitwerking zoveel mogelijk aan op de Open Onderwijs API (OEAPI). Dat kan alleen waar de standaard de begrippen van OKx ook kan dragen.

## Inleiding

Dit document legt het [informatiemodel](informatiemodel.md) naast OEAPI v6 en laat zien waar de standaard het model dekt, waar hij te grof dekt, en waar hij niet dekt.

## Doel

Per objecttype vaststellen of de standaard volstaat, aangepast moet worden, of bewust niet gevolgd wordt. De uitkomst bepaalt welke signaleringen richting de standaard gaan.

## Scope

Objectniveau. Attributen, datatypes en multipliciteit liggen in de payload-specificaties en vallen hier buiten.

![Informatiemodel OKx naast de mapping op OEAPI v6, versie v0.1 van 9 september 2026](<OKx informatiemodel en mapping OEAPI v0.1.jpg>)

## Notatie

De blauwe objecten zijn OEAPI v6 en staan als data-object in het model. Van de OKx-objecttypen zijn er 61 bedrijfsobject en 3 bedrijfsactor: `Persoon`, `Student` en `Medewerker`. De relatie is realisatie: het data-object is de vorm waarin een OKx-objecttype over de lijn gaat. Dat is ook de enige plek in dit model waar realisatie voorkomt, want realisatie overbrugt lagen en loopt niet tussen twee bedrijfsobjecten. `Persoon` naar `Person` is de uitzondering, en dat volgt uit die typering: realisatie loopt naar een bedrijfsobject, niet naar een bedrijfsactor, dus daar is de relatie een associatie.

## Dekking door OEAPI v6

**Een OEAPI-object draagt vaak meerdere OKx-objecttypen.** `Programme` draagt vier specificatietypen, `ProgrammeOffering` drie aanbodtypen en `Result` acht van de negen objecttypen in de kolom Onderwijsresultaat, alle behalve `Aanwezigheid`. OEAPI kent daarnaast wel niveau-specifieke varianten van `Result`, maar het onderscheid tussen de OKx-objecttypen moet buiten de standaard vastliggen.

**Het kwalificatiekader heeft geen tegenhanger.** Kwalificatiedossier, kwalificatie, kerntaak en werkproces komen in OEAPI niet voor. Nationale kaderstelling is geen uitwisselbaar aanbod. De leeruitkomst zelf heeft die tegenhanger wel: `LearningOutcome`, met eigen endpoints.

**De resultaatstructuur is nog niet op OEAPI gemapt.** OEAPI kent `weight` per resultaat, niet per specificatie, en het afrondingscriterium bestaat er alleen als vrije tekst in `qualificationRequirements`. Of de samenstelling van een summatieve structuur daarmee in OEAPI is uit te drukken is nog niet vastgesteld; op grond van deze twee punten lijkt het niet te kunnen. OKx legt hem wel machineleesbaar vast, in [`result-structure.json`](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties/Datamodelschema%27s).

### Objecttypen binnen scope zonder tegenhanger

Deze objecttypen binnen scope hebben geen OEAPI-object. Per objecttype is een besluit nodig: signalering richting de standaard, of bewuste afwijking.

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
