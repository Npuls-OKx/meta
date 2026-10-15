# Casus: de identificaties van de interactiespecificatie onderwijsaanbod

De vaste identificaties onder de interactiespecificatie [ontwerpen en ontsluiten van onderwijsaanbod](README.md). Per laag staat hier wat het object is, welk objecttype uit het [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md) het draagt, welke uuid en versie het houdt, en onder welke naam het in een payload verschijnt. Casus Apothekersassistent, crebo 23450, kwalificatie 27141, cohort 2026, leerroute 1 met [persona Jochem](../leerroute-uitwerking/doc/persona_jochem.md). Relateert aan: #372.

De zes verdiepingsbestanden [stroom-is-oa-01.md](stroom-is-oa-01.md) tot en met [stroom-is-oa-06.md](stroom-is-oa-06.md) halen hun voorbeeldwaarden hier. Wie de keten van verzoek naar aanbod volgt, leest in elke volgende payload dezelfde sleutel terug.

De kolom Bron zegt waar de identificatie vandaan komt. De waarde Public staat bij een object waarvoor [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) al een uuid voor dezelfde casus draagt; die uuid staat hier onveranderd. De waarde Deze snede staat bij een object waarvoor die voorbeeldpayloads nog een uuid krijgen.

## De versie per object

Elk object draagt versie `0.1.0`, de pin die de voorbeeldpayloads in Public aanhouden. Die versie blijft gelijk over de stromen heen: de specificatie die IS-OA-01 aanlevert, die IS-OA-03 planbaar meldt en waarnaar IS-OA-04 met `specificationReference` terugwijst, draagt dezelfde uuid en dezelfde versie.

IS-OA-02 beschrijft de uitzondering. Die eenheid vult de grofmazige specificatie aan met de uitvoeringskenmerken en laat de versie van `0.1.0` naar `0.2.0` lopen, op de onderwijseenheidspecificatie, haar leeronderdeelspecificatie en de proeve van bekwaamheid. Die eenheid staat op voorstel; de melding van IS-OA-03 en het aanbod van IS-OA-04 rusten op `0.1.0`.

## Het kwalificatiekader

Deze objecten reizen als `source` (bron) op de leeruitkomst mee, in de vorm van [source.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/source.json): een object met `standard`, `type` en `code`. Hun identificatie in de payload is de code, en de versie van het kader blijft bij de Samenwerkingsorganisatie Beroepsonderwijs Bedrijfsleven (SBB).

| Wat het is | Objecttype | Identificatie in `source.code` | Naam |
|---|---|---|---|
| Kwalificatiedossier | `Kwalificatie dossier` | `23450` | Apothekersassistent |
| Kwalificatie, niveau 4 | `Kwalificatie` | `27141` | Apothekersassistent |
| Kerntaak | `Kerntaak` | `B1-K1` | Biedt farmaceutische patiëntenzorg |
| Werkproces | `Werkproces` | `B1-K1-W1` | Neemt de zorg-/adviesvraag in behandeling |
| Werkproces | `Werkproces` | `B1-K1-W2` | Voert medicatiebewaking uit |

De `standard` draagt in deze casus overal de waarde `sbb-kwalificatiekader`. Het dossier staat in deze repository als [Apothekersassistent-2.md](../../kwalificatiedossier/Apothekersassistent-2.md).

## De leeruitkomsten

De leeruitkomst is de sleutel: elke specificatie en elke resultaateenheid verwijst met `learningOutcomeId` naar deze identificaties. De naam staat in de stem van de instelling, het kader eronder in `source`.

