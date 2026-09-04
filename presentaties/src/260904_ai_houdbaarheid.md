---
theme: default
title: "Hoe weten we of we het juiste bouwen?"
info: "OKx naast dertig jaar technologietrend gelegd, met de kansen en risico's die dat oplevert. Voor programma- en projectleiding."
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
  <h1 style="font-size: 2.6rem; line-height: 1.15; margin-bottom: 0.7rem; color: var(--np-ink);">Hoe weten we of we het juiste bouwen?</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 780px; line-height: 1.5;">Dertig jaar technologietrend, en het traject van OKx daarnaast gelegd</p>
  <div style="font-size: 0.9rem; color: var(--np-mid-gray); margin-top: 0.9rem;">Niek Derksen &middot; OKx &middot; 4-9-2026</div>
</div>

<!--
De vraag komt van de opdrachtgever, maar het deck is geen verdediging. Het is
een onderzoek: welke kant wijst de historie op, en ligt ons traject op die
lijn. Zo brengen.
-->

---

<!-- 2. AANLEIDING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aanleiding

<div style="font-size: 1rem; line-height: 1.65; margin-top: 0.7rem; max-width: 88%;">

De opdrachtgever stelde een vraag die het waard is om uit te zoeken.

</div>

<div class="np-card" style="border-top-color: #0B4F6C; font-size: 1.05rem; line-height: 1.6; margin-top: 0.7rem; max-width: 90%;">
Bouwen we geen stoomtrein door koppelvlakken te standaardiseren? Zeker met de opkomst van AI. Hebben we straks geen vliegende auto's?
</div>

<div style="font-size: 0.98rem; line-height: 1.6; margin-top: 0.9rem; max-width: 88%;">

Achter die vraag zit een reele zorg. Een standaardisatietraject duurt jaren, en de wereld eromheen verandert sneller dan ooit. Wie in 1995 het perfecte faxprotocol standaardiseerde, had gelijk en verloor toch.

De vraag is dus terecht. En hij is te beantwoorden, want zulke golven hebben een patroon.

</div>

</div>

<!--
De vraag laten staan zoals hij gesteld is en er niet meteen tegenin gaan. Het
faxvoorbeeld erkent dat de zorg hout snijdt.
-->

---

<!-- 3. HOE WE HET UITZOEKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe we dat uitzoeken

<div style="display: flex; flex-direction: column; gap: 0.35rem; margin-top: 0.9rem; max-width: 84%;">

  <div style="display: flex; align-items: center; gap: 1.1rem; background: #eef2f7; border-left: 6px solid #0B4F6C; border-radius: 4px; padding: 0.9rem 1.2rem;">
    <div style="flex: 0 0 2.2rem; height: 2.2rem; border-radius: 50%; background: #0B4F6C; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700;">1</div>
    <div style="font-size: 1rem; line-height: 1.45;"><strong>De historie volgen.</strong> Welke lagen kwamen er in dertig jaar bij een IT-ecosysteem bij, en wat deden ze met de rest?</div>
  </div>

  <div style="display: flex; align-items: center; gap: 1.1rem; background: #eef4f2; border-left: 6px solid #0E7C66; border-radius: 4px; padding: 0.9rem 1.2rem;">
    <div style="flex: 0 0 2.2rem; height: 2.2rem; border-radius: 50%; background: #0E7C66; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700;">2</div>
    <div style="font-size: 1rem; line-height: 1.45;"><strong>De trend eruit halen.</strong> Wat elke golf vroeg, en of daar een richting in zit.</div>
  </div>

  <div style="display: flex; align-items: center; gap: 1.1rem; background: #fdf3ea; border-left: 6px solid #D4A017; border-radius: 4px; padding: 0.9rem 1.2rem;">
    <div style="flex: 0 0 2.2rem; height: 2.2rem; border-radius: 50%; background: #D4A017; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700;">3</div>
    <div style="font-size: 1rem; line-height: 1.45;"><strong>Ons traject ernaast leggen.</strong> Ligt het werk van OKx op die lijn, en welke kansen en risico's levert dat op?</div>
  </div>

</div>

<div class="np-card" style="border-top-color: #0E7C66; font-size: 0.95rem; line-height: 1.5; margin-top: 0.9rem; max-width: 88%;">
<strong style="color: #0E7C66;">De uitkomst vooraf</strong>: de trend wijst een kant op, en ons traject ligt op die lijn. Dat levert vier kansen op en vier risico's. De vraag aan het eind gaat over waar we op inzetten.
</div>

</div>

<!--
De uitkomst staat er alvast, zodat niemand tot slide 14 hoeft te wachten. De
opbouw daarna is de onderbouwing en hoeft niet lineair.
-->

---

