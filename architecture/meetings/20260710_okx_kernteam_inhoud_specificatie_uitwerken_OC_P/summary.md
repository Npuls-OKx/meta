## Requirements & Context

De bijeenkomst richt zich op het in kaart brengen van de **onderwijsspecificatiestructuur naar het plan- en roosterproces**, specifiek gericht op de overgang van specificatie naar het uiteindelijke onderwijsaanbod.

- Het bepalen van de **minimale gegevens en hiërarchische structuur** (zoals de koppeling van leeronderdeelspecificaties aan een planningsgroep) die vanuit een onderwijscatalogus (OC) nodig zijn om een capaciteits- en periodeplanning te kunnen maken.
- Het ondersteunen van **verschillende leerwegen en doelgroepvarianten** (zoals BOL, BBL, zijinstroom en hybride trajecten) binnen de specificatiestructuur, waarbij unieke programma's ontstaan die relationele en gedeelde onderdelen kunnen hergebruiken.
- Het structureren van **keuzedelen binnen de onderwijsspecificatie**, waarbij onderscheid wordt gemaakt tussen generieke, schoolbrede keuzedelen en beroepsgerichte, voorwaardelijke keuzedelen op kwalificatieniveau.
- Het definiëren van de **interactie tussen het OC- en het planningssysteem**, waarbij het planningssysteem leidend wordt in het verrijken van de specificatie met plaats- en tijdgegevens (aanbod) en het afhandelen van asynchrone processen en statusupdates na specificatiewijzigingen.

## Scope

### In Scope

- **Definiëren van de hiërarchische specificatiestructuur**
    - Het vastleggen van de verschillende organisatorische en onderwijskundige lagen binnen de specificatie:
        - De overkoepelende opleidingsspecificatie (de root-node binnen de onderwijscatalogus).
        - De splitsing in specifieke leerwegen, zoals de BOL- en BBL-varianten.
        - De splitsing naar specifieke doelgroepvarianten onder de leerwegen, waaronder reguliere instroom, zij-instroom, LLO en hybride trajecten.
        - De onderliggende onderwijseenheidsspecificaties en de daaraan gekoppelde leeronderdeelspecificaties (lessenreeksen).
- **Modelleren en structureren van keuzedelen binnen de specificatie**
    - Het onderscheiden van generieke, schoolbrede keuzedelen en beroepsgerichte keuzedelen.
    - Het registreren van de toelatingseisen, voorwaardelijkheden en de binding aan crebo's of kwalificatiedossiers voor de beroepsgerichte keuzedelen op het niveau van de onderwijseenheid.
