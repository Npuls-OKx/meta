## Resultaatbegrippen conform ROSA Kernmodel Onderwijsinformatie (KOI)

Status: Voorstel

Datum: 2026-07-23

### Context

Bij het uitwerken van de koppelingspecificatie OC-SIS (#98, #119) ontstond een informatiemodel waarin een verbintenis direct aan een onderwijsspecificatie hing en waarin een verzonnen term ("resultaatregistratie") werd gebruikt. Dat wijkt af van het [ROSA Kernmodel Onderwijsinformatie (KOI)](https://rosa.wikixl.nl/index.php/Kernmodel_Onderwijsinformatie) en van de ankertabel (specificatie, aanbod, verbintenis, resultaat). ADR 0019 legt de conceptuele gelaagdheid (kwalificatiekader, specificatie, aanbod) al langs ROSA/KOI; dit ADR doet hetzelfde voor de resultaatkant.

### Beslissing

1. **Onderwijsresultaat op leeruitkomsten.** Een onderwijsresultaat wordt behaald op leeruitkomsten, conform KOI. Niet op een onderwijsspecificatie als zodanig.
2. **Toetsonderdeelresultaten aggregeren naar onderwijsresultaat.** Om een leeruitkomst af te dichten zijn soms meerdere toetsonderdelen nodig. De toetsonderdeelresultaten leiden samen, gewogen volgens het examenplan, tot een onderwijsresultaat. De mapping welke toetsonderdeelresultaten welke leeruitkomst afdichten is expliciet onderdeel van de resultaatstructuur.
3. **Examenplan mapt via leeruitkomsten.** Het examenplan verbindt de resultaatstructuur via leeruitkomsten aan onderwijsspecificaties (weging en indeling van toetsonderdelen richting kwalificatie).
4. **Verbintenis hoort bij het aanbod.** Conform de ankertabel (kolom verbintenis) gaat een verbintenis over deelname aan aanbod, niet over een specificatie.
5. **Nominaal template en individuele structuur.** Het SIS hanteert de gepubliceerde onderwijsspecificatiestructuur als nominaal template per student. De student vult via het SKS de keuzedeelruimte in; de individuele structuur van de student is het template plus de ingevulde keuzedelen. In LR1-3 wijken nominaal en feitelijk gevolgd uitsluitend daarin af; ook bij versnellen of vertragen (LR2, LR3) blijft het programma en de wijze van afdichten gelijk.
6. **Nominaal en individueel examenplan.** Dezelfde symmetrie geldt voor het examenplan. Een keuzedeel kent een eigen examenplandeel met eigen toetsonderdelen die naar een eigen onderwijsresultaat mappen. Het individuele examenplan van de student is de samenstelling van het nominale examenplan plus de examenplandelen van de gekozen keuzedelen.
7. **Korrelgrootte leeruitkomsten.** Voor nu zijn leeruitkomsten de eenheden uit het SBB-kwalificatiekader (kwalificatiedossier, kerntaak, werkproces, keuzedeel). Fijnmazigere leeruitkomsten volgen later; het model moet die verfijning aankunnen (zie ook #84 R12).

### Alternatieven

- Optie A: eigen resultaatbegrippen per koppeling. Afgewezen: sectorbrede herkenbaarheid vereist KOI-conformiteit.
- Optie B: verbintenis op de specificatie. Afgewezen: strijdig met KOI en de ankertabel; een specificatie is een ontwerp, geen deelname.

### Consequenties

- Het informatiemodel van de koppelingspecificatie OC-SIS volgt deze begrippen (onderwijsresultaat, toetsonderdeelresultaat, individuele onderwijsspecificatiestructuur).
- De resultaatstructuur-payload wordt langs deze lijn omgebouwd (toetsonderdeelresultaat-mapping naar leeruitkomsten).
- De term "resultaatregistratie" vervalt.

### Relaties en links

- Issues: #98, #119, #110
- ROSA KOI: `https://rosa.wikixl.nl/index.php/Kernmodel_Onderwijsinformatie`
- ADR's: 0019 (conceptuele gelaagdheid ROSA/KOI), 0009 (SKS/SVS-rollen), 0021 (koppeling versus koppelvlak)
- Docs: `architecture/agent-artifacts/design-docs/koppelingspecificaties/oc-sis-krs-svs/`

### Vervangt (optioneel)

- Geen; werkt ADR 0019 uit voor de resultaatkant.
