---
theme: default
title: OKx — de koppelingspecificaties
info: Wat er nu ligt voor leerroute 1, hoe we releases en repositories hebben ingericht, en waar we nu aan werken.
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
  <h1 style="font-size: 3.2rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">De koppelingspecificaties</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 700px; line-height: 1.5; margin-bottom: 1rem;">
    Wat er nu ligt, en waar we jullie oordeel bij nodig hebben
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>OKx</strong> &middot; Adviesgroep &middot; 3 augustus 2026
  </div>
</div>

---

<!-- AGENDA -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="margin-left: 42%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding-right: 3rem;">
  <p class="eyebrow">Wat gaan we bespreken</p>
  <h1 style="font-size: 2.2rem !important; margin-bottom: 1.4rem;">Programma</h1>
  <div style="display: flex; flex-direction: column; gap: 1rem;">
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">1</span>
      <div><strong>De koppelingspecificaties</strong><br/><span class="muted" style="font-size: 0.82rem;">Waar we het meeste tijd in hebben gestoken</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>Waar het staat</strong><br/><span class="muted" style="font-size: 0.82rem;">Twee repositories en wat een release is</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Waar we nu aan werken</strong><br/><span class="muted" style="font-size: 0.82rem;">Wie mag welk keuzedeel kiezen</span></div>
    </div>
  </div>
</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 1</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">De koppelingspecificaties</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Wat gaat er tussen de systemen heen en weer?</p>
  </div>
</div>

---

<!-- DE PLAAT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Dit is waar het over gaat

<p class="np-subtitle">Leerroute 1, Jochem. Links het ontwerp van het onderwijs, rechts de student die studeert en kiest.</p>

<img src="/platen/lr1-informatiestromen.jpg" style="width: 100%; max-height: 330px; object-fit: contain; margin-top: 0.3rem;" />

<p class="muted" style="font-size: 0.82rem; margin-top: 0.5rem;">
Elk pijltje is iets dat een systeem aan een ander doorgeeft. Ons werk is die pijltjes zo beschrijven dat twee leveranciers er hetzelfde onder verstaan.
</p>

</div>

<!--
Neem de tijd voor deze plaat. Links: de curriculum ontwerptool maakt
specificaties, die gaan naar de onderwijscatalogus. Rechts: de student meldt
zich aan (intake, KRS), kiest een keuzedeel (SKS), volgt onderwijs (LMS), en
zijn resultaten landen in het studentvolgsysteem (SVS).
-->

---

<!-- DE DRIE KOPPELINGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Drie koppelingen, vanuit de catalogus

<p class="np-subtitle">De onderwijscatalogus is het distributiepunt. Daar staat wat de instelling aanbiedt, en van daaruit gaat het de keten in.</p>

<div class="np-grid-3" style="margin-top: 0.7rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">OC naar P&amp;R</span>
    <h3 style="margin-top: 0.5rem;">Planning en roostering</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Het planningssysteem maakt er <strong>planbaar aanbod</strong> van: welke periode, hoeveel plekken. Het roostersysteem hangt er daarna tijden en lokalen aan.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">OC naar LMS</span>
    <h3 style="margin-top: 0.5rem;">Leermanagementsysteem</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">De online leeromgeving van de student wordt ingericht op de gepubliceerde structuur. Leermiddelen komen terug richting de catalogus.</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">OC naar SIS</span>
    <h3 style="margin-top: 0.5rem;">Studentinformatiesysteem</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Dat is KRS plus SVS: inschrijving aan de ene kant, voortgang en resultaten aan de andere. Krijgt de resultaatstructuur en het examenplan.</p>
  </div>
</div>

<p class="muted" style="font-size: 0.87rem; margin-top: 1.1rem; line-height: 1.7;">
Een <strong>koppeling</strong> is één stroom tussen twee systemen. Alle koppelingen van één systeem bij elkaar heten het <strong>koppelvlak</strong> van dat systeem. Dat onderscheid klinkt muggenzifterig, maar het scheelde ons veel verwarring: we gebruikten hetzelfde woord voor twee dingen.
</p>

</div>

---

<!-- EEN BRON -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Eén beschrijving, drie afnemers

<p class="np-subtitle">Ze hebben alle drie een ander stuk van dezelfde onderwijsspecificatie nodig. Dus schrijven we die één keer op.</p>

<div class="np-grid-3" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Planning</span>
    <h3 style="margin-top: 0.5rem;">Alleen de sleutels</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Krijgt leeruitkomsten als kaal nummer, genoeg om volgorde en omvang te bepalen. Wat er inhoudelijk in staat hoeft de planner niet te weten.</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">SIS</span>
    <h3 style="margin-top: 0.5rem;">De hele laag</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Krijgt de leeruitkomsten volledig, want daar worden de resultaten op behaald. Zonder die inhoud kun je geen diploma onderbouwen.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">LMS</span>
    <h3 style="margin-top: 0.5rem;">De inhoudsvelden</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Krijgt wat nodig is om de leeromgeving in te richten: structuur, lesstof, leermiddelen.</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  Zo krijgt elk systeem <strong>precies wat het nodig heeft</strong>, en niet meer dan dat.
