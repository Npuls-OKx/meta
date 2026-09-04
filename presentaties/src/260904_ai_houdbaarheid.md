---
theme: default
title: "Bouwen we het verkeerde? OKx tegenover de AI-ontwikkeling"
info: "Antwoord op de vraag van de opdrachtgever of OKx een stoomtrein bouwt terwijl de AI-ontwikkeling om vliegtuigen vraagt. Voor programma- en projectleiding."
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
  <h1 style="font-size: 2.6rem; line-height: 1.15; margin-bottom: 0.7rem; color: var(--np-ink);">Bouwen we het verkeerde?</h1>
  <p style="font-size: 1.15rem; color: var(--np-dark-gray); max-width: 760px; line-height: 1.5;">Geen koerswijziging in de richting, wel een keuze over welke gaten voor v0.1.0 dicht moeten</p>
  <div style="font-size: 0.9rem; color: var(--np-mid-gray); margin-top: 0.9rem;">Niek Derksen &middot; OKx &middot; 4-9-2026</div>
</div>

<!--
De vraag komt van de opdrachtgever: bouwen we een stoomtrein terwijl de
AI-ontwikkeling straks om vliegtuigen vraagt. De ondertitel is het antwoord.
Twee besluiten aan het eind; die zijn het doel van dit gesprek.
-->

---

<!-- 2. AANLEIDING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aanleiding

<div style="font-size: 1rem; line-height: 1.65; margin-top: 0.7rem; max-width: 88%;">

De opdrachtgever stelde een vraag die het waard is om serieus te nemen.

</div>

<div class="np-card" style="border-top-color: #A8481F; font-size: 1.05rem; line-height: 1.6; margin-top: 0.7rem; max-width: 90%;">
Bouwen we geen stoomtrein door koppelvlakken te standaardiseren? Zeker met de opkomst van AI. Hebben we straks geen vliegende auto's?
</div>

<div style="font-size: 0.98rem; line-height: 1.6; margin-top: 0.9rem; max-width: 88%;">

Achter die vraag zit een reele zorg: een standaardisatietraject duurt jaren, en de wereld eromheen verandert sneller dan ooit. Wie in 1995 het perfecte faxprotocol standaardiseerde, had gelijk en verloor toch.

Dit deck beantwoordt de vraag in twee stappen. Eerst wat AI werkelijk doet met een IT-ecosysteem, aan de hand van dertig jaar lagen die erbij kwamen. Daarna waar OKx in dat beeld staat.

</div>

</div>

<!--
Kort houden en de vraag laten staan zoals hij gesteld is. Niet meteen
verdedigen; de zorg is terecht. Het faxvoorbeeld maakt duidelijk dat de vraag
niet flauw is.
-->

---

<!-- 3. CONCLUSIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Conclusie

<div style="display: flex; flex-direction: column; gap: 0.3rem; margin-top: 0.6rem; max-width: 94%;">

  <div style="background: #0B4F6C; color: #fff; border-radius: 4px; padding: 0.85rem 1.2rem; font-size: 1rem; line-height: 1.4;">
    Geen stoomtrein. OKx maakt afspraken over betekenis en eigenaarschap. Die overleven een technologiewissel; de techniek eromheen is vervangbaar.
  </div>

  <div style="background: #eef4f2; border-left: 6px solid #0E7C66; border-radius: 4px; padding: 0.8rem 1.2rem; font-size: 0.95rem; line-height: 1.4;">
    Ook de verhouding klopt: het zwaartepunt van het werk ligt al op de betekenislaag, niet op de technische uitwerking. Dat is precies de laag die zijn waarde houdt.
  </div>

  <div style="background: #fdf3ea; border-left: 6px solid #D4A017; border-radius: 4px; padding: 0.8rem 1.2rem; font-size: 0.95rem; line-height: 1.4;">
    Wat de vraag wel blootlegt zijn vier gaten. Drie ervan staan los van AI en zijn al bekend. Het vierde wordt door AI wel urgenter.
  </div>

</div>

<div class="np-card" style="border-top-color: #A8481F; font-size: 0.92rem; line-height: 1.5; margin-top: 0.7rem; max-width: 94%;">
<strong style="color: #A8481F;">Twee besluiten gevraagd</strong>: welke gaten voor de release-PR van v0.1.0 dicht moeten, en bij wie het beheer na Npuls komt te liggen. Aanbeveling en opties op slide 8 en 9.
</div>

