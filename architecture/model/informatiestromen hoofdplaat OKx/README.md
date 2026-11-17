# Uitgebrachte versies van de informatiestromen hoofdplaat

Elke map hier draagt een uitgebrachte plaat. [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) haalt die versies aan, in de tekst als `hoofdplaat v1.7` en in bestandsnamen als `informatiestromen_hoofdplaat_v1_7.png`. Een versie die hier staat is daarmee een afspraak met de sector, niet een werkbestand.

De viewnamen in het ArchiMate-model dragen **geen** versie. Wie een plaatversie wil terugvinden, gaat daarom via [`versiemanifest.json`](versiemanifest.json): per versie het beeld, de modelstaat erachter en hoe hard die verwijzing is.

## De versies

| Versie | Beeld | Gemaakt met | Modelstaat |
|---|---|---|---|
| 1.1 | `1.1/hoofdplaat 1.1.jpg` | handmatig uit de lokale Archi van de modelleur | geen; deze versie heeft nooit een view in het model gehad |
| 1.2 | `1.2/hoofdplaat 1.2.jpg` | handmatig | geen |
| 1.3 | `1.3/hoofdplaat 1.3.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.3` |
| 1.4 | `1.4/hoofdplaat 1.4.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.4 <concept>` |
| 1.6 | `1.6/hoofdplaat 1.6a.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.6a<concept>` |
| 1.7 | `1.7/OKx hoofdplaat 1.7.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.7<concept>` |
| **1.7.1** | `1.7.1/OKx hoofdplaat 1.7.1.png` | `exporteer-archimate-platen.py` uit het gecommitte model | vastgelegd bij export |

Versie 1.5 is nooit uitgebracht; die view bestond van 1 tot 26 mei 2026 in het model en is daarna vervangen door 1.6a en 1.6b.

## Tot 1.7 handmatig, vanaf 1.7.1 uit het gecommitte model

De platen tot en met 1.7 komen uit een handmatige export uit de lokale Archi van de modelleur. Die gelden als release: zij zijn uitgebracht en de sector verwijst ernaar. Maar zij zijn **niet uit hun modelstaat te herbouwen**, en dat is gemeten: hoofdplaat 1.7 is 2267 bij 861, terwijl een export uit precies die modelstaat 2276 bij 1113 geeft voor de volle view en 2241 bij 873 voor de view zonder contextapplicaties.

Daarom draagt elke versie het veld `reproduceerbaar`. Staat dat op `false`, dan zegt het manifest **welke modelstaat erbij hoort** en niet dat het beeld eruit te herbouwen is.

**Vanaf 1.7.1 komt elke plaat uit het centraal gecommitte model**, geexporteerd met Archi headless:

```bash
python3 tools/scripts/exporteer-archimate-platen.py \
  --view "OKx hoofdplaat" --uit "architecture/model/informatiestromen hoofdplaat OKx/<versie>/OKx hoofdplaat <versie>.png"
python3 tools/scripts/maak-versiemanifest-plaat.py --schrijf --versie <versie>
```

Het manifest vult de commit van de export pas wanneer die gecommit is, dus de volgorde is: exporteren, committen, vastleggen.

## Een oude versie terugvinden

Sluit Archi eerst; hij houdt het bestand in geheugen en schrijft bij het opslaan zijn eigen versie er weer overheen.

```bash
git checkout <model_commit> -- architecture/model/model.archimate   # alleen het model
git restore architecture/model/model.archimate                      # en terug
```

De `model_commit` staat in het manifest. Of gebruik het commando [`modelversie`](../../../.cursor/commands/modelversie.md), dat de stappen en de valkuilen uitschrijft.

Dat de verwijzing klopt is na te meten: haal het model van die commit en bereken de hash van de genoemde view met `maak-versiemanifest-plaat.py`. Voor 1.3, 1.4, 1.6 en 1.7 komt dan precies de hash uit het manifest terug.

## Wat de poort afdwingt

`tools/tests/test_maak_versiemanifest_plaat.py` loopt mee in CI en faalt wanneer:

- een eigen viewnaam een versie draagt, want die hoort hier en niet in het model;
- twee views dezelfde naam dragen, want dan pakt elk script de eerste;
- het manifest een versie draagt zonder volledige commithash van veertig tekens;
- de huidige view afwijkt van de hash van de huidige versie, dus de plaat loopt achter op het model;
- een versie een export noemt die niet bestaat.
