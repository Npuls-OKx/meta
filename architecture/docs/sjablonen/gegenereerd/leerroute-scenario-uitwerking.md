| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Versie | 0.0.1 |
| Uitgegeven door | OKx, pijler Leren Zonder Drempels (Npuls) |
| Ingevuld door | *naam en organisatie van de invuller* |
| Datum | *datum van invullen* |
| Inleveren | terug naar OKx SI als Word-bestand |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Inleiding

| Onderdeel | Inhoud |
|---|------------------------------------------------|
| Wat dit wordt | een leerroute scenario uitwerking: het scenario stap voor stap in het informatiemodel, zodat zichtbaar wordt of het model de werkelijkheid draagt |
| Wie dit invult | de adviesgroep. Suggestie: de informatiemanagers vullen de regels, de business analisten leggen ze naast het model |
| Voorbeeld | [de uitwerking van leerroute 1 met Jochem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md) |

Elk hoofdstuk opent met een blok dat zegt wat er van dat hoofdstuk wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het pakket van eisen bijdraagt. Dat blok blijft staan; het is de opdracht en niet de uitwerking. Een hoofdstuk dat niet van toepassing is houdt zijn kop, met de reden eronder.

## Van user story naar eis

Het pakket van eisen komt uit de gedeelde analyse van alles wat scholen hebben ingebracht, geinventariseerd in de PoC-sessies met de koploperscholen. De grootst gemene deler daaruit is wat OKx vastlegt.

Niet elk hoofdstuk levert hetzelfde. Een journey brengt een behoefte naar boven en levert user stories. Een procesbeschrijving zegt wat de instelling moet kunnen. Een gegevens- of systeemhoofdstuk zegt wat een component moet doen. Een interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok boven elk hoofdstuk noemt welke laag daar hoort.

| Laag | Waar die ontstaat | Voorbeeld |
|---|---|------------------------------------|
| User story | in een journey of een scenario | Als student wil ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten wanneer mijn eerste keuze vol is |
| Business requirement | in een procesbeschrijving | de instelling kent per keuzedeelruimte de voorkeursvolgorde van de student voordat zij plaatst |
| Functional requirement | in een gegevens- of systeemhoofdstuk | het studentkeuzesysteem legt per keuzedeelruimte een geordende lijst voorkeuren vast, met per voorkeur het onderdeel, de periode en de locatie |
| Technical requirement | in een interactiehoofdstuk | de voorkeurslijst gaat als geordende verzameling over het koppelvlak, met de volgorde expliciet in het bericht en niet afgeleid uit de positie |

Vul in dit document de laag in die boven het hoofdstuk staat. De lagen eronder volgen in een eigen ronde, met dit document als bron.

## De grootst gemene deler

Tussen de inbreng van instellingen en dit document zit een analysestap. Dat geldt hier sterker dan elders, omdat een voorbeeld overtuigt: een regel die uit een enkele instelling komt en hier als voorbeeld staat, leest als sectorpraktijk.

Een instelling spreekt voor haar eigen praktijk en niet voor de sector. Noteer daarom apart wat afwijkt, onder [Afwijkingen per instelling](#afwijkingen-per-instelling).

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

# Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 1: Kwalificatiekader analyseren en grofmazig ontwerpen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-1-kwalificatiekader-analyseren-en-grofmazig-ontwerpen)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 1 gemarkeerd](<img/leerroute-scenario-uitwerking/f1.png>)

*Schrijf hier de uitwerking.*

## F1-01 - Het kwalificatiedossier ontleed

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-01 - Het kwalificatiedossier ontleed](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-01---het-kwalificatiedossier-ontleed)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kwalificatiedossier analyseren](<img/leerroute-scenario-uitwerking/f1-01-het-kwalificatiedossier-ontleed.png>)

*Schrijf hier de uitwerking.*

## F1-02 - Examenplan, eerste resultaatstructuur en cohort

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-02 - Examenplan, eerste resultaatstructuur en cohort](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-02---examenplan-eerste-resultaatstructuur-en-cohort)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Examenplan opstellen](<img/leerroute-scenario-uitwerking/f1-02-examenplan-eerste-resultaatstructuur-en-cohort.png>)

*Schrijf hier de uitwerking.*

## F1-03 - Leeruitkomsten uit het dossier, in de stem van de instelling

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-03 - Leeruitkomsten uit het dossier, in de stem van de instelling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-03---leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten](<img/leerroute-scenario-uitwerking/f1-03-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.png>)

*Schrijf hier de uitwerking.*

## F1-04 - De leeruitkomst in CompetentNL-skills

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-04 - De leeruitkomst in CompetentNL-skills](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-04---de-leeruitkomst-in-competentnl-skills)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: leeruitkomst naar skills](<img/leerroute-scenario-uitwerking/f1-04-de-leeruitkomst-in-competentnl-skills.png>)

*Schrijf hier de uitwerking.*

## F1-05 - De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-05 - De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-05---de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: van kerntaak naar eenheid en leeronderdelen](<img/leerroute-scenario-uitwerking/f1-05-de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten.png>)

*Schrijf hier de uitwerking.*

## F1-06 - De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-06 - De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-06---de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kwalificatiedossier vertalen naar leeruitkomsten, verdieping: onderwijsontwerp met ruimte en middelen](<img/leerroute-scenario-uitwerking/f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen.png>)

*Schrijf hier de uitwerking.*

