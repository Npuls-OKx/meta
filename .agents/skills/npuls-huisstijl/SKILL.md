---
name: npuls-huisstijl
description: Centrale Npuls huisstijlgids en brand-assets voor CEDA/Npuls projecten. Gebruik wanneer iemand iets maakt in de Npuls stijl — presentaties (Slidev, PowerPoint .potx), dashboards (Streamlit, R Shiny), documenten, visualisaties of branded assets. Levert design tokens, kleurcombinaties, typografie, vormentaal, illustraties en kant-en-klare thema's voor Slidev, Streamlit en R Shiny. Moeder-skill van clidev — gebruik deze voor de bronwaarheid, clidev voor Slidev-workflow.
---

# Npuls Huisstijl

> **Moving Education.**

Deze skill is de **single source of truth** voor de Npuls huisstijl binnen CEDA-projecten. Alle Npuls brand-assets, kleuren, typografie, vormentaal en framework-specifieke thema's (Slidev, Streamlit, R Shiny) staan hier.

Gebruik deze skill wanneer je:

- een Slidev presentatie maakt (zie ook de `clidev` skill voor de volledige presentatie-workflow)
- een Streamlit dashboard bouwt
- een R Shiny app of ggplot-visualisatie maakt
- een document, poster, social-post of andere visuele asset in Npuls-stijl produceert
- wilt weten welke kleuren, fonts of vormen "Npuls" zijn

## Relatie tot andere skills

| Skill | Scope |
|-------|-------|
| **npuls-huisstijl** (deze) | Brand-bronwaarheid: tokens, kleuren, fonts, vormen, assets |
| `clidev` | Slidev-workflow voor CEDA/Npuls presentaties (gebruikt de assets hier) |
| `slidev` | Generieke Slidev-kennis |

Als iemand een presentatie wil maken → start met `clidev`. Die skill gebruikt de brand-bronwaarheid uit deze skill.

## Brand-identiteit in één oogopslag

- **Tagline:** Moving Education.
- **Organisatie:** Npuls — Nationaal Groeifonds programma voor digitale innovatie in het hoger onderwijs (NL)
- **Toon:** energiek, nuchter, samenwerkend, vooruitkijkend
- **Vormentaal:** ronde pulsen, chevrons, starbursts, concentrische ringen, bogen

## Kleuren (primair palet)

| Kleur   | HEX       | RGB              | CMYK             | Gebruik |
|---------|-----------|------------------|------------------|---------|
| Oranje  | `#DD784B` | 221, 120, 75     | 0, 58, 75, 0     | Primair accent, H1/H2 |
| Zwart   | `#000000` | 0, 0, 0          | 0, 0, 0, 100     | Body-tekst |
| Roze    | `#F4D9DC` | 244, 217, 220    | 0, 14, 6, 0      | Zachte achtergrond |
| Blauw   | `#3D68EC` | 61, 104, 236     | 85, 65, 0, 0     | Links, bold, data |
| Geel    | `#F4D74B` | 244, 215, 75     | 5, 10, 80, 0     | Highlight, waarschuwing |
| Groen   | `#00AF81` | 0, 175, 129      | 85, 0, 60, 0     | Succes, positieve data |

Volledige tokens (inclusief neutrals, approved combinations en CSS variables) staan in [`references/design-tokens.json`](references/design-tokens.json).

### Goedgekeurde kleurencombinaties

De huisstijlgids definieert specifieke achtergrond/voorgrond-combinaties. Gebruik **alleen** deze combinaties voor hoofdvlakken:

- Oranje bg + Zwart tekst
- Zwart bg + Oranje tekst
- Roze bg + Blauw tekst
- Blauw bg + Roze tekst
- Geel bg + Groen tekst
- Groen bg + Geel tekst


## Typografie

| Font | Gewicht | Gebruik | Fallback |
|------|---------|---------|----------|
| General Sans | 400 Regular | Body | Inter, Arial |
| General Sans | 600 Semi-Bold | H1-H3, bold | Inter Semi-Bold |
| Kansas / Cooper Light BT | 300 | Quotes, intro's, subtitles | Georgia italic |

Nooit twee decoratieve fonts combineren. Laat General Sans het werk doen.

## Vormentaal

De Npuls vormentaal is ontleend aan het idee van **beweging en pulsen**. Vijf kernvormen:

1. **Pulse curve** — golvende lijn, suggereert dynamiek
2. **Concentrische ringen** — bron van impact, kenniscentrum
3. **Chevron / pijl** — richting, vooruitgang
4. **Starburst** — aandacht, nieuw
5. **Boog / halfcirkel** — verbinding, overgang

Kant-en-klare SVG's staan in `assets/shared/svg/`. Gebruik ze als decoratief element, niet als kerninhoud.

## Iconen en illustraties

- **Stijl:** lijn-iconen, 2px stroke, rond uiteinde, in één kleur
- Plaats iconen altijd in een van de primaire kleuren (niet in grijs)
- Illustraties: vlakke stijl, maximum 3 brand-kleuren per illustratie
- `assets/shared/illustrations/` bevat branded SVG-illustraties

## Fotografie

- Echte mensen in echte onderwijscontext
- Natuurlijk licht, warme tonen
- Geen stockfotografie-clichés
- Als foto's niet beschikbaar zijn: gebruik vormentaal als vervanging

## Frameworks

Voor framework-specifieke integratie, lees de betreffende reference:

- **Slidev** → [`references/slidev.md`](references/slidev.md) + `assets/slidev/`
- **Streamlit** → [`references/streamlit.md`](references/streamlit.md) + `assets/streamlit/`
- **R Shiny** → [`references/rshiny.md`](references/rshiny.md) + `assets/rshiny/`
Voor een complete Slidev-workflow (inclusief projectsetup) gebruik je de `clidev` skill — die bouwt voort op de assets hier.

## Brand-guide (mensleesbaar)

Voor een visuele gids met alle pagina's van de originele huisstijlgids, open:

- `brand-guide/Npuls_Huisstijlgids.html` (interactief, met zijbalk-navigatie)
- `brand-guide/Npuls_Huisstijlgids.md` (Markdown)
- `brand-guide/images/page_01.png` t/m `page_32.png` (screenshots)

## Werkwijze voor Claude

Wanneer je iets in Npuls-stijl maakt:

1. **Check of er een framework-specifieke skill is** (bv. `clidev` voor presentaties) — gebruik die als die bestaat
2. **Lees de relevante reference** in `references/` voordat je code schrijft
3. **Gebruik bestaande assets** (`assets/shared/svg/`, `assets/shared/illustrations/`, `assets/shared/logos/`) voordat je nieuwe maakt
4. **Volg de goedgekeurde kleurencombinaties** — niet zomaar kleuren mengen
5. **Design tokens als bron** — verwijs naar `references/design-tokens.json` voor HEX-codes, nooit hardcoden

## Installatie

Deze skill leeft in `cedanl/.github` onder `.claude/skills/npuls-huisstijl/`. Teamgenoten krijgen automatisch toegang via hun Claude Code setup als `.github` als repo is gekloond.

## Licentie

De Npuls huisstijl is eigendom van Npuls / Nationaal Groeifonds. Assets mogen alleen gebruikt worden voor officiële Npuls- en CEDA-doeleinden.
