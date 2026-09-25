---
theme: default
title: "Werkgroep OKx: voortgang juni tot september 2026"
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
  <h1 style="font-size: 2.9rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Werkgroep OKx</h1>
  <div style="font-size: 1.15rem; color: var(--np-ink); margin-bottom: 0.9rem;">Voortgang juni tot september 2026</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; kerngroep techniek &middot; 29 september 2026</div>
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

<div style="display: grid; grid-template-columns: 1.75fr 1fr; gap: 1rem; align-items: center; margin-top: 0.6rem;">

<div>
  <img src="/platen/koppelvlak-specificatie-breakdown.png" style="width: 100%; max-height: 19.5rem; object-fit: contain; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.3rem;">De koppelvlakspecificatie en haar bouwblokken</div>
</div>

<div>
  <div class="np-card accent-blue np-mini">
    <carbon-assembly-cluster class="np-pic" />
    <div class="np-kop">Vaste bouwblokken</div>
    <small>eisen &middot; systemen &middot; berichtstromen &middot; endpoints &middot; schema's &middot; toegang</small>
  </div>
  <div class="np-card accent-orange np-mini">
    <carbon-network-3 class="np-pic" style="color: var(--np-orange);" />
    <div class="np-kop">Drie koppelingen, in volgorde</div>
    <small>1 onderwijscatalogus en planningssysteem<br/>2 onderwijscatalogus met studentvolgsysteem en kernregistratie<br/>3 onderwijscatalogus en leeromgeving</small>
  </div>
  <div class="np-card accent-green np-mini" style="margin-bottom: 0;">
    <carbon-version class="np-pic" style="color: var(--np-green);" />
    <div class="np-kop">OKx implementeren en versies</div>
    <small>kiezen per koppeling en berichtstroom &middot; een versie legt het ijkpunt vast &middot; een nieuwe eis komt ernaast</small>
  </div>
</div>

</div>

<style scoped>
.np-mini { padding: 0.5rem 0.7rem; margin-bottom: 0.5rem; }
.np-mini small { font-size: 0.74rem; line-height: 1.4; display: block; }
.np-pic { font-size: 1.1rem; color: var(--np-blue); }
.np-kop { font-weight: 700; font-size: 0.84rem; line-height: 1.25; }
</style>

<div style="margin-top: 0.8rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept in afstemming
</div>

</div>

<!--
Dit is het antwoord op "wat leveren jullie nu eigenlijk op". De plaat komt uit de uitwerking van
Garik: de koppelvlakspecificatie als pakket, opgebouwd uit functionele eisen, referentiesystemen,
berichtstromen, endpoints, datamodelschema's en de authenticatiestandaard, met de
requirementsboom als vertrekpunt. De volgorde van de drie koppelingen is de prioritering: eerst
de catalogus met planning, dan de catalogus met het studentvolgsysteem en de kernregistratie, en
als laatste de leeromgeving. Het groene blok beantwoordt twee vragen die in de zaal leven: wat
betekent het voor een leverancier om OKx te ondersteunen, en waarom is er uberhaupt versionering
nodig. Antwoord: een partij kiest per koppeling en per berichtstroom wat zij implementeert, een
versie legt vast hoe de afspraak er op dat moment uitzag, en een nieuwe eis krijgt een eigen
berichtstroom naast de bestaande, zodat draaiende koppelingen blijven werken. Bij de leeromgeving: OKx lijnt uit op het ontworpen onderwijs,
de inhoud blijft van de school. Over versionering: elk onderdeel heeft een eigen versie en een
eigen ritme, zodat een wijziging in een schema niet het hele pakket ophoudt.
-->

---

<!-- 4. LEERROUTE 1 ALS PROCES -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Leerroute 1 als proces

<style scoped>
.mermaid { display: flex; justify-content: center; margin: 0.2rem 0 0; }
.mermaid svg { max-width: 100%; height: auto; }
</style>

<div style="font-size: 0.85rem; color: var(--np-mid-gray); margin-top: 0.2rem;">Ontwerp en planning: twee van de zeven rollen</div>

