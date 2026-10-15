---
name: okx-interactiespecificatie
description: Schrijf een interactiespecificatie voor de OKx-catalogus: per kiesbare eenheid het contract tussen twee componenten, als document om te bekijken in plaats van te lezen. Gebruik wanneer een snede uit de leerroute-uitwerking een koppelvlakspecificatie moet worden, wanneer een instelling een interactie als eis in een aanbesteding wil citeren, of wanneer een bestaande interactiespecificatie een vormronde vraagt.
---

# Een interactiespecificatie schrijven

Een interactiespecificatie wordt opengeslagen door een informatiemanager of architect van een instelling die binnen vijf minuten wil weten of zij deze interactie wil, en binnen vijftien hoe die werkt. Daarna gaat zij met haar implementatiespecialist naar een leverancier en zegt: bouw smaak X en Y, als eis van de aanbesteding volgens OKx-spec. De leverancier offreert erop, dus het hoe moet volledig zijn: de endpoints, de sequenties en de berichten.

Dat vraagt een document om te bekijken, met de tekst voor de details die exact moeten zijn. Twee rondes zijn daar langs twee wegen op gestrand: de eerste poging werd 2766 regels proza en moest opnieuw, de tweede was beter en droeg nog steeds te veel tekst, met de voorbeeldbeelden achter een link in plaats van in beeld. Deze skill draagt wat daaruit is gebleken.

## Vaste uitgangspunten

- **Show, don't tell.** Elke paragraaf opent met het beeld of de tabel die haar punt draagt. Een alinea vooraan zet de tekst voorop, en dan draagt het beeld het verhaal niet.
- **De beelden bestaan al.** De voorbeelduitwerking van een leerroute draagt per stap een getekend beeld onder `architecture/model/informatiemodel/img/regels/`. Die verslaan elk diagram dat erbij wordt bedacht, en zij horen in het verhaal in plaats van ernaast.
- **Public is in aanbouw.** Wat op `Npuls-OKx/Public` ligt is werk in aanbouw en geen waarheid. Een eenheid zonder endpoint is onaf werk: zet het endpoint, het datamodel of de berichtspecificatie erbij als voorstel, met een werkbrief die het daar laat landen.
- **Een stand per regel.** Elke operatie, elk pad en elk schema draagt `vastgelegd` zodra Public het draagt, en `voorstel` zodra deze specificatie het voorstelt. Bij een schema staat die stand ook in het `$id`, dat op `/voorstel` eindigt.
- **De payload valideert.** Een voorbeeldpayload die niet tegen haar schema valideert is een belofte die bij de eerste bouwpoging sneuvelt.

## De volgorde van de stappen