| Wat het is | Objecttype | Identificatie | Versie | Naam in de payload | Bron |
|---|---|---|---|---|---|
| Leeruitkomst op dossierniveau | `Leeruitkomst` | `c5b64fe5-f7bf-490c-acaf-7af1bd24f980` | `0.1.0` | Apothekersassistent (kwalificatiedossier 23450) | Public |
| Leeruitkomst op kwalificatieniveau | `Leeruitkomst` | `b84dc98b-6c5f-4ee8-bdfb-40b2639ca5a4` | `0.1.0` | Apothekersassistent (kwalificatie 27141) | Public |
| Leeruitkomst op kerntaakniveau | `Leeruitkomst` | `12301838-92d4-4040-aea2-050bb131ceb7` | `0.1.0` | Biedt farmaceutische patiëntenzorg in een levensechte apotheekomgeving | Public |
| Leeruitkomst op werkprocesniveau, B1-K1-W1 | `Leeruitkomst` | `78f25d62-9fd4-45c4-aa04-3d22f59213f5` | `0.1.0` | Voert baliegesprek en triage uit in de simulatieapotheek | Public |
| Leeruitkomst op werkprocesniveau, B1-K1-W2 | `Leeruitkomst` | `0ffa279f-c595-49d7-b033-c91f66d18bb1` | `0.1.0` | Voert medicatiebewaking uit | Public |

De aggregatie loopt met `parentLearningOutcomeId` van werkproces naar kerntaak naar kwalificatie naar dossier. Public draagt voor de twee onderste leeruitkomsten de naam van het kader; deze snede houdt de instellingsnaam uit beeld F1-12 aan, omdat ontwerpkeuze 2 het kader naar de stem van de instelling laat vertalen.

## De onderwijsspecificatie

De laag die IS-OA-01 aanlevert, IS-OA-02 aanvult en IS-OA-03 planbaar meldt. Het veld `specificationType` wijst het objecttype aan.

| Wat het is | Objecttype | Identificatie | Versie | Naam in de payload | Bron |
|---|---|---|---|---|---|
| Opleidingsspecificatie | `Opleiding specificatie` | `79736830-1c5c-470f-b2c2-005029c96733` | `0.1.0` | Apothekersassistent | Public |
| Opleidingsprogrammaspecificatie, `programmeLayer` `leerweg` | `Opleidingsprogramma specificatie` | `5ef37812-ae0f-4232-904f-451b9928e45e` | `0.1.0` | BOL voltijd | Public |
| Opleidingsprogrammaspecificatie, `programmeLayer` `doelgroep` | `Opleidingsprogramma specificatie` | `7ae25c1e-ee27-43a2-a001-761ee39ea5c7` | `0.1.0` | Regulier BOL 2026 | Public |
| Onderwijseenheidspecificatie van kerntaak B1-K1 | `Onderwijseenheid specificatie` | `402c2342-d897-4df4-a667-7fc5bd930944` | `0.1.0`, in IS-OA-02 `0.2.0` | Blok B1-K1 | Public |
| Leeronderdeelspecificatie, B1-K1-W1 | `Leeronderdeel specificatie` | `327c8263-3516-4b5a-8d57-c16241ec008d` | `0.1.0`, in IS-OA-02 `0.2.0` | Baliegesprekken 101 | Public |
| Leeronderdeelspecificatie, B1-K1-W2 | `Leeronderdeel specificatie` | `29522e42-fb32-46d2-a504-0869831f941f` | `0.1.0` | Medicatiebewaking in de leerapotheek | Public |
| Keuzedeelruimte, 720 SBU op mbo-4 | `Keuzedeelruimte` | `fb5be5ae-faa0-4b4b-8085-474fce9aae08` | `0.1.0` | Keuzedeelruimte | Public |
| Keuzedeel als eigen programmaspecificatie | `Keuzedeel` | `beaaaf4c-b267-41f7-9b8d-ac9a19a7dfe1` | `0.1.0` | K0037 Farmaceutische Patientenzorg | Deze snede |

De aggregatie loopt met `parentSpecificationId`: de leerweglaag onder de opleiding, de doelgroeplaag onder de leerweg, en de onderwijseenheid met de keuzedeelruimte onder de doelgroeplaag. Het keuzedeel staat als eigen wortel, omdat het over opleidingen heen herbruikbaar is; de catalogus bereikt het via de regelset op de keuzedeelruimte. Public pint de keuzedelen K0072, K0000-ri en K0000-w1 en kent K0037 nog niet, dus draagt dat keuzedeel een uuid van deze snede.

