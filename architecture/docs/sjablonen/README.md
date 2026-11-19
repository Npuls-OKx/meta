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

## Opbouw van een sjabloon

| Pagina | Wat erop staat |
|---|---|
| 1 | de omslag: titel, ondertitel, versie, wie het uitgeeft, wie het invult en wanneer |
| 2 | de inleiding: wat dit wordt, wie het invult, het voorbeeld, en de keten van user story naar eis |
| daarna | de inhoudsopgave, en dan de hoofdstukken uit de uitwerking |

De inhoudsopgave is een Word-veld en staat leeg tot hij wordt bijgewerkt; dat doet de lezer met Ctrl+A en F9, en de tekst in het veld zegt dat ook.

## Het blok boven elk hoofdstuk

Elk hoofdstuk opent met een blok dat zegt wat er wordt verwacht. Dat blok blijft staan: het is de opdracht en niet de uitwerking.

| Regel | Wat erin staat |
|---|---|
| Voorbeeld | de plek in de voorbeelduitwerking waar hetzelfde hoofdstuk al is uitgewerkt, als link |
| Acceptatiecriteria | welk artefact hier hoort, in welke context, en waaraan het voldoet |
| de laag | wat dit hoofdstuk aan het pakket van eisen bijdraagt: user stories, business, functional of technical requirements, of niets |

Een acceptatiecriterium noemt meer dan de soort. Niet "een beeld", maar:

> een procesplaat van de studentreis in mermaid, BPMN, UML of vergelijkbaar, **in het kader van de persona van deze route**, met een link naar het persona-document, en elke stap noemt wat de student doet en wat hij op dat moment moet weten.

Waar geen eigen criterium is vastgelegd, leidt de generator er een af uit wat de voorbeelduitwerking in dat hoofdstuk levert: een mermaid-diagram vraagt om een procesplaat, een tabel om een ingevulde tabel.

## Niet elk hoofdstuk levert een eis

Een journey brengt een behoefte naar boven en levert **user stories**. Een procesbeschrijving zegt wat de instelling moet kunnen: **business requirements**. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen: **functional requirements**. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat: **technical requirements**. Een enkel hoofdstuk levert niets en geeft alleen context.

Zo valt het leerroute-scenario uiteen:

| Laag | Hoofdstukken | Welke |
|---|---|---|
| user story | 7 | de journeys, de keuzemomenten, de scenario's binnen de route |
| business requirement | 5 | de instelling, de procesbeleving, het plan- en roosterproces, de plancyclus |
| functional requirement | 11 | de informatie, de gegevens, de systemen, de componenten en het informatiemodel |
| technical requirement | 9 | de procesfasen met hun interacties |
| context | 2 | de route zelf en haar kenmerken |

De verdeling staat in `hoofdstukken` in de configuratie, en een testgeval faalt wanneer elk hoofdstuk user stories zou vragen: dan zegt de indeling niets meer.

## Wat niet in elke route hoort

Een route kent niet alles wat leerroute 1 kent. Keuzedelen heten in het sjabloon daarom `Kiesbare onderdelen` en zijn **optioneel**: leerroute 9 kan ze niet hebben. Zo'n hoofdstuk opent met de voorwaarde en met de aanwijzing de kop te laten staan met de reden eronder.

Achtergrondtheorie hoort helemaal niet in een route. De verdieping over CSP en NP-hard staat daarom niet in het sjabloon; die hoort in de leesroute, en dat loopt via #556.

## Een kop is een label

Een kop noemt wat eronder staat. Hij stelt geen vraag en hij vat niet samen. `Wat betekent "regulier studeren"?` wordt dus `Kenmerken van de route`, en `Wat levert dit document op?` wordt `Opbrengst`.

Een kop die in de bron een vraag is, krijgt zijn label in `kop_labels` in de configuratie. Staat hij daar niet, dan kapt de generator hem af tot zijn onderwerp; dat is een terugval en geen oplossing, en een testgeval faalt zodra er een vraagkop in een sjabloon staat. De nummering wordt opnieuw opgebouwd, want de bron telt op drie plekken 3.2.1.1.

## Wat de generator met de uitwerking doet

| Onderdeel | Wat ermee gebeurt |
|---|---|
| kop | wordt een feitelijk label, met de termen van die ene uitwerking vervangen door een invulhaak zoals `<student>`; de nummering komt uit het Npuls-sjabloon |
| hoofdstuk | krijgt het blok met voorbeeld, acceptatiecriteria en de laag in de requirementketen |
| hoofdstuk dat niet elke route raakt | wordt optioneel, met de voorwaarde erboven |
| beeld | gaat als beeld mee, verkleind tot wat een A4 nodig heeft; een vectorbeeld wordt een PNG, want het Word-formaat draagt geen SVG |
| tabel | houdt haar kopregel en krijgt evenveel lege rijen als het origineel had |
| verwijzing | wordt volledig, want een Word-bestand staat niet in de repository |
| hoofdstuk buiten de grens | valt weg; `weglaten_tot` en `weglaten_vanaf` zeggen waar het sjabloon begint en eindigt |

