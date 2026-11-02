# OKx Informatiestromen

> **Gearchiveerd op 2 november 2026.** Dit document beschrijft de hoofdplaat van maart 2026 en
> leunt op het MOKA-sjabloon, dat zelf in [`archief/MOKA`](MOKA/) staat. Het wordt niet meer
> bijgewerkt.
>
> Waar de levende versie staat: het [informatiemodel en de stromen](../architecture/model/) komen
> uit het ArchiMate-model, de hoofdplaat staat als versie 1.7a op de [landingspagina](../README.md),
> en hoe OKx van een stroom naar een specificatie komt staat in [deel 4 van de
> leesroute](../project/leesroute.md#deel-4-de-gedeelde-taal). Bij verschil is het model leidend.
>
> De nummering van de stromen hieronder blijft in gebruik: documenten en besluiten verwijzen ernaar,
> onder meer [ADR 0002](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0002-prioriteitsketen-catalogus-drielagen-fundament.md)
> met stroom 1 als eerste prioriteitsstroom.
>
## Rol van dit document

Hier leggen we **conceptueel** vast **wat** de informatiestromen in de onderwijslogistieke keten **doen** (welke informatie gaat waarheen, met welke bedoeling). Die beschrijving is **geen** eindproduct op zich: ze dient als **invoer** voor latere **technische koppelvlakuitwerking** — de **hoofdleverables** van OKx.

Die technische uitwerking wordt straks vergelijkbaar met bestaande sectorpublicaties: o.a. **berichtspecificatie**, **klassendiagram**, **endpointbeschrijving**, en aansluiting op **[OEAPI](https://openonderwijsapi.nl/v6.0/)** waar passend. Een concreet voorbeeld van zo’n pakket (ander domein, wel vergelijkbaar type deliverable) is: [OKE MBO – toetsafname – concept specificaties (PDF, Edustandaard)](https://www.edustandaard.nl/app/uploads/2024/09/OKE-MBO-toetsafname-specs-v1.0_20240909conceptversie.pdf).

**Kort gezegd:** architectuur en keteninzicht gebruiken we om **gericht** koppelvlakken **technisch** te specificeren — met **zicht op de hele keten**, zodat we **lokale optima** (eilandoplossingen per koppelvlak) vermijden en een **gedeeld minimum** aan afspraken bereiken.

## De hoofdplaat als richting (welke stromen nog uitwerken)

De **hoofdplaat OKx informatiestromen** is de **richtinggevende** afbeelding: die maakt zichtbaar **welke** stromen tussen referentiecomponenten **nog** beschreven en gespecificeerd moeten worden. De interpretatie met de nummers, de componenten en de prioriteit staat hieronder onder *De stromen genummerd*.

## Huidige uitwerking en wat nog moet

Uitwerking gebeurt volgens de **MOKA-metamodel**-afspraken: **koppelvlakspecificatie-views**, en **andere MOKA-subproducten** (o.a. informatiemodel) waar nodig, aangevuld met **architectuurproducten** in het ArchiMate-model (zie [Informatiestromen, ArchiMate en MOKA-view](informatiestromen-archimate-en-moka-view.md)).

**Status (indicatief):** er is al inhoudelijke uitwerking voor o.a. **stroom curriculumontwerp ↔ onderwijscatalogus**, **OC–Planning**, **OC–SVS**, en een **beperkt stuk** rond **Student kiest–KRS**. Er moet **nog veel** worden toegevoegd en verfijnd voor de overige stromen uit de hoofdplaat.

## De stromen genummerd

De onderstaande tabel interpreteert de hoofdplaat van maart 2026, en stond eerder in de informatiestromen. De plaat is sindsdien naar versie 1.7a gegaan en het model draagt de stromen nu zelf in `architecture/model/informatiemodel/stromen.json`; bij verschil is het model leidend. De nummering hieronder blijft in gebruik omdat documenten en besluiten ernaar verwijzen. Alleen de flowlijnen die **niet blauw** (procedureel) en **niet oranje** (o.a. OKE/Edubroker) zijn, zijn opgenomen — dit zijn de informatiestromen die verder gespecificeerd moeten worden. De semantische beschrijving op of bij elke lijn in de plaat is overgenomen en waar nodig kort uitgebreid. **Context:** linkervlak = onderwijsontwikkeling, inrichting van nominale- en keuze aanbod; rechter (grijs) vlak = student studeert en maakt keuzes / onderwijsuitvoering (flexibel onderwijs).

| Nr | Referentie component (van) | Referentie component (naar) | Semantische beschrijving informatiestroom | Context | Prioriteit |
|----|----------------------------|-----------------------------|------------------------------------------|---------|------------|
| 1 | Curriculum ontwerptool | Onderwijscatalogus | Uitgewerkt aanbod | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | 0 (Basis, voedt alle andere systemen) |
| 2 | Onderwijscatalogus | Planningssysteem (meer jarenplanning) | Te plannen aanbod | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod |1 |
| 3 | Onderwijscatalogus | Student volg systeem (SVS) | Nominale leerroute (detail), keuze aanbod (detail) en resultaatstructuren | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | 2 |
| 4 | Leer management systeem (LMS) | Onderwijscatalogus | Van leermiddel te voorziene aanbod | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | 3  |
| 5 | Planningssysteem (meer jarenplanning) | Student volg systeem (SVS) | Mogelijke keuzes | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | - |
| 6 | Planningssysteem (jaar/periode) | Student Kiest (nog niet in MORA) | Inschrijving/intekening op te plannen opleidingsonderdeel / leeractiviteit | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 7 | Roostersysteem (periode) | Student Kiest (nog niet in MORA) | Aanbod beschikbare capaciteit | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 8 | Onderwijscatalogus | Roostersysteem (periode) | Acceptatie inschrijving/intekening Lesgroep | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 9 | Onderwijscatalogus | Student volg systeem (SVS) | Actualiseren resultaatstructuren obv keuzes | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 10 | Student Kiest (nog niet in MORA) | Student volg systeem (SVS) | Inschrijving op opleidingsprogramma | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 11 | Student Kiest (nog niet in MORA) | Kernregistratie systeem studenten (KRS) | Studenten, inschrijving nominale leerroute en initiële keuzes | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 12 | Student volg systeem (SVS) | Leer management systeem (LMS) | Toewijzing van leermiddelen obv keuzes | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 13 | Student volg systeem (SVS) | Toets- en examen afname systeem | Voortgang uitkomsten en resultaten | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 14 | Kernregistratie systeem studenten (KRS) | Student | Is ingeschreven | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 15 | Student | Student Kiest (nog niet in MORA) | *In aanbouw* (impliciete keuze-interactie door de student) | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 16 | Planningssysteem (jaar/periode) | Roostersysteem (periode) | Planning | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 17 | Roostersysteem (periode) | Planningssysteem (jaar/periode) | Realisatie | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |

*Waar uit de plaat geen eenduidige tekst of component kon worden afgeleid staat *in aanbouw*; overige rijen kunnen door het kernteam worden aangevuld of verfijnd (circa 20 lijnen in de plaat).*

## Relatie tot MORA en architectuurgremia

Deze uitwerking is **niet** bedoeld als **directe wijziging** van de MORA. We gebruiken **MOKA** als structuur zodat **architectuurgremia** (MORA, MOKA-koppelvlaklijn, enz.) **makkelijk kunnen aanhaken** en kunnen **adviseren**. Op termijn kan een gedragen OKx-uitwerking dienen als **gericht wijzigingsverzoek** richting MORA — niet als vervanging van het sectorproces, maar als onderbouwde input.

## Architectuurbesluiten en impact

De vastgelegde **architectuurrichting** (ADR’s, meetings) en impact op keten en model: **[OKx Architectuurbesluiten en impact](architectuurbesluiten-en-impact.md)**.

## Verwijzing naar (technische) specificaties en OEAPI


| Informatiestroom                                                           | Sector Koppelvlak specificatie(s) MOKA uitwerking                                                                                                      | Originele sector specificatie                                                                                             | OEAPI Technische specificatie                                                                              |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Voorbeeld uitwerking Examen – uitvoering en beoordeling (gebaseerd op OKE) | [MOKA koppelvlakspecificatie OKE](../archief/MOKA/Examen%20Uitvoering%20en%20beoordeling/doc/KoppelvlakSpecificatieDocument.md) | [Originele sector specificatie](https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI/tree/main/specification/v5) | [OEAPI-consumer](https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI/tree/main/specification/v5) |
| Overige stromen uit de hoofdplaat Okx                                      | Worden uitgewerkt naar hetzelfde type deliverables (MOKA + OEAPI waar passend)                                                                         | —                                                                                                                         | —                                                                                                          |


Deze tabel wordt uitgebreid naarmate per stroom de technische bundel gereed is.

## Status

Document in aanbouw. Aanvullingen en correcties via issue of pull request; zie `[CONTRIBUTING.md](../CONTRIBUTING.md)`.