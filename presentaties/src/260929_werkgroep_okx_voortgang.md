---
theme: default
title: "OKx kerngroep techniek: voortgang juni tot september 2026"
info: "Voortgangsupdate van de kerngroep techniek voor de werkgroep OKx: wat er sinds juni is opgeleverd, in businesstaal."
author: OKx - Onderwijskoppelingen (Npuls)
highlighter: shiki
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
  <h1 style="font-size: 3rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Van verhaal naar afspraak</h1>
  <div style="font-size: 1.15rem; color: var(--np-ink); margin-bottom: 0.9rem;">Wat de kerngroep techniek bouwde, juni tot september</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; werkgroep OKx &middot; september 2026</div>
</div>

<!--
Doel van dit blok: de werkgroep in vijf minuten laten zien dat het techniekspoor van praten naar
afspraken is gegaan. Geen techniek uitleggen, wel wat er nu ligt en wat de sector eraan heeft.
-->

---

<!-- 2. VAN JUNI NAAR NU -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# In juni een verhaal, nu een afspraak

<div class="np-pipeline" style="margin-top: 1.5rem;">
  <div class="np-step blue" style="flex: 1;">
    <carbon-map style="font-size: 2rem; color: var(--np-blue);" />
    <strong style="font-size: 0.9rem;">Juni: de reis</strong>
    <small>hoe onderwijs ontstaat, plant en uitvoert, verteld als scenario</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1;">
    <carbon-partnership style="font-size: 2rem; color: var(--np-orange);" />
    <strong style="font-size: 0.9rem;">Zomer: de taal</strong>
    <small>begrippen en informatiemodel, getoetst bij leveranciers en scholen</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1;">
    <carbon-document style="font-size: 2rem; color: var(--np-green);" />
    <strong style="font-size: 0.9rem;">September: de afspraak</strong>
    <small>openbaar gepubliceerd, met versie en datum, klaar om op te bouwen</small>
  </div>
</div>

<div class="np-card accent-green" style="margin-top: 1.5rem; font-size: 1rem; line-height: 1.6;">
  <strong>Wat dat betekent:</strong> een leverancier kan nu lezen wat zijn systeem moet kunnen uitwisselen, en een school kan erop sturen. Waar het in juni nog gesprek was, staat het nu zwart op wit.
</div>

</div>

<!--
Bronnen: releasepakket koppelvlakspecificatie v0.0.1 (18 augustus) en v0.0.2 (1 september) in
Npuls-OKx/Public; informatiemodel v0.1 en begrippenlijst v0.2 gepubliceerd 18 september.
Niet noemen tenzij gevraagd: de werkwijze met issues, branches en reviews.
-->

---

<!-- 3. DE AFSPRAKEN DIE ER LIGGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Drie koppelingen, tot op het veld uitgewerkt

<div class="np-grid-2" style="margin-top: 1.2rem; gap: 1rem; align-items: start;">
  <div class="np-card accent-blue" style="font-size: 0.92rem; line-height: 1.5;">
    <carbon-catalog style="font-size: 1.5rem; color: var(--np-blue);" />
    <strong>Catalogus en planning</strong><br/>
    wat er ontworpen is, wordt planbaar: perioden, groepen, capaciteit
  </div>
  <div class="np-card accent-orange" style="font-size: 0.92rem; line-height: 1.5;">
    <carbon-data-base style="font-size: 1.5rem; color: var(--np-orange);" />
    <strong>Catalogus en studentadministratie</strong><br/>
    waarop een student zich kan inschrijven, en waartegen resultaten tellen
  </div>
  <div class="np-card accent-green" style="font-size: 0.92rem; line-height: 1.5;">
    <carbon-education style="font-size: 1.5rem; color: var(--np-green);" />
    <strong>Catalogus en leeromgeving</strong><br/>
    de lesstof en opdrachten waarmee de docent de les inricht
  </div>
  <div class="np-card accent-blue" style="font-size: 0.92rem; line-height: 1.5;">
    <carbon-task-complete style="font-size: 1.5rem; color: var(--np-blue);" />
    <strong>Per koppeling vastgelegd</strong><br/>
    wie wat stuurt, wanneer, en welke gegevens er precies in zitten
  </div>
</div>

<div class="np-card accent-green" style="margin-top: 1.2rem; font-size: 0.95rem; line-height: 1.55;">
  <strong>Openbaar en versiebeheerd.</strong> Iedereen leest dezelfde tekst, met dezelfde versie en datum. Wijzigingen zijn zichtbaar, met de reden erbij.
</div>

</div>

<!--
Bron: Npuls-OKx/Public, Koppelvlakspecificaties: drie interactiepatronen (onderwijscatalogus naar
planning en rooster, naar kernregistratie, naar leeromgeving), negentien interacties, twaalf
functionele eisen en vierentwintig datamodelschema's. Alfa-status: de vorm ligt vast, de velden
kunnen nog wijzigen tot de payload is vastgesteld.
-->

---

<!-- 4. EEN GEZAMENLIJKE TAAL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een gezamenlijke taal

<div class="np-grid-2" style="margin-top: 0.8rem; gap: 1.2rem; align-items: center;">

