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

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft. De kleine plaat eronder toont de hele productafbakening, met een kader om deze uitsnede.

Het bouwt op een of meer persona's, en gaat vooraf aan de uitwerking en de interactieketen.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/product-breakdown/README.md).

## Doelstelling document

Dit document werkt een Npuls-leerroute uit tot het punt waarop duidelijk is welke informatie waarheen moet, zodat de solutionlaag erop kan bouwen zonder de onderwijskundige keuze over te nemen.

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

Dit document levert **instellingseisen** en **functionele eisen**; de technische eisen volgen later, in de interactieketen. Zo ziet zo'n eis eruit, met de keten erboven en eronder:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story uit de PoC-inbreng | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| **Instellingseis, uit dit document** | **de instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst** |
| Functionele eis, verderop | het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie |
| Technische eis, verderop | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

## Kwaliteit van een eis

Een eis is bruikbaar wanneer een leverancier hem kan lezen zonder de instelling te bellen. Wat hier staat is een voorstel voor een sectorafspraak: opgesteld uit de inbreng van afzonderlijke instellingen, vastgelegd als afspraak, en daarna de grond voor de technische specificatie. Schrijf elke eis uit op de plek waar hij ontstaat, en toets hem aan de criteria hieronder.

**Een instellingseis:**

1. is een zin die opent met `De instelling kan`;
2. noemt een vermogen van de instelling; het systeem dat het draagt volgt in de functionele eis;
3. is toetsbaar: er is een situatie te noemen waarin vaststaat of de instelling het kan;
4. noemt zijn herkomst: de persona met de stap, het scenario of de procesfase;
5. geldt bij meerdere instellingen; wat bij een instelling speelt staat onder Afwijkingen per instelling;
6. draagt een vermogen; een tweede vermogen krijgt een eigen nummer.

**Een functionele eis:**

