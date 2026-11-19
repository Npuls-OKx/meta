---
theme: default
title: "OKx-techniek: product breakdown en projectopzet"
info: "Voor de programma- en projectleiding: de product breakdown van OKx-techniek, de backlog als basis voor planning, de rollen en de capaciteit tot eind Q1 2027, en de opzet voor november 2026."
author: OKx - Onderwijskoppelingen (Npuls)
colorSchema: light
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
<h1 style="font-size: 2.9rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Product breakdown en projectopzet</h1>
<div style="font-size: 1.15rem; color: var(--np-ink); margin-bottom: 0.9rem; max-width: 720px;">Van leerroute tot een koppelvlakspecificatie per keten, en wat het project daarvoor nodig heeft</div>
<div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx-techniek &middot; programma- en projectleiding &middot; november 2026</div>
</div>

<!--
Vier onderwerpen: de product breakdown, de backlog als basis voor een consistente planning, de rollen en
de capaciteit, en de opzet voor november. Alle cijfers over capaciteit zijn schattingen.
-->

---

<!-- 2. DOEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Doel

<div class="np-grid-3" style="margin-top: 0.8rem; align-items: stretch;">
<div class="np-card accent-blue"><span class="np-num">1</span><h3 style="margin-top: 0.6rem;">Duidelijkheid over waar we nu staan</h3><p class="muted" style="font-size: 0.82rem; margin: 0;">Product breakdown, slide 3 en 4</p></div>
<div class="np-card accent-orange"><span class="np-num" style="background: var(--np-orange);">2</span><h3 style="margin-top: 0.6rem;">Een consistente projectplanning</h3><p class="muted" style="font-size: 0.82rem; margin: 0;">Backlog en schatting, slide 5 en 6</p></div>
<div class="np-card accent-green"><span class="np-num" style="background: var(--np-green);">3</span><h3 style="margin-top: 0.6rem;">Inzicht in wat het project nodig heeft</h3><p class="muted" style="font-size: 0.82rem; margin: 0;">Rollen, capaciteit en november, slide 7 tot en met 9</p></div>
</div>

</div>

<!--
Drie doelen. Eén: duidelijkheid over waar we nu staan, met de product breakdown als gedeeld beeld. Twee: komen tot een
consistente projectplanning, met de backlog langs de product breakdown als basis voor schatting en roadmap. Drie: inzicht
in wat het project nodig heeft aan rollen en capaciteit, en hoe we november inrichten.
-->

---

<!-- 3. PRODUCT BREAKDOWN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; gap: 1.2rem; align-items: center; padding: 0.7rem 1.4rem;">
<img src="/platen/product-breakdown.svg" style="height: 530px; width: auto; border: 1px solid #e2e8f0; border-radius: 8px; background: white;" />
<div style="flex: 1; display: flex; flex-direction: column; gap: 0.55rem; font-size: 0.86rem; align-self: flex-start; margin-top: 2.2rem;">
<p class="eyebrow" style="margin: 0 0 0.3rem;">1 &middot; Product breakdown</p>
<div style="display: flex; align-items: center; gap: 0.6rem;"><span style="width: 18px; height: 18px; flex: none; background: #F8EEDB; border: 2px solid #8A5A12; border-radius: 4px;"></span>Projectmanagement</div>
<div style="display: flex; align-items: center; gap: 0.6rem;"><span style="width: 18px; height: 18px; flex: none; background: #F3E6F2; border: 2px solid #874B83; border-radius: 4px;"></span>Domeinarchitectuur</div>
<div style="display: flex; align-items: center; gap: 0.6rem;"><span style="width: 18px; height: 18px; flex: none; background: #E2EBF5; border: 2px solid #2D5B8A; border-radius: 4px;"></span>Solutionarchitectuur</div>
<div style="display: flex; align-items: center; gap: 0.6rem;"><span style="width: 18px; height: 18px; flex: none; background: #E4F2E8; border: 2px solid #2C7548; border-radius: 4px;"></span>Eindproduct</div>
</div>
</div>