</div>

</div>

---

<!-- ANKERTABEL, DEEL 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De ankertabel

<p class="np-subtitle">De begrippen waarmee alle koppelingen spreken. Van links naar rechts loopt het onderwijs van kader naar resultaat.</p>

<div style="font-size: 0.66rem; margin-top: 0.3rem;">

| 1. Kwalificatiekader | 2. Beoogde leeruitkomst | 3. Onderwijsspecificatie | 4. Onderwijsaanbod | 5. Onderwijsverbintenis | 6. Onderwijsresultaat |
| --- | --- | --- | --- | --- | --- |
| `Kwalificatiedossier` | *n.v.t. — leeruitkomsten hangen lager in de boom* | `Opleidingsspecificatie` | `Opleidingsaanbod` | `Opleidingsverbintenis` | `Opleidingsverbintenis resultaat` |
| `Kwalificatie` | *n.v.t. — aggregatie van onderliggende leeruitkomsten* | `Opleidingsprogramma-specificatie` | `Opleidingsprogramma-aanbod` | `Opleidingsprogramma-verbintenis` | `Opleidingsprogramma-verbintenis resultaat` |
| `Kerntaak` | Collectie van leeruitkomst-collecties (één per werkproces) | `Onderwijseenheid-specificatie` | `Onderwijseenheid-aanbod` | `Onderwijseenheid-verbintenis` | `Onderwijseenheid-verbintenis resultaat` |
| `Werkproces` | `Leeruitkomst`-collectie (summatief) | `Leeronderdeel-specificatie` | `Leergelegenheid` | `Leergelegenheid-verbintenis` | `Leergelegenheid-verbintenis resultaat` |

</div>

<p class="muted" style="font-size: 0.8rem; margin-top: 0.9rem;">
Lees een rij zo: op dit niveau van het kwalificatiekader hoort deze leeruitkomst, die specificatie, dat aanbod, die verbintenis en dat resultaat. De rijen op de volgende slide vallen buiten het kwalificatiekader.
</p>

</div>

<!--
Deze tabel staat letterlijk zo in het kaderscenario leerroute 1 in
Npuls-OKx/Public. Alleen de toelichting in kolom 2 is ingekort om te passen.
-->

---

<!-- ANKERTABEL, DEEL 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De ankertabel, vervolg

<p class="np-subtitle">Wat de instelling zelf invult: lessen, toetsen en examens.</p>

<div style="font-size: 0.66rem; margin-top: 0.3rem;">

| 1. Kwalificatiekader | 2. Beoogde leeruitkomst | 3. Onderwijsspecificatie | 4. Onderwijsaanbod | 5. Onderwijsverbintenis | 6. Onderwijsresultaat |
| --- | --- | --- | --- | --- | --- |
| *n.v.t. — eigen beleid instelling* | `Lesuitkomst` (formatief; onder een `Leeruitkomst`) | `Lesspecificatie` | `Lesgelegenheid` | `Lesgelegenheid-verbintenis` | `Lesgelegenheid-verbintenis resultaat` |
| *n.v.t. — toetsing* | Scope van toetsing: set `Leeruitkomst` en/of `Lesuitkomst` | `Toetsonderdeel-specificatie` | `Toetsgelegenheid` | `Toetsgelegenheid-verbintenis` | `Toetsgelegenheid-verbintenis resultaat` |
| Doorgaands `Werkproces` | Te behalen `Leeruitkomst`-set, vastgesteld door examencommissie | `Examenonderdeel-specificatie` | `Examengelegenheid` | `Examengelegenheid-verbintenis` | `Examengelegenheid-verbintenis resultaat` |

</div>

<p class="muted" style="font-size: 0.8rem; margin-top: 0.9rem;">
Examinering is bewust een <strong>gescheiden keten</strong>: eigen specificaties, eigen gelegenheden, eigen governance. Toetsen zijn primair formatief, examens summatief. Dat scheidt de verantwoordelijkheid, ook richting DUO.
</p>

</div>

---

<!-- WAAROM DIE KOLOM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De kolom die erbij moest

<p class="np-subtitle">Kolom 2, de beoogde leeruitkomst, stond er eerst niet in. Dat bleek een gat.</p>

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: start;">
<div style="font-size: 0.92rem; line-height: 1.75;">

Zonder die kolom lijkt het alsof een onderwijseenheid rechtstreeks uit het kwalificatiedossier rolt. Dat is niet zo. Daartussen zit **jullie werk**: het kader vertalen naar leeruitkomsten die concreet en observeerbaar zijn.

En die leeruitkomst is het enige dat **alle kolommen doorkruist**. Specificaties verankeren erop, resultaten worden erop behaald. Vandaar de naam: een *anker*tabel.

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Vraag aan jullie</h3>
    <p style="font-size: 0.93rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Hoort de summatieve leeruitkomst inderdaad aan het <strong>werkproces</strong>? En klopt het dat er op dossier- en kwalificatieniveau alleen aggregatie is?
    </p>
  </div>
</div>
</div>

