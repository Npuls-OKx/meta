# Review van Niels op de voorbeelduitwerking verwerken

Relateert aan: #106, PR #252.

Niels van Duin heeft op 28 en 29 september 35 inline-opmerkingen achtergelaten bij de voorbeelduitwerking van leerroute 1 (Jochem). Alle opmerkingen gaan over domeinkennis: hoe het mbo werkelijk ontwerpt, plant, roostert en toetst. Dit plan neemt ze als gegrond aan en vertaalt ze naar wijzigingen in het voorbeeld.

## Uitkomst van de toets op de architectuur

Geen van de 35 opmerkingen botst met het informatiemodel. Bij zes opmerkingen blijkt de plaat een gat te hebben in plaats van Niels een denkfout. Die zes gaan als vraag mee naar de kerngroep; het voorbeeld blijft ondertussen binnen wat de plaat toestaat.

| # | Punt | Stand van de plaat | Voorstel |
|---|---|---|---|
| 1 | Leeronderdelen clusteren inhoudelijk tot een leergelegenheid, in de onderwijscatalogus | `Leergelegenheid` hangt onder `Onderwijseenheid aanbod` en is dus aanbod; een container aan de specificatiekant ontbreekt | Voorbeeld toont het clusteren via de bestaande associatie `Leeronderdeel specificatie` naar `Leergelegenheid`, meer-op-meer. Het ontbrekende objecttype wordt een vraag, geen verzinsel |
| 2 | De keuzedeelruimte hoort ook in de summatieve resultaatstructuur | Op de plaat ontbreekt die relatie; het logisch gegevensmodel kent haar wel (`RESULTAATEENHEIDSPECIFICATIE.beoordeelt`: onderwijseenheid of keuzedeelruimte) | Voorbeeld toont haar via de weging, met een vraag over het gat tussen laag 2 en laag 3 |
| 3 | Het keuzesysteem moet weten welke keuzedelen de student al heeft gedaan | `KRS` naar `SKS` bestaat op v1.7, `SVS` naar `SKS` bestaat niet | Voorbeeld laat de behaalde leeruitkomsten via KRS lopen, met een vraag of de hoofdplaat een stroom mist |
| 4 | Aanwezigheidsregistratie valt buiten OKx | `Aanwezigheid` staat op de plaat binnen scope, kolom Onderwijsresultaat | Voorbeeld toont het afgeleide deelnameresultaat dat keuzes vrijgeeft, en laat de registratie los. Scope van `Aanwezigheid` wordt een vraag |
| 5 | Toets en examen dragen schaal, afnamevorm, duur, hulpmiddelen en pogingen | MIM-niveau 2 kent geen attributen; het logisch model kent `resultaatmodel` en `toetsvorm` | Kenmerken komen in de instantietekst. Geen modelwijziging nodig |
| 6 | De toetsmatrijs hoort bij het toetsinstrument en woont niet in de catalogus | De conceptplaat hangt `Toetsmatrijs` onder `Les specificatie / toets specificatie` | Voorbeeld haalt de matrijs uit de stroom naar het LMS, met een vraag over de conceptplaat |

Eén opmerking vraagt om nadere duiding. Niels schrijft bij F2-01: "Na deze stap zijn het al leergelegenheden." Letterlijk gelezen zou de catalogus aanbodobjecten maken voordat er gepland is, en dat botst met de scheiding tussen specificatie en aanbod. Zijn eigen term "gewenste leergelegenheid" lost dat op: een wens aan de specificatiekant, zoals de conceptplaat ook `Gewenste Onderwijskundige Leeromgeving` kent. Het voorbeeld houdt die lijn aan.

## Acht werkpakketten

### W1. De verdieping ontkoppeld: werkproces, leeronderdeel, leergelegenheid

De zwaarste en belangrijkste. Het voorbeeld gebruikt werkproces-codes als naam voor leeronderdelen en leergelegenheden en suggereert daarmee dat de ene verdieping de andere is.

Niels: een werkproces is een summatieve verdieping van een kerntaak, een leeronderdeel is een ontwikkelingsgericht antwoord op hoe je daar komt. Een theorieleergelegenheid behandelt leeronderdelen van verschillende onderwijseenheden. Het is vrijwel nooit een op een.

| Onderdeel | Wijziging |
|---|---|
| Namen | 25 regels dragen een code als `B1-K1-W1` op een leeronderdeel, leergelegenheid, verbintenis of resultaat. Die codes eruit; didactische namen ervoor in de plaats, zoals "Baliegesprekken 101" |
| Structuur | Een leergelegenheid toevoegen die leeronderdelen uit twee onderwijseenheden draagt, via de bestaande associatie |
| Teksten | De zinnen bij F1-05, F1-06 en F1-08 herschrijven: de eenheid draagt toetsbare uitkomsten, het leeronderdeel het ontwerp |
| Rijpheid | In F2-01 verschuift `planbaar` van het leeronderdeel naar de gewenste leergelegenheid; het clusteren gebeurt in de catalogus, het logistiek bundelen in planning |