<div style="margin-top: 0.4rem;">

```mermaid {theme: 'base', scale: 0.78, themeVariables: {'fontFamily': 'General Sans, Inter, sans-serif', 'fontSize': '15px', 'primaryColor': '#FFFFFF', 'primaryBorderColor': '#3D68EC', 'primaryTextColor': '#1B2A6B', 'lineColor': '#DD784B', 'clusterBkg': '#F7F8FB', 'clusterBorder': '#3D68EC', 'edgeLabelBackground': '#FFFFFF'}}
flowchart TB
  subgraph OO["Onderwijsontwerper"]
    direction LR
    OO1[Kwalificatiekader analyseren] --> OO2[Opleiding specificatie beschrijven] --> OO3[Opleidingsprogramma specificatie beschrijven] --> OO4[Onderwijseenheid specificaties beschrijven] --> OO5[Leeronderdeel specificaties beschrijven] --> OO6[Onderwijsspecificaties publiceren]
  end
  subgraph PL["Planner"]
    direction LR
    PL1[Strategische jaarplanning] --> PL2[Team-inzetplanning]
  end
  OO6 --> PL1
```

</div>

<div style="display: flex; justify-content: center; gap: 0.4rem; margin-top: 1.4rem; flex-wrap: wrap;">
  <div class="np-fase">1 Ontwerpen</div>
  <div class="np-fase">2 Publiceren en planbaar maken</div>
  <div class="np-fase">3 Intake en plaatsing</div>
  <div class="np-fase">4 Detailleren en roosteren</div>
  <div class="np-fase">5 Uitvoeren en begeleiden</div>
  <div class="np-fase lus"><carbon-recycle style="font-size: 0.9rem;" /> 6 Keuzemomenten</div>
  <div class="np-fase lus"><carbon-recycle style="font-size: 0.9rem;" /> 7 Bijsturen</div>
  <div class="np-fase">8 Examineren en diplomeren</div>
</div>

<div style="margin-top: 0.6rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
  Per stap vastgelegd: welke gegevens ontstaan, en tussen welke systemen zij gaan
</div>

<div style="margin-top: 0.4rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept in afstemming
</div>

