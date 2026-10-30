---
theme: default
title: "Werkgroep OKx: voortgang techniek sinds 29 september 2026"
info: "Techniekblok voor de werkgroep OKx van 3 november 2026: wat er sinds 29 september is uitgewerkt, en hoe OKx verder werkt."
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
  <h1 style="font-size: 2.9rem; line-height: 1.15; margin-bottom: 0.6rem; color: var(--np-ink);">Werkgroep OKx</h1>
  <div style="font-size: 1.15rem; color: var(--np-ink); margin-bottom: 0.9rem;">Elke leerroute die stap voor stap wordt doorlopen, maakt het informatiemodel scherper</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">Techniek &middot; voortgang sinds 29 september &middot; 3 november 2026</div>
</div>

<!--
Vervolg op het techniekblok van 29 september. Toon: werk in uitvoering. Alles wat er ligt is een
voorstel; de laatste slide komt daarop terug. Vier onderwerpen: de voorbeelduitwerking van Jochem,
het informatiemodel na de leveranciersronde, de inbreng van scholen, en de stap van keten naar
specificatie. Bron: issue meta #462.
-->

---

<!-- 2. VERTREKPUNT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vertrekpunt 29 september

<img src="/platen/hoofdplaat-ruim-drie-koppelingen.svg" class="np-breed" />

<div class="np-legenda">
  <span><i style="background: #3D68EC;"></i>catalogus en planning</span>
  <span><i style="background: #00AF81;"></i>catalogus en studentadministratie</span>
  <span><i style="background: #DD784B;"></i>catalogus en leeromgeving</span>
</div>

<div class="np-rij">
  <div class="np-card accent-blue np-mini">
    <div class="np-kop"><carbon-flow class="np-pic" /> Route naar het eindproduct</div>
    <small>van wens tot afspraken tussen systemen</small>
  </div>
  <div class="np-card accent-orange np-mini">
    <div class="np-kop"><carbon-map class="np-pic" style="color: var(--np-orange);" /> Leerroute 1 als toets</div>
    <small>Jochem als rode draad</small>
  </div>
  <div class="np-card accent-green np-mini">
    <div class="np-kop"><carbon-flag class="np-pic" style="color: var(--np-green);" /> Doel</div>
    <small>drie koppelingen, volledig beschreven</small>
  </div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.1rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 0.35rem; }
.np-breed { width: 100%; max-height: 66%; object-fit: contain; display: block; }
.np-legenda { display: flex; justify-content: center; gap: 1.4rem; font-size: 0.78rem; color: var(--np-dark-blue); margin-top: 0.2rem; }
.np-legenda i { display: inline-block; width: 1.4rem; height: 0.3rem; border-radius: 2px; margin-right: 0.4rem; vertical-align: middle; }
.np-rij { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.7rem; margin-top: 0.6rem; }
.np-mini { padding: 0.45rem 0.7rem; margin: 0; }
.np-mini small { font-size: 0.78rem; line-height: 1.4; display: block; margin-top: 0.15rem; }
.np-pic { font-size: 1rem; color: var(--np-blue); vertical-align: -0.15rem; }
.np-kop { font-weight: 700; font-size: 0.86rem; line-height: 1.25; }
</style>

</div>

<!--
Op 29 september liet het techniekblok drie dingen zien. De route naar het eindproduct: van de wens
van een school via bouwblokken, begrippen en het informatiemodel naar de informatiestromen en de
koppelvlakspecificatie. Leerroute 1 als toets, met Jochem als rode draad. En het doel: voor drie
koppelingen, de catalogus met planning, met studentadministratie en met de leeromgeving, alle lagen
beschreven in het eerste kwartaal van 2027, als richting. De plaat toont die koppelingen op de
hoofdplaat van de informatiestromen, opnieuw getekend uit het huidige model (versie 1.7a) met de
ruime opzet uit de voorbeelduitwerking; studentadministratie omvat de kernregistratie (OC-KRS) en het
studentvolgsysteem (OC-SVS). De overige stromen staan grijs.

Bron: presentaties/src/260929_werkgroep_okx_voortgang.md (techniekblok 29 september), meta #255.
-->

---

<!-- 3. DE REIS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De reis sinds 29 september

