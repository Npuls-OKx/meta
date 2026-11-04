# Voorstellen op de hoofdplaat

Een voorstel is een lijn of een vak dat nog niet in het model staat en dat wel getekend moet worden, omdat er een vraag over ligt. Het model in Archi wijzigen voor iets wat nog geen besluit is, maakt van een vraag een feit; een bestand hiernaast houdt het een vraag en laat de plaat toch zien waar de lijn zou lopen.

## Tekenen

```bash
python3 tools/scripts/teken-hoofdplaat-ruim.py \
  --voorstel architecture/model/informatiemodel/voorstellen/<naam>.json --uitsnede \
  --uit architecture/model/informatiemodel/img/hoofdplaat/<naam>.svg
```

De plaat wordt uit het model getekend, dus het voorstel komt in dezelfde vormtaal als de rest: haaks gerouteerd, met dezelfde pijlpunt. Zonder `--uitsnede` staat het voorstel op de hele plaat.

## Wat een voorstel draagt

| Veld | Wat erin staat |
|---|---|
| `titel` | De vraag die het voorstel stelt |
| `herkomst` | Waar het vandaan komt: de sessie met datum, en het issue. Zonder herkomst weigert het script |
| `versie` | SemVer, zoals elke plaat |
| `stromen` | Per stroom `van`, `naar` en `label`. Beide componenten staan op de view en in hetzelfde procesgebied, anders stopt het script met die naam. Staat een component in beide gebieden, dan kiest `zone` welke |

Een voorgestelde stroom komt onderbroken en in de accentkleur op de plaat, met het woord `voorstel` in het label. Zij volgt dezelfde routering als elke andere stroom, zodat zij op de plaat thuishoort en toch te zien is als iets wat er nog niet is.

## Wat er nog niet kan

Een vak toevoegen. De renderer leest de plek van elk vak uit de view, en een nieuw vak heeft geen plek. Zie [#493](https://github.com/Npuls-OKx/meta/issues/493).
