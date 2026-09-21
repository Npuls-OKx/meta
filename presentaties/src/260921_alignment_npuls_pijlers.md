---
theme: default
title: "OKx in samenhang met AII, eduXchange en het ontsluiten van onderwijsaanbod"
info: "Overleg LZD 21 september 2026: de status van OKx, waar OKx andere ontwikkelingen raakt en hoe wij elkaar op de hoogte houden."
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
  <h1 style="font-size: 2.8rem; line-height: 1.15; margin-bottom: 0.8rem; color: var(--np-ink);">OKx in samenhang</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 38rem;">AII spoor 3 &middot; eduXchange &middot; ontsluiten onderwijsaanbod &middot; OKx: wat is de status, waar raken wij elkaar, hoe houden wij elkaar op de hoogte</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">Leren zonder Drempels &middot; 21 september 2026</div>
</div>

<!--
Hans opent. Doel van de sessie is alignment: waar werkt iedereen aan, waar raken wij elkaar,
welke vervolgafspraken. OKx loopt op onderdelen vooruit en zoekt aansluiting op wat buiten de
instelling gebeurt; dat mag hardop. Niek presenteert, Garik vult aan.
-->

---

<!-- 2. AGENDA: DE DRIE VRAGEN VAN HANS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="margin-left: 42%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding-right: 3rem;">
  <p class="eyebrow">Agenda</p>
  <h1 style="font-size: 2rem !important; margin-bottom: 1.1rem;">Drie vragen</h1>
  <div style="display: flex; flex-direction: column; gap: 0.95rem;">
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">1</span>
      <div><strong>Wat is (de status van) OKx?</strong><br/><span class="muted" style="font-size: 0.82rem;">aanpak, focus binnen de instelling, waar de specificaties en het informatiemodel staan</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>Waar raakt OKx andere ontwikkelingen wel, en welke niet?</strong><br/><span class="muted" style="font-size: 0.82rem;">twee uitgangspunten als schot voor de boeg; AII, eduXchange, catalogus, EduID</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Hoe houden wij elkaar op de hoogte?</strong><br/><span class="muted" style="font-size: 0.82rem;">gaten en onnodige overlap voorkomen; vervolgafspraken</span></div>
    </div>
  </div>
  <div class="np-card" style="margin-top: 1.1rem; font-size: 0.85rem; padding: 0.5rem 0.9rem;">
    Doel vandaag: aftasten waar ieder staat en waar het schuurt, en daar afspraken van maken.
  </div>
</div>

<!--
De agenda van Hans, letterlijk. Uit de voorbereiding van vanochtend: orienterend, op
hoofdlijnen zenden, wrijvingspunten benoemen en vervolgafspraken maken. Ashwin vraagt voor
vraag 2 een concreet schot voor de boeg: dat zijn de twee uitgangspunten van Hans en de
raakvlakkenslide.
-->

---

<!-- 3. AANPAK: VAN REIS NAAR SPECIFICATIE (visueel) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aanpak: van reis naar specificatie

<div class="np-pipeline" style="margin-top: 1.4rem;">
  <div class="np-step blue" style="flex: 1;">
    <carbon-map style="font-size: 2rem; color: var(--np-blue);" />
    <strong style="font-size: 0.88rem;">Negen leerroutes</strong>
    <small>per leerroute een kaderscenario: studentreis en instellingsreis samen</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step orange" style="flex: 1;">
    <carbon-user-multiple style="font-size: 2rem; color: var(--np-orange);" />
    <strong style="font-size: 0.88rem;">Koploperscholen</strong>
    <small>user stories uit de praktijk, in de PoC</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1;">
    <carbon-assembly-cluster style="font-size: 2rem; color: var(--np-green);" />
    <strong style="font-size: 0.88rem;">Modulaire bouwstenen</strong>
    <small>generieke stories, herleidbaar naar de leerroutes</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue" style="flex: 1;">
    <carbon-document style="font-size: 2rem; color: var(--np-blue);" />
    <strong style="font-size: 0.88rem;">Specificaties</strong>
    <small>techniekagnostisch, modulair uit bouwblokken, openbaar in GitHub</small>
  </div>
</div>

<div class="np-grid-2" style="margin-top: 1.4rem; align-items: start; gap: 1.2rem;">
  <div class="np-card accent-orange" style="font-size: 0.9rem; line-height: 1.55; padding: 0.6rem 1rem;">
    <strong>Leerroutes 1 tot 3 eerst</strong>, mbo eerst. De reis van de student en die van de instelling bepalen samen wat er wanneer tussen systemen beweegt.
  </div>
  <div class="np-card accent-green" style="font-size: 0.9rem; line-height: 1.55; padding: 0.6rem 1rem;">
    <strong>OKx specificeert het koppelvlak</strong>; de applicatie is van de leverancier. Elke eis is terug te volgen naar de story waar hij uit komt.
  </div>