<div class="np-pipeline" style="margin-top: 1.4rem; align-items: stretch;">
  <div class="np-step blue np-stap">
    <carbon-network-3 class="np-groot" />
    <strong>Specificeren op de stromen</strong>
    <small>inhoud van de lijntjes open</small>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step orange np-stap">
    <carbon-data-structured class="np-groot" style="color: var(--np-orange);" />
    <strong>Informatiemodel en voorbeeld</strong>
    <small>leerroute stap voor stap</small>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step green np-stap">
    <carbon-flow class="np-groot" style="color: var(--np-green);" />
    <strong>Interactieketens</strong>
    <small>samen waarde voor student en docent</small>
  </div>
</div>

<div class="np-citaat">&ldquo;Een geïsoleerd koppelvlak lost voor een instelling geen probleem op.&rdquo;</div>
<div class="np-afzender">afstemming OKx en OEAPI, 20 oktober</div>

<div class="np-card accent-orange np-vraag">
  <div class="np-kop">Welke data wisselt het IT-landschap daarvoor uit?</div>
  <div class="np-pillen"><span class="np-pil">waar vandaan</span><span class="np-pil">in welke vorm</span></div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.8rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-stap { flex: 1; padding: 1rem 0.6rem; align-items: center; justify-content: center; text-align: center; }
