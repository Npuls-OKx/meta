# Koppelingspecificaties

Per **koppeling** (gestandaardiseerde informatiestroom tussen twee referentiecomponenten) een eigen map met de koppelingspecificatie en de payload-specificaties voor de data binnen het afgekaderde informatiemodel van die koppeling. Het **koppelvlak** van een component is de verzameling van alle koppelingspecificaties die dat component raken. Terminologie: [ADR 0021](../../../dr/0021-koppeling-versus-koppelvlak-terminologie.md).

| Map | Koppeling | Status | Inhoud |
|---|---|---|---|
| [`gedeeld/`](gedeeld/) | (alle koppelingen) | Richtinggevend | Centrale onderwijsspecificatie-payload en lifecycle-uitwerking |
| [`oc-p-en-r/`](oc-p-en-r/) | OC naar Planning en Roostering | Alpha, voor stakeholder-review | Koppelingspecificatie, onderwijsaanbod-payload |
| [`oc-sis-krs-svs/`](oc-sis-krs-svs/) | OC naar SIS (KRS/SVS) | Concept, afgeleid, ter review | Koppelingspecificatie, resultaatstructuur/examenplan |
| [`oc-lms/`](oc-lms/) | OC naar LMS | Concept, afgeleid, ter review | Koppelingspecificatie; leermiddelkoppeling-payload volgt |

Gedeelde payload-specificaties staan **éénmaal centraal** in `gedeeld/` (ADR 0021). Elke koppelingspecificatie definieert een **gebruiksprofiel**: welke objecten en velden van de centrale payload die koppeling gebruikt. Voorbeeld: OC-SIS gebruikt de volledige leeruitkomst-laag, OC-P&R alleen leeruitkomst-ids als opaque sleutels (ADR 0023), OC-LMS de leeruitkomst-inhoudsvelden. Koppeling-specifieke payloads staan in de koppeling-map.

Scenario: LR1 (LR2 en LR3 als delta). Leidende prioriteringsvraag (onderwijsvoorbereiding): wat moeten OC-P&R, OC-LMS en OC-SIS uitgewisseld hebben om klaar te zijn voor de start van de student? Geen frontmatter in de documenten: auteurschap en datums via de git-historie, koppeling via issues en PR's (zie `../../README.md`).
