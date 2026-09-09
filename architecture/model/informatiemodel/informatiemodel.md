# Informatiemodel OKx

**Status.** Concept, versie v0.1 (plaatversie 20260909). Ter review binnen het OKx-team; daarna richting kerngroep techniek.

**Deze plaat.** [OKx informatiemodel v0.1.jpg](<OKx informatiemodel v0.1.jpg>). De mapping naar OEAPI staat apart in [informatiemodel-oeapi-mapping.md](informatiemodel-oeapi-mapping.md); de volledige lijst objecttypen en relaties in de [bijlage](informatiemodel-objecten-en-relaties.md).

## Viewpointbeschrijving

Een viewpoint legt de conventies vast waarmee een plaat gemaakt en gelezen wordt: voor wie hij is, welke vragen hij beantwoordt, welke bouwstenen zijn toegestaan en wat ze betekenen. De plaat zelf is de view. Dit hoofdstuk beschrijft het viewpoint; wat er concreet op de plaat staat, staat in de bijlage.

| | |
|---|---|
| **Naam** | Informatiemodel OKx |
| **Stakeholders** | Kerngroep techniek, leveranciers, informatiemanagers en enterprise-architecten van instellingen, onderwijskundig betrokkenen |
| **Concerns** | Welke informatieobjecten onderscheidt OKx, hoe verhouden ze zich tot elkaar, en waar houdt de OKx-scope op |
| **Doel** | Informeren en besluiten. Niet ontwerpen: dit is geen bouwtekening voor een systeem |
| **Scope** | De businesslaag, het informatieaspect. Een keten van kwalificatiekader tot resultaat, binnen een instelling. Geen applicatiecomponenten, geen techniek, geen federatie |
| **Detailniveau** | Objecttypen en hun samenhang. Geen attributen, geen datatypes: die staan in de payload-specificaties in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) |

### Positionering in de informatiegelaagdheid

Dit model draagt **MIM-niveau 1 en 2 tegelijk**. De kolommen zijn de begrippen waarin OKx de keten indeelt, en dat is niveau 1. De objecttypen binnen die kolommen, met hun onderlinge relaties, zijn niveau 2. De payload-specificaties en endpoint-sets in Public vormen het logische niveau, MIM-niveau 3.

Dit model **vervangt het vlakkenmodel** uit de [leerroute-uitwerking](../../docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md), de tabel van niveaus maal families. Dat vlakkenmodel blijft bruikbaar als versimpelde weergave voor doelgroepen die geen tientallen objecttypen nodig hebben, maar het is niet langer de bron.