<!--
De volledige plaat zoals die in meta staat. Op slidegrootte is hij te klein om elk blok te lezen; hij laat vooral de
samenhang zien. De leerroute-uitwerking voedt de interactieketens, de ketens bepalen de interacties en componenten, en die
komen per keten samen in een koppelvlakspecificatie. De backlog ontstaat uit de kaderscenario's en de interactieketens; de
roadmap plant de backlog in de tijd.
-->

---

<!-- 4. OPBOUW -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van leerroute tot specificatie

<div class="np-pipeline" style="margin-top: 1rem; align-items: stretch;">
<div class="np-step" style="flex: 1; max-width: 250px; border-top: 4px solid #874B83;"><strong style="font-size: 0.95rem; color: #874B83;">Leerroute-uitwerking</strong><small>Per stap van de studentreis: welke informatie ontstaat, en in welk systeem</small></div>
<div class="np-arrow" style="align-self: center;">&#8594;</div>
<div class="np-step" style="flex: 1; max-width: 250px; border-top: 4px solid #2D5B8A;"><strong style="font-size: 0.95rem; color: #2D5B8A;">Interactieketens</strong><small>Onderwijsaanbod, student-instroom en bijsturen, uit leerroute 1</small></div>
<div class="np-arrow" style="align-self: center;">&#8594;</div>
<div class="np-step" style="flex: 1; max-width: 250px; border-top: 4px solid #2C7548;"><strong style="font-size: 0.95rem; color: #2C7548;">Specificatie per keten</strong><small>Eigen koppelvlakspecificatie met eigen versiebeheer, uit generieke bouwblokken: interacties, operaties, koppelvlakdiensten, JSON-schema's, applicatiecomponenten</small></div>
</div>

<div class="np-bottomline" style="margin-top: 1.4rem;">
<strong>Eén koppelvlakspecificatie per interactieketen</strong>, met een eigen versie en release.
</div>

</div>

<!--
De product breakdown is de ruggengraat van alles wat volgt: de backlog, de roadmap en de releases volgen dezelfde opbouw.
Een leerroute-uitwerking levert interactieketens op. Elke keten wordt een eigen koppelvlakspecificatie met eigen
versiebeheer, opgebouwd uit generieke bouwblokken die samen de keten beschrijven.
-->

---

<!-- 5. BACKLOG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Backlog langs de product breakdown

<div style="display: flex; flex-direction: column; gap: 0.45rem; margin-top: 0.6rem; font-size: 0.86rem;">
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: #874B83;">Leerroute</span><span style="font-weight: 700;">Leerroute 1</span></div>
<div style="display: flex; flex-direction: column; gap: 0.45rem; border-left: 3px solid #874B83; padding-left: 1rem;">
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: #2D5B8A;">Interactieketen</span><span style="font-weight: 700;">Onderwijsaanbod</span></div>
<div style="display: flex; flex-direction: column; gap: 0.45rem; border-left: 3px solid #2D5B8A; padding-left: 1rem;">
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: #2C7548;">Specificatie</span><span>Koppelvlakspecificatie onderwijsaanbod, v0.x.x</span></div>
<div style="display: flex; flex-direction: column; gap: 0.45rem; border-left: 3px solid #2C7548; padding-left: 1rem;">
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: #2D5B8A;">Bouwblok</span><span>Interacties, koppelvlakdiensten, operaties, JSON-schema's, applicatiecomponenten</span></div>
<div style="display: flex; flex-direction: column; gap: 0.45rem; border-left: 3px solid #2D5B8A; padding-left: 1rem;">
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: var(--np-orange);">Taak</span><span>Uitwerken, review en release, elk met een schatting</span></div>
</div>
</div>
</div>
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: #2D5B8A;">Interactieketen</span><span><b>Student-instroom</b>, zelfde opbouw</span></div>
<div style="display: flex; gap: 0.8rem;"><span style="width: 8.5rem; flex: none; font-weight: 700; color: #2D5B8A;">Interactieketen</span><span><b>Bijsturen</b>, zelfde opbouw</span></div>
</div>
</div>

</div>

<!--
De backlog volgt dezelfde opbouw als het product: per leerroute de interactieketens, per keten de koppelvlakspecificatie,
per specificatie de bouwblokken, en per bouwblok de vaste taken. Zo komt elke taak op één plek terecht en is per keten te
zien wat er nog moet. Garik geeft de backlog en de planning vorm en verfijnt ze met het team; Ruud is als productowner
eigenaar. Waar de backlog komt te staan, kiezen we in de eerste week.
-->

