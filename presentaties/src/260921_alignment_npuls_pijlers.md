---
theme: default
title: "OKx in samenhang met AII, eduXchange en het ontsluiten van onderwijsaanbod"
info: "Overleg LZD 21 september 2026: de status van OKx, waar OKx andere ontwikkelingen raakt en hoe wij elkaar op de hoogte houden."
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
  <h1 style="font-size: 2.8rem; line-height: 1.15; margin-bottom: 0.8rem; color: var(--np-ink);">OKx in samenhang</h1>
  <div style="font-size: 1.1rem; line-height: 1.5; color: var(--np-ink); margin-bottom: 0.8rem; max-width: 38rem;">AII spoor 3 &middot; eduXchange &middot; ontsluiten onderwijsaanbod &middot; OKx: wat is de status, waar raken wij elkaar, hoe houden wij elkaar op de hoogte</div>
  <div style="font-size: 0.95rem; color: var(--np-mid-gray);">Leren zonder Drempels &middot; 21 september 2026</div>
</div>

<!--
Hans opent. Doel van de sessie is alignment, geen inhoudelijke afronding: waar werkt iedereen
aan, waar raken wij elkaar, welke vervolgafspraken. OKx loopt op onderdelen vooruit en heeft
onvoldoende zicht op wat buiten de instelling gebeurt; dat mag hardop.
-->

---

<!-- 2. AGENDA: DE DRIE VRAGEN VAN HANS -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide2.PNG);"></div>

<div style="margin-left: 42%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding-right: 3rem;">
  <p class="eyebrow">Agenda</p>
  <h1 style="font-size: 2rem !important; margin-bottom: 1.1rem;">Drie vragen</h1>
  <div style="display: flex; flex-direction: column; gap: 0.95rem;">
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num">1</span>
      <div><strong>Wat is (de status van) OKx?</strong><br/><span class="muted" style="font-size: 0.82rem;">focus binnen de instelling, aanpak, waar de specificaties en het informatiemodel staan</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-orange);">2</span>
      <div><strong>Waar raakt OKx andere ontwikkelingen wel, en welke niet?</strong><br/><span class="muted" style="font-size: 0.82rem;">twee uitgangspunten als schot voor de boeg; AII, eduXchange, catalogus, EduID</span></div>
    </div>
    <div style="display: flex; align-items: center; gap: 0.8rem;">
      <span class="np-num" style="background: var(--np-green);">3</span>
      <div><strong>Hoe houden wij elkaar op de hoogte?</strong><br/><span class="muted" style="font-size: 0.82rem;">gaten en onnodige overlap voorkomen; vervolgafspraken</span></div>
    </div>
  </div>
  <div class="np-card" style="margin-top: 1.1rem; font-size: 0.85rem; padding: 0.5rem 0.9rem;">
    Doel vandaag: aftasten waar ieder staat en waar het schuurt, en daar afspraken van maken. Niet alles vandaag oplossen.
  </div>
</div>

<!--
De agenda van Hans, letterlijk. Uit de voorbereiding van vanochtend: orienterend, op
hoofdlijnen zenden, wrijvingspunten benoemen en vervolgafspraken maken. Ashwin vraagt voor
vraag 2 een concreet schot voor de boeg: dat zijn de twee uitgangspunten van Hans en de
raakvlakkenslide.
-->

---

<!-- 3. STATUS OKX: BINNEN DE DEUR (hoofdplaat 1.7) -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Wat is OKx: standaardkoppelingen binnen de deur van de instelling

<div style="display:grid;grid-template-columns:2.1fr 1fr;gap:1.2rem;align-items:start;margin-top:0.2rem;">
<div>
  <img src="/platen/hoofdplaat-1.7.jpg" style="width:100%;max-height:25rem;object-fit:contain;" />
  <div style="font-size:0.75rem;color:var(--np-mid-gray);margin-top:0.2rem;">Hoofdplaat informatiestromen v1.7, richtinggevend (draagt nog de aanduiding concept).</div>
</div>
<div style="font-size:0.82rem;line-height:1.42;">

