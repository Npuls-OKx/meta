# Eisen in de productafbakening

Waar ontstaan de eisen van OKx, en waar landen zij? Dit stuk tekent het uit, zodat erover te besluiten is.

Relateert aan: #554, #558

## De vraag

De sjablonen voor de adviesgroep noemen per hoofdstuk welke laag daar ontstaat: een journey brengt user stories naar boven, een procesbeschrijving instellingseisen, een gegevenshoofdstuk functionele eisen, een interactiehoofdstuk technische eisen. Die lagen moeten ergens landen, en de plaat zegt nu niet waar.

De instellings- en functionele eisen **zitten al in de leerroute scenario's**, zoals die nu geschreven zijn. Alleen staan zij er als lopende tekst, en daarmee zijn zij niet te tellen, niet te prioriteren en niet aan een testgeval te hangen.

Wat opvalt in de keten hieronder: de **interactieketens zijn geen bron van eisen maar een gevolg ervan**. Zij ontstaan uit de functionele eisen, de instellingseisen en de uitwerking samen, en leveren daarna pas de technische eisen op.

## De keten

![Links de producten die de eisen voeden, rechts de keten van eis naar koppelvlakspecificatie](gegenereerd/img/requirements-als-artefact.svg)

| Stap | Wat eraan voorafgaat |
|---|---|
| **Instellingseisen** | de PoC-inbreng, de persona's en de leerroute scenario's **definieren ze samen**: wat een instelling kan of wil kunnen om de scenario's te realiseren |
| **Functionele eisen** | de instellingseisen, samen met de leerroute scenario uitwerking in het informatiemodel |
| **Interactieketens** | de functionele eisen, de instellingseisen en diezelfde uitwerking, alle drie |
| **Technische eisen** | die krijgen geen eigen artefact; de solutionlaag *is* de technische eis |
| **Koppelvlakspecificaties** | wat een leverancier leest en bouwt; de interacties, operaties en schema's erin zijn de technische eis |

De keten loopt dus van wat een instelling wil, via wat een component moet doen, naar wat er over de lijn gaat. Elke stap voegt iets toe dat de vorige nog niet kon zeggen.

**De technische eisen staan niet als apart artefact op de plaat.** De solutionlaag is de technische eis: wat er over de lijn gaat, in welke vorm en wat er bij een fout gebeurt, staat in de interacties, de koppelvlakdiensten en de operaties zelf. Een vak ernaast zou twee teksten over hetzelfde opleveren.

De plaat is te hertekenen met `tools/scripts/teken-requirementsvoorstel.py`.

## Instellingseisen en niet bedrijfseisen

De gangbare term is business requirement. Die past hier niet: OKx spreekt met publieke onderwijsinstellingen en niet met bedrijven. **Instellingseis** zegt hetzelfde en past bij wie het aangaat.

Dezelfde lijn geldt voor de andere twee: functionele eis en technische eis, en niet functional of technical requirement. In een gesprek met een leverancier blijft de Engelse term bruikbaar als vertaling; in de documenten staat de Nederlandse.

## PoC-inbreng wordt een eigen artefact

Wat de koploperinstellingen in de sessies hebben ingebracht, is nu geen artefact. Dat is een gat: zonder die vastlegging is de grootst gemene deler later niet te verantwoorden, en kan niemand nagaan welke instelling welke wens had.

De inbreng voedt twee dingen: de **persona's**, die er een gezicht aan geven, en de **leerroute scenario's**, die haar tot een route uitwerken.

## Geen pakket van eisen meer

Eerder stond er een artefact pakket van eisen dat de drie soorten zou optellen. Dat is losgelaten. De drie soorten eisen staan op zichzelf, elk met een eigen bron en een eigen plek in de keten; een vierde vak dat ze optelt voegt geen product toe maar een aanzicht.

## De voorwaarde bij elk eisenartefact

Een eisenartefact is een **register en geen tweede verhaal**. Per regel een nummer, de eis in een zin, en het nummer van de bron waaruit hij komt.

| | |
|---|---|
| De bron blijft leidend | het leerroute scenario beschrijft, het register telt. Wijkt een eis af van zijn bron, dan wint de bron en is het register fout |
| Een eis verwijst omhoog | een functionele eis noemt de instellingseis waaruit hij komt. Zonder die ketting is de herkomst na een halfjaar weg |
| Geen toelichting in het register | zodra er uitleg in komt te staan, loopt het uit de pas met het scenario |

## Moeten de eisen in de leerroute scenario uitwerking zelf?

Nee. De uitwerking is een toets: zij legt het scenario naast het model en laat zien waar het model tekortschiet. Zodra de eisen er als hoofdstuk in komen, is het twee documenten in een band, en de eis raakt zoek tussen de bouwstenen.

Wat er wel in hoort, staat er al: het hoofdstuk **Hiaten in het model**. Dat is de oogst van de toets, en elke regel daaruit wordt een functionele eis in het register.

## Wat dit betekent voor de sjablonen

Niets dat nu moet veranderen. De sjablonen noteren per hoofdstuk alleen de **nummers** van de eisen die daar ontstaan; waar die nummers vandaan komen en waar zij landen is precies wat dit besluit vastlegt. De termen in de sjablonen gaan wel mee: business requirements wordt instellingseisen.
