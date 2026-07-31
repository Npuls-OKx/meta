---
theme: default
title: OKx voortgang — adviesgroep
info: De koppelingspecificaties voor leerroute 1, hoe we releases en repositories hebben ingericht, en waar we nu aan werken.
author: OKx - Onderwijskoppelingen (Npuls)
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
  enabled: false
transition: slide-left
mdc: true
---

<!-- TITELSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide1.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem 4rem; z-index: 1;">
  <h1 style="font-size: 3.1rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">De koppelingspecificaties</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 700px; line-height: 1.5; margin-bottom: 1rem;">
    Wat er nu ligt voor leerroute 1, en waar we uw oordeel bij nodig hebben
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
      <div><strong>De koppelingspecificaties</strong><br/><span class="muted" style="font-size: 0.82rem;">Het hoofdgerecht</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>Waar het staat, en wat een release is</strong><br/><span class="muted" style="font-size: 0.82rem;">Kort</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Waar we nu aan werken</strong><br/><span class="muted" style="font-size: 0.82rem;">Regelsets: wie mag wat kiezen</span></div>
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
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Van leerroute naar wat systemen uitwisselen</p>
  </div>
</div>

---

<!-- DE DRIE KOPPELINGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Drie koppelingen vanuit de catalogus

<p class="np-subtitle">De onderwijscatalogus is het distributiepunt. Van daaruit gaat het onderwijs de keten in.</p>

<div class="np-pipeline" style="margin-top: 1rem;">
  <div class="np-step blue" style="flex: 1; max-width: 190px;">
    <strong style="font-size: 0.95rem;">Planning en rooster</strong>
    <small>Te plannen aanbod</small>
  </div>
  <div class="np-step orange" style="flex: 1; max-width: 190px;">
    <strong style="font-size: 0.95rem;">Leeromgeving</strong>
    <small>Structuur en leermiddelen</small>
  </div>
  <div class="np-step green" style="flex: 1; max-width: 190px;">
    <strong style="font-size: 0.95rem;">Studentadministratie</strong>
    <small>Resultaatstructuur, examenplan</small>
  </div>
</div>

<div class="np-grid-2" style="margin-top: 1.2rem; align-items: start;">
<div style="font-size: 0.9rem; line-height: 1.7;">

- Elke koppeling beschrijft **één informatiestroom**: welk bericht, wanneer, in welke volgorde
- De som van de koppelingen per systeem is het **koppelvlak** van dat systeem
- Uitgewerkt voor **leerroute 1**, met Jochem (Apothekersassistent) als rode draad

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Waarom zo</h3>
    <p style="font-size: 0.93rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      We schrijven de sector niet voor hoe ze moet koppelen. We beschrijven wat er moet bewegen, en ontdekken zo welke operaties nodig zijn.
    </p>
  </div>
</div>
</div>

</div>

<!--
Concreet: OC naar planning en roostering, OC naar LMS, OC naar SIS. Plus een
gedeeld deel met de centrale onderwijsspecificatie-payload en de lifecycle.
-->

---

<!-- EEN BRON -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Eén beschrijving, drie afnemers

<p class="np-subtitle">Planning, leeromgeving en studentadministratie hebben elk een ander deel van dezelfde onderwijsspecificatie nodig.</p>

<div class="np-grid-3" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Planning</span>
    <h3 style="margin-top: 0.5rem;">Alleen de sleutels</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Krijgt leeruitkomsten als kale verwijzing, genoeg om volgorde te bepalen. Geen inhoud.</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Studentadministratie</span>
    <h3 style="margin-top: 0.5rem;">De hele laag</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Krijgt de volledige leeruitkomsten, want daarop worden resultaten behaald.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">Leeromgeving</span>
    <h3 style="margin-top: 0.5rem;">De inhoudsvelden</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Krijgt wat nodig is om de leeromgeving in te richten.</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  De beschrijving staat <strong>één keer</strong> centraal. Elke koppeling legt vast welk deel zij afneemt.
</div>

</div>

---

<!-- ANKERTABEL, DEEL 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De ankertabel

<p class="np-subtitle">De begrippen waarmee alle koppelingen spreken. Eerst de niveaus binnen het kwalificatiekader.</p>

<div style="font-size: 0.66rem; margin-top: 0.3rem;">

