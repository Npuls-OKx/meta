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


<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">De schooladministratie op een server in de kelder. Een applicatie, een gebruiker, een gebouw.</div>
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

<div style="font-size: 0.44rem;">

```mermaid
flowchart LR
  subgraph SA["Applicatie A"]
    direction TB
    GA["Gebruikersschil"] --> BA["Verwerking"]
    BA --> DA[("Opslag")]
    BA --> PA["API"]
  end
  subgraph SB["Applicatie B"]
    direction TB
    GB["Gebruikersschil"] --> BB["Verwerking"]
    BB --> DB[("Opslag")]
    BB --> PB["API"]
  end
  subgraph SC["Applicatie C"]
    direction TB
    GC["Gebruikersschil"] --> BC["Verwerking"]
    BC --> DC[("Opslag")]
    BC --> PC["API"]
  end
  PA <-->|"verzoek en antwoord"| PB
  PB <-->|"verzoek en antwoord"| PC
  PA <-->|"verzoek en antwoord"| PC
  style SA fill:#f7f9fb,stroke:#b7c0ca,color:#1f2937
  style GA fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BA fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DA fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style PA fill:#d9f2e6,stroke:#0E9E7E,stroke-width:2px,color:#0f3b2e
  style SB fill:#f7f9fb,stroke:#b7c0ca,color:#1f2937
  style GB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DB fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style PB fill:#d9f2e6,stroke:#0E9E7E,stroke-width:2px,color:#0f3b2e
  style SC fill:#f7f9fb,stroke:#b7c0ca,color:#1f2937
  style GC fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style BC fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style DC fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style PC fill:#d9f2e6,stroke:#0E9E7E,stroke-width:2px,color:#0f3b2e
  linkStyle 9,10,11 stroke:#D4A017,stroke-width:3.5px
```

</div>

<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">iDEAL. De webwinkel praat met je bank, zonder dat die twee ooit samen zijn gebouwd.</div>
</div>

</div>

<!--
De API is de rand van de applicatie en praat met de API van een ander. Drie
applicaties leveren drie koppelingen op; bij tien zijn het er vijfenveertig.
Elke lijn is een afspraak.
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



<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">De bonuskaart. De supermarkt weet wat er verkocht is en stuurt daarop bij.</div>
</div>
</div>

<!--
Hier begint het patroon: elke nieuwe laag leunt op gegevens uit de laag
eronder, dus de vraag naar uitwisseling wordt groter.
-->

---

<!-- 8. ECOSYSTEEM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van applicatie naar ecosysteem van applicaties

<div style="font-size: 0.42rem;">

```mermaid
flowchart LR
  subgraph ORG["Een organisatie"]
    direction LR
    KERN["Kernapplicatie"]
    VERKOOP["Verkoopplatform"]
    RAPPORT["Rapportage-app"]
    MARKET["Marketinginzichten"]
    SOCIAL["Socialmediaplatform"]
  end
  KERN -->|API| VERKOOP
  KERN -->|API| RAPPORT
  KERN -->|API| MARKET
  VERKOOP -->|API| RAPPORT
  VERKOOP -->|API| MARKET
  MARKET -->|API| SOCIAL
  RAPPORT -->|API| MARKET
  style ORG fill:#f2f5f8,stroke:#b7c0ca,color:#1f2937
  style KERN fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style VERKOOP fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style MARKET fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style RAPPORT fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  style SOCIAL fill:#d9f2e6,stroke:#0E9E7E,color:#0f3b2e
  linkStyle 0,1,2,3,4,5,6 stroke:#D4A017,stroke-width:3px
```

</div>

<div class="np-card" style="border-top-color: #D4A017; font-size: 0.92rem; line-height: 1.5; margin-top: 0.6rem; max-width: 92%;">
Vijf applicaties, zeven koppelingen. Niet meer een applicatie met een paar lagen, maar tientallen applicaties naast elkaar, elk met eigen verwerking en opslag.
</div>


<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">Een instelling met tientallen pakketten naast elkaar: rooster, leeromgeving, studentinformatie, aanmeldportaal, wallet.</div>
</div>
</div>

<!--
Dit is inmiddels het normale beeld bij een instelling, en het is de
voedingsbodem voor de laag die hierna komt: het lakehouse voedt zich uit dit
ecosysteem.
-->

---

<!-- 9. TWEE WERELDEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Ecosystemen koppelen aan ecosystemen

<div style="font-size: 0.56rem;">

