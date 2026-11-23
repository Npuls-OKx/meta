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

Elk sjabloononderdeel opent met een opdrachtblok: waar hetzelfde al is uitgewerkt, de acceptatiecriteria waaraan de invulling voldoet, en welke soort eis het oplevert. Het opdrachtblok blijft staan; de uitwerking komt eronder.

## Eisen uit dit document

OKx kent drie soorten eisen. **Instellingseisen** zeggen wat de instelling moet kunnen; zij komen uit de inbreng van de koploperinstellingen in de proef (de PoC-inbreng), de persona's en de leerroute scenario's samen. **Functionele eisen** zeggen wat een component moet doen met welke gegevens; zij komen uit de instellingseisen en de leerroute scenario uitwerking samen. **Technische eisen** zeggen wat er over het koppelvlak gaat; zij komen uit de interactieketens, die zelf uit de eisen voortkomen, en zijn onderdeel van de koppelvlakspecificatie.

**De solutionlaag bouwt op wat hier als eis staat.** De solutionlaag is het deel van OKx dat de koppelvlakken ontwerpt: het team systeem en informatie (OKx SI), samen met de leveranciers. OKx SI neemt de instellingseisen en de functionele eisen over en vertaalt ze met de leveranciers naar technische eisen. Een behoefte bereikt de leveranciers via een uitgeschreven eis in dit pakket.

Elk onderdeel levert een eigen soort. De reis van een persona brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemonderdeel zegt wat een component moet doen. Een interactie zegt wat er over het koppelvlak gaat. Het opdrachtblok noemt welke soort daar hoort.

| Soort | Komt uit | Zegt wat |
|---|---|------------------------------------|
| Instellingseis | de PoC-inbreng, de persona's en de leerroute scenario's samen | de instelling moet kunnen om de scenario's te realiseren |
| Functionele eis | de instellingseisen en de leerroute scenario uitwerking | een component moet doen met welke gegevens |
| Technische eis | de interactieketens, die zelf uit de eisen voortkomen | er over het koppelvlak gaat en in welke vorm |

Dit document levert **behoeften, geschreven als user story**; samen met de PoC-inbreng en het leerroute scenario worden dat instellingseisen. Zo ziet zo'n eis eruit, met de keten erboven en eronder:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| **User story, uit dit document** | **Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is** |
| Instellingseis, verderop | de instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst |
| Functionele eis, verderop | het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie |
| Technische eis, verderop | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

## Kwaliteit van een eis

Een eis is bruikbaar wanneer een leverancier hem kan lezen zonder de instelling te bellen. Wat hier staat is een voorstel voor een sectorafspraak: opgesteld uit de inbreng van afzonderlijke instellingen, vastgelegd als afspraak, en daarna de grond voor de technische specificatie. Schrijf elke eis uit op de plek waar hij ontstaat, en toets hem aan de criteria hieronder.

**Een user story:**

1. heeft de vorm `Als <persona> wil ik <wat> met als doel dat <waarde>`;
2. noemt de stap van de reis waarin de behoefte ontstaat;
3. noemt wat de persona wil kunnen en waarom; welk systeem dat draagt volgt in de eisen;
4. is herkenbaar bij meerdere instellingen; wat bij een instelling speelt staat onder Afwijkingen per instelling.

| Soort | Zwak | Wat eraan ontbreekt | Sterk |
|---|--------|------|------------|
| user story | Als student wil ik een overzichtelijke app voor mijn keuzedelen | noemt een systeem; de stap en de waarde ontbreken | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| user story | Als instelling willen wij beter kunnen plannen | noemt een organisatie in plaats van een persona; de stap en de waarde ontbreken | Als planner wil ik de haalbaarheid van een opleiding bepalen voordat het onderwijsaanbod wordt gepubliceerd, met als doel dat studenten zich alleen oriënteren op aanbod dat de instelling kan uitvoeren |

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

