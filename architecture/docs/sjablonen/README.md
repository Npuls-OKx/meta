# Sjablonen voor de adviesgroep

Vijf sjablonen waarmee de adviesgroep een OKx-product zelf kan opschrijven. Zij horen bij een invulverzoek van OKx SI: de solutionlaag kan pas zeggen wat zij nodig heeft wanneer de producten eronder er liggen.

Open het Word-bestand. Elk sjabloon is **afgeleid uit de uitwerking die er al ligt**, dus het draagt elke kop, elke tabel en elk beeld van dat document.

| Product | Sjabloon | Afgeleid uit |
|---|---|---|
| persona | `OKx sjabloon persona.docx` | [persona Jochem](../specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| leerroute scenario | `OKx sjabloon leerroute scenario.docx` | [leerroute 1 scenario](../specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
| informatiemodel viewpoint | `OKx sjabloon informatiemodel viewpoint.docx` | [informatiemodel OKx](../../model/informatiemodel/informatiemodel.md) |
| leerroute scenario uitwerking | `OKx sjabloon leerroute scenario uitwerking.docx` | [de uitwerking met Jochem](../../model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |
| interactieketen | `OKx sjabloon interactieketen.docx` | [keten onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review |

## Het verwachtingsblok

Elk hoofdstuk opent met vier regels. Die zeggen wat er van dat hoofdstuk wordt verwacht, en zij blijven staan: het is de opdracht en niet de uitwerking.

| Regel | Wat erin staat |
|---|---|
| Voorbeeld | de plek in de voorbeelduitwerking waar hetzelfde hoofdstuk al is ingevuld, als link |
| Verwacht | het artefact dat hier hoort, afgeleid uit wat de voorbeelduitwerking daar levert |
| User stories | de nummers uit het pakket van eisen die dit hoofdstuk verwezenlijkt |
| Klaar wanneer | het acceptatiecriterium waaraan de uitwerking voldoet |

**Het verwachte artefact is gemeten en niet verzonnen.** Draagt het hoofdstuk in de uitwerking een mermaid-diagram, dan vraagt het sjabloon een procesdiagram; draagt het een tabel, dan vraagt het een ingevulde tabel. Het acceptatiecriterium hangt aan dat artefact: een procesdiagram is klaar wanneer het de terugweg en het foutpad toont en elke stap een rol noemt.

## Een kop is een label

Een kop noemt wat eronder staat. Hij stelt geen vraag en hij vat niet samen. `Wat betekent "regulier studeren"?` wordt dus `Kenmerken van de route`, en `Wat levert dit document op?` wordt `Opbrengst`.

Een kop die in de bron een vraag is, krijgt zijn label in `kop_labels` in de configuratie. Staat hij daar niet, dan kapt de generator hem af tot zijn onderwerp; dat is een terugval en geen oplossing, en een testgeval faalt zodra er een vraagkop in een sjabloon staat. De nummering wordt opnieuw opgebouwd, want de bron telt op drie plekken 3.2.1.1.

## Wat de generator met de uitwerking doet

| Onderdeel | Wat ermee gebeurt |
|---|---|
| kop | wordt een feitelijk label, hernummerd, met de termen van die ene uitwerking vervangen door een invulhaak zoals `<student>` |
| hoofdstuk | krijgt het verwachtingsblok, met een link naar dezelfde plek in de voorbeelduitwerking |
| beeld | gaat als beeld mee, verkleind tot wat een A4 nodig heeft; een vectorbeeld wordt een PNG, want het Word-formaat draagt geen SVG |
| tabel | houdt haar kopregel en krijgt evenveel lege rijen als het origineel had |
| verwijzing | wordt volledig, want een Word-bestand staat niet in de repository |
| hoofdstuk buiten de grens | valt weg; `weglaten_tot` en `weglaten_vanaf` zeggen waar het sjabloon begint en eindigt |

Het leerroute-scenario begint bij de route zelf. De hoofdstukken over OKx, de deliverable-keten en de negen leerroutes horen in de leesroute en de context van de repository en niet in elk scenario opnieuw; dat loopt via #556.

## De invuller aggregeert

Elk sjabloon opent met dezelfde aanwijzing. Tussen de inbreng van instellingen en een ingevuld sjabloon zit een analysestap: ophalen bij meerdere instellingen, de grootst gemene deler bepalen, en die opschrijven. Een instelling spreekt voor haar eigen praktijk en niet voor de sector.

Zonder die stap wordt een sjabloon een verzameling instellingsgewoonten en geen kaderstelling. Elk sjabloon draagt daarom een hoofdstuk `Afwijkingen per instelling`, zodat wat afwijkt bewaard blijft zonder dat het kader erdoor verschuift.

## Van user story naar requirement

Elk sjabloon draagt het hoofdstuk dat de keten uitlegt: een user story uit het pakket van eisen gaat door een business requirement, een functional requirement en een technical requirement. Er staat een uitgewerkt voorbeeld bij, zodat de vorm vastligt. In dit document vult de adviesgroep de user stories in; de drie requirementlagen volgen in een eigen ronde met dit document als bron.

## Koppen blijven staan

In het agent-harnas komt een lezer (parser) die een ingevuld document terugvertaalt naar de kennisbank. Die leest per kop, dus een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Opbouw

| Plek | Wat er staat |
|---|---|
| deze map | de vijf `.docx`-bestanden, want de adviesgroep moet er een kunnen openen zonder iets te bouwen |
| `bron/sjablonen.json` | per sjabloon de uitwerking waaruit het komt, de invulhaken, de koplabels en de grenzen |
| `gegenereerd/` | de afgeleide skeletten, hun beelden en de Word-referentie; hier bewerkt niemand iets met de hand |

Wijzig dus `bron/sjablonen.json` of de uitwerking zelf, en leid daarna opnieuw af:

```bash
python3 tools/scripts/maak-sjabloon-uit-document.py      # skelet en beelden uit de uitwerking
python3 tools/scripts/bouw-sjabloon-referentie.py        # alleen na een wijziging in de huisstijl
python3 tools/scripts/bouw-sjablonen-docx.py
python3 tools/scripts/bouw-sjablonen-docx.py --controleer
```

De referentie komt uit de standaardreferentie van pandoc met de Npuls-waarden erin: oranje `#DD784B` voor de koppen, blauw `#3D68EC` voor links, randen om elke cel, General Sans als letter en `nl-NL` als taal. Staat General Sans niet op de machine van de invuller, dan kiest Word zelf een vervanger; de huisstijl blijft dan in de kleuren zichtbaar.

Twee pakketten in de dev-container horen hierbij: `librsvg2-bin` zet een vectorbeeld om naar PNG, en `libreoffice-writer` laat een gebouwd sjabloon bekijken. Beide staan in [de Dockerfile](../../../.devcontainer/Dockerfile).

## Controle

```bash
python3 -m unittest tools.tests.test_sjablonen
```

`tools/tests/test_sjablonen.py` faalt wanneer:

- een kop een vraag stelt of met een vraagwoord opent, of de nummering niet bij 1 begint;
- een hoofdstuk het verwachtingsblok mist, of het verwachte artefact niet uit de bron komt;
- een beeld als beschrijving in het document staat, of een genoemd beeld niet bestaat, of een SVG in het skelet staat;
- een skelet afwijkt van wat de generator nu uit die uitwerking maakt, dus het sjabloon loopt achter op de bron;
- een skelet een relatieve verwijzing draagt die in Word nergens heen wijst;
- een skelet de aggregatiestap, de requirementketen of de schrijfruimte mist;
- een tabel geen kopregel heeft, want een lege kopregel wordt in Word een lege rij;
- een `.docx` niet in versiebeheer staat of achterloopt op zijn skelet;
- de referentie een van de vijf huisstijlwaarden mist.

**Deze controle is nog geen poort.** De testsuite draait in de workflow `Model`, en die start alleen wanneer een `*.archimate`-bestand wijzigt. Een pull request die alleen aan de sjablonen raakt, draait de testgevallen dus niet.

Relateert aan: #554
