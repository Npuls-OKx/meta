# Projectplan OKx

**Realiseren van standaard gegevensuitwisseling ten behoeve van studentmobiliteit**, transformatiehub Wendbaar georganiseerd onderwijs. Versie 2.1 van 19 november 2024, aangepast na de tweedaagse van januari 2025 en bijgewerkt op 4 juni 2025.

## Leeswijzer

Dit is een bevroren bron: de tekst komt uit het projectplan en wordt hier niet geherformuleerd. Waar elders in deze repository naar het plan wordt verwezen, is dit het document dat bedoeld wordt. Een interpretatie of afleiding staat in [OKx in context](../context.md), met per sectie de herkomst erbij.

| | |
|---|---|
| Overgenomen | De secties 1, 9, 10, 11 en 12, en het conceptcommunicatieplan |
| Weggelaten | De sectie over de inzet van mensen en middelen. Die hoort niet in een publieke repository |
| Nog niet overgenomen | Sectie 8. Die staat in het plan en is hier nog niet opgenomen |
| Ingehaald | Sectie 9 over de governance. Hoe het project vandaag bestuurd wordt staat in [OKx in context](../context.md#governance) |
| Achterhaald in timing | De momenten in de secties 5 en 7. De roadmap is in oktober 2026 herijkt en getemporiseerd; de stand staat in [Status](../status.md) en in het [historisch overzicht](../historie.md) |

## 1. Opdrachtgever

De hoofdopdrachtgever is de transformatiehub Wendbaar georganiseerd onderwijs van Npuls. Daarnaast is er een samenwerking met DSV om de realisatie van de digitale sectorvoorzieningen voor studentmobiliteit te realiseren.

## 2. Reden en motivatie

Stel je voor dat je als lerende makkelijk een onderwijseenheid aan een andere onderwijsinstelling kunt volgen, in het mbo, hbo of wo, en dat de administratie hiervoor ook soepeltjes verloopt via een collectief aangelegde structuur. De transformatiehub Wendbaar georganiseerd onderwijs streeft ernaar om leerroutes te ontwikkelen die studenten in staat stellen om naadloos vakken en modules te volgen bij zowel mbo-, hbo- als wo-instellingen. Dit biedt studenten niet alleen een breder scala aan keuzemogelijkheden, maar draagt ook bij aan het vergroten van hun vaardigheden en arbeidsmarktkansen.

Om deze flexibiliteit te realiseren, wordt er gewerkt met richtlijnen die interoperabiliteit tussen systemen mogelijk maken, terwijl instellingen de ruimte behouden om hun eigen onderwijsvormen en inhoud te ontwikkelen. Daarvoor zijn afsprakenstelsels, standaarden en architecturen van groot belang. Gezamenlijke afspraken en processen zorgen voor optimale ondersteuning van de lerende, onder andere bij het maken van keuzes rondom het leertraject, het inschrijven, het volgen van onderwijs, toetsen, diplomering en het beheer van behaalde resultaten. Samenwerking tussen instellingen binnen de sectoren en tussen de sectoren is daarbij van groot belang.

### 2.1 Use-cases

Vanuit het mbo, hbo en wo zijn verschillende wensen opgehaald rondom studentmobiliteit. De use-cases die te onderscheiden zijn:

1. Studenten krijgen binnen hun opleiding, binnen de instelling meer keuzemogelijkheden.
2. Studenten krijgen buiten hun opleiding, binnen de instelling meer keuzemogelijkheden.
3. Studenten krijgen buiten hun instelling, binnen de sector meer keuzemogelijkheden.
4. Studenten krijgen buiten hun instelling, over sectoren heen meer keuzemogelijkheden.
5. Studenten krijgen buiten hun instelling, over landsgrenzen heen meer keuzemogelijkheden.
6. Studenten krijgen los van een inschrijving bij een instelling keuzemogelijkheden over sectoren heen.

Dit project draagt bij aan de programmadoelstellingen van Npuls:

| | Doel |
|---|---|
| Transformatiedoel | Sectorbreed overzicht |
| Transformatiedoel | Inzicht onderwijsaanbod |
| Transformatiedoel | Bevorderen studentmobiliteit |
| Ontwikkeldoel Student ID credential | Studenten kunnen eduID inzetten als Student ID credential |
| Ontwikkeldoel eduID | Studenten kunnen met een ID terecht bij alle instellingen |

En aan de streefwaarden van Npuls:

1. Studentmobiliteit: de resultaten van de pilot studentmobiliteit geven zicht op de schaalbaarheid en relevantie voor andere instellingen in fase 2.
2. eduID: tien instellingen hebben eduID in een primair proces geimplementeerd.

Tot slot maakt het project gebruik van de standaarden, producten en strategieen die horen bij Npuls en SURF: OOAPI, EduXchange, eduID en SURF eduhub.

## 3. Projectresultaten

1. Komen tot gezamenlijke taal en standaarden voor gegevensuitwisseling die een scala aan flexibilisering mogelijk maken in het mbo.
2. Komen tot functionele en technische gegevensuitwisseling voor het mbo, hbo en wo die studentmobiliteit ondersteunen.
3. Pilot studentmobiliteit starten in het mbo: implementatie en realisatie van de digitale koppelingen met eventueel gebruik van SURF-diensten.

**Toelichting.** Resultaat 1 is bedoeld om het mbo op vlieghoogte te brengen ten opzichte van het hbo en wo, omdat er in het mbo geen standaardisering is rondom modules, beschrijvingen daarvan en bijbehorende catalogi.

Resultaat 2 is bedoeld om gegevensuitwisseling tussen functionele blokken, de referentiecomponenten, binnen een school te automatiseren. In het wo wordt hiervoor vaak een integratielaag gebruikt, bij grote hbo-instellingen ook, maar niet alle hbo- en mbo-instellingen hebben een dergelijke integratielaag, waardoor specifieke digitale koppelingen gewenst kunnen zijn en het gebruik van relevante SURF-diensten.

Uiteindelijk dienen resultaat 1 en resultaat 2 ter voorbereiding op het daadwerkelijk kunnen starten met pilots rondom studentmobiliteit in het mbo, resultaat 3.

## 4. Projectscope

Gegevensuitwisseling tussen functionele blokken, de referentiecomponenten onderwijscatalogus, KRS, SVS, LMS en planning en roostering, voor het realiseren van interne studentmobiliteit. Dit als opmaat voor externe studentmobiliteit via EduXchange en later AII.

De procesketens onderwijslogistiek, onderwijsontwikkeling en onderwijsuitvoering en begeleiding van de referentiearchitectuur MORA zitten in elk geval binnen deze scope. Het project moet rekening houden met het feit dat ook andere functionele blokken worden geraakt. De te realiseren studentmobiliteit moet ook interoperabel zijn met de HORA.

In de tweedaagse in januari 2025 is bovenstaande scope bevestigd, en is vastgesteld dat het mogelijk is te werken met een hoofdproces met varianten ten behoeve van het kiezen van een lerende, om het gewenste wendbaar onderwijs goed te ondersteunen.

## 5. Projectaanpak

De aanpak is verdeeld tussen de transformatiehub Wendbaar georganiseerd onderwijs en Digitale sectorvoorzieningen (DSV), die verantwoordelijk is voor de oplevering van de onderdelen die bij haar staan. De hub Wendbaar is projectverantwoordelijk voor het geheel. Het plan markeert de wijzigingen uit de tweedaagse in groen; deze overname draagt die kleur niet, de inhoud staat er wel in.

**Onderzoeksfase, interdisciplinair:**

| # | Onderdeel | Bij wie |
|---|---|---|
| 1 | Opleveren van een architectuuradvies vanuit de relevante referentiearchitectuur en standaarden, als basis voor de vervolgstappen | DSV |
| 2 | Opleveren van de gereedheidsscan studentmobiliteit voor mbo-, hbo- en wo-instellingen | Wendbaar |
| 3 | Verkennen bij verschillende groepen uit mbo, hbo en wo welke gegevensuitwisseling in scope gebracht zou moeten worden | Wendbaar |
| 4 | Organiseren van een tweedaagse sessie met betrokkenen vanuit mbo, hbo en wo, ondersteunende organisaties zoals Npuls, MBO Digitaal, SURF en Kennisnet, en relevante leveranciers | Wendbaar |

De tweedaagse richtte zich op vier punten: welke gegevensuitwisseling moet plaatsvinden tussen welke functionele blokken; wat wordt geprioriteerd door de groep; met welke standaard kan de gegevensuitwisseling worden gerealiseerd; en het identificeren van raakvlakken met bestaande dienstverlening van SURF. In de tweedaagse zijn die punten behandeld en is een advies opgeleverd, zie de bijlage onder hoofdstuk 12. Na afronding van de onderzoeksfase volgt overleg over het vervolg in de regiegroep.

**Vervolg, punt 5: de geprioriteerde digitale koppelingen worden in een specifieke volgorde ontwikkeld en geimplementeerd, iteratief, door DSV en Wendbaar.**

| | Onderdeel | Product en moment |
|---|---|---|
| a | Onderzoeken welke onderdelen nog missen in de OOAPI of een andere standaard, en dit adresseren bij onder meer de werkgroep OOAPI van SURF | Q3 2025: een vastgesteld aantal missende onderdelen, aan te bieden bij de technische werkgroep OOAPI |
| b | MORA: splitsing van de functionaliteit P&R in twee referentiecomponenten, planning (meerjaren- en jaarplanning) en roosteren (roosterconstructie en wijzigingen) | Q3 2025: beschreven splitsing in de MORA |
| c | HORA en MORA: het proces voor meerjaren- en jaarplanning als basis voor het keuzeproces, het dienstregelingproces, lijkt te ontbreken | Toekomst: productbeschrijving later te leveren |
| d | Onderzoeken van de positionering van het keuzeproces van lerenden en de benodigde functionaliteit, nu SVS | Toekomst: productbeschrijving later te leveren |
| e | Afstemming met vertegenwoordigers van AII (aanmelding, inschrijving en intekenen) voor alignment op functionaliteit en gegevensuitwisseling. AII gebruikt ook de gewenste functionaliteit van de onderwijscatalogus | Continu proces, met een vastgesteld afstemproces tussen OKx en AII |
| f | Functioneel beschrijven van de geprioriteerde digitale koppelingen, te beginnen bij de onderwijscatalogus in relatie tot P&R, KRS en LMS, in die volgorde, met een architectengroep van ondersteunende organisaties en leveranciers | Q4: vastgestelde specificatiedocumenten voor de koppelvlakken OK-CP, OK-CL en OK-CK, op te stellen door de OOAPI-projectgroep OKx |
| g | Bouw van de functioneel beschreven digitale koppelingen door betrokken leveranciers, op basis van de gekozen standaarden | Q1 2026: gebouwde koppelingomgevingen door en tussen de leveranciers |
| h | Testen in pilots van gebouwde digitale koppelingen bij aangesloten instellingen | Q2 2026: volgens testscripts goedgekeurde en door scholen geaccordeerde koppelingen, leidend tot het stempel OKx |
| i | Bepalen van de impact op beleid, organisatie en proces, en die bespreken met leveranciers en instellingen | Q4 2025: uitgewerkte ondersteunende documentatie en de impact in beeld. Q2 2026: BOP-team voorzien van kennis, tools en hulpmiddelen, samen met de koploperscholen |
| j | Stimulering van het gebruik van digitale koppelingen bij alle instellingen door BOP-adviseurs en het adoptieteam van Npuls | Nader te bepalen |
| k | Pilot GetConnected, externe ontsluiting van gegevens uit de onderwijscatalogus | Q1 2026: nader te bepalen in overleg met GetConnected |

De acht onderdelen die onder a als mogelijk missend in de OOAPI zijn benoemd: grove planning met attributen die te specifiek zijn voor een meerjarenplanning; hierarchische resultaatstructuren; persoonlijke invulling van een leerroute; standaard leerroutes met tijdsloten, volgordes en afhankelijkheden; hoe om te gaan met een student die op meerdere opleidingen is ingeschreven; beschikbare capaciteit per course; tijdsloten behorend bij een course; en roostering, waar het component data nodig heeft over gespecialiseerde ruimtes omdat `roomType` nog te beperkend is.

**Punt 6:** accordering en oplevering van geteste digitale koppelingen, door Wendbaar en DSV.

**Punt 7:** start van de pilot studentmobiliteit in het mbo, met een aantal mbo-instellingen voor interne studentmobiliteit en met een aantal mbo-allianties voor externe studentmobiliteit rondom keuzedelen, door Wendbaar.

De stappen vanaf de tweedaagse kunnen iteratief worden uitgevoerd en hebben ook invloed op elkaar.

## 6. Projectdoelstelling

Het project zal resulteren in de ontwikkeling en vaststelling van een gemeenschappelijke taal en een set flexibele richtlijnen en functionele standaarden, die worden verankerd in een gestandaardiseerde architectuurmethode ten behoeve van studentmobiliteit.

Succes wordt gemeten door het aantal deelnemende instellingen dat deze richtlijnen heeft geimplementeerd, met een doel van ten minste tien instellingen tegen eind 2026. Daarmee is een deel van de gewenste use-cases uit 2.1 gerealiseerd bij deelnemende instellingen.

## 7. Projectplanning, concept

| # | Op te leveren | Moment |
|---|---|---|
| 1 | Advies over geraakte functionaliteit binnen MORA en HORA, de functionele hoofdblokken, op basis van de gewenste use-cases | december 2024 |
| 2 | Opgeleverde gereedheidsscan studentmobiliteit voor deelnemende mbo-, hbo- en wo-instellingen | januari 2024, zo in het plan |
| 3 | Uitgevoerde tweedaagse voor bepaling van scope en prioriteiten | januari 2025 |
| 4 | Advies voor de werkgroep OOAPI van SURF welke elementen toegevoegd zouden moeten worden voor het mbo om studentmobiliteit te kunnen realiseren | februari 2025 |
| 5 | Gerealiseerde functionele beschrijving van de gekozen geprioriteerde digitale koppelingen, in een document dat input is voor bouw door leveranciers | oktober 2025 |
| 6 | Voorbereiding pilots met deelnemende instellingen | december 2025 |
| 7 | Plannen maken voor pilots studentmobiliteit mbo voor 2026 | december 2025 |
| 8 | Begeleiding van de uitvoering van use-cases studentmobiliteit bij deelnemende mbo-instellingen | juli 2026 |
| 9 | Oplevering van de resultaten in een beheerorganisatie | december 2026 |

## 9. Governance project

De inrichting hieronder is sinds het plan veranderd. De huidige governance staat in [OKx in context](../context.md#governance); wat hier staat is de vastgestelde tekst van november 2024.

Het project is gepositioneerd onder de regiegroep studentmobiliteit van de transformatiehub Wendbaar georganiseerd onderwijs. Daarmee fungeert deze regiegroep als stuurgroep voor dit project. In deze regiegroep zitten vertegenwoordigers van veel stakeholders.

De projectorganisatie bestaat uit een aantal onderdelen:

| Onderdeel | Wat het doet |
|---|---|
| Cockpit studentmobiliteit mbo, hbo en wo | Samenwerking tussen scholen en leveranciers betreffende de te realiseren functionaliteit. Vaststellen vraag, prioriteiten, accordering functionele beschrijvingen, deelname aan pilots |
| Werkgroep OKx | Samenwerking van scholen met leveranciers en ondersteunende partners voor opstellen van de benodigde functionele specs |
| Kerngroep techniek, subwerkgroep OKE en OKx binnen de OOAPI-organisatie | Samenwerking van architecten (DSV, MBO Digitaal, SURF en betrokken leveranciers): oplevering functionele beschrijving en check met technische haalbaarheid. Bewaken van de standaarden |
| Pilotgroepen | Hierin wordt de gebouwde functionaliteit getest op werking in verschillende configuraties van aangesloten applicaties. In deze pilots wordt akkoord gegeven op een juiste werking door de deelnemende scholen |

De projectmanager zit de werkgroep OKx voor. De projectleider begeleidt de kerngroep techniek (subwerkgroep) en de pilotgroepen. De bezetting van de groepen wordt vormgegeven als de prioritering is gekozen.

## 10. Risico's en mitigerende maatregelen

| # | Risico | Maatregel |
|---|---|---|
| 1 | Concurrentie met veel andere initiatieven en projecten vanuit Npuls en bij scholen en leveranciers, waardoor focus te laag is of capaciteit te weinig beschikbaar is binnen de instellingen en leveranciers | Duidelijke verbinding leggen met initiatieven rondom AII, OKE, OOAPI en EduID, en afbakening ten opzichte van Edu-V |
| 2 | Ontbreken van beschikbaarheid architectuurcapaciteit | Functionaliteiten faseren |
| 3 | Functionele wensen en verwachtingen zijn te groot om te realiseren | Tussentijds meten en verwachtingen uitspreken |
| 4 | Het gedachtegoed rondom interne studentmobiliteit (tussen onderwijsteams en locaties) en externe studentmobiliteit tussen mbo, hbo en wo is nog te volatiel om een goed digitaal antwoord op te kunnen geven | Tussentijds meten, verwachtingen uitspreken, en dit via bestuurders agenderen |
| 5 | Instellingen in mbo, hbo en wo zijn zo divers ingericht dat er niet een of een beperkt aantal studentmobiliteitsoplossingen is | Keuze voor digitale koppelingen. Tussentijds meten, verwachtingen uitspreken, en dit via bestuurders agenderen |

## 11. Mogelijke alternatieven

| Alternatief | Afweging |
|---|---|
| Niets doen | Geen optie: flexibele studentmobiliteit vergt digitalisering en standaardisering |
| Per instelling realiseren | Geen optie: dan wordt de oplossing te versnipperd en kan er geen instellings- of sectoroverstijgende oplossing komen |
| De marktpartijen laten realiseren | Ontbreken van eenduidigheid en ontbreken van grip op standaardtaal; dat geldt met name bij instellingoverstijgende use-cases |

## 12. Bijlagen

Advies uitkomsten tweedaagse januari 2025, *Advies gegevensuitwisseling voor flexibilisering (OKX)*.

## Conceptcommunicatieplan

| Onderwerp | Boodschap | Doel | Wanneer | Prioriteit | Doelgroep | Vorm |
|---|---|---|---|---|---|---|
| Start | Naamsbekendheid maken, communiceren wat de te behalen resultaten zijn | Naamsbekendheid maken om scholen aangehaakt te houden | Na de zomer | Middel | mbo, hbo, wo, Npuls, MBO Digitaal, Kennisnet, Edustandaard | |
| Behaald projectresultaat | Komen tot gezamenlijke taal en standaarden voor gegevensuitwisseling die een scala aan flexibilisering mogelijk maken in het mbo | Informeren | In afstemming met de voortgang van de brede hub | Middel | Scholen | Conferentie, nog te bepalen |
| Behaald projectresultaat | Komen tot functionele en technische gegevensuitwisseling voor mbo, hbo en wo die studentmobiliteit ondersteunen | Informeren | In afstemming met de voortgang van de brede hub | Middel | Scholen | Conferentie, nog te bepalen |
| Behaald projectresultaat | Pilot studentmobiliteit starten in het mbo: implementatie en realisatie van de digitale koppelingen, met eventueel gebruik van SURF-diensten | Informeren | In afstemming met de voortgang van de brede hub | Middel | Scholen | Conferentie, nog te bepalen |
| Voortgang OKx techniek | Voortgang op techniek en standaarden: consumers OOAPI, aanpassingen MORA en MOKA, Edustandaard | Afstemming | Eens per twee maanden | Hoog | Ondersteunende diensten: SURF, MBO Digitaal (Verbinders), Edustandaard, Kennisnet, Npuls | |
| Projectvoortgang OKx BOP | Voortgang BOPSI, wat ook in de brede hub wordt gerapporteerd | | Eens per vier maanden | | mbo, hbo, wo, Npuls, MBO Digitaal, Kennisnet, Edustandaard | |
| Visualisatie OKx | Visualisatie OKx, vergelijkbaar met het Ganzenbord van OKE | Informeren | | | | Beeldtaal |

Relateert aan: #449.
