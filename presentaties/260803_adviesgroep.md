---
theme: default
title: OKx — de koppelingspecificaties
info: Wat er ligt voor leerroute 1, hoe releases en repositories zijn ingericht, en waar nu aan gewerkt wordt.
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
    Wat er ligt voor leerroute 1, en waar een onderwijskundig oordeel over nodig is
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>OKx</strong> &middot; Adviesgroep &middot; 3 augustus 2026
  </div>
</div>

---

<!-- AGENDA -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="margin-left: 42%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding-right: 3rem;">
  <p class="eyebrow">Onderwerpen</p>
  <h1 style="font-size: 2.2rem !important; margin-bottom: 1.4rem;">Programma</h1>
  <div style="display: flex; flex-direction: column; gap: 1rem;">
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">1</span>
      <div><strong>De koppelingspecificaties</strong><br/><span class="muted" style="font-size: 0.82rem;">Het zwaartepunt van het werk sinds mei</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>Waar het materiaal staat</strong><br/><span class="muted" style="font-size: 0.82rem;">Twee repositories en de betekenis van een versienummer</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Het werk van dit moment</strong><br/><span class="muted" style="font-size: 0.82rem;">Vastleggen wie welk keuzedeel mag kiezen</span></div>
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

# Leerroute 1 in één beeld

<p class="np-subtitle">Links het ontwerp van het onderwijs, rechts de student die studeert en kiest. Persona: Jochem.</p>

<img src="/platen/lr1-informatiestromen.jpg" style="width: 100%; max-height: 330px; object-fit: contain; margin-top: 0.3rem;" />

<p class="muted" style="font-size: 0.82rem; margin-top: 0.5rem;">
Elke pijl is iets dat een systeem aan een ander doorgeeft. Het werk van OKx is die pijlen zo beschrijven dat twee leveranciers er hetzelfde onder verstaan.
</p>

</div>

<!--
Neem de tijd voor deze plaat. Links: de curriculum-ontwerptool maakt
specificaties, die gaan naar de onderwijscatalogus. Rechts: de student schrijft
zich in (KRS), kiest een keuzedeel (SKS), volgt onderwijs (LMS), en de
resultaten landen in het studentvolgsysteem (SVS).

Deze plaat is getekend op basis van hoofdplaat 1.6b; leidend voor de
architectuur is inmiddels 1.7. De informatiestromen zijn ongewijzigd, de plaat
is nog niet bijgetekend. Alleen benoemen als er naar gevraagd wordt.
-->

---

<!-- DE KETEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Drie koppelingen, vanuit de catalogus

<p class="np-subtitle">De onderwijscatalogus is het distributiepunt. Daar staat wat de instelling aanbiedt, en van daaruit gaat het de keten in.</p>

<div style="margin-top: 0.6rem;">

```mermaid {scale: 0.52}
flowchart LR
    CO["Curriculum-ontwerptool"] --> OC["Onderwijscatalogus (OC)<br/>distributiepunt"]
    OC -->|"OC-P&R: te plannen aanbod"| PR["Planning en Roostering"]
    OC -->|"OC-LMS: structuur, leermiddelen terug"| LMS["Leermanagementsysteem"]
    OC -->|"OC-SIS: nominaal template, resultaatstructuur"| SIS["Studentinformatiesysteem (KRS/SVS)"]
    SKS["Student Keuze Systeem"] -. "eigen koppeling, buiten scope hier" .-> SIS
```

</div>

<p class="muted" style="font-size: 0.88rem; margin-top: 0.8rem; line-height: 1.7;">
Het planningssysteem maakt van de specificatie <strong>planbaar aanbod</strong>; het roostersysteem hangt daar tijden en lokalen aan. Het leermanagementsysteem richt de online leeromgeving in op de gepubliceerde structuur. Het studentinformatiesysteem — kernregistratie plus studentvolgsysteem — krijgt de resultaatstructuur en het examenplan.
</p>

</div>

---

<!-- KOPPELING EN KOPPELVLAK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Koppeling of koppelvlak

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: center;">
<div style="font-size: 0.93rem; line-height: 1.75;">

Een **koppeling** is één informatiestroom tussen twee componenten. Alle koppelingen die op één component samenkomen, vormen samen het **koppelvlak** van dat component.

