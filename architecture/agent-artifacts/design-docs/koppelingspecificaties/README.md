# Koppelingspecificaties

Per **koppeling** (gestandaardiseerde informatiestroom tussen twee referentiecomponenten) een eigen map met de koppelingspecificatie en de payload-specificaties voor de data binnen het afgekaderde informatiemodel van die koppeling. Het **koppelvlak** van een component is de verzameling van alle koppelingspecificaties die dat component raken. Terminologie: [ADR 0021](../../../dr/0021-koppeling-versus-koppelvlak-terminologie.md).

| Map | Koppeling | Status | Inhoud |
|---|---|---|---|
| [`oc-p-en-r/`](oc-p-en-r/) | OC naar Planning en Roostering | Alpha, voor stakeholder-review | Koppelingspecificatie, onderwijsspecificatie-payload, onderwijsaanbod-payload, lifecycle |
| [`oc-sis-krs-svs/`](oc-sis-krs-svs/) | OC naar SIS (KRS/SVS) | Concept, afgeleid, ter review | Koppelingspecificatie, onderwijsspecificatie-payload, resultaatstructuur/examenplan, lifecycle |
| [`oc-lms/`](oc-lms/) | OC naar LMS | Concept, afgeleid, ter review | Koppelingspecificatie, onderwijsspecificatie-payload, lifecycle; leermiddelkoppeling-payload volgt |

Payload-specificaties zijn per koppeling **gedupliceerd** (ADR 0021): structuur en attributen kunnen per koppeling divergeren; elke kopie vermeldt bij welke koppeling hij hoort. De OC-P&R-versies zijn de meest uitgewerkte; kopieën dragen een divergentie-notitie.

Scenario: LR1 (LR2 en LR3 als delta). Leidende prioriteringsvraag (onderwijsvoorbereiding): wat moeten OC-P&R, OC-LMS en OC-SIS uitgewisseld hebben om klaar te zijn voor de start van de student? Geen frontmatter in de documenten: auteurschap en datums via de git-historie, koppeling via issues en PR's (zie `../../README.md`).