- **Binnen**: catalogus, planning en rooster, studentkeuze, kernregistratie en studentvolgsysteem, LMS, examinering; de pijlen zijn de koppelingen die OKx specificeert
- **Status**: koppelvlakspecificatie v0.0.2 in review bij de kerngroep techniek; informatiemodel v0.1; voorbeelduitwerking leerroute 1 op 30 september; daarna bouwen via de scholen, door leveranciers, en testen
- **Buiten de deur** (AII, eduXchange, EduID, RIO) hebben wij te weinig beeld van wat andere ontwikkelingen doen

<div class="np-card accent-orange" style="margin-top:0.5rem;font-size:0.8rem;padding:0.5rem 0.8rem;">
Daar zoeken wij vandaag de aansluiting.
</div>

</div>
</div>

</div>

<!--
Uit de voorbereiding (Niels): met de hoofdplaat laten zien dat wij vooral kijken naar wat er
binnen de deur gebeurt en te weinig beeld hebben van de gremia daarbuiten. Niet de plaat
uitleggen; alleen de grens aanwijzen. Status uit de mail van Hans: de specificatiedocumenten
komen op korte termijn, de koppelingen worden via de scholen door leveranciers gebouwd en
getest.
-->

---

<!-- 4. AANPAK: STUDENTREIS EN INSTELLINGSREIS, POC MET KOPLOPERSCHOLEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Aanpak: van reis naar specificatie

<div style="display:grid;grid-template-columns:2fr 1fr;gap:1.2rem;align-items:start;margin-top:0.2rem;">
<div>
  <img src="/platen/concept-uitleg-business-architectuur.png" style="width:100%;max-height:26rem;object-fit:contain;" />
  <div style="font-size:0.75rem;color:var(--np-mid-gray);margin-top:0.2rem;">Schets van Niels, concept: van de PoC-school via het gedeelde perspectief naar de OKx-architectuur.</div>
</div>
<div style="font-size:0.82rem;line-height:1.42;">

- **Negen leerroutes**; per leerroute bepalen studentreis en instellingsreis samen wat er wanneer tussen systemen beweegt; leerroutes 1 tot 3 eerst
- **PoC-aanpak**: user stories van koploperscholen, vertaald naar generieke stories en modulaire bouwstenen
- **Specificatiedocumenten**: techniekagnostisch, modulair uit bouwblokken, openbaar en herleidbaar in GitHub

<div class="np-card" style="margin-top:0.5rem;font-size:0.8rem;padding:0.5rem 0.8rem;">
OKx specificeert het koppelvlak, niet de applicatie.
</div>

</div>
</div>

</div>

<!--
Twee zinnen over de specificatiedocumenten volstaan (voorbereiding). De leerroutes en
kaderscenario's staan in Npuls-OKx/Public; leerroute 1 is uitgewerkt met persona Jochem,
Apothekersassistent BOL, cohort 2026, in acht fasen van kwalificatiedossier tot diploma.
Bij vragen over de informatiestromen per leerroute: de plaat OKx_LR1_informatiestromen.
-->

---

<!-- 5. TWEE UITGANGSPUNTEN ALS SCHOT VOOR DE BOEG -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Twee uitgangspunten die verder reiken dan OKx

<div class="np-grid-2" style="margin-top: 0.6rem; gap: 1.3rem; align-items: start;">
<div class="np-card accent-blue" style="padding:0.8rem 1rem;">
<strong style="font-size:1rem;">1. Kiezen door lerenden: niet dieper dan de leeractiviteit</strong>
<div style="font-size:0.86rem;line-height:1.5;margin-top:0.5rem;">
Drie niveaus in de koppelingen, gekozen op organiseerbaarheid en betaalbaarheid:
</div>
<div style="display:flex;flex-direction:column;gap:0.35rem;margin-top:0.5rem;font-size:0.84rem;">
  <div><span class="np-num" style="width:1.4rem;height:1.4rem;font-size:0.75rem;">1</span>&nbsp; <strong>opleiding</strong> &middot; in OKx: opleiding en opleidingsprogramma</div>
  <div><span class="np-num" style="width:1.4rem;height:1.4rem;font-size:0.75rem;background:var(--np-orange);">2</span>&nbsp; <strong>opleidingsonderdeel</strong> &middot; in OKx: onderwijseenheid</div>
  <div><span class="np-num" style="width:1.4rem;height:1.4rem;font-size:0.75rem;background:var(--np-green);">3</span>&nbsp; <strong>leeractiviteit</strong> &middot; in OKx: leeronderdeel en leergelegenheid</div>
