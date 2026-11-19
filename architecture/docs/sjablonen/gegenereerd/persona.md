```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers nemen het voortouw, want zij kennen de instellingspraktijk per stap |
| Voorbeeld | [persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Productplaatsing

![De producten rond sjabloon persona, met dit product uitgelicht](<img/persona/product-breakdown.png>)

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft.

Het wordt samen geschreven met het [leerroute scenario](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md), waar het procesbeeld de stappen bepaalt.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/product-breakdown/README.md).

## Doelstelling document

Dit document maakt een leerroute invoelbaar door haar te volgen door de ogen van de mensen die haar doorlopen, zodat een ontwerpkeuze te toetsen is aan wat zij ervan merken.

Elk hoofdstuk opent met een blok dat zegt wat er wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking.

## Eisen uit dit document

OKx kent drie soorten eisen. **Instellingseisen** zeggen wat de instelling moet kunnen; zij komen uit de inbreng van de koploperinstellingen, de persona's en de leerroute scenario's samen. **Functionele eisen** zeggen wat een component moet doen met welke gegevens; zij komen uit de leerroute scenario uitwerking. **Technische eisen** zeggen wat er over het koppelvlak gaat; die liggen in de interactieketen zelf vast en zijn onderdeel van de koppelvlakspecificatie.

**Dit document bevat die eisen niet; het levert eraan.** Noteer per hoofdstuk alleen de nummers; de eis zelf wordt elders uitgeschreven.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort, en noteert de nummers; de eis zelf wordt elders uitgeschreven.

| Soort | Komt uit | Zegt wat |
|---|---|------------------------------------|
| Instellingseis | de PoC-inbreng, de persona's en de leerroute scenario's | de instelling moet kunnen om de route te draaien |
| Functionele eis | de leerroute scenario uitwerking | een component moet doen met welke gegevens |
| Technische eis | de interactieketen en haar interacties | er over het koppelvlak gaat en in welke vorm |

Een voorbeeld van de keten, van behoefte tot koppelvlak:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Instellingseis | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functionele eis | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technische eis | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de soort in die boven het hoofdstuk staat, als verwijzing. De uitgeschreven eis volgt in een eigen ronde, in het register waar hij hoort.

## Business analyse en aggregatie van pakket van eisen

Tussen de inbreng van instellingen en dit document zit een analysestap. Haal op bij meerdere instellingen, zoek wat zij delen, en schrijf dat op. Wat een persona draagt is wat bij meerdere instellingen zo werkt, niet wat bij een ervan zo heet.

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

Dit document draagt een of meer persona's. Herhaal de twee bouwblokken hieronder per persona tot het leerroute scenario zijn mensen heeft.

**Een persona hoeft geen student te zijn.** Een planner, een examinator, een studieloopbaanbegeleider of een leerbedrijf is net zo goed een persona wanneer de route langs hem loopt. Een leerroute scenario kan er dus meerdere dragen, en dat is eerder regel dan uitzondering: een route die alleen vanuit de student is beschreven, laat niet zien wat zij van de instelling vraagt.

**Schrijf in tandem met het leerroute scenario.** Het procesbeeld daar bepaalt welke stappen deze persona doorloopt; wat deze persona meemaakt scherpt dat procesbeeld aan. Verschilt de stappenreeks hier van die in het scenario, dan is een van de twee nog niet af.

**Een persona is geen gemiddelde.** Een gemiddelde student bestaat niet en is nergens aan te toetsen. Kies een herkenbaar iemand, met een naam, een situatie en een reden waarom hij deze route loopt.

# Bouwblok: het portret

Kopieer dit blok voor elke persona. Begin met wie het is en waarom deze route bij hem hoort; de reis komt in het volgende blok.

**Voorbeeld** [Persona Jochem, Persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#persona-jochem)

**Acceptatiecriteria** een portret in lopende tekst, met het beeld van de persona erbij wanneer dat er is, in het kader van het leerroute scenario waar deze persona bij hoort, en het portret noemt wie deze mens is, waarom hij juist deze route loopt, en wat hem daarin beweegt; een lezer moet hem kunnen navertellen zonder het document erbij

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

| Veld | Invulling |
|---|------------------------------------------------|
| Naam | *de naam waaronder deze persona in alle documenten terugkomt* |
| Rol | *student, planner, examinator, leerbedrijf of een andere belanghebbende* |
| Situatie | *leeftijd, vooropleiding, opleiding en instroommoment, of de positie binnen de instelling* |
| Waarom deze route | *wat maakt dat juist deze leerroute bij hem hoort* |
| Wat hem beweegt | *waar hij het voor doet, en wat hij wil vermijden* |
| Wat het moeilijk maakt | *waar hij in deze route tegenaan loopt* |
| Waaraan hij merkt dat het goed gaat | *het teken dat voor hem telt* |

![Voorbeeld van een portret: Jochem, de persona van leerroute 1](<img/persona/npuls-leerroute1-regulier-jochem.png>)

*Schrijf hier de uitwerking.*

# Bouwblok: de reis per processtap

Kopieer dit blok voor elke persona, direct onder zijn portret. De stappen komen uit het procesbeeld van het leerroute scenario; neem ze over in dezelfde volgorde, zodat de reizen van twee persona's naast elkaar te leggen zijn.

De uitgewerkte vorm staat in [persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md), die elf stappen doorloopt vanaf orienteren tot het diploma.

**Voorbeeld** [Persona Jochem, Studentjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studentjourney)

**Acceptatiecriteria** een tabel met een rij per processtap uit het leerroute scenario, en daarnaast een procesplaat in mermaid, BPMN, UML of vergelijkbaar, met dezelfde stappen en in dezelfde volgorde als het procesbeeld in het leerroute scenario, en elke stap noemt wat deze persona doet, wat hij op dat moment moet weten en wat het met hem doet; een stap die in het scenario staat en hier niet, staat als observatie in het slot

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

| Processtap | Wat hij doet | Wat hij moet weten | Wat het met hem doet |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

# De persona's

Herhaal hieronder het portret en de reis voor elke persona van dit leerroute scenario. Zet de student vooraan; de persona's vanuit de instelling volgen in de volgorde waarin zij de route raken.

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