<style scoped>
.np-fase {
  background: white;
  border: 1px solid var(--np-light-gray);
  border-top: 3px solid var(--np-blue);
  border-radius: 6px;
  padding: 0.3rem 0.6rem;
  font-size: 0.76rem;
  font-weight: 600;
  color: var(--np-dark-blue);
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
.np-fase.lus { border-top-color: var(--np-orange); color: var(--np-orange); }
</style>

</div>

<!--
Zo ziet een leerroute-uitwerking eruit. Het diagram is het ontwerp- en planningsdeel van scenario
1.1 uit leerroute 1, met de stappen letterlijk uit dat scenario; de namen van de specificaties
volgen het informatiemodel (opleiding, opleidingsprogramma, onderwijseenheid, leeronderdeel). Het
ontwerp loopt door tot en met de leeronderdeel specificaties en sluit af met publiceren; dat
publiceren is de overdracht naar de planning. Daarna detailleert de onderwijsontwikkelaar, vaak
een docent, die specificaties tot lesspecificaties; de les blijft binnen de instelling en valt
buiten de uitwisseling (ontwerpkeuze 8), dus die baan staat hier niet. De vijf rollen die hier
niet staan zijn de onderwijsontwikkelaar, de roosteraar, de studieloopbaanbegeleider, de student
en de docent; samen zeven rollen. De acht fasen eronder zijn de journey van het kaderscenario: fasen 1 tot en met 5
lopen lineair, fase 6 (keuzemomenten) en fase 7 (bijsturen) zijn lussen die het jaarplan en het
rooster opnieuw raken, en fase 8 sluit af met examinering en diplomering. Per stap legt de
uitwerking vast welke gegevens ontstaan of veranderen en welke daarvan tussen welke systemen gaan;
dat is precies de brug naar het informatiemodel en de koppelingen.
-->

---

<!-- 5. DE CONCEPTUELE LAAG -->
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
    Afgeleid uit leerroute 1, gelegd naast MORA en ROSA.
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

<!-- 6. VERIFIEREN MET VOORBEELDUITWERKINGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Verifiëren met voorbeelduitwerkingen

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 1.2rem; align-items: center;">

<div>
  <img src="/platen/voorbeeld-f2-07-aanbod-naar-catalogus.svg" style="width: 100%; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
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

<div style="margin-top: 0.8rem; font-size: 0.85rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept in afstemming
</div>

</div>

<!--
Voorbeelduitwerking leerroute 1 met persona Jochem, acht fasen, een beeld per processtap, met
een invulblad per objecttype en zeven vragen. Ligt 30 september bij de kerngroep techniek.
Dit is de manier waarop we de conceptuele laag op robuustheid toetsen voordat we detailleren.
-->

---

<!-- 7. VAN BEELD NAAR BERICHT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van beeld naar bericht

<style scoped>
/* Een mermaid-svg heeft een eigen breedte en duwt anders de tweede kolom van de
   slide af. Binnen de kaart blijven en meeschalen met de kolom. */
.mermaid { display: flex; justify-content: center; margin: 0.2rem 0 0; }
.mermaid svg { max-width: 100%; height: auto; }
</style>

<div style="font-size: 0.85rem; color: var(--np-mid-gray); margin-top: 0.2rem;">Dezelfde stap, als koppeling</div>

<div class="np-grid-2" style="margin-top: 0.7rem; gap: 1.1rem; align-items: start; grid-template-columns: 1.05fr 1fr;">

<div style="min-width: 0;">

<div class="np-card accent-blue" style="padding: 0.7rem 0.9rem 0.4rem;">
  <div style="font-weight: 700; font-size: 0.92rem;">Interactie</div>

```mermaid {theme: 'base', scale: 0.62, themeVariables: {'fontFamily': 'General Sans, Inter, sans-serif', 'fontSize': '15px', 'actorBkg': '#FFFFFF', 'actorBorder': '#3D68EC', 'actorTextColor': '#1B2A6B', 'actorLineColor': '#9CA3AF', 'signalColor': '#DD784B', 'signalTextColor': '#374151', 'primaryColor': '#FFFFFF', 'primaryTextColor': '#1B2A6B', 'lineColor': '#DD784B'}}
sequenceDiagram
    participant P as Planningssysteem
    participant OC as Onderwijscatalogus
    P->>OC: melding: aanbod gepland
    OC->>P: vraagt het aanbod op
    P-->>OC: aanbod met verwijzing naar de specificatie
```

</div>

<div class="np-card accent-orange" style="padding: 0.55rem 0.9rem; margin-top: 0.7rem; display: flex; align-items: baseline; gap: 0.55rem; flex-wrap: wrap;">
  <span style="font-weight: 700; font-size: 0.88rem;">Endpoint</span>
  <code style="font-size: 0.76rem;">GET /onderwijsaanbod/{id}</code>
  <small style="font-size: 0.76rem; color: var(--np-mid-gray);">op het planningssysteem</small>
</div>

</div>

<div class="np-card accent-green" style="padding: 0.7rem 0.9rem; min-width: 0;">
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

<div style="margin-top: 0.7rem; text-align: center; font-size: 0.85rem; color: var(--np-mid-gray);">
  Techniekagnostisch: het bericht ligt vast, de techniek is een keuze
</div>

<div style="display: flex; justify-content: center; gap: 0.6rem; margin-top: 0.45rem; flex-wrap: wrap;">
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 0.8rem; font-weight: 600; color: var(--np-dark-blue);">
    <logos-json style="font-size: 1.1rem;" /> REST en JSON, nu
  </div>
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 0.8rem; font-weight: 600; color: var(--np-dark-blue);">
    <logos-graphql style="font-size: 1.1rem;" /> GraphQL
  </div>
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 0.8rem; font-weight: 600; color: var(--np-dark-blue);">
    <carbon-flash style="font-size: 1.1rem; color: var(--np-orange);" /> Events
  </div>
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 0.8rem; font-weight: 600; color: var(--np-dark-blue);">
    <carbon-bot style="font-size: 1.1rem; color: var(--np-blue);" /> AI-agents via MCP
  </div>
</div>

<div style="margin-top: 0.5rem; font-size: 0.8rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept in afstemming
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

<!-- 8. AMIGO -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# AMIGO van Edustandaard

<style scoped>
.mermaid { display: flex; justify-content: center; margin: 0; }
.mermaid svg { max-width: 100%; height: auto; }
</style>

<div style="font-size: 0.85rem; color: var(--np-mid-gray); margin-top: 0.2rem;">De landelijke route van scenario naar afsprakenset</div>

<div class="np-grid-2" style="margin-top: 0.7rem; gap: 1.1rem; align-items: center; grid-template-columns: 1.1fr 1fr;">

<div style="min-width: 0;">

```mermaid {theme: 'base', scale: 0.78, themeVariables: {'fontFamily': 'General Sans, Inter, sans-serif', 'fontSize': '15px', 'primaryColor': '#FFFFFF', 'primaryBorderColor': '#3D68EC', 'primaryTextColor': '#1B2A6B', 'lineColor': '#DD784B', 'edgeLabelBackground': '#FFFFFF'}}
flowchart TD
  A[Scenario-analyse] --> B[Gegevensanalyse]
  A --> C[Interactie-analyse]
  B --> D[Technologiekeuze]
  C --> D
  D --> E[Berichtspecificatie]
  D --> F[Interfacespecificatie]
  E --> G[Afsprakenset]
  F --> G
```

<div style="display: flex; justify-content: center; margin-top: 0.3rem;">
  <img src="/logos/edustandaard.png" style="height: 1.5rem; width: auto;" />
</div>

</div>

<div class="np-card accent-blue" style="padding: 0.7rem 0.9rem; min-width: 0;">
  <div style="font-weight: 700; font-size: 0.92rem; margin-bottom: 0.45rem;">Zo vullen wij die stappen</div>
  <div style="display: flex; flex-direction: column; gap: 0.32rem; font-size: 0.82rem;">
    <div><span style="color: var(--np-blue); font-weight: 600;">Scenario</span> &#8594; leerroutes</div>
    <div><span style="color: var(--np-blue); font-weight: 600;">Gegevens</span> &#8594; informatiemodel</div>
    <div><span style="color: var(--np-blue); font-weight: 600;">Interactie</span> &#8594; interactiediagrammen</div>
    <div><span style="color: var(--np-blue); font-weight: 600;">Bericht</span> &#8594; datamodelschema's</div>
    <div><span style="color: var(--np-blue); font-weight: 600;">Interface</span> &#8594; endpoints</div>
    <div><span style="color: var(--np-blue); font-weight: 600;">Afsprakenset</span> &#8594; o.a. koppelvlakspecificatie, datamodelprofielen, authenticatie en identity provisioning</div>
  </div>
</div>

</div>

<div style="margin-top: 0.7rem; font-size: 0.8rem; color: var(--np-mid-gray); text-align: center;">
  Een aanpak die leveranciers uit andere onderwijsstandaarden kennen
</div>

</div>

<!--
Waarom dit erbij hoort: de route van de tweede slide is geen eigen vinding. AMIGO is de aanpak van
Edustandaard om van een scenario naar een bouwbare afsprakenset te komen, en leveranciers kennen
hem uit andere onderwijsstandaarden. De stappen worden iteratief doorlopen: een keuze in het
bericht kan aanleiding zijn om scenario, gegevens of interacties aan te scherpen. Twee nuances
voor wie doorvraagt: de interactiestap levert interactiediagrammen op, en dat is iets anders dan de
interactiepatronen (melden en ophalen, en de afhandeling bij een fout) die in de koppelingspecificatie
staan. En de afsprakenset is breder dan de koppelvlakspecificatie alleen: daar horen ook de
datamodelprofielen, de authenticatie en het inrichten van identiteiten bij. Bron:
edustandaard.nl/amigo/aanpak, en paragraaf 2.4 van de leerroute-uitwerking.
-->

---

<!-- 9. DOEL EN FASERING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Doel Q1 2027

<div style="font-size: 0.85rem; color: var(--np-mid-gray); margin-top: 0.2rem;">Drie koppelingen, alle lagen beschreven</div>

<div style="margin-top: 0.5rem;">
  <img src="/platen/koppelingen-hoofdplaat.svg" style="width: 100%; max-height: 15.5rem; object-fit: contain; border-radius: 6px; border: 1px solid var(--np-light-gray); background: #fff;" />
  <div style="font-size: 0.72rem; color: var(--np-mid-gray); margin-top: 0.25rem; text-align: center;">Catalogus met planning, studentadministratie en leeromgeving</div>
</div>

<div class="np-grid-3" style="margin-top: 0.6rem; gap: 0.7rem; align-items: start;">
  <div class="np-card accent-blue" style="padding: 0.6rem 0.8rem;">
    <div style="font-weight: 700; font-size: 0.88rem;">Per koppeling alle lagen</div>
    <small style="font-size: 0.76rem;">eisen &middot; systemen &middot; patronen &middot; endpoints &middot; schema's &middot; toegang</small>
  </div>
  <div class="np-card accent-orange" style="padding: 0.6rem 0.8rem;">
    <div style="font-weight: 700; font-size: 0.88rem;">Najaar 2026</div>
    <small style="font-size: 0.76rem;">aanscherpen met koplopers</small>
  </div>
  <div class="np-card accent-green" style="padding: 0.6rem 0.8rem;">
    <div style="font-weight: 700; font-size: 0.88rem;">Daarna</div>
    <small style="font-size: 0.76rem;">meer koppelingen, meer leerroutes, het ho</small>
  </div>
</div>

<div style="display: flex; justify-content: center; align-items: center; gap: 0.6rem; margin-top: 0.7rem; flex-wrap: wrap;">
  <span style="font-size: 0.8rem; color: var(--np-mid-gray);">Aanhaken kan</span>
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.28rem 0.8rem; font-size: 0.78rem; color: var(--np-dark-blue);">
    <carbon-tools style="font-size: 1rem; color: var(--np-blue);" /> <strong>Mee uitwerken</strong> &middot; kerngroep techniek
  </div>
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.28rem 0.8rem; font-size: 0.78rem; color: var(--np-dark-blue);">
    <carbon-chat style="font-size: 1rem; color: var(--np-orange);" /> <strong>Meedenken</strong> &middot; PoC-sessies
  </div>
  <div style="display: flex; align-items: center; gap: 0.35rem; background: white; border: 1px solid var(--np-light-gray); border-radius: 999px; padding: 0.28rem 0.8rem; font-size: 0.78rem; color: var(--np-dark-blue);">
    <carbon-compass style="font-size: 1rem; color: var(--np-green);" /> <strong>Richting geven</strong> &middot; adviesgroep OKx
  </div>
</div>

<div style="margin-top: 0.5rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center;">
  Status: concept in afstemming
</div>

</div>

<!--
Het doel in de taal van de rest van dit blok: voor drie koppelingen, catalogus met planning,
met studentadministratie en met de leeromgeving, liggen in het eerste kwartaal van 2027 alle
lagen beschreven. De plaat markeert die drie lijnen op de informatiestromen-hoofdplaat; de
bouwblokken eronder zijn dezelfde als op de eindproductslide, dus per lijn is te zien wat er
nog moet gebeuren. Fasering als doel, niet als toezegging. Er staat geen vraag op de slide: de vraag aan de werkgroep
komt van de projectleider. Wie er in de zaal iets wil betekenen, kan op drie plekken aanhaken: mee uitwerken in de kerngroep
techniek, meedenken in de PoC-sessies met de scholen, of richting geven in de adviesgroep OKx. Kennisbasis:
github.com/Npuls-OKx/Public. Bronnen: overleg met het SI-team van 13 juli, vier
koploperleveranciers en zes tot acht koploperinstellingen.
-->
