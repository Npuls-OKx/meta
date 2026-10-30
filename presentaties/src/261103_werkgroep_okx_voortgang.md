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
voorstel; de laatste slide komt daarop terug. Vier onderwerpen: de modeldoorloop van Jochem,
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
.np-breed { width: 100%; max-height: 74%; object-fit: contain; display: block; }
.np-legenda { display: flex; justify-content: center; gap: 1.4rem; font-size: 0.78rem; color: var(--np-dark-blue); margin-top: 0.2rem; }
.np-legenda i { display: inline-block; width: 1.4rem; height: 0.3rem; border-radius: 2px; margin-right: 0.4rem; vertical-align: middle; }
.np-rij { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.7rem; margin-top: 0.4rem; }
.np-mini { padding: 0.3rem 0.7rem; margin: 0; }
.np-mini small { font-size: 0.74rem; line-height: 1.3; display: block; }
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
ruime opzet uit de modeldoorloop; studentadministratie omvat de kernregistratie (OC-KRS) en het
studentvolgsysteem (OC-SVS). In kleur staan alleen de koppelingen vanuit de catalogus in het
vlak onderwijsontwikkeling (OC-P, OC-KRS en OC-LMS) dik in de huisstijlkleuren; de overige stromen
houden de kleur van hun voorlopige koppeling-ID.

Bron: presentaties/src/260929_werkgroep_okx_voortgang.md (techniekblok 29 september), meta #255.
-->

---

<!-- 3. VOORTGANG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voortgang sinds 29 september

<div class="np-card accent-orange np-blok">
  <div class="np-label">Uitgangspunt</div>
  <div class="np-citaat">&ldquo;Een geïsoleerd koppelvlak lost voor een instelling geen probleem op.&rdquo;</div>
  <div class="np-kern">De keten gaat voor het losse koppelvlak</div>
</div>

<div class="np-pijl">&#8595;</div>

<div class="np-card accent-blue np-blok">
  <div class="np-label">Vraag die OKx invult</div>
  <div class="np-kern">Welke schakel van interacties in het IT-landschap van een instelling levert waarde voor instelling en student?</div>
</div>

<div class="np-pijl">&#8595;</div>

<div class="np-pipeline" style="align-items: stretch;">
  <div class="np-step np-stap" style="border-top: 4px solid #00AF81;"><carbon-network-3 class="np-icoon" style="color: #00AF81;" /><strong>Informatiestromen</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #F4D74B;"><carbon-data-structured class="np-icoon" style="color: #1B2A6B;" /><strong>Informatiemodel en modeldoorloop</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #1B2A6B;"><carbon-flow class="np-icoon" style="color: #1B2A6B;" /><strong>Interactieketens en interacties</strong></div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.8rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 1.2rem; }
.np-blok { padding: 0.6rem 1rem; text-align: center; margin: 0; }
.np-label { font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: var(--np-mid-gray); }
.np-citaat { font-size: 1.05rem; font-style: italic; color: var(--np-dark-blue); margin-top: 0.2rem; }
.np-kern { font-size: 1rem; font-weight: 700; color: var(--np-dark-blue); margin-top: 0.25rem; }
.np-pijl { text-align: center; color: var(--np-orange); font-size: 1.3rem; font-weight: 700; line-height: 1; margin: 0.35rem 0; }
.np-stap { flex: 1; padding: 0.55rem 0.4rem; align-items: center; justify-content: center; text-align: center; }
.np-stap strong { font-size: 0.86rem; color: var(--np-dark-blue); }
.np-icoon { font-size: 1.3rem; }
</style>

</div>

<!--
Wat sinds 29 september veranderde, is het uitgangspunt. Op 20 oktober, in de afstemming tussen OKx en
OEAPI, kwam boven: een geïsoleerd koppelvlak lost voor een instelling geen probleem op. Dat Jochem
een keuzedeel kan kiezen, lost geen enkele koppeling alleen op, en ook twee niet. De keten gaat
daarmee voor het losse koppelvlak.

De vraag die OKx nu invult: welke schakel van interacties binnen het IT-landschap van een instelling
levert waarde voor de instelling en de student? Pas daarna komt het specificeren: de
informatiestromen die bij die schakel horen, het informatiemodel en de modeldoorloop die laat zien
welke informatie er beweegt, en zo de interactieketens en de interacties daarbinnen. Bij elke poging
om op de lijntjes van de hoofdplaat te specificeren bleek namelijk niet duidelijk wat daar gebeurt.
Uit een gesprek met een instelling: "Het zijn allemaal blokjes en pijltjes."