```mermaid
flowchart LR
  subgraph ONDERWIJS["Onderwijsinstelling"]
    direction TB
    OC["Onderwijscatalogus"]
    SIS["Studentinformatiesysteem"]
    LMS["Leeromgeving"]
  end
  subgraph OVERHEID["Uitvoeringsorganisatie"]
    direction TB
    INSCHR["Inschrijvingenregister"]
    RECHT["Rechtenadministratie"]
  end
  subgraph VERVOER["Vervoerder"]
    direction TB
    KAART["Kaartsysteem"]
    REIS["Reisadministratie"]
  end
  SIS <-->|"koppeling"| INSCHR
  RECHT <-->|"koppeling"| KAART
  OC <-->|"koppeling"| RECHT
  style ONDERWIJS fill:#f7f9fb,stroke:#b7c0ca,color:#1f2937
  style OVERHEID fill:#f7f9fb,stroke:#b7c0ca,color:#1f2937
  style VERVOER fill:#f7f9fb,stroke:#b7c0ca,color:#1f2937
  style OC fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style SIS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style LMS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style INSCHR fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style RECHT fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style KAART fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style REIS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  linkStyle 0,1,2 stroke:#D4A017,stroke-width:3.5px
```

</div>

<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">Het studentenreisproduct. Instelling, uitvoeringsorganisatie en vervoerder moeten het eens zijn over wie student is en vanaf wanneer.</div>
</div>

</div>

<!--
Niet meer twee applicaties, maar drie ecosystemen uit drie verschillende
domeinen die elkaars gegevens nodig hebben. Elk heeft zijn eigen taal, eigen
regels en eigen belangen.
-->

---

<!-- 10. HETZELFDE WOORD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hetzelfde woord, een andere betekenis

<div style="display: flex; align-items: stretch; gap: 1rem; margin-top: 1rem; max-width: 96%;">

  <div style="flex: 1; background: #dceffa; border-radius: 10px; padding: 1.1rem 1.3rem;">
    <div style="font-size: 0.85rem; color: #2E86C1; font-weight: 700;">Onderwijsontwerper</div>
    <div style="font-size: 1.35rem; font-weight: 700; margin: 0.35rem 0; color: #1f2937;">groep</div>
    <div style="font-size: 0.95rem; line-height: 1.45;">Studenten die samen dezelfde leeruitkomst nastreven, ongeacht waar en wanneer.</div>
  </div>

  <div style="flex: 0 0 4rem; display: flex; align-items: center; justify-content: center; font-size: 2.6rem; font-weight: 700; color: #A8481F;">&ne;</div>

  <div style="flex: 1; background: #ffeed9; border-radius: 10px; padding: 1.1rem 1.3rem;">
    <div style="font-size: 0.85rem; color: #E8912B; font-weight: 700;">Planner</div>
    <div style="font-size: 1.35rem; font-weight: 700; margin: 0.35rem 0; color: #1f2937;">groep</div>
    <div style="font-size: 0.95rem; line-height: 1.45;">Het aantal studenten dat op dat tijdstip in dat lokaal past.</div>
  </div>

</div>

<div class="np-card" style="border-top-color: #A8481F; font-size: 1rem; line-height: 1.55; margin-top: 1rem; max-width: 96%;">
Twee systemen die allebei werken, en toch niet samenwerken. De leiding leggen is techniek. Het eens worden over wat het woord betekent, is dat niet.
</div>

</div>

<!--
Dit is het hele probleem in een plaatje. Het werkt met elk woord: klant,
deelnemer, periode, resultaat. Zolang dit niet vastligt, levert elke koppeling
een nieuw misverstand op.
-->

---

<!-- 11. LAAG 3 -->
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



<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">Spotify. Wat je te horen krijgt komt uit modellen die op miljarden luisterbeurten zijn getraind.</div>
</div>
</div>

<!--
Twee dingen tegelijk: de stapel wordt hoger en hij wordt breder. Externe
bronnen betekenen dat uitwisseling niet meer alleen intern is.
-->

---

<!-- 12. LAAG 4 -->
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


<div style="display:flex; align-items:center; gap:0.7rem; margin-top:0.6rem; max-width:92%;">
  <div style="background:#ffeed9; color:#8a5a12; font-weight:700; font-size:0.8rem; padding:0.25rem 0.7rem; border-radius:999px;">Voorbeeld</div>
  <div style="font-size:0.92rem; line-height:1.4;">Een assistent die je hele reis boekt terwijl jij een zin typt.</div>
</div>
</div>

<!--
Dit is het kantelpunt. De AI-laag heeft zelf geen opslag: hij bestaat bij de
gratie van wat de pijlen aanleveren.
-->

