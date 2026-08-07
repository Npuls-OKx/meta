# Begrippenkader en ankertabel

Het semantisch kader van OKx: de zes begrippenfamilies (kader, beoogde leeruitkomst, onderwijsspecificatie, onderwijsaanbod, onderwijsverbintenis, onderwijsresultaat), de zes niveaus van het kwalificatiekader, de stadia van aanbod en verbintenis, en de ankertabel die niveaus en families kruist. Dit kader is vastgesteld en is de toetssteen voor naamgeving in de requirementsboom, de koppelingspecificaties en de reviews. Relateert aan: #137.

Dit bestand is bij de herstructurering van augustus 2026 losgemaakt uit de [leerroute-uitwerking](leerroute-uitwerking-lr1.md). Het beschrijft de begrippen zonder techniekkeuze; de eerdere OEAPI-vertaling staat als bronmateriaal in het [archief](archief-conceptmodellen.md), en de definitieve vertaling volgt bottom-up uit de endpoint-gedreven datamodellen in [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties).

## Zes niveaus: van diploma tot lesopdracht

Dezelfde zes families komen op meerdere **niveaus** terug. Het kwalificatiekader (SBB) bepaalt de niveaus, OKx volgt diezelfde rij-discipline:

| Niveau (rij) | Wat het betekent |
| ---------------------------------- | ---------------------------------------------------------------------- |
| **Kwalificatiedossier**            | Geheel van een mbo-beroepsdomein                                       |
| **Kwalificatie**                   | Diplomeerbare opleiding binnen het dossier                             |
| **Kerntaak**                       | Samenhangend cluster van werkprocessen                                 |
| **Werkproces**                     | Concreet uitvoerbaar onderdeel van het beroep                          |
| **Lesuitkomst**               | Wat een student in één les leert (formatief)                           |
| **Toets** (cross-cutting)       | Welk cluster van leeruitkomsten of lesuitkomsten summatief wordt beoordeeld |

De hiërarchie groeit mee: een kerntaak heeft meerdere werkprocessen, een werkproces meerdere leeruitkomsten, en een leeruitkomst kan over meerdere lessen worden gespreid (gerichte acyclische graaf, DAG).


## Stadia van onderwijsaanbod: specificatie, planbaar, geroosterd

Aanbod ontstaat in stappen. Dit onderscheid is **cruciaal** voor de scenario's, omdat een student aan het begin van het schooljaar typisch *niet* voor alle drie de jaren tegelijk geroosterd is: sommige eenheden zijn al geroosterd, andere alleen planbaar, en weer andere staan nog alleen als specificatie.

```mermaid
stateDiagram-v2
    [*] --> Specificatie : ontwerper publiceert in OC
    Specificatie --> PlanbaarAanbod : planning maakt periode + capaciteit, ZONDER concrete resources
    PlanbaarAanbod --> GeroosterdAanbod : roostering wijst lokaal/docent/groep toe in tijdsloten
    PlanbaarAanbod --> NietPlanbaar : capaciteit/resources tekort (bottleneck)
    GeroosterdAanbod --> AfgelastAanbod : minimum aantal studenten niet gehaald of conflict
    Specificatie --> Specificatie : nieuwe versie
    PlanbaarAanbod --> PlanbaarAanbod : capaciteitsupdate
    GeroosterdAanbod --> GeroosterdAanbod : roosterwijziging
```

- **Specificatie** = ontwerp/sjabloon. Stabiel, herbruikbaar, versieerbaar. Bevat *wat* geleerd wordt en *hoe organiseerbaar* (onder meer leervorm, onderwijstijd, ruimtetype en expertiseprofiel).
- **Planbaar aanbod (stadium 2a)** = specificatie ingepast in **perioden** + **capaciteit** (maximum aantal studenten). **Geen** concrete resource-instanties. Hoort bij de planner.
- **Geroosterd aanbod (stadium 2b)** = planbaar aanbod met **concrete tijdsloten** + **resource-instanties** (lokaal-instantie, personeelsnummer). Hoort bij de roosteraar.

## Stadia van onderwijsverbintenis: aangemeld, ingeschreven, deelnemend, afgerond

Een student loopt parallel een eigen state-machine: van eerste belangstelling tot afronding. Verbintenissen bestaan op elk niveau (programma, eenheid, leergelegenheid, toets) en ze hebben elk hun eigen state:

```mermaid
stateDiagram-v2
    [*] --> Aangemeld : student dient verzoek in (SVS/aanmeldsysteem)
    Aangemeld --> Ingeschreven : SLB'er/SVS plaatst student op programma
    Ingeschreven --> Deelnemend : start van uitvoering
    Deelnemend --> Afgerond : afronding, met resultaat
    Deelnemend --> Onderbroken : pauze, ziekte, time-out
    Onderbroken --> Deelnemend : hervat
    Aangemeld --> Geannuleerd : verzoek ingetrokken
    Ingeschreven --> Geannuleerd : uitschrijving voor uitvoering
    Deelnemend --> Geannuleerd : voortijdig stoppen
```

