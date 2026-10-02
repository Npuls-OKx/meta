## Testrapport, tweede ronde (versie 2 van het featureplan)

Voorcontrole: geslaagd (`validate-docs.py` op feature-plans en de research-map: 17 bestanden, 0 problemen). Toets beperkt tot de verwerking van bevinding 1 tot 10 uit `tegenlezing-plan-tester.md` en nieuwe eisen die niet toetsbaar zijn.

| Bevinding v1 | Oordeel | Bewijs |
|---|---|---|
| 1 Basis niet genoemd (blokkerend) | verwerkt | Sectie 4 opent met de basis (branch 89, PR 225) en een keuze A of B voor 18 september; feature 1 hangt ervan af; het publiceerscript staat feitelijk alleen op branch 232, wat feature 7 apart afdekt |
| 2 R1 schema: velden, lege regel, aanname-objecttype | verwerkt | R1 noemt soort, van en naar, toestand, bron en zin; "geen pijl op de hoofdplaat" is een geldige lege regel (sectie 2, R1); een objecttype buiten de plaat wordt geweigerd, een aanname geldt alleen voor de instantie |
| 3 R1 relatielabels | verwerkt | Controle op het drietal (soort, van, naar); nesting alleen op aggregatie of compositie; een relatie die de plaat niet kent wordt een vraag (sectie 2, R1, feature 4) |
| 4 R2 dekking: bron per fase, een of meer regels | verwerkt | Verwachting per fase in de kop van de regeltabel (feature 1, 18 september); latere verschijning is soort `verandert`; dekking telt op de eerste verschijning; R2 zegt "minstens een" waar sectie 2 "een keer" zegt, de test moet precies een afdwingen |
| 5 Pijlnummers zonder bron | deels | Nummers vervallen, `stromen.json` uit v1.7 is de enige bron (sectie 2, R4a); maar (van, naar) is op v1.7 na junction-resolutie geen identiteit: Planningssysteem naar Onderwijscatalogus, Onderwijscatalogus naar LMS en Roostersysteem naar SKS komen elk twee keer voor met een andere labelexpressie |
| 6 Feature 1 leunt op feature 3 | verwerkt | Feature 3 gesplitst in 3a (export, 18 september, geen layout) en 3b (render, optioneel); feature 1 noemt 3a als afhankelijkheid op dezelfde dag |
| 7 Feature 8 zonder datum, dubbele spatie | verwerkt | Model bevroren tot na 30 september; de controle normaliseert witruimte (sectie 2, R1); de hernoeming zit in R10 en feature 8 met datum 3 oktober |
| 8 Omvang bijlage inconsistent | verwerkt | Doel 3 en R6 zeggen zes pagina's met een vaste indeling; het deck is dezelfde zes pagina's; harde grens in de risicotabel met terugval fase 4 als chips |
| 9 Doel 4 zonder eis | verwerkt | Doel 4 en R8 leggen de antwoordvorm vast (invulblad per regel, kolommen "heet bij u" en "hangt bij u onder" in R5); R8 heeft een telbaar criterium en een uitkomst als comment binnen twee werkdagen |
| 10 Doel 1 tegenover feature 4 en 5 | verwerkt | Doel 1 en R5: stub-fasen tonen chips met de verwachte objecttypen en de vaste zin "regels volgen na 30 september"; de chips komen uit de verwachting per fase van feature 1 |

Nieuwe bevindingen (alleen moet):

- **Moet, R1 en R4a (vervolg op 5).** Maak de pijlidentiteit uniek: (van, naar, labelexpressie) of de relatie-id uit Archi als derde onderdeel, anders is de stroomt-controle voor drie pijlparen niet eenduidig en R4a ("precies een regel per flow") niet herleidbaar naar de regeltabel.
- **Moet, R4a en R4b.** R4a noemt de view "OKx hoofdplaat v1.7<concept>" (67 elementen, 66 connecties, 33 flows), R4b zegt "dezelfde view" maar telt 49 en 43, de aantallen van de view zonder context (28 flows; zeven flows over toetsing en EduHub ontbreken daar, en Planningssysteem naar Onderwijscatalogus loopt er via een junction). Kies een view voor `stromen.json` en de render, of noem beide met eigen aantallen.

Geen nieuwe niet-toetsbare eisen: R3, R5, R6, R7, R8 en R11 hebben elk een telbaar of waarneembaar criterium; de knikpuntformule in R4b (gemiddelde van bron- en doeloffset) klopt met de bendpoints in het model.

Eindoordeel: GESLAAGD. De blokkerende bevinding en de moet-punten 2 tot 10 zijn verwerkt; de twee resterende moet-punten zijn correcties van een zin in R1 en R4a/R4b, houden de uitvoering en het doel van 30 september niet tegen, en horen in de tekst van sub-issues 1 en 3a voordat het werk op 18 september start.