## F1-07 - De opleidingsspecificatie met programma, eenheden en keuzedeelruimte

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-07 - De opleidingsspecificatie met programma, eenheden en keuzedeelruimte](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-07---de-opleidingsspecificatie-met-programma-eenheden-en-keuzedeelruimte)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Opleidingsspecificatie met programma en eenheden beschrijven](<img/leerroute-scenario-uitwerking/f1-07-de-opleidingsspecificatie-met-programma-eenheden-en-keuzedeelruimte.png>)

*Schrijf hier de uitwerking.*

## F1-08 - Kiesbaar onderwijsprogrammaonderdeel: keuzedelen en minor

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-08 - Kiesbaar onderwijsprogrammaonderdeel: keuzedelen en minor](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-08---kiesbaar-onderwijsprogrammaonderdeel-keuzedelen-en-minor)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Keuzedeelprogramma als eigen specificatie vormgeven](<img/leerroute-scenario-uitwerking/f1-08-kiesbaar-onderwijsprogrammaonderdeel-keuzedelen-en-minor.png>)

*Schrijf hier de uitwerking.*

## F1-09 - Toetsonderdelen, wegingen en afrondingscriterium

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-09 - Toetsonderdelen, wegingen en afrondingscriterium](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-09---toetsonderdelen-wegingen-en-afrondingscriterium)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Toetsonderdelen en resultaatstructuur uit het examenplan afleiden](<img/leerroute-scenario-uitwerking/f1-09-toetsonderdelen-wegingen-en-afrondingscriterium.png>)

*Schrijf hier de uitwerking.*

## F1-10 - De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-10 - De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-10---de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Exameninstrumenten bepalen, inkopen of construeren, verdieping: examenvorm, instrument en beoordelaar](<img/leerroute-scenario-uitwerking/f1-10-de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte.png>)

*Schrijf hier de uitwerking.*

## F1-11 - Het examenplan vastgesteld

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-11 - Het examenplan vastgesteld](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-11---het-examenplan-vastgesteld)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Examenplan vaststellen](<img/leerroute-scenario-uitwerking/f1-11-het-examenplan-vastgesteld.png>)

*Schrijf hier de uitwerking.*

## F1-12 - De opleiding zoals ontworpen naar de catalogus

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-12 - De opleiding zoals ontworpen naar de catalogus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-12---de-opleiding-zoals-ontworpen-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus](<img/leerroute-scenario-uitwerking/f1-12-de-opleiding-zoals-ontworpen-naar-de-catalogus.png>)

*Schrijf hier de uitwerking.*

## F1-13 - Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)

**Voorbeeld** [Leerroute 1 scenario uitwerking, F1-13 - Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f1-13---het-onderwijs--en-examenontwerp-mee-naar-de-catalogus-conceptplaat)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Grofmazig resultaat publiceren naar de onderwijscatalogus](<img/leerroute-scenario-uitwerking/f1-13-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat.png>)

*Schrijf hier de uitwerking.*

# Fase 2: Publiceren en planbaar maken

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 2: Publiceren en planbaar maken](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-2-publiceren-en-planbaar-maken)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 2 gemarkeerd](<img/leerroute-scenario-uitwerking/f2.png>)

*Schrijf hier de uitwerking.*

## F2-01 - De specificatie planbaar gemaakt

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-01 - De specificatie planbaar gemaakt](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-01---de-specificatie-planbaar-gemaakt)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Specificatie aanvullen tot planbare specificatie](<img/leerroute-scenario-uitwerking/f2-01-de-specificatie-planbaar-gemaakt.png>)

*Schrijf hier de uitwerking.*

## F2-02 - Het verzoek om onderwijsaanbod

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-02 - Het verzoek om onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-02---het-verzoek-om-onderwijsaanbod)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Planningssysteem verzoeken om onderwijsaanbod](<img/leerroute-scenario-uitwerking/f2-02-het-verzoek-om-onderwijsaanbod.png>)

*Schrijf hier de uitwerking.*

## F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-03 - Verzoek met specificatiestructuur en planbare waarden naar planning](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-03---verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Planningssysteem verzoeken om onderwijsaanbod](<img/leerroute-scenario-uitwerking/f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.png>)

*Schrijf hier de uitwerking.*

## F2-04 - De specificatie op haalbaarheid getoetst

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-04 - De specificatie op haalbaarheid getoetst](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-04---de-specificatie-op-haalbaarheid-getoetst)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Specificatie op haalbaarheid toetsen](<img/leerroute-scenario-uitwerking/f2-04-de-specificatie-op-haalbaarheid-getoetst.png>)

*Schrijf hier de uitwerking.*

## F2-05 - De aanbodvraag naast de schaarste van ruimtes en mensen (conceptplaat)

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-05 - De aanbodvraag naast de schaarste van ruimtes en mensen (conceptplaat)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-05---de-aanbodvraag-naast-de-schaarste-van-ruimtes-en-mensen-conceptplaat)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Aanbodvraag per opleiding bepalen, verdieping: ruimtes en mensen op de specificatie](<img/leerroute-scenario-uitwerking/f2-05-de-aanbodvraag-naast-de-schaarste-van-ruimtes-en-mensen-conceptplaat.png>)

*Schrijf hier de uitwerking.*

## F2-06 - De jaarplanning op instellingsniveau (conceptplaat)

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-06 - De jaarplanning op instellingsniveau (conceptplaat)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-06---de-jaarplanning-op-instellingsniveau-conceptplaat)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Jaarplanning op instellingsniveau vaststellen, verdieping: jaarplanning op instellingsniveau](<img/leerroute-scenario-uitwerking/f2-06-de-jaarplanning-op-instellingsniveau-conceptplaat.png>)

