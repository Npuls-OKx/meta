# Informatiemodel OKx

**Status.** Concept, versie v0.1 (plaatversie 20260909). Ter review binnen het OKx-team; daarna richting kerngroep techniek.

**Doel.** Vastleggen welke objecttypen OKx onderscheidt, hoe ze zich tot elkaar verhouden, en waar de grens van de OKx-scope ligt. Dit document beschrijft de plaat [OKx informatiemodel v0.1.jpg](<OKx informatiemodel v0.1.jpg>); de mapping naar OEAPI staat apart in [informatiemodel-oeapi-mapping.md](informatiemodel-oeapi-mapping.md).

**Bron.** Alle objecttypen en relaties in dit document zijn uit het ArchiMate-model gehaald, uit de view `OKx informatiemodel`. Er is niets van de plaat overgetypt.

## Positionering

Het [begrippenkader](../../docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) is het model van begrippen, MIM-niveau 1: de zes families, de zes niveaus en de ankertabel. Dit document is het conceptuele informatiemodel, **MIM-niveau 2**: objecttypen, relaties en cardinaliteiten. De payload-specificaties en endpoint-sets in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) vormen het logische niveau, MIM-niveau 3.

Begrippen en objecttypen blijven elk op hun eigen niveau. Waar een objecttype samenvalt met een begrip uit de ankertabel, staat hier geen tweede definitie maar een verwijzing.

## Leeswijzer bij de plaat

De plaat leest van links naar rechts als de keten uit het begrippenkader: van wat normatief geldt, via wat we organiseren en aanbieden, naar wie meedoet en wat er behaald is. De kolommen zijn de families uit de ankertabel.

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

