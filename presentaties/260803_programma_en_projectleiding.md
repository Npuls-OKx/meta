---
theme: default
title: OKx — waar staan we
info: De koppelingspecificaties liggen er, we hebben release management en de repo-indeling geregeld, en we werken nu aan de keuzeregels.
author: OKx - Onderwijskoppelingen (Npuls)
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
  enabled: false
transition: slide-left
mdc: true
# De huisstijl levert eigen fonts via style.css; geen Google Fonts ophalen.
# Dat scheelt een blokkerende externe stylesheet in de head.
fonts:
  provider: none
---

<!-- TITELSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide1.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem 4rem; z-index: 1;">
  <h1 style="font-size: 3.3rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Waar staan we</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 660px; line-height: 1.5; margin-bottom: 1rem;">
    De specificaties liggen er. Nu het spannende deel: klopt het ook?
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>OKx</strong> &middot; 3 augustus 2026
  </div>
</div>

---

<!-- KERN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 1rem 2rem 0;">
  <div style="font-family: 'Cooper Light BT', serif; font-size: 1.9rem; line-height: 1.5; color: var(--np-blue); max-width: 720px;">
    Het schrijfwerk is grotendeels klaar. Vanaf nu draait het om de vraag of de sector zich erin herkent.
  </div>
</div>

<div class="np-proof-strip" style="justify-content: center; margin-top: 2.2rem;">
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Drie koppelingen beschreven</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Alles staat publiek</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Adviesgroep vandaag aan zet</div>
</div>

</div>

---

<!-- WAT ER LIGT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er nu ligt

<p class="np-subtitle">De kern van het werk: hoe de systemen in een school onderwijs aan elkaar doorgeven.</p>

<div class="np-pipeline" style="margin-top: 1.1rem;">
  <div class="np-step blue" style="flex: 1; max-width: 190px;">
    <strong style="font-size: 0.95rem;">Planning en rooster</strong>
    <small>Wanneer en waar het draait</small>
  </div>
  <div class="np-step orange" style="flex: 1; max-width: 190px;">
    <strong style="font-size: 0.95rem;">Leeromgeving (LMS)</strong>
    <small>Waar de student leert</small>
  </div>
  <div class="np-step green" style="flex: 1; max-width: 190px;">
    <strong style="font-size: 0.95rem;">Studentsysteem (SIS)</strong>
    <small>Inschrijving en resultaten</small>
  </div>
</div>

<p class="muted" style="font-size: 0.95rem; margin-top: 1.4rem; line-height: 1.7;">
Voor de reguliere leerroute is nu beschreven wat er tussen die systemen heen en weer gaat: welk bericht, wanneer, en in welke volgorde. Dat is waar leveranciers straks op bouwen.
</p>

<div class="np-bottomline" style="margin-top: 1.1rem;">
  Dit is het stuk waar het project om draait. De rest is randvoorwaarde.
</div>

</div>

---

<!-- RANDVOORWAARDEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee dingen die we onderweg geregeld hebben

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Release management</span>
    <h3 style="margin-top: 0.5rem;">Versienummers die iets zeggen</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Een leverancier kan aan het nummer zien of er werk aan de winkel is. Kleine correctie, iets erbij, of iets fundamenteels anders. Zonder die afspraak weet niemand wanneer hij moet ingrijpen.
    </p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Twee repositories</span>
    <h3 style="margin-top: 0.5rem;">Werkplaats en etalage</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Waar we denken en schuiven staat apart van wat we publiceren. Wie iets doorstuurt naar een instelling, weet zeker dat daar geen halffabricaat tussen zit.
    </p>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.3rem;">
Allebei saai. Allebei nodig: zonder dit kunnen we niets naar buiten brengen zonder het meteen weer terug te moeten halen.
</p>

</div>

---

<!-- WAAR WE NU AAN WERKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar we nu aan werken

<p class="np-subtitle">De keuzeregels. Klinkt klein, is het niet.</p>

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: start;">
<div style="font-size: 0.95rem; line-height: 1.75;">

Een school laat niet elke student elk keuzedeel kiezen. Dat kan logistiek niet. Maar hoe leg je vast wie wat mag kiezen, op een manier die overal hetzelfde werkt?

Die vraag kwam in juni uit de adviesgroep. We hebben hem uitgewerkt tot zestien eisen en een eerste vorm.

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Waarom nu</h3>
    <p style="font-size: 0.93rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Als wij dit niet vastleggen, verzint elke leverancier het zelf. Dat wordt vanzelf de standaard, en dan is het te laat om er nog iets van te vinden.
    </p>
  </div>
</div>
</div>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  Naarmate onderwijs flexibeler wordt, wordt <strong>bijna alles</strong> een keuze. Dit is de generieke oplossing, niet alleen voor keuzedelen.
</div>

</div>

---

<!-- PLANNING EN ZORGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Planning en zorgen

<div style="font-size: 0.9rem; margin-top: 0.5rem;">

| | |
| --- | --- |
| **19 augustus** | Koppelvlakspecificatie alpha. Inhoud staat, 3 punten open. Haalbaar. |
| **31 augustus** | Deel specificatiedocument af. **27 punten open.** In een vakantiemaand. |

</div>

<div class="np-grid-2" style="margin-top: 1rem; align-items: start;">
  <div class="np-card accent-yellow">
    <h3>Waar ik me zorgen over maak</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Niet de inhoud, maar de review. We hebben de sector nodig om te bevestigen dat dit klopt, en augustus is daar geen beste maand voor.
    </p>
  </div>
  <div class="np-card accent-blue">
    <h3>Wat dat betekent</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Of 31 augustus schuift, of we spreken scherper af wat "af" betekent. Liever het tweede: dan houden we tempo zonder te doen alsof.
    </p>
  </div>
</div>

</div>

<!--
Eerlijk blijven als er doorgevraagd wordt: de 27 open punten zijn feitelijk,
de inschatting over haalbaarheid is mijn oordeel.
-->

---

<!-- BESLISPUNTEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee dingen waar ik jullie voor nodig heb

<div class="np-grid-2" style="margin-top: 0.9rem; align-items: start;">
  <div class="np-card accent-orange">
    <span class="np-badge orange">1</span>
    <h3 style="margin-top: 0.5rem;">Wanneer gaat dit naar buiten?</h3>
    <p class="muted" style="font-size: 0.9rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Publiceren geeft leveranciers iets om op te reageren, maar legt ons ook vast. Mijn voorstel: pas na de kerngroep techniek, dus september.
    </p>
  </div>
  <div class="np-card accent-blue">
    <span class="np-badge blue">2</span>
    <h3 style="margin-top: 0.5rem;">Wat betekent "af" op 31 augustus?</h3>
    <p class="muted" style="font-size: 0.9rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Alles, met uitloop? Of een scherpere afbakening en de rest naar september? Ik heb geen voorkeur, maar wel een besluit nodig.
    </p>
  </div>
</div>

<p class="muted" style="font-size: 0.92rem; margin-top: 1.4rem;">
Verder niks. De inhoudelijke vragen liggen bij de adviesgroep en de kerngroep techniek, niet hier.
</p>

</div>

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
