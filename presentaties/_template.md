---
theme: default
title: Titel van de presentatie
info: Korte omschrijving van de presentatie.
author: OKx - Onderwijskoppelingen (Npuls)
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
  enabled: false
transition: slide-left
mdc: true
---

<!-- De huisstijl komt uit style.css in de projectroot; die wordt automatisch
     door Slidev geladen. Geen <style> blok of theme-map nodig.
     Achtergronden via <div class="np-bg">, content via <div class="fill">. -->

<!-- TITELSLIDE (Slide1.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide1.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem 4rem; z-index: 1;">
  <h1 style="font-size: 3.2rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Titel</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 680px; line-height: 1.5; margin-bottom: 1rem;">
    Ondertitel of pakkende eenregelige samenvatting
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>OKx</strong> &middot; Onderwijskoppelingen
  </div>
  <div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Npuls &middot; 2026</div>
</div>

<!--
Sprekersnotities horen in een HTML-commentaarblok onderaan elke slide.
-->

---

<!-- AGENDA (Slide2.PNG) — tekst rechts, afbeelding links -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="margin-left: 42%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding-right: 3rem;">
  <p class="eyebrow">Wat gaan we bespreken</p>
  <h1 style="font-size: 2.2rem !important; margin-bottom: 1.4rem;">Programma</h1>
  <div style="display: flex; flex-direction: column; gap: 1rem;">
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">1</span>
      <div><strong>Onderwerp 1</strong><br/><span class="muted" style="font-size: 0.82rem;">Korte toelichting</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>Onderwerp 2</strong><br/><span class="muted" style="font-size: 0.82rem;">Korte toelichting</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Onderwerp 3</strong><br/><span class="muted" style="font-size: 0.82rem;">Korte toelichting</span></div>
    </div>
  </div>
</div>

---

<!-- HOOFDSTUKDIVIDER (Slide13/14/15.PNG) — witte tekst verplicht, geen bullets -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 1</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Hoofdstuktitel</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Ondertitel van het hoofdstuk</p>
  </div>
</div>

---

<!-- CONTENTSLIDE — bullets + accentkaart (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Slidetitel

<p class="np-subtitle">Een ondertitel die de slide in een zin samenvat.</p>

<div class="np-grid-2" style="margin-top: 0.3rem;">
<div style="font-size: 0.92rem; line-height: 1.7;">

- Punt **een** met een vetgedrukt kernwoord
- Punt twee
- Punt drie

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Kernpunt</h3>
    <p style="font-size: 1rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Een korte, krachtige boodschap in een accentkaart.
    </p>
  </div>
</div>
</div>

</div>

---

<!-- DRIE KAARTEN (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Slidetitel

<p class="np-subtitle">Drie punten naast elkaar in accentkaarten.</p>

<div class="np-grid-3" style="margin-top: 0.5rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Label</span>
    <h3 style="margin-top: 0.5rem;">Kaart 1</h3>
    <p class="muted" style="font-size: 0.84rem; margin: 0;">Korte toelichting bij de eerste kaart.</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Label</span>
    <h3 style="margin-top: 0.5rem;">Kaart 2</h3>
    <p class="muted" style="font-size: 0.84rem; margin: 0;">Korte toelichting bij de tweede kaart.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">Label</span>
    <h3 style="margin-top: 0.5rem;">Kaart 3</h3>
    <p class="muted" style="font-size: 0.84rem; margin: 0;">Korte toelichting bij de derde kaart.</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 0.8rem;">
  De <strong>kernboodschap</strong> van deze slide in een opvallende balk.
</div>

</div>

---

<!-- PIPELINE / PROCES (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe het werkt

<p class="np-subtitle">Drie stappen van invoer naar resultaat.</p>

<div class="np-pipeline" style="margin-top: 1.5rem;">
  <div class="np-step blue" style="flex: 1; max-width: 200px;">
    <strong style="font-size: 0.95rem;">Stap 1</strong>
    <small>Korte toelichting</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1; max-width: 200px;">
    <strong style="font-size: 0.95rem;">Stap 2</strong>
    <small>Korte toelichting</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1; max-width: 200px;">
    <strong style="font-size: 0.95rem;">Stap 3</strong>
    <small>Korte toelichting</small>
  </div>
</div>

<div class="np-proof-strip" style="justify-content: center; margin-top: 1.3rem;">
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Bewijspunt een</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Bewijspunt twee</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Bewijspunt drie</div>
</div>

</div>

---

<!-- TWEE KOLOMMEN MET KAARTEN (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Slidetitel

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: start;">
  <div class="np-card accent-green">
    <h3>Links</h3>
    <p class="muted" style="font-size: 0.86rem; margin: 0;">Toelichting in de linkerkaart.</p>
  </div>
  <div class="np-card accent-blue">
    <h3>Rechts</h3>
    <p class="muted" style="font-size: 0.86rem; margin: 0;">Toelichting in de rechterkaart.</p>
  </div>
</div>

</div>

---

<!-- CITAAT / HIGHLIGHT (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 0 2rem;">
  <div style="font-family: 'Cooper Light BT', serif; font-size: 1.8rem; line-height: 1.5; color: var(--np-blue); max-width: 700px;">
    "Citaat of kernboodschap die de aandacht trekt."
  </div>
  <div style="margin-top: 1.5rem; font-size: 0.9rem; color: var(--np-dark-gray);">&mdash; Naam, Functie</div>
</div>

</div>

---

<!-- CODE DEMO (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Slidetitel

```python {1|3-5|all}
# Stap 1: importeer de bibliotheek
import pandas as pd

# Stap 2: laad de data
df = pd.read_csv("data.csv")
print(df.head())
```

</div>

---

<!-- SCREENSHOT (Slide3.PNG) — afbeelding uit public/shots/ -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Zo ziet het eruit

<div style="display: flex; justify-content: center; margin-top: 0.2rem;">
  <img src="/shots/voorbeeld.png" style="max-height: 430px; width: auto; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.12);" />
</div>

</div>

---

<!-- TABEL (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Slidetitel

| Kolom A | Kolom B | Kolom C |
|---------|---------|---------|
| Waarde 1 | Waarde 2 | Waarde 3 |
| Waarde 4 | Waarde 5 | Waarde 6 |

</div>

---

<!-- ILLUSTRATIE + TEKST (Slide3.PNG) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Slidetitel

<div class="np-grid-2" style="margin-top: 1rem; align-items: center;">
<div style="font-size: 0.95rem; line-height: 1.8;">

- Punt een
- Punt twee
- Punt drie

</div>
<div style="display: flex; justify-content: center;">
  <img src="/npuls/powerpoint_illustrations/data.svg" style="width: 180px;" />
</div>
</div>

</div>

---

<!-- AFSLUITSLIDE (Slide17.PNG) — geen tekst -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
