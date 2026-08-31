# .agents

Toolneutrale agent-omgeving van OKx-meta (issue #115). Basisdocument voor agents: [AGENTS.md](../AGENTS.md) op de repo-root.

## Structuur

- [`skills/`](skills/): alle skills, één submap per skill met een `SKILL.md` (naam, beschrijving in de frontmatter; verder geen frontmatter-administratie). `.cursor/skills` en `.claude/skills` zijn symlinks naar deze map, zodat Cursor, Claude Code en Codex dezelfde bron zien.
- [`skills.json`](skills.json): het manifest. Per skill: naam, type (`okx-specifiek` of `extern`), doel, en voor externe skills de bron en de adaptatie-wrapper.
- [`../skills-lock.json`](../skills-lock.json): provenance van extern geïnstalleerde skills (formaat van de skills-CLI: bron-repo, bronpad, hash).
- [`skill-bronnen.md`](skill-bronnen.md): de vaste bronnenlijst waarover we zoeken, plus het selectieproces.

## Externe skills (register skills.sh)

Externe, professioneel geschreven skills worden gevendord via de skills-CLI, altijd **in de dev-container**:

```bash
npx skills find "business analysis"           # zoeken in het register
npx skills add <owner/repo> -s <skill> -a cursor -y --copy
npx skills update                              # bijwerken naar de laatste versies
npx skills list                                # wat staat er geïnstalleerd
```

Afspraken:

- **Nooit rechtstreeks bewerken.** Een externe skill blijft zoals gevendord, anders breekt het update-pad. OKx-aanpassingen gaan via een adaptatie-wrapper (voorbeeld: [`skills/business-analyse-okx/`](skills/business-analyse-okx/SKILL.md)), die de externe skill aanroept en de OKx-kaders erboven zet.
- **Na elke add of update**: manifest [`skills.json`](skills.json) bijwerken (doel, type, adaptatie) en de wijziging als gewone PR reviewen.
- **Review vóór gebruik**: gevendorde skills draaien met volledige agent-rechten; lees ze bij binnenkomst.

## Symlinks en Windows

De symlinks werken in de dev-container (Linux). Wie buiten de container op Windows uitcheckt heeft `git config core.symlinks true` en Developer Mode nodig; de dev-container is de norm ([.cursor/rules/dev-omgeving.mdc](../.cursor/rules/dev-omgeving.mdc)).