Opmerkingen: 4123325730, 4124013113, 4124357071, 4124364937, 4124370664, 4126981947, 4132366524, 4133697818, 4133733225.
Beelden: F1-05, F1-07, F1-08, F1-11, F2-01, F2-03, F2-04, F2-07, F4-01, F4-02, F4-07, F4-08, F4-09, F4-10, F4-11, F5-03, F5-04, F7-06.

### W2. Realistische maatvoering

Het scenario werkt met een instroomcohort van 120 studenten. Niels: 20 tot 40 is realistisch, enkele populaire opleidingen bij grote ROC's tikken de 100 aan. Juist daar zit de logistieke uitdaging van het mbo.

| Onderdeel | Wijziging |
|---|---|
| Scenario 1.1 | Cohort naar 48 studenten in twee groepen van 24. Verdeling over leerroutes toevoegen: 70 procent leerroute 1, 15 procent leerroute 2, 15 procent leerroute 3 |
| Docent | Aanstelling 0,8 FTE, dus een dag per week niet inzetbaar; 200 uur jaartaak als lid van de examencommissie; 10 minuten voor- en nazorg per gepland lesuur |
| Lesuur | Geen landelijke standaard: een ROC-eigen eenheid van 35, 45 of 50 minuten, vaak als blokuur van twee eenheden. Het voorbeeld kiest 45 minuten en noemt dat expliciet een keuze van de instelling |
| Aanbodgetallen | `120 plaatsen` naar `48 plaatsen`; `18 tot 120 studenten` naar `24 tot 48 studenten`, zodat de bandbreedte niet groter is dan een groepsgrootte |

Opmerkingen: 4122687194, 4122816686, 4122878371, 4126981947.
Beelden: scenario 1.1, F2-04, F2-05, F2-07, F6-05, F6-06.

### W3. Capaciteit en haalbaarheid

F2-05 laat de haalbaarheid uit de specificatie volgen. Niels: een specificatie zegt op zichzelf weinig over gevraagde capaciteit. Het inzicht ontstaat door de specificatie te combineren met de prognose op studentaantallen en de beschikbare capaciteit aan mensen en middelen.

| Onderdeel | Wijziging |
|---|---|
| Perspectief | F2-05 herbouwen: specificatie plus prognose plus toegewezen capaciteit als drie ingangen van een applicatiefunctie binnen planning |
| Cohort | Cohort uit het schaarstebeeld halen. Het cohort bepaalt welke leergelegenheden bij welk leerjaar horen, en speelt in schaarste geen rol |
| Rekenlijn | De doorrekening als zin opnemen: prognose naar aantal groepen, standaard jaarplan per groep, opgeteld per organisatie-eenheid tot vraag per lokaaltype en docentexpertise, afgezet tegen de beschikbare uren |
| Vrijgeven | F2-07: exacte capaciteit vrijgeven vergt hoge volwassenheid. Als zin opnemen, met de kanttekening dat het voor een aantal logistieke scenario's wel voorwaarde is |
| Roosteren | F4-07: lokaaltype, docentexpertise en groep aan de stroom naar het roostersysteem toevoegen; zonder die kenmerken heeft roosteren niets aan de uitwisseling |

Opmerkingen: 4126698562, 4126981947, 4133697818.
Beelden: F2-05, F2-07, F4-07, F4-08.

### W4. Toets en examen: kenmerken en scheiding

| Onderdeel | Wijziging |
|---|---|
| Kenmerken | Elk toets- en examenonderdeel krijgt schaal (cijfer met minimum, maximum en decimalen, of onvoldoende/voldoende/goed), afnamevorm, toetsduur, hulpmiddelen en aantal pogingen in de instantie |
| Titels | F4-04 en F4-05 heten voortaan "Summatieve resultaatstructuur naar ..."; nu staat er alleen "Resultaatstructuur" |
| Resultaatwaarde | F5-03: `Quiz WHAM-vragen: 8 van 10` wordt `Quiz WHAM-vragen: 8`, met de schaal op het toetsonderdeel. Het resultaat is in de praktijk een 8 |
| Keuzedeelruimte | F1-11: de keuzedeelruimte opnemen in de summatieve resultaatstructuur, plus een concept formatieve resultaatstructuur |
| Mengvorm | Als zin opnemen dat formatieve en summatieve onderdelen naast elkaar bestaan, dat een examen ook als toets telt, en dat het studentvolgsysteem ze op unieke codering onderscheidt |
| Vaststellen | F1-02: de examencommissie stelt vast; ontwerp van examenplan en resultaatstructuur ligt bij de ontwerper |

