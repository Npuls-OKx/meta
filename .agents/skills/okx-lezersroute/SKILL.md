---
name: okx-lezersroute
description: Een lezerspagina of leesroute vormgeven: de route in delen met een vraag per deel, de verdieping in vier vaste regels, en de beelden die het verhaal dragen in de Npuls-vormtaal. Gebruik bij elke wijziging aan README, leesroute, context, historie of status, en bij elke plaat die uit scripts/teken-npuls-plaat.py komt.
---

# De lezersroute van OKx

Deze repository draagt 636 beelden en ruim driehonderd documenten. Een lezer die binnenkomt ziet daar niets van: hij ziet een landingspagina en besluit binnen een halve minuut of hij blijft. De lezersroute is wat hij daarna volgt.

Dit harnas legt vast wat in oktober 2026 werkte, na vier ronden waarin de opdrachtgever hetzelfde euvel bleef aanwijzen: te veel proza, te weinig beeld, koppen die niets benoemen.

## De drie wetten

**Een beeld boven een alinea, maar alleen waar het iets toevoegt.** Een plaat die herhaalt wat de tekst zegt is decoratie. Een plaat die een verhouding toont die in woorden drie alinea's kost, verdient zijn plek. Toets elke plaat op de vraag: staat hier iets dat nergens anders staat.

**Een kop is een label dat iets noemt wat de lezer al kent.** Een product, een status, een document, een plek, een datum. Twee soorten vervallen: de verhalende zin (`Hoe OKx hier kwam`) en het begrip dat in dat document is bedacht (`De terugloop`, `Lege niveaus`). `scripts/validate-docs.py` vangt de eerste soort op de lezerspaginas; de tweede blijft handwerk.

**Meten voor je oplevert.** Woorden per deel, beelden per deel, dode verwijzingen. Een deel dat vier keer zo zwaar is als zijn buren loopt vast, hoe goed het ook geschreven is.

```bash
python3 tools/scripts/validate-docs.py README.md project/
python3 -m unittest discover -s tools/tests
```

## De route als geheel

De leesroute telt acht delen. Elk deel opent met zijn vraag in vet, draagt een beeld, en eindigt met een of meer verdiepingen.

| Wat | Maat |
|---|---|
| Woorden per deel | 100 tot 800. Daarboven splitsen |
| Beelden per deel | ten minste een |
| Verdiepingen per deel | een tot drie. Vier is een teken dat het deel twee onderwerpen draagt |
| De kern | 45 minuten, bij 120 woorden per minuut |

De volgorde draagt een verhaal en geen inhoudsopgave. In oktober 2026 kwam die uit op: waarvoor OKx bestaat, hoe het zo liep, waar het ophoudt, hoe de gedeelde taal wordt opgebouwd, wat dat oplevert, waarop dat steunt, hoe het in leven blijft, en wat een lezer hierna doet. Het deel over de taal staat met opzet voor het deel over de producten: een lezer die eerst de producten ziet, mist waarom de vorm nog niet vaststaat.

### De verdieping draagt vier regels

Elke verdieping is een tabel met dezelfde vier rijen, zodat een lezer leert waar hij moet kijken.

| Rij | Wat erin staat |
|---|---|
| Beantwoordt | De vragen die dit document beantwoordt, in een zin |
| Overslaan | Wat een lezer bij eerste lezing kan laten liggen, en waarom |
| Status | De status van het stuk, met de lopende pull request erbij |
| Omvang | Woorden en leestijd, gemeten en niet geschat |

Een vijfde rij mag, wanneer het document iets is wat een lezer anders verkeerd leest. Een eerste poging die is ingehaald, bijvoorbeeld, draagt een rij `Wat het is`.

## De platen

De beelden in de lezersroute komen uit `tools/scripts/teken-npuls-plaat.py`, dat een SVG tekent uit een selectiebestand in `project/img/visueel/`. Het palet komt uit `presentaties/src/style.css` en de pictogrammen uit `project/img/visueel/iconen.json`, beide bron: een wijziging daar raakt elke plaat.

