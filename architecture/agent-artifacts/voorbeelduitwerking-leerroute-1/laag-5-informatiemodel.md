# Laag informatiemodel: instantieerbaarheid voor de casus Jochem

Analyse voor Public #106 (de opleiding van Jochem uitgedrukt in het informatiemodel), stand 16 september 2026. Alleen bevindingen met bron; niets gewijzigd, niets gepost.

## Bronnen en afkortingen

| Afkorting | Bestand |
|---|---|
| im.md | meta wt-232 `architecture/model/informatiemodel/informatiemodel.md`; ontwerpkeuzes 1 tot 17 op r74-90, brugtabel r96-115 |
| im.json | idem `informatiemodel.json`: 66 `objecttypen` (naam, kolom, scope, oeapi), 156 `relaties` (soort, van, naar, label), 36 `oeapi_mapping`; 56 objecttypen binnen scope, 10 buiten |
| map.md | idem `informatiemodel-oeapi-mapping.md` |
| plaat | idem `OKx informatiemodel v0.1.jpg`, bekeken |
| bl.md, bl.json | meta wt-232 `architecture/docs/specificatie/begrippen/begrippenlijst.md` en `begrippen.json`: 73 begrippen (7 families, 66 objecttypen), 33 objecttypen gedefinieerd, 33 nog te definiëren (bl.md r27-30, r86-98) |
| pj | meta wt-232 `architecture/docs/specificatie/leerroute-uitwerking/doc/persona_jochem.md` |
| lr1 | Public wt-102 `Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md`: ankertabel r556-637, gegevensoverzicht r798-832, bronrollen r872-890, fasen r921-1015, ASCII-boom r1017-1118 |
| #234, #235, #105 | Npuls-OKx/meta#234 (26 punten), meta#235, Npuls-OKx/Public#105, gelezen met gh |

Oordeel per objecttype: direct (de bron noemt een instantie), afleidbaar (instantie vraagt een gemarkeerde aanname), niet (de bron biedt niets, of het objecttype is buiten scope). Telling over 66: 33 direct, 21 afleidbaar, 12 niet (10 buiten scope, 2 binnen scope: `Toetsonderdeel weging`, `Persoonlijke ontwikkeling`).

## 1. Instantiematrix

Kolommen: scope uit im.json, definitie uit bl.json (`status`), oordeel, voorbeeldinstantie, bron of aanname. Jaartallen (cohort 2026) zijn overal een aanname; geen bron noemt een jaar.

### Kwalificatiekader mbo (plaatkop `Kwalificatiekader MBO`)

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Kwalificatie dossier` | binnen | ja | direct | Apothekersassistent, crebo-dossier 23450 | lr1 r52, r1025 |
| `Kwalificatie` | binnen | ja | direct | kwalificatie 27141, niveau 4 | lr1 r52, r1026 |
| `Kerntaak` | binnen | ja | direct | B1-K1 Biedt farmaceutische patiëntenzorg; B1-K2; B1-K3 | lr1 r52 |
| `Werkproces` | binnen | ja | direct | B1-K1-W2 Voert medicatiebewaking uit | lr1 r728, r1047 |

### Onderwijskundig kader instelling (plaatkop `Onderwijskundigkader instelling`)

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Leeruitkomst` | binnen | ja | afleidbaar | "voert medicatiebewaking uit volgens protocol", vertaling van B1-K1-W2 | pj r26; lr1 r1039 noemt alleen "LO-sets van W1..W4", nergens een geformuleerde leeruitkomst; aanname: een op een per werkproces (im.md r75) |
| `Competenties / Skills` | buiten | nee | niet | | pj r39 "beroepsvaardigheden" heeft geen drager binnen scope |
| `Kennis` | buiten | nee | niet | | lr1 r599 noemt de dimensie; buiten scope (im.md r84) |
| `Vaardigheid` | buiten | nee | niet | | idem |
| `Inzicht` | buiten | nee | niet | | idem |