---

<!-- 6. VAN BACKLOG NAAR ROADMAP EN CAPACITEIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van backlog naar roadmap en capaciteit

<div class="np-pipeline" style="margin-top: 0.6rem; align-items: stretch;">
<div class="np-step blue" style="flex: 1; max-width: 190px;"><strong style="font-size: 0.9rem;">Backlog</strong><small>Alle taken per leerroute en interactieketen</small></div>
<div class="np-arrow" style="align-self: center;">&#8594;</div>
<div class="np-step orange" style="flex: 1; max-width: 190px;"><strong style="font-size: 0.9rem;">Schatting</strong><small>Werklast per taak, door het team dat het werk doet</small></div>
<div class="np-arrow" style="align-self: center;">&#8594;</div>
<div class="np-step green" style="flex: 1; max-width: 190px;"><strong style="font-size: 0.9rem;">Roadmap</strong><small>Wat wanneer af is, met een release per keten</small></div>
<div class="np-arrow" style="align-self: center;">&#8594;</div>
<div class="np-step blue" style="flex: 1; max-width: 190px;"><strong style="font-size: 0.9rem;">Capaciteit</strong><small>FTE per rol, en wat er ontbreekt</small></div>
</div>

<p style="font-size: 0.86rem; font-weight: 700; color: var(--np-dark-blue); margin: 1rem 0 0.3rem;">Tot dan: een schatting op rekenregels</p>
<table style="font-size: 0.74rem; width: 86%;">
<thead><tr><th style="width: 34%;">Werk</th><th style="width: 46%;">Bezetting</th><th style="width: 20%;">Doorlooptijd</th></tr></thead>
<tbody>
<tr><td>Leerroute uitwerken</td><td>1 solutionarchitect, 1 business-analist, 0,5 domeinarchitect</td><td>4 weken</td></tr>
<tr><td>Variant van een leerroute</td><td>hetzelfde team</td><td>2 weken per variant</td></tr>
<tr><td>Interactieketen tot specificatie</td><td>1 solutionarchitect</td><td>2 weken per keten</td></tr>
<tr><td>Reviewronde per keten</td><td>0,5 solutionarchitect, 0,5 business-analist</td><td>2 weken</td></tr>
<tr><td>Backlog, roadmap en releases</td><td>0,2 productowner</td><td>doorlopend</td></tr>
</tbody>
</table>

</div>

<!--
De backlog is de basis: daarop schatten we de werklast, en daaruit volgen de roadmap en de capaciteit. Begin december staat
dat er voor leerroute 1. Tot die tijd rekenen we met deze rekenregels. De productowner op 0,2 FTE is een schatting.
-->

---

<!-- 7. CAPACITEIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Capaciteit: schatting tot eind Q1 2027

