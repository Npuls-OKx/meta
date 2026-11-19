```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers vullen de regels, de business analisten leggen ze naast het model |
| Voorbeeld | [de uitwerking van leerroute 1 met Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Productplaatsing

![De producten rond sjabloon leerroute scenario uitwerking in het informatiemodel, met dit product uitgelicht](<img/leerroute-scenario-uitwerking/product-breakdown.png>)

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft.

Het volgt op het leerroute scenario en toetst het informatiemodel aan die route.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/product-breakdown/README.md).

## Doelstelling document

Dit document legt een leerroute scenario stap voor stap naast het informatiemodel, zodat zichtbaar wordt of het model de werkelijkheid van die route draagt en waar het tekortschiet.

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

Dit document levert **functionele eisen**, samen met de instellingseisen. Zo ziet zo'n eis eruit, met de keten erboven en eronder:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story uit de PoC-inbreng | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Instellingseis, eerder | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| **Functionele eis, uit dit document** | **het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie** |
| Technische eis, verderop | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de soort in die boven het hoofdstuk staat, als verwijzing. De uitgeschreven eis volgt in een eigen ronde, in het register waar hij hoort.

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

Het gaat hier niet alleen om wat er nieuw ontstaat. Een bouwsteen is pas af wanneer ook de **relaties naar eerder ontstane informatie** erin staan: waaraan hangt het nieuwe element, en wat verwijst ernaar. Zonder die relaties is het een losse doos en zegt de uitwerking niets over het model.

Het voorbeeld hieronder is er een met meerdere relaties tegelijk: het kiesbare onderwijsprogrammaonderdeel ontstaat, en hangt aan de opleidingsspecificatie, de keuzedeelruimte en de leeruitkomsten die in eerdere stappen al bestonden.

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-08 - Kiesbaar onderwijsprogrammaonderdeel: keuzedelen en minor](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-08---kiesbaar-onderwijsprogrammaonderdeel-keuzedelen-en-minor)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze processtap uitgelicht, met daarnaast de tabel hieronder ingevuld, en de plaat toont de actor, de processtap en het informatie-element dat daar ontstaat, elk met de term uit de begrippenlijst, **en de relaties naar de informatie-elementen die in eerdere bouwstenen zijn ontstaan**; wat de begrippenlijst niet kent staat als observatie in het slot

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *F1-01* |
| Processtap | *welke stap uit het leerroute scenario* |
| Actor | *wie handelt, met de rol uit het scenario* |
| Applicatiecomponent | *welk systeem daarbij hoort* |
| Ontstaat | *welk objecttype hier voor het eerst bestaat* |
| Relaties naar eerder ontstane elementen | *waaraan het hangt en wat ernaar verwijst, met het nummer van de bouwsteen waar dat element ontstond* |
| Voorbeeldwaarde | *de ingevulde waarde voor deze persona* |

![Voorbeeld van bouwsteen A: het kiesbare onderwijsprogrammaonderdeel, met de relaties naar de opleidingsspecificatie en de keuzedeelruimte die eerder zijn ontstaan](<img/leerroute-scenario-uitwerking/f1-08-kiesbaar-onderwijsprogrammaonderdeel-keuzedelen-en-minor.png>)

*Schrijf hier de uitwerking.*

# Bouwsteen B: uitwisseling

Kopieer dit blok voor elke uitwisseling. Hier gaat niet een los gegeven over de lijn maar het hele samenhangende voorbeeld: het objecttype met alles wat eraan hangt.

Het voorbeeld hieronder is er een met een volle structuur: het verzoek om onderwijsaanbod neemt de specificatiestructuur en de planbare waarden mee, zodat het planningssysteem zonder navraag kan plannen.

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-03---verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze uitwisseling uitgelicht, met daarnaast het volledige ingevulde informatievoorbeeld dat over de lijn gaat, en de plaat toont beide applicatiecomponenten en de richting; het voorbeeld draagt elk objecttype **met zijn relaties**, zodat zichtbaar is wat de ontvanger werkelijk binnenkrijgt en niet alleen welk veld er over de lijn gaat

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *F2-01* |
| Van | *welke applicatiecomponent levert* |
| Naar | *welke applicatiecomponent neemt af* |
| Aanleiding | *welke processtap deze uitwisseling veroorzaakt* |
| Informatievoorbeeld | *het ingevulde voorbeeld, met alle relaties* |
| Informatiestroom | *het nummer uit het leerroute scenario* |

![Voorbeeld van bouwsteen B: het verzoek om onderwijsaanbod gaat met de hele specificatiestructuur en de planbare waarden van de onderwijscatalogus naar het planningssysteem](<img/leerroute-scenario-uitwerking/f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.png>)

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
