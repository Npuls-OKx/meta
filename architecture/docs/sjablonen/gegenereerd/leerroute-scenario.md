# Sjabloon leerroute scenario

## Invullen

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een leerroute scenario: een van de negen Npuls-leerroutes uitgewerkt tot het punt waarop duidelijk is welke informatie waarheen moet. Het is kaderstellend, dus geen anekdote en geen instellingsontwerp |
| Wie dit invult | de adviesgroep. Suggestie: de BOP-adviseurs en de business analisten samen, met de onderwijskundige kant bij de adviesgroep zelf |
| Voorbeeld | [leerroute 1 scenario](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) |
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

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier dubbel, want een leerroute scenario is wat OKx als afspraak vastlegt: een procesgewoonte van een instelling die hier als kader belandt, wordt een eis aan elke leverancier.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

## 1 De leerroute

**Voorbeeld** [Leerroute 1 scenario, De leerroute](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-leerroute-1--regulier)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![Conceptbeeld leerroute <nummer> - regulier studeren in samenhang](<img/leerroute-scenario/Npuls_leerroute_1.jpg>)

*Schrijf hier de uitwerking.*

## 2 Kenmerken van de route

**Voorbeeld** [Leerroute 1 scenario, Kenmerken van de route](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-wat-betekent-regulier-studeren)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.1 Studentjourney

**Voorbeeld** [Leerroute 1 scenario, Studentjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-de-student-beleving---de-student-journey)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.2 Keuzedelen

