---
theme: default
title: "OKx kerngroep techniek: voortgang juni tot september 2026"
info: "Voortgangsupdate van de kerngroep techniek voor de werkgroep OKx: wat er sinds juni is opgeleverd, in businesstaal."
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

<!-- 1. TITEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide1.PNG);"></div>

<div style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem 4rem; z-index: 1;">
  <h1 style="font-size: 2.9rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Kerngroep techniek</h1>
  <div style="font-size: 1.15rem; color: var(--np-ink); margin-bottom: 0.9rem;">Voortgang juni tot september 2026</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; werkgroep OKx</div>
</div>

<!--
Dit blok is de techniekparagraaf in de bredere OKx-update. Toon: werk in uitvoering. Alles wat er
ligt is concept in afstemming met leveranciers en scholen; de waarde zit in de manier van werken
die dat concept oplevert.
-->

---

<!-- 2. DE ROUTE NAAR HET EINDPRODUCT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Route naar eindproduct scherp

<div style="font-size: 0.85rem; color: var(--np-mid-gray); margin-top: 0.2rem;">Vertalen langs een vaste route</div>

<div class="np-pipeline" style="margin-top: 0.6rem; align-items: stretch;">
  <div class="np-step orange" style="flex: 1; padding: 0.7rem 0.4rem; align-items: center; justify-content: center;">
    <carbon-user-multiple style="font-size: 1.5rem; color: var(--np-orange);" />
    <strong style="font-size: 0.82rem;">Userstories</strong>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue" style="flex: 1; padding: 0.7rem 0.4rem; align-items: center; justify-content: center;">
    <carbon-assembly-cluster style="font-size: 1.5rem; color: var(--np-blue);" />
    <strong style="font-size: 0.82rem;">Bouwblokken</strong>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue" style="flex: 1; padding: 0.7rem 0.4rem; align-items: center; justify-content: center;">
    <carbon-book style="font-size: 1.5rem; color: var(--np-blue);" />
    <strong style="font-size: 0.82rem;">Begrippen</strong>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue" style="flex: 1; padding: 0.7rem 0.4rem; align-items: center; justify-content: center;">
    <carbon-machine-learning-model style="font-size: 1.5rem; color: var(--np-blue);" />
    <strong style="font-size: 0.82rem;">Informatiemodel</strong>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue" style="flex: 1; padding: 0.7rem 0.4rem; align-items: center; justify-content: center;">
    <carbon-network-3 style="font-size: 1.5rem; color: var(--np-blue);" />
    <strong style="font-size: 0.82rem;">Informatiestromen</strong>
    <small>tussen applicatiecomponenten</small>
  </div>
</div>

<div style="text-align: center; color: var(--np-green); font-size: 1.3rem; font-weight: 700; line-height: 1; margin: 0.35rem 0;">&#8595;</div>

<div class="np-card accent-green" style="padding: 0.6rem 1rem; text-align: center;">
  <carbon-document style="font-size: 1.5rem; color: var(--np-green);" />
  <div style="font-weight: 700; font-size: 0.95rem;">Eindproduct: koppelvlakspecificatie</div>
  <small style="font-size: 0.82rem; color: var(--np-mid-gray);">koppelingspecificaties &middot; datamodelschema's &middot; interacties &middot; koppelvlakdiensten</small>
</div>

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 0.8rem;">
  <div class="np-card accent-orange" style="padding: 0.7rem 0.9rem;">
    <carbon-partnership style="font-size: 1.5rem; color: var(--np-orange);" />
    <div style="font-weight: 700; font-size: 0.92rem;">In gesprek met instellingen en leveranciers</div>
    <small style="font-size: 0.82rem;">wat moet er gebouwd worden</small>
  </div>
  <div class="np-card accent-blue" style="padding: 0.7rem 0.9rem;">
    <carbon-education style="font-size: 1.5rem; color: var(--np-blue);" />
    <div style="font-weight: 700; font-size: 0.92rem;">Leerroute 1 in uitwerking</div>
    <small style="font-size: 0.82rem;">volgt deze opbouw</small>
  </div>
