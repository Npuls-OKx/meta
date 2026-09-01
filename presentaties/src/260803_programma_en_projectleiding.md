---
theme: default
title: OKx — stand van zaken
info: De koppelingspecificaties liggen er, release management en de repo-indeling zijn geregeld, en het werk richt zich nu op de keuzeregels.
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
  <h1 style="font-size: 3.3rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Stand van zaken</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 680px; line-height: 1.5; margin-bottom: 1rem;">
    De specificaties liggen er. De vraag is nu of de sector zich erin herkent.
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>OKx</strong> &middot; Programma- en projectleiding &middot; 3 augustus 2026
  </div>
</div>

---

<!-- KERN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 1rem 2rem 0;">
  <div style="font-family: 'Cooper Light BT', serif; font-size: 1.9rem; line-height: 1.5; color: var(--np-blue); max-width: 720px;">
    Het schrijfwerk is grotendeels klaar. Het zwaartepunt verschuift van specificeren naar valideren.
  </div>
</div>

<div class="np-proof-strip" style="justify-content: center; margin-top: 2.2rem;">
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Drie koppelingen beschreven</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Materiaal staat publiek</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Adviesgroep aan zet</div>
</div>

</div>

---

<!-- WAT ER LIGT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er nu ligt

<p class="np-subtitle">De kern van het werk: hoe de systemen binnen een instelling onderwijs aan elkaar doorgeven.</p>

<div class="np-pipeline" style="margin-top: 1.1rem;">
  <div class="np-step blue" style="flex: 1 1 0; max-width: 270px;">
    <strong style="font-size: 0.88rem;">Planning en rooster</strong>
    <small>Wanneer en waar het draait</small>
  </div>
  <div class="np-step orange" style="flex: 1 1 0; max-width: 270px;">
    <strong style="font-size: 0.88rem;">Leermanagementsysteem</strong>
    <small>Waar de student leert</small>
  </div>
  <div class="np-step green" style="flex: 1 1 0; max-width: 270px;">
    <strong style="font-size: 0.88rem;">Studentinformatiesysteem</strong>
    <small>Inschrijving en resultaten</small>
  </div>
</div>

<p class="muted" style="font-size: 0.95rem; margin-top: 1.4rem; line-height: 1.7;">
Voor de reguliere leerroute is beschreven wat er tussen die systemen heen en weer gaat: welk bericht, wanneer, en in welke volgorde. Dat is het materiaal waar leveranciers straks op bouwen.
</p>

<div class="np-bottomline" style="margin-top: 1.1rem;">
  Dit is het stuk waar het project om draait. De rest is randvoorwaarde.
</div>

</div>

---

<!-- POSITIE IN HET GEHEEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Leerroute 1 van de negen

<p class="np-subtitle">Het huidige werk beslaat de reguliere leerroute. Leerroute 2 en 3 volgen als verschil ten opzichte daarvan, niet als nieuw document.</p>

<img src="/platen/leerroutes.png" style="width: 100%; max-height: 300px; object-fit: contain; margin-top: 0.4rem;" />

<p class="muted" style="font-size: 0.85rem; margin-top: 0.6rem;">
Die aanpak scheelt werk en houdt de specificaties consistent: wat voor de reguliere route geldt, hoeft daarna niet opnieuw beschreven te worden.
</p>

</div>

---

<!-- RANDVOORWAARDEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee randvoorwaarden, onderweg geregeld

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Release management</span>
    <h3 style="margin-top: 0.5rem;">Versienummers die iets zeggen</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Aan het nummer is af te lezen of er werk aan de winkel is: een correctie, een uitbreiding, of iets fundamenteels anders. Zonder die afspraak wordt elke wijziging een telefoonrondje.
    </p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Twee repositories</span>
    <h3 style="margin-top: 0.5rem;">Private source en public source</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      De <strong>private source</strong> draagt de concepten en de discussie, de <strong>public source</strong> de artefacten waarmee een instelling of leverancier bouwt. Wat naar buiten gaat komt uit de public source; daar zit geen halffabricaat tussen.
    </p>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.3rem;">
Allebei saai, allebei nodig. Zonder deze twee kan er niets naar buiten zonder het risico het meteen te moeten terughalen.
</p>

</div>

---

<!-- WERKWIJZE PROJECT- EN REPOSETUP -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van bron naar releasepakket

<p class="np-subtitle">De werkwijze achter release management: drie plekken, elk met een eigen publiek.</p>

<div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 1.3rem; align-items: center; margin-top: 0.3rem;">

  <div style="background: #141414; border-radius: 14px; overflow: hidden; line-height: 0;">
    <img src="/platen/repo-setup.jpg" style="width: 100%; max-height: 300px; object-fit: contain; display: block;" />
  </div>

  <div style="font-size: 0.86rem; line-height: 1.6;">
    <p style="margin: 0 0 0.7rem;"><strong>Lees de plaat van links naar rechts.</strong> De <strong>private source</strong> draagt interne planning en referentiemateriaal, de <strong>public source</strong> het bronmateriaal van de releasepakketten, en de <strong>public release</strong> de pakketten zelf.</p>
    <p style="margin: 0 0 0.7rem; color: var(--np-dark-gray);">Rechts staat wat er uiteindelijk uitkomt: de koppelvlakspecificatie, de OEAPI-profielen en de leerroute-implementatie.</p>
    <p style="margin: 0; color: var(--np-dark-gray);">De rollen erboven bepalen wie waar bij kan. Een <strong>implementeerder</strong> raakt alleen de rechterkolom; een <strong>contributor</strong> van buiten draagt bij aan de public source.</p>
  </div>

