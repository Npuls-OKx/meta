---
theme: default
title: "Kerngroep techniek, 14 oktober 2026"
info: "Kerngroep techniek 14 oktober 2026, online: de stand van de vijf punten van 30 september, de voorbeelduitwerking per fase, de scope van het informatiemodel en twee besluiten die blijven liggen."
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
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 14 oktober 2026 &middot; online</div>
</div>

<!--
Online sessie, twee weken na Amersfoort. Opzet nog af te stemmen. Twee van de vijf punten van
30 september zijn niet beslecht, en op de versionering kwam weerstand uit de werkgroep techniek.
Die twee besluiten zijn het doel van vandaag; de voorbeelduitwerking is het bewijs dat er iets
ligt om op te besluiten.
-->

---

<!-- 2. AGENDA -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Agenda

<div style="margin-top:0.6rem;max-width:92%;">
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#B8BEC7;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">1</div><div style="line-height:1.4;"><strong>Afspraken van 30 september</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">Wat OKx zou leveren, wat is gevraagd, en de stand</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#7CCBA8;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">2</div><div style="line-height:1.4;"><strong>Voorbeelduitwerking: van een pull request naar veertien (Niek)</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">Veertien afgebakende pull requests, en de leeruitkomst herschreven</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#7A97F2;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">3</div><div style="line-height:1.4;"><strong>Sectoroverstijgend: wat is mbo, wat is generiek (Niek)</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">De taak van 30 september: wat is mbo, wat geldt breder</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#E9A27F;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">4</div><div style="line-height:1.4;"><strong>Versionering: de scenario's van de leveranciers (Garik)</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">Drie richtingen, en wat de scenario's zeggen</span></div></div>
<div style="display:grid;grid-template-columns:2.2rem 1fr;gap:0.6rem;align-items:start;margin-top:0.55rem;"><div style="width:2rem;height:2rem;border-radius:50%;background:#00AF81;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.95rem;">5</div><div style="line-height:1.4;"><strong>Capaciteit, gevraagd en peiling</strong><br/><span style="font-size:0.9rem;color:var(--np-dark-gray);">De inschatting van 30 september, en de bouwfase in Q1</span></div></div>
</div>

</div>

<!--
Opzet van het kernteam, nog af te stemmen met Garik, Niels en Ruud. Blok 1 is de terugblik en
duurt kort. Blok 2 en 3 zijn van mij, blok 4 van Garik, blok 5 van Ruud. De peiling is de vaste
afsluiting uit meta #205.
-->

---

<!-- SECTIE 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 1 van 5</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Stand van zaken</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; afspraken, voortgang en wat er blijft liggen</div>
</div>

<!--
Sectiescheiding. Terugblik op 30 september: wat er is afgesproken, wat er sindsdien is verzet,
en wat dat zegt over het tempo richting de bouwfase.
-->

---

<!-- 3. AFSPRAKEN: WAT OKX ZOU LEVEREN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Afspraken van 30 september: OKx

<div style="font-size: 0.84rem; line-height: 1.5; margin-top: 0.4rem;">

