# Organisatie-eenheid en locatie in de keuzeregels

Tekenopdracht voor het informatiemodel, met het voorbeeld dat erbij hoort. Hoort bij [Public #114](https://github.com/Npuls-OKx/Public/issues/114) en de werkbrief [#332](https://github.com/Npuls-OKx/meta/issues/332), en bij de eisen R18 en R19 in [keuze-requirements.md](keuze-requirements.md).

## Waar het vandaan komt

Jan Hendrik van Schaik, vanuit Xedule, op de reviewronde van het informatiemodel:

> Locatie en organisatie eenheid kunnen een rol spelen bij kiezen van onderwijs. Een keuzedeel van Vista in Heerlen, zal niet zo snel door een student in Sittard worden gekozen. Ook bij Firda weet ik dat afstand een rol speelt in keuze proces. LOCATIE doet er dus toe.
>
> Verder is het ook zo dat keuzes soms beperkt zijn tot keuzedelen van het zelfde domein of sector, wat gemapt kan worden op ORGANISATIEEENHEID

Met een kanttekening die net zo zwaar weegt:

> Locaties zijn in Xedule in planning wat lastiger af te leiden dan in de roosters. Een geroosterde les heeft een ruimte toegewezen gekregen die aan een faciliteitlocatie kan zijn gekoppeld (niet verplicht). In de planfase zie je soms aan de groepscodering op welke locatie aanbod plaats zal vinden.

## Wat het model nu draagt

Geen van beide. De 66 objecttypen kennen geen `Organisatie-eenheid` en geen `Locatie`. De enige voorwaarde die de plaat vandaag kent loopt via de leeruitkomst:

```text
Leeruitkomst  --voorwaarde op-->  Student keuze regelset
```

Die vorm is het aanknopingspunt: een factor die een keuze beperkt, hangt met `voorwaarde op` aan de regelset.

## Het voorstel

Twee objecttypen erbij, elk met dezelfde relatievorm naar de regelset, en elk verankerd op de plek waar hun waarde ontstaat.

| Objecttype | Kolom | Scope | Waarom daar |
|---|---|---|---|
| `Organisatie-eenheid` | geen kolom, zoals `Medewerker` en `Plaatsingsgroep` | binnen | Snijdt door de families heen: een specificatie valt eronder, een aanbod ook, en een medewerker hoort erbij |
| `Locatie` | geen kolom | binnen | Idem, en zij hangt aan het aanbod in plaats van aan de specificatie |

Relaties:

```text
Organisatie-eenheid  --voorwaarde op-->   Student keuze regelset
Locatie              --voorwaarde op-->   Student keuze regelset

Opleidingsprogramma specificatie  --valt onder-->  Organisatie-eenheid
Opleidingsprogramma aanbod        --vindt plaats op-->  Locatie
```

De eerste twee maken de factor evalueerbaar in een regel. De laatste twee zeggen waar de waarde vandaan komt, en daarmee wanneer zij bekend is.

## Het verschil dat ertoe doet

De twee factoren lijken op elkaar en zijn het niet.

| | Organisatie-eenheid | Locatie |
|---|---|---|
| Hangt aan | de specificatie | het aanbod |
| Hard vanaf | het ontwerp van de opleiding | het toewijzen van een ruimte bij het roosteren |
| Regel evalueerbaar | voordat er aanbod is | pas betrouwbaar als het rooster er is |
| Daarvoor | niet van toepassing, de waarde staat al vast | de regel filtert op een voornemen, of filtert nog niet |

Dat laatste is wat R19 afdwingt: een locatieregel zegt zelf welk van de twee geldt. Zonder die uitspraak krijgt een student in de keuzefase een lijst die op het rooster anders blijkt te zijn.

## Voorbeeld

Vista heeft vestigingen in Heerlen en Sittard, en Jochem volgt Apothekersassistent in het domein Zorg en Welzijn.

```text
regel 1   organisatie-eenheid = domein van de opleiding van de student
          -> Jochem ziet de keuzedelen van Zorg en Welzijn, niet die van Techniek
          -> evalueerbaar in de keuzefase, want het domein ligt vast bij de specificatie

regel 2   locatie binnen 25 km van de vestiging van de student
          -> Jochem in Sittard ziet Ruimtelijk inzicht in Heerlen als voorlopig
          -> hard zodra de ruimte is toegewezen; daarvoor draagt de uitkomst
             de status voorlopig
```

Regel 1 verkleint de lijst voordat de student hem ziet. Regel 2 kleurt de lijst en sluit niets uit zolang de locatie een voornemen is.

## Wat de modelleur tekent

In Archi, op de plaat van het informatiemodel:

1. `Organisatie-eenheid` als objecttype, zonder kolom, scope binnen, in dezelfde vormtaal als `Plaatsingsgroep`.
2. `Locatie` als objecttype, zonder kolom, scope binnen.
3. `Organisatie-eenheid --voorwaarde op--> Student keuze regelset`, zoals de bestaande relatie vanaf `Leeruitkomst`.
4. `Locatie --voorwaarde op--> Student keuze regelset`.
5. `Opleidingsprogramma specificatie --valt onder--> Organisatie-eenheid`.
6. `Opleidingsprogramma aanbod --vindt plaats op--> Locatie`.

Na het tekenen: `python3 scripts/validate-archimate.py`, daarna de export verversen zodat `informatiemodel.json` de twee objecttypen draagt.

## Wat hierna nog volgt

Het logisch gegevensmodel draagt de velden die bij deze twee objecttypen horen. Dat model staat in [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104) en is nog niet gemerged, dus dat deel volgt als eigen pull request op Public.