*Schrijf hier de uitwerking.*

## F2-07 - Examenbehoefte uit de resultaatstructuur (conceptplaat)

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-07 - Examenbehoefte uit de resultaatstructuur (conceptplaat)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-07---examenbehoefte-uit-de-resultaatstructuur-conceptplaat)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Jaarplanning op instellingsniveau vaststellen, verdieping: examenplanning uit de resultaatstructuur](<img/leerroute-scenario-uitwerking/f2-07-examenbehoefte-uit-de-resultaatstructuur-conceptplaat.png>)

*Schrijf hier de uitwerking.*

## F2-08 - Het aanbod gepland: opleiding, programma, eenheid, gelegenheid

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-08 - Het aanbod gepland: opleiding, programma, eenheid, gelegenheid](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-08---het-aanbod-gepland-opleiding-programma-eenheid-gelegenheid)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Aanbod plannen](<img/leerroute-scenario-uitwerking/f2-08-het-aanbod-gepland-opleiding-programma-eenheid-gelegenheid.png>)

*Schrijf hier de uitwerking.*

## F2-09 - Het geplande aanbod terug naar de catalogus

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-09 - Het geplande aanbod terug naar de catalogus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-09---het-geplande-aanbod-terug-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Gepland aanbod terugleveren aan de onderwijscatalogus](<img/leerroute-scenario-uitwerking/f2-09-het-geplande-aanbod-terug-naar-de-catalogus.png>)

*Schrijf hier de uitwerking.*

## Variant capaciteitsgestuurd

**Voorbeeld** [Leerroute 1 scenario uitwerking, Variant capaciteitsgestuurd](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#variant-capaciteitsgestuurd)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

### F2-C01 - Keuzedeel K0037 vooraf gepland op capaciteit

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-C01 - Keuzedeel K0037 vooraf gepland op capaciteit](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-c01---keuzedeel-k0037-vooraf-gepland-op-capaciteit)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Keuzedeelaanbod plannen op inzetbare capaciteit en prognose](<img/leerroute-scenario-uitwerking/f2-c01-keuzedeel-k0037-vooraf-gepland-op-capaciteit.png>)

*Schrijf hier de uitwerking.*

### F2-C02 - Geplande keuzedeelgroepen naar de catalogus

**Voorbeeld** [Leerroute 1 scenario uitwerking, F2-C02 - Geplande keuzedeelgroepen naar de catalogus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f2-c02---geplande-keuzedeelgroepen-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Gepland keuzedeelaanbod terugleveren aan de onderwijscatalogus](<img/leerroute-scenario-uitwerking/f2-c02-geplande-keuzedeelgroepen-naar-de-catalogus.png>)

*Schrijf hier de uitwerking.*

# Fase 3: Instroom, intake en plaatsing

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 3: Instroom, intake en plaatsing](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-3-instroom-intake-en-plaatsing)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 3 gemarkeerd](<img/leerroute-scenario-uitwerking/f3.png>)

*Schrijf hier de uitwerking.*

## F3-01 - Aanmeldbaar aanbod naar de kernregistratie

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-01 - Aanmeldbaar aanbod naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-01---aanmeldbaar-aanbod-naar-de-kernregistratie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Orienteren op het gepubliceerde aanbod](<img/leerroute-scenario-uitwerking/f3-01-aanmeldbaar-aanbod-naar-de-kernregistratie.png>)

*Schrijf hier de uitwerking.*

## F3-02 - Aanmeldbaar aanbod van de kernregistratie naar AII

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-02 - Aanmeldbaar aanbod van de kernregistratie naar AII](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-02---aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Orienteren op het gepubliceerde aanbod](<img/leerroute-scenario-uitwerking/f3-02-aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii.png>)

*Schrijf hier de uitwerking.*

## F3-03 - <student> meldt zich aan: aanmelding en verbintenissen

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-03 - <student> meldt zich aan: aanmelding en verbintenissen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-03---jochem-meldt-zich-aan-aanmelding-en-verbintenissen)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Aanmelden via het intakesysteem](<img/leerroute-scenario-uitwerking/f3-03-jochem-meldt-zich-aan-aanmelding-en-verbintenissen.png>)

*Schrijf hier de uitwerking.*

## F3-04 - De aanmelding van de voorziening naar het intakesysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-04 - De aanmelding van de voorziening naar het intakesysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-04---de-aanmelding-van-de-voorziening-naar-het-intakesysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Aanmelden via het intakesysteem](<img/leerroute-scenario-uitwerking/f3-04-de-aanmelding-van-de-voorziening-naar-het-intakesysteem.png>)

*Schrijf hier de uitwerking.*

## F3-05 - Intake: student en plaatsingsgroep

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-05 - Intake: student en plaatsingsgroep](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-05---intake-student-en-plaatsingsgroep)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Intake doorlopen en plaatsen](<img/leerroute-scenario-uitwerking/f3-05-intake-student-en-plaatsingsgroep.png>)

*Schrijf hier de uitwerking.*

## F3-06 - Inschrijving: van aangemeld naar ingeschreven

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-06 - Inschrijving: van aangemeld naar ingeschreven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-06---inschrijving-van-aangemeld-naar-ingeschreven)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Persoon en verbintenissen vastleggen in de kernregistratie](<img/leerroute-scenario-uitwerking/f3-06-inschrijving-van-aangemeld-naar-ingeschreven.png>)

*Schrijf hier de uitwerking.*