</div>

</div>

<!--
Twee zinnen over de specificatiedocumenten volstaan (voorbereiding): modulaire aanpak met
bouwblokken (koppelingen, applicatiediensten, interactiepatronen, datamodellen), openbaar en
herleidbaar in Npuls-OKx/Public. De leerroutes en kaderscenario's staan daar ook; leerroute 1
is uitgewerkt met persona Jochem, Apothekersassistent BOL, cohort 2026, in acht fasen.
De schets van Niels op de volgende slide laat de lagen zien.
-->

---

<!-- 4. PLAAT: SCHETS VAN NIELS -->
<div style="position: absolute; inset: 0; background: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1rem 1.5rem 0.6rem;">
  <img src="/platen/concept-uitleg-business-architectuur.png" style="max-width: 100%; max-height: 92%; object-fit: contain;" />
  <div style="font-size: 0.8rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Van de PoC-school (links) via het gedeelde perspectief naar de OKx-architectuur met de kerngroep techniek (rechts). Schets van Niels, concept.</div>
</div>

<!--
Links het PoC-schoolperspectief: user stories van de applicatie, app-dienst, sectordienst.
Midden het gedeelde perspectief: leerroutes, studentreis en instellingsreis, user stories OKx,
generieke stories en bouwstenen. Rechts de OKx-architectuur met de kerngroep techniek:
features, koppelvlakdienst, koppeling, endpoints, interactie, informatiemodel. Een story die
applicatiefunctionaliteit beschrijft is de aanloop; het product is de koppelvlakspecificatie.
-->

---

<!-- 5. INSTELLINGSPERSPECTIEF: HET ECOSYSTEEM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Het instellingsperspectief: een ecosysteem van koppelingen

<p class="eyebrow" style="margin-top:0.6rem;">Binnen de deur</p>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:0.6rem;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-catalog style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Onderwijscatalogus</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-calendar style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Planning en rooster</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-user-favorite style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Studentkeuze</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-data-base style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Kernregistratie</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-chart-line style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Studentvolgsysteem</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-education style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">LMS</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-task-complete style="font-size:2rem;color:var(--np-blue);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Examinering</span></div>
</div>

<p class="eyebrow" style="margin-top:0.9rem;color:var(--np-orange);">Aan de rand van de plaat</p>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:0.6rem;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-building style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">RIO</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-user-follow style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Centraal aanmelden, AII</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-user-identification style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">IAM, identity provisioning</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-network-3 style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">EduHub</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-chat style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Communicatie</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-analytics style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">Business intelligence</span></div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.3rem;background:#fff;border:1px solid var(--np-light-gray);border-radius:12px;padding:0.6rem 0.4rem;text-align:center;"><carbon-machine-learning-model style="font-size:2rem;color:var(--np-orange);" /><span style="font-size:0.78rem;font-weight:600;color:var(--np-ink);line-height:1.2;">AI</span></div>
</div>

<div class="np-card accent-green" style="margin-top: 1rem; font-size: 1rem; line-height: 1.5; padding: 0.6rem 1.1rem;">
<carbon-checkmark-filled style="font-size:1.3rem;color:var(--np-green);vertical-align:-0.25rem;" /> Het overzicht van het instellingsperspectief staat. Daarin zien wij de raakvlakken.
</div>

</div>

<!--
Niels licht de plaat toe (volgende slide). Binnen de deur: de catalogus als spil, de pijlen
ertussen zijn de koppelingen die OKx specificeert. Aan de rand raken de andere pijlers: RIO,
CAMBO en straks AII, IAM met identity provisioning, EduHub, communicatiesystemen, business
intelligence, AI. De raakvlakken zelf komen na de plaat.
-->

---

<!-- 6. PLAAT: HOOFDPLAAT 1.7 -->
<div style="position: absolute; inset: 0; background: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1rem 1.5rem 0.6rem;">
  <img src="/platen/hoofdplaat-1.7.jpg" style="max-width: 100%; max-height: 92%; object-fit: contain;" />
  <div style="font-size: 0.8rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Hoofdplaat informatiestromen v1.7: de referentiecomponenten binnen de instelling en de informatiestromen ertussen. Richtinggevend; draagt nog de aanduiding concept.</div>
</div>

