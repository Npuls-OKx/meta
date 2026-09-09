# Informatiemodel OKx naast OEAPI v6

## Context

OKx sluit voor de technische uitwerking zoveel mogelijk aan op de Open Onderwijs API (OEAPI). Dat kan alleen waar de standaard de begrippen van OKx ook kan dragen.

## Inleiding

Dit document legt het [informatiemodel](informatiemodel.md) naast OEAPI v6 en laat zien waar de standaard het model dekt, waar hij te grof dekt, en waar hij niet dekt.

## Doel

Per objecttype vaststellen of de standaard volstaat, aangepast moet worden, of bewust niet gevolgd wordt. De uitkomst bepaalt welke signaleringen richting de standaard gaan.

## Scope

Objectniveau. Attributen liggen in de payload-specificaties.

![Informatiemodel OKx naast de mapping op OEAPI v6, versie v0.1 van 9 september 2026](<OKx informatiemodel en mapping OEAPI v0.1.jpg>)

## Notatie

De blauwe objecten zijn OEAPI v6. De relatie is realisatie: OEAPI is de vorm waarin een OKx-objecttype over de lijn gaat. `Persoon` naar `Person` is de uitzondering, daar is de relatie een associatie.

## Dekking door OEAPI v6

**Eén OEAPI-object draagt vaak meerdere OKx-objecttypen.** Het onderscheid tussen die objecttypen moet daarom buiten OEAPI vastliggen; de standaard draagt het niet.

**Het kwalificatiekader heeft geen tegenhanger.** Kwalificatiedossier, kwalificatie, kerntaak, werkproces en de onderwijskundige begrippen komen in OEAPI niet voor. Nationale kaderstelling is geen uitwisselbaar aanbod.

**De resultaatstructuur heeft geen tegenhanger.** Wegingen, afrondingscriteria en de samenstelling van een summatieve structuur zijn in OEAPI niet uit te drukken.

De volledige mapping staat in [`informatiemodel.json`](informatiemodel.json), onder `oeapi_mapping`.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](informatiemodel.md) | Het model zelf, zonder de standaard ernaast |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken de mapping uit tot attribuutniveau |
| [`informatiemodel.json`](informatiemodel.json) | De mapping machineleesbaar, gegenereerd uit `model.archimate` |