## F3-07 - Inschrijving en verbintenissen naar de kernregistratie

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-07 - Inschrijving en verbintenissen naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-07---inschrijving-en-verbintenissen-naar-de-kernregistratie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Persoon en verbintenissen vastleggen in de kernregistratie](<img/leerroute-scenario-uitwerking/f3-07-inschrijving-en-verbintenissen-naar-de-kernregistratie.png>)

*Schrijf hier de uitwerking.*

## F3-08 - Student, verbintenis, groep en behaalde leeruitkomsten naar het studentkeuzesysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F3-08 - Student, verbintenis, groep en behaalde leeruitkomsten naar het studentkeuzesysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f3-08---student-verbintenis-groep-en-behaalde-leeruitkomsten-naar-het-studentkeuzesysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Persoon en verbintenissen vastleggen in de kernregistratie](<img/leerroute-scenario-uitwerking/f3-08-student-verbintenis-groep-en-behaalde-leeruitkomsten-naar-het-studentkeuzesysteem.png>)

*Schrijf hier de uitwerking.*

# Fase 4: Detailleren, roosteren en inschrijven

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 4: Detailleren, roosteren en inschrijven](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-4-detailleren-roosteren-en-inschrijven)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 4 gemarkeerd](<img/leerroute-scenario-uitwerking/f4.png>)

*Schrijf hier de uitwerking.*

## F4-01 - Het leeronderdeel fijnmazig: lessenreeks en les

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-01 - Het leeronderdeel fijnmazig: lessenreeks en les](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-01---het-leeronderdeel-fijnmazig-lessenreeks-en-les)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Leeronderdeel- en toetsonderdeelspecificaties fijnmazig uitwerken](<img/leerroute-scenario-uitwerking/f4-01-het-leeronderdeel-fijnmazig-lessenreeks-en-les.png>)

*Schrijf hier de uitwerking.*

## F4-02 - Detailspecificaties naar het LMS

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-02 - Detailspecificaties naar het LMS](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-02---detailspecificaties-naar-het-lms)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Detailspecificaties leveren aan het LMS](<img/leerroute-scenario-uitwerking/f4-02-detailspecificaties-naar-het-lms.png>)

*Schrijf hier de uitwerking.*

## F4-03 - De les en de toets van binnen, elk met hun eigen onderdelen (conceptplaat)

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-03 - De les en de toets van binnen, elk met hun eigen onderdelen (conceptplaat)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-03---de-les-en-de-toets-van-binnen-elk-met-hun-eigen-onderdelen-conceptplaat)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Detailspecificaties leveren aan het LMS](<img/leerroute-scenario-uitwerking/f4-03-de-les-en-de-toets-van-binnen-elk-met-hun-eigen-onderdelen-conceptplaat.png>)

*Schrijf hier de uitwerking.*

## F4-04 - Summatieve resultaatstructuur naar het studentvolgsysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-04 - Summatieve resultaatstructuur naar het studentvolgsysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-04---summatieve-resultaatstructuur-naar-het-studentvolgsysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Detailspecificaties leveren aan het LMS](<img/leerroute-scenario-uitwerking/f4-04-summatieve-resultaatstructuur-naar-het-studentvolgsysteem.png>)

*Schrijf hier de uitwerking.*

## F4-05 - Summatieve resultaatstructuur naar de kernregistratie

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-05 - Summatieve resultaatstructuur naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-05---summatieve-resultaatstructuur-naar-de-kernregistratie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Detailspecificaties leveren aan het LMS](<img/leerroute-scenario-uitwerking/f4-05-summatieve-resultaatstructuur-naar-de-kernregistratie.png>)

*Schrijf hier de uitwerking.*

## F4-06 - Plaatsingsgroepen naar planning

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-06 - Plaatsingsgroepen naar planning](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-06---plaatsingsgroepen-naar-planning)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Plaatsings- en planninggroepen definieren en aan personen koppelen](<img/leerroute-scenario-uitwerking/f4-06-plaatsingsgroepen-naar-planning.png>)

*Schrijf hier de uitwerking.*

## F4-07 - Te roosteren leergelegenheden naar het roostersysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-07 - Te roosteren leergelegenheden naar het roostersysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-07---te-roosteren-leergelegenheden-naar-het-roostersysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Te roosteren specificaties aan het roostersysteem geven](<img/leerroute-scenario-uitwerking/f4-07-te-roosteren-leergelegenheden-naar-het-roostersysteem.png>)

*Schrijf hier de uitwerking.*

## F4-08 - Roosteren: lesgelegenheid, lokaal en docent

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-08 - Roosteren: lesgelegenheid, lokaal en docent](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-08---roosteren-lesgelegenheid-lokaal-en-docent)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Leer-, les- en toetsgelegenheden roosteren](<img/leerroute-scenario-uitwerking/f4-08-roosteren-lesgelegenheid-lokaal-en-docent.png>)

*Schrijf hier de uitwerking.*

## F4-09 - <student>s verbintenissen op de geroosterde gelegenheden

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-09 - <student>s verbintenissen op de geroosterde gelegenheden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-09---jochems-verbintenissen-op-de-geroosterde-gelegenheden)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Verwachte deelnemers delen en toegang geven](<img/leerroute-scenario-uitwerking/f4-09-jochems-verbintenissen-op-de-geroosterde-gelegenheden.png>)

*Schrijf hier de uitwerking.*

