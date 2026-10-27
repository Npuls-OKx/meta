# OKx-meta

De publieke kennisbank van **OKx**: de plek waar het keteninzicht en de koppelvlakrichting voor onderwijslogistiek ontstaan, in het open en samen met de sector. OKx is onderdeel van [Npuls, pijler Leren Zonder Drempels](https://npuls.nl/project-onderwijskoppelingen).

De releaseartefacten staan niet hier maar in [`Npuls-OKx/Public`](https://github.com/Npuls-OKx/Public): wat in deze kennisbank tot een releasebaar artefact rijpt, verhuist daarheen. Bestaat een document in beide repositories, dan is de versie in Public de vastgelegde en de versie hier de werkversie.

## Doel

Systemen in de onderwijsketen werken nu per instelling en per leverancier op eigen afspraken samen. Dat maakt elke verandering in het onderwijs duur: een school die een leerroute wil flexibiliseren, moet daarvoor langs elk systeem afzonderlijk. OKx legt daarom een gedeeld minimum aan afspraken vast, zodat instellingen en leveranciers tegen dezelfde koppelvlakken bouwen en de onderwijslogistiek de onderwijsvraag kan volgen in plaats van te begrenzen.

## Scope

| | |
|---|---|
| Onderwijssoort | Start bij het mbo, daarna het hoger onderwijs |
| Leerroutes | De reguliere leerroute eerst, met temporiseren en versnellen erna; de flexibele en modulaire routes volgen als verschil daarop |
| Bereik | Binnen een instelling eerst, federatie tussen instellingen gefaseerd |
| Buiten scope | De onderwijskundige keuze van een instelling. OKx legt de vorm van de uitwisseling vast, niet hoe een school haar onderwijs inricht |

De afbakening staat als architectuurbesluit vast in [ADR 0008](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md).

## Wat OKx oplevert

| Deliverable | Wat het is | Waar het staat |
|---|---|---|
| Koppelvlakspecificatie | De specificaties waarmee een partij een koppelvlak bouwt: per component de diensten, per koppeling het berichtgedrag, met de schema's erbij | [Public, Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) |
| Informatie- en gegevensmodellen | De taal van de keten: de begrippenfamilies, de objecttypen en hun samenhang, tot aan het technische gegevensmodel | [Public, Informatie-en-gegevensmodellen](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen) |
| Referentiemateriaal | De onderbouwing: principes, uitgangspunten, architectuurbesluiten en de kaderscenario's per leerroute | [Public, Referentiemateriaal](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal) |
| Kaderstelling en modellen | Het ArchiMate-model, de hoofdplaat informatiestromen, de interactieketens en de voorbeelduitwerkingen | deze repository |

De koppelvlakspecificatie is de hoofdoplevering: een set specificaties van koppelingen die als functioneel ontwerp dient voor een implementatie, bij voorkeur als [OEAPI-profiel](https://oeapi.eu/v6.0/#/technical/consumers-and-profiles/profiling-guidelines). Valt een eis buiten de profielvorm, dan komt een andere generieke standaard in beeld. Het uitgangspunt is OEAPI tenzij.

## Hoe het tot stand komt

De route van een vraag naar een vastgelegde afspraak volgt [AMIGO](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md): scenario-analyse, gegevens- en interactieanalyse, technologiekeuze, berichtspecificatie, interfacespecificatie. Daarbinnen gelden vier werkafspraken: ontwerpen en reviewen voor af, machine-interpreteerbaar vastleggen, beelden en tabellen boven lange tekst, en elk issue onder een milestone die naar de requirementsboom herleidt.

Drie lagen houden de uitwerking bij elkaar. Een **informatiestroom** is de conceptuele beweging van gegevens tussen twee componenten, zichtbaar op de hoofdplaat. Een **koppeling** is de gestandaardiseerde realisatie daarvan. Een **koppelvlak** is de verzameling koppelingen van precies een component. In die volgorde wordt er gewerkt, en een eis sneuvelt nooit omdat een technische standaard hem niet toestaat; zo'n verschil wordt een signalering richting die standaard.

Elk deliverable doorloopt de [product-flow](.agents/skills/okx-product-flow/SKILL.md): een story met een benoemde gebruiker en waarde, acceptatiecriteria in het issue, een plan met tegenlezing, uitwerking met onafhankelijke review, en een toets of de waarde geleverd is. Wijzigen gaat via een pull request; alleen het OKx-team merget.

## De stand per onderdeel

Deze tabel zegt per onderdeel hoe hard het is en welke wijziging in behandeling is. Wat er deze week gebeurt staat in de [milestones](https://github.com/Npuls-OKx/meta/milestones) en de [openstaande pull requests](https://github.com/Npuls-OKx/meta/pulls) van beide repositories; het [wijzigingenoverzicht](CHANGELOG.md) draagt de uitgebrachte versies.

| Onderdeel | Hoe hard | Wijziging in behandeling |
|---|---|---|
| Principes en uitgangspunten | Vastgelegd in Public, de aangehaalde besluiten dragen de status voorstel | [Public PR 71](https://github.com/Npuls-OKx/Public/pull/71): een principe dat eisen voor de techniekkeuze plaatst |
| Architectuurbesluiten | Vastgelegd in Public, alle met de status voorstel; de statusregel in het besluit zelf is leidend | [Public PR 71](https://github.com/Npuls-OKx/Public/pull/71) en [72](https://github.com/Npuls-OKx/Public/pull/72) |
| Requirementsboom | Vroeg concept. De huidige boom demonstreert de vorm van een uiteindelijke uitwerking en is geen weergave van de werkelijke breakdown; die ontstaat in de proefopstellingen die Niels van Duin uitvoert | Loopt buiten de boom om, in die proefopstellingen |
| Kaderscenario reguliere leerroute | Kaderstellend; de andere leerroutes volgen als verschil daarop | [meta PR 144](https://github.com/Npuls-OKx/meta/pull/144): de leerroute-uitwerking herstructureren |
| Informatiemodel | Laag 1 en 2 vastgelegd in Public, met de ontwerpkeuzes erbij | [Public PR 131](https://github.com/Npuls-OKx/Public/pull/131) brengt de modelronde van oktober; [meta PR 391](https://github.com/Npuls-OKx/meta/pull/391) en [410](https://github.com/Npuls-OKx/meta/pull/410) raken het kwalificatiekader en de resultaatkant |
| Hoofdplaat informatiestromen | Werkbeeld van het project; elke stroom erop is een kandidaat voor een koppelingspecificatie | [meta PR 412](https://github.com/Npuls-OKx/meta/pull/412) en [Public PR 133](https://github.com/Npuls-OKx/Public/pull/133) |
| Vorm van de oplevering | In de specificatiefase. De productopdeling, de verwachte vorm per product en de afhankelijkheden worden uitgewerkt | [meta #396](https://github.com/Npuls-OKx/meta/issues/396), [#342](https://github.com/Npuls-OKx/meta/issues/342), [#259](https://github.com/Npuls-OKx/meta/issues/259) en [PR 300](https://github.com/Npuls-OKx/meta/pull/300) |
| Koppelvlakspecificatie | Eerste pakket uitgebracht, en nu in herziening naar interactieketens die bij de waarde voor student en instelling beginnen | [meta PR 364](https://github.com/Npuls-OKx/meta/pull/364), [373](https://github.com/Npuls-OKx/meta/pull/373), [387](https://github.com/Npuls-OKx/meta/pull/387) en [377](https://github.com/Npuls-OKx/meta/pull/377); [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) legt een dienstlaag tussen component en endpoint |
| Voorbeelduitwerking reguliere leerroute | In uitwerking per fase, als toets van het model aan een echte casus | [meta PR 314](https://github.com/Npuls-OKx/meta/pull/314), [413](https://github.com/Npuls-OKx/meta/pull/413) en [414](https://github.com/Npuls-OKx/meta/pull/414) |
| Release en versionering | Elk pakket in Public draagt een eigen versielijn met een manifest | [Public PR 82](https://github.com/Npuls-OKx/Public/pull/82): de volgende momentopname |

## Waar te beginnen

| Wie binnenkomt | Begint bij | Tijd |
|---|---|---|
| Wie nieuw aanhaakt bij OKx | [De leesroute](doc/leesroute-okx.md): tien stappen door beide repositories, langs doel, scope, deliverables en totstandkoming | 2 uur |
| Wie wil bijdragen | [`CONTRIBUTING.md`](CONTRIBUTING.md) voor de werkwijze, [`doc/Bijdragen-voor-beginners.md`](doc/Bijdragen-voor-beginners.md) voor de eerste stappen | 20 min |
| Een AI-agent | [`AGENTS.md`](AGENTS.md): de harde regels, de product-flow en de skills | eerst dit |
| Wie wil bouwen tegen een koppelvlak | [Koppelvlakspecificaties in Public](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md), met de leesvolgorde daar | 1 uur |

## Wat staat waar

| Onderdeel | Locatie | Inhoud |
|---|---|---|
| Projectcontext | [`doc/`](doc/) en [`img/`](img/) | Overzichten, ketenplaten en contextdocumenten |
| Architectuur en model | [`architecture/`](architecture/) | Het ArchiMate-model, de hoofdplaat per versie, meetingverslagen |
| Specificaties | [`architecture/docs/specificatie/`](architecture/docs/specificatie/) | Begrippenlijst, leerroute-uitwerking, interactieketens, keuzevraagstukken |
| Agent-artifacten | [`architecture/agent-artifacts/`](architecture/agent-artifacts/) | Ontwerpen, plannen en onderzoek van agents |
| OKE en MOKA | [`OKE/`](OKE/), [`moka-koppelvlakspecificaties/`](moka-koppelvlakspecificaties/) | De eerste subdomein-uitwerking en de MOKA-templates |
| Presentaties | [`presentaties/`](presentaties/) | De decks per gremium, in de Npuls-huisstijl |
| Scripts | [`scripts/`](scripts/) | De generatoren en de controles op model, platen en documenten |
| Agent-omgeving | [`AGENTS.md`](AGENTS.md), [`.agents/`](.agents/), [`.cursor/`](.cursor/) | Basisdocument, skills met manifest, commands, rules en hooks |
| Dev-container | [`.devcontainer/`](.devcontainer/) | De reproduceerbare werkomgeving; installaties horen alleen hier |

## Verhouding met de standaarden en de referentiearchitecturen

Waar passend sluiten de uitwerkingen aan op de [Open Education API](https://openonderwijsapi.nl/v6.0/), als profiel bovenop de standaard en niet als afsplitsing ervan. De sectorarchitecturen blijven leidend: deze kennisbank wijzigt MORA niet, en een uitwerking die goed draagt kan later als onderbouwd voorstel richting de sectorprocessen gaan. De verhouding met ROSA en het Kernmodel Onderwijsinformatie ligt vast in de architectuurbesluiten.

## Meepraten

Vragen en open gesprekken gaan via [Discussions](https://github.com/Npuls-OKx/meta/discussions), achtergrond en langere uitleg staan in de [wiki](https://github.com/Npuls-OKx/meta/wiki), en concrete wijzigingen lopen via issues en pull requests.

## Privacy bij meetings

Sessies die deze kennisbank voeden kunnen opgenomen en met AI getranscribeerd worden; de facilitator kondigt dat vooraf aan. Bij bezwaar volgt anonimisering in het transcript of beëindiging van de deelname. Niet-publieke informatie hoort niet in deze repository. Volledige toelichting: [`doc/Privacy-meetings-en-transcriptie.md`](doc/Privacy-meetings-en-transcriptie.md).

Contact voor afstemming: niek.derksen@surf.nl.
