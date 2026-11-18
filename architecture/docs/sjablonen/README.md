# Sjablonen voor de adviesgroep

Vijf sjablonen waarmee de adviesgroep een OKx-product zelf kan opschrijven. Zij horen bij een invulverzoek van OKx SI: de solutionlaag kan pas zeggen wat zij nodig heeft wanneer de producten eronder er liggen.

Open het Word-bestand; de markdown eronder is de bron.

| Product | Sjabloon | Voorbeelduitwerking |
|---|---|---|
| persona | `OKx sjabloon persona.docx` | [persona Jochem](../specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| leerroute-kaderscenario | `OKx sjabloon leerroute-kaderscenario.docx` | [kaderscenario leerroute 1](../specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
| informatiemodel-viewpoint | `OKx sjabloon informatiemodel-viewpoint.docx` | [informatiemodel OKx](../../model/informatiemodel/informatiemodel.md) |
| informatiemodel-voorbeelduitwerking | `OKx sjabloon informatiemodel-voorbeelduitwerking.docx` | [de opleiding van Jochem](../../model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |
| interactieketen | `OKx sjabloon interactieketen.docx` | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review |

## De invuller aggregeert

Elk sjabloon opent met dezelfde aanwijzing, en die is het belangrijkste eraan. Tussen de inbreng van instellingen en een ingevuld sjabloon zit een analysestap: ophalen bij meerdere instellingen, de grootst gemene deler bepalen, en die opschrijven. Een instelling spreekt voor haar eigen praktijk en niet voor de sector.

Zonder die stap wordt een sjabloon een verzameling instellingsgewoonten en geen kaderstelling, en dan kan de solutionlaag er niets mee. Elk sjabloon draagt daarom een hoofdstuk `Afwijkingen per instelling`, zodat wat afwijkt bewaard blijft zonder dat het kader erdoor verschuift.

## Koppen blijven staan

In het agent-harnas komt een lezer (parser) die een ingevuld document terugvertaalt naar de kennisbank. Die leest per kop, dus een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Opbouw

Drie dingen, elk op een eigen plek:

| Plek | Wat er staat |
|---|---|
| deze map | de vijf `.docx`-bestanden, want de adviesgroep moet er een kunnen openen zonder iets te bouwen |
| `bron/` | de markdown-skeletten, de bron die een mens bewerkt |
| `gegenereerd/` | de Word-referentie in de Npuls-huisstijl, die alleen een script leest |

Wijzig dus een skelet in `bron/` en bouw daarna opnieuw:

```bash
python3 tools/scripts/bouw-sjabloon-referentie.py   # alleen na een wijziging in de huisstijl
python3 tools/scripts/bouw-sjablonen-docx.py
python3 tools/scripts/bouw-sjablonen-docx.py --controleer   # faalt wanneer een .docx ontbreekt
```

De referentie komt uit de standaardreferentie van pandoc met de Npuls-kleuren erin: oranje `#DD784B` voor de koppen, blauw `#3D68EC` voor links, General Sans als letter. Staat General Sans niet op de machine van de invuller, dan kiest Word zelf een vervanger; de huisstijl blijft dan in de kleuren zichtbaar.

## Controle in CI

`tools/tests/test_sjablonen.py` loopt mee in CI en faalt wanneer:

- een skelet ontbreekt, of een `.docx` niet in versiebeheer staat;
- een skelet de aggregatiestap, de invultabel of de aanwijzing over de koppen mist;
- een skelet geen verwijzing naar een voorbeelduitwerking draagt;
- een tabel geen kopregel heeft, want een lege kopregel wordt in Word een lege rij;
- een `.docx` ouder is dan zijn skelet, dus het sjabloon loopt achter op de bron.

Relateert aan: #554