Het citaat op de slide is licht ingekort.

Bron (Jamie): afstemming OKx en OEAPI 20 oktober; informatiemodel en koppelingen 2 oktober;
informatiemodel en ontwerpvragen 29 oktober; SI-afstemming 28 oktober. Formulering van de vraag:
de opdrachtgever, 30 oktober 2026 (issue meta #462).
-->

---

<!-- 4. HOOFDVRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoofdvraag

<div class="np-vraag">&ldquo;Wat moet OKx nu eigenlijk beschrijven en bouwen?&rdquo; <span>SI-team, techniek</span></div>

<div class="np-card accent-orange np-hoofd">
  <div class="np-hoofdtekst">Specificeren met wat we nu weten en de randvoorwaardelijke documentatie levert geen stabiele specificatie op</div>
  <div class="np-kortom">Kortom: er ontbreekt informatie</div>
</div>

<div class="np-label">Zo halen we die op</div>
<div class="np-vier">
  <div class="np-card accent-blue np-vak"><carbon-partnership class="np-groot" /><div class="np-kop">Gesprekken met de sector</div><small>instellingen en leveranciers</small></div>
  <div class="np-card accent-green np-vak"><mdi-key-variant class="np-groot" style="color: var(--np-green);" /><div class="np-kop">Leeruitkomsten</div><small>met de werkgroep</small></div>
  <div class="np-card accent-yellow np-vak"><carbon-document-protected class="np-groot" style="color: var(--np-dark-blue);" /><div class="np-kop">Leveranciers</div><small>afspraken over geheimhouding</small></div>
  <div class="np-card np-vak" style="border-top: 4px solid var(--np-dark-blue);"><carbon-flow class="np-groot" style="color: var(--np-dark-blue);" /><div class="np-kop">Zelf fijnmazig uitwerken</div><small>het IT-landschap stap voor stap</small></div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.8rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 0.8rem; }
.np-vraag { text-align: center; font-size: 1.1rem; font-style: italic; color: var(--np-dark-blue); }
.np-vraag span { font-style: normal; font-size: 0.8rem; color: var(--np-mid-gray); margin-left: 0.5rem; }
.np-hoofd { margin-top: 0.8rem; padding: 0.8rem 1.2rem; text-align: center; }
.np-hoofdtekst { font-size: 1.3rem; font-weight: 700; color: var(--np-dark-blue); line-height: 1.3; }
.np-kortom { margin-top: 0.5rem; font-size: 1.05rem; font-weight: 700; color: var(--np-orange); }
.np-label { margin-top: 1rem; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: var(--np-mid-gray); }
.np-vier { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.7rem; margin-top: 0.35rem; }
.np-vak { padding: 0.6rem 0.6rem; text-align: center; margin: 0; }
.np-vak small { font-size: 0.78rem; display: block; color: var(--np-mid-gray); }
.np-groot { font-size: 1.4rem; color: var(--np-blue); }
.np-kop { font-weight: 700; font-size: 0.9rem; line-height: 1.25; margin-top: 0.15rem; }
</style>

</div>

<!--
De hoofdvraag waar het SI-team (systeem en informatie) aan de techniekkant mee worstelt: wat moet OKx nu eigenlijk beschrijven
en bouwen? In de woorden van het team: "Ik weet niet wat we bouwen, en daarvoor hebben we de sector
nodig."

Het hoofdpunt: specificeren met wat we nu weten en met de randvoorwaardelijke documentatie die er
ligt, levert geen stabiele specificatie op, geen versie die partijen kunnen beoordelen en waarover OKx
met hen in gesprek kan. Daarom is de indeling van een release op 28 oktober geparkeerd. Kortom: er
ontbreekt informatie.

Zo halen we die op. Gesprekken met de sector: koploperscholen, informatiemanagers en leveranciers van
planning, studentadministratie en leeromgeving. Leeruitkomsten: met de werkgroep leeruitkomsten, want
de leeruitkomst is de sleutel van het informatiemodel. Leveranciers: afspraken over geheimhouding
(NDA), zodat zij kunnen laten zien hoe hun product werkt. En zelf fijnmazig uitwerken wat ontbreekt:
het IT-landschap van een instelling stap voor stap doorlopen. Dat is de volgende slide.

