# ArchiMate-model

Het OKx **ArchiMate-model** (`model.archimate`) met o.a. de MOKA-koppelvlak-views en de bijbehorende informatiemodel-diagrammen. Te openen met [Archi](https://www.archimatetool.com/); `.bak` is een automatische back-up.

## Informatiemodel

De map [`informatiemodel/`](informatiemodel/) bevat de twee informatiemodelplaten met hun documentatie: het [informatiemodel](informatiemodel/informatiemodel.md), de [mapping naar OEAPI v6](informatiemodel/informatiemodel-oeapi-mapping.md) en [`informatiemodel.json`](informatiemodel/informatiemodel.json), dat met `python3 scripts/genereer-informatiemodel-doc.py` uit het model wordt gegenereerd. Draai dat script na elke wijziging aan een van beide views.

Deze documentatie en de [begrippenlijst](../docs/specificatie/begrippen/begrippenlijst.md) landen in Public in het releasepakket `Informatie-en-gegevensmodellen/` als laag 1 en 2. Meta is de bron; Public krijgt de release-variant via `python3 scripts/publiceer-informatiemodel.py --doel <Public-worktree>`. Het script zet de verwijzingen om naar paden binnen Public, pint wat in meta blijft op een commit, hernoemt de platen naar `img/` en faalt op een verwijzing die het niet kent, een entiteit in de brugtabel die niet in het logisch gegevensmodel staat, of een definitie die niet letterlijk in het kaderscenario van Public terug te vinden is. Met `--controleer` meldt het of Public nog gelijk loopt met meta. Exporteer de platen eerst met de hand uit Archi (het script leest de jpg's, het rendert ze niet).

## Voorbeelduitwerking leerroute 1 (Jochem)

De opleiding van Jochem stap voor stap in het informatiemodel leeft als regeltabel `informatiemodel/voorbeeld-lr1-regels.json` (schema ernaast). De kop legt de fasen met hun stappen en verwachte objecttypen vast, de rollen, de toestanden, de scope-uitzonderingen en de koppeling-ID's; de regels zijn fragmenten van de plaat per processtap; een verdieping (veld `verdieping`) zoomt in op een regel en mag met `plaat: onderwijsontwerp` putten uit de conceptplaat. De scripts:

- `python3 scripts/exporteer-archimate-view.py --mapping <koppelingen>` schrijft `informatiemodel/stromen.json`: per flow op hoofdplaat v1.7 de relatie-id, van en naar (junctions opgelost) en het label; de pijlen waar stroomt-regels naar verwijzen.
- `python3 scripts/exporteer-componenten.py` schrijft `informatiemodel/componenten.json`: per applicatiecomponent van de hoofdplaat de MORA-beschrijving uit het model en de applicatiediensten die hij realiseert. Componenten buiten de plaat voeg je toe met `--extra "Intake systeem"`. De voorbeeldcontrole toetst componentnamen hiertegen.
- `python3 scripts/exporteer-conceptplaat.py` schrijft `informatiemodel/conceptplaat-onderwijsontwerp.json`: de objecttypen (met groep) en relaties van de view "Informatiemodel Onderwijsontwerp", waar verdiepingen op de conceptplaat tegen worden getoetst.
- `python3 scripts/controleer-voorbeeldregels.py [--fasen 2,3,4]` toetst de regeltabel tegen `informatiemodel.json`, `stromen.json` en de conceptplaat (namen, relaties, rollen, stappen, pijlen) en meldt per fase welke objecttypen nog geen ontstaat-regel hebben.
- `python3 scripts/teken-voorbeeldregels.py` tekent elk beeld (regels met dezelfde beeldtitel) als SVG in ArchiMate-vormtaal naar `informatiemodel/img/regels/`, met de titel als bestandsnaam; `python3 scripts/genereer-voorbeeld-lr1.py` schrijft daaruit `informatiemodel/voorbeeld-leerroute-1-jochem.md`.
- `python3 scripts/exporteer-archimate-platen.py --view NAAM --uit pad.png` exporteert een view met Archi headless (zie `.devcontainer/Dockerfile`); met `--objecten`, `--ruimte` en `--hoekvast` als SVG met de informatieobjecten op de pijlen.

Alle scripts lezen het model alleen. Plan en eisen: het featureplan bij Public #106.

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