<!-- 4. LAAG 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een systeem, jaren negentig

<div style="font-size: 0.62rem;">

```mermaid
flowchart LR
  UI["Gebruikersschil"] --> APP["Toepassing"]
  APP --> DB[("Gegevensopslag")]
  style UI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style APP fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
```

</div>

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.9rem; max-width: 90%;">

Drie delen. Een scherm waarmee iemand werkt, een toepassing die de logica draait, en een plek waar de gegevens staan. Alles binnen een organisatie, alles onder een dak.

</div>

</div>

<!--
Bewust simpel beginnen. Iedereen in de zaal herkent dit beeld. De volgende
slides voegen er laag voor laag iets aan toe.
-->

---

<!-- 5. LAAG 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de dot-comjaren toevoegden

<div style="font-size: 0.58rem;">

```mermaid
flowchart LR
  UI["Gebruikersschil"] --> APP["Toepassing"]
  APP --> DB[("Gegevensopslag")]
  DB --> DWH[("Datawarehouse")]
  DWH --> BI["Rapportage en<br/>stuurinformatie"]
  style UI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style APP fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DWH fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style BI fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
```

</div>

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.8rem; max-width: 90%;">

Organisaties wilden weten wat er in hun gegevens zat. Er kwam een datawarehouse bij, en daarbovenop rapportage en stuurinformatie. Een nieuwe laag, met een nieuwe vraag: hoe komen gegevens uit de bronsystemen daarin terecht?

</div>

</div>

<!--
Dit is het patroon dat door het hele verhaal loopt: elke nieuwe laag leunt op
gegevens uit de laag eronder. De vraag naar uitwisseling werd dus groter, niet
kleiner.
-->

---

<!-- 6. LAAG 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat cloud, platformen en machine learning toevoegden

<div style="font-size: 0.5rem;">

```mermaid
flowchart LR
  UI["Gebruikersschil"] --> APP["Toepassing"]
  APP --> DB[("Gegevensopslag")]
  DB --> DWH[("Datawarehouse")]
  DWH --> BI["Rapportage en<br/>stuurinformatie"]
  DWH --> LH[("Data lakehouse<br/>met rekenkracht")]
  LH --> ML["Modellen en<br/>voorspellingen"]
  EXT["Externe bronnen:<br/>platformen, sensoren, partners"] --> LH
  style UI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style APP fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DWH fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style LH fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style ML fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style EXT fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
```

</div>

<div style="font-size: 0.92rem; line-height: 1.5; margin-top: 0.7rem; max-width: 92%;">

De hoeveelheid gegevens groeide, en de rekenkracht verhuisde naar de cloud. Het datawarehouse kreeg een opvolger die ook ongestructureerde gegevens aankan en er rekenkracht naast zet. Daarbovenop kwamen modellen en voorspellingen. En er kwamen bronnen bij van buiten de eigen organisatie.

</div>

</div>

<!--
Twee dingen tegelijk: de stapel wordt hoger en hij wordt breder. Externe
bronnen betekenen dat uitwisseling niet meer alleen intern is.
-->

---

<!-- 7. LAAG 4 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat AI toevoegt

<div style="font-size: 0.46rem;">

```mermaid
flowchart LR
  UI["Gebruikersschil"] --> APP["Toepassing"]
  APP --> DB[("Gegevensopslag")]
  DB --> DWH[("Datawarehouse")]
  DWH --> BI["Rapportage en<br/>stuurinformatie"]
  DWH --> LH[("Data lakehouse<br/>met rekenkracht")]
  LH --> ML["Modellen en<br/>voorspellingen"]
  EXT["Externe bronnen:<br/>platformen, sensoren, partners"] --> LH
  LH --> AI["AI-laag:<br/>assistenten en agents"]
  ML --> AI
  AI --> UI
  style UI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style APP fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DWH fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style LH fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style ML fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style EXT fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style AI fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  linkStyle default stroke:#D4A017,stroke-width:2.5px
```

</div>

<div class="np-card" style="border-top-color: #D4A017; font-size: 0.95rem; line-height: 1.5; margin-top: 0.6rem; max-width: 92%;">
Elke laag in dertig jaar is erbij gekomen, geen enkele is verdwenen. En elke nieuwe laag leunt zwaarder op de laag eronder. Wat al die lagen verbindt, is <strong>gegevensuitwisseling</strong>: nog altijd via afspraken over wat er heen en weer gaat.
</div>

</div>

<!--
De pijlen zijn hier goudkleurig: dat is de gegevensuitwisseling, en dat is het
enige element dat in alle vier de plaatjes voorkomt. Dit is het kantelpunt van
het verhaal.
-->

---

<!-- 8. DE TREND -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De trend achter dertig jaar lagen

