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

<!-- 2. DE KERN: EEN WERKWIJZE DIE COMPLEXITEIT HANTEERBAAR MAAKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een werkwijze die de complexiteit hanteerbaar maakt

<div class="np-pipeline" style="margin-top: 1.4rem;">
  <div class="np-step orange" style="flex: 1;">
    <carbon-user-multiple style="font-size: 1.9rem; color: var(--np-orange);" />
    <strong style="font-size: 0.88rem;">Wat scholen willen</strong>
    <small>opgehaald bij koplopers, per leerroute uitgewerkt</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step blue" style="flex: 1;">
    <carbon-partnership style="font-size: 1.9rem; color: var(--np-blue);" />
    <strong style="font-size: 0.88rem;">Beschreven vertaalslag</strong>
    <small>scenario, begrippen, informatiemodel, informatiestromen</small>
  </div>
  <div class="np-arrow">&#8594;</div>
  <div class="np-step green" style="flex: 1;">
    <carbon-document style="font-size: 1.9rem; color: var(--np-green);" />
    <strong style="font-size: 0.88rem;">Eindproduct</strong>
    <small>koppelvlakspecificatie, opgebouwd uit koppelingspecificaties</small>
  </div>
</div>

<div class="np-card accent-green" style="margin-top: 1.4rem; font-size: 0.98rem; line-height: 1.6;">
  <strong>Dat is de winst van dit kwartaal:</strong> een vorm waarin business en techniek aan elkaar te knopen zijn, en waarin de vraag van een school herleidbaar terugkomt in wat een leverancier moet bouwen.
</div>

</div>

<!--
Kernboodschap van dit blok. De inhoud is nog concept; de werkwijze is wat we hebben bereikt.
Koppelingspecificatie is de afspraak tussen twee systemen; het koppelvlak is alles wat een
systeem raakt. Die twee begrippen zijn zelf ook nog onderwerp van afstemming.
-->

---

<!-- 3. HET EINDPRODUCT IN BOUWBLOKKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Het eindproduct, scherper in beeld

<div class="np-grid-2" style="margin-top: 0.7rem; gap: 1.1rem; align-items: center;">

<div>
  <img src="/platen/koppelvlak-specificatie-breakdown.png" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.3rem;">De koppelvlakspecificatie en haar bouwblokken</div>
</div>

<div>
  <div class="np-card accent-blue" style="font-size: 0.87rem; line-height: 1.5; padding: 0.6rem 0.9rem; margin-bottom: 0.6rem;">
    <strong>Vaste bouwblokken per koppeling:</strong> wat systemen van elkaar vragen, wanneer zij dat doen, welke gegevens meegaan en hoe toegang is geregeld. Elke eis komt uit de vraag van de sector.
  </div>
  <div class="np-card accent-orange" style="font-size: 0.87rem; line-height: 1.5; padding: 0.6rem 0.9rem; margin-bottom: 0.6rem;">
    <strong>Drie koppelingen in uitwerking:</strong> catalogus en planning voor nominaal en keuze-aanbod, catalogus en studentadministratie, catalogus en leeromgeving.
  </div>
  <div class="np-card accent-green" style="font-size: 0.87rem; line-height: 1.5; padding: 0.6rem 0.9rem;">
    <strong>Per onderdeel een eigen versie en ritme,</strong> openbaar en met de reden bij elke wijziging. Een school of leverancier weet welke versie hij leest en wat er veranderd is.
  </div>
</div>

</div>

<div style="margin-top: 0.8rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept. Richting en eerste invulling liggen er; de details scherpen wij aan met leveranciers.
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
    Begrippenkader, informatiemodel en informatiestromen liggen als concept voor. Elk begrip ligt naast MORA en ROSA: waar de sector al een woord heeft, gebruiken wij dat.
  </div>
  <div class="np-card accent-orange" style="font-size: 0.87rem; line-height: 1.5; padding: 0.6rem 0.9rem; margin-top: 0.6rem;">
    Open punten: de grens tussen koppeling en koppelvlak, en hoe fijnmazig de uitwisseling moet zijn.
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

# Toetsen met voorbeelduitwerkingen

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 1.2rem; align-items: center;">

<div>
  <img src="/platen/jochem.png" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray);" />
</div>

<div>
  <div class="np-card accent-orange" style="font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.7rem;">
    <strong>Omvang en complexiteit vragen om voorbeelden</strong><br/>
    abstracte modellen blijven anders te ver van de praktijk
  </div>
  <div class="np-card accent-blue" style="font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.7rem;">
    <strong>Een echte opleiding per leerroute</strong><br/>
    apothekersassistent, van het ontwerp van de opleiding tot diplomering
  </div>
  <div class="np-card accent-green" style="font-size: 0.9rem; line-height: 1.5;">
    <strong>Robuustheid toetsen</strong><br/>
    scholen en leveranciers leggen het naast hun praktijk: herkennen zij het, ontbreekt er iets
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

<!-- 6. FASERING EN DOELEN (CONCEPT) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Fasering en doelen

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 0.8rem; align-items: start;">
  <div class="np-card accent-orange" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>Najaar 2026</strong><br/>
    concept aanscherpen met koploperscholen en leveranciers
  </div>
  <div class="np-card accent-blue" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>Doel Q1 2027</strong><br/>
    eerste koppeling bouwbaar bij leveranciers
  </div>
  <div class="np-card accent-green" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>Daarna: verbreden</strong><br/>
    meer koppelingen, meer detail per koppeling
  </div>
  <div class="np-card accent-green" style="font-size: 0.88rem; line-height: 1.5;">
    <strong>En verder</strong><br/>
    meer leerroutes, daarna het hoger onderwijs
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
