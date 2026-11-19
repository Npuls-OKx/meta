# Sjabloon persona

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een persona: een student met een naam, een opleiding en een route door het onderwijs, waar elk leerroute scenario daarna naar verwijst |
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers nemen het voortouw, want zij kennen de instellingspraktijk per stap |
| Voorbeeld | [persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Werkwijze

Elk hoofdstuk opent met een blok van vier regels. Dat blok zegt wat er van dit hoofdstuk wordt verwacht, en het blijft staan: het is de opdracht en niet de uitwerking.

| Regel | Wat erin staat |
|---|------------------------------------------------|
| Voorbeeld | de plek in de voorbeelduitwerking waar hetzelfde hoofdstuk al is ingevuld |
| Verwacht | het artefact dat hier hoort, afgeleid uit wat de voorbeelduitwerking daar levert |
| User stories | de nummers uit het pakket van eisen die dit hoofdstuk verwezenlijkt |
| Klaar wanneer | het acceptatiecriterium waaraan de uitwerking voldoet |

De koppen blijven staan zoals zij hier staan. In het agent-harnas komt een lezer (parser) die een ingevuld document per kop terugvertaalt naar de kennisbank; een kop die is herschreven of weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van toepassing is houdt dus zijn kop, met de reden eronder.

## Van user story naar requirement

Een hoofdstuk is pas af wanneer het aanwijsbaar is welke user stories het verwezenlijkt. Die stories komen uit de gedeelde analyse van alles wat scholen als input hebben geleverd, geinventariseerd in de PoC-sessies met de koploperscholen en samengebracht tot het pakket van eisen. De grootst gemene deler daaruit is wat OKx vastlegt.

Elke story gaat daarna door drie lagen. Een voorbeeld, zodat de vorm vastligt:

| Laag | Voorbeeld |
|---|------------------------------------------------|
| User story | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het keuzedeel, de periode en de locatie |
| Technical requirement | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de user stories in; de drie requirementlagen volgen daarna in een eigen ronde, met dit document als bron.

## De grootst gemene deler

Tussen de inbreng van instellingen en dit document zit een analysestap. Haal op bij meerdere instellingen, zoek wat zij delen, en schrijf dat op. Wat een persona draagt is wat bij meerdere instellingen zo werkt, niet wat bij een ervan zo heet.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

## 1 Persona <student>

**Voorbeeld** [Persona Jochem, Persona <student>](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#persona-jochem)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![Npuls leerroute 1](<img/persona/npuls-leerroute1-regulier-jochem.png>)

*Schrijf hier de uitwerking.*

### 1.1 Studentjourney

**Voorbeeld** [Persona Jochem, Studentjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studentjourney)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.1 Oriënteren

**Voorbeeld** [Persona Jochem, Oriënteren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#oriënteren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.2 Aanmelden

**Voorbeeld** [Persona Jochem, Aanmelden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#aanmelden)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.3 Inschrijven

**Voorbeeld** [Persona Jochem, Inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#inschrijven)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.4 Informeren

**Voorbeeld** [Persona Jochem, Informeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#informeren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.5 Studeren

**Voorbeeld** [Persona Jochem, Studeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studeren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.6 BPV

**Voorbeeld** [Persona Jochem, BPV](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#bpv)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.7 Kiezen keuzedelen

**Voorbeeld** [Persona Jochem, Kiezen keuzedelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#kiezen-keuzedelen)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.8 Studievoortgang

**Voorbeeld** [Persona Jochem, Studievoortgang](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studievoortgang)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.9 Examineren

**Voorbeeld** [Persona Jochem, Examineren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#examineren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.10 Uitstroom

**Voorbeeld** [Persona Jochem, Uitstroom](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#uitstroom)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.1.11 Diploma

**Voorbeeld** [Persona Jochem, Diploma](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#diploma)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 1.2 Instellingsjourney

**Voorbeeld** [Persona Jochem, Instellingsjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#instellingsjourney)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.1 Oriënteren

**Voorbeeld** [Persona Jochem, Oriënteren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#oriënteren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.2 Aanmelden

**Voorbeeld** [Persona Jochem, Aanmelden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#aanmelden)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.3 Inschrijven

**Voorbeeld** [Persona Jochem, Inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#inschrijven)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.4 Informeren

**Voorbeeld** [Persona Jochem, Informeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#informeren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.5 Studeren

**Voorbeeld** [Persona Jochem, Studeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studeren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.6 BPV

**Voorbeeld** [Persona Jochem, BPV](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#bpv)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.7 Kiezen keuzedelen

**Voorbeeld** [Persona Jochem, Kiezen keuzedelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#kiezen-keuzedelen)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.8 Studievoortgang

**Voorbeeld** [Persona Jochem, Studievoortgang](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#studievoortgang)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.9 Examineren

**Voorbeeld** [Persona Jochem, Examineren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#examineren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.10 Uitstroom

**Voorbeeld** [Persona Jochem, Uitstroom](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#uitstroom)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

#### 1.2.11 Diploma

**Voorbeeld** [Persona Jochem, Diploma](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md#diploma)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

## Afwijkingen per instelling

Wat bij een instelling anders gaat dan hierboven staat, per regel met de instelling erbij. Dit is geen restcategorie: hier staat het materiaal waaruit blijkt of de grootst gemene deler houdbaar is.

| Instelling | Hoofdstuk | Wat daar anders gaat |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

## Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het speelt.

| Nummer | Hoofdstuk | Vraag |
|---|---|------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
