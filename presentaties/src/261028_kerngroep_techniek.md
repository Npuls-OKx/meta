---
theme: default
title: "Kerngroep techniek, 28 oktober 2026"
info: "Kerngroep techniek 28 oktober 2026, online: de stand van de vijf punten van 30 september, de voorbeelduitwerking per fase, de scope van het informatiemodel en twee besluiten die blijven liggen."
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
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 36rem;">Voorbeelduitwerking per fase &middot; Scope van het informatiemodel &middot; Versionering &middot; Twee besluiten</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 28 oktober 2026 &middot; online</div>
</div>

<!--
Online sessie. De sessie van 14 oktober is vervallen, dus er zit vier weken tussen deze en
Amersfoort. Datum onder voorbehoud. Opzet nog af te stemmen. Twee van de vijf punten van
30 september zijn niet beslecht, en op de versionering kwam weerstand uit de werkgroep techniek.
Die twee besluiten zijn het doel van vandaag; de voorbeelduitwerking is het bewijs dat er iets
ligt om op te besluiten.
-->

---

<!-- 2. AGENDA -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Agenda

<div class="np-grid-3" style="margin-top:1.3rem;gap:0.9rem;">
<div class="np-card"><carbon-time style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">1 Stand van zaken</div><small>30 september, en de cijfers</small></div>
<div class="np-card accent-orange"><carbon-chat style="font-size:1.5rem;color:var(--np-orange);" /><div style="font-weight:600;margin-top:0.3rem;">2 De reviewronde</div><small>veertien issues</small></div>
<div class="np-card accent-green"><carbon-map style="font-size:1.5rem;color:var(--np-green);" /><div style="font-weight:600;margin-top:0.3rem;">3 Voorbeelduitwerking</div><small>Niek</small></div>
<div class="np-card"><carbon-network-3 style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">4 Sectoroverstijgend</div><small>Niek</small></div>
<div class="np-card accent-orange"><carbon-assembly-cluster style="font-size:1.5rem;color:var(--np-orange);" /><div style="font-weight:600;margin-top:0.3rem;">5 Versionering</div><small>Garik</small></div>
<div class="np-card accent-green"><carbon-user-multiple style="font-size:1.5rem;color:var(--np-green);" /><div style="font-weight:600;margin-top:0.3rem;">6 Capaciteit</div><small>Ruud</small></div>
</div>

</div>

<!--
Opzet van het kernteam, nog af te stemmen met Garik, Niels en Ruud.

Blok 1 is de terugblik op 30 september en duurt kort: wat is afgesproken, wat is gevraagd, en
wat er sindsdien is verzet. Blok 2 is nieuw en gaat over de werkwijze: pull request 104 is
gesloten en elke opmerking draagt nu een eigen issue. Blok 3 en 4 zijn van mij, blok 5 van
Garik, blok 6 van Ruud.

De peiling aan het eind is de vaste afsluiting uit meta #205.
-->

---

<!-- SECTIE 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 1 van 6</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Stand van zaken</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; 30 september, en wat er sindsdien gebeurde</div>
</div>

<!--
Sectiescheiding. Terugblik op 30 september: zes toezeggingen van OKx, vijf vragen aan de
leveranciers, en wat de cijfers zeggen over waar het werk heen ging.
-->

---

<!-- 3. AFSPRAKEN OKX -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat OKx zou leveren

<div style="margin-top:1rem;display:grid;grid-template-columns:1fr auto;gap:0.5rem 1rem;align-items:center;max-width:88%;font-size:0.98rem;">
<div><carbon-pull-request style="font-size:1.1rem;color:var(--np-blue);vertical-align:-0.15rem;" /> Kleinere pull requests</div><div class="pil groen">Gedaan</div>
<div><carbon-network-3 style="font-size:1.1rem;color:var(--np-blue);vertical-align:-0.15rem;" /> Mbo en sectoroverstijgend scheiden</div><div class="pil blauw">Loopt</div>
<div><mdi-key-variant style="font-size:1.1rem;color:var(--np-blue);vertical-align:-0.15rem;" /> Kwalificatiedossier naar leeruitkomsten</div><div class="pil blauw">Loopt</div>
<div><carbon-user-favorite style="font-size:1.1rem;color:var(--np-mid-gray);vertical-align:-0.15rem;" /> Keuzeregels voor mbo en hbo</div><div class="pil grijs">Niet opgepakt</div>
<div><carbon-assembly-cluster style="font-size:1.1rem;color:var(--np-mid-gray);vertical-align:-0.15rem;" /> Eenheid aan meerdere opleidingen</div><div class="pil grijs">Niet opgepakt</div>
<div><carbon-document style="font-size:1.1rem;color:var(--np-mid-gray);vertical-align:-0.15rem;" /> Document bij de bouwblokaanpak</div><div class="pil grijs">Draft</div>
</div>

<div class="np-bottomline" style="margin-top:1.4rem;">Twee van de zes schoven door: de capaciteit ging naar het opsplitsen.</div>

