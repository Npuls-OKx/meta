---
theme: default
title: "Kerngroep techniek, 1 september 2026"
info: "Update kerngroep techniek: voortgang sinds 19 augustus, de branchingstrategie en het releaseproces, en de reviewregels die daaruit volgen."
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
  <h1 style="font-size: 3.2rem; line-height: 1.15; margin-bottom: 0.8rem; color: var(--np-ink);">Kerngroep techniek</h1>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 1 september 2026</div>
</div>

<!--
Kort houden. Doorlopen: stand van zaken, voortgang, branching en release, reviewregels.
-->

---

<!-- 2. STAND VAN ZAKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Stand van zaken

```mermaid
flowchart LR
  A["v0.0.1<br/>alpha, 18 aug"] --> B["v0.0.2<br/>PR 82"]
  B --> X["0.0.x<br/>..."]
  X --> C["v0.1.0 beta<br/>bij de PoC"]
  C --> D["v1.0.0<br/>stabiel"]
  style A fill:#0B4F6C,stroke:#0B4F6C,color:#fff
  style X stroke-dasharray: 3 3
  style C stroke-dasharray: 5 5
  style D stroke-dasharray: 5 5
```

<div class="np-grid-2" style="margin-top: 1rem; font-size: 0.9rem; line-height: 1.7; gap: 1.6rem;">
<div>

**Gesloten sinds 19 augustus: 9**

