---
theme: default
title: Koppelvlakspecificaties, geconsolideerd en releasebaar
info: Sessie kerngroep techniek, 19 augustus 2026 — versimpelde werkwijze, publieke repository, release management en het alpha-document v0.01.
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

<!-- TITELSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide1.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem 4rem; z-index: 1;">
  <h1 style="font-size: 3rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Koppelvlakspecificaties</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 680px; line-height: 1.5; margin-bottom: 1rem;">
    Geconsolideerd, vindbaar en releasebaar &mdash; dezelfde inhoud, eenvoudiger gemaakt
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>Kerngroep techniek</strong> &middot; Amersfoort
  </div>
  <div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.3rem;">OKx &middot; Onderwijskoppelingen &middot; Npuls &middot; 19 augustus 2026</div>
</div>

<!--
Framing vanaf de eerste zin: dit is een VEREENVOUDIGING en CONSOLIDATIE van wat er al was,
geen koerswijziging. Niet zeggen "alles wordt anders". De aanleiding is jullie eigen vraag:
"wanneer is iets af, en waar vinden we het?" Vandaag laten we zien hoe we die vraag beantwoorden.
Let op de term: dit gezelschap heet de kerngroep techniek.
-->

---

<!-- AGENDA -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="margin-left: 42%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding-right: 3rem;">
  <p class="eyebrow">Wat gaan we bespreken</p>
  <h1 style="font-size: 2.1rem !important; margin-bottom: 1.1rem;">Programma</h1>
  <div style="display: flex; flex-direction: column; gap: 0.7rem;">
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">1</span>
      <div><strong>Versimpelde werkwijze</strong><br/><span class="muted" style="font-size: 0.8rem;">Eenvoudiger gemaakt en geconsolideerd</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>De publieke repository</strong><br/><span class="muted" style="font-size: 0.8rem;">Structuur en opbouw van een koppelvlakspecificatie</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Release management</strong><br/><span class="muted" style="font-size: 0.8rem;">Wanneer is iets af, en hoe versies werken</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">4</span>
      <div><strong>Alpha-document v0.01</strong><br/><span class="muted" style="font-size: 0.8rem;">Het eerste releasepakket, om in te lezen</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">5</span>
      <div><strong>Sprintplanning</strong><br/><span class="muted" style="font-size: 0.8rem;">De belangrijkste issues voor de komende periode</span></div>
    </div>
  </div>
</div>

<!--
De volgorde is de agenda zoals Ruud die heeft vastgesteld. Tussendoor is er een werkdeel:
we zetten iedereen zelf aan het werk in de repository en het document. Er is vandaag
bewust geen volledige demo; het werk is nog niet af en dat hoeft het ook niet te zijn.
-->

---

<!-- DIVIDER DEEL 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 1</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Versimpelde werkwijze</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Gewerkt en nagedacht: eenvoudiger gemaakt, geconsolideerd en bestendigd</p>
  </div>
</div>

<!--
Kernwoorden: versimpeld, consolidatie, bestendiging — nooit "nieuw" of "anders".
De inhoud die jullie kennen blijft; we maken hem beter vindbaar en expliciet af of niet-af.
-->

---

<!-- WAAROM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De aanleiding, kort

<p class="np-subtitle">Jullie vroegen het zelf: "wanneer is iets af, en waar vinden we het?"</p>

<div class="np-grid-2" style="margin-top: 0.3rem;">
<div style="font-size: 0.95rem; line-height: 1.8;">

- Af en onderweg stonden door elkaar; <strong>welke versie telt</strong> was niet te zien
- De inhoud verandert niet: <strong>dezelfde informatiestromen, dezelfde begrippen</strong>

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Consolidatie, geen koerswijziging</h3>
    <p style="font-size: 0.95rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Wat af is, staat voortaan op &eacute;&eacute;n publieke plek met een versienummer.
      Wat nog rijpt, blijft werkmateriaal.
    </p>
  </div>
</div>
</div>

</div>

