# OKx-profiel op OEAPI, ronde april en mei 2026

Deze map bewaart een afgesloten uitwerkingsronde: het OKx-profiel als consumer-extensie op de Open Education API. De documenten stonden in de fork `Npuls-OKx/specification` en zijn daaruit gehaald voordat die fork werd verwijderd.

Relateert aan: #265, #266.

## Status

**Afgesloten ronde, geen geldend kader.** De documenten dateren van 14 april tot 1 mei 2026 en zijn daarna niet meer bijgewerkt. Het geldende kader staat elders; zie [Waar het huidige werk staat](#waar-het-huidige-werk-staat).

Wie hieruit citeert, noemt de datum erbij. Een aantal keuzes in deze documenten is sindsdien herzien.

## Wat er sindsdien is veranderd

Twee verschuivingen maken dat deze ronde anders leest dan het werk van vandaag.

| Toen | Nu |
|---|---|
| De uitwerking heette het OKx OEAPI consumer-profiel | Zij heet de [leerroute-uitwerking](../../docs/specificatie/leerroute-uitwerking/README.md) en volgt de AMIGO-aanpak |
| De vertaling liep top-down: vanaf de OEAPI-objecten naar de OKx-behoefte | De vertaling loopt bottom-up: eisen komen vóór de techniekkeuze, en OEAPI volgt uit de koppelingspecificaties |

Die tweede verschuiving is de belangrijkste. Een eis sneuvelt niet omdat OEAPI hem niet toestaat; zo'n verschil is een signalering richting de standaard. De feature-indeling hieronder is dus opgezet vanuit OEAPI-objecten, terwijl het huidige werk vanuit leerroutes en scenario's vertrekt.

## Wat hier bruikbaar blijft

Drie dingen hebben de verschuiving overleefd en dienen als basis voor verdere uitwerking.

- **De leeruitkomsten.** Feature 6 draagt de mapping van Nederlands naar Engels, de OEAPI-kernvelden met de OKx-extensieattributen ernaast, validatie-invarianten, een toestandsdiagram voor `standardisationStatus` en een voorbeeld met een root-leeruitkomst, een lesuitkomst en een gedeelde lesuitkomst in een gerichte acyclische graaf.
- **De signaleringen richting OEAPI.** Feature 12 benoemt er vier: `studyLoad` op LearningComponent en TestComponent, uitbreiding van de extensible-enum `modesOfDelivery`, `prerequisiteIds` op Course en LearningComponent, en `credentialDocument` als kernattribuut.
- **De overlay-structuur.** De documenten schrijven paden als `source/consumers/OKx/V1/LearningOutcome.yaml`, en dat is dezelfde opbouw die OEAPI aanraadt in [oeapi-profile-example](https://github.com/open-education-api/oeapi-profile-example). Het werk past dus op de submodule-werkwijze uit #268.

## Wat er in deze map staat

**Aanpak en uitwerking**

| Document | Wat het is |
|---|---|
| [`20260414_1800_okx-oeapi-consumer-profiel.md`](20260414_1800_okx-oeapi-consumer-profiel.md) | Het featureplan dat de twaalf features belegt |
| [`doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md`](doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) | Het specificatiedocument van de ronde, het grootste stuk |
| [`20260430_archimate_extract_businessobjects_processtappen.md`](20260430_archimate_extract_businessobjects_processtappen.md) | Extract van businessobjecten en processtappen uit het ArchiMate-model |

**Ontwerpdocumenten per feature**

| Document | Onderwerp |
|---|---|
| [Feature 1](20260414_1900_feature-1-enumeraties-en-gedeelde-typen.md) | Enumeraties en gedeelde typen |
| [Feature 2](20260414_1930_feature-2-programme-extensie.md) | Programme-extensie: curriculum- en kwalificatielaag |
| [Feature 3](20260414_1930_feature-3-course-extensie.md) | Course-extensie: opleidingsonderdeel en leertaak |
| [Feature 4](20260414_1930_feature-4-lc-tc-extensie.md) | LearningComponent- en TestComponent-extensie |
| [Feature 5](20260414_1930_feature-5-offering-extensies.md) | Offering-extensies: aanbod- en planningslaag |
| [Feature 6](20260414_1930_feature-6-learningoutcome-extensie.md) | LearningOutcome-extensie: leeruitkomsten en CompetentNL |
| [Feature 7](20260414_1930_feature-7-aggregatie-validatie.md) | Aggregatie-validatie en voorbeeldscenario's |
| [Feature 8](20260414_1930_feature-8-programme-trechters.md) | Programme-extensies: trechters en instroomeisen |
| [Feature 9](20260414_1930_feature-9-courseoffering-extensies.md) | CourseOffering-extensies: beschikbaarheid en budget |
| [Feature 10](20260414_1930_feature-10-planningsattributen.md) | Planningsattributen op offerings |
| [Feature 11](20260414_1930_feature-11-cross-instelling.md) | Cross-instelling interoperabiliteit |
| [Feature 12](20260414_1930_feature-12-oeapi-signaleringen.md) | Signaleringen en wijzigingsverzoeken richting OEAPI |

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