</div>

<div class="np-bottomline" style="margin-top: 0.9rem;">
  Alles links van de release is <strong>werk in uitvoering</strong>. Dat onderscheid is precies waarom de scheiding er ligt.
</div>

</div>

<!--
De plaat komt uit Werkwijze/src/ in Npuls-OKx/Public, naast zijn drawio-bron.

Bij doorvragen over hoe een wijziging de release in komt: dat staat in
Release-management-algemeen.md, hoofdstuk 6 Releaseproces, met de rollentabel,
de zes processtappen en de branchstrategie in 6.1. Die branching-plaat staat in
het manifest onder de naam 'branching' en kan er desgewenst naast.

Feitelijk: de drie containers en de rollen staan zo in de plaat. Inschatting:
dat een implementeerder alleen de rechterkolom raakt is de bedoeling van de
opzet, niet iets wat technisch is afgedwongen.
-->

---

<!-- WAAR NU AAN GEWERKT WORDT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Het werk van dit moment: de keuzeregels

<p class="np-subtitle">Klein onderwerp in naam, groot in gevolgen.</p>

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: start;">
<div style="font-size: 0.95rem; line-height: 1.75;">

Een instelling laat niet elke student elk keuzedeel kiezen; logistiek kan dat niet. De vraag is hoe vastgelegd wordt wie wat mag kiezen, op een manier die bij elke instelling en elke leverancier hetzelfde uitpakt.

Die vraag kwam in juni uit de adviesgroep. Inmiddels uitgewerkt tot zestien eisen en een eerste vorm, met de status concept.

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Waarom nu</h3>
    <p style="font-size: 0.93rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Zonder afspraak vult elke leverancier dit zelf in. Die invulling wordt vanzelf de praktijk, en is daarna nauwelijks nog bij te sturen.
    </p>
  </div>
</div>
</div>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  Naarmate onderwijs flexibeler wordt, wordt <strong>bijna alles</strong> een keuze. Dit is de generieke oplossing, niet alleen die voor keuzedelen.
</div>

</div>

---

<!-- PLANNING EN RISICO -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Planning en risico

<div style="font-size: 0.9rem; margin-top: 0.5rem;">

| | |
| --- | --- |
| **19 augustus** | Koppelvlakspecificatie alpha. Inhoud staat, 3 punten open. Haalbaar. |
| **31 augustus** | Deel specificatiedocument af. **27 punten open.** In een vakantiemaand. |

</div>

<div class="np-grid-2" style="margin-top: 1rem; align-items: start;">
  <div class="np-card accent-yellow">
    <h3>Risico</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Niet de inhoud, maar de reviewcapaciteit. Validatie door de sector is nodig om te bevestigen dat de specificaties kloppen, en augustus is daarvoor een ongunstige maand.
    </p>
  </div>
  <div class="np-card accent-blue">
    <h3>Consequentie</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Of 31 augustus schuift, of de definitie van "af" wordt scherper afgebakend. Het tweede houdt tempo zonder een voorstelling van zaken te geven die niet klopt.
    </p>
  </div>
</div>

</div>

<!--
Bij doorvragen het onderscheid bewaken: de 27 open punten en de datums zijn
feitelijk en na te lezen. De haalbaarheidsinschatting en de voorkeur voor
scherper afbakenen zijn een oordeel, geen vaststaand gegeven.
-->

---

<!-- BESLUITEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagde besluiten

<dl class="np-besluit" style="margin-top: 0.8rem;">
  <dt>Besluit nodig op</dt>
  <dd>Het publicatiemoment van de koppelvlakspecificatie leerroute 1</dd>
  <dt>Door</dt>
  <dd>Programmaleiding, in afstemming met de kerngroep techniek OKx</dd>
  <dt>Voor</dt>
  <dd>19 augustus 2026</dd>
  <dt>Opties</dt>
  <dd>Publiceren ná de kerngroep techniek, dus september — of eerder publiceren, met de kans op wijzigingen na leveranciersreacties</dd>
</dl>

<dl class="np-besluit" style="margin-top: 0.9rem;">
  <dt>Besluit nodig op</dt>
  <dd>De betekenis van "af" op de mijlpaal van 31 augustus</dd>
  <dt>Door</dt>
  <dd>Programma- en projectleiding</dd>
  <dt>Voor</dt>
  <dd>31 augustus 2026</dd>
  <dt>Opties</dt>
  <dd>Alle 27 punten, met uitloop — of een scherpere afbakening, met het restant naar september</dd>
</dl>

<p class="muted" style="font-size: 0.92rem; margin-top: 1.2rem;">
Verder geen besluitpunten. De inhoudelijke vragen liggen bij de adviesgroep en de kerngroep techniek OKx.
</p>

</div>

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