De studielast per laag: de opleiding en beide programmalagen 4800 SBU, Blok B1-K1 2000 SBU, Baliegesprekken 101 600 SBU, Medicatiebewaking 500 SBU, de keuzedeelruimte 720 SBU. De optelling sluit over de volledige boom in de voorbeeldpayloads van Public; de payloads in de zes stromen zijn een uitsnede van die boom.

### De regelsets

| Wat het is | Objecttype | Identificatie | Versie | Naam in de payload | Bron |
|---|---|---|---|---|---|
| Regelset op de keuzedeelruimte | `Student keuze regelset` | `e4037953-17d6-40a4-9e59-92ec1f9c19a8` | `0.1.0` | Kiesbare keuzedelen voor Apothekersassistent | Public |
| Regelset op de resultaateenheid keuzedelen | `Student keuze regelset` | `132f165a-973c-41c2-98df-e58d4ca6d7eb` | `0.1.0` | Meetellende keuzedeelresultaten Apothekersassistent | Public |

De eerste regelset geldt met `appliesTo` op de keuzedeelruimte en maakt K0037 kiesbaar zodra de leeruitkomst op kerntaakniveau behaald is. De tweede geldt op de resultaateenheid keuzedelen en legt vast welke keuzedeelresultaten meetellen. De sleutels binnen `rules` dragen in beide gevallen dezelfde namen, omdat [rule-set.json](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/schemas/rule-set.json) het regelobject vrij laat en de voorbeeldpayloads in Public de vorm aanhouden:

| Sleutel | Nederlands | Wat zij draagt |
|---|---|---|
| `type` | `type` | het regeltype |
| `scope` | `bereik` | waar de regel over gaat |
| `electiveUnit` | `keuzedeel` | het keuzedeel waarop de regel slaat |
| `precondition` | `voorwaardeVooraf` | de deelnamevoorwaarde, met `requiredLearningOutcomeId` en `status` eronder |
| `value` plus `unit` | `waarde` plus `eenheid` | de maat bij een omvangregel |
| `requirement` | `eis` | het resultaat dat de regel verlangt |
| `sourceSpecificationId` | `bronSpecificatieId` | de specificatie waaruit de maat komt |

De sleutel `source` (`bron`) blijft daarmee voorbehouden aan de vorm van source.json op de leeruitkomst en op de aanbodinstantie.

## De resultaatstructuur

De laag die IS-OA-01 met de resultaatstructuur aanlevert en die IS-OA-02 aan de toetskant aanvult.

| Wat het is | Objecttype | Identificatie | Versie | Naam in de payload | Bron |
|---|---|---|---|---|---|
| Examenplanspecificatie als vastgesteld geheel | `Summatieve resultaat structuur`, met `Examenplan` | `08b4656d-27ec-4175-8c1b-1f1d51780785` | `0.1.0` | Resultaatstructuur Apothekersassistent | Public |
| Resultaateenheid op kerntaak B1-K1 | drager van `Examenonderdeel weging` en `Toetsonderdeel weging` | `0512c773-9c1b-42c4-ae0d-9af8554f2462` | `0.1.0` | Resultaat kerntaak B1-K1 | Public |
| Resultaateenheid op de keuzedeelruimte | idem | `df0d3e50-c7c3-416e-b694-12fe5791eb7c` | `0.1.0` | Resultaat keuzedelen | Public |
| Examenonderdeel, weging 2 | `Examenonderdeelspecificatie` | `941f180d-b0af-4933-a580-6ab654dfadda` | `0.1.0`, in IS-OA-02 `0.2.0` | Proeve van bekwaamheid B1-K1 | Public |
| Toetsonderdeel, weging 1 | `Toetsonderdeel specificatie` | `6061f30c-e8fd-44b8-a553-e3078c07dc75` | `0.1.0` | Praktijktoets baliegesprek (OSCE) | Deze snede |
| Toetsonderdeel, formatief, weging 0 | `Toetsonderdeel specificatie`, onder `Formatieve resultaat structuur` | `f004ba43-1e0b-4b8f-a677-0644ce29f4ea` | `0.1.0` | Formatieve voortgang baliegesprek | Public |

