Executive Summary

Informatiemodel uitgelijnd met ROSA/KOI-standaarden: Niek Derksen heeft een nieuwe iteratie gepusht waarin terminologie voor o.a. onderwijseenheid-aanbod en leergelegenheid consistent is gemaakt met landelijke modellen om semantische discussies met externe architecten voor te zijn.

Conceptuele gelaagdheid vastgesteld: Het model onderscheidt nu strikt het kwalificatiekader (o.a. crebo-dossier), de onderwijsspecificatie (het ontwerp) en het onderwijsaanbod (de realisatie), waarbij leeruitkomsten losgetrokken zijn van het kwalificatiekader voor betere onderwijskundige zuiverheid.

Happy flow voor curriculumontwerp gedefinieerd: Er is een interactiepatroon ontworpen tussen de curriculumontwerptool en de onderwijscatalogus waarbij gebruik wordt gemaakt van UUID's voor hergebruik van bestaande componenten en een PubSub-mechanisme voor het synchroniseren van updates, in de specificatie-repo.

Besluit over technisch fundament: Niek Derksen integreert de volledige OEAPI-specificatie in de ontwikkelomgeving om consistentie op attribuutniveau te waarborgen, ondanks de huidige beperkingen in contextlimieten van de gebruikte AI-modellen.

Strategische scholen-tour gepland: Niels van Duin start gesprekken met koploper-scholen (o.a. Rijn IJssel, Alfa) om awareness te creëren rondom de SKS-componenten en om de prioriteitenstelling van het project te bewaken ten opzichte van externe verwachtingen.

Full Summary

Deze samenvatting bespreekt de voortgang van het informatiemodel, de technische interactiepatronen tussen onderwijssystemen en de strategie voor stakeholdermanagement richting de mbo-instellingen.

Herziene Structuur van het Informatiemodel

Niek Derksen heeft een tweede iteratie van het informatiemodel opgeleverd om de consistentie in terminologie te verbeteren. Zowel in Archimate als in een hoofdstuk binnen de eerste iteratie op het specificatie document.

Het model is gebaseerd op een boomstructuur, technisch gedefinieerd als een directed acyclic graph (DAG), om cyclische redeneringen te voorkomen.

Er is een expliciete scheiding aangebracht tussen het kwalificatiekader en de leeruitkomsten, wat een correctie is op de eerdere oversimplificatie in de MORA-voorstellen.

De hiërarchie van leeruitkomsten is nu als volgt vastgelegd:

Op kwalificatie- en dossierniveau zijn er geen directe leeruitkomsten gedefinieerd.

Op kerntaakniveau worden collecties van leeruitkomsten geaggregeerd.

Op werkprocesniveau worden de specifieke leeruitkomsten gedefinieerd.

Op lesniveau wordt gesproken over lesdoelen of beoogde resultaten.

De onderwijsspecificaties zijn uitgelijnd met de ROSA en het KOOI (Kernonderwijsinformatiemodel).

De gehanteerde terminologie volgt strikt de semantiek van deze standaarden om discussies met architecten te minimaliseren.

De lagen zijn als volgt onderverdeeld:

Opleidingsspecificatie (gekoppeld aan het kwalificatiedossier).

Opleidingsprogrammaspecificatie (gekoppeld aan de kwalificatie).

Onderwijseenheidsspecificatie (gekoppeld aan de kerntaak).

Leeronderdeelspecificatie (gekoppeld aan het werkproces).

Interactiepatronen en Systeemarchitectuur

De interactie tussen de Curriculumontwerptool (CO) en de Onderwijscatalogus (OC) is technisch aangescherpt voor de zogenaamde happy flow.

De CO-tool bevraagt de OC op basis van leeruitkomsten om bestaand aanbod te hergebruiken.

Indien er nieuw aanbod nodig is, wordt een Request for Specification ingediend bij de OC, waarna de onderwijsontwikkelaar de fijnmazige details invult.

Voor het synchroniseren van wijzigingen wordt gekozen voor een Pub/Sub-model (Publisher/Subscriber) via een message bus in plaats van enkel point-to-point koppelingen.

Dit model borgt dat alle aangesloten systemen op de hoogte blijven van wijzigingen in de onderwijsspecificaties, wat cruciaal is voor de integriteit van de planning.

Er is een fundamentele discussie gevoerd over de omgang met extern onderwijsaanbod van andere instellingen.

Instellingen kunnen kiezen tussen het adopteren van een referentie (waarbij de release cycle van de bron gevolgd wordt) of het klonen van de specificatie.

Klonen biedt meer controle over de eigen lifecycle, maar brengt het risico op ongecontroleerde wildgroei van data met zich mee.

Strategie en Stakeholdermanagement

Niels van Duin start vanaf 30 april 2026 een tour langs diverse koplopersscholen om de plannen te toetsen.

De tour omvat bezoeken aan Rijn IJssel, Alfa College en Midden-Nederland.

Het doel van deze gesprekken is het creëren van bewustwording rondom de SKS-componenten en het inventariseren van de huidige inrichting en tekortkomingen bij deze scholen.

Niels van Duin Neemt in dit proces de rol van technische sparringpartner voor collega Alda, om gezamenlijk te bewaken dat afgestemde prioriteiten met scholen aansluiten bij de architectuurlijn.

Het huidige ontwikkelproces fungeert als een skelet voor de uiteindelijke specificaties.

Hoewel Niek Derksen momenteel veel werk verzet buiten de formele werkgroepen om, wordt dit gezien als een noodzakelijke versnelling om een basis te leggen waar anderen op kunnen schieten.

Jos zal worden ingezet om specifieke hoofdstukken van de gegenereerde documentatie te controleren op onjuistheden en inconsistenties.

Er wordt overwogen om de volledige meta-repository te verhuizen naar de huidige werkomgeving om de context voor de specificatie-ontwikkeling te versterken.