Dit document draagt een of meer persona's. Herhaal de twee sjabloononderdelen hieronder per persona tot elke mens uit het leerroute scenario een persona heeft.

**Een persona is een student of een actor binnen de instelling.** De onderwijsontwerper, de planner, de roostermaker, de studieloopbaanbegeleider, de examinator en het leerbedrijf zijn net zo goed een persona wanneer de route langs hen loopt. Beschrijf naast de student minstens een persona vanuit de instelling: de student laat zien wat de route moet opleveren, de medewerker laat zien wat de instelling daarvoor moet kunnen. De bestaande voorbeelden Jochem, Linda en Larissa zijn alle drie student; de persona's vanuit de instelling zijn wat dit document toevoegt.

**Schrijf in tandem met het leerroute scenario.** Het procesbeeld daar bepaalt welke stappen deze persona doorloopt; wat deze persona meemaakt scherpt dat procesbeeld aan. Verschilt de stappenreeks hier van die in het scenario, dan is een van de twee nog niet af.

**Een persona is geen gemiddelde.** Een gemiddelde student bestaat niet en is nergens aan te toetsen. Kies een herkenbaar iemand, met een naam, een situatie en een reden waarom hij deze route loopt.

**Elke behoefte wordt een user story.** Waar de persona iets nodig heeft dat vandaag ontbreekt of misloopt, staat dat als user story bij de stap. Het leerroute scenario leidt daar de instellingseisen uit af; een behoefte die hier ontbreekt, komt daar niet vanzelf boven.

# Sjabloononderdeel: het portret

Kopieer dit sjabloononderdeel voor elke persona. Begin met wie het is en waarom deze route bij hem hoort; de reis komt in het volgende onderdeel.

**Voorbeeld** [Persona Jochem, Persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#persona-jochem)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. het portret staat in lopende tekst, met het beeld van de persona erbij wanneer dat er is;
2. de tabel is volledig ingevuld; een veld dat voor deze persona vervalt draagt de reden;
3. het portret noemt wie deze mens is, waarom hij juist deze route loopt en wat hem daarin beweegt; een lezer kan hem navertellen zonder het document erbij;
4. het veld Rol noemt of dit een student is of een actor binnen de instelling, met de naam van de rol;
5. het leerroute scenario waar deze persona bij hoort is met een link genoemd;
6. het veld Wat het moeilijk maakt noemt minstens een concrete situatie in de route, want daaruit komen de behoeften.

**Eisen** *dit hoofdstuk levert geen eis op; het geeft de context waarin de eisen van de andere hoofdstukken te lezen zijn*

**Ingevuld voorbeeld** uit Persona Jochem en Leerroute 1 scenario:

| Veld | Invulling |
|---|------------------------------------------------|
| Naam | Jochem |
| Rol | student |
| Situatie | 17 jaar, komt van het vmbo, volgt de opleiding Apothekersassistent (mbo niveau 4) en start in september |
| Waarom deze route | hij volgt de route zoals de instelling haar heeft ontworpen en heeft geen ondersteunings- of maatwerkvraag; alleen zijn keuzedelen kiest hij zelf |
| Wat hem beweegt | hij wil apothekersassistent worden en later in een openbare apotheek werken |
| Wat het moeilijk maakt | zijn eerste keuzedeel kan buiten de onderwijsperiode of de onderwijslocatie van zijn voorkeur vallen; dan blijft zijn keuzedeelruimte leeg en loopt hij studievertraging op |
| Waaraan hij merkt dat het goed gaat | hij weet bij de start welke modules hij volgt en wat er van hem wordt verwacht, en hij ziet welke leeruitkomsten hij heeft behaald |

**Vul in:**

| Veld | Invulling |
|---|------------------------------------------------|
| Naam | *de naam waaronder deze persona in alle documenten terugkomt* |
| Rol | *student, of een actor binnen de instelling: onderwijsontwerper, planner, roostermaker, studieloopbaanbegeleider, examinator, leerbedrijf* |
| Situatie | *voor een student: leeftijd, vooropleiding, opleiding en instroommoment; voor een medewerker: afdeling, taak in de route en de systemen waarmee hij werkt* |
| Waarom deze route | *wat maakt dat juist deze leerroute bij hem hoort* |
| Wat hem beweegt | *waar hij het voor doet, en wat hij wil vermijden* |
| Wat het moeilijk maakt | *waar hij in deze route tegenaan loopt* |
| Waaraan hij merkt dat het goed gaat | *het teken dat voor hem telt* |

![Voorbeeld van een portret: Jochem, de persona van leerroute 1](<img/persona/npuls-leerroute1-regulier-jochem.png>)

*Schrijf hier de uitwerking.*

# Sjabloononderdeel: de reis per processtap

Kopieer dit sjabloononderdeel voor elke persona, direct onder zijn portret. De stappen komen uit het procesbeeld van het leerroute scenario; neem ze over in dezelfde volgorde, zodat de reizen van twee persona's naast elkaar te leggen zijn.

De uitgewerkte vorm staat in [persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md), die elf stappen doorloopt vanaf orienteren tot het diploma.

**Voorbeeld** [Persona Jochem, Studentjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studentjourney)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. er staat een tabel met een rij per processtap, met dezelfde stappen in dezelfde volgorde als het procesbeeld in het leerroute scenario;
2. er staat een procesplaat in mermaid, BPMN, UML of vergelijkbaar van de reis;
3. elke rij noemt wat deze persona doet, wat hij op dat moment moet weten en wat het met hem doet;
4. elke stap waar de persona iets nodig heeft dat vandaag ontbreekt of misloopt, draagt een user story; een stap die soepel loopt draagt in de kolom User story het woord geen;
5. elke user story voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis);
6. een stap die in het scenario staat en hier ontbreekt, staat onder Observaties en signaleringen.

