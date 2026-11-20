```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wie dit invult | de adviesgroep. Suggestie: de BOP-adviseurs en de business analisten samen, met de onderwijskundige kant bij de adviesgroep zelf |
| Voorbeeld | [leerroute 1 scenario](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Productplaatsing

![De producten rond sjabloon leerroute scenario, met dit product uitgelicht](<img/leerroute-scenario/product-breakdown.png>)

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft.

Het bouwt op een of meer persona's, en gaat vooraf aan de uitwerking en de interactieketen.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/product-breakdown/README.md).

## Doelstelling document

Dit document werkt een Npuls-leerroute uit tot het punt waarop duidelijk is welke informatie waarheen moet, zodat de solutionlaag erop kan bouwen zonder de onderwijskundige keuze over te nemen.

Elk hoofdstuk opent met een blok dat zegt wat er wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking.

## Eisen uit dit document

OKx kent drie soorten eisen. **Instellingseisen** zeggen wat de instelling moet kunnen; zij komen uit de inbreng van de koploperinstellingen, de persona's en de leerroute scenario's samen. **Functionele eisen** zeggen wat een component moet doen met welke gegevens; zij komen uit de instellingseisen en de leerroute scenario uitwerking samen. **Technische eisen** zeggen wat er over het koppelvlak gaat; zij komen uit de interactieketens, die zelf uit de eisen voortkomen, en zijn onderdeel van de koppelvlakspecificatie.

**Dit document bevat die eisen niet; het levert eraan.** Noteer per hoofdstuk alleen de nummers; de eis zelf wordt elders uitgeschreven.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort, en noteert de nummers; de eis zelf wordt elders uitgeschreven.

| Soort | Komt uit | Zegt wat |
|---|---|------------------------------------|
| Instellingseis | de PoC-inbreng, de persona's en de leerroute scenario's samen | een instelling wil kunnen om de scenario's te realiseren |
| Functionele eis | de instellingseisen en de leerroute scenario uitwerking | een component moet doen met welke gegevens |
| Technische eis | de interactieketens, die zelf uit de eisen voortkomen | er over het koppelvlak gaat en in welke vorm |

Dit document levert **instellingseisen** en **functionele eisen**; de technische eisen volgen later, in de interactieketen. Zo ziet zo'n eis eruit, met de keten erboven en eronder:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story uit de PoC-inbreng | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| **Instellingseis, uit dit document** | **de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst** |
| Functionele eis, verderop | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technische eis, verderop | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de soort in die boven het hoofdstuk staat, als verwijzing. De uitgeschreven eis volgt in een eigen ronde, in het register waar hij hoort.

## Business analyse en aggregatie van pakket van eisen

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier dubbel, want een leerroute scenario is wat OKx als afspraak vastlegt: een procesgewoonte van een instelling die hier als kader belandt, wordt een eis aan elke leverancier.

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

Een leerroute scenario is opgebouwd uit vijf bouwblokken. Het routeprofiel staat er een keer in; de andere vier herhalen zich tot de route gedekt is.

| Bouwblok | Hoe vaak | Levert |
|---|---|---|
| Routeprofiel | een keer | context |
| Reis | per persona | user stories en instellingseisen |
| Scenario binnen de route | per scenario | instellingseisen |
| Procesfase | per fase | instellingseisen |
| Informatie en systemen | per fase, of een keer voor de route | functionele eisen |

Technische eisen horen hier niet: die volgen later, in de interactieketen. De uitgewerkte vorm staat in [leerroute 1 scenario](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md); neem daar de diepgang van over, niet de hoofdstukindeling. Wat leerroute 1 eigen is, zoals keuzedelen, hoort alleen in een route die het ook kent.

# Notatie van eisen

Elke eis krijgt een nummer en verwijst naar het bouwblok waaruit hij komt. Een eis is een zin die te toetsen is, zonder toelichting; de toelichting staat in het bouwblok zelf.

| Soort | Nummer | Vorm van de zin |
|---|---|---|
| Instellingseis | `IE-LR<route>-<volgnummer>`, bijvoorbeeld `IE-LR2-03` | De instelling kan ... |
| Functionele eis | `FE-LR<route>-<volgnummer>`, bijvoorbeeld `FE-LR2-07` | Het <component> ... |

Een functionele eis noemt de instellingseis waaruit hij komt. Een voorbeeld uit leerroute 1:

| Nummer | Eis | Komt uit |
|---|---|---|
| IE-LR1-01 | De instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst | reis van de student, stap kiezen |
| FE-LR1-01 | Het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie | IE-LR1-01, bouwblok informatie en systemen |

# Bouwblok: routeprofiel

Dit blok staat er een keer in, vooraan.

**Voorbeeld** [Leerroute 1 scenario, 3.2.1.1 Leerroute 1 — Regulier](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-leerroute-1--regulier)

**Acceptatiecriteria** het conceptbeeld van de route uit de Npuls-leerroutereeks, met de tabel hieronder ingevuld, en het profiel zegt in een zin wat deze route onderscheidt van leerroute 1, de reguliere en aanbodgedreven route die als vergelijkingspunt dient

**Eisen** *dit hoofdstuk levert geen eis op; het geeft de context waarin de eisen van de andere hoofdstukken te lezen zijn*

| Veld | Invulling |
|---|------------------------------------------------|
| Route | *nummer en naam uit de negen Npuls-leerroutes* |
| Persona's | *wie deze route doorlopen, met een link naar het persona-document* |
| Sturing | *aanbodgedreven, vraaggedreven of hybride, en voor welk deel van de route* |
| Verschil met leerroute 1 | *wat gelijk blijft en wat anders gaat, in tempo, keuzeruimte en rollen* |
| Eindbeeld | *waar dit scenario eindigt, en waarom daar* |

![Voorbeeld van een routeprofiel: het conceptbeeld van leerroute 1](<img/leerroute-scenario/Npuls_leerroute_1.jpg>)

*Schrijf hier de uitwerking.*

# Bouwblok: reis

Kopieer dit blok voor elke persona van de route: de student, en elke rol vanuit de instelling waar de route langs loopt. De stappen van twee reizen dragen dezelfde namen, zodat zij naast elkaar te leggen zijn.

**Voorbeeld** [Leerroute 1 scenario, 3.2.1.1 De student beleving - De Student Journey](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-de-student-beleving---de-student-journey)

**Acceptatiecriteria** een procesplaat in mermaid, BPMN, UML of vergelijkbaar van de reis van een persona, in het kader van de persona's van deze route, met een link naar het persona-document, en de plaat toont de stappen in volgorde, met de terugweg waar die bestaat; de tabel noemt per stap wat deze persona doet, wat hij moet weten en welk systeem hij raakt; elke instellingseis die eruit volgt staat genummerd in de laatste kolom

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

| Stap | Wat de persona doet | Wat hij moet weten | Systeem | Instellingseis |
|---|---|---|---|---|
| | | | | *IE-LR..-..* |
| | | | | |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

# Bouwblok: scenario binnen de route

Kopieer dit blok per scenario. Vier scenario's keren in elke route terug: het nominale verloop, incidenteel temporiseren, incidenteel versnellen en incidenteel hybride.

*Optioneel: het nominale verloop hoort er altijd in; een incidentele variant of een routespecifiek scenario alleen wanneer de route dat kent. Geldt het niet voor deze route, laat de kop staan met die reden eronder.*

**Voorbeeld** [Leerroute 1 scenario, Scenario's binnen deze leerroute](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#scenarios-binnen-deze-leerroute)

**Acceptatiecriteria** een beschrijving in vier vaste delen, met een procesplaat in mermaid, BPMN, UML of vergelijkbaar wanneer het verloop afwijkt van de reis, in het kader van een persona en het routeprofiel, en het scenario noemt de uitgangssituatie, de aanleiding, het verloop en het eindbeeld; wat alleen in deze route voorkomt staat erbij met de reden

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

| Veld | Invulling |
|---|------------------------------------------------|
| Scenario | *naam, en of het nominaal, incidenteel of routespecifiek is* |
| Uitgangssituatie | *wat er al staat voordat het begint* |
| Aanleiding | *wat er verandert, en op welk moment* |
| Verloop | *wie wat doet, in welke volgorde* |
| Eindbeeld | *wat er klaar is wanneer het scenario eindigt* |
| Instellingseisen | *IE-LR..-.., een regel per eis* |

*Schrijf hier de uitwerking.*

# Bouwblok: procesfase

Kopieer dit blok per fase. Houd de fasenamen van leerroute 1 aan waar de fase hetzelfde is; een eigen fase krijgt een eigen naam met de reden erbij.

**Voorbeeld** [Leerroute 1 scenario, Fase 1 — Kwalificatiekader analyseren en grofmazig ontwerpen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen)

**Acceptatiecriteria** een procesplaat in mermaid, BPMN, UML of vergelijkbaar van de fase aan de kant van de instelling, naast de reis van de persona's te leggen, met het MORA-hoofdproces erbij, en de plaat toont wie handelt en met welk systeem, met het foutpad erbij; elke stap die de instelling moet kunnen, staat als genummerde instellingseis in de tabel

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

| Processtap | Rol | Systeem | Wat de instelling moet kunnen | Instellingseis |
|---|---|---|---|---|
| | | | | *IE-LR..-..* |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

# Bouwblok: informatie en systemen

Kopieer dit blok per procesfase, of vul het een keer in voor de hele route wanneer de fasen dezelfde informatie raken.

**Voorbeeld** [Leerroute 1 scenario, Betrokken informatie bij proces](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze fase uitgelicht op de informatiestromen hoofdplaat, met daarnaast de tabel hieronder ingevuld, en elk informatieobject draagt de term uit de begrippenlijst en heeft precies een bronsysteem; elke functionele eis noemt het component en de instellingseis waaruit hij komt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| Informatieobject | Bronsysteem | Wie leest of bewerkt | Functionele eis | Komt uit |
|---|---|---|---|---|
| | | | *FE-LR..-..* | *IE-LR..-..* |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

# Uitwerking

Zet hieronder eerst het routeprofiel, en herhaal daarna de bouwblokken tot de hele route gedekt is: de reizen, de scenario's, en per fase het proces met zijn informatie en systemen.

*Schrijf hier de uitwerking.*

# Eisenoverzicht

Alle eisen uit de bouwblokken hierboven, bij elkaar. Dit overzicht is wat de volgende producten overnemen.

| Nummer | Eis | Komt uit bouwblok | Komt uit eis of story |
|---|---|---|---|
| IE-LR..-01 | | | |
| IE-LR..-02 | | | |
| FE-LR..-01 | | | |
| FE-LR..-02 | | | |

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
