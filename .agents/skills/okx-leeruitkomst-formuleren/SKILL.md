---
name: okx-leeruitkomst-formuleren
description: Schrijf of beoordeel een leeruitkomst volgens het tuning model, met de taxonomie die bij het NLQF-niveau hoort. Gebruik deze skill zodra een leeruitkomst wordt opgesteld, herschreven of gereviewd, in mbo of hoger onderwijs.
---

# Een leeruitkomst formuleren

De vorm van een leeruitkomst is geen OKx-afspraak maar een landelijke norm. De [Handleiding Formuleren leeruitkomsten](https://nlqf.nl/wp-content/uploads/2025/06/Handleiding_Formuleren_leeruitkomsten_2020_NCP_NLQF_28122020.pdf) van het Nationaal Coordinatiepunt NLQF schrijft het tuning model voor. De onderbouwing met bronnen staat in [de vorm van een leeruitkomst](../../../architecture/docs/specificatie/begrippen/leeruitkomst-vorm/README.md).

## De vijf plekken

```
Actief werkwoord + Type + Onderwerp + Standaard + Context
```

| Plek | Wat erin hoort | Signaalwoorden |
|---|---|---|
| Actief werkwoord | Wat de lerende kan. Kies het met een taxonomie | een werkwoord, nooit twee |
| Type | Aan welke eindkwalificatie de leeruitkomst bijdraagt | ten behoeve van de kwalificatie |
| Onderwerp | Het deskundigheidsgebied waarop de handeling zich richt | |
| Standaard | Welke richtlijn, methodiek of norm gehanteerd wordt | volgens, aan de hand van, toetsbaar aan, op basis van, en met, onderbouwd met, geverifieerd bij |
| Context | De omgeving waarin de lerende het laat zien | in, bij, op, onder begeleiding |

Het voorbeeld uit de handleiding, met de reikwijdte erboven:

*Voor de kwalificatie operator productietechniek (NLQF niveau 2), technische module*

| Afstellen | Ten behoeve van de kwalificatie operator productietechniek | Apparatuur | Aan de hand van specificaties | In een mechanische omgeving |
|---|---|---|---|---|
| Actief ww | Type | Onderwerp | Standaard | Context |

## De taxonomie hangt af van het niveau

De handleiding kiest per niveau, en die keuze is geen smaak.

| NLQF | Taxonomie | Wat zij levert |
|---|---|---|
| 1 tot en met 4 | Romiszowski | Scheidt kennis van vaardigheden en dekt alle vaardigheidsdomeinen |
| 5 tot en met 8 | SOLO (Biggs) | Richt zich op het cognitieve domein, passend bij hogere niveaus |

Bloom wordt in de handleiding genoemd en terzijde gelegd ten gunste van SOLO. Gebruik Bloom dus niet als eerste keuze; wordt er toch naar gevraagd, zeg dan dat de handleiding SOLO aanbeveelt en waarom.

### De codes van Romiszowski

| Hoofdcategorie | Onderverdeling | Code |
|---|---|---|
| Feitelijke kennis | feiten, procedure | `Ff`, `Fp` |
| Begripsmatige kennis | begrip, principe | `Bb`, `Bp` |
| Reproductieve vaardigheid | cognitief, psychomotorisch, reactief, interactief | `Rc`, `Rpm`, `Rr`, `Ri` |
| Productieve vaardigheid | cognitief, psychomotorisch, reactief, interactief | `Pc`, `Ppm`, `Pr`, `Pi` |

Reproductief betekent weinig planning, herhaling en standaardprocedures. Productief betekent planning en creativiteit, zonder pasklare oplossing. Een leeruitkomst die hoger in het NLQF staat schuift van reproductief naar productief: "stelt af volgens specificaties" is `Rpm`, "bepaalt de juiste instellingen bij afwijkingen" is `Ppm`.

De vier domeinen: cognitief is denken, reactief is reageren op, psychomotorisch is handelen, interactief is communiceren.

## Werkwijze

1. Stel de reikwijdte vast: welke kwalificatie, welk NLQF-niveau, welke module of eenheid. Die staat boven de leeruitkomst, niet erin.
2. Kies de taxonomie op het niveau.
3. Kies het actieve werkwoord met die taxonomie. Een werkwoord per leeruitkomst.
4. Vul de vijf plekken in de voorgeschreven volgorde.
5. Draai de controle: `python3 scripts/keur-leeruitkomst.py <pad>`.
6. Loop de zes vragen na die een mens moet beantwoorden, hieronder.

## Het uitgangspunt van de instelling hoort in de standaard

Een instelling die duurzaam werken vooropstelt zet dat in de standaard en niet in het werkwoord: het ontwerp versterkt de biodiversiteit en verstoort de bestaande natuurwaarden niet. Een uitgangspunt is een criterium waarop het resultaat wordt beoordeeld, en daarmee toetsbaar. Als werkwoord zou het een aparte handeling suggereren die er niet is.

Dat is tevens de plek waar de begrippenfamilie `Onderwijskundig kader instelling` de leeruitkomst binnenkomt.

## Wat de controle niet doet

Het script toetst de vorm. Zes vragen uit de checklist van de handleiding vragen een menselijk oordeel en horen in de review:

1. Is het beroepsveld meegenomen bij het bepalen van thema en onderwerp.
2. Begrijpt de student wat er van hem wordt verwacht.
3. Past de gedetailleerdheid bij het niveau: kwalificatie, kerntaak of bouwsteen.
4. Past de omschreven context bij het NLQF-niveau van de kwalificatie.
5. Is de leeruitkomst haalbaar en in lijn met de professionele normen in de praktijk.
6. Zijn de leeruitkomsten van programma en module onderling in lijn.

## Valkuilen

| Valkuil | Waarom het misgaat |
|---|---|
| Twee werkwoorden in een leeruitkomst | De handleiding verbiedt het; twee handelingen horen twee leeruitkomsten te zijn |
| Het uitgangspunt van de instelling als werkwoord | Suggereert een handeling die er niet is, en maakt het ontoetsbaar |
| Bloom kiezen omdat die bekend is | De handleiding beveelt SOLO aan boven Bloom, met redenen |
| De taxonomie in de waarde zetten, zoals `bloom3` | Romiszowski kent twee assen; leg taxonomie en code als paar vast |
| Kwalificatie, niveau en herkomst in de zin proppen | Die horen in de reikwijdte erboven of als relatie in het model |