<div style="font-size: 0.92rem; line-height: 1.5; margin-top: 0.6rem; max-width: 96%;">

| Periode | Wat erbij kwam | Wat dat vroeg van uitwisseling |
|---|---|---|
| Jaren negentig | Datawarehouse en rapportage | Gegevens uit bronsystemen halen, periodiek |
| Dot-com en daarna | Webkoppelingen tussen organisaties | Afspraken tussen partijen in plaats van binnen een organisatie |
| Cloud en platformen | Externe bronnen en rekenkracht op afstand | Continu, over organisatiegrenzen heen |
| Machine learning | Modellen die op veel bronnen tegelijk leunen | Meer bronnen, betere kwaliteit, herleidbaar |
| AI-assistenten en agents | Een laag die alles wil kunnen bevragen | Alles hierboven, plus vindbaar en interpreteerbaar zonder mens |

</div>

<div class="np-card" style="border-top-color: #0E7C66; font-size: 0.95rem; line-height: 1.5; margin-top: 0.7rem; max-width: 94%;">
Elke golf maakte de vraag naar gegevensuitwisseling groter. Geen enkele maakte hem kleiner. AI is de eerste laag die niets eigens opslaat en dus volledig afhankelijk is van wat de lagen eronder aanleveren.
</div>

</div>

<!--
Dit is de richting die uit de historie komt. Wie hem betwist, moet uitleggen
waarom deze golf de eerste is die het patroon omkeert.
-->

---

<!-- 9. ONS TRAJECT ERNAAST -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Ons traject ernaast gelegd

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.6rem; max-width: 92%;">

OKx werkt niet aan een laag. OKx werkt aan de verbinding tussen de lagen: welke gegevens tussen systemen gaan, wat ze betekenen, en wie waarvan de bron is. Dat is precies het element dat in alle vier de platen voorkomt en dat elke golf overleefde.

</div>

<div style="font-size: 0.9rem; line-height: 1.5; margin-top: 0.8rem; max-width: 94%;">

| De trend vraagt | Wat OKx daarvoor maakt |
|---|---|
| Afspraken tussen partijen, niet binnen een organisatie | Koppelingen tussen referentiecomponenten, met een eigenaar per gegeven |
| Bronnen van betere kwaliteit, herleidbaar | Een begrippenkader waarin vastligt wat een leeruitkomst is |
| Vindbaar en interpreteerbaar zonder mens | 24 datamodelschema's, meegeleverd bij elke release |

</div>

<div class="np-card" style="border-top-color: #0E7C66; font-size: 0.95rem; line-height: 1.5; margin-top: 0.8rem; max-width: 92%;">
Een instelling met losse systemen en onduidelijke begrippen heeft niets aan een AI-laag: die kan alleen bevragen wat ontsloten en gedefinieerd is. Meer interconnectie levert sterkere bronnen op, en sterkere bronnen zijn waar AI op aanhaakt.
</div>

</div>

<!--
Dit is het antwoord op de vraag, maar dan als bevinding en niet als
verdediging. De tabel koppelt elke trendeis aan iets dat aantoonbaar bestaat.
-->

---

<!-- 10. KANSEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vier kansen

<div style="font-size: 0.88rem; line-height: 1.45; margin-top: 0.5rem; max-width: 96%;">

| Kans | Waar die vandaan komt |
|---|---|
| De sector als eerste met een specificatie die een agent kan gebruiken | De payloads zijn al machineleesbaar. Wie ook de interactie zo uitgeeft, levert iets dat elders nog niet bestaat |
| Ons eigen tempo als voorbeeld | Twee releases in twee weken, mediaan 9 dagen per issue, met AI in de keten. Dat is een werkwijze die andere standaardisatietrajecten missen |
| De verschuiving werkt in ons voordeel | Bouwen wordt goedkoop, het eens worden over betekenis niet. Precies dat laatste is wat OKx maakt |
| Laat zijn heeft een voordeel | Andere sectoren zijn ons voor. Hun keuzes zijn over te nemen in plaats van uit te vinden |

</div>

<div style="font-size: 0.9rem; color: var(--np-dark-gray); margin-top: 0.8rem; max-width: 92%;">
De eerste twee zijn een positie die we kunnen innemen. De laatste twee zijn meewind die er sowieso is.
</div>

</div>

<!--
Deze slide ontbrak eerst helemaal; het deck signaleerde alleen gaten. De eerste
kans is de interessantste voor de opdrachtgever: dat is iets om over te
vertellen buiten de sector.
-->

---

<!-- 11. RISICO'S -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vier risico's

<div style="font-size: 0.86rem; line-height: 1.45; margin-top: 0.5rem; max-width: 96%;">