---

<!-- 13. DE TREND -->
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

<!-- 14. WAAR OKX ZIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat OKx doet

<div style="font-size: 0.5rem;">

```mermaid
flowchart LR
  OC["Onderwijscatalogus"]
  PR["Planning en roostering"]
  SIS["Studentinformatiesysteem"]
  LMS["Leeromgeving"]
  OC <-->|"specificatiestructuur<br/>en aanbod"| PR
  OC <-->|"specificatiestructuur,<br/>verbintenis en resultaat"| SIS
  OC <-->|"specificatiestructuur<br/>en leermiddel"| LMS
  style OC fill:#d9f2e6,stroke:#0E9E7E,stroke-width:2px,color:#0f3b2e
  style PR fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style SIS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  style LMS fill:#e9edf2,stroke:#94a3b0,color:#1f2937
  linkStyle 0,1,2 stroke:#D4A017,stroke-width:4px
```

</div>

<div class="np-card" style="border-top-color: #0E9E7E; font-size: 0.98rem; line-height: 1.55; margin-top: 0.7rem; max-width: 94%;">
OKx wijst de punten aan waar systemen elkaar raken, en legt vast wat er over zo'n punt gaat en wat het betekent. Niet willekeurig, maar op basis van wat een student moet kunnen: kiezen, inschrijven, leren, resultaat halen.
</div>

</div>

<!--
Drie koppelingen op een koppelvlak, dat van de onderwijscatalogus. De gouden
lijnen zijn het werk. De doelen eronder komen uit de requirementsboom.
-->

---

<!-- 15. WAT DAT MOGELIJK MAAKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat dat straks mogelijk maakt

<div style="display:flex; gap:1rem; margin-top:0.9rem; max-width:96%;">

  <div style="flex:1; background:#d9f5ec; border-radius:10px; padding:0.9rem 1rem; display:flex; flex-direction:column; align-items:center;">
    <div style="font-size:0.95rem; font-weight:700; color:#0E9E7E; margin-bottom:0.6rem;">Onderwijsontwerp</div><div style="font-size:0.68rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:#0E9E7E; opacity:0.75; margin:-0.4rem 0 0.55rem 0; text-align:center;">vraag naast aanbod</div>
    <div style="width:100%;"><div style="background:#fff; border:1px solid #0E9E7E; border-radius:6px; padding:0.3rem 0.6rem; font-size:0.78rem; margin-bottom:0.25rem; text-align:center;">Ons aanbod in leeruitkomsten</div><div style="background:#fff; border:1px solid #0E9E7E; border-radius:6px; padding:0.3rem 0.6rem; font-size:0.78rem; margin-bottom:0.25rem; text-align:center;">Gevraagde vaardigheden uit de markt</div></div>
    <div style="font-size:1.1rem; color:#0E9E7E; line-height:1;">&#9660;</div>
    <div style="background:#0E9E7E; color:#fff; border-radius:6px; padding:0.35rem 0.9rem; font-size:0.85rem; font-weight:700; margin:0.25rem 0;">Agent</div>
    <div style="font-size:1.1rem; color:#0E9E7E; line-height:1;">&#9660;</div>
    <div style="font-size:0.85rem; text-align:center; line-height:1.35; margin-top:0.25rem;">Waar sluit ons aanbod niet aan op de markt, en wat ontwikkelen we bij</div>
  </div>

  <div style="flex:1; background:#dceffa; border-radius:10px; padding:0.9rem 1rem; display:flex; flex-direction:column; align-items:center;">
    <div style="font-size:0.95rem; font-weight:700; color:#2E86C1; margin-bottom:0.6rem;">Ori&euml;ntatie en leerroute</div><div style="font-size:0.68rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:#2E86C1; opacity:0.75; margin:-0.4rem 0 0.55rem 0; text-align:center;">tussen instellingen en sectoren</div>
    <div style="width:100%;"><div style="background:#fff; border:1px solid #2E86C1; border-radius:6px; padding:0.3rem 0.6rem; font-size:0.78rem; margin-bottom:0.25rem; text-align:center;">Behaalde en gewenste leeruitkomsten</div><div style="background:#fff; border:1px solid #2E86C1; border-radius:6px; padding:0.3rem 0.6rem; font-size:0.78rem; margin-bottom:0.25rem; text-align:center;">Aanbod van meerdere instellingen</div></div>
    <div style="font-size:1.1rem; color:#2E86C1; line-height:1;">&#9660;</div>
    <div style="background:#2E86C1; color:#fff; border-radius:6px; padding:0.35rem 0.9rem; font-size:0.85rem; font-weight:700; margin:0.25rem 0;">Agent</div>
    <div style="font-size:1.1rem; color:#2E86C1; line-height:1;">&#9660;</div>
    <div style="font-size:0.85rem; text-align:center; line-height:1.35; margin-top:0.25rem;">Welke volgende stap past bij jouw doelen, ook bij een andere instelling</div>
  </div>

  <div style="flex:1; background:#f0e9fb; border-radius:10px; padding:0.9rem 1rem; display:flex; flex-direction:column; align-items:center;">
    <div style="font-size:0.95rem; font-weight:700; color:#7a5dba; margin-bottom:0.6rem;">Lesopzet</div><div style="font-size:0.68rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:#7a5dba; opacity:0.75; margin:-0.4rem 0 0.55rem 0; text-align:center;">binnen de instelling</div>
    <div style="width:100%;"><div style="background:#fff; border:1px solid #7a5dba; border-radius:6px; padding:0.3rem 0.6rem; font-size:0.78rem; margin-bottom:0.25rem; text-align:center;">Onderwijsspecificatie</div><div style="background:#fff; border:1px solid #7a5dba; border-radius:6px; padding:0.3rem 0.6rem; font-size:0.78rem; margin-bottom:0.25rem; text-align:center;">Leermiddelen in het LMS</div></div>
    <div style="font-size:1.1rem; color:#7a5dba; line-height:1;">&#9660;</div>
    <div style="background:#7a5dba; color:#fff; border-radius:6px; padding:0.35rem 0.9rem; font-size:0.85rem; font-weight:700; margin:0.25rem 0;">Agent</div>
    <div style="font-size:1.1rem; color:#7a5dba; line-height:1;">&#9660;</div>
    <div style="font-size:0.85rem; text-align:center; line-height:1.35; margin-top:0.25rem;">Een concept-lesopzet bij de specificatie</div>
  </div>

