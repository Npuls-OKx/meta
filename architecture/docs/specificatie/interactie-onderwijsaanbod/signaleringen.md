# Signaleringen en openstaande punten

Achtentwintig signaleringen vragen een besluit voordat een eenheid vastligt. Elke rij zegt wat er is aangetroffen en welk besluit dat vraagt; de eenheid waar zij valt staat in de [interactiespecificatie](README.md).

| Nr | Signalering | Besluit |
|---|---|---|
| S1 | De beeldregels citeren het kaderscenario in Public, de stories staan in [leerroute-uitwerking-lr1.md](../leerroute-uitwerking/doc/leerroute-uitwerking-lr1.md) | welk bestand normatief is |
| S2 | IS-OA-05 heet OC-KRS in de beeldregels en OC-SIS op v1.7; het [interactiepatroon](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md) vat KRS en studentvolgsysteem samen, en hetzelfde pijl-id draagt de stroom naar CAMBO | een naam en een pijl per koppeling |
| S3 | IS-OA-06 loopt via de kernregistratie naar AII op gezag van de sectorarchitect, v1.7 ontsluit rechtstreeks aan CAMBO | richting, component en naam |
| S5 | De stroomregels van IS-OA-01 en IS-OA-02 dragen geen koppeling-ID: op v1.7 valt het ontwerpen binnen de catalogus | een eigen lijn op de plaat |
| S6 | 79 van de 145 regels dragen een aanname, bij F1-13 alle 11; 26 objecttypen komen van de conceptplaat en 13 van de 33 missen een definitie | de grond per eenheid zichtbaar maken |
| S7 | B01 tot en met B10 staan open (issues 283 en 284): de clustering, de keuzedeelruimte in de resultaatstructuur, exacte geplande capaciteit | de bevindingen wegen voor een eenheid vastligt |
| S8 | Fase 1 en 2 dragen procesketen 6 en 4; informeren, aanmelden, intake en plaatsen valt onder keten 5 | de ketentoewijzing van fase 3 |
| S9 | [U5](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u5-bericht-versus-kanaal) laat het afleveringsmechanisme bij de partijen, `subscription.json` dekt de OC-P&R-events, en OC-SIS kent nog geen interactie voor een afleveradres | het afleveradres per koppeling |
| S10 | Story-0007, story-0022 en story-0023 staan op de onderwijsontwikkelaar, het voorbeeld noemt de planner | de actor per story |
| S11 | 7 van de 24 stromen op v1.7 dragen een koppelingspecificatie, de aangehaalde [ADR's](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr) staan op Voorstel en elk schema in Public op alfa | wanneer een stand van voorstel naar vastgelegd gaat |
| S12 | De dienstenlijst staat op commit d0c20d99 van `feature/restructure-and-versioning`, de enige plek waar `Applicatiediensten/` vandaag leeft | welke branch normatief is |
| S13 | IS-OA-01 levert het ontwerp met POST, IS-OA-02 meldt gereed en laat de catalogus ophalen | een aanleverpatroon van ontwerptool naar catalogus |
| S14 | De dienstenlijst schrijft `specificatie-beschikbaar` en `verwerkingsuitkomst`, de componentpagina's `specificatie-planbaar` en `verwerkingsstatus`; dezelfde statusmelding heet `aanbod-aanmeldbaar` bij IS-OA-05 en `aanmeldbaar-aanbod-beschikbaar` bij IS-OA-06 | een naam per bericht |
| S15 | Interactie I3 valt uiteen: ontvangen, gestart en afgekeurd bij IS-OA-03, gelukt en nietGelukt bij IS-OA-04 | de knip bevestigen |
| S16 | De schema's en [mapping.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/mapping.md) dragen Engelse veldnamen met de Nederlandse naam ernaast, [voorbeeldpayloads.md](https://github.com/Npuls-OKx/Public/blob/dev/Informatie-en-gegevensmodellen/voorbeeldpayloads.md) en [U7](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie) Nederlandse sleutels; deze snede volgt de schema's, zodat elke payload valideert | een sleuteltaal, op een plek |
| S17 | De uitkomst van de inname landt in `processing-status.json` met `deliveryId` en `findings` erbij, of in [intake-outcome.json](schemas/intake-outcome.json) ernaast; het voorstel vraagt `specificationReference` alleen op `gelukt`, waar dat schema hem altijd verplicht | welke landing, en of die versoepeling daar mag (MAJOR) |
| S18 | Twee gesloten lijsten vragen een waarde erbij: `events` in `subscription.json` voor de nieuwe meldingssoorten, en `status` in `education-offering.json` voor `aanmeldbaar` | of die lijsten open gaan; elke waarde erbij is MAJOR voor wie erop valideert |
| S19 | Verwijzingen zonder onderwerp in het informatiemodel: de inrichting achter `arrangementReference`, `Plaatsingsgroep` op de aanbodlaag, het toetsinstrument, de leermiddelgroep, de resultaateenheidspecificatie en de publicatie bij centraal aanmelden | het objecttype per verwijzing |
| S20 | De inhoud van IS-OA-06 staat als V1 tot en met V10 in [Public#112](https://github.com/Npuls-OKx/Public/issues/112), van de aanbodlagen en het aanmeldvenster tot de terugmelding en het locatieniveau | per regel een antwoord van AII |
| S21 | Het lichaam bij een foutcode draagt drie vormen: op de inname [intake-rejection.json](schemas/intake-rejection.json), op de opvragingen een eigen foutschema dat W15 van [IS-OA-03](is-oa-03.md#5-werkbrieven-de-issueset-die-hieruit-volgt) vraagt, en op `/aanmeldbaar-aanbod` en `/abonnementen` de HTTP-code zonder lichaam. De codelijst van de innamebevinding dekt de gronden van een opvraag niet | een foutvorm over de opvragingen, of de HTTP-code als enige grond |
| S22 | De lijstopvraag `/onderwijsspecificaties` antwoordt met een array zonder omhulling, waarin een vervolgverwijzing en een totaal geen plek hebben; paginering uit W14 van [IS-OA-03](is-oa-03.md#5-werkbrieven-de-issueset-die-hieruit-volgt) komt daarmee op een omhullend object uit | de omhulling nu, of bij de paginering en dan MAJOR |
| S23 | De groep RIO/CAMBO/AII op hoofdplaat v1.7 draagt vier vakken: het aanmeldsysteem, RIO, de voorziening voor centraal aanmelden (CAMBO) en een commerciele of LLO-oplossing. AII heeft er geen eigen vak, en CAMBO draagt de stroom van IS-OA-06 | een eigen vak voor AII in die groep, naast S3 over de richting en de naam |
| S24 | De groep Student Informatie Systeem draagt naast de kernregistratie en het studentvolgsysteem ook het studentbegeleidingsysteem; de markering omlijnt alle drie, want zij staan in dezelfde groep | of elk vak in die groep het aanmeldbare aanbod afneemt |
| S25 | De resultaatstructuur naar het studentvolgsysteem (F4-04, koppeling OC-SVS, interactie S3) is dezelfde publicatiehandeling als IS-OA-03, IS-OA-05 en IS-OA-07, en staat nog niet als eigen interactiespecificatie in deze keten | of die stroom erbij komt als IS-OA-08 |
| S26 | De dienst [onderwijsspecificatie-inname](https://github.com/Npuls-OKx/Public/blob/d0c20d99b110b29ccf6b0e50109f7d54ffd88d7a/Koppelvlakspecificaties/Applicatiediensten/onderwijsspecificatie-inname-aanbieder.md) heet naar de handeling, de dertien andere diensten naar het gegeven dat beweegt. Zij is bovendien de enige inkomende dienst, waardoor de aanbieder hier ontvangt in plaats van levert; de dienstenlijst zegt dat zelf. Wie het endpoint implementeert verschilt per patroon: bij ophalen de aanbieder, bij melden de afnemer, bij aanleveren de aanbieder terwijl het gegeven de andere kant op gaat | een naamregel voor een inkomende dienst, en of `onderwijsspecificatielevering` haar beter dekt, met `/leveringen/{leveringId}` als de resource die de catalogus bezit |
| S27 | De diensten `aanmeldbaar-onderwijsaanbod-aanbieder` en `-afnemer` staan niet in de dienstenlijst; IS-OA-05 en IS-OA-06 claimen ze wel, en werkbrief W9 belegt ze. De twaalf andere diensten van deze keten staan er wel | of dit paar erbij komt, of dat het aanmeldbare aanbod onder `planbaar-onderwijsaanbod` valt |
| S28 | De resource `/examenplanspecificaties` draagt [result-structure.json](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema's/result-structure.json), dus een resultaatstructuur. De [begrippenlijst](../begrippen/begrippenlijst.md) rekent `Resultaatstructuur` tot de zeven families en zet `Examenplan` daarbuiten; het informatiemodel kent beide als eigen objecttype, waarbij het examenplan een summatieve resultaatstructuur kent | of de resource `/resultaatstructuren` gaat heten, en wat er dan met het examenplan als eigen objecttype gebeurt |

S4, waar de dienst voor aanmeldbaar aanbod hoort, is beslecht: de catalogus krijgt de eigen resource `/aanmeldbaar-aanbod`, en `/onderwijsaanbod` blijft bij het planningssysteem.

Open beeldvragen: het generieke basisdeel (F1-09), de keuzedeelruimte in de summatieve resultaatstructuur (F1-12), en de container voor geclusterde leeronderdelen, met de vraag of het onderwijsontwerp daar landt of bij het leeronderdeel (F1-06, F2-01).

Verder open:

| Punt | Stand |
|---|---|
| De fase-2 update van de ontwerptool, de route naar het intakesysteem vanaf F3-04, en de stories van roosteraar en student | volgen elk als eigen snede |
| `Onderwijsvorm`, `Onderwijslocatie type`, `Onderwijslocatie` en `Organisatie-eenheid` staan in F1-06 nog onder hun conceptplaat-naam | de namen gelijktrekken |
| Het versieformaat: `2026.1` in de voorbeelduitwerking naast het patroon `n.n.n` van de schema's | een aanduiding per specificatie |
| De bewaartermijn van een afgehandelde levering, en of een lijstopvraag op `/leveringen` erbij hoort | W17 van IS-OA-01 |
| Het aanmeldvenster en de uiterste inschrijfdatum staan nog niet in [casus.md](casus.md), terwijl IS-OA-05 en IS-OA-06 dezelfde waarden dragen | een regel daar houdt beide eenheden gelijk |
| [offering-open-for-application.json](schemas/offering-open-for-application.json) sluit zijn objecten om de snede uit te drukken | of het profiel open gaat voor latere velden |
| Elke verdieping nummert haar operaties en haar werkbrieven zelf: O1, I1, C1, W1 en WB-01 beginnen elk een reeks | een nummering over de stromen |
| `Competenties / skills` naast `Competenties / Skills`, `Schaartste van mensen` (F2-05), `Opleiding aanbod` naast `Opleidingaanbod` | blokkeren een kruiscontrole op naam |
