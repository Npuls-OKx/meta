# Platen in de Npuls-vormtaal

De beelden in `architecture/model/` staan in ArchiMate-vormtaal: vakken, relatielijnen, kolommen per begrippenfamilie. Die werkt voor wie het model leest, en is onleesbaar voor wie binnenkomt. De platen in deze map spreken de taal van de presentaties: het Npuls-palet met kaarten en iconen.

Zij schetsen de situatie en voegen geen inhoud toe. Elk element is terug te voeren op een document of een beeld dat er al is.

## Tekenen

```bash
python3 tools/scripts/teken-npuls-plaat.py --selectie project/img/visueel/<naam>.json --uit project/img/visueel/<naam>.svg
```

De selectie is het werk; het tekenen kost seconden. Een plaat hertekenen na een wijziging kost dus niets.

## De platen

| Plaat | Toont | Gebruikt in |
|---|---|---|
| [`wat-okx-doet`](wat-okx-doet.svg) | wat OKx doet: zes systemen onderling tegenover zes via een koppelvlakstandaard | de landing |
| [`status-ladder`](status-ladder.svg) | de zeven statussen die een product doorloopt | [Status](../../status.md) |
| [`status-nu`](status-nu.svg) | waar de producten vandaag staan, met het werk tussen status 1 en 4 | [Status](../../status.md), de leesroute |
| [`specificatie-hoofdvraag`](specificatie-hoofdvraag.svg) | wat er in concept ligt tegenover wat open staat, met de route ernaartoe | de landingspagina, de leesroute |
| [`aanleiding`](aanleiding.svg) | wat de sector vraagt, en de tegenvraag van een leverancier | de leesroute, deel 1 |
| [`fasen`](fasen.svg) | specificatie, bouw, adoptie, borging, met 2032 als eindpunt | de leesroute, deel 6 |
| [`besluiten`](besluiten.svg) | de besluiten die de rest van het werk dragen | de leesroute, deel 5 |

## Bronnen

| | |
|---|---|
| Palet | `presentaties/src/style.css`, de `--np-` tokens. Een wijziging daar raakt elke plaat |
| Iconen | [`iconen.json`](iconen.json), uitgepakt uit de Carbon-set van IBM, Apache License 2.0 |
| Achtergrond | altijd expliciet licht; een doorzichtige SVG valt weg in de donkere modus van GitHub |

Relateert aan: #454, #455.