| Risico | Stand van zaken | Wat er gebeurt als het blijft |
|---|---|---|
| Doorlooptijd tot een gedragen afspraak | Binnen het project gaat het snel. De tijd tot een afspraak die de sector draagt is niet gemeten; de eerste toets is de review van v0.1.0 | De uitkomst van die review overvalt ons |
| Interactie niet machineleesbaar | De 24 datamodelschema's wel, de interactiepatronen en endpoints niet | Kans 1 gaat naar een andere sector |
| Binding naar OEAPI open | Payloads zijn Nederlandstalig en wijken bewust af; het afleveringsmechanisme is niet belegd | Twee partijen die beide aan de specificatie voldoen, kunnen alsnog niet koppelen |
| Beheerpartij na Npuls | De route ligt vast via AMIGO richting Edustandaard. De partij niet | Alles in dit deck verloopt op de dag dat het programma stopt |

</div>

<div style="font-size: 0.9rem; color: var(--np-dark-gray); margin-top: 0.8rem; max-width: 92%;">
Drie van de vier staan los van AI en waren al bekend. Alleen het tweede wordt door de AI-ontwikkeling urgenter.
</div>

</div>

<!--
Signalering, geen aanklacht. De derde kolom maakt duidelijk waarom het ertoe
doet zonder er een verwijt van te maken.
-->

---

<!-- 12. WAT DE SECTOR MERKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat instellingen en leveranciers hiervan merken

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.5rem; font-size: 0.9rem; line-height: 1.5; max-width: 94%;">
<div style="border-left: 4px solid #0B4F6C; padding-left: 0.9rem;">

<strong style="color: #0B4F6C;">Instellingen</strong>

Een student kan alleen over systemen heen kiezen als die systemen het eens zijn over wat een leeruitkomst is. Dat is wat OKx vastlegt. Wordt de interactie machineleesbaar, dan kan een instelling straks controleren of haar leveranciers zich eraan houden, in plaats van het te moeten geloven.

</div>
<div style="border-left: 4px solid #A8481F; padding-left: 0.9rem;">

<strong style="color: #A8481F;">Leveranciers</strong>

Zij bouwen tegen het koppelvlak van de onderwijscatalogus, met drie koppelingen: naar planning en roostering, naar het studentinformatiesysteem en naar het leermanagementsysteem. Zolang de interactie alleen in tekst staat, kunnen zij niet automatisch valideren.

</div>
</div>

<div class="np-card" style="border-top-color: #D4A017; font-size: 0.9rem; line-height: 1.5; margin-top: 0.9rem; max-width: 94%;">
<strong style="color: #D4A017;">Wat hier niet ter discussie staat</strong>: het detailniveau dat leveranciers toegezegd hebben gekregen voor v0.1.0. Wordt daaraan getornd, dan is dat een apart gesprek met elke leverancier, gevoerd door de projectleiding.
</div>

</div>

<!--
De onderste kaart voorkomt dat een inzetkeuze op de volgende slide gelezen
wordt als het terugdraaien van een toezegging.
-->

---

<!-- 13. WAAR ZETTEN WE OP IN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar zetten we op in?

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.5rem; max-width: 92%;">

Drie richtingen waar de kansen en de risico's samenkomen. Ze kunnen niet alle drie tegelijk voorrang krijgen.

</div>

<div style="font-size: 0.86rem; line-height: 1.45; margin-top: 0.7rem; max-width: 96%;">

| Inzet | Wat het oplevert | Wat het vraagt |
|---|---|---|
| **Tempo** | Een gedragen afspraak voordat de praktijk verder is. Dekt risico 1 | Een norm op doorlooptijd en sturing erop, bij de projectleiding |
| **Machineleesbaar** | Kans 1 verzilveren en risico 2 wegnemen | 3 tot 4 weken werk, plus onderhoud per release. Inschatting |
| **Borging** | Alles behouden na afloop van het programma. Dekt risico 4 | Een gesprek met Edustandaard en Npuls, met de langste doorlooptijd van de drie |

</div>

<div class="np-card" style="border-top-color: #0B4F6C; font-size: 0.92rem; line-height: 1.55; margin-top: 0.8rem; max-width: 94%;">
<strong>Gevraagd</strong>: welke van deze drie voorrang krijgt richting v0.1.0, en of borging daar los van alvast in gang gezet wordt. De binding naar OEAPI hoort bij de technische werkgroep en staat hier daarom niet als keuze.
</div>

</div>

<!--
Geen aanbeveling met ja en nee, want dat is niet aan mij. Wel de drie
richtingen met wat ze kosten, zodat de keuze te maken is. Borging staat er
apart bij omdat die de langste doorlooptijd heeft.
-->

---

<!-- 14. AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
