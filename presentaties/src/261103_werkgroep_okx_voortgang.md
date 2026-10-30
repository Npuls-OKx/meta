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

<!-- 2. JOCHEM -->
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

<!-- 3. INFORMATIEMODEL -->
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

<!-- 4. INBRENG VAN SCHOLEN -->
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

<!-- 5. VAN KETEN NAAR SPECIFICATIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van keten naar specificatie

<div class="np-pipeline" style="margin-top: 3.2rem; align-items: stretch;">
  <div class="np-step blue np-stap">
    <carbon-catalog class="np-groot" />
    <strong>Aanbod</strong>
    <small>van ontwerp tot aanmeldbaar</small>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue np-stap">
    <carbon-user-follow class="np-groot" />
    <strong>Instroom</strong>
    <small>van aanmelding tot start</small>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue np-stap">
    <carbon-user-favorite class="np-groot" />
    <strong>Keuzedelen</strong>
    <small>wat kiesbaar is, met reden</small>
  </div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step green np-stap">
    <carbon-document class="np-groot" style="color: var(--np-green);" />
    <strong>Technische specificatie</strong>
    <small>per systeem, eerst de catalogus</small>
  </div>
</div>

<div class="np-card accent-orange" style="margin-top: 2.4rem; padding: 0.6rem 1rem; text-align: center;">
  <div style="font-weight: 700; font-size: 0.95rem;">Uitgewerkt tot het bericht tussen systemen</div>
</div>

<div style="margin-top: 1rem; font-size: 0.86rem; color: var(--np-dark-blue); text-align: center;">
  Sluit aan op de Open Education API, een bestaande standaard
</div>

<div style="margin-top: 0.6rem; font-size: 0.78rem; color: var(--np-mid-gray); text-align: center;">
  Status: ter beoordeling
</div>

