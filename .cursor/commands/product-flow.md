Start de OKx product-flow voor het opgegeven deliverable. $ARGUMENTS

Volg de skill `.agents/skills/okx-product-flow/SKILL.md` stap voor stap. Sla geen stap over, en loop geen stopmoment voorbij.

0. **Story**: als `<gebruiker>` wil ik `<X>` met als doel dat `<waarde>`. De gebruiker is een lezerspersona uit `.agents/personas/` of een rol die in de leerroute-uitwerking bestaat; nooit een systeem en nooit een verzonnen rol. Zonder benoemde gebruiker en waarde begint het werk niet.
1. **Acceptatiecriteria** met de persona `business-analyse-okx`: genummerd en toetsbaar, met per criterium een testgeval, vastgelegd in het issue. *Stopmoment: akkoord van de opdrachtgever.*
2. **Implementatieplan**, autonoom opgesteld.
3. **Tegenlezing van het plan** door een onafhankelijke agent in een verse context, die afkeurt op vier gronden en niet op volledigheid of smaak.
4. *Stopmoment: groen licht van de opdrachtgever op het plan.*
5. **Uitwerken** met de passende specialist-skill (informatiemodel of payload: `mbo-informatie-modelleur`; scenario: `okx-oeapi-scenario-uitwerking`; ontwerp: command `ontwerp-document`; ADR: command `adr-opstellen`). Daarna onafhankelijke review in verse subagent-contexten door drie sporen: tester (`okx-requirements-tester`), specialist (`okx-semantiek-review`, of `architecture-review` bij tooling) en schrijfstijl (`okx-schrijfstijl-review`). Geef de reviewers alleen het issue en het deliverable, niet deze conversatie.
6. **Waardevalidatie**: levert het geleverde de waarde uit de story. Vervolgpunten worden kleine iteraties.

Itereer tot de reviews slagen, maximaal drie ronden per poort; daarna escaleren naar de opdrachtgever met de openstaande bevindingen. Sluit af met het agent-rapport uit de skill in de PR-beschrijving.