<!--
De plaat alleen als grens aanwijzen: alles binnen het kader is OKx, de pijlen naar buiten zijn
de raakvlakken. De koppelingen die nu gespecificeerd zijn: catalogus naar planning en rooster,
catalogus naar SIS, catalogus naar LMS.
-->

---

<!-- 7. RAAKVLAKKEN OP DE PLAAT (steekwoorden) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar OKx andere ontwikkelingen raakt

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.8rem;margin-top:0.5rem;">
  <div class="np-card accent-blue" style="padding:0.6rem 0.8rem;font-size:0.84rem;line-height:1.45;">
    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;"><carbon-user-follow style="font-size:1.8rem;color:var(--np-blue);" /><strong>AII spoor 3</strong></div>
    <ul style="margin:0;padding-left:1.1rem;"><li>aanmelden, intekenen, inschrijven</li><li>aanmeldbaar aanbod ontsluiten</li><li>aanmelding terug naar kernregistratie</li></ul>
  </div>
  <div class="np-card accent-orange" style="padding:0.6rem 0.8rem;font-size:0.84rem;line-height:1.45;">
    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;"><carbon-network-3 style="font-size:1.8rem;color:var(--np-orange);" /><strong>eduXchange en EduHub</strong></div>
    <ul style="margin:0;padding-left:1.1rem;"><li>keuzedeel over instellingen heen</li><li>aanbod en verbintenis</li><li>een gedeeld model</li></ul>
  </div>
  <div class="np-card accent-green" style="padding:0.6rem 0.8rem;font-size:0.84rem;line-height:1.45;">
    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;"><carbon-catalog style="font-size:1.8rem;color:var(--np-green);" /><strong>Onderwijscatalogus</strong></div>
    <ul style="margin:0;padding-left:1.1rem;"><li>de spil in het web</li><li>gedeelde uitgangspunten</li><li>hetzelfde informatiemodel</li></ul>
  </div>
  <div class="np-card accent-pink" style="padding:0.6rem 0.8rem;font-size:0.84rem;line-height:1.45;">
    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;"><carbon-user-identification style="font-size:1.8rem;color:var(--np-pink);" /><strong>EduID, identity provisioning</strong></div>
    <ul style="margin:0;padding-left:1.1rem;"><li>de student in de keten</li><li>van aanmelding tot toegang</li><li>wie is leidend</li></ul>
  </div>
  <div class="np-card accent-yellow" style="padding:0.6rem 0.8rem;font-size:0.84rem;line-height:1.45;">
    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;"><mdi-key-variant style="font-size:1.8rem;color:var(--np-yellow);" /><strong>Leeruitkomsten</strong></div>
    <ul style="margin:0;padding-left:1.1rem;"><li>de sleutel in het model</li><li>gestandaardiseerd over de pijlers</li><li>LUK-definities</li></ul>
  </div>
  <div class="np-card accent-blue" style="padding:0.6rem 0.8rem;font-size:0.84rem;line-height:1.45;">
    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;"><carbon-machine-learning-model style="font-size:1.8rem;color:var(--np-blue);" /><strong>Toekomstige wijzigingen, zoals AI</strong></div>
    <ul style="margin:0;padding-left:1.1rem;"><li>modulair en versiebeheerd</li><li>nieuwe eisen landen als bouwsteen</li><li>gesprek te plannen</li></ul>
  </div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:0.8rem;">
  <div style="display:flex;align-items:center;gap:0.7rem;background:#E6F7F0;border-radius:12px;padding:0.5rem 0.9rem;font-size:0.84rem;">
    <carbon-building style="font-size:1.6rem;color:var(--np-green);flex-shrink:0;" />
    <div><strong>OKx</strong> &middot; koppelingen, informatiemodel, eisen &middot; nu binnen de instelling, straks over instellingen heen</div>
  </div>
  <div style="display:flex;align-items:center;gap:0.7rem;background:#EEF2FF;border-radius:12px;padding:0.5rem 0.9rem;font-size:0.84rem;">
    <carbon-partnership style="font-size:1.6rem;color:var(--np-blue);flex-shrink:0;" />
    <div><strong>De grens</strong> &middot; applicatie: leverancier &middot; les en didactiek: instelling, vastgelegd in de specificatie &middot; voorzieningen: eigen pijler</div>
  </div>
</div>

</div>