<div class="np-grid-2" style="margin-top: 0.4rem; gap: 1.2rem;">
<table style="font-size: 0.66rem;">
<thead><tr><th style="width: 74%;">Leerroute 1, regulier</th><th style="width: 26%; text-align: right;">FTE-weken</th></tr></thead>
<tbody>
<tr><td>Anker, scenario 1.1 uitwerken</td><td style="text-align: right;">10</td></tr>
<tr><td>Scenario's 1.2 tot en met 1.4</td><td style="text-align: right;">15</td></tr>
<tr><td>Keten onderwijsaanbod tot specificatie</td><td style="text-align: right;">4</td></tr>
<tr><td>Keten student-instroom tot specificatie</td><td style="text-align: right;">4</td></tr>
<tr><td>Keten bijsturen tot specificatie</td><td style="text-align: right;">4</td></tr>
<tr><td>Ketenwerk door de scenario's</td><td style="text-align: right;">0–12</td></tr>
<tr><td><b>Subtotaal leerroute 1</b></td><td style="text-align: right;"><b>37–49</b></td></tr>
</tbody>
</table>
<table style="font-size: 0.66rem;">
<thead><tr><th style="width: 74%;">Leerroute 2, temporiseren</th><th style="width: 26%; text-align: right;">FTE-weken</th></tr></thead>
<tbody>
<tr><td>Anker, scenario 2.1 uitwerken</td><td style="text-align: right;">10</td></tr>
<tr><td>Scenario's 2.2 tot en met 2.4</td><td style="text-align: right;">15</td></tr>
<tr><td>Keten onderwijsaanbod, wijziging</td><td style="text-align: right;">0–4</td></tr>
<tr><td>Keten student-instroom, wijziging</td><td style="text-align: right;">0–4</td></tr>
<tr><td>Keten bijsturen, wijziging</td><td style="text-align: right;">0–4</td></tr>
<tr><td>Ketenwerk door de scenario's</td><td style="text-align: right;">0–12</td></tr>
<tr><td><b>Subtotaal leerroute 2</b></td><td style="text-align: right;"><b>25–49</b></td></tr>
</tbody>
</table>
</div>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.6rem; margin-top: 0.7rem;">
<div style="background: white; border: 1px solid var(--np-light-gray); border-radius: 10px; padding: 0.45rem 0.7rem;"><div style="font-size: 0.62rem; color: var(--np-mid-gray);">Gezamenlijk: basis, productowner, stakeholders, backlog</div><div style="font-size: 1.15rem; font-weight: 700;">33,8</div></div>
<div style="background: white; border: 1px solid var(--np-light-gray); border-radius: 10px; padding: 0.45rem 0.7rem;"><div style="font-size: 0.62rem; color: var(--np-mid-gray);">Totaal, in FTE-weken</div><div style="font-size: 1.15rem; font-weight: 700;">96–132</div></div>
<div style="background: var(--np-ink); border-radius: 10px; padding: 0.45rem 0.7rem;"><div style="font-size: 0.62rem; color: #BFD3D5;">Nodig technisch, zonder Ruud</div><div style="font-size: 1.15rem; font-weight: 700; color: #73C3CE;">4,9–6,9 FTE</div></div>
<div style="background: var(--np-ink); border-radius: 10px; padding: 0.45rem 0.7rem;"><div style="font-size: 0.62rem; color: #BFD3D5;">Beschikbaar technisch</div><div style="font-size: 1.15rem; font-weight: 700; color: white;">2,8 FTE</div></div>
</div>

<p class="muted" style="font-size: 0.66rem; line-height: 1.45; margin: 0.6rem 0 0; max-width: 740px;">Schatting op de rekenregels van slide 6. Ketenwerk van leerroute 2 en de scenario's: van niets tot een volle keten. Stakeholders: een dag per week per persoon. Backlog in november: Garik 0,5, Niek en Niels 0,1.</p>

</div>

<!--
Dit is een schatting, geen meting. De opgave: leerroute 1 en 2, elk met het anker en drie incidentele scenario's
(vertraging, versnelling, hybride), af aan het eind van Q1 2027: 18 werkweken vanaf 9 november, met de kerstvakantie vrij.
Bronnen: per leerroute vier scenario's volgens de scenario-uitwerkingen in meta; doel Q1 2027 uit de werkgroepdecks van 29
september en 3 november; Garik 32 uur volgens de SI-afstemming van 13 juli. Bij leerroute 2 nemen we aan dat dezelfde drie
ketens terugkomen met een wijziging; dat kost van niets tot een volle keten. Gezamenlijk: basis 13 FTE-weken (informatiemodel,
begrippen, logisch gegevensmodel, ArchiMate-model), productowner 3,6, stakeholdercontact 14,4 (een dag per week voor Ruud,
Garik, Niek en Niels), backlog en planning in november 2,8 (Ruuds 0,1 valt binnen zijn 0,2 als productowner). Het tekort is
2 tot 4 FTE. De backlog en de schatting per taak in november vervangen deze schatting.
-->

---

<!-- 8. BENODIGDE ROLLEN EN WIE ZE DEKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Benodigde rollen en wie ze dekt