**User stories** *de behoeften die hier naar boven komen; schrijf elke behoefte uit als user story, bij de stap waar zij ontstaat*

**Ingevuld voorbeeld** uit Persona Jochem en Leerroute 1 scenario:

| Processtap | Wat hij doet | Wat hij moet weten | Wat het met hem doet | User story |
|---|---|---|---|---|
| Informeren | bekijkt bij de start het geplande leertraject, met de modules, de BPV en de examenplanning | welke modules hij volgt en wat er van hem wordt verwacht | rust: hij overziet zijn opleiding | geen |
| Kiezen keuzedelen | bekijkt het aanbod van keuzedelen en stelt een voorkeurslijst op, met per voorkeur de onderwijsperiode en optioneel de onderwijslocatie | welke keuzedelen in zijn keuzedeelruimte passen, hoeveel SBU hij nog nodig heeft, en waar en wanneer elk keuzedeel wordt gegeven | onzekerheid: past zijn eerste keuze niet, dan dreigt een lege keuzedeelruimte en studievertraging | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |

**Ingevuld voorbeeld** uit Leerroute 1 scenario, fase 2, voor de persona planner:

| Processtap | Wat hij doet | Wat hij moet weten | Wat het met hem doet | User story |
|---|---|---|---|---|
| Publiceren en planbaar maken | bepaalt of de opleiding haalbaar is binnen de strategische jaarplanning, met de mensen en middelen van alle opleidingen | welke specificaties planbaar zijn, met hun tijdvensters, capaciteit, expertise en faciliteit | een onhaalbaar plan betekent dat er in september geen aanbod is om op te oriënteren | Als planner wil ik de haalbaarheid van een opleiding bepalen voordat het onderwijsaanbod wordt gepubliceerd, met als doel dat studenten zich alleen oriënteren op aanbod dat de instelling kan uitvoeren |

**Vul in:**

| Processtap | Wat hij doet | Wat hij moet weten | Wat het met hem doet | User story |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

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