Bron van de citaten en de aanpak: de opdrachtgever, 30 oktober 2026 (issue meta #462). Release-indeling
geparkeerd: SI-afstemming 28 oktober (Jamie). Leveranciers en NDA: teammeeting 9 oktober en
leveranciersoverleg 12 oktober (Jamie).
-->

---

<!-- 5. VAN PROCESGEBIED NAAR MODELDOORLOOPSTAP -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van procesgebied naar modeldoorloopstap

<div class="np-rij">
  <div class="np-card accent-blue np-niveau">
    <div class="np-label">Procesgebied</div>
    <div class="np-beeld"><span class="np-wrap"><img src="/platen/mora-procesgebieden.png" /><span class="np-kader" style="left: 20%; top: 76%; width: 57%; height: 23%;"></span></span></div>
    <div class="np-naam">Onderwijs ondersteunen</div>
  </div>
  <div class="np-pijl">&#8594;</div>
  <div class="np-card accent-orange np-niveau">
    <div class="np-label">Procesketen</div>
    <div class="np-beeld"><span class="np-wrap"><img src="/platen/mora-procesketen-onderwijslogistiek.png" /><span class="np-kader" style="left: 39.5%; top: 19.5%; width: 48.5%; height: 62.5%;"></span></span></div>
    <div class="np-naam">Onderwijslogistiek</div>
  </div>
  <div class="np-pijl">&#8594;</div>
  <div class="np-card accent-green np-niveau">
    <div class="np-label">Processtap</div>
    <div class="np-beeld"><span class="np-wrap"><img src="/platen/mora-plannen-en-roosteren.png" /><span class="np-kader" style="left: 0.5%; top: 13.5%; width: 27%; height: 18%;"></span></span></div>
    <div class="np-naam">Clusteren leeractiviteiten</div>
  </div>
  <div class="np-pijl">&#8594;</div>
  <div class="np-card accent-yellow np-niveau">
    <div class="np-label">Leerroute-procesbeeld</div>
    <div class="np-beeld"><span class="np-wrap"><img src="/platen/lr1-fase2-informatiestromen.jpg" /></span></div>
    <div class="np-naam">Leerroute 1, fase 2: student en instelling</div>
  </div>
  <div class="np-pijl">&#8594;</div>
  <div class="np-card  np-niveau" style="border-top: 4px solid var(--np-dark-blue);">
    <div class="np-label">Modeldoorloopstap</div>
    <div class="np-beeld"><span class="np-wrap"><img src="/platen/jochem-f2-01-planbaar.png" /></span></div>
    <div class="np-naam">Opleiding van Jochem planbaar</div>
  </div>
</div>

<div class="np-laag"><span>MORA</span><span>OKx-oplossingsmodel en producten</span></div>

<div class="np-onder">
  <div class="np-card np-lus" style="border-top: 4px solid #C2577A;">
    <carbon-renew class="np-groot" style="color: #C2577A;" />
    <div><div class="np-kop">Toetsen en verifiëren</div><small>op de instellingsvloer, steeds opnieuw</small></div>
  </div>
  <div class="np-pijl">&#8594;</div>
  <div class="np-card np-lus" style="border-top: 4px solid var(--np-dark-blue);">
    <carbon-data-structured class="np-groot" style="color: var(--np-dark-blue);" />
    <div><div class="np-kop">Informatiemodel bijgewerkt</div><small>nieuwe begrippen en relaties</small></div>
  </div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.2rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0 0 0.8rem; }
