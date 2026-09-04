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
Geen verdediging maar een onderzoek: welke kant wijst de historie op, en ligt
ons traject op die lijn.
-->

---

<!-- 2. AANLEIDING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aanleiding

<div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1.6rem; max-width: 88%;">

  <div style="background: #ffeed9; border-left: 6px solid #E8912B; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.2rem; line-height: 1.5;">Bouwen we geen stoomtrein door koppelvlakken te standaardiseren?</div>

  <div style="background: #f0e9fb; border-left: 6px solid #7a5dba; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.2rem; line-height: 1.5;">Zeker met de opkomst van AI. Hebben we straks geen vliegende auto's?</div>

</div>

</div>

<!--
De vraag van de opdrachtgever, in twee blokken. Het verhaal eromheen vertel ik:
een standaardisatietraject duurt jaren en de wereld verandert snel; wie in 1995
het perfecte faxprotocol standaardiseerde had gelijk en verloor toch.
-->

---

<!-- 3. CONCLUSIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Conclusie

<div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1.2rem; max-width: 90%;">

  <div style="background: #d9f5ec; border-left: 6px solid #0E9E7E; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.05rem; line-height: 1.5;">Elke technologiegolf van dertig jaar maakte gegevensuitwisseling belangrijker. Geen enkele maakte hem kleiner.</div>

  <div style="background: #dceffa; border-left: 6px solid #2E86C1; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.05rem; line-height: 1.5;">AI is de eerste laag die zelf niets opslaat. Die leunt volledig op wat de lagen eronder aanleveren.</div>

  <div style="background: #ffeed9; border-left: 6px solid #E8912B; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.05rem; line-height: 1.5;">OKx werkt precies daar: aan de afspraken over wat er tussen systemen gaat en wat het betekent.</div>

</div>

</div>

<!--
Conclusie voorop, drie regels. De rest van het deck is de onderbouwing en hoeft
niet lineair doorlopen te worden.
-->

---

<!-- 4. ONDERBOUWING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Onderbouwing

<div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1.3rem; max-width: 86%;">

  <div style="background: #dceffa; border-left: 6px solid #2E86C1; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.05rem; line-height: 1.5;"><strong>Historie volgen.</strong> Welke lagen kwamen er in dertig jaar bij?</div>

  <div style="background: #d9f5ec; border-left: 6px solid #0E9E7E; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.05rem; line-height: 1.5;"><strong>Trend eruit halen.</strong> Wat vroeg elke golf?</div>

  <div style="background: #ffeed9; border-left: 6px solid #E8912B; border-radius: 8px; padding: 1rem 1.3rem; font-size: 1.05rem; line-height: 1.5;"><strong>Ons traject ernaast leggen.</strong> Welke kansen en risico's levert dat op?</div>

</div>

</div>

<!--
De leeswijzer voor de rest van het deck.
-->

---

<!-- 5. LAAG 1 -->
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

<!-- 6. INTERNET -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Het internet: systemen aan elkaar

<div style="font-size: 0.5rem;">

```mermaid
flowchart LR
  subgraph A["Organisatie A"]
    direction TB
    GA["Gebruikersschil"] --> BA["Verwerking"] --> DA[("Opslag")]
  end
  subgraph B["Organisatie B"]
    direction TB
    GB["Gebruikersschil"] --> BB["Verwerking"] --> DB2[("Opslag")]
  end
  subgraph C["Organisatie C"]
    direction TB
    GC["Gebruikersschil"] --> BC["Verwerking"] --> DC[("Opslag")]
  end
  BA <-->|koppeling| BB
  BB <-->|koppeling| BC
  BA <-->|koppeling| BC
  style A fill:#f2f5f8,stroke:#b7c0ca,color:#1f2937
  style B fill:#f2f5f8,stroke:#b7c0ca,color:#1f2937
  style C fill:#f2f5f8,stroke:#b7c0ca,color:#1f2937
  style GA fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BA fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style DA fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style GB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BB fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style DB2 fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style GC fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BC fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style DC fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  linkStyle 6,7,8 stroke:#D4A017,stroke-width:3px
```

</div>

</div>

<!--
Backends aan elkaar hangen. Vanaf hier is het geen systeem meer maar een
ecosysteem van applicaties, en elke verbinding vraagt een afspraak. Drie
organisaties leveren al drie koppelingen op; bij tien zijn het er
vijfenveertig.
-->

---

<!-- 7. LAAG 2 -->
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
  style DWH fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style BI fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style M fill:#fff2d6,stroke:#D4A017,color:#3b2a02
```

</div>


</div>

<!--
Hier begint het patroon: elke nieuwe laag leunt op gegevens uit de laag
eronder, dus de vraag naar uitwisseling wordt groter.
-->

---

<!-- 8. LAAG 3 -->
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
  style LH fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style ML fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style EXT fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
```

</div>


</div>

<!--
Twee dingen tegelijk: de stapel wordt hoger en hij wordt breder. Externe
bronnen betekenen dat uitwisseling niet meer alleen intern is.
-->

---

<!-- 9. LAAG 4 -->
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
  style AI fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
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

<!-- 10. DE TREND -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Steeds meer lagen om te verbinden

<div style="font-size: 0.95rem; line-height: 1.5; margin-top: 0.5rem; max-width: 92%;">

Geteld in de vier platen hiervoor: het aantal blokken groeide, maar het aantal informatiestromen ertussen groeide harder.