1. **Bepaal de snede en de eenheden.** Welke informatiestromen horen bij elkaar, en welke daarvan kan een instelling los uitvragen. Elke kiesbare eenheid krijgt een stabiele aanduiding, want dit is aanbestedingsmateriaal: `IS-<domein>-<nr>`.
2. **Schrijf `casus.md` eerst.** De vaste identificaties van de snede: per objecttype de instantie met haar uuid en haar versie. Zie [hieronder](#zonder-casusmd-lopen-de-payloads-uiteen) waarom dit vooraf gaat.
3. **Leg de vorm van de operatietabel vast.** Een koprij, voor alle eenheden dezelfde. Zie [hieronder](#een-koprij-voor-alle-eenheden).
4. **Schrijf het hoofddocument en de verdiepingen.** Het hoofddocument draagt het verhaal met de beelden, een eigen bestand per eenheid draagt de lading veld voor veld.
5. **Toets de vorm en de payloads.**

   ```bash
   python3 scripts/controleer-interactiespec-vorm.py <de map>
   python3 scripts/controleer-interactiespec.py <de map>
   python3 scripts/validate-docs.py <de map>
   ```

6. **Kijk ernaar.** Een document dat elke maat haalt kan nog steeds het verkeerde zeggen. Open het en lees hoofdstuk 1 als een lezer die de snede niet kent.

## Twee fasen met een stopmoment ertussen

De eerste poging leverde 2766 regels voordat iemand naar de vorm kon kijken. De tweede werd in twee fasen gemaakt, met een stopmoment ertussen, en dat werkte: eerst de stories en de acceptatiecriteria met de opdrachtgever, daarna de uitwerking.

Begin dus nooit met schrijven. De story en de criteria zijn het gesprek, en zij bepalen welke eenheden in de snede horen; dat gesprek is in een uur gevoerd en een misgelopen snede kost een week.

## Zonder `casus.md` lopen de payloads uiteen

Zes agenten die elk hun eigen stroombestand schrijven kiezen elk hun eigen identificaties. Bij de aanbodsnede leverde dat vierendertig keer versie `0.1.0`, achtentwintig keer `1.0.0` en drie keer `0.2.0` voor dezelfde specificaties, plus uuids die per bestand verschilden. Dat kostte een hele ronde om recht te zetten.

De oorzaak is structureel en niet slordigheid: wie een payload schrijft heeft een identificatie nodig, en zonder gedeelde bron verzint hij er een. `casus.md` is die bron, en zij gaat vooraf. Neem de uuids over uit de voorbeeldpayloads van Public waar die bestaan, zodat de twee documenten dezelfde casus dragen.

## Een koprij voor alle eenheden

De zes verdiepingen van de aanbodsnede droegen zes verschillende koprijen voor hun operatietabel. Geen enkele kolom stond in alle zes op dezelfde plek, het component stond in vijf verschillende vormen, en een kolom met het verzoek- of antwoordschema bestond nergens.

Een lezer mist dat niet, want de tekst eronder vult het aan. Een generator die er een OpenAPI-document uit leidt vraagt zes parsers, en elke redactieronde op een tabel kan er een zevende van maken ([#374](https://github.com/Npuls-OKx/meta/issues/374)). Juist het component en het schema bepalen in welk document een operatie landt en met welk contract, en dat zijn de velden die het minst regelmatig stonden.

Leg daarom een koprij vast voordat de eenheden uiteengaan, met deze zeven kolommen:

| Kolom | Wat erin staat |
|---|---|
| Id | De aanduiding binnen de eenheid, `O1`, `O2` |
| Operatie | Wat er gebeurt, als handeling |
| Pad of melding | Het pad, of de naam van de melding |
| Implementeert | Het component dat de operatie serveert, of de melding ontvangt |
| Methode | GET, POST |
| Parameters | Per parameter de naam, of hij verplicht is, en de standaardwaarde |
| Statuscodes en foutgedrag | De set, en wat er bij elke code gebeurt |
| Stand | `vastgelegd` of `voorstel`, met de kwalificatie en de werkbrief |

En bind per operatie het verzoekschema en het antwoordschema, met de voorbeeldpayload erbij. De aanbodsnede bond die binding in vier verschillende conventies naast elkaar, en liet bij twee operaties het antwoord van een lijstopvraag helemaal zonder vorm: een contract waarop niemand kan bouwen.

## Een werkbriefcode draagt haar eenheid

Elke verdieping nummert haar eigen reeks werkbrieven, dus staat W15 van IS-OA-01 naast een andere W15 van IS-OA-03. Dat ging mis: W15 van de ene eenheid haalde W15 van de andere aan en zei iets anders dan daar stond, waarmee een antwoordlichaam werd belegd dat de server vormgeldig niet kon produceren.

Noem bij een verwijzing over een eenheidsgrens daarom altijd de eenheid: `W15 van IS-OA-03`. En haal de tekst over, in plaats van hem te parafraseren.

## Wat in het hoofddocument hoort, en wat in een verdieping

| Waar | Wat erin staat |
|---|---|
| Hoofddocument | Het scenario in zijn stappen, de eenheden elk met hun beeld, het informatiemodel als uitsnede, de stromen op de hoofdplaat, de endpoints per bezitter, en de keten in operaties |
| Een bestand per eenheid | De operaties met hun statuscodes, de berichtvelden met hun grond, de voorbeeldpayloads en de werkbrieven. Hier mag de tekst volledig zijn |
| Een bestand voor de landing | Per schema wat er in Public moet landen en wat dat kost, met de versie-impact |
| Een bestand voor de signaleringen | Wat een besluit vraagt, met per regel het besluit dat erbij hoort |

Het hoofddocument van de aanbodsnede droeg de schema-landing en de signaleringen eerst zelf: samen dertienhonderd woorden tabel, een derde van het document, en allebei detail. Zij verhuisden naar een eigen bestand, met in het hoofddocument een rij per bestand.

## De maten, en waarom zij er zijn

`scripts/controleer-interactiespec-vorm.py` draagt deze maten, en is de bron: een maat die hier en daar uiteenloopt is geen maat.

| Maat | Waarom |
|---|---|
| Elke kop in het hoofddocument opent met een beeld, een tabel of een diagram | Een kop die met een alinea opent zet de tekst voorop |
| Een beeldregel uit de voorbeelduitwerking staat als beeld | Zes stonden er als link: naast het verhaal in plaats van erin |
| Een leesregel bij een beeld draagt hoogstens twee zinnen | Een leesregel wijst aan waar de lezer naar kijkt; wie meer nodig heeft, legt het beeld uit in plaats van het te laten werken |
| Geen alinea langer dan vijfenzeventig woorden | Ongeveer vijf gerenderde regels, de hoogte waarop een alinea nog in een oogopslag te overzien is |
| Het hoofddocument draagt hoogstens zevenhonderd woorden buiten de tabellen | De vijftienminutenmaat |

Twee maten die een leesoordeel blijven. Een kop zegt het punt en niet de categorie: "Elke laag keert driemaal terug" in plaats van "Het informatiemodel". En hoofdstuk 1 draagt het vijfminutenbesluit, dus hoort daar een beeld per kiesbare eenheid.

## Het bewijs dat het bouwbaar is

`scripts/controleer-interactiespec.py` vindt elke voorbeeldpayload in de specificatie en valideert haar tegen het schema dat de afbakening van haar codeblok aanwijst: na de drie backquotes komt `json schema=intake-outcome`. Twee namen achter elkaar, met een komma ertussen, staan voor een dragend schema met een overlay erop; de payload gaat dan tegen beide. Het script meldt daarnaast elke sleutel die in geen van de schema's voorkomt, en dat is de controle die op Public ontbrak: daar valideren 84 van de 96 sleutels in de gepubliceerde voorbeeldpayloads tegen geen enkel schema ([Public#132](https://github.com/Npuls-OKx/Public/issues/132)).

Draai het script met de schemamap van Public ernaast. Ontbreekt die werkmap, dan eindigt het met de code voor geen oordeel in plaats van met een loos alarm.

## Verwante skills

| Skill | Verhouding |
|---|---|
| [okx-koppelingspecificatie](../okx-koppelingspecificatie/SKILL.md) | de koppeling als gestandaardiseerde stroom; deze skill schrijft het contract eromheen |
| [okx-oeapi-scenario-uitwerking](../okx-oeapi-scenario-uitwerking/SKILL.md) | de scenario's en de leerroutes waaruit een snede volgt |
| [okx-uitsnede-bij-een-reviewvraag](../okx-uitsnede-bij-een-reviewvraag/SKILL.md) | de uitsnede van het informatiemodel die bij een eenheid hoort |
| [okx-presentatie](../okx-presentatie/SKILL.md) | waar de vormregels vandaan komen: bron of sneuvelt, echte beelden boven nagebouwde, een onderwerp per slide |
| [okx-product-flow](../okx-product-flow/SKILL.md) | de twee stopmomenten en de vorm van de pull request |
