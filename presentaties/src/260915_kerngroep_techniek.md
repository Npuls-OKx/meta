---
theme: default
title: "Kerngroep techniek, 15 september 2026"
info: "Kerngroep techniek 15 september 2026: stories, applicatiediensten en versionering, informatiemodel."
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
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 34rem;">Stories &middot; Applicatiediensten en versionering &middot; Informatiemodel</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">OKx &middot; Npuls &middot; 15 september 2026</div>
</div>

<!--
Ruud is afwezig. Niek en Garik trekken de sessie. Twee thema's: modulariteit en versionering
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
  A --> C["Informatiemodel en begrippenlijst<br/>Public PR 104, gestapeld"]
```

<div style="font-size: 0.92rem; line-height: 1.7; margin-top: 1rem;">

| Afgesproken op 1 september | Stand |
|---|---|
| Versioneringsvoorstel als pull request | Ligt er: [Public PR 100](https://github.com/Npuls-OKx/Public/pull/100), groter geworden dan aangekondigd |
| Uitkomst van de review op v0.0.2 | Twee reacties binnen, zie de volgende slide |
| Informatiemodel eerst reviewen, dan de payloads | Ligt er: [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104), laag 1 en 2 van de informatie- en gegevensmodellen |

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

# Review op v0.0.2: twee reacties, één rode draad

<div style="font-size: 0.95rem; line-height: 1.7; margin-top: 0.6rem;">

- Xedule en YNC: een pdf met opmerkingen per story ([Public #99](https://github.com/Npuls-OKx/Public/issues/99))
- Kees en Luke: 28 reviewopmerkingen op inleiding, ADR 0025, epics, features en stories ([Public PR 82](https://github.com/Npuls-OKx/Public/pull/82), 14 september); de formele review volgt

</div>

<div class="np-grid-3" style="margin-top: 0.9rem; gap: 1rem;">
<div class="np-card" style="font-size: 0.9rem; line-height: 1.45;"><strong>Applicatiefunctionaliteit, geen koppelvlak</strong><br/>Stories en features beschrijven hoe een onderwijscatalogus werkt of wat een school kiest, niet de interactie tussen systemen</div>
<div class="np-card" style="font-size: 0.9rem; line-height: 1.45;"><strong>Uitgangspunt of feature</strong><br/>Leeruitkomsten als gegeven, versionering, query-parameters: uitgangspunten en implementatiekeuzes staan als feature</div>
<div class="np-card" style="font-size: 0.9rem; line-height: 1.45;"><strong>Notify of transactie</strong><br/>Wanneer informeren systemen elkaar en wanneer verandert een aanroep echt iets; wie is de client van het endpoint en wie is waarvoor verantwoordelijk</div>
</div>

<div class="np-card accent-green" style="margin-top: 0.9rem; font-size: 0.95rem; background: #F3FAF6;">
Voorstel van Kees en Luke voor vandaag: eerst vaststellen wat een koppelvlakspecificatie bepaalt en vastlegt, dan pas de inhoud van de stories.
</div>

</div>

<!--
Twee reacties op v0.0.2. De pdf van Xedule en YNC (#99) bevat acht pagina's opmerkingen per
story; Niels heeft daarop geantwoord dat de stories met de PoC-instellingen verder worden
aangepakt. Kees en Luke hebben op 14 september de epics, features en stories bekeken: 28
opmerkingen op PR 82 (inleiding 3, ADR 0025 1, epics 3, features 15, stories 6), de review
zelf volgt via GitHub. Hun overkoepelende gevoel, per mail aan Niek: het neigt naar een
functionele beschrijving van applicaties of componenten of naar beleidskeuzes van een school,
in plaats van een aanloop naar een koppelvlakspecificatie; dezelfde afdronk als in #99. Voorbeelden
uit de opmerkingen: "is onderwijscatalogusfunctionaliteit, niet iets met koppelvlak te maken"
(stories 9 en 19), "je kiest hier hoe een school zijn onderwijs gaat doen" (epics 14), "is dit
geen uitgangspunt in plaats van feature" (features 41, 42, 44), "wanneer transactioneel en
synchroon" (features 39, 70), "wat we missen is de client van het endpoint" (ADR 0025), "welke
verbintenistoestand, opleiding of leergelegenheid; beschrijf wat de docent wil doen" (stories 58).
De reacties uit de demo van 1 september tellen niet als review. Vragend stellen: het voorstel
om eerst het kader te bespreken past bij het eerste agendapunt.
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
| Informatiemodel voor payloads ([meta #163](https://github.com/Npuls-OKx/meta/issues/163)) | Uitgewerkt in [meta PR 225](https://github.com/Npuls-OKx/meta/pull/225), ter review voor leveranciers in [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104); vandaag op tafel |

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
    <h1 style="color: #FFFFFF !important; font-size: 3rem;">Modulariteit en versionering</h1>
  </div>
</div>

<!--
Blok van Garik. De opzet staat; Garik vervangt en vult aan met zijn
eigen sheets, voorbeeld en diagrammen.
-->

---

<!-- BOUWBLOKKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Bouwblokken van de koppelvlakspecificatie

<div style="margin-top: 2.5rem;">

```mermaid {scale: 0.75}
flowchart LR
  KV["Koppelvlakspecificatie"] -->|bevat| K["Koppelingspecificaties"]
  K -->|bevatten elk| D["Berichtstromen"]
  D -->|gebruiken| A["Applicatiediensten"]
  D -->|gerealiseerd met| I["Interactiepatronen"]