### Onderwijsspecificatie

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Opleiding specificatie` | binnen | nee | direct | Apothekersassistent, versie 2026.1, status definitief | lr1 r1024-1029 |
| `Opleidingsprogramma specificatie` | binnen | ja | direct | BOL voltijd (diplomaprogramma); daarnaast BBL, Havisten-route en programma Keuzedelen | lr1 r1031-1079 |
| `Keuzedeel` | binnen | nee | direct | Ondernemerschap in de zorg | lr1 r71, r81, r677; lr1 r1075-1080 modelleert het als onderwijseenheid onder programma Keuzedelen, de plaat als specialisatie van de programmaspecificatie |
| `Keuzedeelruimte` | binnen | ja | direct | keuzeruimte 720 SBU, elke derde periode een keuzedeel | lr1 r52, r1058; pj r97 |
| `Onderwijseenheid specificatie` | binnen | ja | direct | Blok B1-K1; Basisfarmacologie; Generieke onderdelen (NL, rekenen, Engels, LB&B) | lr1 r1036, r1056-1057, r734 |
| `Leeronderdeel specificatie` | binnen | ja | direct | B1-K1-W2 Medicatiebewaking, 40 SBU (20 BOT, 12 OOT, 8 BPV) | lr1 r728-736, r1047 |
| `Les specificatie` | buiten | ja | niet | (lr1 r1094 noemt wel Les 1 Introductie WHAM-vragen) | buiten scope (im.md r81) |
| `Toetsonderdeel specificatie` | binnen | ja | direct | Praktijktoets baliegesprek (OSCE), schaal onvoldoende/voldoende/goed; formatieve casuïstiek | lr1 r1114-1118, r735 |
| `Examenonderdeelspecificatie` | binnen | ja | afleidbaar | kennisexamens Nederlands, rekenen, Engels; proeve van bekwaamheid (assisteren bij een wortelkanaalbehandeling) | pj r112; aanname: de proeve dekt B1-K1; de OSCE staat als "summatief" (lr1 r1116), zie keuze 9 |
| `Student keuze regelset` | binnen | nee | afleidbaar | voorsortering keuzedelen op leerroute, keuzedeelruimte, type, domein en locatie; minimaal 720 SBU | pj r98-99 (story-0013); aanname: de voorsortering is de regelset; de casus kent geen voorwaarde in behaalde leeruitkomsten |

### Onderwijsaanbod

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Opleidingsaanbod van Instelling` | binnen | ja | afleidbaar | opleidingenoverzicht instroommoment september | pj r70; aanname: schooljaar |
| `Opleidingaanbod` | binnen | ja | direct | Apothekersassistent regulier, start september | lr1 r58, r943 |
| `Opleidingsprogramma aanbod` | binnen | nee | direct | BOL voltijd, startcohort september, 4 perioden per jaar | lr1 r933, r1034 |
| `Keuzedeelaanbod` | binnen | nee | direct | Ondernemerschap in de zorg, periode 7, locatie A | lr1 r81, r981 (daar `opleidingsprogramma-aanbod` van type keuzedeel) |
| `Onderwijseenheid aanbod` | binnen | nee | afleidbaar | Blok B1-K1 in periode 1 en 2 | lr1 r728 "Jochems cohort", r1001 (variant); aanname: perioden |
| `Leergelegenheid` | binnen | nee | afleidbaar | lessenreeks Baliegesprek en triage, 6 weken x 1 dagdeel, geroosterd | lr1 r953, r1090-1092; aanname: rooster |
| `Lesgelegenheid` | buiten | nee | niet | (pj r87: de geroosterde les waarin de docent aanwezigheid opneemt) | buiten scope |
| `Toetsgelegenheid` | binnen | ja | afleidbaar | afname OSCE in periode 2 | lr1 r963, r1114; aanname: moment |
| `Examengelegenheid` | binnen | ja | direct | proeve bij het leerbedrijf, stand-by tot een patiënt zich meldt; kennisexamens vroeg in het programma | pj r112; lr1 r1009 |

