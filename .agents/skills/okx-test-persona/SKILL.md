---
name: okx-test-persona
description: >-
  OKx-testpersona: schrijft en reviewt testgevallen voor scripts en
  valideerbare definities, met de OKx-conventies voor testlocatie,
  given-when-then en rapportage. Gebruik in stap 1 van de product-flow om
  testgevallen bij de acceptatiecriteria op te stellen, in stap 2 om ze te
  implementeren, en in stap 3 als naslag voor de tester. Ook bij elke vraag
  om testgevallen, teststructuur of testdekking voor een OKx-script.
---

# Testpersona (OKx-adaptatie)

Wrapper om de externe skill [`test-driven-development`](../test-driven-development/SKILL.md) (rood-groen-refactor, arrange-act-assert oftewel voorbereiden, uitvoeren en toetsen, testpiramide, DAMP boven DRY, anti-patronen). Pas die methodiek toe binnen de OKx-kaders; bij strijd gaan die kaders voor.

## OKx-kaders (gaan voor)

De conventies voor testlocatie, raamwerk, given-when-then, taal en rapportage staan in [`product-flow`](../../../.cursor/rules/product-flow.mdc). Deze wrapper voegt er een kader aan toe:

- **Onafhankelijke verwachtingen.** Een testgeval berekent of telt zijn verwachte waarde zelf, los van de huidige inhoud van de repository. Geen hardgecodeerde momentopname (bijvoorbeeld een vast aantal boom-items) die stilletjes veroudert zodra de repo groeit; zie de [reviewbevinding op PR 178](https://github.com/Npuls-OKx/meta/pull/178).

## Wat een goed testgeval is

- **Eén positief geval.** De gangbare, correcte invoer levert het verwachte resultaat op.
- **Negatieve gevallen per faalmodus.** Voor elke manier waarop het script of de definitie kan falen (ontbrekend bestand, kapotte link, verkeerd formaat, dubbele waarde) een eigen testgeval met de bijbehorende foutmelding of exitcode.
- **Randgevallen.** Lege invoer, grensbestanden, ontbrekende afhankelijkheden (bijvoorbeeld een niet-gecheckte Public-checkout) en de overgang tussen geldig en ongeldig.

Een testgeval dat niet in een van deze categorieën past, dekt waarschijnlijk niets nieuws af.

## Plaats in de product-flow

Testgevallen horen bij stap 1: samen met de acceptatiecriteria opgesteld en ter controle aangeboden aan de mens, vóór de uitwerking begint (issue #172). Zonder vastgestelde testgevallen geen uitwerking.

In stap 2 implementeert de specialist-skill eerst de tests, dan de productiecode: rood (test faalt), groen (minimale implementatie), refactor. In stap 3 loopt de tester (`okx-requirements-tester`) de testgevallen één voor één af tegen de opgestelde lijst; afwijkingen zijn een bevinding, geen interpretatieruimte.

## Werkwijze

1. Lees de acceptatiecriteria van het deliverable.
2. Leid per criterium ten minste één testgeval af: het positieve geval, de faalmodi, de randgevallen.
3. Schrijf de testgevallen als tabel (methode, given, then) voor het stopmoment met de mens.
4. Na akkoord: implementeer de tests eerst, dan de code; draai de suite en noteer de werkelijke uitkomst per testgeval.
5. Neem de tabel met uitkomsten op in de PR-beschrijving.
