# OKx Informatiestromen

## Rol van dit document

Hier leggen we **conceptueel** vast **wat** de informatiestromen in de onderwijslogistieke keten **doen** (welke informatie gaat waarheen, met welke bedoeling). Die beschrijving is **geen** eindproduct op zich: ze dient als **invoer** voor latere **technische koppelvlakuitwerking** — de **hoofdleverables** van OKx.

Die technische uitwerking wordt straks vergelijkbaar met bestaande sectorpublicaties: o.a. **berichtspecificatie**, **klassendiagram**, **endpointbeschrijving**, en aansluiting op **[OEAPI](https://openonderwijsapi.nl/v6.0/)** waar passend. Een concreet voorbeeld van zo’n pakket (ander domein, wel vergelijkbaar type deliverable) is: [OKE MBO – toetsafname – concept specificaties (PDF, Edustandaard)](https://www.edustandaard.nl/app/uploads/2024/09/OKE-MBO-toetsafname-specs-v1.0_20240909conceptversie.pdf).

**Kort gezegd:** architectuur en keteninzicht gebruiken we om **gericht** koppelvlakken **technisch** te specificeren — met **zicht op de hele keten**, zodat we **lokale optima** (eilandoplossingen per koppelvlak) vermijden en een **gedeeld minimum** aan afspraken bereiken.

## De hoofdplaat als richting (welke stromen nog uitwerken)

De **hoofdplaat OKx informatiestromen** is de **richtinggevende** afbeelding: die maakt zichtbaar **welke** stromen tussen referentiecomponenten **nog** beschreven en gespecificeerd moeten worden. De interpretatie (nummers, componenten, prioriteit) staat in het **[OKx-projectoverzicht](Projectoverzicht.md)** onder *Hoofdplaat OKx informatiestromen* — daar is de **actuele** plaat en tabel leidend; dit document herhaalt die tabel niet.

## Huidige uitwerking en wat nog moet

Uitwerking gebeurt volgens de **MOKA-metamodel**-afspraken: **koppelvlakspecificatie-views**, en **andere MOKA-subproducten** (o.a. informatiemodel) waar nodig, aangevuld met **architectuurproducten** in het ArchiMate-model (zie [Informatiestromen, ArchiMate en MOKA-view](Informatiestromen-ArchiMate-en-MOKA-view.md)).

**Status (indicatief):** er is al inhoudelijke uitwerking voor o.a. **stroom curriculumontwerp ↔ onderwijscatalogus**, **OC–Planning**, **OC–SVS**, en een **beperkt stuk** rond **Student kiest–KRS**. Er moet **nog veel** worden toegevoegd en verfijnd voor de overige stromen uit de hoofdplaat.

## Relatie tot MORA en architectuurgremia

Deze uitwerking is **niet** bedoeld als **directe wijziging** van de MORA. We gebruiken **MOKA** als structuur zodat **architectuurgremia** (MORA, MOKA-koppelvlaklijn, enz.) **makkelijk kunnen aanhaken** en kunnen **adviseren**. Op termijn kan een gedragen OKx-uitwerking dienen als **gericht wijzigingsverzoek** richting MORA — niet als vervanging van het sectorproces, maar als onderbouwde input.

## Architectuurbesluiten en impact

De vastgelegde **architectuurrichting** (ADR’s, meetings) en impact op keten en model: **[OKx Architectuurbesluiten en impact](Architectuurbesluiten-en-impact.md)**.

## Verwijzing naar (technische) specificaties en OEAPI


| Informatiestroom                                                           | Sector Koppelvlak specificatie(s) MOKA uitwerking                                                                                                      | Originele sector specificatie                                                                                             | OEAPI Technische specificatie                                                                              |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Voorbeeld uitwerking Examen – uitvoering en beoordeling (gebaseerd op OKE) | [MOKA koppelvlakspecificatie OKE](../../OKE/moka-koppelvlakspecificaties/Examen%20Uitvoering%20en%20beoordeling/doc/KoppelvlakSpecificatieDocument.md) | [Originele sector specificatie](https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI/tree/main/specification/v5) | [OEAPI-consumer](https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI/tree/main/specification/v5) |
| Overige stromen uit de hoofdplaat Okx                                      | Worden uitgewerkt naar hetzelfde type deliverables (MOKA + OEAPI waar passend)                                                                         | —                                                                                                                         | —                                                                                                          |


Deze tabel wordt uitgebreid naarmate per stroom de technische bundel gereed is.

## Status

Document in aanbouw. Aanvullingen en correcties via issue of pull request; zie `[CONTRIBUTING.md](../CONTRIBUTING.md)`.