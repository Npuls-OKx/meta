# IS-OA-03, het verzoek tot aanbod naar het planningssysteem

Deze eenheid levert het planningssysteem de planbare specificatiestructuur van een opleiding met haar planbare waarden, als verzoek om daarvan onderwijsaanbod te maken.

## De eenheid

| | |
|---|---|
| Bronsysteem | Onderwijscatalogus, bezitter van de onderwijsspecificaties ([U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap)) |
| Doelsysteem | Planningssysteem, bezitter van het onderwijsaanbod |
| Koppeling | OC-P&R, interactie I1, I2, I3, I7 en I8 van het [interactiepatroon onderwijscatalogus naar planning en roostering](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md) |
| Beeld | [F2-03](../../../model/informatiemodel/img/regels/f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.svg), met de regels in [voorbeeld-lr1-regels.json](../../../model/informatiemodel/voorbeeld-lr1-regels.json) |
| Status | Gespecificeerd: het interactiepatroon draagt de endpoints en de meldpatronen (webhooks), elk schema staat op alfa |
| Applicatiedienst | `Onderwijsspecificatie uitwerking` op de onderwijscatalogus ontsluit de structuur, `(meer) jaar capaciteit planning` en `Periode planning` op het planningssysteem nemen haar aan (hoofdplaat v1.7) |

