# De casus: Jochem meldt zich aan

De vaste identificaties van deze keten. Elke voorbeeldpayload gebruikt ze, zodat dezelfde student en hetzelfde aanbod door de hele keten dezelfde uuid dragen. Wat uit de keten [onderwijsaanbod ontsluiten](../interactie-onderwijsaanbod/casus.md) komt, houdt daar zijn identificatie.

## Wat deze keten overneemt

| Wat | Objecttype | Identificatie | Versie | Naam |
|---|---|---|---|---|
| Het aanbod waarop Jochem zich meldt | `Opleidingsprogramma aanbod` | `8c494250-b67a-4666-a762-6f9ec1e70aff` | `0.1.0` | Regulier BOL 2026 |
| De specificatie erachter | `Opleidingsprogramma specificatie` | `7ae25c1e-ee27-43a2-a001-761ee39ea5c7` | `0.1.0` | Regulier BOL 2026 |

## Wat deze keten toevoegt

| Wat | Objecttype | Identificatie | Toelichting |
|---|---|---|---|
| Jochem | `Persoon` | `b1f0c7d2-5a84-4e3b-9f61-2c7d8e45a013` | 17 jaar, komt van het vmbo |
| Jochem als student | `Student` | `c4a2e918-7b36-4d50-8e29-1f6b3a97d824` | Ontstaat bij de inschrijving, niet bij de aanmelding |
| De aanmelding | `Aanmelding` | `d7e3b065-9c41-4a82-b5d8-3e9f1c20a675` | April 2026, Apothekersassistent BOL |
| De verbintenis op de opleiding | `Opleiding aanbod verbintenis` | `e2c58f74-1d93-4b06-a7e5-8c4d9b31f206` | Toestand `aangemeld` |
| De verbintenis op het programma | `Opleidingsprogramma aanbod verbintenis` | `f9b4d1a8-6e27-4c35-9d80-5a2e7f84c139` | Toestand `aangemeld` |
| De plaatsingsgroep | `Plaatsingsgroep` | `a3d9e6c5-2f18-4970-8b43-6d1c5e92a748` | Ontstaat bij de intake |

De toestand van een verbintenis loopt van `aangemeld` via `ingeschreven` naar wat de uitvoering ervan maakt. Welke waarden die reeks kent, staat in het schema dat haar draagt; deze keten stelt die reeks voor.