| 1. Kwalificatiekader | 2. Beoogde leeruitkomst | 3. Onderwijsspecificatie | 4. Onderwijsaanbod | 5. Onderwijsverbintenis | 6. Onderwijsresultaat |
| --- | --- | --- | --- | --- | --- |
| `Kwalificatiedossier` | *n.v.t. — leeruitkomsten hangen lager in de boom* | `Opleidingsspecificatie` | `Opleidingsaanbod` | `Opleidingsverbintenis` | `Opleidingsverbintenis resultaat` |
| `Kwalificatie` | *n.v.t. — aggregatie van onderliggende leeruitkomsten* | `Opleidingsprogramma-specificatie` | `Opleidingsprogramma-aanbod` | `Opleidingsprogramma-verbintenis` | `Opleidingsprogramma-verbintenis resultaat` |
| `Kerntaak` | Collectie van leeruitkomst-collecties (één per werkproces) | `Onderwijseenheid-specificatie` | `Onderwijseenheid-aanbod` | `Onderwijseenheid-verbintenis` | `Onderwijseenheid-verbintenis resultaat` |
| `Werkproces` | `Leeruitkomst`-collectie (summatief) | `Leeronderdeel-specificatie` | `Leergelegenheid` | `Leergelegenheid-verbintenis` | `Leergelegenheid-verbintenis resultaat` |

</div>

<p class="muted" style="font-size: 0.8rem; margin-top: 0.9rem;">
Kolom 2 is sinds juli toegevoegd. Daaronder valt de instellingseigen laag: les, toets en examen (volgende slide).
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

<p class="np-subtitle">De lagen die buiten het kwalificatiekader vallen: instellingsbeleid, toetsing en examinering.</p>

<div style="font-size: 0.66rem; margin-top: 0.3rem;">

| 1. Kwalificatiekader | 2. Beoogde leeruitkomst | 3. Onderwijsspecificatie | 4. Onderwijsaanbod | 5. Onderwijsverbintenis | 6. Onderwijsresultaat |
| --- | --- | --- | --- | --- | --- |
| *n.v.t. — eigen beleid instelling* | `Lesuitkomst` (formatief; onder een `Leeruitkomst`) | `Lesspecificatie` | `Lesgelegenheid` | `Lesgelegenheid-verbintenis` | `Lesgelegenheid-verbintenis resultaat` |
| *n.v.t. — toetsing* | Scope van toetsing: set `Leeruitkomst` en/of `Lesuitkomst` | `Toetsonderdeel-specificatie` | `Toetsgelegenheid` | `Toetsgelegenheid-verbintenis` | `Toetsgelegenheid-verbintenis resultaat` |
| Doorgaands `Werkproces` | Te behalen `Leeruitkomst`-set, vastgesteld door examencommissie | `Examenonderdeel-specificatie` | `Examengelegenheid` | `Examengelegenheid-verbintenis` | `Examengelegenheid-verbintenis resultaat` |

</div>

<p class="muted" style="font-size: 0.8rem; margin-top: 0.9rem;">
Examinering is een <strong>gescheiden keten</strong> binnen de instelling: eigen specificaties, eigen gelegenheden, eigen governance. Toetsen zijn primair formatief, examens summatief.
</p>

</div>

---

<!-- WAAROM DIE KOLOM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waarom kolom 2 erbij moest

<p class="np-subtitle">Zonder die kolom lijkt een specificatie rechtstreeks uit het kwalificatiekader te volgen.</p>

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: start;">
<div style="font-size: 0.92rem; line-height: 1.75;">

- Daartussen zit de **vertaalslag van de onderwijskundige**: het kader omzetten in concreet en observeerbaar geformuleerde leeruitkomsten
- De leeruitkomst is het **enige object dat alle kolommen doorkruist**: specificaties verankeren erop, resultaten worden erop behaald
- De relatie is **veel-op-veel**: dezelfde leeruitkomst kan over meerdere onderdelen verdeeld zijn

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Vraag aan u</h3>
    <p style="font-size: 0.93rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Hoort de summatieve leeruitkomst inderdaad aan het <strong>werkproces</strong>? En klopt het dat er op dossier- en kwalificatieniveau alleen aggregatie is?
    </p>
  </div>
</div>
</div>

<p class="muted" style="font-size: 0.85rem; margin-top: 0.9rem;">
Daarom heet het een <strong>anker</strong>tabel. Het Kernteam stelt deze kolom nog vast; dit is het moment om er iets van te vinden.
</p>