Opmerkingen: 4123033949, 4124180834, 4124218572, 4132618678, 4133587743, 4135374336.
Beelden: F1-02, F1-09, F1-11, F4-04, F4-05, F5-03.

### W5. Rollen terug naar de praktijk

Niels bij F4-09: de tekst doet alsof de SLB'er verbintenissen op geroosterde gelegenheden legt. Dat gebeurt niet.

| Onderdeel | Wijziging |
|---|---|
| Plaatsing | De SLB'er koppelt Jochem aan het opleidingsprogramma-aanbod en aan een plaatsingsgroep, en verder niets |
| Doorwerking | De plaatsingsgroep gaat vanuit de kernregistratie naar planning; daar worden alle geneste leergelegenheden voor de groep gepland, zonder tussenkomst van de SLB'er |
| Planninggroep | De planner mag om logistieke redenen een nieuwe groep vormen met een tijdelijke leergelegenheidverbintenis, omdat die lesgroep afwijkt van de plaatsingsgroep |
| Uitzondering | Pas bij vertraging komt de SLB'er in actie, om Jochem van specifieke gelegenheden af te halen |
| Examenplan | F1-02: als zin opnemen dat een vastgesteld examenplan in de praktijk nog wijzigt wanneer het beheer van het studentvolgsysteem de structuur niet kan verwerken, en dat de catalogus dat idealiter vooraf bewaakt |

Opmerkingen: 4123033949, 4133733225, 4135092754.
Beelden: F1-02, F4-08, F4-09.

### W6. Keuze rijpt in het studentkeuzesysteem

Drie opmerkingen halen de keuzedeelvoorkeur uit de intake weg.

| Onderdeel | Wijziging |
|---|---|
| Intake | F3-05: de voorlopige keuzedeelvoorkeur vervalt. Bij intake is dat nog niet gebruikelijk; definitieve vastlegging gebeurt minimaal een periode voor de keuzedeelruimte |
| Kernregistratie | F3-07: de voorkeur gaat niet mee naar de kernregistratie. Die registreert de definitieve keuze, en heeft geen rol in het rijpen ervan |
| Naar het keuzesysteem | F3-08: de kernregistratie levert de student, de opleidingsverbintenis, de groep en de al behaalde leeruitkomsten, zodat het keuzesysteem geen keuzes voorlegt die de student al deed. De deadline komt niet uit de kernregistratie, want die kent de planning van de keuzedeelruimte niet |
| Route | F6-01: kiezen tussen planning naar het keuzesysteem en planning via de catalogus naar het keuzesysteem. Beide stromen staan op v1.7; het voorbeeld kiest de catalogus als bron en zegt waarom |
| Regelset | F6-02: als vraag opnemen of de regelset bij het keuzedeel of bij het keuzedeelaanbod hoort, en of de condities dan op verbintenisniveau liggen |

Opmerkingen: 4127071654, 4127113197, 4132316949, 4135477493, 4135513429.
Beelden: F3-05, F3-07, F3-08, F6-01, F6-02.

### W7. Scope scherper, en waar resultaten hangen

| Onderdeel | Wijziging |
|---|---|
| Aanwezigheid | F5-01: de registratie zelf valt buiten OKx. Wat blijft is het afgeleide deelnameresultaat: het aandeel bijgewoonde lesgelegenheden bij een ongetoetste onderwijseenheid, dat in het keuzesysteem keuzes vrijgeeft of beperkt |
| Toetslogistiek | F5-02: intekenen op toetsgelegenheden loopt niet via het studentkeuzesysteem. OKE heeft daar functionaliteit voor; toets- en examenlogistiek valt buiten OKx. De variant "zelf ingetekend" vervalt, de openstaande vraag bij F5-02 is hiermee beantwoord |
| Resultaatanker | F5-04: het resultaat van een toetsgelegenheid hangt aan de onderwijseenheidverbintenis, niet aan de leergelegenheidverbintenis. De plaat kent `Onderwijseenheid aanbod verbintenis` naar `Onderwijseenheid resultaat`, dus dit past |
| LMS | F4-02: het LMS krijgt de volledige opleidingsspecificatie-boom en de formatieve resultaatstructuur |
| Lesspecificatie | F4-03: de catalogus dicteert de losse les niet. De leergelegenheid komt als reeks met de te verwerken leerspecificaties; het LMS vult de lessen in. De toetsmatrijs hoort bij het toetsinstrument en gaat uit de stroom |
| Kernregistratie en volgsysteem | F4-05: als zin opnemen dat beide in de praktijk lastig te scheiden zijn, dat resultaten idealiter in dynamische structuren in het volgsysteem staan, en dat huidige studentinformatiesystemen een vaste summatieve structuur vragen om een opleiding inschrijfbaar te maken |

