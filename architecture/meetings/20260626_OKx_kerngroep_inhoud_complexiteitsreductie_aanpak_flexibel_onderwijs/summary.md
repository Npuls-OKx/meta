## Executive Summary

- **Strategische focus op complexiteitsreductie**: **Mark Hoogenboom** stelt voor om de fenomenale complexiteit van flexibel onderwijs te vertalen naar een eenvoudig, iteratief model (in 3 tot 5 stappen) dat scholen kunnen begrijpen en implementeren.
- **Iteratief onderwijsontwerp voor kiesbaarheid**: In de eerste iteratie hoeft onderwijs nog niet volledig 'leverbaar' te zijn; met slechts 5 of 6 datapunten (naam, leeruitkomst, certificaat, toetsvorm en periode) kan een student al een eerste keuze of belangstelling registreren via de **OOX-koppeling**.
- **Besluit over scope-beperking**: Om de technische koppeling uitvoerbaar te houden, wordt geadviseerd om fijnmazige roostering (specifieke dagen/uren) buiten de **OOX-koppeling** te laten en dit binnen de applicaties van de individuele instelling op te lossen.
- **Prioriteit voor organisatie-inrichting en planconcepten**: **Niek Derksen** gaat de samenhang tussen informatievoorziening, roostering en organisatievormen concreet maken voor verschillende scenario's (zoals de samenwerking tussen _DNA_, _NEXE_ en _Drenthe College_).
- **Volgende stappen**: **Mark Hoogenboom** vult de openstaande tickets aan om de visie op complexiteitsreductie te formaliseren, waarna **Mark Hoogenboom**, **Niels van Duin**, **Niek Derksen** en de nieuwe architect (Geric) dit gezamenlijk uitwerken tot een presenteerbaar model voor scholen.

## Full Summary

### Strategische visie op complexiteitsreductie in onderwijsontwerp

- Het hoofddoel is om het onderwijsontwerpproces zo te beschrijven dat duidelijk wordt wanneer onderwijsspecificaties voldoende informatie bevatten om planbaar en kiesbaar te zijn.
    - **Mark Hoogenboom** stelt voor om de brute complexiteit van het onderwijs te reduceren door een iteratieve aanpak te hanteren, waarbij de focus ligt op wat een school aan studenten kan uitleggen.
    - Door de scope te verkleinen en niet alle anekdotische scenario's direct in de techniek op te lossen, blijft de OKX-koppeling hanteerbaar en uitvoerbaar.
        - Een essentieel uitgangspunt is dat complexe roostervraagstukken binnen één instelling door de eigen applicaties opgelost moeten worden en niet via de OKX-koppeling tussen scholen hoeven te lopen.

### Iteratieve fasering van kiesbaarheid naar leverbaarheid

- Het ontwerp van flexibel onderwijs moet worden opgedeeld in verschillende iteraties om de hoeveelheid benodigde data per fase te beheersen.
    - In de eerste iteratie is het onderwijs voor minder dan 10% definitief, maar moet het al wel in de Onderwijscatalogus (OC) en het studentenfunnelsysteem staan.
        - Studenten kunnen in deze fase al kiezen op basis van de modulenaam, het certificaat, de leeruitkomsten, de toetscomponent en de globale periode.
        - De eerste iteratie is met name geschikt voor specifieke persona's, zoals topsporters, die enkel de toetscomponent willen afleggen zonder lessen te volgen.
    - Naarmate het proces vordert, neemt de informatiedichtheid toe tot het onderwijs in iteratie 5 volledig leverbaar is.
        - In iteratie 2 of 3 wordt pas bepaald welke specifieke middelen, zoals brandweerfaciliteiten voor een praktijkdag, aanwezig moeten zijn.
        - Vanaf iteratie 3 of 4 vindt de gedetailleerde capaciteitsplanning plaats voor mensen, lokalen en specifieke lesdagen.
    - De student moet gedurende het proces zijn keuze drie tot vier keer herbevestigen naarmate er meer details over locatie en tijdstip bekend worden.

### Logistieke randvoorwaarden en planningsprincipes

- Er moet een fundamenteel onderscheid gemaakt worden tussen wat centraal geregeld wordt en wat de verantwoordelijkheid van de student of de school is.
    - **Niels van Duin** benadrukt dat gelijktijdig persoonlijk roosteren over meerdere omgevingen onmogelijk is zonder duidelijke prioriteiten en tijdigheid in het vastzetten van variabelen.
        - In het Jochem-scenario is 95% van de opleiding in één omgeving en hoeft enkel voor het keuzedeel afstemming tussen verschillende omgevingen plaats te vinden.
        - Scholen moeten beleid maken over prioriteitsstelling, bijvoorbeeld of de primaire opleiding altijd voorrang krijgt op een keuzedeel om vertraging te voorkomen.
    - De complexiteit aan de aanbodzijde kan worden beperkt door geografische en tijdsgebonden spelregels, zoals het aanbieden van een specifiek keuzedeel op een vaste middag in een vaste regio.
        - Indien een module door te weinig studenten (bijvoorbeeld minder dan 5) wordt gekozen, kan de school besluiten geen resources in te zetten en de module niet te realiseren.

