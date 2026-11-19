| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Versie | 0.0.1 |
| Uitgegeven door | OKx, pijler Leren Zonder Drempels (Npuls) |
| Ingevuld door | *naam en organisatie van de invuller* |
| Datum | *datum van invullen* |
| Inleveren | terug naar OKx SI als Word-bestand |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een leerroute scenario uitwerking: het scenario stap voor stap naast het informatiemodel gelegd, als een herhaling van twee bouwstenen tot de hele route gedekt is |
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers vullen de regels, de business analisten leggen ze naast het model |
| Voorbeeld | [de uitwerking van leerroute 1 met Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |

Elk hoofdstuk opent met een blok dat zegt wat er van dat hoofdstuk wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Doelstelling document

Dit document legt een leerroute scenario stap voor stap naast het informatiemodel, zodat zichtbaar wordt of het model de werkelijkheid van die route draagt en waar het tekortschiet.

## Pakket van eisen

Het pakket van eisen komt uit de gedeelde analyse van alles wat scholen hebben ingebracht, geinventariseerd in de PoC-sessies met de koploperscholen. De grootst gemene deler daaruit is wat OKx vastlegt.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort.

| Laag | Waar die ontstaat | Voorbeeld |
|---|---|------------------------------------|
| User story | in een journey of een scenario | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | in een procesbeschrijving | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | in een gegevens- of systeemhoofdstuk | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technical requirement | in een interactiehoofdstuk | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de laag in die boven het hoofdstuk staat. De lagen eronder volgen in een eigen ronde, met dit document als bron.

## Business analyse en aggregatie van pakket van eisen

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier sterker dan elders, omdat een voorbeeld overtuigt: een regel die uit een enkele instelling komt en hier als voorbeeld staat, leest als sectorpraktijk.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

Een hoofdstuk is een interactie, en de business analist bepaalt waar hij begint en eindigt. Kies de kleinst mogelijke eenheid die waarde oplevert voor zowel de student als de instelling: groter dan een enkele interactie, kleiner dan het hele ecosysteem. Een scope die daarboven zit levert een eis die niemand kan bouwen, een scope die daaronder zit levert een eis die niemand mist.

```{=openxml}
<w:p><w:pPr><w:pStyle w:val="Kop1zondernummer"/></w:pPr>
<w:r><w:t>Inhoudsopgave</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>
<w:r><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="separate"/></w:r>
<w:r><w:t xml:space="preserve">Werk deze inhoudsopgave bij met Ctrl+A en F9.</w:t></w:r>
<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Werkwijze

Dit document is een herhaling van twee bouwstenen. Bouwsteen A legt een processtap vast: wie handelt, en welk informatie-element daar ontstaat. Bouwsteen B legt een uitwisseling vast: het hele ingevulde informatievoorbeeld dat van de ene applicatiecomponent naar de andere gaat.

Herhaal A tot er een uitwisseling plaatsvindt, zet dan B neer, en ga verder met A. Stop wanneer het hele leerroute scenario is doorlopen. Het aantal bouwstenen ligt niet vast; de dekking van het scenario bepaalt hoeveel het er zijn.

De uitgewerkte vorm staat in [de uitwerking van leerroute 1 met Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md). Die telt acht fasen en ruim honderd bouwstenen; dat is de maat waar dit document naartoe werkt, niet de vorm die het moet overnemen.

# Bouwsteen A: processtap

Kopieer dit blok voor elke processtap. De nummering volgt het leerroute scenario: F1-01 is de eerste stap van fase 1.

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-1-kwalificatiekader-analyseren-en-grofmazig-ontwerpen)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze processtap uitgelicht, met daarnaast de tabel hieronder ingevuld, en de plaat toont de actor, de processtap en het informatie-element dat daar ontstaat, elk met de term uit de begrippenlijst; wat die lijst niet kent staat als observatie in het slot

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *F1-01* |
| Processtap | *welke stap uit het leerroute scenario* |
| Actor | *wie handelt, met de rol uit het scenario* |
| Applicatiecomponent | *welk systeem daarbij hoort* |
| Ontstaat | *welk objecttype hier voor het eerst bestaat* |
| Hangt aan | *aan welk bestaand objecttype het hangt* |
| Voorbeeldwaarde | *de ingevulde waarde voor deze persona* |

*Schrijf hier de uitwerking.*

# Bouwsteen B: uitwisseling

Kopieer dit blok voor elke uitwisseling. Hier gaat niet een los gegeven over de lijn maar het hele samenhangende voorbeeld: het objecttype met alles wat eraan hangt.

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 2: Publiceren en planbaar maken](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-2-publiceren-en-planbaar-maken)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze uitwisseling uitgelicht, met daarnaast het volledige ingevulde informatievoorbeeld dat over de lijn gaat, en de plaat toont beide applicatiecomponenten en de richting; het voorbeeld draagt elk objecttype met zijn relaties, zodat zichtbaar is wat de ontvanger werkelijk binnenkrijgt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *F2-01* |
| Van | *welke applicatiecomponent levert* |
| Naar | *welke applicatiecomponent neemt af* |
| Aanleiding | *welke processtap deze uitwisseling veroorzaakt* |
| Informatievoorbeeld | *het ingevulde voorbeeld, met de relaties* |
| Informatiestroom | *het nummer uit het leerroute scenario* |

*Schrijf hier de uitwerking.*

# Uitwerking

Herhaal hieronder bouwsteen A en bouwsteen B tot het hele leerroute scenario is doorlopen. Houd de volgorde van het scenario aan, zodat beide documenten naast elkaar te leggen zijn.

*Schrijf hier de uitwerking.*

# Hiaten in het model

Welke bouwstenen niet in het informatiemodel pasten, per regel met wat ontbrak. Dit hoofdstuk is de opbrengst van de uitwerking: een voorbeeld dat overal paste heeft niets gemeten. Wat hier staat wordt een functional requirement.

| Nummer | Wat ontbrak | Wat er nodig is |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

*Schrijf hier de uitwerking.*

# Afwijkingen per instelling

Wat bij een instelling anders gaat dan hierboven staat, per regel met de instelling erbij. Dit is geen restcategorie: hier staat het materiaal waaruit blijkt of de grootst gemene deler houdbaar is.

| Instelling | Hoofdstuk | Wat daar anders gaat |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

# Observaties en signaleringen

Wat tijdens het invullen opviel en wat openstaat, genummerd. Een observatie is wat u zag; een signalering is wat daarmee moet gebeuren, bijvoorbeeld richting OKx, richting een standaard of richting het eigen bestuur.

| Nummer | Hoofdstuk | Observatie | Wat er nodig is |
|---|---|---|------------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
