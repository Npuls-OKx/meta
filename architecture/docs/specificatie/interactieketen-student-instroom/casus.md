# De casus: Jochem meldt zich aan

De vaste identificaties van deze keten. Elke voorbeeldpayload gebruikt ze, zodat dezelfde student en hetzelfde aanbod door de hele keten dezelfde uuid dragen. Wat uit de keten [onderwijsaanbod ontsluiten](../interactieketen-onderwijsaanbod/casus.md) komt, houdt daar zijn identificatie.

## Wat deze keten overneemt

| Wat | Objecttype | Identificatie | Versie | Naam |
|---|---|---|---|---|
| Het aanbod waarop Jochem zich meldt | `Opleidingsprogramma aanbod` | `8c494250-b67a-4666-a762-6f9ec1e70aff` | `0.1.0` | Regulier BOL 2026 |
| De specificatie erachter | `Opleidingsprogramma specificatie` | `7ae25c1e-ee27-43a2-a001-761ee39ea5c7` | `0.1.0` | Regulier BOL 2026 |
| De eenheid waarop de leeromgeving haar onderdeel zet | `Onderwijseenheid aanbod` | `04af26e6-96be-480a-8413-87a128164681` | `0.1.0` | B1-K1, leerjaar 1, periode 1 tot 4 |
| De gelegenheid binnen die eenheid | `Leergelegenheid` | `04070a96-01e0-4958-9f7e-69b429c72eec` | `0.1.0` | Baliegesprekken 101, periode 1 |
| Het opleidingsaanbod waaronder dat programma valt | `Opleiding aanbod` | `7aa6609f-1d1b-471a-a0f8-beae490d31b5` | `0.1.0` | Apothekersassistent 2026 |
| Het lokaaltype dat de roosteropdracht vraagt | `Onderwijslocatie type` | `skillslab` | | Skillslab met baliesimulatie |
| Het docentprofiel dat de roosteropdracht vraagt | `Expertise of functieprofiel` | `8e1dcda7-ef4e-45d0-931a-e47c3c77ddef` | | Apothekersassistent-docent met baliepraktijk |

## Wat deze keten toevoegt

| Wat | Objecttype | Identificatie | Toelichting |
|---|---|---|---|
| Jochem | `Persoon` | `b1f0c7d2-5a84-4e3b-9f61-2c7d8e45a013` | 17 jaar, komt van het vmbo |
| Jochem als student | `Student` | `c4a2e918-7b36-4d50-8e29-1f6b3a97d824` | Ontstaat bij de inschrijving, niet bij de aanmelding |
| De aanmelding | `Aanmelding` | `d7e3b065-9c41-4a82-b5d8-3e9f1c20a675` | April 2026, Apothekersassistent BOL |
| De verbintenis op de opleiding | `Opleiding aanbod verbintenis` | `e2c58f74-1d93-4b06-a7e5-8c4d9b31f206` | Toestand `aangemeld` |
| De verbintenis op het programma | `Opleidingsprogramma aanbod verbintenis` | `f9b4d1a8-6e27-4c35-9d80-5a2e7f84c139` | Toestand `aangemeld` |
| De plaatsingsgroep | `Plaatsingsgroep` | `a3d9e6c5-2f18-4970-8b43-6d1c5e92a748` | Ontstaat bij de intake |
| Het `eventId` van een melding | contracteigenschap, geen objecttype | `9f3c2e81-4d7a-4b56-8e30-1c6f5b29d407` | Elke meldingspayload in deze keten draagt deze waarde, zodat een toets op idempotentie dezelfde delivery kan herhalen |
| De verbintenis op de onderwijseenheid | `Onderwijseenheid aanbod verbintenis` | `12e0f8b6-74eb-4a1e-90ff-c130c4c71dda` | Jochem op B1-K1, leerjaar 1; gaat mee naar de leeromgeving in IS-SI-06 |
| De verbintenis op de leergelegenheid | `Leergelegenheid verbintenis` | `084ebac2-6ca8-44fc-b3f9-efca5b7bd1bd` | Jochem op Baliegesprekken 101, periode 1; beeld F4-10 beweegt haar naar de leeromgeving, en dat niveau staat open (W5 van IS-SI-06) |
| De geroosterde les | `Lesgelegenheid` | `2b47d9e6-5c81-4f03-a95d-8e16b7c43052` | Les 1, maandag 1 september 09:00 tot 11:00; ontstaat bij het roosteren (F4-08) |
| Het lokaal van die les | `Onderwijslocatie` | `3c9e1a85-6d72-4b18-8a40-9f25d8e61347` | Simulatieruimte 2.14, het lokaalnummer dat het lokaaltype is geworden |
| De docent op die les | `Medewerker` | `4a2d7f63-1b95-4e80-9c37-5d81a6f29e04` | Personeelsnummer 4711 |
| De verbintenis op de lesgelegenheid | `Lesgelegenheid verbintenis` | `7e94a26d-8c13-4f57-b021-3d75e8c4196a` | Jochem op les 1; gaat mee naar het studentkeuzesysteem in IS-SI-05 |
| De tweede plaatsingsgroep op diezelfde leergelegenheid | `Plaatsingsgroep` | `ca26d662-48fc-463d-b9d1-b1957ec3d102` | APO26-1B, de tweede van de twee groepen van 24 uit F4-07 |
| De roosteropdracht | `Verzoek tot Aanbod / Intekening op specificatie` | `da0a666e-04d4-4da4-811b-c22064cf28a1` | Roosteropdracht periode 1 cohort 2026, aangevraagd op 15 juni 2026 (F4-07) |
| De periode waarvoor wordt geroosterd | `Cohort / periode` | `2026-09-01` tot `2026-11-06` | Periode 1 van cohort 2026; period.json draagt geen eigen identificatie |

De toestand van een verbintenis loopt van `aangemeld` via `ingeschreven` naar wat de uitvoering ervan maakt. Welke waarden die reeks kent, staat in het schema dat haar draagt; deze keten stelt die reeks voor.