Opmerkingen: 4132430633, 4132524374, 4133587743, 4135220654, 4135336554, 4135436228.
Beelden: F4-02, F4-03, F4-05, F5-01, F5-02, F5-04.

### W8. Fase 7 herschreven

| Onderdeel | Wijziging |
|---|---|
| Aanleiding | F7-01: gemiste BPV-weken vervalt. Jochem heeft een groot deel van periode 4 niet kunnen bijwonen en de bijbehorende toetsen niet voldoende afgerond |
| Titel | F7-02: het gaat om annulering van een onderwijseenheid-aanbodverbintenis. Dat komt in de titel, want annuleren heeft per niveau een andere impact |
| Groep | F7-03: groepen die in de kernregistratie ontstaan zijn per definitie plaatsingsgroepen. De achterlopers komen in een nieuwe plaatsingsgroep |
| Bron | F7-04: de planner haalt het aanbod bij de catalogus op, of dat nu het nominale pad van periode 5 is of een maatwerkprogramma met gelegenheden uit periode 4, 5 en 6 |
| Teruglevering | F7-05: als vraag opnemen of maatwerkaanbod voor een specifieke groep achterblijvers naar de catalogus terug hoort |

Opmerkingen: 4135583766, 4136024899, 4136069131, 4136135243, 4136165350.
Beelden: F7-01, F7-02, F7-03, F7-04, F7-05.

## Vragen die hieruit volgen

Het document toont maximaal zeven vragen en er staan er al 30 in de regeltabel. De nieuwe vragen vragen dus een keuze: welke zeven gaan mee naar de kerngroep van 30 september, en welke worden een issue in meta.

| Vraag | Herkomst |
|---|---|
| Heeft de specificatiekant een container nodig voor het inhoudelijk clusteren van leeronderdelen, een gewenste leergelegenheid? | W1 |
| Hoort de keuzedeelruimte in de summatieve resultaatstructuur, zoals het logisch gegevensmodel al aanneemt? | W4 |
| Mist de hoofdplaat een stroom van het studentvolgsysteem naar het studentkeuzesysteem voor behaalde leeruitkomsten? | W6 |
| Valt aanwezigheid binnen de uitwisseling, of alleen het afgeleide deelnameresultaat? | W7 |
| Hoort de toetsmatrijs op de conceptplaat bij de toets in plaats van bij de les, en blijft zij buiten de catalogus? | W7 |
| Hoort de keuzeregelset bij het keuzedeel of bij het keuzedeelaanbod, en waar liggen de condities dan? | W6 |
| Gaat maatwerkaanbod voor een groep achterblijvers terug naar de catalogus? | W8 |

## Volgorde

W1 eerst, want de naamgeving raakt 18 beelden en alle latere pakketten bouwen erop. Daarna W2 en W3 samen, omdat de getallen en de capaciteitslijn elkaar raken. W4 tot en met W8 zijn onderling onafhankelijk.

| Stap | Pakket | Omvang |
|---|---|---|
| 1 | W1 verdieping ontkoppeld | 25 regels hernoemd, 18 beelden |
| 2 | W2 maatvoering en W3 capaciteit | scenario 1.1 plus 8 beelden |
| 3 | W4 toets en examen | 6 beelden |
| 4 | W5 rollen | 3 beelden |
| 5 | W6 keuze | 5 beelden |
| 6 | W7 scope en resultaten | 6 beelden |
| 7 | W8 fase 7 | 5 beelden |
| 8 | Vragen kiezen en de rest als issue wegzetten | 7 vragen |

## Uitvoeren

Alle wijzigingen gaan in `architecture/model/informatiemodel/voorbeeld-lr1-regels.json` en in `scenario-1.1-regulier-happyflow.md`. De rest is gegenereerd. Na elke stap:

```bash
python3 scripts/controleer-voorbeeldregels.py     # 0 bevindingen, anders eerst herstellen
python3 scripts/teken-voorbeeldregels.py
python3 scripts/genereer-voorbeeld-lr1.py         # waarschuwt voor vragen buiten de zeven
python3 -m unittest
python3 scripts/validate-docs.py architecture/model/informatiemodel/voorbeeld-leerroute-1-jochem.md
```

Het ArchiMate-model blijft onaangeraakt. De zes vragen raken de plaat, maar het voorbeeld past zich aan de plaat aan en niet andersom.

## Wat hier niet in zit

De modelwijzigingen zelf. Als de kerngroep de gewenste leergelegenheid, de keuzedeelruimte in de resultaatstructuur of de stroom naar het studentkeuzesysteem overneemt, volgt dat in een eigen modelronde met een eigen issue.