De definities van de begrippen zelf staan niet hier maar in de begrippenlijst (#223), zodat begrip en objecttype elk op hun eigen niveau blijven en niets dubbel wordt vastgelegd.

### Welke bouwstenen zijn toegestaan

Alleen bedrijfsobjecten en bedrijfsactoren. Geen processen, geen applicatiecomponenten, geen services: die horen in andere views en zouden deze plaat onleesbaar maken.

Vier relatiesoorten, elk met een eigen betekenis. De notatie is die van ArchiMate; de plaat is de legenda.

| Relatie | Notatie op de plaat | Wat wij ermee bedoelen | Voorbeeld |
|---|---|---|---|
| **Specialisatie** | doorgetrokken lijn met een open driehoek bij het algemenere type | Het ene objecttype is een bijzonder geval van het andere en erft alles wat daar geldt | `Examenonderdeelspecificatie` is een `Toetsonderdeel specificatie`, met als verschil dat hij summatief is en door de examencommissie wordt vastgesteld |
| **Aggregatie** | lijn met een open ruit bij het geheel | Het ene objecttype bestaat uit het andere. Het deel kan ook zonder het geheel bestaan | Een `Summatieve resultaat structuur` bestaat uit `Examenonderdeelspecificatie` en `Examenonderdeel weging`, en kan zichzelf bevatten |
| **Associatie** | dunne lijn, met een label als de richting telt | Een inhoudelijke samenhang zonder eigenaarschap of samenstelling. Dit is de meest gebruikte relatie en zegt bewust weinig | `Onderwijseenheid specificatie` wijst naar `Leeruitkomst`: de specificatie dicht die leeruitkomsten af |
| **Toegang** | gestippelde lijn met een open pijlpunt | Een persoon raakt het objecttype, als student of als medewerker | `Persoon` raakt `Onderwijseenheid aanbod verbintenis` |

### Notatieconventies

**Kleur zegt iets over scope, niet over belang.** Geel is het OKx-referentiekader, uitgelijnd met MORA en HORA via klus 53. Grijs is wat OKx wel erkent maar niet zelf vastlegt. De plaat gebruikt op dit moment drie grijstinten terwijl de legenda er een kent; dat staat als openstaand punt.

**De kolommen zijn begrippen, geen niveaus.** Ze delen de keten in naar de vraag die ze beantwoorden.

| Kolom | Beantwoordt de vraag |
|---|---|
| Kwalificatiekader MBO | Wat is normatief geldig |
| Onderwijskundigkader instelling | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Wat gaan we organiseren |
| Onderwijsaanbod | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat is er behaald |
| Resultaatstructuur | Hoe telt dat op tot een uitspraak over de kwalificatie |

Objecttypen die niet in een kolom passen staan erbuiten: `Persoon` en `Plaatsingsgroep` raken de hele keten, `Verzoek tot Aanbod / Intekening op specificatie` is de brug van specificatie naar aanbod, en `Examenplan` en `Waarde document` staan buiten scope.

### Hoe deze view zich verhoudt tot de rest

| Artefact | Verhouding |
|---|---|
| Begrippenlijst (#223) | Levert de definities bij de kolommen en de objecttypen. Dit model definieert niets zelf |
| Payload-specificaties in Public | Werken deze objecttypen uit tot velden en datatypes. Elk veld hoort herleidbaar te zijn tot een objecttype hier |
| Vlakkenmodel in de leerroute-uitwerking | Vervangen. Blijft als versimpelde weergave voor doelgroepen die de volledige plaat niet nodig hebben |
| [Mapping naar OEAPI](informatiemodel-oeapi-mapping.md) | Zelfde objecttypen, met de standaard ernaast gelegd. Bewust een aparte plaat, zie [Public#89](https://github.com/Npuls-OKx/Public/issues/89) |

## Wat de plaat laat zien

Drie structuren die je van de plaat kunt aflezen en die het waard zijn om te benoemen.

**De keten herhaalt zich per specificatietype.** Elke specificatie heeft een aanbod, elk aanbod een verbintenis, elke verbintenis een resultaat. Dat patroon loopt van opleiding tot lesgelegenheid en ook door de toets- en examenketen. Wie een nieuw specificatietype toevoegt, voegt vier objecttypen toe.

**De leeruitkomst is het scharnier.** Elke specificatie wijst ernaar en de resultaatstructuur ook. Het is het enige objecttype dat de kolommen overbrugt.

**De resultaatstructuur is een samenstelling, geen lijst.** Een `Summatieve resultaat structuur` bestaat uit `Examenonderdeelspecificatie` en `Examenonderdeel weging`, kan zichzelf bevatten, en is verbonden met een `Summatief Afrondingscriterium` en een `Waarde document`. Dat afrondingscriterium is de zak-slaagregeling: de regel die zegt wanneer het waardedocument verdiend is. De formatieve variant heeft dezelfde vorm met `Toetsonderdeel specificatie` en `Toetsonderdeel weging`, en komt uit op `Persoonlijke ontwikkeling` in plaats van op een waardedocument.

## Bewuste keuzes en afbakening

**De leeruitkomst is de verbindende sleutel, en OKx definieert hem niet.** Leeruitkomsten zijn landelijk gestandaardiseerd en in beheer; instellingen vertalen kwalificatiekaders zelf volgens het principe van onderwijskundige vrijheid. OKx heeft de leeruitkomst nodig als sleutel en laat de vorm ervan aan een ander. Dat is meer dan een modelkeuze en hoort als uitgangspunt vastgelegd te worden naast [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md); zie de openstaande punten.

**Het niveau waarop iets gespecificeerd wordt ligt niet vast.** In het vlakkenmodel hoorde bij elk niveau precies een specificatietype: een `Onderwijseenheid-specificatie` hoorde bij het niveau kerntaak. Dat is hier bewust losgelaten. Een `Onderwijseenheid specificatie` **kan** op kerntaakniveau worden gespecificeerd, en veel instellingen zullen dat ook doen, maar dat hoeft niet zo te blijven. De koppeling loopt via de leeruitkomst, en op welk niveau een instelling haar specificaties formuleert is haar keuze. Daarom staat het niveau niet als eigenschap bij de objecttypen, en kijkt wie het vlakkenmodel gebruikt naar een gangbare indeling in plaats van naar een vaste koppeling.

**De les-laag valt buiten de uitwisseling.** `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan wel in het model maar buiten scope. Ze worden erkend zodat een latere behoefte om tot op lesniveau te beschrijven niet geblokkeerd wordt, maar er lopen geen uitwisselingen tussen applicatiecomponenten over. Dit is het antwoord op #216.

**Het examenonderdeel is een verbijzondering van het toetsonderdeel.** Wat beide gemeen hebben, het afdichten van leeruitkomsten en de reeks gelegenheid, verbintenis en resultaat, staat op het generieke type. Het verschil is dat het examenonderdeel summatief is, door de examencommissie wordt vastgesteld en meetelt in de summatieve resultaatstructuur. Dit is geen nieuwe keuze maar een herstel: het oorspronkelijke vlakkenmodel had beide al gescheiden, met een voetnoot over de gescheiden keten, verantwoording richting DUO en het scheiden van de custody chain. Die scheiding ging verloren bij het uittrekken naar het begrippenkader. Zie #162 en [Public#98](https://github.com/Npuls-OKx/Public/issues/98).

**Verbintenissen lopen ook via een groep.** `Plaatsingsgroep` hangt aan `Persoon` en associeert met vijf verbintenistypen. Daarmee is een verbintenis niet uitsluitend per student vast te leggen. Dit is het antwoord op #217.

**Het examenplan is geen objecttype van OKx.** Het examenplan is het document waarin een instelling de summatieve resultaatstructuur publiceert en vaststelt; de structuur zelf is wat uitgewisseld wordt.

## Openstaande punten

| Punt | Waarom het opgelost moet worden | Issue |
|---|---|---|
| De plaat gebruikt drie grijstinten en de legenda kent er een | Een lezer kan nu niet zien of `Leeruitkomst`, de les-laag en `Examenplan` om dezelfde reden buiten scope staan | #215 |
| Het eigenaarschap van de leeruitkomst staat nergens als uitgangspunt | Nu staat het alleen als notitie op de plaat en in dit document. Het raakt scope en verwachtingen richting instellingen en hoort in de uitgangspunten in Public | nog aan te maken |
| Het `Summatief Afrondingscriterium` hangt met een associatie aan de resultaatstructuur | Als de zak-slaagregeling onderdeel is van de structuur past een aggregatie beter | nog aan te maken |
| `Leeruitkomst` is een specialisatie van `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces` en `Competenties / Skills` | Die richting leest als: een leeruitkomst is een soort kerntaak. Bedoeld is waarschijnlijk op welk niveau een leeruitkomst is geformuleerd | nog aan te maken |
| Cardinaliteiten staan nog niet in het model | MIM-niveau 2 vraagt erom; nu staat alleen `Minimaal 1` als los label | nog aan te maken |
| De naamgeving van de objecttypen is nog niet consequent | Spaties, koppeltekens en hoofdletters lopen door elkaar | wordt opgepakt |
| De objecttypen hebben nog geen vastgestelde definitie | Zonder definitie is de plaat interpreteerbaar en daarmee betwistbaar | #223 |

Relateert aan: #163
