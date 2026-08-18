---
theme: default
title: Koppelvlakspecificaties, geconsolideerd en releasebaar
info: Sessie kerngroep techniek, 19 augustus 2026: de eerste structuur voor het eindproduct, de publieke repository, release management en het alpha-document v0.0.1.
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
    De eerste structuur voor het eindproduct
  </p>
  <div style="font-size: 0.92rem; color: var(--np-ink);">
    <strong>Kerngroep techniek</strong> &middot; Amersfoort
  </div>
  <div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.3rem;">OKx &middot; Onderwijskoppelingen &middot; Npuls &middot; 19 augustus 2026</div>
</div>

<!--
Framing vanaf de eerste zin: vereenvoudiging en consolidatie van wat er al was, geen
koerswijziging. De aanleiding is de vraag uit de keten zelf: "wanneer is iets af, en waar
vinden we het?" Dit gezelschap heet de kerngroep techniek.
-->

---

<!-- OPENING: HET KERNPUNT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; text-align: center; padding: 0 2rem;">
  <div style="font-family: 'Cooper Light BT', serif; font-size: 2.1rem; line-height: 1.4; color: var(--np-blue); max-width: 760px;">
    De eerste structuur van de koppelvlakspecificatie staat.
  </div>
  <p style="margin-top: 1.2rem; font-size: 1.05rem; color: var(--np-dark-gray); max-width: 640px; line-height: 1.6;">
    Gereleased als alpha-document v0.0.1, in docx en pdf.
    Vandaag: hoe die structuur in elkaar zit, en of ermee te werken is.
  </p>
</div>

</div>

<!--
Dit is de boodschap van de hele sessie, in de eerste minuut. Alles wat volgt is uitwerking
van deze ene zin. Niet doorpraten; laten landen en door naar het programma.
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
      <div><strong>Versimpelde werkwijze</strong><br/><span class="muted" style="font-size: 0.8rem;">Twee bronnen, elk hun eigen prioriteit</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>De publieke repository</strong><br/><span class="muted" style="font-size: 0.8rem;">De opbouw van een koppelvlakspecificatie</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Release management</strong><br/><span class="muted" style="font-size: 0.8rem;">Van bron naar releasepakket</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">4</span>
      <div><strong>Alpha-document v0.0.1</strong><br/><span class="muted" style="font-size: 0.8rem;">Wat erin zit en wat we vragen</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">5</span>
      <div><strong>Planning</strong><br/><span class="muted" style="font-size: 0.8rem;">De belangrijkste issues voor de komende periode</span></div>
    </div>
  </div>
</div>

<!--
De volgorde is de agenda zoals Ruud die heeft vastgesteld. Tussendoor een werkdeel: iedereen
gaat zelf de repository en het document in. Er is bewust geen volledige demo.
-->

---

<!-- DIVIDER DEEL 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 1</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Versimpelde werkwijze</h1>
  </div>
</div>

<!--
Kernwoorden: versimpeld, consolidatie, bestendiging; nooit "nieuw" of "anders".
De inhoud die iedereen kent blijft; hij wordt beter vindbaar en expliciet af of niet-af.
-->

---

<!-- AANLEIDING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De aanleiding

<div class="np-grid-2" style="margin-top: 0.8rem;">
<div style="font-size: 0.98rem; line-height: 1.9;">

- De vraag uit de keten: <strong>"wanneer is iets af, en waar vinden we het?"</strong>
- Af en onderweg stonden door elkaar; welke versie telt was niet te zien
- De inhoud verandert niet: dezelfde informatiestromen, dezelfde begrippen

</div>
<div>
  <div class="np-card accent-orange">
    <h3>Consolidatie, geen koerswijziging</h3>
    <p style="font-size: 0.95rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0.4rem 0 0;">
      Wat af is, staat op &eacute;&eacute;n publieke plek en krijgt via
      release management een versienummer. Wat nog rijpt, blijft werkmateriaal.
    </p>
  </div>
</div>
</div>

</div>

<!--
Kort houden; de rest mondeling: werkmateriaal (onderzoek, concepten) en vastgestelde
specificaties stonden op dezelfde plek, daardoor was voor leveranciers niet te zien wat
telde. De informatiestromen-hoofdplaat en het begrippenkader blijven de kern.
-->

---

<!-- TWEE BRONNEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee bronnen, elk hun eigen prioriteit

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: center; gap: 1rem;">
<div style="font-size: 0.92rem; line-height: 1.85;">

- De <strong>werkomgeving</strong>: bronbestanden, iteraties en context; daar wordt gewerkt
- De <strong>publieke bron</strong>: het product, de geconsolideerde koppelvlakspecificaties en hun releases
- Wat rijp is, verhuist via review van werkomgeving naar publieke bron

