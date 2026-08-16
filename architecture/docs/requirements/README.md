# Requirementsboom

De gelaagde breakdown van de OKx-requirements: van de opdracht (Leren zonder Drempels) via epics en features naar stories, met onderaan de aansluiting op de koppelingspecificaties. De boom is de getoonde koppeling tussen business en techniek; elke rij draagt een bron.

## De boom in één plaat

De plaat toont de opdracht, de drie doelen en de acht epics. Features en stories staan alleen in de tabellen; elke rij draagt een id (epic, feature, story) om naar te verwijzen.

```mermaid
flowchart LR
  LZD["Leren zonder Drempels"] --> DL1["doel-0001 gezamenlijke taal"] & DL2["doel-0002 gegevensuitwisseling en mobiliteit"] & DL3["doel-0003 keuze en personalisering"]
  DL1 --> EP1["epic-0001 Gezamenlijke taal en standaard"]
  DL2 --> EP2["epic-0002 Onderwijsaanbod specificeren en ontsluiten"]
  DL2 --> EP3["epic-0003 Aanbod plannen en roosteren"]
  DL2 --> EP4["epic-0004 Betrouwbare en vervangbare koppelingen"]
  DL2 --> EP5["epic-0005 Standaard piloteren en adopteren"]
  DL3 --> EP6["epic-0006 Student kiest onderwijsspecificaties"]
  DL3 --> EP7["epic-0007 Keuze en verbintenis vastleggen"]
  DL3 --> EP8["epic-0008 Voortgang en resultaat op leeruitkomsten"]
```

## Navigatie

| Laag | Bestand | Stand | Voor wie vooral |
|---|---|---|---|
| Opdracht | [opdracht.md](opdracht.md) | drie doelen | product owner en kernteam |
| Epics | [epics.md](epics.md) | acht epics, zes tot stories uitgewerkt | product owner en kernteam |
| Features | [features.md](features.md) | zesendertig features | kernteam en technische werkgroep |
| Stories | [stories.md](stories.md) | vierentwintig stories, negen met interactiekoppeling | technische werkgroep en leveranciers |
| Leeswijzer | [leeswijzer.md](leeswijzer.md) | leesroutes naar de bestaande documentatie | iedereen |

## Conventies

- Vorm en spelregels: [skill okx-requirements-boom](../../../.agents/skills/okx-requirements-boom/SKILL.md). Kern: één document per laag, elke rij één ouder, één bron en een id, overzicht boven volledigheid.
- Id's (epic-0001, feature-0001, story-0001) zijn verwijzings-id's voor issues, reviews en gesprekken: plat per soort, voluit met vier cijfers, zonder oudernummer in het id. Planningsstatus leeft in milestones en issues, niet in deze tabellen.
- Systeemafkortingen in de tabellen: OC (onderwijscatalogus), SKS (studentkeuzesysteem), P&R (planning en roostering), SIS (studentinformatiesysteem), LMS (leermanagementsysteem), SVS (studievoortgangsysteem).
- Bronafkortingen in de tabellen: ADR (architecture decision record, in Npuls-OKx/Public), U (uitgangspunt bij de koppelvlakspecificaties), OKx-AP (architectuurprincipe).
- Herkomst en verificatie van elke rij: [extractieverantwoording](../../agent-artifacts/research/20260806_0837_requirementsboom-extractie.md), inclusief de parkeerlijst met kandidaten voor een volgende ronde. Oudere documenten en verantwoordingen gebruiken de id-vormen van vóór de hernummering (E1, F2.1, S2.3); de [hernummeringstabel](../../agent-artifacts/research/20260816_1820_hernummering-requirementsboom.md) vertaalt oud naar nieuw.
- Eis-id's en uitvoerbare scenario's staan bewust niet in de boom. Die achtergrondmechaniek volgt gefaseerd; zie de [synthese van het onderzoek](../../agent-artifacts/research/20260804_1700_oplossingsrichtingen-business-techniek.md).

## Scope

Deze map bevat de requirementsboom: de vier laagdocumenten, de leeswijzer en deze index. De boom verwijst naar bestaande documenten en herhaalt ze niet. Al het overige valt buiten scope.