1. is een zin die opent met de applicatiecomponent, in de naam van de [hoofdplaat informatiestromen](https://github.com/Npuls-OKx/meta/blob/dev/project/README.md);
2. noemt wat de component doet en met welke informatieobjecten, elk met de naam van het objecttype uit de [begrippenlijst](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/begrippen/begrippenlijst.md), tussen backquotes;
3. kiest het objecttype dat bij het moment past: een `Aanmelding` op aanbod is een wens, een verbintenis bestaat pas wanneer zij is aangegaan;
4. noemt de instellingseis waaruit hij komt;
5. beschrijft gedrag; formaat, protocol en veldnamen volgen in de technische eis;
6. is toetsbaar: er is een invoer te noemen met de uitkomst die de component dan geeft;
7. draagt een gedrag; een tweede gedrag krijgt een eigen nummer.

| Soort | Zwak | Wat eraan ontbreekt | Sterk |
|---|--------|------|------------|
| instellingseis | De instelling wil flexibel omgaan met keuzedelen | er is geen situatie waarin vaststaat of het kan | De instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst |
| instellingseis | Het roosterpakket stuurt een melding wanneer een keuzedeel vol zit | noemt een product en een oplossing; het vermogen van de instelling ontbreekt | De instelling kan signaleren dat de keuzedeelruimte van een student oningevuld blijft, op een moment dat de student nog een nieuwe keuze kan maken |
| functionele eis | Het systeem ondersteunt voorkeuren voor keuzedelen | de component, de gegevens en het gedrag ontbreken | Het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie |
| functionele eis | Het Student Keuze Systeem stuurt de voorkeuren als JSON-lijst naar het Planningssysteem | legt het formaat vast; dat hoort in de technische eis | Het Student Keuze Systeem levert per voorkeur van een student de `Aanmelding` op het `Keuzedeel aanbod` aan het Planningssysteem, met haar plaats in de volgorde |

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

# Werkwijze

Een leerroute scenario is opgebouwd uit vijf sjabloononderdelen. Het routeprofiel staat er een keer in; de andere vier herhalen zich tot de route gedekt is.

| Sjabloononderdeel | Hoe vaak | Levert |
|---|---|---|
| Routeprofiel | een keer | context |
| Reis | per persona | instellingseisen, uit de user stories van het persona-document |
| Scenario binnen de route | per scenario | instellingseisen |
| Procesfase | per fase | instellingseisen |
| Informatie en systemen | per fase, of een keer voor de route | functionele eisen |

De opbrengst van dit document is het [Eisenoverzicht](#eisenoverzicht): de instellingseisen en de functionele eisen van deze route, uitgeschreven en genummerd. OKx SI vertaalt dat overzicht met de leveranciers naar technische eisen, in de interactieketen.

De uitgewerkte vorm staat in [leerroute 1 scenario](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md); neem daar de diepgang van over en houd de indeling van dit sjabloon aan. Wat leerroute 1 eigen is, zoals keuzedelen, hoort alleen in een route die het ook kent.

# Notatie van eisen

Elke eis krijgt een nummer en verwijst naar het sjabloononderdeel waaruit hij komt. Een eis is een zin die te toetsen is; de toelichting staat in het sjabloononderdeel zelf. Waaraan die zin voldoet staat onder [Kwaliteit van een eis](#kwaliteit-van-een-eis).

| Soort | Nummer | Vorm van de zin |
|---|---|---|
| Instellingseis | `IE-LR<route>-<volgnummer>`, bijvoorbeeld `IE-LR2-03` | De instelling kan ... |
| Functionele eis | `FE-LR<route>-<volgnummer>`, bijvoorbeeld `FE-LR2-07` | Het <component> ... |

Een instellingseis noemt de persona met de stap, het scenario of de procesfase waaruit hij komt. Een functionele eis noemt de instellingseis waaruit hij komt. Een voorbeeld uit leerroute 1:

| Nummer | Eis | Komt uit |
|---|---|---|
| IE-LR1-01 | De instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst | reis van Jochem, stap kiezen keuzedelen |
| FE-LR1-01 | Het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie | IE-LR1-01, sjabloononderdeel informatie en systemen |

# Sjabloononderdeel: routeprofiel

Dit sjabloononderdeel staat er een keer in, vooraan.

**Voorbeeld** [Leerroute 1 scenario, 3.2.1.1 Leerroute 1 — Regulier](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-leerroute-1--regulier)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. het conceptbeeld van de route uit de Npuls-leerroutereeks staat erbij;
2. de tabel is volledig ingevuld;
3. het veld Persona's noemt elke persona van de route, met een link naar het persona-document;
4. het veld Verschil met leerroute 1 zegt in een zin wat deze route onderscheidt van leerroute 1, de reguliere en aanbodgedreven route die als vergelijkingspunt dient;
5. het veld Eindbeeld noemt het punt waar dit scenario eindigt, met de reden.

**Eisen** *dit hoofdstuk levert geen eis op; het geeft de context waarin de eisen van de andere hoofdstukken te lezen zijn*

**Ingevuld voorbeeld** uit Leerroute 1 scenario:

| Veld | Invulling |
|---|------------------------------------------------|
| Route | leerroute 1, regulier |
| Persona's | Jochem, student: [persona Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md) |
| Sturing | aanbodgedreven: de instelling ontwerpt, plant en roostert de route vooraf; alleen de keuzedelen kiest de student |
| Verschil met leerroute 1 | dit is leerroute 1 zelf, het vergelijkingspunt voor de andere routes |
| Eindbeeld | het diploma: Jochem heeft zijn examens afgelegd en de opleiding voltooid |

**Vul in:**

| Veld | Invulling |
|---|------------------------------------------------|
| Route | *nummer en naam uit de negen Npuls-leerroutes* |
| Persona's | *wie deze route doorlopen, met een link naar het persona-document* |
| Sturing | *aanbodgedreven, vraaggedreven of hybride, en voor welk deel van de route* |
| Verschil met leerroute 1 | *wat gelijk blijft en wat anders gaat, in tempo, keuzeruimte en rollen* |
| Eindbeeld | *waar dit scenario eindigt, en waarom daar* |

![Voorbeeld van een routeprofiel: het conceptbeeld van leerroute 1](<img/leerroute-scenario/Npuls_leerroute_1.jpg>)

*Schrijf hier de uitwerking.*

# Sjabloononderdeel: reis

Kopieer dit sjabloononderdeel voor elke persona van de route: de student, en elke rol vanuit de instelling waar de route langs loopt. De stappen van twee reizen dragen dezelfde namen, zodat zij naast elkaar te leggen zijn.

Neem de user stories uit het persona-document als vertrekpunt: elke story wordt hier een instellingseis, bij de stap waar zij ontstond.

**Voorbeeld** [Leerroute 1 scenario, 3.2.1.1 De student beleving - De Student Journey](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#3211-de-student-beleving---de-student-journey)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. er staat een procesplaat in mermaid, BPMN, UML of vergelijkbaar van de reis van een persona, met de stappen in volgorde en de terugweg waar die bestaat;
2. de reis staat in het kader van de persona's van deze route, met een link naar het persona-document; de stapnamen komen uit deze procesplaat en het persona-document neemt ze over;
3. de tabel noemt per stap wat deze persona doet, wat hij moet weten en welk systeem hij raakt;
4. elke user story uit het persona-document is hier een instellingseis geworden, of staat met de reden onder Observaties en signaleringen;
5. elke instellingseis staat uitgeschreven en genummerd in de laatste kolom en voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis).

**Instellingseisen** *wat de instelling moet kunnen; schrijf elke eis uit met zijn nummer, bij de stap, het scenario of de fase waar hij ontstaat*

**Ingevuld voorbeeld** uit Leerroute 1 scenario:

| Stap | Wat de persona doet | Wat hij moet weten | Systeem | Instellingseis |
|---|---|---|---|---|
| Kiezen keuzedelen | Jochem stelt een geprioriteerde voorkeurslijst op, met per voorkeur de onderwijsperiode en optioneel de onderwijslocatie | welke keuzedelen in zijn keuzedeelruimte passen, en waar en wanneer zij worden gegeven | Student Keuze Systeem | IE-LR1-01: De instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst |
| Kiezen keuzedelen | zijn eerste voorkeur past niet; hij oriënteert zich op een ander keuzedeel of een andere onderwijslocatie | welk aanbod nog in zijn keuzedeelruimte past | Student Keuze Systeem | IE-LR1-02: De instelling kan signaleren dat de keuzedeelruimte van een student oningevuld blijft, op een moment dat de student nog een nieuwe keuze kan maken |

**Vul in:**

| Stap | Wat de persona doet | Wat hij moet weten | Systeem | Instellingseis |
|---|---|---|---|---|
| | | | | *IE-LR..-..: De instelling kan ...* |
| | | | | |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

# Sjabloononderdeel: scenario binnen de route

Kopieer dit sjabloononderdeel per scenario. Vier scenario's keren in elke route terug: het nominale verloop, incidenteel temporiseren, incidenteel versnellen en incidenteel hybride.

*Optioneel: het nominale verloop hoort er altijd in; een incidentele variant of een routespecifiek scenario alleen wanneer de route dat kent. Geldt het niet voor deze route, laat de kop staan met die reden eronder.*

**Voorbeeld** [Leerroute 1 scenario, Scenario's binnen deze leerroute](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#scenarios-binnen-deze-leerroute)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. het scenario staat in vier vaste delen: de uitgangssituatie, de aanleiding, het verloop en het eindbeeld;
2. het veld Persona noemt wie het scenario doorloopt, en het scenario past binnen het routeprofiel;
3. er staat een procesplaat in mermaid, BPMN, UML of vergelijkbaar wanneer het verloop afwijkt van de reis;
4. wat alleen in deze route voorkomt staat erbij met de reden;
5. elke instellingseis die dit scenario toevoegt staat uitgeschreven en genummerd; voegt het scenario geen eis toe, dan staat dat er.

**Instellingseisen** *wat de instelling moet kunnen; schrijf elke eis uit met zijn nummer, bij de stap, het scenario of de fase waar hij ontstaat*

**Ingevuld voorbeeld** uit Leerroute 1 scenario:

| Veld | Invulling |
|---|------------------------------------------------|
| Scenario | incidenteel temporiseren, incidenteel |
| Persona | Jochem |
| Uitgangssituatie | Jochem volgt het programma zoals het is ontworpen en gepland |
| Aanleiding | hij haalt een toetsmoment niet in een keer |
| Verloop | Jochem herkanst; de instelling plant het onderdeel opnieuw in; de rest van zijn programma loopt door |
| Eindbeeld | het onderdeel is opnieuw ingepland en behaald; de rest van zijn programma is ongewijzigd |
| Instellingseisen | IE-LR1-03: De instelling kan een onderdeel voor een student opnieuw inplannen terwijl de rest van zijn programma doorloopt |

**Vul in:**

| Veld | Invulling |
|---|------------------------------------------------|
| Scenario | *naam, en of het nominaal, incidenteel of routespecifiek is* |
| Persona | *wie dit scenario doorloopt, met een link naar het persona-document* |
| Uitgangssituatie | *wat er al staat voordat het begint* |
| Aanleiding | *wat er verandert, en op welk moment* |
| Verloop | *wie wat doet, in welke volgorde* |
| Eindbeeld | *wat er klaar is wanneer het scenario eindigt* |
| Instellingseisen | *IE-LR..-..: De instelling kan ..., een regel per eis* |

*Schrijf hier de uitwerking.*

# Sjabloononderdeel: procesfase

Kopieer dit sjabloononderdeel per fase. Houd de fasenamen van leerroute 1 aan waar de fase hetzelfde is; een eigen fase krijgt een eigen naam met de reden erbij.

**Voorbeeld** [Leerroute 1 scenario, Fase 2 — Publiceren en planbaar maken](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#fase-2--publiceren-en-planbaar-maken)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. er staat een procesplaat in mermaid, BPMN, UML of vergelijkbaar van de fase aan de kant van de instelling, met wie handelt, met welk systeem, en het foutpad;
2. de plaat is naast de reis van de persona's te leggen: een stap die een persona raakt draagt daar dezelfde naam;
3. elke processtap staat in de tabel, met de rol en het systeem;
4. elke stap die de instelling moet kunnen, draagt een uitgeschreven en genummerde instellingseis die voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis).

**Instellingseisen** *wat de instelling moet kunnen; schrijf elke eis uit met zijn nummer, bij de stap, het scenario of de fase waar hij ontstaat*

**Ingevuld voorbeeld** uit Leerroute 1 scenario, fase 2 Publiceren en planbaar maken:

| Processtap | Rol | Systeem | Instellingseis |
|---|---|---|---|
| Haalbaarheid bepalen binnen de strategische jaarplanning | planner | Planningssysteem | IE-LR1-04: De instelling kan de haalbaarheid van een `Opleiding specificatie` bepalen voordat zij het onderwijsaanbod publiceert |

**Vul in:**

| Processtap | Rol | Systeem | Instellingseis |
|---|---|---|---|
| | | | *IE-LR..-..: De instelling kan ...* |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

# Sjabloononderdeel: informatie en systemen

Kopieer dit sjabloononderdeel per procesfase, of vul het een keer in voor de hele route wanneer de fasen dezelfde informatie raken.

**Voorbeeld** [Leerroute 1 scenario, Betrokken informatie bij proces](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#betrokken-informatie-bij-proces)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. er staat een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze fase uitgelicht op de hoofdplaat informatiestromen;
2. elk informatieobject draagt de naam van het objecttype uit de begrippenlijst, tussen backquotes, en past bij het moment in het proces: een specificatie, een aanbod, een aanmelding of een verbintenis;
3. elk informatieobject heeft precies een bronsysteem;
4. elke functionele eis staat uitgeschreven en genummerd, opent met de component en noemt de instellingseis waaruit hij komt;
5. elke instellingseis uit de reizen, de scenario's en de procesfasen heeft minstens een functionele eis, hier of in de leerroute scenario uitwerking; volgt hij daar, dan staat dat onder Observaties en signaleringen;
6. elke functionele eis voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis).

**Functionele eisen** *wat een component moet doen met welke gegevens; schrijf elke eis uit met zijn nummer en de instellingseis waaruit hij komt*

**Ingevuld voorbeeld** uit Leerroute 1 scenario, fase 6 Organiseren van keuzemomenten:

| Informatieobject | Bronsysteem | Wie leest of bewerkt | Functionele eis | Komt uit |
|---|---|---|---|---|
| `Aanmelding` op een `Keuzedeel aanbod`, met haar plaats in de voorkeursvolgorde | Student Keuze Systeem | de student bewerkt | FE-LR1-01: Het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie | IE-LR1-01 |
| `Aanmelding` op een `Keuzedeel aanbod`, met haar plaats in de voorkeursvolgorde | Student Keuze Systeem | het Planningssysteem leest | FE-LR1-02: Het Student Keuze Systeem levert per voorkeur van een student de `Aanmelding` op het `Keuzedeel aanbod` aan het Planningssysteem, met haar plaats in de volgorde | IE-LR1-01 |

**Vul in:**

| Informatieobject | Bronsysteem | Wie leest of bewerkt | Functionele eis | Komt uit |
|---|---|---|---|---|
| | | | *FE-LR..-..: Het <component> ...* | *IE-LR..-..* |
| | | | | |
| | | | | |

*Schrijf hier de uitwerking.*

# Uitwerking

Zet hieronder eerst het routeprofiel, en herhaal daarna de sjabloononderdelen tot de hele route gedekt is: de reizen, de scenario's, en per fase het proces met zijn informatie en systemen.

*Schrijf hier de uitwerking.*

# Eisenoverzicht

Alle eisen uit de sjabloononderdelen hierboven, bij elkaar. Samen met het eisenoverzicht van de leerroute scenario uitwerking is dit het pakket van eisen van de route, dat OKx SI overneemt en met de leveranciers naar technische eisen vertaalt.

Het overzicht is af wanneer:

1. elke eis uit de sjabloononderdelen erin staat, met dezelfde zin en hetzelfde nummer;
2. elke instellingseis de persona met de stap, het scenario of de procesfase noemt waaruit hij komt;
3. elke functionele eis de instellingseis noemt waaruit hij komt;
4. elke instellingseis minstens een functionele eis heeft, hier of in de leerroute scenario uitwerking;
5. elke eis voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis).

**Ingevuld voorbeeld** uit Leerroute 1 scenario:

| Nummer | Eis | Komt uit sjabloononderdeel | Komt uit eis of story |
|---|---|---|---|
| IE-LR1-01 | De instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst | reis van Jochem, stap kiezen keuzedelen | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| IE-LR1-02 | De instelling kan signaleren dat de keuzedeelruimte van een student oningevuld blijft, op een moment dat de student nog een nieuwe keuze kan maken | reis van Jochem, stap kiezen keuzedelen | dezelfde user story als IE-LR1-01 |
| IE-LR1-03 | De instelling kan een onderdeel voor een student opnieuw inplannen terwijl de rest van zijn programma doorloopt | scenario incidenteel temporiseren | geen story; volgt uit het scenario |
| IE-LR1-04 | De instelling kan de haalbaarheid van een `Opleiding specificatie` bepalen voordat zij het onderwijsaanbod publiceert | procesfase 2, Publiceren en planbaar maken | Als planner wil ik de haalbaarheid van een opleiding bepalen voordat het onderwijsaanbod wordt gepubliceerd, met als doel dat studenten zich alleen oriënteren op aanbod dat de instelling kan uitvoeren |
| FE-LR1-01 | Het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie | informatie en systemen, fase 6 | IE-LR1-01 |
| FE-LR1-02 | Het Student Keuze Systeem levert per voorkeur van een student de `Aanmelding` op het `Keuzedeel aanbod` aan het Planningssysteem, met haar plaats in de volgorde | informatie en systemen, fase 6 | IE-LR1-01 |
| FE-LR1-03 | *volgt in de leerroute scenario uitwerking, bij uitwisseling F2-03* | | IE-LR1-04 |

**Vul in:**

| Nummer | Eis | Komt uit sjabloononderdeel | Komt uit eis of story |
|---|---|---|---|
| IE-LR..-01 | | | |
| IE-LR..-02 | | | |
| FE-LR..-01 | | | |
| FE-LR..-02 | | | |

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