- **Gegevensuitwisseling tussen het OC en het plan- en roostersysteem**
    - Het overdragen van de volledige specificatieboom (inclusief de hiërarchische relaties en unieke ID's) vanuit de onderwijscatalogus naar het planningssysteem ten behoeve van capaciteits- en periodeplanning.
    - Het opstellen van een standaard responsstructuur voor het terugkoppelen van verwerkingsresultaten en statusupdates.
    - Het definiëren van hoe het planningssysteem de specificatie transformeert naar concreet onderwijsaanbod door het toevoegen van planningsgegevens:
        - Tijd en datum (daytime range).
        - Locatiegegevens.
        - De unieke identifier van het gerealiseerde programma- of opleidingsaanbod met een referentie naar de bijbehorende specificatie.
- **Afhandelen van updates en wijzigingen in de specificatie**
    - Het specificeren van hoe wijzigingen in de specificatieboom (zoals een titelwijziging of urenwijziging) vanuit de onderwijscatalogus naar het planningssysteem worden gecommuniceerd, inclusief de verwerking van de hiërarchische relaties (parent-ID's) bij updates.

### Out of Scope

- **Gedetailleerde lesplanning en individuele lesroosters**
    - Het modelleren en gedetailleerd plannen van individuele, losse lessen onder het niveau van de lessenreeks (de leeronderdeelspecificatie).
- **HR- en docentadministratie**
    - Het in kaart brengen van HR-systemen of het koppelen van specifieke docenten aan de planning. Hoewel docentexpertise als eis binnen de specificatie kan worden opgenomen, valt het daadwerkelijke labelen van personen en de afstemming met HR buiten de scope van dit traject.
- **Opleidingsbrede uniformering van bedrijfsprocessen**
    - Het volledig gelijktrekken van alle interne bedrijfsprocessen en interne datastructuren binnen alle verschillende scholen en instellingen. De focus ligt uitsluitend op het definiëren van een gemeenschappelijke uitwisselingsstandaard en een gezamenlijk referentiekader (streefarchitectuur).
- **Definiëren van nieuwe security- of authenticatiestandaarden**
    - Het ontwerpen van nieuwe beveiligingsprotocollen. Er wordt uitsluitend gebruikgemaakt van reeds bestaande standaarden en overheidskaders, zoals OAuth2 en PKI-overheidscertificaten.

## Technical & Implementation Details

### Technische & implementatiedetails

- **Architectuur en informatiemodel (de specificatieboom)**
    - De onderwijsspecificatie is opgebouwd als een hiërarchische boomstructuur die vanuit de onderwijscatalogus (OC) naar het planningssysteem wordt gestuurd. Deze boom bestaat uit de volgende technische lagen:
        - **Opleidingsspecificatie (Root-node):** De overkoepelende identifier van de opleiding binnen de catalogus.
        - **Leerweg (Programmalaag 1):** De splitsing naar de specifieke leerweg, zoals BOL of BBL.
        - **Doelgroepprogramma (Programmalaag 2):** Een verdere verfijning voor specifieke groepen, zoals regulier, zij-instroom, LLO of hybride.
        - **Onderwijseenheidsspecificatie:** De modulaire eenheden waarin het onderwijsprogramma is opgedeeld. Op dit niveau worden ook de voorwaardelijkheden en crebo-koppelingen voor specifieke keuzedelen vastgelegd.
        - **Leeronderdeelspecificatie (Lessenreeks):** Het diepste niveau binnen de specificatieboom (de 'cut-off point'). Individuele lessen of lesdetails worden hieronder niet meer gemodelleerd.
    - **Relaties en overerving:**
        - Alle objecten binnen de boomstructuur moeten een expliciete verwijzing naar hun bovenliggende object bevatten (`parent-ID`). Dit is noodzakelijk om bij wijzigingen recursief te kunnen terugredeneren waar de wijziging invloed op heeft.
        - Elementen onder de unieke programma's (zoals specifieke onderwijseenheidsspecificaties) kunnen relationeel worden gedeeld en hergebruikt over verschillende leerwegen of doelgroepen heen.
- **API-ontwerp en gegevensuitwisseling (OAP & Amigo-aanpak)**
    - De gegevensuitwisseling wordt vormgegeven volgens de Amigo-aanpak om registratie als standaard (via OEAPI of EU-standaarden) mogelijk te maken.
    - Er wordt gebruikgemaakt van de Open Onderwijs API (OAP) als gedragen, extensibele standaard.
    - **Profiel en consumers:**
        - De implementatie wordt ingericht op basis van één enkel technisch profiel binnen OAP, gecombineerd met meerdere 'consumers' om specifieke datasets af te bakenen.
        - Het profiel specificeert welke eindpunten (`endpoints`) worden gebruikt, welke optionele velden uit de OAP-standaard verplicht worden gesteld, en welke specifieke extensies (consumers) worden toegepast voor niet-standaard velden.
    - **Beveiliging:**
        - Voor authenticatie en autorisatie wordt aangesloten bij de OAuth2-standaard en het gebruik van PKI-overheidscertificaten voor beveiligde gegevensuitwisseling bij gevoelige stromen (zoals persoonsgegevens).
- **Interactiepatronen en asynchrone processen**
    - Het plan- en roosterproces is vanwege de menselijke tussenkomst en de complexiteit van roostering inherent asynchroon.
    - **Initialisatie en validatie:**
        - Zodra een specificatie in het OC de status 'planbaar' bereikt, wordt de volledige specificatieboom via een `POST`-request aangeboden aan het planningssysteem.
        - Het planningssysteem voert een directe technische validatie uit en geeft direct een synchrone status respons terug:
            - Een positieve ontvangstbevestiging (waarna het asynchrone planningsproces start).
            - Een foutmelding bij onjuiste formattering (bijvoorbeeld een `HTTP 400 Bad Request`).
    - **Aanbodmodellering (Output):**
        - Het planningssysteem verrijkt de ontvangen specificaties tot een concreet 'aanbodobject'.
        - Het aanbodobject bevat uitsluitend gegevens die relevant zijn voor de planning (Single Responsibility): start- en eindtijden (`daytime range`), locaties en de unieke identifier van het gerealiseerde programma- of opleidingsaanbod met de referentie naar de OC-specificatie.
        - Terugkoppeling naar het OC gebeurt door het opleveren van deze unieke aanbod-ID's, zodat het OC via een verwijzing (bijvoorbeeld een iframe of applicatieve integratie) de actuele planning kan tonen zonder de volledige planningsdata zelf te dupliceren of te beheren.
    - **Wijzigingsbeheer (Updates):**
        - Bij wijzigingen in de specificatie (bijvoorbeeld een aanpassing van uren of titels) stuurt de onderwijscatalogus een update-event.
        - Om inconsistenties en complexe delta-berekeningen te vermijden, is het uitgangspunt dat de onderwijscatalogus bij een wijziging de volledige, geactualiseerde boom opnieuw aanbiedt, waarna het planningssysteem zelf de impact op de actieve planning bepaalt en het asynchrone proces herstart.

## Decisions & Next Steps

### Besluiten

- **Technische kaders en standaarden**
    - Er wordt gebruikgemaakt van de **Amigo-aanpak** voor het opstellen van het specificatiedocument, om aan te sluiten bij de Europese en OEAPI-standaarden.
    - De gegevensuitwisseling wordt gebaseerd op de **Open Onderwijs API (OAP)**, waarbij wordt gewerkt met **één profiel en meerdere consumers** om de complexiteit voor softwareleveranciers te beheersen en noodzakelijke uitbreidingen te ondersteunen.
    - Voor de beveiliging van de gegevensuitwisseling wordt aangesloten bij de **OAuth2-standaard**. Er wordt geadviseerd om voor gevoelige stromen gebruik te maken van **PKI-overheidscertificaten**, conform de landelijke richtlijnen.
    - Het plan- en roostersysteem wordt de **eigenaar van het aanbodobject**. Het onderwijscatalogussysteem (OC) blijft uitsluitend de bron voor de onderwijsspecificatie. Het aanbod in het OC wordt ontsloten via een verwijzing (zoals een ID of iframe) naar het planningssysteem om dataduplicatie te voorkomen.
- **Grenzen van de onderwijsboom**
    - De onderwijsspecificatiestructuur wordt opgebouwd als een **hiërarchische boom** (Opleiding -> Leerweg -> Doelgroep -> Onderwijseenheid -> Leeronderdeel/Lessenreeks).
    - Er is besloten om een harde grens te trekken bij de **lessenreeks (leeronderdeelspecificatie) als diepste niveau**. Individuele, losse lessen worden niet opgenomen in de uit te wisselen specificatie.

---

### Actiepunten

- **@niek**
    - Een apart **issue aanmaken in de milestone** voor het technisch uitwerken van de interactiepatronen en het asynchrone proces tussen het OC en het plan- en roostersysteem, inclusief de bijbehorende diagrammen uit de bijeenkomst.
    - Het opstellen van een **losse memo in Markdown-formaat** met daarin een korte procesbeschrijving, informatiemodellering, datamodellering en het interactiesequentiepatroon, om dit als pull request (PR) voor te leggen aan de softwareleveranciers.
    - De gemaakte boomstructuur en de transcriptie/samenvatting van deze bijeenkomst toevoegen aan de documentatie om de context te borgen.
- **Niels van Duin**
    - Het voorbereiden en voeren van het geplande gesprek op maandag met de nieuwe teamleider van Albeda/Rijnmond (**Alda Kroneman** noemde haar Alice) om haar aan te sluiten op de lopende materie rondom de planning en onderwijsspecificaties.
    - Het plannen van een sparringsessie met @niek en **Niels van Duin** om dieper in te gaan op de technische werking en de implementatie van de OAP-profielen en consumers, om eventuele onduidelijkheden bij ontwikkelaars weg te nemen.
- **Alda Kroneman**
    - Het op papier zetten van de benodigde capaciteit (FTE) en dit tijdens de vakantieperiode formeel indienen, om de benodigde ondersteuning en procesmapping voor de scholen te organiseren.