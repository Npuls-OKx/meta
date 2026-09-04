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

<div class="np-card" style="border-top-color: #0B4F6C; font-size: 1.15rem; line-height: 1.6; margin-top: 1.4rem; max-width: 92%;">
Bouwen we geen stoomtrein door koppelvlakken te standaardiseren? Zeker met de opkomst van AI. Hebben we straks geen vliegende auto's?
</div>

<div style="font-size: 1.05rem; line-height: 1.65; margin-top: 1.2rem; max-width: 88%;">

Een terechte vraag. Een standaardisatietraject duurt jaren, en de wereld eromheen verandert snel. Wie in 1995 het perfecte faxprotocol standaardiseerde, had gelijk en verloor toch.

</div>

</div>

<!--
De vraag van de opdrachtgever, kort. Niet meteen tegenspreken; het faxvoorbeeld
erkent dat de zorg hout snijdt.
-->

---

<!-- 3. HOE WE HET UITZOEKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe we dat uitzoeken

<div style="display: flex; flex-direction: column; gap: 0.45rem; margin-top: 1.1rem; max-width: 86%;">

  <div style="display: flex; align-items: center; gap: 1.1rem; background: #dceffa; border-radius: 8px; padding: 1rem 1.3rem;">
    <div style="flex: 0 0 2.4rem; height: 2.4rem; border-radius: 50%; background: #2E86C1; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.05rem;">1</div>
    <div style="font-size: 1.05rem; line-height: 1.45;"><strong style="color: #2E86C1;">Historie volgen.</strong> Welke lagen kwamen er in dertig jaar bij?</div>
  </div>

  <div style="display: flex; align-items: center; gap: 1.1rem; background: #d9f5ec; border-radius: 8px; padding: 1rem 1.3rem;">
    <div style="flex: 0 0 2.4rem; height: 2.4rem; border-radius: 50%; background: #0E9E7E; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.05rem;">2</div>
    <div style="font-size: 1.05rem; line-height: 1.45;"><strong style="color: #0E9E7E;">Trend eruit halen.</strong> Wat vroeg elke golf?</div>
  </div>

  <div style="display: flex; align-items: center; gap: 1.1rem; background: #ffeed9; border-radius: 8px; padding: 1rem 1.3rem;">
    <div style="flex: 0 0 2.4rem; height: 2.4rem; border-radius: 50%; background: #E8912B; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.05rem;">3</div>
    <div style="font-size: 1.05rem; line-height: 1.45;"><strong style="color: #E8912B;">Ons traject ernaast leggen.</strong> Welke kansen en risico's levert dat op?</div>
  </div>

</div>

<div style="background: #f0e9fb; border-radius: 8px; padding: 1rem 1.3rem; margin-top: 1rem; max-width: 86%; font-size: 1.05rem; line-height: 1.5;">
<strong style="color: #7a5dba;">De uitkomst</strong>: de trend wijst een kant op, en ons traject ligt op die lijn.
</div>

</div>

<!--
Drie stappen, en de uitkomst er alvast bij. De rest van het deck is de
onderbouwing en hoeft niet lineair.
-->

---

<!-- 4. LAAG 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Fundament IT-applicaties, jaren 80 en 90

<div style="font-size: 0.52rem;">

```mermaid
flowchart LR
  U(("Gebruiker"))
  GUI["Gebruikersschil<br/>frontend, GUI"]
  BE["Verwerking<br/>backend, logica en transacties"]
  DB[("Gegevensopslag<br/>database")]
  U -- "invoer en vraag" --> GUI
  GUI -- "verzoek" --> BE
  BE -- "opvragen en schrijven" --> DB
  DB -- "gegevens" --> BE
  BE -- "antwoord" --> GUI
  GUI -- "beeld" --> U
  style U fill:#fff2d6,stroke:#D4A017,color:#3b2a02
  style GUI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BE fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
```

</div>

<div style="font-size: 0.92rem; line-height: 1.5; margin-top: 0.7rem; max-width: 92%;">

Drie blokken en een kringloop. De gebruiker geeft invoer of stelt een vraag aan de gebruikersschil, die stuurt een verzoek naar de verwerking, die haalt of schrijft in de gegevensopslag en stuurt het antwoord terug. Alles binnen een organisatie.

</div>

</div>

<!--
De pijlen zijn het punt, niet de blokken. Elke pijl is een informatiestroom met
een vraag en een antwoord.
-->

---

<!-- 5. LAAG 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Systeem in de jaren 2000

<div style="font-size: 0.46rem;">

```mermaid
flowchart LR
  U(("Gebruiker"))
  GUI["Gebruikersschil<br/>frontend, GUI"]
  BE["Verwerking<br/>backend, logica en transacties"]
  DB[("Gegevensopslag<br/>database")]
  U -- "invoer en vraag" --> GUI
  GUI -- "verzoek" --> BE
  BE -- "opvragen en schrijven" --> DB
  DB -- "gegevens" --> BE
  BE -- "antwoord" --> GUI
  GUI -- "beeld" --> U
  DWH[("Datawarehouse<br/>historie en samenhang")]
  BI["Rapportage<br/>stuurinformatie, BI"]
  M(("Manager"))
  DB -- "periodieke kopie" --> DWH
  DWH -- "cijfers" --> BI
  BI -- "overzicht" --> M
  style U fill:#fff2d6,stroke:#D4A017,color:#3b2a02
  style GUI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BE fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DWH fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style BI fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style M fill:#fff2d6,stroke:#D4A017,color:#3b2a02
```