</div>

<!--
Conclusie voorop. Let op de tweede regel: die weerspreekt de aanname dat het
gewicht verkeerd ligt. Dat is gemeten, niet aangenomen; de cijfers staan op
slide 5. Niet defensief brengen, wel feitelijk.
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
Dit is de kern van het antwoord op de vraag. De geschiedenis wijst een kant op
en die kant is meer uitwisseling, niet minder. Wie dat betwist, moet uitleggen
waarom deze golf de eerste is die het patroon omkeert.
-->

---

<!-- 9. WAAR OKX ZIT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar OKx in dit beeld staat

<div style="font-size: 0.95rem; line-height: 1.55; margin-top: 0.6rem; max-width: 92%;">

OKx werkt niet aan een laag. OKx werkt aan de verbinding tussen de lagen: welke gegevens tussen systemen gaan, wat ze betekenen, en wie waarvan de bron is. Dat is precies het element dat in alle vier de plaatjes voorkomt.

</div>

<div class="np-grid-2" style="margin-top: 0.8rem; gap: 1.5rem; font-size: 0.9rem; line-height: 1.5; max-width: 94%;">
<div style="border-left: 4px solid #0E7C66; padding-left: 0.9rem;">

<strong style="color: #0E7C66;">Wat dit voor de vraag betekent</strong>

Een instelling met losse systemen en onduidelijke begrippen heeft niets aan een AI-laag: die kan alleen bevragen wat ontsloten en gedefinieerd is. Meer interconnectie levert sterkere bronnen op, en sterkere bronnen zijn waar AI op aanhaakt.

</div>
<div style="border-left: 4px solid #A8481F; padding-left: 0.9rem;">

<strong style="color: #A8481F;">Waar de zorg wel terecht is</strong>

Wij zijn laat. Andere sectoren hebben deze afspraken al. Dat is geen argument om het niet te doen, maar wel om er tempo op te zetten en om de uitwisseling zo vast te leggen dat een machine hem kan lezen.

</div>
</div>

</div>

<!--
Hier komen de twee helften bij elkaar: de trend rechtvaardigt het werk, en de
zorg over tempo blijft staan. Niet doorslaan naar zelffelicitatie.
-->

---

<!-- 10. WAT STANDHOUDT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat standhoudt, en wat niet

<div style="font-size: 0.88rem; line-height: 1.45; margin-top: 0.5rem; max-width: 96%;">

| Onderdeel | Blijft | Waarom |
|---|---|---|
| Wat begrippen betekenen | Ja | Een model kan een voorstel doen; de sector moet het vaststellen. Dat blijft een bestuurlijk besluit |
| Welk systeem bron is van welk gegeven | Ja | Een onderwijsverbintenis en een waardedocument zijn administratief bindend. Daar hoort vastlegging bij, geen inschatting |
| De inhoud van een bericht, los van het kanaal waarover het gaat | Ja | Vastgelegd als uitgangspunt. Een ander kanaal raakt de inhoud niet |
| De keuze voor OEAPI en voor OAuth 2.0 | Nee | Dit zijn expliciete keuzes met een tenzij-clausule. Ze zijn vervangbaar; dat is bewust zo opgezet |
| Het detailniveau per koppeling | Nee | Groeit mee met wat leveranciers nodig hebben om te bouwen |

</div>

<div style="font-size: 0.86rem; color: var(--np-dark-gray); margin-top: 0.7rem; max-width: 92%;">
Alle genoemde afspraken hebben op dit moment de status voorstel. Ze zijn vastgelegd in de principes en uitgangspunten, en nog niet formeel bekrachtigd.
</div>

</div>

<!--
De laatste regel is belangrijk: eerder stond hier dat het staande afspraken
zijn. Dat is niet zo, alles staat op status voorstel. Wie dat controleert en
het anders aantreft, gelooft de rest van het deck ook niet meer.
-->

---

<!-- 11. DE VIER GATEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vier gaten die de vraag blootlegt

<div style="font-size: 0.86rem; line-height: 1.45; margin-top: 0.5rem; max-width: 96%;">