</div>
<div style="font-size:0.84rem;line-height:1.5;margin-top:0.6rem;color:var(--np-dark-gray);">
Daaronder (de les) wisselt OKx niet uit; wie dat wil, lost het functioneel of in de klas op, niet via de standaardkoppeling.
</div>
</div>
<div class="np-card accent-green" style="padding:0.8rem 1rem;">
<strong style="font-size:1rem;">2. Leeruitkomsten als ordenend principe</strong>
<div style="font-size:0.86rem;line-height:1.5;margin-top:0.5rem;">
OKx sluit volledig aan op de leeruitkomst (LUK) zoals besproken op de LUK-dag van 3 juni bij de MBO Raad, wetend dat de definities nog bewegen.
</div>
<div style="font-size:0.84rem;line-height:1.5;margin-top:0.6rem;color:var(--np-dark-gray);">
In het informatiemodel is de leeruitkomst de sleutel: specificaties, toets- en examenonderdelen en de resultaatstructuur verwijzen ernaar. De instelling vult haar in vanuit haar eigen onderwijskundig kader; het kwalificatiedossier zegt wat, de leeruitkomst zegt waar en hoe de student het laat zien.
</div>
</div>
</div>

<div class="np-card accent-orange" style="margin-top: 0.8rem; font-size: 0.9rem; line-height: 1.5; padding: 0.55rem 1rem;">
<strong>De vraag aan de tafel:</strong> maken andere ontwikkelingen binnen LZD dezelfde keuzes, of andere? Dan weten wij dat liever nu dan bij de oplevering van de keten.
</div>

</div>

<!--
De twee voorbeelden uit de mail van Hans, letterlijk als uitgangspunt. De vertaling naar
OKx-objecttypen komt uit het informatiemodel v0.1: opleiding en opleidingsprogramma,
onderwijseenheid, leeronderdeel (specificatie) en leergelegenheid (aanbod); de les staat op de
plaat buiten de uitwisseling. Dit is het schot voor de boeg dat Ashwin vraagt.
-->

---

<!-- 6. INFORMATIEMODEL: ZEVEN BEGRIPPEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Informatiemodel: zeven begrippen delen de keten in

<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:1.2rem;align-items:start;margin-top:0.3rem;">
<div style="font-size: 0.82rem; line-height: 1.5;">

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
<div>
  <img src="/platen/informatiemodel-v0.1.jpg" style="width:100%;max-height:22rem;object-fit:contain;" />
  <div style="font-size:0.75rem;color:var(--np-mid-gray);margin-top:0.2rem;">Informatiemodel OKx v0.1, conceptueel (MIM 1 en 2), gemapt op OEAPI v6.</div>
</div>
</div>

</div>

<!--
Overgenomen uit het deck van 15 september. Het model is de aanzet tot het conceptueel
informatiemodel; de begrippen staan in het begrippenkader en de begrippenlijst. Op OEAPI-gebied
is de alignment redelijk te pakken; EduExchange moesten wij uitleggen hoe een keuzedeel in het
model hoort.
-->

---

<!-- 7. VOORBEELDUITWERKING JOCHEM EN DE LEERUITKOMST ALS SLEUTEL -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Voorbeelduitwerking: Jochem stap voor stap in het model

<div style="display:grid;grid-template-columns:1.35fr 1fr;gap:1.2rem;align-items:start;margin-top:0.2rem;">
<div>
  <img src="/platen/voorbeeld-jochem-leeruitkomst.png" style="width:100%;max-height:24rem;object-fit:contain;" />
  <div style="font-size:0.75rem;color:var(--np-mid-gray);margin-top:0.2rem;">Drie beelden uit fase 1: de leeruitkomst uit het dossier, in CompetentNL-skills, en de toetsonderdelen die ernaar verwijzen.</div>
