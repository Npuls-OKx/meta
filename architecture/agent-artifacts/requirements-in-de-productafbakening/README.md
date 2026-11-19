# Requirements in de productafbakening

Waar horen business, functional en technical requirements op de [productafbakening](../../product-breakdown/README.md)? Dit stuk legt drie varianten naast elkaar en tekent de derde uit, zodat erover te besluiten is.

Relateert aan: #554, #558

## De vraag

De sjablonen voor de adviesgroep noemen per hoofdstuk welke laag daar ontstaat: een journey brengt user stories naar boven, een procesbeschrijving business requirements, een gegevenshoofdstuk functional requirements, een interactiehoofdstuk technical requirements. Die lagen moeten ergens landen, en de plaat zegt nu niet waar.

## Drie varianten

| | Wat het betekent | Wat eraan wringt |
|---|---|---|
| **A, pakket van eisen op de solutionlaag** | het pakket van eisen komt als artefact bij de interactieketens en het logisch gegevensmodel; de technische laag staat er expliciet, de business- en functionele laag zitten impliciet in het leerroute scenario en de informatiemodeluitwerking | een pakket van eisen is geen oplossing maar een vraag; het hoort niet in de laag die de oplossing beschrijft. En wat impliciet is, is niet te tellen en niet te toetsen |
| **B, pakket van eisen als aggregatie** | het pakket van eisen is de optelsom van alle eisen, die zelf in hun bronproducten blijven staan: business en functioneel in het leerroute scenario en de informatiemodeluitwerking, technisch in de interacties en de interactieketens | dan is het pakket van eisen een aanzicht en geen product: er is niets om aan te wijzen, te versioneren of over te dragen. Een eis die alleen in lopende tekst bestaat, is bovendien niet te nummeren en dus niet te traceren naar een test |
| **C, drie eigen artefacten** | business, functional en technical requirements worden elk een eigen artefact, elk met een pijl naar de bron waaruit zij voortkomen; het pakket van eisen draagt de user stories | vier vakken erbij op een plaat die al vol is, en het risico dat een eis en zijn bron uit elkaar gaan lopen |

## Het voorstel, uitgetekend

![Business, functional en technical requirements als eigen artefact, met de bron waaruit elk voortkomt](gegenereerd/img/requirements-als-artefact.svg)

Vier vakken met een oranje rand bestaan nog niet. De pijl omlaag zegt uit welk product de eis voortkomt; de pijl naar rechts zegt hoe een eis verfijnt tot de laag eronder.

De plaat is te hertekenen met `tools/scripts/teken-requirementsvoorstel.py`.

## Mijn afweging

**Variant C, met een voorwaarde.** Een eis die alleen in een document staat, is niet te tellen, niet te prioriteren en niet aan een testgeval te hangen. Een eigen artefact lost dat op: het draagt een nummer, een eigenaar en een status, en het is overdraagbaar aan een leverancier zonder het hele scenario mee te sturen.

De voorwaarde is dat elk artefact een **register** is en geen tweede verhaal. Het bevat per regel een nummer, de eis in een zin, en het nummer van de bron waaruit hij komt. Zodra er toelichting in komt te staan, gaat hij uit de pas lopen met het leerroute scenario, en dan is variant B achteraf beter geweest.

Twee dingen die daarbij horen:

| | |
|---|---|
| De bron blijft leidend | het leerroute scenario beschrijft, het register telt. Wijkt een eis af van zijn bron, dan wint de bron en is het register fout |
| Een eis verwijst omlaag en omhoog | een functional requirement noemt de business requirement waaruit hij komt, en een technical requirement de functional requirement. Zonder die ketting is de herkomst na een halfjaar weg |

## Wat dit betekent voor de sjablonen

Niets dat nu moet veranderen. De sjablonen noteren per hoofdstuk alleen de **nummers** van de eisen die daar ontstaan; waar die nummers vandaan komen en waar zij landen, is precies wat dit besluit vastlegt. Valt het besluit op variant C, dan wijzen de sjablonen naar drie registers in plaats van naar twee documenten.