</div>

</div>

<!--
De kern van het blok: de route van wens naar eindproduct staat scherp. Een userstory van een school
wordt een bouwblok, dat bouwblok krijgt begrippen met een definitie, die begrippen landen in het
informatiemodel, en daaruit volgen de informatiestromen tussen applicatiecomponenten. Aan het eind
staat de koppelvlakspecificatie: per koppeling een koppelingspecificatie volgens datamodelschema's,
de interacties tussen de systemen en de koppelvlakdiensten. Die route werkt alleen in gesprek met
instellingen en leveranciers, en dat gesprek loopt nu opnieuw: wat moet er gebouwd worden. Leerroute
1 gaat als eerste volledig langs deze opbouw. Alles wat er ligt is concept in afstemming.
-->

---

<!-- 3. HET EINDPRODUCT IN BOUWBLOKKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Het eindproduct in bouwblokken

<div class="np-grid-2" style="margin-top: 0.7rem; gap: 1.1rem; align-items: center;">

<div>
  <img src="/platen/koppelvlak-specificatie-breakdown.png" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.3rem;">De koppelvlakspecificatie en haar bouwblokken</div>
</div>

<div>
  <div class="np-card accent-blue" style="padding: 0.7rem 0.9rem; margin-bottom: 0.6rem;">
    <carbon-assembly-cluster style="font-size: 1.5rem; color: var(--np-blue);" />
    <div style="font-weight: 700; font-size: 0.95rem;">Vaste bouwblokken</div>
    <small style="font-size: 0.82rem;">eisen &middot; systemen &middot; patronen &middot; endpoints &middot; schema's &middot; toegang</small>
  </div>
  <div class="np-card accent-orange" style="padding: 0.7rem 0.9rem; margin-bottom: 0.6rem;">
    <carbon-network-3 style="font-size: 1.5rem; color: var(--np-orange);" />
    <div style="font-weight: 700; font-size: 0.95rem;">Drie koppelingen</div>
    <small style="font-size: 0.82rem;">planning &middot; studentadministratie &middot; leeromgeving</small>
  </div>
  <div class="np-card accent-green" style="padding: 0.7rem 0.9rem;">
    <carbon-version style="font-size: 1.5rem; color: var(--np-green);" />
    <div style="font-weight: 700; font-size: 0.95rem;">Eigen versie per deel</div>
    <small style="font-size: 0.82rem;">openbaar, met de reden erbij</small>
  </div>
</div>

</div>

<div style="margin-top: 0.8rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept in afstemming
</div>

</div>

<!--
Dit is het antwoord op "wat leveren jullie nu eigenlijk op". De plaat komt uit de uitwerking van
Garik: de koppelvlakspecificatie als pakket, opgebouwd uit functionele eisen, referentiesystemen,
interactiepatronen, endpoints, datamodelschema's en de authenticatiestandaard, met de
requirementsboom als vertrekpunt. Bij de leeromgeving: OKx lijnt uit op het ontworpen onderwijs,
de inhoud blijft van de school. Over versionering: elk onderdeel heeft een eigen versie en een
eigen ritme, zodat een wijziging in een schema niet het hele pakket ophoudt.
-->

---

<!-- 4. DE CONCEPTUELE LAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De conceptuele laag, in afstemming

<div class="np-grid-2" style="margin-top: 0.8rem; gap: 1.2rem; align-items: center;">

<div>
  <div style="display: flex; gap: 0.7rem; margin-bottom: 0.8rem;">
    <div class="np-card accent-blue" style="flex: 1; text-align: center; padding: 0.7rem 0.5rem;">
      <div style="font-size: 2.1rem; font-weight: 700; color: var(--np-blue); line-height: 1;">73</div>
      <small style="font-size: 0.8rem;">begrippen met definitie en herkomst</small>
    </div>
    <div class="np-card accent-orange" style="flex: 1; text-align: center; padding: 0.7rem 0.5rem;">
      <div style="font-size: 2.1rem; font-weight: 700; color: var(--np-orange); line-height: 1;">66</div>
      <small style="font-size: 0.8rem;">objecten in het informatiemodel</small>
    </div>
  </div>
  <div class="np-card accent-green" style="font-size: 0.87rem; line-height: 1.5; padding: 0.6rem 0.9rem;">
    Begrippen, model en stromen liggen als concept voor, naast MORA en ROSA.
  </div>
  <div class="np-card accent-orange" style="font-size: 0.87rem; line-height: 1.5; padding: 0.6rem 0.9rem; margin-top: 0.6rem;">
    Open: grens koppeling en koppelvlak, en hoe fijnmazig.
  </div>