De lading: het verzoek tot aanbod voor cohort 2026, met de opleiding, haar programma, de eenheden en hun leeronderdelen, en per specificatie de leeruitkomst waarnaar zij verwijst. De planbare waarden uit het onderwijsontwerp staan in [werkbrief](#werkbrieven) W2 tot en met W7.

## De stroom

```mermaid
sequenceDiagram
    autonumber
    participant OC as Onderwijscatalogus
    participant PL as Planningssysteem

    PL->>OC: I8 [POST /abonnementen] callbackUrl en event-typen
    OC-->>PL: 201 abonnement-id
    Note over OC: opleidingsprogrammaspecificatie krijgt status gepubliceerd
    OC-)PL: I1 [specificatie-planbaar] specificatieId en versie
    PL->>OC: I2 [GET /onderwijsspecificaties/{id}] structuur op versie
    OC-->>PL: 200 onderwijsspecificaties en regelsets, manifest legt de versies vast
    alt structuur valide
        PL-)OC: I3 [verwerkingsstatus] ontvangen, planproces gestart
    else structuur afgekeurd
        PL-)OC: I3 [verwerkingsstatus] afgekeurd, met de validatiefout
    end
    opt melding beland in de wachtrij voor onbestelbare berichten
        PL->>OC: I7 [GET /onderwijsspecificaties] gewijzigdSinds en status
        OC-->>PL: 200 specificatie-ids met hun laatste versie
    end
```

Het planproces loopt daarna los van deze aanroep. De uitkomst, met de verwijzing naar het `Opleiding aanbod`, komt terug in [IS-OA-04](README.md#de-kiesbare-eenheden).

## Functionele eisen

De eisen komen uit het interactiepatroon OC-P&R. Een instelling citeert het eis-id en toetst op de genoemde operaties.

| Id | Eis | Operaties | Toetsgeval |
|---|---|---|---|
| [functionele-eis-0001](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0001) | De onderwijscatalogus laat het planningssysteem weten dat een specificatie gereed is om te plannen, waarna het planningssysteem een opleidingsaanbod met referentie teruglevert | O1, O2, O4 | Een specificatie die status `gepubliceerd` krijgt levert een melding op, en de daaropvolgende opvraag geeft dezelfde `specificatieId` en `versie` terug |
| [functionele-eis-0002](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0002) | Het planningssysteem werkt de planning bij wanneer een specificatie wijzigt, met de wijziging of de volledige structuur als keuze voor de ontvanger ([U11](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u11-toekomstvaste-endpoints-volledige-structuur-en-delta)) | O2, O3 | Beide vormen staan op dezelfde resource: de volledige structuur op `{id}` en de wijziging op `{id}/delta` tussen twee versies |
| [functionele-eis-0006](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0006) | Beide partijen halen de informatie na een gemiste melding alsnog op | O5 | Een opvraag met `gewijzigdSinds` op een tijdstip voor de gemiste melding geeft de betrokken specificatie terug |
| [functionele-eis-0007](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0007) | Beide partijen leggen een afleveradres vast voordat meldingen worden afgeleverd | O6 | Een tweede registratie op dezelfde `callbackUrl` en hetzelfde event-type overschrijft de eerste en levert elk event eenmaal af |

Eis 0003 en 0004 landen op IS-OA-04, eis 0005 op de statusmelding die naast deze eenheid loopt.

## Operaties

Authenticatie op elk endpoint volgt de [auth-standaard](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/auth-standaard.md). Elke GET is alleen-lezen en geeft bij herhaling hetzelfde resultaat.

| Nr | Operatie | Pad of event, en wie het implementeert | Methode | Parameters | Statuscodes | Foutgedrag |
|---|---|---|---|---|---|---|
| O1 | Melden dat de specificatie planbaar is (I1) | `specificatie-planbaar`, meldpatroon op het planningssysteem | POST | de lading is de [specificatie-referentie](#bericht-1-specificatie-planbaar) | 200 | Blijft de bevestiging uit, dan opnieuw aanbieden met oplopende wachttijd (backoff) en daarna de wachtrij voor onbestelbare berichten (dead letter channel). Een dubbele aflevering blijft zonder effect op het event-id |
| O2 | De volledige structuur ophalen (I2) | `/onderwijsspecificaties/{id}`, op de onderwijscatalogus | GET | `versie`, optioneel, standaard de laatst gepubliceerde | 200, 400, 404 | HTTP-foutcode, de aanroeper bepaalt het herhalen |
| O3 | De wijziging ophalen (I2) | `/onderwijsspecificaties/{id}/delta`, op de onderwijscatalogus | GET | `van` en `naar`, beide een versie en beide verplicht | 200, 400, 404 | HTTP-foutcode. Het antwoord volgt JSON Patch (RFC 6902) |
| O4 | De ontvangst en de afkeur terugmelden (I3) | `verwerkingsstatus`, meldpatroon op de onderwijscatalogus | POST | de lading is de [verwerkingsstatus](#bericht-3-verwerkingsstatus) met status `ontvangen`, `gestart` of `afgekeurd` | 200 | Zoals O1. Een afgekeurde structuur komt langs deze weg terug, waarbij O2 beschikbaar blijft voor een nieuwe poging |
| O5 | Herstellen na een gemiste melding (I7) | `/onderwijsspecificaties`, op de onderwijscatalogus | GET | `status`, optioneel, standaard `gepubliceerd`. `gewijzigdSinds`, optioneel, een tijdstempel | 200, 400 | HTTP-foutcode. Bedoeld voor herstel, waarbij de reguliere stroom meldinggedreven blijft |
| O6 | Het afleveradres vastleggen (I8) | `/abonnementen`, op het planningssysteem | POST | de lading is het [abonnement](#bericht-4-abonnement) | 201, 400 | HTTP-foutcode. Idempotent op `callbackUrl` plus event-type: herregistratie overschrijft de vorige |

De validatiefout bij `afgekeurd` draagt geen veld in processing-status.json: werkbrief W8.

## Berichtspecificatie

Elk veld komt uit een schema in [Informatie-en-gegevensmodellen/schemas](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen/schemas). De objecttypen komen uit het [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md), met de definities in de [begrippenlijst](../begrippen/begrippenlijst.md).

### Bericht 1, specificatie-planbaar

Schema [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json). Dit bericht draagt het `Verzoek tot Aanbod / Intekening op specificatie`, met de referentie als enige inhoud ([U4](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u4-notify-then-pull)).

| Veld | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|
| `specificatieId` | string, uuid | 1 | ja | `Opleidingsprogramma specificatie`, de specificatie die planbaar is |
| `versie` | string | 1 | ja | idem |

### Bericht 2, de onderwijsspecificatiestructuur

Schema [education-specification.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-specification.json), met het [gebruiksprofiel](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md) voor deze koppeling.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|
| `onderwijsspecificaties` | array | 1..n | ja | de zeven specificatietypen uit de tabel hieronder |
| `regelsets` | array | 0..n | nee | `Student keuze regelset` |
| `leeruitkomsten` | array | 0 | nee | `Leeruitkomst`. Het gebruiksprofiel laat de inhoud bij de koppelingen die haar nodig hebben ([ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md)) |

Per element van `onderwijsspecificaties`:

| Veld | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|
| `id` | string, uuid | 1 | ja | het type dat `specificatieType` aanwijst |
| `specificatieType` | enum, 8 waarden | 1 | ja | idem |
| `versie` | string, patroon `n.n.n` | 1 | ja | idem |
| `bovenliggendSpecificatieId` | string, uuid of null | 1 | ja | de aggregatie tussen twee specificatietypen |
| `naam` | string | 1 | ja | het type dat `specificatieType` aanwijst |
| `studielast` | [volume.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/volume.json): `waarde` en `eenheid` SBU of EC | 1 | ja | idem |
| `leeruitkomstId` | string, uuid | 0..1 | nee | `Leeruitkomst`, als verbindende sleutel |
| `omschrijving`, `toelichting` | string | 0..1 | nee | het type dat `specificatieType` aanwijst |
| `status` | enum: concept, vastgesteld, gepubliceerd, gedeactiveerd, vervallen, gearchiveerd | 0..1 | nee | idem |
| `curriculumtype` | enum: nominaal, hybride, flexibel | 0..1 | nee | `Opleiding specificatie`, `Opleidingsprogramma specificatie` |
| `programmatype` | string, open lijst | 0..1 | nee | `Opleidingsprogramma specificatie` |
| `programmaLaag` | enum: leerweg, doelgroep | 0..1 | nee | idem |
| `leerweg` | enum: BOL, BBL | 0..1 | nee | idem |
| `doelgroep` | string, open lijst | 0..1 | nee | idem |
| `keuzedeelKlasse` | string, open lijst | 0..1 | nee | `Keuzedeel` |
| `cohort` | string | 0..1 | nee | `Cohort / periode` |
| `startdatum`, `geldigVanaf`, `geldigTot` | string, datum | 0..1 | nee | het type dat `specificatieType` aanwijst |
| `tijdsverdeling` | string, open lijst: BOT, OOT, BPV | 0..1 | nee | `Leeronderdeel specificatie` |
| `organisatie` | [organisation-unit.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/organisation-unit.json) | 0..1 | nee | `Organisatie-eenheid` |
| `regelsetVerwijzingen` | array van uuid | 0..n | nee | `Student keuze regelset` |
| `manifest` | array van [manifest-item.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/manifest-item.json): `specificatieId`, `versie`, `relatie` | 0..n | nee | legt per onderdeel de versie vast waarop de planning rust |

De waarden van `specificatieType` slaan terug op deze objecttypen:

| Waarde | Objecttype |
|---|---|
| `opleidingsspecificatie` | `Opleiding specificatie` |
| `opleidingsprogrammaspecificatie` | `Opleidingsprogramma specificatie`, en voor een keuzedeelprogramma `Keuzedeel` |
| `onderwijseenheidspecificatie` | `Onderwijseenheid specificatie` |
| `leeronderdeelspecificatie` | `Leeronderdeel specificatie` |
| `keuzedeelruimtespecificatie` | `Keuzedeelruimte` |
| `toetsonderdeelspecificatie` | `Toetsonderdeel specificatie` |
| `examenplanspecificatie` | `Examenplan`, dat buiten de kolommen van het informatiemodel staat |
| `resultaateenheidspecificatie` | geen objecttype: werkbrief W11 |

Per element van `regelsets`, schema [rule-set.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/rule-set.json):

| Veld | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|
| `id`, `versie`, `naam` | string, `id` als uuid | 1 | ja | `Student keuze regelset` |
| `omschrijving` | string | 0..1 | nee | idem |
| `vanToepassingOp` | string, uuid | 1 | ja | `Keuzedeelruimte`, de specificatie waarop de regelset geldt |
| `regels` | array van object | 1..n | ja | `Student keuze regelset`. De regelvorm staat open: werkbrief W9 |

### Bericht 3, verwerkingsstatus

Schema [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json). Binnen deze eenheid draagt het de waarden `ontvangen`, `gestart` en `afgekeurd`.

| Veld | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|
| `status` | enum: ontvangen, gestart, afgekeurd, gelukt, nietGelukt | 1 | ja | `Verzoek tot Aanbod / Intekening op specificatie` |
| `specificatieVerwijzing` | specification-reference.json | 1 | ja | `Opleidingsprogramma specificatie` |
| `opleidingsaanbodId` | string, uuid of null | 0..1 | nee | `Opleiding aanbod`, gevuld bij `gelukt` en daarmee de overgang naar IS-OA-04 |

### Bericht 4, abonnement

Schema [subscription.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/subscription.json). Dit bericht richt het kanaal in en vervalt zodra de aflevering over een bus of broker loopt ([U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal)).

| Veld | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|
| `callbackUrl` | string, uri | 1 | ja | geen: inrichting van de koppeling |
| `events` | array, enum: specificatie-planbaar, specificatie-gewijzigd, specificatie-status-gewijzigd, verwerkingsstatus | 1..n | ja | geen |
| `id` | string, uuid | 0..1 | toegekend in de respons | geen |

## Voorbeeldpayload

Casus Apothekersassistent, kwalificatiedossier crebo 23450, met de instantiewaarden uit beeld F2-03. De melding van O1:

```json
{
  "specificatieId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
  "versie": "2026.1.0"
}
```

Het antwoord van O2, met de opleiding, de programmalaag leerweg en de programmalaag doelgroep, de eenheid Blok B1-K1 met haar leeronderdelen, en de keuzedeelruimte uit F1-07 met de regelset waarnaar zij verwijst. De sleutels volgen de [voorbeeldpayloads](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) in Public, zodat elke uuid naar hetzelfde object wijst.

```json
{
  "onderwijsspecificaties": [
    {
      "id": "79736830-1c5c-470f-b2c2-005029c96733",
      "specificatieType": "opleidingsspecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": null,
      "leeruitkomstId": "c5b64fe5-f7bf-490c-acaf-7af1bd24f980",
      "naam": "Apothekersassistent",
      "omschrijving": "Opleiding tot apothekersassistent, kwalificatiedossier 23450, kwalificatie 27141.",
      "curriculumtype": "nominaal",
      "status": "gepubliceerd",
      "geldigVanaf": "2026-08-01",
      "geldigTot": null,
      "studielast": { "waarde": 4800, "eenheid": "SBU" },
      "manifest": [
        { "specificatieId": "5ef37812-ae0f-4232-904f-451b9928e45e", "versie": "2026.1.0", "relatie": "variant" }
      ]
    },
    {
      "id": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "specificatieType": "opleidingsprogrammaspecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": "79736830-1c5c-470f-b2c2-005029c96733",
      "leeruitkomstId": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "naam": "BOL voltijd",
      "programmatype": "diplomaprogramma",
      "programmaLaag": "leerweg",
      "leerweg": "BOL",
      "status": "gepubliceerd",
      "studielast": { "waarde": 4800, "eenheid": "SBU" },
      "manifest": [
        { "specificatieId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7", "versie": "2026.1.0", "relatie": "variant" }
      ]
    },
    {
      "id": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "specificatieType": "opleidingsprogrammaspecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "leeruitkomstId": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "naam": "Regulier BOL 2026",
      "programmatype": "diplomaprogramma",
      "programmaLaag": "doelgroep",
      "doelgroep": "regulier",
      "leerweg": "BOL",
      "curriculumtype": "nominaal",
      "cohort": "2026",
      "startdatum": "2026-09-01",
      "status": "gepubliceerd",
      "studielast": { "waarde": 4800, "eenheid": "SBU" },
      "manifest": [
        { "specificatieId": "402c2342-d897-4df4-a667-7fc5bd930944", "versie": "2026.1.0", "relatie": "onderdeel" },
        { "specificatieId": "fb5be5ae-faa0-4b4b-8085-474fce9aae08", "versie": "2026.1.0", "relatie": "onderdeel" }
      ]
    },
    {
      "id": "402c2342-d897-4df4-a667-7fc5bd930944",
      "specificatieType": "onderwijseenheidspecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "leeruitkomstId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "naam": "Blok B1-K1",
      "omschrijving": "Biedt farmaceutische patiëntenzorg, op kerntaakniveau.",
      "status": "gepubliceerd",
      "studielast": { "waarde": 2000, "eenheid": "SBU" },
      "manifest": [
        { "specificatieId": "327c8263-3516-4b5a-8d57-c16241ec008d", "versie": "2026.1.0", "relatie": "onderdeel" },
        { "specificatieId": "29522e42-fb32-46d2-a504-0869831f941f", "versie": "2026.1.0", "relatie": "onderdeel" }
      ]
    },
    {
      "id": "327c8263-3516-4b5a-8d57-c16241ec008d",
      "specificatieType": "leeronderdeelspecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": "402c2342-d897-4df4-a667-7fc5bd930944",
      "leeruitkomstId": "78f25d62-9fd4-45c4-aa04-3d22f59213f5",
      "naam": "Baliegesprekken 101",
      "status": "gepubliceerd",
      "tijdsverdeling": "BOT",
      "studielast": { "waarde": 600, "eenheid": "SBU" }
    },
    {
      "id": "29522e42-fb32-46d2-a504-0869831f941f",
      "specificatieType": "leeronderdeelspecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": "402c2342-d897-4df4-a667-7fc5bd930944",
      "leeruitkomstId": "0ffa279f-c595-49d7-b033-c91f66d18bb1",
      "naam": "Medicatiebewaking in de leerapotheek",
      "status": "gepubliceerd",
      "tijdsverdeling": "BOT",
      "studielast": { "waarde": 500, "eenheid": "SBU" }
    },
    {
      "id": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "specificatieType": "keuzedeelruimtespecificatie",
      "versie": "2026.1.0",
      "bovenliggendSpecificatieId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "naam": "Keuzedeelruimte",
      "status": "gepubliceerd",
      "studielast": { "waarde": 720, "eenheid": "SBU" },
      "regelsetVerwijzingen": ["e4037953-17d6-40a4-9e59-92ec1f9c19a8"]
    }
  ],
  "regelsets": [
    {
      "id": "e4037953-17d6-40a4-9e59-92ec1f9c19a8",
      "versie": "2026.1.0",
      "naam": "Kiesbare keuzedelen voor Apothekersassistent",
      "vanToepassingOp": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "regels": [
        {
          "type": "kiesbaar",
          "bereik": "alle keuzedelen met keuzedeelKlasse algemeen-verbredend"
        },
        {
          "type": "kiesbaar",
          "keuzedeel": "ecf4a1ce-8fe4-4ed2-82d4-6c743862094e",
          "voorwaardeVooraf": [
            { "vereisteLeeruitkomstId": "0d83e73a-e0d8-47de-8b83-983d2b8226e8", "status": "behaald" }
          ]
        }
      ]
    }
  ]
}
```

De tweede regel geeft de volgordebepaling waarop het planningssysteem plant: het keuzedeel is kiesbaar zodra de vereiste leeruitkomst behaald is, waarbij de sleutel volstaat en de inhoud bij de catalogus blijft. De sleutels binnen `regels` ontlenen hun vorm aan de voorbeeldpayloads in Public, waar rule-set.json een vrij object toestaat: werkbrief W9.

## Werkbrieven

Elke werkbrief noemt het veld of schema dat de beelden F2-01 en F2-03 vragen en dat de schema's in Public nog niet dragen, met de impact op het versienummer van het schema.

| Nr | Wat erbij moet | Waar | Versie-impact |
|---|---|---|---|
| W1 | Een eigen bericht voor het verzoek: een `verzoekId`, het aangevraagde cohort, het aanvraagmoment en de verwachte instroom. Het objecttype `Verzoek tot Aanbod / Intekening op specificatie` reist nu mee als een referentie van twee velden | nieuw schema `offering-request.json`, waar O1 naar verwijst | Minor: een nieuw schema naast specification-reference.json, dat in I7 en processing-status.json ongewijzigd blijft |
| W2 | De onderwijsvorm per leeronderdeel, in F2-03 "Simulatie in de leerapotheek, theorie ondersteunend". Het objecttype `Onderwijsvorm` staat in het informatiemodel | education-specification.json, veld `onderwijsvorm` op de leeronderdeelspecificatie | Minor: optioneel veld, bestaande implementaties blijven geldig |
| W3 | Het gevraagde type leeromgeving, in F2-03 "Balie-simulatie in het skillslab". Het objecttype `Onderwijslocatie type` bestaat, en location.json noemt alleen de concrete locatie aan de aanbodkant | education-specification.json, veld `onderwijslocatieType` op de leeronderdeelspecificatie | Minor: optioneel veld |
| W4 | Het gevraagde docentprofiel, in F2-03 "Apothekersassistent-docent met baliepraktijk". Het objecttype `Expertise of functieprofiel` bestaat zonder schema | nieuw schema voor het profiel, plus een veld erop in education-specification.json | Minor: een nieuw schema en een optioneel veld |
| W5 | De verdeling van begeleide en overige onderwijstijd in uren, in F2-01 "BOT 50 / OOT 50 SBU". `tijdsverdeling` draagt nu een enkele waarde uit een open lijst | education-specification.json, een array naast `tijdsverdeling` met per soort een [volume.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/volume.json) | Minor zolang `tijdsverdeling` blijft staan. Vervangen van dat veld wordt major |
| W6 | De gevraagde capaciteit en de gewenste groepsgrootte, in F2-01 op het programma en op de eenheid. `minAantalStudenten`, `maxAantalStudenten` en `groepen` liggen in education-offering.json, dat planning bezit | education-specification.json, velden `gevraagdeCapaciteit` en `gewensteGroepsgrootte` | Minor: optionele velden |
| W7 | Het tijdvenster per eenheid, de plek in de opleidingsduur uit F2-01. De specificatie draagt nu `startdatum`, `geldigVanaf` en `geldigTot`, die de geldigheid vastleggen | education-specification.json, veld `tijdvenster` met een verwijzing naar het bestaande [period.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/period.json) | Minor: optioneel veld op een bestaand schema |
| W8 | Het foutmodel bij status `afgekeurd`, dat het interactieoverzicht wel belooft. processing-status.json draagt status, aanbodreferentie en specificatieverwijzing | processing-status.json, veld `fouten` met een code en een omschrijving, naar het model van [bottleneck.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/bottleneck.json) | Minor: optioneel veld, met een eigen codelijst voor validatiefouten |
| W9 | De regelvorm. `regels` is een array van vrije objecten, terwijl de sleutels die de volgordebepaling van eis 0001 dragen (`type`, `bereik`, `keuzedeel`, `voorwaardeVooraf` met daarin `vereisteLeeruitkomstId` en `status`) hun vorm alleen aan de voorbeeldpayloads in Public ontlenen | rule-set.json, de regelvormen als benoemde varianten in `$defs` | Minor als de varianten naast de vrije vorm komen. Dichtzetten van `regels` wordt major |
| W10 | De container voor inhoudelijk geclusterde leeronderdelen, de gewenste leergelegenheid uit bevinding B06 en B07. `leergelegenheid` bestaat nu als `aanbodType` in education-offering.json | education-specification.json, een waarde in de enum `specificatieType` | Minor voor de verzender. Een ontvanger die de enum streng valideert ziet een brekende wijziging, dus met een conformiteitstoets (conformance test) erbij |
| W11 | Een objecttype of een definitie bij de enumwaarde `resultaateenheidspecificatie`, die in het informatiemodel geen tegenhanger heeft | informatiemodel OKx, of de waarde uit education-specification.json | Major zodra de waarde vervalt, omdat een bestaande payload dan afkeurt |
| W12 | Een afspraak over het versieformaat. education-specification.json eist het patroon `n.n.n`, beeld F2-03 noteert "versie 2026.1" en specification-reference.json laat `versie` een vrije tekenreeks | beide schema's, met een patroon dat de instellingspraktijk dekt | Minor bij het verruimen van het patroon. Dichtzetten van specification-reference.json wordt major |

Wat deze werkbrieven open laten: de clustering uit bevinding B02, B06 en B07 raakt zowel de specificatiekant als de aanbodkant, en het besluit daarover gaat voor op W10.