## F4-10 - Student, verbintenissen en groep naar het LMS

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-10 - Student, verbintenissen en groep naar het LMS](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-10---student-verbintenissen-en-groep-naar-het-lms)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Verwachte deelnemers delen en toegang geven](<img/leerroute-scenario-uitwerking/f4-10-student-verbintenissen-en-groep-naar-het-lms.png>)

*Schrijf hier de uitwerking.*

## F4-11 - Verbintenissen op alle niveaus naar het studentvolgsysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-11 - Verbintenissen op alle niveaus naar het studentvolgsysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-11---verbintenissen-op-alle-niveaus-naar-het-studentvolgsysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Verwachte deelnemers delen en toegang geven](<img/leerroute-scenario-uitwerking/f4-11-verbintenissen-op-alle-niveaus-naar-het-studentvolgsysteem.png>)

*Schrijf hier de uitwerking.*

## Variant capaciteitsgestuurd

**Voorbeeld** [Leerroute 1 scenario uitwerking, Variant capaciteitsgestuurd](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#variant-capaciteitsgestuurd)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

### F4-C01 - Na de toewijzing: de keuzedeelgroep met vaste capaciteit naar het roostersysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F4-C01 - Na de toewijzing: de keuzedeelgroep met vaste capaciteit naar het roostersysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f4-c01---na-de-toewijzing-de-keuzedeelgroep-met-vaste-capaciteit-naar-het-roostersysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Keuzedeelgroep met vaste capaciteit aan het roostersysteem geven](<img/leerroute-scenario-uitwerking/f4-c01-na-de-toewijzing-de-keuzedeelgroep-met-vaste-capaciteit-naar-het-roostersysteem.png>)

*Schrijf hier de uitwerking.*

# Fase 5: Onderwijs uitvoeren en voortgang begeleiden

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 5: Onderwijs uitvoeren en voortgang begeleiden](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-5-onderwijs-uitvoeren-en-voortgang-begeleiden)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 5 gemarkeerd](<img/leerroute-scenario-uitwerking/f5.png>)

*Schrijf hier de uitwerking.*

## F5-01 - Les gevolgd: aanwezigheid en lesresultaat

**Voorbeeld** [Leerroute 1 scenario uitwerking, F5-01 - Les gevolgd: aanwezigheid en lesresultaat](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f5-01---les-gevolgd-aanwezigheid-en-lesresultaat)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Onderwijs verzorgen](<img/leerroute-scenario-uitwerking/f5-01-les-gevolgd-aanwezigheid-en-lesresultaat.png>)

*Schrijf hier de uitwerking.*

## F5-02 - De verbintenis op de toetsgelegenheid: geplaatst of zelf gekozen

**Voorbeeld** [Leerroute 1 scenario uitwerking, F5-02 - De verbintenis op de toetsgelegenheid: geplaatst of zelf gekozen](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f5-02---de-verbintenis-op-de-toetsgelegenheid-geplaatst-of-zelf-gekozen)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Toetsmomenten plannen tijdens lessen](<img/leerroute-scenario-uitwerking/f5-02-de-verbintenis-op-de-toetsgelegenheid-geplaatst-of-zelf-gekozen.png>)

*Schrijf hier de uitwerking.*

## F5-03 - Formatieve voortgang: structuur, resultaten en beoordeling

**Voorbeeld** [Leerroute 1 scenario uitwerking, F5-03 - Formatieve voortgang: structuur, resultaten en beoordeling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f5-03---formatieve-voortgang-structuur-resultaten-en-beoordeling)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Formatieve voortgang bijhouden](<img/leerroute-scenario-uitwerking/f5-03-formatieve-voortgang-structuur-resultaten-en-beoordeling.png>)

*Schrijf hier de uitwerking.*

## F5-04 - Formatieve resultaten van het LMS naar het studentvolgsysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F5-04 - Formatieve resultaten van het LMS naar het studentvolgsysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f5-04---formatieve-resultaten-van-het-lms-naar-het-studentvolgsysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Formatieve voortgang bijhouden](<img/leerroute-scenario-uitwerking/f5-04-formatieve-resultaten-van-het-lms-naar-het-studentvolgsysteem.png>)

*Schrijf hier de uitwerking.*

## F5-05 - Studiebeeld: de nominale route naast wat <student> heeft behaald

**Voorbeeld** [Leerroute 1 scenario uitwerking, F5-05 - Studiebeeld: de nominale route naast wat <student> heeft behaald](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f5-05---studiebeeld-de-nominale-route-naast-wat-jochem-heeft-behaald)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Studiebeeld volgen in het studentvolgsysteem](<img/leerroute-scenario-uitwerking/f5-05-studiebeeld-de-nominale-route-naast-wat-jochem-heeft-behaald.png>)

*Schrijf hier de uitwerking.*

# Fase 6: Organiseren van keuzemomenten

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 6: Organiseren van keuzemomenten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-6-organiseren-van-keuzemomenten)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 6 gemarkeerd](<img/leerroute-scenario-uitwerking/f6.png>)

*Schrijf hier de uitwerking.*

## F6-01 - Keuzedeelaanbod ontsloten

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-01 - Keuzedeelaanbod ontsloten](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-01---keuzedeelaanbod-ontsloten)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem](<img/leerroute-scenario-uitwerking/f6-01-keuzedeelaanbod-ontsloten.png>)

*Schrijf hier de uitwerking.*

