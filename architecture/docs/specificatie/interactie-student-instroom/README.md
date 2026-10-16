# Interactieketenspecificatie: aanmelden, intake, inschrijven en roosteren tot de start

| | |
|---|---|
| **Document doel** | Legt vast welke koppelingen een instelling nodig heeft om een student van aanmelding naar een geroosterde verbintenis te brengen, en wat een leverancier daarvoor bouwt |
| **Doelgroep** | De implementatiespecialist en de tester bij een instelling of een leverancier, en wie een profiel of consumer bouwt |
| **Dient als input voor** | De bouw van de koppelvlakken, de testgevallen erbij, en de acceptatie van een opgeleverde koppeling |
| **Kaderstelling** | Het [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md), de [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) en hoofdplaat v1.7 |
| **Inhoud** | Zeven interactiespecificaties met hun operaties en berichten, twee signaleringen, en de koppelvlakdiensten per applicatiecomponent |
| **Status** | Voorstel. Vijf van de zes stromen die deze keten draagt, staan op v1.7 zonder koppelingspecificatie |

## Leeswijzer

| Bestand | Wat erin staat |
|---|---|
| [signaleringen.md](signaleringen.md) | Twee punten die een besluit vragen |
| De zeven interactiespecificaties | Het contract per koppelvlakdienst, met het bericht onder zijn operatie |

## 1. De informatiestromen

| Eenheid | Beelden | Van | Naar | Stroom op hoofdplaat v1.7 |
|---|---|---|---|---|
| IS-SI-01 | F3-04 | Voorziening Centraal Aanmelden (CAMBO) | Kernregistratie (KRS) | `Persoon(Student) Opleidingprogramma verbintenis` |
| IS-SI-02 | F3-05, F3-06 | Intakesysteem | Kernregistratie (KRS) | Geen; het intakesysteem draagt geen stroom ([S1](signaleringen.md)) |
| IS-SI-03 | F3-07, F3-08 | Kernregistratie (KRS) | Studentkeuzesysteem (SKS) | `Student, opleidingprogramma verbintenis, relevante groepen` |
| IS-SI-04 | F4-06 | Kernregistratie (KRS) | Planningssysteem | `Ontsluiten plaatsingsgroepen met studenten` |
| IS-SI-05 | F4-07, F4-08 | Planningssysteem | Roostersysteem | `Verzoek tot roosteren leergelegenheid` |
| IS-SI-06 | F4-09 | Roostersysteem | Studentkeuzesysteem (SKS) | `Student Opleidingprogramma- en onderwijseenheid verbintenis` ([S2](signaleringen.md)) |
| IS-SI-07 | F4-10 | Kernregistratie (KRS) | Leermanagementsysteem (LMS) | Hetzelfde been van de junctie als IS-SI-03 |

De eenheden volgen de beeldnummers van de voorbeelduitwerking, en dat is ook de volgorde waarin een instelling ze doorloopt. IS-SI-03 en IS-SI-07 delen hun lading: de kernregistratie bedient de leeromgeving en het studentkeuzesysteem langs dezelfde junctie. Het zijn twee eenheden, want een koppeling verbindt twee componenten en de afnemers verschillen; IS-SI-07 wijst voor de lading naar IS-SI-03.

Negen beelden uit de voorbeelduitwerking van leerroute 1 dragen deze keten. De keten begint waar de aanmelding de instelling binnenkomt: hoe een student zich bij de voorziening voor centraal aanmelden meldt (F3-03) wordt door AII beschreven. De knip met de keten [onderwijsaanbod ontsluiten](../interactie-onderwijsaanbod/README.md) ligt op de informatiestroom en niet op de procesfase: wat de specificatie fijnmaziger maakt hoort daar, wat de student plaatst en roostert hoort hier.

Veertien objecttypen bewegen door deze keten: `Aanmelding`, `Inschrijving`, `Persoon`, `Student`, `Plaatsingsgroep`, `Leergelegenheid`, `Lesgelegenheid`, `Medewerker`, `Leeruitkomst` en de vijf verbintenissoorten op opleiding, opleidingsprogramma, onderwijseenheid, leergelegenheid en lesgelegenheid.

## 2. Wat deze keten oplevert

| Partij | Wat zij eruit haalt |
|---|---|
| Instelling | De koppelingen die zij uitvraagt om een student van aanmelding naar rooster te brengen, met de aanduiding per eenheid |
| Leverancier | Het contract per koppelvlakdienst: welke endpoints zij bouwt en welke zij aanroept |
| Tester | De operaties met hun statuscodes en voorbeeldpayloads |

## 3. Koppelvlakdiensten

Een dienst zegt wat er over een koppeling moet kunnen, en elk component kan hem claimen; de aanbieder en de afnemer zijn twee losse diensten. Een leverancier die meer dan een component in een product draagt, legt dat product daarom op deze laag.

| Component | Dienst | Endpoints en meldingen | Eenheid | Stand |
|---|---|---|---|---|
| Kernregistratie (KRS) | aanmelding-inname-aanbieder | `POST /aanmeldingen`, `GET /aanmeldingen/{id}` | IS-SI-01 | Voorstel (W1) |
| Kernregistratie (KRS) | verwerkingsuitkomst-aanbieder | de melding `aanmelding-verwerkt` | IS-SI-01 | Voorstel (W3) |
| Kernregistratie (KRS) | afleverabonnement-aanbieder | `POST /abonnementen` | IS-SI-01 | Voorstel |
| Voorziening Centraal Aanmelden (CAMBO) | aanmelding-inname-afnemer | `POST /aanmeldingen`, `GET /aanmeldingen/{id}` bij de kernregistratie | IS-SI-01 | Voorstel |
| Voorziening Centraal Aanmelden (CAMBO) | verwerkingsuitkomst-afnemer | de melding `aanmelding-verwerkt` | IS-SI-01 | Voorstel |
| Voorziening Centraal Aanmelden (CAMBO) | afleverabonnement-afnemer | `POST /abonnementen` bij de kernregistratie | IS-SI-01 | Voorstel |

De dienstnamen volgen de [dienstenlijst](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/README.md) van Npuls-OKx/Public. `aanmelding-inname` staat daar nog niet en wordt hier voorgesteld.

## 4. Deze keten stelt voor waar de vorige beschreef

| | De keten onderwijsaanbod | Deze keten |
|---|---|---|
| Interactiepatroon in Public | OC-P&R, OC-SIS en OC-LMS, met endpoints en schema's | Geen |
| Stromen met een koppelingspecificatie | 7 van 7 | 0 van 7 |
| De bronvraag | Rustig genoeg voor een plaat gegevensoorsprong | Betwist op vier punten |

Elke eenheid draagt die stand. De vier bevindingen uit de tegenlezing raken precies de componenten hier: of de intake een bron is, of de kernregistratie bron is van de keuzedeelvoorkeur en van de opleidingsverbintenis, en of de kernregistratie en het studentvolgsysteem los te zien zijn.

Die worden een signalering en geen besluit. De koppelvlakdienst draagt dat beter dan het applicatiecomponent: een dienst zegt wat er moet kunnen, en welk component hem claimt is een tweede vraag.