<div>
  <div style="display: flex; gap: 0.7rem; margin-bottom: 0.8rem;">
    <div class="np-card accent-blue" style="flex: 1; text-align: center; padding: 0.7rem 0.5rem;">
      <div style="font-size: 2.1rem; font-weight: 700; color: var(--np-blue); line-height: 1;">73</div>
      <small style="font-size: 0.8rem;">begrippen met definitie en herkomst</small>
    </div>
    <div class="np-card accent-orange" style="flex: 1; text-align: center; padding: 0.7rem 0.5rem;">
      <div style="font-size: 2.1rem; font-weight: 700; color: var(--np-orange); line-height: 1;">66</div>
      <small style="font-size: 0.8rem;">objecten in het informatiemodel</small>
    </div>
  </div>
  <div class="np-card accent-green" style="font-size: 0.88rem; line-height: 1.5; padding: 0.6rem 0.9rem;">
    Elk begrip ligt naast de sectorkaders MORA en ROSA. Waar de sector al een woord heeft, gebruiken wij dat woord.
  </div>
  <div class="np-card accent-orange" style="font-size: 0.88rem; line-height: 1.5; padding: 0.6rem 0.9rem; margin-top: 0.6rem;">
    <strong>De leeruitkomst is de sleutel:</strong> zij verbindt het ontwerp van het onderwijs met wat de student aantoont.
  </div>
</div>

<div>
  <img src="/platen/informatiemodel-v0.1.jpg" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray);" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Informatiemodel OKx v0.1</div>
</div>

</div>

</div>

<!--
Bron: informatiemodel v0.1 (66 objecttypen, 156 relaties, zeven begrippenfamilies) en
begrippenlijst v0.2 (73 begrippen, waarvan 22 met een definitie uit een referentiekader),
gepubliceerd naar Public op 18 september. Zeg erbij dat systemen elkaar pas begrijpen als
mensen dezelfde woorden gebruiken; dat is de reden dat dit er ligt.
-->

---

<!-- 5. DE TOETS: DE REIS VAN EEN STUDENT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De proef op de som: de reis van Jochem

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.2rem; align-items: center;">

<div>
  <img src="/platen/jochem.png" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray);" />
</div>

<div>
  <div class="np-card accent-blue" style="font-size: 0.92rem; line-height: 1.55; margin-bottom: 0.8rem;">
    <carbon-user-favorite style="font-size: 1.4rem; color: var(--np-blue);" />
    <strong>Een echte opleiding, stap voor stap</strong><br/>
    apothekersassistent, van het ontwerp van de opleiding tot zijn diploma
  </div>
  <div class="np-card accent-orange" style="font-size: 0.92rem; line-height: 1.55; margin-bottom: 0.8rem;">
    <carbon-search style="font-size: 1.4rem; color: var(--np-orange);" />
    <strong>Elke stap naast het model gelegd</strong><br/>
    klopt het, ontbreekt er iets, heet het bij uw school hetzelfde?
  </div>
  <div class="np-card accent-green" style="font-size: 0.92rem; line-height: 1.55;">
    <carbon-calendar style="font-size: 1.4rem; color: var(--np-green);" />
    <strong>30 september bij de kerngroep techniek</strong><br/>
    scholen en leveranciers leggen het naast hun eigen praktijk
  </div>
</div>

</div>

</div>

<!--
Bron: voorbeelduitwerking leerroute 1 (persona Jochem, apothekersassistent, cohort 2026), acht
fasen van kwalificatiedossier tot diplomering, met een beeld per processtap. Het document stelt
zeven vragen aan de kerngroep en heeft een invulblad per objecttype: herkent u dit, heet het bij u
anders, hangt het anders, ontbreekt het. Nog niet publiek; wordt 30 september voorgelegd.
-->

---

<!-- 6. WAT ER NU GEBEURT EN WAT WIJ VRAGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er nu gebeurt, en wat wij vragen

<div class="np-pipeline" style="margin-top: 1.3rem;">
  <div class="np-step orange" style="flex: 1;">
    <carbon-user-multiple style="font-size: 1.9rem; color: var(--np-orange);" />
    <strong style="font-size: 0.88rem;">Najaar 2026</strong>
    <small>koploperscholen en vier leveranciers leggen de afspraken naast hun praktijk</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue" style="flex: 1;">
    <carbon-tools style="font-size: 1.9rem; color: var(--np-blue);" />
    <strong style="font-size: 0.88rem;">Q1 2027</strong>
    <small>leveranciers bouwen de eerste koppeling op de gepubliceerde afspraken</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1;">
    <carbon-growth style="font-size: 1.9rem; color: var(--np-green);" />
    <strong style="font-size: 0.88rem;">Daarna</strong>
    <small>meer leerroutes, en het hoger onderwijs erbij</small>
  </div>
</div>

<div class="np-card accent-orange" style="margin-top: 1.4rem; font-size: 1rem; line-height: 1.6;">
  <strong>Wat wij van de werkgroep vragen:</strong> houd de vraag bij de instellingen op tafel. Wat hier ligt is pas van waarde als scholen het herkennen als hun eigen praktijk en hun leverancier erop aanspreken.
</div>

<div style="margin-top: 0.9rem; font-size: 0.9rem; color: var(--np-mid-gray);">
  Alles openbaar te lezen in de kennisbasis: github.com/Npuls-OKx/Public
</div>

</div>

<!--
Sluit af met de vraag, niet met een opsomming. Bronnen: planning uit het overleg met het SI-team
van 13 juli (bouw bij leveranciers in het eerste kwartaal van 2027, specificaties af rond de
herfstvakantie); vier koploperleveranciers en zes tot acht koploperinstellingen betrokken.
-->
