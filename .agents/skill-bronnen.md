# Skill-bronnen

Vaste bronnenlijst voor het vinden van externe skills, naast het register van de skills-CLI. Reden: dat register is één kanaal en was op 26 augustus 2026 minutenlang onbereikbaar. Met een eigen lijst zoeken we over meerdere repositories tegelijk en kiezen we bewust in plaats van te nemen wat één register toont.

## Bronnen

Peildatum 31 augustus 2026, gesorteerd op sterren. De lijst is een startpunt, geen keurmerk: passendheid bij de OKx-kaders weegt zwaarder dan populariteit.

| Repository | Sterren | Waarvoor |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 280k | Agentisch skills-raamwerk en ontwikkelmethodiek |
| [anthropics/skills](https://github.com/anthropics/skills) | 173k | Referentie-skills van de leverancier |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 135k | Verzamelrepo met agents, skills en RAG-toepassingen |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 91k | Engineering-skills voor codeer-agents |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 74k | Curatielijst, ingang naar kleinere bronnen |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | 48k | Skills voor markdown- en documentwerk |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | 46k | Catalogus met lokale ontsluiting |
| [blader/humanizer](https://github.com/blader/humanizer) | 39k | Tekst ontdoen van AI-kenmerken, raakt ons taalkader |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 38k | Instructies, agents en configuraties |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 37k | Architectuur-, workflow- en sequentiediagrammen |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 28k | Redactionele diagrammen, in adoptie |

## Zoeken en kiezen

1. Zoek breed: `npx skills find "<zoekterm>"` en daarnaast `gh search repos "<zoekterm> skill" --sort stars`, plus de bronnen hierboven.
2. Weeg kandidaten op passendheid bij de OKx-kaders: taal (Nederlandse uitvoer), conventies (schrijfstijl, testgevallen), en of de skill onze werkwijze aanvult in plaats van doorkruist.
3. Vendor de gekozen skill: `npx skills add <owner/repo> -s <skill> -a cursor -y --copy`. Provenance komt in [`../skills-lock.json`](../skills-lock.json).
4. Vul het manifest [`skills.json`](skills.json) aan met naam, type, doel en de adaptatie-wrapper.
5. Externe skills nooit rechtstreeks bewerken. OKx-aanpassingen gaan via een wrapper, zoals bij de business-analyse-persona.

Bij een skill-behoefte geldt de skill-check uit [`skill-first`](../.cursor/rules/skill-first.mdc): eerst het manifest, dan deze bronnen, en pas daarna met de hand bouwen met de afwijking benoemd in de pull request.
