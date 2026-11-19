```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want het viewpoint hangt aan het ArchiMate-model |
| Voorbeeld | [informatiemodel OKx](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Productplaatsing

![De producten rond sjabloon informatiemodel viewpoint, met dit product uitgelicht](<img/informatiemodel-viewpoint/product-breakdown.png>)

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft.

Het staat naast alle andere producten en levert de begrippen waarin zij spreken.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/product-breakdown/README.md).

## Doelstelling document

Dit document legt vast welke objecttypen er zijn, hoe zij samenhangen en voor welke lezer de plaat bedoeld is, zodat een leverancier dezelfde begrippen leest als een onderwijskundige.

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

Tussen de inbreng van instellingen en dit document zit een analysestap. Een objecttype hoort hier wanneer meerdere instellingen het nodig hebben, niet wanneer een instelling het zo genoemd heeft. Hoe een instelling haar onderwijs inricht blijft haar keuze: OKx legt alleen de vorm van de uitwisseling vast.

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

# Informatiemodel OKx

**Voorbeeld** [Informatiemodel OKx, Informatiemodel OKx](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#informatiemodel-okx)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Context

**Voorbeeld** [Informatiemodel OKx, Context](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#context)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Inleiding

**Voorbeeld** [Informatiemodel OKx, Inleiding](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#inleiding)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Doel

**Voorbeeld** [Informatiemodel OKx, Doel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#doel)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Scope

**Voorbeeld** [Informatiemodel OKx, Scope](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#scope)

**Acceptatiecriteria** een beeld, een ingevulde tabel, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| | Niveau | Waar het staat |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

![Informatiemodel OKx, versie v0.2 van 14 oktober 2026](<img/informatiemodel-viewpoint/OKx informatiemodel v0.2.jpg>)

*Schrijf hier de uitwerking.*

## Lezers en detailniveau

**Voorbeeld** [Informatiemodel OKx, Lezers en detailniveau](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#lezers-en-detailniveau)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| | |
|---|---|
| | |
| | |

*Schrijf hier de uitwerking.*

## Begrippenfamilies

**Voorbeeld** [Informatiemodel OKx, Begrippenfamilies](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#begrippenfamilies)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| Begrip | Wat het is | Beantwoordt de vraag |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

*Schrijf hier de uitwerking.*

## Notatie

**Voorbeeld** [Informatiemodel OKx, Notatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#notatie)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| | Relatie | Betekenis in dit model |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

*Schrijf hier de uitwerking.*

## Ontwerpkeuzes

**Voorbeeld** [Informatiemodel OKx, Ontwerpkeuzes](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#ontwerpkeuzes)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Verwante documenten

**Voorbeeld** [Informatiemodel OKx, Verwante documenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#verwante-documenten)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

| Document | Verhouding |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |

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