</div>
<div style="font-size:0.82rem;line-height:1.42;">

- **Per processtap** van de instellingsreis: wat ontstaat in het informatiemodel en wat stroomt tussen systemen, met Jochems waarde erin
- **De leeruitkomst is de sleutel**: specificaties, toets- en examenonderdelen en de resultaatstructuur verwijzen ernaar; de instelling vult haar in (waar en hoe de student het laat zien)
- **CompetentNL** als verdieping van dezelfde leeruitkomst: vaardigheden en kennisgebieden
- Gecontroleerd tegen de plaat; wat de plaat niet kent wordt een vraag

<div class="np-card accent-green" style="margin-top:0.5rem;font-size:0.8rem;padding:0.5rem 0.8rem;">
Kerngroep techniek, 30 september: het voorbeeld naast het eigen model leggen.
</div>

</div>
</div>

</div>

<!--
Voorbeelduitwerking leerroute 1 in Npuls-OKx/meta (branch 106): 174 regels over acht fasen,
gegenereerd uit een regeltabel die tegen het informatiemodel en de hoofdplaat wordt
gecontroleerd. De leeruitkomst als sleutel is de kandidaat voor standaardisatie over de keten
heen; dat is vraag drie op de laatste slide.
-->

---

<!-- 8. WAAR RAAKT OKX ANDERE ONTWIKKELINGEN WEL EN NIET -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar OKx andere ontwikkelingen raakt, en waar niet

<div style="font-size: 0.84rem; line-height: 1.45; margin-top: 0.4rem;">

| Ontwikkeling | Raakvlak met OKx | Wat wij zien |
|---|---|---|
| **AII spoor 3** | aanmelden, intekenen, inschrijven; het ontsluiten van aanmeldbaar aanbod; de aanmelding met verbintenis terug naar de kernregistratie | wij spreken over intekenen op een specificatie, AII hanteert aanmelden, intekenen, inschrijven: begrippen naast elkaar leggen |
| **eduXchange** | keuzedeel, aanbod en verbintenis over instellingen heen; de catalogus | OKx begint binnen de instelling, federatie is een latere stap; het informatiemodel als gedeelde taal voor keuzedeel en resultaat |
| **Ontsluiten onderwijsaanbod, functioneel gebied Onderwijs Catalogus** | dezelfde definities en gegevenssets: specificatie, aanbod in fasen van rijpheid, OEAPI v6 | een begrippenlijst en een informatiemodel delen in plaats van ieder een eigen dialect |
| **EduID, identity provisioning** | de student als persoon en deelnemer van aanmelding tot LMS en toegang | welke voorziening is leidend, en wat gaat er over de OKx-koppelingen |
| **RIO** | verantwoording van studievoortgang vanuit de kernregistratie | de resultaatstructuur ook in de kernregistratie |

</div>

<div class="np-grid-2" style="margin-top: 0.6rem; align-items: start; gap: 1.2rem;">
  <div class="np-card accent-green" style="padding:0.5rem 0.9rem;font-size:0.84rem;line-height:1.45;">
    <strong>Wel OKx:</strong> de koppelingen tussen de componenten binnen de instelling, hun informatiemodel en hun eisen; kiezen tot en met de leeractiviteit; leeruitkomsten als sleutel.
  </div>
  <div class="np-card accent-orange" style="padding:0.5rem 0.9rem;font-size:0.84rem;line-height:1.45;">
    <strong>Niet OKx:</strong> de functionaliteit binnen een applicatie, uitwisseling onder de leeractiviteit, roosteralgoritmes, didactiek, en de landelijke voorzieningen zelf.
  </div>
</div>

</div>

<!--
Het antwoord op vraag 2 van Hans, zo concreet als wij het nu kunnen maken. Het functionele
gebied Onderwijs Catalogus is het grootste raakvlak: daar werken meerdere ontwikkelingen met
dezelfde begrippen. Federatie gefaseerd: ADR 0008, intra-instelling eerst. RIO en EduID zijn
raakvlakken waar wij vooral vragen hebben.
-->

