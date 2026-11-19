```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Context van het document | De persona is het beginpunt van de keten. Elk leerroute scenario volgt een persona, en elke uitwerking legt diezelfde persona naast het informatiemodel. |
| Plek in de keten | komt voor het [leerroute scenario](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers nemen het voortouw, want zij kennen de instellingspraktijk per stap |
| Voorbeeld | [persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

Elk hoofdstuk opent met een blok dat zegt wat er van dat hoofdstuk wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Doelstelling document

Dit document legt een student vast waar elk leerroute scenario naar verwijst, zodat elk scenario over dezelfde mens gaat en de reizen naast elkaar te leggen zijn.

## Pakket van eisen

Het pakket van eisen is een eigen document. Het komt uit de gedeelde analyse van alles wat scholen hebben ingebracht, geinventariseerd in de PoC-sessies met de koploperscholen, en de grootst gemene deler daaruit is wat OKx vastlegt. **Dit document bevat het pakket van eisen dus niet; het verwijst ernaar en levert eraan.**

Waar een eis landt hangt af van zijn laag. Een business of functional requirement hoort in de leerroute specificatie, want daar staat wat de instelling moet kunnen en wat een component moet doen. Een technical requirement hoort in de interactieketenspecificatie, want daar staat wat er over het koppelvlak gaat.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort, en noteert de nummers; de eis zelf wordt elders uitgeschreven.

| Laag | Waar die ontstaat | Waar die landt | Voorbeeld |
|---|---|---|------------------------------|
| User story | in een journey of een scenario | pakket van eisen | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | in een procesbeschrijving | leerroute specificatie | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | in een gegevens- of systeemhoofdstuk | leerroute specificatie | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technical requirement | in een interactiehoofdstuk | interactieketenspecificatie | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de laag in die boven het hoofdstuk staat, als verwijzing. De uitgeschreven eis volgt in een eigen ronde, in het document waar hij hoort.

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

# Persona <student>

**Voorbeeld** [Persona Jochem, Persona <student>](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#persona-jochem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

![Npuls leerroute 1](<img/persona/npuls-leerroute1-regulier-jochem.png>)

*Schrijf hier de uitwerking.*

## Studentjourney

**Voorbeeld** [Persona Jochem, Studentjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studentjourney)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Oriënteren

**Voorbeeld** [Persona Jochem, Oriënteren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#oriënteren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Aanmelden

**Voorbeeld** [Persona Jochem, Aanmelden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#aanmelden)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Inschrijven

**Voorbeeld** [Persona Jochem, Inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#inschrijven)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Informeren

**Voorbeeld** [Persona Jochem, Informeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#informeren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Studeren

**Voorbeeld** [Persona Jochem, Studeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studeren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### BPV

**Voorbeeld** [Persona Jochem, BPV](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#bpv)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Kiezen keuzedelen

**Voorbeeld** [Persona Jochem, Kiezen keuzedelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#kiezen-keuzedelen)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Studievoortgang

**Voorbeeld** [Persona Jochem, Studievoortgang](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studievoortgang)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Examineren

**Voorbeeld** [Persona Jochem, Examineren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#examineren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Uitstroom

**Voorbeeld** [Persona Jochem, Uitstroom](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#uitstroom)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Diploma

**Voorbeeld** [Persona Jochem, Diploma](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#diploma)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

## Instellingsjourney

**Voorbeeld** [Persona Jochem, Instellingsjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#instellingsjourney)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Oriënteren

**Voorbeeld** [Persona Jochem, Oriënteren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#oriënteren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Aanmelden

**Voorbeeld** [Persona Jochem, Aanmelden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#aanmelden)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Inschrijven

**Voorbeeld** [Persona Jochem, Inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#inschrijven)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Informeren

**Voorbeeld** [Persona Jochem, Informeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#informeren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Studeren

**Voorbeeld** [Persona Jochem, Studeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studeren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### BPV

**Voorbeeld** [Persona Jochem, BPV](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#bpv)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Kiezen keuzedelen

**Voorbeeld** [Persona Jochem, Kiezen keuzedelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#kiezen-keuzedelen)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Studievoortgang

**Voorbeeld** [Persona Jochem, Studievoortgang](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studievoortgang)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Examineren

**Voorbeeld** [Persona Jochem, Examineren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#examineren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Uitstroom

**Voorbeeld** [Persona Jochem, Uitstroom](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#uitstroom)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

### Diploma

**Voorbeeld** [Persona Jochem, Diploma](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#diploma)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

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
