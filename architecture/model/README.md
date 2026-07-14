# ArchiMate-model

Het OKx **ArchiMate-model** (`model.archimate`) met o.a. de MOKA-koppelvlak-views en de bijbehorende informatiemodel-diagrammen. Te openen met [Archi](https://www.archimatetool.com/); `.bak` is een automatische back-up.

## Valideren vóór commit

Het model is één XML-boom waarin views via **ID's** verwijzen naar elementen elders in het bestand. Raken die verwijzingen los, dan blijft het geldige XML — maar **Archi gooit de losgeraakte objecten bij de eerstvolgende save stilzwijgend weg**. In een diff van 5 MB zie je dat niet.

Draai daarom vóór elke commit:

```bash
python3 scripts/validate-archimate.py architecture/model/model.archimate
```

Controleert dode verwijzingen, dubbele id's en XML-welgevormdheid; exitcode ≠ 0 bij problemen.

## Nooit tekstueel mergen

Een `.archimate` mag **nooit** regelgebaseerd worden samengevoegd — niet door git, niet met de hand. `.gitattributes` dwingt dit af (`-merge`): git weigert het bestand te mergen en vraagt om een expliciete keuze voor één kant. De andere kant breng je terug via **Archi → File → Import → Another model into the selected model** (Archi merget op ID-niveau).

Volledige procedure: [ADR 0010](../dr/0010-archimatemodel-werkafspraken.md).
