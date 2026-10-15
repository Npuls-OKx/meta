# IS-OA-01: het ontworpen onderwijs naar de onderwijscatalogus

De curriculum ontwerptool levert de onderwijscatalogus het vastgestelde ontwerp van een opleiding: de leeruitkomsten, de specificatiestructuur tot leeronderdeel met de keuzedeelruimte en haar keuzeregels, en de resultaatstructuur met de toets- en examenonderdelen, alles verankerd op de leeruitkomst.

De uuid's, de versies en de namen in de voorbeeldpayloads hieronder komen uit [casus.md](casus.md), de vaste identificaties van deze interactiespecificatie.

## 1. De eenheid

| Bronsysteem | Doelsysteem | Koppeling | Beeld | Status | Applicatiedienst |
|---|---|---|---|---|---|
| Curriculum ontwerptool | Onderwijscatalogus | volgt, [S5](README.md#signaleringen-en-openstaande-punten) | [F1-12](../../../model/informatiemodel/img/regels/f1-12-de-opleiding-zoals-ontworpen-naar-de-catalogus.svg) | Voorstel: hoofdplaat v1.7 laat het ontwerpen binnen de catalogus vallen, en een interactiepatroon voor deze lijn volgt | [onderwijsspecificatie-inname](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/onderwijsspecificatie-inname-aanbieder.md): de ontwerptool levert, de catalogus neemt in |

De dienst legt de rolverdeling vast.

| Component | Wat zij doet | In het ArchiMate-model |
|---|---|---|
| Onderwijscatalogus | De vorm valideren, toetsen of de studielast van onderliggende delen optelt naar het bovenliggende niveau, de opname bevestigen of afkeuren met een reden, en de opgenomen specificatie een eigen identiteit en versie toekennen | `Onderwijsspecificatie uitwerking` |
| Curriculum ontwerptool | Aanleveren, de uitkomst verwerken, en de toegekende identiteit en versie voortaan als verwijzing gebruiken | `Curriculum ontwerp` |

| Grond | Wat zij voor deze eenheid vastlegt |
|---|---|
| [ADR 0020](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md) | De ontwerptool zoekt hergebruik op leeruitkomst, de catalogus beslist over publicatie, de ontwerptool krijgt statusterugkoppeling |
| [U3](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u3-resource-eigenaarschap) | De ontwerptool bezit het ontwerp in bewerking, de catalogus de opgenomen onderwijsspecificatie |
| [U4](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u4-notify-then-pull) | De uitkomst en de statuswijziging komen als dunne melding met een verwijzing terug |
| [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) | Platte arrays met een ouder-verwijzing, sleutelvelden met een naam die de richting zegt |
| [U11](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u11-toekomstvaste-endpoints-volledige-structuur-en-delta) | Naast de volledige structuur staat de delta op dezelfde resource |
| [Ontwerpkeuze 1](../../../model/informatiemodel/informatiemodel.md#ontwerpkeuzes) | Elk geleverd objecttype verwijst naar de leeruitkomst |
| [Beeldregels F1-12](../../../model/informatiemodel/voorbeeld-lr1-regels.json) | De objecttypen en instanties die deze stroom draagt |

## 2. De stroom in beeld

```mermaid
sequenceDiagram
    autonumber
    participant CO as Curriculum ontwerptool
    participant OC as Onderwijscatalogus

    Note over CO,OC: beide partijen hebben hun afleveradres vastgelegd (O7)
    CO->>OC: O1 [GET /onderwijsspecificaties] herbruikbare specificaties zoeken
    OC-->>CO: lijst met verwijzingen, de structuur per id via O2
    Note over CO: de ontwerper vult aan wat ontbreekt,<br/>de examencommissie stelt het examenplan vast
    CO->>OC: O3 [POST /onderwijsspecificaties] leeruitkomsten, specificatiestructuur, regelsets
    OC-->>CO: 202, de inname is gestart
    CO->>OC: O4 [POST /examenplanspecificaties] examenplan, resultaateenheden, toetsonderdelen
    OC-->>CO: 202, de inname is gestart
    alt vorm geldig en studielast telt op
        OC-)CO: O5 [verwerkingsstatus] gelukt, met de toegekende identiteit en versie
        OC-)CO: O6 [specificatie-status-gewijzigd] vastgesteld naar gepubliceerd
    else vorm ongeldig of studielast telt niet op
        OC-)CO: O5 [verwerkingsstatus] afgekeurd, met de reden
    end
```

Afkeuring is een geldige uitkomst van de inname: de catalogus meldt haar op O5 met de reden erbij, en het kanaal blijft staan. De ontwerptool stelt haar eigen beeld bij op een terminale uitkomst: gelukt, niet gelukt of afgekeurd.

## 3. De operaties

`CO` is de curriculum ontwerptool, `OC` de onderwijscatalogus. De dienstpagina's staan in [Applicatiediensten](https://github.com/Npuls-OKx/Public/tree/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten) op het vastgezette commit `d0c20d9` van de branch `feature/restructure-and-versioning`; die map staat nog niet op `dev`, en signalering [S12](README.md#signaleringen-en-openstaande-punten) belegt welke branch normatief is.

| Nr | Operatie | Dienst | Richting | Pad of melding | Methode | Stand |
|---|---|---|---|---|---|---|
| O1 | Herbruikbare specificaties zoeken | onderwijsspecificatiestructuur-aanbieder | CO vraagt OC | `/onderwijsspecificaties` | GET | In Public, filter op leeruitkomst via W3 |
| O2 | Een herbruikbare structuur ophalen | onderwijsspecificatiestructuur-aanbieder | CO vraagt OC | `/onderwijsspecificaties/{id}` | GET | In Public |
| O3 | Het ontwerp aanleveren | onderwijsspecificatie-inname | CO levert OC | voorstel `/onderwijsspecificaties` | POST | W1 |
| O4 | De resultaatstructuur aanleveren | onderwijsspecificatie-inname | CO levert OC | voorstel `/examenplanspecificaties` | POST | W1 |
| O5 | De uitkomst van de inname melden | verwerkingsstatus | OC meldt CO | `verwerkingsstatus` | POST | Schema in Public, endpoint op CO via W2 |
| O6 | Een statuswijziging melden | onderwijsspecificatiestructuur-aanbieder | OC meldt CO | `specificatie-status-gewijzigd` | POST | Schema en eventwaarde in Public, endpoint op CO via W2 |
| O7 | Het afleveradres vastleggen | afleverabonnement-aanbieder | over en weer | `/abonnementen` | POST | In Public op OC, op CO via W2 |

Parameters, statuscodes en foutgedrag. De GET-operaties zijn alleen-lezen: herhaald aanroepen levert hetzelfde resultaat.

| Nr | Parameters | Statuscodes | Foutgedrag |
|---|---|---|---|
| O1 | `status` (optioneel, standaard `gepubliceerd`), `gewijzigdSinds` (optioneel, tijdstempel), `leeruitkomstId` (voorstel, W3) | 200, 400 | HTTP-foutcode, de aanroeper bepaalt de herhaling |
| O2 | `versie` (optioneel, standaard de laatst gepubliceerde) | 200, 400, 404 | 404 bij een onbekend id, 400 bij een onbekende versie. De delta staat op `/onderwijsspecificaties/{id}/delta` met `van` en `naar`, beide verplicht |
| O3 | geen | 202, 400, 409 | 202 bij een aangenomen structuur: het oordeel volgt als uitkomst op O5. 400 bij een vorm die het schema schendt, 409 bij een herhaalde aanlevering van dezelfde ontwerpversie (W1) |
| O4 | geen | 202, 400, 409 | Als O3. De resultaatstructuur verwijst met `appliesTo` naar een opgenomen opleidingsprogrammaspecificatie, dus O3 gaat voor |
| O5 | geen | 200 | `afgekeurd` draagt de reden, bijvoorbeeld studielast die niet optelt. De ontvanger bevestigt met 200. Zonder bevestiging herhaalt de melder met oplopende wachttijd (backoff) en daarna via de wachtrij voor onbestelbare berichten (dead letter channel). Een herhaald bericht heeft geen extra effect: de ontvanger herkent het `eventId` (W12) |
| O6 | geen | 200 | Als O5 |
| O7 | geen | 201, 400 | Herhaalbaar zonder extra effect (idempotent) op afleveradres plus soort melding: een herhaalde registratie overschrijft de vorige |

De ontwerptool abonneert zich op de meldingen die zij ontvangt: `verwerkingsstatus` en `specificatie-status-gewijzigd`, de waarden die [subscription.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/subscription.json) kent. De dienstenlijst op het vastgezette commit draagt de eerste als [verwerkingsuitkomst-aanbieder](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/verwerkingsuitkomst-aanbieder.md); signalering [S14](README.md#signaleringen-en-openstaande-punten) belegt een naam per bericht. De volgorde per `specificationId` blijft behouden, en het kanaal is vrij binnen de eigenschappen van [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal):

- gegarandeerde aflevering
- herhaalbare verwerking zonder extra effect (idempotent)
- een wachtrij voor onbestelbare berichten (dead letter channel)
- volgorde per sleutel

## 4. De berichten

De kolom Veld draagt de Engelse sleutel uit het schema, de kolom Nederlands de naam waaronder [mapping.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/mapping.md) hem vastlegt; enumwaarden blijven Nederlands. Kardinaliteit en verplichting gelden voor deze stroom. Een afwijking van het schema staat in de kolom Verplicht met de werkbrief erbij.

### 4.1 De uitkomst van de inname (O5)

Volgt [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json).

| Veld | Nederlands | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|---|
| `status` | `status` | enum `ontvangen`, `gestart`, `afgekeurd`, `gelukt`, `nietGelukt` | 1 | ja | de toestand van de inname |
| `specificationReference` | `specificatieVerwijzing` | object: `specificationId`, `version` | 1 | ja | `Opleiding specificatie`, met de identiteit en versie die de catalogus toekent (W4) |
| `programmeOfferingId` | `opleidingsaanbodId` | uuid of null | 0..1 | nee, leeg in deze stroom | `Opleiding aanbod`, gevuld in IS-OA-04 |
| `eventId` | `eventId` | uuid | 0..1 | nee, voorgestelde sleutel bij W12 | kanaaleigenschap, geen objecttype |

De reden bij `afgekeurd` en `nietGelukt` krijgt haar vorm in het innamecontract (W1).

### 4.2 De statusmelding (O6)

Volgt [specification-status-changed.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-status-changed.json).

| Veld | Nederlands | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|---|
| `objectId` | `objectId` | uuid | 1 | ja | `Opleiding specificatie`, de wortel van de opgenomen structuur |
| `oldStatus` | `oudeStatus` | enum | 1 | ja | `Opleiding specificatie`, `vastgesteld` bij opname |
| `newStatus` | `nieuweStatus` | enum | 1 | ja | `Opleiding specificatie`, `gepubliceerd` zodra de catalogus publiceert |
| `eventId` | `eventId` | uuid | 0..1 | nee, voorgestelde sleutel bij W12 | kanaaleigenschap, geen objecttype |

### 4.3 Het ontwerp (O3), leeruitkomsten

Volgt [learning-outcome.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/learning-outcome.json).

| Veld | Nederlands | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|---|
| `id` | `id` | uuid | 1 | ja | `Leeruitkomst` |
| `version` | `versie` | string, semver | 1 | ja | `Leeruitkomst` |
| `name` | `naam` | string | 1 | ja | `Leeruitkomst`, in de stem van de instelling |
| `source` | `bron` | object: `standard`, `type`, `code` | 1 | ja | `Kwalificatie dossier`, `Kwalificatie`, `Kerntaak`, `Werkproces`, `Keuzedeel`, via het `type` |
| `parentLearningOutcomeId` | `bovenliggendLeeruitkomstId` | uuid of null | 1 | ja | `Leeruitkomst`, de aggregatie tussen de niveaus |
| `indicativeVolume` | `indicatieveOmvang` | array van `value` plus `unit` SBU of EC | 1..n | ja | `Leeruitkomst` |
| `nlqfLevel` | `nlqfNiveau` | integer 1 tot 8 | 0..1 | nee | `Leeruitkomst`, draagt het mbo-niveau van de keuzedeelruimte |
| `credentialDocument` | `waardedocument` | string | 0..1 | nee | `Waarde document (diploma / certificaat)` |
| `description`, `result`, `behaviour` | `omschrijving`, `resultaat`, `gedrag` | string, string, array string | 0..1, 0..1, 0..n | nee | `Leeruitkomst` |

`Competenties / Skills` met `Vaardigheid`, `Kennis` en `Inzicht` eronder zijn de verdieping die F1-12 meestuurt en krijgen hun veld via [W6](#7-de-werkbrieven).

### 4.4 Het ontwerp (O3), onderwijsspecificaties

Volgt [education-specification.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-specification.json). Het `specificationType` bepaalt het objecttype.

| `specificationType` | Objecttype | Instantie in F1-12 |
|---|---|---|
| `opleidingsspecificatie` | `Opleiding specificatie` | Apothekersassistent |
| `opleidingsprogrammaspecificatie` | `Opleidingsprogramma specificatie`, en `Keuzedeel` bij `programmeType` `keuzedeelprogramma` | BOL voltijd, Regulier BOL 2026 |
| `onderwijseenheidspecificatie` | `Onderwijseenheid specificatie` | Blok B1-K1 |
| `leeronderdeelspecificatie` | `Leeronderdeel specificatie` | Baliegesprekken 101 |
| `keuzedeelruimtespecificatie` | `Keuzedeelruimte` | 720 SBU, mbo-4 |

| Veld | Nederlands | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|---|
| `id` | `id` | uuid | 1 | ja | het objecttype uit de tabel hierboven |
| `specificationType` | `specificatieType` | enum | 1 | ja | idem |
| `version` | `versie` | string, semver | 1 | ja | idem, W4 en W10 |
| `parentSpecificationId` | `bovenliggendSpecificatieId` | uuid of null | 1 | ja | de aggregatie tussen de specificatie-objecttypen |
| `learningOutcomeId` | `leeruitkomstId` | uuid | 0..1 | ja in deze stroom, buiten `keuzedeelruimtespecificatie` om (W5) | `Leeruitkomst` |
| `name` | `naam` | string | 1 | ja | het objecttype uit de tabel hierboven |
| `studyLoad` | `studielast` | object: `value` plus `unit` | 1 | ja | idem, telt bottom-up op binnen onderdeel-van |
| `status` | `status` | enum | 1 | ja in deze stroom: `vastgesteld` bij aanlevering | idem |
| `manifest` | `manifest` | array van `specificationId`, `version`, `relation` | 0..n | ja zodra er onderdelen of varianten zijn | de gepinde versie per onderdeel |
| `ruleSetReferences` | `regelsetVerwijzingen` | array uuid | 0..n | ja op de keuzedeelruimte | `Student keuze regelset` |
| `description` | `omschrijving` | string | 0..1 | nee | het objecttype uit de tabel hierboven |
| `curriculumType` | `curriculumtype` | enum `nominaal`, `hybride`, `flexibel` | 0..1 | nee | `Opleiding specificatie`, `Opleidingsprogramma specificatie` |
| `programmeType` | `programmatype` | string, open lijst | 0..1 | ja op een programma | `Opleidingsprogramma specificatie`, `Keuzedeel` |
| `programmeLayer` | `programmaLaag` | enum `leerweg`, `doelgroep` | 0..1 | ja op een programma | `Opleidingsprogramma specificatie` |
| `learningPathway` | `leerweg` | enum `BOL`, `BBL` | 0..1 | ja op een programma | `Opleidingsprogramma specificatie` |
| `targetGroup` | `doelgroep` | string, open lijst | 0..1 | ja op de doelgroeplaag | `Opleidingsprogramma specificatie` |
| `electiveUnitClass` | `keuzedeelKlasse` | string, open lijst | 0..1 | ja op een keuzedeelprogramma | `Keuzedeel` |
| `cohort` | `cohort` | string | 0..1 | ja op de doelgroeplaag | `Cohort / periode` |
| `startDate`, `validFrom`, `validUntil` | `startdatum`, `geldigVanaf`, `geldigTot` | date | 0..1 elk | ja op de doelgroeplaag | geldigheid per ontwerpkeuze 16 |
| `timeDistribution` | `tijdsverdeling` | string, open lijst BOT, OOT, BPV | 0..1 | nee | `Leeronderdeel specificatie` |

### 4.5 Het ontwerp (O3), regelsets

Volgt [rule-set.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/rule-set.json).

| Veld | Nederlands | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|---|
| `id` | `id` | uuid | 1 | ja | `Student keuze regelset` |
| `version` | `versie` | string | 1 | ja | `Student keuze regelset` |
| `name` | `naam` | string | 1 | ja | `Student keuze regelset` |
| `appliesTo` | `vanToepassingOp` | uuid | 1 | ja | `Keuzedeelruimte` |
| `rules` | `regels` | array object | 1..n | ja | `Student keuze regelset`, getypeerde vorm via W9 |
| `description` | `omschrijving` | string | 0..1 | nee | `Student keuze regelset` |

rule-set.json laat het regelobject vrij. De sleutels waarmee de voorbeeldpayload hem vult zijn een voorstel bij W9, dat de getypeerde vorm belegt. Dezelfde namen gelden in [IS-OA-03](stroom-is-oa-03.md) en staan bij elkaar in [casus.md](casus.md#de-regelsets); de Nederlandse namen volgen de voorbeeldpayloads in Public.

| Veld | Nederlands | Wat zij draagt |
|---|---|---|
| `type` | `type` | het regeltype uit de gesloten set |
| `scope` | `bereik` | waar de regel over gaat |
| `electiveUnit` | `keuzedeel` | het keuzedeel waarop de regel slaat |
| `precondition` | `voorwaardeVooraf` | de deelnamevoorwaarde, met `requiredLearningOutcomeId` en `status` eronder |
| `value` plus `unit` | `waarde` plus `eenheid` | de maat bij een omvangregel |
| `requirement` | `eis` | het resultaat dat de regel verlangt |
| `sourceSpecificationId` | `bronSpecificatieId` | de specificatie waaruit de maat komt |

De sleutel `source` (`bron`) blijft daarmee de vorm van [source.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/source.json) op de leeruitkomst: een object met `standard`, `type` en `code`.

### 4.6 De resultaatstructuur (O4)

Volgt [result-structure.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/result-structure.json).

| `specificationType` | Objecttype | Instantie in F1-12 |
|---|---|---|
| `examenplanspecificatie` | `Summatieve resultaat structuur`, met `Examenplan` als vastgesteld geheel | Resultaatstructuur Apothekersassistent |
| `resultaateenheidspecificatie` | drager van `Examenonderdeel weging` en `Toetsonderdeel weging`, zonder eigen objecttype (W11) | Resultaat kerntaak B1-K1, Resultaat keuzedelen |
| `toetsonderdeelspecificatie` | `Toetsonderdeel specificatie`, en `Examenonderdeelspecificatie` bij een examen-toetsvorm | Praktijktoets baliegesprek (OSCE), Proeve van bekwaamheid B1-K1 |

| Veld | Nederlands | Type | Kardinaliteit | Verplicht | Objecttype |
|---|---|---|---|---|---|
| `id` | `id` | uuid | 1 | ja | het objecttype uit de tabel hierboven |
| `specificationType` | `specificatieType` | enum | 1 | ja | idem |
| `version` | `versie` | string, semver | 1 | ja | idem |
| `parentSpecificationId` | `bovenliggendSpecificatieId` | uuid of null | 1 | ja | de aggregatie binnen de resultaatstructuur |
| `name` | `naam` | string | 1 | ja | idem |
| `status` | `status` | string | 1 | ja | idem, `concept` bij de formatieve structuur |
| `resultModel` | `resultaatmodel` | object: `scale`, `passMark`, `decimalPlaces` | 1 | ja | `Summatieve resultaat structuur` |
| `appliesTo` | `geldtVoor` | uuid | 0..1 | ja op het examenplan | `Opleidingsprogramma specificatie` |
| `assesses` | `beoordeelt` | uuid | 0..1 | ja op een resultaateenheid | `Onderwijseenheid specificatie` of `Keuzedeelruimte` |
| `learningOutcomeId` | `leeruitkomstId` | uuid | 0..1 | ja buiten de keuzedeel-resultaateenheid om | `Leeruitkomst` |
| `learningOutcome` | `leeruitkomst` | object: `type`, `code` | 0..1 | nee, leesbare aanduiding naast de sleutel | `Kerntaak`, `Werkproces`, `Kwalificatie` |
| `nature` | `aard` | enum `summatief`, `formatief` | 0..1 | ja op een toetsonderdeel | `Summatieve resultaat structuur`, `Formatieve resultaat structuur` (W7) |
| `assessmentForm` | `toetsvorm` | string, open lijst | 0..1 | ja op een toetsonderdeel | `Toetsonderdeel specificatie`, `Examenonderdeelspecificatie` |
| `aggregation` | `aggregatie` | enum | 0..1 | ja op examenplan en resultaateenheid | `Summatief Afrondingscriterium` (W8) |
| `weighting` | `weging` | number | 0..1 | ja op resultaateenheid en toetsonderdeel, 0 bij formatief | `Examenonderdeel weging`, `Toetsonderdeel weging` |
| `mandatory` | `verplicht` | boolean | 0..1 | ja op resultaateenheid en toetsonderdeel | `Summatief Afrondingscriterium` |
| `ruleSetReferences` | `regelsetVerwijzingen` | array uuid | 0..n | ja op de keuzedeel-resultaateenheid | `Student keuze regelset` |
| `manifest` | `manifest` | array van `specificationId`, `version`, `relation` | 0..n | ja zodra er onderdelen zijn | de gepinde versie per onderdeel |
| `validFrom`, `validUntil` | `geldigVanaf`, `geldigTot` | date | 0..1 elk | ja op het examenplan | geldigheid per ontwerpkeuze 16 |
| `description` | `omschrijving` | string | 0..1 | nee | het objecttype uit de tabel hierboven |

De keuzedeelruimte in de summatieve resultaatstructuur loopt via `assesses` op de resultaateenheid, met de meetellende keuzedeelresultaten in de regelset. Dat beantwoordt de open beeldvraag bij F1-12.

## 5. Voorbeeldpayload: het ontwerp (O3)

Casus Apothekersassistent, crebo 23450, met de instantiewaarden uit F1-12. De id's en de versies staan in [casus.md](casus.md) en volgen daar [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) in Public, zodat dezelfde instantie over de hele keten dezelfde identiteit draagt.

```json
{
  "learningOutcomes": [
    {
      "id": "c5b64fe5-f7bf-490c-acaf-7af1bd24f980",
      "version": "0.1.0",
      "name": "Apothekersassistent (kwalificatiedossier 23450)",
      "source": { "standard": "sbb-kwalificatiekader", "type": "kwalificatiedossier", "code": "23450" },
      "parentLearningOutcomeId": null,
      "indicativeVolume": [{ "value": 4800, "unit": "SBU" }],
      "nlqfLevel": 4,
      "credentialDocument": "diploma"
    },
    {
      "id": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "version": "0.1.0",
      "name": "Apothekersassistent (kwalificatie 27141)",
      "source": { "standard": "sbb-kwalificatiekader", "type": "kwalificatie", "code": "27141" },
      "parentLearningOutcomeId": "c5b64fe5-f7bf-490c-acaf-7af1bd24f980",
      "indicativeVolume": [{ "value": 4800, "unit": "SBU" }]
    },
    {
      "id": "12301838-92d4-4040-aea2-050bb131ceb7",
      "version": "0.1.0",
      "name": "Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving",
      "source": { "standard": "sbb-kwalificatiekader", "type": "kerntaak", "code": "B1-K1" },
      "parentLearningOutcomeId": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "indicativeVolume": [{ "value": 2000, "unit": "SBU" }]
    },
    {
      "id": "78f25d62-9fd4-45c4-aa04-3d22f59213f5",
      "version": "0.1.0",
      "name": "Voert baliegesprek en triage uit in de simulatieapotheek",
      "source": { "standard": "sbb-kwalificatiekader", "type": "werkproces", "code": "B1-K1-W1" },
      "parentLearningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "indicativeVolume": [{ "value": 600, "unit": "SBU" }]
    }
  ],
  "educationSpecifications": [
    {
      "id": "79736830-1c5c-470f-b2c2-005029c96733",
      "specificationType": "opleidingsspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": null,
      "learningOutcomeId": "c5b64fe5-f7bf-490c-acaf-7af1bd24f980",
      "name": "Apothekersassistent",
      "description": "Opleiding tot apothekersassistent. Domein Zorg en welzijn.",
      "curriculumType": "nominaal",
      "status": "vastgesteld",
      "validFrom": "2026-08-01",
      "validUntil": null,
      "studyLoad": { "value": 4800, "unit": "SBU" },
      "manifest": [
        { "specificationId": "5ef37812-ae0f-4232-904f-451b9928e45e", "version": "0.1.0", "relation": "variant" }
      ]
    },
    {
      "id": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "specificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "79736830-1c5c-470f-b2c2-005029c96733",
      "learningOutcomeId": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "name": "BOL voltijd",
      "programmeType": "diplomaprogramma",
      "programmeLayer": "leerweg",
      "learningPathway": "BOL",
      "status": "vastgesteld",
      "studyLoad": { "value": 4800, "unit": "SBU" },
      "manifest": [
        { "specificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7", "version": "0.1.0", "relation": "variant" }
      ]
    },
    {
      "id": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "specificationType": "opleidingsprogrammaspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "5ef37812-ae0f-4232-904f-451b9928e45e",
      "learningOutcomeId": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "name": "Regulier BOL 2026",
      "programmeType": "diplomaprogramma",
      "programmeLayer": "doelgroep",
      "targetGroup": "regulier",
      "learningPathway": "BOL",
      "curriculumType": "nominaal",
      "cohort": "2026",
      "startDate": "2026-09-01",
      "validFrom": "2026-09-01",
      "validUntil": null,
      "status": "vastgesteld",
      "studyLoad": { "value": 4800, "unit": "SBU" },
      "manifest": [
        { "specificationId": "402c2342-d897-4df4-a667-7fc5bd930944", "version": "0.1.0", "relation": "onderdeel" },
        { "specificationId": "fb5be5ae-faa0-4b4b-8085-474fce9aae08", "version": "0.1.0", "relation": "onderdeel" }
      ]
    },
    {
      "id": "402c2342-d897-4df4-a667-7fc5bd930944",
      "specificationType": "onderwijseenheidspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "learningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "name": "Blok B1-K1",
      "status": "vastgesteld",
      "studyLoad": { "value": 2000, "unit": "SBU" },
      "manifest": [
        { "specificationId": "327c8263-3516-4b5a-8d57-c16241ec008d", "version": "0.1.0", "relation": "onderdeel" }
      ]
    },
    {
      "id": "327c8263-3516-4b5a-8d57-c16241ec008d",
      "specificationType": "leeronderdeelspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "402c2342-d897-4df4-a667-7fc5bd930944",
      "learningOutcomeId": "78f25d62-9fd4-45c4-aa04-3d22f59213f5",
      "name": "Baliegesprekken 101",
      "timeDistribution": "BOT",
      "status": "vastgesteld",
      "studyLoad": { "value": 600, "unit": "SBU" }
    },
    {
      "id": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "specificationType": "keuzedeelruimtespecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "name": "Keuzedeelruimte",
      "description": "Ruimte binnen de kwalificatie die met keuzedelen wordt ingevuld.",
      "status": "vastgesteld",
      "studyLoad": { "value": 720, "unit": "SBU" },
      "ruleSetReferences": ["e4037953-17d6-40a4-9e59-92ec1f9c19a8"]
    }
  ],
  "ruleSets": [
    {
      "id": "e4037953-17d6-40a4-9e59-92ec1f9c19a8",
      "version": "0.1.0",
      "name": "Kiesbare keuzedelen voor Apothekersassistent",
      "description": "Bepaalt welke keuzedelen in de keuzedeelruimte kiesbaar zijn.",
      "appliesTo": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "rules": [
        { "type": "kiesbaar", "scope": "alle keuzedelen met electiveUnitClass algemeen-verbredend" },
        {
          "type": "kiesbaar",
          "electiveUnit": "beaaaf4c-b267-41f7-9b8d-ac9a19a7dfe1",
          "precondition": [
            { "requiredLearningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7", "status": "behaald" }
          ]
        },
        { "type": "minimaleStudielast", "value": 720, "unit": "SBU" }
      ]
    }
  ]
}
```

De payload volgt de lijn van F1-12: kerntaak B1-K1 met een leeronderdeel. De optelling van `studyLoad` sluit over de volledige boom in voorbeeldpayloads.md. De tweede regel in de regelset draagt de volgordebepaling: keuzedeel K0037 is kiesbaar zodra de leeruitkomst op kerntaakniveau behaald is. [IS-OA-03](stroom-is-oa-03.md) levert dezelfde regelset op dezelfde versie door aan planning.

## 6. Voorbeeldpayload: de resultaatstructuur (O4)

```json
{
  "educationSpecifications": [
    {
      "id": "08b4656d-27ec-4175-8c1b-1f1d51780785",
      "specificationType": "examenplanspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": null,
      "appliesTo": "7ae25c1e-ee27-43a2-a001-761ee39ea5c7",
      "learningOutcomeId": "b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4",
      "learningOutcome": { "type": "kwalificatie", "code": "27141" },
      "name": "Resultaatstructuur Apothekersassistent",
      "description": "Alle kerntaken voldoende, de keuzedeelruimte gevuld en afgerond, en het basisdeel behaald.",
      "aggregation": "allenVoldoende",
      "resultModel": { "scale": "voldoende-onvoldoende" },
      "status": "vastgesteld",
      "validFrom": "2026-09-01",
      "validUntil": null,
      "manifest": [
        { "specificationId": "0512c773-9c1b-42c4-ae0d-9af8554f2462", "version": "0.1.0", "relation": "onderdeel" },
        { "specificationId": "df0d3e50-c7c3-416e-b694-12fe5791eb7c", "version": "0.1.0", "relation": "onderdeel" }
      ]
    },
    {
      "id": "0512c773-9c1b-42c4-ae0d-9af8554f2462",
      "specificationType": "resultaateenheidspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "08b4656d-27ec-4175-8c1b-1f1d51780785",
      "learningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "learningOutcome": { "type": "kerntaak", "code": "B1-K1" },
      "assesses": "402c2342-d897-4df4-a667-7fc5bd930944",
      "name": "Resultaat kerntaak B1-K1",
      "weighting": 1,
      "aggregation": "gewogenGemiddelde",
      "resultModel": { "scale": "cijfer-1-10", "passMark": 5.5, "decimalPlaces": 1 },
      "mandatory": true,
      "status": "vastgesteld",
      "manifest": [
        { "specificationId": "941f180d-b0af-4933-a580-6ab654dfadda", "version": "0.1.0", "relation": "onderdeel" },
        { "specificationId": "6061f30c-e8fd-44b8-a553-e3078c07dc75", "version": "0.1.0", "relation": "onderdeel" },
        { "specificationId": "f004ba43-1e0b-4b8f-a677-0644ce29f4ea", "version": "0.1.0", "relation": "onderdeel" }
      ]
    },
    {
      "id": "941f180d-b0af-4933-a580-6ab654dfadda",
      "specificationType": "toetsonderdeelspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "0512c773-9c1b-42c4-ae0d-9af8554f2462",
      "learningOutcomeId": "12301838-92d4-4040-aea2-050bb131ceb7",
      "learningOutcome": { "type": "kerntaak", "code": "B1-K1" },
      "name": "Proeve van bekwaamheid B1-K1",
      "nature": "summatief",
      "assessmentForm": "proeveVanBekwaamheid",
      "weighting": 2,
      "resultModel": { "scale": "cijfer-1-10", "passMark": 5.5, "decimalPlaces": 1 },
      "mandatory": true,
      "status": "vastgesteld"
    },
    {
      "id": "6061f30c-e8fd-44b8-a553-e3078c07dc75",
      "specificationType": "toetsonderdeelspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "0512c773-9c1b-42c4-ae0d-9af8554f2462",
      "learningOutcomeId": "78f25d62-9fd4-45c4-aa04-3d22f59213f5",
      "learningOutcome": { "type": "werkproces", "code": "B1-K1-W1" },
      "name": "Praktijktoets baliegesprek (OSCE)",
      "nature": "summatief",
      "assessmentForm": "praktijkopdracht",
      "weighting": 1,
      "resultModel": { "scale": "cijfer-1-10", "passMark": 5.5, "decimalPlaces": 1 },
      "mandatory": true,
      "status": "vastgesteld"
    },
    {
      "id": "f004ba43-1e0b-4b8f-a677-0644ce29f4ea",
      "specificationType": "toetsonderdeelspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "0512c773-9c1b-42c4-ae0d-9af8554f2462",
      "learningOutcomeId": "78f25d62-9fd4-45c4-aa04-3d22f59213f5",
      "learningOutcome": { "type": "werkproces", "code": "B1-K1-W1" },
      "name": "Formatieve voortgang baliegesprek",
      "nature": "formatief",
      "assessmentForm": "criteriumgesprek",
      "weighting": 0,
      "resultModel": { "scale": "voldoende-onvoldoende" },
      "mandatory": false,
      "status": "concept"
    },
    {
      "id": "df0d3e50-c7c3-416e-b694-12fe5791eb7c",
      "specificationType": "resultaateenheidspecificatie",
      "version": "0.1.0",
      "parentSpecificationId": "08b4656d-27ec-4175-8c1b-1f1d51780785",
      "assesses": "fb5be5ae-faa0-4b4b-8085-474fce9aae08",
      "name": "Resultaat keuzedelen",
      "description": "Welke keuzedeelresultaten meetellen staat in de regelset.",
      "weighting": 1,
      "aggregation": "minimaalAantal",
      "resultModel": { "scale": "voldoende-onvoldoende" },
      "mandatory": true,
      "status": "vastgesteld",
      "ruleSetReferences": ["132f165a-973c-41c2-98df-e58d4ca6d7eb"]
    }
  ],
  "ruleSets": [
    {
      "id": "132f165a-973c-41c2-98df-e58d4ca6d7eb",
      "version": "0.1.0",
      "name": "Meetellende keuzedeelresultaten Apothekersassistent",
      "appliesTo": "df0d3e50-c7c3-416e-b694-12fe5791eb7c",
      "rules": [
        { "type": "minimaleStudielast", "value": 720, "unit": "SBU", "sourceSpecificationId": "fb5be5ae-faa0-4b4b-8085-474fce9aae08" },
        { "type": "resultaatEis", "scope": "elk gekozen keuzedeel", "requirement": "voldoende" }
      ]
    }
  ]
}
```

De proeve weegt twee keer zo zwaar als de praktijktoets, de formatieve toets weegt 0 en komt als concept mee. Het id `6061f30c` is de instantie die deze snede toevoegt aan de id-reeks uit voorbeeldpayloads.md.


## 7. De werkbrieven

| Nr | Wat erbij moet | Waar | Versie-impact |
|---|---|---|---|
| W1 | Het innamecontract: welke endpoints de dienst dragen, met als voorstel `POST /onderwijsspecificaties` en `POST /examenplanspecificaties`, de respons 202 met de uitkomst via O5, en de vorm van de reden bij afkeuring | [onderwijsspecificatie-inname-aanbieder.md](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/onderwijsspecificatie-inname-aanbieder.md), paragraaf Endpoints, en [onderwijscatalogus.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md) | Additief: deze endpoints komen erbij op de catalogus, de bestaande opvragingen en payloadschema's blijven gelijk |
| W2 | Endpointtabel voor de curriculum ontwerptool met `verwerkingsstatus` POST en `POST /abonnementen`, de diensten die zij als ontvanger implementeert | [curriculum-ontwerptool.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/curriculum-ontwerptool.md) | Additief: bestaande paden en schema's, nieuw koppelvlak op een component zonder endpoints |
| W3 | Parameter `leeruitkomstId` op het zoeken naar hergebruik, en kopmetadata (`name`, `studyLoad`) in de respons, zodat de ontwerper kan kiezen op wat de specificatie belooft | [onderwijscatalogus.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Applicatiecomponenten/onderwijscatalogus.md) en [specification-reference.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-reference.json) | MINOR: additieve parameter en additieve optionele velden |
| W4 | Regel hoe de toegekende identiteit zich verhoudt tot de id's waarmee de ontwerptool aanlevert, met `specificationReference` als terugweg | [regels.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/regels.md), naast de regel dat de catalogus versienummers uitgeeft | Geen schemawijziging |
| W5 | Gebruiksprofiel voor deze koppeling: `educationSpecifications` volledig met manifest, `learningOutcomes` volledig met inhoudsvelden, `ruleSets` volledig, en `learningOutcomeId` verplicht buiten de `keuzedeelruimtespecificatie` om | [gebruiksprofielen.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/gebruiksprofielen.md) | Geen schemawijziging |
| W6 | Veld voor `Competenties / Skills` met `Vaardigheid`, `Kennis` en `Inzicht` eronder, elk met standaard en code | [learning-outcome.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/learning-outcome.json) | MINOR: optionele array, met een eigen schema voor het competentie-item |
| W7 | Type voor de `Formatieve resultaat structuur` als eigen wortel naast het examenplan | [result-structure.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/result-structure.json), enum `specificationType` | MINOR: additieve enumwaarde. Strikt validerende ontvangers krijgen de waarde vooraf |
| W8 | Drager voor het generieke basisdeel in het `Summatief Afrondingscriterium`: Nederlands en rekenen, Engels, loopbaan en burgerschap | result-structure.json via `ruleSetReferences` op het examenplan, plus een resultaateenheid in de instantie | Geen schemawijziging, wel een uitwerking van de regels en de instantie |
| W9 | Getypeerde regels met `scopes` (`bereiken`) en `parameters`, conform de uitwerking in [regelset-payload.md](../student-keuze/regelset-payload.md), plus de Engelse sleutels van het regelobject uit 4.5 | [rule-set.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/rule-set.json) | MINOR voor `scopes`, MAJOR bij overname van `ruleSetId` als sleutelnaam |
| W10 | Releaseaanduiding naast `version` voor de vorm 2026.1 uit de voorbeelduitwerking, die buiten het semver-patroon valt | [education-specification.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/education-specification.json), of semver in de [voorbeelduitwerking](../../../model/informatiemodel/voorbeeld-lr1-regels.json) | MINOR voor een additief veld, of geen schemawijziging bij semver in het voorbeeld |
| W11 | Objecttype voor de `resultaateenheidspecificatie`, de laag tussen examenplan en toetsonderdeel | [informatiemodel.md](../../../model/informatiemodel/informatiemodel.md) en [begrippenlijst.md](../begrippen/begrippenlijst.md) | Geen schemawijziging: informatiemodel en begrippenlijst |
| W12 | Een stabiel `eventId` op O5 en O6, waarop de ontvanger een herhaald bericht herkent, zoals [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) voor herhaalbare verwerking vraagt | [processing-status.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/processing-status.json) en [specification-status-changed.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/specification-status-changed.json), gelijk aan W6 van IS-OA-05 en W8 van IS-OA-06 | Optioneel: MINOR. Verplicht: MAJOR |
| W13 | De Engelse sleuteltaal van de payload vastleggen in de uitgangspunten, zodat [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) en de voorbeeldpayloads dezelfde sleutels dragen als de schema's | [uitgangspunten.md](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md), [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) | Geen schemawijziging: de schema's dragen de Engelse sleutels al, documentatie volgt |

Wat deze eenheid verder raakt staat in de [signaleringen](README.md#signaleringen-en-openstaande-punten) van de interactiespecificatie: S5 vraagt een koppeling-ID en een eigen lijn op de hoofdplaat, S6 de grond per objecttype.
