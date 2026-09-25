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

<!-- 6. VOORBEELDUITWERKING: WAT HET IS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De opleiding van Jochem in het informatiemodel

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.2rem; color: var(--np-dark-gray);">
De vraag van 15 september: druk een opleiding helemaal uit in het informatiemodel, zodat zichtbaar wordt of iedereen hetzelfde bedoelt.
</div>

<div class="np-grid-3" style="margin-top: 1rem; gap: 1.1rem; align-items: start;">
<div class="np-card accent-blue">
<strong>Wat er ligt</strong>
<div style="margin-top:0.4rem;font-size:0.88rem;line-height:1.5;">257 regels over acht fasen, in 64 beelden; 65 objecttypen in acht begrippenfamilies</div>
</div>
<div class="np-card accent-green">
<strong>Hoe het leest</strong>
<div style="margin-top:0.4rem;font-size:0.88rem;line-height:1.5;">Per stap: wat ontstaat, wat verandert, en wat tussen welke systemen stroomt</div>
</div>
<div class="np-card accent-orange">
<strong>Wat gevraagd wordt</strong>
<div style="margin-top:0.4rem;font-size:0.88rem;line-height:1.5;">Feedback, geen commitment: per objecttype de eigen naam en de eigen plek in het model, op het invulblad</div>
</div>
</div>

<div style="margin-top: 1rem; font-size: 0.88rem; color: var(--np-dark-gray);">
Conceptueel niveau (MIM 1 en 2). De bijlage van zes pagina's en het invulblad liggen op tafel.
</div>

</div>

<!--
Dit blok beantwoordt de vraag van Kees van 15 september, met instemming van Huib Jan: een
opleiding helemaal uitdrukken in het informatiemodel. Het is een leeshulp, geen besluit: de
regels tonen wat het model zegt, en de vraag is of dat klopt met het eigen model van de
leverancier. Bron: voorbeeld-leerroute-1-jochem.md op branch 106 (meta PR 252).
-->

---

<!-- 7. VOORBEELDUITWERKING: EEN REGEL VAN DICHTBIJ -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een regel van dichtbij

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
    <small style="font-size: 0.84rem;">F2-07 is het zevende beeld van fase 2; het invulblad noemt hetzelfde ID</small>
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
| Gedekt door OC-P&amp;R, OC-SIS en OC-LMS | 5 |
| Pijl op de hoofdplaat, nog zonder specificatie | 8 |
| Stroom zonder pijl op de hoofdplaat | 7 |

<div style="margin-top: 0.7rem; font-size: 0.86rem; color: var(--np-dark-gray);">
De drie koppelingen van dit jaar dragen de kern van de reis. De rest is zichtbaar gemaakt, met de plek waar die vraag hoort.
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

<style scoped>
table td:first-child { white-space: nowrap; }
</style>

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.2rem; color: var(--np-dark-gray);">
De vraag van Kees op 15 september: geef elke koppeling een naam die in een gesprek meteen duidelijk is.
</div>

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 1.3rem; align-items: start;">
<div>

| Voorstel | Koppeling |
|---|---|
| **OC-P&amp;R** | onderwijscatalogus en planning en roostering |
| **OC-SIS** | onderwijscatalogus en studentadministratie |
| **OC-LMS** | onderwijscatalogus en leeromgeving |

</div>
<div class="np-card accent-green">
<strong>Wat het voorstel regelt</strong>
<div style="margin-top:0.4rem;font-size:0.88rem;line-height:1.55;">
Een korte, stabiele ID naast de volledige naam; beide richtingen in een specificatie; dezelfde ID in berichtstromen, diensten en issues
</div>
</div>
</div>

<div style="margin-top: 0.9rem; font-size: 0.86rem; color: var(--np-dark-gray);">
De voorbeelduitwerking gebruikt deze ID's al, zodat direct zichtbaar is wat het oplevert. Uitwerking in <a href="https://github.com/Npuls-OKx/Public/issues/107">Public #107</a>.
</div>

</div>

<!--
Voorstel, geen besluit. De ID's komen uit de koppelingspecificaties die er al zijn; de
voorbeelduitwerking past ze toe op twintig stromen en laat zo meteen zien wat de conventie doet.
Open punt uit #107: de volgorde van de componenten in de ID, en de regel voor een koppeling met
meer dan twee componenten.
-->

---

<!-- 12. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.9rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="19" cy="19" r="8" fill="none" stroke="#fff" stroke-width="3"/><line x1="25" y1="25" x2="33" y2="33" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><dl class="np-besluit review" style="flex:1;"><dt>Feedback</dt><dd>de voorbeelduitwerking naast het eigen model: wat heet anders, wat hangt anders, wat ontbreekt</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="19" cy="19" r="8" fill="none" stroke="#fff" stroke-width="3"/><line x1="25" y1="25" x2="33" y2="33" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><dl class="np-besluit review" style="flex:1;"><dt>Review</dt><dd><a href="https://github.com/Npuls-OKx/Public/pull/104">Public PR 104</a>: het informatiemodel en de begrippen, opmerkingen in de pull request</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><dl class="np-besluit" style="flex:1;"><dt>Besluit</dt><dd>het koppeling-ID: OC-P&amp;R, OC-SIS en OC-LMS, met beide richtingen in een specificatie</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><path d="M11 13 h22 a3 3 0 0 1 3 3 v11 a3 3 0 0 1 -3 3 h-12 l-6 5 v-5 h-4 a3 3 0 0 1 -3 -3 v-11 a3 3 0 0 1 3 -3 z" fill="#fff"/></svg><dl class="np-besluit kennisname" style="flex:1;"><dt>Input</dt><dd>de acht pijlen zonder specificatie: welke daarvan komt als eerste aan de beurt</dd></dl></div>

</div>

<!--
Vier punten. De feedback op de voorbeelduitwerking is de kern van vandaag en gaat mee op het
invulblad. De review op PR 104 staat er opnieuw, want die stond ook op 15 september. Het besluit
over het koppeling-ID kan vandaag vallen; de laatste vraag zet de agenda voor de volgende periode.
-->

---

<!-- 13. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div style="margin-top: 0.8rem;">
<div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="36" height="36" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7CCBA8"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Invulblad terug: per objecttype de eigen naam en de eigen plek in het model</div></div>
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