Dat onderscheid klinkt muggenzifterig. Het loste wel een concreet probleem op: hetzelfde woord stond voor twee verschillende dingen, en daardoor liepen afspraken over scope telkens vast. Sinds het vastligt, is per document duidelijk of het over één stroom gaat of over het geheel.

<p class="muted" style="font-size: 0.85rem; margin-top: 0.9rem;">
Hiernaast: alle koppelingen die op de onderwijscatalogus samenkomen. Dat plaatje is dus een koppelvlak; elke pijl erin is een koppeling.
</p>

</div>
<div>
  <img src="/platen/koppelvlak-oc.jpg" style="width: 100%; max-height: 300px; object-fit: contain; border-radius: 10px;" />
  <p class="muted" style="font-size: 0.75rem; text-align: center; margin-top: 0.4rem;">Koppelvlak onderwijscatalogus, versie 1.7</p>
</div>
</div>

</div>

---

<!-- EEN BRON -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Eén beschrijving, drie afnemers

<p class="np-subtitle">Alle drie hebben ze een ander deel van dezelfde onderwijsspecificatie nodig. Die staat daarom één keer beschreven.</p>

<div class="np-grid-3" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Planning</span>
    <h3 style="margin-top: 0.5rem;">Alleen de sleutels</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Leeruitkomsten komen mee als kaal nummer. Dat is genoeg om volgorde en omvang te bepalen; de inhoud is voor planning niet nodig.</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">SIS</span>
    <h3 style="margin-top: 0.5rem;">De hele laag</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Leeruitkomsten komen volledig mee, want daarop worden de resultaten behaald. Zonder die inhoud is een diploma niet te onderbouwen.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">LMS</span>
    <h3 style="margin-top: 0.5rem;">De inhoudsvelden</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Mee komt wat nodig is om de leeromgeving in te richten: structuur, lesstof en leermiddelen.</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  Elk systeem krijgt <strong>precies wat het nodig heeft</strong>, en niet meer dan dat.
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
Een rij leest zo: op dit niveau van het kwalificatiekader horen deze leeruitkomst, die specificatie, dat aanbod, die verbintenis en dat resultaat. De rijen op de volgende slide vallen buiten het kwalificatiekader.
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

<!-- DE LEERUITKOMSTKOLOM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De kolom die erbij moest

<p class="np-subtitle">Kolom 2, de beoogde leeruitkomst, ontbrak in de eerdere versie. Dat bleek een gat.</p>

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: start;">
<div style="font-size: 0.92rem; line-height: 1.75;">

Zonder die kolom lijkt het alsof een onderwijseenheid rechtstreeks uit het kwalificatiedossier rolt. Dat is niet zo. Daartussen zit de onderwijskundige vertaalslag: het kader omzetten naar leeruitkomsten die concreet en observeerbaar zijn.

De leeruitkomst is bovendien het enige begrip dat **alle kolommen doorkruist**. Specificaties verankeren erop, resultaten worden erop behaald. Vandaar de naam *anker*tabel.

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Openstaand punt</h3>
    <p style="font-size: 0.93rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Hangt de summatieve leeruitkomst inderdaad aan het <strong>werkproces</strong>? En klopt het dat er op dossier- en kwalificatieniveau uitsluitend sprake is van aggregatie?
    </p>
  </div>
</div>
</div>

<p class="muted" style="font-size: 0.85rem; margin-top: 1rem;">
Complicatie: dezelfde leeruitkomst kan over meerdere onderdelen verdeeld zijn, en één onderdeel kan meerdere leeruitkomsten dekken. Precies daarom past dit niet in de specificatiekolom en moest het een eigen kolom worden.
</p>

</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide13.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.8rem;">Waar het materiaal staat</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.1rem; margin-top: 0.5rem;">Kort, maar nuttig om te weten</p>
  </div>
</div>

---