| Gat | Stand van zaken | Door AI urgenter |
|---|---|---|
| Doorlooptijd tot een gedragen afspraak | Binnen het project gaat het snel: mediaan 9 dagen per issue, twee releases in twee weken. Wat niet gemeten is, is de tijd tot een afspraak die de sector draagt. De eerste echte toets is de review van v0.1.0 | Nee |
| Machineleesbaar op interactieniveau | De 24 datamodelschema's zijn machineleesbaar en worden meegeleverd. De interactiepatronen en de endpoints zijn dat niet | **Ja** |
| Binding naar OEAPI | De payloads zijn Nederlandstalig en wijken bewust af van de OEAPI-sleutelnamen. Ook het afleveringsmechanisme tussen partijen is nog niet belegd | Nee |
| Beheerpartij na Npuls | De route ligt vast: standaardiseren via AMIGO, richting Edustandaard. Welke partij het overneemt is niet belegd | Nee |

</div>

<div style="font-size: 0.86rem; color: var(--np-dark-gray); margin-top: 0.7rem; max-width: 92%;">
Alleen het tweede gat wordt door de AI-ontwikkeling groter: wie met een agent wil bouwen, kan de payloads gebruiken maar moet de interactie nog zelf uit tekst halen.
</div>

</div>

<!--
Dit is de eerlijkste slide. Let op de eerste rij: het tempo binnen het project
is aantoonbaar hoog. Wat we niet weten is de doorlooptijd naar draagvlak; dat
is een risico, geen vastgestelde tekortkoming. Zo ook brengen.
-->

---

<!-- 12. WAT DE SECTOR MERKT -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat instellingen en leveranciers hiervan merken

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.5rem; font-size: 0.9rem; line-height: 1.5; max-width: 94%;">
<div style="border-left: 4px solid #0B4F6C; padding-left: 0.9rem;">

<strong style="color: #0B4F6C;">Instellingen</strong>

Een student kan alleen over systemen heen kiezen als die systemen het eens zijn over wat een leeruitkomst is. Dat is wat OKx vastlegt. Sluit gat 2 en 3, dan kan een instelling straks controleren of haar leveranciers zich eraan houden, in plaats van het te moeten geloven.

</div>
<div style="border-left: 4px solid #A8481F; padding-left: 0.9rem;">

<strong style="color: #A8481F;">Leveranciers</strong>

Zij bouwen tegen het koppelvlak van de onderwijscatalogus, met drie koppelingen: naar planning en roostering, naar het studentinformatiesysteem en naar het leermanagementsysteem. Zolang gat 2 openstaat, leest een leverancier de interactie uit tekst en kan hij niet automatisch valideren.

</div>
</div>

<div class="np-card" style="border-top-color: #D4A017; font-size: 0.9rem; line-height: 1.5; margin-top: 0.9rem; max-width: 94%;">
<strong style="color: #D4A017;">Wat geen enkele optie verandert</strong>: het detailniveau dat leveranciers toegezegd hebben gekregen voor v0.1.0. Wordt daaraan getornd, dan is dat een apart gesprek met elke leverancier, gevoerd door de projectleiding, en geen bijvangst van dit besluit.
</div>

</div>

<!--
Deze slide is toegevoegd op verzoek: het deck ging alleen over OKx zelf.
De onderste kaart is de belangrijkste: eerder stond "leveranciers krijgen later
detail" verstopt in een kostenkolom. Dat is nu expliciet uitgesloten.
-->

---

<!-- 13. WAT WE DOEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De vier gaten dichten

<div style="font-size: 0.84rem; line-height: 1.4; margin-top: 0.5rem; max-width: 98%;">

| Gat | Wat er gebeurt | Inschatting | Hoort bij |
|---|---|---|---|
| Doorlooptijd | Norm afspreken van eerste concept naar gedragen afspraak, en erop rapporteren | 1 week, projectleiding | Sowieso |
| Beheerpartij | Gesprek met Edustandaard en Npuls over overname na afloop | Maanden doorlooptijd, opdrachtgever | Sowieso |
| Machineleesbare interactie | Interactiepatronen en endpoints ook als schema uitgeven, naast de leesbare versie | 3 tot 4 weken, plus onderhoud per release | Besluit 1 |
| OEAPI-binding | Sleutelnamen en afleveringsmechanisme vastleggen | 4 tot 6 weken, samen met de technische werkgroep | Besluit 1 |

</div>