```

</div>

</div>

---

<!-- KOPPELINGSPECIFICATIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Koppelingspecificatie

<div class="np-card accent-blue" style="margin-top: 2.2rem; max-width: 85%;">
  <p style="font-size: 1.45rem; line-height: 1.6; color: var(--np-ink); margin: 0;">Een benoemde verbinding tussen twee of meer componenten die met elkaar moeten interacteren. Per interactie bevat zij een lijst van berichtstromen.</p>
</div>

</div>

---

<!-- DATASTROMEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Berichtstromen

<div class="np-card accent-blue" style="margin-top: 2.2rem; max-width: 85%;">
  <p style="font-size: 1.45rem; line-height: 1.6; color: var(--np-ink); margin: 0;">Een verzameling gegevensstromen die gegevens tussen systemen overdraagt.</p>
</div>

</div>

---

<!-- APPLICATIEDIENSTEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Applicatiediensten

<div class="np-card accent-blue" style="margin-top: 2.2rem; max-width: 85%;">
  <p style="font-size: 1.45rem; line-height: 1.6; color: var(--np-ink); margin: 0;">Een verzameling koppelvlakfunctionaliteiten die een component kan implementeren.</p>
</div>

<div class="np-grid-2" style="margin-top: 1.2rem; max-width: 85%;">
  <div class="np-card"><p style="font-size: 1.1rem; margin: 0;">Een verzameling endpoints</p></div>
  <div class="np-card"><p style="font-size: 1.1rem; margin: 0;">Het vermogen om specifieke soorten gegevens af te nemen</p></div>
</div>

</div>

---

<!-- INTERACTIEPATRONEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Interactiepatronen

<div style="font-size: 1.0rem; line-height: 1.6; margin-top: 0.4rem;">
Een interactiepatroon beschrijft hoe twee partijen informatie uitwisselen, los van welke partijen dat zijn en welke informatie het betreft. Een koppelingspecificatie kiest per interactie een patroon en vult het in; het patroon staat één keer, in rollen: de <strong>bezitter</strong> van de resource en de <strong>consument</strong>.
</div>

<div style="font-size: 0.86rem; line-height: 1.4; margin-top: 0.8rem; max-width: 92%;">

| Patroon | Waarvoor | Naam uit |
|---|---|---|
| [Event Notification](https://github.com/Npuls-OKx/Public/blob/feature/restructure-and-versioning/Koppelvlakspecificaties/Interactiepatronen/event-notification.md) | De bezitter meldt dat er iets is; de consument haalt het op wanneer het hem uitkomt | Fowler |
| [Event-Carried State Transfer](https://github.com/Npuls-OKx/Public/blob/feature/restructure-and-versioning/Koppelvlakspecificaties/Interactiepatronen/event-carried-state-transfer.md) | Het event draagt de wijziging zelf; de ontvanger hoeft niets op te halen | Fowler |
| [Asynchronous Request-Reply](https://github.com/Npuls-OKx/Public/blob/feature/restructure-and-versioning/Koppelvlakspecificaties/Interactiepatronen/asynchronous-request-reply.md) | De verwerking duurt; de uitkomst komt terug als apart bericht | Azure Cloud Design Patterns, AIP-151 |
| [Request-Reply](https://github.com/Npuls-OKx/Public/blob/feature/restructure-and-versioning/Koppelvlakspecificaties/Interactiepatronen/request-reply.md) | De afnemer vraagt zelf op, zonder voorafgaand event | Enterprise Integration Patterns |
| [Subscription registration](https://github.com/Npuls-OKx/Public/blob/feature/restructure-and-versioning/Koppelvlakspecificaties/Interactiepatronen/subscription-registration.md) | Vastleggen waar events afgeleverd mogen worden | WebSub (W3C), CloudEvents Subscriptions |

</div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 0.7rem;">
Vijf patronen, alle uit bestaande catalogi onder de naam die daar geldt. Bron: <code>Koppelvlakspecificaties/Interactiepatronen/</code> in Public PR 100.
</div>

</div>

<!--
Uit de README van de interactiepatronen op de branch van Public PR 100. Twee onderscheidingen
bepalen de keuze: of het event genoeg draagt om zonder opvraag te handelen scheidt de eerste
twee; wie begint scheidt de derde van de vierde. Wie bezitter en wie consument is volgt uit
resource-eigenaarschap (U3) en wisselt per resource, ook binnen een koppeling. De eisen aan
aflevering, idempotentie, foutafhandeling en volgorde staan in ADR 0018.
-->

---

<!-- VOORBEELD INTERACTIEPATROON -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorbeeld: Event Notification

<div class="np-grid-2" style="margin-top: 0.4rem; gap: 1.6rem; align-items: start; grid-template-columns: 1.15fr 1fr;">
<div>

```mermaid
sequenceDiagram
    autonumber
    participant B as Bezitter
    participant C as Consument
    Note over B: De resource wijzigt
    B-)C: Event: resource-id en versie
    Note over C: Moment van ophalen bepaalt de consument
    C->>B: Opvraag op id en versie
    B-->>C: De resource, of de delta tussen twee versies
```

</div>
<div style="font-size: 0.95rem; line-height: 1.6;">

- Het event draagt de aanleiding, de opvraag draagt de inhoud
- De consument kiest het moment en de vorm: de volledige structuur of de delta
- Een gemist event is herstelbaar, want de inhoud blijft bij de bezitter
- Geen bevestiging en geen termijn; wil de bezitter de uitkomst weten, dan is dat Asynchronous Request-Reply

<div class="np-card" style="margin-top: 0.8rem; font-size: 0.9rem;">
Vastgelegd als uitgangspunt U4. Toegepast in alle drie de koppelingen: de onderwijscatalogus meldt dat een specificatie planbaar, beschikbaar of gewijzigd is; planning, SIS en LMS halen de structuur of de delta op.
</div>

</div>
</div>

</div>

<!--
Uit event-notification.md op de branch van Public PR 100. De naam en afbakening komen van
Martin Fowler; dat het bericht een verwijzing draagt in plaats van de inhoud is Claim Check,
in CloudEvents het attribuut dataref. Het event is idempotent op event-id en de volgorde blijft
behouden per resource-id. Het verschil met Event-Carried State Transfer: daar is een verloren
bericht verloren informatie, hier haalt de consument alsnog op met Request-Reply.
-->

---

<!-- VOORBEELD UIT DE SPECIFICATIE -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorbeeld uit de koppelvlakspecificatie

<div style="margin-top: 1.4rem;">

```mermaid {scale: 0.58}
%%{init: {"flowchart": {"wrappingWidth": 460}}}%%
flowchart LR
  KV["<small>KOPPELVLAKSPECIFICATIE</small><br/>Koppelvlakspecificatie OKx"] -->|bevat| K["<small>KOPPELINGSPECIFICATIE</small><br/>Onderwijscatalogus naar<br/>planning en roostering"]
  K -->|bevat| D["<small>BERICHTSTROOM</small><br/>Opleidingsaanbod aanmaken<br/><i>1 van 7 berichtstromen</i>"]
  D -->|gebruikt| A["<small>APPLICATIEDIENSTEN</small><br/>onderwijsspecificatiestructuur-aanbieder<br/>onderwijsspecificatiestructuur-afnemer<br/>verwerkingsuitkomst-afnemer<br/>planbaar-onderwijsaanbod-aanbieder"]
  D -->|gerealiseerd met| I["<small>INTERACTIEPATRONEN</small><br/>Event Notification<br/>Asynchronous Request-Reply"]