<style scoped>
.fill { padding: 0.9rem 1.8rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-stap { flex: 1; padding: 1.4rem 0.5rem; align-items: center; justify-content: center; text-align: center; }
.np-stap strong { font-size: 0.95rem; }
.np-stap small { font-size: 0.8rem; }
.np-groot { font-size: 1.8rem; color: var(--np-blue); }
</style>

</div>

<!--
Op 29 september stond het doel voor het eerste kwartaal van 2027: per koppeling alle lagen
beschreven. Sindsdien zijn drie ketens uitgewerkt tot op het bericht dat tussen twee systemen gaat,
in de volgorde waarin een student ze meemaakt.

Aanbod: van het ontwerp in de curriculumontwerptool tot aanbod dat aanmeldbaar in de catalogus staat
(zeven interactiespecificaties). Instroom: van de aanmelding die binnenkomt tot alles wat klaar moet
staan voordat de student begint (zeven interactiespecificaties). Keuzedelen: de catalogus levert de
keuzedeelruimte, het geplande aanbod en de keuzeregels, en het studentkeuzesysteem berekent wat voor
deze student kiesbaar is, met de reden bij een keuzedeel dat niet kan; casus apothekersassistent.

Een proef laat zien dat uit die uitwerking per systeem een technische specificatie (een
OpenAPI-document) af te leiden is; voor de onderwijscatalogus zijn dat 22 operaties.

OKx sluit aan op de Open Education API. Op verzoek van de beheerder van die standaard gebeurt dat als een
laag bovenop een vaste versie van de standaard, zodat OKx met de standaard in de pas blijft.

Bron: meta #373 (aanbod), meta #387 (instroom), meta #364 (keuzedelen), meta #377 (proef OpenAPI),
alle vier PR ter beoordeling; meta #270 (OEAPI als vaste versie, gemerged 1 oktober).
-->

---

<!-- 6. STAND EN KOERS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Stand en koers

<div class="np-card accent-blue" style="padding: 0.55rem 1rem; margin-top: 1.2rem;">
  <div style="font-weight: 700; font-size: 1rem;">Hoofdvraag: wat OKx bouwt</div>
  <div style="margin-top: 0.35rem; display: flex; gap: 0.45rem; flex-wrap: wrap;">
    <span class="np-pil">de oplevering</span>
    <span class="np-pil">wat een instelling overneemt</span>
    <span class="np-pil">wat een instelling moet kunnen</span>
  </div>
</div>

<div class="np-pipeline" style="margin-top: 1.2rem; align-items: stretch;">
  <div class="np-step green np-stap"><carbon-user-multiple class="np-icoon" style="color: var(--np-green);" /><strong>Persona</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step green np-stap"><carbon-map class="np-icoon" style="color: var(--np-green);" /><strong>Leerroute</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step green np-stap"><carbon-flow class="np-icoon" style="color: var(--np-green);" /><strong>Uitwerking</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step orange np-stap"><carbon-search class="np-icoon" style="color: var(--np-orange);" /><strong>Ontbrekende begrippen</strong></div>
  <div class="np-arrow" style="align-self: center;">&#8594;</div>
  <div class="np-step blue np-stap"><carbon-data-structured class="np-icoon" /><strong>Informatiemodel</strong></div>
</div>

<div class="np-terug"><carbon-recycle style="font-size: 0.9rem; vertical-align: -0.15rem;" /> volgende leerroute, met instellingen en leveranciers</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-top: 1.2rem;">
  <div class="np-card accent-orange np-mini">
    <carbon-document class="np-icoon" style="color: var(--np-orange);" />
    <div class="np-kop">Alles is voorstel</div>
    <small>uitgave wacht op de vorm</small>
  </div>
  <div class="np-card accent-blue np-mini">
    <carbon-partnership class="np-icoon" />
    <div class="np-kop">Met architecten van Npuls</div>
    <small>naast toetsen (OKE) en aanmelden (AII)</small>
  </div>
</div>

<style scoped>
.fill { padding: 0.9rem 1.6rem; justify-content: flex-start; }
h1 { font-size: 1.75rem !important; line-height: 1.1; margin: 0; }
.np-pil { display: inline-block; background: #F1F3F5; border-radius: 999px; padding: 0.15rem 0.7rem; font-size: 0.8rem; color: var(--np-dark-blue); }
.np-stap { flex: 1; padding: 0.45rem 0.3rem; align-items: center; justify-content: center; text-align: center; }
.np-stap strong { font-size: 0.82rem; }
.np-icoon { font-size: 1.25rem; color: var(--np-blue); }
.np-terug { margin-top: 0.4rem; text-align: center; font-size: 0.8rem; color: var(--np-mid-gray); border-top: 2px dashed var(--np-light-gray); padding-top: 0.3rem; }
.np-mini { padding: 0.5rem 0.8rem; margin: 0; }
.np-mini small { font-size: 0.8rem; display: block; }
.np-kop { font-weight: 700; font-size: 0.9rem; line-height: 1.25; }
</style>

</div>

<!--
Wat er ligt is een voorstel. Van de 26 architectuurbesluiten in Public staan er 25
op voorstel en is er een vervangen; de releases zijn een pre-release (0.0.1) en een concept (0.0.2).
Er is nog geen vastgestelde release, wel een pre-release en een concept; de vorm van wat OKx
uitbrengt ligt zelf nog open.

De hoofdvraag is wat OKx bouwt. In de woorden van het team: "Ik weet niet wat we bouwen, en daarvoor
hebben we de sector nodig." OKx vult de afhankelijkheden in die ontbraken. Drie
vraaggebieden: wat OKx oplevert en in welke vorm (meta #342, #365), welk deel van de afspraken een
instelling overneemt (meta #447), en wat een instelling moet kunnen om een leerroute te realiseren
(Public #100, meta #440).

De route om die vragen te beantwoorden: een persona, de leerroute die hij loopt, die leerroute stap
voor stap uitgewerkt in het informatiemodel, en wat daarbij ontbreekt, komt in het informatiemodel.
Daarna de volgende leerroute. Zo kwam bijvoorbeeld de nominale leerroute boven water. Dat gebeurt
samen met instellingen en leveranciers. OKx zet door op het informatiemodel en de voorbeelden.

Samen met de architecten van Npuls (de architectuursync) wordt de vraag concreet: waar OKx staat in
de keten, naast de afsprakenset voor toetsafname (OKE) en het zusterproject voor aanmelden,
inschrijven en intekenen (AII). De plaat daarvan staat ter beoordeling in meta #300.

Bron: besluiten in Public, Referentiemateriaal/adr/ (status per besluit); releases op de
releasepagina van Npuls-OKx/Public; vraaggebieden in de issues meta #342, #365, #447 en #440 en de
PR Public #100 (open); nominale leerroute: meta #314, fase 2 (PR open); sectorketen: meta #300 (PR
open).
-->