<div style="display: flex; gap: 1.2rem; align-items: center; margin-top: 0.4rem;">
<div style="position: relative; width: 600px; height: 330px; flex: none;">
<div style="position: absolute; left: 0; top: 110px; width: 200px; height: 200px; border-radius: 50%; background: rgba(163,58,74,0.13); border: 2px solid #A33A4A;"></div>
<div style="position: absolute; left: 130px; top: 105px; width: 210px; height: 210px; border-radius: 50%; background: rgba(135,75,131,0.15); border: 2px solid #874B83;"></div>
<div style="position: absolute; left: 265px; top: 105px; width: 210px; height: 210px; border-radius: 50%; background: rgba(45,91,138,0.15); border: 2px solid #2D5B8A;"></div>
<div style="position: absolute; left: 440px; top: 0; width: 150px; height: 150px; border-radius: 50%; background: rgba(138,90,18,0.15); border: 2px solid #8A5A12;"></div>
<div style="position: absolute; left: 15px; top: 152px; width: 120px; text-align: center; font-size: 0.66rem; line-height: 1.3; color: #A33A4A;"><b style="color: #A33A4A;">Business-analyse</b><br>1,7–2,2 FTE</div>
<div style="position: absolute; left: 195px; top: 272px; width: 80px; text-align: center; font-size: 0.66rem; line-height: 1.3; color: #874B83;"><b style="color: #874B83;">Domein</b><br>0,9 FTE</div>
<div style="position: absolute; left: 368px; top: 192px; width: 100px; text-align: center; font-size: 0.66rem; line-height: 1.3; color: #2D5B8A;"><b style="color: #2D5B8A;">Solution en API</b><br>1,6–3,1 FTE</div>
<div style="position: absolute; left: 270px; top: 36px; width: 160px; text-align: right; font-size: 0.66rem; line-height: 1.3; color: #8A5A12;"><b style="color: #8A5A12;">Productowner en planning</b><br>0,2 FTE, plus de backlog</div>
<div style="position: absolute; left: 487px; top: 64px; width: 56px; text-align: center; font-size: 0.7rem; font-weight: 700; line-height: 1.6; color: white; background: var(--np-ink); border-radius: 999px;">Ruud</div>
<div style="position: absolute; left: 274px; top: 180px; width: 56px; text-align: center; font-size: 0.7rem; font-weight: 700; line-height: 1.6; color: white; background: var(--np-ink); border-radius: 999px;">Niek</div>
<div style="position: absolute; left: 274px; top: 218px; width: 56px; text-align: center; font-size: 0.7rem; font-weight: 700; line-height: 1.6; color: white; background: var(--np-ink); border-radius: 999px;">Garik</div>
<div style="position: absolute; left: 137px; top: 199px; width: 56px; text-align: center; font-size: 0.7rem; font-weight: 700; line-height: 1.6; color: white; background: var(--np-ink); border-radius: 999px;">Niels</div>
</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 0.6rem;">
<div style="background: var(--np-ink); color: white; border-radius: 12px; padding: 0.8rem 1rem;">
<div style="font-size: 0.7rem; color: #BFD3D5;">Nodig tot eind Q1 2027, geschat</div>
<div style="font-size: 1.9rem; font-weight: 700; color: #73C3CE; line-height: 1.1;">4,9–6,9</div>
<div style="font-size: 0.7rem; color: #BFD3D5;">FTE technisch, met stakeholdercontact</div>
<div style="font-size: 0.7rem; color: #BFD3D5; margin-top: 0.6rem;">Beschikbaar, hoogstens</div>
<div style="font-size: 1.9rem; font-weight: 700; color: white; line-height: 1.1;">2,8</div>
<div style="font-size: 0.7rem; color: #BFD3D5;">FTE technisch: Garik 0,8, Niek en Niels voltijd</div>
</div>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; max-width: 740px; margin-top: 0.5rem;">
<div style="font-size: 0.72rem; line-height: 1.45; color: var(--np-dark-gray);"><b>Overlap is vervanging, geen extra capaciteit:</b> wie domein doet, doet in die uren geen solution of business-analyse.</div>
<div style="font-size: 0.72rem; line-height: 1.45; color: var(--np-dark-gray);"><b>Stakeholdercontact:</b> iedereen besteedt ongeveer een dag per week aan instellingen en leveranciers.</div>
</div>

</div>