Het examenplan geldt met `appliesTo` voor de doelgroeplaag `Regulier BOL 2026`. De resultaateenheid op de kerntaak beoordeelt met `assesses` de onderwijseenheidspecificatie, die op de keuzedelen de keuzedeelruimte. Werkbrief W11 van IS-OA-01 belegt het objecttype achter de enumwaarde `resultaateenheidspecificatie`.

## Het geplande aanbod

De lagen die IS-OA-04 terugmeldt en die IS-OA-05 en IS-OA-06 verder ontsluiten. Het veld `offeringType` wijst de laag aan, en `specificationReference` draagt per laag de uuid en de versie uit de tabellen hierboven.

| Wat het is | Objecttype | Identificatie | Versie | Naam in de payload | Bron |
|---|---|---|---|---|---|
| Opleidingsaanbod, 48 plaatsen | `Opleiding aanbod` | `7aa6609f-1d1b-471a-a0f8-beae490d31b5` | `0.1.0` | Apothekersassistent 2026 | Public |
| Opleidingsprogramma-aanbod, 24 tot 48 plaatsen | `Opleidingsprogramma aanbod` | `8c494250-b67a-4666-a762-6f9ec1e70aff` | `0.1.0` | Regulier BOL 2026 | Public |
| Onderwijseenheid-aanbod | `Onderwijseenheid aanbod` | `04af26e6-96be-480a-8413-87a128164681` | `0.1.0` | B1-K1, leerjaar 1, periode 1 tot 4 | Public |
| Leergelegenheid, twee groepen | `Leergelegenheid` | `04070a96-01e0-4958-9f7e-69b429c72eec` | `0.1.0` | Baliegesprekken 101, periode 1 | Public |
| Keuzedeelaanbod als eigen wortel | `Keuzedeel aanbod` | `daffa71f-d6dc-470e-9914-4477ea15075f` | `0.1.0` | K0037 Farmaceutische Patientenzorg, periode 7 | Deze snede |

Welke specificatie elke laag aanwijst:

| Aanbodlaag | `specificationReference.specificationId` |
|---|---|
| Apothekersassistent 2026 | `79736830-1c5c-470f-b2c2-005029c96733` |
| Regulier BOL 2026 | `7ae25c1e-ee27-43a2-a001-761ee39ea5c7` |
| B1-K1, leerjaar 1, periode 1 tot 4 | `402c2342-d897-4df4-a667-7fc5bd930944` |
| Baliegesprekken 101, periode 1 | `327c8263-3516-4b5a-8d57-c16241ec008d` |
| K0037 Farmaceutische Patientenzorg, periode 7 | `beaaaf4c-b267-41f7-9b8d-ac9a19a7dfe1` |

Dat is de aansluiting die de lezer van IS-OA-03 en IS-OA-04 naast elkaar legt: de specificatie die IS-OA-03 planbaar meldt is dezelfde als die waarop IS-OA-04 het aanbod terugmeldt, op dezelfde uuid en dezelfde versie.

### De groepen, de locaties en de organisatie

Deze objecten dragen een naam en een uuid, en geen eigen versie in de payload.

