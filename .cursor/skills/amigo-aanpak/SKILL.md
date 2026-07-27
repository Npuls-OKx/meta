---
name: amigo-aanpak
description: >-
  Harness voor de AMIGO-aanpak (Edustandaard) binnen OKx: leidt stapsgewijs van
  scenario naar een bouwbare afsprakenset via scenario-analyse, gegevensanalyse,
  interactie-analyse, technologiekeuze, berichtspecificatie en
  interfacespecificatie. Routeert naar de juiste substap-skill of stapbeschrijving.
  Gebruik wanneer de gebruiker de AMIGO-aanpak, een specifieke AMIGO-stap of het
  komen tot bouwbare uitwisselspecificaties voor het OKx OEAPI consumer-profiel
  aan de orde stelt.
disable-model-invocation: true
---

# AMIGO-aanpak (skill-harness)

AMIGO leidt ketenpartijen stapsgewijs naar een **bouwbare afsprakenset**
(uitwisselspecificatie). Bron: [Edustandaard — AMIGO aanpak](https://www.edustandaard.nl/amigo/aanpak/)
en §2.3 van het OKx OEAPI consumer-profiel. Deze harness bundelt de stappen en
verwijst per stap naar de skill of stapbeschrijving die hem uitwerkt.

## Bron van waarheid

- Profiel: `architecture/docs/specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md` (§2.3 Projectaanpak AMIGO).
- Release-roadmap: [`doc/release-management/Release-management-meta.md`](../../../doc/release-management/Release-management-meta.md) §8 (`v0.1.0` milestone 3 → `v1.0.0` ecosysteem compleet).
- Stappen worden **iteratief** doorlopen: een keuze in bericht/interface kan aanleiding zijn scenario, gegevens of interacties aan te scherpen.

## Ladder: informatiestroom → koppeling → koppelvlak

| Laag | Wat | AMIGO-stap | Waar vastgelegd |
| --- | --- | --- | --- |
| **Informatiestroom** | Conceptuele gegevensbeweging tussen ketenpartners | 1 (scenario) + input 2–3 | meta: scenario's, informatiestromenplaat |
| **Koppeling** | Gestandaardiseerde realisatie van stromen (bericht + interactie, nog geen volledige endpoints) | 3–5 | meta (+ spec bij overname) |
| **Koppelvlak** | Technische uitwerking: **meerdere endpoints** per koppeling | 6 | **spec**-repo (OpenAPI) |

Op basis van **alle gestandaardiseerde koppelingen** worden uiteindelijk **alle koppelvlakken** gebouwd. Milestone 3 levert de eerste set koppelingen voor OC P (LR1–LR3) in meta **`v0.1.0`**; **`v1.0.0`** volgt wanneer stromen, koppelingen en koppelvlakken compleet zijn.

## Stappen en routering

| # | AMIGO-stap            | Levert (onderdeel afsprakenset) | Uitgewerkt in |
| - | --------------------- | ------------------------------- | ------------- |
| 1 | Scenario-analyse      | Scenariobeschrijving            | skill [`okx-oeapi-scenario-uitwerking`](../okx-oeapi-scenario-uitwerking/SKILL.md) · [stappen/1-scenario-analyse.md](stappen/1-scenario-analyse.md) |
| 2 | Gegevensanalyse       | Informatiemodel (→ berichtspec) | skill [`mbo-informatie-modelleur`](../mbo-informatie-modelleur/SKILL.md) · [stappen/2-gegevensanalyse.md](stappen/2-gegevensanalyse.md) |
| 3 | Interactie-analyse    | Interactiepatronen              | [stappen/3-interactie-analyse.md](stappen/3-interactie-analyse.md) |
| 4 | Technologiekeuze      | Transport/beveiliging/standaarden | [stappen/4-technologiekeuze.md](stappen/4-technologiekeuze.md) |
| 5 | Berichtspecificatie   | Berichten (structuur/constraints/syntax) + vocabulaire | [stappen/5-berichtspecificatie.md](stappen/5-berichtspecificatie.md) |
| 6 | Interfacespecificatie | Endpoints + aanroep             | [stappen/6-interfacespecificatie.md](stappen/6-interfacespecificatie.md) |

> **OKx-nummering.** Het informatiemodel (stap 2, gegevensanalyse) is de directe
> **leg-up naar de berichtspecificatie** (stap 5). Waar in OKx-uitwerkingen over
> "de berichtspecificatie-stap" wordt gesproken, begint dat bij dit
> informatiemodel — daarom hangt [`mbo-informatie-modelleur`](../mbo-informatie-modelleur/SKILL.md) aan zowel stap 2 als de input van stap 5.

## Werkvolgorde

```text
1. Scenario-analyse  ──►  2. Gegevensanalyse ──┐
                          3. Interactie-analyse ┤
                                                 ▼
                          4. Technologiekeuze
                                 ├─► 5. Berichtspecificatie ──┐
                                 └─► 6. Interfacespecificatie ─┴─►  Afsprakenset
```

## Gebruik

1. Bepaal in welke AMIGO-stap de vraag valt (tabel hierboven).
2. Open de bijbehorende **skill** (indien aanwezig) of **stapbeschrijving** in [`stappen/`](stappen/).
3. Blijf **binnen** het consumer-profiel en de ankertabel/§12.5; gaps → signalering (§9), geen OEAPI-kernwijziging.
4. Houd het per stap op het afgesproken niveau: analyse blijft analyse tot het team om bericht-/interfacedetail vraagt.

## Status

- **Uitgewerkt:** stap 1 (scenario) en stap 2 (informatiemodel) hebben een eigen skill.
- **Kader (TO-DO):** stap 3–6 zijn als stapbeschrijving aanwezig en worden in latere iteraties tot volwaardige skills uitgewerkt.

## Governance

OKx-meta: issues en PR's; **alleen OKx-team merge**; link PR aan issues
(`Fixes #…` / `See also #…`). Zie `.cursor/rules/okx-governance.mdc`.
