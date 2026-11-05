---
name: okx-json-bericht-in-beeld
description: Teken de indeling van een JSON-bericht als plaat, in de vorm van een JSON-viewer, met per sleutel het type uit RFC 8259 en JSON Schema en het aantal erbij. Gebruik zodra er JSON op tafel komt: een payload van een leverancier of een instelling, een voorbeeldbericht bij een koppelingspecificatie, een exportbestand dat naast het OKx-informatiemodel gelegd wordt, of een antwoord onder een issue waarin de structuur van een bericht moet blijken. Ook wanneer een bericht te lang is voor een json-blok, of wanneer iemand vraagt wat er eigenlijk in een bestand zit.
---

# Een JSON-bericht in beeld

Er komt een bestand binnen. Een leverancier stuurt een voorbeeldpayload, een instelling levert haar eigen uitwisseling aan, een exportbestand moet naast het informatiemodel. De eerste vraag is altijd dezelfde: wat zit erin.

Die vraag is met het bestand zelf niet te beantwoorden. Het SBIS-bericht van een enkele opleiding telt ruim veertienhonderd regels; wie het opent ziet de inhoud en juist niet de structuur. Een `json`-blok onder een issue maakt dat erger, want niemand scrollt dat door. En een mermaid-boom die je er zelf bij tekent is een tweede waarheid: hij klopt op de dag dat je hem maakt en loopt daarna stil uiteen met het bestand.

```bash
python3 tools/scripts/teken-json-structuur.py \
  --bron <bericht>.json --uit <plaat>.svg \
  --titel "Indeling van het <soort>-bericht" \
  --herkomst "van wie, wanneer, en het issue" --versie 0.1.0 \
  --diepte 3 --merk <sleutel>,<sleutel>
```

De plaat leest als een JSON-viewer, omdat iedereen die kent: per sleutel het type, het aantal, en bij een lijst de sleutels die een element draagt.

## Vaste uitgangspunten

- **Het bericht is de bron.** Het script leest het bestand; niemand typt de structuur over. Komt er een nieuwe versie van het bericht, dan is de plaat een aanroep later bij.
- **Waarden staan uit.** Een bericht van een instelling of een leverancier draagt hun inhoud, en die hoort niet ongevraagd in een publiek repository. De plaat toont sleutels, typen en aantallen. `--waarden` zet ze er alsnog bij, en dat doe je pas als de inbrenger heeft gezegd dat het mag.
- **Elke sleutel komt erop.** Een afkapping met *en nog vijf* laat de lezer precies de velden missen waar het gesprek over kan gaan, en het zijn nooit de eerste vijf die ertoe doen. Past de rij niet op een regel, dan komt er een regel bij.
- **De typenamen zijn die van de standaard.** Onvertaald, zoals hieronder.

## De typen komen uit RFC 8259 en JSON Schema

Een bericht wordt straks tegen een schema gelegd, en vaak tegen een OpenAPI-specificatie bovenop OEAPI. Dan helpt het als de plaat dezelfde woorden gebruikt als dat schema. Daarom staan de typen er onvertaald en in kleine letters op, precies zoals [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) en [JSON Schema](https://json-schema.org/draft/2020-12/json-schema-validation) ze schrijven.

| Op de plaat | Wat het is |
|---|---|
| `string` | een tekst |
| `integer` | een heel getal |
| `number` | een getal met een breuk |
| `boolean` | `true` of `false` |
| `null` | het veld is er en is leeg |
| `object { 17 }` | een object met zeventien leden |
| `array [ 22 ] of object` | een lijst van tweeentwintig objecten |
| `array [ 0 ]` | een lege lijst |

`integer` is de verfijning die JSON Schema op `number` kent. RFC 8259 zelf kent alleen `number`, maar bij een payload is het verschil tussen een telling en een maat precies wat je wilt zien.

Een leeg veld blijft zichtbaar als `null`, en een lege lijst als `array [ 0 ]`. Dat is geen ruis: een veld dat bestaat en nooit gevuld is, is vaak het interessantste veld van het bericht. In het SBIS-bericht stond `dekkingsgraad` negen keer leeg, en dat bleek de weging waar OKx zelf nog een open vraag over heeft.

## De volgorde van de stappen

1. **Zet het bericht ergens neer.** Zolang de inbrenger niet heeft gezegd dat het bestand in de repository mag, blijft het erbuiten en staat alleen de plaat erin. Zeg dat in de README naast de plaat, met de aanroep erbij, zodat zichtbaar is dat de plaat nu niet te herbouwen is.
2. **Teken op diepte 3.** Dat is bijna altijd het goede begin: de bovenlaag, de takken eronder, en de vorm van een element. Dieper levert een bestand op in plaats van een beeld, en het script stopt boven de zestig regels.
3. **Merk de takken die het gesprek dragen.** `--merk` zet een sleutel in de accentkleur. Drie tot vijf is genoeg; wie alles merkt, merkt niets. Een sleutel die niet op de plaat staat laat het script stoppen, zodat een tikfout geen stille plaat oplevert.
4. **Kijk ernaar.** Zet de SVG om naar een beeld en open het. De keuring loopt mee: `python3 tools/scripts/keur-plaat.py <plaat>.svg`.
5. **Hang hem onder het issue**, gepind op een commit, met de herkomst erbij.

## Wat je ermee zegt

De plaat is een argument en geen dump. Drie dingen vallen erop op die in de tekst eronder horen te landen.

| Wat je ziet | Wat het betekent |
|---|---|
| Een tak die OKx niet kent | Een eigen laag van de inbrenger. Noem hem bij naam en zeg wat het dichtstbijzijnde OKx-objecttype is |
| Een veld dat overal leeg is | Een afspraak die wel bestaat en nog niet wordt gebruikt. Vraag de inbrenger wat erin hoort |
| Een lijst die naar een andere lijst verwijst | De boom is in werkelijkheid een netwerk. Dat raakt het informatiemodel, dat een boom met bevatting kent |

## De maten, en waarom zij er zijn

| Maat | Waarde | Waarom |
|---|---|---|
| Regels op de plaat | hoogstens 60 | daarboven is het geen beeld meer maar een bestand; verlaag `--diepte` |
| Diepte | 3 als begin | de bovenlaag, de takken, en de vorm van een element |
| Tekens per vormregel | 86 | daarboven wordt de plaat breder dan een scherm; de rij breekt af naar een volgende regel |
| Gemerkte sleutels | drie tot vijf | wie alles merkt, merkt niets |

## Verwante skills

| Skill | Verhouding |
|---|---|
| [okx-koppelingspecificatie](../okx-koppelingspecificatie/SKILL.md) | De payload-conventies van OKx zelf; deze skill tekent een bericht dat van buiten komt |
| [okx-uitsnede-bij-een-reviewvraag](../okx-uitsnede-bij-een-reviewvraag/SKILL.md) | Hetzelfde idee voor het informatiemodel: objecttypen in plaats van sleutels |
| [okx-voorstel-op-de-hoofdplaat](../okx-voorstel-op-de-hoofdplaat/SKILL.md) | Waar een bericht de hoofdplaat raakt, met de koppelingen gemarkeerd |
| [okx-product-flow](../okx-product-flow/SKILL.md) | De vorm van het issue en de comment waar de plaat onder hangt |
