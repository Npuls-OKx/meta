# Interactieketenspecificatie: aanmelden, intake, inschrijven en roosteren tot de start

| | |
|---|---|
| **Document doel** | Legt vast welke koppelingen een instelling nodig heeft om een student van aanmelding naar een geroosterde verbintenis te brengen, en wat een leverancier daarvoor bouwt |
| **Doelgroep** | De implementatiespecialist en de tester bij een instelling of een leverancier, en wie een profiel of consumer bouwt |
| **Dient als input voor** | De bouw van de koppelvlakken, de testgevallen erbij, en de acceptatie van een opgeleverde koppeling |
| **Kaderstelling** | Het [informatiemodel OKx](../../../model/informatiemodel/informatiemodel.md), de [uitgangspunten](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) en hoofdplaat v1.7 |
| **Inhoud** | Zes interactiespecificaties met hun operaties en berichten, twee signaleringen, en de koppelvlakdiensten per applicatiecomponent |
| **Status** | Voorstel. Vijf van de zes stromen die deze keten draagt, staan op v1.7 zonder koppelingspecificatie |

## Leeswijzer

| Bestand | Wat erin staat |
|---|---|
| [signaleringen.md](signaleringen.md) | Twee punten die een besluit vragen |
| De zes interactiespecificaties | Het contract per koppelvlakdienst, met het bericht onder zijn operatie |

## 1. De informatiestromen

| Eenheid | Beelden | Van | Naar | Stroom op hoofdplaat v1.7 |
|---|---|---|---|---|
| IS-SI-01 | F3-04 | Voorziening Centraal Aanmelden (CAMBO) | Kernregistratie (KRS) | `Persoon(Student) Opleidingprogramma verbintenis`, zonder koppelingspecificatie |
| IS-SI-02 | F3-05, F3-06 | Intakesysteem | Kernregistratie (KRS) | Geen; het intakesysteem draagt geen stroom ([S1](signaleringen.md)) |
| IS-SI-03 | F3-07, F3-08 | Kernregistratie (KRS) | Studentvolgsysteem (SVS) | Geen ([S2](signaleringen.md)) |
| IS-SI-04 | F4-06 | Kernregistratie (KRS) | Planningssysteem | `Ontsluiten plaatsingsgroepen met studenten`, zonder koppelingspecificatie |
| IS-SI-05 | F4-07, F4-08 | Planningssysteem | Roostersysteem | `Verzoek tot roosteren leergelegenheid`, zonder koppelingspecificatie |
| IS-SI-06 | F4-10 | Kernregistratie (KRS) | Leermanagementsysteem (LMS) | `Student, opleidingprogramma verbintenis, relevante groepen`, zonder koppelingspecificatie |

Negen beelden uit de voorbeelduitwerking van leerroute 1 dragen deze keten. De keten begint waar de aanmelding de instelling binnenkomt: hoe een student zich bij de voorziening voor centraal aanmelden meldt (F3-03) wordt door AII beschreven. De knip met de keten [onderwijsaanbod ontsluiten](../interactie-onderwijsaanbod/README.md) ligt op de informatiestroom en niet op de procesfase: wat de specificatie fijnmaziger maakt hoort daar, wat de student plaatst en roostert hoort hier.

Veertien objecttypen bewegen door deze keten: `Aanmelding`, `Inschrijving`, `Persoon`, `Student`, `Plaatsingsgroep`, `Leergelegenheid`, `Lesgelegenheid`, `Medewerker`, `Leeruitkomst` en de vijf verbintenissoorten op opleiding, opleidingsprogramma, onderwijseenheid, leergelegenheid en lesgelegenheid.

## 2. Wat deze keten oplevert

| Partij | Wat zij eruit haalt |
|---|---|
| Instelling | De koppelingen die zij uitvraagt om een student van aanmelding naar rooster te brengen, met de aanduiding per eenheid |
| Leverancier | Het contract per koppelvlakdienst: welke endpoints zij bouwt en welke zij aanroept |
| Tester | De operaties met hun statuscodes en voorbeeldpayloads |

## 3. Deze keten stelt voor waar de vorige beschreef

| | De keten onderwijsaanbod | Deze keten |
|---|---|---|
| Interactiepatroon in Public | OC-P&R, OC-SIS en OC-LMS, met endpoints en schema's | Geen |
| Stromen met een koppelingspecificatie | 7 van 7 | 1 van 6 |
| De bronvraag | Rustig genoeg voor een plaat gegevensoorsprong | Betwist op vier punten |

Elke eenheid draagt die stand. De vier bevindingen uit de tegenlezing raken precies de componenten hier: of de intake een bron is, of de kernregistratie bron is van de keuzedeelvoorkeur en van de opleidingsverbintenis, en of de kernregistratie en het studentvolgsysteem los te zien zijn.

Die worden een signalering en geen besluit. De koppelvlakdienst draagt dat beter dan het applicatiecomponent: een dienst zegt wat er moet kunnen, en welk component hem claimt is een tweede vraag.