Het leerroute-scenario begint bij de route zelf. De hoofdstukken over OKx, de deliverable-keten en de negen leerroutes horen in de leesroute en de context van de repository en niet in elk scenario opnieuw; dat loopt via #556.

## De invuller aggregeert

Elk sjabloon opent met dezelfde aanwijzing. Tussen de inbreng van instellingen en een ingevuld sjabloon zit een analysestap: ophalen bij meerdere instellingen, de grootst gemene deler bepalen, en die opschrijven. Een instelling spreekt voor haar eigen praktijk en niet voor de sector.

Zonder die stap wordt een sjabloon een verzameling instellingsgewoonten en geen kaderstelling. Elk sjabloon draagt daarom een hoofdstuk `Afwijkingen per instelling`, zodat wat afwijkt bewaard blijft zonder dat het kader erdoor verschuift.

## Koppen blijven staan

Een kop die is herschreven of weggehaald maakt zijn hoofdstuk onvindbaar, en een ingevuld sjabloon is daarna niet meer naast een ander te leggen. Later leest een parser uit het agent-harnas deze documenten per kop terug naar de kennisbank; dat is de tweede reden, en hij staat hier en niet in het sjabloon zelf.

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

De referentie komt uit **[Npuls Word template uitgebreid.dotx](<Npuls Word template uitgebreid.dotx>)**, het sjabloon van Npuls zelf: de omslag met het logo, de kleuren, Arial, de genummerde koppen en de kop- en voetteksten. Dat bestand wordt niet bewerkt.

Pandoc zoekt daarnaast een handvol stijlen op hun Engelse naam die het Npuls-sjabloon niet kent. `bouw-sjabloon-referentie.py` zet die erbij met Npuls-waarden: een tabel met randen, een citaat met een oranje kantlijn, links in `#3D68EC`, en `nl-NL` als taal zodat Word niet elk woord onderstreept. De titel krijgt ruimte boven zich, anders loopt hij door het logo van de omslag. In de voettekst van het sjabloon staat letterlijk `[titel]`; de bouwer vervangt die door de titel van het sjabloon, want het is geen veld dat Word zelf vult.

Twee pakketten in de dev-container horen hierbij: `librsvg2-bin` zet een vectorbeeld om naar PNG, en `libreoffice-writer` laat een gebouwd sjabloon bekijken. Beide staan in [de Dockerfile](../../../.devcontainer/Dockerfile).

## Controle

```bash
python3 -m unittest tools.tests.test_sjablonen
```

`tools/tests/test_sjablonen.py` faalt wanneer:

- een kop een vraag stelt, met een vraagwoord opent, of een eigen nummer draagt naast dat van Word;
- een hoofdstuk het blok mist, het artefact niet uit de bron komt, of elk hoofdstuk user stories zou vragen;
- een acceptatiecriterium geen context noemt, of de optionele hoofdstukken verdwenen zijn;
- de referentie niet uit het Npuls-sjabloon komt, een stijl mist die pandoc zoekt, de titel door het logo loopt, of `[titel]` in de voettekst blijft staan;
- een beeld als beschrijving in het document staat, of een genoemd beeld niet bestaat, of een SVG in het skelet staat;
- een skelet afwijkt van wat de generator nu uit die uitwerking maakt, dus het sjabloon loopt achter op de bron;
- een skelet een relatieve verwijzing draagt die in Word nergens heen wijst;
- een skelet de aggregatiestap, de requirementketen of de schrijfruimte mist;
- een tabel geen kopregel heeft, want een lege kopregel wordt in Word een lege rij;
- een `.docx` niet in versiebeheer staat of achterloopt op zijn skelet;
- een beeld ontbreekt of een SVG in het skelet staat;
- een alinea een alinea of een tabel bevat, want **Word weigert dat bestand te openen**;
- een onderdeel van het pakket geen content-type draagt, of het hoofddocument als sjabloon in plaats van als document is aangemerkt;
- de voorpagina meer draagt dan de omslag, of de inhoudsopgave voor de inleiding staat.

**Deze controle is nog geen poort.** De testsuite draait in de workflow `Model`, en die start alleen wanneer een `*.archimate`-bestand wijzigt. Een pull request die alleen aan de sjablonen raakt, draait de testgevallen dus niet.

Relateert aan: #554