### Operationele actiepunten en documentatie

- De huidige abstracte procesplaten moeten worden vertaald naar concrete, begrijpelijke stappen voor scholen en leveranciers.
    - **Niek Derksen** heeft twee issues aangemaakt om de samenhang tussen onderwijsspecificatie, planningsfasen en organisatie-inrichting vast te leggen.
        - **Mark Hoogenboom** zal deze tickets uiterlijk volgende week controleren en aanvullen om de visie op complexiteitsreductie concreet te maken.
    - Het onderzoek moet leiden tot een pakket waarin drie dimensies samenkomen: de informatievoorziening, de roostering en de organisatorische inrichting.
        - Dit pakket moet bruikbaar zijn voor zowel grote eenheden zoals Amsterdam-Flevoland als voor kleine, lokale instellingen.
    - Er wordt gewerkt aan een abstractie in de vorm van een presentatie om het complexe onderzoek begrijpelijk te maken voor scholen en adviseurs.

-- tweede summary doordat tool opname fout liep en herstart moest worden --

## Requirements & Context

- Het project betreft de **architectuur aanpak voor flexibel onderwijs**.
- Er is behoefte aan het **uitwerken van concepten** en het vastleggen van specificaties.
- Het doel is om een **duidelijke aanpak** te creëren voor het ontwerpen van flexibel onderwijs, die scholen kunnen toepassen.
- De huidige fase van het project bevindt zich in de **business architectuur**, waarbij de focus ligt op het begrijpen en delen van de concepten voordat er gedetailleerde oplossingen worden uitgewerkt.

## Scope

- **In Scope:**
    - Het uitwerken van een aanpak voor complexiteitsreductie, specifiek voor flexibel onderwijs, die alleen toegepast hoeft te worden bij vier en vijf scholen.
    - Het opstellen van een document dat de aanpak voor flexibel onderwijs beschrijft, gericht op hoe scholen dit kunnen toepassen.
    - Het uitwerken van de specificatie voor open tickets.
    - Het creëren van een template of eerste uitwerking van concepten voor Larissa, die veel van de besproken concepten zal bevatten.
    - Het modelleren van bedrijfsprocessen op ArchiMate-niveau, zodat deze begrijpelijk zijn voor afnemers en processen gekoppeld kunnen worden aan informatie.
    - Het testen van de ontwikkelde aanpak in de POC (Proof of Concept) met scholen.
- **Out of Scope:**
    - Het direct uitwerken van een volledige specificatie van de koppeling in de eerste iteraties.
    - Het in detail uitwerken van het hele proces van flexibel onderwijs in de beginfase, aangezien dit in latere iteraties aan bod komt.

## Technical & Implementation Details

- Er is een voorkeur voor het gebruik van ArchiMate voor het uittekenen van businessprocessen, omdat dit visueel dicht bij BPMN ligt, maar het ook mogelijk maakt om processen te koppelen aan informatie.
- De uitdaging is om een bruikbaar format te vinden voor de uitwerkingen, aangezien BPMN niet geschikt is voor het weergeven van de ontwikkeling van informatie, en ArchiMate als te complex wordt ervaren.
- De eerste uitwerkingen van de koppelspecificaties moeten zich richten op de minimale informatie die nodig is om onderwijs te kunnen aanbieden, zoals cursusduur en periode, zonder gedetailleerde studentinformatie.
- De informatieproducten die worden opgeleverd, moeten de koppelspecificatiedocumenten bevatten.
- De specificatie van het onderwijs en de organisatie van het onderwijs kunnen los van elkaar worden gezien, ondanks hun afhankelijkheid, om de complexiteit te beheren.

## Decisions & Next Steps

- Er is besloten om een kleine groep van vier personen te vormen om de aanpak verder uit te werken.
- **Mark Hoogenboom** zal een voorstel uitwerken voor de aanpak van complexiteitsreductie.
- **Niek Derksen** zal aan de slag gaan met open tickets en de specificatie verder uitwerken.
- **Niek Derksen** zal een template of eerste uitwerking voor Larissa voorbereiden.
- **Niek Derksen** zal een meeting inplannen voor volgende week woensdag, met als eerste mogelijke datum voor de bespreking volgende week vrijdag.
- **Niels van Duin** zal zaken voorbereiden met betrekking tot zijn ideeën over de architectuur.
- Er is een besluit genomen om ArchiMate te gebruiken voor het modelleren van businessprocessen, omdat dit de koppeling van processen aan informatie mogelijk maakt.