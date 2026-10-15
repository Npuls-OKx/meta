# IS-OA-05: aanmeldbaar opleidingsprogramma-aanbod naar de kernregistratie

De onderwijscatalogus ontsluit het aanmeld- en inschrijfbare `Opleidingsprogramma aanbod` aan de kernregistratie, waar de `Aanmelding` en de `Opleidingsprogramma aanbod verbintenis` van een aspirant-student erop ontstaan.

## De eenheid

| Kenmerk | Waarde |
|---|---|
| Bronsysteem | Onderwijscatalogus |
| Doelsysteem | Kernregistratie systeem studenten (KRS) |
| Koppeling | OC-KRS volgens de beeldregels, OC-SIS volgens hoofdplaat v1.7 ([S-A](#signaleringen)) |
| Beeld | [F3-01, aanmeldbaar aanbod naar de kernregistratie](../../../model/informatiemodel/img/regels/f3-01-aanmeldbaar-aanbod-naar-de-kernregistratie.svg) |
| Lading | `Opleidingsprogramma aanbod`, instantie `Regulier BOL 2026` |
| Status | De pijl en de koppeling staan op v1.7; het [interactiepatroon OC-SIS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md) dekt specificatie en resultaatstructuur, en de operaties voor aanbod staan hier als werkbrief |
| Applicatiedienst | [planbaar-onderwijsaanbod-aanbieder](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md) bij de catalogus, [planbaar-onderwijsaanbod-afnemer](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/planbaar-onderwijsaanbod-afnemer.md) bij de kernregistratie ([S-B](#signaleringen)) |

Grond per regel: [voorbeeld-lr1-regels.json](../../../model/informatiemodel/voorbeeld-lr1-regels.json), beeld F3-01. Objecttypen: [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md). Definities: [begrippenlijst](../begrippen/begrippenlijst.md). De eenheid in haar keten: [de interactiespecificatie](README.md).

## De stroom

```mermaid
sequenceDiagram
    autonumber
    participant OC as Onderwijscatalogus
    participant KRS as Kernregistratie
    Note over OC: Regulier BOL 2026 staat op aanmeldbaar
    OC-)KRS: O1 [aanbod-aanmeldbaar] aanbodId, versie, specificatieVerwijzing
    KRS->>OC: O2 [GET /onderwijsaanbod/{id}] aanbod op id
    alt Aanbod en versie bekend
        OC-->>KRS: 200, aanbodinstantie met haar onderliggende instanties
        KRS-)OC: O4 [inrichtingsstatus] ontvangen, verwerking gestart
        alt Aanbod opgenomen
            KRS-)OC: O4 [inrichtingsstatus] ingericht, met referentie naar de inrichting
        else Aanbod afgekeurd
            KRS-)OC: O4 [inrichtingsstatus] afgekeurd, met reden
        end
    else Aanbod of versie onbekend
        OC-->>KRS: 404, de kernregistratie herhaalt met uitstel, daarna het dead letter-pad
    end
```

De catalogus meldt dun en de kernregistratie haalt op ([U4](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u4-notify-then-pull)). Over de koppeling gaat een verwijzing, met de inhoud op opvraag ([U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap)).

## De operaties

| Id | Operatie | Implementeert | Methode | Parameters | Statuscodes | Foutgedrag | Grond |
|---|---|---|---|---|---|---|---|
| O1 | `aanbod-aanmeldbaar` | Kernregistratie | POST | geen | 200 | Herhalen met uitstel, daarna het dead letter-pad; herhaalde aflevering blijft zonder effect op het event-id | W1 |
| O2 | `/onderwijsaanbod/{id}` | Onderwijscatalogus | GET | `status`, optioneel filter op de onderliggende instanties | 200, 400, 404 | HTTP-foutcodes, de afnemer bepaalt de herhaling | [planbaar-onderwijsaanbod-aanbieder](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md), S-B |
| O3 | `/onderwijsaanbod/{id}/delta` | Onderwijscatalogus | GET | `van`, versie, verplicht; `naar`, versie, verplicht | 200, 400, 404 | HTTP-foutcodes | [U11](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u11-toekomstvaste-endpoints-volledige-structuur-en-delta), W7 |
| O4 | `inrichtingsstatus` | Onderwijscatalogus | POST | geen | 200 | Herhalen met uitstel, daarna het dead letter-pad; herhaalde aflevering blijft zonder effect op het status-id | [dienstpagina onderwijscatalogus](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md), interactie S4; W4 voor het payloadschema |
| O5 | `/abonnementen` | Onderwijscatalogus en kernregistratie | POST | geen | 201, 400 | HTTP-foutcodes; herregistratie overschrijft op de combinatie afleveradres plus meldingssoort | [dienstpagina onderwijscatalogus](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md), interactie I8; W5 voor de meldingssoort |

Het bericht ligt hier vast, het kanaal blijft een inrichtingskeuze van instelling en leverancier binnen de vier eigenschappen van [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal).

## De eisen

Deze eisen zijn de uitvraagbare kern van IS-OA-05, elk met een toetsgeval op de casus.

| Id | Eis | Toetsgeval |
|---|---|---|
| E1 | De onderwijscatalogus meldt de kernregistratie dat een `Opleidingsprogramma aanbod` aanmeldbaar is, met id, versie en de verwijzing naar de specificatie | O1 op `Regulier BOL 2026`: de melding draagt aanbod-id, versie en specificatieverwijzing, en laat de aanbodinhoud bij de bezitter |
| E2 | De onderwijscatalogus levert dat aanbod op id, met de onderliggende instanties | O2 op `8c494250-b67a-4666-a762-6f9ec1e70aff`: statuscode 200, met de instanties die via `bovenliggendAanbodId` eronder hangen |
| E3 | Een tweede aflevering van dezelfde melding heeft geen aanvullend effect | O1 tweemaal afleveren met hetzelfde event-id: de kernregistratie richt het aanbod eenmaal in en meldt eenmaal `ingericht` |
| E4 | De kernregistratie meldt de uitkomst terug, met een referentie bij opname en een reden bij afkeuring | O4 na opname: status `ingericht` met de referentie naar de inrichting; na een validatiefout: status `afgekeurd` met reden |
| E5 | Een onbekend aanbod of een onbekende versie levert een verwerkbaar antwoord | O2 op een onbekend id: statuscode 404, waarna de kernregistratie herhaalt met uitstel en daarna neerlegt in het dead letter-pad |

## De berichtspecificatie

Elk veld slaat terug op een objecttype uit het [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md). De kolom Grond noemt het schema in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen/schemas) of de werkbrief die het veld nog moet vastleggen.

### M1, melding `aanbod-aanmeldbaar`

Dun, conform U4: de aanleiding met een verwijzing.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|
| `eventId` | uuid | 1 | ja | kanaaleigenschap, geen objecttype | W6 |
| `aanbodId` | uuid | 1 | ja | `Opleidingsprogramma aanbod` | `id` uit [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), W1 |
| `versie` | string, semver | 1 | ja | `Opleidingsprogramma aanbod` | `versie` uit education-offering.json, W1 |
| `aanbodType` | enum | 1 | ja | `Opleidingsprogramma aanbod` | waarde `opleidingsprogramma-aanbod`, W1 |
| `specificatieVerwijzing` | object | 1 | ja | `Opleidingsprogramma specificatie` | [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json), W1 |

### M2, respons van `GET /onderwijsaanbod/{id}`

De aanbodinstantie uit [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), op de laag `opleidingsprogramma-aanbod`.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|
| `id` | uuid | 1 | ja | `Opleidingsprogramma aanbod` | education-offering.json |
| `aanbodType` | enum | 1 | ja | `Opleidingsprogramma aanbod` | waarde `opleidingsprogramma-aanbod` |
| `versie` | string, semver | 1 | ja | `Opleidingsprogramma aanbod` | education-offering.json |
| `bovenliggendAanbodId` | uuid of null | 1 | ja | `Opleiding aanbod` | education-offering.json, S-C |
| `specificatieVerwijzing` | object | 1 | ja | `Opleidingsprogramma specificatie` | [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json) |
| `naam` | string | 1 | ja | `Opleidingsprogramma aanbod` | education-offering.json |
| `status` | enum | 1 | ja | `Opleidingsprogramma aanbod` | waarden `inPlanning`, `gepland`, `nietRealiseerbaar`, `geannuleerd`; W2 |
| `cohort` | string | 0..1 | nee | `Cohort / periode` | education-offering.json |
| `periode` | object | 0..1 | nee | `Cohort / periode` | [period.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/period.json), `start` en `eind` |
| `minAantalStudenten` | integer | 0..1 | nee | `Opleidingsprogramma aanbod` | education-offering.json |
| `maxAantalStudenten` | integer | 0..1 | nee | `Opleidingsprogramma aanbod` | education-offering.json |
| `locatieId` | uuid | 0..1 | nee | `Onderwijslocatie` | [location.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/location.json), uitgewerkt in `locaties` |
| `uitvoerendTeamId` | uuid | 0..1 | nee | `Organisatie-eenheid` | [organisation-unit.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/organisation-unit.json), uitgewerkt in `organisatieEenheden` |
| `groepen` | array | 0..n | nee | `Plaatsingsgroep` | [group.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/group.json), instantie `APO26-1A` |
| `knelpunten` | array | 0..n | nee | `Opleidingsprogramma aanbod`, als eigenschap | [bottleneck.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/bottleneck.json) |

### M3, melding `inrichtingsstatus`

| Veld | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|
| `status` | enum | 1 | ja | verwerkingsinformatie, geen objecttype | waarden `ontvangen`, `gestart`, `ingericht`, `afgekeurd`, `nietIngericht` uit interactie S4; W4 |
| `aanbodId` | uuid | 1 | ja | `Opleidingsprogramma aanbod` | W4 |
| `inrichtingReferentie` | uuid | 0..1 | nee | de inrichting bij de kernregistratie, geen objecttype | [dienstpagina onderwijscatalogus](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md); W4 |
| `reden` | string | 0..1 | nee | verwerkingsinformatie, geen objecttype | W4 |

## De voorbeeldpayload

Respons van O2 op `Regulier BOL 2026`, met alleen velden die [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json) vandaag draagt. De uuid's komen uit de [voorbeeldpayloads](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/voorbeeldpayloads.md) in Public, de naam en de aantallen uit beeld F3-01 en F2-07.

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
      "status": "gepland",
      "cohort": "2026",
      "periode": { "start": "2026-09-01", "eind": "2029-07-15" }
    },
    {
      "id": "8c494250-b67a-4666-a762-6f9ec1e70aff",
      "aanbodType": "opleidingsprogramma-aanbod",
      "versie": "0.1.0",
      "bovenliggendAanbodId": "7aa6609f-1d1b-471a-a0f8-beae490d31b5",
      "specificatieVerwijzing": { "specificatieId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7", "versie": "0.1.0" },
      "naam": "Regulier BOL 2026",
      "status": "gepland",
      "knelpunten": [],
      "cohort": "2026",
      "periode": { "start": "2026-09-01", "eind": "2029-07-15" },
      "minAantalStudenten": 24,
      "maxAantalStudenten": 48,
      "locatieId": "59807057-a6f1-473b-9084-114644557a68",
      "uitvoerendTeamId": "d9561371-5ece-482d-a675-a076e63f980f"
    }
  ]
}
```

De crebo 23450 van het kwalificatiedossier staat in `leeruitkomsten[].bron.code` van de onderwijsspecificatie en is vanuit het aanbod alleen via `specificatieVerwijzing` en de leeruitkomst bereikbaar. Werkbrief W2 en W3 leggen de twee velden vast die het aanbod aanmeldbaar maken voor de kernregistratie en voor centraal aanmelden. Dit fragment toont de vorm die zij voorstellen.

```json
{
  "id": "8c494250-b67a-4666-a762-6f9ec1e70aff",
  "status": "aanmeldbaar",
  "aanmeldvenster": { "start": "2025-10-01", "eind": "2026-08-01" },
  "codes": [
    { "codeType": "crebo", "code": "23450" },
    { "codeType": "kwalificatie", "code": "27141" }
  ]
}
```

## De werkbrieven

| Id | Wat erbij moet | In welk schema | Versie-impact |
|---|---|---|---|
| W1 | De melding `aanbod-aanmeldbaar` met `aanbodId`, `versie`, `aanbodType` en `specificatieVerwijzing`, naar het model van `specificatie-planbaar` | Nieuw schema `offering-available.json`, plus een rij op de [dienstpagina van de kernregistratie](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/studentinformatiesysteem.md) | Nieuw schema en nieuw endpoint, additief: minor |
| W2 | Een uitdrukking van aanmeldbaarheid: de waarde `aanmeldbaar` in `status`, plus `aanmeldvenster` met `start` en `eind` voor de termijn waarin aanmelden openstaat, los van `periode` die de looptijd draagt | [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), eigenschap `status` en een nieuwe eigenschap `aanmeldvenster` naar het model van [period.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/period.json) | Nieuw optioneel veld: minor. Een waarde toevoegen aan de gesloten `status`-lijst is additief voor de verzender en brekend voor wie op die lijst valideert: major |
| W3 | Een identificerende code op de aanbodinstantie, zodat crebo en kwalificatie meekomen zonder de leeruitkomstboom; [ADR 0023](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) houdt leeruitkomsten uit de koppeling met planning | [education-offering.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-offering.json), nieuwe eigenschap `codes` als array van [code.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/code.json), zoals `locaties` die al draagt | Nieuw optioneel veld: minor |
| W4 | Het payloadschema van `inrichtingsstatus`, met `aanbodId` naast de bestaande specificatieverwijzing; [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json) draagt `opleidingsaanbodId` voor de wortellaag, dus de naam zegt om welke laag het gaat | Nieuw schema `arrangement-status.json`, aangekondigd op de [dienstpagina van de onderwijscatalogus](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md) als nog uit te werken | Nieuw schema, additief: minor |
| W5 | De meldingssoorten `aanbod-aanmeldbaar` en `inrichtingsstatus` in de lijst waarop een partij zich abonneert | [subscription.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/subscription.json), eigenschap `events` | Waarden toevoegen aan een gesloten lijst: additief voor de abonnee en brekend voor wie erop valideert, major |
| W6 | Een stabiel `eventId` op elke melding, dat U5 voor herhaalde aflevering eist | [specification-changed.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-changed.json), [specification-status-changed.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-status-changed.json) en het nieuwe schema uit W1 | Optioneel: minor. Verplicht: major |
| W7 | De deltavorm op het aanbod, die U11 naast de volledige structuur vraagt | Nieuw schema `education-offering-delta.json` naar het model van [education-specification-delta.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-specification-delta.json), plus endpoint O3 op de dienstpagina | Nieuw schema en nieuw endpoint, additief: minor |

## Signaleringen

| Id | Signalering | Besluit |
|---|---|---|
| S-A | De beeldregels noemen deze koppeling OC-KRS, hoofdplaat v1.7 noemt haar OC-SIS, en het [interactiepatroon OC-SIS](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md) vat kernregistratie en studentvolgsysteem samen in hetzelfde component. Hetzelfde pijl-id draagt ook de stroom naar centraal aanmelden | Een naam en een pijl per koppeling, en of de kernregistratie hier als eigen component telt |
| S-B | De dienst `planbaar-onderwijsaanbod-aanbieder` legt haar endpoints bij het planningssysteem en [U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap) legt het aanbod daar. Deze eenheid laat de catalogus aanbod ontsluiten. De dienstenlijst staat op een vastgezet commit en bereikt `dev` nog | Claimt de catalogus dezelfde dienst, of komt er een dienst voor aanmeldbaar aanbod. Dit is signalering S4 van de [interactiespecificatie](README.md) |
| S-C | Het informatiemodel noemt de laag boven het programma `Opleiding aanbod`, de voorbeelduitwerking schrijft `Opleidingaanbod` | Een naam, in het model en in de voorbeelduitwerking gelijk |
| S-D | De voorbeelduitwerking geeft `Regulier BOL 2026` 24 tot 48 studenten, de voorbeeldpayload in Public geeft 18 tot 120 | Welke waarden de casus draagt |
| S-E | Het interactiepatroon OC-SIS kent voor deze koppeling nog geen interactie voor het registreren van een afleveradres, terwijl de melding O1 daarop leunt | Het afleveradres per koppeling, aansluitend op [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) |

Fase 3 begint hier; de aanmelding, de intake en de inschrijving beginnen bij beeld F3-03 en vallen buiten deze eenheid.