### Onderwijsverbintenis

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Opleiding aanbod  verbintenis` | binnen | nee | direct | Jochem op Apothekersassistent regulier (lr1 noemt het `opleidingsverbintenis`) | lr1 r943-947; pj r77-78 |
| `Opleidingsprogramma aanbod verbintenis` | binnen | nee | direct | Jochem op BOL voltijd | lr1 r943, r185 |
| `Keuzedeel aanbod verbintenis` | binnen | nee | direct | inschrijving keuzedeel Ondernemerschap in de zorg | lr1 r183-188, r981; pj r104 |
| `Onderwijseenheid aanbod verbintenis` | binnen | nee | afleidbaar | Jochem op Blok B1-K1, periode 1 | lr1 r967, r999 (alleen in de variant temporiseren); aanname voor de happy flow |
| `Leergelegenheid verbintenis` | binnen | nee | direct | presentielijst lessenreeks Baliegesprek en triage; ook de docent als deelnemer met rol | lr1 r953-957, r822 |
| `Lesgelegenheid verbintenis` | buiten | nee | niet | | buiten scope |
| `Toetsgelegenheid verbintenis` | binnen | ja | afleidbaar | Jochem als kandidaat OSCE | lr1 r888; aanname |
| `Examengelegenheid verbintenis` | binnen | ja | direct | Jochem op de kandidatenlijst van de proeve | lr1 r1009; pj r112 |
| `Inschrijving` | binnen | ja | direct | bewijs van inschrijving; registratie naar ROD | pj r21, r77-79; lr1 r178-185 |

### Onderwijsresultaat

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Opleiding aanbod resultaat` | binnen | nee | afleidbaar | kwalificatie behaald, diplomastatus | pj r119; lr1 r826; aanname |
| `Opleidingsprogramma resultaat` | binnen | nee | afleidbaar | voortgang programma: op schema | pj r107-109; lr1 r827; aanname |
| `Keuzedeel resultaat` | binnen | nee | afleidbaar | examenresultaat keuzedeel, eventueel certificaat | pj r46, r104; lr1 r52; aanname |
| `Onderwijseenheid resultaat` | binnen | nee | afleidbaar | Blok B1-K1 behaald | lr1 r967 (variant), r828; aanname |
| `Leergelegenheid resultaat` | binnen | nee | afleidbaar | deelname en formatieve score lessenreeks | lr1 r971, r829; pj r49; aanname |
| `Lesgelegenheid resultaat` | buiten | nee | niet | (drager van `Aanwezigheid` op de plaat) | buiten scope; #234 punt 15 |
| `Toetsgelegenheid resultaat` | binnen | nee | afleidbaar | OSCE: voldoende | lr1 r971, r1118; aanname |
| `Examengelegenheid resultaat` | binnen | nee | direct | kennisexamens behaald, verwerkt in SVS en examendossier | pj r112 |
| `Aanwezigheid` | binnen | nee | direct | aanwezigheid per les; 3075 uur BOT en BPV over alle leerjaren | pj r87, r119; lr1 r957; de drager op de plaat is buiten scope |
| `Formatief resultaat` | binnen | ja | afleidbaar | resultaat formatieve casuïstiek medicatiebewaking | lr1 r735; pj r49; aanname |
| `Formatieve beoordeling` | binnen | ja | afleidbaar | idem; de casus scheidt beoordeling niet van resultaat | #234 punt 12; aanname |
| `Summatief resultaat` | binnen | ja | direct | kennisexamen Nederlands behaald; summatieve praktijkbeoordeling in de BPV | pj r112; lr1 r735 |
| `Summatieve beoordeling` | binnen | ja | afleidbaar | beoordeling van de proeve, vastgesteld door de examencommissie | lr1 r411, r1009; aanname |

