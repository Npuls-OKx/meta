# De vorm van een leeruitkomst

Bronmateriaal voor het vastleggen van de vorm waarin een leeruitkomst wordt geschreven. Relateert aan: #347 en #345.

De [begrippenlijst](../begrippenlijst.md) zegt wat een leeruitkomst is. Hoe zij geschreven wordt stond nergens vast, terwijl de negen leeruitkomsten in de voorbeelduitwerking van leerroute 1 alle dezelfde opbouw volgen. Dit document bewaart het bronmateriaal waarop die opbouw te onderbouwen is.

## Vijf plekken in de zin

Firda, instelling in het middelbaar beroepsonderwijs, hanteert een indeling in vijf plekken. De slide "Komen tot leeruitkomsten" zet die naast elkaar, met de rolnaam onder elke cel.

![Slide Komen tot leeruitkomsten van Firda, met de vijf plekken in een leeruitkomst](img/firda-komen-tot-leeruitkomsten.jpg)

*Bron: Firda, slide "Komen tot leeruitkomsten". Opgenomen met bronvermelding; het materiaal blijft van Firda.*

De tabel op de slide, uitgeschreven:

| Afstellen | Ten behoeve van de kwalificatie operator productietechniek | Apparatuur | Aan de hand van specificaties | In een mechanische omgeving |
|---|---|---|---|---|
| Actief ww | Type | Onderwerp | Standaard | Context |

Boven de tabel staat de reikwijdte waarbinnen de leeruitkomst geldt: *Voor de kwalificatie operator productietechniek (NLQF niveau 2), technische module*.

## Wat daaruit volgt voor OKx

| Waarneming | Gevolg |
|---|---|
| `Type` verwijst naar de kwalificatie, letterlijk "ten behoeve van de kwalificatie X" | Het is een verwijzing naar het kwalificatiekader, geen beroepsrol |
| Kwalificatie, NLQF-niveau en module staan boven de tabel, buiten de zin | Het niveau is een metagegeven naast de leeruitkomst, geen onderdeel van de formulering |
| De volgorde ligt vast | Actief werkwoord, type, onderwerp, standaard, context |

De negen leeruitkomsten in [`voorbeeld-lr1-regels.json`](../../../../model/informatiemodel/voorbeeld-lr1-regels.json) dragen alle vijf de plekken, met het type achteraan tussen haakjes in plaats van op plek twee:

> Verleent farmaceutische patientenzorg, volgens de vigerende protocollen en met navolgbare vastlegging, in een levensechte apotheekomgeving (apothekersassistent NLQF 4, kerntaak B1-K1)

Die haakjes dragen nu kwalificatie, niveau en herkomst door elkaar. Of het type naar de zin verhuist en het niveau een eigen veld krijgt, staat open in #347.

## Taxonomieen staan naast de leeruitkomst

Meerdere taxonomieen zijn inzetbaar om een leeruitkomst te plaatsen, en zij spreken elkaar niet tegen omdat zij naar iets anders kijken.

| Taxonomie | Wat zij zegt | Voorbeeld: afstellen van apparatuur |
|---|---|---|
| Romiszowski | Soort vaardigheid, en of zij reproductief of productief is | psychomotorisch, reproductief |
| Bloom | Denkniveau | toepassen |
| SOLO | Structuur van het leerresultaat | nog niet uitgewerkt |

Een leeruitkomst draagt daarmee nul of meer paren van taxonomie en niveau. De aanvulbare opsomming `complexityLevel` uit het [gearchiveerde conceptmodel](../../leerroute-uitwerking/doc/archief-conceptmodellen.md) zette de taxonomie in de waarde (`bloom1-6`, `solo0-4`); met Romiszowski erbij, die twee assen kent, loopt dat vast.

Geen van de negen bestaande leeruitkomsten legt een taxonomie vast. Dat is het openstaande gat.

## Het uitgangspunt van de instelling landt in de standaard

Een instelling die duurzaam werken vooropstelt zet dat in de standaard en niet in het werkwoord: het ontwerp versterkt de biodiversiteit en verstoort de bestaande natuurwaarden niet. Duurzaamheid is daar geen handeling maar het criterium waarop het resultaat wordt beoordeeld, en daarmee toetsbaar.

Dat maakt de begrippenfamilie `Onderwijskundig kader instelling` concreet: de standaard is de plek waar de invulling door de instelling de leeruitkomst binnenkomt.

## Nog op te halen

De NLQF-handleiding voor het formuleren van leeruitkomsten uit 2020 en de volledige indeling van Romiszowski zijn nog niet geraadpleegd. Zolang die ontbreken draagt dit document de waarneming en niet de onderbouwing.
