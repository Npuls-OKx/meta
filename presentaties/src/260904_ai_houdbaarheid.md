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

<!-- 2. CONCLUSIE -->
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

<!-- 3. DE VRAAG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# De vraag

<div class="np-card" style="border-top-color: #0B4F6C; font-size: 1.05rem; line-height: 1.6; margin-top: 0.5rem; max-width: 90%;">
Bouwen we met OKx niet een stoomtrein, terwijl de AI-ontwikkeling straks om vliegtuigen vraagt?
</div>

<div style="font-size: 0.9rem; line-height: 1.5; margin-top: 0.8rem; max-width: 94%;">

| De vraag kan drie dingen betekenen | Antwoord staat op |
|---|---|
| De gekozen techniek is achterhaald | Slide 4: de techniek is de vervangbare laag |
| Het duurt te lang voordat er een gedragen afspraak ligt | Slide 5: dit is een risico, nog niet gemeten |
| AI lost de koppelpunten tussen systemen zelf op | Slide 4: de vraag wie waarvan bron is, is bestuurlijk en verdwijnt niet |

</div>

<div style="font-size: 0.9rem; color: var(--np-dark-gray); margin-top: 0.8rem; max-width: 90%;">
Alle drie worden beantwoord. De derde is de zwaarste en krijgt daarom de eerste helft van slide 4.
</div>

</div>

<!--
De vraag laten staan zoals hij gesteld is, en dan zeggen waar elk antwoord
staat. Niet wegen welke lezing zwaar is: dat leest als een beoordeling van de
vrager.
-->

---

<!-- 4. WAT STANDHOUDT -->
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

<!-- 5. DE VIER GATEN -->
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

<!-- 6. WAT DE SECTOR MERKT -->
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

<!-- 7. WAT WE DOEN -->
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

<!-- 8. BESLUIT 1 -->
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

<!-- 9. BESLUIT 2 -->
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

<!-- 10. AFSLUITER -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide17.PNG);"></div>

<!--
Einde. Npuls-afsluiter met logo en licentie.
-->
