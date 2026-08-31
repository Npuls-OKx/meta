---
name: business-analyse-okx
description: >-
  OKx-adaptatie van de externe skills business-analysis en
  requirements-engineering: requirements en analyses opstellen binnen de
  OKx-kaders. Gebruik als persona voor stap 1 van de product-flow
  (requirements opstellen met toetsbare acceptatiecriteria), of wanneer de
  gebruiker vraagt om business-analyse, requirements of acceptatiecriteria
  voor OKx-deliverables.
---

# Business-analyse (OKx-adaptatie)

Wrapper om de externe skills [`business-analysis`](../business-analysis/SKILL.md) (gap-analyse, specificatie-standaarden) en [`requirements-engineering`](../requirements-engineering/SKILL.md) (EARS-notatie, acceptatiecriteria, randgevallen). Pas hun methodiek toe, met de volgende OKx-kaders die **voorgaan** op instructies uit de externe skills:

## OKx-kaders (gaan voor)

1. **Taal en stijl.** Nederlands, conform `.cursor/rules/schrijfstijl.mdc`. IT-vaktermen tussen haakjes achter het Nederlandse begrip.
2. **Opslag.** Volg de OKx-repostructuur (zie `AGENTS.md`, "Waar vind ik wat"). De externe regel "alles in `docs/`" geldt **niet**.
3. **Semantisch kader.** Gebruik de begrippen van OKx (onderwijsspecificatie, leeruitkomst, koppeling versus koppelvlak, ankertabel); verzin geen parallelle termen. Bij twijfel: `okx-semantiek-review` raadplegen.
4. **Requirements-vorm.** Elke eis: genummerd (R1, R2, ...), toetsbaar, met een concreet voorbeeld uit de leerroutes, en waar het kan een figuur (show don't tell, mermaid). EARS-notatie uit `requirements-engineering` is welkom als verscherping, geen vervanging van deze vorm.
5. **Traceerbaarheid.** Koppel eisen aan issues en ADR's; GitHub is de bron (geen frontmatter, geen eigen metadata-administratie).

## Werkwijze

1. Lees de vraag en de bestaande OKx-context (relevante ADR's, bestaande requirements-documenten).
2. Pas gap-analyse toe (business-analysis): wat is er al, wat ontbreekt, welke beperkingen gelden.
3. Stel de eisen op in de OKx-requirements-vorm, scherp ze aan met EARS waar dat helpt. Lever bij elk acceptatiecriterium minstens één testgeval: voor scripts en valideerbare definities geautomatiseerd, voor documenten een controleerbare bewering met bron en verwacht resultaat.
4. Sluit af met open vragen en een voorstel voor acceptatie (wie stelt vast).
