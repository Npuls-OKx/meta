## Executive Summary

Hier is de beknopte samenvatting van de vergadering:


- **Strategische visie op de **_**Student Ontwikkelings Wallet**_** (EDU-wallet) gepresenteerd**, waarbij Mark Hoogenboom drie basisprincipes vaststelt: de wallet is eigendom van het individu, instellingen vragen toestemming voor inzage, en de context (leer- zorg- of werkgeschiedenis) wordt via _EduID_ en publieke standaarden ontsloten.
- **Kritieke noodzaak voor een **_**Student Kiest Systeem**_** (SKS) en een modulaire onderwijsovereenkomst**, omdat het huidige systeem vastloopt op LLO-trajecten (Leven Lang Ontwikkelen) waarbij studenten losse modules en certificaten stapelen in plaats van volledige meerjarige opleidingen volgen.
- **Besluit: **Alda** start direct met het uitrollen van **_**Student Journeys**_** bij pilot-instellingen** (waaronder Amsterdam en Rijnland) om eigenaarschap te creëren en de abstracte procesarchitectuur visueel en tastbaar te maken voor onderwijsprofessionals.
- **Projectrisico geïdentificeerd wat betreft de interne adoptie en voortgang**, waarbij Mark Hoogenboom aangeeft dat de complexiteit leidt tot weerstand in het team; de focus verschuift nu naar het leveren van concrete koppelvlak-specificaties en _mockups_ om de fundering te bewijzen.
- **Volgende mijlpalen:** Leveranciersupdates op maandag en woensdag in week 14, gevolgd door de kick-off van de _Werkgroep Techniek_ op **7 april 2026**, waar de architectuurplaten in ArchiMate en de GitHub-omgeving centraal staan.


## Full Summary

In de vergadering van maart 2026 is de voortgang besproken van de architectuur voor flexibel onderwijs, met een sterke focus op de technische realisatie van de studentenwallet en de noodzakelijke cultuuromslag binnen onderwijsinstellingen.


### Architectuur van de Studentenontwikkelingswallet (EDU-wallet)

- Er wordt gewerkt aan een centrale studentenontwikkelingswallet die dient als bron voor de leercontext, zorgcontext en sociaal-pedagogische context van studenten.
  - De wallet is gebaseerd op het principe van individueel eigendom waarbij instellingen of werkgevers expliciet recht moeten aanvragen om gegevens in een specifieke context uit te lezen.
  - De technische koppeling wordt gefaciliteerd via Edu ID, dat fungeert als een broker tussen de identiteit van de student en de gegevens in de wallet.
  - Mark Hoogenboom benadrukt dat deze architectuur essentieel is voor het principe van een leven lang leren, waarbij gegevens uit de educatieve en arbeidscontext elkaar overlappen.
  - Voor de implementatie van het intake-proces binnen de MORA moet de studentcontext een trigger geven aan de administratieve systemen van de instelling om benodigde gegevens op te halen.


### Technische Specificaties en Koppelvlakken

- Niek en Mark Hoogenboom bespreken de noodzaak voor robuuste applicatie-naar-applicatie koppelingen die rekening houden met foutafhandeling en procesvolgorde.
  - Er wordt gebruikgemaakt van specifieke Enterprise Application Patterns om de betrouwbaarheid van berichtenverkeer te garanderen.
    - Guaranteed delivery zorgt ervoor dat berichten persistent blijven tot de daadwerkelijke aflevering is bevestigd.
    - Dead Letter Channels worden ingericht om mislukte berichten apart te verwerken zonder het hoofdproces te verstoren.
    - Idempotent receivers worden ingezet om dubbele berichten veilig te kunnen verwerken.
  - Niek wijst op het belang van strikte berichtvolgorde (First-In-First-Out) om synchronisatiefouten tussen instellingen te voorkomen.
  - Technische behoeften en issues worden vanaf nu centraal bijgehouden in GitHub om de backlog voor het projectmanagement inzichtelijk te maken.


### Uitdagingen in de Flexibilisering van het Onderwijs

- Scott deelt bevindingen uit een recente verkenning waaruit blijkt dat veel scholen nog vasthouden aan verouderde logistieke kaders, zoals rigide cycli van tien weken.
  - Onderwijsinstellingen ervaren een grote kloof tussen de papieren visie op flexibiliteit en de weerbarstige praktijk van de administratieve processen.
  - Directeuren sturen vaak primair op begrotingsbewaking en studiesucces, wat een remmende werking heeft op de noodzakelijke vernieuwing naar modulair onderwijs.
  - Er is sprake van paniek bij instellingen omdat huidige systemen, zoals OSIRIS, nog niet volledig zijn toegerust op de complexe registratievereisten van flexibele leerroutes.


### Leven Lang Ontwikkelen (LLO) en Regionale Ontwikkelpaden

- Het beleid verschuift van nationale kwalificatiedossiers naar regionale ontwikkelpaden die in co-creatie met het bedrijfsleven worden opgesteld.
  - Voor sectoren zoals de energietransitie (waterstof) worden modules georganiseerd op basis van actuele arbeidsmarktvraagstukken in plaats van standaardcurricula.
  - Scott meldt dat er voor 2027 een intensieve samenwerking met Defensie op de planning staat om personeelstekorten via flexibele leerroutes aan te pakken.
  - Er is geld beschikbaar voor de inrichting van LLO-structuren, waarbij regionale servicepunten en leer-werk-loketten een centrale rol spelen in de vraagarticulatie.
  - De bekostiging zal in de toekomst vaker plaatsvinden op moduleniveau in plaats van op basis van volledige meerjarige opleidingen.


### Operationele Planning en Volgende Stappen

- De komende periode staat in het teken van de voorbereiding op cruciale sessies met leveranciers en de werkgroep techniek.
  - Op maandag en woensdag 30 en 1 april (vóór 7 april 2026) vinden updates plaats met leveranciers om hen mee te nemen in de technische stand van zaken en de ArchiMate-modellen/way of working.
  - De OKx werkgroep komt op 7 april 2026 bijeen voor een diepe duik in de twintig geïdentificeerde koppelvlakken tussen systemen zoals de onderwijscatalogus en planningsmodules.
  - Scott gaat bij instellingen in Amsterdam en de regio Rijnland sessies organiseren om student journeys uit te werken die als basis dienen voor verdere systeemontwikkeling.
  - Algemene behoefte word uitgesproken door team inhoud OKx aan meer actieve ondersteuning van het bredere team (waaronder Werner, Rick en Rosalie) om de complexe materie tastbaar te maken via mockups en documentatie.