Het minimumresultaat is de status van de verbintenis per niveau (deelgenomen, afgerond). Rijkere bewijsvoering op leeruitkomstniveau vraagt een aanvullend resultaat-koppelvlak; die signalering staat met het oudere conceptmateriaal in het [archief](archief-conceptmodellen.md).


## De ankertabel: zes niveaus maal zes families

De volgende tabel is de **canonieke verankering** van de zes begrippenfamilies (kolommen) op de zes niveaus (rijen). Lees als: "*per kwalificatiekader-niveau (rij) hebben we kader, beoogde uitkomsten, een specificatie, een aanbod, een verbintenis en een resultaat*". De tabel is in eerdere versies §12.0.2 geweest; dit is nu de definitieve plek.

| Niveau (rij) ↓ \ Familie (kolom) →                                                           | **1. Kader**                                                                  | **2. Beoogde leeruitkomst**                                                                   | **3. Onderwijsspecificatie**       | **4. Onderwijsaanbod**                                                                                                         | **5. Onderwijsverbintenis**                  | **6. Onderwijsresultaat**                            |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------- |
| `Kwalificatiedossier`                                                                        | SBB-dossier                                                                   | *n.v.t. op dit niveau*                                                                        | `Opleidingsspecificatie`           | `Opleidingsaanbod`                                                                                                             | `Opleidingsverbintenis`                      | `Opleidingsresultaat`                                |
| `Kwalificatie`                                                                               | SBB-kwalificatie                                                              | *n.v.t. op dit niveau*                                                                        | `Opleidingsprogramma-specificatie` | `Opleidingsprogramma-aanbod`                                                                                                   | `Opleidingsprogramma-verbintenis`            | `Opleidingsprogramma-resultaat`                      |
| `Kerntaak`                                                                                   | SBB-kerntaak                                                                  | **Collectie van LO-collecties** (kerntaak heeft meerdere werkprocessen, elk met eigen LO-set) | `Onderwijseenheid-specificatie`    | `Onderwijseenheid-aanbod`                                                                                                      | `Onderwijseenheid-verbintenis`               | `Onderwijseenheid-resultaat`                         |
| `Werkproces`                                                                                 | SBB-werkproces                                                                | **Collectie leeruitkomsten** (summatief)                                                      | `Leeronderdeel-specificatie`       | `Leergelegenheid` (groep van lessen)     | Verbintenis op de `leergelegenheid` | Resultaat op de `leergelegenheid` (behaald-status) |
| *n.v.t. kwalificatiekader*                                                                   | (instelling-eigen)                                                            | `Lesdoel / Lesuitkomst`                                                                       | `Lesspecificatie`                  | `Lesgelegenheid`      | Verbintenis op de `lesgelegenheid` | Resultaat op de `lesgelegenheid` (eventueel aanwezigheid) |
| Summatief: vaststelling Examencommissie t.o.v. leeruitkomsten / formatief: instellingsbeleid | Examencie-besluit (summatief) of instellingsbeleid (formatief)                | `Lesuitkomst`/set, `Leeruitkomst`/set, `Werkproces`/set, … (scope van toetsing)               | `Toetsonderdeel-specificatie`      | `Toetsgelegenheid`                                                                                                             | `Toetsgelegenheid-verbintenis`               | `Toetsresultaat / Aanwezigheid`                      |

**Cardinaliteit (normatief voor dit profiel):**

- `Kerntaak (1..*) Werkproces`
- `Werkproces (1..*) Leeruitkomst` (summatief)
- `Leeruitkomst (0..*) Onderwijseenheid` / `Leeronderdeel` / `Toetsonderdeel` (dezelfde LO kan over meerdere onderdelen verdeeld zijn; onderdelen kunnen meerdere LO's dekken)
- `Leeruitkomst (0..*) Lesuitkomst` (formatief; DAG/boom-structuur)

**Voetnoot.** OKx richt zich in dit profiel primair op het beschrijven van de **werkproceslaag**. De entiteit *leergelegenheid* (groep van lessen) leidt uiteindelijk tot individueel geroosterde lessen. Binnen geroosterde lessen kunnen op hun beurt geneste lessen voorkomen; in toekomstige iteraties moeten ook deze recursief volgens dit datamodel gemodelleerd kunnen worden. Dit geldt eveneens voor diepere sublagen zoals een *lessenreeks* of specifieke leeractiviteiten binnen een les. Dit erkent expliciet dat onder een *leergelegenheid* of *lessenreeks* nog een hiërarchie van leeronderdelen kan bestaan, met directe impact op bottom-up en top-down aggregatie.

> **Verdiepende verwijzingen:** de uitwerking op attribuutniveau staat in de [payload-onderwijsspecificatie](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/payload-onderwijsspecificatie.md); het oudere conceptmateriaal en de OEAPI-vertaling staan in het [archief](archief-conceptmodellen.md).