<!--
Geen uitputtende lijst; de punten die op de plaat zichtbaar zijn. De onderwijscatalogus is de
spil in het web en verspreidt haar inhoud door de keten: daar horen gedeelde uitgangspunten en
hetzelfde informatiemodel bij. De didactiek is van de instelling (in een studio, veel of weinig
theorie, alles mag), maar de manier waarop dat in de specificatie wordt vastgelegd, met de
leeruitkomsten erin, is waar de afspraken over gaan; anders is het niet uitwisselbaar.
AI: de OKx-aanpak is modulair en versiebeheerd, zodat nieuwe eisen als bouwsteen landen;
Niels heeft documentatie over AI ontvangen, gesprek te plannen. Federatie gefaseerd: ADR 0008.
-->

---

<!-- 8. TWEE UITGANGSPUNTEN ALS SCHOT VOOR DE BOEG (visueel) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee uitgangspunten die verder reiken dan OKx

<div class="np-grid-2" style="margin-top: 0.3rem; gap: 1.2rem; align-items: start;">
<div class="np-card accent-blue" style="padding:0.6rem 0.9rem;">
<div style="display:flex;align-items:center;gap:0.6rem;"><carbon-tree-view-alt style="font-size:1.8rem;color:var(--np-blue);" /><strong style="font-size:1rem;">1. Kiezen door lerenden: tot en met het leeronderdeel</strong></div>
<div style="font-size:0.8rem;line-height:1.4;margin-top:0.4rem;color:var(--np-dark-gray);">De gelaagdheid van het OKx-informatiemodel; kiezen en uitwisselen gaan tot en met het leeronderdeel.</div>
<div style="display:flex;flex-direction:column;gap:0.2rem;margin-top:0.4rem;">
  <div style="display:flex;align-items:center;gap:0.5rem;background:#EEF2FF;border-radius:8px;padding:0.22rem 0.6rem;margin-left:0rem;font-size:0.8rem;"><span class="np-num" style="width:1.35rem;height:1.35rem;font-size:0.7rem;">1</span><div><strong>Opleidingsspecificatie</strong> <span class="muted">&middot; de opleiding, met haar programma's</span></div></div>
  <div style="display:flex;align-items:center;gap:0.5rem;background:#EEF2FF;border-radius:8px;padding:0.22rem 0.6rem;margin-left:0.8rem;font-size:0.8rem;"><span class="np-num" style="width:1.35rem;height:1.35rem;font-size:0.7rem;">2</span><div><strong>Opleidingsprogrammaspecificatie</strong> <span class="muted">&middot; een leerweg, met keuzedeelruimte</span></div></div>
  <div style="display:flex;align-items:center;gap:0.5rem;background:#FFF1E8;border-radius:8px;padding:0.22rem 0.6rem;margin-left:1.6rem;font-size:0.8rem;"><span class="np-num" style="width:1.35rem;height:1.35rem;font-size:0.7rem;background:var(--np-orange);">3</span><div><strong>Onderwijseenheidspecificatie</strong> <span class="muted">&middot; het blok, verbonden aan de kerntaak</span></div></div>
  <div style="display:flex;align-items:center;gap:0.5rem;background:#E6F7F0;border-radius:8px;padding:0.22rem 0.6rem;margin-left:2.4rem;font-size:0.8rem;"><span class="np-num" style="width:1.35rem;height:1.35rem;font-size:0.7rem;background:var(--np-green);">4</span><div><strong>Leeronderdeelspecificatie</strong> <span class="muted">&middot; de leeractiviteit; als aanbod de leergelegenheid</span></div></div>
  <div style="display:flex;align-items:center;gap:0.5rem;border:1px dashed var(--np-mid-gray);border-radius:8px;padding:0.22rem 0.6rem;margin-left:3.2rem;color:var(--np-dark-gray);font-size:0.8rem;"><carbon-home style="font-size:1.1rem;color:var(--np-mid-gray);" /><div><strong>Lesspecificatie</strong></div></div>
