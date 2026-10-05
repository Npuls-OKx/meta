# De sectorketen en haar producten

Deze plaat toont de keten van kaderstelling tot implementatie, met per laag de partijen en de producten die zij maken. Zij beschrijft wat er is. Een oordeel over wat voor een bepaald doel ontbreekt laat zij aan de lezer, zodat dezelfde plaat een gatanalyse, een voortgangsanalyse en een aansluitvraag kan dragen.

Relateert aan: #262, #186.

## De view

![De sectorketen en haar producten](../img/OKx_sectorketen_v20261005.png)

De plaat in vectorvorm staat in [`img/OKx_sectorketen_v20261005.svg`](../img/OKx_sectorketen_v20261005.svg).

## Viewpointbeschrijving

| Onderdeel | Invulling |
|---|---|
| **Doel** | Zichtbaar maken welke partij welk product maakt in de keten die uitkomt bij een werkende koppeling, zodat een architect kan bepalen welke producten voor zijn eigen vraag bruikbaar zijn en waar zijn eigen werk landt. |
| **Concerns** | Welke producten zijn over te nemen en welke schrijven alleen een werkwijze voor. Op welk detailniveau staat een product, en is dat niveau toereikend voor een bouwbare specificatie. Welke partij maakt en beheert een product. Waar landt een OKx-product in de keten. |
| **Scope** | De keten rond onderwijslogistiek in het mbo, van overheidsbreed kader tot koppelingimplementatie, met het hoger onderwijs als nevenspoor via HOSA en HORA. Op de plaat staan de producten die in het afhankelijkheidspad van OKx liggen; de volledige lijst leeft in [`doc/sectorketen-producten.json`](sectorketen-producten.json). |
| **Gebruikte modeltaal** | Een gelaagde productenkaart, getekend als SVG uit een JSON-bron. De vulkleuren volgen het ArchiMate-kleurenschema zoals de overige OKx-platen dat hanteren. |
| **Relevante objecttypen en relaties** | Laag, partij, product, deelproduct en standaard. De relaties zijn levering van boven naar beneden, keuze vanuit de gereedschapsband, en terugkoppeling van beneden naar boven. |
| **Verantwoording** | De laagnamen en hun soort volgen [Relevante architecturen binnen het onderwijs](https://www.edustandaard.nl/rosa/onderwijsarchitecturen/) van Edustandaard en de plaat [`rosa-knooppunt.png`](../architecture/docs/specificatie/leerroute-uitwerking/img/rosa-knooppunt.png) die al in deze repository staat. De productlijsten komen uit de bronnen die per product in de JSON staan, met de peildatum erbij. |

## Legenda

De legenda staat in de plaat zelf, zodat het beeld ook buiten dit document leesbaar blijft.

| Kenmerk | Hoe het op de plaat staat |
|---|---|
| Detailniveau | De vulkleur: geel voor conceptueel, paars voor logisch, cyaan voor technisch, grijs waar een product geen model is |
| Aard | De rand: onderbroken voor een voorschrift, doorgetrokken voor een herbruikbaar product |
| Ouderdom | Rechtsonder in een blok het jaar van vaststelling of laatste wijziging, zoals de bron dat geeft |

## De ordening

Elke laag leunt op de uitkomst van de lagen erboven. Die lijn slaat op plaatsen over, en op twee plaatsen loopt zij terug. De plaat tekent die lijnen mee, links langs de ladder.

| Laag | Partijen | Soort |
|---|---|---|
| 1 Overheidsbreed | EIRA, NORA | referentiearchitectuur |
| 2 Programma en sectorvisie | OCW groeifonds, Npuls | visie en opdracht |
| 3 Onderwijsketen | ROSA, met AMIGO daarbinnen | ketenreferentiearchitectuur |
| 4 Sector | MOSA en HOSA naast MORA en HORA | doelarchitectuur naast referentiearchitectuur |
| 5 Koppelvlakontwerp | MOKA | ontwerpsjabloon |
| 6 Solutionarchitectuur | OKx | koppelvlakspecificatie |
| 7 Implementatie | leveranciers, instellingen | koppelingimplementatie |

Drie soorten architectuur staan apart, omdat zij een ander type product opleveren. ROSA is de ketenreferentiearchitectuur voor het hele onderwijs, gericht op uitwisseling tussen organisaties. MORA, HORA en FORA zijn sectorale referentiearchitecturen op het niveau van de bedrijfsvoering binnen een instelling. MOSA, HOSA en FOSA zijn de doelarchitecturen, met een agenda van te realiseren voorzieningen.

De lijnen langs de ladder:

| Lijn | Betekenis |
|---|---|
| Laag 3 naar laag 6 | AMIGO staat op laag 3 en bindt OKx rechtstreeks, via OKx-AP03 |
| Laag 3 en laag 4 | Uitwisseling in twee richtingen, zoals de stippellijn in `rosa-knooppunt.png` toont |
| Laag 6 naar laag 3 | Het OKx-informatiemodel en het begrippenkader landen bij ROSA |
| Laag 7 naar laag 6 | Een wijzigingsverzoek uit de implementatie komt terug bij de specificatie |

## Twee kenmerken dragen het beeld

**Aard.** Een `voorschrift` zegt hoe iets gedaan moet worden en draagt geen inhoud die een volgende laag overneemt; de AMIGO-methodiek is daarvan het voorbeeld. Een `herbruikbaar product` draagt inhoud die een volgende laag kan overnemen zonder die opnieuw te maken; het KOI met zijn 13 kernobjecten is daarvan het voorbeeld.

Waar beide waarden passen geldt een beslisregel: wat een volgende laag ervan overneemt is bepalend. De inhoud zelf maakt het een herbruikbaar product; de werkwijze die het voorschrijft maakt het een voorschrift. Het MOSA-principehuis valt daarmee aan de productkant, omdat OKx de principes zelf overneemt in zijn eigen architectuurprincipes.

**Detailniveau.** `conceptueel` staat voor begrippen, objecten en relaties zonder attributen; `logisch` voor objecten met attributen en de structuur van de uitwisseling; `technisch` voor syntax, endpoints en berichten. Een product dat geen model is draagt `niet van toepassing`.

Die twee kenmerken samen zeggen waar een product bruikbaar is. Het MORA-informatiemodel draagt ruim honderd informatieobjecten op conceptueel niveau, zonder attributen, en kan een bericht daarmee dragen op het niveau van de begrippen. De stap naar een bouwbare specificatie vraagt een logisch model eronder.

## De gereedschapsband

Standaarden staan naast de ladder. Een standaard is een keuze van de solutionlaag, gemaakt op grond van wat de oplossing vraagt. In AMIGO is dat stap 4, technologie- en paradigmakeuze met rationale erbij. De plaatsing van een standaard volgt een eigen as, het [Edustandaard Lagenmodel](https://rosa.wikixl.nl/index.php/Standaarden_geplot_op_het_Edustandaard_Lagenmodel) met vijf interoperabiliteitslagen; dat is hetzelfde vijflaagsmodel dat NORA hanteert, toegepast op het onderwijs.

De band kent twee soorten. **IT-fundamenten** zijn algemene techniek die buiten het onderwijs is ontstaan: OpenAPI, REST, GraphQL, JSON Schema, OAuth 2.0 met OpenID Connect, en TLS. **Domein- en sectorprofielen** liggen daarbovenop en zijn toegesneden op het onderwijs: OEAPI, Edukoppeling, ECK iD en OKE.

De voorkeursregel: het sectorprofiel gaat voor het fundament. Waar het profiel aantoonbaar tekortschiet volgt de terugval op het fundament, met de onderbouwing erbij. Het uitgangspunt [OEAPI, tenzij](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/uitgangspunten.md) is daarvan het voorbeeld.

Een plaatsing die aandacht verdient: OEAPI staat in het lagenmodel geplot op de informatielaag, als standaard voor uitwisseling tussen instellingen in het hoger onderwijs. OKx past hem toe in het mbo.

## De plaat opnieuw maken

De bron is [`doc/sectorketen-producten.json`](sectorketen-producten.json). Een actualisatie is een wijziging in dat bestand, waarna de plaat opnieuw wordt getekend en de keuring draait.

```bash
python3 scripts/teken-sectorketen.py --uit img/OKx_sectorketen_v20261005.svg
python3 scripts/keur-plaat.py img/OKx_sectorketen_v20261005.svg --max-kruisingen 1
npx svgexport img/OKx_sectorketen_v20261005.svg img/OKx_sectorketen_v20261005.png 1680:
```

De keuring meldt schuine segmenten, tekst buiten het doek, tekst onder de leesbaarheidsgrens en het aantal kruisende lijnen. Het aantal van vandaag staat vast met `--max-kruisingen 1`, zodat een latere wijziging het beeld niet stilletjes drukker maakt.

Elk product draagt twee datums, omdat zij verschillende dingen zeggen. De `bron_datum` is de vaststelling of de laatste wijziging zoals de bron die geeft. De `peildatum` is wanneer OKx keek. Het jaar op de plaat is de `bron_datum`.

## Besluit nodig op

**Besluit nodig op:** de borging van de producten die OKx oplevert, na afloop van OKx.
**Door:** architectuur board, in afstemming met MBO Digitaal en Bureau Edustandaard.
**Voor:** de architectuursync van 2 tot en met 6 november 2026.
**Opties:** het beheer beleggen bij de ketenreferentiearchitectuur ROSA, met de logische gegevensmodellen bij de Architectuurraad; of het beheer beleggen bij de sectorarchitectuur MORA; of per product kiezen, langs de bestemmingen die in de bron staan.

## Vervolg

Deze versie draagt de plaat en haar viewpoint. De volledige productcatalogus, het invulblad waarin een lezer zijn eigen oordeel per product kwijt kan, en de tabellen uit dezelfde bron volgen in een volgende iteratie onder #262.