| Blok | Waarvoor |
|---|---|
| `ladder` | Treden die oplopen, met een trede die leeg kan zijn, chips per trede, een band over een reeks, en een terugloop van hoog naar laag |
| `stappen` | Kaarten naast elkaar met een pijl ertussen, en een lus eronder die terugwijst |
| `kolommen` | Twee lijsten naast elkaar, bijvoorbeeld wat er ligt tegenover wat open staat. Een regel met `open: true` krijgt een vraagteken |
| `kaarten` | Een rij kaarten met pictogram, titel en een regel |
| `netwerk` | Knopen in een ovaal, onderling verbonden of elk naar een midden |
| `niveaus` | Rijen met een naam en een strook miniaturen van bestaande beelden |
| `legenda`, `tekst` | De uitleg onder een blok |

```bash
python3 tools/scripts/teken-npuls-plaat.py --selectie project/img/visueel/status-nu.json \
  --uit project/img/visueel/status-nu.svg
```

### Vier dingen die misgingen

**Een doorzichtige achtergrond valt weg.** GitHub toont een SVG in de donkere modus op een donkere ondergrond. De tekenaar zet daarom altijd een expliciet lichte achtergrond.

**Een externe verwijzing laadt niet.** GitHub toont een SVG via een `img`-element, dus een verwijzing naar een jpg ernaast blijft leeg. Miniaturen van bestaande beelden gaan daarom als data in de plaat zelf; het blok `niveaus` doet dat.

**Een merk dat te lang is loopt uit het vak.** De breedteberekening is een benadering. Kijk naar het beeld voor je het opneemt: zet het om naar een afbeelding en bekijk het.

**Een plaat zonder versie is na een ronde niet te plaatsen.** Elke selectie draagt een veld `versie` volgens SemVer, en de tekenaar zet die rechts in de voetregel. Een eerste beeld begint op `0.1.0`, nieuwe inhoud verhoogt de minor, een correctie de patch. `tools/tests/test_plaatversies.py` dwingt dat af, inclusief het geval waarin iemand de bron wijzigde zonder opnieuw te tekenen.

## Een beeld uit een deck hergebruiken

Een slide die het al goed zegt verslaat een nieuwe plaat. De decks staan in `presentaties/src/` en hun export in `presentaties/export/`.

```bash
pdftoppm -r 110 -f 5 -l 5 -png presentaties/export/<deck>/<deck>.pdf /tmp/slide
convert /tmp/slide-5.png -trim +repage -bordercolor white -border 12 project/img/<naam>-<datum>.png
```

Zet in het bijschrift uit welk deck en welke datum het beeld komt. Een slide draagt de stand van die dag, en die veroudert.

## De statusregel

Elk deel en elke verdieping draagt de status van het materiaal, in de woorden van [Status](../../../project/status.md): vraag en wens, verkenning, concept, voorstel, besloten in OKx, gereleased, bekrachtigd. Schrijf de status voluit en niet als nummer; `Concept, gepubliceerd op dev in Public` leest, `Niveau 3` niet.

De route schrijft nooit een status over. Staat er op een besluit `Voorstel`, dan is dat wat de route zegt, ook als het team het in de praktijk al aanhoudt.

## Wat een ronde afmaakt

1. Meten: woorden en beelden per deel, dode verwijzingen, testgevallen.
2. Elke gewijzigde plaat opnieuw tekenen en bekijken, niet alleen genereren.
3. De versie van elke gewijzigde plaat ophogen.
4. Het platenmanifest bijwerken wanneer er een plaat bij komt: `python3 tools/scripts/platen-inventariseren.py`.
5. De index in `project/README.md` bijwerken wanneer er een document bij komt.

## Verwante skills

| Skill | Verhouding |
|---|---|
| [okx-presentatie-visueel](../okx-presentatie-visueel/SKILL.md) | dezelfde vormtaal, maar voor een slide waar een spreker bij staat |
| [okx-uitsnede-bij-een-reviewvraag](../okx-uitsnede-bij-een-reviewvraag/SKILL.md) | een beeld dat een enkele vraag beantwoordt, uit het informatiemodel |
| [okx-plaat-uit-het-model](../okx-plaat-uit-het-model/SKILL.md) | een plaat uit de view-geometrie van het ArchiMate-model |