In totaal 62 objecttypen, waarvan er **38 niet in de ankertabel voorkomen**. Die laatste groep heeft nog geen vastgestelde definitie; dat is de brug naar de begrippenlijst (#223).

### Kwalificatiekader MBO

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Kerntaak` | binnen scope | ja |
| `Kwalificatie` | binnen scope | ja |
| `Kwalificatie dossier` | binnen scope | ja |
| `Werkproces` | binnen scope | ja |

### Onderwijskundigkader instelling

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Competenties / Skills` | binnen scope | nee, nieuw |
| `Inzicht` | binnen scope | nee, nieuw |
| `Kennis` | binnen scope | nee, nieuw |
| `Leeruitkomst` | buiten scope (landelijk belegd) | ja |
| `Vaardigheid` | binnen scope | nee, nieuw |

### Onderwijsspecificatie

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Examenonderdeelspecificatie` | binnen scope | nee, nieuw |
| `Keuzedeel` | binnen scope | nee, nieuw |
| `Keuzedeelruimte` | binnen scope | nee, nieuw |
| `Les specificatie` | buiten scope (les-laag) | ja |
| `Onderwijseenheid specificatie` | binnen scope | ja |
| `Opleidingspecificatie` | binnen scope | ja |
| `Student keuze regelset` | binnen scope | nee, nieuw |
| `Toetsonderdeel specificatie` | binnen scope | ja |
| `leeronderdeel specificatie` | binnen scope | ja |

### Onderwijsaanbod

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Examengelegenheid` | binnen scope | nee, nieuw |
| `Keuzedeelaanbod` | binnen scope | nee, nieuw |
| `Leergelegenheid` | binnen scope | ja |
| `Lesgelegenheid` | buiten scope (les-laag) | ja |
| `Onderwijseenheid aanbod` | binnen scope | ja |
| `Opleidingaanbod` | binnen scope | nee, nieuw |
| `Opleidingsaanbod van Instelling` | binnen scope | nee, nieuw |
| `Opleidingsprogramma aanbod` | binnen scope | ja |
| `Toetsgelegenheid` | binnen scope | ja |

### Onderwijsverbintenis

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Examengelegenheid verbintenis` | binnen scope | nee, nieuw |
| `Keuzedeel aanbod verbintenis` | binnen scope | nee, nieuw |
| `Leergelegenheid verbintenis` | binnen scope | ja |
| `Lesgelegenheid verbintenis` | buiten scope (les-laag) | ja |
| `Onderwijseenheid aanbod verbintenis` | binnen scope | nee, nieuw |
| `Opleiding aanbod  verbintenis` | binnen scope | nee, nieuw |
| `Opleidingsprogramma aanbod verbintenis` | binnen scope | nee, nieuw |
| `Toetsgelegenheid verbintenis` | binnen scope | ja |

### Onderwijsresultaat

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Aanwezigheid` | binnen scope | ja |
| `Examengelegenheid resultaat` | binnen scope | nee, nieuw |
| `Keuzedeel resultaat` | binnen scope | nee, nieuw |
| `Leergelegenheid resultaat` | binnen scope | ja |
| `Lesgelegenheid resultaat` | buiten scope (les-laag) | ja |
| `Onderwijseenheid resultaat` | binnen scope | ja |
| `Opleiding aanbod resultaat` | binnen scope | nee, nieuw |
| `Opleidingsprogramma resultaat` | binnen scope | ja |
| `Toetsgelegenheid resultaat` | binnen scope | nee, nieuw |

### Resultaatstructuur

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Examenonderdeel weging` | binnen scope | nee, nieuw |
| `Formatief resultaat` | binnen scope | nee, nieuw |
| `Formatieve beoordeling` | binnen scope | nee, nieuw |
| `Formatieve resultaat structuur` | binnen scope | nee, nieuw |
| `Persoonlijke ontwikkeling` | binnen scope | nee, nieuw |
| `Summatief Afrondingscriterium` | binnen scope | nee, nieuw |
| `Summatief resultaat` | binnen scope | nee, nieuw |
| `Summatieve beoordeling` | binnen scope | nee, nieuw |
| `Summatieve resultaat structuur` | binnen scope | nee, nieuw |
| `Toetsonderdeel weging` | binnen scope | nee, nieuw |

### Buiten de kolommen

| Objecttype | Scope | In de ankertabel |
|---|---|---|
| `Examenplan` | buiten scope (instellingsartefact) | nee, nieuw |
| `Medewerker` | binnen scope | nee, nieuw |
| `Opleidingsprogramma specificatie` | binnen scope | ja |
| `Persoon` | binnen scope | nee, nieuw |
| `Plaatsingsgroep` | binnen scope | nee, nieuw |
| `Student` | binnen scope | nee, nieuw |
| `Verzoek tot Aanbod / Intekening op specificatie` | binnen scope | nee, nieuw |
| `Waarde document (diploma / certificaat)` | binnen scope | nee, nieuw |

## Relaties

Het model gebruikt vier relatiesoorten. De betekenis per soort staat hieronder, gevolgd door de volledige lijst uit het model.

### Specialization (13)

Het ene objecttype is een verbijzondering van het andere. Hier zit de scheiding tussen toetsen en examineren, en de opbouw van het keuzedeel.

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

Het ene objecttype bestaat uit het andere. De recursieve varianten (een specificatie die een specificatie bevat) zijn bewust: structuren kunnen genest zijn.

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

Een persoon raakt het objecttype: als student of als medewerker.

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

## Bewuste keuzes en afbakening

**De leeruitkomst is de verbindende sleutel, en OKx definieert hem niet.** Elke specificatie in de plaat wijst naar `Leeruitkomst`, en de resultaatstructuur ook. Het objecttype zelf staat grijs: leeruitkomsten zijn landelijk gestandaardiseerd en in beheer, en instellingen vertalen kwalificatiekaders zelf volgens het principe van onderwijskundige vrijheid. OKx heeft de leeruitkomst nodig als sleutel en laat de vorm ervan aan een ander. Zie [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md).

**De les-laag valt buiten de uitwisseling.** `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis` en `Lesgelegenheid resultaat` staan wel in het model maar buiten scope. Ze worden erkend zodat een latere behoefte om tot op lesniveau te beschrijven niet geblokkeerd wordt, maar er lopen geen uitwisselingen tussen applicatiecomponenten over. Dit is het antwoord op #216.

**Het examenonderdeel is een verbijzondering van het toetsonderdeel.** `Examenonderdeelspecificatie` is in het model een specialisatie van `Toetsonderdeel specificatie`. Wat beide gemeen hebben, het afdichten van leeruitkomsten en de reeks gelegenheid, verbintenis en resultaat, staat op het generieke type. Het verschil is dat het examenonderdeel summatief is, door de examencommissie wordt vastgesteld en meetelt in de resultaatstructuur. Dit is de lijn uit #162 en uit [Public#98](https://github.com/Npuls-OKx/Public/issues/98).

**Verbintenissen lopen ook via een groep.** `Plaatsingsgroep` hangt aan `Persoon` en associeert met vijf verbintenistypen. Daarmee is een verbintenis niet uitsluitend per student vast te leggen. Dit is het antwoord op #217.

**Het examenplan is geen objecttype van OKx.** `Examenplan` staat grijs en kent de summatieve resultaatstructuur. Het examenplan is het document waarin een instelling die structuur publiceert en vaststelt; de structuur zelf is wat uitgewisseld wordt.

## Openstaande punten

| Punt | Waarom het opgelost moet worden | Issue |
|---|---|---|
| De plaat gebruikt drie grijstinten en de legenda kent er een | Een lezer kan nu niet zien of `Leeruitkomst`, de les-laag en `Examenplan` om dezelfde reden buiten scope staan | #215 |
| `Leeruitkomst` is in het model een specialisatie van `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces` en `Competenties / Skills` | Die richting leest als: een leeruitkomst is een soort kerntaak. Waarschijnlijk is bedoeld op welk niveau een leeruitkomst is geformuleerd. Een associatie met een label past daar beter bij dan een specialisatie | nog aan te maken |
| `Opleidingsprogramma specificatie` valt op de plaat buiten de kolom Onderwijsspecificatie | Alleen een tekenkwestie, maar het maakt de kolomindeling automatisch onbetrouwbaar | nog aan te maken |
| 38 objecttypen hebben nog geen vastgestelde definitie | Zonder definitie is de plaat interpreteerbaar en daarmee betwistbaar | #223 |
| Cardinaliteiten staan nog niet in het model | MIM-niveau 2 vraagt erom; nu staat alleen `Minimaal 1` als los label | nog aan te maken |

Relateert aan: #163