<!--
Elke cirkel is een rol die het project nodig heeft, met de geschatte gemiddelde vraag tot eind Q1 2027 voor twee leerroutes
met elk vier scenario's. De namen staan in de overlap van de rollen die iemand kan vervullen. Niek en Garik kunnen allebei
domein en solution, met API- en technische kennis; Garik geeft daarnaast backlog en planning vorm. Niels werkt op
domeinniveau en als business-analist. Ruud is productowner en projectleider. Voor test en adoptie is er nog niemand. De
overlap maakt vervanging mogelijk, maar levert geen extra uren: technisch is er hoogstens 2,8 FTE, terwijl 4,9 tot 6,9 FTE
nodig is, inclusief het backlogwerk in november en een dag per week contact met instellingen en leveranciers per persoon.
Bron voor Gariks 32 uur: SI-afstemming 13 juli 2026.
-->

---

<!-- 9. PROJECTOPZET NOVEMBER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Projectopzet november

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.6rem; margin-top: 0.4rem;">
<div class="np-card accent-blue" style="padding: 0.5rem 0.7rem;"><h3 style="margin: 0;">Niek</h3><p class="muted" style="font-size: 0.7rem; margin: 0;">Leerroute 1, solution; 0,1 FTE backlog en planning</p></div>
<div class="np-card accent-pink" style="padding: 0.5rem 0.7rem;"><h3 style="margin: 0;">Niels</h3><p class="muted" style="font-size: 0.7rem; margin: 0;">Leerroute 1, business-analyse; 0,1 FTE backlog en planning</p></div>
<div class="np-card accent-orange" style="padding: 0.5rem 0.7rem;"><h3 style="margin: 0;">Garik</h3><p class="muted" style="font-size: 0.7rem; margin: 0;">0,5 FTE backlog en planning, vormgeven en verfijnen met het team; daarnaast leerroute 1</p></div>
<div class="np-card accent-yellow" style="padding: 0.5rem 0.7rem;"><h3 style="margin: 0;">Ruud</h3><p class="muted" style="font-size: 0.7rem; margin: 0;">Productowner; 0,1 FTE om backlog en planning te bespreken</p></div>
</div>

<table style="font-size: 0.68rem; margin-top: 0.7rem;">
<thead><tr><th style="width: 19%;">Week</th><th style="width: 45%;">Backlog en planning</th><th style="width: 16%;">Leerroute 1</th><th style="width: 20%;">Wie</th></tr></thead>
<tbody>
<tr><td>46 &middot; 9–13 nov</td><td>Opbouw van de backlog vastleggen; plek kiezen</td><td>Uitwerken</td><td>Garik, met Ruud</td></tr>
<tr><td>47 &middot; 16–20 nov</td><td>Backlog vullen voor de drie ketens</td><td>Uitwerken</td><td>Garik, met Niek en Niels</td></tr>
<tr><td>48 &middot; 23–27 nov</td><td>Werklast per taak schatten</td><td>Uitwerken</td><td>Garik, met het team</td></tr>
<tr><td>49 &middot; 30 nov–4 dec</td><td>Roadmap en capaciteit afleiden; backlog bijwerken met de ketens uit de uitwerking</td><td>Uitwerken</td><td>Garik, met Ruud</td></tr>
</tbody>
</table>

<p style="font-size: 0.74rem; line-height: 1.45; margin: 0.6rem 0 0; color: var(--np-dark-gray); max-width: 740px;"><b>Begin december:</b> een backlog voor leerroute 1 met een schatting per taak, en daaruit de roadmap en de capaciteit per rol. Leerroute 1 krijgt in november minder dan de 2,5 FTE uit de rekenregel.</p>

</div>

<!--
Niek, Niels en Garik werken leerroute 1 verder uit. Garik geeft de backlog en de planning vorm en verfijnt ze met het team:
0,5 FTE van Garik, 0,1 FTE van Niek en van Niels, en 0,1 FTE van Ruud om backlog en planning te bespreken. Leerroute 1
krijgt daardoor in november minder dan de 2,5 FTE die de rekenregel vraagt (een solutionarchitect, een business-analist en
een halve domeinarchitect), ook omdat iedereen ongeveer een dag per week aan contact met instellingen en leveranciers
besteedt. De uitwerking duurt dus langer dan vier weken.
-->

---

<!-- AFSLUITSLIDE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>