</div>
</div>
<div class="np-card accent-green" style="padding:0.8rem 1rem;">
<div style="display:flex;align-items:center;gap:0.6rem;"><mdi-key-variant style="font-size:1.8rem;color:var(--np-green);" /><strong style="font-size:1rem;">2. Leeruitkomsten als ordenend principe</strong></div>
<svg width="100%" viewBox="0 0 400 150" style="display:block;margin:0.4rem 0 0.1rem;max-height:9.5rem;"><rect x="140" y="52" width="120" height="46" rx="10" fill="#00AF81"/><text x="200" y="72" text-anchor="middle" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">Leeruitkomst</text><text x="200" y="88" text-anchor="middle" fill="#F0FFF8" style="font-size:9px;font-family:inherit">LUK, definities 3 juni</text><rect x="6" y="6" width="112" height="36" rx="8" fill="#fff" stroke="#7A97F2" stroke-width="2"/><text x="62" y="28" text-anchor="middle" fill="#1B1B2F" style="font-size:10px;font-weight:700;font-family:inherit">Kwalificatiedossier</text><rect x="282" y="6" width="112" height="36" rx="8" fill="#fff" stroke="#7A97F2" stroke-width="2"/><text x="338" y="28" text-anchor="middle" fill="#1B1B2F" style="font-size:10px;font-weight:700;font-family:inherit">Specificatie</text><rect x="6" y="108" width="112" height="36" rx="8" fill="#fff" stroke="#E9A27F" stroke-width="2"/><text x="62" y="130" text-anchor="middle" fill="#1B1B2F" style="font-size:10px;font-weight:700;font-family:inherit">Toets en examen</text><rect x="282" y="108" width="112" height="36" rx="8" fill="#fff" stroke="#E9A27F" stroke-width="2"/><text x="338" y="130" text-anchor="middle" fill="#1B1B2F" style="font-size:10px;font-weight:700;font-family:inherit">Resultaatstructuur</text><line x1="118" y1="30" x2="140" y2="60" stroke="#6B7280" stroke-width="1.6"/><line x1="282" y1="30" x2="260" y2="60" stroke="#6B7280" stroke-width="1.6"/><line x1="118" y1="120" x2="140" y2="90" stroke="#6B7280" stroke-width="1.6"/><line x1="282" y1="120" x2="260" y2="90" stroke="#6B7280" stroke-width="1.6"/></svg>
<div style="font-size:0.84rem;line-height:1.5;margin-top:0.3rem;color:var(--np-dark-gray);">
De leeruitkomst is de sleutel: het dossier wordt erin vertaald, specificaties, toetsen en de resultaatstructuur verwijzen ernaar. De instelling vult haar in vanuit haar eigen onderwijskundig kader.
</div>
</div>
</div>

<div class="np-card accent-orange" style="margin-top: 0.5rem; font-size: 0.88rem; line-height: 1.45; padding: 0.45rem 1rem;">
<strong>De vraag aan de tafel:</strong> maken andere ontwikkelingen binnen LZD dezelfde keuzes? Dan weten wij dat liever nu dan bij de oplevering van de keten.
</div>

</div>

<!--
De twee voorbeelden uit de mail van Hans als uitgangspunt, in de termen van het
OKx-referentiekader: de gelaagdheid opleiding, opleidingsprogramma, onderwijseenheid,
leeronderdeel (specificatie) en leergelegenheid (aanbod). Hans noemt het opleiding,
opleidingsonderdeel en leeractiviteit; het begrippenkader van OKx is leidend, zodat de tafel
met ons begrippenkader gaat associeren. De les staat op de plaat buiten de uitwisseling en
blijft van de instelling. LUK: definities zoals besproken op de LUK-dag van 3 juni bij de MBO
Raad in Woerden, wetend dat die nog bewegen. Dit is het schot voor de boeg dat Ashwin vraagt.
-->

---

<!-- 9. INFORMATIEMODEL: ZEVEN BEGRIPPEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Informatiemodel: zeven begrippen delen de keten in

<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:1.4rem;align-items:start;margin-top:0.4rem;">
<div style="font-size: 0.86rem; line-height: 1.55;">

| Begrip | Beantwoordt de vraag |
|---|---|
| Kwalificatiekader mbo | Wat is normatief geldig |
| Onderwijskundig kader instelling | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Wat wordt georganiseerd |
| Onderwijsaanbod | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat is er behaald |
| Resultaatstructuur | Hoe telt dat op tot een uitspraak over de kwalificatie |

</div>
<div style="display:flex;flex-direction:column;gap:0.8rem;">
  <div class="np-card accent-blue" style="font-size:0.86rem;line-height:1.5;padding:0.6rem 0.9rem;">
    <carbon-data-base style="font-size:1.3rem;color:var(--np-blue);vertical-align:-0.25rem;" /> <strong>Conceptueel</strong> (MIM 1 en 2): begrippen, objecttypen en relaties. De plaat op de volgende slide; op de sessie live erbij.
  </div>
  <div class="np-card accent-green" style="font-size:0.86rem;line-height:1.5;padding:0.6rem 0.9rem;">
    <carbon-arrows-horizontal style="font-size:1.3rem;color:var(--np-green);vertical-align:-0.25rem;" /> <strong>Gemapt op OEAPI v6</strong>: daar is de aansluiting met de landelijke standaard redelijk te pakken.
  </div>
  <div class="np-card accent-orange" style="font-size:0.86rem;line-height:1.5;padding:0.6rem 0.9rem;">
    <carbon-catalog style="font-size:1.3rem;color:var(--np-orange);vertical-align:-0.25rem;" /> <strong>Onderwijs Catalogus</strong>: hetzelfde functionele gebied als eduXchange en het ontsluiten van aanbod; dezelfde definities en gegevenssets zijn de inzet.
  </div>
