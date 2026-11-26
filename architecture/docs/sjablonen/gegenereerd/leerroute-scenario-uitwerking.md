```{=openxml}
<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/><w:tblBorders><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders><w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Versie</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">0.0.1</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Auteurs</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">OKx, pijler Leren Zonder Drempels (Npuls)</w:t></w:r></w:p></w:tc></w:tr><w:tr><w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr><w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Datum</w:t></w:r></w:p></w:tc><w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr><w:p><w:r><w:t xml:space="preserve">datum van invullen</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
```

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers vullen de regels, de business analisten leggen ze naast het model |
| Voorbeeld | [de uitwerking van leerroute 1 met Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |
| Inleveren | terug naar OKx SI als Word-bestand |

## Productplaatsing

![De producten rond sjabloon leerroute scenario uitwerking in het informatiemodel, met dit product uitgelicht](<img/leerroute-scenario-uitwerking/product-breakdown.png>)

Het uitgelichte vak is het product dat u met dit sjabloon beschrijft. De kleine plaat eronder toont de hele productafbakening, met een kader om deze uitsnede.

Het volgt op het leerroute scenario en toetst het informatiemodel aan die route.

Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager eerder is; de hele plaat staat in de [productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/architecture/producten/product-breakdown/README.md).

## Doelstelling document

Dit document legt een leerroute scenario stap voor stap naast het informatiemodel, zodat zichtbaar wordt of het model de werkelijkheid van die route draagt en waar het tekortschiet.

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

Dit document levert **functionele eisen**, samen met de instellingseisen. Zo ziet zo'n eis eruit, met de keten erboven en eronder:

| Soort | Voorbeeld |
|---|------------------------------------------------|
| User story uit de PoC-inbreng | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Instellingseis, eerder | de instelling kan per keuzedeelruimte de voorkeursvolgorde van de student vastleggen voordat zij plaatst |
| **Functionele eis, uit dit document** | **het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie** |
| Technische eis, verderop | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

## Kwaliteit van een eis

Een eis is bruikbaar wanneer een leverancier hem kan lezen zonder de instelling te bellen. Wat hier staat is een voorstel voor een sectorafspraak: opgesteld uit de inbreng van afzonderlijke instellingen, vastgelegd als afspraak, en daarna de grond voor de technische specificatie. Schrijf elke eis uit op de plek waar hij ontstaat, en toets hem aan de criteria hieronder.

**Een functionele eis:**

1. is een zin die opent met de applicatiecomponent, in de naam van de [hoofdplaat informatiestromen](https://github.com/Npuls-OKx/meta/blob/dev/project/README.md);
2. noemt wat de component doet en met welke informatieobjecten, elk met de naam van het objecttype uit de [begrippenlijst](https://github.com/Npuls-OKx/meta/blob/dev/architecture/docs/specificatie/begrippen/begrippenlijst.md), tussen backquotes;
3. kiest het objecttype dat bij het moment past: een `Aanmelding` op aanbod is een wens, een verbintenis bestaat pas wanneer zij is aangegaan;
4. draagt een vast nummer `FE-LR<route>-<volgnummer>` uit het nummerregister van de route, het eisenoverzicht van het leerroute scenario;
5. noemt de instellingseis waaruit hij komt;
6. beschrijft gedrag; formaat, protocol en veldnamen volgen in de technische eis;
7. is toetsbaar: er is een invoer te noemen met de uitkomst die de component dan geeft;
8. draagt een gedrag; een tweede gedrag krijgt een eigen nummer.

| Soort | Zwak | Wat eraan ontbreekt | Sterk |
|---|--------|------|------------|
| functionele eis | Het systeem ondersteunt voorkeuren voor keuzedelen | de component, de gegevens en het gedrag ontbreken | Het Student Keuze Systeem legt per keuzedeelruimte de `Aanmeldingen` van een student vast in volgorde van voorkeur, elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en optioneel de onderwijslocatie |
| functionele eis | Het Student Keuze Systeem stuurt de voorkeuren als JSON-lijst naar het Planningssysteem | legt het formaat vast; dat hoort in de technische eis | Het Student Keuze Systeem levert per voorkeur van een student de `Aanmelding` op het `Keuzedeel aanbod` aan het Planningssysteem, met haar plaats in de volgorde |

## Business analyse en aggregatie van pakket van eisen

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier sterker dan elders, omdat een voorbeeld overtuigt: een regel die uit een enkele instelling komt en hier als voorbeeld staat, leest als sectorpraktijk.

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

Dit document is een herhaling van twee sjabloononderdelen. Onderdeel A legt een processtap vast: wie handelt, en welk informatie-element daar ontstaat. Onderdeel B legt een uitwisseling vast: het hele ingevulde informatievoorbeeld dat van de ene applicatiecomponent naar de andere gaat, met de functionele eisen die daaruit volgen.

Herhaal A tot er een uitwisseling plaatsvindt, zet dan B neer, en ga verder met A. Stop wanneer het hele leerroute scenario is doorlopen. Het aantal sjabloononderdelen ligt open; de dekking van het scenario bepaalt hoeveel het er zijn.

De opbrengst van dit document is tweeledig: het [Eisenoverzicht](#eisenoverzicht) met de functionele eisen per uitwisseling, en de [Hiaten in het model](#hiaten-in-het-model). OKx SI vertaalt beide met de leveranciers naar technische eisen.

De uitgewerkte vorm staat in [de uitwerking van leerroute 1 met Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md). Die loopt alle acht fasen door; dat is de diepgang waar dit document naartoe werkt.

# Sjabloononderdeel A: processtap

Kopieer dit sjabloononderdeel voor elke processtap. De nummering volgt het leerroute scenario: F1-01 is de eerste stap van fase 1.

Een onderdeel is af wanneer ook de **relaties naar eerder ontstane informatie** erin staan: waaraan hangt het nieuwe element, en wat verwijst ernaar. Die relaties zijn wat de uitwerking over het model zegt.

In het voorbeeld hieronder draagt het keuzedeel meerdere relaties tegelijk: het ontstaat als eigen programmaspecificatie en hangt aan de keuzedeelruimte en de leeruitkomsten uit eerdere stappen.

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-08 - Kiesbaar onderwijsprogrammaonderdeel: keuzedelen en minor](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-08---kiesbaar-onderwijsprogrammaonderdeel-keuzedelen-en-minor)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. er staat een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze processtap uitgelicht;
2. de plaat toont de actor, de processtap en het informatie-element dat daar ontstaat, elk met de term uit de begrippenlijst;
3. de plaat toont **de relaties naar de informatie-elementen die in eerdere sjabloononderdelen zijn ontstaan**, met het nummer van dat onderdeel;
4. de tabel is volledig ingevuld, met een voorbeeldwaarde voor de persona van deze route;
5. wat de begrippenlijst of het informatiemodel mist staat onder [Hiaten in het model](#hiaten-in-het-model).

**Eisen** *dit hoofdstuk levert geen eis op; het geeft de context waarin de eisen van de andere hoofdstukken te lezen zijn*

**Ingevuld voorbeeld** uit Leerroute 1 scenario uitwerking:

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | F1-08 |
| Processtap | Keuzedeelprogramma als eigen specificatie vormgeven |
| Actor | onderwijsontwerper |
| Applicatiecomponent | Curriculum ontwerptool |
| Ontstaat | `Keuzedeel`, een bijzondere vorm van de `Opleidingsprogramma specificatie`; in het informatiemodel staat dat als voorstel |
| Relaties naar eerder ontstane elementen | hangt via de `Student keuze regelset` aan de `Keuzedeelruimte` uit F1-07; draagt eigen `Onderwijseenheid specificaties`, elk met hun `Leeruitkomst` |
| Voorbeeldwaarde | K0037 Farmaceutische Patientenzorg (480 SBU, verdiepend) |

**Vul in:**

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *F1-01* |
| Processtap | *welke stap uit het leerroute scenario* |
| Actor | *wie handelt, met de rol uit het scenario* |
| Applicatiecomponent | *welk systeem daarbij hoort* |
| Ontstaat | *welk objecttype hier voor het eerst bestaat* |
| Relaties naar eerder ontstane elementen | *waaraan het hangt en wat ernaar verwijst, met het nummer van het sjabloononderdeel waar dat element ontstond* |
| Voorbeeldwaarde | *de ingevulde waarde voor deze persona* |

![Voorbeeld van sjabloononderdeel A: het kiesbare onderwijsprogrammaonderdeel, met de relaties naar de opleidingsspecificatie en de keuzedeelruimte die eerder zijn ontstaan](<img/leerroute-scenario-uitwerking/f1-08-onderwijsontwerper-geeft-keuzedelen-en-minor-een-eigen-specificatie.png>)

*Schrijf hier de uitwerking.*

# Sjabloononderdeel B: uitwisseling

Kopieer dit sjabloononderdeel voor elke uitwisseling. Over de lijn gaat het hele samenhangende voorbeeld: het objecttype met alles wat eraan hangt.

Het voorbeeld hieronder is er een met een volle structuur: het verzoek om onderwijsaanbod neemt de specificatiestructuur en de planbare waarden mee, zodat het planningssysteem zonder navraag kan plannen.

Elke uitwisseling levert functionele eisen op: wat de leverende component moet kunnen leveren, en wat de afnemende component ermee moet kunnen doen. Haal elk nummer uit het eisenoverzicht van het leerroute scenario: dat is het nummerregister van de route. Zo blijft een nummer vast en uniek, ook wanneer twee documenten eisen toevoegen.

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-03---verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning)

**Acceptatiecriteria** Dit sjabloononderdeel is af wanneer dit klopt:

1. er staat een ArchiMate-plaat of een SVG-render daarvan, met de scope van deze uitwisseling uitgelicht, beide applicatiecomponenten en de richting;
2. het informatievoorbeeld draagt elk objecttype **met zijn relaties**, zodat zichtbaar is wat de ontvanger binnenkrijgt;
3. het veld Aanleiding noemt de processtap die de uitwisseling veroorzaakt, met het nummer van dat sjabloononderdeel;
4. het veld Informatiestroom noemt het nummer uit het leerroute scenario;
5. elke functionele eis aan de leverende of de afnemende component staat uitgeschreven en genummerd, met de instellingseis waaruit hij komt, en voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis).

**Functionele eisen** *wat een component moet doen met welke gegevens; schrijf elke eis uit met zijn nummer en de instellingseis waaruit hij komt*

**Ingevuld voorbeeld** uit Leerroute 1 scenario uitwerking:

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | F2-03 |
| Van | Onderwijscatalogus |
| Naar | Planningssysteem |
| Aanleiding | het verzoek om onderwijsaanbod uit F2-02, nadat F2-01 de specificatie planbaar heeft gemaakt |
| Informatievoorbeeld | het `Verzoek tot Aanbod / Intekening op specificatie` Planopgave Apothekersassistent, cohort 2026, met de `Opleiding specificatie` Apothekersassistent, versie 2026.1, haar `Opleidingsprogramma specificatie` BOL voltijd, en per `Onderwijseenheid specificatie` en `Leeronderdeel specificatie` de `Leeruitkomst` en de planbare waarden: Blok B1-K1 met 80 uur begeleide onderwijstijd, een praktijkruimte en een docent farmacie. De gewenste periode gaat mee in de `Nominale Leerroute`, die in het informatiemodel als voorstel staat |
| Informatiestroom | OC-P&R, de koppeling tussen de Onderwijscatalogus en het Planningssysteem |
| Functionele eisen | FE-LR1-003: De Onderwijscatalogus stuurt het verzoek om onderwijsaanbod aan het Planningssysteem, met de specificatiestructuur en per eenheid de planbare waarden; komt uit IE-LR1-004 |

**Vul in:**

| Veld | Invulling |
|---|------------------------------------------------|
| Nummer | *F2-01* |
| Van | *welke applicatiecomponent levert* |
| Naar | *welke applicatiecomponent neemt af* |
| Aanleiding | *welke processtap deze uitwisseling veroorzaakt* |
| Informatievoorbeeld | *het ingevulde voorbeeld, met alle relaties* |
| Informatiestroom | *de koppeling op de hoofdplaat informatiestromen, bijvoorbeeld OC-P&R* |
| Functionele eisen | *FE-LR..-...: Het <component> ..., met de instellingseis waaruit hij komt; een regel per eis* |

![Voorbeeld van sjabloononderdeel B: het verzoek om onderwijsaanbod gaat met de hele specificatiestructuur en de planbare waarden van de onderwijscatalogus naar het planningssysteem](<img/leerroute-scenario-uitwerking/f2-03-onderwijscatalogus-stuurt-het-verzoek-met-de-specificatie-naar-het-planningssysteem.png>)

*Schrijf hier de uitwerking.*

# Uitwerking

Herhaal hieronder sjabloononderdeel A en sjabloononderdeel B tot het hele leerroute scenario is doorlopen. Houd de volgorde van het scenario aan, zodat beide documenten naast elkaar te leggen zijn.

*Schrijf hier de uitwerking.*

# Hiaten in het model

Welke sjabloononderdelen het informatiemodel niet kon dragen, per regel met wat ontbrak. Dit hoofdstuk is de tweede opbrengst van de uitwerking: een voorbeeld dat overal paste heeft niets gemeten. Volgt er een functionele eis uit een hiaat, schrijf hem dan uit in de laatste kolom en neem hem over in het eisenoverzicht.

| Nummer | Wat ontbrak | Wat er nodig is | Functionele eis |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

# Eisenoverzicht

Alle functionele eisen uit de uitwisselingen en de hiaten hierboven, bij elkaar. Samen met het eisenoverzicht van het leerroute scenario is dit het pakket van eisen van de route, dat OKx SI overneemt en met de leveranciers naar technische eisen vertaalt.

Het overzicht is af wanneer:

1. elke functionele eis uit de sjabloononderdelen erin staat, met dezelfde zin en hetzelfde nummer;
2. elke eis de uitwisseling of het hiaat noemt waaruit hij komt, en de instellingseis;
3. elke uitwisseling minstens een functionele eis heeft;
4. elk nummer uit het nummerregister van het leerroute scenario komt en daar ook staat;
5. elke eis voldoet aan [Kwaliteit van een eis](#kwaliteit-van-een-eis).

**Ingevuld voorbeeld** uit Leerroute 1 scenario uitwerking:

| Nummer | Eis | Komt uit sjabloononderdeel | Komt uit instellingseis | Status |
|---|---|---|---|---|
| FE-LR1-003 | De Onderwijscatalogus stuurt het verzoek om onderwijsaanbod aan het Planningssysteem, met de specificatiestructuur en per eenheid de planbare waarden | F2-03 | IE-LR1-004 | geldig |

**Vul in:**

| Nummer | Eis | Komt uit sjabloononderdeel | Komt uit instellingseis | Status |
|---|---|---|---|---|
| FE-LR..-... | | |  | |
| FE-LR..-... | | |  | |
| FE-LR..-... | | |  | |

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
