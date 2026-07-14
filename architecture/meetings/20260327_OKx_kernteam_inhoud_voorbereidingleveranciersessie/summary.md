## Executive Summary

- **Mock-ups voor flexibele leerroutes behandeld van STEDEN/NHL/YOS**: Niek presenteerde ontwerpen vanuit LZD community spotlight voor een systeem waarin studenten zelf modules, toetsvormen en leeractiviteiten (zoals Strategic Management) kiezen op basis van **leeruitkomsten** in plaats van vaste vakken.
- **Verschuiving naar leeruitkomsten als standaard**: De strategische koers wijzigt van traditionele leereenheden naar **leeruitkomsten** gekoppeld aan **SBU/EC** (studiebelastingsuren), waarbij het onderwijsontwerp complexer wordt om massa-maatwerk en studentmobiliteit tussen instellingen mogelijk te maken.
- **Architectuur en koppelingen**: Er zijn **22 kritieke informatiestromen** geïdentificeerd voor het project _OKX_; Niek constateert dat huidige sectorarchitecturen (MORA/HORA) onvoldoende specifiek zijn, waardoor het team zelf het fundament voor gegevensuitwisseling legt.
- **Besluit over tooling en governance**: Het team gebruikt **GitHub** als centrale _knowledge base_ en projectbord voor het ontwerpproces; Alda Kroneman en Scott benadrukken dat dit noodzakelijk is voor technisch versiebeheer, los van de algemene projectplanning.
- **Next steps**: Niek scherpt de presentatie voor leveranciers aan voor de sessie op **maandag**, waarna op **donderdag om 10:30 uur** een evaluatie volgt om de werkgroep van **7 april** voor te bereiden.


## Full Summary

Hieronder volgt de strategische samenvatting van de bespreking over de voortgang van het project rondom flexibele leerroutes en de voorbereiding op de leverancierssessies.


### Visie op Flexibele Leerroutes en Mockups

- Niek presenteerde mockups van een studentportaal (gebaseerd op NHL Stenden) waarin de verschuiving van traditioneel onderwijs naar flexibele leerpaden centraal staat.
  - Het systeem maakt gebruik van leeruitkomsten die in maximaal twee tot drie zinnen worden beschreven, ondersteund door specifieke indicatoren.
  - In het getoonde LLO-profiel (Life Long Learning) kan een student een eigen toetsvorm kiezen, zoals een stakeholderanalyse of bedrijfsbezoek, en eigen bewijslast toevoegen aan het portfolio.
  - Een cruciaal logistiek verschil is dat studenten hun eigen beschikbaarheid opgeven in plaats van een vast rooster te volgen, wat vraagt om verregaande integratie met agenda-systemen.
- Er is gesproken over de architectuur van het portfolio en de zogenaamde Student Wallet.
  - De school blijft verantwoordelijk voor de bewijslast en de opslag in het lokale portfolio.
  - Resultaten worden als micro-credentials uitgegeven aan een landelijke sectorvoorziening of de persoonlijke wallet van de student.
- Een voorbeeld van bestaande integratie van systemen vindt momenteel plaats in een centrale hub genaamd YOS(Your Own Space), systeem in productie bij STEDEN/NHL.
  - Dit platform koppelt Blackboard, Xedule, Office 365 en Progress aan elkaar om de voortgang van studenten te monitoren.
  - Alda Kroneman merkte op dat dit concept al door meerdere hogescholen en mbo-instellingen (zoals Saxion en ROC van Amsterdam) wordt gehanteerd binnen het ecosysteem van de LLO-katalysator.


### Strategische Aanpak en Architectuur (OKX)

- Het projectteam hanteert de Amigo-aanpak voor het realiseren van sectorstandaarden voor gegevensuitwisseling.
  - De focus ligt op het creëren van een gezamenlijke taal en technische specificaties voor mbo, hbo en vo om studentmobiliteit te faciliteren.
  - Er is geconstateerd dat de huidige sectorvisie vanuit het Ministerie van OCW onvoldoende specifiek is, waardoor het team zelf het fundament legt voor procesbeschrijvingen en koppelvlakken.
- Wat betreft de gegevensuitwisseling zijn er 22 informatiestromen geïdentificeerd voor het scenario waarin de student zelf kiest.
  - Van deze 22 stromen zijn er momenteel ongeveer 8 inhoudelijk aangeraakt of gemodelleerd.
  - Er bestaat een spanningsveld tussen de top-down curriculumontwerpen van instellingen en de bottom-up aggregatie van leeruitkomsten op lesniveau.
- Het team maakt gebruik van de OEAPI-standaard (Open Education API), maar ziet de noodzaak voor een specifiek consumer profile om de gewenste flexibiliteit te ondersteunen.
  - Leeruitkomsten worden de centrale sleutel voor de verbinding van onderwijs; zij bepalen de schaling van een leertraject (van een les van 30 minuten tot een programma van meerdere jaren).
  - De kwantificering van deze uitkomsten gebeurt via EC’s voor het hbo en SBU’s (Studiebelastingsuren) voor het mbo.


### Voorbereiding Leverancierssessies en Governance

- Voor de komende presentatie aan leveranciers (gepland op maandag en dinsdag in de komende week) is een specifiek narratief ontwikkeld.
  - De kernboodschap is dat niet het koppelen van systemen de grootste uitdaging is, maar het verwerken van de logistieke en onderwijskundige impact van flexibilisering.
  - Leveranciers worden uitgenodigd om deel te nemen via een publiek-private samenwerking, waarbij gebruik wordt gemaakt van een Knowledge Base op GitHub.
- De samenwerking met leveranciers en koploper-scholen wordt gefaciliteerd via asynchrone communicatie in GitHub.
  - Deelnemers kunnen discussies starten, issues inschieten voor de backlog en bijdragen aan code via Pull Requests.
  - Dit moet de snelheid van de ontwikkeling verhogen en de technische werkgroep direct betrekken bij de specificaties.
- Er is discussie over de governance en de structuur van de diverse werkgroepen.
  - Niek en Niels pleiten voor een werkgericht planbord in GitHub voor het ontwerpproces, los van het algemene projectbord van de projectleiders.
  - Voor de werkgroepvergadering op 7 april 2026 moet de commitment van de acht koploper-scholen expliciet worden bevestigd.


### Deadlines en Vervolgacties

- De definitieve presentatie voor de leverancierssessies wordt dit weekend door Niek afgerond.
- Op donderdag 2 april om 10:30 uur vindt een afstemming plaats om de sessie van 7 april 2026 voor te bereiden.
- Alda Kroneman zal de presentatie ombouwen tot een agenda voor de werkgroep op 7 april om de scholen te informeren en te betrekken bij de volgende stappen.
- Ruud zal worden gevraagd om een vereenvoudigd organogram op te stellen voor de governance-paragraaf in de presentatie.