<div style="font-size: 0.86rem; color: var(--np-dark-gray); margin-top: 0.7rem; max-width: 94%;">
De eerste twee gebeuren ongeacht de uitkomst; ze staan los van de AI-vraag en zijn al langer bekend. De laatste twee zijn het onderwerp van besluit 1. De doorlooptijden zijn een inschatting, geen toezegging.
</div>

</div>

<!--
De kolom "Hoort bij" is toegevoegd omdat eerder onduidelijk was wat er met een
besluit meekwam. Twee regels gebeuren sowieso; die niet als onderhandelbaar
presenteren.
-->

---

<!-- 14. BESLUIT 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Besluit 1: volgorde richting v0.1.0

<div class="np-card" style="border-top-color: #0B4F6C; font-size: 0.92rem; line-height: 1.55; margin-top: 0.4rem; max-width: 94%;">
<strong>Besluit nodig op:</strong> of de machineleesbare interactie en de OEAPI-binding voor v0.1.0 af moeten<br/>
<strong>Door:</strong> opdrachtgever en programmamanagement. De kaderstelling zelf wordt bij v0.1.0 door de kerngroep techniek beoordeeld; dat blijft hun gate<br/>
<strong>Voor:</strong> de release-PR van v0.1.0, datum uit de projectplanning
</div>

<div style="font-size: 0.84rem; line-height: 1.4; margin-top: 0.6rem; max-width: 98%;">

| Optie | Gevolg voor v0.1.0 | Gevolg voor de sector | Aanbeveling |
|---|---|---|---|
| **A.** Beide gaten dicht voor v0.1.0 | Schuift met 4 tot 6 weken | Leveranciers kunnen bij de review meteen automatisch valideren | Nee |
| **B.** Beide gaten in de 0.1.x-reeks daarna | v0.1.0 op de geplande datum, gaten benoemd in de release notes | De kerngroep techniek weet wat er nog komt en wanneer | **Ja** |
| **C.** Beide gaten niet plannen | v0.1.0 op datum | De kerngroep techniek vindt de gaten zelf bij de review, zonder antwoord van ons | Nee |

</div>

<div style="font-size: 0.86rem; color: var(--np-dark-gray); margin-top: 0.6rem; max-width: 94%;">
Zonder besluit geldt C. Dat is de enige uitkomst waarin een bevinding van de kerngroep techniek ons overvalt.
</div>

</div>

<!--
A en C zijn allebei reeel: A is verdedigbaar als de review zwaar weegt, C is
wat er gebeurt bij uitstel. Bij B hoort dat de gaten in de release notes staan;
dat is de mitigatie en die niet vergeten te noemen.
-->

---

<!-- 15. BESLUIT 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Besluit 2: beheer na Npuls

<div class="np-card" style="border-top-color: #A8481F; font-size: 0.92rem; line-height: 1.55; margin-top: 0.4rem; max-width: 94%;">
<strong>Besluit nodig op:</strong> welke partij de afspraken overneemt als het programma stopt<br/>
<strong>Door:</strong> opdrachtgever, met Npuls-programmamanagement<br/>
<strong>Voor:</strong> zo snel mogelijk. Dit besluit heeft de langste doorlooptijd van alles in dit deck en staat los van de AI-vraag
</div>

<div style="font-size: 0.9rem; line-height: 1.5; margin-top: 0.8rem; max-width: 94%;">

De route ligt al vast: standaardiseren volgens AMIGO, richting Edustandaard, dat de OKE-standaard al beheert. Wat niet belegd is, is de partij die het daadwerkelijk overneemt, met mensen en geld erbij.

Zolang dat open staat, verliest elke afspraak in dit deck geldigheid op de dag dat het programma stopt. Dat is geen AI-vraagstuk; het zou ook zonder deze discussie opgelost moeten worden.

</div>

<div style="font-size: 0.86rem; color: var(--np-dark-gray); margin-top: 0.9rem; max-width: 94%;">
Gevraagd: een eigenaar en een datum waarop het gesprek met Edustandaard gevoerd is.
</div>

</div>

<!--
Dit stond eerder als voetnoot onder besluit 1. Het hoort er los van: beheer
speelt bij elke uitkomst en heeft de langste doorlooptijd. Als er vandaag maar
een ding besloten wordt, dan dit.
-->

---

<!-- 16. AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
