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

Een voorbeeld van de keten, van behoefte tot koppelvlak:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Instellingseis | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functionele eis | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technische eis | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

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

# De leerroute

**Voorbeeld** [Leerroute 1 scenario, De leerroute](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-leerroute-1--regulier)

**Acceptatiecriteria** het conceptbeeld van de route uit de Npuls-leerroutereeks, met in een zin wat deze route onderscheidt van leerroute 1, en het beeld staat in het document zelf en draagt het nummer en de naam van de route

**Eisen** *dit hoofdstuk levert geen eis op; het geeft de context waarin de eisen van de andere hoofdstukken te lezen zijn*

![Conceptbeeld leerroute <nummer> - regulier studeren in samenhang](<img/leerroute-scenario/Npuls_leerroute_1.jpg>)

*Schrijf hier de uitwerking.*

# Kenmerken van de route

**Voorbeeld** [Leerroute 1 scenario, Kenmerken van de route](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-wat-betekent-regulier-studeren)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wat deze route anders maakt in sturing, tempo en keuzeruimte

**Eisen** *dit hoofdstuk levert geen eis op; het geeft de context waarin de eisen van de andere hoofdstukken te lezen zijn*

*Schrijf hier de uitwerking.*

## Studentjourney

**Voorbeeld** [Leerroute 1 scenario, Studentjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-de-student-beleving---de-student-journey)

**Acceptatiecriteria** een procesplaat van de studentreis in mermaid, BPMN, UML of vergelijkbaar, in het kader van de persona van deze route, met een link naar het persona-document, en elke stap noemt wat de student doet en wat hij op dat moment moet weten

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

## Kiesbare onderdelen

*Optioneel: alleen wanneer deze route kiesbare onderdelen kent; leerroute 9 kan ze bijvoorbeeld niet hebben. Geldt het niet voor deze route, laat de kop staan met die reden eronder.*