</div>
</div>

</div>

<!--
Overgenomen uit het deck van 15 september. Het model is de aanzet tot het conceptueel
informatiemodel; de begrippen staan in het begrippenkader en de begrippenlijst. Voorbeeld uit
de voorbereiding: eduXchange moesten wij uitleggen hoe een keuzedeel in het model hoort.
-->

---

<!-- 10. PLAAT: INFORMATIEMODEL V0.1 -->
<div style="position: absolute; inset: 0; background: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1rem 1.5rem 0.6rem;">
  <img src="/platen/informatiemodel-v0.1.jpg" style="max-width: 100%; max-height: 92%; object-fit: contain;" />
  <div style="font-size: 0.8rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Informatiemodel OKx v0.1: zeven kolommen, een per begrippenfamilie, met de objecttypen en hun relaties. Concept, ter review bij de kerngroep techniek.</div>
</div>

<!--
Op de sessie inzoomen in de browser. Wijs de kolommen aan, van kwalificatiekader links tot
resultaatstructuur rechts; de leeruitkomst zit in de tweede kolom en is de sleutel waar de
andere kolommen naar verwijzen.
-->

---

<!-- 11. AII EN OKX: AANMELDEN, INTEKENEN, INSCHRIJVEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar wij elkaar raken: aanmelden, intekenen, inschrijven

<div style="font-size: 0.9rem; line-height: 1.5; margin-top: 0.2rem;">
OKx onderscheidt de <code>Intekening op specificatie</code>, de <code>Aanmelding</code> en de <code>Inschrijving</code>, en laat aanbod rijpen in fasen. AII hanteert de volgorde aanmelden, intekenen, inschrijven. Wat verstaan wij elk onder intekenen?
</div>

<svg width="100%" viewBox="0 0 940 250" style="display:block;margin:0.5rem 0 0.1rem;"><rect x="10" y="34" width="190" height="78" rx="8" fill="#FFFFFF" stroke="#7A97F2" stroke-width="2"/><text x="105.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Specificatie</text><text x="105.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">het ontwerp,</text><text x="105.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">los van wanneer</text><text x="580" y="20" text-anchor="middle" fill="#6B7280" style="font-size:11px;letter-spacing:1px;font-family:inherit">ONDERWIJSAANBOD, STEEDS RIJPER</text><line x1="240" y1="26" x2="920" y2="26" stroke="#6B7280" stroke-width="1"/><rect x="240" y="34" width="210" height="78" rx="8" fill="#E6F7F0" stroke="#00AF81" stroke-width="2"/><text x="345.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Intentie</text><text x="345.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">we gaan dit aanbieden;</text><text x="345.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">gaat door bij voldoende vraag</text><rect x="475" y="34" width="210" height="78" rx="8" fill="#B3E8D3" stroke="#00AF81" stroke-width="2"/><text x="580.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Grofmazig gepland</text><text x="580.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">periode en start, gebouw,</text><text x="580.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">misschien al een docent</text><rect x="710" y="34" width="210" height="78" rx="8" fill="#00AF81" stroke="#00AF81" stroke-width="2"/><text x="815.0" y="58" text-anchor="middle" fill="#FFFFFF" style="font-size:14px;font-weight:700;font-family:inherit">Geroosterd</text><text x="815.0" y="78" text-anchor="middle" fill="#F0FFF8" style="font-size:11px;font-family:inherit">dag, tijd, lokaal, docent,</text><text x="815.0" y="93" text-anchor="middle" fill="#F0FFF8" style="font-size:11px;font-family:inherit">groep</text><line x1="202" y1="73" x2="236" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="236,68 242,73 236,78" fill="#6B7280"/><line x1="452" y1="73" x2="486" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="486,68 492,73 486,78" fill="#6B7280"/><line x1="687" y1="73" x2="721" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="721,68 727,73 721,78" fill="#6B7280"/><rect x="10" y="130" width="190" height="26" rx="13" fill="#7A97F2"/><text x="24" y="147" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">intekenen: op de specificatie</text><rect x="240" y="172" width="680" height="26" rx="13" fill="#3DB88F"/><text x="254" y="189" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">aanmelden: op aanbod, in elke fase van rijpheid</text><rect x="710" y="214" width="210" height="26" rx="13" fill="#E9A27F"/><text x="724" y="231" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">inschrijven: op geroosterd</text><circle cx="904" cy="227" r="11" fill="#fff"/><text x="904" y="232" text-anchor="middle" fill="#E9A27F" style="font-size:15px;font-weight:700;font-family:inherit">?</text><path d="M200 143 C 225 143, 225 185, 238 185" fill="none" stroke="#6B7280" stroke-width="2"/><polygon points="236,180 244,185 236,190" fill="#6B7280"/><text x="222" y="167" text-anchor="middle" fill="#6B7280" style="font-size:10px;font-family:inherit">bevestiging</text><line x1="815" y1="198" x2="815" y2="212" stroke="#6B7280" stroke-width="2"/><polygon points="810,210 815,216 820,210" fill="#6B7280"/></svg>