## F6-02 - Keuzedeelaanbod, specificatie en regels naar het studentkeuzesysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-02 - Keuzedeelaanbod, specificatie en regels naar het studentkeuzesysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-02---keuzedeelaanbod-specificatie-en-regels-naar-het-studentkeuzesysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Keuzedeelaanbod ontsluiten naar het studentkeuzesysteem](<img/leerroute-scenario-uitwerking/f6-02-keuzedeelaanbod-specificatie-en-regels-naar-het-studentkeuzesysteem.png>)

*Schrijf hier de uitwerking.*

## F6-03 - <student>s aanmelding op het keuzedeelaanbod, met zijn voorkeurslijst

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-03 - <student>s aanmelding op het keuzedeelaanbod, met zijn voorkeurslijst](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-03---jochems-aanmelding-op-het-keuzedeelaanbod-met-zijn-voorkeurslijst)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Voorkeurslijst samenstellen in het studentkeuzesysteem](<img/leerroute-scenario-uitwerking/f6-03-jochems-aanmelding-op-het-keuzedeelaanbod-met-zijn-voorkeurslijst.png>)

*Schrijf hier de uitwerking.*

## F6-04 - Keuzestelling naar planning

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-04 - Keuzestelling naar planning](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-04---keuzestelling-naar-planning)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Voorkeurslijst samenstellen in het studentkeuzesysteem](<img/leerroute-scenario-uitwerking/f6-04-keuzestelling-naar-planning.png>)

*Schrijf hier de uitwerking.*

## F6-05 - Definitieve keuzes verwerkt naar groepen en capaciteit

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-05 - Definitieve keuzes verwerkt naar groepen en capaciteit](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-05---definitieve-keuzes-verwerkt-naar-groepen-en-capaciteit)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Definitieve keuzes verwerken naar groepen en capaciteit](<img/leerroute-scenario-uitwerking/f6-05-definitieve-keuzes-verwerkt-naar-groepen-en-capaciteit.png>)

*Schrijf hier de uitwerking.*

## F6-06 - Geactualiseerd keuzedeelaanbod terug naar de catalogus

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-06 - Geactualiseerd keuzedeelaanbod terug naar de catalogus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-06---geactualiseerd-keuzedeelaanbod-terug-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Planbaar aanbod actualiseren](<img/leerroute-scenario-uitwerking/f6-06-geactualiseerd-keuzedeelaanbod-terug-naar-de-catalogus.png>)

*Schrijf hier de uitwerking.*

## F6-07 - De aanmelding wordt een inschrijving op het keuzedeel

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-07 - De aanmelding wordt een inschrijving op het keuzedeel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-07---de-aanmelding-wordt-een-inschrijving-op-het-keuzedeel)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Keuzedeel formeel inschrijven](<img/leerroute-scenario-uitwerking/f6-07-de-aanmelding-wordt-een-inschrijving-op-het-keuzedeel.png>)

*Schrijf hier de uitwerking.*

## F6-08 - Keuzedeelverbintenis naar de kernregistratie

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-08 - Keuzedeelverbintenis naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-08---keuzedeelverbintenis-naar-de-kernregistratie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Keuzedeel formeel inschrijven](<img/leerroute-scenario-uitwerking/f6-08-keuzedeelverbintenis-naar-de-kernregistratie.png>)

*Schrijf hier de uitwerking.*

## Variant capaciteitsgestuurd

**Voorbeeld** [Leerroute 1 scenario uitwerking, Variant capaciteitsgestuurd](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#variant-capaciteitsgestuurd)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

### F6-C01 - Capaciteit vastgesteld na de animo

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-C01 - Capaciteit vastgesteld na de animo](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-c01---capaciteit-vastgesteld-na-de-animo)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Capaciteit vaststellen na de animo](<img/leerroute-scenario-uitwerking/f6-c01-capaciteit-vastgesteld-na-de-animo.png>)

*Schrijf hier de uitwerking.*

### F6-C02 - Geplande leergelegenheid naar het studentkeuzesysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-C02 - Geplande leergelegenheid naar het studentkeuzesysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-c02---geplande-leergelegenheid-naar-het-studentkeuzesysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Geplande leergelegenheden ontsluiten naar het studentkeuzesysteem](<img/leerroute-scenario-uitwerking/f6-c02-geplande-leergelegenheid-naar-het-studentkeuzesysteem.png>)

*Schrijf hier de uitwerking.*

### F6-C03 - <student> kiest een plek op de geplande leergelegenheid

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-C03 - <student> kiest een plek op de geplande leergelegenheid](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-c03---jochem-kiest-een-plek-op-de-geplande-leergelegenheid)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Plek kiezen op een geplande leergelegenheid](<img/leerroute-scenario-uitwerking/f6-c03-jochem-kiest-een-plek-op-de-geplande-leergelegenheid.png>)

*Schrijf hier de uitwerking.*

### F6-C04 - Toegewezen binnen de capaciteit: inschrijving op het keuzedeel

**Voorbeeld** [Leerroute 1 scenario uitwerking, F6-C04 - Toegewezen binnen de capaciteit: inschrijving op het keuzedeel](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f6-c04---toegewezen-binnen-de-capaciteit-inschrijving-op-het-keuzedeel)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Toewijzen binnen de capaciteit](<img/leerroute-scenario-uitwerking/f6-c04-toegewezen-binnen-de-capaciteit-inschrijving-op-het-keuzedeel.png>)

*Schrijf hier de uitwerking.*

# Fase 7: Bijsturen planning en aanbod

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 7: Bijsturen planning en aanbod](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-7-bijsturen-planning-en-aanbod)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 7 gemarkeerd](<img/leerroute-scenario-uitwerking/f7.png>)

*Schrijf hier de uitwerking.*

