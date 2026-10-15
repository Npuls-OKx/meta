# IS-OA-06: het aanmeldbare aanbod naar centraal aanmelden

Deze eenheid ontsluit het `Opleidingsprogramma aanbod` van de kernregistratie aan de voorziening voor centraal aanmelden, zodat een aspirant-student daar het startmoment van een opleiding kiest.

Deze eenheid draagt twee soorten onzekerheid, en die blijven hier uit elkaar:

| Onzekerheid | Waar zij staat |
|---|---|
| De vorm: het endpoint, de melding en de schema's die de koppeling nodig heeft | Deze eenheid werkt ze uit, met de grond per veld en per artefact de werkbrief die hem in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public) laat landen |
| De inhoud: wat er werkelijk naar de voorziening voor centraal aanmelden gaat | De afstemming met AII staat open als [Public#112](https://github.com/Npuls-OKx/Public/issues/112). OKx doet het voorstel, AII beslist mee. [De lijst voor AII](#de-lijst-voor-aii) geeft die afstemming een regel per punt |

Elk artefact hieronder draagt zijn stand. De stand `vastgelegd` zegt dat Public het draagt, op het alfa-label dat daar geldt; de stand `voorstel` zegt dat deze eenheid het voorstelt. De voorgestelde schema's staan in [schemas/](schemas/), elk met een `$id` die op `/voorstel` eindigt, zodat wie er een payload tegen valideert ziet waarop hij staat.

De uuid's, de versies en de namen in de voorbeeldpayloads komen uit [casus.md](casus.md), de vaste identificaties van deze interactiespecificatie. Het aanbod is hetzelfde dat [IS-OA-05](stroom-is-oa-05.md) aan de kernregistratie ontsluit.

## De eenheid

| | |
|---|---|
| Bronsysteem | `Kernregistratie systeem studenten (KRS)` |
| Doelsysteem | `Voorziening Centraal Aanmelden (CAMBO)`, de component die hoofdplaat v1.7 kent. Beeld F3-02 noemt AII als opvolger |
| Koppeling | Voorstel: KRS-CAMBO. De beeldregel draagt nog geen koppeling-ID en v1.7 tekent in deze richting geen pijl |
| Beeld | F3-02, met instantie `Regulier BOL 2026` |
| Stand | Voorstel, in beide soorten onzekerheid hierboven |
| Applicatiedienst | Voorstel: ontsluiten van aanmeldbaar aanbod, op het koppelvlak van de kernregistratie. Het model belegt bij KRS `Inschrijvingen beheer` en bij het aanmeldsysteem `Opleiding aanmelding dienst`; W7 vraagt de dienst die aanbod ontsluit |
| Schema's | [offering-status-changed.json](schemas/offering-status-changed.json) voor de melding, [offering-open-for-application.json](schemas/offering-open-for-application.json) voor het aanbod, [offering-processing-status.json](schemas/offering-processing-status.json) voor de verwerking terug, elk met de stand voorstel |

![Beeld F3-02: hetzelfde aanmeldbare aanbod van de kernregistratie naar AII, de voorziening voor centraal aanmelden](../../../model/informatiemodel/img/regels/f3-02-aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii.svg)

De vorm is die van IS-OA-05, met de kernregistratie nu als bezitter en instantie `Regulier BOL 2026` als lading. Welke velden AII vraagt staat open.

De aannames waarop dit voorstel rust, met de partij die erover beslist:

| Nr | Aanname | Grond | Beslist |
|---|---|---|---|
| A1 | Het aanbod gaat naar de component `Voorziening Centraal Aanmelden (CAMBO)`, waarvoor beeld F3-02 AII als opvolger noemt | [voorbeeld-lr1-regels.json](../../../model/informatiemodel/voorbeeld-lr1-regels.json), F3-02; hoofdplaat v1.7 | OKx en AII, [Public#112](https://github.com/Npuls-OKx/Public/issues/112) |
| A2 | De kernregistratie is het ontsluitingspunt van de instelling naar de sector. [U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap) belegt het aanbod bij planning en reikt tot de instellingsgrens | keuze van de sectorarchitect in de beeldregel F3-02 | kerngroep techniek |
| A3 | Een startmoment is een eigen `Opleidingsprogramma aanbod`, met zijn startdatum in `period.start` (`periode.start`) | [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json); het [conceptueel gegevensoverzicht van leerroute 1](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) noemt startmoment op het aanbod | OKx |
| A4 | De `specificationReference` (`specificatieVerwijzing`) blijft op elke instantie staan, zodat de lijn naar de catalogus leesbaar blijft | [U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap), [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) | OKx |
| A5 | Centraal aanmelden meldt terug of het aanbod is opgenomen | spiegelt interactie I3 van de koppeling OC-P&R | AII |
| A6 | Deze eenheid vult het instellings- en opleidingsaanbod aan dat centraal aanmelden uit het Register Instellingen en Opleidingen (RIO) ontvangt, met het programma-aanbod per startmoment | model: de stroom van RIO naar CAMBO draagt de instellings- en opleidingsgegevens | AII |
| A7 | Het aanmeldvenster hangt aan de laag `Opleidingsprogramma aanbod`, want daar kiest de aspirant-student zijn startmoment | model: `Opleidingsprogramma aanbod` `Op basis van` `Aanmelding`; [persona Jochem](../leerroute-uitwerking/doc/persona_jochem.md) kiest in het aanmeldsysteem zijn startmoment en voltooit daar de aanmelding | OKx en AII, [Public#112](https://github.com/Npuls-OKx/Public/issues/112) |
| A8 | De voorziening dient meer instellingen, dus het aanbod draagt zijn aanbieder | [begrippenlijst](../begrippen/begrippenlijst.md): `Opleiding aanbod` is aanbod dat "door een onderwijsaanbieder aangeboden wordt"; model: `Opleidingsaanbod van Instelling` staat boven `Opleiding aanbod` | AII |

Op hoofdplaat v1.7 bereikt de catalogus zowel de kernregistratie als CAMBO langs een knooppunt (junction) achter de pijl van IS-OA-05. Welke route en welke naam gelden staat open als signalering S2 en S3 in de [interactiespecificatie](signaleringen.md).

## De stroom

```mermaid
sequenceDiagram
    autonumber
    participant KRS as Kernregistratie (KRS)
    participant CA as Centraal aanmelden (CAMBO)

    CA->>KRS: C5 [POST /abonnementen] afleveradres en meldingssoorten
    KRS-->>CA: 201, abonnement-id
    Note over KRS: Regulier BOL 2026 gaat van gepland naar aanmeldbaar
    KRS-)CA: C1 [aanmeldbaar-aanbod-beschikbaar] aanbodId, versie, oudeStatus, nieuweStatus, cohort
    CA->>KRS: C2 [GET /aanmeldbaar-aanbod?cohort=2026] de aanmeldbare instanties
    KRS-->>CA: 200, aanbodInstanties met aanmeldvenster, leerweg en locaties
    alt Aanbod gepubliceerd
        CA-)KRS: C4 [verwerkingsstatus] gelukt, met de publicatieVerwijzing
    else Aanbod afgekeurd
        CA-)KRS: C4 [verwerkingsstatus] afgekeurd, met de reden
    end
    Note over KRS: De instelling trekt het aanbod in
    KRS-)CA: C1 [aanmeldbaar-aanbod-beschikbaar] nieuweStatus geannuleerd
    CA->>KRS: C3 [GET /aanmeldbaar-aanbod/{id}] herstel na een gemist bericht
    KRS-->>CA: 200, status geannuleerd
```

Het patroon is melden en dan ophalen (notify-then-pull, [U4](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u4-notify-then-pull)): C1 draagt de aanleiding, C2 haalt de inhoud. Een intrekking rijdt mee op de statusovergang naar `geannuleerd` uit [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), zodat centraal aanmelden het aanbod uit de etalage haalt en C3 die stand ook na een gemist bericht teruggeeft.

## De operaties

Het koppelvlak van de kernregistratie in Public draagt vandaag de meldpatronen (webhooks) voor specificatie en resultaatstructuur. Elke operatie hieronder staat daarom op voorstel; de kolom Stand noemt de vastgelegde operatie waarvan zij de vorm overneemt en de werkbrief die haar in Public laat landen.

| Id | Operatie | Pad of event | Methode | Parameters | Statuscodes | Foutgedrag | Stand |
|---|---|---|---|---|---|---|---|
| C1 | Aanmeldbaar aanbod melden, bij centraal aanmelden | `aanmeldbaar-aanbod-beschikbaar` | POST | geen | 200 | Zonder 200 volgt herhaling met uitstel (backoff) en daarna de wachtrij voor onbestelbare berichten (dead letter channel). Het bericht is herhaalbaar op `offeringId` plus `newStatus` | Voorstel. Vorm van `specificatie-status-gewijzigd` bij het [planningssysteem](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/planningssysteem.md), W5 |
| C2 | De aanmeldbare instanties ophalen, bij de kernregistratie | `/aanmeldbaar-aanbod` | GET | `cohort` (verplicht), `gewijzigdSinds` (optioneel, tijdstempel) | 200, 400 | 400 bij een cohort dat de kernregistratie niet kent. Alleen-lezen, dus herhalen geeft hetzelfde antwoord | Voorstel. Vorm van `GET /onderwijsaanbod` bij het [planningssysteem](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/planningssysteem.md), W4 |
| C3 | Een enkele instantie ophalen, bij de kernregistratie | `/aanmeldbaar-aanbod/{id}` | GET | `versie` (optioneel, standaard de laatste) | 200, 400, 404 | 404 bij een onbekend aanbod-id. Een ingetrokken aanbod komt terug met status `geannuleerd` | Voorstel. Vorm van `GET /onderwijsaanbod/{id}` bij het planningssysteem, W4 |
| C4 | De verwerking terugmelden, bij de kernregistratie | `verwerkingsstatus` | POST | geen | 200 | Zonder 200 volgt herhaling met uitstel en daarna de wachtrij voor onbestelbare berichten. Het bericht is herhaalbaar op `offeringReference` plus `status` | Voorstel. Vorm van `verwerkingsstatus` bij de [onderwijscatalogus](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md), interactie I3, W6 |
| C5 | Het afleveradres vastleggen, over en weer | `/abonnementen` | POST | geen | 201, 400 | Herhaalbaar op `callbackUrl` plus meldingssoort: herregistratie overschrijft | Voorstel op deze koppeling. `POST /abonnementen` met [subscription.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/subscription.json) staat vastgelegd bij de catalogus en het planningssysteem, met `verwerkingsstatus` in de enum `events`. De meldingssoort `aanmeldbaar-aanbod-beschikbaar` komt erbij, W5 |

De voorziening voor centraal aanmelden implementeert C1, de kernregistratie C2, C3 en C4, en beide partijen C5. Het bericht ligt hier vast en het kanaal blijft een inrichtingskeuze van instelling en leverancier, binnen de eigenschappen die [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) opsomt.

## De berichtspecificatie

De sleutel in de payload is de Engelse `properties`-naam uit het schema; de kolom Nederlands geeft de naam uit [mapping.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/mapping.md), waarmee wie de modellen kent de weg terugvindt. De kolom Objecttype noemt het objecttype uit het [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md) waarop het veld terugslaat, en daarmee de aanbodlaag die het veld draagt. De kolom Grond noemt het schema of het document waaruit het veld bestaat.

De kolom Stand zegt waarop een leverancier vandaag kan bouwen. De stand `vastgelegd` geldt voor een sleutel waarvan Public de naam en de waarden draagt; de stand `voorstel` geldt zodra deze eenheid de sleutel of een waarde ervan voorstelt.

### C1, aanmeldbaar aanbod beschikbaar

Een dun bericht met de aanleiding, in de vorm van [specification-status-changed.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-status-changed.json) met het aanbod als onderwerp. Schema: [offering-status-changed.json](schemas/offering-status-changed.json).

| Veld | Nederlands | Type | Kardinaliteit | Objecttype | Stand | Grond |
|---|---|---|---|---|---|---|
| `offeringId` | aanbodId | uuid | 1 | `Opleidingsprogramma aanbod` | voorstel | `id` in education-offering.json, met de naam van [offering-reference.json](schemas/offering-reference.json); specification-status-changed.json noemt dezelfde plek `objectId` |
| `version` | versie | string, semver | 1 | `Opleidingsprogramma aanbod` | vastgelegd | `version` in education-offering.json |
| `offeringType` | aanbodType | enum | 1 | `Opleiding aanbod`, `Opleidingsprogramma aanbod` | vastgelegd | `offeringType` in education-offering.json |
| `specificationReference` | specificatieVerwijzing | object | 1 | `Opleidingsprogramma specificatie` | vastgelegd | [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json), zoals A4 vraagt |
| `oldStatus` | oudeStatus | enum | 1 | `Opleidingsprogramma aanbod` | voorstel | sleutel uit specification-status-changed.json, met de statuswaarden van education-offering.json plus `aanmeldbaar` (W1) |
| `newStatus` | nieuweStatus | enum | 1 | `Opleidingsprogramma aanbod` | voorstel | idem. Deze koppeling meldt op de overgang naar `aanmeldbaar` en naar `geannuleerd` |
| `cohort` | cohort | string | 0..1 | `Cohort / periode` | vastgelegd | `cohort` in education-offering.json; de afnemer filtert zijn opvraag erop |
| `eventId` | eventId | uuid | 0..1 | verwerkingsinformatie, geen objecttype | voorstel | [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) vraagt een stabiel event-id voor herhaalbare verwerking (W8) |

### C2 en C3, het aanmeldbare aanbod

De respons draagt de twee bovenste aanbodlagen uit [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), in `offeringInstances` (`aanbodInstanties`), met `locations` (`locaties`) en `organisationUnits` (`organisatieEenheden`) ernaast. Schema: [offering-open-for-application.json](schemas/offering-open-for-application.json), de snede van education-offering.json voor deze afnemer.

| Veld | Nederlands | Type | Kardinaliteit | Objecttype | Stand | Grond |
|---|---|---|---|---|---|---|
| `offeringInstances[].id` | id | uuid | 1 | `Opleiding aanbod`, `Opleidingsprogramma aanbod` | vastgelegd | education-offering.json. Op dit id ontstaat de `Aanmelding`, die het model met `Op basis van` aan beide lagen hangt |
| `offeringInstances[].offeringType` | aanbodType | enum | 1 | `Opleiding aanbod`, `Opleidingsprogramma aanbod` | vastgelegd | idem, met de waarden `opleidingsaanbod` en `opleidingsprogramma-aanbod` |
| `offeringInstances[].version` | versie | string, semver | 1 | `Opleidingsprogramma aanbod` | vastgelegd | idem |
| `offeringInstances[].parentOfferingId` | bovenliggendAanbodId | uuid of null | 1 | `Opleiding aanbod` | vastgelegd | idem. De startmomenten van een opleiding staan hiermee bij elkaar |
| `offeringInstances[].specificationReference` | specificatieVerwijzing | object | 1 | `Opleidingsprogramma specificatie` | vastgelegd | [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json) |
| `offeringInstances[].name` | naam | string | 1 | `Opleidingsprogramma aanbod` | vastgelegd | education-offering.json. De aspirant-student leest deze naam |
| `offeringInstances[].status` | status | enum | 1 | `Opleidingsprogramma aanbod` | voorstel | idem, met de waarde `aanmeldbaar` erbij (W1). Deze snede draagt `aanmeldbaar` en `geannuleerd` |
| `offeringInstances[].cohort` | cohort | string | 0..1 | `Cohort / periode` | vastgelegd | idem |
| `offeringInstances[].period` | periode | object, `start` en `end` | 0..1 | `Opleidingsprogramma aanbod` | vastgelegd | [period.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/period.json); `start` draagt het startmoment (A3) |
| `offeringInstances[].applicationWindow` | aanmeldvenster | object, `start` en `end` | 0..1 | `Opleidingsprogramma aanbod` | voorstel | vorm van period.json. W2 van [IS-OA-05](stroom-is-oa-05.md) stelt dezelfde sleutel voor; A7 legt haar op het startmoment (W10) |
| `offeringInstances[].enrolmentDeadline` | uitersteInschrijfdatum | string, date | 0..1 | `Opleiding aanbod` | voorstel | het [conceptueel gegevensoverzicht van leerroute 1](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) legt de uiterste inschrijfdatum op de opleidingslaag, naast de opleidingsspecificatie (W3) |
| `offeringInstances[].learningPathway` | leerweg | enum `BOL`, `BBL` | 0..1 | `Opleidingsprogramma aanbod` | voorstel | sleutel, enum en Nederlandse naam van `learningPathway` in [education-specification.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-specification.json), op de programmalaag `leerweg` (W12) |
| `offeringInstances[].targetGroup` | doelgroep | string, open lijst | 0..1 | `Opleidingsprogramma aanbod` | voorstel | sleutel van `targetGroup` in education-specification.json, op de programmalaag `doelgroep`, met de waarde `regulier` voor deze casus (W12) |
| `offeringInstances[].source` | bron | array van object | 0..n | `Kwalificatie dossier`, `Kwalificatie` | voorstel | vorm van [source.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/source.json), die [casus.md](casus.md) voor de leeruitkomst en de aanbodinstantie aanhoudt (W2) |
| `offeringInstances[].providerId` | aanbiederId | uuid | 0..1 | `Organisatie-eenheid`, op de laag `Opleidingsaanbod van Instelling` | voorstel | de onderwijsaanbieder uit de definitie van `Opleiding aanbod` in de [begrippenlijst](../begrippen/begrippenlijst.md), op te lossen in `organisationUnits` (W12) |
| `offeringInstances[].minStudentCount` | minAantalStudenten | integer | 0..1 | `Opleidingsprogramma aanbod` | vastgelegd | education-offering.json |
| `offeringInstances[].maxStudentCount` | maxAantalStudenten | integer | 0..1 | `Opleiding aanbod`, `Opleidingsprogramma aanbod` | vastgelegd | idem. Het conceptueel gegevensoverzicht van leerroute 1 noemt de capaciteit instroom op de opleidingslaag |
| `offeringInstances[].locationId` | locatieId | uuid | 0..1 | `Onderwijslocatie` | vastgelegd | idem, op te lossen in `locations`. Het model hangt `Wordt gegeven op` aan beide lagen |
| `offeringInstances[].executingTeamId` | uitvoerendTeamId | uuid | 0..1 | `Organisatie-eenheid` | vastgelegd | [organisation-unit.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/organisation-unit.json), op te lossen in `organisationUnits` |
| `locations[]` | locaties | array van object | 0..n | `Onderwijslocatie` | vastgelegd | [location.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/location.json); `codes` draagt de vestigingscode, de sleutel waarop een sectorale partij de locatie terugvindt |
| `organisationUnits[]` | organisatieEenheden | array van object | 0..n | `Organisatie-eenheid` | vastgelegd | organisation-unit.json, met `unitType` `instelling` voor de aanbieder en `onderwijsteam` voor het uitvoerend team |

De groepen, de knelpunten en de aanbodlagen onder het programma blijven binnen de instelling, waar het planningssysteem en de kernregistratie ze dragen. Werkbrief W9 legt die snede vast in [gebruiksprofielen.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md), en het schema drukt haar uit met gesloten objecten (`additionalProperties: false`).

#### De lijst voor AII

Per regel het punt waarop de afstemming met AII een antwoord geeft, met het voorstel van OKx ernaast. De velden die hier ontbreken dragen de stand `vastgelegd`: Public draagt ze al.

| Nr | Punt | Voorstel van OKx |
|---|---|---|
| V1 | Welke aanbodlagen de voorziening bereiken | Twee: `opleidingsaanbod` groepeert, `opleidingsprogramma-aanbod` draagt het startmoment waarop de `Aanmelding` ontstaat |
| V2 | Waar het aanmeldvenster hangt en welke termijn het draagt | `applicationWindow` met `start` en `end`, op het startmoment (A7) |
| V3 | Of de uiterste inschrijfdatum naast het venster meereist | `enrolmentDeadline` op de opleidingslaag, waar het conceptueel gegevensoverzicht van leerroute 1 haar legt |
| V4 | Hoe de leerweg en de doelgroep de voorziening bereiken | `learningPathway` en `targetGroup` op het startmoment, met de sleutels die education-specification.json draagt |
| V5 | Hoe het crebo-dossier en de kwalificatie meekomen | `source` als array van source.json op het aanbod, zodat de voorziening ze naast de opleidingsgegevens uit RIO legt (A6) |
| V6 | Of de aanbieder in de payload staat of uit het kanaal volgt | `providerId` op de opleidingslaag, opgelost in `organisationUnits` (A8) |
| V7 | Of de capaciteit meereist, en of de ondergrens daarbij hoort | `maxStudentCount` als capaciteit instroom, met `minStudentCount` als de ondergrens uit de planning, beide optioneel |
| V8 | Welke statusovergangen de voorziening aangaan | `aanmeldbaar` zet het aanbod in de etalage, `geannuleerd` haalt het eruit |
| V9 | Of de voorziening de verwerking terugmeldt, en of zij haar publicatie daarin noemt | C4 met `offeringReference`, en `publicationReference` bij de waarde `gelukt` (A5) |
| V10 | Op welk niveau de locatie meereist | `locationId` wijst de vestiging aan, `locations` draagt de boom daaronder, met de vestigingscode in `codes` |

### C4, de verwerking terug

De vorm van [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json) met het aanbod als onderwerp: dat schema sleutelt op een specificatie. Schema: [offering-processing-status.json](schemas/offering-processing-status.json).

| Veld | Nederlands | Type | Kardinaliteit | Objecttype | Stand | Grond |
|---|---|---|---|---|---|---|
| `status` | status | enum: `ontvangen`, `gestart`, `afgekeurd`, `gelukt`, `nietGelukt` | 1 | verwerkingsinformatie, geen objecttype | vastgelegd | de vijf waarden van `status` in processing-status.json (W6) |
| `offeringReference` | aanbodVerwijzing | object, `offeringId` en `version` | 1 | `Opleidingsprogramma aanbod` | voorstel | [offering-reference.json](schemas/offering-reference.json), de vorm van specification-reference.json met het aanbod als onderwerp; processing-status.json draagt `programmeOfferingId` (`opleidingsaanbodId`) als losse sleutel |
| `publicationReference` | publicatieVerwijzing | uuid | 0..1 | de publicatie bij centraal aanmelden, modelgat in W6 | voorstel | spiegelt `programmeOfferingId` in processing-status.json, dat op `Opleiding aanbod` terugslaat. Hoort bij de waarde `gelukt` |
| `reason` | reden | string | 0..1 | verwerkingsinformatie, geen objecttype | voorstel | hoort bij `afgekeurd` en `nietGelukt`, zoals de reden op `inrichtingsstatus` bij de catalogus (W6) |
| `eventId` | eventId | uuid | 0..1 | verwerkingsinformatie, geen objecttype | voorstel | U5 vraagt een stabiel event-id (W8) |

## De voorbeeldpayloads

De casus is Apothekersassistent, crebo-dossier 23450 met kwalificatie 27141, cohort 2026. Elke uuid staat in [casus.md](casus.md) en volgt daar de [voorbeeldpayloads in Public](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) voor dezelfde casus; de sleutels komen uit de `properties` van de schema's. Elke payload hieronder valideert tegen het schema dat erbij staat.

De melding van C1, waarmee `Regulier BOL 2026` van `gepland` naar `aanmeldbaar` gaat. Het melding-id blijft bij het kanaal, dus buiten de identificaties van casus.md.

```json schema=offering-status-changed
{
  "offeringId": "8c494250-b67a-4666-a762-6f9ec1e70aff",
  "version": "0.1.0",
  "offeringType": "opleidingsprogramma-aanbod",
  "specificationReference": { "specificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7", "version": "0.1.0" },
  "oldStatus": "gepland",
  "newStatus": "aanmeldbaar",
  "cohort": "2026"
}
```

De respons op `GET /aanmeldbaar-aanbod?cohort=2026`. Aanmelden staat open van 1 oktober 2025 tot 1 augustus 2026, de uiterste inschrijfdatum die het conceptueel gegevensoverzicht van leerroute 1 voor deze casus noemt, en het onderwijs start op 1 september 2026.

```json schema=offering-open-for-application
{
  "offeringInstances": [
    {
      "id": "7aa6609f-1d1b-471a-a0f8-beae490d31b5",
      "offeringType": "opleidingsaanbod",
      "version": "0.1.0",
      "parentOfferingId": null,
      "specificationReference": { "specificationId": "79736830-1c5c-470f-b2c2-005029c96733", "version": "0.1.0" },
      "name": "Apothekersassistent 2026",
      "status": "aanmeldbaar",
      "cohort": "2026",
      "period": { "start": "2026-09-01", "end": "2029-07-15" },
      "enrolmentDeadline": "2026-08-01",
      "maxStudentCount": 48,
      "providerId": "6132ece6-d75e-4e80-81ce-91ab7448794d",
      "source": [
        { "standard": "sbb-kwalificatiekader", "type": "kwalificatiedossier", "code": "23450" },
        { "standard": "sbb-kwalificatiekader", "type": "kwalificatie", "code": "27141" }
      ]
    },
    {
      "id": "8c494250-b67a-4666-a762-6f9ec1e70aff",
      "offeringType": "opleidingsprogramma-aanbod",
      "version": "0.1.0",
      "parentOfferingId": "7aa6609f-1d1b-471a-a0f8-beae490d31b5",
      "specificationReference": { "specificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7", "version": "0.1.0" },
      "name": "Regulier BOL 2026",
      "status": "aanmeldbaar",
      "cohort": "2026",
      "period": { "start": "2026-09-01", "end": "2029-07-15" },
      "applicationWindow": { "start": "2025-10-01", "end": "2026-08-01" },
      "learningPathway": "BOL",
      "targetGroup": "regulier",
      "minStudentCount": 24,
      "maxStudentCount": 48,
      "locationId": "59807057-a6f1-473b-9084-114644557a68",
      "executingTeamId": "d9561371-5ece-482d-a675-a076e63f980f"
    }
  ],
  "locations": [
    {
      "id": "59807057-a6f1-473b-9084-114644557a68",
      "locationType": "vestiging",
      "name": "Hoofdlocatie Utrecht",
      "partOfLocationId": null,
      "codes": [ { "codeType": "vestigingscode", "code": "UTR-01" } ]
    }
  ],
  "organisationUnits": [
    {
      "id": "6132ece6-d75e-4e80-81ce-91ab7448794d",
      "unitType": "instelling",
      "name": "ROC Leren Zonder Drempels",
      "parentUnitId": null
    },
    {
      "id": "d9561371-5ece-482d-a675-a076e63f980f",
      "unitType": "onderwijsteam",
      "name": "Onderwijsteam Farmacie",
      "parentUnitId": "6132ece6-d75e-4e80-81ce-91ab7448794d"
    }
  ]
}
```

De terugmelding van C4 op een afkeuring. De publicatieverwijzing bij de waarde `gelukt` kent de voorziening zelf toe en staat daarmee buiten de identificaties van casus.md.

```json schema=offering-processing-status
{
  "status": "afgekeurd",
  "offeringReference": { "offeringId": "8c494250-b67a-4666-a762-6f9ec1e70aff", "version": "0.1.0" },
  "reason": "De vestigingscode UTR-01 staat niet bij deze instelling in het Register Instellingen en Opleidingen"
}
```

## De werkbrieven

Wat er in Npuls-OKx/Public moet gebeuren om dit voorstel daar te laten landen. Alle schema's dragen daar het label alfa, dus een uitbreiding blijft binnen dezelfde ronde. De nieuwe schema's staan in [schemas/](schemas/) met het label voorstel in hun `$id`; bij landing in Public wisselt dat label naar alfa en worden de verwijzingen naar andere schema's relatieve paden, zoals de schema's daar ze dragen.

| Nr | Wat erbij moet | Waar | Versie-impact |
|---|---|---|---|
| W1 | De waarde `aanmeldbaar` in de enum `status`, naast `inPlanning`, `gepland`, `nietRealiseerbaar` en `geannuleerd` | `education-offering.json`, `offeringInstances[].status` | Een waarde in een gesloten lijst: additief voor de verzender en brekend voor wie op die lijst valideert, dus major. W2 van IS-OA-05 vraagt dezelfde waarde |
| W2 | Het veld `source` (`bron`) op de aanbodinstantie, als array van `source.json`, zodat het aanbod zijn crebo-dossier en kwalificatie draagt. Het alternatief laat centraal aanmelden de code ophalen langs de `specificationReference` | `education-offering.json`, `offeringInstances[].source`, met `source.json` als type | Optioneel veld: minor. `source.json` is nu een enkel object op `learning-outcome.json` en wordt hier een array |
| W3 | Het veld `enrolmentDeadline` (`uitersteInschrijfdatum`) op de instantie van de laag `opleidingsaanbod`: daar legt het conceptueel gegevensoverzicht van leerroute 1 de uiterste inschrijfdatum, naast de opleidingsspecificatie. De werkbrief legt die laag vast | `education-offering.json`, `offeringInstances[].enrolmentDeadline` | Optioneel veld: minor. Een latere verschuiving naar de programmalaag is brekend voor de afnemer die hem al leest |
| W4 | De operaties C2 en C3 met hun parameters en statuscodes, plus een componentpagina voor de voorziening voor centraal aanmelden die C1 draagt | de componentpagina [studentinformatiesysteem.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/studentinformatiesysteem.md), plus een nieuwe componentpagina | Nieuwe regels in de endpointtabel, waar de kernregistratie vandaag meldpatronen draagt. Geen schemawijziging |
| W5 | De meldingssoort `aanmeldbaar-aanbod-beschikbaar` in de enum `events`, met [offering-status-changed.json](schemas/offering-status-changed.json) als payload. W1 van [IS-OA-05](stroom-is-oa-05.md) laat datzelfde schema landen voor de melding aan de kernregistratie | `subscription.json`, plus het nieuwe bestand in `schemas/` uit W1 van IS-OA-05 | Nieuw schema, additief: minor. De enumwaarde in `events` is major voor wie op die lijst valideert |
| W6 | Het schema [offering-processing-status.json](schemas/offering-processing-status.json) voor de verwerking terug, dat op [offering-reference.json](schemas/offering-reference.json) uit W8 van IS-OA-05 leunt, plus een objecttype voor de publicatie bij centraal aanmelden | nieuw bestand in `schemas/`, naast `processing-status.json`; het modelgat in het [informatiemodel](../../../model/informatiemodel/informatiemodel.md) | Nieuw schema, additief: minor. Het objecttype voor de publicatie volgt de afstemming met AII, [Public#112](https://github.com/Npuls-OKx/Public/issues/112) |
| W7 | Een applicatiedienst die aanmeldbaar aanbod ontsluit, op het koppelvlak van de kernregistratie, met de pijl naar centraal aanmelden erbij | het ArchiMate-model en de volgende versie van de informatiestromen-hoofdplaat | Nieuwe versie van de plaat. Volgt op het besluit over richting en naam, signalering S2 en S3 |
| W8 | Een stabiel `eventId` in elk bericht, dat [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) vraagt voor herhaalbare verwerking | alle eventschema's in `schemas/`, dus breder dan deze eenheid | Optioneel veld per schema: minor. Verplicht: major |
| W9 | Het gebruiksprofiel van deze koppeling: de twee bovenste aanbodlagen met de statusovergangen naar `aanmeldbaar` en `geannuleerd` | [gebruiksprofielen.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md) | Nieuwe sectie, naast de bestaande profielen. Geen schemawijziging |
| W10 | Het veld `applicationWindow` (`aanmeldvenster`) op de aanbodinstantie, met `start` en `end` in de vorm van `period.json`, naast de `period` die de looptijd draagt | `education-offering.json`, `offeringInstances[].applicationWindow` | Optioneel veld: minor. W2 van IS-OA-05 vraagt dezelfde sleutel, dus een vorm volstaat voor beide koppelingen |
| W11 | Het gebruiksprofiel van [offering-open-for-application.json](schemas/offering-open-for-application.json) voor deze afnemer: de drie velden uit W12 erbij, en de statuswaarden `aanmeldbaar` en `geannuleerd`. W2 van [IS-OA-05](stroom-is-oa-05.md) laat datzelfde schema landen voor de kernregistratie | het nieuwe bestand in `schemas/` uit W2 van IS-OA-05, plus een rij in `gebruiksprofielen.md` per afnemer | Een profiel per afnemer op een schema, additief: minor |
| W12 | De drie velden waarmee de voorziening het aanbod toont zonder in de catalogus te kijken: `learningPathway` (`leerweg`) en `targetGroup` (`doelgroep`) met de sleutels en waarden van `education-specification.json`, en `providerId` (`aanbiederId`) voor de onderwijsaanbieder | `education-offering.json`, `offeringInstances[]` | Optioneel veld per stuk: minor. De sleutels bestaan al op de specificatie, dus de vertaling blijft gelijk |
| W13 | Een resourcenaam voor aanmeldbaar aanbod die elke bezitter in de keten draagt: W3 van [IS-OA-05](stroom-is-oa-05.md) legt `/aanmeldbaar-aanbod` bij de onderwijscatalogus, W4 hierboven bij de kernregistratie | de componentpagina's van beide bezitters | Geen schemawijziging. Een leverancier bouwt dezelfde resource tweemaal in de keten, met dezelfde parameters en statuscodes |
| W14 | De vertaalrijen van de nieuwe schema's en de nieuwe velden, zodat wie de modellen kent de Nederlandse naam terugvindt | [mapping.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/mapping.md) | Nieuwe tabellen en rijen. Geen schemawijziging |

De eis die een instelling hieruit uitvraagt: de kernregistratie ontsluit het aanmeldbare `Opleidingsprogramma aanbod` per startmoment aan centraal aanmelden, met de verwijzing naar de specificatie, het aanmeldvenster en de leerweg erop, en neemt de terugmelding over de verwerking aan. De vorm van die eis ligt vast zodra de aannames hierboven en [de lijst voor AII](#de-lijst-voor-aii) een antwoord hebben, in de afstemming die [Public#112](https://github.com/Npuls-OKx/Public/issues/112) draagt.
