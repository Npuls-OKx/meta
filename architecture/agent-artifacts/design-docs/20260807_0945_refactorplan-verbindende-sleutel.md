# Refactorplan: leeruitkomst als verbindende sleutel

Relateert aan: #138. Kader: [featureplan werkpakket 2](https://github.com/Npuls-OKx/meta/blob/130-onderzoek-business-techniek-koppeling/architecture/agent-artifacts/feature-plans/20260807_0930_refactors-en-uitgangspunten.md).

## Probleem

"Leeruitkomsten als opaque sleutels" (ADR 0023) is voor functionele en businesslezers onbegrijpelijk jargon, en het onderschat de rol van het begrip: de leeruitkomst is de verbindende sleutel die specificaties, keuzeregels, planning, voortgang, resultaten en waardepapieren aan elkaar knoopt. De technische eigenschap (een afnemend systeem hoeft de inhoud van de leeruitkomst niet te kennen om ermee te werken) is een toelichting, geen naam.

## Aanpak

1. **Terminologiebesluit.** Werkrichting: "de leeruitkomst als verbindende sleutel". Toetsen bij de semantiekbewaking (ankertabel: de leeruitkomst is al "de sleutel tussen specificatie, regel en resultaat", dus de nieuwe naam sluit aan op bestaand kader). Vaststellen met het kernteam.
2. **Public.** ADR 0023 herzien of vervangen door een opvolgend besluit met de nieuwe naam (de inhoud blijft: over de koppeling gaan id's en behaald-status). Koppelingspecificatie OC-P&R en de payload-documenten die de term dragen bijwerken. Eigen branch en PR in Npuls-OKx/Public.
3. **Meta.** De boom-feature "Leeruitkomst-id's als opaque sleutels in keuzeregels" hernoemen (na merge van PR 131), plus het begrippenkader in de leerroute-uitwerking en de skill `okx-semantiek-review` als die de term gaat bewaken.
4. **Volgorde.** Eerst het besluit (stap 1 en 2), dan de doorwerking (stap 3); anders lopen de repo's uit de pas.

## Buiten scope

De werking zelf verandert niet: systemen wisselen leeruitkomst-id's en behaald-status uit, zonder de inhoud te hoeven kennen. Al het overige valt buiten scope.

## Verificatie

- `git grep -i "opaque"` in meta en Public levert na afloop alleen historische documenten op (onderzoeksartifacten, meetingverslagen).
- De semantiekreview accepteert de nieuwe term; de tester ziet geen gebroken verwijzingen.

## Status voor volgende sessie

Plan opgesteld; terminologiebesluit is de eerste stap en vraagt een stop met de mens (naamkeuze vaststellen) voordat er iets wordt hernoemd.
