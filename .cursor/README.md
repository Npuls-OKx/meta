# Cursor-configuratie (`.cursor`)

Configuratie voor de **Cursor-editor** en de **AI-agents** die in deze repo worden gebruikt: herbruikbare commands, rules, hooks en skills. Doel is om werk in de kennisbasis **reproduceerbaar** en **consistent** te maken voor het hele team.

Uitleg voor bijdragers staat in [`doc/Bijdragen-voor-beginners.md`](../doc/Bijdragen-voor-beginners.md) (Deel B — Cursor en agents).

Sinds issue #115 is de agent-omgeving toolneutraal opgezet: het basisdocument is [`AGENTS.md`](../AGENTS.md) op de repo-root, en `skills/` is hier een **symlink** naar de canonieke map [`.agents/skills/`](../.agents/) (gedeeld met Claude Code en Codex). Commands, rules en hooks blijven Cursor-specifiek in deze map.
