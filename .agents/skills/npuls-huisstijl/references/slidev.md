# Slidev — Npuls huisstijl

> Voor een volledige presentatie-workflow gebruik de `clidev` skill. Deze file is de **bronwaarheid** voor de Slidev-styling die clidev gebruikt.

## Twee manieren om Slidev te theme'en

| Aanpak | Wanneer |
|--------|---------|
| **`theme: ./theme`** lokaal (clidev-style) | Standaard binnen het `clidev-presentaties` project. Alles staat al ingesteld. |
| **Kopieer losse bestanden** vanuit `assets/slidev/` | Voor losse Slidev projecten buiten clidev. Kopieer `styles/`, `layouts/` en `components/` naar je project's `theme/` folder. |

## Frontmatter template

```yaml
---
theme: ./theme
title: [Titel]
info: |
  [Korte beschrijving]
author: CEDA - Centre for Educational Data Analytics
colorSchema: light
layout: cover
class: text-left
transition: slide-left
fonts:
  sans: 'General Sans'
  serif: 'Kansas'
---
```

## Layouts (afgeleid van de officiële .potx)

De 13 layouts in master 1 van `Npuls_powerpoint-template.potx` mappen 1-op-1 naar Slidev layouts in `assets/slidev/layouts/`:

| .potx layout | Slidev layout | Gebruik |
|-------------|---------------|---------|
| Titeldia | `cover.vue` | Openingsslide met groot titelblok, logo links-boven, vormgraphic rechts-onder |
| Inhoud | `toc.vue` | Agenda met grote cirkel-graphic links |
| Titel en tekst | `default.vue` | Standaard content slide |
| Tekst klein - 2 koloms | `two-col-text.vue` | Twee tekst-kolommen |
| Inhoud van twee | `two-col.vue` | Twee contentblokken |
| Tekst en afbeelding 1 | `image-right.vue` | Tekst links, beeld rechts |
| Tekst en afbeelding 2 | `image-left.vue` | Beeld links, tekst rechts |
| Tekst en vorm-blokken | `shapes-grid.vue` | Tekst links, 3x2 vormen-grid rechts |
| Afbeeldingen en vormen | `gallery.vue` | Beeld/vorm mozaïek |
| Quote | `quote.vue` | Grote quote, gecentreerd |
| Stappen | `steps.vue` | Genummerde stappen met iconen |
| Alleen titel | `title-only.vue` | Sectiescheider kort |
| Partnerslide | `partner.vue` | Logo/partner showcase |

Extra layouts uit master 2 (Sectiescheider, Tussendia, Einddia) zitten in `section.vue`, `intermezzo.vue`, `end.vue`.

## CSS variabelen

```css
:root {
  --npuls-orange: #DD784B;
  --npuls-black: #000000;
  --npuls-pink: #F4D9DC;
  --npuls-blue: #3D68EC;
  --npuls-yellow: #F4D74B;
  --npuls-green: #00AF81;
}
```

## Mermaid

```markdown
​```mermaid {scale: 0.55}
graph LR
    A[Input] --> B[Process] --> C[Output]
    style A fill:#3D68EC,stroke:#DD784B,color:#fff
    style B fill:#DD784B,stroke:#3D68EC,color:#fff
    style C fill:#00AF81,color:#fff
​```
```

## Decoratieve vormen

Plaats concentrische ringen of pulse curves rechts-onder als signature-accent:

```html
<img src="/shared/svg/concentric-rings.svg" class="absolute bottom-4 right-4 w-40 opacity-90" />
```