**Voorbeeld** [Leerroute 1 scenario, Keuzedelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#keuzedelen)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Voorkeur  | Keuzedeel                            | Onderwijsperiode   | Onderwijslocatie         |
|-----------|--------------------------------------|--------------------|--------------------------|
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

### 2.3 Keuzemoment keuzedelen

**Voorbeeld** [Leerroute 1 scenario, Keuzemoment keuzedelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#wanneer-kiest-een-student-keuzedelen)

**Verwacht** een procesdiagram (BPMN, mermaid, UML of vergelijkbaar), een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt; elke rij is ingevuld, of doorgehaald met de reden erbij

| Moment | Van (aanmelding) | Naar (inschrijving) | Voorwaarde |
| --- | --- | --- | --- |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

### 2.4 Start van de onderwijsperiode

**Voorbeeld** [Leerroute 1 scenario, Start van de onderwijsperiode](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#jochems-onderwijsperiode-start)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.5 Instellingsjourney

**Voorbeeld** [Leerroute 1 scenario, Instellingsjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3312-de-instellingsbeleving---de-instellingsjourney)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.6 De onderwijsinstelling

**Voorbeeld** [Leerroute 1 scenario, De onderwijsinstelling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#de-onderwijsinstelling)

**Verwacht** een procesdiagram (BPMN, mermaid, UML of vergelijkbaar)

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt

*Schrijf hier de uitwerking.*

### 2.7 Procesbeleving bij de instelling

**Voorbeeld** [Leerroute 1 scenario, Procesbeleving bij de instelling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#de-procesbeleving-achter-regulier-onderwijs-van-een-instelling)

**Verwacht** een procesdiagram (BPMN, mermaid, UML of vergelijkbaar), een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt; het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_12_05_26.png>)

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_keten3_onderwijsUitvoering_en_begeleiding_12_05_26.png>)

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_keten4_OnderwijsLogistiek_12_05_26.png>)

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_keten6_onderwijsOntwikkeling_12_05_26.png>)

*Schrijf hier de uitwerking.*

### 2.8 Scenario's binnen deze leerroute

**Voorbeeld** [Leerroute 1 scenario, Scenario's binnen deze leerroute](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#scenarios-binnen-deze-leerroute)

**Verwacht** een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elk punt is een uitspraak die te toetsen is, geen onderwerp

*Schrijf hier de uitwerking.*

### 2.9 Routespecifieke scenario's

**Voorbeeld** [Leerroute 1 scenario, Routespecifieke scenario's](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#overige-scenarios-specifiek-voor-leerroute-1)

**Verwacht** een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elk punt is een uitspraak die te toetsen is, geen onderwerp

*Schrijf hier de uitwerking.*

### 2.10 Overstap naar een set certificaten

**Voorbeeld** [Leerroute 1 scenario, Overstap naar een set certificaten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#switch-regulier-onderwijs--set-certificaten)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Aspect | Regulier | Switch naar certificaten (of terug) |
| --- | --- | --- |
| | | |
| | | |
| | | |

| Dimensie | Wat moet vastliggen |
| --- | --- |
| | |
| | |
| | |
| | |

| Leerroute | Happy / nominaal | Incidenteel Temporiseren | Incidenteel Versnellen | Incidenteel Hybride | Route-specifiek (voorbeeld) |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Schrijf hier de uitwerking.*

### 2.11 Betrokken informatie

**Voorbeeld** [Leerroute 1 scenario, Betrokken informatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces)

**Verwacht** een beeld, een ingevulde tabel, een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elke rij is ingevuld, of doorgehaald met de reden erbij; elk punt is een uitspraak die te toetsen is, geen onderwerp

| Vraag                                        | Concept                | Doel/toelichting                                                                                                   |
|----------------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------|
| | | |
| | | |
| | | |
| | | |
| | | |

| **1. Kwalificatiekader** | **2. Onderwijsspecificatie** | **3. Onderwijsaanbod** | **4. Onderwijsverbintenis** | **5. Onderwijsresultaat** |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

| Informatie-object | Conceptdefinitie |
| --- | --- |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

![Informatiemodel visual — Klus 53 allignment MORA-HORA](<img/leerroute-scenario/Informatiemodel_visual_Klus_56_allignment_MORA_HORA_20260519.png>)

*Schrijf hier de uitwerking.*

### 2.12 Plan- en roosterproces

**Voorbeeld** [Leerroute 1 scenario, Plan- en roosterproces](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#het-plan-en-rooster-proces)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.13 Plancyclus

**Voorbeeld** [Leerroute 1 scenario, Plancyclus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#plannen-is-cyclisch)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.14 Verdieping: CSP, NP-hard en controle

**Voorbeeld** [Leerroute 1 scenario, Verdieping: CSP, NP-hard en controle](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#voor-wie-dieper-wil-csp-np-hard-en-controle)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 2.15 Groeperingen, plannen en roosteren

**Voorbeeld** [Leerroute 1 scenario, Groeperingen, plannen en roosteren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#voorbeeld-van-groeperingen-en-plannen-en-roosteren)

**Verwacht** een procesdiagram (BPMN, mermaid, UML of vergelijkbaar)

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt

*Schrijf hier de uitwerking.*

## 3 Planbare onderwijsspecificaties

**Voorbeeld** [Leerroute 1 scenario, Planbare onderwijsspecificaties](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#planbare-onderwijsspecificaties)

**Verwacht** een procesdiagram (BPMN, mermaid, UML of vergelijkbaar), een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het diagram toont de terugweg en het foutpad, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt; elke rij is ingevuld, of doorgehaald met de reden erbij

| Gegevensdimensie | Wat de planner nodig heeft | Voorbeeld (generiek) |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| Gegevensdimensie | Invulling voor <student>s cohort |
| --- | --- |
| | |
| | |
| | |
| | |
| | |

*Schrijf hier de uitwerking.*

### 3.1 Persoon, groep en constraint

**Voorbeeld** [Leerroute 1 scenario, Persoon, groep en constraint](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#persoon-groep-en-constraint--informatie-overzicht)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| **Bron (keten)** | **Primair inzicht** | **`Persoon` (student / medewerker)** | **Groep / cluster / populatie** | **Constraintdimensie (voorbeelden)** |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

| **Hoofdtype `Persoon`** | **Rol of functietitel (voorbeelden; koppelbaar aan HR)** | **Skills-profiel** (vaardigheden, kennis, inzichten; bevoegdheden waar van toepassing) | **Als constraint geformuleerd** (skill-vraag / skill-aanbod; typisch plan vs rooster) |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| **Reële-wereldvlak** | **Voorbeelden van constraints** | **Meest zichtbaar in** |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

*Schrijf hier de uitwerking.*

### 3.2 Conceptueel gegevensoverzicht

**Voorbeeld** [Leerroute 1 scenario, Conceptueel gegevensoverzicht](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| **Gegevensgroep / informatie-object** | **Vlak** | **Doel en conceptuele inhoud** | **Voorbeeld attributen** (niet exhaustief) | **Conceptdefinitie** |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

### 3.3 Betrokken systemen

**Voorbeeld** [Leerroute 1 scenario, Betrokken systemen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-systemen-bij-gegevensuitwisseling)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> - Regulier](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526.jpg>)

*Schrijf hier de uitwerking.*

### 3.4 Applicatiecomponenten op de plaat

**Voorbeeld** [Leerroute 1 scenario, Applicatiecomponenten op de plaat](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#applicatiecomponenten-op-de-plaat--doelen-gegevens-en-interacties)

**Verwacht** een beschrijving in lopende tekst

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

*Schrijf hier de uitwerking.*

### 3.5 Componenten en hun scope

**Voorbeeld** [Leerroute 1 scenario, Componenten en hun scope](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#componenten-en-hun-doel--wat-hoort-hier-wel-en-niet-thuis)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Component (zoals op plaat) | Hoofddoel in dit scenario | Wat dit systeem **niet** doet (rolafbakening) | Welke informatie hier ontstaat of leeft (conceptueel) |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

### 3.6 Bron-, lees- en bewerkrollen

**Voorbeeld** [Leerroute 1 scenario, Bron-, lees- en bewerkrollen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#bron--lees--en-bewerkrollen-tov-informatie-objecten)

**Verwacht** een ingevulde tabel

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij

| Systeem | Bron van waarheid voor (informatie-objecten) | Leest (consumeert) | Bewerkt / schrijft |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

### 3.7 Anti-patronen tussen systemen

**Voorbeeld** [Leerroute 1 scenario, Anti-patronen tussen systemen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#anti-patronen-tussen-systemen--tegengestelde-doelen-om-te-voorkomen)

**Verwacht** een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elk punt is een uitspraak die te toetsen is, geen onderwerp

*Schrijf hier de uitwerking.*

### 3.8 Procesfasen, interacties en informatie

**Voorbeeld** [Leerroute 1 scenario, Procesfasen, interacties en informatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#procesfasen--interacties-op-de-plaat--informatie)

**Verwacht** een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elk punt is een uitspraak die te toetsen is, geen onderwerp

*Schrijf hier de uitwerking.*

#### 3.8.1 Fase 1 — Kwalificatiekader analyseren en grofmazig ontwerpen

**Voorbeeld** [Leerroute 1 scenario, Fase 1 — Kwalificatiekader analyseren en grofmazig ontwerpen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 1](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f1.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.2 Fase 2 — Publiceren en planbaar maken

**Voorbeeld** [Leerroute 1 scenario, Fase 2 — Publiceren en planbaar maken](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-2--publiceren-en-planbaar-maken)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 2](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f2.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.3 Fase 3 — Instroom, intake en plaatsing

**Voorbeeld** [Leerroute 1 scenario, Fase 3 — Instroom, intake en plaatsing](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-3--instroom-intake-en-plaatsing)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 3](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f3.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.4 Fase 4 — Detailleren, roosteren en inschrijven

**Voorbeeld** [Leerroute 1 scenario, Fase 4 — Detailleren, roosteren en inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-4--detailleren-roosteren-en-inschrijven)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 4](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f4.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.5 Fase 5 — Onderwijs uitvoeren en voortgang begeleiden

**Voorbeeld** [Leerroute 1 scenario, Fase 5 — Onderwijs uitvoeren en voortgang begeleiden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden)

**Verwacht** een beeld, een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elk punt is een uitspraak die te toetsen is, geen onderwerp

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 5](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f5.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.6 Fase 6 — Organiseren van keuzemomenten

**Voorbeeld** [Leerroute 1 scenario, Fase 6 — Organiseren van keuzemomenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-6--organiseren-van-keuzemomenten)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 6](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f6.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.7 Fase 7 — Bijsturen planning en aanbod

**Voorbeeld** [Leerroute 1 scenario, Fase 7 — Bijsturen planning en aanbod](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-7--bijsturen-planning-en-aanbod)

**Verwacht** een beeld, een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken; elk punt is een uitspraak die te toetsen is, geen onderwerp

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 7](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f7.jpg>)

*Schrijf hier de uitwerking.*

#### 3.8.8 Fase 8 — Examineren, vaststellen en diplomeren

**Voorbeeld** [Leerroute 1 scenario, Fase 8 — Examineren, vaststellen en diplomeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-8--examineren-vaststellen-en-diplomeren)

**Verwacht** een beeld

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 8](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f8.jpg>)

*Schrijf hier de uitwerking.*

### 3.9 Concept informatiemodel: geneste onderwijsspecificatie

**Voorbeeld** [Leerroute 1 scenario, Concept informatiemodel: geneste onderwijsspecificatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#concept-informatiemodel--geneste-onderwijsspecificatie-jochem-apothekersassistent)

**Verwacht** een ingevulde tabel, een opsomming

**User stories** *vul de nummers in uit het pakket van eisen die dit hoofdstuk verwezenlijkt*

**Klaar wanneer** elke rij is ingevuld, of doorgehaald met de reden erbij; elk punt is een uitspraak die te toetsen is, geen onderwerp

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