</div>
<div style="display: flex; justify-content: center;">
  <img src="/platen/repo-setup.jpg" style="max-height: 400px; width: auto; border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,0.18);" />
</div>
</div>

</div>

<!--
Leeswijzer bij de plaat: links de private source (interne planning en referentiemateriaal),
midden de public source met CI/CD, rechts de public release waarmee een implementeerder
bouwt, met de rollen erboven. De scheiding is er een van prioriteiten: werken versus
opleveren.
-->

---

<!-- META WORDT PRIVE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De werkomgeving wordt privé

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
<div style="font-size: 0.95rem; line-height: 1.9;">

- De meta-repository wordt <strong>privé</strong>: daar gaat het team aan het werk, en blijft het
- Wat daar leeft: bronbestanden en iteraties, <strong>productiviteitstooling</strong>, en interne context zoals memo's van de adviesgroep
- De publieke repository is puur de <strong>productrepository</strong>: de specificaties en hun releases

</div>
<div>
  <div class="np-card accent-blue">
    <h3>Wat dit voor afnemers betekent</h3>
    <p class="muted" style="font-size: 0.86rem; margin: 0;">Alles wat nodig is om een koppelvlak te bouwen, staat in de publieke repository. Niets daarbuiten is nodig.</p>
  </div>
</div>
</div>

</div>

<!--
Deze vraag komt sowieso: wat gebeurt er in meta versus public. Meta is de source repository
met complexere bestanden en meer context; de koppelvlakspecificaties hebben markdown-bronnen
die daar geïtereerd worden; releases en definitieve documenten leven publiek.
-->

---

<!-- DIVIDER DEEL 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">De publieke repository</h1>
  </div>
</div>

<!--
Zwaartepunt van de sessie: de kaart van de repository en de vaste opbouw van een
koppelvlakspecificatie. Alles hier is straks in het werkdeel zelf aan te klikken.
-->

---

<!-- REPO-STRUCTUUR -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee folders

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: start;">
<div>

<pre style="background: #f6f8fa; color: var(--np-ink); border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.8rem 1rem; font-size: 0.78rem; line-height: 1.55; margin: 0; font-family: ui-monospace, monospace;">Koppelvlakspecificaties/
├── inleiding.md
├── afbakening.md          ← eisen aan de keten
├── Applicatiecomponenten/ ← rollen + endpoints
├── Interactiepatronen/    ← per koppeling, met
│                            functionele eisen
├── Datamodelschema's/     ← JSON-schema's
├── auth-standaard.md      ← eigen pijler
└── uitgangspunten.md</pre>

</div>
<div>

<pre style="background: #f6f8fa; color: var(--np-ink); border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.8rem 1rem; font-size: 0.78rem; line-height: 1.55; margin: 0; font-family: ui-monospace, monospace;">Referentiemateriaal/
├── adr/                   ← besluiten met
│                            onderbouwing
├── principes/
├── kaderscenario's/       ← de leerroutes
└── persona's/             ← wie de student is</pre>

<p class="muted" style="font-size: 0.82rem; margin-top: 0.4rem;">
Bouwen gebeurt uit <strong>Koppelvlakspecificaties/</strong>; het waarom staat in <strong>Referentiemateriaal/</strong>.
</p>

</div>
</div>

</div>

<!--
Hier meteen de opdracht geven: de link staat in de chat en als QR verderop. Open
github.com/Npuls-OKx/Public en klik mee door de folders terwijl dit deel loopt.
-->

---

<!-- OPBOUW KOPPELVLAKSPECIFICATIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De opbouw van een koppelvlakspecificatie

<div class="np-grid-2" style="margin-top: 0.5rem; align-items: center; gap: 1rem;">
<div style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.76rem;">
  <div class="np-card accent-blue" style="padding: 0.4rem 0.7rem;"><strong>Functionele eisen</strong>: dragen de doelen van Leren zonder Drempels</div>
  <div class="np-card accent-orange" style="padding: 0.4rem 0.7rem;"><strong>Interactiepatronen</strong>: de processen waarmee referentiecomponenten interacteren</div>
  <div class="np-card accent-green" style="padding: 0.4rem 0.7rem;"><strong>Endpoints</strong>: wat een referentiecomponent implementeert, per interactie</div>
  <div class="np-card accent-blue" style="padding: 0.4rem 0.7rem;"><strong>Applicatiecomponenten</strong>: de componenten die via koppelvlakken interacteren</div>
  <div class="np-card accent-green" style="padding: 0.4rem 0.7rem;"><strong>Datamodelschema's</strong>: JSON-schema's van de payloads</div>
</div>
<div style="display: flex; justify-content: center;">
  <img src="/platen/koppelvlak-specificatie-breakdown.png" style="max-height: 400px; width: auto; border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,0.18);" />
</div>
</div>

