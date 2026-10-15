# Casus: Jochem kiest een keuzedeel

De werkcasus onder de koppelvlakspecificatie voor keuzedelen kiesbaar maken. Leerroute 1, regulier, persona Jochem. Relateert aan: #359.

Alles in deze casus komt uit een bron in deze repository. Waar een gegeven ontbreekt staat dat erbij als uitvraag, zodat een lezer ziet wat vaststaat en wat nog niet.

## De opleiding

| | | Bron |
|---|---|---|
| Kwalificatiedossier | Apothekersassistent, crebo 23450 | [dossier](../../kwalificatiedossier/Apothekersassistent-2.md) |
| Kwalificatie | Apothekersassistent, crebo 27141, niveau 4 | idem |
| Domein | Zorg en welzijn, crebo 79140 | idem |
| Geldig vanaf | 1 augustus 2026 | idem |
| Keuzedeelruimte | 720 SBU, te vullen in de loop van de opleiding | [leerroute-uitwerking](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#L295) |

## De drie keuzedelen

Twee staan als dossier in deze repository, de derde komt uit de leerroute-uitwerking.

| Code | Titel | SBU | Aard | Bron |
|---|---|---|---|---|
| K0037 | Farmaceutische Patientenzorg | 480 | Verdiepend | [dossier](../../kwalificatiedossier/K0037-farmaceutische-patientenzorg.md) |
| K0262 | ARBO, kwaliteitszorg en hulpverlening niveau 3 | 240 | Generiek | [dossier](../../kwalificatiedossier/K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md) |
| K0023 | Digitale vaardigheden gevorderd | 240 | Generiek, met certificaat | [dossier](../../kwalificatiedossier/K0023-digitale-vaardigheden-gevorderd.md) |

Hun kerntaken, waarmee zij aan leeruitkomsten hangen:

| Keuzedeel | Kerntaak | Werkproces |
|---|---|---|
| K0037 | D1-K1 Voert farmaceutische patientenzorg uit | W1 Zorgt voor een medicatieoverzicht |
| | | W2 Biedt farmaceutische patientenzorg aan specifieke doelgroepen |
| K0262 | D1-K1 Draagt bij aan kwaliteitszorg en arbeidsomstandigheden | W1 Levert een bijdrage aan de inrichting van het kwaliteitszorgsysteem |
| | | W2 Voert een risico-inventarisatie en -evaluatie uit |
| K0262 | D1-K2 Verleent EHBO en BHV | W1 Verleent hulp bij calamiteiten |
| K0023 | D1-K1 Verzamelt informatie, gegevens en content | W1 Wint digitale informatie in |
| K0023 | D1-K2 Produceert informatie en content | W1 tot en met W3 |
| K0023 | D1-K3 Beheert informatie en content | W1 tot en met W3 |

## Waarom er iets te kiezen valt

De ruimte is 720 SBU. Met drie keuzedelen van 480, 240 en 240 ontstaan twee geldige vullingen en een die tekortschiet.

```
ruimte 720 SBU

  K0037  480  +  K0262  240   =  720   geldig
  K0037  480  +  K0023  240   =  720   geldig
  K0262  240  +  K0023  240   =  480   240 SBU tekort
```

Zonder de derde is de ruimte met K0037 en K0262 precies vol en valt er niets te kiezen. De derde maakt de kiesbaarheid aantoonbaar: er is een combinatie die een regel moet afwijzen.

## Wat de instelling doet en wat Jochem ziet

| | De instelling | Jochem |
|---|---|---|
| Vooraf | Stelt vast welke keuzedelen in het assortiment zitten | Ziet niets; het aanbod is nog niet ontsloten |
| Voorsorteren | Beperkt tot wat past bij leerroute, keuzedeelruimte, aard, domein en locatie | Krijgt een lijst die hij kan overzien |
| Aanbod plannen | Zet per keuzedeel een periode, een locatie en een aantal plaatsen | Ziet wanneer en waar het draait |
| Regels vastleggen | Legt vast hoeveel SBU gevuld moet worden en welke combinaties mogen | Ziet wat kiesbaar is, en bij afwijzing waarom |
| Kiezen | Ontvangt een geprioriteerde voorkeurslijst | Zet zijn voorkeuren op volgorde |

De instellingskant staat in de instellingsjourney van [persona Jochem](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md); de studentkant in [de leerroute-uitwerking](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md#L272), waar zijn voorkeurslijst met periode en locatie als vignet staat.

## Waarom hiervoor een koppelvlakstandaard nodig is

De voorsortering ontstaat bij de ene partij en moet bij de andere tot een lijst leiden. Dat is de kern.

```
onderwijscatalogus                          studentkeuzesysteem
  kent de specificaties                       kent de student
  kent het aanbod met periode en locatie      toont wat kiesbaar is
  kent de regels                              zegt waarom iets afvalt
        \                                    /
         de regel gaat over de lijn, niet de uitkomst
```

Wie de uitkomst verstuurt, verstuurt een lijst per student en moet die bij elke wijziging opnieuw bepalen. Wie de **regel** verstuurt, laat de ontvanger de lijst afleiden en kan dezelfde regel aan de planner geven. Dat is wat een standaard hier oplevert en waarom het om meer gaat dan een exportbestand.

## Wat er dan over de lijn moet

Afgeleid uit de casus, op het niveau van informatieobjecten en nog zonder berichtvorm.

| Wat | Waarom het nodig is | Uit de casus |
|---|---|---|
| De specificatie van de keuzedeelruimte | Zonder ruimte is er geen opgave | 720 SBU |
| De kiesbare specificaties | De voorsortering zelf | K0037, K0262, K0023 |
| Hun studielast | De ruimte moet vol | 480, 240, 240 |
| Hun aard | Een regel kan op aard selecteren | verdiepend, generiek |
| Het aanbod met periode en locatie | Anders is haalbaarheid niet te bepalen | uitvraag |
| De regelset | De ontvanger leidt de lijst af | zie de specificatie |
| De reden bij niet-kiesbaar | Jochem moet weten waarom iets afvalt | zie de specificatie |

## Wat deze casus nog niet draagt

| Ontbreekt | Gevolg | Hoe te vullen |
|---|---|---|
| Periode en locatie per keuzedeelaanbod | De beschikbaarheidsregel is niet te demonstreren | Uitvraag bij een instelling |
| Het aantal plaatsen per aanbod | Een capaciteitsregel is niet te demonstreren | Uitvraag |
| Het volledige assortiment | De voorsortering is niet te meten | Uitvraag |

Deze drie zijn de uitvraag aan instellingen die de businesscase ook nodig heeft.

## Verwijzingen

| Bron | Wat het levert |
|---|---|
| [Leerroute-uitwerking leerroute 1](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) | De keuzedeelruimte, de voorkeurslijst, het keuzemoment en de signalering bij een lege ruimte |
| [Kwalificatiedossier apothekersassistent](../../kwalificatiedossier/Apothekersassistent-2.md) | Crebo, niveau, domein en geldigheid |
| [K0037](../../kwalificatiedossier/K0037-farmaceutische-patientenzorg.md), [K0262](../../kwalificatiedossier/K0262-arbo-kwaliteitszorg-en-hulpverlening-niveau-3.md) en [K0023](../../kwalificatiedossier/K0023-digitale-vaardigheden-gevorderd.md) | Code, studielast, aard, certificaat, kerntaken en werkprocessen |