<!-- REPO EN RELEASE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee plekken, en de betekenis van een versienummer

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Waar het staat</span>
    <h3 style="margin-top: 0.5rem;">Werkplaats en etalage</h3>
    <p class="muted" style="font-size: 0.87rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Concepten en discussie staan apart van wat gepubliceerd is. Wat doorgestuurd wordt naar een collega of een instelling, komt uit het <strong>publieke</strong> repository. Daar staat geen halffabricaat tussen.
    </p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Versienummers</span>
    <h3 style="margin-top: 0.5rem;">Een belofte, geen datum</h3>
    <p class="muted" style="font-size: 0.87rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Laatste cijfer omhoog: er is iets verduidelijkt. Middelste: er komt iets bij, bestaand werk blijft geldig. Eerste: er verandert iets fundamenteels, en wie al gebouwd heeft moet aanpassen.
    </p>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.3rem; line-height: 1.7;">
Waarom dit ertoe doet: zodra dit materiaal naar leveranciers gaat, moet aan het nummer af te lezen zijn of er werk aan de winkel is. Zonder die afspraak is elke wijziging een telefoonrondje.
</p>

</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide15.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 3</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.8rem;">Het werk van dit moment</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.1rem; margin-top: 0.5rem;">Wie mag welk keuzedeel kiezen</p>
  </div>
</div>

---

<!-- DE VRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-grid-2" style="align-items: center; height: 100%;">
<div>
  <div style="font-family: 'Cooper Light BT', serif; font-size: 1.25rem; line-height: 1.5; color: var(--np-blue);">
    "Binnen de meeste mbo-instellingen mogen niet alle keuzedelen door alle studenten gekozen worden, omdat dit logistiek niet uitvoerbaar is. Hoe zorgen we er in de keten voor dat duidelijk is welke keuzedelen Jochem mag kiezen?"
  </div>
  <div style="margin-top: 1.2rem; font-size: 0.9rem; color: var(--np-dark-gray);">&mdash; Jan Hendrik van Schaik, juni 2026</div>
</div>
<div>
  <img src="/platen/jochem.png" style="width: 100%; max-height: 320px; object-fit: contain;" />
  <p class="muted" style="font-size: 0.75rem; text-align: center; margin-top: 0.3rem;">Jochem, de persona van leerroute 1</p>
</div>
</div>

</div>

<!--
Kees van Ginkel (Eduarte) herkende dit meteen en noemde verwante gevallen:
"minimaal twee vreemde talen", "deze keuze mag pas na Engels", en
slaag-zakregels per opleiding. Dat is de reden dat het generiek is opgepakt en
niet alleen voor keuzedelen.
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
    <small>Wat er georganiseerd wordt</small>
  </div>
  <div class="np-arrow">&#43;</div>
  <div class="np-step orange" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.95rem;">Regelset</strong>
    <small>Wie dit mag kiezen, en wanneer</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.95rem;">Aanbod</strong>
    <small>Wanneer en waar het draait</small>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.2rem; line-height: 1.7;">
De reden voor die scheiding: een voorwaarde gaat over <strong>wat een student heeft behaald</strong>, niet over welk vak is gevolgd. Bij een herziening van het onderwijs blijft de regel daardoor geldig. Er liggen zestien eisen; de vorm heeft de status <strong>concept</strong>.
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

<!-- WAT ER GEVRAAGD WORDT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er van de adviesgroep gevraagd wordt

<dl class="np-besluit review" style="margin-top: 0.9rem;">
  <dt>Review gevraagd op</dt>
  <dd>De ankertabel, en in het bijzonder de nieuwe kolom <em>beoogde leeruitkomst</em>: hangt de summatieve leeruitkomst aan het werkproces, en klopt de aggregatie daarboven?</dd>
  <dt>Door</dt>
  <dd>Adviesgroep — onderwijskundig oordeel</dd>
  <dt>Voor</dt>
  <dd>19 augustus 2026, het alpha-moment van de koppelvlakspecificatie</dd>
</dl>

<dl class="np-besluit review" style="margin-top: 0.9rem;">
  <dt>Review gevraagd op</dt>
  <dd>De regelset. Gezocht: een keuzeregel uit de eigen instellingspraktijk die de voorgestelde vorm <strong>niet</strong> kan uitdrukken</dd>
  <dt>Door</dt>
  <dd>Adviesgroep — IM'ers en onderwijskundigen vanuit de instellingen</dd>
  <dt>Voor</dt>
  <dd>31 augustus 2026, voordat de vorm vastligt</dd>
</dl>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  Een tegenvoorbeeld is waardevoller dan instemming. Alle onderdelen hebben nog de status <strong>concept</strong>.
</div>

</div>

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