</div>

<div>
  <img src="/platen/informatiemodel-v0.1.jpg" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray);" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Informatiemodel OKx v0.1, concept</div>
</div>

</div>

</div>

<!--
Bron: informatiemodel v0.1 (66 objecttypen, zeven begrippenfamilies) en begrippenlijst v0.2 (73
begrippen), beide met status concept, ter bekrachtiging door de kerngroep techniek. De
leeruitkomst is daarin de sleutel tussen ontwerp en resultaat. Noem dat de afstemming loopt:
dit is voorgelegd, niet vastgesteld.
-->

---

<!-- 5. TOETSEN MET VOORBEELDUITWERKINGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Verifiëren met voorbeelduitwerkingen

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 1.2rem; align-items: center;">

<div>
  <img src="/platen/voorbeeld-f2-07-aanbod-naar-catalogus.png" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
  <div style="font-size: 0.7rem; color: var(--np-mid-gray); margin-top: 0.3rem;">Een stap uit de uitwerking: het geplande aanbod terug naar de catalogus</div>
</div>

<div>
  <div class="np-card accent-orange" style="font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.7rem;">
    <strong>Voorbeelden nodig</strong><br/>
    <small>een model alleen blijft abstract</small>
  </div>
  <div class="np-card accent-blue" style="font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.7rem;">
    <strong>Een echte opleiding</strong><br/>
    <small>apothekersassistent, ontwerp tot diploma</small>
  </div>
  <div class="np-card accent-green" style="font-size: 0.9rem; line-height: 1.5;">
    <strong>Verifi&euml;ren bij scholen</strong><br/>
    <small>herkennen zij het, ontbreekt er iets</small>
  </div>
</div>

</div>

</div>

<!--
Voorbeelduitwerking leerroute 1 met persona Jochem, acht fasen, een beeld per processtap, met
een invulblad per objecttype en zeven vragen. Ligt 30 september bij de kerngroep techniek.
Dit is de manier waarop we de conceptuele laag op robuustheid toetsen voordat we detailleren.
-->

---

<!-- 6. VAN BEELD NAAR BERICHT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van beeld naar bericht

<div style="font-size: 0.85rem; color: var(--np-mid-gray); margin-top: 0.2rem;">Dezelfde stap, als koppeling</div>

<div class="np-grid-2" style="margin-top: 0.7rem; gap: 1.1rem; align-items: start;">

<div>
  <div class="np-card accent-blue" style="padding: 0.7rem 0.9rem;">
    <div style="font-weight: 700; font-size: 0.92rem; margin-bottom: 0.45rem;">Interactie</div>
    <div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.82rem;">
      <div style="display: flex; gap: 0.5rem; align-items: baseline;">
        <span style="flex: 0 0 9.2rem; color: var(--np-blue); font-weight: 600;">Planning &#8594; Catalogus</span>
        <span>melding: aanbod gepland</span>
      </div>
      <div style="display: flex; gap: 0.5rem; align-items: baseline;">
        <span style="flex: 0 0 9.2rem; color: var(--np-orange); font-weight: 600;">Catalogus &#8594; Planning</span>
        <span>haalt het aanbod op</span>
      </div>
      <div style="display: flex; gap: 0.5rem; align-items: baseline;">
        <span style="flex: 0 0 9.2rem; color: var(--np-blue); font-weight: 600;">Planning &#8594; Catalogus</span>
        <span>aanbod met verwijzing naar de specificatie</span>
      </div>
    </div>
  </div>
  <div class="np-card accent-orange" style="padding: 0.7rem 0.9rem; margin-top: 0.7rem;">
    <div style="font-weight: 700; font-size: 0.92rem; margin-bottom: 0.35rem;">Endpoint</div>
    <code style="font-size: 0.8rem;">GET /onderwijsaanbod/{id}</code>
    <div><small style="font-size: 0.8rem; color: var(--np-mid-gray);">op het planningssysteem</small></div>
  </div>