### Resultaatstructuur

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Summatieve resultaat structuur` | binnen | ja | direct | structuur Apothekersassistent van het startcohort, bij inschrijving gekoppeld, na de keuze verrijkt met het keuzedeel | pj r78, r104; lr1 r189 |
| `Formatieve resultaat structuur` | binnen | ja | direct | formatieve structuur in het SVS | pj r104; inhoud aanname |
| `Examenonderdeel weging` | binnen | nee | afleidbaar | elk examenonderdeel telt als voldoende-vereiste | pj r112; aanname: de bron noemt geen cijferweging |
| `Toetsonderdeel weging` | binnen | nee | niet | | geen bron noemt een formatieve weging |
| `Summatief Afrondingscriterium` | binnen | nee | afleidbaar | alle examens behaald en 3075 uur BOT en BPV | pj r119; aanname: onderwijstijd hoort bij het criterium |
| `Persoonlijke ontwikkeling` | binnen | nee | niet | | betekenis onbekend (#234 punt 16) |

### Buiten de kolommen

| Objecttype | Scope | Def. | Oordeel | Instantie | Bron / aanname |
|---|---|---|---|---|---|
| `Persoon` | binnen | nee | direct | Jochem, 17, na het vmbo | lr1 r52 |
| `Student` | binnen | ja | direct | Jochem als student | pj |
| `Medewerker` | binnen | ja | direct | SLB'er, docent farmacotherapie, BPV-begeleider, examinator | lr1 r202; pj r84, r91, r112 |
| `Plaatsingsgroep` | binnen | nee | direct | stam/plaatsingsgroep bij inschrijving; lesgroep keuzedeel (groep A); BPV-cluster max 6; planninggroep | pj r78, r104; lr1 r189, r677, r736, r953 |
| `Cohort / periode` | binnen | ja | direct | startcohort september; daarnaast "periode 7" als tijdvak | pj r78; lr1 r81, r728 |
| `Verzoek tot Aanbod / Intekening op specificatie` | binnen | ja | afleidbaar | animo-check keuzedelen vóór de planning; verzoek van de OC aan planning om aanbod te maken | pj r101; lr1 r933; aanname: de animo-check is een intekening op de keuzedeelspecificatie |
| `Aanmelding` | binnen | ja | direct | aanmelding opleiding via CAMBO/AII; aanmelding keuzedeel (voorkeurslijst) | pj r14, r74; lr1 r178-185 |
| `Waarde document (diploma / certificaat)` | binnen | ja | direct | diploma Apothekersassistent; certificaat keuzedeel | pj r119-120, r104 |
| `Examenplan` | buiten | ja | niet | (pj r55 en lr1 r1009 noemen het wel) | buiten scope (im.md r83) |
| `OER` | buiten | ja | niet | (pj r78, r112 noemen het wel) | buiten scope |

## 2. Relatiematrix

Toonbaar: aan beide kanten een instantie uit deel 1 (direct of afleidbaar). Telling van deze analyse over de 156 relaties in im.json: 124 toonbaar (44 met een directe instantie aan beide kanten, 80 met minstens een aanname), 32 niet. Aantallen per soort: Access 12, Aggregation 24, Association 106, Specialization 14; 105 relaties dragen geen label.

| Soort en label (van, naar) | Aantal | Toonbaar | Niet toonbaar, met reden |
|---|---|---|---|
| Access, ongelabeld (`Persoon` naar `Aanmelding`, `Verzoek`, `Aanwezigheid` en 8 resultaattypen; `Student` naar `Cohort / periode`) | 12 | 11 | `Persoon` naar `Lesgelegenheid resultaat` (buiten scope) |
| Aggregation `bevat`, `bestaat uit` (dossier, kwalificatie, kerntaak, werkproces) | 3 | 3 direct | |
| Aggregation ongelabeld (specificatieboom, aanbodboom, structuren, zelfaggregaties) | 21 | 14 | `Competenties / Skills` naar kennis, vaardigheid, inzicht (3); `Formatieve resultaat structuur` naar `Toetsonderdeel weging`; `Leergelegenheid` naar `Lesgelegenheid`; `Leeronderdeel specificatie` naar `Les specificatie`; `OER` naar `Examenplan` |
| Association `Wordt vertaald naar` (dossier, kwalificatie, kerntaak, werkproces naar `Leeruitkomst`) | 4 | 4 met aanname | de ankertabel zegt dat op dossier- en kwalificatieniveau geen eigen leeruitkomst bestaat (lr1 r573-575, r586); de plaat trekt vanaf beide wel een pijl |
| Association `voorwaarde op` (`Leeruitkomst` naar regelset) | 1 | 0 | de casus kent alleen een volgorde-eis tussen onderwijseenheden (lr1 r734), geen voorwaarde in behaalde leeruitkomsten |
| Association `Input voor` (8 specificatietypen naar `Verzoek`) | 8 | 7 met aanname | `Les specificatie`; `Keuzedeelruimte` heeft geen `Input voor` |
| Association `Leidt tot` (`Verzoek` naar 8 aanbodtypen) | 8 | 7 met aanname | `Lesgelegenheid` |
| Association `Op basis van` (8 aanbodtypen naar `Aanmelding`) | 8 | 7, waarvan 2 direct (opleiding, keuzedeel) | `Lesgelegenheid`; in im.json loopt de relatie van aanbod naar `Aanmelding`, im.md r86 leest andersom ("de Aanmelding gaat Op basis van een aanbod") |
| Association `middels` (`Aanmelding` naar 8 verbintenistypen) | 8 | 7, waarvan 3 direct | `Lesgelegenheid verbintenis` |
| Association `Minimaal 1` (opleidingsverbintenis, programmaverbintenis) | 1 | 1 direct | richting ontbreekt (#234 punt 16) |
| Association `Worden gegroepeerd via`, `Groepeert Studenten op toepasbare` | 2 | 2 direct | het niveau van de groep blijft open (#235) |
| Association `wordt uitgewerkt in`, `staat beschreven in` (cohort, OER, kwalificatie) | 2 | 0 | `OER` buiten scope, terwijl pj r78 en r112 de OER noemen |
| Association `kent` | 2 | 1 met aanname | `Examenplan` kent structuur (buiten scope); `Formatieve beoordeling` kent `Formatief resultaat` blijft toonbaar met aanname |
| Association `conform`, `met` | 3 | 3, waarvan 1 direct | formatief heet `kent`, summatief `met`: twee labels voor dezelfde verhouding |
| Association ongelabeld: specificatie naar leeruitkomst (7), specificatie naar aanbod (8), aanbod naar verbintenis (8), verbintenis naar resultaat (8), `Plaatsingsgroep` naar verbintenis (8), regelset naar specificatie (6), keuzedeelruimte naar regelset, keuzedeel naar keuzedeelruimte, weging naar specificatie (2), structuur en criterium naar waardedocument (3), structuur naar leeruitkomst, aanwezigheid (3), persoonlijke ontwikkeling (2), examenplan naar kerntaak | 59 | 44 | leslaag (7); `Toetsonderdeel weging`; `Persoonlijke ontwikkeling` (2); `Examenplan` naar `Kerntaak`; `Aanwezigheid` naar `Lesgelegenheid resultaat`; regelset naar opleiding, programma, onderwijseenheid, leeronderdeel (4: de casus kiest alleen keuzedelen) |
| Specialization ongelabeld | 13 | 12 | `Leeruitkomst` naar `Competenties / Skills` (buiten scope) |
| Specialization `wordt` (`Aanmelding` naar `Inschrijving`) | 1 | 1 direct | de enige specialisatie die een toestandsovergang uitdrukt; de 13 andere lopen van bijzonder naar algemeen |

Onduidelijk voor een lezer, naast `Minimaal 1` zonder richting en de leesrichting van `Op basis van`: de 7 pijlen van specificatie naar `Leeruitkomst` dragen geen label terwijl keuze 1 (im.md r74) ze "wijzen naar" noemt; specificatie naar aanbod draagt geen "instantieert" terwijl de ankertabel dat woord gebruikt (lr1 r627-633); ongelabeld en niet uit de objecttypen af te leiden zijn `Examenplan` met `Kerntaak`, structuur en criterium met `Waarde document`, twee resultaattypen met `Aanwezigheid`, `Keuzedeel` met `Keuzedeelruimte` en beide relaties van `Persoonlijke ontwikkeling`. De brugtabel zegt dat de plaat het toetsonderdeel onder de onderwijseenheid hangt (im.md r103); im.json kent geen aggregatie van `Onderwijseenheid specificatie` naar `Toetsonderdeel specificatie` (alleen vanuit de twee structuren), en de casus hangt de OSCE onder het leeronderdeel (lr1 r1088, r1114). Drie plaatsen voor een objecttype. `Medewerker` heeft geen eigen relatie; de docent op een leergelegenheid (lr1 r822, r953) bereikt zijn verbintenis op de plaat alleen via `Aanmelding`.

## 3. Ontwerpkeuzes onder de loep

| Nr | Keuze (im.md r74-90) | Zichtbaar in de casus | Forceert een besluit |
|---|---|---|---|
| 1 | leeruitkomst als sleutel | ja, mits leeruitkomsten worden aangenomen: elke specificatie in de boom draagt `dektLeeruitkomsten` (lr1 r1035-1039, r1076); structuur naar leeruitkomst komt in de bron niet voor | nee, maar elke instantie van kolom 2 is een aanname |
| 2 | vertaald, niet gespecialiseerd | ja: blok = kerntaak, leeronderdeel = werkproces (lr1 r1021, r1036, r1043); de bron formuleert nergens een leeruitkomst | ja: de uitwerking moet kiezen tussen "leeruitkomst = werkproces met uuid" (#234 punt 1) en een eigen formulering |
| 3 | landelijke leeruitkomsten | nee: intra-instelling; lr1 r599 noemt CompetentNL als voorkeur | nee |
| 4 | niveau ligt niet vast | ja: een onderwijseenheid per kerntaak, plus Generieke onderdelen zonder kerntaak (lr1 r1057) | nee |
| 5 | specificatie zelfstandig | ja: programma Keuzedelen zonder bovenliggende opleiding, N:M gekoppeld (lr1 r1071-1080) | nee |
| 6 | keuze uit specificaties, voorwaarde in leeruitkomsten | nee: Jochem kiest op periode 7 en locatie A, dus op aanbod (lr1 r71-81, r981); de enige voorwaarde is een volgorde-eis op onderwijseenheden (lr1 r734) | ja: specificatie-id of aanbod-id uit het SKS (#234 punt 10) |
| 7 | resultaat op verbintenis, structuur als vertaaltabel | half: SVS registreert per verbintenis (lr1 r890), maar de ankertabel zegt "erop behaald" (lr1 r583) en Jochem "monitort welke leeruitkomsten hij heeft behaald" (pj r50, r109) | ja: de uitwerking moet de weg van kennisexamen Nederlands naar een leeruitkomst tekenen |
| 8 | leslaag buiten | ja, in negatieve zin: de docent registreert per les (pj r87) en het diploma vraagt 3075 uur (pj r119); `Aanwezigheid` hangt aan een objecttype buiten scope | ja: drager van aanwezigheid (#234 punt 15) |
| 9 | examenonderdeel specialiseert toetsonderdeel | ja: de OSCE is een toetsonderdeel "summatief" (lr1 r1116), de praktijkbeoordeling in de BPV is summatief (lr1 r735); lr1 r593 houdt toets en examen als gescheiden ketens | ja: is de OSCE een toetsonderdeel dat meetelt of een examenonderdeel (#234 punt 5) |
| 10 | structuur, niet examenplan | ja: de bron redeneert vanuit examenplan en examendossier (pj r55, r112; lr1 r1009); de resultaatboom wordt per student verrijkt met het keuzedeel (lr1 r189) | ja: de uitwerking moet laten zien dat de structuur alleen volstaat, en of zij per cohort of per student is (#234 punt 4) |
| 11 | leeruitkomst is competentie | nee: grijs op de plaat | nee |
| 12 | keuzedeelruimte is oningevuld keuzedeel | ja: 720 SBU, elke derde periode, oningevuld bij geen passend aanbod (lr1 r52, r183; pj r97); de boom zet het keuzedeel als onderwijseenheid (lr1 r1075) | ja: meerdere ruimtes per programma en de plek van het keuzedeel (#234 punt 8) |
| 13 | intekenen, aanmelden, inschrijven | half: aanmelding wordt inschrijving voor opleiding en keuzedeel (lr1 r178-185); intekening alleen als animo-check (pj r101); aanbod rijpt van gepland naar geroosterd (lr1 r738-752) | ja: de kerngroep herkent intekenen niet (context r14) |
| 14 | student en medewerker zijn rollen | ja: Jochem en vier medewerkerrollen (lr1 r202); niemand is beide | deels: hoe bereikt een docent zijn leergelegenheidverbintenis zonder aanmelding |
| 15 | verbintenis via groep | ja: stamgroep, lesgroep keuzedeel, BPV-cluster, planninggroep (pj r78, r104; lr1 r677, r736, r953) | ja: een groep per specificatieniveau of niet (#235) |
| 16 | specificatie draagt geldigheid | ja: versie 2026.1 en status definitief op de specificatie (lr1 r1027); uiterste inschrijf- en afstudeerdatum staan in lr1 op specificatie (r805) en op aanbod (r812) | ja: welke datums op welk objecttype |
| 17 | cohort bepaalt structuur | ja: bij inschrijving verbonden aan cohort, OER en resultaatstructuur (pj r78); "periode 7" is een tijdvak zonder objecttype | ja: cohort en periode als een of twee objecttypen (#234 punt 19), en de structuur per student (lr1 r189) |

## 4. Verhouding tot de ankertabel

De ankertabel (lr1 r572-580) heeft zes kolommen en zeven rijen; de plaat zeven families (im.md r41-51). Kolom 2 "Beoogde leeruitkomst" heet op de plaat `Onderwijskundig kader instelling`; de familie `Resultaatstructuur` heeft in de ankertabel geen kolom. Het kaderscenario zegt zelf dat kolom 2 nog door het kernteam bevestigd moet worden (lr1 r591).

| Richting | Wat mist |
|---|---|
| In de ankertabel, niet op de plaat | de cellen van kolom 2 per niveau: "collectie van leeruitkomst-collecties", "leeruitkomst-collectie", `Lesuitkomst`, "scope van toetsing", "te behalen leeruitkomst-set vastgesteld door de examencommissie" (lr1 r574-580); de plaat kent alleen `Leeruitkomst` met een zelfaggregatie; de statuswaarde per verbintenis (`Association.state`, lr1 r637); de leeruitkomstdefinitie met CompetentNL (lr1 r599) wijkt af van im.md r75 en bl.md |
| Op de plaat, niet in de ankertabel | de keuzedeelrij (`Keuzedeel`, `Keuzedeelruimte`, `Keuzedeelaanbod`, `Keuzedeel aanbod verbintenis`, `Keuzedeel resultaat`); `Opleidingsaanbod van Instelling`; `Student keuze regelset`; `Inschrijving`; `Aanwezigheid`, de vier formatieve en summatieve resultaattypen; de zes objecttypen van `Resultaatstructuur`; alles buiten de kolommen (persoon en rollen, plaatsingsgroep, cohort, verzoek, aanmelding, waardedocument, examenplan, OER); de grijze onderwijskundige begrippen |
| Tegenstrijdig | kolom 2 zegt "n.v.t." op dossier- en kwalificatieniveau (lr1 r573-575), de plaat trekt `Wordt vertaald naar` vanaf beide; de ankertabel zet `Kerntaak / Werkproces` in een rij, de plaat kent twee objecttypen met `bestaat uit` |

| Ankertabel en lr1 | Plaat (im.json) | Aard van het verschil |
|---|---|---|
| `Kwalificatiedossier` | `Kwalificatie dossier` | spatie |
| `Opleidingsspecificatie`, `Opleidingsprogramma-specificatie`, `Onderwijseenheid-specificatie`, `Leeronderdeel-specificatie`, `Toetsonderdeel-specificatie` | `Opleiding specificatie`, `Opleidingsprogramma specificatie`, `Onderwijseenheid specificatie`, `Leeronderdeel specificatie`, `Toetsonderdeel specificatie` | koppelteken tegenover spatie; "Opleidings" tegenover "Opleiding" |
| `Lesspecificatie` | `Les specificatie` | aaneen tegenover spatie |
| `Examenonderdeel-specificatie` (r580), `Examenspecificatie` (r610, r811) | `Examenonderdeelspecificatie` | twee namen in lr1 zelf; bl.md r64 signaleert het |
| `Opleidingsaanbod`, `Opleidingsprogramma-aanbod`, `Onderwijseenheid-aanbod` | `Opleidingaanbod`, `Opleidingsprogramma aanbod`, `Onderwijseenheid aanbod` | "Opleidingsaanbod" is op de plaat gereserveerd voor `Opleidingsaanbod van Instelling` |
| `opleidingsprogramma-aanbod` van type keuzedeel, `opleidingsprogramma-verbintenis` als keuzestelling (r850, r981) | `Keuzedeelaanbod`, `Keuzedeel aanbod verbintenis` | lr1 gebruikt het programmaniveau, de plaat een eigen specialisatie |
| `Opleidingsverbintenis`, `Opleidingsprogramma-verbintenis`, `Onderwijseenheid-verbintenis`, `Leergelegenheid-verbintenis` | `Opleiding aanbod  verbintenis` (dubbele spatie), `Opleidingsprogramma aanbod verbintenis`, `Onderwijseenheid aanbod verbintenis`, `Leergelegenheid verbintenis` | de plaat voegt "aanbod" toe, behalve bij de gelegenheden |
| `…-verbintenis resultaat` (zes rijen) | `Opleiding aanbod resultaat`, `Opleidingsprogramma resultaat`, `Onderwijseenheid resultaat`, `Leergelegenheid resultaat`, `Toetsgelegenheid resultaat`, `Examengelegenheid resultaat` | de plaat laat "verbintenis" weg, en bij de eerste staat "aanbod" |
| "Beoogde leeruitkomst", "Kwalificatiekader" | `Onderwijskundigkader instelling`, `Kwalificatiekader MBO` (plaatkoppen) tegenover `Onderwijskundig kader instelling`, `Kwalificatiekader mbo` (bl.json) | drie schrijfwijzen voor twee families (#234 punt 17) |

## 5. Wat de open issues voor de casus betekenen

| Punt | Raakt in de casus | Landt als |
|---|---|---|
| #234 punt 1, keuze 2 | de leeruitkomst bij B1-K1-W2 moet worden opgeschreven; de bron heeft er geen | aanname (formulering en identifier) |
| #234 punt 2, keuze 7, ADR 0022 | "kennisexamen Nederlands behaald" en "welke leeruitkomsten heeft Jochem behaald" (pj r50, r112) | aanname: resultaat op de examengelegenheidverbintenis, structuur wijst de leeruitkomst aan; vraag aan de kerngroep |
| #234 punt 3 | plaats van de OSCE: onder leeronderdeel (lr1 r1114), onder onderwijseenheid (im.md r103), onder resultaateenheid (logisch model); im.json heeft de aggregatie vanuit de onderwijseenheid niet | vraag |
| #234 punt 4 en 10 | examenplan en examendossier in de bron (pj r55, r112); resultaatboom per student verrijkt (lr1 r189) | aanname: individuele structuur als specialisatie of als instantie per student |
| #234 punt 5, keuze 9 | OSCE "summatief" (lr1 r1116) en summatieve praktijkbeoordeling in de BPV (lr1 r735) hebben op de plaat geen resultaatpad met weging | vraag |
| #234 punt 8, keuze 12 | keuzedeelruimte elke derde periode (pj r97) tegenover een ruimte per doelgroepprogramma in het logisch model | aanname |
| #234 punt 10, keuze 6 en 13 | keuze op periode 7 en locatie A (lr1 r81): aanbod, geen specificatie; intekening alleen als animo-check (pj r101) | vraag |
| #234 punt 11, #235, keuze 15 | vier soorten groepen in de bron (pj r78, r104; lr1 r677, r736, r953) | vraag: groep per specificatieniveau |
| #234 punt 12 | de bron scheidt beoordeling niet van resultaat | aanname: alleen resultaat instantiëren |
| #234 punt 13 | `Opleidingaanbod` als "Apothekersassistent regulier, start september" is ingepland, MORA en RIO kennen het tijdloos | aanname |
| #234 punt 15, keuze 8 | aanwezigheid per les en 3075 uur (pj r87, r119) zonder drager binnen scope | vraag |
| #234 punt 16 | `Persoonlijke ontwikkeling` en vier ongelabelde associaties blijven leeg | leeg laten en benoemen |
| #234 punt 18 | van de 22 verbintenis- en resultaattypen zijn 15 ongedefinieerd; elke instantie is dan een impliciete definitie | benoemen per rij |
| #234 punt 19, keuze 17 | "periode 7", schooljaar en startcohort vragen een tijdvak naast `Cohort / periode` | aanname |
| #234 punt 22, #105.1 | aanmelding naar inschrijving, gepland naar geroosterd, voorlopig naar vastgesteld, inactieve inschrijving (lr1 r183, r738, r1009) | aanname: toestanden als tekst bij de instantie, geen statusmodel |
| #234 punt 23, #105.2 | crebo 23450, kwalificatie 27141, B1-K1-W2 zijn de enige sleutels in de bron; keuzedeelcode, RIO, eduID ontbreken | aanname: alleen bronsleutels tonen |
| #234 punt 25, #105.3 | BPV-plek, leerbedrijf, POK in KRS, BPV-begeleider, proeve bij het leerbedrijf, 8 BPV-SBU (pj r37-38, r91, r112; lr1 r729) zonder objecttype | vraag: BPV als onderwijseenheid met organisatie erachter, of buiten scope |
| #234 punt 24 | eigenaarschap per objecttype | de bronrollentabel (lr1 r872-890) levert per rij een bron; kolom "bron" in de uitwerking beantwoordt dit punt |
| #234 punt 26 | precies dit deliverable, plus een invulbare toetslijst per objecttype | vorm van de uitwerking |

## 6. Aanbeveling

1. Vorm: per familie een tabel met objecttype, instantie, bron, aanname en oordeel, in de volgorde van deel 1; daaronder een mermaid-diagram met alleen de instanties als knopen en de relaties uit im.json waarvan beide uiteinden een instantie hebben, met label en richting uit im.json. Objecttypen zonder instantie staan in een aparte tabel met de reden.
2. Generatie: een script leest im.json (objecttypen per kolom, relaties) en een handmatig bestand `instanties.json` (objecttype, instantie, bron, aanname, oordeel) en schrijft de tabellen en het diagram; de plaat zelf niet invullen (harde regel 1, geen archimate-bestand aanraken).
3. Controles die falen en waarop: elk objecttype binnen scope heeft een rij (faalt op `Toetsonderdeel weging`, `Persoonlijke ontwikkeling`); elke relatie met twee instanties wordt getekend en elke relatie met een lege kant wordt geteld (32 nu); elke naam komt uit bl.json en niet van de plaatkoppen (faalt op `Kwalificatiekader MBO`, `Onderwijskundigkader instelling`, de dubbele spatie); elk gelabeld paar leest in de richting van im.json (faalt op `Op basis van`, `Minimaal 1`, `wordt`); daarna `python3 scripts/validate-docs.py` op het resultaat.
4. Drie vragen die de casus het scherpst stelt aan de kerngroep: (a) kiest Jochem zijn keuzedeel op de specificatie of op gepland aanbod (periode 7, locatie A), en levert het SKS dus een specificatie-id of een aanbod-id (keuzes 6 en 13, #234 punt 10); (b) waar landen "kennisexamen Nederlands behaald" en "3075 uur onderwijstijd": op de verbintenis met de structuur als vertaaltabel naar de leeruitkomst, en is aanwezigheid dan een resultaat binnen scope (keuzes 7 en 8, #234 punten 2 en 15); (c) welke groepen kent Jochem (stamgroep, lesgroep keuzedeel, BPV-cluster) en is BPV met leerbedrijf en POK een onderwijseenheid of buiten scope (#235, #105).
