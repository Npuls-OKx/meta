---
name: okx-requirements-boom
description: >-
  Vaste opbouw en conventies voor de OKx-requirementsboom: de gelaagde
  breakdown van opdracht naar epics, features en stories die de businesslaag
  aan de techniek verbindt. Bevat de laagdefinities, de tabelformats per laag,
  de bronplicht met bronhierarchie, de aansluiting van stories op
  koppelingspecificaties en endpoint-sets, de omvangslimieten en de
  reviewerchecklist. Gebruik bij het schrijven, uitbreiden of reviewen van
  documenten onder architecture/docs/requirements/.
---

# De OKx-requirementsboom

De boom is de getoonde koppeling tussen business en techniek: van de opdracht (Leren zonder Drempels) via epics en features naar stories, en van stories naar de interacties en endpoint-sets in de koppelingspecificaties. Achterliggende mechaniek (eis-ID's, uitvoerbare scenario's) staat niet in de boom; zie het architectuurbesluit bij issue #130 en de ID-conventie bij issue #135.

Twee leidende regels, uit de sparsessie van 5 augustus 2026 (issue #130):

1. **Overzicht boven volledigheid.** Liever iets minder informatie met overzicht dan volledigheid zonder overzicht. Wat niet past gaat naar de parkeerlijst, niet in een extra laag of voetnoot.
2. **Eén document per laag**, met een overkoepelende index. Geen document per requirement.

## De vier lagen

| Laag | Wat het is | Voorbeeld |
|---|---|---|
| Opdracht | Waarom OKx bestaat: de maatschappelijke opdracht en de projectdoelen | "Lerenden krijgen meer regie over hun eigen leer- en ontwikkelroute zonder (administratieve) drempels" |
| Epic | Een bekwaamheid van de keten, als actorzin | "Student kiest onderwijsspecificaties" |
| Feature | Een afgebakend stuk gedrag binnen een epic | "Kiesbaarheid bepalen: welke onderwijsspecificaties mag deze student kiezen" |
| Story | Eén toetsbare wens van één actor, in één zin | "Als planner wil ik de voorwaarden bij een keuzedeel kennen zodat ik het na de vereiste leeruitkomst kan plannen" |

Geen tussenlagen, geen sublagen. Een story die niet onder een feature past wijst op een ontbrekende feature of hoort op de parkeerlijst.

## Bestanden en omvangslimieten

Alles staat in `architecture/docs/requirements/`. De limieten zijn hard; overschrijding betekent samenvoegen of parkeren, nooit de bronkolom schrappen.

| Bestand | Inhoud | Limiet |
|---|---|---|
| `README.md` | Index: doel, mermaid-boom, lagenplaat (opdracht tot endpoint), navigatietabel, conventies, scope | 120 regels, mermaid 15 knopen per plaat |
| `opdracht.md` | Opdracht en projectdoelen (doel-0001, doel-0002, ...), tabel doel naar epics | 80 regels |
| `epics.md` | Eén tabel met alle epics | 150 regels, 8 epics |
| `features.md` | Subsectie per epic met featuretabel | 200 regels, 6 features per epic |
| `stories.md` | Stories van de uitgewerkte epics | 250 regels, 15 stories per epic |
| `leeswijzer.md` | Leesroutes naar bestaande documenten | 100 regels |

## Tabelformats

Elke laag is een tabel en elke rij draagt een id, plat per soort, voluit met vier cijfers en zonder oudernummer in het id: `doel-0001`, `epic-0001`, `feature-0001`, `story-0001` (conform de vastgestelde id-conventie, PR 136). Dat zijn verwijzings-id's voor issues, reviews en gesprekken, geen traceernotatie. De nummering volgt de boomvolgorde van boven naar onder: doelen in de vastgestelde volgorde, epics per doel, features en stories in de volgorde van hun epic (stories binnen een epic gegroepeerd per feature); een nieuwe rij krijgt het eerstvolgende vrije nummer van zijn soort, bestaande nummers schuiven nooit op. Elke node heeft precies één ouder: daar staat hij, daar telt hij mee voor de omvangslimieten en daar landt zijn issue. De boom is strikt: epics overlappen niet, en valt een feature of story inhoudelijk onder meerdere ouders, dan is die leaf te groot en wordt hij opgeknipt tot delen die elk precies één ouder hebben (besluit 13 augustus, overleg Niek-Garik). Dat het onderwijsdomein zelf N:M-relaties kent (de leeruitkomst-cardinaliteiten in het begrippenkader) verandert daar niets aan: die relaties leven in de payloads, niet in de boomstructuur. De doelzin van een epic en de omschrijving van een feature beschrijven de beoogde toestand of waarde (wat is er bereikt als dit werkt), niet de werking, en zijn maximaal 25 woorden. Planningsstatus hoort in milestones en issues, niet in de boom; een epic zonder uitwerking heeft in `features.md` een sectie met één verklarende regel in plaats van een tabel.

- **Epics**: `| Id | Epic | Doel | Draagt bij aan | Bron | Features |`. "Draagt bij aan" verwijst naar een doel (doel-id) in `opdracht.md`. "Features" is een ankerlink naar de subsectie in `features.md`.
- **Features**: `| Id | Feature | Omschrijving | Bron | Verwijzing |`, gegroepeerd per epic in een eigen subsectie (de ouder staat in de sectiekop, niet per rij; de omschrijving herhaalt het epicdoel niet). Elke rij draagt een anker om het id heen (`<a id="feature-0001"></a>feature-0001`) zodat stories er direct op linken. "Verwijzing" wijst naar een bestaand document dat de feature uitwerkt, of blijft leeg.
- **Stories**: `| Id | Story | Feature | Bron | Functionele eisen |`. De story is een actorzin ("Als ... wil ik ... zodat ..."); de featurecel is een ankerlink naar de feature — id en naam als linktekst, het feature-anker in `features.md` als doel — zo traceert een story via zijn feature terug naar de epic, een tweede ouderrelatie bestaat niet. "Functionele eisen" verwijst naar de functionele eisen in de koppelingspecificatie: het koppelingsacroniem voorop en dan de FR-nummers (bijvoorbeeld `OC-P&R FR2 en FR4`), als link naar de sectie Functionele eisen van het interactiepatroon in Npuls-OKx/Public — FR-nummers zijn per koppeling genummerd, dus zonder acroniem zijn ze ambigu. Bestaat er geen functionele eis, dan expliciet "geen".

## Bronplicht

Elke rij heeft een gevulde bronkolom. Een kandidaat zonder herleidbare bron staat op de parkeerlijst in het extractie-artifact, niet in de boom.

- Bronhierarchie bij meerdere bronnen, sterkste eerst: vastgesteld document, ADR, meetingbesluit, meetingdiscussie. Noem maximaal twee bronnen per rij.
- Repobestanden krijgen een relatieve link met sectie-anker. Documenten in `Npuls-OKx/Public` krijgen een absolute GitHub-link.
- Nog niet gemergde bronnen (een open pull request) krijgen een absolute link naar de pull request met de noot "in review". Na de merge wordt dat een gewone link; benoem die omzetting als vervolgpunt in de PR-tekst.
- Meetingbronnen verwijzen naar het verslag in `architecture/meetings/`, of naar het extractie-artifact wanneer de meeting alleen extern (Jamie) is vastgelegd.

## Aansluiting op de techniek

De boom eindigt bij specificaties, niet bij implementaties.

- De kolom Functionele eisen verbindt de boom met de koppelvlakspecificaties: een story verwijst naar de functionele eisen (FR-nummers) die zijn wens technisch dragen; de FR verwijst zelf door naar het interactiepatroon en via het interactieoverzicht naar de endpoint-sets van de applicatiecomponenten. De keten is dus story, functionele eis, interactie, endpoint-set — het spiegelbeeld van de keten-eisenlijn in de afbakening van de koppelvlakspecificaties (keten-eis, functionele eis, interactiepatroon, endpoint).
- De redenering is: wie deze featureset wil ondersteunen, wordt eigenaar van deze endpoints. Hoe een leverancier dat intern oplost valt buiten de boom.
- Endpoint-sets die nog in een open pull request staan volgen de regel voor niet-gemergde bronnen.

## Mermaid-conventies voor de indexplaat

- `flowchart LR`, geen puntkomma's (breken de GitHub-render).
- De plaat blijft leesbaar door hem met de hand klein te houden: alleen de opdracht, de doelen en de epics (met id in het label), maximaal 15 knopen. Features en stories staan alleen in de tabellen; zo heeft elke informatie-eenheid één drager.
- Geen statuskleuren of andere planningsinformatie in de plaat. Elke epicknoop staat in `epics.md` en omgekeerd; wijkt de plaat af, dan is dat een bevinding.

## Plaats in de product-flow

Deze skill is de specialist-skill voor stap 2 (uitwerken) van [`okx-product-flow`](../okx-product-flow/SKILL.md) wanneer het deliverable de requirementsboom is. Stap 1 (requirements met [`business-analyse-okx`](../business-analyse-okx/SKILL.md)) en stap 3 (onafhankelijke reviews) blijven verplicht.

## Reviewerchecklist

- [ ] Elke node heeft precies één ouder; geen laag overgeslagen (opdracht, epic, feature, story). Raakt een leaf inhoudelijk een tweede ouder, dan is hij te groot: opknippen, nooit een tweede relatie vastleggen.
- [ ] Geen twee nodes met dezelfde naam of dezelfde strekking.
- [ ] Elke rij heeft een gevulde bronkolom; links werken (`python3 scripts/validate-docs.py architecture/docs/requirements`).
- [ ] Elke story heeft in de kolom Functionele eisen een FR-verwijzing (koppelingsacroniem voorop, link naar de sectie Functionele eisen van het interactiepatroon) of expliciet "geen", en een featurecel die als ankerlink naar de feature werkt.
- [ ] Doelzinnen en feature-omschrijvingen maximaal 25 woorden en geformuleerd als beoogde toestand, niet als werking; een feature-omschrijving herhaalt het epicdoel niet.
- [ ] Elke rij draagt een id in het vaste format (`doel-0001`, `epic-0001`, `feature-0001`, `story-0001`), zonder dubbelingen en zonder oude id-vormen (E1, F2.1, S2.3); geen statuskolommen.
- [ ] Omvangslimieten gehaald (regels tellen met `wc -l`, tabelrijen en mermaid-knopen handmatig).
- [ ] Mermaid-plaat toont alleen opdracht, doelen en epics, liggend (`flowchart LR`) zodat de boom hoog wordt in plaats van breed, en is consistent met `epics.md`; geen puntkomma's.
- [ ] Geen eis-ID's of Gherkin in de boom; achtergrondmechaniek alleen via verwijzing naar het ADR.
- [ ] Nieuwe bestanden staan in de README-index van de map en van `architecture/docs/`.

Bredere schrijfstijl staat in [`docs-style`](../../../.cursor/rules/docs-style.mdc).