---

<!-- 9. WAAR WIJ ELKAAR RAKEN: AII EN OKX -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Waar wij elkaar raken: aanmelden, intekenen, inschrijven

<div style="font-size: 0.9rem; line-height: 1.5; margin-top: 0.2rem;">
OKx onderscheidt de <code>Intekening op specificatie</code>, de <code>Aanmelding</code> en de <code>Inschrijving</code>, en laat aanbod rijpen in fasen. AII hanteert de volgorde aanmelden, intekenen, inschrijven. Wat verstaan wij elk onder intekenen?
</div>

<svg width="100%" viewBox="0 0 940 250" style="display:block;margin:0.5rem 0 0.1rem;"><rect x="10" y="34" width="190" height="78" rx="8" fill="#FFFFFF" stroke="#7A97F2" stroke-width="2"/><text x="105.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Specificatie</text><text x="105.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">het ontwerp,</text><text x="105.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">los van wanneer</text><text x="580" y="20" text-anchor="middle" fill="#6B7280" style="font-size:11px;letter-spacing:1px;font-family:inherit">ONDERWIJSAANBOD, STEEDS RIJPER</text><line x1="240" y1="26" x2="920" y2="26" stroke="#6B7280" stroke-width="1"/><rect x="240" y="34" width="210" height="78" rx="8" fill="#E6F7F0" stroke="#00AF81" stroke-width="2"/><text x="345.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Intentie</text><text x="345.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">we gaan dit aanbieden;</text><text x="345.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">gaat door bij voldoende vraag</text><rect x="475" y="34" width="210" height="78" rx="8" fill="#B3E8D3" stroke="#00AF81" stroke-width="2"/><text x="580.0" y="58" text-anchor="middle" fill="#1B1B2F" style="font-size:14px;font-weight:700;font-family:inherit">Grofmazig gepland</text><text x="580.0" y="78" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">periode en start, gebouw,</text><text x="580.0" y="93" text-anchor="middle" fill="#4A4F57" style="font-size:11px;font-family:inherit">misschien al een docent</text><rect x="710" y="34" width="210" height="78" rx="8" fill="#00AF81" stroke="#00AF81" stroke-width="2"/><text x="815.0" y="58" text-anchor="middle" fill="#FFFFFF" style="font-size:14px;font-weight:700;font-family:inherit">Geroosterd</text><text x="815.0" y="78" text-anchor="middle" fill="#F0FFF8" style="font-size:11px;font-family:inherit">dag, tijd, lokaal, docent,</text><text x="815.0" y="93" text-anchor="middle" fill="#F0FFF8" style="font-size:11px;font-family:inherit">groep</text><line x1="202" y1="73" x2="236" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="236,68 242,73 236,78" fill="#6B7280"/><line x1="452" y1="73" x2="486" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="486,68 492,73 486,78" fill="#6B7280"/><line x1="687" y1="73" x2="721" y2="73" stroke="#6B7280" stroke-width="2"/><polygon points="721,68 727,73 721,78" fill="#6B7280"/><rect x="10" y="130" width="190" height="26" rx="13" fill="#7A97F2"/><text x="24" y="147" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">intekenen: op de specificatie</text><rect x="240" y="172" width="680" height="26" rx="13" fill="#3DB88F"/><text x="254" y="189" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">aanmelden: op aanbod, in elke fase van rijpheid</text><rect x="710" y="214" width="210" height="26" rx="13" fill="#E9A27F"/><text x="724" y="231" fill="#fff" style="font-size:12px;font-weight:700;font-family:inherit">inschrijven: op geroosterd</text><circle cx="904" cy="227" r="11" fill="#fff"/><text x="904" y="232" text-anchor="middle" fill="#E9A27F" style="font-size:15px;font-weight:700;font-family:inherit">?</text><path d="M200 143 C 225 143, 225 185, 238 185" fill="none" stroke="#6B7280" stroke-width="2"/><polygon points="236,180 244,185 236,190" fill="#6B7280"/><text x="222" y="167" text-anchor="middle" fill="#6B7280" style="font-size:10px;font-family:inherit">bevestiging</text><line x1="815" y1="198" x2="815" y2="212" stroke="#6B7280" stroke-width="2"/><polygon points="810,210 815,216 820,210" fill="#6B7280"/></svg>

