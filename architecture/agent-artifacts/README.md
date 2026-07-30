# Agent-artifacten (traceerbare AI-sessies)

Hier slaan we **projectaanvragen**, **featureplannen** en **ontwerpdocumenten** op die (mede) met **Cursor-agents** zijn opgebouwd. Zo blijft zichtbaar **wat** wanneer is ontstaan en **welke mensen** verantwoordelijk waren (**human in the loop**).

## Mappen

| Map | Inhoud |
|-----|--------|
| [`project-requests/`](project-requests/) | Iteratieve projectaanvragen (`/project-aanvraag`) |
| [`feature-plans/`](feature-plans/) | Featureplannen uit een request (`/maak-plan`) |
| [`design-docs/`](design-docs/) | Ontwerp per feature (`/ontwerp-document`) |

## Bestandsnaam

Gebruik **UTC of lokale tijd + korte slug** (één bestand per “lijn” van werk, geen overschrijven zonder versienummer):

`YYYYMMDD_HHmm_<korte-beschrijving-kebab-case>.md`

Voorbeeld: `20260319_1430_okx-koppelvlak-projectaanvraag.md`

Bij **grote herziening** van hetzelfde onderwerp: nieuw bestand met nieuwe timestamp of suffix `_v2`.

## Geen frontmatter

Documenten hier hebben **geen** YAML-frontmatter. GitHub is de bron: **auteurschap en datums** via de git-historie, **koppeling en traceerbaarheid** via issues en pull requests. Vermeld gerelateerde issues en bronnen in de **documenttekst** zelf, bijvoorbeeld met een contextregel onder de titel ("Relateert aan: #12") en een sectie *Gerelateerde uitwerkingen*. Human-in-the-loop blijft gelden: de mens die de PR opent is verantwoordelijk voor de inhoud.

Zie ook [`doc/Bijdragen-voor-beginners.md`](../../doc/Bijdragen-voor-beginners.md) (Cursor-workflow).
