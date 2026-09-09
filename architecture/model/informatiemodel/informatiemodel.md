# Informatiemodel OKx

**Status.** Concept, versie v0.1 (plaatversie 20260909). Ter review binnen het OKx-team; daarna richting kerngroep techniek.

**Doel.** Vastleggen welke objecttypen OKx onderscheidt, hoe ze zich tot elkaar verhouden, en waar de grens van de OKx-scope ligt. Dit document beschrijft de plaat [OKx informatiemodel v0.1.jpg](<OKx informatiemodel v0.1.jpg>); de mapping naar OEAPI staat apart in [informatiemodel-oeapi-mapping.md](informatiemodel-oeapi-mapping.md).

**Bron.** De tabellen in dit document worden gegenereerd uit het ArchiMate-model, uit de view `OKx informatiemodel`, met `python3 scripts/genereer-informatiemodel-doc.py`. Er is niets van de plaat overgetypt. Wijzigt het model, draai het script dan opnieuw.

## Positionering

Dit model draagt **MIM-niveau 1 en 2 tegelijk**. De kolommen zijn de begrippen waarin OKx de keten indeelt, en dat is niveau 1: het model van begrippen. De objecttypen binnen die kolommen, met hun onderlinge relaties, zijn niveau 2: het conceptuele informatiemodel. De payload-specificaties en endpoint-sets in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) vormen het logische niveau, MIM-niveau 3.

Dit model **vervangt het vlakkenmodel** uit de [leerroute-uitwerking](../../docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md), de tabel van niveaus maal families. Dat vlakkenmodel blijft bruikbaar als versimpelde weergave voor doelgroepen die geen 62 objecttypen nodig hebben, maar het is niet langer de bron. Zie ook de afbakening hieronder over de koppeling tussen niveau en objecttype.