.np-rij { display: flex; align-items: stretch; gap: 0.3rem; }
.np-niveau { flex: 1; min-width: 0; padding: 0.4rem 0.4rem; margin: 0; text-align: center; display: flex; flex-direction: column; }
.np-label { font-size: 0.64rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; color: var(--np-mid-gray); }
.np-beeld { margin: 0.3rem 0; flex: 1; display: flex; align-items: center; justify-content: center; height: 7.5rem; }
.np-wrap { position: relative; display: inline-block; line-height: 0; }
.np-wrap img { max-width: 100%; max-height: 7.5rem; display: block; border-radius: 3px; border: 1px solid var(--np-light-gray); }
.np-kader { position: absolute; border: 3px solid var(--np-orange); border-radius: 6px; }
.np-naam { font-size: 0.78rem; font-weight: 700; color: var(--np-dark-blue); line-height: 1.25; }
.np-pijl { align-self: center; color: var(--np-orange); font-size: 1.2rem; font-weight: 700; }
.np-laag { display: grid; grid-template-columns: 3fr 2fr; gap: 0.6rem; margin-top: 0.35rem; }
.np-laag span { border-top: 2px solid var(--np-light-gray); padding-top: 0.2rem; font-size: 0.72rem; color: var(--np-mid-gray); text-align: center; }
.np-onder { display: flex; justify-content: center; align-items: center; gap: 0.6rem; margin-top: 0.9rem; }
.np-lus { display: flex; align-items: center; gap: 0.7rem; padding: 0.55rem 1rem; margin: 0; min-width: 17rem; }
.np-lus small { font-size: 0.8rem; display: block; color: var(--np-mid-gray); }
.np-groot { font-size: 1.7rem; }
.np-kop { font-weight: 700; font-size: 0.92rem; color: var(--np-dark-blue); }
</style>

</div>

<!--
Zo ziet zelf fijnmazig uitwerken eruit. MORA, de referentiearchitectuur voor het mbo, deelt het werk
van een instelling in procesgebieden in; hier onderwijs ondersteunen. Daaronder loopt de procesketen
onderwijslogistiek, met daarin de processen en hun processtappen; het kader staat om plannen en
roosteren. Een van de processtappen daarin is clusteren leeractiviteiten.

Die processtappen verdiept OKx met het procesbeeld van de leerroute, per student en per instelling:
hier fase 2 van leerroute 1, met de informatiestromen die in die fase lopen. Dat procesbeeld valt onder
het OKx-oplossingsmodel en onze producten. Pas daaronder komt de modeldoorloopstap: voor de opleiding
van Jochem, apothekersassistent, maakt de onderwijsontwerper de opleiding planbaar, met tijdvensters,
groepsgrootte, ruimte en docent; de catalogus clustert leeronderdelen tot logistieke eenheden. Over de
hele leerroute zijn dat 67 platen in acht fasen. Een conceptuele processtap leidt zo tot een hele boel
detail.

