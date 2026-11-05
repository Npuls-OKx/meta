# Cursor-configuratie (`.cursor`)

Configuratie voor de **Cursor-editor** en de **AI-agents** die in deze repository worden gebruikt: herbruikbare commands, rules, hooks en skills. Doel is om werk in de kennisbasis **reproduceerbaar** en **consistent** te maken voor het hele team.

Sinds issue #115 is de agent-omgeving toolneutraal opgezet: het basisdocument is [`AGENTS.md`](../AGENTS.md) op de repo-root, en `skills/` is hier een **symlink** naar de canonieke map [`.agents/skills/`](../.agents/) (gedeeld met Claude Code en Codex). Commands, rules en hooks blijven Cursor-specifiek in deze map.

De eerste stappen in Git en GitHub staan in [`project/bijdragen-voor-beginners.md`](../project/bijdragen-voor-beginners.md). Wat hieronder staat is de uitleg voor een mens die met Cursor in deze repository begint.

## Cursor naast een gewone editor

Een IDE is een programmeeromgeving waarin bewerken, een terminal en versiebeheer in één venster zitten. Voor deze repository werk je vooral met markdown, mappen en Git; dezelfde werkwijze, zonder dat er iets gebouwd hoeft te worden.

| | Een gewone editor | Cursor |
|---|---|---|
| Focus | Typen en opslaan | Typen, met taalmodellen in dezelfde omgeving |
| Context | Je opent zelf bestanden | Je koppelt bestanden of mappen aan een gesprek met `@` |
| Herhaling | Je onthoudt zelf de stappen | Commands met `/`, uit [`commands/`](commands/) |
| Basis | | Gebouwd op VS Code, dus de Git- en terminalbediening is herkenbaar |

Een agent is de assistent die in stappen met de repository werkt: bestanden inzien, tekstvoorstellen doen, en wijzigingen of terminalacties uitvoeren nadat jij ze hebt bevestigd. Jij bepaalt wat er in Git terechtkomt.

## Rules, commands en context

| Bron | Rol |
|---|---|
| [`rules/`](rules/) (`*.mdc`) | Voorwaarden waaronder de agent werkt, met `globs` en `alwaysApply` |
| [`commands/`](commands/) (`*.md`) | Herbruikbare opdrachten; typ `/` in de chat. De bestandsnaam zonder `.md` is de naam |
| [`hooks/`](hooks/) | Controlescripts die ingrijpen, zoals de guard die installaties naar de dev-container stuurt |
| `@` | Bestanden of mappen aan het gesprek koppelen |

Begin een deliverable met het command `/product-flow`: dat start de keten uit [`.agents/skills/okx-product-flow/SKILL.md`](../.agents/skills/okx-product-flow/SKILL.md), met de story, de acceptatiecriteria en de stopmomenten op hun plek.

## Praktisch

- **Source Control**, het takicoon links, geeft dezelfde commit- en push-stappen als de terminal, naast elkaar in beeld.
- Nieuwe bestanden horen in de juiste map; de indeling staat in [`AGENTS.md`](../AGENTS.md) onder "Waar vind ik wat".
- Agent-artifacten dragen **geen metadatakop**: GitHub is de bron voor auteurschap en datums. Zie [`architecture/agent-artifacts/README.md`](../architecture/agent-artifacts/README.md).
- Stem grote binaire bestanden eerst af met het team.
- Controleer een voorstel van een agent altijd inhoudelijk: juistheid, privacy, en geen vertrouwelijke gegevens.
- Mermaid rendert betrouwbaar op GitHub; PlantUML kan ernaast, maar niet in plaats daarvan.
