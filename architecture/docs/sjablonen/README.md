# Sjablonen voor de adviesgroep

Vijf sjablonen waarmee de adviesgroep een OKx-product zelf kan opschrijven. Zij horen bij een invulverzoek van OKx SI: de solutionlaag kan pas zeggen wat zij nodig heeft wanneer de producten eronder er liggen.

Open het Word-bestand. Elk sjabloon is **afgeleid uit de uitwerking die er al ligt**, dus het draagt elke kop en elke tabel van dat document. Een sjabloon is daarmee even groot als het product dat het nadoet.

| Product | Sjabloon | Afgeleid uit |
|---|---|---|
| persona | `OKx sjabloon persona.docx` | [persona Jochem](../specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| leerroute-kaderscenario | `OKx sjabloon leerroute-kaderscenario.docx` | [kaderscenario leerroute 1](../specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
| informatiemodel-viewpoint | `OKx sjabloon informatiemodel-viewpoint.docx` | [informatiemodel OKx](../../model/informatiemodel/informatiemodel.md) |
| informatiemodel-voorbeelduitwerking | `OKx sjabloon informatiemodel-voorbeelduitwerking.docx` | [de opleiding van Jochem](../../model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |
| interactieketen | `OKx sjabloon interactieketen.docx` | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review |

## Wat de generator met de uitwerking doet

| Onderdeel | Wat ermee gebeurt |
|---|---|
| kop | blijft staan, met de termen van die ene uitwerking vervangen door een invulhaak zoals `<student>` |
| alinea die algemeen is | blijft staan, want die geldt voor elke uitwerking |
| alinea die aan die ene uitwerking hing | wordt een ingesprongen citaat met de eerste zin eruit, en schrijfruimte onder het hoofdstuk |
| tabel | houdt haar kopregel; algemene rijen blijven staan, uitwerkingsrijen worden leeg, evenveel rijen als het origineel had |
| beeld en diagram | worden een regel die zegt dat daar een beeld hoort |
| verwijzing | wordt volledig, want een Word-bestand staat niet in de repository |

De grens tussen kader en uitwerking staat per sjabloon in `invullen_vanaf`. Bij het kaderscenario blijven de hoofdstukken over OKx, de deliverable-keten en de negen leerroutes dus staan, en begint de schrijfruimte bij de uitwerking van de route zelf.

## De invuller aggregeert

Elk sjabloon opent met dezelfde aanwijzing, en die is het belangrijkste eraan. Tussen de inbreng van instellingen en een ingevuld sjabloon zit een analysestap: ophalen bij meerdere instellingen, de grootst gemene deler bepalen, en die opschrijven. Een instelling spreekt voor haar eigen praktijk en niet voor de sector.

Zonder die stap wordt een sjabloon een verzameling instellingsgewoonten en geen kaderstelling, en dan kan de solutionlaag er niets mee. Elk sjabloon draagt daarom een hoofdstuk `Afwijkingen per instelling`, zodat wat afwijkt bewaard blijft zonder dat het kader erdoor verschuift.

## Koppen blijven staan

In het agent-harnas komt een lezer (parser) die een ingevuld document terugvertaalt naar de kennisbank. Die leest per kop, dus een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Opbouw

| Plek | Wat er staat |
|---|---|
| deze map | de vijf `.docx`-bestanden, want de adviesgroep moet er een kunnen openen zonder iets te bouwen |
| `bron/sjablonen.json` | per sjabloon de uitwerking waaruit het komt, de invulhaken en de grens tussen kader en uitwerking |
| `gegenereerd/` | de afgeleide skeletten en de Word-referentie in de Npuls-huisstijl; hier bewerkt niemand iets met de hand |

Wijzig dus `bron/sjablonen.json` of de uitwerking zelf, en leid daarna opnieuw af:

```bash
python3 tools/scripts/maak-sjabloon-uit-document.py      # skelet uit de uitwerking
python3 tools/scripts/bouw-sjabloon-referentie.py        # alleen na een wijziging in de huisstijl
python3 tools/scripts/bouw-sjablonen-docx.py
python3 tools/scripts/bouw-sjablonen-docx.py --controleer
```

De referentie komt uit de standaardreferentie van pandoc met de Npuls-waarden erin: oranje `#DD784B` voor de koppen, blauw `#3D68EC` voor links, randen om elke cel, General Sans als letter en `nl-NL` als taal. Staat General Sans niet op de machine van de invuller, dan kiest Word zelf een vervanger; de huisstijl blijft dan in de kleuren zichtbaar.

## Controle in CI

`tools/tests/test_sjablonen.py` loopt mee in CI en faalt wanneer:

- een skelet minder koppen draagt dan de uitwerking waaruit het komt;
- een skelet afwijkt van wat de generator nu uit die uitwerking maakt, dus het sjabloon loopt achter op de bron;
- een skelet een relatieve verwijzing draagt, die in Word nergens heen wijst;
- een skelet de aggregatiestap, de invultabel, de aanwijzing over de koppen of de schrijfruimte mist;
- een tabel geen kopregel heeft, want een lege kopregel wordt in Word een lege rij;
- een `.docx` niet in versiebeheer staat of achterloopt op zijn skelet;
- de referentie een van de vijf huisstijlwaarden mist.

Relateert aan: #554