<div class="np-bottomline" style="margin-top: 0.5rem;">
  Volg de pijlen: <strong>functionele eisen</strong> bepalen de processen, die bepalen de <strong>endpoints</strong>, en endpoints gebruiken de <strong>datamodelschema's</strong>.
</div>

</div>

<!--
De authenticatiestandaard hoort hier mondeling bij: die ligt als buitenlaag om alle
koppelvlakken heen en komt in deel 4 apart terug; de plaat wordt daar nog op bijgetekend.
Wie/wat/hoe: applicatiecomponenten (wie), datamodelschema's (wat), interactiepatronen (hoe).
-->

---

<!-- VOORBEELD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorbeeld

<div style="max-width: 46rem; margin: 1rem auto 0; font-size: 0.98rem; line-height: 1.9;">

Eén lijn door het document. De keten-eis <em>"een vastgestelde specificatie bereikt elk systeem dat ermee werkt"</em> is per koppeling afgeleid naar een functionele eis. Voor planning en roostering: <em>"de onderwijscatalogus moet het planningssysteem kunnen laten weten dat een specificatie gereed is om te plannen&nbsp;&hellip;"</em>.

Die eis werkt via de interactie <strong>specificatie planbaar melden</strong>: een dun event met id en versie, waarna de afnemer de structuur of de delta ophaalt. De interactie landt op het endpoint <code>/onderwijsspecificaties/{id}</code>, met <code>education-specification.json</code> als antwoord.

Zo leest elk hoofdstuk door naar het volgende: eis, proces, endpoint, schema.

</div>

</div>

<!--
Rustig voorlezen; dit is de leeservaring die het document zelf moet geven. In het werkdeel
loopt iedereen precies deze lijn zelf na.
-->

---

<!-- VOORUITBLIK FUNCTIONELE EISEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar de functionele eisen vandaan komen

<div class="np-pipeline" style="margin-top: 1.4rem;">
  <div class="np-step blue" style="flex: 1;">
    <strong style="font-size: 0.9rem;">Leren zonder Drempels</strong>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue" style="flex: 1;">
    <strong style="font-size: 0.9rem;">Doelen en epics</strong>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1;">
    <strong style="font-size: 0.9rem;">Features en stories</strong>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1;">
    <strong style="font-size: 0.9rem;">Functionele eisen</strong>
  </div>
</div>

<div style="display: flex; justify-content: center; margin-top: 1.4rem;">
  <div class="np-card accent-green" style="max-width: 34rem;">
    <p style="font-size: 0.95rem; color: var(--np-dark-gray); line-height: 1.6; margin: 0;">
      Elke functionele eis wordt herleidbaar tot de wens waaruit hij voortkomt. En andersom: geen eis zonder herkomst.
    </p>
  </div>
</div>

</div>

<!--
Alleen aankondigen, niet uitwerken; geen toezeggingen over wanneer. Mondeling: wensen en
eisen van instellingen en van leveranciers landen als features en stories in deze keten ,
de zaal zit er dus zelf in. Bij vragen: dat is precies de werkvraag van het werkdeel.
-->

---

<!-- DIVIDER DEEL 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 3</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Release management</h1>
  </div>
</div>

<!--
Dit deel beantwoordt de kernvraag uit de aanleiding: wanneer is iets af. Kort houden.
-->

---

<!-- RELEASE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van bron naar releasepakket

<div class="np-pipeline" style="margin-top: 1.6rem;">
  <div class="np-step blue" style="flex: 1; max-width: 230px;">
    <strong style="font-size: 0.92rem;">Geconsolideerde bron</strong>
    <small>de publieke repository</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1; max-width: 230px;">
    <strong style="font-size: 0.92rem;">Automatische controle en bouw</strong>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1; max-width: 230px;">
    <strong style="font-size: 0.92rem;">Releasepakket</strong>
    <small>&eacute;&eacute;n document, docx en pdf</small>
  </div>
</div>

<div class="np-proof-strip" style="justify-content: center; margin-top: 1.4rem;">
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Links en conventies automatisch gecontroleerd</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Diagrammen meegebouwd</div>
  <div class="np-proof-divider"></div>
  <div class="np-proof-item"><span class="np-proof-check">&#10003;</span>Versienummer zegt wat er gold</div>
</div>

</div>

<!--
Antwoord op "wanneer is iets af": als het in een release zit. Verwijzen gebeurt naar een
versienummer, niet naar de laatste stand van een branch. Feedback loopt via issues; elke
volgende release verwerkt die zichtbaar.
-->

---

<!-- DIVIDER DEEL 4 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 4</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Alpha-document v0.0.1</h1>
  </div>
</div>

<!--
Alpha zegt precies wat het is: compleet genoeg om op te schieten, niet af.
-->

---

<!-- WAT ERIN ZIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er in v0.0.1 zit