</div>

<div class="np-card" style="border-top-color: #A8481F; font-size: 0.98rem; line-height: 1.55; margin-top: 0.9rem; max-width: 96%;">
<strong>Drie schalen, hetzelfde raamwerk eronder.</strong> De agent moet bij die informatie kunnen en weten wat ze betekent. Het eerste is een koppeling. Het tweede is een afspraak.
</div>

</div>

<!--
Drie gevallen, elk met dezelfde vorm: bronnen, agent, resultaat. Wat verschilt
is de schaal waarop vergeleken wordt: vraag naast aanbod, tussen instellingen
en over mbo, hbo en wo heen, en binnen een instelling. Wat gelijk blijft is de
sleutel eronder. Zonder dat raamwerk moet elke vergelijking apart gebouwd
worden, met raamwerk is het telkens dezelfde beweging.
-->

---

<!-- 16. KANSEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vier kansen

<div style="font-size: 0.88rem; line-height: 1.45; margin-top: 0.5rem; max-width: 96%;">

| Kans | Waar die vandaan komt |
|---|---|
| De sector als eerste met een specificatie die een agent kan gebruiken | De payloads zijn al machineleesbaar. Wie ook de interactie zo uitgeeft, levert iets dat elders nog niet bestaat |
| De specificatie als meer dan een document | Dezelfde bron kan een API-definitie voeden en de invoer zijn voor een testomgeving waarin een leverancier zich meet |
| Ons eigen tempo als voorbeeld | Twee releases in twee weken, mediaan 9 dagen per issue, met AI in de keten |
| Laat zijn heeft een voordeel | Andere sectoren zijn ons voor. Hun keuzes zijn over te nemen in plaats van uit te vinden |

</div>

<div style="font-size: 0.9rem; color: var(--np-dark-gray); margin-top: 0.8rem; max-width: 92%;">
De eerste twee zijn een positie die we kunnen innemen. De laatste twee zijn meewind die er sowieso is.
</div>

</div>

<!--
De tweede kans is nieuw en de interessantste: de specificatie is nu een
document, maar dezelfde inhoud kan meer dragen.
-->

---

<!-- 17. RISICO'S -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee risico's

