# Plan: twee refactors, twee uitgangspunten en het Gate A-herstel

Relateert aan: #130, #137, #138, #139 en [Public #12](https://github.com/Npuls-OKx/Public/issues/12). Volgt uit de review van de requirementsboom op 7 augustus 2026.

Dwarsdoorsnijdend uitgangspunt voor alle werkpakketten: **eisen eerst, techniekkeuze daarna**. Een requirement wordt nooit uitgesloten omdat OEAPI of een andere technische keuze het niet toestaat; een mismatch is een signalering richting de standaard (#139).

## Werkpakketten (parallel uitvoerbaar, elk 1 issue = 1 branch = 1 PR)

### 1. Consumer-profiel wordt leerroute-uitwerking volgens AMIGO (#137)

- **Wat**: hernoemen en herpositioneren van het document en de map `okx-oeapi-consumer-profiel`; het is een gedetailleerde leerroute-uitwerking volgens de AMIGO-aanpak (begrippen, actoren, scenario's, systemen, informatie, data, interacties via informatiestromen), basis voor technische specificatie. LR1 is uitgewerkt; LR2/3 volgen als delta, en die volgorde mag nergens als "geen requirements op LR2/3" gelezen worden. Opknippen waar een bestand meer dan één doel draagt.
- **Hangt af van**: refactorplan (design first) op de eigen branch; #139 voor de naamgevingsrichting.
- **Levert op**: hernoemde structuur, bijgewerkte verwijzingen (requirementsboom, leeswijzer, skills, AGENTS.md), validate-docs schoon.
- **Sluit uit**: inhoudelijke wijziging van scenario's of begrippen; dat is regulier onderhoud.

### 2. Leeruitkomst als verbindende sleutel (#138)

- **Wat**: de term "opaque sleutel" vervangen door een begrijpelijke naam; werkrichting "verbindende sleutel", de sleutel die specificaties, keuzeregels, planning, resultaten en waardepapieren verbindt. De technische eigenschap (inhoud hoeft niet gekend) wordt toelichting, niet naam.
- **Hangt af van**: terminologiebesluit samen met de semantiekbewaking; herziening van ADR 0023 in Public.
- **Levert op**: doorgevoerde term in ADR 0023 (of opvolger), koppelingspecificatie OC-P&R, de boom-feature en het semantisch kader.
- **Sluit uit**: wijziging van de werking zelf (id's en behaald-status blijven wat over de koppeling gaat).

### 3. Uitgangspunt toekomstvaste endpoints ([Public #12](https://github.com/Npuls-OKx/Public/issues/12))

- **Wat**: vastleggen dat OKx endpoints definieert die ook toekomstige scenario's mogelijk maken, en daarom de volledige structuur én de delta ontsluit zodat implementaties zelf kiezen.
- **Hangt af van**: niets; de koppelingspecificatie OC-P&R doet dit al, het uitgangspunt ontbreekt.
- **Levert op**: nieuw uitgangspunt in `Koppelvlakspecificaties/uitgangspunten.md` plus verwijzingen vanuit de koppelingspecificaties.
- **Sluit uit**: endpointontwerp zelf (loopt in Public PR 9).

### 4. Principe: eisen formuleren vóór techniekkeuze (#139)

- **Wat**: kernprincipe 2 herformuleren in `architecture/docs/principes.md` en `AGENTS.md`: eerst wensen en eisen, daarna de vertaling naar OEAPI of een andere techniek; OEAPI past zich naar verwachting aan onze eisen aan. Geen requirement uitsluiten om technische redenen. Mbo-focus met aansluiting op hbo en wo (niet in de weg zitten) hoort bij dezelfde herijking.
- **Hangt af van**: vaststelling door het kernteam; daarna ADR-concept in Public.
- **Levert op**: herzien principe, aangepaste verwerpingsregels voor extracties en reviews.
- **Sluit uit**: het terugdraaien van bestaande OEAPI-mappingwerk; dat blijft bruikbaar als vertaling.

### 5. Gate A-herstel in de requirementsboom (deze branch, #130)

- **Wat**: de Gate A-verworpen kandidaten herstellen met correcte bronnen; de verwerping was steeds een bronprobleem of een techniek-gedreven redenering, niet een inhoudelijk oordeel. Kandidaat 4 (volledige structuur bij wijziging) blijft terecht verworpen zoals geformuleerd; de onderliggende keuze wordt werkpakket 3.
- **Herstellijst**: (1) tempoflexibiliteit via de verbintenistoestand, herformuleren conform scenario 1.4 en 3.2; (2) wisselen tussen nominale route en maatwerk, met ADR 0012 als enige bron; (3) individuele structuur in het studentinformatiesysteem inclusief examenplan-symmetrie, met beide besluitpunten als bron; (5) request for offering is nodig en belangrijk, opnemen als eis met de OEAPI-mismatch als signalering, niet als blokkade; (6) mbo-focus met aansluiting op hbo en wo als requirement op de opdracht- of epiclaag; (7) herformuleren tot het principe uit werkpakket 4.
- **Ook**: parkeerlijst-items die alleen vanwege LR1-blik zijn blijven liggen (persona Larissa en Linda, tempo-varianten) heroverwegen bij de volgende boomuitbreiding.
- **Hangt af van**: werkpakket 4 voor de formulering van (7); de rest kan direct.
- **Levert op**: bijgewerkte boom met hernieuwde Gate C-toets (product-flow).
- **Sluit uit**: nieuwe extractieronde; dit is herstel, geen uitbreiding.

## Volgorde

Werkpakketten 1 tot en met 4 parallel op eigen branches (issues en concept-PR's staan open); werkpakket 5 op deze branch na of naast de merge van PR 131, met (7) wachtend op de vaststelling van #139.
