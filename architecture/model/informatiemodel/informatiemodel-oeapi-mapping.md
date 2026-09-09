# Informatiemodel OKx naast OEAPI v6

Dezelfde objecttypen als in het [informatiemodel](informatiemodel.md), met OEAPI v6 ernaast gelegd. Doel: zichtbaar maken waar de standaard het model dekt en waar niet, zodat de kerngroep techniek kan besluiten wat een signalering richting OEAPI wordt en wat een bewuste afwijking blijft. Twee platen in plaats van een, zodat de vraag of het model klopt niet door de vraag loopt of het op de standaard past.

![Informatiemodel OKx naast de mapping op OEAPI v6](<OKx informatiemodel en mapping OEAPI v0.1.jpg>)

## Viewpoint

| | |
|---|---|
| **Voor wie** | Kerngroep techniek, technische werkgroep OEAPI, leveranciers |
| **Doel** | Besluiten. Per objecttype vaststellen of de standaard volstaat, aangepast moet worden, of bewust niet gevolgd wordt |
| **Vraag die het beantwoordt** | Waar dekt OEAPI v6 het OKx-model, waar dekt het te grof, en waar dekt het niet |
| **Scope** | Objectniveau. Attribuutniveau volgt in de payload-specificaties |

De blauwe objecten zijn OEAPI v6. De relatie is realisatie: het OEAPI-object realiseert het OKx-objecttype. OKx beschrijft wat er nodig is, OEAPI is de vorm waarin dat over de lijn gaat.

## Wat de mapping laat zien

**Eén OEAPI-object draagt vaak meerdere OKx-objecttypen.** `Programme` draagt de opleidingsspecificatie, de opleidingsprogrammaspecificatie, het keuzedeel en de keuzedeelruimte. `ProgrammeOffering` draagt drie aanbodtypen, `Result` draagt elk resultaat ongeacht niveau. Dat werkt zolang het onderscheid ergens anders vastligt; ligt het alleen in OEAPI vast, dan is het weg.

**Het kwalificatiekader heeft geen tegenhanger.** Kwalificatiedossier, kwalificatie, kerntaak, werkproces en de onderwijskundige begrippen komen in OEAPI niet voor. Dat is te verwachten: het is nationale kaderstelling, geen uitwisselbaar aanbod.

**De resultaatstructuur heeft geen tegenhanger.** Wegingen, afrondingscriteria en de samenstelling van een summatieve structuur zijn in OEAPI niet uit te drukken. Dat sluit aan op wat een leverancier meldde bij het modelleren van onderwijsaanbod in OOAPI: samengestelde rekenmethoden over een lijst toetsen pasten niet.

De volledige mapping staat machineleesbaar in [`informatiemodel.json`](informatiemodel.json), onder `oeapi_mapping`.

## Verwante documenten

| Document | Verhouding |
|---|---|
| [Informatiemodel OKx](informatiemodel.md) | Het model zelf, zonder de standaard ernaast |
| [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) | Werken de mapping uit tot attribuutniveau |