</div>

<div style="font-size: 0.9rem; line-height: 1.5; margin-top: 0.6rem; max-width: 92%;">

Er komt een tweede kringloop bij. De gegevensopslag levert periodiek een kopie aan het datawarehouse, dat daar historie en samenhang uit haalt, en de rapportage levert een overzicht aan een tweede gebruiker. Nieuwe laag, nieuwe stromen.

</div>

</div>

<!--
Hier begint het patroon: elke nieuwe laag leunt op gegevens uit de laag
eronder, dus de vraag naar uitwisseling wordt groter.
-->

---

<!-- 6. LAAG 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Systeem in de jaren 2010

<div style="font-size: 0.4rem;">

```mermaid
flowchart LR
  U(("Gebruiker"))
  GUI["Gebruikersschil<br/>frontend, GUI"]
  BE["Verwerking<br/>backend, logica en transacties"]
  DB[("Gegevensopslag<br/>database")]
  U -- "invoer en vraag" --> GUI
  GUI -- "verzoek" --> BE
  BE -- "opvragen en schrijven" --> DB
  DB -- "gegevens" --> BE
  BE -- "antwoord" --> GUI
  GUI -- "beeld" --> U
  DWH[("Datawarehouse<br/>historie en samenhang")]
  BI["Rapportage<br/>stuurinformatie, BI"]
  M(("Manager"))
  DB -- "periodieke kopie" --> DWH
  DWH -- "cijfers" --> BI
  BI -- "overzicht" --> M
  LH[("Data lakehouse<br/>opslag met rekenkracht")]
  ML["Modellen<br/>machine learning"]
  EXT["Externe bronnen<br/>platformen, partners"]
  DWH -- "doorstroom" --> LH
  EXT -- "koppeling" --> LH
  LH -- "trainen" --> ML
  ML -- "voorspelling" --> BE
  style U fill:#fff2d6,stroke:#D4A017,color:#3b2a02
  style GUI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BE fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DWH fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style M fill:#fff2d6,stroke:#D4A017,color:#3b2a02
  style LH fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style ML fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  style EXT fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
```

</div>

<div style="font-size: 0.88rem; line-height: 1.45; margin-top: 0.5rem; max-width: 94%;">

Opslag en rekenkracht komen samen in het lakehouse, gevoed door het datawarehouse en door bronnen van buiten de organisatie. Daarop worden modellen getraind, en die sturen een voorspelling terug de verwerking in. De kringloop loopt nu ook buiten de eigen muren.

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

# Systeem nu

<div style="font-size: 0.42rem;">

```mermaid
flowchart LR
  U(("Gebruiker"))
  GUI["Gebruikersschil<br/>frontend, GUI"]
  BE["Verwerking<br/>backend, logica en transacties"]
  DB[("Gegevensopslag<br/>database")]
  U -- "invoer en vraag" --> GUI
  GUI -- "verzoek" --> BE
  BE -- "opvragen en schrijven" --> DB
  DB -- "gegevens" --> BE
  BE -- "antwoord" --> GUI
  GUI -- "beeld" --> U
  DWH[("Datawarehouse<br/>historie en samenhang")]
  BI["Rapportage<br/>stuurinformatie, BI"]
  M(("Manager"))
  DB -- "periodieke kopie" --> DWH
  DWH -- "cijfers" --> BI
  BI -- "overzicht" --> M
  LH[("Data lakehouse<br/>opslag met rekenkracht")]
  ML["Modellen<br/>machine learning"]
  EXT["Externe bronnen<br/>platformen, partners"]
  DWH -- "doorstroom" --> LH
  EXT -- "koppeling" --> LH
  LH -- "trainen" --> ML
  ML -- "voorspelling" --> BE
  AI["AI-laag<br/>assistenten en agents"]
  LH -- "context" --> AI
  ML -- "model" --> AI
  AI -- "bevraagt" --> BE
  AI -- "antwoord en actie" --> GUI
  style U fill:#fff2d6,stroke:#D4A017,color:#3b2a02
  style GUI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BE fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DWH fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BI fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style M fill:#fff2d6,stroke:#D4A017,color:#3b2a02
  style LH fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style ML fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style EXT fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style AI fill:#1D4ED8,stroke:#1D4ED8,color:#ffffff
  linkStyle default stroke:#8a94a3,stroke-width:1.4px
```

</div>

<div class="np-card" style="border-top-color: #D4A017; font-size: 0.9rem; line-height: 1.45; margin-top: 0.5rem; max-width: 94%;">
Elke laag van dertig jaar staat er nog. Wat ze verbindt zijn de pijlen: <strong>informatiestromen, vastgelegd in afspraken</strong>. De AI-laag heeft zelf geen opslag en bestaat volledig bij de gratie van wat die pijlen aanleveren.
</div>

</div>

<!--
Dit is het kantelpunt. De AI-laag heeft zelf geen opslag: hij bestaat bij de
gratie van wat de pijlen aanleveren.
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