</div>

<div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.9rem; max-width: 88%;">

  <div style="display: flex; align-items: center; gap: 1rem;">
    <div style="flex: 0 0 12rem; font-size: 0.92rem;">Jaren 80 en 90</div>
    <div style="flex: 0 0 5.5rem; font-size: 0.85rem; color: var(--np-mid-gray);">4 blokken</div>
    <div style="flex: 1; display: flex; align-items: center; gap: 0.6rem;">
      <div style="height: 1.1rem; width: 28%; background: #94a3b0; border-radius: 3px;"></div>
      <div style="font-size: 0.9rem; font-weight: 700; color: #94a3b0;">6 stromen</div>
    </div>
  </div>
  <div style="display: flex; align-items: center; gap: 1rem;">
    <div style="flex: 0 0 12rem; font-size: 0.92rem;">Jaren 2000</div>
    <div style="flex: 0 0 5.5rem; font-size: 0.85rem; color: var(--np-mid-gray);">7 blokken</div>
    <div style="flex: 1; display: flex; align-items: center; gap: 0.6rem;">
      <div style="height: 1.1rem; width: 42%; background: #2E86C1; border-radius: 3px;"></div>
      <div style="font-size: 0.9rem; font-weight: 700; color: #2E86C1;">9 stromen</div>
    </div>
  </div>
  <div style="display: flex; align-items: center; gap: 1rem;">
    <div style="flex: 0 0 12rem; font-size: 0.92rem;">Jaren 2010</div>
    <div style="flex: 0 0 5.5rem; font-size: 0.85rem; color: var(--np-mid-gray);">10 blokken</div>
    <div style="flex: 1; display: flex; align-items: center; gap: 0.6rem;">
      <div style="height: 1.1rem; width: 60%; background: #0E9E7E; border-radius: 3px;"></div>
      <div style="font-size: 0.9rem; font-weight: 700; color: #0E9E7E;">13 stromen</div>
    </div>
  </div>
  <div style="display: flex; align-items: center; gap: 1rem;">
    <div style="flex: 0 0 12rem; font-size: 0.92rem;">Nu, met AI</div>
    <div style="flex: 0 0 5.5rem; font-size: 0.85rem; color: var(--np-mid-gray);">11 blokken</div>
    <div style="flex: 1; display: flex; align-items: center; gap: 0.6rem;">
      <div style="height: 1.1rem; width: 72%; background: #E8912B; border-radius: 3px;"></div>
      <div style="font-size: 0.9rem; font-weight: 700; color: #E8912B;">17 stromen</div>
    </div>
  </div>

</div>

<div class="np-card" style="border-top-color: #E8912B; font-size: 0.95rem; line-height: 1.5; margin-top: 0.9rem; max-width: 92%;">
En dat is nog binnen een organisatie. Zet er de koppelingen tussen organisaties naast en het loopt hard op. AI verwerkt informatie makkelijker dan ooit, en vergroot daarmee de vraag naar wat er te verwerken valt.
</div>

</div>

<!--
De aantallen komen uit de platen hiervoor, dus ze zijn na te tellen. De
boodschap is de verhouding: blokken maal ruim twee, stromen maal bijna drie.
-->

---

<!-- 11. WAAR OKX ZIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Precies daar werkt OKx

<div style="font-size: 0.52rem;">

```mermaid
flowchart LR
  OC["Onderwijscatalogus"]
  PR["Planning en roostering"]
  SIS["Studentinformatiesysteem"]
  LMS["Leermanagementsysteem"]
  OC <-->|"onderwijsspecificatie"| PR
  OC <-->|"verbintenis en resultaat"| SIS
  OC <-->|"leermiddel"| LMS
  style OC fill:#d9f2e6,stroke:#0E9E7E,stroke-width:2px,color:#0f3b2e
  style PR fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style SIS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style LMS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  linkStyle 0,1,2 stroke:#D4A017,stroke-width:4px
```

</div>

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.4rem; font-size: 0.88rem; line-height: 1.45; max-width: 94%;">
<div style="background: #d9f5ec; border-radius: 8px; padding: 0.85rem 1.1rem;">

<strong style="color: #0E9E7E;">Waar AI bij helpt</strong>

Koppelen wordt goedkoper. Een model leest een schema, schrijft een adapter, en vertaalt tussen formaten. Het bouwwerk eromheen wordt sneller gemaakt dan ooit.

</div>
<div style="background: #ffeed9; border-radius: 8px; padding: 0.85rem 1.1rem;">

<strong style="color: #E8912B;">Waar AI niet bij helpt</strong>

Beleid, afspraken, semantiek en duiding. Wat een systeem uit twee verschillende werelden bedoelt met hetzelfde woord, is geen taalvraag maar een bestuurlijke. Wat er nu is, zijn slimme taalmodellen, geen AGI.

</div>
</div>

</div>

<!--
De gouden pijlen zijn wat OKx maakt: de afspraak over wat er tussen twee
systemen gaat en wat het betekent. Het grootste probleem is systemen uit twee
werelden integreren; daar helpt een model wel bij het bouwen, niet bij het eens
worden.
-->

---

<!-- 12. KANSEN -->
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

<!-- 13. RISICO'S -->
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

<!-- 14. WAT DE SECTOR MERKT -->
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

<!-- 15. WAAR ZETTEN WE OP IN -->
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

<!-- 16. AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
