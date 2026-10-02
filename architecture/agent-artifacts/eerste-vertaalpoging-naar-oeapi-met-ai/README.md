# Eerste vertaalpoging van de OKx-specificatie naar OEAPI, met AI

Deze map bewaart een afgesloten ronde uit april en mei 2026: een eerste poging om de OKx-specificatie te gebruiken en te vertalen naar de Open Education API, met AI als hulpmiddel. De documenten stonden in de fork `Npuls-OKx/specification` en zijn daaruit gehaald voordat die fork werd verwijderd.

Relateert aan: #265, #266.

## Wat dit wel en niet is

**Geen OEAPI-profiel.** De documenten dragen die naam wel, en dat is misleidend. Een profiel is een vastgestelde overlay op een vastgezette OEAPI-versie, opgebouwd volgens de werkwijze in [AGENTS.md](../../../AGENTS.md). Dit is een verkenning: een poging om te zien hoe de OKx-begrippen op OEAPI-objecten zouden kunnen landen.

**Werkmateriaal, geen geldend kader.** De stukken dateren van 14 april tot 1 mei 2026 en zijn daarna niet bijgewerkt. Wie hieruit citeert, noemt de datum erbij.

**Met AI gemaakt, en dat is te zien.** De uitwerking is breed en op punten gedetailleerder dan de onderbouwing draagt. Lees de inhoud als voorstel, niet als bevinding.

## Wat er sindsdien is veranderd

| Toen | Nu |
|---|---|
| De uitwerking heette het OKx OEAPI consumer-profiel | Zij heet de [leerroute-uitwerking](../../docs/specificatie/leerroute-uitwerking/README.md) en volgt de AMIGO-aanpak |
| De vertaling liep top-down: vanaf de OEAPI-objecten naar de OKx-behoefte | De vertaling loopt bottom-up: eisen komen vóór de techniekkeuze, en OEAPI volgt uit de koppelingspecificaties |
| Het werk lag in een fork van de OEAPI-specificatie | Specificeren bovenop OEAPI gaat via een submodule op een vastgezet versielabel |

Die tweede verschuiving verklaart waarom het specificatiedocument vreemd aanvoelt. Het is opgezet vanuit OEAPI-objecten (Programme, Course, Offering, LearningOutcome), terwijl het huidige werk vanuit leerroutes en scenario's vertrekt.

## Het bruikbaarste deel

[**Student kiest op het OEAPI-datamodel**](doc/20260501_student-kiest-op-het-oeapi-datamodel.md) staat apart. Het is paragraaf 4 en 5 van het specificatiedocument, losgetrokken omdat juist dat deel de verschuiving in aanpak overleeft:

- de keten van student kiest, met de onderwijscatalogus als centraal distributiepunt;
- de leeruitkomsthierarchie op het recursieve datamodel van OEAPI, met bottom-up aggregatie, een uitgewerkt voorbeeld voor de apothekersassistent, de gerichte acyclische graaf met hergebruik over meerdere ouders, en CompetentNL-referenties als matchingsleutel.

De twaalf ontwerpdocumenten per feature zijn ingehaald en staan er niet meer. Twee stukken eruit zijn bewaard: de validatie-invarianten en het toestandsdiagram voor `standardisationStatus` staan als bijlage bij het uittreksel. De signaleringen richting OEAPI staan uitgebreider in paragraaf 9 van het volledige specificatiedocument, met zeven punten in plaats van vier.

Het specificatiedocument schrijft paden als `source/consumers/OKx/V1/LearningOutcome.yaml`, dezelfde opbouw die OEAPI aanraadt in [oeapi-profile-example](https://github.com/open-education-api/oeapi-profile-example). Het werk past dus op de submodule-werkwijze.

## Wat er in deze map staat

**De uitwerking**

| Document | Wat het is |
|---|---|
| [`doc/20260501_student-kiest-op-het-oeapi-datamodel.md`](doc/20260501_student-kiest-op-het-oeapi-datamodel.md) | Paragraaf 4 en 5, losgetrokken |
| [`doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md`](doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | Het volledige specificatiedocument van de ronde, twintig paragrafen |

**Beeldmateriaal**

Het procesbeeld van leerroute 1, scenario 1a, staat als [SVG](doc/leerroute-1-scenario-1-a-regulier-basis-svg.svg) en als [BPMN-bronbestand](doc/leerroute-1-scenario-1-a-regulier-basis.bpmn2) in `doc/`.

## Waar het huidige werk staat

| Onderwerp | Vindplaats |
|---|---|
| Leerroutes, scenario's en persona's | [`architecture/docs/specificatie/leerroute-uitwerking/`](../../docs/specificatie/leerroute-uitwerking/README.md) |
| Informatiemodel en begrippen | [`architecture/model/informatiemodel/`](../../model/informatiemodel/informatiemodel.md) en de [begrippenlijst](../../docs/specificatie/begrippen/begrippenlijst.md) |
| De leeruitkomst als verbindende sleutel | [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md) in Npuls-OKx/Public |
| Koppelingspecificaties en datamodelschema's | [`Koppelvlakspecificaties/`](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties) in Npuls-OKx/Public |
| De werkwijze voor specificeren op OEAPI | #268 |