.np-stap strong { font-size: 0.95rem; }
.np-stap small { font-size: 0.8rem; }
.np-groot { font-size: 1.7rem; color: var(--np-blue); }
.np-citaat { margin-top: 1.4rem; text-align: center; font-size: 1.15rem; font-style: italic; color: var(--np-dark-blue); }
.np-afzender { text-align: center; font-size: 0.78rem; color: var(--np-mid-gray); margin-top: 0.2rem; }
.np-vraag { margin-top: 1.2rem; padding: 0.7rem 1rem; text-align: center; }
.np-kop { font-weight: 700; font-size: 1rem; }
.np-pillen { margin-top: 0.45rem; display: flex; gap: 0.5rem; justify-content: center; }
.np-pil { display: inline-block; background: #F1F3F5; border-radius: 999px; padding: 0.15rem 0.7rem; font-size: 0.8rem; color: var(--np-dark-blue); }
</style>

</div>

<!--
Sinds 29 september liep elke poging om op de informatiestromen van de hoofdplaat te specificeren tegen
dezelfde vraag aan: wat gebeurt er precies op die lijntjes? Uit een gesprek met een instelling: "Het
zijn allemaal blokjes en pijltjes." Daarom ging het werk naar het informatiemodel en de
voorbeelduitwerking: de leerroute van Jochem stap voor stap, zodat zichtbaar wordt welke informatie
van welk systeem naar welk systeem gaat. Die vraag kwam ook uit de markt.

Op 20 oktober kwam het begrip interactieketen op tafel: een reeks interacties die samen iets bereiken
voor de student en de docent. Dat Jochem een keuzedeel kan kiezen, lost geen enkele koppeling alleen
op, en ook twee niet. Het voorbeeld maakt die ketens concreet en toetsbaar.

De vraag die daaruit volgt: welke data wisselt het IT-landschap van een instelling uit om die waarde te
leveren, waar komt die data vandaan en hoe ziet die eruit? Of, zoals een deelnemer het zei: "het gaat
erom wat je wilt dat er in die applicatie gebeurt."

Het citaat op de slide is licht ingekort uit de afstemming tussen OKx en OEAPI van 20 oktober.

Bron (Jamie): afstemming OKx en OEAPI 20 oktober; informatiemodel en koppelingen 2 oktober;
informatiemodel en ontwerpvragen 29 oktober; afstemming POC-resultaten 30 oktober; versionering
bouwblokken 30 september. De docent als begunstigde is de lezing van de opdrachtgever.
-->

---

<!-- 4. HOOFDVRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoofdvraag

<div class="np-citaat">
  <div class="np-citaattekst">&ldquo;Wat moet OKx nu eigenlijk beschrijven en bouwen?&rdquo;</div>
  <div class="np-afzender">SI-team, techniek</div>
</div>

<div class="np-drie">
  <div class="np-card accent-blue np-vak">
    <carbon-partnership class="np-groot" />
    <div class="np-kop">Gesprekken met de sector</div>
    <small>leveranciers en instellingen geven richting</small>
  </div>
  <div class="np-card accent-orange np-vak">
    <carbon-document class="np-groot" style="color: var(--np-orange);" />
    <div class="np-kop">Specificeren met wat er ligt</div>
    <small>levert nog geen stabiele versie om te bespreken</small>
  </div>
  <div class="np-card accent-green np-vak">
    <carbon-enterprise class="np-groot" style="color: var(--np-green);" />
    <div class="np-kop">Het IT-landschap van een instelling</div>
    <small>wat het moet kunnen voor wat de sector wil</small>
  </div>
</div>

<div class="np-kern">Kortom: er ontbreekt informatie</div>

<style scoped>
.fill { padding: 0.9rem 1.8rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-citaat { margin: 2.6rem auto 0; text-align: center; }
.np-citaattekst { font-size: 1.9rem; font-weight: 500; font-style: italic; color: var(--np-dark-blue); line-height: 1.2; }
.np-afzender { font-size: 0.86rem; color: var(--np-mid-gray); margin-top: 0.3rem; }
.np-drie { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.9rem; margin-top: 1.8rem; }
.np-vak { padding: 0.8rem 0.9rem; text-align: center; }
.np-vak small { font-size: 0.8rem; display: block; color: var(--np-mid-gray); }
.np-groot { font-size: 1.6rem; color: var(--np-blue); }
.np-kop { font-weight: 700; font-size: 0.92rem; line-height: 1.25; margin-top: 0.2rem; }
.np-kern { margin-top: 1.4rem; text-align: center; font-weight: 700; font-size: 1.05rem; color: var(--np-dark-blue); }
</style>

</div>

<!--
De hoofdvraag waar het SI-team aan de techniekkant mee worstelt: wat moet OKx nu eigenlijk beschrijven
en bouwen? In de woorden van het team: "Ik weet niet wat we bouwen, en daarvoor hebben we de sector
nodig."

Er zijn veel gesprekken gevoerd met leveranciers van planning, studentadministratie en leeromgeving,
met koploperscholen en met informatiemanagers, om hier richting aan te geven. Er blijven veel vragen.
Een daarvan: specificeren met wat er nu ligt, leidt nog niet tot een stabiele versie die partijen
kunnen beoordelen en waarover OKx met hen in gesprek kan. Daarom is de indeling van een release op 28
oktober geparkeerd en ligt de focus op het informatiemodel en de voorbeelden.

De kern: wat moet het uitwisselende IT-landschap van een instelling kunnen om de functionaliteit te
leveren die OKx met de sector wil realiseren? Kortom: er ontbreekt informatie, en die komt uit de
leerroutes en uit de sector.

Vraaggebieden in de kennisbank: wat OKx oplevert en in welke vorm (issues meta #342 en #365), welk
deel een instelling overneemt (issue meta #447), wat een instelling moet kunnen (PR Public #100,
open; issue meta #440).

Bron van de citaten: de opdrachtgever bij het maken van dit deck, 30 oktober 2026 (issue meta #462).
Release-indeling geparkeerd: SI-afstemming 28 oktober (Jamie).
-->

---

<!-- 5. JOCHEM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Jochem van dossier tot diploma

<div class="np-plaatrij">

<img src="/platen/jochem-f2-01-planbaar.png" class="np-plaat" />

<div class="np-kolom">
  <div class="np-card accent-blue np-mini">
    <carbon-map class="np-pic" />
    <div class="np-kop">Acht fasen</div>
    <small>van kwalificatiedossier tot diploma</small>
  </div>
  <div class="np-card accent-orange np-mini">
    <carbon-calendar class="np-pic" style="color: var(--np-orange);" />
    <div class="np-kop">Capaciteitsgestuurd plannen</div>
    <small>keuze op geplande groepen</small>
  </div>
  <div class="np-card accent-green np-mini">
    <carbon-user-multiple class="np-pic" style="color: var(--np-green);" />
    <div class="np-kop">Beoordeling verwerkt</div>
    <small>33 bevindingen</small>
  </div>
  <div class="np-kern">Een school ziet haar eigen werk terug in het model</div>
  <div class="np-bijschrift">Fase 2: de specificatie planbaar gemaakt</div>
  <div class="np-status">Status: ter beoordeling</div>
</div>

</div>

<style scoped>
.fill { padding: 0.9rem 1.1rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 0.35rem; }
.np-plaatrij { display: flex; gap: 1rem; align-items: center; height: calc(100% - 3.2rem); }
.np-plaat { height: 100%; width: auto; max-width: 62%; object-fit: contain; flex: none; border: 1px solid var(--np-light-gray); border-radius: 6px; background: #fff; }
.np-kolom { flex: 1; min-width: 0; }
.np-mini { padding: 0.5rem 0.7rem; margin-bottom: 0.5rem; }
.np-mini small { font-size: 0.78rem; line-height: 1.4; display: block; }
.np-pic { font-size: 1.1rem; color: var(--np-blue); }
.np-kop { font-weight: 700; font-size: 0.86rem; line-height: 1.25; }
.np-bijschrift { font-size: 0.78rem; color: var(--np-mid-gray); margin-top: 0.4rem; }
.np-status { font-size: 0.78rem; color: var(--np-mid-gray); margin-top: 0.3rem; }
.np-kern { font-weight: 700; font-size: 0.9rem; color: var(--np-dark-blue); margin-top: 0.6rem; background: #fff; }
.np-bijschrift, .np-status { background: #fff; display: table; }
</style>

</div>

<!--
De opleiding van Jochem, apothekersassistent in leerroute 1, staat stap voor stap in het
informatiemodel: in acht fasen van kwalificatiedossier tot diploma, 67 platen per processtap. De
plaat links is een stap uit fase 2: de onderwijsontwerper maakt de opleiding planbaar, met
tijdvensters, groepsgrootte, ruimte en docent. Zo ziet een school haar eigen werk terug in de taal
van het model.

Daarnaast staat nu de vorm van plannen die bij de meeste instellingen voorkomt: capaciteitsgestuurd.
De planner plant het keuzedeel vooraf op inzetbare capaciteit en een prognose, en Jochem kiest daarna
een geplande groep. Eerst toonde het voorbeeld alleen vraaggestuurd plannen; een planner die zijn
eigen vorm niet terugvindt, legt het voorbeeld weg.

De 33 bevindingen uit de beoordeling door Niels zijn verwerkt; vijftien vragen staan klaar voor de
kerngroep techniek.

Bron: meta #314 (voorbeelduitwerking, PR ter beoordeling), meta #414 (variant capaciteitsgestuurd, PR ter
beoordeling), meta #404 (varianten mogelijk gemaakt, gemerged 26 oktober).
-->

---

<!-- 6. INFORMATIEMODEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Informatiemodel na de leveranciersronde

<div class="np-plaatrij">

<img src="/platen/informatiemodel-v0.2.jpg" class="np-plaat" />

<div class="np-kolom">
  <div class="np-card accent-blue np-mini">
    <carbon-partnership class="np-pic" />
    <div class="np-kop">Leveranciersronde</div>
    <small>13 van 15 opmerkingen verwerkt</small>
  </div>
  <div class="np-card accent-orange np-mini">
    <carbon-assembly-cluster class="np-pic" style="color: var(--np-orange);" />
    <div class="np-kop">Mbo en hoger onderwijs</div>
    <small>minor naast keuzedeel</small>
  </div>
  <div class="np-card accent-green np-mini">
    <mdi-key-variant class="np-pic" style="color: var(--np-green);" />
    <div class="np-kop">Leeruitkomst</div>
    <small>de sleutel, geschreven volgens de landelijke handleiding</small>
    <div class="np-pil">werkversie, voorstel</div>
  </div>
  <div class="np-kern">Een gemeenschappelijke taal, door leveranciers gelezen</div>
  <div class="np-bijschrift">Versie 0.2, gepubliceerd als voorstel</div>
</div>

</div>

<style scoped>
.fill { padding: 0.9rem 1.1rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 0.35rem; }
.np-plaatrij { display: flex; gap: 0.9rem; align-items: center; height: calc(100% - 3.2rem); }
.np-plaat { height: 100%; width: auto; max-width: 72%; object-fit: contain; flex: none; background: #fff; }
.np-kolom { flex: 1; min-width: 0; }
.np-mini { padding: 0.5rem 0.7rem; margin-bottom: 0.5rem; }
.np-mini small { font-size: 0.78rem; line-height: 1.4; display: block; }
.np-pic { font-size: 1.1rem; color: var(--np-blue); }
.np-kop { font-weight: 700; font-size: 0.86rem; line-height: 1.25; }
.np-pil { margin-top: 0.3rem; display: inline-block; background: #F1F3F5; border-radius: 999px; padding: 0.1rem 0.55rem; font-size: 0.7rem; color: var(--np-dark-blue); }
.np-bijschrift { font-size: 0.78rem; color: var(--np-mid-gray); margin-top: 0.4rem; }
.np-kern { font-weight: 700; font-size: 0.9rem; color: var(--np-dark-blue); margin-top: 0.6rem; background: #fff; }
.np-bijschrift, .np-status { background: #fff; display: table; }
</style>

</div>

<!--
Het informatiemodel is de gemeenschappelijke taal: van kwalificatiekader tot resultaat, in zeven
families van begrippen, de kolommen op de plaat. Leveranciers hebben het in september gelezen en
vijftien opmerkingen geplaatst; dertien daarvan zijn verwerkt. Versie 0.2 staat sinds 27 oktober
in Public, de openbare publicatie van OKx, met 82 objecttypen en 230 relaties. Het is een voorstel.

Het model draagt nu ook het hoger onderwijs: de minor staat naast het keuzedeel, en het
kwalificatiekader kent naast het mbo een tak voor het hoger onderwijs.

De leeruitkomst is de sleutel van het model. Hoe zij geschreven wordt, volgt de landelijke
Handleiding Formuleren leeruitkomsten (NLQF, het Tuning-model), en een script controleert of een
leeruitkomst die vorm draagt. De keuze voor een taxonomie ligt bij de instelling. Dit staat als
voorstel in de kennisbank (meta).

Bron: Public #104 (reviewronde, PR gemerged 13 oktober), Public #131 (versie 0.2, PR gemerged 27
oktober), meta #356 (minor en hoger onderwijs, PR gemerged in meta, in Public via #131), meta #349
(leeruitkomst, PR gemerged in meta).
-->

---

<!-- 7. INBRENG VAN SCHOLEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Inbreng van scholen

<div class="np-plaatvak">
  <img src="/platen/hoofdplaat-1.7a.png" class="np-breed" />
  <div class="np-ring"></div>
</div>

<div class="np-onder">
  <div class="np-card accent-orange np-mini" style="flex: 1;">
    <div class="np-kop"><carbon-chart-line class="np-pic" style="color: var(--np-orange);" /> Casus mboRijnland</div>
    <small>Het keuzesysteem weet wat een student al afrondde</small>
  </div>
  <div class="np-card accent-blue np-mini" style="flex: 1.6;">
    <div class="np-kop"><carbon-map class="np-pic" /> Leerroute 4 tot en met 9</div>
    <div class="np-duimen">
      <img src="/platen/leerroute-4-klein.jpg" />
      <img src="/platen/leerroute-5-klein.jpg" />
      <img src="/platen/leerroute-6-klein.jpg" />
      <img src="/platen/leerroute-7-klein.jpg" />
      <img src="/platen/leerroute-8-klein.jpg" />
      <img src="/platen/leerroute-9-klein.jpg" />
    </div>
  </div>
</div>

<div class="np-status">Status: hoofdplaat ter beoordeling, tekeningen in de kennisbank</div>

<style scoped>
.fill { padding: 0.9rem 1.1rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 0.35rem; }
.np-plaatvak { position: relative; width: 100%; }
.np-breed { width: 100%; display: block; background: #fff; }
.np-ring { position: absolute; left: 73.5%; top: 50%; width: 7%; height: 15%; border: 3px solid var(--np-orange); border-radius: 50%; }
.np-onder { display: flex; gap: 0.7rem; margin-top: 0.5rem; }
.np-mini { padding: 0.45rem 0.7rem; margin: 0; }
.np-mini small { font-size: 0.78rem; line-height: 1.4; display: block; margin-top: 0.2rem; }
.np-pic { font-size: 1rem; color: var(--np-blue); vertical-align: -0.15rem; }
.np-kop { font-weight: 700; font-size: 0.86rem; line-height: 1.25; }
.np-duimen { display: flex; gap: 0.3rem; margin-top: 0.3rem; }
.np-duimen img { width: calc((100% - 1.5rem) / 6); border-radius: 3px; border: 1px solid var(--np-light-gray); }
.np-status { font-size: 0.78rem; color: var(--np-mid-gray); margin-top: 0.35rem; text-align: center; }
</style>

</div>

<!--
Wat scholen inbrengen, landt in de keten. In de gesprekken met koploperscholen bracht mboRijnland een
casus in waarvoor een stroom ontbrak. Op de hoofdplaat, versie 1.7a, is die nu toegevoegd (de
oranje ring): het studentvolgsysteem meldt het studentkeuzesysteem welk resultaat een student al
behaalde op een opleidingsprogramma of onderwijseenheid, zodat het keuzesysteem dat onderdeel uit
de keuzes kan laten.

Onderaan de tekeningen van leerroute 4 tot en met 9 uit de publicatie van Npuls: personaliseren
binnen de instelling, binnen de sector en over sectoren heen, vrije keuze, bundelen en stapelen.
Leerroute 1 tot en met 3 hadden hun tekening al; de persona's bij 4 tot en met 9 volgen.

Bron: meta #400 (stroom in het model, gemerged 26 oktober), Public #133 (hoofdplaat 1.7a, ter
review), meta #448 (tekeningen, gemerged 28 oktober).
-->

---

<!-- 8. INTERACTIEKETENS UITGEWERKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Interactieketens uitgewerkt

<div class="np-vier">
  <div class="np-card accent-blue np-keten">
    <div class="np-kop"><carbon-catalog class="np-pic" /> Aanbod</div>
    <small>van ontwerp tot aanmeldbaar</small>
    <div class="np-getal" style="color: var(--np-blue);">7</div>
    <small>uitwisselingen</small>
  </div>
  <div class="np-card accent-orange np-keten">
    <div class="np-kop"><carbon-user-follow class="np-pic" style="color: var(--np-orange);" /> Instroom</div>
    <small>van aanmelding tot start</small>
    <div class="np-getal" style="color: var(--np-orange);">7</div>
    <small>uitwisselingen</small>
  </div>
  <div class="np-card accent-green np-keten">
    <div class="np-kop"><carbon-user-favorite class="np-pic" style="color: var(--np-green);" /> Keuzedelen</div>
    <small>wat kiesbaar is, met reden</small>
    <div class="np-getal" style="color: var(--np-green);">7</div>
    <small>berichtstromen</small>
  </div>
  <div class="np-card accent-yellow np-keten">
    <div class="np-kop"><carbon-document class="np-pic" style="color: var(--np-dark-blue);" /> Technische specificatie</div>
    <small>proef voor de catalogus</small>
    <div class="np-getal" style="color: var(--np-dark-blue);">22</div>
    <small>operaties</small>
  </div>
</div>

<div class="np-onderkop">Leerroute 1, per fase</div>
<div class="np-fasen"><div class="np-fase" style="border-top-color: #3D68EC;">1 Ontwerpen</div><div class="np-fase" style="border-top-color: #3D68EC;">2 Plannen</div><div class="np-fase" style="border-top-color: #DD784B;">3 Intake</div><div class="np-fase open">4 Roosteren</div><div class="np-fase open">5 Uitvoeren</div><div class="np-fase" style="border-top-color: #00AF81;">6 Kiezen</div><div class="np-fase open">7 Bijsturen</div><div class="np-fase open">8 Examineren</div></div>

<div class="np-voet">Aansluitend op de Open Education API &middot; ter beoordeling</div>

<style scoped>
.fill { padding: 0.9rem 1.6rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-vier { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.8rem; margin-top: 1.2rem; }
.np-keten { padding: 0.7rem 0.8rem; text-align: center; }
.np-keten small { font-size: 0.78rem; display: block; color: var(--np-mid-gray); }
.np-kop { font-weight: 700; font-size: 0.95rem; }
.np-pic { font-size: 1.1rem; color: var(--np-blue); vertical-align: -0.2rem; }
.np-getal { font-size: 2.4rem; font-weight: 700; line-height: 1.1; margin-top: 0.5rem; }
.np-onderkop { margin-top: 1.4rem; font-size: 0.86rem; font-weight: 700; color: var(--np-dark-blue); }
.np-fasen { display: grid; grid-template-columns: repeat(8, 1fr); gap: 0.35rem; margin-top: 0.4rem; }
.np-fase { background: #fff; border: 1px solid var(--np-light-gray); border-top: 4px solid var(--np-blue); border-radius: 4px; padding: 0.35rem 0.3rem; font-size: 0.72rem; font-weight: 600; color: var(--np-dark-blue); text-align: center; line-height: 1.25; }
.np-fase.open { border-top: 4px dashed var(--np-light-gray); color: var(--np-mid-gray); font-weight: 400; }
.np-voet { margin-top: 1rem; text-align: center; font-size: 0.8rem; color: var(--np-mid-gray); }
</style>

</div>

<!--
Wat er sinds 29 september is opgeleverd aan de specificatiekant: drie interactieketens, uitgewerkt tot
op het bericht dat tussen twee systemen gaat, in de volgorde waarin een student ze meemaakt.

Aanbod: van het ontwerp in de curriculumontwerptool tot aanbod dat aanmeldbaar in de catalogus staat;
zeven uitwisselingen, elk met het contract, het bericht en een gegevensmodel (zeven
interactiespecificaties). Instroom: van de aanmelding die binnenkomt tot alles wat klaar moet staan
voordat de student begint; ook zeven. Keuzedelen: de catalogus levert keuzedeelruimte, gepland aanbod
en keuzeregels, en het studentkeuzesysteem berekent wat voor deze student kiesbaar is, met de reden
bij een keuzedeel dat niet kan; elf diensten, zeven berichtstromen, twaalf operaties, casus
apothekersassistent. De proef laat zien dat uit die uitwerking een technische specificatie (een
OpenAPI-document) af te leiden is; voor de onderwijscatalogus zijn dat 22 operaties.

De strook onderaan legt de ketens naast de acht fasen van leerroute 1: aanbod raakt fase 1 en 2,
instroom fase 3, keuzedelen fase 6. Fase 4, 5, 7 en 8 hebben nog geen keten. Die toewijzing is een
afleiding van het team uit de beschrijving van de ketens.

OKx sluit aan op de Open Education API, als laag bovenop een vaste versie van de standaard, zodat OKx
met de standaard in de pas blijft.

Bron: meta #373 (aanbod), meta #387 (instroom), meta #364 (keuzedelen), meta #377 (proef OpenAPI),
alle vier PR ter beoordeling; meta #270 (OEAPI als vaste versie, gemerged 1 oktober).
-->

---

<!-- 9. STAND EN KOERS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Stand en koers

<div class="np-onderkop">Opgeleverd, als voorstel</div>
<div class="np-vier">
  <div class="np-card accent-blue np-klein"><div class="np-kop">Informatiemodel 0.2</div><small>in Public</small></div>
  <div class="np-card accent-orange np-klein"><div class="np-kop">Leerroute 1 uitgewerkt</div><small>67 platen, acht fasen</small></div>
  <div class="np-card accent-green np-klein"><div class="np-kop">Drie interactieketens</div><small>tot op het bericht</small></div>
  <div class="np-card accent-yellow np-klein"><div class="np-kop">Hoofdplaat 1.7a</div><small>met inbreng mboRijnland</small></div>
</div>

<div class="np-onderkop">Koers</div>
<div class="np-pipeline" style="margin-top: 0.35rem; align-items: stretch;">
  <div class="np-step np-stap" style="border-top: 4px solid #3D68EC;"><carbon-user-multiple class="np-icoon" style="color: #3D68EC;" /><strong>Persona</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #DD784B;"><carbon-map class="np-icoon" style="color: #DD784B;" /><strong>Leerroute</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #00AF81;"><carbon-flow class="np-icoon" style="color: #00AF81;" /><strong>Uitwerking</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #F4D74B;"><carbon-search class="np-icoon" style="color: #1B2A6B;" /><strong>Ontbrekende begrippen</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #1B2A6B;"><carbon-data-structured class="np-icoon" style="color: #1B2A6B;" /><strong>Informatiemodel</strong></div>
</div>
<div class="np-terug"><carbon-recycle style="font-size: 0.9rem; vertical-align: -0.15rem;" /> volgende: leerroute 2 en 3, met instellingen en leveranciers</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-top: 0.9rem;">
  <div class="np-card accent-green np-klein"><div class="np-kop"><carbon-arrow-right class="np-icoon2" style="color: #00AF81;" /> Doorzetten</div><small>informatiemodel en voorbeelden</small></div>
  <div class="np-card accent-blue np-klein"><div class="np-kop"><carbon-partnership class="np-icoon2" /> Verbinden met andere pijlers binnen Npuls</div><small>eduXchange, eduID, leeruitkomsten</small></div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.6rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-onderkop { margin-top: 0.9rem; font-size: 0.86rem; font-weight: 700; color: var(--np-dark-blue); }
.np-vier { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.7rem; margin-top: 0.35rem; }
.np-klein { padding: 0.45rem 0.7rem; margin: 0; }
.np-klein small { font-size: 0.78rem; display: block; color: var(--np-mid-gray); }
.np-kop { font-weight: 700; font-size: 0.9rem; line-height: 1.25; }
.np-stap { flex: 1; padding: 0.4rem 0.3rem; align-items: center; justify-content: center; text-align: center; }
.np-stap strong { font-size: 0.8rem; }
.np-icoon { font-size: 1.2rem; }
.np-icoon2 { font-size: 1rem; color: var(--np-blue); vertical-align: -0.15rem; }
.np-terug { margin-top: 0.35rem; text-align: center; font-size: 0.8rem; color: var(--np-mid-gray); border-top: 2px dashed var(--np-light-gray); padding-top: 0.3rem; }
</style>

</div>

<!--
Wat er ligt, is opgeleverd als voorstel. Het informatiemodel versie 0.2 staat in Public, de openbare
publicatie van OKx (PR Public #131, gemerged 27 oktober). De opleiding van Jochem staat in 67 platen
over acht fasen in het informatiemodel (PR meta #314, ter beoordeling). Drie interactieketens zijn
uitgewerkt tot op het bericht (PR meta #373, #387, #364, ter beoordeling). Hoofdplaat 1.7a draagt de
stroom uit de casus van mboRijnland (PR meta #400 gemerged, plaat in PR Public #133 ter beoordeling).
Van de 26 architectuurbesluiten in Public staan er 25 op voorstel en is er een vervangen; de releases
zijn een pre-release (0.0.1) en een concept (0.0.2). De vorm van wat OKx uitbrengt ligt nog open.

De koers: een persona, de leerroute die hij loopt, die leerroute stap voor stap uitgewerkt in het
informatiemodel, en wat daarbij ontbreekt, komt in het informatiemodel. Daarna de volgende leerroute:
leerroute 2 (Larissa) en 3 (Linda), samen met instellingen en leveranciers. Zo kwam bijvoorbeeld de
nominale leerroute boven water. OKx zet door op het informatiemodel en de voorbeelden.

OKx verbindt met de andere pijlers binnen Npuls: eduXchange voor de catalogus, eduID en het inrichten
van toegang, en de werkgroep leeruitkomsten voor de sleutel over de pijlers heen. Binnen de eigen
pijler Leren Zonder Drempels raakt OKx ook de afsprakenset voor toetsafname (OKE) en het project voor
aanmelden, inschrijven en intekenen (AII). De sectorketen staat ter beoordeling in PR meta #300.

Bron: besluiten in Public, Referentiemateriaal/adr/; releases op de releasepagina van
Npuls-OKx/Public; leerroute 2 en 3 als volgende persona's: SI-afstemming 28 oktober en informatiemodel
en ontwerpvragen 29 oktober (Jamie); pijlers: deck alignment Npuls-pijlers 21 september
(presentaties/src/260921_alignment_npuls_pijlers.md); nominale leerroute: PR meta #314, fase 2.
-->