Elke modeldoorloopstap wordt getoetst en geverifieerd op de instellingsvloer, met de koploperscholen,
en dat gaat in rondes: de 33 bevindingen uit de beoordeling door Niels zijn er zo een. Wat daaruit komt,
werkt het beeld van het informatiemodel bij: begrippen en relaties die de doorloop blootlegt, komen in
het model. Daarnaast staat de capaciteitsgestuurde planningsvorm, die bij de meeste instellingen
voorkomt (PR meta #414).

Demo: de modeldoorloop in PR meta #314.

Bron: MORA, procesketen onderwijslogistiek (mora.mbodigitaal.nl, view van 11 oktober 2026) en het
MORA-hoofdprocesmodel; leerroute 1 fase 2: OKx_LR1_informatiestromen_v20260526_f2
(architecture/docs/specificatie/leerroute-uitwerking/img/); PR meta #314 (modeldoorloop, ter
beoordeling), PR meta #414 (variant capaciteitsgestuurd, ter beoordeling). Opbouw van procesgebied
tot modeldoorloopstap: de opdrachtgever, 30 oktober 2026 (issue meta #462).
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

<!-- 8. INTERACTIEKETENS IN CONCEPT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Interactieketens in concept

<div class="np-kern">Elk inzicht scherpt het eindproduct aan</div>

<div class="np-drie">
  <div class="np-card accent-blue np-keten"><div class="np-kop"><carbon-catalog class="np-pic" /> Aanbod</div><small>van ontwerp tot aanmeldbaar</small></div>
  <div class="np-card accent-orange np-keten"><div class="np-kop"><carbon-user-follow class="np-pic" style="color: var(--np-orange);" /> Instroom</div><small>van aanmelding tot start</small></div>
  <div class="np-card accent-green np-keten"><div class="np-kop"><carbon-user-favorite class="np-pic" style="color: var(--np-green);" /> Keuzedelen</div><small>wat kiesbaar is, met reden</small></div>
</div>

<div class="np-onderkop">Leerroute 1, per fase</div>
<div class="np-fasen"><div class="np-fase" style="border-top-color: #3D68EC;">1 Ontwerpen</div><div class="np-fase" style="border-top-color: #3D68EC;">2 Plannen</div><div class="np-fase" style="border-top-color: #DD784B;">3 Intake</div><div class="np-fase open">4 Roosteren</div><div class="np-fase open">5 Uitvoeren</div><div class="np-fase" style="border-top-color: #00AF81;">6 Kiezen</div><div class="np-fase open">7 Bijsturen</div><div class="np-fase open">8 Examineren</div></div>

<div class="np-card accent-yellow np-weg">
  <div class="np-kop">Nog verre van implementatiewaardig</div>
  <small>eerst intern vormgeven, daarna review met de sector, over twee maanden</small>
</div>

<style scoped>
.fill { padding: 0.9rem 1.6rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-kern { margin-top: 0.6rem; font-size: 1.1rem; font-weight: 700; color: var(--np-dark-blue); text-align: center; }
.np-drie { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin-top: 0.9rem; }
.np-keten { padding: 0.6rem 0.8rem; text-align: center; margin: 0; }
.np-keten small { font-size: 0.8rem; display: block; color: var(--np-mid-gray); }
.np-kop { font-weight: 700; font-size: 0.95rem; }
.np-pic { font-size: 1.1rem; color: var(--np-blue); vertical-align: -0.2rem; }
.np-pil { display: inline-block; margin-top: 0.4rem; background: #F1F3F5; border-radius: 999px; padding: 0.1rem 0.6rem; font-size: 0.74rem; color: var(--np-dark-blue); }
.np-onderkop { margin-top: 1.1rem; font-size: 0.84rem; font-weight: 700; color: var(--np-dark-blue); }
.np-fasen { display: grid; grid-template-columns: repeat(8, 1fr); gap: 0.35rem; margin-top: 0.35rem; }
.np-fase { background: #fff; border: 1px solid var(--np-light-gray); border-top: 4px solid var(--np-blue); border-radius: 4px; padding: 0.3rem 0.2rem; font-size: 0.72rem; font-weight: 600; color: var(--np-dark-blue); text-align: center; }
.np-fase.open { border-top: 4px dashed var(--np-light-gray); color: var(--np-mid-gray); font-weight: 400; }
.np-weg { margin-top: 1.1rem; padding: 0.6rem 1rem; text-align: center; }
.np-weg small { font-size: 0.82rem; display: block; color: var(--np-dark-gray); margin-top: 0.2rem; }
</style>

</div>

<!--
Elk inzicht uit de modeldoorloop en de gesprekken gebruiken we om het eindproduct aan te scherpen. Voor
drie onderdelen van leerroute 1 ligt een eerste concept van de interactieketens: aanbod (van ontwerp
tot aanmeldbaar aanbod), instroom (van aanmelding tot de start) en keuzedelen (wat voor deze student
kiesbaar is, met de reden erbij). In de strook: aanbod raakt fase 1 en 2, instroom fase 3,
keuzedelen fase 6; de andere fasen hebben nog geen keten. Die toewijzing is indicatief, een
afleiding van het team.

Deze ketens zijn nog verre van implementatiewaardig. We geven ze nu intern vorm, zodat we ze tegen
leveranciers en instellingen kunnen aanhouden. Het doel is over ongeveer twee maanden een eerste
review.

Bron: PR meta #373 (aanbod), #387 (instroom), #364 (keuzedelen), alle drie ter beoordeling; de proef met
een technische specificatie per systeem staat in PR meta #377. Doel van twee maanden: de opdrachtgever,
30 oktober 2026 (issue meta #462).
-->

---

<!-- 9. SAMENVATTING TECHNIEK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Samenvatting techniek

<div class="np-onderkop">Opgeleverd, als voorstel</div>
<div class="np-vier">
  <div class="np-card accent-blue np-klein"><div class="np-kop">Informatiemodel 0.2</div><small>in Public</small></div>
  <div class="np-card accent-orange np-klein"><div class="np-kop">Leerroute 1 uitgewerkt</div><small>67 platen, acht fasen</small></div>
  <div class="np-card accent-green np-klein"><div class="np-kop">Interactieketens</div><small>eerste concept</small></div>
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
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #C2577A;"><carbon-network-3 class="np-icoon" style="color: #C2577A;" /><strong>Interactieketen</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step np-stap" style="border-top: 4px solid #6B7280;"><carbon-document class="np-icoon" style="color: #374151;" /><strong>Interactie&shy;specificaties</strong></div>
</div>
<div class="np-terug"><carbon-recycle style="font-size: 0.9rem; vertical-align: -0.15rem;" /> volgende: leerroute 2 en 3, met instellingen en leveranciers</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-top: 0.9rem;">
  <div class="np-card accent-orange np-klein"><div class="np-kop"><carbon-flag class="np-icoon2" style="color: #DD784B;" /> Doel over twee maanden</div><small>reviewbare interactieketenspecificatie, met leveranciers</small></div>
  <div class="np-card accent-blue np-klein"><div class="np-kop"><carbon-partnership class="np-icoon2" /> Verbinden met andere pijlers binnen Npuls</div><small>eduXchange, eduID, leeruitkomsten</small></div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.4rem; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-onderkop { margin-top: 0.8rem; font-size: 0.84rem; font-weight: 700; color: var(--np-dark-blue); }
.np-vier { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.7rem; margin-top: 0.35rem; }
.np-klein { padding: 0.45rem 0.7rem; margin: 0; }
.np-klein small { font-size: 0.78rem; display: block; color: var(--np-mid-gray); }
.np-kop { font-weight: 700; font-size: 0.88rem; line-height: 1.25; }
.np-stap { flex: 1; padding: 0.4rem 0.2rem; align-items: center; justify-content: center; text-align: center; }
.np-stap strong { font-size: 0.72rem; color: var(--np-dark-blue); line-height: 1.2; }
.np-icoon { font-size: 1.1rem; }
.np-icoon2 { font-size: 1rem; color: var(--np-blue); vertical-align: -0.15rem; }
.np-terug { margin-top: 0.35rem; text-align: center; font-size: 0.8rem; color: var(--np-mid-gray); border-top: 2px dashed var(--np-light-gray); padding-top: 0.3rem; }
</style>

</div>

<!--
Samenvatting van de voortgang aan de techniekkant. Opgeleverd, als voorstel: het informatiemodel
versie 0.2 in Public, de openbare publicatie van OKx (PR Public #131, gemerged 27 oktober); de
opleiding van Jochem in 67 platen over acht fasen (PR meta #314, ter beoordeling); een eerste concept
van de interactieketens voor drie onderdelen (PR meta #373, #387, #364, ter beoordeling); hoofdplaat
1.7a met de stroom uit de casus van mboRijnland (PR meta #400 gemerged, plaat in PR Public #133 ter
beoordeling). Van de 26 architectuurbesluiten in Public staan er 25 op voorstel en is er een vervangen;
de releases zijn een pre-release (0.0.1) en een concept (0.0.2).

De koers: een persona, de leerroute die hij loopt, die leerroute stap voor stap uitgewerkt, de
begrippen die daarbij ontbreken, het informatiemodel, en dan de interactieketen op basis van waarde
voor student en instelling, met de interactiespecificaties als laatste stap. Daarna de volgende
leerroute: 2 (Larissa) en 3 (Linda), samen met instellingen en leveranciers.

Het doel: over twee maanden een reviewbare interactieketenspecificatie die ter review naar de
leveranciers gaat. De oplevering van de specificaties zelf is getemporiseerd tot de zomer van 2027;
dat licht de projectleider toe (herijking 26 oktober). Ondertussen blijft OKx verbinden met de andere pijlers binnen Npuls: eduXchange
voor de catalogus, eduID en het inrichten van toegang, en de werkgroep leeruitkomsten. Binnen de eigen
pijler Leren Zonder Drempels raakt OKx de afsprakenset voor toetsafname (OKE) en het project voor
aanmelden, inschrijven en intekenen (AII). Deze richting zetten we door.

Bron: besluiten in Public, Referentiemateriaal/adr/; releases op de releasepagina van
Npuls-OKx/Public; leerroute 2 en 3: SI-afstemming 28 oktober en informatiemodel en ontwerpvragen 29
oktober (Jamie); pijlers: deck alignment Npuls-pijlers 21 september; doel van twee maanden: de
opdrachtgever, 30 oktober 2026 (issue meta #462).
-->
