# npuls-huisstijl

Claude Code skill met de volledige Npuls huisstijl voor CEDA projecten. Bron van waarheid voor kleuren, typografie, vormentaal en framework-thema's (Slidev, Streamlit, R Shiny).

## Wat zit erin

```
npuls-huisstijl/
├── SKILL.md                     # Hoofdskill (brand overview + routing)
├── README.md                    # Dit bestand
│
├── references/                  # Gedetailleerde gidsen
│   ├── design-tokens.json       # Single source of truth voor kleuren/fonts/spacing
│   ├── slidev.md                # Slidev theming guide
│   ├── streamlit.md             # Streamlit theming guide
│   └── rshiny.md                # R Shiny theming guide
│
├── brand-guide/                 # Mensleesbare huisstijlgids
│   ├── Npuls_Huisstijlgids.html # Interactief met zijbalk-navigatie
│   ├── Npuls_Huisstijlgids.md   # Markdown versie
│   └── images/                  # 32 hoge-res screenshots uit originele PDF
│
└── assets/
    ├── shared/
    │   ├── Npuls_powerpoint-template.potx   # Originele PowerPoint template
    │   ├── svg/                 # Vormentaal (rings, pulse, chevron, starburst, arch)
    │   ├── illustrations/       # Nieuwe branded SVG illustraties
    │   ├── logos/               # Npuls logos (placeholder SVG's)
    │   ├── screenshots/         # PDF pagina screenshots (duplicaat brand-guide)
    │   └── potx-media/          # 101 PNGs + SVGs geëxtraheerd uit .potx
    │
    ├── slidev/                  # Slidev theme
    │   ├── styles/theme.css     # CSS variabelen + base styling
    │   └── layouts/             # Vue layouts (cover, default, image-left/right,
    │                            #              two-col, quote, section, end)
    │
    ├── streamlit/
    │   ├── streamlit-config.toml
    │   └── streamlit-custom.css
    │
    └── rshiny/
        └── rshiny-npuls-theme.R
```

## Installatie voor teamgenoten

Deze skill leeft in `cedanl/.github` onder `.claude/skills/`. Wie dit repo kloont en Claude Code gebruikt, krijgt de skill automatisch. Claude laadt `SKILL.md` als frontmatter en expandeert de references on-demand.

## Hoe Claude het gebruikt

1. Gebruiker vraagt iets in Npuls-stijl
2. Claude laadt `SKILL.md` (brand overview + routing)
3. Claude leest de relevante reference (slidev.md / streamlit.md / rshiny.md)
4. Claude gebruikt `design-tokens.json` voor exacte kleurcodes
5. Claude kopieert of verwijst naar assets uit `assets/<framework>/`

## Relatie tot `clidev`

Voor Slidev-presentaties is er al de `clidev` skill die een volledige projectworkflow levert (clone, `_template.md`, `npx slidev`). Die skill gebruikt de brand-assets en tokens uit **deze** skill als bron — niet duplicaten.

## Assets: bestaand + nieuw

Deze skill combineert drie bronnen:

1. **Officiële PDF huisstijlgids** — screenshots van alle 32 pagina's (`brand-guide/images/`)
2. **Officiële PowerPoint template** — .potx + alle 101 media-assets geëxtraheerd (`assets/shared/potx-media/`)
3. **Nieuwe SVG assets** — vormentaal en illustraties op basis van de brand-values (`assets/shared/svg/` + `assets/shared/illustrations/`)

## Bijwerken

Als de huisstijl verandert:

1. Update `references/design-tokens.json` (bron van waarheid)
2. Update `SKILL.md` als er nieuwe regels zijn
3. Voeg nieuwe assets toe in `assets/shared/` of framework-specifieke subfolders
4. Commit + push naar `cedanl/.github`

## Licentie

Npuls huisstijl © Npuls / Nationaal Groeifonds. Alleen voor officieel Npuls- en CEDA-gebruik.