| Afgesproken | Wie | Stand op 12 oktober |
|---|---|---|
| Kleinere, beter afgebakende pull requests voor het informatiemodel en de voorbeelden | Niek | Gedaan. [PR 252](https://github.com/Npuls-OKx/meta/pull/252) is opgesplitst in veertien, waarvan acht per fase |
| In het informatiemodel zichtbaar maken wat mbo-specifiek is en wat sectoroverstijgend | Niek | Loopt. Drie issues aangemaakt: [#318](https://github.com/Npuls-OKx/meta/issues/318), [#319](https://github.com/Npuls-OKx/meta/issues/319), [#320](https://github.com/Npuls-OKx/meta/issues/320); de minor staat al in fase 1 |
| Voorstel voor een gestandaardiseerde vertaling van kwalificatiedossier naar leeruitkomsten | OKx-team | Loopt. De vijf leeruitkomsten van fase 1 zijn herschreven; de definitie staat als [#315](https://github.com/Npuls-OKx/meta/issues/315), de gelaagdheid als [#316](https://github.com/Npuls-OKx/meta/issues/316) |
| Keuzeregels uitwerken, bruikbaar voor mbo en hbo | OKx-team | Niet opgepakt. [Public PR 6](https://github.com/Npuls-OKx/Public/pull/6) staat op draft |
| Onderwijseenheden koppelen aan meerdere opleidingen | OKx-team | Niet opgepakt |
| Het onderliggende document bij de bouwblok- en versioneringsaanpak publiceren | Garik | [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100) staat nog op draft |

</div>

</div>

<!--
Bron: de notulen van 30 september, kopje "Op te volgen taken". Zes toezeggingen van onze kant.
Twee ervan zijn niet opgepakt, en dat is een keuze geweest: de capaciteit ging naar het
opsplitsen van de voorbeelduitwerking, omdat dat de afspraak was die de review moest
vlottrekken. De keuzeregels en de modulaire koppeling van onderwijseenheden schuiven dus door.
-->

---

<!-- 4. AFSPRAKEN: WAT AAN LEVERANCIERS IS GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd aan leveranciers en instellingen

<div style="font-size: 0.84rem; line-height: 1.5; margin-top: 0.4rem;">

| Gevraagd op 30 september, binnen twee weken | Zichtbaar op 12 oktober |
|---|---|
| **Versioneringsscenario's**: wanneer is volgens jullie een nieuwe versie, service of berichtenstroom nodig | Nog niet in GitHub |
| **Capaciteitsinschatting**: hoeveel tijd voor review, modellering, voorbeelden en uitwerking. Acht uur per week is als minimum genoemd | Nog niet in GitHub |
| **Per open pull request**: akkoord, inhoudelijke input, of meer tijd nodig | [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104) draagt 14 opmerkingen en 8 reviews. De vijf andere open pull requests staan op draft |
| **Validatie**: houd objecttypen, relaties, definities en processtappen tegen de eigen systemen | Opmerkingen van twee leveranciers op PR 104, beide beantwoord |
| **Bouwfase**: welke koppelingen willen jullie in Q1 daadwerkelijk bouwen | Nog niet in GitHub |

</div>

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.8rem;">
Zichtbaar in GitHub is niet hetzelfde als niet geleverd: wat per mail of in een een-op-eensessie is gezegd staat hier niet in.
</div>

</div>

<!--
Bron: de notulen van 30 september. Vijf vragen, alle vijf met een termijn van twee weken, die
vandaag afloopt. Drie ervan zijn in GitHub niet terug te zien. Dat is bewust voorzichtig
geformuleerd: er lopen een-op-eensessies met Topicus, Kaski, Schedule en Educator, en wat daar
is gezegd staat niet in een repository. De vraag aan de zaal is dus eerst: is dit beeld juist?
-->

---

<!-- 5. WAT ER IS VERZET -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er sinds 30 september is verzet

<div style="display:grid;grid-template-columns:7rem repeat(5,1fr);gap:0.5rem 0.6rem;align-items:center;margin-top:0.8rem;max-width:92%;">
<div></div>
<div style="font-size:0.76rem;color:var(--np-mid-gray);text-align:center;">PR gemerged</div>
<div style="font-size:0.76rem;color:var(--np-mid-gray);text-align:center;">PR geopend</div>
<div style="font-size:0.76rem;color:var(--np-mid-gray);text-align:center;">issues gesloten</div>
<div style="font-size:0.76rem;color:var(--np-mid-gray);text-align:center;">issues geopend</div>
<div style="font-size:0.76rem;color:var(--np-mid-gray);text-align:center;">commits op dev</div>
<div style="font-size:0.84rem;font-weight:600;color:var(--np-ink);">Public</div>
<div class="np-getal">1</div><div class="np-getal">1</div><div class="np-getal">0</div><div class="np-getal">1</div><div class="np-getal">2</div>
<div style="font-size:0.84rem;font-weight:600;color:var(--np-ink);">meta</div>
<div class="np-getal">16</div><div class="np-getal">27</div><div class="np-getal">34</div><div class="np-getal">37</div><div class="np-getal">39</div>
</div>

<div style="margin-top: 1rem; font-size: 0.88rem; line-height: 1.55; max-width: 92%;">

Public draagt de artefacten waarmee een leverancier bouwt. Daar sloot in twaalf dagen een pull request, met dode verwijzingen naar de opgeheven fork.

</div>

<div style="font-size: 0.8rem; color: var(--np-mid-gray); margin-top: 0.7rem;">
Stand van 12 oktober, uit GitHub. Aantallen zeggen iets over de hoeveelheid werk, niet over de waarde ervan.
</div>

<style scoped>
.np-getal { background:#fff; border:1px solid var(--np-light-gray); border-radius:8px; padding:0.45rem 0; text-align:center; font-size:1.7rem; font-weight:600; color:var(--np-ink); line-height:1.1; }
</style>

</div>

<!--
Het verschil tussen de twee rijen is de boodschap van dit deel. In meta liep het door; in Public
stond de releaselijn vrijwel stil. Inschatting van de maker, te overrulen: de draft-status is
hier de rem. Vijf van de zes open pull requests in Public staan op draft en vragen formeel geen
review, dus er is weinig om op te sluiten.
-->

---

<!-- 6. WERK PER ONDERWERP -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Werk per onderwerp

<div style="font-size: 0.85rem; line-height: 1.5; margin-top: 0.5rem;">

| Onderwerp | Wat er is gebeurd |
|---|---|
| **Voorbeelduitwerking leerroute 1** | [PR 252](https://github.com/Npuls-OKx/meta/pull/252) gemerged en opgesplitst in veertien; 38 bevindingen uit de reviewronde verantwoord in de bron; de leeruitkomsten van fase 1 herschreven volgens het tuning model |
| **Specificeren op OEAPI** | De fork is op verzoek van de OEAPI-beheerder opgeheven en vervangen door een submodule met een overlay erover ([#270](https://github.com/Npuls-OKx/meta/issues/270)); het werk uit de fork is bewaard |
| **Sectorketen** | Nieuwe plaat met zeven lagen en 52 producten, getekend uit een bron, plus het viewpoint met een besluitpunt ([PR 300](https://github.com/Npuls-OKx/meta/pull/300)). Voor de architectuursync van 3 november |
| **Model bewaakt** | Een controle die het ArchiMate-model bewaakt bij elke wijziging, en een keuringsharnas voor gegenereerde platen |
| **Werkwijze** | Acceptatiecriteria in het issue, een planpoort met onafhankelijke tegenlezing, en een vaste vorm voor elke pull request-beschrijving |

</div>

</div>

<!--
Vijf onderwerpen, in volgorde van wat de kerngroep ervan merkt. De eerste twee raken de
specificatie rechtstreeks. De sectorketen hoort bij de architectuursync en staat hier alleen ter
kennisname. De laatste twee zijn werkplaatsonderhoud: zichtbaar in de cijfers, onzichtbaar in de
specificatie, en de reden dat de aantallen in meta zo hoog liggen.
-->

---

<!-- 7. TWEE AFSPRAKEN DIE AL STAAN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee afspraken die al staan

<div class="np-grid-2" style="margin-top: 1rem; gap: 2rem;">
<div>

### Wat een akkoord betekent

De inhoud is bekeken en de richting wordt gesteund.

Geen verplichting om alles te bouwen.

</div>
<div>

### Hoe lang een review openstaat

Ongeveer twee weken, langer bij een groter onderwerp.

Meer tijd nodig: meld dat. Stilte levert te weinig om op te plannen.

</div>
</div>

<div style="font-size: 0.84rem; color: var(--np-mid-gray); margin-top: 1.4rem;">
Beide vastgesteld op 30 september. Zij beantwoorden de vraag die toen op tafel lag: waar teken je voor.
</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Betekenis van akkoord" en "Reviewtermijn". Ruud
verduidelijkte het eerste, ik het tweede. Dit herhalen loont: de aarzeling om te tekenen kwam
voort uit het idee dat een akkoord een bouwverplichting is, en dat is het niet.
-->

---

<!-- SECTIE 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 2 van 5</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Voorbeelduitwerking</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; van een pull request naar veertien</div>
</div>

<!--
Sectiescheiding. De afspraak van 30 september was: kleinere, beter afgebakende pull requests.
Dit deel laat zien wat dat heeft opgeleverd en waar de review nu op kan aangrijpen.
-->

---

<!-- 8. VAN EEN PR NAAR VEERTIEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van een pull request naar veertien

<div style="margin-top:1rem;max-width:88%;">

<div style="display:grid;grid-template-columns:auto 1fr;gap:0.7rem 1.1rem;align-items:center;font-size:1rem;line-height:1.5;">
<div style="background:#7CCBA8;color:#fff;border-radius:8px;padding:0.5rem 0.9rem;font-weight:700;font-size:1.3rem;">5</div>
<div><strong>over het gereedschap</strong><br/><span style="font-size:0.88rem;color:var(--np-dark-gray);">het contract onder de bron, de controle, de generator, de tekenaar, het kaderscenario</span></div>
<div style="background:#7A97F2;color:#fff;border-radius:8px;padding:0.5rem 0.9rem;font-weight:700;font-size:1.3rem;">8</div>
<div><strong>per fase van de leerroute</strong><br/><span style="font-size:0.88rem;color:var(--np-dark-gray);">elk met de bevindingen van die fase verantwoord</span></div>
<div style="background:#B8BEC7;color:#fff;border-radius:8px;padding:0.5rem 0.9rem;font-weight:700;font-size:1.3rem;">1</div>
<div><strong>leeswijzer bij de bron</strong><br/><span style="font-size:0.88rem;color:var(--np-dark-gray);">zodat een reviewer weet welk bestand hij opent</span></div>
</div>

<div style="font-size:0.9rem;color:var(--np-dark-gray);margin-top:1.3rem;">
Op 30 september lag dit er als een pull request. Te groot om op te reageren, en dat was het bezwaar.
</div>

</div>

</div>

<!--
Dit is de afspraak van 30 september, uitgevoerd. De splitsing is geen cosmetica: een reviewer
kan nu op een fase reageren zonder de andere zeven te hoeven lezen. De eerste van de veertien
is gemerged, de rest gaat op volgorde door.
-->

---

<!-- 8b. WAT EEN FASE-PR DRAAGT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat een fase-pull request draagt

<div class="np-grid-2" style="margin-top:1rem;gap:2rem;align-items:start;">
<div>

<div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:10px;padding:1.1rem 1.2rem;font-size:0.92rem;line-height:1.9;">
<div>De beelden van die fase, uit de bron getekend</div>
<div>De bevindingen van de reviewronde</div>
<div>Het stuk document dat bij die fase hoort</div>
<div>De controle die zegt of de fase compleet is</div>
</div>

</div>
<div>

<div style="font-size:0.92rem;line-height:1.6;">

<strong>38 bevindingen</strong> staan in de bron zelf, elk met het beeld waarop zij slaat, de lezer, de datum en de status.

</div>

<div style="display:flex;gap:0.5rem;margin-top:1rem;font-size:0.84rem;">
<div style="flex:1;background:#DDF3E8;border-radius:8px;padding:0.6rem;text-align:center;">doorgevoerd</div>
<div style="flex:1;background:#FFF4CC;border-radius:8px;padding:0.6rem;text-align:center;">open</div>
<div style="flex:1;background:#F3E4DC;border-radius:8px;padding:0.6rem;text-align:center;">geparkeerd,<br/>met een reden</div>
</div>

</div>
</div>

</div>

<!--
De bevindingen staan in de bron in plaats van in een commitbericht, dus de controle kan nalopen
of een bevinding naar een bestaand beeld wijst en of elk thema bekend is. Een geparkeerde
bevinding draagt verplicht een reden; dat voorkomt dat iets stil verdwijnt.
-->

---

<!-- 9. DE LEERUITKOMST HERSCHREVEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De leeruitkomst, herschreven

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.6rem; align-items: center;">
<div>

<div style="font-size:0.86rem;line-height:1.6;">

De leeruitkomsten in het voorbeeld stonden er als losse zinnen. Zij zijn herschreven langs vijf vaste onderdelen, zodat zij toetsbaar worden:

<div style="margin-top:0.7rem;display:grid;grid-template-columns:auto 1fr;gap:0.35rem 0.7rem;font-size:0.85rem;">
<div style="font-weight:600;color:var(--np-orange);">werkwoord</div><div>wat de student doet</div>
<div style="font-weight:600;color:var(--np-orange);">type</div><div>welke soort beheersing</div>
<div style="font-weight:600;color:var(--np-orange);">onderwerp</div><div>waarover</div>
<div style="font-weight:600;color:var(--np-orange);">standaard</div><div>waaraan het wordt afgemeten</div>
<div style="font-weight:600;color:var(--np-orange);">context</div><div>waar en op welk niveau</div>
</div>

<div style="margin-top:0.8rem;font-size:0.82rem;color:var(--np-dark-gray);">
De standaard draagt wat de instelling belangrijk vindt. Zonder die standaard is een leeruitkomst niet te toetsen, en dus ook niet te vergelijken tussen instellingen.
</div>

</div>

</div>
<div>

<div style="height: 330px; overflow: hidden; display: flex; justify-content: center;">
  <img src="/platen/voorbeeld-f1-03.svg" style="width: 100%; object-fit: cover; object-position: top;" />
</div>

<div style="font-size:0.78rem;color:var(--np-mid-gray);text-align:center;margin-top:0.5rem;">
Fase 1: de leeruitkomsten uit het dossier, in de stem van de instelling
</div>

</div>
</div>

</div>

<!--
Bron: de conventie leeruitkomsten van 6 oktober, het tuning model. Dit raakt de taak van
30 september over de gestandaardiseerde vertaling van kwalificatiedossier naar leeruitkomsten.
De vorm is nu vast; de definitie zelf en de gelaagdheid staan nog open als meta #315 en #316.
Wijs op de standaard: dat is het onderdeel dat in de praktijk het vaakst ontbreekt, en precies
het onderdeel dat uitwisseling tussen instellingen mogelijk maakt.
-->

---

<!-- SECTIE 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 3 van 5</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Sectoroverstijgend</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Niek &middot; wat is mbo, en wat geldt breder</div>
</div>

<!--
Sectiescheiding. De taak van 30 september: maak in het informatiemodel duidelijk welke
onderdelen mbo-specifiek zijn en welke sectoroverstijgend bedoeld zijn.
-->

---

<!-- 10. GENERIEK EN SPECIFIEK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een generiek object, een eigen naam per sector

<div style="margin-top:0.7rem;max-width:94%;">

<div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:10px;padding:1.1rem 1.3rem;font-family:ui-monospace,monospace;font-size:0.84rem;line-height:1.9;">
<div style="color:var(--np-ink);font-weight:600;">Opleidingsprogramma specificatie</div>
<div style="color:var(--np-mid-gray);">&nbsp;&nbsp;&#9492;&#9472; specialisatie</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#00AF81;font-weight:600;">Keuzedeel</span> <span style="color:var(--np-mid-gray);">mbo</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#7A97F2;font-weight:600;">Minor</span> <span style="color:var(--np-mid-gray);">hbo</span></div>
</div>

<div style="font-size:0.88rem;line-height:1.6;margin-top:1rem;">

De plaat modelleert het kiesbare onderwijsprogrammaonderdeel al generiek: hetzelfde patroon loopt door alle vier de lagen, van specificatie via aanbod en verbintenis naar resultaat. Een keuzedeel en een minor erven die structuur en voegen hun eigen regels toe.

Daarmee is een sectorspecifieke term geen apart model, maar een naam op een generiek object. Dat is wat een module tussen instellingen en tussen sectoren uitwisselbaar houdt.

</div>

<div style="font-size:0.82rem;color:var(--np-mid-gray);margin-top:0.9rem;">
Loopt als <a href="https://github.com/Npuls-OKx/meta/issues/318">meta #318</a> met twee deelvragen: de minor expliciet in het model, en het kwalificatiekader neutraal met croho en het hbo-kader erbij.
</div>

</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Sectoroverstijgende opbouw" en "Keuzeregels en
subtypen", plus de review van Luke op Public PR 104. Het punt dat ik hier wil maken: dit stond
al in de plaat, alleen niet expliciet genoeg. De vraag van de leverancier was terecht, en de
uitwerking is nu zichtbaar in fase 1. Wat er nog moet gebeuren is de minor in het model zelf
zetten, en dat vraagt de modelleur in Archi.
-->

---

<!-- 11. DE LEERUITKOMST ALS SLEUTEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De leeruitkomst als sleutel tussen instellingen

<div style="margin-top:0.8rem;max-width:94%;">

<div style="display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:0.8rem;align-items:center;font-size:0.84rem;">
<div style="background:#FFF4CC;border:1px solid #E8D48A;border-radius:10px;padding:0.8rem 0.9rem;line-height:1.45;"><strong>Kwalificatiedossier</strong><br/><span style="color:var(--np-dark-gray);">landelijk, per sector anders ingericht</span></div>
<div style="font-size:1.4rem;color:var(--np-orange);">&rarr;</div>
<div style="background:#E8F0FF;border:1px solid #A9BEF0;border-radius:10px;padding:0.8rem 0.9rem;line-height:1.45;"><strong>Leeruitkomst</strong><br/><span style="color:var(--np-dark-gray);">de tussenlaag, met een standaard erin</span></div>
<div style="font-size:1.4rem;color:var(--np-orange);">&rarr;</div>
<div style="background:#DDF3E8;border:1px solid #96CDB2;border-radius:10px;padding:0.8rem 0.9rem;line-height:1.45;"><strong>Onderwijsspecificatie</strong><br/><span style="color:var(--np-dark-gray);">per instelling, eigen context</span></div>
</div>

<div style="font-size:0.88rem;line-height:1.6;margin-top:1.1rem;">

Zonder die tussenlaag vergelijkt niemand twee onderwijsblokken van verschillende instellingen. Met die laag kan een systeem zoeken welke module een gewenste leeruitkomst draagt, binnen een instelling, tussen instellingen, en op termijn tussen sectoren.

</div>

<div style="font-size:0.82rem;color:var(--np-mid-gray);margin-top:0.9rem;">
De koppeling alleen lost dit niet op: de vertaling hoort bij het onderwijsontwerp.
</div>

</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Herbruikbare leeruitkomsten", "Vertaling naar
leeruitkomsten" en "Huidige beperking". Dit is het toekomstbeeld waar de groep het over had,
en het is bewust geen onderdeel van wat nu wordt uitgewisseld. De eerlijke kanttekening staat
onderaan: dit is een ontwerpopgave bij de instelling, geen koppelvlakprobleem.
-->

---

<!-- SECTIE 4 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 4 van 5</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Versionering</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Garik &middot; de scenario's van de leveranciers</div>
</div>

<!--
Sectiescheiding. Dit blok is van Garik en moet met hem worden ingevuld. De twee slides hierna
zijn de terugblik uit de notulen; wat de opgehaalde scenario's zeggen vult hij aan.
-->

---

<!-- 12. DRIE RICHTINGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Drie richtingen, elk met een prijs

<div style="font-size: 0.85rem; line-height: 1.5; margin-top: 0.5rem;">

| Richting | Wat het oplevert | Wat het kost |
|---|---|---|
| **Een versie voor het hele document** | Eenvoudig te begrijpen en uit te leggen | Een kleine wijziging zet iedereen formeel achter, ook wie de wijziging niet gebruikt |
| **Een pakket per koppeling** | Minder brede impact bij een wijziging | Relaties en versiebeheer tussen de pakketten worden ingewikkelder |
| **Modulair, op bouwblokniveau** | De meeste ruimte: wie niets nieuws nodig heeft, wijzigt niets | Meer bouwblokken, en leveranciers onderhouden op termijn oude naast nieuwe |

</div>

<div style="margin-top: 1rem; font-size: 0.88rem; line-height: 1.6; max-width: 92%;">

In het modulaire voorstel bepaalt niet de documentversie de conformiteit, maar de bouwblokken die een partij werkelijk implementeert. De documentversie blijft een historische verwijzing.

</div>

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 0.8rem;">
Nog geen besluit. Een hybride blijft open: afspraken op een hoger niveau, met modulaire regels voor compatibiliteit eronder.
</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Drie richtingen" en "Conformiteitsgrens". Deze slide
is de terugblik; Garik vult aan met wat de opgehaalde scenario's laten zien. Twee punten die in
de vorige sessie bleven liggen: uitfasering, want oude bouwblokken kunnen niet onbeperkt naast
nieuwe blijven bestaan, en zichtbaarheid, want een instelling moet bij een aanbesteding kunnen
vaststellen welke bouwblokken een leverancier ondersteunt. Het voorstel daarvoor was metadata
of een publiek endpoint.
-->

---

<!-- 13. WAT ER AAN SCENARIO'S IS OPGEHAALD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de scenario's laten zien

<div style="margin-top: 1rem; font-size: 0.9rem; line-height: 1.6; max-width: 90%;">

Op 30 september is aan de leveranciers gevraagd om concrete scenario's: wanneer is volgens jullie een nieuwe versie, een nieuwe applicatieservice of een nieuwe berichtenstroom nodig?

</div>

<div style="margin-top: 1.4rem; padding: 1.2rem 1.4rem; background: #FFF4E8; border: 1px dashed #E9A27F; border-radius: 10px; font-size: 0.9rem; line-height: 1.6; max-width: 90%;">
<strong>In te vullen door Garik.</strong> Hier komen de opgehaalde scenario's, het aangepaste voorstel dat daaruit volgt, en de vraag die vandaag aan de groep voorligt.
</div>

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 1rem;">
Zonder scenario's blijft de keuze tussen de drie richtingen een inschatting in plaats van een toets.
</div>

</div>

<!--
Placeholder. Deze slide hoort door Garik gevuld te worden voordat het deck af is. Komen er geen
scenario's, dan is dat zelf het bericht: dan gaat de keuze over op basis van aannames, en dat is
de moeite waard om hardop te zeggen.
-->

---

<!-- SECTIE 5 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; text-align: right; padding: 3rem 4rem 3rem 45%; z-index: 1;">
  <div style="font-size: 0.8rem; color: var(--np-orange); letter-spacing: 2px; text-transform: uppercase;">Deel 5 van 5</div>
  <h1 style="font-size: 2.4rem; line-height: 1.15; margin: 0.4rem 0 0.5rem; color: var(--np-ink);">Capaciteit en vervolg</h1>
  <div style="font-size: 1rem; color: var(--np-mid-gray);">Ruud &middot; de bouwfase in Q1</div>
</div>

<!--
Sectiescheiding. Dit blok is van Ruud. De capaciteitsvraag van 30 september loopt af vandaag,
en de bouwfase in Q1 hangt eraan.
-->

---

<!-- 14. DE BOUWFASE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De bouwfase vraagt een keuze, geen intekening op alles

<div style="margin-top:1rem;max-width:90%;">

<div style="display:flex;flex-wrap:wrap;gap:0.5rem;font-size:0.86rem;">
<div style="background:#EEF1F5;border-radius:20px;padding:0.4rem 0.9rem;">informatiemodellen</div>
<div style="background:#EEF1F5;border-radius:20px;padding:0.4rem 0.9rem;">resultaatstructuren</div>
<div style="background:#EEF1F5;border-radius:20px;padding:0.4rem 0.9rem;">opleidingsinrichting</div>
<div style="background:#EEF1F5;border-radius:20px;padding:0.4rem 0.9rem;">onderwijslogistiek</div>
<div style="background:#EEF1F5;border-radius:20px;padding:0.4rem 0.9rem;">koppelingen</div>
<div style="background:#EEF1F5;border-radius:20px;padding:0.4rem 0.9rem;">berichtenstromen</div>
</div>

<div style="font-size:1rem;line-height:1.6;margin-top:1.2rem;">

Die onderwerpen raken binnen een leveranciersorganisatie verschillende teams. De inzet valt daarmee hoger uit dan acht uur per week.

</div>

<div style="font-size:1.05rem;line-height:1.5;margin-top:1.1rem;color:var(--np-ink);">
De vraag is dus niet <em>of</em> een leverancier meedoet, maar <strong>welke koppelingen hij in Q1 wil bouwen</strong>.
</div>

</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Capaciteitsinschatting" en "Programmascope". Dit
blok is van Ruud; ik zet het neer zoals het in de notulen staat zodat hij het kan aanscherpen.
-->

---

<!-- 19b. WAT DE PLANNING NODIG HEEFT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de planning nodig heeft

<div class="np-grid-2" style="margin-top:1rem;gap:2rem;align-items:start;">
<div>

<div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:10px;padding:1.1rem 1.2rem;font-size:0.95rem;line-height:1.9;">
<div>Hoeveel tijd voor review, modellering en voorbeelden</div>
<div>Welke koppelvlakken in beeld zijn</div>
<div>Waar het niet past, en waarom</div>
</div>

</div>
<div>

<div style="font-size:0.92rem;line-height:1.6;">

Een meerjarig programma past niet in een kwartaal. De vraag is welke deelstappen er wel in passen, zonder de uitbreiding erna onmogelijk te maken.

</div>

<div style="font-size:0.84rem;color:var(--np-mid-gray);margin-top:1rem;line-height:1.5;">
Aan de financiering wordt gewerkt, mogelijk rechtstreeks richting leveranciers. Bedragen en goedkeuring zijn nog niet bekend.
</div>

</div>
</div>

</div>

<!--
Bron: de notulen van 30 september, kopjes "Bouwfase Q1", "Financiering" en "Gefaseerde
aanpak". De lijn van Ruud: deelstappen en een mogelijk mvp in plaats van alles tegelijk.
-->

---

<!-- 15. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<div style="margin-top:0.7rem;max-width:94%;font-size:0.88rem;line-height:1.55;">

<div style="display:grid;grid-template-columns:6.5rem 1fr;gap:0.55rem 0.9rem;align-items:start;">
<div style="background:#C4675A;color:#fff;border-radius:6px;padding:0.2rem 0;text-align:center;font-size:0.78rem;font-weight:600;">Besluit</div>
<div><strong>De versioneringsrichting</strong>: een van de drie, of de hybride. Dit staat sinds 15 september open en blokkeert de opbouw van de specificatiepakketten</div>

<div style="background:#C4675A;color:#fff;border-radius:6px;padding:0.2rem 0;text-align:center;font-size:0.78rem;font-weight:600;">Besluit</div>
<div><strong>Het koppeling-ID</strong>: nu een eerste indeling vastleggen als werkafspraak, of wachten tot de bouwstenen scherper zijn (<a href="https://github.com/Npuls-OKx/Public/issues/107">Public #107</a>)</div>

<div style="background:#E9A27F;color:#fff;border-radius:6px;padding:0.2rem 0;text-align:center;font-size:0.78rem;font-weight:600;">Aanleveren</div>
<div><strong>De capaciteitsinschatting en de koppelingen voor Q1</strong>. De termijn van twee weken loopt vandaag af; zonder die cijfers is de bouwfase niet te plannen</div>

<div style="background:#7A97F2;color:#fff;border-radius:6px;padding:0.2rem 0;text-align:center;font-size:0.78rem;font-weight:600;">Review</div>
<div><strong>De acht fase-pull requests</strong>, elk afgebakend tot een fase van de leerroute. Dit is de afspraak van 30 september, uitgevoerd</div>

<div style="background:#B8BEC7;color:#fff;border-radius:6px;padding:0.2rem 0;text-align:center;font-size:0.78rem;font-weight:600;">Kennis</div>
<div>De fork van de OEAPI-specificatie is opgeheven; OKx specificeert erbovenop via een submodule met een overlay</div>
</div>

</div>

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-top: 1rem;">
Twee besluiten, en beide stonden ook op 30 september op de lijst.
</div>

</div>

<!--
Vijf punten. De twee besluiten staan voorop omdat zij blijven liggen: de versionering sinds
15 september, het koppeling-ID sinds 30 september. Dat is geen verwijt, want beide vroegen
input die er nog niet was. Maar de bouwfase in Q1 kan niet wachten op een versioneringsrichting.
De aanlevervraag is de capaciteit: de termijn loopt vandaag af. De reviewvraag is nieuw in deze
vorm, want de pull requests zijn nu klein genoeg om per fase te beoordelen.
-->

---

<!-- 16. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div style="margin-top:0.9rem;max-width:92%;font-size:0.92rem;line-height:1.8;">

Reacties op de voorbeelduitwerking: in de pull request van de fase waar het over gaat

Opmerkingen op <a href="https://github.com/Npuls-OKx/Public/pull/104">Public PR 104</a>: in de pull request. Die blijft open tot de reacties binnen zijn

Een pull request staat ongeveer twee weken open. Meer tijd nodig: meld dat, dan past de planning zich aan

Vrijdagsessies en een-op-eensessies blijven beschikbaar om modellen en vragen door te nemen

Nieuw punt: als issue op <a href="https://github.com/Npuls-OKx/Public/issues">github.com/Npuls-OKx/Public</a>

</div>

<div style="font-size: 0.84rem; color: var(--np-mid-gray); margin-top: 1.3rem;">
Volgende sessie: nader te bepalen. De een-op-eensessies met leveranciers lopen door en kunnen het ritme van de kerngroep beinvloeden.
</div>

</div>

<!--
De datum van de volgende sessie staat bewust open: in de voorbereiding van 5 oktober is
afgesproken dat de een-op-eensessies voorrang krijgen, waar nodig ten koste van het tempo van de
kerngroep. Dat hoort hardop gezegd, anders lijkt het ritme vanzelf te verwateren.
-->

---

<!-- 17. PEILING -->
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
