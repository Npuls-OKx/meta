# IS-OA-06: het aanmeldbare aanbod naar centraal aanmelden

Deze eenheid ontsluit het `Opleidingsprogramma aanbod` van de kernregistratie aan de voorziening voor centraal aanmelden, zodat een aspirant-student daar het startmoment van een opleiding kiest.

## De eenheid

| | |
|---|---|
| Bronsysteem | `Kernregistratie systeem studenten (KRS)` |
| Doelsysteem | `Voorziening Centraal Aanmelden (CAMBO)`, de component die hoofdplaat v1.7 kent. Beeld F3-02 noemt AII als opvolger |
| Koppeling | Voorstel: KRS-CAMBO. De beeldregel draagt nog geen koppeling-ID en v1.7 tekent in deze richting geen pijl |
| Beeld | [F3-02](../../../model/informatiemodel/img/regels/f3-02-aanmeldbaar-aanbod-van-de-kernregistratie-naar-aii.svg), met instantie `Regulier BOL 2026` |
| Status | Voorstel. De afstemming met AII over aanmelden, inschrijven en intekenen staat open als [Public#112](https://github.com/Npuls-OKx/Public/issues/112) |
| Applicatiedienst | Voorstel: ontsluiten van aanmeldbaar aanbod, op het koppelvlak van de kernregistratie. Het model belegt bij KRS `Inschrijvingen beheer` en bij het aanmeldsysteem `Opleiding aanmelding dienst`; W7 vraagt de dienst die aanbod ontsluit |

De aannames waarop dit voorstel rust, met de partij die erover beslist:

| Nr | Aanname | Grond | Beslist |
|---|---|---|---|
| A1 | Het aanbod gaat naar de component `Voorziening Centraal Aanmelden (CAMBO)`, waarvoor beeld F3-02 AII als opvolger noemt | [voorbeeld-lr1-regels.json](../../../model/informatiemodel/voorbeeld-lr1-regels.json), F3-02; hoofdplaat v1.7 | OKx en AII, [Public#112](https://github.com/Npuls-OKx/Public/issues/112) |
| A2 | De kernregistratie is het ontsluitingspunt van de instelling naar de sector. [U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap) belegt het aanbod bij planning en reikt tot de instellingsgrens | keuze van de sectorarchitect in de beeldregel F3-02 | kerngroep techniek |
| A3 | Een startmoment is een eigen `Opleidingsprogramma aanbod`, met zijn startdatum in `periode.start` | [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json); de ankertabel van leerroute 1 noemt startmoment op het aanbod | OKx |
| A4 | De `specificatieVerwijzing` blijft op elke instantie staan, zodat de lijn naar de catalogus leesbaar blijft | [U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap), [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) | OKx |
| A5 | Centraal aanmelden meldt terug of het aanbod is opgenomen | spiegelt interactie I3 van de koppeling OC-P&R | AII |
| A6 | Deze eenheid vult het instellings- en opleidingsaanbod aan dat centraal aanmelden uit het Register Instellingen en Opleidingen (RIO) ontvangt, met het programma-aanbod per startmoment | model: de stroom van RIO naar CAMBO draagt de instellings- en opleidingsgegevens | AII |

Op hoofdplaat v1.7 bereikt de catalogus zowel de kernregistratie als CAMBO langs een knooppunt (junction) achter de pijl van IS-OA-05. Welke route en welke naam gelden staat open als signalering S2 en S3 in de [interactiespecificatie](README.md#signaleringen-en-openstaande-punten).

## De stroom

```mermaid
sequenceDiagram
    autonumber
    participant KRS as Kernregistratie (KRS)
    participant CA as Centraal aanmelden (CAMBO)

    CA->>KRS: C5 [POST /abonnementen] afleveradres en events
    KRS-->>CA: 201, abonnement-id
    Note over KRS: Regulier BOL 2026 staat aanmeldbaar
    KRS-)CA: C1 [aanmeldbaar-aanbod-beschikbaar] aanbod-id, versie, cohort, status
    CA->>KRS: C2 [GET /aanmeldbaar-aanbod?cohort=2026] de aanmeldbare instanties
    KRS-->>CA: 200, aanbodinstanties met specificatieVerwijzing en locaties
    alt Aanbod opgenomen
        CA-)KRS: C4 [aanbodstatus] gelukt, met verwijzing naar de publicatie
    else Aanbod afgekeurd
        CA-)KRS: C4 [aanbodstatus] afgekeurd, met de reden
    end
    CA->>KRS: C3 [GET /aanmeldbaar-aanbod/{id}] herstel na een gemist bericht
    KRS-->>CA: 200, status geannuleerd: het aanbod is ingetrokken
```

Het patroon is notify-then-pull ([U4](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u4-notify-then-pull)): C1 draagt de aanleiding, C2 haalt de inhoud. Een intrekking rijdt mee op de status `geannuleerd` uit [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), zodat centraal aanmelden de reden van de intrekking leest.

## De operaties

Het koppelvlak van de kernregistratie in Public draagt vandaag uitsluitend webhooks. Elke operatie hieronder is daarmee een werkbrief; de kolom Vorm noemt de bestaande operatie waarvan zij de vorm overneemt.

| Id | Operatie | Pad of event | Methode | Parameters | Statuscodes | Foutgedrag | Vorm |
|---|---|---|---|---|---|---|---|
| C1 | Aanmeldbaar aanbod melden, bij centraal aanmelden | `aanmeldbaar-aanbod-beschikbaar` | POST | geen | 200 | Zonder 200 volgt herhaling met uitstel (backoff) en daarna het dead-letterpad. Het bericht is herhaalbaar op het aanbod-id | `specificatie-planbaar` bij het planningssysteem (W5) |
| C2 | De aanmeldbare instanties ophalen, bij de kernregistratie | `/aanmeldbaar-aanbod` | GET | `cohort` (verplicht), `gewijzigdSinds` (optioneel, timestamp) | 200, 400 | 400 bij een cohort dat de kernregistratie niet kent. Alleen-lezen, dus herhalen geeft hetzelfde antwoord | `GET /onderwijsaanbod` bij het planningssysteem (W4) |
| C3 | Een enkele instantie ophalen, bij de kernregistratie | `/aanmeldbaar-aanbod/{id}` | GET | `versie` (optioneel, standaard de laatste) | 200, 400, 404 | 404 bij een onbekend aanbod-id. Een ingetrokken aanbod komt terug met status `geannuleerd` | `GET /onderwijsaanbod/{id}` bij het planningssysteem (W4) |
| C4 | De verwerking terugmelden, bij de kernregistratie | `aanbodstatus` | POST | geen | 200 | Zonder 200 volgt herhaling met uitstel en daarna het dead-letterpad. Het bericht is herhaalbaar op het status-id | `verwerkingsstatus` bij de onderwijscatalogus (W6) |
| C5 | Het afleveradres vastleggen, over en weer | `/abonnementen` | POST | geen | 201, 400 | Herhaalbaar op `callbackUrl` plus eventtype: herregistratie overschrijft | `POST /abonnementen` bij de onderwijscatalogus (W5) |

## De berichten

**C1, aanmeldbaar aanbod beschikbaar.** Een dun bericht met de aanleiding.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|
| `objectId` | uuid | 1 | ja | `Opleidingsprogramma aanbod` | vorm van [specification-status-changed.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-status-changed.json) (W5) |
| `versie` | string, semver | 1 | ja | `Opleidingsprogramma aanbod` | `versie` in education-offering.json |
| `nieuweStatus` | enum | 1 | ja | `Opleidingsprogramma aanbod` | `status` in education-offering.json, waarde `aanmeldbaar` (W1) |
| `cohort` | string | 0..1 | nee | `Cohort / periode` | `cohort` in education-offering.json |
| `eventId` | uuid | 0..1 | nee | geen | [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) vraagt een stabiel event-id (W8) |

**C2 en C3, het aanmeldbare aanbod.** De respons volgt education-offering.json, met `aanbodInstanties` en `locaties`.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|
| `aanbodInstanties[].id` | uuid | 1 | ja | `Opleidingsprogramma aanbod` | education-offering.json |
| `aanbodInstanties[].aanbodType` | enum | 1 | ja | `Opleidingsprogramma aanbod` | idem, waarde `opleidingsprogramma-aanbod` |
| `aanbodInstanties[].versie` | string, semver | 1 | ja | `Opleidingsprogramma aanbod` | idem |
| `aanbodInstanties[].bovenliggendAanbodId` | uuid of null | 1 | ja | `Opleiding aanbod` | idem |
| `aanbodInstanties[].specificatieVerwijzing` | object | 1 | ja | `Opleidingsprogramma specificatie` | [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json) |
| `aanbodInstanties[].naam` | string | 1 | ja | `Opleidingsprogramma aanbod` | education-offering.json |
| `aanbodInstanties[].status` | enum | 1 | ja | `Opleidingsprogramma aanbod` | idem, waarde `aanmeldbaar` (W1) |
| `aanbodInstanties[].cohort` | string | 0..1 | nee | `Cohort / periode` | idem |
| `aanbodInstanties[].periode` | object, `start` en `eind` | 0..1 | nee | `Opleidingsprogramma aanbod` | [period.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/period.json); `start` draagt het startmoment (A3) |
| `aanbodInstanties[].minAantalStudenten` | integer | 0..1 | nee | `Opleidingsprogramma aanbod` | education-offering.json |
| `aanbodInstanties[].maxAantalStudenten` | integer | 0..1 | nee | `Opleidingsprogramma aanbod` | idem, draagt de instroomcapaciteit |
| `aanbodInstanties[].locatieId` | uuid | 0..1 | nee | `Onderwijslocatie` | idem, op te lossen in `locaties` |
| `aanbodInstanties[].uitvoerendTeamId` | uuid | 0..1 | nee | `Organisatie-eenheid` | [organisation-unit.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/organisation-unit.json) |
| `aanbodInstanties[].bron` | array van object | 0..n | nee | `Kwalificatie dossier`, `Kwalificatie` | vorm van [source.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/source.json), nu alleen op de leeruitkomst (W2) |
| `aanbodInstanties[].uitersteInschrijfdatum` | string, date | 0..1 | nee | `Opleidingsprogramma aanbod` | de ankertabel van leerroute 1 noemt haar op het aanbod (W3) |
| `locaties[]` | array van object | 0..n | nee | `Onderwijslocatie` | [location.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/location.json); `codes` draagt de vestigingscode |

**C4, de verwerking terug.** De vorm van [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json), met het aanbod als onderwerp.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|
| `status` | enum: `ontvangen`, `gestart`, `afgekeurd`, `gelukt`, `nietGelukt` | 1 | ja | geen | processing-status.json (W6) |
| `aanbodVerwijzing` | object, `aanbodId` en `versie` | 1 | ja | `Opleidingsprogramma aanbod` | vorm van specification-reference.json (W6) |
| `publicatieVerwijzing` | uuid | 0..1 | nee | `Aanmelding` | spiegelt `opleidingsaanbodId` in processing-status.json (W6) |
| `reden` | string | 0..1 | nee | geen | nieuw bij `afgekeurd` en `nietGelukt` (W6) |

Welk deel van education-offering.json over deze koppeling reist hoort in [gebruiksprofielen.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md) (W9). Het voorstel: de lagen `opleidingsaanbod` en `opleidingsprogramma-aanbod` met hun locaties reizen mee, de groepen en de knelpunten blijven binnen de instelling.

## De voorbeeldpayload

De respons op `GET /aanmeldbaar-aanbod?cohort=2026` voor Apothekersassistent, crebo-dossier 23450 met kwalificatie 27141. De sleutels zijn die van de [voorbeeldpayload in Public](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) voor dezelfde casus; `status`, `bron` en `uitersteInschrijfdatum` rusten op een werkbrief.

```json
{
  "aanbodInstanties": [
    {
      "id": "7aa6609f-1d1b-471a-a0f8-beae490d31b5",
      "aanbodType": "opleidingsaanbod",
      "versie": "0.1.0",
      "bovenliggendAanbodId": null,
      "specificatieVerwijzing": { "specificatieId": "79736830-1c5c-470f-b2c2-005029c96733", "versie": "0.1.0" },
      "naam": "Apothekersassistent 2026",
      "status": "aanmeldbaar",
      "cohort": "2026",
      "periode": { "start": "2026-09-01", "eind": "2029-07-15" },
      "maxAantalStudenten": 48,
      "bron": [
        { "standaard": "sbb-kwalificatiekader", "type": "kwalificatiedossier", "code": "23450" },
        { "standaard": "sbb-kwalificatiekader", "type": "kwalificatie", "code": "27141" }
      ]
    },
    {
      "id": "8c494250-b67a-4666-a762-6f9ec1e70aff",
      "aanbodType": "opleidingsprogramma-aanbod",
      "versie": "0.1.0",
      "bovenliggendAanbodId": "7aa6609f-1d1b-471a-a0f8-beae490d31b5",
      "specificatieVerwijzing": { "specificatieId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7", "versie": "0.1.0" },
      "naam": "Regulier BOL 2026",
      "status": "aanmeldbaar",
      "cohort": "2026",
      "periode": { "start": "2026-09-01", "eind": "2029-07-15" },
      "minAantalStudenten": 24,
      "maxAantalStudenten": 48,
      "locatieId": "59807057-a6f1-473b-9084-114644557a68",
      "uitvoerendTeamId": "d9561371-5ece-482d-a675-a076e63f980f",
      "uitersteInschrijfdatum": "2026-08-15"
    }
  ],
  "locaties": [
    {
      "id": "59807057-a6f1-473b-9084-114644557a68",
      "locatieType": "vestiging",
      "naam": "Hoofdlocatie Utrecht",
      "valtBinnenLocatieId": null,
      "codes": [ { "codeType": "vestigingscode", "code": "UTR-01" } ]
    }
  ]
}
```

## De werkbrieven

Elke werkbrief noemt wat erbij moet, in welk schema of document, en de versie-impact. Alle schema's dragen het label alfa in hun `$id`, dus een uitbreiding blijft binnen dezelfde ronde.

| Nr | Wat erbij moet | Waar | Versie-impact |
|---|---|---|---|
| W1 | De waarde `aanmeldbaar` in de enum `status`, naast `inPlanning`, `gepland`, `nietRealiseerbaar` en `geannuleerd` | `education-offering.json`, `offeringInstances[].status` | Uitbreiding van de enum. Een afnemer die strikt valideert loopt mee in dezelfde alfa-ronde |
| W2 | Het veld `bron` op de aanbodinstantie, als array van `source.json`, zodat het aanbod zijn crebo-dossier en kwalificatie draagt. Het alternatief laat centraal aanmelden de code ophalen langs de `specificatieVerwijzing` | `education-offering.json`, met `source.json` als type | Optioneel veld, verenigbaar met de huidige alfa. `source.json` is nu een enkel object op `learning-outcome.json` en wordt hier een array |
| W3 | Het veld `uitersteInschrijfdatum` op de aanbodinstantie, dat de ankertabel van leerroute 1 al op het aanbod noemt | `education-offering.json` | Optioneel veld, verenigbaar met de huidige alfa |
| W4 | De operaties `GET /aanmeldbaar-aanbod` en `GET /aanmeldbaar-aanbod/{id}`, met de parameters en statuscodes uit de operatietabel | de dienstpagina [studentinformatiesysteem.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/studentinformatiesysteem.md) | Nieuwe regels in de endpointtabel, waar de kernregistratie vandaag uitsluitend webhooks draagt |
| W5 | Een eventschema `aanmeldbaar-aanbod-beschikbaar` met de velden uit de C1-tabel, en de bijbehorende waarde in de enum `events` | nieuw bestand in `schemas/`, plus `subscription.json` | Nieuw schema met eigen `$id`; de releasebijlage leest de map in. Voor `subscription.json` een enum-uitbreiding |
| W6 | Een statusschema voor het aanbod, met `aanbodVerwijzing`, `publicatieVerwijzing` en `reden`, naast het bestaande schema dat op een specificatie sleutelt | nieuw bestand in `schemas/`, naast `processing-status.json` | Nieuw schema met eigen `$id` |
| W7 | Een applicatiedienst die aanmeldbaar aanbod ontsluit, op het koppelvlak van de kernregistratie, met de pijl naar centraal aanmelden erbij | het ArchiMate-model en de volgende versie van de informatiestromen-hoofdplaat | Nieuwe versie van de plaat. Volgt op het besluit over richting en naam, signalering S2 en S3 |
| W8 | Een stabiel `eventId` in elk bericht, dat [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) vraagt voor herhaalbare verwerking | alle eventschema's in `schemas/`, dus breder dan deze eenheid | Optioneel veld per schema, verenigbaar met de huidige alfa |
| W9 | Het gebruiksprofiel van deze koppeling: welke lagen van het aanbod meereizen | [gebruiksprofielen.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md) | Nieuwe sectie, naast de bestaande profielen |

De eis die een instelling hieruit uitvraagt: de kernregistratie ontsluit het aanmeldbare `Opleidingsprogramma aanbod` per startmoment aan centraal aanmelden, met de verwijzing naar de specificatie erop, en neemt de terugmelding over de verwerking aan. De vorm van die eis ligt vast zodra A1 tot en met A6 zijn beantwoord.