De definities van de begrippen zelf staan niet hier maar in de begrippenlijst (#223), zodat begrip en objecttype elk op hun eigen niveau blijven en niets dubbel wordt vastgelegd.

## Leeswijzer bij de plaat

De plaat leest van links naar rechts als de keten van idee tot resultaat: van wat normatief geldt, via wat we organiseren en aanbieden, naar wie meedoet en wat er behaald is. De kolommen zijn de begrippen waarin OKx die keten indeelt.

| Kolom | Beantwoordt de vraag |
|---|---|
| Kwalificatiekader MBO | Wat is normatief geldig |
| Onderwijskundigkader instelling | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Wat gaan we organiseren |
| Onderwijsaanbod | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat is er behaald |
| Resultaatstructuur | Hoe telt dat op tot een uitspraak over de kwalificatie |

Kleur zegt iets over scope, niet over belang. Geel is het OKx-referentiekader, uitgelijnd met MORA en HORA via klus 53. Grijs is wat OKx wel erkent maar niet zelf vastlegt. De plaat gebruikt op dit moment drie grijstinten terwijl de legenda er een kent; welke tint wat betekent staat als openstaand punt hieronder.

## Objecttypen

<!-- gegenereerd:objecttypen -->
In totaal 62 objecttypen.

### Kwalificatiekader MBO

| Objecttype | Scope |
|---|---|
| `Kerntaak` | binnen scope |
| `Kwalificatie` | binnen scope |
| `Kwalificatie dossier` | binnen scope |
| `Werkproces` | binnen scope |

### Onderwijskundigkader instelling

| Objecttype | Scope |
|---|---|
| `Competenties / Skills` | binnen scope |
| `Inzicht` | binnen scope |
| `Kennis` | binnen scope |
| `Leeruitkomst` | buiten scope (landelijk belegd) |
| `Vaardigheid` | binnen scope |

### Onderwijsspecificatie

| Objecttype | Scope |
|---|---|
| `Examenonderdeelspecificatie` | binnen scope |
| `Keuzedeel` | binnen scope |
| `Keuzedeelruimte` | binnen scope |
| `Les specificatie` | buiten scope (les-laag) |
| `Onderwijseenheid specificatie` | binnen scope |
| `Opleidingspecificatie` | binnen scope |
| `Student keuze regelset` | binnen scope |
| `Toetsonderdeel specificatie` | binnen scope |
| `leeronderdeel specificatie` | binnen scope |

### Onderwijsaanbod

| Objecttype | Scope |
|---|---|
| `Examengelegenheid` | binnen scope |
| `Keuzedeelaanbod` | binnen scope |
| `Leergelegenheid` | binnen scope |
| `Lesgelegenheid` | buiten scope (les-laag) |
| `Onderwijseenheid aanbod` | binnen scope |
| `Opleidingaanbod` | binnen scope |
| `Opleidingsaanbod van Instelling` | binnen scope |
| `Opleidingsprogramma aanbod` | binnen scope |
| `Toetsgelegenheid` | binnen scope |

### Onderwijsverbintenis

| Objecttype | Scope |
|---|---|
| `Examengelegenheid verbintenis` | binnen scope |
| `Keuzedeel aanbod verbintenis` | binnen scope |
| `Leergelegenheid verbintenis` | binnen scope |
| `Lesgelegenheid verbintenis` | buiten scope (les-laag) |
| `Onderwijseenheid aanbod verbintenis` | binnen scope |
| `Opleiding aanbod  verbintenis` | binnen scope |
| `Opleidingsprogramma aanbod verbintenis` | binnen scope |
| `Toetsgelegenheid verbintenis` | binnen scope |

### Onderwijsresultaat

| Objecttype | Scope |
|---|---|
| `Aanwezigheid` | binnen scope |
| `Examengelegenheid resultaat` | binnen scope |
| `Keuzedeel resultaat` | binnen scope |
| `Leergelegenheid resultaat` | binnen scope |
| `Lesgelegenheid resultaat` | buiten scope (les-laag) |
| `Onderwijseenheid resultaat` | binnen scope |
| `Opleiding aanbod resultaat` | binnen scope |
| `Opleidingsprogramma resultaat` | binnen scope |
| `Toetsgelegenheid resultaat` | binnen scope |

### Resultaatstructuur

| Objecttype | Scope |
|---|---|
| `Examenonderdeel weging` | binnen scope |
| `Formatief resultaat` | binnen scope |
| `Formatieve beoordeling` | binnen scope |
| `Formatieve resultaat structuur` | binnen scope |
| `Persoonlijke ontwikkeling` | binnen scope |
| `Summatief Afrondingscriterium` | binnen scope |
| `Summatief resultaat` | binnen scope |
| `Summatieve beoordeling` | binnen scope |
| `Summatieve resultaat structuur` | binnen scope |
| `Toetsonderdeel weging` | binnen scope |

### Buiten de kolommen

| Objecttype | Scope |
|---|---|
| `Examenplan` | buiten scope (instellingsartefact) |
| `Medewerker` | binnen scope |
| `Opleidingsprogramma specificatie` | binnen scope |
| `Persoon` | binnen scope |
| `Plaatsingsgroep` | binnen scope |
| `Student` | binnen scope |
| `Verzoek tot Aanbod / Intekening op specificatie` | binnen scope |
| `Waarde document (diploma / certificaat)` | binnen scope |
<!-- /gegenereerd -->

## Relaties

Het model gebruikt vier relatiesoorten.

<!-- gegenereerd:relaties -->
### Specialization (13)

Het ene objecttype is een verbijzondering van het andere.

| Van | Naar | Label |
|---|---|---|
| `Examenonderdeelspecificatie` | `Toetsonderdeel specificatie` |  |
| `Formatieve beoordeling` | `Toetsgelegenheid resultaat` |  |
| `Keuzedeel` | `Opleidingsprogramma specificatie` |  |
| `Keuzedeel aanbod verbintenis` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Keuzedeel resultaat` | `Opleidingsprogramma resultaat` |  |
| `Keuzedeelaanbod` | `Opleidingsprogramma aanbod` |  |
| `Keuzedeelruimte` | `Opleidingsprogramma specificatie` |  |
| `Leeruitkomst` | `Competenties / Skills` |  |
| `Leeruitkomst` | `Kerntaak` |  |
| `Leeruitkomst` | `Kwalificatie` |  |
| `Leeruitkomst` | `Kwalificatie dossier` |  |
| `Leeruitkomst` | `Werkproces` |  |
| `Summatieve beoordeling` | `Examengelegenheid resultaat` |  |

### Aggregation (25)

Het ene objecttype bestaat uit het andere. De recursieve varianten zijn bewust: structuren kunnen genest zijn.

| Van | Naar | Label |
|---|---|---|
| `Competenties / Skills` | `Inzicht` |  |
| `Competenties / Skills` | `Kennis` |  |
| `Competenties / Skills` | `Vaardigheid` |  |
| `Formatieve resultaat structuur` | `Toetsonderdeel specificatie` |  |
| `Formatieve resultaat structuur` | `Toetsonderdeel weging` |  |
| `Kerntaak` | `Werkproces` | bestaat uit |
| `Kwalificatie` | `Kerntaak` | bestaat uit |
| `Kwalificatie dossier` | `Kwalificatie` | bevat |
| `Leergelegenheid` | `Lesgelegenheid` |  |
| `Leeruitkomst` | `Leeruitkomst` |  |
| `Onderwijseenheid aanbod` | `Leergelegenheid` |  |
| `Onderwijseenheid specificatie` | `Onderwijseenheid specificatie` |  |
| `Onderwijseenheid specificatie` | `leeronderdeel specificatie` |  |
| `Opleidingaanbod` | `Opleidingsprogramma aanbod` |  |
| `Opleidingsaanbod van Instelling` | `Opleidingaanbod` |  |
| `Opleidingspecificatie` | `Opleidingsprogramma specificatie` |  |
| `Opleidingsprogramma aanbod` | `Onderwijseenheid aanbod` |  |
| `Opleidingsprogramma specificatie` | `Onderwijseenheid specificatie` |  |
| `Opleidingsprogramma specificatie` | `Opleidingsprogramma specificatie` |  |
| `Persoon` | `Medewerker` |  |
| `Persoon` | `Student` |  |
| `Summatieve resultaat structuur` | `Examenonderdeel weging` |  |
| `Summatieve resultaat structuur` | `Examenonderdeelspecificatie` |  |
| `Summatieve resultaat structuur` | `Summatieve resultaat structuur` |  |
| `leeronderdeel specificatie` | `Les specificatie` |  |

### Association (79)

Een inhoudelijke samenhang zonder eigenaarschap of samenstelling.

| Van | Naar | Label |
|---|---|---|
| `Aanwezigheid` | `Lesgelegenheid resultaat` |  |
| `Examengelegenheid` | `Examengelegenheid verbintenis` |  |
| `Examengelegenheid resultaat` | `Aanwezigheid` |  |
| `Examengelegenheid verbintenis` | `Examengelegenheid resultaat` |  |
| `Examenonderdeel weging` | `Examenonderdeelspecificatie` |  |
| `Examenonderdeelspecificatie` | `Examengelegenheid` |  |
| `Examenonderdeelspecificatie` | `Leeruitkomst` |  |
| `Examenonderdeelspecificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Examenplan` | `Kerntaak` |  |
| `Examenplan` | `Summatieve resultaat structuur` | kent |
| `Formatieve beoordeling` | `Formatief resultaat` | kent |
| `Formatieve resultaat structuur` | `Formatief resultaat` | conform |
| `Keuzedeel` | `Keuzedeelaanbod` |  |
| `Keuzedeel` | `Keuzedeelruimte` |  |
| `Keuzedeel` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Keuzedeel aanbod verbintenis` | `Keuzedeel resultaat` |  |
| `Keuzedeelaanbod` | `Keuzedeel aanbod verbintenis` |  |
| `Keuzedeelaanbod` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Keuzedeelruimte` | `Student keuze regelset` |  |
| `Leergelegenheid` | `Leergelegenheid verbintenis` |  |
| `Leergelegenheid` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Leergelegenheid verbintenis` | `Leergelegenheid resultaat` |  |
| `Les specificatie` | `Leeruitkomst` |  |
| `Les specificatie` | `Lesgelegenheid` |  |
| `Les specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Lesgelegenheid` | `Lesgelegenheid verbintenis` |  |
| `Lesgelegenheid` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Lesgelegenheid verbintenis` | `Lesgelegenheid resultaat` |  |
| `Onderwijseenheid aanbod` | `Onderwijseenheid aanbod verbintenis` |  |
| `Onderwijseenheid aanbod` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Onderwijseenheid aanbod verbintenis` | `Onderwijseenheid resultaat` |  |
| `Onderwijseenheid specificatie` | `Leeruitkomst` |  |
| `Onderwijseenheid specificatie` | `Onderwijseenheid aanbod` |  |
| `Onderwijseenheid specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Opleiding aanbod  verbintenis` | `Opleiding aanbod resultaat` |  |
| `Opleiding aanbod  verbintenis` | `Opleidingsprogramma aanbod verbintenis` | Minimaal 1 |
| `Opleidingaanbod` | `Opleiding aanbod  verbintenis` |  |
| `Opleidingspecificatie` | `Leeruitkomst` |  |
| `Opleidingspecificatie` | `Opleidingaanbod` |  |
| `Opleidingspecificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Opleidingsprogramma aanbod` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Opleidingsprogramma aanbod` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Opleidingsprogramma aanbod verbintenis` | `Opleidingsprogramma resultaat` |  |
| `Opleidingsprogramma specificatie` | `Leeruitkomst` |  |
| `Opleidingsprogramma specificatie` | `Opleidingsprogramma aanbod` |  |
| `Persoon` | `Plaatsingsgroep` | Worden gegroepeerd via |
| `Persoonlijke ontwikkeling` | `Competenties / Skills` |  |
| `Persoonlijke ontwikkeling` | `Formatieve resultaat structuur` |  |
| `Plaatsingsgroep` | `Keuzedeel aanbod verbintenis` |  |
| `Plaatsingsgroep` | `Leergelegenheid verbintenis` |  |
| `Plaatsingsgroep` | `Onderwijseenheid aanbod verbintenis` |  |
| `Plaatsingsgroep` | `Opleiding aanbod  verbintenis` |  |
| `Plaatsingsgroep` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Student keuze regelset` | `Keuzedeel` |  |
| `Student keuze regelset` | `Les specificatie` |  |
| `Student keuze regelset` | `Onderwijseenheid specificatie` |  |
| `Student keuze regelset` | `Opleidingspecificatie` |  |
| `Student keuze regelset` | `Opleidingsprogramma specificatie` |  |
| `Student keuze regelset` | `leeronderdeel specificatie` |  |
| `Summatief Afrondingscriterium` | `Waarde document (diploma / certificaat)` |  |
| `Summatieve beoordeling` | `Summatief resultaat` | met |
| `Summatieve resultaat structuur` | `Leeruitkomst` |  |
| `Summatieve resultaat structuur` | `Summatief Afrondingscriterium` |  |
| `Summatieve resultaat structuur` | `Summatief resultaat` | conform |
| `Summatieve resultaat structuur` | `Waarde document (diploma / certificaat)` |  |
| `Toetsgelegenheid` | `Toetsgelegenheid verbintenis` |  |
| `Toetsgelegenheid resultaat` | `Aanwezigheid` |  |
| `Toetsgelegenheid verbintenis` | `Toetsgelegenheid resultaat` |  |
| `Toetsonderdeel specificatie` | `Leeruitkomst` |  |
| `Toetsonderdeel specificatie` | `Toetsgelegenheid` |  |
| `Toetsonderdeel specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Toetsonderdeel weging` | `Toetsonderdeel specificatie` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Examengelegenheid` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Opleidingaanbod` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Opleidingsprogramma specificatie` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Toetsgelegenheid` |  |
| `leeronderdeel specificatie` | `Leergelegenheid` |  |
| `leeronderdeel specificatie` | `Leeruitkomst` |  |
| `leeronderdeel specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |

### Access (23)

Een persoon raakt het objecttype, als student of als medewerker.

| Van | Naar | Label |
|---|---|---|
| `Persoon` | `Aanwezigheid` |  |
| `Persoon` | `Examengelegenheid resultaat` |  |
| `Persoon` | `Examengelegenheid verbintenis` |  |
| `Persoon` | `Keuzedeel aanbod verbintenis` |  |
| `Persoon` | `Keuzedeel resultaat` |  |
| `Persoon` | `Keuzedeelaanbod` |  |
| `Persoon` | `Leergelegenheid` |  |
| `Persoon` | `Leergelegenheid resultaat` |  |
| `Persoon` | `Leergelegenheid verbintenis` |  |
| `Persoon` | `Lesgelegenheid resultaat` |  |
| `Persoon` | `Lesgelegenheid verbintenis` |  |
| `Persoon` | `Onderwijseenheid aanbod` |  |
| `Persoon` | `Onderwijseenheid aanbod verbintenis` |  |
| `Persoon` | `Onderwijseenheid resultaat` |  |
| `Persoon` | `Opleiding aanbod  verbintenis` |  |
| `Persoon` | `Opleiding aanbod resultaat` |  |
| `Persoon` | `Opleidingaanbod` |  |
| `Persoon` | `Opleidingsprogramma aanbod` |  |
| `Persoon` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Persoon` | `Opleidingsprogramma resultaat` |  |
| `Persoon` | `Toetsgelegenheid resultaat` |  |
| `Persoon` | `Toetsgelegenheid verbintenis` |  |
| `Persoon` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
<!-- /gegenereerd -->

## Bewuste keuzes en afbakening

**De leeruitkomst is de verbindende sleutel, en OKx definieert hem niet.** Elke specificatie in de plaat wijst naar `Leeruitkomst`, en de resultaatstructuur ook. Het objecttype zelf staat grijs: leeruitkomsten zijn landelijk gestandaardiseerd en in beheer, en instellingen vertalen kwalificatiekaders zelf volgens het principe van onderwijskundige vrijheid. OKx heeft de leeruitkomst nodig als sleutel en laat de vorm ervan aan een ander. Zie [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md).

**De les-laag valt buiten de uitwisseling.** `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan wel in het model maar buiten scope. Ze worden erkend zodat een latere behoefte om tot op lesniveau te beschrijven niet geblokkeerd wordt, maar er lopen geen uitwisselingen tussen applicatiecomponenten over. Dit is het antwoord op #216.

**Het examenonderdeel is een verbijzondering van het toetsonderdeel.** `Examenonderdeelspecificatie` is in het model een specialisatie van `Toetsonderdeel specificatie`. Wat beide gemeen hebben, het afdichten van leeruitkomsten en de reeks gelegenheid, verbintenis en resultaat, staat op het generieke type. Het verschil is dat het examenonderdeel summatief is, door de examencommissie wordt vastgesteld en meetelt in de resultaatstructuur. Dit is geen nieuwe keuze maar een herstel. Het oorspronkelijke vlakkenmodel in de leerroute-uitwerking had toetsing en examinering al als twee gescheiden rijen, met een voetnoot over de gescheiden keten: summatief tegenover formatief, verantwoording richting DUO, en het scheiden van de custody chain. Die scheiding is verloren gegaan toen de tabel naar het begrippenkader werd uitgetrokken. Zie #162 en [Public#98](https://github.com/Npuls-OKx/Public/issues/98).

**Verbintenissen lopen ook via een groep.** `Plaatsingsgroep` hangt aan `Persoon` en associeert met vijf verbintenistypen. Daarmee is een verbintenis niet uitsluitend per student vast te leggen. Dit is het antwoord op #217.

**Het niveau waarop iets gespecificeerd wordt ligt niet vast.** In het vlakkenmodel hoorde bij elk niveau precies een specificatietype: een `Onderwijseenheid-specificatie` hoorde bij het niveau kerntaak. Dat is in dit model bewust losgelaten. Een `Onderwijseenheid specificatie` **kan** op kerntaakniveau worden gespecificeerd, en veel instellingen zullen dat ook doen, maar dat hoeft niet zo te blijven. De koppeling loopt via de leeruitkomst, en op welk niveau een instelling haar specificaties formuleert is haar keuze binnen de onderwijskundige vrijheid.

Daarom staat het niveau niet als eigenschap bij de objecttypen. Wie het vlakkenmodel als versimpelde weergave gebruikt, kijkt dus naar een gangbare indeling en niet naar een vaste koppeling.

**Het examenplan is geen objecttype van OKx.** `Examenplan` staat grijs en kent de summatieve resultaatstructuur. Het examenplan is het document waarin een instelling die structuur publiceert en vaststelt; de structuur zelf is wat uitgewisseld wordt.

## Openstaande punten

| Punt | Waarom het opgelost moet worden | Issue |
|---|---|---|
| De plaat gebruikt drie grijstinten en de legenda kent er een | Een lezer kan nu niet zien of `Leeruitkomst`, de les-laag en `Examenplan` om dezelfde reden buiten scope staan | #215 |
| `Opleidingsprogramma specificatie` valt op de plaat buiten de kolom Onderwijsspecificatie | Alleen een tekenkwestie, maar het maakt de kolomindeling automatisch onbetrouwbaar | nog aan te maken |
| De objecttypen hebben nog geen vastgestelde definitie | Zonder definitie is de plaat interpreteerbaar en daarmee betwistbaar | #223 |
| Cardinaliteiten staan nog niet in het model | MIM-niveau 2 vraagt erom; nu staat alleen `Minimaal 1` als los label | nog aan te maken |
| `Leeruitkomst` is in het model een specialisatie van `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces` en `Competenties / Skills` | Die richting leest als: een leeruitkomst is een soort kerntaak. Bedoeld is waarschijnlijk op welk niveau een leeruitkomst is geformuleerd | nog aan te maken |
| De naamgeving van de objecttypen is nog niet consequent | Spaties, koppeltekens en hoofdletters lopen door elkaar, en een dubbele spatie | wordt opgepakt |

Relateert aan: #163
