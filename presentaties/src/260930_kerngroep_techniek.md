---
theme: default
title: "Kerngroep techniek, 30 september 2026"
info: "Kerngroep techniek 30 september 2026, Amersfoort: de voorbeelduitwerking van leerroute 1, versionering, business-architectuur en het koppeling-ID."
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
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 36rem;">Voorbeelduitwerking leerroute 1 &middot; Versionering &middot; Business-architectuur &middot; Koppeling-ID</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 30 september 2026 &middot; Amersfoort</div>
</div>

<!--
Sessie op locatie. Vier blokken, elk met een eigen eigenaar: Niek de voorbeelduitwerking, Garik
de versionering, Niels de business-architectuur, het kernteam het koppeling-ID. Opzet, nog af te
stemmen met Garik en Niels.
-->

---

<!-- 2. AGENDA -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Agenda

<div style="margin-top:0.6rem;max-width:92%;">
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#B8BEC7;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">1</div><div style="line-height:1.4;"><strong>Afspraken van 15 september</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">Per afspraak de stand van vandaag</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#7CCBA8;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">2</div><div style="line-height:1.4;"><strong>Voorbeelduitwerking leerroute 1 (Niek)</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">De opleiding van Jochem in het informatiemodel, met de vraag om feedback per regel</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#7A97F2;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">3</div><div style="line-height:1.4;"><strong>Versionering met een voorbeeldflow (Garik)</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">De iteratie op Public PR 100, toegelicht aan een voorbeeld</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#E9A27F;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">4</div><div style="line-height:1.4;"><strong>Business-architectuur en stories (Niels)</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">De stories uit de PoC-scholen</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#00AF81;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">5</div><div style="line-height:1.4;"><strong>Koppeling-ID, gevraagd, vervolg en peiling</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">Public #107, de reviewvraag op PR 104 en de peiling</span></div></div>
</div>

</div>

<!--
Opzet van het kernteam, af te stemmen met Garik en Niels. Blok 2 vraagt de meeste tijd: de
voorbeelduitwerking is de afspraak van 15 september en levert de kerngroep iets concreets om op
te reageren. De peiling is de vaste afsluiting uit #205.
-->

---

<!-- 3. AFSPRAKEN 15 SEPTEMBER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Afspraken van 15 september

<div style="font-size: 0.88rem; line-height: 1.6; margin-top: 0.6rem;">

