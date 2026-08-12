# Plan: leerroute-uitwerkingen verder herstructureren en de scenario's verbinden met de requirementsboom

Relateert aan: #143. Bron: overleg Niek-Niels van Duin, 12 augustus 2026 (Jamie-transcript, tijdstempels in mm:ss). Kader: het refactorplan van #137 en de requirementsboom van #130.

## Probleem

Drie samenhangende problemen uit het overleg van 12 augustus:

1. **Het hoofddocument draagt nog meer dan één doel.** Naast de leerroute-uitwerking zelf staan er de OKx-context (§1-2) en de AMIGO-uitleg in; Pull request (PR) 140 is daarmee volgens Niek nog niet reviewklaar (36:39-38:56). De scenario-opdeling per document en de versoepeling van de 1-ouder-regel uit datzelfde gesprek (38:10, 43:45) zijn op 12 augustus al gerealiseerd; het opknippen van de context is het restant.
2. **De relatie tussen scenario's en stories is niet vastgelegd.** Stories komen "één op één uit de leerroute-uitwerking" (43:21), maar geen document legt vast welk scenario welke story verantwoordt. Niels wil in de scenario's coderingen die per story verantwoorden waarom hij bestaat (42:26-43:21); Werner heeft per processtap data-eisen nodig als basis voor testkits (58:42-1:00:33).
3. **De gewenste businessmapping wijkt af van de boomvolgorde.** Niek beschrijft tweemaal de lijn opdracht, epic, story, feature, koppeling of endpoint (17:14, 43:21): de story komt uit het scenario en de feature is de koppelvlakeis daaronder. De boom hanteert nu opdracht, epic, feature, story. Dit vraagt een expliciet besluit, geen stilzwijgende aanpassing.

## Aanpak

Vijf werkpakketten, in volgorde:

1. **WP1, hoofddocument opknippen (branch 137, rondt #137 af).** §1-2 ("Wat is OKx", deliverable-keten) vervangen door een korte verwijzing naar `doc/OKx_Projectoverzicht.md`; de AMIGO-passages naar een eigen document of een verwijzing naar de [architectuurprincipes (OKx-AP03)](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md) en de [amigo-aanpak-skill](../../../.agents/skills/amigo-aanpak/SKILL.md); het hoofddocument houdt inleiding, leerroutes en delta's. Daarmee is PR 140 wél reviewklaar.
2. **WP2, beslispunt id-conventie (stopmoment, #143).** De laagvolgorde is op 12 augustus door Niek besloten: de boom houdt opdracht, epic, feature, story; de story blijft de actorzin ("als student, instelling of rol wil ik ... kunnen, met als doel dat ...") en komt uit de leerroute-uitwerkingen en de scenario's daarbinnen (happyflow en de veelvoorkomende unhappy flows); de knip tussen business en techniek wordt in de leeswijzer vastgelegd (business leest tot en met de stories, techniek vanaf de koppelingen). Resteert de id-conventie: het overleg schetst letterprefixen U, R, E, F en S met gelaagde nummering (41:40-42:24), terwijl PR 136 een soort-nummer-patroon voorstelt (bijvoorbeeld `eis-001`); dat verschil moet beslecht. Besluit door Niek, met Niels.
3. **WP3, scenario-story-verantwoording (#143, na het WP2-besluit).** Elk scenariodocument krijgt een sectie "Verantwoordt" met de story-id's die eruit volgen; elke story in de boom krijgt het scenario als bron of nevenbron (keteninfrastructuur-stories zoals S1.1 houden hun harde bron en krijgen het scenario als nevenbron). De kolom "Raakt ook" draagt de meervoudige relaties; de harde eis blijft herleidbaarheid naar minimaal één epic (43:45-44:08). De verantwoording werkt in twee richtingen als toetsinstrument: stories zonder scenario signaleren een ontbrekend scenario, scenario's zonder stories signaleren een gat in de boom.
4. **WP4, data-eisen per processtap (leerroute 1; vervolgissue, nog aan te maken).** Scenario 1.1 uitbreiden met per processtap (oriëntatie tot en met aanmelding) een in- en uitgaande-datatabel, als opstap naar de testkits van de adoptieadviseurs en de latere testsuite tegen de endpoints (58:42-1:00:33). Sjabloonuitbreiding vastleggen in de scenario-README. De datatabellen verwijzen naar de payload-specificaties in Public; zolang PR 9 daar niet gemerged is, verwijzen ze naar de branchversie.
5. **WP5, leerroutes 2, 3, 4 en 7 (met Niels; vervolgissues per leerroute).** De pitch-scenario's van leerroute 2 en 3 uitwerken volgens het sjabloon, daarna leerroute 4 en 7 als nieuwe delta's ten opzichte van leerroute 1 (34:57-35:15). Niels voert de regie op de businesslaag en het begrippenkader (15:23-16:35, 17:51-18:12); de agent levert concepten en de gates, en toetst begrippenkader-taal tegen de ankertabel.

Planning: WP1 en het WP2-beslisdocument op 13 augustus, zodat PR 140 reviewklaar is ruim vóór release 0.3 van woensdag 19 augustus richting de kerngroep techniek (26:16-28:20); WP3 direct na het WP2-besluit; WP4 en WP5 daarna, in het tempo van Niels' reviews (vrijdag: Public PR 6, meta PR 131 en PR 140).

## Buiten scope

Het memo over kerntaken en werkprocessen tegenover leeruitkomsten (intentie, expliciet geen prioriteit; 15:23-15:38), de koppeling met het ArchiMate-model (open vraag uit het overleg), en de endpoint-specificaties zelf (Public, Garik). Al het overige valt buiten scope.

## Verificatie

- WP1: het hoofddocument bevat geen OKx-introductie of AMIGO-uitleg meer; `validate-docs.py` schoon; beide reviewgates GESLAAGD.
- WP2: het laagvolgorde-besluit van 12 augustus is in dit plan vastgelegd; het id-conventiebesluit volgt in het beslisdocument of als architectuurbesluit (ADR), vóór enige hernummering van de boom.
- WP3: elke uitgewerkte story is vanuit minstens één "Verantwoordt"-sectie bereikbaar én wijst in zijn bron- of "Raakt ook"-kolom terug naar minstens één scenario; beide richtingen mechanisch telbaar, veel-op-veel toegestaan.
- WP4: per processtap van scenario 1.1 een gevulde in- en uitgaande-datatabel, herleidbaar naar de payload-specificaties in Public.
- WP5: per leerroute een uitgewerkt ankerscenario volgens het sjabloon, met delta-verwijzing naar leerroute 1.

## Status voor volgende sessie

Plan opgesteld en tegengelezen; wacht op review door Niek (#143). Eerste stap bij oppakken: WP1 uitvoeren en het WP2-beslisdocument (id-conventie; de laagvolgorde is al besloten) voorleggen; na het besluit volgt WP3, de scenario-story-verantwoording.
