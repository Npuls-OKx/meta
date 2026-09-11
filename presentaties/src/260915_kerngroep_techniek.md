---
theme: default
title: "Kerngroep techniek, 15 september 2026"
info: "Update kerngroep techniek: versionering en modulariteit van de koppelvlakspecificatie, het informatiemodel met de begrippenlijst, en het open werk met een voorstel voor de prioritering."
author: OKx - Onderwijskoppelingen (Npuls)
highlighter: shiki
colorSchema: light
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
  <h1 style="font-size: 3.2rem; line-height: 1.15; margin-bottom: 0.8rem; color: var(--np-ink);">Kerngroep techniek</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 34rem;">De koppelvlakspecificatie krijgt een laag die versioneren mogelijk maakt, en het informatiemodel waar om gevraagd is ligt er</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 15 september 2026</div>
</div>

<!--
Ruud is afwezig. Niek en Garik trekken de sessie. Twee thema's: versionering en modulariteit
(Garik, het grootste deel van de tijd) en het informatiemodel met de begrippenlijst (Niek).
Daarna het open werk met een voorstel voor de prioritering.
-->

---

<!-- 2. STAND VAN ZAKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Stand van zaken

```mermaid
flowchart LR
  A["v0.0.2<br/>Public PR 82, ter review sinds 1 september"] --> B["Applicatiediensten en versionering<br/>Public PR 100, voorstel"]
  A --> C["Informatiemodel en begrippenlijst<br/>meta PR 225, interne review"]
```

<div style="font-size: 0.92rem; line-height: 1.7; margin-top: 1rem;">