| Afgesproken | Wie | Stand op 25 september |
|---|---|---|
| Voorbeelduitwerking van het informatiemodel langs leerroute 1 | Niek | Ligt er: [meta PR 252](https://github.com/Npuls-OKx/meta/pull/252), vandaag op tafel |
| Iteratie op de versionering met een voorbeeldflow, en een sessie vooraf | Garik | [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) staat op draft |
| Business-architectuur doorontwikkelen en stories ophalen bij de PoC-scholen | Niels | Milestone [requirementsboom](https://github.com/Npuls-OKx/Public/milestone/3), negen open |
| [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104) bekijken en opmerkingen achterlaten | Kerngroep | Open, nog zonder opmerkingen |
| Voorstel voor een kort koppeling-ID, beide richtingen in een specificatie | Kernteam | [Public #107](https://github.com/Npuls-OKx/Public/issues/107), voorstel vandaag |
| Aanpak voor draagvlak bij leveranciers, plus de tijdsbesteding | Ruud en Hans | Follow-up na vandaag |

</div>

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.7rem;">
Ook afgesproken: <a href="https://github.com/Npuls-OKx/Public/pull/82">Public PR 82</a> en PR 100 staan op draft, en een draft-PR vraagt geen review. De keuzeregelsets volgen zodra er ruimte is.
</div>

</div>

<!--
Bron: het deck met afspraken van 15 september (meta, presentaties/src). Zes afspraken, elk met
de stand van vandaag uit GitHub. De enige die vandaag nog open staat richting de groep is de
review op PR 104: daar liggen nog geen opmerkingen. Dat is geen verwijt; het is de reden om er
vandaag samen een moment voor te nemen.
-->

---

<!-- 4. VERZET WERK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er sinds 15 september is verzet

<div style="display:grid;grid-template-columns:8.5rem repeat(5,1fr);gap:0.6rem 0.7rem;align-items:center;margin-top:0.9rem;max-width:92%;">
<div></div>
<div style="font-size:0.78rem;color:var(--np-mid-gray);text-align:center;">PR gemerged</div>
<div style="font-size:0.78rem;color:var(--np-mid-gray);text-align:center;">PR geopend</div>
<div style="font-size:0.78rem;color:var(--np-mid-gray);text-align:center;">issues gesloten</div>
<div style="font-size:0.78rem;color:var(--np-mid-gray);text-align:center;">issues geopend</div>
<div style="font-size:0.78rem;color:var(--np-mid-gray);text-align:center;">commits op dev</div>
<div style="font-size:0.84rem;font-weight:600;color:var(--np-ink);">Public</div>
<div class="np-getal">0</div><div class="np-getal">0</div><div class="np-getal">0</div><div class="np-getal">4</div><div class="np-getal">0</div>
<div style="font-size:0.84rem;font-weight:600;color:var(--np-ink);">meta</div>
<div class="np-getal">4</div><div class="np-getal">5</div><div class="np-getal">0</div><div class="np-getal">17</div><div class="np-getal">34</div>
</div>

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem; font-size: 0.86rem; line-height: 1.55; max-width: 92%;">
<div>

**Public:** vier nieuwe issues: het koppeling-ID ([#107](https://github.com/Npuls-OKx/Public/issues/107)) en de voorbeelduitwerking ([#106](https://github.com/Npuls-OKx/Public/issues/106), [#108](https://github.com/Npuls-OKx/Public/issues/108), [#109](https://github.com/Npuls-OKx/Public/issues/109))

</div>
<div>

**meta:** de voorbeelduitwerking ([PR 252](https://github.com/Npuls-OKx/meta/pull/252)), FHIR als spiegel ([PR 254](https://github.com/Npuls-OKx/meta/pull/254)) en de update voor de werkgroep OKx ([PR 256](https://github.com/Npuls-OKx/meta/pull/256))

</div>
</div>

<div style="font-size: 0.8rem; color: var(--np-mid-gray); margin-top: 0.8rem;">
Stand van 25 september. Nul gesloten issues: het werk zit in de branches, en de milestone van de voorbeelduitwerking sluit met de acceptatietest van vandaag.
</div>

<style scoped>
.np-getal { background:#fff; border:1px solid var(--np-light-gray); border-radius:8px; padding:0.5rem 0; text-align:center; font-size:1.8rem; font-weight:600; color:var(--np-ink); line-height:1.1; }
</style>

</div>

<!--
Aantallen zeggen iets over de hoeveelheid werk, niet over de kwaliteit; dat oordeel ligt bij de
review. De nul bij gesloten issues staat er bewust: sinds 15 september is in beide repositories
geen issue gesloten, omdat het werk op branches staat en de issues van de voorbeelduitwerking pas
sluiten na de acceptatietest van vandaag (Public #109).
-->

---

<!-- 5. WERK PER ONDERWERP -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Werk per onderwerp

<div style="margin-top:0.6rem;max-width:80%;">
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/meta/milestone/14" style="color:var(--np-ink);">Voorbeelduitwerking Jochem</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">meta</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:50%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:12;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">12</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/meta/pull/252">PR 252</a></span></div></div>
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/Public/milestone/9" style="color:var(--np-ink);">Voorbeelduitwerking Jochem</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:13%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:3;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">3</div></div></div></div>
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/Public/milestone/5" style="color:var(--np-ink);">Koppelingspecificatiestructuur doorontwikkelen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:55%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:1;background:#00AF81;display:flex;align-items:center;justify-content:center;color:#fff;font-size:0.72rem;font-weight:600;">1</div><div style="flex:12;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">12</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/Public/pull/100">PR 100</a></span></div></div>
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/Public/milestone/3" style="color:var(--np-ink);">Requirementsboom doorontwikkelen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:46%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:2;background:#00AF81;display:flex;align-items:center;justify-content:center;color:#fff;font-size:0.72rem;font-weight:600;">2</div><div style="flex:9;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">9</div></div></div></div>
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/meta/milestone/7" style="color:var(--np-ink);">Begrippenkader en informatiemodel verdiepen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">meta</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:76%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:18;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">18</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/Public/pull/104">PR 104</a></span></div></div>
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/Public/milestone/4" style="color:var(--np-ink);">Koppelvlakspecificatie releaseproces en kwaliteit</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:46%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:11;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">11</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/Public/pull/82">PR 82</a></span></div></div>
<div style="display:grid;grid-template-columns:20rem 1fr;align-items:center;gap:0.8rem;margin-top:0.45rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/Public/milestone/7" style="color:var(--np-ink);">Keuzedelen kiesbaarheid en groepsindeling</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:13%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:3;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">3</div></div></div></div>
</div>

<div style="font-size: 0.8rem; color: var(--np-dark-gray); margin-top: 0.7rem;">
Stand van 25 september. Onderwerpen zijn de milestones; de balklengte is het aantal issues, groen gesloten, grijs open; het icoon markeert werk dat als pull request ter review ligt. Oranje: staat vandaag op de agenda.
</div>

</div>

<!--
Een balk per milestone, groen wat gesloten is, grijs wat open staat. Oranje stip: staat vandaag
op de agenda. Bron: de milestones van beide repositories, GitHub, 25 september.
-->

---

<!-- 5b. CONCLUSIE PO-DEEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Veel verzet, weinig afgerond

<div class="np-pipeline" style="margin-top: 1.4rem;">
  <div class="np-step blue"><carbon-branch class="np-pic" /><div class="np-getal">34</div><div>commits</div><small>op branches</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue"><carbon-pull-request class="np-pic" /><div class="np-getal">6</div><div>pull requests</div><small>vijf op draft</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange"><carbon-merge class="np-pic oranje" /><div class="np-getal oranje">0</div><div>gemerged</div><small>sinds 4 september</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange"><carbon-task-complete class="np-pic oranje" /><div class="np-getal oranje">0</div><div>gesloten</div><small>sinds 15 september</small></div>
</div>

<div class="np-card accent-green" style="margin-top: 1.3rem; padding: 0.7rem 1rem;">
<carbon-play style="font-size: 1.3rem; color: var(--np-green); vertical-align: -0.2rem;" /> <strong style="color: var(--np-ink);">Vandaag een pull request uit draft, en de eerste milestone sluiten</strong>
</div>

<style scoped>
.np-pic { font-size: 1.5rem; color: var(--np-blue); margin: 0 auto; }
.np-pic.oranje { color: var(--np-orange); }
.np-getal { font-size: 2.1rem; line-height: 1.05; color: var(--np-dark-blue); }
.np-getal.oranje { color: var(--np-orange); }
.np-step { min-width: 8.2rem; }
</style>

</div>

<!--
Eerlijke conclusie van het voortgangsdeel, in vier getallen. Bron: GitHub, 25 september. Op
Public dev landde sinds 4 september niets en van de zes open pull requests staan er vijf op
draft, dus formeel vraagt bijna niets om review. Dat draft-besluit is van 15 september en houdt
de ruis weg, met als keerzijde dat er ook niets sluit. De hoeveelheid werk is niet het probleem:
het gaat om stukken die klein genoeg zijn om te landen. Voorstel: per milestone vooraf afspreken
wanneer iets af is, elke cyclus iets kleins naar dev brengen, en vandaag kiezen welke pull
request uit draft gaat. De milestone van de voorbeelduitwerking kan vandaag sluiten met de
acceptatietest, Public #109.
-->

---

<!-- 6b. DOORLOOPTIJD EN CAPACITEIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe lang dit duurt

<style scoped>
.mermaid { display: flex; justify-content: center; margin: 0.2rem 0 0; }
.mermaid svg { max-width: 100%; height: auto; }
.np-strip { display: flex; justify-content: center; gap: 0.5rem; margin-top: 0.7rem; flex-wrap: wrap; }
.np-pil { display: flex; align-items: center; gap: 0.35rem; background: #fff; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.3rem 0.85rem; font-size: 0.8rem; color: var(--np-dark-blue); }
</style>

<div style="margin-top: 0.3rem;">

```mermaid {theme: 'base', scale: 0.92, themeVariables: {'fontFamily': 'General Sans, Inter, sans-serif', 'fontSize': '14px', 'sectionBkgColor': '#F7F8FB', 'altSectionBkgColor': '#FFFFFF', 'gridColor': '#E5E7EB', 'doneTaskBkgColor': '#D8ECDD', 'doneTaskBorderColor': '#00AF81', 'activeTaskBkgColor': '#FBE3D6', 'activeTaskBorderColor': '#DD784B', 'taskBkgColor': '#E8EDFC', 'taskBorderColor': '#3D68EC', 'taskTextColor': '#1B2A6B', 'taskTextDarkColor': '#1B2A6B', 'taskTextOutsideColor': '#374151', 'todayLineColor': '#DD784B'}}
gantt
    dateFormat YYYY-MM-DD
    axisFormat %b
    todayMarker off
    section Gereed
    Koppelvlakspecificatie v0.0.1      :done, 2026-07-30, 2026-08-18
    Informatiemodel en begrippen v0.1  :done, 2026-08-18, 2026-09-18
    Voorbeelduitwerking leerroute 1    :done, 2026-09-17, 2026-09-30
    section Loopt
    OC-P&R afronden, v0.0.2            :active, 2026-08-31, 2026-10-31
    section Doorgetrokken
    OC-KRS en OC-SVS                   :2026-10-15, 2027-01-15
    OC-LMS                             :2026-12-01, 2027-03-15
    Alle lagen beschreven              :milestone, 2027-03-31, 0d
```

</div>

<div class="np-strip">
  <div class="np-pil"><carbon-user-multiple style="font-size: 1rem; color: var(--np-blue);" /> <strong>3</strong> schrijvers</div>
  <div class="np-pil"><carbon-time style="font-size: 1rem; color: var(--np-blue);" /> <strong>2 maanden</strong> per koppeling</div>
  <div class="np-pil"><carbon-hourglass style="font-size: 1rem; color: var(--np-orange);" /> <strong>3 weken</strong> zonder merge</div>
</div>

<div class="np-card accent-orange" style="margin-top: 0.8rem; padding: 0.6rem 1rem;">
<strong style="color: var(--np-ink);">Q1 2027 haalbaar bij twee koppelingen tegelijk en review binnen twee weken</strong>
</div>

</div>

<!--
Doorgetrokken lijn op basis van de voortgang, geen toezegging. De bovenste drie balken zijn
gerealiseerd en dateerbaar: de koppelvlakspecificatie kwam op 30 juli naar Public, v0.0.1 stond er
op 18 augustus, het informatiemodel en de begrippen op 18 september, en de voorbeelduitwerking
loopt van 17 tot 30 september. De eerste koppeling, OC-P&R, loopt sinds eind juli en is na twee
maanden nog niet vastgesteld: dat is de maat die onder de doorgetrokken balken ligt. Capaciteit,
uit de commit-historie sinds 1 juli: drie mensen schrijven, met het zwaartepunt bij een. De derde
pil is de rem: op Public dev landde sinds 4 september niets. Serieel doorgerekend komen vier
koppelingen uit op ongeveer acht maanden en dus op Q2 2027; Q1 2027 vraagt dat twee koppelingen
tegelijk lopen en dat een reviewronde binnen twee weken rond is. Dat is een keuze over capaciteit
en over hoe snel de kerngroep leest, geen kwestie van harder schrijven.
-->

---

<!-- 6. VOORBEELDUITWERKING: WAT HET IS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De opleiding van Jochem in het model

<div style="font-size: 0.92rem; color: var(--np-mid-gray); margin-top: 0.1rem;">Een hele opleiding uitgedrukt in het informatiemodel, van dossier tot diploma</div>

<div class="np-grid-4" style="margin-top: 1.2rem; gap: 0.9rem;">
  <div class="np-tegel"><carbon-map class="np-pic" /><div class="np-getal">8</div><div>fasen</div></div>
  <div class="np-tegel"><carbon-image class="np-pic" /><div class="np-getal">64</div><div>beelden</div></div>
  <div class="np-tegel"><carbon-list-checked class="np-pic" /><div class="np-getal">257</div><div>regels</div></div>
  <div class="np-tegel"><carbon-assembly-cluster class="np-pic" /><div class="np-getal">65</div><div>objecttypen</div></div>
</div>

<div class="np-card accent-orange" style="margin-top: 1.2rem; padding: 0.7rem 1rem;">
<carbon-chat style="font-size: 1.3rem; color: var(--np-orange); vertical-align: -0.2rem;" /> <strong style="color: var(--np-ink);">Gevraagd: feedback per beeld, geen commitment</strong>
</div>

<style scoped>
.np-tegel { background: #fff; border: 1px solid var(--np-light-gray); border-top: 4px solid var(--np-blue); border-radius: 12px; padding: 0.8rem 0.6rem; text-align: center; font-weight: 600; color: var(--np-dark-blue); font-size: 0.86rem; }
.np-pic { font-size: 1.5rem; color: var(--np-blue); display: block; margin: 0 auto 0.2rem; }
.np-getal { font-size: 2.1rem; line-height: 1.05; color: var(--np-dark-blue); }
</style>

</div>

<!--
Dit blok beantwoordt de vraag van Kees van 15 september, met instemming van Huib Jan: een
opleiding helemaal uitdrukken in het informatiemodel. Het is een leeshulp op conceptueel niveau
(MIM 1 en 2), zonder payloads, endpoints of diensten: per stap wat ontstaat, wat verandert en wat
tussen welke systemen stroomt, met Jochems eigen waarden erin. Vandaag loopt fase 1 er helemaal
doorheen, beeld voor beeld. De vraag per beeld: klopt dit met het eigen model, en hoe heet het
daar. Bron: voorbeeld-leerroute-1-jochem.md op branch 106, meta PR 252.
-->

---

<!-- 7. VOORBEELDUITWERKING: HOE EEN BEELD LEEST -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe een beeld leest

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.2rem; align-items: center;">

<div>
  <img src="/platen/voorbeeld-f2-07-aanbod-naar-catalogus.png" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
</div>

<div>
  <div class="np-card accent-blue" style="padding: 0.7rem 0.9rem; margin-bottom: 0.6rem;">
    <div style="font-weight: 700; font-size: 0.95rem;">Blauwe rand: een stroom</div>
    <small style="font-size: 0.84rem;">van planningssysteem naar onderwijscatalogus, koppeling OC-P&amp;R</small>
  </div>
  <div class="np-card accent-green" style="padding: 0.7rem 0.9rem; margin-bottom: 0.6rem;">
    <div style="font-weight: 700; font-size: 0.95rem;">Geel: rol, stap en object</div>
    <small style="font-size: 0.84rem;">de vormtaal van de informatiemodelplaat, met Jochems waarde erin</small>
  </div>
  <div class="np-card accent-orange" style="padding: 0.7rem 0.9rem;">
    <div style="font-weight: 700; font-size: 0.95rem;">Elk beeld heeft een ID</div>
    <small style="font-size: 0.84rem;">F2-07 is het zevende beeld van fase 2; de bijlage en het register noemen hetzelfde ID</small>
  </div>
</div>

</div>

<div style="margin-top: 0.7rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
Status: concept in afstemming
</div>

</div>

<!--
Een voorbeeld van hoe een regel eruitziet, zodat de bijlage zichzelf uitlegt. F2-07 volgt op de
planning: het geplande aanbod gaat terug naar de catalogus. Het beeld staat in de vormtaal van de
informatiemodelplaat, zodat wie de plaat kent het beeld direct leest.
-->

---

<!-- FASE 1: DE KAART -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">Fase 1 &middot; kwalificatiekader analyseren en grofmazig ontwerpen</div>

# Twaalf beelden, een fase

<img src="/regels/fase1-hoofdplaat.svg" class="np-beeld" />

<div class="np-onder">De stromen die deze fase raakt, op de hoofdplaat; een gestippelde lijn kent de plaat nog niet</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 360px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
h1 { font-size: 1.9rem !important; margin-top: 0.1rem; }
</style>

</div>

<!--
Deze plaat opent het blok: fase 1 loopt van het kwalificatiedossier tot het gepubliceerde
ontwerp, en raakt een stroom die de hoofdplaat nog niet kent. Daarna twaalf beelden, een voor een.
-->

---

<!-- FASE 1: F1-01 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-01 &middot; ontstaat &middot; Het kwalificatiedossier ontleed</div>

<img src="/regels/f1-01-het-kwalificatiedossier-ontleed.svg" class="np-beeld" />

<div class="np-onder">Stap: Kwalificatiedossier analyseren</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 420px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-01. Het kwalificatiedossier ontleed. Vraag bij elk beeld: klopt dit met het eigen model, en hoe heet het daar.
-->

---

<!-- FASE 1: F1-02 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-02 &middot; ontstaat &middot; Examenplan, eerste resultaatstructuur en cohort</div>

<img src="/regels/f1-02-examenplan-eerste-resultaatstructuur-en-cohort.svg" class="np-beeld" />

<div class="np-onder">Stap: Examenplan vaststellen</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 420px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-02. Examenplan, eerste resultaatstructuur en cohort. Vraag bij elk beeld: klopt dit met het eigen model, en hoe heet het daar.
-->

---

<!-- FASE 1: F1-03 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-03 &middot; ontstaat &middot; Leeruitkomsten uit het dossier, in de stem van de instelling</div>

<img src="/regels/f1-03-leeruitkomsten-uit-het-dossier-in-de-stem-van-de-instelling.svg" class="np-beeld" />

<div class="np-onder">Stap: Kwalificatiedossier vertalen naar leeruitkomsten</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 420px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-03. Leeruitkomsten uit het dossier, in de stem van de instelling. Vraag bij elk beeld: klopt dit met het eigen model, en hoe heet het daar.
-->

---

<!-- FASE 1: F1-04 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-04 &middot; ontstaat &middot; De leeruitkomst in CompetentNL-skills</div>

<img src="/regels/f1-04-de-leeruitkomst-in-competentnl-skills.svg" class="np-beeld" />

<div class="np-onder">Stap: Kwalificatiedossier vertalen naar leeruitkomsten &middot; verdieping: leeruitkomst naar skills</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 420px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-04. De leeruitkomst in CompetentNL-skills. Vraag bij elk beeld: klopt dit met het eigen model, en hoe heet het daar.
-->

---

<!-- FASE 1: F1-05 deel 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-05 &middot; deel 1 van 2 &middot; De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten</div>

<img src="/regels/f1-05-de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten-deel1.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-05, deel 1 van 2. De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-05 deel 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-05 &middot; deel 2 van 2 &middot; De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten</div>

<img src="/regels/f1-05-de-eenheidspecificatie-met-haar-leeronderdelen-en-de-gelinkte-leeruitkomsten-deel2.svg" class="np-beeld" />

<div class="np-onder">Stap: Kwalificatiedossier vertalen naar leeruitkomsten &middot; verdieping: van kerntaak naar eenheid en leeronderdelen</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-05, deel 2 van 2. De eenheidspecificatie met haar leeronderdelen en de gelinkte leeruitkomsten. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-06 deel 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-06 &middot; deel 1 van 3 &middot; De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen</div>

<img src="/regels/f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen-deel1.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-06, deel 1 van 3. De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-06 deel 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-06 &middot; deel 2 van 3 &middot; De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen</div>

<img src="/regels/f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen-deel2.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-06, deel 2 van 3. De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-06 deel 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-06 &middot; deel 3 van 3 &middot; De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen</div>

<img src="/regels/f1-06-de-eenheidspecificatie-met-haar-onderwijsontwerp-vorm-ruimte-mensen-en-middelen-deel3.svg" class="np-beeld" />

<div class="np-onder">Stap: Kwalificatiedossier vertalen naar leeruitkomsten &middot; verdieping: onderwijsontwerp met ruimte en middelen</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-06, deel 3 van 3. De eenheidspecificatie met haar onderwijsontwerp: vorm, ruimte, mensen en middelen. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-07 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-07 &middot; ontstaat &middot; De opleidingsspecificatie met programma, eenheden en keuzedeelruimte</div>

<img src="/regels/f1-07-de-opleidingsspecificatie-met-programma-eenheden-en-keuzedeelruimte.svg" class="np-beeld" />

<div class="np-onder">Stap: Opleidingsspecificatie met programma en eenheden beschrijven</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 420px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-07. De opleidingsspecificatie met programma, eenheden en keuzedeelruimte. Vraag bij elk beeld: klopt dit met het eigen model, en hoe heet het daar.
-->

---

<!-- FASE 1: F1-08 deel 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-08 &middot; deel 1 van 3 &middot; Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen</div>

<img src="/regels/f1-08-het-keuzedeel-als-eigen-programmaspecificatie-met-kerntaken-en-werkprocessen-deel1.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-08, deel 1 van 3. Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-08 deel 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-08 &middot; deel 2 van 3 &middot; Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen</div>

<img src="/regels/f1-08-het-keuzedeel-als-eigen-programmaspecificatie-met-kerntaken-en-werkprocessen-deel2.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-08, deel 2 van 3. Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-08 deel 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-08 &middot; deel 3 van 3 &middot; Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen</div>

<img src="/regels/f1-08-het-keuzedeel-als-eigen-programmaspecificatie-met-kerntaken-en-werkprocessen-deel3.svg" class="np-beeld" />

<div class="np-onder">Stap: Keuzedeelprogramma als eigen specificatie vormgeven</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-08, deel 3 van 3. Het keuzedeel als eigen programmaspecificatie, met kerntaken en werkprocessen. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-09 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-09 &middot; ontstaat &middot; Toetsonderdelen, wegingen en afrondingscriterium</div>

<img src="/regels/f1-09-toetsonderdelen-wegingen-en-afrondingscriterium.svg" class="np-beeld" />

<div class="np-onder">Stap: Toetsonderdelen en resultaatstructuur uit het examenplan afleiden</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 420px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-09. Toetsonderdelen, wegingen en afrondingscriterium. Vraag bij elk beeld: klopt dit met het eigen model, en hoe heet het daar.
-->

---

<!-- FASE 1: F1-10 deel 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-10 &middot; deel 1 van 2 &middot; De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte</div>

<img src="/regels/f1-10-de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte-deel1.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-10, deel 1 van 2. De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-10 deel 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-10 &middot; deel 2 van 2 &middot; De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte</div>

<img src="/regels/f1-10-de-examenonderdeelspecificatie-met-haar-toetsvorm-instrumenten-materiaal-en-ruimte-deel2.svg" class="np-beeld" />

<div class="np-onder">Stap: Exameninstrumenten bepalen, inkopen of construeren &middot; verdieping: examenvorm, instrument en beoordelaar</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-10, deel 2 van 2. De examenonderdeelspecificatie met haar toetsvorm, instrumenten, materiaal en ruimte. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-11 deel 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-11 &middot; deel 1 van 3 &middot; De opleiding zoals ontworpen naar de catalogus</div>

<img src="/regels/f1-11-de-opleiding-zoals-ontworpen-naar-de-catalogus-deel1.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-11, deel 1 van 3. De opleiding zoals ontworpen naar de catalogus. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-11 deel 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-11 &middot; deel 2 van 3 &middot; De opleiding zoals ontworpen naar de catalogus</div>

<img src="/regels/f1-11-de-opleiding-zoals-ontworpen-naar-de-catalogus-deel2.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-11, deel 2 van 3. De opleiding zoals ontworpen naar de catalogus. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-11 deel 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-11 &middot; deel 3 van 3 &middot; De opleiding zoals ontworpen naar de catalogus</div>

<img src="/regels/f1-11-de-opleiding-zoals-ontworpen-naar-de-catalogus-deel3.svg" class="np-beeld" />

<div class="np-onder">Stroom: Curriculum ontwerptool naar Onderwijscatalogus, geen pijl op de hoofdplaat</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-11, deel 3 van 3. De opleiding zoals ontworpen naar de catalogus. Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-12 deel 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-12 &middot; deel 1 van 2 &middot; Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)</div>

<img src="/regels/f1-12-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat-deel1.svg" class="np-beeld" />

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-12, deel 1 van 2. Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat). Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- FASE 1: F1-12 deel 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

<div class="np-eyebrow">F1-12 &middot; deel 2 van 2 &middot; Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat)</div>

<img src="/regels/f1-12-het-onderwijs-en-examenontwerp-mee-naar-de-catalogus-conceptplaat-deel2.svg" class="np-beeld" />

<div class="np-onder">Stroom: Curriculum ontwerptool naar Onderwijscatalogus, geen pijl op de hoofdplaat</div>

<style scoped>
.np-eyebrow { font-size: 0.75rem; color: var(--np-orange); letter-spacing: 1px; text-transform: uppercase; }
.np-beeld { display: block; margin: 0.5rem auto 0; max-width: 100%; max-height: 430px; object-fit: contain; }
.np-onder { margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center; }
</style>

</div>

<!--
F1-12, deel 2 van 2. Het onderwijs- en examenontwerp mee naar de catalogus (conceptplaat). Het beeld staat in delen op de slides en in een geheel in het document.
-->

---

<!-- 8. VOORBEELDUITWERKING: WAT DE STROMEN LATEN ZIEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de stromen laten zien

<div class="np-grid-2" style="margin-top: 0.5rem; gap: 1.2rem; align-items: center;">

<div>
  <img src="/platen/koppelingen-hoofdplaat.svg" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Hoofdplaat v1.7, met de drie koppelingen gemarkeerd</div>
</div>

<div style="font-size: 0.9rem; line-height: 1.6;">

| Twintig stromen in leerroute 1 | |
|---|---|
| Gedekt door OC-P&amp;R, OC-KRS, OC-SVS, OC-LMS | 5 |
| Pijl op de hoofdplaat, nog zonder specificatie | 8 |
| Stroom zonder pijl op de hoofdplaat | 7 |

<div style="margin-top: 0.7rem; font-size: 0.86rem; color: var(--np-dark-gray);">
De koppelingen van dit jaar dragen de kern van de reis. De rest is zichtbaar gemaakt, met de plek waar die vraag hoort.
</div>

</div>

</div>

</div>

<!--
Dit is de opbrengst die de kerngroep het meest raakt: de voorbeelduitwerking maakt zichtbaar
welke stromen al een koppelingspecificatie hebben en welke nog niet. Acht pijlen op de hoofdplaat
hebben nog geen specificatie; zeven stromen uit het kaderscenario staan nog niet op de hoofdplaat.
Dat laatste is een vraag aan het model, geen fout in het scenario. Bron: de tabel "De hoofdplaat
als kaart" in voorbeeld-leerroute-1-jochem.md.
-->

---

<!-- 9. BLOK GARIK: VERSIONERING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Versionering met een voorbeeldflow

<div class="np-card accent-blue" style="margin-top: 0.9rem; padding: 1rem 1.2rem;">
<strong>Blok van Garik</strong>
<div style="margin-top:0.5rem;font-size:0.95rem;line-height:1.6;">
Afgesproken op 15 september: een iteratie op de versionering met een voorbeeldflow, en een sessie vooraf om die samen door te nemen. Deze plek in het deck is voor die sheets.
</div>
</div>

<div style="margin-top: 1rem; font-size: 0.9rem; line-height: 1.6; color: var(--np-dark-gray);">
Vertrekpunt: <a href="https://github.com/Npuls-OKx/Public/pull/100">Public PR 100</a>, applicatiediensten als laag tussen component en endpoint, en de datamodellen als eigen pakket. Staat op draft tot de iteratie er is.
</div>

</div>

<!--
Plaatshouder. Garik levert de sheets aan; dit blok blijft herkenbaar afgebakend zodat hij het kan
vervangen zonder de rest te raken. De vraag uit de vorige sessie die hier terugkomt: hoe ver reikt
een versieophoging van een datamodel door de keten van endpoints en diensten.
-->

---

<!-- 10. BLOK NIELS: BUSINESS-ARCHITECTUUR -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Business-architectuur en de stories

<div class="np-card accent-orange" style="margin-top: 0.9rem; padding: 1rem 1.2rem;">
<strong>Blok van Niels</strong>
<div style="margin-top:0.5rem;font-size:0.95rem;line-height:1.6;">
Afgesproken op 15 september: de business-architectuur doorontwikkelen langs de lijn van story naar koppelvlakfunctionaliteit, en de stories opnieuw ophalen bij de PoC-scholen. Deze plek in het deck is voor die sheets.
</div>
</div>

<div style="margin-top: 1rem; font-size: 0.9rem; line-height: 1.6; color: var(--np-dark-gray);">
Vertrekpunt: de milestone <a href="https://github.com/Npuls-OKx/Public/milestone/3">requirementsboom doorontwikkelen</a>, negen open issues, en <a href="https://github.com/Npuls-OKx/Public/pull/82">Public PR 82</a> die op draft staat zolang de boom beweegt.
</div>

</div>

<!--
Plaatshouder. Niels levert de sheets aan. De koppeling met blok 2: de stories uit de PoC-scholen
en de voorbeelduitwerking gaan over hetzelfde onderwijs, van twee kanten bekeken.
-->

---

<!-- 11. KOPPELING-ID -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een korte naam per koppeling

<div style="font-size: 0.92rem; color: var(--np-mid-gray); margin-top: 0.1rem;">De ID noemt twee applicatiecomponenten, in beide richtingen dezelfde specificatie</div>

<div class="np-grid-4" style="margin-top: 1.1rem; gap: 0.9rem;">
  <div class="np-tegel"><carbon-calendar class="np-pic" /><div class="np-id">OC-P&amp;R</div><div>planning en rooster</div></div>
  <div class="np-tegel"><carbon-data-base class="np-pic" /><div class="np-id">OC-KRS</div><div>kernregistratie</div></div>
  <div class="np-tegel"><carbon-chart-line class="np-pic" /><div class="np-id">OC-SVS</div><div>studentvolgsysteem</div></div>
  <div class="np-tegel"><carbon-education class="np-pic" /><div class="np-id">OC-LMS</div><div>leeromgeving</div></div>
</div>

<div class="np-card accent-orange" style="margin-top: 1.1rem; padding: 0.7rem 1rem;">
<carbon-idea style="font-size: 1.3rem; color: var(--np-orange); vertical-align: -0.2rem;" /> <strong style="color: var(--np-ink);">SIS en P&amp;R groeperen voor de leesbaarheid; de specificatie volgt de component</strong>
</div>

<div style="margin-top: 0.7rem; font-size: 0.82rem; color: var(--np-mid-gray);">
Voorstel, uitgewerkt in <a href="https://github.com/Npuls-OKx/Public/issues/107">Public #107</a>; de voorbeelduitwerking gebruikt deze ID's al.
</div>

<style scoped>
.np-tegel { background: #fff; border: 1px solid var(--np-light-gray); border-top: 4px solid var(--np-blue); border-radius: 12px; padding: 0.7rem 0.5rem; text-align: center; font-weight: 500; color: var(--np-mid-gray); font-size: 0.8rem; }
.np-pic { font-size: 1.4rem; color: var(--np-blue); display: block; margin: 0 auto 0.2rem; }
.np-id { font-size: 1.35rem; font-weight: 700; color: var(--np-dark-blue); line-height: 1.2; }
</style>

</div>

<!--
Voorstel, geen besluit. De vraag van Kees op 15 september was een korte naam per koppeling. De
regel in het voorstel: een ID noemt de twee applicatiecomponenten die de koppeling verbindt, en
beide richtingen staan in een specificatie als aparte berichtstromen. Daarom OC-KRS en OC-SVS in
plaats van een ID op SIS-niveau: SIS is de praktijknaam voor de verzameling koppelvlakken naar
kernregistratie en studentvolgsysteem, en dat is een leesbaarheidsgroepering, geen component.
Dezelfde toets ligt bij OC-P&R: planning en roostering zijn twee componenten, dus die naam is nog
een open punt in #107. Op de hoofdplaat hoort per lijn te staan welke ID erover loopt; dat is een
modelronde na 30 september.
-->

---

<!-- 12. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.9rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="19" cy="19" r="8" fill="none" stroke="#fff" stroke-width="3"/><line x1="25" y1="25" x2="33" y2="33" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><dl class="np-besluit review" style="flex:1;"><dt>Feedback</dt><dd>de voorbeelduitwerking naast het eigen model: wat heet anders, wat hangt anders, wat ontbreekt</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="19" cy="19" r="8" fill="none" stroke="#fff" stroke-width="3"/><line x1="25" y1="25" x2="33" y2="33" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><dl class="np-besluit review" style="flex:1;"><dt>Review</dt><dd><a href="https://github.com/Npuls-OKx/Public/pull/104">Public PR 104</a>: het informatiemodel en de begrippen, opmerkingen in de pull request</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><dl class="np-besluit" style="flex:1;"><dt>Besluit</dt><dd>het koppeling-ID per applicatiecomponent, met beide richtingen in een specificatie</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><path d="M11 13 h22 a3 3 0 0 1 3 3 v11 a3 3 0 0 1 -3 3 h-12 l-6 5 v-5 h-4 a3 3 0 0 1 -3 -3 v-11 a3 3 0 0 1 3 -3 z" fill="#fff"/></svg><dl class="np-besluit kennisname" style="flex:1;"><dt>Input</dt><dd>de acht pijlen zonder specificatie: welke daarvan komt als eerste aan de beurt</dd></dl></div>

</div>

<!--
Vier punten. De feedback op de voorbeelduitwerking is de kern van vandaag: per beeld-ID, tijdens
de doorloop van fase 1 of daarna als issue. De review op PR 104 staat er opnieuw, want die stond ook op 15 september. Het besluit
over het koppeling-ID kan vandaag vallen; de laatste vraag zet de agenda voor de volgende periode.
-->

---

<!-- 13. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div style="margin-top: 0.8rem;">
<div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="36" height="36" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7CCBA8"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Reacties per beeld-ID: als issue op Public, of in de pull request</div></div>
<div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="36" height="36" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="19" cy="19" r="8" fill="none" stroke="#fff" stroke-width="3"/><line x1="25" y1="25" x2="33" y2="33" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><div>Opmerkingen op <a href="https://github.com/Npuls-OKx/Public/pull/104">Public PR 104</a>, in de pull request</div></div>
<div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="36" height="36" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><rect x="11" y="14" width="22" height="19" rx="2" fill="#fff"/><rect x="15" y="10" width="3" height="6" rx="1" fill="#fff"/><rect x="26" y="10" width="3" height="6" rx="1" fill="#fff"/></svg><div>Volgende sessie: in overleg met Ruud, na de werkgroep OKx</div></div>
</div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 1rem;">
Commentaar op een lopende release: in de pull request. Nieuw punt: als issue op <strong>github.com/Npuls-OKx/Public</strong>
</div>

</div>

<!--
Geen datum beloven die nog niet vaststaat: de volgende sessie gaat in overleg met Ruud, die na
30 september weer aansluit. De voortgangsupdate voor de werkgroep OKx van 29 september komt hier
kort terug, zodat de groep weet wat er over dit werk aan de business is verteld.
-->

---

<!-- 14. PEILING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe gaat het?

<div class="np-grid-2" style="margin-top: 1.2rem; gap: 1.8rem; align-items: center;">
<div>
<div style="display:flex;align-items:center;gap:0.8rem;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><path d="M12 27 a10 10 0 0 1 20 0" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><line x1="22" y1="27" x2="27" y2="19" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="22" cy="27" r="2.5" fill="#fff"/></svg><div>Welk cijfer krijgt de voortgang, en waarom?</div></div>
<div style="display:flex;align-items:center;gap:0.8rem;margin-top:1rem;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7CCBA8"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Wat ging er goed?</div></div>
<div style="display:flex;align-items:center;gap:0.8rem;margin-top:1rem;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><line x1="22" y1="32" x2="22" y2="13" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><polyline points="14,21 22,13 30,21" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Wat kan er beter?</div></div>
</div>
<div>
  <div style="display: flex; gap: 0.32rem; justify-content: center;">
    <div class="np-cijfer" style="background: #f3d9d4; color: #8a4038;">1</div>
    <div class="np-cijfer" style="background: #f6e0d2; color: #8a5638;">2</div>
    <div class="np-cijfer" style="background: #f8e8d1; color: #8a6a38;">3</div>
    <div class="np-cijfer" style="background: #f9f0d2; color: #7f7538;">4</div>
    <div class="np-cijfer" style="background: #f2f2d6; color: #6f7538;">5</div>
    <div class="np-cijfer" style="background: #e6f0da; color: #547038;">6</div>
    <div class="np-cijfer" style="background: #d8ecdd; color: #3d6b49;">7</div>
    <div class="np-cijfer" style="background: #cde7e4; color: #356663;">8</div>
    <div class="np-cijfer" style="background: #c2e0e9; color: #2d5c6b;">9</div>
    <div class="np-cijfer" style="background: #b7d8ef; color: #27506e;">10</div>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 0.5rem; font-size: 0.8rem; color: var(--np-mid-gray);">
    <span>loopt niet</span><span>loopt goed</span>
  </div>
</div>
</div>

<style scoped>
.np-cijfer { width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; }
</style>

</div>

<!--
Vaste afsluiting van elke sessie, zie meta #205. Het cijfer maakt de lijn over sessies zichtbaar,
de twee open vragen leveren de inhoud.
-->

---

<!-- AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
