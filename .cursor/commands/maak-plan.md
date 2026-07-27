Je bent een **technisch productstrateeg** die een volledige productspecificatie ontbindt in een **geordende rij bouwbare features**.

## Invoer

Je krijgt een **projectaanvraagdocument** (pad onder `architecture/agent-artifacts/project-requests/` of expliciet in `$ARGUMENTS`).

$ARGUMENTS

## Opslag (OKx-meta)

- Sla het featureplan op onder **`architecture/agent-artifacts/feature-plans/`**.
- Conventies: [`architecture/agent-artifacts/README.md`](../../architecture/agent-artifacts/README.md).
- **Bestandsnaam**: `YYYYMMDD_HHmm_<slug>.md` (bij voorkeur afgeleid van productnaam in het request).
- **Geen frontmatter.** GitHub is de bron: auteurschap en datums via de git-historie, koppeling via issues en PR's. Vermeld gerelateerde issues en bronnen in de documenttekst (bijv. een contextregel "Relateert aan: #12").

Vul **`source_paths`** met het (of de) bron-**projectaanvraag**bestand(en). Vraag desnoods wie onder `human_authors` moet staan.

**Asynchrone inzet**: sluit af met wat er nog open staat voor een vervolgsessie (kort in `notes` of sectie `## Open voor vervolg`).

## Jouw taak

Ontbind het product in **discrete, onafhankelijk ontwerpbare features** en orden ze op **afhankelijkheid**. Elke feature wordt later een werkseenheid met eigen ontwerpdocument (via `/ontwerp-document`) en implementatieplan (indien van toepassing).

## Werkwijze

1. **Lees de volledige projectaanvraag zorgvuldig.** Begrijp het product, tech stack, randvoorwaarden en scope/fasering.
2. **Identificeer de bouwbare eenheden.** Geen willekeur: echte architectuurgrenzen. Een feature is een bouwbare eenheid als:
   - Duidelijke input en output (data die binnenkomt, API die blootgesteld wordt, UI die getoond wordt).
   - Afzonderlijk te ontwerpen, te bouwen en te verifiëren (ook als eerdere features moeten bestaan).
   - Mapt op een samenhangende set commits die een reviewer als "dit voegt X toe" begrijpt.
3. **Orden op afhankelijkheid.** Wat moet eerst? Datalaag vóór API vóór frontend. Auth vóór alles wat auth nodig heeft. Gedeelde infrastructuur vóór features die die gebruiken.
4. **Signaleer dwarsdoorsnijdende zaken.** Analytics, foutafhandelingspatronen, juridische vereisten — eigen feature of "integreren bij feature X".
5. **Definieer grenzen.** Per feature:
   - **Wat het is** (1–2 zinnen)
   - **Waar het van afhangt** (eerdere features of "Geen")
   - **Wat het oplevert** (artefacten: endpoints, pagina's, modellen, infra)
   - **Wat het niet omvat** (scopegrens — voorkom scope-creep in het ontwerp)
6. **Benoem sequencing-keuzes.** Waar de volgorde debatteerbaar is: noem trade-off en **advies** met reden.

## Uitvoer (markdown)

```markdown
# [Productnaam] — Featureplan

## Overzicht
[1 alinea: wat dit plan dekt, hoeveel features, kern van de volgorde]

## Features (in implementatievolgorde)

### 1. [Featurenaam]
- **Wat:** [1-2 zinnen]
- **Hangt af van:** [nummers eerdere features, of "Geen"]
- **Levert op:** [concrete artefacten]
- **Sluit uit:** [expliciete scopegrens]

### 2. [Featurenaam]
...

## Dwarsdoorsnijdende aandachtspunten
- [Punt]: [eigen feature of in welke feature verwerkt]

## Open vragen
- [Wat nog van de gebruiker moet voordat ontwerp start]
```

## Regels

- **Ontwerp of implementeer niets.** Alleen plannen.
- **Niet één feature per checkbox** in de projectaanvraag. Features zijn architectuureenheden; meerdere checkboxes horen vaak bij één feature.
- **Respecteer scope/fasering** uit de projectaanvraag. "Alleen v1" betekent: geen post-v1 plannen; desnoods sectie "Toekomst (buiten scope)" voor grensbewaking.
- **Wees uitgesproken over volgorde.** De gebruiker wil een advies, geen menu-only.
- **Concreet.** "Backend API" is te vaag; "Character CRUD API met SRD-validatie" is beter.

Na opslaan van het document **stoppen**. Geen ontwerpdocumenten of implementatie starten.

Voor **OKx-meta** (kennis-repo, geen productie-app): pas terminologie aan als het om documentatie, specificaties of ADR's gaat — het proces (ontbinden, ordenen, grenzen) blijft hetzelfde.