| Afgesproken op 1 september | Stand |
|---|---|
| Versioneringsvoorstel als pull request | Ligt er: [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100), groter geworden dan aangekondigd |
| Uitkomst van de review op v0.0.2 | Eén reactie binnen, zie de volgende slide |
| Informatiemodel eerst reviewen, dan de payloads | Issue geworden ([meta #163](https://github.com/Npuls-OKx/meta/issues/163)), uitgewerkt in [meta PR 225](https://github.com/Npuls-OKx/meta/pull/225) |

</div>

</div>

<!--
Drie regels, elk met status. Bronnen: de slide Vervolg van het deck van 1 september, en de
twee pull requests. PR 100 raakt 63 bestanden; het was aangekondigd als een versioneringsvoorstel
en is een herindeling van de koppelvlakspecificatie geworden.
-->

---

<!-- 3. REVIEW OP V0.0.2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Review op v0.0.2: wat is er gezien?

<div style="font-size: 0.95rem; line-height: 1.8; margin-top: 1rem;">

- Eén reactie binnen: Xedule en YNC, een pdf met opmerkingen per story ([Public #99](https://github.com/Npuls-OKx/Public/issues/99))
- Op de pull request zelf geen review ingediend; de reacties die erop staan komen uit de demo van 1 september ([Public PR 82](https://github.com/Npuls-OKx/Public/pull/82))

</div>

<div class="np-card" style="margin-top: 1.4rem; font-size: 0.98rem;">
Gezocht: de bevindingen van ieder die v0.0.2 heeft doorgenomen, en wat er nodig is om de review te laten gebeuren.
</div>

</div>

<!--
Vragend stellen, niet verwijtend. De drie reviewregels en de comment op PR 82 zijn tijdens de
demo van 1 september geplaatst en tellen niet als review. De pdf van Xedule en YNC bevat acht
pagina's opmerkingen per story; Niels heeft daarop geantwoord dat de stories met de
PoC-instellingen verder worden aangepakt.
-->

---

<!-- 4. OPDRACHTEN VORIGE SESSIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Openstaande punten van 1 september

<div style="font-size: 0.92rem; line-height: 1.7; margin-top: 1rem;">

| Punt | Stand |
|---|---|
| Versionering per koppeling ([Public #47](https://github.com/Npuls-OKx/Public/issues/47)) | Voorstel ligt er als [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100), vandaag op tafel |
| Meerdere instanties van een referentiecomponent ([meta #80](https://github.com/Npuls-OKx/meta/issues/80)) | Niet opgepakt |
| Keuzes en regelsets ([Public #74](https://github.com/Npuls-OKx/Public/issues/74)) | Niet opgepakt; staat in het voorstel voor de prioritering |
| Informatiemodel voor payloads ([meta #163](https://github.com/Npuls-OKx/meta/issues/163)) | Uitgewerkt in [meta PR 225](https://github.com/Npuls-OKx/meta/pull/225), vandaag op tafel |

</div>

</div>

<!--
Twee van de vier opgepakt, twee niet. Bron: de slide Openstaande punten van 1 september en
de stand van de issues op 11 september. Meta #80 heeft sinds juli een reactie van Ruud met
het rondje uit de kerngroep en verder niets.
-->

---

<!-- DIVIDER DEEL 1 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 1</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Versionering en modulariteit</h1>
  </div>
</div>

<!--
Blok van Garik: slides 6 tot en met 9. De opzet staat; Garik vervangt en vult aan met zijn
eigen sheets, voorbeeld en diagrammen.
-->

---

<!-- 6. HET PROBLEEM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een veld erbij in een datamodel, en dan?

```mermaid
flowchart LR
  D["Datamodel"] --> E["Endpoint"] --> S["Applicatiedienst"] --> K["Koppeling"]
```

<div style="font-size: 0.98rem; line-height: 1.9; margin-top: 1.4rem;">

- Een optioneel veld breekt geen bestaande koppeling
- Zonder versie ziet een implementatiepartij niet wie het veld wel en niet ondersteunt
- Dus: een versie op elke laag, of een knip die de kettingreactie stopt

</div>

</div>

<!--
BLOK GARIK. Bron: de afstemming van 11 september. Het voorbeeld dat Garik gaf: partij een
implementeert het nieuwe veld, partij twee niet, en niemand kan zien dat de een op versie Y
zit en de ander op X. Hier komt zijn eigen voorbeeld en diagram.
-->

---

<!-- 7. DE LAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Applicatiediensten als laag tussen component en endpoint

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem; font-size: 0.92rem; line-height: 1.8;">
<div>

**Wat het oplost**

- Eén contract, niet drie keer beschreven per koppeling
- Aanbieden en afnemen zijn twee losse diensten
- Elke dienst zelfstandig te claimen en te versioneren

</div>
<div>

**Wat er ligt**

- Veertien paren aanbieder en afnemer, uit de requirementsboom
- Vijf generieke interactiepatronen, met de naam uit de catalogus waar ze vandaan komen
- Twaalf functionele eisen vervangen door de stories die ze navertelden

</div>
</div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 1.4rem;">
Status: voorstel, <a href="https://github.com/Npuls-OKx/Public/pull/100">Public PR 100</a>. Hoogstens twee gelijktijdig actieve major versies per dienst.
</div>

</div>

<!--
BLOK GARIK. Bron: de beschrijving van Public PR 100 en Koppelvlakspecificaties/Applicatiediensten/README.md
op de branch. Er is nog geen plaat van de nieuwe laag; de opgeslagen overzichtsplaat toont
de oude opbouw. Garik levert het diagram.
-->

---

<!-- 8. HET VOORSTEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Datamodellen als eigen pakket

<div style="font-size: 0.98rem; line-height: 1.9; margin-top: 1rem;">

- De datamodellen krijgen samen een eigen versie, los van endpoint en dienst
- Een kleine wijziging in een model dwingt geen ophoging af in de lagen erboven
- Een implementatiepartij plant de overstap zelf

</div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 1.4rem;">
Status: voorstel. Nog niet in de pull request opgenomen.
</div>

</div>

<!--
BLOK GARIK. Bron: de afstemming van 11 september. Dit deel zit nog niet in PR 100; Garik was
het aan het toevoegen. Hier komen zijn sheets over wat dit betekent voor de implementatielaag
en hoe flexibel een leverancier kan zijn.
-->

---

<!-- 9. DE A/B-VRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee varianten voor de versie van de datamodellen

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem; font-size: 0.95rem; line-height: 1.8;">
<div class="np-card">

**A. Eén versie voor alle datamodellen**

- Eén nummer om te volgen
- Elke wijziging raakt iedereen

</div>
<div class="np-card">

**B. Een versie per domein**

- Een wijziging blijft bij het domein
- Meer nummers om te volgen

</div>
</div>

<div class="np-card" style="margin-top: 1.4rem; font-size: 0.98rem;">
Gezocht: welke variant landt in de implementatie het best, gezien vanuit het eigen systeem.
</div>

</div>

<!--
BLOK GARIK. De A/B-test uit de afstemming van 11 september. Garik richt de scheiding tussen de
datamodellen alvast in en demonstreert die. Het antwoord van de leveranciers bepaalt welke
variant in PR 100 wordt uitgewerkt.
-->

---

<!-- DIVIDER DEEL 2 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Informatiemodel</h1>
  </div>
</div>

---

<!-- 11. DE VRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De vraag uit de kerngroep

<div class="np-card" style="margin-top: 1.2rem; font-size: 1.05rem; line-height: 1.7;">
"Voordat we de details in de koppeling velden specificeren hebben we behoefte om het very high level domain model te valideren. Waar kunnen we die vinden?"
<div style="font-size: 0.8rem; color: var(--np-mid-gray); margin-top: 0.6rem;"><a href="https://github.com/Npuls-OKx/Public/issues/89">Public #89</a>, 1 september 2026</div>
</div>

<div style="font-size: 0.98rem; line-height: 1.9; margin-top: 1.4rem;">

- Het antwoord: twee platen uit het ArchiMate-model, met de conventies en de keuzes erachter
- Het OKx-model staat los van OEAPI; de mapping is een tweede plaat
- Status: concept, interne review afgerond, ter review in [meta PR 225](https://github.com/Npuls-OKx/meta/pull/225); twee ontwerpkeuzes liggen bij het kernteam ([meta #227](https://github.com/Npuls-OKx/meta/issues/227), [#228](https://github.com/Npuls-OKx/meta/issues/228))

</div>

</div>

<!--
De vraag letterlijk, want het deck beantwoordt hem. Niels stelde in hetzelfde issue voor om
vanuit twee platen te werken; Ruud ging akkoord; Jan Hendrik gaf op 4 september eerste
feedback op de plaat, die is verwerkt.
-->

---

<!-- 12. DE PLAAT -->
<div style="position: absolute; inset: 0; background: #FFFFFF; display: flex; align-items: center; justify-content: center; padding: 0.5rem;">
  <img src="/platen/informatiemodel-v0.1.jpg" style="max-width: 100%; max-height: 100%; object-fit: contain;" />
</div>

<!--
Het informatiemodel OKx, versie v0.1 van 9 september. Leeswijzer: de kolommen zijn de begrippen,
van kwalificatiekader links tot resultaatstructuur onderaan. Geel is het OKx-referentiekader,
grijs valt buiten scope. De leeruitkomst, tweede kolom, is de sleutel: elke specificatie en de
summatieve resultaatstructuur wijzen ernaar. Bron: architecture/model/informatiemodel/ in meta,
branch van PR 225. Op de sessie inzoomen in de browser of het document ernaast openen.
-->

---

<!-- 13. DE BEGRIPPEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Zeven begrippen delen de keten in

<div style="font-size: 0.9rem; line-height: 1.6; margin-top: 0.8rem;">

| Begrip | Beantwoordt de vraag |
|---|---|
| Kwalificatiekader mbo | Wat is normatief geldig |
| Onderwijskundig kader instelling | Wat moet de student kennen en kunnen |
| Onderwijsspecificatie | Wat wordt georganiseerd |
| Onderwijsaanbod | Wanneer, met hoeveel plekken, met wie |
| Onderwijsverbintenis | Welke relatie heeft een student met dat aanbod |
| Onderwijsresultaat | Wat is er behaald |
| Resultaatstructuur | Hoe telt dat op tot een uitspraak over de kwalificatie |

</div>

</div>

<!--
Letterlijk overgenomen uit de begrippentabel in informatiemodel.md. Het informatiemodel is de
aanzet tot het conceptueel informatiemodel, MIM-niveau 2; de begrippen zelf staan op niveau 1
in het begrippenkader en de begrippenlijst.
-->

---

<!-- 14. DE MAPPINGPLAAT -->
<div style="position: absolute; inset: 0; background: #FFFFFF; display: flex; align-items: center; justify-content: center; padding: 0.5rem;">
  <img src="/platen/informatiemodel-oeapi-mapping-v0.1.jpg" style="max-width: 100%; max-height: 100%; object-fit: contain;" />
</div>

<!--
Dezelfde objecttypen met OEAPI v6 ernaast. Blauw is OEAPI; de pijl is realisatie: het
OEAPI-object is de vorm waarin een OKx-objecttype over de lijn gaat. Versie v0.1 van
9 september. De bevindingen staan op de volgende slide.
-->

---

<!-- 15. BEVINDINGEN OEAPI -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de mapping op OEAPI v6 laat zien

<div style="font-size: 0.98rem; line-height: 1.9; margin-top: 1rem;">

- Eén OEAPI-object draagt vaak meerdere OKx-objecttypen: `Programme` vier, `ProgrammeOffering` drie
- De leeruitkomst heeft een tegenhanger, `LearningOutcome`
- De resultaatstructuur is nog niet gemapt; de vraag is of dat kan, en het lijkt er nu op van niet
- 21 objecttypen binnen scope zonder OEAPI-object: per stuk signalering of bewuste afwijking

</div>

<div class="np-card" style="margin-top: 1.2rem; font-size: 0.98rem;">
Gezocht: hoe mapt OEAPI een kwalificatiekader naar objecten? Kwalificatiedossier, kwalificatie, kerntaak en werkproces hebben in de mapping nu geen tegenhanger.
</div>

</div>

<!--
Bron: informatiemodel-oeapi-mapping.md. Geverifieerd tegen de OEAPI 6.0 OpenAPI-specificatie:
LearningOutcome bestaat met eigen endpoints. Voor de resultaatstructuur is de mapping nog niet
gemaakt; wat er tot nu toe gevonden is: weight staat per resultaat, niet per specificatie, en
het afrondingscriterium bestaat alleen als vrije tekst in qualificationRequirements. Daarom de
inschatting dat het niet kan; vastgesteld is dat niet. De vraag over het kwalificatiekader is
een echte vraag aan de zaal: in de OpenAPI-specificatie is geen object voor dossier, kwalificatie,
kerntaak of werkproces gevonden, maar wie OEAPI in de praktijk implementeert weet misschien hoe
dat elders wordt opgelost.
-->

---

<!-- 16. BEGRIPPENKADER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Eerste begrippenkader

<div style="font-size: 0.95rem; line-height: 1.7; margin-top: 0.3rem;">

- Elk begrip gerelateerd aan de referentiearchitecturen: MORA, ROSA (Kernmodel Onderwijsinformatie) en HORA
- Doel: iteratief uitbreiden en reviewen

</div>

<div style="font-size: 0.74rem; line-height: 1.35; margin-top: 0.6rem; max-width: 88%;">

| Begrip | Definitie | Herkomst | ROSA | MORA | HORA |
|---|---|---|---|---|---|
| `Kwalificatie dossier` | Het kwalificatiedossier beschrijft de eisen waaraan een student moet voldoen om zijn diploma te behalen | overgenomen uit MORA | geen tegenhanger | <a href="https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762">Kwalificatie dossier</a> | nog niet onderzocht |
| `Onderwijsverbintenis` | Een afspraak voor het gaan volgen, volgen en hebben gevolgd van onderwijs | overgenomen uit ROSA | <a href="https://rosa.wikixl.nl/index.php/Id-ec977035c9be4b01bb1c14a5950a1799">onderwijsdeelname</a> | geen tegenhanger | nog niet onderzocht |
| `Onderwijseenheid specificatie` | De specificatie van de fundamentele eenheid waarin onderwijs wordt ontworpen en aangeboden | afgeleid uit klus 53 | <a href="https://rosa.wikixl.nl/index.php/Id-c74c161c6f1f4690933a31ce4d11f3b8">onderwijseenheid</a> | <a href="https://mora.mbodigitaal.nl/index.php/Id-17db36ca-368f-450e-cbfe-604b2fafee6e">Opleidings-onderdeel</a> | nog niet onderzocht |
| `Toetsgelegenheid` | Het georganiseerde aanbod van een toetsmoment: wanneer, waar en onder welke condities | afgeleid uit klus 53 | geen tegenhanger | geen tegenhanger | nog niet onderzocht |
| `Keuzedeelruimte` | <em>nog te definiëren</em> | nieuw voor OKx | geen tegenhanger | geen tegenhanger | nog niet onderzocht |

</div>

<div style="font-size: 0.8rem; color: var(--np-dark-gray); margin-top: 0.6rem;">
Uitsnede: vijf van de 69 begrippen en objecttypen. Status: v0.2, concept. MORA en ROSA zijn geraadpleegd, HORA volgt.
</div>

</div>

<!--
Uitsnede uit begrippenlijst.md op de branch van meta PR 225, stand 11 september. Definities
zijn ingekort tot de eerste zin; de volledige tekst staat in de lijst met citaat, URL en
ophaaldatum. De vijf rijen laten de vier soorten zien: overgenomen uit MORA, overgenomen uit
ROSA, twee die zijn afgeleid uit de alignment MORA en HORA (klus 53), en een nog leeg begrip.
Stand van de hele lijst: 69 begrippen, 20 overgenomen, 14 eigen OKx-definitie, 35 nog open.
-->

---

<!-- DIVIDER DEEL 3 -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 3</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Open werk</h1>
  </div>
</div>

---

<!-- 18. OPEN WERK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Open werk in Npuls-OKx/Public

<div class="np-grid-2" style="margin-top: 0.8rem; gap: 1.6rem; font-size: 0.86rem; line-height: 1.55;">
<div>

**Zes milestones met openstaand werk**

| Milestone | Open |
|---|---|
| [Releaseproces en kwaliteit](https://github.com/Npuls-OKx/Public/milestone/4) | 11 |
| [Requirementsboom doorontwikkelen](https://github.com/Npuls-OKx/Public/milestone/3) | 9 |
| [Koppelingspecificatiestructuur doorontwikkelen](https://github.com/Npuls-OKx/Public/milestone/5) | 7 |
| [Leerroute-refactor](https://github.com/Npuls-OKx/Public/milestone/1) | 3 |
| [Keuzedelen](https://github.com/Npuls-OKx/Public/milestone/7) | 3 |
| [Agent-harness](https://github.com/Npuls-OKx/Public/milestone/2) | 2 |

</div>
<div>

**Sinds 1 september van buiten het kernteam**

- Vijf issues van Kees over granulariteit, definities, eigenaarschap en leestijd ([#85](https://github.com/Npuls-OKx/Public/issues/85) tot en met [#89](https://github.com/Npuls-OKx/Public/issues/89))
- Twee van Xedule: notificaties ontvangen ([#84](https://github.com/Npuls-OKx/Public/issues/84)) en de opmerkingen per story ([#99](https://github.com/Npuls-OKx/Public/issues/99))

**Wat nu loopt**

- Versionering ([PR 100](https://github.com/Npuls-OKx/Public/pull/100)), informatiemodel ([#89](https://github.com/Npuls-OKx/Public/issues/89)), granulariteit ([#85](https://github.com/Npuls-OKx/Public/issues/85)), stories met de PoC-instellingen ([#99](https://github.com/Npuls-OKx/Public/issues/99))

</div>
</div>

</div>

<!--
Stand van 11 september: 44 open issues, waarvan 7 zonder milestone. Links de milestones met hun
aantallen; rechts wat er van buiten binnenkwam en wat er aantoonbaar aan gewerkt wordt (een
pull request, een toegewezen persoon, of een antwoord in het issue). Wat niet in de laatste
regel staat, wordt op dit moment niet opgepakt.
-->

---

<!-- 18b. VERZET WERK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er sinds 1 september is verzet

<div style="font-size: 0.86rem; line-height: 1.5; margin-top: 0.6rem; max-width: 60%;">

| | Npuls-OKx/Public | Npuls-OKx/meta |
|---|---|---|
| Pull requests gemerged | 2 | 4 |
| Pull requests geopend | 1 | 6 |
| Issues gesloten | 5 | 11 |
| Issues geopend | 8 | 21 |
| Commits op `dev` | 1 | 47 |

</div>

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.6rem; font-size: 0.84rem; line-height: 1.55; max-width: 86%;">
<div>

**Public**

- Overzichtsplaat en branching-diagram; redactie op kaderscenario leerroute 1
- Applicatiediensten en versionering in voorbereiding: 63 bestanden op een branch ([PR 100](https://github.com/Npuls-OKx/Public/pull/100))
- Vijf correctie-issues op de hoofdplaat en het kaderscenario gesloten

</div>
<div>

**meta**

- Deck van 1 september met PowerPoint-export, Nederlands als voertaal, lezerspersona's
- Informatiemodel en begrippenlijst: 22 commits op een branch ([PR 225](https://github.com/Npuls-OKx/meta/pull/225))
- Elf issues gesloten, vooral de harness rond presentaties en reviews

</div>
</div>

</div>

<!--
Stand van 11 september, beide repositories, alles na 1 september. De aantallen zeggen iets
over de hoeveelheid werk, niet over de kwaliteit ervan; dat oordeel ligt bij de review. Het
grote werk van deze periode staat op branches en niet op dev: PR 100 in Public en PR 225 in
meta. De 21 nieuwe issues op meta zijn grotendeels intern harness- en reviewwerk.
-->

---

<!-- 19. VOORSTEL PRIORITERING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorstel voor de prioritering

<div style="font-size: 0.92rem; line-height: 1.7; margin-top: 1rem;">

| | Eerst | Waarom |
|---|---|---|
| 1 | Review op de pull requests: versionering ([Public PR 100](https://github.com/Npuls-OKx/Public/pull/100)), v0.0.2 ([Public PR 82](https://github.com/Npuls-OKx/Public/pull/82)), het informatiemodel zodra het naar Public gaat | Zonder review geen release, en zonder release geen bouw |
| 2 | Keuzedeelregels: de typologie toetsen aan de echte scenario's ([Public #74](https://github.com/Npuls-OKx/Public/issues/74), [#64](https://github.com/Npuls-OKx/Public/issues/64), [#1](https://github.com/Npuls-OKx/Public/issues/1)) | Elke studentkeuze werkt door in planning, rooster en leeromgeving; dit is de spil van flexibilisering |

</div>

<div style="font-size: 0.92rem; line-height: 1.7; margin-top: 1rem;">

**Wat daarmee wacht:** meerdere instanties van een referentiecomponent ([meta #80](https://github.com/Npuls-OKx/meta/issues/80)), de terminologie- en correctie-issues, en de verdieping van de requirementsboom.

</div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 1rem;">
Status: voorstel van het kernteam. Zonder keuze blijft alles even zwaar en beweegt niets.
</div>

</div>

<!--
Voorstel, geen besluit. De volgorde en de twee prioriteiten komen van Niek; de rest is afgeleid
uit de backlog. Vraag aan de groep: klopt deze volgorde, en wat ontbreekt?
-->

---

<!-- 20. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<dl class="np-besluit kennisname" style="margin-top: 1rem;">
  <dt>Input</dt><dd>welke versioneringsvariant landt in de implementatie het best, A of B</dd>
</dl>

<dl class="np-besluit review" style="margin-top: 0.8rem;">
  <dt>Review</dt><dd>het informatiemodel op conceptueel niveau: klopt de samenhang, welke objecttypen missen, en welke begrippen missen in de lijst. Tot de volgende sessie, in <a href="https://github.com/Npuls-OKx/meta/pull/225">meta PR 225</a></dd>
</dl>

<dl class="np-besluit" style="margin-top: 0.8rem;">
  <dt>Besluit</dt><dd>de prioritering van het open werk: eerst de reviews, dan de keuzedeelregels</dd>
</dl>

<dl class="np-besluit kennisname" style="margin-top: 0.8rem;">
  <dt>Input</dt><dd>de bevindingen op v0.0.2, en wat er nodig is om de review te laten gebeuren</dd>
</dl>

</div>

<!--
Geen besluit over het informatiemodel zelf: dat is pas aan de orde als de ADR-punten zijn
opgelost. Wel een besluit over de prioritering, want zonder keuze beweegt niets.
-->

---

<!-- 21. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div style="font-size: 1rem; line-height: 2.1; margin-top: 1.4rem;">

Volgende sessie:

- De gekozen versioneringsvariant, uitgewerkt in Public PR 100
- Het informatiemodel na de interne besluiten als pull request naar Public
- De keuzedeelregels, getoetst aan de scenario's

</div>

<div style="font-size: 0.95rem; color: var(--np-dark-gray); margin-top: 1.6rem;">
Op 6 oktober is de leeruitkomstendag; daar wordt het informatiemodel getoond. Commentaar op een lopende release: in de pull request. Nieuw punt: als issue op <strong>github.com/Npuls-OKx/Public</strong>
</div>

</div>

<!--
De drie regels volgen uit Gevraagd; de datum van 6 oktober komt uit de afstemming van
11 september. Geen andere data beloven.
-->

---

<!-- PEILING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe gaat het?

<div class="np-grid-2" style="margin-top: 1.2rem; gap: 1.8rem; align-items: center;">
<div style="font-size: 1.05rem; line-height: 2.2;">

- Welk cijfer krijgt de voortgang, en waarom?
- Wat ging er goed?
- Wat kan er beter?

</div>
<div>
  <div style="display: flex; gap: 0.32rem; justify-content: center;">
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #f3d9d4; color: #8a4038;">1</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #f6e0d2; color: #8a5638;">2</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #f8e8d1; color: #8a6a38;">3</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #f9f0d2; color: #7f7538;">4</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #f2f2d6; color: #6f7538;">5</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #e6f0da; color: #547038;">6</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #d8ecdd; color: #3d6b49;">7</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #cde7e4; color: #356663;">8</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #c2e0e9; color: #2d5c6b;">9</div>
    <div style="width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 600; background: #b7d8ef; color: #27506e;">10</div>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 0.5rem; font-size: 0.8rem; color: var(--np-mid-gray);">
    <span>loopt niet</span><span>loopt goed</span>
  </div>
</div>
</div>

</div>

<!--
Vaste afsluiting van elke sessie, zie meta #205. Het cijfer maakt de lijn over sessies
zichtbaar, de twee open vragen leveren de inhoud.
-->

---

<!-- AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