<div style="max-width: 40rem; margin: 0.8rem auto 0; font-size: 0.98rem; line-height: 2.0;">

- Inleiding en afbakening, met de <strong>eisen aan de keten</strong>
- <strong>Applicatiecomponenten</strong> met hun endpoints
- <strong>Interactiepatronen</strong> met functionele eisen, per koppeling
- <strong>Authenticatiestandaard</strong>
- <strong>Datamodelschema's</strong> en voorbeeldpayloads
- Uitgangspunten en veldnamenmapping

</div>

</div>

<!--
Leesvolgorde is de volgorde van het gebundelde document. Kort langslopen, niet openen ,
dat gebeurt in het werkdeel.
-->

---

<!-- VRAAGSTELLING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd: feedback op de structuur

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: center;">
<div style="font-size: 0.95rem; line-height: 1.9;">

- Is het document <strong>logisch te volgen</strong> en navigeerbaar?
- De inhoud is nog niet af: modellen, authenticatielagen en interactiepatronen worden nog ge&iuml;tereerd; inhoudelijke feedback komt in latere rondes
- Wat schuurt in de structuur: <strong>meld het als issue onder OKx Public</strong>

</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 0.4rem;">
  <img src="/shots/qr-npuls-okx-public.png" style="width: 190px; border-radius: 8px; border: 1px solid #e2e8f0;" />
  <span class="muted" style="font-size: 0.8rem;">github.com/Npuls-OKx/Public</span>
</div>
</div>

</div>

<!--
Expliciet ontmoedigen dat mensen morgen de inhoud gaan fileren: daar wordt nog veel
overheen geïtereerd. De vraag is of de structuur draagt. Link ook in de chat delen.
-->

---

<!-- AUTH -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Authenticatie en autorisatie

<div class="np-grid-2" style="margin-top: 0.8rem; align-items: start;">
<div style="font-size: 0.95rem; line-height: 1.9;">

- Doel: <strong>standaarden vaststellen</strong> voor de API-endpoints en de koppelvlakspecificatielaag, niet hoe een partij dat implementeert
- Uitgangspunt: open standaarden, <strong>OAuth 2.0 client credentials</strong>, conform het Edukoppeling-profiel
- Het bestaande OKE-document (hoofdstuk 5) blijft leidend tot het profiel definitief is

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
Bewust kort en eenvoudig: geen lijst eisen richting leveranciers. De diepgang van dit
gesprek bepaalt de zaal; Ruud jaagt de discussie aan als het stil blijft.
-->

---

<!-- WERKDEEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aan de slag

<div class="np-grid-3" style="margin-top: 0.8rem; align-items: start;">
  <div class="np-card accent-blue">
    <span class="np-badge blue">Opdracht 1</span>
    <h3 style="margin-top: 0.5rem; font-size: 0.95rem;">Vind het eigen systeem</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Open <strong>github.com/Npuls-OKx/Public</strong> en zoek het applicatiecomponent-document van het eigen systeem. Welke endpoints raken dat systeem?</p>
  </div>
  <div class="np-card accent-green">
    <span class="np-badge green">Opdracht 2</span>
    <h3 style="margin-top: 0.5rem; font-size: 0.95rem;">Open het releasepakket</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Open v0.0.1 (docx of pdf) en volg &eacute;&eacute;n functionele eis naar zijn interactie en endpoint.</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">Werkvraag</span>
    <h3 style="margin-top: 0.5rem; font-size: 0.95rem;">Hoe komen we tot de functionele eisen?</h3>
    <p class="muted" style="font-size: 0.8rem; margin: 0;">Wat is er per systeem nodig om een eis compleet te noemen? Wat mist er?</p>
  </div>
</div>

<div class="np-bottomline" style="margin-top: 0.8rem;">
  Klopt er iets niet, of is iets niet vindbaar? <strong>Dat is precies de feedback die we zoeken.</strong>
</div>

</div>

<!--
Uitwerksessie: iedereen zelf laten klikken. Rondlopen en verzamelen wat mensen niet kunnen
vinden: dat zijn de eerste issues. De werkvraag is de brug naar de boom-uitwerking.
-->

---

<!-- DIVIDER DEEL 5 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 5</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Planning</h1>
  </div>
</div>

<!--
Overdracht aan Ruud: hij heeft de issues geselecteerd en loopt ze langs.
-->

---

<!-- PLANNING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Planning

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

<p class="muted" style="font-size: 0.82rem; margin-top: 1rem;">De komende periode werken we minimaal drie koppelvlakken op deze manier uit.</p>

</div>

<!--
Dit agendapunt is van Ruud; de slide is het haakje, niet de inhoud.
-->

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Afsluiting: herhaal de oproep. Inlezen v0.0.1, structuurfeedback als issue onder OKx Public.
-->