<style scoped>
.pil { border-radius:999px; padding:0.2rem 0.8rem; font-size:0.8rem; font-weight:600; text-align:center; }
.pil.groen { background:#DDF3E8; color:#2b6b4a; }
.pil.blauw { background:#E8F0FF; color:#2d4f8a; }
.pil.grijs { background:#EEF1F5; color:#5b6472; }
</style>

</div>

<!--
Bron: de notulen van 30 september, kopje "Op te volgen taken". Zes toezeggingen van onze kant.

Gedaan: PR 252 is opgesplitst in veertien, waarvan acht per fase. Dat was de afspraak die de
review moest vlottrekken.

Loopt: het onderscheid tussen mbo-specifiek en generiek staat als meta #318, #319 en #320, en
de minor staat al in fase 1. De vertaling naar leeruitkomsten loopt via de herschreven
leeruitkomsten van fase 1, met meta #315 voor de definitie en #316 voor de gelaagdheid.

Niet opgepakt: de keuzeregels voor mbo en hbo, en het koppelen van een onderwijseenheid aan
meerdere opleidingen. Dat is een keuze geweest, geen vergeten punt: de capaciteit ging naar het
opsplitsen van de voorbeelduitwerking.

Het document bij de bouwblokaanpak staat bij Garik, Public PR 100, nog op draft.
-->

---

<!-- 4. GEVRAAGD AAN LEVERANCIERS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat aan de leveranciers is gevraagd

<div style="margin-top:1rem;display:grid;grid-template-columns:1fr auto;gap:0.5rem 1rem;align-items:center;max-width:88%;font-size:0.98rem;">
<div><carbon-assembly-cluster style="font-size:1.1rem;color:var(--np-mid-gray);vertical-align:-0.15rem;" /> Versioneringsscenario's</div><div class="pil grijs">Nog niet gezien</div>
<div><carbon-time style="font-size:1.1rem;color:var(--np-mid-gray);vertical-align:-0.15rem;" /> Capaciteitsinschatting</div><div class="pil grijs">Nog niet gezien</div>
<div><carbon-pull-request style="font-size:1.1rem;color:var(--np-green);vertical-align:-0.15rem;" /> Reactie per pull request</div><div class="pil groen">14 opmerkingen</div>
<div><carbon-task-complete style="font-size:1.1rem;color:var(--np-green);vertical-align:-0.15rem;" /> Validatie tegen eigen systemen</div><div class="pil groen">Drie lezers</div>
<div><carbon-catalog style="font-size:1.1rem;color:var(--np-mid-gray);vertical-align:-0.15rem;" /> Koppelingen voor Q1</div><div class="pil grijs">Nog niet gezien</div>
</div>

<div class="np-bottomline" style="margin-top:1.4rem;">Termijn liep op 14 oktober af. Wat per mail of in een sessie kwam, staat hier niet in.</div>

<style scoped>
.pil { border-radius:999px; padding:0.2rem 0.8rem; font-size:0.8rem; font-weight:600; text-align:center; }
.pil.groen { background:#DDF3E8; color:#2b6b4a; }
.pil.grijs { background:#EEF1F5; color:#5b6472; }
</style>

</div>

<!--
Bron: de notulen van 30 september. Vijf vragen, alle vijf met een termijn van twee weken, die op
14 oktober afliep. Deze sessie is verzet van 14 naar 28 oktober, dus die termijn staat nu twee
weken over tijd.

Drie van de vijf zijn in GitHub niet terug te zien: de versioneringsscenario's, de
capaciteitsinschatting en de koppelingen voor Q1. Dat is bewust voorzichtig geformuleerd, want
er lopen een-op-eensessies met Topicus, Kaski, Schedule en Educator, en wat daar is gezegd staat
niet in een repository. De vraag aan de zaal is dus eerst: klopt dit beeld?

Wat wel kwam is de review zelf: veertien opmerkingen op PR 104 van drie lezers, met Jan Hendrik
van Schaik die Xedule er regel voor regel naast legde. Daar gaat deel 2 over.
-->

---

<!-- 5. WAT ER IS VERZET -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar het werk heen ging

<div class="np-grid-2" style="margin-top:1.2rem;gap:2.4rem;">
<div class="np-card accent-green" style="text-align:center;padding:1.2rem;">
<carbon-code style="font-size:1.6rem;color:var(--np-green);" />
<div style="font-weight:600;margin-top:0.3rem;font-size:1.05rem;">meta</div>
<div style="display:flex;justify-content:center;gap:1.6rem;margin-top:0.7rem;">
<div><div class="np-big-number" style="color:var(--np-green);">16</div><small>pull requests</small></div>
<div><div class="np-big-number" style="color:var(--np-green);">34</div><small>issues</small></div>
</div>
</div>
<div class="np-card accent-orange" style="text-align:center;padding:1.2rem;">
<carbon-document style="font-size:1.6rem;color:var(--np-orange);" />
<div style="font-weight:600;margin-top:0.3rem;font-size:1.05rem;">Public</div>
<div style="display:flex;justify-content:center;gap:1.6rem;margin-top:0.7rem;">
<div><div class="np-big-number" style="color:var(--np-orange);">1</div><small>pull request</small></div>
<div><div class="np-big-number" style="color:var(--np-orange);">0</div><small>issues</small></div>
</div>
</div>
</div>

<div class="np-bottomline" style="margin-top:1.5rem;">Public draagt wat een leverancier gebruikt om te bouwen.</div>

</div>

<!--
Cijfers uit GitHub over 1 tot en met 12 oktober, beide repositories. Deze willen een opfrissing
vlak voor de sessie.

Het verschil tussen de twee kaarten is de boodschap. In meta liep het door: gereedschap, de
voorbeelduitwerking en het harnas. In Public, waar de artefacten staan waarmee een leverancier
bouwt, sloot in twaalf dagen een pull request, met dode verwijzingen naar de opgeheven fork.

Inschatting van de maker, te overrulen: de draft-status is hier de rem. Vijf van de zes open
pull requests in Public staan op draft en vragen formeel geen review, dus er is weinig om op te
sluiten. Dat is dezelfde lijn als de slide "Veel verzet, weinig afgerond" van 30 september.
-->

---

<!-- 6. WERK PER ONDERWERP -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Werk per onderwerp

<div class="np-grid-3" style="margin-top:1.3rem;gap:0.9rem;">
<div class="np-card accent-green"><carbon-map style="font-size:1.5rem;color:var(--np-green);" /><div style="font-weight:600;margin-top:0.3rem;">Voorbeelduitwerking</div><small>veertien pull requests<br/>38 bevindingen verantwoord</small></div>
<div class="np-card accent-orange"><carbon-network-3 style="font-size:1.5rem;color:var(--np-orange);" /><div style="font-weight:600;margin-top:0.3rem;">OEAPI</div><small>fork opgeheven<br/>submodule met overlay</small></div>
<div class="np-card"><carbon-building style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Sectorketen</div><small>zeven lagen, 52 producten<br/>voor de sync van 3 november</small></div>
<div class="np-card"><carbon-rule style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Model bewaakt</div><small>controle bij elke wijziging</small></div>
<div class="np-card"><carbon-task-complete style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Werkwijze</div><small>criteria in het issue<br/>vaste vorm per pull request</small></div>
</div>

</div>

<!--
Vijf onderwerpen, in volgorde van wat de kerngroep ervan merkt.

De eerste twee raken de specificatie rechtstreeks. PR 252 is gemerged en opgesplitst in
veertien; de 38 bevindingen uit de reviewronde van Niels staan nu in de bron zelf, met per
bevinding het beeld waarop zij slaat en de status. De fork van de OEAPI-specificatie is op
verzoek van de OEAPI-beheerder opgeheven en vervangen door een submodule met een overlay
erover; het werk uit de fork is bewaard.

De sectorketen hoort bij de architectuursync van 3 november en staat hier alleen ter
kennisname: zeven lagen met hun partijen en producten, getekend uit een bron.

De laatste twee zijn werkplaatsonderhoud: zichtbaar in de cijfers, onzichtbaar in de
specificatie, en de reden dat de aantallen in meta zo hoog liggen.
-->

---

<!-- 7. TWEE AFSPRAKEN DIE AL STAAN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee afspraken die al staan

<div class="np-grid-2" style="margin-top:1.4rem;gap:2rem;">
<div class="np-card accent-green" style="padding:1.3rem;">
<carbon-task-complete style="font-size:1.7rem;color:var(--np-green);" />
<div style="font-weight:600;font-size:1.1rem;margin-top:0.4rem;">Akkoord op een pull request</div>
<div style="margin-top:0.6rem;font-size:0.95rem;line-height:1.7;">Gezien en richting gesteund<br/>Geen bouwverplichting</div>
</div>
<div class="np-card accent-orange" style="padding:1.3rem;">
<carbon-time style="font-size:1.7rem;color:var(--np-orange);" />
<div style="font-weight:600;font-size:1.1rem;margin-top:0.4rem;">Review staat twee weken open</div>
<div style="margin-top:0.6rem;font-size:0.95rem;line-height:1.7;">Langer bij een groter onderwerp<br/>Meer tijd nodig: zeg het</div>
</div>
</div>

<div class="np-bottomline" style="margin-top:1.5rem;">Beide vastgesteld op 30 september.</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Betekenis van akkoord" en "Reviewtermijn". Ruud
verduidelijkte het eerste, ik het tweede.

Dit herhalen loont. De aarzeling om te tekenen kwam voort uit het idee dat een akkoord een
bouwverplichting is, en dat is het niet: het zegt dat de inhoud is bekeken en dat de richting
wordt gesteund. Een bouwverplichting ontstaat pas bij de bouwfase, en daar gaat deel 6 over.

Over de termijn: stilte levert te weinig om op te plannen. Meer tijd nodig is een prima
antwoord, mits het gezegd wordt.
-->

---

<!-- SECTIE 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 2 van 6</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">De reviewronde</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; wat er met elke opmerking gebeurt</div>
</div>

<!--
Sectiescheiding. Pull request 104 is gesloten en elke opmerking draagt nu een eigen issue. Dit
deel legt die werkwijze uit en laat zien wat er vandaag een keuze vraagt. De inbrengers zitten
in de zaal, dus dit is het moment om te laten zien dat hun tijd ergens heen is gegaan.
-->

---

<!-- 8. PR 104 GESLOTEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Pull request 104 is gesloten

<div class="np-pipeline" style="margin-top:1.5rem;">
  <div class="np-step blue"><carbon-chat class="np-pic" /><div class="np-getal">13</div><div>opmerkingen</div><small>drie lezers</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue"><carbon-list-checked class="np-pic" /><div class="np-getal">14</div><div>issues</div><small>elk met het citaat</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange"><carbon-chat class="np-pic oranje" /><div class="np-getal oranje">12</div><div>op tafel</div><small>vandaag</small></div>
</div>

<div class="np-card accent-green" style="margin-top:1.5rem;padding:0.8rem 1.1rem;">
<carbon-user-follow style="font-size:1.3rem;color:var(--np-green);vertical-align:-0.2rem;" /> <strong style="color:var(--np-ink);">Elk issue staat op naam van de inbrenger</strong>
</div>

<style scoped>
.np-pic { font-size: 1.5rem; color: var(--np-blue); margin: 0 auto; }
.np-pic.oranje { color: var(--np-orange); }
.np-getal { font-size: 2.1rem; line-height: 1.05; color: var(--np-dark-blue); }
.np-getal.oranje { color: var(--np-orange); }
.np-step { min-width: 8.4rem; }
</style>

</div>

<!--
De pull request stond open op een discussie die nooit kon sluiten: inhoudelijk antwoorden houdt
hem open, mergen zonder antwoord laat de inbrenger in het ongewisse. Vandaar deze knip. Het
informatiemodel komt daarmee beschikbaar als laag 1 en 2, en geen enkele opmerking vervalt.

In elk issue staat de opmerking letterlijk, met auteur en datum, dan wat OKx erin leest, en de
vraag of het issue de opmerking dekt. Dat citaat is wat het issue bruikbaar houdt als niemand
de pull request er nog bij pakt.

Dat het issue op naam van de inbrenger staat is geen werkopdracht maar eigenaarschap over de
afhandeling: hij bepaalt of het antwoord volstaat, en hij kan het volgen.

Dertien opmerkingen worden veertien issues omdat een comment van Jan Hendrik vijf losse punten
droeg en twee opmerkingen over hetzelfde onderwerp zijn samengevoegd.
-->

---

<!-- 9. DRIE UITGANGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Elke opmerking kent drie uitgangen

<div class="np-grid-3" style="margin-top:1.4rem;gap:1rem;">
<div class="np-card accent-green" style="padding:1.2rem;">
<carbon-task-complete style="font-size:1.7rem;color:var(--np-green);" />
<div style="font-weight:600;font-size:1.05rem;margin-top:0.4rem;">Jij sluit</div>
<small>Het antwoord volstaat</small>
<div class="telling" style="color:#2b6b4a;background:#DDF3E8;">vandaag 2</div>
</div>
<div class="np-card accent-orange" style="padding:1.2rem;">
<carbon-chat style="font-size:1.7rem;color:var(--np-orange);" />
<div style="font-weight:600;font-size:1.05rem;margin-top:0.4rem;">Op de agenda</div>
<small>Het vraagt een keuze</small>
<div class="telling" style="color:#7a6320;background:#FFF4CC;">vandaag 12</div>
</div>
<div class="np-card" style="padding:1.2rem;">
<carbon-close-outline style="font-size:1.7rem;color:var(--np-mid-gray);" />
<div style="font-weight:600;font-size:1.05rem;margin-top:0.4rem;">Wij sluiten</div>
<small>Met de reden erbij</small>
<div class="telling" style="color:#5b6472;background:#EEF1F5;">vandaag 0</div>
</div>
</div>

<div class="np-bottomline" style="margin-top:1.5rem;">Oppakken is een antwoord, geen toezegging om te bouwen.</div>

<style scoped>
.np-card small { display: block; }
.telling { border-radius:999px; padding:0.15rem 0.7rem; font-size:0.78rem; font-weight:600; display:inline-block; margin-top:0.7rem; }
</style>

</div>

<!--
Dit is de kern van de nieuwe werkwijze en het verdient een minuut.

Jij sluit: het antwoord staat onder het issue, het issue staat op jouw naam, en jij sluit hem
of zegt wat er nog mist. Vandaag twee: het keuzedeel als specialisatie, en het examen als
bijzondere vorm van toets. Bij beide staat het beeld uit de plaat erbij.

Op de agenda: het vraagt een keuze, of het raakt meer partijen dan de inbrenger. Vandaag twaalf,
en die staan op de volgende slide.

Wij sluiten staat er bewust bij: OKx mag een punt ook niet overnemen, mits de reden erbij staat
met de bron, zodat die te weerspreken is. Zonder die uitgang wordt elke opmerking stilzwijgend
een belofte. Vandaag valt geen enkel punt in die categorie.

En de regel eronder: een wijziging volgt pas als wij daar samen aanleiding voor zien, en dan
als pull request.
-->

---

<!-- 10. TWAALF PUNTEN, VIER KEUZES -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twaalf punten, vier keuzes

<div class="np-grid-2" style="margin-top:1.2rem;gap:1rem;">
<div class="np-card accent-orange"><carbon-crop style="font-size:1.4rem;color:var(--np-orange);" /><div style="font-weight:600;margin-top:0.25rem;">Scope van de uitwisseling</div><small>Valt de les erbinnen<br/>Wat mag een koppeling aannemen</small><div class="nrs">#115 #119 #121</div></div>
<div class="np-card accent-green"><carbon-user-favorite style="font-size:1.4rem;color:var(--np-green);" /><div style="font-weight:600;margin-top:0.25rem;">Kiezen</div><small>Regelset op specificatie of aanbod<br/>Telt locatie mee</small><div class="nrs">#113 #114</div></div>
<div class="np-card"><carbon-chart-line style="font-size:1.4rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.25rem;">De resultaatlijn</div><small>Waar ontstaat een resultaat<br/>Altijd via een groep</small><div class="nrs">#117 #120 #122</div></div>
<div class="np-card"><carbon-book style="font-size:1.4rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.25rem;">Begrippen</div><small>Intekenen, leeruitkomst,<br/>kwalificatiekader, examenonderdeel</small><div class="nrs">#112 #118 #124 #125</div></div>
</div>

<div class="np-bottomline" style="margin-top:1.3rem;">Aanvullen vooraf maakt de bespreking korter.</div>

<style scoped>
.nrs { font-family: ui-monospace, monospace; font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.45rem; }
</style>

</div>

<!--
Twaalf losse punten passen niet in een sessie, dus zij staan hier gegroepeerd naar de keuze die
eronder ligt. Per thema een keuze in plaats van twaalf toelichtingen.

Scope: valt de lesgelegenheid binnen de uitwisseling, zoals Jan Hendrik bij ontwerpkeuze 8
vraagt, en wat mag een koppeling veronderstellen over de opbouw in het bronsysteem. Dat laatste
komt uit zijn constatering dat het aanbod in Xedule niet topdown opvraagbaar is.

Kiezen: hangt de keuzeregelset aan de specificatie of aan het aanbod, en telt locatie mee als
keuzebepalende factor. Jan Hendrik gaf bij het eerste zijn eigen afweging: de specificatie is
methodisch het mooiere vertrekpunt, met mutatie per aanbodsperiode.

De resultaatlijn: op welke niveaus ontstaat een resultaat, loopt een verbintenis altijd via een
groep, en waar hangt het cohort.

Begrippen: vier terminologiepunten die schriftelijk kunnen als de tijd ontbreekt.

Inschatting van de maker, te overrulen: scope en kiezen raken de koppeling het hardst en gaan
dus voor.

Alle twaalf dragen het label agenda kerngroep techniek en staan op naam van de inbrenger.
-->

---

<!-- SECTIE 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 3 van 6</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Voorbeelduitwerking</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; van een pull request naar veertien</div>
</div>

<!--
Sectiescheiding. De afspraak van 30 september was: kleinere, beter afgebakende pull requests.
Dit deel laat zien wat dat heeft opgeleverd en waar de review nu op kan aangrijpen.
-->

---

<!-- 11. VAN EEN PR NAAR VEERTIEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van een pull request naar veertien

<div style="margin-top:1.5rem;display:grid;grid-template-columns:auto 1fr;gap:0.9rem 1.2rem;align-items:center;max-width:76%;">
<div class="nr groen">5</div><div><strong>Gereedschap</strong><br/><small>bron, controle, generator, tekenaar</small></div>
<div class="nr blauw">8</div><div><strong>Per fase van de leerroute</strong><br/><small>elk met zijn bevindingen verantwoord</small></div>
<div class="nr grijs">1</div><div><strong>Leeswijzer bij de bron</strong><br/><small>wat een reviewer opent</small></div>
</div>

<div class="np-bottomline" style="margin-top:1.6rem;">Op 30 september lag dit er als een. Te groot om op te reageren.</div>

<style scoped>
.nr { width:3rem;height:3rem;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:700;color:#fff; }
.nr.groen { background:#7CCBA8; } .nr.blauw { background:#7A97F2; } .nr.grijs { background:#B8BEC7; }
</style>

</div>

<!--
Dit is de afspraak van 30 september, uitgevoerd.

De splitsing is geen cosmetica: een reviewer kan nu op een fase reageren zonder de andere zeven
te hoeven lezen. De vijf over het gereedschap zijn het contract onder de bron, de controle, de
documentgenerator, de tekenaar en het kaderscenario. De acht per fase volgen de leerroute van
Jochem van kwalificatiedossier tot diplomering.

De eerste van de veertien is gemerged, de rest gaat op volgorde door.
-->

---

<!-- 12. WAT EEN FASE-PR DRAAGT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat een fase-pull request draagt

<div class="np-grid-4" style="margin-top:1.4rem;gap:0.8rem;">
<div class="np-card"><carbon-image style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Beelden</div><small>uit de bron getekend</small></div>
<div class="np-card"><carbon-chat style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Bevindingen</div><small>38 uit de reviewronde</small></div>
<div class="np-card"><carbon-document style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Document</div><small>het stuk van die fase</small></div>
<div class="np-card"><carbon-rule style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Controle</div><small>is de fase compleet</small></div>
</div>

<div style="display:flex;gap:0.6rem;margin-top:1.5rem;max-width:70%;font-size:0.88rem;">
<div style="flex:1;background:#DDF3E8;border-radius:8px;padding:0.55rem;text-align:center;">doorgevoerd</div>
<div style="flex:1;background:#FFF4CC;border-radius:8px;padding:0.55rem;text-align:center;">open</div>
<div style="flex:1;background:#F3E4DC;border-radius:8px;padding:0.55rem;text-align:center;">geparkeerd, met reden</div>
</div>

</div>

<!--
De bevindingen staan in de bron zelf in plaats van in een commitbericht, elk met het beeld
waarop zij slaat, de lezer, de datum en de status. Daardoor kan de controle nalopen of een
bevinding naar een bestaand beeld wijst en of elk thema bekend is.

Een geparkeerde bevinding draagt verplicht een reden. Dat voorkomt dat iets stil verdwijnt, en
het is dezelfde gedachte als de derde uitgang uit deel 2.

De 38 bevindingen komen uit de reviewronde van Niels van Duin op de voorbeelduitwerking.
-->

---

<!-- 13. DE LEERUITKOMST HERSCHREVEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill" style="padding: 0.9rem 1.2rem;">

# De leeruitkomst, herschreven

<div style="display:grid;grid-template-columns:11rem 1fr;gap:1.2rem;align-items:center;margin-top:0.5rem;height:calc(100% - 3.4rem);">
<div style="font-size:0.95rem;line-height:2;">
<div style="color:var(--np-orange);font-weight:700;">werkwoord</div>
<div style="color:var(--np-orange);font-weight:700;">type</div>
<div style="color:var(--np-orange);font-weight:700;">onderwerp</div>
<div style="color:var(--np-orange);font-weight:700;">standaard</div>
<div style="color:var(--np-orange);font-weight:700;">context</div>
<div style="margin-top:0.9rem;font-size:0.82rem;color:var(--np-dark-gray);line-height:1.45;">De standaard maakt haar toetsbaar</div>
</div>
<div style="height:100%;overflow:hidden;display:flex;align-items:flex-start;justify-content:center;">
  <img src="/platen/voorbeeld-f1-03.svg" style="width:100%;object-fit:cover;object-position:top;" />
</div>
</div>

</div>

<!--
Bron: de conventie leeruitkomsten van 6 oktober, het tuning model.

De leeruitkomsten in het voorbeeld stonden er als losse zinnen. Zij zijn herschreven langs vijf
vaste onderdelen: een actief werkwoord voor wat de student doet, het type beheersing, het
onderwerp, de standaard waaraan het wordt afgemeten, en de context waarin de student het laat
zien.

Wijs op de standaard. Dat is het onderdeel dat in de praktijk het vaakst ontbreekt, en precies
het onderdeel dat een leeruitkomst toetsbaar maakt en daarmee vergelijkbaar tussen instellingen.

Dit raakt de taak van 30 september over de gestandaardiseerde vertaling van kwalificatiedossier
naar leeruitkomsten. De vorm staat nu vast; de definitie zelf staat als meta #315 en de
gelaagdheid als #316. Jan Hendrik stelde daarbij voor om het niveau van een competentie in de
formulering op te nemen; dat is Public #118.
-->

---

<!-- SECTIE 4 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 4 van 6</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Sectoroverstijgend</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; wat is mbo, wat geldt breder</div>
</div>

<!--
Sectiescheiding. De taak van 30 september: maak in het informatiemodel duidelijk welke
onderdelen mbo-specifiek zijn en welke sectoroverstijgend bedoeld zijn. Luke en Huib Jan
brachten dit allebei in, vanuit verschillende hoek.
-->

---

<!-- 14. GENERIEK OBJECT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een generiek object, een eigen naam per sector

<div style="margin-top:1.6rem;display:flex;flex-direction:column;align-items:center;gap:0.5rem;">
<div style="background:#E8F0FF;border:1px solid #A9BEF0;border-radius:10px;padding:0.75rem 1.6rem;font-weight:600;font-size:1.05rem;">Opleidingsprogramma specificatie</div>
<div style="color:var(--np-mid-gray);font-size:0.78rem;">specialisatie</div>
<div style="display:flex;gap:1.2rem;">
<div style="background:#DDF3E8;border:1px solid #96CDB2;border-radius:10px;padding:0.7rem 1.5rem;text-align:center;"><strong>Keuzedeel</strong><br/><small>mbo</small></div>
<div style="background:#FFF4CC;border:1px solid #E8D48A;border-radius:10px;padding:0.7rem 1.5rem;text-align:center;"><strong>Minor</strong><br/><small>hbo</small></div>
</div>
</div>

<div class="np-bottomline" style="margin-top:1.6rem;">Hetzelfde patroon door alle vier de lagen, van specificatie tot resultaat.</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Sectoroverstijgende opbouw" en "Keuzeregels en
subtypen", plus de review van Luke Niesink en Huib Jan Wielemaker op Public PR 104.

Het punt dat ik hier maak: dit stond al in de plaat, alleen niet expliciet genoeg. Keuzedeel is
een specialisatie van Opleidingsprogramma specificatie, en datzelfde patroon loopt door alle
vier de lagen: specificatie, aanbod, verbintenis en resultaat. Een keuzedeel en een minor erven
die structuur en voegen hun eigen regels toe.

Daarmee is een sectorspecifieke term geen apart model maar een naam op een generiek object, en
dat is wat een module tussen instellingen en tussen sectoren uitwisselbaar houdt.

De vraag van de leverancier was terecht, want de uitleg ontbrak. Die staat nu in de leeswijzer
van de voorbeelduitwerking. Wat er nog moet gebeuren is de minor in het model zelf zetten, en
dat vraagt de modelleur in Archi. Dat loopt als meta #319.
-->

---

<!-- 15. DE LEERUITKOMST ALS SLEUTEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De leeruitkomst als sleutel tussen instellingen

<div class="np-pipeline" style="margin-top:1.6rem;">
  <div class="np-step"><carbon-building class="np-pic" /><div style="font-weight:600;">Kwalificatiedossier</div><small>landelijk</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange"><mdi-key-variant class="np-pic oranje" /><div style="font-weight:600;">Leeruitkomst</div><small>met een standaard</small></div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step"><carbon-catalog class="np-pic" /><div style="font-weight:600;">Onderwijsspecificatie</div><small>per instelling</small></div>
</div>

<div class="np-bottomline" style="margin-top:1.7rem;">Zonder die tussenlaag vergelijkt niemand twee onderwijsblokken.</div>

<style scoped>
.np-pic { font-size: 1.6rem; color: var(--np-blue); margin: 0 auto; }
.np-pic.oranje { color: var(--np-orange); }
.np-step { min-width: 9.5rem; }
</style>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Herbruikbare leeruitkomsten", "Vertaling naar
leeruitkomsten" en "Huidige beperking".

Kwalificatiedossiers zijn vaak instelling- of opleidingsspecifiek ingericht. Daarom is een
tussenlaag nodig waarin kwalificaties worden vertaald naar beschreven leeruitkomsten. Met die
laag kan een systeem zoeken welke module een gewenste leeruitkomst draagt: binnen een
instelling, tussen instellingen, en op termijn tussen sectoren.

De eerlijke kanttekening erbij: de koppeling alleen lost dit niet op. Blijft een instelling
uitsluitend haar eigen kwalificatiekaart gebruiken, dan blijft uitwisseling beperkt. De
vertaling hoort onderdeel van het onderwijsontwerp te zijn, en dat is een ontwerpopgave bij de
instelling en geen koppelvlakprobleem.

Het toekomstbeeld dat de groep op 30 september besprak, een student die zoekt op een
vaardigheid, is bewust geen onderdeel van wat nu wordt uitgewisseld.
-->

---

<!-- SECTIE 5 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 5 van 6</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Versionering</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Garik &middot; de scenario's van de leveranciers</div>
</div>

<!--
Sectiescheiding. Dit blok is van Garik en moet met hem worden ingevuld. De slide hierna is de
terugblik uit de notulen; wat de opgehaalde scenario's zeggen vult hij aan.
-->

---

<!-- 16. DRIE RICHTINGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Drie richtingen, elk met een prijs

<div class="np-grid-3" style="margin-top:1.4rem;gap:1rem;">
<div class="np-card"><carbon-document style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Een documentversie</div><small style="color:#2b6b4a;">+ eenvoudig uit te leggen</small><br/><small style="color:#8a4a38;">&minus; iedereen loopt achter</small></div>
<div class="np-card"><carbon-assembly-cluster style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Pakket per koppeling</div><small style="color:#2b6b4a;">+ minder brede impact</small><br/><small style="color:#8a4a38;">&minus; relaties ingewikkelder</small></div>
<div class="np-card accent-orange"><carbon-chemistry style="font-size:1.5rem;color:var(--np-orange);" /><div style="font-weight:600;margin-top:0.3rem;">Modulair, bouwblokken</div><small style="color:#2b6b4a;">+ wijzig alleen wat je gebruikt</small><br/><small style="color:#8a4a38;">&minus; oud naast nieuw onderhouden</small></div>
</div>

<div class="np-card accent-green" style="margin-top:1.4rem;padding:0.75rem 1.1rem;">
<carbon-checkmark-outline style="font-size:1.3rem;color:var(--np-green);vertical-align:-0.2rem;" /> <strong style="color:var(--np-ink);">Conformiteit volgt de bouwblokken die je implementeert</strong>
</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Drie richtingen" en "Conformiteitsgrens". Deze slide
is de terugblik; Garik vult aan met wat de opgehaalde scenario's laten zien.

Bij een globale documentversie zet een kleine wijziging iedereen formeel achter, ook wie de
gewijzigde functionaliteit niet gebruikt. Opsplitsing per koppeling vermindert die impact maar
maakt relaties en versiebeheer ingewikkelder. Modulair geeft de meeste ruimte: nieuwe
bouwblokken komen naast bestaande, dus wie niets nieuws nodig heeft wijzigt niets. De prijs is
dat leveranciers op termijn oude naast nieuwe bouwblokken onderhouden.

In het modulaire voorstel bepaalt niet de documentversie de conformiteit maar de bouwblokken
die een partij werkelijk implementeert; de documentversie blijft een historische verwijzing.

Twee punten die op 30 september bleven liggen: uitfasering, want oude bouwblokken kunnen niet
onbeperkt naast nieuwe blijven bestaan, en zichtbaarheid, want een instelling moet bij een
aanbesteding kunnen vaststellen welke bouwblokken een leverancier ondersteunt. Het voorstel
daarvoor was metadata of een publiek endpoint.

Nog geen besluit. Een hybride blijft open.
-->

---

<!-- 17. DE SCENARIO'S -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de scenario's laten zien

<div class="np-placeholder" style="margin-top:1.8rem;padding:2rem;text-align:center;">
<carbon-edit style="font-size:2rem;color:var(--np-orange);" />
<div style="font-weight:600;font-size:1.1rem;margin-top:0.5rem;color:var(--np-ink);">In te vullen door Garik</div>
<div style="margin-top:0.5rem;font-size:0.92rem;color:var(--np-dark-gray);">De opgehaalde scenario's &middot; het aangepaste voorstel &middot; de vraag van vandaag</div>
</div>

<div class="np-bottomline" style="margin-top:1.6rem;">Zonder scenario's blijft de keuze een inschatting in plaats van een toets.</div>

</div>

<!--
Placeholder. Deze slide hoort door Garik gevuld te worden voordat het deck af is.

Op 30 september is aan de leveranciers gevraagd om concrete scenario's: wanneer is volgens jullie
een nieuwe versie, een nieuwe applicatieservice of een nieuwe berichtenstroom nodig? De termijn
daarvoor liep op 14 oktober af.

Komen er geen scenario's, dan is dat zelf het bericht: dan gaat de keuze tussen de drie
richtingen op basis van aannames, en dat is de moeite waard om hardop te zeggen.
-->

---

<!-- SECTIE 6 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 6 van 6</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Capaciteit en vervolg</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Ruud &middot; de bouwfase in Q1</div>
</div>

<!--
Sectiescheiding. Dit blok is van Ruud. De capaciteitsvraag van 30 september is twee weken over
tijd, en de bouwfase in Q1 hangt eraan.
-->

---

<!-- 18. DE BOUWFASE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De scope raakt meer teams dan een

<div style="display:flex;flex-wrap:wrap;gap:0.55rem;margin-top:1.4rem;max-width:88%;font-size:0.92rem;">
<div class="chip">informatiemodellen</div>
<div class="chip">resultaatstructuren</div>
<div class="chip">opleidingsinrichting</div>
<div class="chip">onderwijslogistiek</div>
<div class="chip">koppelingen</div>
<div class="chip">berichtenstromen</div>
</div>

<div class="np-card accent-orange" style="margin-top:1.8rem;padding:0.9rem 1.2rem;">
<carbon-help style="font-size:1.4rem;color:var(--np-orange);vertical-align:-0.25rem;" /> <strong style="color:var(--np-ink);font-size:1.05rem;">Welke koppelingen wil je in Q1 bouwen?</strong>
</div>

<style scoped>
.chip { background:#EEF1F5; border-radius:999px; padding:0.4rem 0.9rem; }
</style>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Capaciteitsinschatting" en "Programmascope". Dit blok
is van Ruud; ik zet het neer zoals het in de notulen staat zodat hij het kan aanscherpen.

Die onderwerpen raken binnen een leveranciersorganisatie verschillende teams, waardoor de
totale inzet hoger uitvalt dan de acht uur per week die als minimum is genoemd.

Daarom is de vraag niet of een leverancier meedoet, maar welke koppelingen hij in Q1
daadwerkelijk wil bouwen. Deelname aan meerdere koppelvlakken verhoogt de inspanning.
-->

---

<!-- 19. WAT DE PLANNING NODIG HEEFT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de planning nodig heeft

<div class="np-grid-3" style="margin-top:1.5rem;gap:1rem;">
<div class="np-card"><carbon-time style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Hoeveel tijd</div><small>review, modellering, voorbeelden</small></div>
<div class="np-card"><carbon-catalog style="font-size:1.5rem;color:var(--np-blue);" /><div style="font-weight:600;margin-top:0.3rem;">Welke koppelvlakken</div><small>in beeld voor Q1</small></div>
<div class="np-card accent-orange"><carbon-warning-alt style="font-size:1.5rem;color:var(--np-orange);" /><div style="font-weight:600;margin-top:0.3rem;">Waar het niet past</div><small>en waarom</small></div>
</div>

<div class="np-bottomline" style="margin-top:1.7rem;">Een meerjarig programma past niet in een kwartaal. Welke deelstappen wel?</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Bouwfase Q1", "Financiering" en "Gefaseerde aanpak".

De lijn van Ruud: concrete deelstappen en een mogelijk mvp, met een haalbare planning, zonder
toekomstige uitbreidingen onmogelijk te maken.

Aan de financiering voor de bouwfase wordt gewerkt, mogelijk rechtstreeks richting leveranciers
en niet uitsluitend via instellingen. Bedragen en goedkeuring zijn nog niet bekend, en de
financiering hangt mede samen met overeenstemming over de specificaties.

De derde kaart is de belangrijkste: waar het niet past en waarom is bruikbaarder dan een
toezegging die later sneuvelt.
-->

---

<!-- 20. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<div style="margin-top:1.2rem;display:grid;grid-template-columns:7rem 1fr;gap:0.6rem 1rem;align-items:center;max-width:92%;font-size:1rem;">
<div class="et rood">Besluit</div><div><strong>Versioneringsrichting</strong> <small>een van de drie, of hybride</small></div>
<div class="et rood">Besluit</div><div><strong>Koppeling-ID</strong> <small>nu vastleggen of wachten</small></div>
<div class="et oranje">Aanleveren</div><div><strong>Capaciteit en koppelingen voor Q1</strong> <small>twee weken over tijd</small></div>
<div class="et blauw">Review</div><div><strong>De acht fase-pull requests</strong> <small>elk een fase</small></div>
<div class="et groen">Bevestigen</div><div><strong>Dekt het issue jouw opmerking?</strong> <small>bijsturen is waardevoller</small></div>
<div class="et grijs">Kennis</div><div><strong>OEAPI via een submodule</strong> <small>de fork is opgeheven</small></div>
</div>

<style scoped>
.et { border-radius:6px; padding:0.22rem 0; text-align:center; font-size:0.78rem; font-weight:600; color:#fff; }
.et.rood { background:#C4675A; } .et.oranje { background:#E9A27F; } .et.blauw { background:#7A97F2; }
.et.groen { background:#7CCBA8; } .et.grijs { background:#B8BEC7; }
</style>

</div>

<!--
Zes punten. De twee besluiten staan voorop omdat zij blijven liggen: de versioneringsrichting
sinds 15 september, het koppeling-ID sinds 30 september. Dat is geen verwijt, want beide vroegen
input die er nog niet was. Maar de bouwfase in Q1 kan niet wachten op een versioneringsrichting.

De aanlevervraag is de capaciteit. De termijn liep op 14 oktober af, dus die staat nu twee weken
over tijd; zonder die cijfers is de bouwfase niet te plannen.

De reviewvraag is nieuw in deze vorm, want de pull requests zijn nu klein genoeg om per fase te
beoordelen.

De bevestigingsvraag hoort bij deel 2: veertien issues staan op naam van hun inbrenger, en
bijsturen daar levert meer op dan een akkoord.

De vier thema's uit deel 2 komen in de bespreking hierbij.
-->

---

<!-- 21. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div style="margin-top:1.3rem;display:grid;grid-template-columns:auto 1fr;gap:0.75rem 1rem;align-items:center;max-width:84%;font-size:1rem;">
<carbon-chat style="font-size:1.4rem;color:var(--np-blue);" /><div>Reactie op je opmerking: <strong>in jouw issue</strong></div>
<carbon-pull-request style="font-size:1.4rem;color:var(--np-blue);" /><div>Reactie op een fase: <strong>in die pull request</strong></div>
<carbon-time style="font-size:1.4rem;color:var(--np-blue);" /><div>Een review staat <strong>twee weken</strong> open</div>
<carbon-partnership style="font-size:1.4rem;color:var(--np-green);" /><div>Vrijdagsessies en <strong>een-op-eensessies</strong></div>
<carbon-logo-github style="font-size:1.4rem;color:var(--np-blue);" /><div>Nieuw punt: <strong>issue op Npuls-OKx/Public</strong></div>
</div>

<div class="np-bottomline" style="margin-top:1.6rem;">Volgende sessie: nader te bepalen.</div>

</div>

<!--
De datum van de volgende sessie staat bewust open. In de voorbereiding van 5 oktober is
afgesproken dat de een-op-eensessies met leveranciers voorrang krijgen, waar nodig ten koste van
het tempo van de kerngroep. Dat hoort hardop gezegd, anders lijkt het ritme vanzelf te
verwateren.

De sessie van 14 oktober is om die reden vervallen; deze is daarvan de verzette versie.

De een-op-eensessies lopen met Topicus, Kaski, Schedule en Educator. Daar kunnen ook
vertrouwelijke onderwerpen op tafel; wat daaruit komt wordt geabstraheerd tot een uniform model.
-->

---

<!-- 22. PEILING -->
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
Vaste afsluiting van elke sessie, zie meta #205. Het cijfer maakt de lijn over sessies
zichtbaar, de twee open vragen leveren de inhoud.
-->

---

<!-- AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