```

</div>

</div>

---

<!-- VERSIONERING: NIVEAU -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Versionering op het niveau van berichtstromen

<div class="np-grid-2" style="margin-top: 2.2rem; max-width: 85%;">
  <div class="np-card accent-blue"><p style="font-size: 1.3rem; line-height: 1.55; margin: 0;">Elke berichtstroom kan een versie dragen</p></div>
  <div class="np-card accent-green"><p style="font-size: 1.3rem; line-height: 1.55; margin: 0;">Versies bestaan meestal naast elkaar, in plaats van elkaar te vervangen</p></div>
</div>

</div>

---

<!-- VERSIONERING: AFHANKELIJKHEDEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat een berichtstroom nodig heeft

<div style="margin-top: 1.6rem;">

```mermaid {scale: 0.75}
flowchart LR
  subgraph KV["Koppelvlakspecificatie"]
    D["Berichtstroom"] --> A["Applicatiediensten"] --> E["Endpoints"]
  end
  subgraph DM["Apart pakket"]
    S["Datamodelschema's"]
  end
  E -->|ondersteunde versies| S
```

</div>

<div class="np-bottomline" style="margin-top: 1.6rem;">
  Welke applicatiediensten en endpoints beschikbaar zijn, bepaalt de <strong>versie van de koppelvlakspecificatie</strong>.
</div>

</div>

---

<!-- VERSIONERING: VOORBEELD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorbeeld: koppelvlakspecificatie 0.5

<div class="np-grid-3" style="margin-top: 2rem; max-width: 85%; text-align: center;">
  <div class="np-card"><div class="np-big-number">5</div><p style="font-size: 1.05rem; margin: 0.6rem 0 0;">berichtstromen</p></div>
  <div class="np-card"><div class="np-big-number">20</div><p style="font-size: 1.05rem; margin: 0.6rem 0 0;">applicatiediensten</p></div>
  <div class="np-card"><div class="np-big-number">0.5</div><p style="font-size: 1.05rem; margin: 0.6rem 0 0;">versie</p></div>
</div>

<div class="np-bottomline" style="margin-top: 1.6rem;">
  Alle applicatiediensten dragen versie 0.5, de versie van de koppelvlakspecificatie.
</div>

</div>

---

<!-- VERSIONERING: OPHOGEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wanneer de versie ophoogt

<div class="np-grid-2" style="margin-top: 2rem; max-width: 90%; align-items: start;">
  <div class="np-card accent-green">
    <span class="np-badge green">Patch</span>
    <p style="font-size: 1.15rem; line-height: 1.55; margin: 0.7rem 0 0;">Een berichtstroom toevoegen of wijzigen zonder iets te breken, zolang die bestaande applicatiediensten en interactiepatronen gebruikt</p>
  </div>
  <div class="np-card accent-orange">
    <span class="np-badge orange">Major, minor of patch</span>
    <p style="font-size: 1.15rem; line-height: 1.55; margin: 0.7rem 0 0;">Applicatiediensten toevoegen, bijwerken of wijzigen; de zwaarte van de wijziging bepaalt de ophoging</p>
  </div>
</div>

</div>

---

<!-- 6. HET PROBLEEM -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Een veld erbij in een datamodel, en dan?

```mermaid {scale: 0.7}
flowchart LR
  D["Datamodel<br/>+1 veld"]:::bron
  D --> E1["Endpoint"]:::geraakt & E2["Endpoint"]:::geraakt
  E1 --> A1["Applicatiedienst"]:::geraakt & A2["Applicatiedienst"]:::geraakt
  E2 --> A2 & A3["Applicatiedienst"]:::geraakt
  A1 --> B1["Berichtenstroom"]:::geraakt & B2["Berichtenstroom"]:::geraakt
  A2 --> B2 & B3["Berichtenstroom"]:::geraakt
  A3 --> B3 & B4["Berichtenstroom"]:::geraakt
  B1 --> K1["Koppeling"]:::geraakt
  B2 --> K1
  B3 --> K2["Koppeling"]:::geraakt
  B4 --> K2
  classDef bron fill:#E07A4B,stroke:#E07A4B,color:#fff
  classDef geraakt fill:#FBE3D6,stroke:#E07A4B,color:#1F2937
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
Gezocht: welke variant sluit het best aan bij de ervaring in het veld, A, B of een andere.
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
- Status: concept; gereviewd in [meta PR 225](https://github.com/Npuls-OKx/meta/pull/225) en gepubliceerd als laag 1 en 2 van het pakket informatie- en gegevensmodellen in [Public PR 104](https://github.com/Npuls-OKx/Public/pull/104), gestapeld op PR 100. Twee ontwerpkeuzes liggen bij het kernteam ([meta #227](https://github.com/Npuls-OKx/meta/issues/227), [#228](https://github.com/Npuls-OKx/meta/issues/228)); de modelvragen uit de tegenlezing staan in [meta #234](https://github.com/Npuls-OKx/meta/issues/234)

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
Het informatiemodel OKx, versie v0.1, stand 14 september. Leeswijzer: de kolommen zijn de begrippen,
van kwalificatiekader links tot resultaatstructuur onderaan. Geel is het OKx-referentiekader,
grijs valt buiten scope. De leeruitkomst, tweede kolom, is de sleutel: elke specificatie en de
summatieve resultaatstructuur wijzen ernaar. Bron: architecture/model/informatiemodel/ in meta,
branch van PR 225, nu ook in Public PR 104 als Informatie-en-gegevensmodellen/informatiemodel.md.
Op de sessie inzoomen in de browser of het document ernaast openen.
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
OEAPI-object is de vorm waarin een OKx-objecttype over de lijn gaat. Versie v0.1, stand
14 september. De bevindingen staan op de volgende slide.
-->

---

<!-- 15. BEVINDINGEN OEAPI -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat de mapping op OEAPI v6 laat zien

<div style="font-size: 0.98rem; line-height: 1.9; margin-top: 1rem;">

- Eén OEAPI-object draagt vaak meerdere OKx-objecttypen: `Programme` vier, `ProgrammeOffering` drie
- De leeruitkomst heeft een tegenhanger, `LearningOutcome`
- De resultaatstructuur is nog niet gemapt: OEAPI kent cesuur, schaal en pogingen per toetsonderdeel, maar geen weging per specificatie en geen aggregatieregel
- 24 objecttypen binnen scope zonder OEAPI-object: per stuk signalering of bewuste afwijking

</div>

<div class="np-card" style="margin-top: 1.2rem; font-size: 0.98rem;">
Gezocht: hoe mapt OEAPI een kwalificatiekader naar objecten? Kwalificatiedossier, kwalificatie, kerntaak en werkproces hebben in de mapping nu geen tegenhanger.
</div>

</div>

<!--
Bron: informatiemodel-oeapi-mapping.md. Geverifieerd tegen de OEAPI 6.0 OpenAPI-specificatie:
LearningOutcome bestaat met eigen endpoints. Voor de resultaatstructuur is de mapping nog niet
gemaakt; wat er tot nu toe gevonden is: weight staat per resultaat, niet per specificatie;
passFrom (cesuur), resultValueType (schaal) en attempts staan op het toetsonderdeel; final op
het resultaat; het afrondingscriterium over onderdelen heen bestaat alleen als vrije tekst in
qualificationRequirements. Of het kan is niet vastgesteld. Andersom kent OEAPI objecten die de
plaat niet heeft: Organisation, AcademicSession, Membership en de poging (Attempt). De vraag over het kwalificatiekader is
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

<div style="font-size: 0.7rem; line-height: 1.3; margin-top: 0.4rem; max-width: 88%;">

| Begrip | Definitie | Herkomst | ROSA | MORA | HORA |
|---|---|---|---|---|---|
| `Kwalificatie dossier` | Het kwalificatiedossier beschrijft de eisen waaraan een student moet voldoen om zijn diploma te behalen | overgenomen uit MORA | geen tegenhanger | <a href="https://mora.mbodigitaal.nl/index.php/Id-3389d485-20a7-6e53-21df-d09eb49d4762">Kwalificatie dossier</a> | nog niet onderzocht |
| `Onderwijsverbintenis` | Een afspraak voor het gaan volgen, volgen en hebben gevolgd van onderwijs | overgenomen uit ROSA | <a href="https://rosa.wikixl.nl/index.php/Id-ec977035c9be4b01bb1c14a5950a1799">onderwijsdeelname</a> | geen tegenhanger | nog niet onderzocht |
| `Onderwijseenheid specificatie` | De specificatie van de fundamentele eenheid waarin onderwijs wordt ontworpen en aangeboden | afgeleid uit klus 53 | <a href="https://rosa.wikixl.nl/index.php/Id-c74c161c6f1f4690933a31ce4d11f3b8">onderwijseenheid</a> | <a href="https://mora.mbodigitaal.nl/index.php/Id-17db36ca-368f-450e-cbfe-604b2fafee6e">Opleidings-onderdeel</a> | nog niet onderzocht |
| `Toetsgelegenheid` | Het georganiseerde aanbod van een toetsmoment: wanneer, waar en onder welke condities | afgeleid uit klus 53 | geen tegenhanger | geen tegenhanger | nog niet onderzocht |
| `Keuzedeelruimte` | Een oningevuld keuzedeel: vrijgemaakte ruimte waarin een student een keuzedeel kiest | nieuw voor OKx | geen tegenhanger | geen tegenhanger | nog niet onderzocht |

</div>

<div style="font-size: 0.8rem; color: var(--np-dark-gray); margin-top: 0.6rem;">
Uitsnede: vijf van de 73 begrippen en objecttypen. Status: v0.2, concept. MORA en ROSA zijn geraadpleegd, HORA volgt.
</div>

</div>

<!--
Uitsnede uit begrippen.md in Public PR 104, stand 14 september. Definities
zijn ingekort tot de eerste zin; de volledige tekst staat in de lijst met citaat, URL en
ophaaldatum. De vijf rijen laten de vier soorten zien: overgenomen uit MORA, overgenomen uit
ROSA, twee die zijn afgeleid uit de alignment MORA en HORA (klus 53), en een eigen OKx-definitie
zonder tegenhanger. Stand van de hele lijst op 14 september: 73 begrippen, 22 overgenomen,
18 eigen OKx-definitie, 33 nog open.
-->

---

<!-- 17a. KEUZE: WAT IS INTEKENEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waarop teken je in: de specificatie, of aanbod in een van zijn fasen?

<div style="font-size: 0.92rem; line-height: 1.5; margin-top: 0.2rem;">
De plaat onderscheidt nu drie stappen: het <code>Verzoek tot Aanbod / Intekening op specificatie</code>, de <code>Aanmelding</code> op aanbod en de <code>Inschrijving</code> als verbintenis. Uit de afstemming van 14 september komt dit beeld: aanbod rijpt in fasen, en aanmelden kan in elke fase.
</div>

<svg width="100%" viewBox="0 0 940 190" style="display:block;margin:0.6rem 0 0.2rem;"><rect x="10" y="34" width="190" height="78" rx="8" fill="#FFFFFF" stroke="#7A97F2" stroke-width="2"/><text x="105.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Specificatie</text><text x="105.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">het ontwerp,</text><text x="105.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">los van wanneer</text><text x="580" y="20" text-anchor="middle" fill="#6B7280" style="font-size:11px;letter-spacing:1px;font-family:inherit">ONDERWIJSAANBOD, STEEDS RIJPER</text><line x1="240" y1="26" x2="920" y2="26" stroke="#6B7280" stroke-width="1"/><rect x="240" y="34" width="210" height="78" rx="8" fill="#E6F7F0" stroke="#00AF81" stroke-width="2"/><text x="345.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Intentie</text><text x="345.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">we gaan dit aanbieden;</text><text x="345.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">gaat door bij voldoende vraag</text><rect x="475" y="34" width="210" height="78" rx="8" fill="#B3E8D3" stroke="#00AF81" stroke-width="2"/><text x="580.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Grofmazig gepland</text><text x="580.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">periode en start, gebouw,</text><text x="580.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">misschien al een docent</text><rect x="710" y="34" width="210" height="78" rx="8" fill="#00AF81" stroke="#00AF81" stroke-width="2"/><text x="815.0" y="58" text-anchor="middle" fill="#FFFFFF" style="font-size:14px;font-weight:700;font-family:inherit">Geroosterd</text><text x="815.0" y="78" text-anchor="middle" fill="#F0FFF8" style="font-size:11px;font-family:inherit">dag, tijd, lokaal, docent,</text><text x="815.0" y="93" text-anchor="middle" fill="#F0FFF8" style="font-size:11px;font-family:inherit">groep</text><line x1="202" y1="73" x2="236" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="236,68 242,73 236,78" fill="#6B7280"/><line x1="452" y1="73" x2="486" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="486,68 492,73 486,78" fill="#6B7280"/><line x1="687" y1="73" x2="721" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="721,68 727,73 721,78" fill="#6B7280"/><path d="M12 122 v8 H918 v-8" fill="none" stroke="#7A97F2" stroke-width="2"/><text x="465.0" y="146" text-anchor="middle" fill="#7A97F2" style="font-size:13px;font-weight:700;font-family:inherit">intekenen op de specificatie (regel dit); aanmelden op aanbod, in elke fase</text><path d="M242 156 v8 H918 v-8" fill="none" stroke="#E9A27F" stroke-width="2"/><text x="580.0" y="180" text-anchor="middle" fill="#E9A27F" style="font-size:13px;font-weight:700;font-family:inherit">inschrijven: op aanbod</text></svg>

<div style="display:flex;align-items:center;gap:0.5rem;margin-top:0.3rem;font-size:0.8rem;color:var(--np-dark-gray);">Geldt op elk niveau:&nbsp;<span style="display:inline-block;padding:0.15rem 0.6rem;border-radius:999px;background:#F1F3F5;color:var(--np-ink);font-size:0.78rem;margin-right:0.35rem;">opleiding</span><span style="display:inline-block;padding:0.15rem 0.6rem;border-radius:999px;background:#F1F3F5;color:var(--np-ink);font-size:0.78rem;margin-right:0.35rem;">opleidingsprogramma</span><span style="display:inline-block;padding:0.15rem 0.6rem;border-radius:999px;background:#F1F3F5;color:var(--np-ink);font-size:0.78rem;margin-right:0.35rem;">onderwijseenheid</span><span style="display:inline-block;padding:0.15rem 0.6rem;border-radius:999px;background:#F1F3F5;color:var(--np-ink);font-size:0.78rem;margin-right:0.35rem;">leeronderdeel</span><span style="display:inline-block;padding:0.15rem 0.6rem;border-radius:999px;background:#F1F3F5;color:var(--np-ink);font-size:0.78rem;margin-right:0.35rem;">les</span></div>

<div class="np-card" style="margin-top: 0.7rem; font-size: 0.95rem; line-height: 1.5; padding: 0.7rem 1rem;">
<strong>Klopt dit beeld?</strong> En hoort de fasering van het aanbod in het informatiemodel: als toestand op het aanbod, of als eigen objecttypen per fase?
</div>

</div>

<!--
Bron: afstemming met Niels en Ronald op 14 september (Jamie, minuut 9 tot 17). Niels: een
aanbod heeft fasen, van "we gaan een opleiding aanbieden" via start, periode, gebouw en
misschien een docent, tot concreet geroosterd (eerste uur maandag, lokaal, leerlingen en
docenten); daartussen nog een fase waarin we wel aanbieden maar nog niet weten hoe vaak en
hoeveel, met keuzedelen als voorbeeld (gaat alleen door bij voldoende vraag). Ronald: in de
praktijk aanbodgedreven op opleidingsniveau, inschrijven op aanbod (op de opleidingsgroep),
intekenen vraaggestuurd met aanmelden-tot en afmelden-tot. Niek: intekenen in eerste
instantie op de specificatie (ik zie nog geen aanbod, school, regel dit) en daarna op de lagen
van aanbod; de gelaagdheid van aanbod zit nog niet in het model en vraagt uitwerking, met de
vraag of dat in dit model hoort: hoe rijper het aanbod, hoe meer data en hoe dichter bij het
geplande moment. Niels' conclusie: intekenen op specificatie kan; aanmelden, intekenen en
inschrijven kunnen op aanbod. Verwerkt als ontwerpkeuze 13 op de plaat van 14 september (aanmelding, inschrijving, cohort en OER
erbij); de fasering van aanbod staat daar als open vraag en raakt Public #105 en de POC-sessies
bij de instellingen.
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

# Werk per onderwerp

<div style="margin-top:0.6rem;max-width:74%;"><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/Public/milestone/4" style="color:var(--np-ink);">Koppelvlakspecificatie releaseproces en kwaliteit</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:48%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:11;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">11</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/Public/pull/82">PR 82</a></span></div></div><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/Public/milestone/3" style="color:var(--np-ink);">Requirementsboom doorontwikkelen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:48%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:2;background:#00AF81;display:flex;align-items:center;justify-content:center;color:#fff;font-size:0.72rem;font-weight:600;">2</div><div style="flex:9;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">9</div></div></div></div><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/Public/milestone/5" style="color:var(--np-ink);">Koppelingspecificatiestructuur doorontwikkelen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:48%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:1;background:#00AF81;display:flex;align-items:center;justify-content:center;color:#fff;font-size:0.72rem;font-weight:600;">1</div><div style="flex:10;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">10</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/Public/pull/100">PR 100</a>, <a href="https://github.com/Npuls-OKx/Public/pull/104">PR 104</a></span></div></div><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><span style="color:var(--np-orange);font-weight:600;">&#9679;</span> <a href="https://github.com/Npuls-OKx/meta/milestone/7" style="color:var(--np-ink);">Begrippenkader en informatiemodel verdiepen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">meta</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:74%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:17;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">17</div></div><span style="display:inline-flex;align-items:center;gap:0.25rem;margin-left:0.5rem;font-size:0.72rem;color:var(--np-ink);white-space:nowrap;"><svg width="18" height="18" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="15" cy="13" r="4" fill="#fff"/><circle cx="15" cy="31" r="4" fill="#fff"/><circle cx="30" cy="31" r="4" fill="#fff"/><line x1="15" y1="17" x2="15" y2="27" stroke="#fff" stroke-width="3"/><path d="M30 27 v-6 a5 5 0 0 0 -5 -5 h-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><a href="https://github.com/Npuls-OKx/meta/pull/225">PR 225</a>, <a href="https://github.com/Npuls-OKx/meta/pull/233">PR 233</a></span></div></div><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/Public/milestone/1" style="color:var(--np-ink);">Leerroute-refactor met harness-waarborgen</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:26%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:3;background:#00AF81;display:flex;align-items:center;justify-content:center;color:#fff;font-size:0.72rem;font-weight:600;">3</div><div style="flex:3;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">3</div></div></div></div><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/Public/milestone/7" style="color:var(--np-ink);">Keuzedelen kiesbaarheid en groepsindeling</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:13%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:3;background:#E5E7EB;display:flex;align-items:center;justify-content:center;color:var(--np-ink);font-size:0.72rem;">3</div></div></div></div><div style="display:grid;grid-template-columns:19rem 1fr;align-items:center;gap:0.8rem;margin-top:0.42rem;font-size:0.82rem;"><div style="line-height:1.25;"><a href="https://github.com/Npuls-OKx/Public/milestone/6" style="color:var(--np-ink);">Informatiestromen hoofdplaat</a> <span style="color:var(--np-mid-gray);font-size:0.7rem;">Public</span></div><div style="display:flex;align-items:center;"><div style="display:flex;width:18%;height:20px;border-radius:4px;overflow:hidden;gap:2px;"><div style="flex:4;background:#00AF81;display:flex;align-items:center;justify-content:center;color:#fff;font-size:0.72rem;font-weight:600;">4</div></div></div></div></div>

<div style="font-size: 0.8rem; color: var(--np-dark-gray); margin-top: 0.7rem;">
Stand van 14 september. Onderwerpen zijn de milestones; de balklengte is het aantal issues, groen gesloten, grijs open; het icoon markeert werk dat als pull request ter review ligt. Oranje: staat vandaag op de agenda. Niet getoond: Agent-harness (Public, 2 open) en de interne milestones van meta.
</div>

</div>

<!--
Een balk per milestone, groen wat gesloten is, grijs wat open staat, met het pull request-icoon
waar het werk in een branch ter review ligt. Oranje stip: staat vandaag op de agenda. Het beeld:
het grote werk van deze periode zit in de pull requests en niet in gesloten issues; de hoofdplaat
is af (vier correcties gesloten sinds 1 september). Van buiten het kernteam kwamen sinds
1 september zeven issues: vijf van Kees (#85 tot en met #89) en twee van Xedule (#84, #99).
Nieuw sinds 11 september: het informatiemodel ligt als Public PR 104 gestapeld op PR 100, met
de 26 modelvragen uit de leverancierstegenlezing in meta #234 (milestone Begrippenkader, 17 open).
Bron: de milestones en issues van beide repositories, GitHub, 14 september.
-->

---

<!-- 18b. VERZET WERK -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat er sinds 1 september is verzet

<div style="display:grid;grid-template-columns:8.5rem repeat(5,1fr);gap:0.6rem 0.7rem;align-items:center;margin-top:0.8rem;max-width:90%;"><div></div><div style="display:flex;align-items:center;gap:0.4rem;font-size:0.76rem;color:var(--np-mid-gray);justify-content:center;"><svg width="22" height="22" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="14" cy="12" r="4" fill="#fff"/><circle cx="14" cy="32" r="4" fill="#fff"/><circle cx="31" cy="22" r="4" fill="#fff"/><path d="M14 16 v12 M14 22 h13" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>PR gemerged</div><div style="display:flex;align-items:center;gap:0.4rem;font-size:0.76rem;color:var(--np-mid-gray);justify-content:center;"><svg width="22" height="22" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><line x1="22" y1="12" x2="22" y2="32" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><line x1="12" y1="22" x2="32" y2="22" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/></svg>PR geopend</div><div style="display:flex;align-items:center;gap:0.4rem;font-size:0.76rem;color:var(--np-mid-gray);justify-content:center;"><svg width="22" height="22" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>issues gesloten</div><div style="display:flex;align-items:center;gap:0.4rem;font-size:0.76rem;color:var(--np-mid-gray);justify-content:center;"><svg width="22" height="22" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><line x1="22" y1="12" x2="22" y2="32" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><line x1="12" y1="22" x2="32" y2="22" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/></svg>issues geopend</div><div style="display:flex;align-items:center;gap:0.4rem;font-size:0.76rem;color:var(--np-mid-gray);justify-content:center;"><svg width="22" height="22" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><line x1="8" y1="22" x2="36" y2="22" stroke="#fff" stroke-width="3"/><circle cx="22" cy="22" r="6" fill="#fff"/></svg>commits op dev</div><div style="font-size:0.84rem;font-weight:600;color:var(--np-ink);">Public</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">2</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">1</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">5</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">8</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">1</div><div style="font-size:0.84rem;font-weight:600;color:var(--np-ink);">meta</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">4</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">6</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">11</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">21</div><div style="background:#fff;border:1px solid var(--np-light-gray);border-radius:8px;padding:0.55rem 0;text-align:center;font-size:1.9rem;font-weight:600;color:var(--np-ink);line-height:1.1;">47</div></div>

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem; font-size: 0.86rem; line-height: 1.55; max-width: 90%;">
<div>

**Public:** overzichtsplaat en branching-diagram; redactie op kaderscenario leerroute 1; applicatiediensten en versionering op een branch, 63 bestanden ([PR 100](https://github.com/Npuls-OKx/Public/pull/100))

</div>
<div>

**meta:** deck van 1 september met PowerPoint-export; Nederlands als voertaal; lezerspersona's; informatiemodel en begrippenlijst, 28 commits ([PR 225](https://github.com/Npuls-OKx/meta/pull/225)), gepubliceerd naar Public ([PR 104](https://github.com/Npuls-OKx/Public/pull/104))

</div>
</div>

</div>

<!--
Stand van 11 september, beide repositories, alles na 1 september. De aantallen zeggen iets
over de hoeveelheid werk, niet over de kwaliteit ervan; dat oordeel ligt bij de review. Het
grote werk van deze periode staat op branches en niet op dev: PR 100 en PR 104 in Public en
PR 225 in meta. De 21 nieuwe issues op meta zijn grotendeels intern harness- en reviewwerk.
-->

---

<!-- 19. VOORSTEL PRIORITERING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorstel voor de prioritering

<div class="np-grid-2" style="margin-top: 1rem; gap: 1.6rem; align-items: start;">
<div class="np-card accent-green" style="background: #F3FAF6;">
<strong>Nu</strong>
<div style="display:flex;align-items:center;gap:0.7rem;margin-top:0.55rem;font-size:0.95rem;line-height:1.35;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7CCBA8"/><polygon points="17,12 34,22 17,32" fill="#fff"/></svg><div>Review op de pull requests: versionering (<a href="https://github.com/Npuls-OKx/Public/pull/100">Public PR 100</a>), v0.0.2 (<a href="https://github.com/Npuls-OKx/Public/pull/82">Public PR 82</a>), het informatiemodel</div></div><div style="display:flex;align-items:center;gap:0.7rem;margin-top:0.55rem;font-size:0.95rem;line-height:1.35;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7CCBA8"/><polygon points="17,12 34,22 17,32" fill="#fff"/></svg><div>Student keuze regelsets toetsen aan de scenario's (<a href="https://github.com/Npuls-OKx/Public/issues/74">Public #74</a>, <a href="https://github.com/Npuls-OKx/Public/issues/64">#64</a>, <a href="https://github.com/Npuls-OKx/Public/issues/1">#1</a>)</div></div>
</div>
<div class="np-card" style="border-top-color: #B8BEC7; background: #F6F7F9;">
<strong>Wacht</strong>
<div style="display:flex;align-items:center;gap:0.7rem;margin-top:0.55rem;font-size:0.95rem;line-height:1.35;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#B8BEC7"/><rect x="15" y="12" width="5" height="20" rx="1" fill="#fff"/><rect x="24" y="12" width="5" height="20" rx="1" fill="#fff"/></svg><div>Meerdere instanties van een referentiecomponent (<a href="https://github.com/Npuls-OKx/meta/issues/80">meta #80</a>)</div></div><div style="display:flex;align-items:center;gap:0.7rem;margin-top:0.55rem;font-size:0.95rem;line-height:1.35;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#B8BEC7"/><rect x="15" y="12" width="5" height="20" rx="1" fill="#fff"/><rect x="24" y="12" width="5" height="20" rx="1" fill="#fff"/></svg><div>Terminologie- en correctie-issues</div></div><div style="display:flex;align-items:center;gap:0.7rem;margin-top:0.55rem;font-size:0.95rem;line-height:1.35;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#B8BEC7"/><rect x="15" y="12" width="5" height="20" rx="1" fill="#fff"/><rect x="24" y="12" width="5" height="20" rx="1" fill="#fff"/></svg><div>Verdieping van de requirementsboom</div></div>
</div>
</div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 1rem;">
Status: voorstel van het kernteam. Zonder keuze blijft alles even zwaar en beweegt niets.
</div>

</div>

<!--
Voorstel, geen besluit. Links wat het kernteam eerst wil doen: zonder review geen release en
zonder release geen bouw; en de student keuze regelsets, omdat elke studentkeuze doorwerkt in
planning, rooster en leeromgeving. Rechts wat daarmee wacht. Vraag aan de groep: klopt deze
volgorde, en wat ontbreekt? De naam student keuze regelset volgt het informatiemodel.
-->

---

<!-- 20. GEVRAAGD -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Gevraagd

<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><path d="M11 13 h22 a3 3 0 0 1 3 3 v11 a3 3 0 0 1 -3 3 h-12 l-6 5 v-5 h-4 a3 3 0 0 1 -3 -3 v-11 a3 3 0 0 1 3 -3 z" fill="#fff"/></svg><dl class="np-besluit kennisname" style="flex:1;"><dt>Input</dt><dd>het versioneringsvraagstuk: welke variant sluit het best aan bij de ervaring in het veld, A, B of een andere</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><circle cx="19" cy="19" r="8" fill="none" stroke="#fff" stroke-width="3"/><line x1="25" y1="25" x2="33" y2="33" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg><dl class="np-besluit review" style="flex:1;"><dt>Review</dt><dd>het informatiemodel op conceptueel niveau: klopt de samenhang, welke objecttypen missen, welke begrippen missen. Tot de volgende sessie, in <a href="https://github.com/Npuls-OKx/meta/pull/225">meta PR 225</a></dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><dl class="np-besluit " style="flex:1;"><dt>Besluit</dt><dd>de prioritering van het open werk: eerst de reviews, dan de student keuze regelsets</dd></dl></div>
<div style="display:flex;align-items:center;gap:0.9rem;margin-top:0.7rem;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><path d="M11 13 h22 a3 3 0 0 1 3 3 v11 a3 3 0 0 1 -3 3 h-12 l-6 5 v-5 h-4 a3 3 0 0 1 -3 -3 v-11 a3 3 0 0 1 3 -3 z" fill="#fff"/></svg><dl class="np-besluit kennisname" style="flex:1;"><dt>Input</dt><dd>de bevindingen op v0.0.2, en wat er nodig is om de review te laten gebeuren</dd></dl></div>

</div>

<!--
Geen besluit over het informatiemodel zelf: dat is pas aan de orde als de ADR-punten zijn
opgelost (meta #227 en #228). Wel een besluit over de prioritering, want zonder keuze beweegt
niets. Bij de versionering zijn A en B de voorgegeven opties; een variant uit de praktijk van
een leverancier is net zo welkom.
-->

---

<!-- 21. VERVOLG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Vervolg

<div class="np-card accent-orange" style="margin-top: 0.8rem; padding: 0.8rem 1.2rem;"><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><rect x="11" y="14" width="22" height="19" rx="2" fill="#fff"/><rect x="11" y="14" width="22" height="5" fill="#E9A27F" opacity="0.35"/><rect x="15" y="10" width="3" height="6" rx="1" fill="#fff"/><rect x="26" y="10" width="3" height="6" rx="1" fill="#fff"/><rect x="15" y="22" width="4" height="4" fill="#E9A27F"/><rect x="21" y="22" width="4" height="4" fill="#E9A27F"/><rect x="27" y="22" width="4" height="4" fill="#E9A27F"/></svg><div><strong>Volgende sessie: woensdag 30 september 2026</strong></div></div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.5rem;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><path d="M22 10 a8 8 0 0 1 8 8 c0 6 -8 15 -8 15 s-8 -9 -8 -15 a8 8 0 0 1 8 -8 z" fill="#fff"/><circle cx="22" cy="18" r="3" fill="#E9A27F"/></svg><div>Amersfoort, op locatie</div></div></div>

<div style="margin-top: 0.6rem;"><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><line x1="12" y1="22" x2="30" y2="22" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><polyline points="24,15 31,22 24,29" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>De gekozen versioneringsvariant, uitgewerkt in <a href="https://github.com/Npuls-OKx/Public/pull/100">Public PR 100</a></div></div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><line x1="12" y1="22" x2="30" y2="22" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><polyline points="24,15 31,22 24,29" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Het informatiemodel na de interne besluiten als pull request naar Public</div></div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.98rem;line-height:1.4;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><line x1="12" y1="22" x2="30" y2="22" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><polyline points="24,15 31,22 24,29" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>De student keuze regelsets, getoetst aan de scenario's</div></div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0.7rem;font-size:0.92rem;line-height:1.4;"><svg width="40" height="40" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#B8BEC7"/><rect x="11" y="14" width="22" height="19" rx="2" fill="#fff"/><rect x="11" y="14" width="22" height="5" fill="#B8BEC7" opacity="0.35"/><rect x="15" y="10" width="3" height="6" rx="1" fill="#fff"/><rect x="26" y="10" width="3" height="6" rx="1" fill="#fff"/><rect x="15" y="22" width="4" height="4" fill="#B8BEC7"/><rect x="21" y="22" width="4" height="4" fill="#B8BEC7"/><rect x="27" y="22" width="4" height="4" fill="#B8BEC7"/></svg><div>Maandag 6 oktober: leeruitkomstendag, waar het informatiemodel wordt getoond</div></div></div>

<div style="font-size: 0.85rem; color: var(--np-dark-gray); margin-top: 0.8rem;">
Commentaar op een lopende release: in de pull request. Nieuw punt: als issue op <strong>github.com/Npuls-OKx/Public</strong>
</div>

</div>

<!--
De volgende sessie is op locatie in Amersfoort, woensdag 30 september; expliciet noemen, want de
vaste tweewekelijkse dinsdag verschuift. De drie pijlen volgen uit Gevraagd. De datum van
6 oktober komt uit de afstemming van 11 september. Geen andere data beloven.
-->

---

<!-- PEILING -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Hoe gaat het?

<div class="np-grid-2" style="margin-top: 1.2rem; gap: 1.8rem; align-items: center;">
<div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:0;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7A97F2"/><path d="M12 27 a10 10 0 0 1 20 0" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><line x1="22" y1="27" x2="27" y2="19" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="22" cy="27" r="2.5" fill="#fff"/></svg><div>Welk cijfer krijgt de voortgang, en waarom?</div></div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:1rem;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#7CCBA8"/><polyline points="12,23 19,30 32,15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Wat ging er goed?</div></div><div style="display:flex;align-items:center;gap:0.8rem;margin-top:1rem;font-size:1.05rem;line-height:1.4;"><svg width="44" height="44" viewBox="0 0 44 44" style="flex:none;"><circle cx="22" cy="22" r="21" fill="#E9A27F"/><line x1="22" y1="32" x2="22" y2="13" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><polyline points="14,21 22,13 30,21" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div>Wat kan er beter?</div></div></div>
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
