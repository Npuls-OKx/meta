```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want de keten raakt de koppelvlakken |
| Voorbeeld | [interactieketen onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md), nog in review als pull request 373 |
| Inleveren | terug naar OKx SI als Word-bestand |

## Productplaatsing

![De producten rond sjabloon interactieketen, met dit product uitgelicht](<img/interactieketen/product-breakdown.png>)

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft.

Het volgt op het leerroute scenario en gaat vooraf aan de koppelvlakspecificatie.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/product-breakdown/README.md).

## Doelstelling document

Dit document legt vast welke diensten elkaar in welke volgorde aanroepen om een keten af te maken, zodat een bouwer weet wat hij moet bouwen en wat hij mag verwachten.

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

Een voorbeeld van de keten, van behoefte tot koppelvlak:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Instellingseis | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functionele eis | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technische eis | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de soort in die boven het hoofdstuk staat, als verwijzing. De uitgeschreven eis volgt in een eigen ronde, in het register waar hij hoort.

## Business analyse en aggregatie van pakket van eisen

Tussen de inbreng van instellingen en leveranciers en dit document zit een analysestap. Houd daarbij drie dingen uit elkaar: wat een product vandaag doet, wat een component moet kunnen, en wat OKx als grootst gemene deler vastlegt. Een leverancier spreekt voor zijn product en niet voor de sector.

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

Een interactieketen is een reeks interacties. Dit document zet er een neer als bouwblok, en dat blok herhaalt zich tot de keten af is.

**De nummering.** Elke interactie draagt een nummer dat begint met `IS`, voor interactiespecificatie. Daarna de afkorting van de keten en een volgnummer: `IS-OA-01` is de eerste interactie van de keten onderwijsaanbod. Kies de afkorting van uw keten en houd hem door het hele document aan; OKx neemt dat nummer over, dus hernummeren achteraf kost iedereen werk.

**De scope van een interactie** bepaalt de business analist: de kleinst mogelijke eenheid die waarde oplevert voor zowel de student als de instelling. Een aanroep die alleen een technische stap zet is te klein; een hele fase is te groot.

# Bouwblok: een interactie

Kopieer dit blok voor elke interactie in de keten. Houd de volgorde van de keten aan, zodat het document van begin tot eind te lezen is.

**Voorbeeld** [Keten onderwijsaanbod, IS-OA-03 Verzoek om aanbod naar planning](https://github.com/Npuls-OKx/meta/blob/e05b4444a29a09b92cc8afd73bce69af78f1ac12/architecture/docs/specificatie/interactieketen-onderwijsaanbod/README.md#is-oa-03-verzoek-om-aanbod-naar-planning)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze interactie uitgelicht, met daarnaast de tabel hieronder ingevuld, en de plaat toont beide componenten, de richting en het bericht; de tabel noemt wat er gebeurt wanneer de aanbieder niet antwoordt, want een keten zonder foutpad is niet te bouwen

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *IS-XX-01* |
| Naam | *wat deze interactie doet, als werkwoord met zijn onderwerp* |
| Aanbieder | *welke component de dienst aanbiedt, met naam en versie* |
| Afnemer | *welke component hem afneemt, met naam en versie* |
| Aanleiding | *welke gebeurtenis deze interactie start* |
| Bericht | *welke informatie meegaat, met de termen uit de begrippenlijst* |
| Informatiestroom | *het nummer uit het leerroute scenario* |
| Antwoord | *wat de afnemer terugkrijgt* |
| Foutpad | *wat er gebeurt wanneer de aanbieder niet of fout antwoordt* |
| Herhaalbaar | *wat een tweede dezelfde aanroep doet* |

*Schrijf hier de uitwerking.*

# De keten

Herhaal het bouwblok hierboven voor elke interactie, in de volgorde van de keten. Zet er een plaat van de hele keten bij zodra alle interacties erin staan: een reeks losse blokken laat niet zien waar de keten wacht, splitst of terugkomt.

*Schrijf hier de uitwerking.*

# Gegevensoorsprong

Per gegeven welke component de bron is, en welke het alleen doorgeeft. Dit hoofdstuk voorkomt dat twee componenten zich later eigenaar noemen van hetzelfde gegeven.

| Gegeven | Bronsysteem | Wie neemt het over | In welke interactie |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

# Afspraken per dienst

Wat elke dienst nakomt, ongeacht wie hem bouwt: wanneer hij antwoordt, wat een herhaalde aanroep doet, en wat er gebeurt wanneer hij niet beschikbaar is. Vaktermen op protocolniveau blijven onvertaald.

| Dienst | Antwoordt binnen | Herhaalde aanroep | Niet beschikbaar |
|---|---|---|---|
| | | | |
| | | | |

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