## F7-01 - Afwijkingen verzameld in een plaatsingsgroep

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-01 - Afwijkingen verzameld in een plaatsingsgroep](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-01---afwijkingen-verzameld-in-een-plaatsingsgroep)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Afwijkingen verzamelen in een planninggroep](<img/leerroute-scenario-uitwerking/f7-01-afwijkingen-verzameld-in-een-plaatsingsgroep.png>)

*Schrijf hier de uitwerking.*

## F7-02 - Onderwijseenheid-aanbodverbintenis geannuleerd

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-02 - Onderwijseenheid-aanbodverbintenis geannuleerd](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-02---onderwijseenheid-aanbodverbintenis-geannuleerd)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Bestaande verbintenissen annuleren](<img/leerroute-scenario-uitwerking/f7-02-onderwijseenheid-aanbodverbintenis-geannuleerd.png>)

*Schrijf hier de uitwerking.*

## F7-03 - Plaatsingsgroep van de kernregistratie naar planning

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-03 - Plaatsingsgroep van de kernregistratie naar planning](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-03---plaatsingsgroep-van-de-kernregistratie-naar-planning)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Bestaande verbintenissen annuleren](<img/leerroute-scenario-uitwerking/f7-03-plaatsingsgroep-van-de-kernregistratie-naar-planning.png>)

*Schrijf hier de uitwerking.*

## F7-04 - Nieuw aanbod voor de plaatsingsgroep

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-04 - Nieuw aanbod voor de plaatsingsgroep](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-04---nieuw-aanbod-voor-de-plaatsingsgroep)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Nieuw aanbod maken en publiceren](<img/leerroute-scenario-uitwerking/f7-04-nieuw-aanbod-voor-de-plaatsingsgroep.png>)

*Schrijf hier de uitwerking.*

## F7-05 - Bijgestuurd aanbod naar de catalogus

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-05 - Bijgestuurd aanbod naar de catalogus](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-05---bijgestuurd-aanbod-naar-de-catalogus)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Nieuw aanbod maken en publiceren](<img/leerroute-scenario-uitwerking/f7-05-bijgestuurd-aanbod-naar-de-catalogus.png>)

*Schrijf hier de uitwerking.*

## F7-06 - Nieuwe leergelegenheden naar het roostersysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-06 - Nieuwe leergelegenheden naar het roostersysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-06---nieuwe-leergelegenheden-naar-het-roostersysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Nieuw aanbod maken en publiceren](<img/leerroute-scenario-uitwerking/f7-06-nieuwe-leergelegenheden-naar-het-roostersysteem.png>)

*Schrijf hier de uitwerking.*

## Variant capaciteitsgestuurd

**Voorbeeld** [Leerroute 1 scenario uitwerking, Variant capaciteitsgestuurd](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#variant-capaciteitsgestuurd)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

### F7-C01 - Een plek komt vrij binnen de capaciteit

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-C01 - Een plek komt vrij binnen de capaciteit](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-c01---een-plek-komt-vrij-binnen-de-capaciteit)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Vrijgekomen plek binnen de capaciteit verwerken](<img/leerroute-scenario-uitwerking/f7-c01-een-plek-komt-vrij-binnen-de-capaciteit.png>)

*Schrijf hier de uitwerking.*

### F7-C02 - De vrije plek terug naar het studentkeuzesysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F7-C02 - De vrije plek terug naar het studentkeuzesysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f7-c02---de-vrije-plek-terug-naar-het-studentkeuzesysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Vrije plek ontsluiten naar het studentkeuzesysteem](<img/leerroute-scenario-uitwerking/f7-c02-de-vrije-plek-terug-naar-het-studentkeuzesysteem.png>)

*Schrijf hier de uitwerking.*

# Fase 8: Examineren, vaststellen en diplomeren

**Voorbeeld** [Leerroute 1 scenario uitwerking, Fase 8: Examineren, vaststellen en diplomeren](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#fase-8-examineren-vaststellen-en-diplomeren)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![De hoofdplaat met de stromen van fase 8 gemarkeerd](<img/leerroute-scenario-uitwerking/f8.png>)

*Schrijf hier de uitwerking.*

## F8-01 - Examengelegenheid uit de examenspecificatie

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-01 - Examengelegenheid uit de examenspecificatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-01---examengelegenheid-uit-de-examenspecificatie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Examenspecificaties omzetten in examengelegenheden](<img/leerroute-scenario-uitwerking/f8-01-examengelegenheid-uit-de-examenspecificatie.png>)

*Schrijf hier de uitwerking.*

## F8-02 - Kandidatenlijst: verbintenis op de examengelegenheid

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-02 - Kandidatenlijst: verbintenis op de examengelegenheid](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-02---kandidatenlijst-verbintenis-op-de-examengelegenheid)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kandidatenlijsten samenstellen](<img/leerroute-scenario-uitwerking/f8-02-kandidatenlijst-verbintenis-op-de-examengelegenheid.png>)

*Schrijf hier de uitwerking.*

## F8-03 - Afname en beoordeling: de proeve individueel, een centraal examen in een zitting

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-03 - Afname en beoordeling: de proeve individueel, een centraal examen in een zitting](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-03---afname-en-beoordeling-de-proeve-individueel-een-centraal-examen-in-een-zitting)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Zitting uitvoeren en resultaten doorgeven](<img/leerroute-scenario-uitwerking/f8-03-afname-en-beoordeling-de-proeve-individueel-een-centraal-examen-in-een-zitting.png>)

*Schrijf hier de uitwerking.*