<div style="display: flex; flex-direction: column; gap: 0.6rem; margin-top: 1rem; max-width: 94%;">

  <div style="background:#fdf3ea; border-left:6px solid #D4A017; border-radius:8px; padding:1rem 1.3rem;">
    <div style="font-size:1.05rem; font-weight:700; color:#8a5a12; margin-bottom:0.3rem;">Doorlooptijd tot een gedragen afspraak</div>
    <div style="font-size:0.95rem; line-height:1.5;">Binnen het project gaat het snel. De tijd tot een afspraak die de sector draagt is niet gemeten; de eerste toets is de review van v0.1.0. Duurt dat te lang, dan is de uitkomst achterhaald bij oplevering.</div>
  </div>

  <div style="background:#fbf1ec; border-left:6px solid #A8481F; border-radius:8px; padding:1rem 1.3rem;">
    <div style="font-size:1.05rem; font-weight:700; color:#A8481F; margin-bottom:0.3rem;">Vastgroeien aan een standaard</div>
    <div style="font-size:0.95rem; line-height:1.5;">Als de eisen alleen in OEAPI-vorm bestaan, kost een nieuwe versie of een ander protocol een nieuwe specificatie. Dat is het stoomtreinrisico, maar dan van binnenuit.</div>
  </div>

</div>

<div class="np-card" style="border-top-color: #0E9E7E; font-size: 0.98rem; line-height: 1.55; margin-top: 0.9rem; max-width: 94%;">
<strong style="color: #0E9E7E;">De remedie</strong>: wensen en eisen standaardonafhankelijk vastleggen, en die pas daarna vertalen naar de techniekkeuze. De eis blijft dan staan als de techniek wisselt.
</div>

</div>

<!--
Het risico is niet dat we te weinig standaardiseren, maar dat we ons vastleggen
op een standaard in plaats van op de eis eronder. Machineleesbaar zijn we al;
dat is geen risico maar een vertrekpunt.
-->

---

<!-- 18. WAT DE SECTOR MERKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat instellingen en leveranciers hiervan merken

<div class="np-grid-2" style="margin-top: 0.7rem; gap: 1.5rem; font-size: 0.92rem; line-height: 1.5; max-width: 94%;">
<div style="background:#dceffa; border-radius:10px; padding:1rem 1.2rem;">

<strong style="color: #2E86C1;">Instellingen</strong>

Een student kan alleen over systemen heen kiezen als die systemen het eens zijn over wat een leeruitkomst is. Ligt de eis standaardonafhankelijk vast, dan zit een instelling niet vast aan de techniekkeuze van een leverancier.

</div>
<div style="background:#ffeed9; border-radius:10px; padding:1rem 1.2rem;">

<strong style="color: #E8912B;">Leveranciers</strong>

Zij bouwen tegen het koppelvlak van de onderwijscatalogus, met drie koppelingen. Komt er een nieuwe versie of een ander protocol, dan kost dat een vertaling in plaats van opnieuw specificeren.

</div>
</div>

<div class="np-card" style="border-top-color: #D4A017; font-size: 0.92rem; line-height: 1.5; margin-top: 0.9rem; max-width: 94%;">
<strong style="color: #D4A017;">Wat hier niet ter discussie staat</strong>: het detailniveau dat leveranciers toegezegd hebben gekregen voor v0.1.0. Wordt daaraan getornd, dan is dat een apart gesprek met elke leverancier, gevoerd door de projectleiding.
</div>

</div>

<!--
De onderste kaart voorkomt dat een inzetkeuze gelezen wordt als het
terugdraaien van een toezegging.
-->

---

<!-- 19. WAAR ZETTEN WE OP IN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar zetten we op in?

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.5rem; max-width: 92%;">

Drie richtingen waar de kansen en de risico's samenkomen. Ze kunnen niet alle drie tegelijk voorrang krijgen.

</div>

<div style="font-size: 0.88rem; line-height: 1.45; margin-top: 0.8rem; max-width: 96%;">

| Inzet | Wat het oplevert | Wat het vraagt |
|---|---|---|
| **Tempo** | Een gedragen afspraak voordat de praktijk verder is | Een norm op doorlooptijd en sturing erop, bij de projectleiding |
| **Standaardonafhankelijk vastleggen** | De eis blijft staan als de techniek wisselt | De eisen los van OEAPI opschrijven, en de vertaling apart houden |
| **Meer dan een document** | De specificatie voedt ook een API-definitie en een testomgeving | Werk aan de uitgave, en onderhoud daarvan per release |

</div>

<div class="np-card" style="border-top-color: #0B4F6C; font-size: 0.95rem; line-height: 1.55; margin-top: 0.9rem; max-width: 94%;">
<strong>Gevraagd</strong>: welke van deze drie voorrang krijgt richting v0.1.0.
</div>

</div>

<!--
Geen aanbeveling met ja en nee; die keuze is niet aan de opsteller. Wel de drie
richtingen met wat ze kosten, zodat de keuze te maken is.
-->

---

<!-- 20. AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