<div class="np-card accent-orange" style="margin-top: 0.6rem; font-size: 0.92rem; line-height: 1.5; padding: 0.6rem 1rem;">
<strong>Vraag aan AII:</strong> intekenen op een specificatie (er is nog geen aanbod) is wat koploperscholen ons vragen; bij leveranciers is het nieuw. Zien wij hetzelfde, of noemen wij twee dingen hetzelfde?
</div>

</div>

<!--
Overgenomen uit het deck van 15 september (positionering intekenen, aanmelden, inschrijven).
Uit de voorbereiding: wij hebben met scholen gesproken over intekenen op specificatie; AII lijkt
de begrippen anders te interpreteren. Vandaag vaststellen dat het een raakvlak is en een
afspraak maken. Verbonden vraag: wie ontsluit het aanmeldbare aanbod aan AII, de catalogus of
de kernregistratie, en hoe komt de aanmelding met verbintenissen terug.
-->

---

<!-- 12. OP DE HOOGTE BLIJVEN, EN DE AFSPRAKEN VAN VANDAAG (visueel) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Op de hoogte blijven, en de afspraken van vandaag

<div style="display:grid;grid-template-columns:1fr 1.3fr;gap:1.3rem;align-items:start;margin-top:0.4rem;">
<div class="np-card accent-blue" style="padding:0.7rem 1rem;font-size:0.86rem;line-height:1.5;">
<strong>Wat OKx aanbiedt</strong>
<div style="display:flex;flex-direction:column;gap:0.55rem;margin-top:0.6rem;">
  <div style="display:flex;align-items:flex-start;gap:0.6rem;"><carbon-logo-github style="font-size:1.4rem;color:var(--np-blue);flex-shrink:0;" /><div><strong>Alles openbaar en herleidbaar</strong> in GitHub: begrippen, informatiemodel, specificaties, besluiten<br/><span class="muted" style="font-size:0.78rem;">github.com/Npuls-OKx/Public &middot; github.com/Npuls-OKx/meta</span></div></div>
  <div style="display:flex;align-items:flex-start;gap:0.6rem;"><carbon-navaid-helipad style="font-size:1.4rem;color:var(--np-blue);flex-shrink:0;" /><div><strong>Een makkelijk navigeerbare opzet</strong> van de kennisbasis, zodat elk gremium dezelfde inhoud vindt</div></div>
  <div style="display:flex;align-items:flex-start;gap:0.6rem;"><carbon-chat style="font-size:1.4rem;color:var(--np-blue);flex-shrink:0;" /><div><strong>Een gemeenschappelijke taal</strong>: de begrippenlijst en het informatiemodel om het eigen model naast te leggen</div></div>
</div>
</div>
<div class="np-card accent-green" style="padding:0.7rem 1rem;font-size:0.86rem;line-height:1.5;">
<strong>Voorstel voor vandaag</strong>
<div style="display:flex;flex-direction:column;gap:0.45rem;margin-top:0.6rem;">
  <div style="display:flex;align-items:center;gap:0.6rem;"><carbon-user-follow style="font-size:1.3rem;color:var(--np-green);flex-shrink:0;" /><div><strong>AII spoor 3</strong>: werksessie over aanmelden, intekenen, inschrijven en het ontsluiten van aanbod</div></div>
  <div style="display:flex;align-items:center;gap:0.6rem;"><carbon-catalog style="font-size:1.3rem;color:var(--np-green);flex-shrink:0;" /><div><strong>Onderwijs Catalogus</strong>: gedeelde begrippen en informatiemodel met eduXchange</div></div>
  <div style="display:flex;align-items:center;gap:0.6rem;"><carbon-user-identification style="font-size:1.3rem;color:var(--np-green);flex-shrink:0;" /><div><strong>EduID en identity provisioning</strong>: wie is leidend voor de student in de keten</div></div>
  <div style="display:flex;align-items:center;gap:0.6rem;"><mdi-key-variant style="font-size:1.3rem;color:var(--np-green);flex-shrink:0;" /><div><strong>Leeruitkomsten</strong>: met de LUK-werkgroep de sleutel over de pijlers heen vaststellen</div></div>
  <div style="display:flex;align-items:center;gap:0.6rem;"><carbon-recycle style="font-size:1.3rem;color:var(--np-green);flex-shrink:0;" /><div><strong>Npuls-programmabrede aanpak van de afstemming gevraagd</strong>, OKx aan tafel</div></div>