- Requirementsboom overgeheveld: [#33](https://github.com/Npuls-OKx/Public/issues/33)
- Id-conventie voor eisen: [#37](https://github.com/Npuls-OKx/Public/issues/37), [#38](https://github.com/Npuls-OKx/Public/issues/38)
- Leesroute en verdieping per rij: [#60](https://github.com/Npuls-OKx/Public/issues/60), [#69](https://github.com/Npuls-OKx/Public/issues/69), [#70](https://github.com/Npuls-OKx/Public/issues/70)
- Engelse veldnamen in de schema's: [#8](https://github.com/Npuls-OKx/Public/issues/8)
- LMS-koppelvlakplaat gecorrigeerd: [#48](https://github.com/Npuls-OKx/Public/issues/48), review-opmerking verwerkt: [#28](https://github.com/Npuls-OKx/Public/issues/28)

</div>
<div>

**Ter review**

- [PR 82](https://github.com/Npuls-OKx/Public/pull/82): release v0.0.2

</div>
</div>

</div>

<!--
We staan op alpha. De doelen zijn nog niet bereikt, we werken ernaartoe. Dat is de toon
van het hele deck. PR 82 is de release-PR waar we straks de demo op doen.
-->

---

<!-- OPDRACHTEN VORIGE SESSIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Opdrachten vorige sessie

<div style="font-size: 0.95rem; line-height: 1.7; margin-top: 1rem;">

| Opdracht | Stand |
|---|---|
| De architectuurbesluiten doorlezen | Nog geen reacties binnen |
| Het referentiemateriaal doornemen: kaderscenario, persona, principes | Nog geen reacties binnen |
| Structuur en navigeerbaarheid beproeven, bevindingen als issue | Drie issues van buiten het projectteam |

</div>

<div style="font-size: 0.9rem; color: var(--np-dark-gray); margin-top: 1.4rem;">
De vraag vandaag: is er tijd voor geweest, en wat is ervoor nodig om dit wel te laten lukken?
</div>

</div>

<!--
Eerlijk beginnen: de opdrachten van 19 augustus zijn grotendeels blijven liggen. Niet als
verwijt, wel als vraag. Wat helpt: minder materiaal tegelijk, een kortere lijst, of meer tijd?
-->

---

<!-- REFERENTIEMATERIAAL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar het materiaal staat

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem; font-size: 0.92rem; line-height: 1.8;">
<div>

**Om te lezen**

- [Architectuurbesluiten](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr): 26 besluiten, alle met status voorstel
- [Kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/kaderscenario's): de keten van begin tot eind
- [Persona Jochem](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/persona's): de student die door dat scenario loopt

</div>
<div>

**Om op te bouwen**

- [Principes en uitgangspunten](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/principes): waarom en hoe
- [Requirementsboom](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/requirementsboom): van doel naar eis
- [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties): het releasepakket

</div>
</div>

</div>

<!--
Concreet maken wat er te lezen is, zodat de oproep aan het eind niet in het luchtledige
hangt. De besluiten dragen allemaal de status voorstel: commentaar erop is nog van invloed.
-->

---

<!-- 3. OPEN WERK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Open werk

<div class="np-grid-2" style="margin-top: 0.9rem; gap: 1.6rem; font-size: 0.86rem; line-height: 1.55;">
<div>

**Vijf milestones met openstaand werk**

| Milestone | Open |
|---|---|
| [Releaseproces en kwaliteit](https://github.com/Npuls-OKx/Public/milestone/4) | 10 |
| [Requirementsboom doorontwikkelen](https://github.com/Npuls-OKx/Public/milestone/3) | 9 |
| [Interactiepatroon-documenten](https://github.com/Npuls-OKx/Public/milestone/5) | 7 |
| [Leerroute-refactor](https://github.com/Npuls-OKx/Public/milestone/1) | 4 |
| [Keuzedelen](https://github.com/Npuls-OKx/Public/milestone/7) | 3 |

</div>
<div>

**Vermoedelijk werk zonder issue**

- Informatiemodel eerst reviewen, dan de payloads
- Supporttermijn en deprecatie: AP06 belooft het, het releasedocument sluit het uit
- Eigenaarschap en RACI van het releasepakket: het template is er, nooit ingevuld

</div>
</div>

</div>

<!--
Rechts staat wat tussen wal en schip dreigt te vallen: besproken werk dat nooit een
issue kreeg. Vraag de groep of ze er meer zien. De issues onder Informatiestromen
hoofdplaat zijn inmiddels met een highlight opgelost en staan hier niet meer bij; de
harness-issues horen op meta, niet op Public.
-->

---

<!-- 4. OPENSTAANDE ITEMS 19 AUGUSTUS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voortgang issues vorige meeting

<div style="font-size: 0.92rem; line-height: 1.6; margin-top: 0.8rem;">

| Item | Vervolgactie |
|---|---|
| [#47](https://github.com/Npuls-OKx/Public/issues/47) versionering tussen koppelingen | Voorstel volgt als pull request |
| [#51](https://github.com/Npuls-OKx/Public/issues/51) releases via pull request | Ingericht, PR 82 loopt deze route |
| [#45](https://github.com/Npuls-OKx/Public/issues/45) klikbare referenties | Deels opgenomen in de requirementsboom |
| [#46](https://github.com/Npuls-OKx/Public/issues/46) tags van releases bewaren | Opgelost via de release branches; issue nog bij te werken |
| [#44](https://github.com/Npuls-OKx/Public/issues/44) werkwijze issuesessie | Nog niet opgepakt |
| Informatiemodel eerst reviewen, dan payloads | **Geen issue, dus niet opgepakt** |

</div>

</div>

<!--
De laatste regel is het punt van deze slide. Kees en Jos vroegen op conceptueel niveau
over het informatiemodel te sparren voordat we de payloads in gaan. Dat is nooit een
issue geworden en is daardoor blijven liggen. Vraag: wat missen we nog meer?
-->

---

<!-- 4. DIVIDER VOORTGANG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 1</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Voortgang</h1>
  </div>
</div>

---

<!-- 5. REQUIREMENTSBOOM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Requirementsboom

<div style="font-size: 0.8rem; margin-top: 0.5rem;">

```mermaid
flowchart LR
  LZD["Leren zonder Drempels"] --> DL1 & DL2 & DL3
  subgraph doelen["OKx-projectdoelen"]
    DL1["doel-0001 gezamenlijke taal"]
    DL2["doel-0002 gegevensuitwisseling"]
    DL3["doel-0003 keuze"]
  end
  DL1 --> EP1["epic-0001"]
  DL2 --> EP2["epic-0002 t/m 0005"]
  DL3 --> EP6["epic-0006 t/m 0008"]
  EP1 & EP2 & EP6 -.-> FT["features"] -.-> ST["stories"]
```

</div>

<div style="font-size: 0.92rem; line-height: 1.8; margin-top: 0.8rem;">

- De structuur staat: van doel via epic en feature naar story, en door naar de eis
- Klikbaar in beide richtingen, deels antwoord op [#45](https://github.com/Npuls-OKx/Public/issues/45)
- Verdieping loopt in milestone [Requirementsboom doorontwikkelen](https://github.com/Npuls-OKx/Public/milestone/3)

</div>

</div>

<!--
De boom is de koppeling tussen business en techniek, beschreven in ADR 0025 (voorstel).
Negen van de 28 stories reiken nu tot een functionele eis; de rest volgt. De verdieping
zit in de milestone, met onder meer de keuzesemantiek (#64).
-->

---

<!-- CALL TO ACTION BOOM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Loop het wensen- en eisenpakket door

<div style="font-size: 0.92rem; color: var(--np-dark-gray); margin-top: 0.4rem;">
Voordat we gaan bouwen moeten we scherp hebben wat we willen en wat we moeten kunnen.
</div>

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem;">
<div style="font-size: 1rem; line-height: 2;">

**Drie vragen, via [PR 82](https://github.com/Npuls-OKx/Public/pull/82)**

- Wat mis je?
- Wat staat er goed?
- Is dit de juiste vorm?

</div>
<div style="font-size: 0.95rem; line-height: 1.9;">

**Hulp bij het doorlopen**

- Een sessie van een uur per leverancier, via Teams
- De wekelijkse inloop op vrijdag

</div>
</div>

</div>

<!--
Dit is de belangrijkste vraag van de sessie. Concreet: welke epics, features, stories en
functionele eisen mis je voor jouw koppeling, en klopt de vorm waarin ze staan. Ruud
plant de individuele sessies; drempel bewust laag.
-->

---

<!-- 7. DIVIDER RELEASE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Deel 2</p>
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Branching en release</h1>
  </div>
</div>

---

<!-- BRANCHMODEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill" style="padding: 1.2rem 2.4rem;">

<div style="display: flex; align-items: baseline; gap: 1rem; margin-bottom: 0.4rem;">
  <h1 style="font-size: 1.9rem; margin: 0;">Branchmodel</h1>
  <span style="font-size: 0.8rem; color: var(--np-mid-gray);">Voorstel, Public PR 81</span>
</div>

<div style="flex: 1; min-height: 0; display: flex; justify-content: center; align-items: center;">
  <img src="/platen/release-branching.png" style="max-height: 100%; max-width: 100%; object-fit: contain; border-radius: 8px; border: 1px solid #e2e8f0; background: #fff;" />
</div>

</div>

<!--
Toelichting door Garik. De huidige en de vorige majorversie blijven allebei bestaan,
als branch en als pakket.
-->

---

<!-- 9. RELEASEPROCES -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Van bron naar releasepakket

```mermaid
flowchart LR
  F["feature branch"] -->|PR, interne review| D["dev"]
  D -->|kloon| R["release branch<br/>bronbestanden"]
  R -->|PR| K{"tests en<br/>review"}
  K -->|akkoord| N["release branch N<br/>en N-1"]
  N --> B["CI-build"]
  B --> P["releasepakket"]
  style K fill:#0B4F6C,stroke:#0B4F6C,color:#fff
```

<div style="font-size: 0.92rem; line-height: 1.8; margin-top: 0.9rem;">

- Feature branch met pull request naar dev: de interne review
- Dev wordt gekloond naar een release branch, met alle bronbestanden erin
- Vanaf die release branch een pull request ter review voor de kerngroep techniek
- Na akkoord landen de bronbestanden op release branch N; de vorige blijft als N-1 staan
- Daarna start de CI de build; de bronbestanden blijven refereerbaar ([#46](https://github.com/Npuls-OKx/Public/issues/46))
- De build levert ook het volledige document als markdown, zodat twee versies naast elkaar te leggen zijn

</div>

</div>

<!--
Twee reviewmomenten: intern op de feature branch, extern op de release branch. De kloon
zorgt dat doorlopend werk op dev de release niet verschuift, en houdt de bronbestanden
bij de release zodat je er later naar kunt verwijzen.
-->

---

<!-- 9. WAT IS EEN PULL REQUEST -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat is een pull request

<div style="font-size: 1.05rem; line-height: 2.2; margin-top: 1.4rem;">

- Een voorstel tot wijziging, met de aanleiding erbij
- Regel voor regel te bekijken en van commentaar te voorzien
- Automatische controles draaien mee en moeten slagen
- Pas na goedkeuring gaat de wijziging erin

</div>

</div>

<!--
Voor wie GitHub niet dagelijks gebruikt. Dit is de aanloop naar de demo en naar de
vraag daarna: wanneer is een pull request gedragen door de kerngroep techniek.
-->

---

<!-- 11. DIVIDER DEMO -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide14.PNG);"></div>

<div class="flex items-center justify-center h-full">
  <div style="text-align: center;">
    <p class="eyebrow" style="color: rgba(255,255,255,0.85);">Demo</p>
    <h1 style="color: #FFFFFF !important; font-size: 2.6rem;">Reviewen via een pull request</h1>
  </div>
</div>

---

<!-- 12. RESUME DEMO -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Reviewen in vier stappen

<div style="font-size: 0.95rem; line-height: 1.5; margin-top: 0.7rem; max-width: 760px;">

<div class="np-step"><span class="np-num">1</span>Opgemaakte weergave van de wijziging</div>
<div class="np-step"><span class="np-num">2</span>Commentaar per regel</div>
<div class="np-step"><span class="np-num">3</span>Review indienen</div>
<div class="np-step"><span class="np-num">4</span>Automatische controles: werken de verwijzingen nog</div>

</div>

<div style="font-size: 0.88rem; color: var(--np-dark-gray); margin-top: 0.8rem;">
De controles groeien mee: verwijzingen, diagrammen tegen de schema's, navigeerbaarheid van de boom.
</div>

</div>

<!--
Live in GitHub op PR 82, de release van v0.0.2. Doel: de groep weet na afloop waar de
review plaatsvindt en waar te klikken. Bij de controles: dit is geen afvinklijst maar
een groeiend vangnet. Suggesties voor nieuwe controles zijn welkom als issue.
-->

---

<!-- 11. REVIEWREGELS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Afspraken bij een pull request-review

<div style="font-size: 0.82rem; color: var(--np-mid-gray); margin-bottom: 0.5rem;">Status: concept</div>

<div style="font-size: 0.9rem; line-height: 1.55;">

| | Voorzet |
|---|---|
| **Goedkeuringen** | Minimaal een per leverancier die de koppeling bouwt, plus een vanuit de sector |
| **Tester** | Automatische controles, aangevuld met een mens die de testgevallen naloopt |
| **Reviewer** | Een ander persoon dan de tester, beoordeelt de inhoud |
| **Termijn** | Twee weken, tot de volgende sessie |
| **Nooit** | Een review door de maker van de wijziging |

</div>

<dl class="np-besluit" style="margin-top: 0.9rem;">
  <dt>Besluit nodig op</dt><dd>zijn we het eens met dit concept?</dd>
</dl>

</div>

<!--
Voorzet, bewust concreet zodat er iets ligt om op te reageren. Open vraag in de zaal:
is een goedkeuring per bouwende leverancier haalbaar, en wie vertegenwoordigt de sector?
-->

---

<!-- 12. OPENSTAANDE PUNTEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Openstaande punten

<div style="font-size: 0.9rem; line-height: 1.6; margin-top: 0.8rem;">

| | Vervolgactie |
|---|---|
| **Versionering per koppeling** ([#47](https://github.com/Npuls-OKx/Public/issues/47)) | Voorstel eerst intern in het kernteam, daarna als PR hierheen |
| **Meerdere instanties van een referentiecomponent** ([meta #80](https://github.com/Npuls-OKx/meta/issues/80)) | Uitwerken, nog geen uitspraak |
| **Keuzes en regelsets** ([#74](https://github.com/Npuls-OKx/Public/issues/74)) | Keuzeregel-typologie toetsen aan echte scenario's |
| **Informatiemodel voor payloads** | Issue aanmaken, dan agenderen |

</div>

<dl class="np-besluit" style="margin-top: 1rem;">
  <dt>Input gevraagd</dt><dd>waar ligt de prioriteit, en welke issues missen we nog</dd>
</dl>

</div>

<!--
Alleen echte openstaande punten. Voorstel voor de route: eerst interne review in het
kernteam OKx, en pas als dat staat een pull request hierheen. Vraag de groep expliciet
of er nog meer werk is dat wel besproken is maar nooit een issue werd.
-->

---

<!-- 13. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<dl class="np-besluit review" style="margin-top: 1rem;">
  <dt>Review</dt><dd>de requirementsboom in PR 82: welke epics, features, stories en functionele eisen mis jij? Tot de volgende sessie</dd>
</dl>

<dl class="np-besluit" style="margin-top: 0.8rem;">
  <dt>Besluit</dt><dd>de afspraken voor een pull request-review, en de prioritering van de openstaande punten</dd>
</dl>

<dl class="np-besluit kennisname" style="margin-top: 0.8rem;">
  <dt>Input</dt><dd>welke issues missen we nog</dd>
</dl>

<dl class="np-besluit kennisname" style="margin-top: 0.8rem;">
  <dt>Lezen</dt><dd>de architectuurbesluiten en de kaderscenario's; alle besluiten staan op voorstel, dus commentaar telt nog</dd>
</dl>

</div>

<!--
Alleen PR 82 gaat naar deze groep ter review. De andere pull requests lopen intern.
-->

---

<!-- 14. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div style="font-size: 1rem; line-height: 2.1; margin-top: 1.4rem;">

Volgende sessie:

- Versioneringsvoorstel als pull request
- Uitkomst van de review op v0.0.2
- De issues die vandaag ontbraken

</div>

<div style="font-size: 0.95rem; color: var(--np-dark-gray); margin-top: 1.6rem;">
Over drie maanden: start bouw op een eerste betaversie van de koppelvlakken OC naar SIS, OC naar P&amp;R en OC naar LMS. Commentaar op een release: in de pull request. Nieuw punt: als issue op <strong>github.com/Npuls-OKx/Public</strong>
</div>

</div>

<!--
Onderscheid benoemen: commentaar op een lopende release hoort in de pull request,
een nieuw onderwerp wordt een issue.
-->

---

<!-- PEILING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe gaat het?

<div class="np-grid-2" style="margin-top: 1.2rem; gap: 1.8rem; align-items: center;">
<div style="font-size: 1.05rem; line-height: 2.2;">

- Welk cijfer geef je de voortgang, en waarom?
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
Vaste afsluiting van elke sessie. Vandaag mondeling; de peiling via QR-code staat als
issue op meta. Het cijfer maakt de lijn over sessies zichtbaar, de twee open vragen
leveren de inhoud.
-->

---

<!-- AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