| Wat het is | Objecttype | Identificatie | Naam in de payload | Bron |
|---|---|---|---|---|
| Groep bij de leergelegenheid, capaciteit 24 | `Plaatsingsgroep` | `13cc9125-6f0d-4faf-b483-9f0e4102790e` | APO26-1A | Public |
| Groep bij de leergelegenheid, capaciteit 24 | `Plaatsingsgroep` | `93937bfe-4e4a-4f6a-9d5b-2754613aa2df` | APO26-1B | Public |
| Groep bij het keuzedeelaanbod, capaciteit 24 | `Plaatsingsgroep` | `55169145-f993-4bfe-8b89-888807820d8d` | KD-K0037-28-P7 | Deze snede |
| Vestiging, vestigingscode UTR-01 | `Onderwijslocatie` | `59807057-a6f1-473b-9084-114644557a68` | Hoofdlocatie Utrecht | Public |
| Ruimte binnen die vestiging | `Onderwijslocatie` | `cfe4ae31-d8d1-40f8-9d62-eda917fefbd3` | Praktijklokaal farmacie 2.14 | Public |
| Instelling | `Organisatie-eenheid` | `6132ece6-d75e-4e80-81ce-91ab7448794d` | ROC Leren Zonder Drempels | Deze snede |
| Uitvoerend onderwijsteam | `Organisatie-eenheid` | `d9561371-5ece-482d-a675-a076e63f980f` | Onderwijsteam Farmacie | Public |

De instelling van deze casus is ROC Leren Zonder Drempels en draagt daarom een uuid van deze snede; de voorbeeldpayloads in Public voeren hun eigen instelling onder de naam ROC Voorbeeld.

## Het onderwijs- en examenontwerp

De objecten die IS-OA-02 op de specificatie en op het toetsonderdeel zet. Zij dragen een naam en een uuid, en geen eigen versie in de payload.

| Wat het is | Objecttype | Identificatie | Naam in de payload | Bron |
|---|---|---|---|---|
| Docentprofiel bij de eenheid en het leeronderdeel | `Expertise of functieprofiel` | `8e1dcda7-ef4e-45d0-931a-e47c3c77ddef` | Apothekersassistent-docent met baliepraktijk | Deze snede |
| Examinatorprofiel bij de proeve | `Expertise of functieprofiel` | `4037f1a2-c182-4f2d-ae00-bfb06b076337` | Examinator met baliepraktijk en toetsbekwaamheid | Deze snede |
| Toetsinstrument bij de proeve | zonder objecttype, van de conceptplaat Onderwijsontwerp | `da138f60-ebb1-4853-870f-7e7d642873f2` | Beoordelingsformulier met rubric | Deze snede |

Werkbrief WB-03 en WB-06 van IS-OA-02 beleggen het schema voor het expertiseprofiel en voor het toetsinstrument.

## Wat deze casus openlaat

| Punt | Stand |
|---|---|
| Het versieformaat: de voorbeelduitwerking schrijft `2026.1` op de opleidingsspecificatie, de schema's eisen het patroon `n.n.n` | W12 van IS-OA-03, W10 van IS-OA-01. Deze casus pint `0.1.0` |
| De capaciteit van `Regulier BOL 2026`: de voorbeelduitwerking geeft 24 tot 48 plaatsen, de voorbeeldpayload in Public 18 tot 120 | Signalering S-D van IS-OA-05. Deze casus draagt 24 tot 48 |
| Een uuid voor keuzedeel K0037 in de voorbeeldpayloads van Public | Zolang die ontbreekt draagt K0037 de uuid van deze snede |
| Een objecttype voor `Plaatsingsgroep` op de aanbodlaag en voor het toetsinstrument | W5 van IS-OA-04, WB-06 van IS-OA-02, signalering S-F van IS-OA-05 |

## Verwijzingen

| Bron | Wat het levert |
|---|---|
| [voorbeeldpayloads.md in Public](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) | De uuid's en de versiepin voor dezelfde casus |
| [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md) | De objecttypen en hun relaties |
| [begrippenlijst](../begrippen/begrippenlijst.md) | De definitie per objecttype |
| [voorbeeld-lr1-regels.json](../../../model/informatiemodel/voorbeeld-lr1-regels.json) | De instanties per beeld, F1-01 tot en met F3-02 |
| [kwalificatiedossier Apothekersassistent](../../kwalificatiedossier/Apothekersassistent-2.md) | Crebo, kwalificatie, niveau, domein en geldigheid |
| [casus Jochem kiest een keuzedeel](../koppelvlak-keuzedeel-kiesbaar/casus.md) | De keuzedeelruimte, de keuzedelen en hun studielast |