</div>
</div>
</div>

<div class="np-card accent-orange" style="margin-top: 0.7rem; padding: 0.55rem 1rem;">
<div style="display:flex;align-items:center;gap:0.6rem;font-size:0.95rem;"><carbon-partnership style="font-size:1.5rem;color:var(--np-orange);flex-shrink:0;" /><strong>Ecosysteem eerst, dan de koppelingen</strong> <span class="muted" style="font-size:0.85rem;">&middot; ons architectuurprincipe, ook op programmaniveau</span></div>
<div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.45rem;font-size:0.8rem;">
  <span style="background:#fff;border:1px solid var(--np-light-gray);border-radius:999px;padding:0.2rem 0.7rem;">het ecosysteem lost het probleem van de instelling op</span>
  <span style="background:#fff;border:1px solid var(--np-light-gray);border-radius:999px;padding:0.2rem 0.7rem;">united front, de juiste mensen aan tafel</span>
  <span style="background:#fff;border:1px solid var(--np-light-gray);border-radius:999px;padding:0.2rem 0.7rem;">gedeelde expertise naar de scholen</span>
  <span style="background:#fff;border:1px solid var(--np-light-gray);border-radius:999px;padding:0.2rem 0.7rem;">een claim op de schaarse capaciteit van scholen</span>
</div>
</div>

</div>

<!--
Vraag 3 van Hans. Uit de afstemming van 21 september (Niek en Niels): trek het
OKx-architectuurprincipe "ecosysteem eerst, dan koppelingen" door naar programmaniveau. Lokaal
goede keuzes zijn te weinig; het ecosysteem moet het probleem oplossen dat instellingen ervaren,
en daarvoor is gezamenlijke afstemming nodig: een united front met de juiste mensen aan tafel,
gedeelde expertise naar de scholen (OKx is bereid mensen aan te laten haken, andere pijlers
ook), omdat eduXchange, EduID en OKx anders elk beslag leggen op de beperkte capaciteit van
scholen en scholen niet meer weten waar ze op moeten inzetten. OKx voert die regie niet alleen;
OKx wil wel aan tafel. De QR-code naar de kennisbasis op de laatste slide.
-->

---

<!-- 13. QR-CODE: DE KENNISBASIS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Alles staat open: de kennisbasis van OKx

<div style="display:grid;grid-template-columns:1fr 1.4fr;gap:2rem;align-items:center;margin-top:1rem;">
  <div style="display:flex;flex-direction:column;align-items:center;gap:0.6rem;">
    <img src="/platen/qr-github-public.png" style="width:15rem;height:15rem;" />
    <div style="font-size:0.95rem;font-weight:600;color:var(--np-ink);">github.com/Npuls-OKx/Public</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:0.8rem;font-size:0.95rem;line-height:1.55;">
    <div class="np-card accent-blue" style="padding:0.6rem 1rem;"><carbon-book style="font-size:1.3rem;color:var(--np-blue);vertical-align:-0.25rem;" /> <strong>Referentiemateriaal</strong>: leerroutes en kaderscenario's, principes, begrippenlijst, requirementsboom, architectuurbesluiten</div>
    <div class="np-card accent-green" style="padding:0.6rem 1rem;"><carbon-document style="font-size:1.3rem;color:var(--np-green);vertical-align:-0.25rem;" /> <strong>Koppelvlakspecificaties</strong>: koppelingen, interactiepatronen, datamodelschema's, met versie en release</div>
    <div class="np-card accent-orange" style="padding:0.6rem 1rem;"><carbon-data-base style="font-size:1.3rem;color:var(--np-orange);vertical-align:-0.25rem;" /> <strong>Informatiemodel</strong>: de begrippenfamilies en de plaat, gemapt op OEAPI</div>
  </div>
</div>

</div>

<!--
Verwijzing naar de publieke omgeving (Garik en Niek, 21 september). Alles wat vandaag is
getoond staat daar met historie en besluiten; wie het naast het eigen werk wil leggen, begint
bij het referentiemateriaal.
-->