## F8-04 - Examenresultaat naar het studentvolgsysteem

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-04 - Examenresultaat naar het studentvolgsysteem](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-04---examenresultaat-naar-het-studentvolgsysteem)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Zitting uitvoeren en resultaten doorgeven](<img/leerroute-scenario-uitwerking/f8-04-examenresultaat-naar-het-studentvolgsysteem.png>)

*Schrijf hier de uitwerking.*

## F8-05 - Summatief vastgesteld: resultaten en beoordeling

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-05 - Summatief vastgesteld: resultaten en beoordeling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-05---summatief-vastgesteld-resultaten-en-beoordeling)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Summatief vaststellen](<img/leerroute-scenario-uitwerking/f8-05-summatief-vastgesteld-resultaten-en-beoordeling.png>)

*Schrijf hier de uitwerking.*

## F8-06 - Vaststelling naar de kernregistratie

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-06 - Vaststelling naar de kernregistratie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-06---vaststelling-naar-de-kernregistratie)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![stroomt: Summatief vaststellen](<img/leerroute-scenario-uitwerking/f8-06-vaststelling-naar-de-kernregistratie.png>)

*Schrijf hier de uitwerking.*

## F8-07 - Gediplomeerd: opleidingsresultaat en diploma

**Voorbeeld** [Leerroute 1 scenario uitwerking, F8-07 - Gediplomeerd: opleidingsresultaat en diploma](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#f8-07---gediplomeerd-opleidingsresultaat-en-diploma)

**Acceptatiecriteria** een beeld, en het beeld staat in het document zelf, met een regel eronder die zegt waar de lezer naar moet kijken

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

![ontstaat: Kwalificering en diplomering registreren](<img/leerroute-scenario-uitwerking/f8-07-gediplomeerd-opleidingsresultaat-en-diploma.png>)

*Schrijf hier de uitwerking.*

# Bijlage: alle objecttypen per begrippenfamilie

**Voorbeeld** [Leerroute 1 scenario uitwerking, Bijlage: alle objecttypen per begrippenfamilie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#bijlage-alle-objecttypen-per-begrippenfamilie)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Kwalificatiekader

**Voorbeeld** [Leerroute 1 scenario uitwerking, Kwalificatiekader](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#kwalificatiekader)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Onderwijskundig kader instelling

**Voorbeeld** [Leerroute 1 scenario uitwerking, Onderwijskundig kader instelling](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#onderwijskundig-kader-instelling)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Onderwijsspecificatie

**Voorbeeld** [Leerroute 1 scenario uitwerking, Onderwijsspecificatie](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#onderwijsspecificatie)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Onderwijsaanbod

**Voorbeeld** [Leerroute 1 scenario uitwerking, Onderwijsaanbod](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#onderwijsaanbod)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Onderwijsverbintenis

**Voorbeeld** [Leerroute 1 scenario uitwerking, Onderwijsverbintenis](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#onderwijsverbintenis)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Onderwijsresultaat

**Voorbeeld** [Leerroute 1 scenario uitwerking, Onderwijsresultaat](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#onderwijsresultaat)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Resultaatstructuur

**Voorbeeld** [Leerroute 1 scenario uitwerking, Resultaatstructuur](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#resultaatstructuur)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

## Buiten de kolommen (persoon, groep, cohort, verzoek)

**Voorbeeld** [Leerroute 1 scenario uitwerking, Buiten de kolommen (persoon, groep, cohort, verzoek)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#buiten-de-kolommen-persoon-groep-cohort-verzoek)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Objecttype | Beeld | <student> | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Schrijf hier de uitwerking.*

# Vragen aan de kerngroep

**Voorbeeld** [Leerroute 1 scenario uitwerking, Vragen aan de kerngroep](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#vragen-aan-de-kerngroep)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Vragen, vervolg (2 van 3)

**Voorbeeld** [Leerroute 1 scenario uitwerking, Vragen, vervolg (2 van 3)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#vragen-vervolg-2-van-3)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

## Vragen, vervolg (3 van 3)

**Voorbeeld** [Leerroute 1 scenario uitwerking, Vragen, vervolg (3 van 3)](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#vragen-vervolg-3-van-3)

**Acceptatiecriteria** een beschrijving in lopende tekst, en de tekst noemt wie handelt, met welk systeem, en welke informatie van waar naar waar beweegt

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

*Schrijf hier de uitwerking.*

# Regelregister

**Voorbeeld** [Leerroute 1 scenario uitwerking, Regelregister](https://github.com/Npuls-OKx/meta/blob/dev/architecture/model/informatiemodel/leerroute-uitwerking-model-lr1-jochem.md#regelregister)

**Acceptatiecriteria** een ingevulde tabel, en elke rij is ingevuld, of doorgehaald met de reden erbij

**Functional requirements** *wat een component moet doen met welke gegevens; verwijs naar het nummer van de story*

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Soort | Objecttype | Instantie | Bron |
|---|---|---|---|
| | | | |
| | | | |

*Schrijf hier de uitwerking.*

# Afwijkingen per instelling

Wat bij een instelling anders gaat dan hierboven staat, per regel met de instelling erbij. Dit is geen restcategorie: hier staat het materiaal waaruit blijkt of de grootst gemene deler houdbaar is.

| Instelling | Hoofdstuk | Wat daar anders gaat |
|---|---|------------------------------------|
| | | |
| | | |
| | | |

# Vragen aan OKx

Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het speelt.

| Nummer | Hoofdstuk | Vraag |
|---|---|------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