</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide13.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.8rem;">Waar het staat</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.1rem; margin-top: 0.5rem;">Repositories en releases, kort</p>
  </div>
</div>

---

<!-- REPO-INDELING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee plekken, met een duidelijk verschil

<div class="np-grid-2" style="margin-top: 0.7rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">meta</span>
    <h3 style="margin-top: 0.5rem;">De werkplaats</h3>
    <p class="muted" style="font-size: 0.87rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Waar het denkwerk gebeurt: scenario's, het architectuurmodel, meeting-notulen, materiaal dat nog beweegt.
    </p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Public</span>
    <h3 style="margin-top: 0.5rem;">De etalage</h3>
    <p class="muted" style="font-size: 0.87rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Wat af genoeg is om te publiceren: de koppelingspecificaties, de onderbouwing en de besluiten.
    </p>
  </div>
</div>

<p class="muted" style="font-size: 0.9rem; margin-top: 1.2rem; line-height: 1.7;">
Waarom dit ertoe doet voor u: als u iets wilt nalezen of doorsturen naar een collega, is <strong>Public</strong> de plek. Daar staat geen halffabricaat tussen. Alles wat er staat is bedoeld om gelezen te worden.
</p>

</div>

---

<!-- RELEASE MANAGEMENT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat een release betekent

<p class="np-subtitle">Een versienummer is een belofte, geen datum.</p>

<div class="np-grid-3" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-green">
    <span class="np-badge green">Patch</span>
    <h3 style="margin-top: 0.5rem;">Verduidelijking</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Een typefout, een betere formulering. De betekenis verandert niet.</p>
  </div>
  <div class="np-card accent-blue">
    <span class="np-badge blue">Minor</span>
    <h3 style="margin-top: 0.5rem;">Er kan iets bij</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Een nieuw scenario, een extra optioneel veld. Wie al gebouwd heeft, hoeft niets te doen.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">Major</span>
    <h3 style="margin-top: 0.5rem;">Er verandert iets fundamenteels</h3>
    <p class="muted" style="font-size: 0.85rem; margin: 0;">Een begrip of een rij in de ankertabel wijzigt. Wie gebouwd heeft, moet aanpassen.</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 1.2rem;">
  Een instelling of leverancier kan aan het nummer zien <strong>of er werk aan de winkel is</strong>.
</div>

</div>

---

<!-- DIVIDER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide15.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 3</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.8rem;">Waar we nu aan werken</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.1rem; margin-top: 0.5rem;">Regelsets: wie mag wat kiezen</p>
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
Kees van Ginkel (Eduarte) herkende dit en noemde verwante gevallen:
"minimaal twee vreemde talen", "deze keuze mag pas na Engels", slaag-zakregels
per opleiding.
-->

---

<!-- DE REGELSET -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De regel staat los van het onderwijs

<p class="np-subtitle">Kiesbaarheid is geen eigenschap van een keuzedeel, maar een regel erover.</p>

<div class="np-pipeline" style="margin-top: 1.1rem;">
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

<p class="muted" style="font-size: 0.88rem; margin-top: 1.2rem; line-height: 1.7;">
Een voorwaarde gaat over <strong>wat je hebt behaald</strong>, niet over welke specificatie je hebt doorlopen. Zo blijft een regel geldig als het onderwijs verandert. Zestien eisen liggen er; de vorm is nog concept.
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

# Wat we u vragen

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
  <div class="np-card accent-orange">
    <span class="np-badge orange">1</span>
    <h3 style="margin-top: 0.5rem;">Klopt de ankertabel?</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Met name de nieuwe kolom: hoort de summatieve leeruitkomst aan het werkproces, en klopt de aggregatie daarboven?
    </p>
  </div>
  <div class="np-card accent-blue">
    <span class="np-badge blue">2</span>
    <h3 style="margin-top: 0.5rem;">Kent u een keuzeregel die niet past?</h3>
    <p class="muted" style="font-size: 0.88rem; margin: 0.3rem 0 0; line-height: 1.6;">
      Een regel uit uw instelling die met de regelset <strong>niet</strong> uit te drukken is. Dat is precies wat we willen weten voordat de vorm vastligt.
    </p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 1.3rem;">
  Een tegenvoorbeeld is waardevoller dan instemming. Alles staat nog op <strong>concept</strong>.
</div>

</div>

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
