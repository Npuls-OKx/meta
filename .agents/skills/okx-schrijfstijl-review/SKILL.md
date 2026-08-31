---
name: okx-schrijfstijl-review
description: >-
  Onafhankelijke schrijfstijl-reviewer in de OKx product-flow: toetst een
  tekst tegen de schrijfstijl-rule en de vastgelegde stijl-lessen. Draait in
  een verse subagent-context, los van de maker, als eigen spoor naast tester
  en semantiek-specialist. Gebruik in stap 3 van okx-product-flow voor elk
  tekstueel deliverable, en los voor issue- en PR-teksten.
---

# Schrijfstijl-review

Rol: reviewer die de tekst niet zelf schreef. Input: alleen het te toetsen document of de te toetsen tekst, plus `.cursor/rules/schrijfstijl.mdc` en `.cursor/rules/docs-style.mdc`. Niet de makende conversatie.

## Toetslijst

Elke bevinding met regelnummer, letterlijk citaat en een concreet herschrijfvoorstel.

1. **Leestekens.** Geen em-dash of en-dash (ook niet als `&mdash;`); punt, komma of dubbele punt. Geen nadruk-accenten (én, dé, hét, zó, wél, óók): "één" alleen als telwoord dat anders met het lidwoord verward wordt, "vóór" en "ná" alleen als de betekenis erom vraagt.
2. **Kern.** Korte zinnen, geen uitweidingen, geen herhaling van wat elders staat. Boven circa vier A4: adviseer opknippen en verwijzen.
3. **Aard, niet stand.** Toelichtende tekst noemt geen aantallen, uitwerkingsstatussen, bereiken of maakproceslimieten; die leven in tabellen, platen en validatie.
4. **Geen definitie-echo.** Een toelichting herdefinieert niet wat een kolom, veld of begrip "is"; hij benoemt de rol (ouder, stap omlaag, bron). Definities leven in het begrippenkader of de skill.
5. **Referenties op één plek.** Verwijzingen leven in de tabel of bronkolom; toelichtingen herhalen ze niet.
6. **Nederlands.** IT-vaktermen tussen haakjes bij eerste gebruik; begrippenkader-termen voluit; geen verzonnen termen; geen onnodig Engels.
7. **Meta-taal blijft buiten de tekst.** Geen "kort", "samengevat", aanwijzingen aan de maker of verwijzingen naar het maakproces in het deliverable zelf.

## Oordeel

GESLAAGD of GEFAALD. Schendingen van punt 1, 2 of 3 zijn blokkerend; de rest weegt de reviewer met motivering. Bij GEFAALD: bevindingen terug naar de maker (stap 4 van de product-flow), herbeoordeling na herstel.

## Plaats in de product-flow

Eigen spoor in stap 3 van [`okx-product-flow`](../okx-product-flow/SKILL.md), naast [`okx-requirements-tester`](../okx-requirements-tester/SKILL.md) en [`okx-semantiek-review`](../okx-semantiek-review/SKILL.md), voor elk tekstueel deliverable. Ook los inzetbaar op issue-teksten, PR-beschrijvingen en comments; de schrijfstijl geldt voor elke agent-uiting.
