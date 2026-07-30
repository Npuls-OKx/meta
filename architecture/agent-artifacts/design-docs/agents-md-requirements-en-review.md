# Requirements en reviewrapport AGENTS.md (proefrun product-flow)

Relateert aan: #115. Dit document legt de proefrun van de product-flow-keten op [AGENTS.md](../../../AGENTS.md) vast: de toetsbare eisen (stap 1), en de rapporten van de onafhankelijke tester en specialist die in verse subagent-contexten reviewden (stap 3). De uitwerking zelf is AGENTS.md; het agent-rapport staat in de PR-beschrijving.

## Eisen

| Eis | Omschrijving | Acceptatiecriterium |
|---|---|---|
| R1 | Repo-beschrijving | AGENTS.md beschrijft wat de repo is (publieke kennisbank, documentatie, geen code) met links naar de kerndocumenten. |
| R2 | Kernprincipes | De kernprincipes staan samengevat met verwijzing naar de bron `architecture/docs/principes.md`; inhoudelijk consistent met die bron. |
| R3 | Aannames en kaders | Scope (leerroutes 1-3, persona's), taal, semantisch kader (ankertabel, koppeling vs. koppelvlak) en de frontmatter-regel staan benoemd. |
| R4 | Harde regels | De vijf harde regels staan expliciet: nooit `*.archimate` aanraken, installaties alleen in de dev-container, 1 issue = 1 branch = 1 PR, product-flow verplicht, voorcontrole `validate-docs.py`. |
| R5 | Waar vind ik wat | Een tabel met de hoofdmappen; alle links verwijzen naar bestaande paden. |
| R6 | Agent-omgeving | Skills (canoniek `.agents/skills/` met symbolische links), manifest, commands, rules en hooks staan beschreven en kloppen met de repo. |
| R7 | Product-flow | De keten (requirements, uitwerking, onafhankelijke review, itereren, agent-rapport) is samengevat met het startcommand `product-flow`. |
| R8 | Externe skills | De werkwijze voor vendoren staat beschreven: `npx skills`, lock, manifest bijwerken, nooit rechtstreeks bewerken (adaptatie-wrapper). |
| R9 | Taal en stijl | Nederlands, conform `schrijfstijl.mdc` (geen em-dash, kort en feitelijk, bullets en tabellen boven proza). |
| R10 | Voorcontrole | `python3 scripts/validate-docs.py AGENTS.md` slaagt zonder problemen. |

## Testrapport (okx-requirements-tester, verse context)

Voorcontrole geslaagd: 1 bestand gecontroleerd, 0 problemen. Alle tien eisen gehaald, met per eis bewijs (bestaande paden, symbolische links geverifieerd, inhoud vergeleken met bronnen). Eindoordeel: GESLAAGD, geen bevindingen. Eén observatie zonder eis-gebrek: het "nooit rechtstreeks bewerken"-principe staat in de sectie Agent-omgeving en wordt niet herhaald onder "Skills toevoegen of bijwerken".

## Semantiekreview (okx-semantiek-review, verse context)

Steekproef van repo-beweringen klopte (paden, commands, skillnamen, symbolische links, ADR 0008 en 0010). Eindoordeel: GESLAAGD, zes bevindingen.

| # | Bevinding | Ernst | Afhandeling |
|---|---|---|---|
| 1 | "Geen frontmatter in agent-documenten" te absoluut; `SKILL.md` en `.mdc`-rules hebben een verplichte metadatakop. | belangrijk | Geherformuleerd met expliciete uitzondering voor `SKILL.md` en `.mdc`-rules. |
| 2 | Rules-opsomming noemde alles "altijd geldend" en week af van de bestandsnamen; `docs-style` en `architecture-artifacts` zijn bestandstype-gebonden. | klein | Bestandsnamen gebruikt en gesplitst in altijd geldend en bestandstype-gebonden. |
| 3 | Ankertabel-verwijzing noemde vier van de zes begrippenfamilies; de leeruitkomst ontbrak. | klein | Alle zes families benoemd (kader, beoogde leeruitkomst, specificatie, aanbod, verbintenis, resultaat), met de leeruitkomst als sleutel. |
| 4 | Kernprincipes noemden vier van de vijf principes; Uitbreidbaarheid ontbrak. | klein | Principe 5 toegevoegd. |
| 5 | "1 issue = 1 branch = 1 PR" stond niet in de aangehaalde bron CONTRIBUTING.md. | klein | Regel opgenomen in de workflow van CONTRIBUTING.md; verwijzing klopt nu. |
| 6 | IT-vaktermen zonder Nederlandse term: frontmatter, hook, symlinks. | klein | Bij eerste gebruik: metadatakop (frontmatter), controlescript (hook), symbolische links (symlinks). |

## Uitkomst

Eén iteratie: beide reviews GESLAAGD, alle bevindingen doorgevoerd, voorcontrole opnieuw schoon op AGENTS.md en CONTRIBUTING.md.
