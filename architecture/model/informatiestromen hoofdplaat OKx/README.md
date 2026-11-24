# Uitgebrachte versies van de informatiestromen hoofdplaat

Elke map hier draagt een uitgebrachte plaat. [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) haalt die versies aan, in de tekst als `hoofdplaat v1.7` en in bestandsnamen als `informatiestromen_hoofdplaat_v1_7.png`. Een versie die hier staat is daarmee een afspraak met de sector, niet een werkbestand.

De viewnamen in het ArchiMate-model dragen **geen** versie. Wie een plaatversie wil terugvinden, gaat daarom via [`bron/versiemanifest.json`](../bron/versiemanifest.json): per plaat en per versie het beeld, de modelstaat erachter en hoe hard die verwijzing is. Dat manifest dekt drie platen:

| Plaat | View | Waar de versies staan |
|---|---|---|
| hoofdplaat | `OKx hoofdplaat` | deze map, een map per versie |
| informatiemodel | `OKx informatiemodel` | `architecture/model/informatiemodel/`, de versie in de bestandsnaam |
| informatiemodel-oeapi | `OKx informatiemodel en mapping OEAPI` | idem |

Hieronder de hoofdplaat.

## De versies

| Versie | Beeld | Gemaakt met | Modelstaat |
|---|---|---|---|
| 1.1.0 | `1.1.0/hoofdplaat 1.1.jpg` | handmatig uit de lokale Archi van de modelleur | geen; deze versie heeft nooit een view in het model gehad |
| 1.2.0 | `1.2.0/hoofdplaat 1.2.jpg` | handmatig | geen |
| 1.3.0 | `1.3.0/hoofdplaat 1.3.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.3` |
| 1.4.0 | `1.4.0/hoofdplaat 1.4.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.4 <concept>` |
| 1.6.1 | `1.6.1/hoofdplaat 1.6a.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.6a<concept>` |
| 1.6.2 | `1.6.2/hoofdplaat 1.6b.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.6b<concept>` |
| 1.7.0 | `1.7.0/OKx hoofdplaat 1.7.jpg` | handmatig | nagemeten, view `OKx hoofdplaat v1.7<concept>` |
| 1.7.1 | `1.7.1/OKx hoofdplaat 1.7.1.png` | `exporteer-archimate-platen.py` uit het gecommitte model | vastgelegd bij export |
| **1.7.2** | `1.7.2/OKx hoofdplaat 1.7.2.png` | `exporteer-archimate-platen.py` uit het gecommitte model | vastgelegd bij export |

Versie 1.5 is nooit uitgebracht; die view bestond van 1 tot 26 mei 2026 in het model en is daarna vervangen door 1.6a en 1.6b. Die twee zijn als `1.6.1` en `1.6.2` opgenomen, want een letterversie wordt semver; zij stonden eerder samen in een map `1.6` en daardoor viel `1.6b` buiten het manifest.

**Elke mapnaam draagt drie delen**, want een letterversie wordt semver: `1.6a` en `1.6b` werden `1.6.1` en `1.6.2`, en `1.7` werd `1.7.0`. Versie 1.1 tot 1.4 zijn als `.0` gezet; zij dateren van voor die afspraak en hun patchnummer is nooit gebruikt. De naam van het beeld in de map blijft zoals het is uitgebracht, dus `1.6.1` draagt `hoofdplaat 1.6a.jpg`. Een versie in twee delen laat open of er nog een patch volgt, en een testgeval weigert haar daarom.

Public haalt de plaat nog aan als `hoofdplaat v1.7`, in de tekst en in bestandsnamen als `informatiestromen_hoofdplaat_v1_7.png`. Die kant loopt via #532 en vraagt een eigen pull request op Public.

Versie 1.7.2 bestaat niet. In de sessie van 4 november is afgesproken dat een `1.7b` die Niels in voorbereiding had `1.7.2` zou worden; die plaat is nog niet uitgebracht.

**Een map is een versie en draagt precies een beeld.** Staan er twee, dan weigert `maak-versiemanifest-plaat.py` in plaats van er een te kiezen, en een testgeval vangt het af.

## Tot 1.7 handmatig, vanaf 1.7.1 uit het gecommitte model

De platen tot en met 1.7 komen uit een handmatige export uit de lokale Archi van de modelleur. Die gelden als release: zij zijn uitgebracht en de sector verwijst ernaar. Maar zij zijn **niet uit hun modelstaat te herbouwen**, en dat is gemeten: hoofdplaat 1.7 is 2267 bij 861, terwijl een export uit precies die modelstaat 2276 bij 1113 geeft voor de volle view en 2241 bij 873 voor de view zonder contextapplicaties.

Daarom draagt elke versie het veld `reproduceerbaar`. Staat dat op `false`, dan zegt het manifest **welke modelstaat erbij hoort** en niet dat het beeld eruit te herbouwen is.

**Vanaf 1.7.1 komt elke plaat uit het centraal gecommitte model**, geexporteerd met Archi headless:

```bash
python3 tools/scripts/exporteer-archimate-platen.py \
  --view "OKx hoofdplaat" --uit "architecture/model/informatiestromen hoofdplaat OKx/<versie>/OKx hoofdplaat <versie>.png"
python3 tools/scripts/maak-versiemanifest-plaat.py --plaat hoofdplaat --schrijf --versie <versie>
```

Het manifest vult de commit van de export pas wanneer die gecommit is, dus de volgorde is: exporteren, committen, vastleggen.

## Een oude versie terugvinden

Sluit Archi eerst; hij houdt het bestand in geheugen en schrijft bij het opslaan zijn eigen versie er weer overheen.

```bash
git checkout <model_commit> -- architecture/model/model.archimate   # alleen het model
git restore architecture/model/model.archimate                      # en terug
```

De `model_commit` staat in het manifest. Of gebruik het commando [`modelversie`](../../../.cursor/commands/modelversie.md), dat de stappen en de valkuilen uitschrijft.

Dat de verwijzing klopt is na te meten: haal het model van die commit en bereken de hash van de genoemde view met `maak-versiemanifest-plaat.py`. Voor 1.3.0, 1.4.0, 1.6.1, 1.6.2 en 1.7.0 komt dan precies de hash uit het manifest terug.

## Controle in CI

`tools/tests/test_maak_versiemanifest_plaat.py` loopt mee in CI en faalt wanneer:

- een eigen viewnaam een versie draagt, want die hoort hier en niet in het model;
- twee views dezelfde naam dragen, want dan pakt elk script de eerste;
- een versie geen `MAJOR.MINOR.PATCH` is, of een commithash draagt die niet de volle veertig tekens heeft;
- de huidige view afwijkt van de hash van de huidige versie, dus de plaat loopt achter op het model;
- een versie een export noemt die niet bestaat;
- een versiemap twee beelden draagt, of een map geen regel in het manifest heeft;
- een plaat is gewijzigd en dezelfde versie opnieuw wordt vastgelegd: een gewijzigde plaat krijgt een nieuw nummer.