**Voorbeeld** [Leerroute 1 scenario, Kiesbare onderdelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#keuzedelen)

**Acceptatiecriteria** een beschrijving met een tabel van de keuzeruimte, en per kiesbaar onderdeel staat erbij hoeveel ruimte er is en wie kiest

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

| Voorkeur  | Keuzedeel                            | Onderwijsperiode   | Onderwijslocatie         |
|-----------|--------------------------------------|--------------------|--------------------------|
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

## Keuzemomenten

*Optioneel: alleen wanneer de route keuzemomenten kent. Geldt het niet voor deze route, laat de kop staan met die reden eronder.*

**Voorbeeld** [Leerroute 1 scenario, Keuzemomenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#wanneer-kiest-een-student-keuzedelen)

**Acceptatiecriteria** een procesplaat van het keuzemoment in mermaid, BPMN, UML of vergelijkbaar, in het kader van de persona van deze route, en het moment is aanwijsbaar in de tijd, en de plaat toont wat er gebeurt wanneer er geen passend aanbod is

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

| Moment | Van (aanmelding) | Naar (inschrijving) | Voorwaarde |
| --- | --- | --- | --- |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

## Start van de onderwijsperiode

**Voorbeeld** [Leerroute 1 scenario, Start van de onderwijsperiode](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#jochems-onderwijsperiode-start)

**Acceptatiecriteria** een beschrijving in lopende tekst, in het kader van de persona van deze route, en er staat wat er klaar moet zijn voordat de periode start

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

## Instellingsjourney

**Voorbeeld** [Leerroute 1 scenario, Instellingsjourney](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3312-de-instellingsbeleving---de-instellingsjourney)

**Acceptatiecriteria** een procesplaat van de instellingsreis in mermaid, BPMN, UML of vergelijkbaar, in het kader van de persona van deze route, naast de studentjourney te leggen, en elke stap noemt de rol die handelt en het systeem dat zij gebruikt

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

*Schrijf hier de uitwerking.*

## De onderwijsinstelling

**Voorbeeld** [Leerroute 1 scenario, De onderwijsinstelling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#de-onderwijsinstelling)

**Acceptatiecriteria** een beschrijving van de organisatie-inrichting, en de teams en rollen die deze route dragen staan erin, en wat zij extra moeten organiseren tegenover leerroute 1

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

*Schrijf hier de uitwerking.*

## Procesbeleving bij de instelling

**Voorbeeld** [Leerroute 1 scenario, Procesbeleving bij de instelling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#de-procesbeleving-achter-regulier-onderwijs-van-een-instelling)

**Acceptatiecriteria** een procesplaat in mermaid, BPMN, UML of vergelijkbaar, en het proces toont de terugweg en het foutpad, en elke stap noemt de rol en het systeem

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_12_05_26.png>)

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_keten3_onderwijsUitvoering_en_begeleiding_12_05_26.png>)

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_keten4_OnderwijsLogistiek_12_05_26.png>)

![MORA Hoofdprocesmodel](<img/leerroute-scenario/MORA_hoofdprocesmodel_keten6_onderwijsOntwikkeling_12_05_26.png>)

*Schrijf hier de uitwerking.*

## Scenario's binnen deze leerroute

**Voorbeeld** [Leerroute 1 scenario, Scenario's binnen deze leerroute](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#scenarios-binnen-deze-leerroute)

**Acceptatiecriteria** een opsomming van scenario's, en de vier herbruikbare scenario's staan erin (nominaal verloop, incidenteel temporiseren, incidenteel versnellen, incidenteel hybride), elk met een regel over wat er in deze route anders gaat

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

## Routespecifieke scenario's

*Optioneel: alleen wanneer deze route een eigen scenario kent dat in geen andere route voorkomt. Geldt het niet voor deze route, laat de kop staan met die reden eronder.*

**Voorbeeld** [Leerroute 1 scenario, Routespecifieke scenario's](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#overige-scenarios-specifiek-voor-leerroute-1)

**Acceptatiecriteria** per scenario een beschrijving met een procesplaat, en er staat bij waarom dit scenario alleen in deze route voorkomt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

*Schrijf hier de uitwerking.*

## Routespecifieke scenario's

*Optioneel: alleen wanneer deze route een eigen scenario kent dat in geen andere route voorkomt. Geldt het niet voor deze route, laat de kop staan met die reden eronder.*

**Voorbeeld** [Leerroute 1 scenario, Routespecifieke scenario's](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#switch-regulier-onderwijs--set-certificaten)

**Acceptatiecriteria** per scenario een beschrijving met een procesplaat, en er staat bij waarom dit scenario alleen in deze route voorkomt

**User stories** *welke stories uit het pakket van eisen dit hoofdstuk naar boven brengt; noteer de nummers, niet de stories zelf*

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

## Betrokken informatie

**Voorbeeld** [Leerroute 1 scenario, Betrokken informatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces)

**Acceptatiecriteria** een tabel met de informatieobjecten, en elk object staat met de term uit de begrippenlijst, en wat niet in de lijst staat is als vraag genoteerd

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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

## Plan- en roosterproces

**Voorbeeld** [Leerroute 1 scenario, Plan- en roosterproces](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#het-plan-en-rooster-proces)

**Acceptatiecriteria** een procesplaat in mermaid, BPMN, UML of vergelijkbaar, en de plaat toont wanneer er gepland wordt, waarop wordt bijgestuurd, en wat er gebeurt wanneer het plan niet sluit

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

*Schrijf hier de uitwerking.*

## Plancyclus

**Voorbeeld** [Leerroute 1 scenario, Plancyclus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#plannen-is-cyclisch)

**Acceptatiecriteria** een beschrijving met een beeld van de cyclus, en de momenten voor en na de startweek staan uit elkaar

**Instellingseisen** *wat de instelling moet kunnen om die stories waar te maken; noteer de nummers uit het register instellingseisen*

*Schrijf hier de uitwerking.*

## Groeperingen, plannen en roosteren

**Voorbeeld** [Leerroute 1 scenario, Groeperingen, plannen en roosteren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#voorbeeld-van-groeperingen-en-plannen-en-roosteren)

**Acceptatiecriteria** een voorbeeld met een tabel, en de groeperingen zijn benoemd met hun kardinaliteit, en elk getal heeft een voorbeeld

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

# Planbare onderwijsspecificaties

**Voorbeeld** [Leerroute 1 scenario, Planbare onderwijsspecificaties](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#planbare-onderwijsspecificaties)

**Acceptatiecriteria** een beschrijving met een tabel, en er staat per specificatie wat haar planbaar maakt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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

## Persoon, groep en constraint

**Voorbeeld** [Leerroute 1 scenario, Persoon, groep en constraint](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#persoon-groep-en-constraint--informatie-overzicht)

**Acceptatiecriteria** een tabel met de constraints, en elke constraint is te toetsen en noemt het systeem dat hem kent

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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

## Conceptueel gegevensoverzicht

**Voorbeeld** [Leerroute 1 scenario, Conceptueel gegevensoverzicht](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#conceptueel-gegevensoverzicht)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van de gegevens, met een tabel ernaast, en elk gegeven noemt zijn bronsysteem en de term uit de begrippenlijst

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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

## Betrokken systemen

**Voorbeeld** [Leerroute 1 scenario, Betrokken systemen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-systemen-bij-gegevensuitwisseling)

**Acceptatiecriteria** een tabel met de systemen, en elk systeem staat met zijn afkorting uit de afkortingenlijst, dus Onderwijscatalogus (OC) en niet de catalogus

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

![OKx informatiestromen Leerroute <nummer> - Regulier](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526.jpg>)

*Schrijf hier de uitwerking.*

## Applicatiecomponenten op de plaat

**Voorbeeld** [Leerroute 1 scenario, Applicatiecomponenten op de plaat](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#applicatiecomponenten-op-de-plaat--doelen-gegevens-en-interacties)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van de informatiestromen hoofdplaat, in het kader van de interactieketen die deze route raakt, en per component staat welk doel het dient en welke gegevens het draagt; wat buiten de scope valt is op de plaat zichtbaar gedimd

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Componenten en hun scope

**Voorbeeld** [Leerroute 1 scenario, Componenten en hun scope](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#componenten-en-hun-doel--wat-hoort-hier-wel-en-niet-thuis)

**Acceptatiecriteria** een tabel, en per component staat wat er wel en wat er niet in hoort, met de reden

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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

## Bron-, lees- en bewerkrollen

**Voorbeeld** [Leerroute 1 scenario, Bron-, lees- en bewerkrollen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#bron--lees--en-bewerkrollen-tov-informatie-objecten)

**Acceptatiecriteria** een tabel met de rollen per informatieobject, en per object is er precies een bronsysteem

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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

## Anti-patronen tussen systemen

**Voorbeeld** [Leerroute 1 scenario, Anti-patronen tussen systemen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#anti-patronen-tussen-systemen--tegengestelde-doelen-om-te-voorkomen)

**Acceptatiecriteria** een opsomming, en elk anti-patroon noemt het tegengestelde doel dat eronder ligt

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

*Schrijf hier de uitwerking.*

## Procesfasen, interacties en informatie

**Voorbeeld** [Leerroute 1 scenario, Procesfasen, interacties en informatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#procesfasen--interacties-op-de-plaat--informatie)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht per fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat; dit is de brug naar de interactieketen

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

*Schrijf hier de uitwerking.*

### Fase 1 — Kwalificatiekader analyseren en grofmazig ontwerpen

**Voorbeeld** [Leerroute 1 scenario, Fase 1 — Kwalificatiekader analyseren en grofmazig ontwerpen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-1--kwalificatiekader-analyseren-en-grofmazig-ontwerpen)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 1](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f1.jpg>)

*Schrijf hier de uitwerking.*

### Fase 2 — Publiceren en planbaar maken

**Voorbeeld** [Leerroute 1 scenario, Fase 2 — Publiceren en planbaar maken](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-2--publiceren-en-planbaar-maken)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 2](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f2.jpg>)

*Schrijf hier de uitwerking.*

### Fase 3 — Instroom, intake en plaatsing

**Voorbeeld** [Leerroute 1 scenario, Fase 3 — Instroom, intake en plaatsing](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-3--instroom-intake-en-plaatsing)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 3](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f3.jpg>)

*Schrijf hier de uitwerking.*

### Fase 4 — Detailleren, roosteren en inschrijven

**Voorbeeld** [Leerroute 1 scenario, Fase 4 — Detailleren, roosteren en inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-4--detailleren-roosteren-en-inschrijven)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 4](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f4.jpg>)

*Schrijf hier de uitwerking.*

### Fase 5 — Onderwijs uitvoeren en voortgang begeleiden

**Voorbeeld** [Leerroute 1 scenario, Fase 5 — Onderwijs uitvoeren en voortgang begeleiden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-5--onderwijs-uitvoeren-en-voortgang-begeleiden)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 5](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f5.jpg>)

*Schrijf hier de uitwerking.*

### Fase 6 — Organiseren van keuzemomenten

**Voorbeeld** [Leerroute 1 scenario, Fase 6 — Organiseren van keuzemomenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-6--organiseren-van-keuzemomenten)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 6](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f6.jpg>)

*Schrijf hier de uitwerking.*

### Fase 7 — Bijsturen planning en aanbod

**Voorbeeld** [Leerroute 1 scenario, Fase 7 — Bijsturen planning en aanbod](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-7--bijsturen-planning-en-aanbod)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 7](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f7.jpg>)

*Schrijf hier de uitwerking.*

### Fase 8 — Examineren, vaststellen en diplomeren

**Voorbeeld** [Leerroute 1 scenario, Fase 8 — Examineren, vaststellen en diplomeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-8--examineren-vaststellen-en-diplomeren)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van deze fase, met een tabel ernaast, in het kader van de interactieketen, en per interactie staat welk systeem levert, welk systeem afneemt en welke informatie meegaat

**Technische eisen** *wat er over het koppelvlak gaat en in welke vorm; die liggen in de interactieketen zelf vast*

![OKx informatiestromen Leerroute <nummer> — highlight Procesfase 8](<img/leerroute-scenario/OKx_LR1_informatiestromen_v20260526_f8.jpg>)

*Schrijf hier de uitwerking.*

## Concept informatiemodel: geneste onderwijsspecificatie

**Voorbeeld** [Leerroute 1 scenario, Concept informatiemodel: geneste onderwijsspecificatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#concept-informatiemodel--geneste-onderwijsspecificatie-jochem-apothekersassistent)

**Acceptatiecriteria** een ArchiMate-plaat of een SVG-render daarvan, met de scope uitgelicht van het informatiemodel, met alleen de objecttypen die deze route raakt, en elk objecttype draagt de term uit de begrippenlijst, en elke kardinaliteit tussen twee typen heeft een ingevuld voorbeeld

**Functionele eisen** *wat een component moet doen met welke gegevens; noteer de nummers uit het register functionele eisen*

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
