# De taxonomiecode per leeruitkomst

De zeven leeruitkomsten in de voorbeelduitwerking van leerroute 1 dragen sinds dit document een taxonomiecode in het veld `taxonomie` van [`voorbeeld-lr1-regels.json`](voorbeeld-lr1-regels.json). Hier staat welke code en waarom. Relateert aan: #350 en #347.

**De codes zijn een voorstel.** De plaatsing van een leeruitkomst in een taxonomie is onderwijskundig werk. Wat hier staat is afgeleid uit de formulering en uit de indeling van Romiszowski; bevestiging door een onderwijskundige staat nog open.

## Welke taxonomie

De [Handleiding Formuleren leeruitkomsten](https://nlqf.nl/wp-content/uploads/2025/06/Handleiding_Formuleren_leeruitkomsten_2020_NCP_NLQF_28122020.pdf) van het NCP NLQF wijst de taxonomie aan op het NLQF-niveau: Romiszowski tot en met niveau 4, SOLO van Biggs vanaf niveau 5. Zes van de zeven leeruitkomsten staan op NLQF 3 of 4; de minor staat op NLQF 6.

## De keuze per leeruitkomst

| Leeruitkomst | Niveau | Code | Waarom |
|---|---|---|---|
| Verleent farmaceutische patientenzorg | NLQF 4, kerntaak | `Pi` | Zorg verlenen aan patienten in een levensechte omgeving vraagt afstemming per persoon: interactief, en zonder pasklare oplossing |
| Voert een baliegesprek met triage uit | NLQF 4, werkproces | `Pi` | Een gesprek voeren is interactief, en een onderbouwd advies of doorverwijzing vraagt een eigen afweging |
| Draagt bij aan kwaliteitszorg en arbeidsomstandigheden | NLQF 3, kerntaak | `Rc` | Werken volgens de RI&E-systematiek en het kwaliteitshandboek volgt een vastgelegde procedure |
| Levert een bijdrage aan de inrichting van het kwaliteitszorgsysteem | NLQF 3, werkproces | `Pc` | Een kwaliteitszorgsysteem inrichten is ontwerpen; er is geen kant en klare oplossing |
| Voert verdiepende farmaceutische patientenzorg uit | NLQF 4, kerntaak | `Pc` | Meervoudig geneesmiddelgebruik vraagt een onderbouwd advies per casus, dus denkwerk zonder vast antwoord |
| Stelt een medicatieoverzicht op | NLQF 4, werkproces | `Rc` | Opstellen volgens de richtlijn en verifieren is een vaste procedure |
| Beoordeelt farmacotherapie op patientveiligheid | NLQF 6, minor | `solo3` | Vanaf NLQF 5 geldt SOLO; richtlijnen, literatuur en de casus aan elkaar verbinden is relationeel |

## Wat het patroon laat zien

```
werkprocesniveau                    kerntaakniveau
  Rc  Stelt een medicatieoverzicht op   Rc  Draagt bij aan kwaliteitszorg
  Pc  Levert een bijdrage aan de        Pc  Voert verdiepende zorg uit
      inrichting                        Pi  Verleent patientenzorg
  Pi  Voert een baliegesprek uit
                                      minor, NLQF 6
                                        solo3  Beoordeelt farmacotherapie
```

Twee dingen vallen op. Het onderscheid reproductief tegenover productief loopt niet gelijk met kerntaak tegenover werkproces: op beide niveaus staan zowel `R`- als `P`-codes. Wat de code bepaalt is de aard van de handeling, en niet de plek in het dossier.

En de minor valt buiten de reeks, want daar wisselt de taxonomie mee met het NLQF-niveau. Dat is precies de overgang die de handleiding beschrijft, hier zichtbaar in een voorbeeld: dezelfde vorm, een andere taxonomie.

## Controle

```bash
python3 scripts/keur-leeruitkomst.py architecture/model/informatiemodel/voorbeeld-lr1-regels.json
```

Die toetst of de code bestaat en of zij bij het NLQF-niveau in de zin past. Het schema [`voorbeeld-lr1-regels.schema.json`](voorbeeld-lr1-regels.schema.json) kent de zeventien toegestane waarden: twaalf van Romiszowski en vijf van SOLO.