<div class="np-card accent-orange" style="margin-top: 0.6rem; font-size: 0.92rem; line-height: 1.5; padding: 0.6rem 1rem;">
<strong>Vraag aan AII:</strong> intekenen op een specificatie (nog geen aanbod) is wat koploperscholen ons vragen; leveranciers herkennen het nog niet. Zien wij hetzelfde, of noemen wij twee dingen hetzelfde?
</div>

</div>

<!--
Overgenomen uit het deck van 15 september (positionering intekenen, aanmelden, inschrijven).
Uit de voorbereiding: wij hebben met scholen gesproken over intekenen op specificatie; AII lijkt
de begrippen anders te interpreteren. Niet oplossen vandaag: vaststellen dat het een raakvlak
is en een afspraak maken. Verbonden vraag: wie ontsluit het aanmeldbare aanbod aan AII, de
catalogus of de kernregistratie, en hoe komt de aanmelding met verbintenissen terug.
-->

---

<!-- 10. HOE HOUDEN WIJ ELKAAR OP DE HOOGTE, EN DE VERVOLGAFSPRAKEN -->
<div class="np-bg" style="background-image: url(/npuls/powerpoint_slides/Slide3.PNG);"></div>

<div class="fill">

# Op de hoogte blijven, en de afspraken van vandaag

<div class="np-grid-2" style="margin-top: 0.5rem; gap: 1.3rem; align-items: start;">
<div class="np-card accent-blue" style="padding:0.7rem 1rem;font-size:0.86rem;line-height:1.5;">
<strong>Wat OKx aanbiedt</strong>
<ul style="margin:0.4rem 0 0;padding-left:1.1rem;">
<li><strong>Alles openbaar en herleidbaar</strong> in GitHub (Npuls-OKx/Public): begrippen, informatiemodel, specificaties, besluiten</li>
<li><strong>Per doelgroep de juiste vorm</strong>, uit dezelfde bron: leeshulp met invulblad, specificatie, deck</li>
<li><strong>De voorbeelduitwerking</strong> als gemeenschappelijke taal</li>
</ul>
</div>
<div class="np-card accent-green" style="padding:0.7rem 1rem;font-size:0.86rem;line-height:1.5;">
<strong>Voorstel voor vandaag</strong>
<ul style="margin:0.4rem 0 0;padding-left:1.1rem;">
<li><strong>AII spoor 3</strong>: werksessie over aanmelden, intekenen, inschrijven en het ontsluiten van aanbod</li>
<li><strong>Onderwijs Catalogus</strong>: gedeelde begrippen en informatiemodel met eduXchange</li>
<li><strong>EduID en identity provisioning</strong>: wie is leidend voor de student in de keten</li>
<li><strong>Leeruitkomsten</strong>: met de LUK-werkgroep de sleutel over de pijlers heen vaststellen</li>
<li><strong>Ritme</strong>: OKx aan tafel op de raakvlakken, de anderen bij de kerngroep techniek</li>
</ul>
</div>
</div>

<div class="np-card accent-orange" style="margin-top: 0.8rem; font-size: 0.9rem; line-height: 1.5; padding: 0.55rem 1rem;">
<strong>Twee knopen die wij vandaag kunnen doorhakken:</strong> kiezen tot en met de leeractiviteit, en leeruitkomsten als ordenend principe. Deelt de tafel die, dan bouwen wij daarop verder.
</div>

</div>

<!--
Vraag 3 van Hans. Uit de voorbereiding (Garik): een groot deel van het werk is de informatie
op een behapbare manier bij betrokken partijen brengen, want het stakeholderveld is complex.
Ashwin wil vanmiddag knopen doorhakken: de twee uitgangspunten zijn daarvoor de kandidaten.
AI als mogelijk extra onderwerp alleen noemen als het ter sprake komt.
-->
