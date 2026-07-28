Start de OKx product-flow voor het opgegeven deliverable. $ARGUMENTS

Volg de skill `.agents/skills/okx-product-flow/SKILL.md` stap voor stap:

1. **Requirements** met de persona `business-analyse-okx`: genummerde, toetsbare eisen met acceptatiecriteria, samen met de gebruiker vastgesteld.
2. **Uitwerken** met de passende specialist-skill (informatiemodel of payload: `mbo-informatie-modelleur`; scenario: `okx-oeapi-scenario-uitwerking`; ontwerp: command `ontwerp-document`; ADR: command `adr-opstellen`).
3. **Onafhankelijke review** in verse subagent-contexten: tester (`okx-requirements-tester`) en specialist (`okx-semantiek-review`, of `architecture-review` bij tooling). Geef de reviewers alleen het requirements-document en het deliverable, niet deze conversatie.
4. **Itereren** tot beide reviews slagen (maximaal drie rondes, daarna escaleren naar de gebruiker).
5. **Afsluiten** met het agent-rapport (format in de skill) voor de PR-beschrijving.

Sla geen stappen over; vraag de gebruiker om vaststelling van de requirements voordat je uitwerkt.
