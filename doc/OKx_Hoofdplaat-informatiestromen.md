# Hoofdplaat OKx informatiestromen

**Doel.** De hoofdplaat duiden: welke informatiestromen tussen de applicatiecomponenten in de keten bestaan, en welke daarvan verder gespecificeerd worden richting koppelingspecificaties.

**Scope.** Versie 1.7 is de leidende plaat; de legenda draagt zelf nog de aanduiding "concept", dus de plaat is richtinggevend en niet vastgesteld. De interpretatietabel hieronder is opgesteld bij versie v20260317 en wordt bij v1.7 herijkt. Wat de stromen in de keten betekenen als invoer voor berichtspecificaties staat in [OKx Informatiestromen (ketenconcept)](OKx_Informatiesstromen.md).

## De plaat (v1.7)

![Hoofdplaat OKx informatiestromen v1.7](../img/hoofdplaat-okx-informatiestromen-v1.7.jpg)

**In de eerdere plaat (v20260317, hieronder in de tabel geïnterpreteerd): rood = eerste prioriteit.**

![Hoofdplaat OKx informatiestromen v20260317](../img/hoofdplaat-okx-informatiestromen-v20260317.png)

## Interpretatie van de informatiestromen (opgesteld bij v20260317)

De onderstaande tabel interpreteert de plaat **"hoofdplaat-okx-informatiestromen-v20260317.png"**. Alleen de flowlijnen die **niet blauw** (procedureel) en **niet oranje** (o.a. OKE/Edubroker) zijn, zijn opgenomen — dit zijn de informatiestromen die verder gespecificeerd moeten worden. De semantische beschrijving op of bij elke lijn in de plaat is overgenomen en waar nodig kort uitgebreid. **Context:** linkervlak = onderwijsontwikkeling, inrichting van nominale- en keuze aanbod; rechter (grijs) vlak = student studeert en maakt keuzes / onderwijsuitvoering (flexibel onderwijs).

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
