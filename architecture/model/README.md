# ArchiMate-model

Het OKx **ArchiMate-model** (`model.archimate`) met o.a. de MOKA-koppelvlak-views en de bijbehorende informatiemodel-diagrammen. Te openen met [Archi](https://www.archimatetool.com/); `.bak` is een automatische back-up.

## Informatiemodel

De map [`informatiemodel/`](informatiemodel/) bevat de twee informatiemodelplaten met hun documentatie: het [informatiemodel](informatiemodel/informatiemodel.md), de [mapping naar OEAPI v6](informatiemodel/informatiemodel-oeapi-mapping.md) en [`informatiemodel.json`](informatiemodel/informatiemodel.json), dat met `python3 scripts/genereer-informatiemodel-doc.py` uit het model wordt gegenereerd. Draai dat script na elke wijziging aan een van beide views.

Deze documentatie en de [begrippenlijst](../docs/specificatie/begrippen/begrippenlijst.md) landen in Public in het releasepakket `Informatie-en-gegevensmodellen/` als laag 1 en 2. Meta is de bron; Public krijgt de release-variant via `python3 scripts/publiceer-informatiemodel.py --doel <Public-worktree>`. Het script zet de verwijzingen om naar paden binnen Public, pint wat in meta blijft op een commit, hernoemt de platen naar `img/` en faalt op een verwijzing die het niet kent, een entiteit in de brugtabel die niet in het logisch gegevensmodel staat, of een definitie die niet letterlijk in het kaderscenario van Public terug te vinden is. Met `--controleer` meldt het of Public nog gelijk loopt met meta. Exporteer de platen eerst met de hand uit Archi (het script leest de jpg's, het rendert ze niet).

## Valideren vóór commit

Het model is één XML-boom waarin views via **ID's** verwijzen naar elementen elders in het bestand. Raken die verwijzingen los, dan blijft het geldige XML — maar **Archi gooit de losgeraakte objecten bij de eerstvolgende save stilzwijgend weg**. In een diff van 5 MB zie je dat niet.

Draai daarom vóór elke commit:

```bash
python3 scripts/validate-archimate.py architecture/model/model.archimate
```

Controleert dode verwijzingen, dubbele id's en XML-welgevormdheid; exitcode ≠ 0 bij problemen.

## Nooit tekstueel mergen

Een `.archimate` mag **nooit** regelgebaseerd worden samengevoegd — niet door git, niet met de hand. `.gitattributes` dwingt dit af (`-merge`): git weigert het bestand te mergen en vraagt om een expliciete keuze voor één kant. De andere kant breng je terug via **Archi → File → Import → Another model into the selected model** (Archi merget op ID-niveau).

Volledige procedure: [ADR 0010](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0010-archimatemodel-werkafspraken.md).