</div>

<div class="np-card accent-green" style="padding: 0.7rem 0.9rem;">
  <div style="font-weight: 700; font-size: 0.92rem; margin-bottom: 0.4rem;">Voorbeeldbericht</div>
<pre style="margin: 0; padding: 0.6rem 0.7rem; background: #F8F9FA; border: 1px solid var(--np-light-gray); border-radius: 6px; font-size: 0.62rem; line-height: 1.5; color: var(--np-dark-blue); overflow: hidden;">{
  <span style="color: var(--np-blue);">"aanbodType"</span>: "opleidingsaanbod",
  <span style="color: var(--np-blue);">"naam"</span>: "Apothekersassistent, cohort 2026",
  <span style="color: var(--np-blue);">"status"</span>: "gepland",
  <span style="color: var(--np-blue);">"specificatieVerwijzing"</span>: {
    "specificatieId": "79736830-1c5c-470f...",
    "versie": "0.1.0"
  },
  <span style="color: var(--np-blue);">"periode"</span>: { "start": "2026-09-01", "eind": "2029-07-15" }
}</pre>
</div>

</div>

<div style="margin-top: 0.8rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
  Endpoint, interactie en schema: bouwblokken van het eindproduct
</div>

</div>

<!--
Hier komt de lijn samen: de stap uit de voorbeelduitwerking van de vorige slide (F2-07, het
geplande aanbod terug naar de catalogus) staat in de koppelvlakspecificatie als endpoint,
interactiepatroon en datamodelschema. Het patroon heet notify-then-pull: planning meldt dat het
aanbod er is, de catalogus haalt het op bij de eigenaar van de gegevens. Het bericht is ingekort
voor de slide; het volledige voorbeeld staat in de datamodelschema's, met per laag van het aanbod
een verwijzing naar de specificatie waarvan het is gemaakt. Bron: interactiepatroon
onderwijscatalogus en planning (I3 en I5) en education-offering.json in Npuls-OKx/Public. Concept
in afstemming met de leveranciers.
-->

---

<!-- 7. FASERING EN DOELEN (CONCEPT) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Fasering en doelen

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 0.8rem; align-items: start;">
  <div class="np-card accent-orange" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>Najaar 2026</strong><br/>
    <small>concept aanscherpen met koplopers</small>
  </div>
  <div class="np-card accent-blue" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>Doel Q1 2027</strong><br/>
    <small>eerste koppeling bouwbaar</small>
  </div>
  <div class="np-card accent-green" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>Daarna</strong><br/>
    <small>meer koppelingen, meer detail</small>
  </div>
  <div class="np-card accent-green" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>En verder</strong><br/>
    <small>meer leerroutes, daarna het ho</small>
  </div>
</div>

<div class="np-card accent-orange" style="margin-top: 1.2rem; font-size: 1.1rem; line-height: 1.5; text-align: center;">
  <strong>Welke instellingen toetsen dit najaar mee?</strong>
</div>

<div style="margin-top: 0.7rem; font-size: 0.8rem; color: var(--np-mid-gray); text-align: center;">
  Concept, af te stemmen met de projectleiding &middot; kennisbasis: github.com/Npuls-OKx/Public
</div>

</div>

<!--
Fasering als doelen, niet als toezegging: Q1 2027 is het doel voor de eerste bouwbare koppeling.
De vraag aan de werkgroep staat hier als concept; de definitieve vraag komt van de projectleider.
Bronnen: overleg met het SI-team van 13 juli (specificaties rond de herfstvakantie, bouw in het
eerste kwartaal van 2027), vier koploperleveranciers en zes tot acht koploperinstellingen.
-->
