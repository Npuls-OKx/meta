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
| Wat dit wordt | een viewpoint op het informatiemodel: welke objecttypen er zijn, hoe zij samenhangen, en voor welke lezer deze plaat bedoeld is |
| Wie dit invult | de adviesgroep. Suggestie: de business analisten met Niels, want het viewpoint hangt aan het ArchiMate-model |
| Voorbeeld | [informatiemodel OKx](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md) |

Elk hoofdstuk opent met een blok dat zegt wat er van dat hoofdstuk wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Van user story naar eis

Het pakket van eisen komt uit de gedeelde analyse van alles wat scholen hebben ingebracht, geinventariseerd in de PoC-sessies met de koploperscholen. De grootst gemene deler daaruit is wat OKx vastlegt.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort.

| Laag | Waar die ontstaat | Voorbeeld |
|---|---|------------------------------------|
| User story | in een journey of een scenario | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | in een procesbeschrijving | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | in een gegevens- of systeemhoofdstuk | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technical requirement | in een interactiehoofdstuk | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de laag in die boven het hoofdstuk staat. De lagen eronder volgen in een eigen ronde, met dit document als bron.

## De grootst gemene deler

Tussen de inbreng van instellingen en dit document zit een analysestap. Een objecttype hoort hier wanneer meerdere instellingen het nodig hebben, niet wanneer een instelling het zo genoemd heeft. Hoe een instelling haar onderwijs inricht blijft haar keuze: OKx legt alleen de vorm van de uitwisseling vast.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

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

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Context

**Voorbeeld** [Informatiemodel OKx, Context](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#context)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Inleiding

**Voorbeeld** [Informatiemodel OKx, Inleiding](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#inleiding)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Doel

**Voorbeeld** [Informatiemodel OKx, Doel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#doel)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Scope

**Voorbeeld** [Informatiemodel OKx, Scope](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#scope)

**Acceptatiecriteria** een beeld, een ingevulde tabel, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

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

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| | |
|---|---|
| | |
| | |

*Schrijf hier de uitwerking.*

## Begrippenfamilies

**Voorbeeld** [Informatiemodel OKx, Begrippenfamilies](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#begrippenfamilies)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

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

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

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

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Verwante documenten

**Voorbeeld** [Informatiemodel OKx, Verwante documenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/informatiemodel.md#verwante-documenten)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

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

# Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het speelt.

| Nummer | Hoofdstuk | Vraag |
|---|---|------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
