---
theme: default
title: "Kerngroep techniek, 14 oktober 2026"
info: "Kerngroep techniek 14 oktober 2026, online: de stand van de vijf punten van 30 september, de voorbeelduitwerking per fase, de scope van het informatiemodel en twee besluiten die blijven liggen."
author: OKx - Onderwijskoppelingen (Npuls)
highlighter: shiki
colorSchema: light
lineNumbers: false
drawings:
  persist: false
  enabled: false
transition: slide-left
mdc: true
fonts:
  provider: none
---


<!-- 1. TITEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide1.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem 4rem; z-index: 1;">
  <h1 style="font-size: 3.2rem; line-height: 1.15; margin-bottom: 0.8rem; color: var(--np-ink);">Kerngroep techniek</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 36rem;">Voorbeelduitwerking per fase &middot; Scope van het informatiemodel &middot; Versionering &middot; Twee besluiten</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 14 oktober 2026 &middot; online</div>
</div>

<!--
Online sessie, twee weken na Amersfoort. Opzet nog af te stemmen. Twee van de vijf punten van
30 september zijn niet beslecht, en op de versionering kwam weerstand uit de werkgroep techniek.
Die twee besluiten zijn het doel van vandaag; de voorbeelduitwerking is het bewijs dat er iets
ligt om op te besluiten.
-->

---

<!-- SECTIE: STAND VAN ZAKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 1</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Stand van zaken</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Wat er met de vijf punten van 30 september is gebeurd</div>
</div>

<!--
Sectiescheiding. Het eerste deel kijkt terug: de vijf gevraagde punten van 30 september, de
doorvoer over beide repositories, en wat dat zegt over waar het werk heen gaat.
-->

---

<!-- 2. GEVRAAGD OP 30 SEPTEMBER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd op 30 september

<div style="font-size: 0.86rem; line-height: 1.55; margin-top: 0.5rem;">

| Gevraagd | Stand op 9 oktober |
|---|---|
| **Feedback** op de voorbeelduitwerking: vorm, detail, scope | Gekomen. [meta PR 252](https://github.com/Npuls-OKx/meta/pull/252) is gemerged; het werk loopt door als acht fase-pull requests met 38 verantwoorde bevindingen |
| **Review** op de openstaande pull requests, te beginnen bij [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104) | Op gang: PR 104 draagt 14 opmerkingen en 8 reviews. De vijf andere open pull requests in Public staan op draft en vragen dus geen review |
| **Besluit** koppeling-ID: nu een indeling vastleggen, of wachten | Niet genomen. [Public #107](https://github.com/Npuls-OKx/Public/issues/107) staat open met twee reacties |
| **Besluit** reviewdoorloop: welke termijn, en wie reviewt wat | Niet genomen |
| **Input** op het versioneringsvoorstel: sluit dit aan op de eigen releasepraktijk | Gekomen, met weerstand op de complexiteit en de uitwisselbaarheid. [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) staat nog op draft |

</div>

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.7rem;">
Twee van de vijf punten zijn besluiten die blijven liggen. Die staan vandaag voorop, in deel 4.
</div>

</div>

<!--
Bron: de slide Gevraagd uit het deck van 30 september, met de stand van vandaag uit GitHub. Vijf
punten, en de twee besluiten zijn precies de punten die niet zijn beslecht. Dat is geen verwijt:
de sessie van 30 september was vol en de besluiten vroegen meer dan de tijd die er was. Maar ze
blijven nu twee weken staan, en het koppeling-ID blokkeert de naamgeving in de specificaties.
De weerstand op de versionering kwam uit de werkgroep techniek van 1 oktober; die ligt bij
Garik en Edo, die documentatie uitwisselen.
-->

---

<!-- 3. WAAR HET WERK HEEN GING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar het werk heen ging

<div style="display:grid;grid-template-columns:12rem 1fr 1fr;gap:0.55rem 1.2rem;align-items:center;margin-top:1rem;max-width:80%;">
<div></div>
<div style="font-size:0.8rem;color:var(--np-mid-gray);text-align:center;font-weight:600;">meta</div>
<div style="font-size:0.8rem;color:var(--np-mid-gray);text-align:center;font-weight:600;">Public</div>

<div style="font-size:0.95rem;">Pull requests gemerged</div>
<div style="text-align:center;font-size:1.6rem;font-weight:700;color:#00AF81;">16</div>
<div style="text-align:center;font-size:1.6rem;font-weight:700;color:#C4675A;">1</div>

<div style="font-size:0.95rem;">Issues gesloten</div>
<div style="text-align:center;font-size:1.6rem;font-weight:700;color:#00AF81;">34</div>
<div style="text-align:center;font-size:1.6rem;font-weight:700;color:#C4675A;">0</div>

<div style="font-size:0.95rem;">Issues open</div>
<div style="text-align:center;font-size:1.15rem;color:var(--np-dark-gray);">100</div>
<div style="text-align:center;font-size:1.15rem;color:var(--np-dark-gray);">51</div>

<div style="font-size:0.95rem;">Pull requests open</div>
<div style="text-align:center;font-size:1.15rem;color:var(--np-dark-gray);">19</div>
<div style="text-align:center;font-size:1.15rem;color:var(--np-dark-gray);">6, waarvan 5 draft</div>
</div>

<div style="margin-top:1.1rem;font-size:0.95rem;line-height:1.5;max-width:80%;">
Public draagt de artefacten waarmee een leverancier bouwt. Daar sloot een pull request in negen dagen.
</div>

</div>

<!--
Cijfers uit GitHub, 1 tot en met 9 oktober, beide repositories. Het verschil is de boodschap: in
meta liep het gereedschap en de voorbeelduitwerking door, in Public stond de releaselijn vrijwel
stil. Dat is dezelfde lijn als de slide "Veel verzet, weinig afgerond" van 30 september, nu
scherper. Inschatting van de maker, te overrulen: de draft-status is hier de rem, want vijf van
de zes open pull requests in Public vragen formeel geen review en blijven daarom staan.
-->
