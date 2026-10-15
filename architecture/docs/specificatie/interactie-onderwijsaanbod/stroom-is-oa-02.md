# IS-OA-02: het onderwijs- en examenontwerp naar de onderwijscatalogus

Deze eenheid levert de uitvoeringskenmerken van het ontwerp aan de onderwijscatalogus: de onderwijsvorm, het ruimtetype, de expertiseprofielen van docent en examinator, de verdeling van de studiebelasting, de toetsvorm en het toetsinstrument, elk als veld op de specificatie die [IS-OA-01](README.md#de-kiesbare-eenheden) al draagt.

## De eenheid

| | |
|---|---|
| Bronsysteem | Curriculum ontwerptool, applicatiedienst `Curriculum ontwerp` |
| Doelsysteem | Onderwijscatalogus |
| Koppeling | Curriculum ontwerptool naar onderwijscatalogus. De [dienstpagina van de ontwerptool](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/curriculum-ontwerptool.md) laat de endpoints aan een volgend pakket, [ADR 0020](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md) legt de richting vast |
| Beeld | [F1-13, het onderwijs- en examenontwerp mee naar de catalogus](../../../model/informatiemodel/img/regels/f1-13-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat.svg), van de conceptplaat Onderwijsontwerp |
| Status | Voorstel. Elke regel achter F1-13 draagt een aanname, en de objecttypen komen van de conceptplaat ([voorbeeld-lr1-regels.json](../../../model/informatiemodel/voorbeeld-lr1-regels.json)) |
| Applicatiedienst | `Onderwijs beheer` van de onderwijscatalogus neemt de lading aan, gevoed door `Curriculum ontwerp` van de ontwerptool ([componenten.json](../../../model/informatiemodel/componenten.json)) |
| Sleuteltaal | De sleutels in de payload zijn Engels, zoals de schema's in Public ze dragen; [mapping.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/mapping.md) legt per schema de Nederlandse naam ernaast. Enumwaarden blijven Nederlands. Een sleutel uit een werkbrief draagt daar haar voorgestelde Engelse naam |
| Toetsbare eis | De ontwerptool levert per onderwijseenheid- en leeronderdeelspecificatie de sleutels uit [de berichtspecificatie](#de-berichtspecificatie) over [de operaties](#de-operaties), en de catalogus neemt ze onveranderd over met O2 en O3. De sleutels `educationForm`, `roomType`, `expertiseProfileIds`, `timeDistributions` en `assessmentInstrumentId` rusten op WB-01 tot en met WB-06, de paden van O2 en O3 op WB-07; de eis is af te dwingen zodra die werkbrieven vastliggen |

![Beeld F1-13: het onderwijs- en examenontwerp mee naar de catalogus](../../../model/informatiemodel/img/regels/f1-13-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat.svg)

Dezelfde waarden gaan in [F2-03](../../../model/informatiemodel/img/regels/f2-03-verzoek-met-specificatiestructuur-en-planbare-waarden-naar-planning.svg) door naar planning, en de knelpuntcodes `expertiseTekort` en `ruimteTekort` uit de [regels bij de schema's](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/regels.md) veronderstellen ze. Daarom landen zij hier als veld op de specificatie.

## De stroom

```mermaid
sequenceDiagram
    autonumber
    participant CO as Curriculum ontwerptool
    participant OC as Onderwijscatalogus

    Note over CO: De ontwerper legt vorm, ruimte, mensen en middelen<br/>vast bij de eenheid en bij de toets
    CO-)OC: O1 [ontwerp-gereed] melding met de verwijzing naar de specificatie
    OC->>CO: O2 [GET /onderwijsspecificaties/{id}] het ontwerp ophalen
    CO-->>OC: 200 momentopname met de ontwerpvelden
    OC->>CO: O3 [GET /examenplanspecificaties/{id}] de toetskant ophalen
    CO-->>OC: 200 toetsvorm, instrument en examinatorprofiel
    alt Waarden binnen de lijst
        OC-)CO: O4 [verwerkingsstatus] status gelukt, met specificationReference
    else Waarde buiten de lijst of sleutel uit een werkbrief
        OC-)CO: O4 [verwerkingsstatus] status afgekeurd, met de geschonden regel
    end
    Note over CO: De vorm of het instrument wijzigt
    CO-)OC: O1 [ontwerp-gereed] nieuwe versie, changeClass niet-brekend
    OC->>CO: O2 [GET /onderwijsspecificaties/{id}] de nieuwe versie ophalen
```

## De operaties

Deze lading rijdt mee op de operaties van dezelfde koppeling, die [IS-OA-01](README.md#de-kiesbare-eenheden) voluit beschrijft: de ontwerptool houdt het ontwerp in bewerking vast en meldt dat het gereed is, waarna de catalogus het ophaalt ([U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap) en [U4](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u4-notify-then-pull)). Hieronder staat wat elke operatie voor deze lading draagt. Authenticatie per operatie volgt de [auth-standaard](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/auth-standaard.md).

| Nr | Pad of meldpatroon (webhook), en waar het staat | Methode | Parameters | Statuscodes | Foutgedrag | Grond |
|---|---|---|---|---|---|---|
| O1 | `ontwerp-gereed` op OC | POST | geen | 200 | Bevestiging met 200. Zonder bevestiging herhaalt de melder met oplopende wachttijd (backoff) en daarna via de wachtrij voor onbestelbare berichten (dead letter channel). Een herhaald event blijft zonder extra effect door het event-id ([ADR 0018](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md)) | WB-07, ADR 0020 (melden dat het ontwerp gereed is) |
| O2 | `/onderwijsspecificaties/{id}` op CO, met het schema in Public bij de [onderwijscatalogus](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md), die het gelijknamige pad zelf bezit; WB-07 kiest het voorvoegsel per bezitter | GET | `versie` (optioneel, standaard de laatst vastgestelde) | 200, 400, 404 | Alleen-lezen en zonder neveneffect. 404 bij een onbekend id, 400 bij een onbekende versie. De wijziging staat als delta op `/onderwijsspecificaties/{id}/delta` ([U11](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u11-toekomstvaste-endpoints-volledige-structuur-en-delta)) | WB-07 voor het pad op CO en het gebruiksprofiel |
| O3 | `/examenplanspecificaties/{id}` op CO, met het schema in Public bij de onderwijscatalogus, die het gelijknamige pad zelf bezit | GET | `versie` (optioneel, standaard de laatst vastgestelde) | 200, 400, 404 | Als O2 | WB-07 voor het pad op CO |
| O4 | `verwerkingsstatus` op CO, payload [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json) met `programmeOfferingId` (opleidingsaanbodId) op `null`, want deze eenheid meldt op een specificatie | POST | geen | 200 | `afgekeurd` draagt de geschonden regel met het veld en de waarde die de controle raakte, waarna de vorige versie blijft staan. Herhaling als O1 | WB-07, ADR 0020 (statusfeedback) |

Deze operaties staan als voorstel: ADR 0020 vraagt operaties voor aanleggen, uitwerken, publiceren en wijzigen met statusfeedback naar de ontwerptool, en legt het publicatiebesluit bij de catalogus.

## De berichtspecificatie

Waar de lading van F1-13 landt, van de conceptplaat naar het [informatiemodel](../../../model/informatiemodel/informatiemodel.md) en het schema:

| Objecttype op de conceptplaat | Objecttype in het informatiemodel | Sleutel in de payload | Nederlandse naam | Vervolg |
|---|---|---|---|---|
| `Onderwijsvorm specificatie` | `Onderwijsvorm` (ontwerpkeuze 18, voorstel) | `explanation` draagt de leesbare vorm | toelichting | WB-01 voor het gecodeerde veld |
| `Gewenste Onderwijskundige Leeromgeving` | `Onderwijslocatie type` (OEAPI `roomType`) | `roomType`, voorgesteld bij WB-02 | onderwijslocatieType | WB-02 |
| `Gewenst medewerker competentieprofiel` | `Expertise of functieprofiel` | `expertiseProfiles`, voorgesteld bij WB-03 | expertiseprofielen | WB-03, WB-04 |
| `Studiebelasting en begeleide onderwijstijd indicatie` | attribuut van de specificatie | `studyLoad`, `timeDistribution` | studielast, tijdsverdeling | WB-05 voor de verdeling per deel |
| `Toetsvormspecificatie` | `Toetsonderdeel specificatie` | `assessmentForm` in result-structure.json | toetsvorm | aanwezig |
| `Toetsinstrument`, een `Collectie van Leermiddelgroepen` | zonder objecttype | `assessmentInstrumentId`, voorgesteld bij WB-06 | toetsinstrumentId | WB-06 |

### Bericht 1: de ontwerpvelden op de onderwijsspecificatie

Per onderwijseenheid- of leeronderdeelspecificatie in [education-specification.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-specification.json).

| Veld | Nederlandse naam | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|---|
| `educationForm` | onderwijsvorm | string, open lijst | 0..1 | nee | `Onderwijsvorm` | WB-01, F1-13 |
| `roomType` | onderwijslocatieType | string, open lijst | 0..1 | nee | `Onderwijslocatie type` | WB-02, F1-13 |
| `expertiseProfileIds` | expertiseprofielIds | array van uuid | 0..n | nee | `Expertise of functieprofiel` | WB-04, F1-13 |
| `studyLoad` | studielast | object, [volume.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/volume.json) | 1..1 | ja | attribuut van de specificatie | education-specification.json |
| `timeDistribution` | tijdsverdeling | string, open lijst BOT, OOT, BPV | 0..1 | nee | attribuut van de specificatie | education-specification.json |
| `timeDistributions` | tijdsverdelingen | array van object met `timeDistribution` en `volume` | 0..n | nee | attribuut van de specificatie | WB-05, F1-13 en F2-01 |
| `explanation` | toelichting | string | 0..1 | nee | attribuut van de specificatie | education-specification.json |

### Bericht 2: de ontwerpvelden op het toetsonderdeel

Per toetsonderdeelspecificatie in [result-structure.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/result-structure.json).

| Veld | Nederlandse naam | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|---|
| `assessmentForm` | toetsvorm | string, open lijst | 0..1 | nee | `Toetsonderdeel specificatie` | result-structure.json |
| `roomType` | onderwijslocatieType | string, open lijst | 0..1 | nee | `Onderwijslocatie type` | WB-02, F1-13 |
| `assessmentInstrumentId` | toetsinstrumentId | uuid | 0..1 | nee | `Toetsinstrument`, conceptplaat | WB-06, F1-13 |
| `expertiseProfileIds` | expertiseprofielIds | array van uuid | 0..n | nee | `Expertise of functieprofiel` | WB-04, F1-13 |

### Bericht 3: het expertiseprofiel en het toetsinstrument

Beide staan als eigen array naast `educationSpecifications`, net als `ruleSets` in beide schema's.

| Veld | Nederlandse naam | Type | Kardinaliteit | Verplicht | Objecttype | Grond |
|---|---|---|---|---|---|---|
| `expertiseProfiles[].id` | expertiseprofielen[].id | uuid | 1..1 | ja | `Expertise of functieprofiel` | WB-03, [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) |
| `expertiseProfiles[].name` | expertiseprofielen[].naam | string | 1..1 | ja | `Expertise of functieprofiel` | WB-03, F1-13 |
| `expertiseProfiles[].role` | expertiseprofielen[].rol | string, open lijst docent, examinator, praktijkbegeleider | 0..1 | nee | `Expertise of functieprofiel` | WB-03, F1-13 |
| `expertiseProfiles[].competences` | expertiseprofielen[].competenties | array van string | 0..n | nee | `Competenties / Skills`, scope buiten | WB-03, F1-06 |
| `assessmentInstruments[].id` | toetsinstrumenten[].id | uuid | 1..1 | ja | `Toetsinstrument`, conceptplaat | WB-06, [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) |
| `assessmentInstruments[].name` | toetsinstrumenten[].naam | string | 1..1 | ja | `Toetsinstrument`, conceptplaat | WB-06, F1-13 |

## Voorbeeldpayload

Casus Apothekersassistent, kwalificatiedossier 23450, met de instantiewaarden uit F1-13. De uuid's van de specificaties komen uit de [voorbeeldpayloads](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md), de namen uit het beeld, en de profielen en het instrument dragen een voorbeeld-uuid. De ontwerpvelden komen additief bovenop de grofmazige specificatie van IS-OA-01, dus loopt de versie van `0.1.0` naar `0.2.0`.

De specificatiekant, het antwoord op O2:

```json
{
  "educationSpecifications": [
    {
      "id": "402c2342-d897-4df4-a667-7fc5bd930944",
      "specificationType": "onderwijseenheidspecificatie",
      "version": "0.2.0",
      "parentSpecificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "learningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "name": "Blok B1-K1, biedt farmaceutische patientenzorg",
      "studyLoad": { "value": 2000, "unit": "SBU" },
      "educationForm": "simulatie",
      "roomType": "skillslab",
      "expertiseProfileIds": ["8e1dcda7-ef4e-45d0-931a-e47c3c77ddef"],
      "explanation": "Simulatie in de leerapotheek, theorie ondersteunend"
    },
    {
      "id": "327c8263-3516-4b5a-8d57-c16241ec008d",
      "specificationType": "leeronderdeelspecificatie",
      "version": "0.2.0",
      "parentSpecificationId": "402c2342-d897-4df4-a667-7fc5bd930944",
      "learningOutcomeId": "78f25d62-9fd4-45c4-aa04-3d22f59213f5",
      "name": "Baliegesprekken 101",
      "studyLoad": { "value": 600, "unit": "SBU" },
      "timeDistributions": [
        { "timeDistribution": "BOT", "volume": { "value": 300, "unit": "SBU" } },
        { "timeDistribution": "OOT", "volume": { "value": 300, "unit": "SBU" } }
      ],
      "educationForm": "simulatie",
      "roomType": "skillslab",
      "expertiseProfileIds": ["8e1dcda7-ef4e-45d0-931a-e47c3c77ddef"],
      "explanation": "Balie-simulatie in het skillslab, theorie ondersteunend"
    }
  ],
  "expertiseProfiles": [
    {
      "id": "8e1dcda7-ef4e-45d0-931a-e47c3c77ddef",
      "name": "Apothekersassistent-docent met baliepraktijk",
      "role": "docent",
      "competences": [
        "didactische en communicatieve vaardigheden (CompetentNL laag 2)",
        "farmacie (ISCED-F 0916)"
      ]
    }
  ]
}
```

De toetskant, het antwoord op O3:

```json
{
  "educationSpecifications": [
    {
      "id": "941f180d-b0af-4933-a580-6ab654dfadda",
      "specificationType": "toetsonderdeelspecificatie",
      "version": "0.2.0",
      "parentSpecificationId": "0512c773-9c1b-42c4-ae0d-9af8554f2462",
      "learningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "learningOutcome": { "type": "kerntaak", "code": "B1-K1" },
      "name": "Proeve van bekwaamheid farmaceutische patientenzorg",
      "nature": "summatief",
      "assessmentForm": "proeveVanBekwaamheid",
      "weighting": 2,
      "resultModel": { "scale": "cijfer-1-10", "passMark": 5.5, "decimalPlaces": 1 },
      "mandatory": true,
      "status": "concept",
      "roomType": "skillslab",
      "assessmentInstrumentId": "da138f60-ebb1-4853-870f-7e7d642873f2",
      "expertiseProfileIds": ["4037f1a2-c182-4f2d-ae00-bfb06b076337"],
      "description": "Proeve van bekwaamheid in de simulatieapotheek"
    }
  ],
  "expertiseProfiles": [
    {
      "id": "4037f1a2-c182-4f2d-ae00-bfb06b076337",
      "name": "Examinator met baliepraktijk en toetsbekwaamheid",
      "role": "examinator",
      "competences": ["farmacie (ISCED-F 0916)", "toetsbekwaamheid"]
    }
  ],
  "assessmentInstruments": [
    {
      "id": "da138f60-ebb1-4853-870f-7e7d642873f2",
      "name": "Beoordelingsformulier met rubric"
    }
  ]
}
```

## De werkbrieven

De versie-impact volgt de versionering uit de [regels bij de schema's](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/regels.md): een additief veld is MINOR, en een wijziging van de uitvoeringsvorm draagt `changeClass` (wijzigingsklasse) `niet-brekend`. Elke sleutel die een werkbrief voorstelt draagt haar Engelse naam hier, in de vorm die [mapping.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/mapping.md) per schema aanhoudt.

| Nr | Wat erbij komt | Waar | Versie-impact | Grond |
|---|---|---|---|---|
| WB-01 | Veld `educationForm` (onderwijsvorm), naam voorgesteld in deze werkbrief, string uit een open lijst met simulatie, theorie, praktijk, beroepspraktijkvorming en zelfstudie | education-specification.json | Additief optioneel veld, MINOR op het releasepakket | F1-13 en F2-03 dragen `Onderwijsvorm specificatie`, het informatiemodel kent `Onderwijsvorm` als voorstel en de [begrippenlijst](../begrippen/begrippenlijst.md) houdt het zonder definitie |
| WB-02 | Veld `roomType` (onderwijslocatieType), de OEAPI-naam die het informatiemodel bij `Onderwijslocatie type` draagt, string uit een open lijst per ruimtesoort. F1-13 noemt het skillslab, F2-01 de praktijkruimte, dus beide krijgen een eigen waarde | education-specification.json en result-structure.json | Additief optioneel veld, MINOR | Knelpuntcode `ruimteTekort` veronderstelt het ruimtetype, `Onderwijslocatie type` staat zonder definitie |
| WB-03 | Schema voor het expertiseprofiel met `id`, `name`, `role` en `competences`, plus de array `expertiseProfiles` naast `ruleSets` in beide payloads; de Engelse namen zijn in deze werkbrief voorgesteld | nieuw bestand in [schemas/](https://github.com/Npuls-OKx/Public/tree/dev/Informatie-en-gegevensmodellen/schemas) | Nieuw schema met een additieve array, MINOR | Knelpuntcode `expertiseTekort` veronderstelt het profiel, `Expertise of functieprofiel` aggregeert `Competenties / Skills` en staat zonder definitie |
| WB-04 | Veld `expertiseProfileIds` (expertiseprofielIds), naam voorgesteld in deze werkbrief, array van uuid | education-specification.json en result-structure.json | Additief optioneel veld, MINOR | F1-13 hangt `Gewenst medewerker competentieprofiel` aan de onderwijsvorm en aan de toetsvorm |
| WB-05 | Veld `timeDistributions` (tijdsverdelingen), naam voorgesteld in deze werkbrief, array van `timeDistribution` met `volume` uit volume.json, naast het bestaande enkelvoudige `timeDistribution` | education-specification.json | Additief optioneel veld, MINOR. Het enkelvoudige veld blijft geldig zolang de koppeling open staat | F1-13 en F2-01 noemen BOT 50 en OOT 50 SBU, een verdeling over delen, waar het schema vandaag een waarde draagt |
| WB-06 | Veld `assessmentInstrumentId` (toetsinstrumentId) plus de plek van het instrument zelf: een eigen schema met de array `assessmentInstruments`, of de leermiddelkoppeling-payload; de Engelse namen zijn in deze werkbrief voorgesteld | result-structure.json, en het besluit over de leermiddelkoppeling-payload | Nieuw schema met een additief veld, MINOR. De route via de leermiddelkoppeling raakt het meldpatroon `leermiddelkoppeling-beschikbaar` op de catalogus | F1-13 draagt `Toetsinstrument` als `Collectie van Leermiddelgroepen`, het informatiemodel kent dat objecttype als voorstel van de conceptplaat en de leermiddelkoppeling-payload staat open |
| WB-07 | De meldpatronen O1 en O4, de paden van O2 en O3 op de ontwerptool met een voorvoegsel per bezitter naast het gelijknamige pad van de catalogus, en het gebruiksprofiel van deze koppeling: welk deel van de payload over O2 en O3 meekomt | [curriculum-ontwerptool.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/curriculum-ontwerptool.md) en [onderwijscatalogus.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md), plus [gebruiksprofielen.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md) | Nieuwe endpoints en een nieuw profiel, MINOR op het koppelvlakpakket | ADR 0020 vraagt operaties voor aanleggen, uitwerken, publiceren en wijzigen met statusfeedback naar de ontwerptool |
| WB-08 | Toetskenmerken naast de toetsvorm: `assessmentMode` (afnamevorm), `assessmentDuration` (toetsduur), `permittedResources` (hulpmiddelen) en `attemptCount` (aantal pogingen), alle namen voorgesteld in deze werkbrief | result-structure.json | Additieve optionele velden, MINOR | Bevinding B04 bij F1-09 van de leverancierslezing, issue 283 |
| WB-09 | Het besluit op welk niveau `educationForm` landt: de leeronderdeelspecificatie, of de gewenste leergelegenheid die de catalogus uit geclusterde leeronderdelen vormt | education-specification.json, samen met WB-01 | Zolang WB-01 open staat kost het verschuiven van het niveau niets; na vaststelling is het MAJOR voor de afnemer | Bevinding B06 bij F2-01 legt het rijpheidskenmerk planbaar op de gewenste leergelegenheid en het inhoudelijk clusteren bij de catalogus, issue 284 |
| WB-10 | De waarde `ontwerp-gereed` in de lijst waarop een partij zich abonneert | [subscription.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/subscription.json), eigenschap `events` | Waarden toevoegen aan een gesloten lijst: additief voor de abonnee en brekend voor wie erop valideert, MAJOR | De enum draagt vandaag `verwerkingsstatus` voor de terugmelding op O4, en O1 vraagt een eigen waarde om in te richten |

Alle overige lading van fase 1, van de leeruitkomst tot de resultaatstructuur, draagt [IS-OA-01](README.md#de-kiesbare-eenheden).