<!--
Kort houden op de slide; de rest mondeling, zoals in het overleg: werkmateriaal
(onderzoek, concepten) en vastgestelde specificaties stonden op dezelfde plek,
daardoor was voor leveranciers niet te zien wat telde. Benadrukken: de
informatiestromen-hoofdplaat en het begrippenkader blijven de kern; die zijn niet veranderd.
-->

---

<!-- TWEE BRONNEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee bronnen, één richting

<p class="np-subtitle">Van werkomgeving naar publieke bron: alleen wat af is, steekt over.</p>

<div style="display: flex; justify-content: center; margin-top: 0.2rem;">
  <img src="/platen/repo-setup.jpg" style="max-height: 360px; width: auto; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.12);" />
</div>

<div class="np-bottomline" style="margin-top: 0.6rem;">
  Kijk naar de richting van de pijl: consolidatie stroomt van <strong>werkomgeving</strong> naar <strong>Npuls-OKx/Public</strong> &mdash; nooit andersom.
</div>

</div>

<!--
Leeswijzer bij de plaat: links de werkomgeving (onderzoek, notulen, memo's, eerste uitwerkingen),
rechts de publieke bron met alleen geconsolideerde koppelvlakspecificaties. Wat rijp is verhuist
via een review naar Public; daar komt het in een release terecht.
-->

---

<!-- DIVIDER DEEL 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">De publieke repository</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Waar wat staat, en hoe een koppelvlakspecificatie is opgebouwd</p>
  </div>
</div>

---

<!-- REPO-STRUCTUUR -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Eén map om te bouwen, één map voor context

<p class="np-subtitle">github.com/Npuls-OKx/Public &mdash; compact en compleet.</p>

<div class="np-grid-2" style="margin-top: 0.4rem; align-items: start;">
<div>

```text
Koppelvlakspecificaties/
├── inleiding.md
├── afbakening.md          ← eisen aan de keten
├── Applicatiecomponenten/ ← rollen + endpoints
├── Interactiepatronen/    ← per koppeling, met
│                            functionele eisen
├── Datamodelschema's/     ← JSON-schema's
├── auth-standaard.md      ← eigen pijler
└── uitgangspunten.md
```

</div>
<div>

```text
Referentiemateriaal/
├── adr/                   ← besluiten met
│                            onderbouwing
├── principes/
├── kaderscenario's/       ← leerroutes,
│                            persona's
└── memos/
```

<p class="muted" style="font-size: 0.82rem; margin-top: 0.4rem;">
Bouwen doe je uit <strong>Koppelvlakspecificaties/</strong>; het waarom vind je in <strong>Referentiemateriaal/</strong>.
</p>

</div>
</div>

</div>

<!--
Dit is de kaart van de repository. Alles wat een leverancier nodig heeft om een koppelvlak
te bouwen staat in de ene map; de onderbouwing van keuzes (ADR's, principes, kaderscenario's)
staat ernaast, ter referentie, niet als verplichte kost.
-->

---

<!-- OPBOUW KOPPELVLAKSPECIFICATIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De opbouw van een koppelvlakspecificatie

<p class="np-subtitle">Vier bouwstenen per koppelvlak, met authenticatie als gedeelde pijler.</p>

<!-- Zodra de componenten-plaat is geupload naar public/platen/, deze img activeren
     en de kaarten hieronder verwijderen of naar de sprekersnotities verplaatsen:
<div style="display: flex; justify-content: center; margin-top: 0.2rem;">
  <img src="/platen/koppelvlakspec-opbouw.png" style="max-height: 400px; width: auto;" />
</div>
-->

<div class="np-grid-2" style="margin-top: 0.4rem; align-items: start; gap: 0.7rem;">
  <div class="np-card accent-blue" style="padding: 0.7rem 0.9rem;">
    <span class="np-badge blue">Wie</span>
    <h3 style="margin-top: 0.3rem; font-size: 1rem;">Applicatiecomponenten</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Rollen uit de MORA; per component de endpoints die hij aanbiedt. E&eacute;n systeem kan meerdere rollen vervullen.</p>
  </div>
  <div class="np-card accent-orange" style="padding: 0.7rem 0.9rem;">
    <span class="np-badge orange">Hoe</span>
    <h3 style="margin-top: 0.3rem; font-size: 1rem;">Interactiepatronen</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Per koppeling de interacties (melden, ophalen, terugmelden), verankerd in functionele eisen.</p>
  </div>
  <div class="np-card accent-green" style="padding: 0.7rem 0.9rem;">
    <span class="np-badge green">Wat</span>
    <h3 style="margin-top: 0.3rem; font-size: 1rem;">Datamodelschema's</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">JSON-schema's van de payloads; hi&euml;rarchisch en valideerbaar.</p>
  </div>
  <div class="np-card accent-blue" style="padding: 0.7rem 0.9rem;">
    <span class="np-badge blue">Toegang</span>
    <h3 style="margin-top: 0.3rem; font-size: 1rem;">Authenticatiestandaard</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">E&eacute;n gedeeld mechanisme voor alle koppelvlakken; eigen pijler, los van de inhoud.</p>
  </div>
</div>

</div>

<!--
Per koppelvlak dezelfde vier bouwstenen: wie (applicatiecomponent met endpoints),
hoe (interactiepatroon met functionele eisen), wat (JSON-schema's) en toegang (auth).
Als de eigen componenten-plaat is geupload vervangt die de vier kaarten; de leeswijzer blijft gelijk.
-->

---

<!-- VOORBEELDEN PER HOOFDSTUK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Elk hoofdstuk in één voorbeeld

<p class="np-subtitle">Zo leest de specificatie &mdash; van eis tot endpoint.</p>

<div style="font-size: 0.78rem; margin-top: 0.3rem;">

| Hoofdstuk | Voorbeeld uit het document |
|---|---|
| Afbakening: eisen aan de keten | "Een vastgestelde specificatie bereikt elk systeem dat ermee werkt" — afgeleid naar functionele eisen per koppeling |
| Interactiepatroon (functionele eis) | "De onderwijscatalogus moet het planningssysteem kunnen laten weten dat een specificatie gereed is om te plannen" |
| Interactiepatroon (interactie) | Specificatie planbaar melden: dun event met id en versie, asynchroon; daarna haalt de afnemer de structuur of delta op |
| Applicatiecomponent (endpoint) | `/onderwijsspecificaties/{id}` · GET · response `education-specification.json` · statuscodes 200, 400, 404 |
| Datamodelschema | `education-specification.json`: hiërarchische onderwijsspecificatie, valideerbaar JSON-schema |

</div>

<div class="np-bottomline" style="margin-top: 0.5rem;">
  De lijn is steeds dezelfde: <strong>keten-eis &rarr; functionele eis &rarr; interactie &rarr; endpoint</strong>.
</div>

</div>

<!--
Per hoofdstuk kort stilstaan bij dit voorbeeld; alles komt uit hetzelfde document en wijst
naar elkaar door. Niet dieper ingaan dan dit; wie meer wil ziet het straks in het werkdeel zelf.
-->

---

<!-- FUNCTIONELE EISEN + VOORUITBLIK BOOM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar komen de functionele eisen vandaan?

<p class="np-subtitle">Vooruitblik: elke eis wordt herleidbaar tot de opdracht van Npuls.</p>

<div class="np-pipeline" style="margin-top: 1.2rem;">
  <div class="np-step blue" style="flex: 1;">
    <strong style="font-size: 0.88rem;">Opdracht</strong>
    <small>Leren zonder Drempels</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue" style="flex: 1;">
    <strong style="font-size: 0.88rem;">Doelen en epics</strong>
    <small>wat de keten kan</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1;">
    <strong style="font-size: 0.88rem;">Features en stories</strong>
    <small>toetsbare wensen</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1;">
    <strong style="font-size: 0.88rem;">Functionele eisen</strong>
    <small>per koppelvlak</small>
  </div>
</div>

<div class="np-grid-2" style="margin-top: 1rem; align-items: start;">
  <div class="np-card accent-green">
    <h3 style="font-size: 0.98rem;">Wat dit oplevert</h3>
    <p class="muted" style="font-size: 0.82rem; margin: 0;">Bij elke functionele eis is na te lopen w&aacute;&aacute;rom hij bestaat &mdash; en andersom: geen eis zonder herkomst.</p>
  </div>
  <div class="np-card accent-orange">
    <h3 style="font-size: 0.98rem;">Vandaag alleen de aankondiging</h3>
    <p class="muted" style="font-size: 0.82rem; margin: 0;">De requirementsboom is in opbouw; de uitwerking tonen we in een volgende sessie.</p>
  </div>
</div>

</div>

<!--
Alleen aankondigen, niet uitwerken (afspraak met Ruud en Garik). Als er vragen komen:
prima gespreksstof voor het werkdeel, de werkvraag daar is precies "hoe komen we tot
die functionele eisen?". Niet de boom zelf laten zien; die is nog niet af.
-->

---

<!-- DIVIDER DEEL 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 3</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Release management</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Wanneer iets af is, zeggen we het met een versienummer</p>
  </div>
</div>

---

<!-- RELEASE-WERKWIJZE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van repository naar releasepakket

<p class="np-subtitle">Een release is een gebouwd, gebundeld en genummerd document &mdash; geen losse map bestanden.</p>

<div class="np-pipeline" style="margin-top: 1.3rem;">
  <div class="np-step blue" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.92rem;">Geconsolideerde bron</strong>
    <small>de publieke repository</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.92rem;">Releasemanifest</strong>
    <small>volgorde en versienummer</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1; max-width: 210px;">
    <strong style="font-size: 0.92rem;">Releasepakket</strong>
    <small>&eacute;&eacute;n document + losse bestanden</small>
  </div>
</div>

<div class="np-proof-strip" style="justify-content: center; margin-top: 1.2rem;">
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Links en conventies automatisch gecontroleerd</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Diagrammen meegebouwd</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Versienummer zegt wat er gold</div>
</div>

</div>

<!--
Antwoord op "wanneer is iets af": als het in een release zit. Verwijzen doe je naar een
versienummer, niet naar "de laatste stand van een branch". Feedback loopt via issues op de
publieke repository; elke volgende release verwerkt die zichtbaar.
-->

---

<!-- DIVIDER DEEL 4 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 4</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Alpha-document v0.01</h1>
    <p style="color: rgba(255,255,255,0.88); font-size: 1.15rem; margin-top: 0.5rem;">Het eerste releasepakket ligt er &mdash; om in te lezen en op te schieten</p>
  </div>
</div>

---

<!-- ALPHA-DOCUMENT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er in v0.01 zit — en wat we vragen

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: start;">
<div style="font-size: 0.88rem; line-height: 1.7;">

**Inhoud, in leesvolgorde:**

- Inleiding en afbakening met de <strong>eisen aan de keten</strong>
- <strong>Applicatiecomponenten</strong> met hun endpoints
- <strong>Interactiepatronen</strong> met functionele eisen, per koppeling
- <strong>Authenticatiestandaard</strong>
- <strong>Datamodelschema's</strong> en voorbeeldpayloads
- Uitgangspunten en veldnamenmapping

</div>
<div>
  <div class="np-card accent-orange" style="margin-bottom: 0.6rem;">
    <h3 style="font-size: 0.98rem;">Wat we van jullie vragen</h3>
    <p class="muted" style="font-size: 0.82rem; margin: 0;">Inlezen v&oacute;&oacute;r de volgende sessie. Wat schuurt met je eigen implementatie of met de oude situatie: meld het als issue.</p>
  </div>
  <div class="np-card accent-blue">
    <h3 style="font-size: 0.98rem;">Oud versus nieuw</h3>
    <p class="muted" style="font-size: 0.82rem; margin: 0;">De inhoudelijke lijn van OKE loopt door; wat anders leest dan je gewend bent horen we graag expliciet.</p>
  </div>
</div>
</div>

</div>

<!--
Alpha betekent: compleet genoeg om op te schieten, niet af. Jos kijkt mee met de OKE-bril
op oud versus nieuw; nodig de rest uit hetzelfde te doen vanuit hun eigen systeem.
-->

---

<!-- AUTH -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Authenticatie: bewust eenvoudig

<p class="np-subtitle">Eén uitgangspunt voor alle koppelvlakken, aansluitend op wat er al is.</p>

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: start;">
<div style="font-size: 0.9rem; line-height: 1.75;">

- Uitgangspunt: <strong>OAuth 2.0 client credentials</strong>, conform het Edukoppeling-profiel
- Machine-naar-machine, cloudvriendelijk &mdash; de les uit eerdere PKI-discussies
- Zolang het profiel niet definitief is, blijft het bestaande <strong>OKE-document</strong> leidend

</div>
<div>
  <div class="np-card accent-green">
    <h3 style="font-size: 0.98rem;">Status</h3>
    <p class="muted" style="font-size: 0.84rem; margin: 0;">Voorlopig vastgesteld als uitgangspunt; formele bekrachtiging loopt via de werkgroep OKx.</p>
  </div>
</div>
</div>

</div>

<!--
Bewust kort en simpel houden: geen lange lijst eisen richting leveranciers. De diepgang
van dit gesprek mag de zaal zelf bepalen; Ruud jaagt de discussie aan als het stil blijft.
-->

---

<!-- WERKDEEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aan de slag — zelf kijken

<p class="np-subtitle">Geen demo; jullie zoeken zelf. Dat is precies de bedoeling van deze opzet.</p>

<div class="np-grid-3" style="margin-top: 0.6rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Opdracht 1</span>
    <h3 style="margin-top: 0.5rem; font-size: 0.95rem;">Vind je eigen rol</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Open <strong>github.com/Npuls-OKx/Public</strong> en zoek het applicatiecomponent-document dat jouw systeem beschrijft. Welke endpoints raken jou?</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Opdracht 2</span>
    <h3 style="margin-top: 0.5rem; font-size: 0.95rem;">Open het releasepakket</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Open het gebouwde v0.01-document en volg &eacute;&eacute;n functionele eis naar zijn interactie en endpoint.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">Werkvraag</span>
    <h3 style="margin-top: 0.5rem; font-size: 0.95rem;">Hoe komen we tot de functionele eisen?</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Wat is er voor jouw systeem nodig om een eis compleet te noemen? Wat mist er?</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 0.8rem;">
  Kom je iets tegen dat niet klopt of niet vindbaar is? <strong>Dat is precies de feedback die we zoeken.</strong>
</div>

</div>

<!--
Uitwerksessie: iedereen zelf laten klikken. Loop rond, verzamel wat mensen niet kunnen vinden;
dat zijn de eerste issues. De werkvraag over functionele eisen is de brug naar de boom-sessie
van de volgende keer.
-->

---

<!-- SPRINTPLANNING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Sprintplanning

<p class="np-subtitle">De belangrijkste issues voor de komende periode &mdash; selectie en toelichting door Ruud.</p>

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
  <div class="np-card accent-blue">
    <h3 style="font-size: 0.98rem;">Uit de publieke repository</h3>
    <p class="muted" style="font-size: 0.84rem; margin: 0;">De issues die de koppelvlakspecificaties zelf aanscherpen.</p>
  </div>
  <div class="np-card accent-orange">
    <h3 style="font-size: 0.98rem;">Uit de werkomgeving</h3>
    <p class="muted" style="font-size: 0.84rem; margin: 0;">Wat er in voorbereiding staat om over te steken naar de publieke bron.</p>
  </div>
</div>

<p class="muted" style="font-size: 0.82rem; margin-top: 1rem;">Vooruitblik: de komende periode werken we minimaal drie koppelvlakken op deze manier uit.</p>

</div>

<!--
Dit agendapunt is van Ruud; hij selecteert de issues en loopt ze langs. De slide is het haakje,
niet de inhoud.
-->

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Afsluiting: bedanken, oproep herhalen (inlezen v0.01, feedback als issue), volgende sessie
komt de requirementsboom-uitwerking.
-->