<p class="muted" style="font-size: 0.85rem; margin-top: 1rem;">
Let op: dezelfde leeruitkomst kan over meerdere onderdelen verdeeld zijn, en een onderdeel kan meerdere leeruitkomsten dekken. Dat is precies waarom het een eigen kolom moest worden en niet in de specificatiekolom past.
</p>

</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide13.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.8rem;">Waar het staat</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.1rem; margin-top: 0.5rem;">Kort, maar wel handig om te weten</p>
  </div>
</div>

---

<!-- REPO EN RELEASE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee plekken, en wat een versienummer betekent

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Waar het staat</span>
    <h3 style="margin-top: 0.5rem;">Werkplaats en etalage</h3>
    <p class="muted" style="font-size: 0.87rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Waar we denken en schuiven staat apart van wat we publiceren. Wil je iets nalezen of doorsturen naar een collega: pak de <strong>publieke</strong> kant. Daar staat geen halffabricaat tussen.
    </p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Versienummers</span>
    <h3 style="margin-top: 0.5rem;">Een belofte, geen datum</h3>
    <p class="muted" style="font-size: 0.87rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Laatste cijfer omhoog: er is iets verduidelijkt. Middelste: er kan iets bij, niks breekt. Eerste: er verandert iets fundamenteels, en wie al gebouwd heeft moet aan de bak.
    </p>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.3rem; line-height: 1.7;">
Waarom dit ertoe doet: zodra dit naar leveranciers gaat, moeten ze aan het nummer kunnen zien of er werk aan de winkel is. Zonder die afspraak weet niemand wanneer hij moet ingrijpen, en wordt elke wijziging een telefoonrondje.
</p>

</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide15.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 3</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.8rem;">Waar we nu aan werken</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.1rem; margin-top: 0.5rem;">Wie mag welk keuzedeel kiezen</p>
  </div>
</div>

---

<!-- DE VRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 0 2rem;">
  <div style="font-family: 'Cooper Light BT', serif; font-size: 1.5rem; line-height: 1.5; color: var(--np-blue); max-width: 780px;">
    "Binnen de meeste mbo-instellingen mogen niet alle keuzedelen door alle studenten gekozen worden, omdat dit logistiek niet uitvoerbaar is. Hoe zorgen we er in de keten voor dat duidelijk is welke keuzedelen Jochem mag kiezen?"
  </div>
  <div style="margin-top: 1.4rem; font-size: 0.9rem; color: var(--np-dark-gray);">&mdash; Jan Hendrik van Schaik, juni 2026</div>
</div>

</div>

<!--
Kees van Ginkel (Eduarte) herkende dit meteen en noemde verwante gevallen:
"minimaal twee vreemde talen", "deze keuze mag pas na Engels", en
slaag-zakregels per opleiding. Dat is de reden dat we het generiek hebben
opgepakt en niet alleen voor keuzedelen.
-->

---

<!-- DE REGELSET -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De regel staat naast het onderwijs, niet erin

<p class="np-subtitle">Kiesbaarheid is geen eigenschap van een keuzedeel. Het is een regel erover.</p>

<div class="np-pipeline" style="margin-top: 1rem;">
  <div class="np-step blue" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.95rem;">Onderwijsspecificatie</strong>
    <small>Wat we organiseren</small>
  </div>
  <div class="np-arrow">&#43;</div>
  <div class="np-step orange" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.95rem;">Regelset</strong>
    <small>Wie mag dit kiezen, en wanneer</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.95rem;">Aanbod</strong>
    <small>Wanneer en waar het draait</small>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.2rem; line-height: 1.7;">
Waarom los? Omdat een voorwaarde gaat over <strong>wat een student heeft behaald</strong>, niet over welk vak hij heeft gevolgd. Herzien jullie het onderwijs, dan blijft de regel gewoon geldig. Zestien eisen liggen er; de vorm is nog concept.
</p>

<div class="np-proof-strip" style="justify-content: center; margin-top: 1rem;">
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>"Kies uit deze lijst"</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>"Pas na Wiskunde 1"</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>"Minimaal twee uit deze groep"</div>
</div>

</div>

---

<!-- WAT WE VRAGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar we jullie voor nodig hebben

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
  <div class="np-card accent-orange">
    <span class="np-badge orange">1</span>
    <h3 style="margin-top: 0.5rem;">Klopt de ankertabel?</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Vooral de nieuwe kolom. Hangt de summatieve leeruitkomst aan het werkproces, en klopt de aggregatie daarboven? Jullie zien sneller dan wij of dat onderwijskundig hout snijdt.
    </p>
  </div>
  <div class="np-card accent-blue">
    <span class="np-badge blue">2</span>
    <h3 style="margin-top: 0.5rem;">Kennen jullie een keuzeregel die niet past?</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Een regel uit jullie eigen instelling die we hiermee <strong>niet</strong> kunnen uitdrukken. Dat willen we weten voordat de vorm vastligt, niet erna.
    </p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 1.3rem;">
  Een tegenvoorbeeld helpt ons meer dan instemming. Alles staat nog op <strong>concept</strong>.
</div>

</div>

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
