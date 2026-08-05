# R Shiny — Npuls huisstijl

## Quickstart

```r
source("rshiny-npuls-theme.R")

library(shiny)
library(bslib)

ui <- page_sidebar(
  title = npuls_logo("App Naam", "Subtitel"),
  theme = npuls_theme(),
  sidebar = sidebar(
    tags$div(class = "npuls-section-label", "Sectie"),
    # inputs...
    npuls_rings_decoration()
  ),
  card(
    card_header("Titel"),
    # content...
  )
)
```

## Functies in `assets/rshiny/rshiny-npuls-theme.R`

| Functie | Gebruik |
|---------|---------|
| `npuls_colors` | named vector van alle brand-kleuren |
| `npuls_theme()` | bslib theme: zwarte navbar, Roze sidebar, Inter font, alle brand-kleuren |
| `npuls_logo(app_name, subtitle)` | Navbar logo: dot-mark + wordmark + "Moving Education." tagline |
| `npuls_rings_decoration(color, size, opacity)` | Concentrische ringen decoratie voor sidebar-onderkant |
| `npuls_ggplot_theme()` | ggplot2 theme |
| `npuls_color_scale()` | discrete color scale |
| `npuls_color_continuous()` | continue color scale (Roze → Blauw) |
| `npuls_palette(n)` | pak n kleuren in brand-volgorde |

## Logo in de navbar

De `npuls_logo()` functie bouwt de navbar titel op met het echte dot-mark SVG uit `assets/shared/logos/npuls-logo-white.svg`, de wordmark, "Moving Education." tagline, en een optionele app-naam:

```r
# Minimaal
npuls_logo()

# Met app-naam en subtitel
npuls_logo("NFWA", "Kansengelijkheidsanalyse")
```

De navbar is zwart (`#000000`) met een 4-kleurige gradiëntstreep eronder (Blauw → Groen → Geel → Oranje).

## Sidebar

De sidebar gebruikt Roze (`#F4D9DC`) als achtergrond. Inputs krijgen een witte achtergrond zodat ze afsteken tegen het roze. Sectielabels gebruiken de `.npuls-section-label` class (kleine uppercase letters met blauwe linkerborder):

```r
sidebar = sidebar(
  tags$div(class = "npuls-section-label", "Bestanden"),
  fileInput(...),
  hr(),
  tags$div(class = "npuls-section-label", "Instellingen"),
  selectInput(...),
  npuls_rings_decoration()   # altijd onderaan de sidebar
)
```

## Concentrische ringen decoratie

De `npuls_rings_decoration()` plaatst de karakteristieke gedeeltelijke concentrische ringen rechtsonder in de sidebar — een vast onderdeel van de Npuls vormentaal (zie `brand-guide/images/page_20.png`). Het SVG bestand staat ook in `assets/shared/svg/concentric-rings.svg`.

## ggplot2

```r
ggplot(df, aes(x, y, fill = cat)) +
  geom_col() +
  npuls_color_scale(aesthetics = "fill") +
  npuls_ggplot_theme() +
  labs(title = "Titel", subtitle = "Subtitel in grijs")
```

## plotly

```r
library(plotly)

plot_ly(df, x = ~x, y = ~y, color = ~cat,
        colors = unname(npuls_colors[c("blauw","oranje","groen","geel","roze")])) |>
  layout(
    font = list(family = "Inter, 'General Sans'", color = "#000000"),
    plot_bgcolor = "white",
    paper_bgcolor = "white"
  )
```

## Value boxes

```r
value_box(
  title = "Actieve studenten",
  value = "12.345",
  showcase = bsicons::bs_icon("people-fill"),
  theme = value_box_theme(bg = npuls_colors[["blauw"]], fg = "#FFFFFF")
)

# Groen voor succes
value_box(title = "Geslaagd", value = "87%",
  theme = value_box_theme(bg = npuls_colors[["groen"]], fg = "#FFFFFF"))

# Oranje voor aandacht
value_box(title = "Risico", value = "3",
  theme = value_box_theme(bg = npuls_colors[["oranje"]], fg = "#FFFFFF"))
```

## Goedgekeurde kleurencombinaties

Zie `brand-guide/images/page_12.png` voor de visuele referentie. Gebruik alleen:

- Zwart navbar + witte tekst + Blauw/Groen/Geel/Oranje accenten
- Roze sidebar + Blauw sectielabels + witte inputs
- Witte cards + Blauw linkerborder op card-header
- Blauwe knoppen (primair), Groene knoppen (succes/download)
