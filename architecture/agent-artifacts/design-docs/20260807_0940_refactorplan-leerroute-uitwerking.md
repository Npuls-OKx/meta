# Refactorplan: van consumer-profiel naar leerroute-uitwerking

Relateert aan: #137. Kader: [featureplan werkpakket 1](https://github.com/Npuls-OKx/meta/blob/130-onderzoek-business-techniek-koppeling/architecture/agent-artifacts/feature-plans/20260807_0930_refactors-en-uitgangspunten.md).

## Probleem

De naam "OKx OEAPI consumer-profiel" beschrijft het document niet. Wat er staat is een gedetailleerde leerroute-uitwerking volgens de AMIGO-aanpak: begrippen, actoren, scenario's, betrokken systemen, informatie, data en interacties tussen systemen via informatiestromen. De naam zet bovendien de techniekkeuze (OEAPI) voorop, terwijl het principe is: eisen eerst, techniekkeuze daarna (#139). En de naam verhult dat de uitwerking op leerroute 1 is gebaseerd, wat lezers laat aannemen dat er buiten LR1 geen requirements bestaan.

## Aanpak

1. **Naam en plek.** Map `architecture/docs/specificatie/okx-oeapi-consumer-profiel/` wordt `architecture/docs/specificatie/leerroute-uitwerking/`; het hoofddocument krijgt een naam zonder datumprefix en zonder OEAPI in de titel (werknaam `leerroute-uitwerking-lr1.md`). Hernoemen met `git mv` zodat de historie meegaat.
2. **Inleiding herschrijven.** Drie boodschappen: dit is de leerroute-uitwerking volgens AMIGO (stap 1 tot en met 3: scenario-analyse, gegevensanalyse, interactie-analyse); LR1 is uitgewerkt en LR2/3 volgen als delta; dat de uitwerking LR1-gebaseerd is betekent niet dat er geen requirements op LR2/3-vlakken bestaan. De OEAPI-mapping (huidige §5, §6, §13, §14) wordt gepositioneerd als vertaling, niet als vertrekpunt.
3. **Verwijzingen bijwerken.** Alle vindplaatsen van het pad en de term "consumer-profiel": de requirementsboom (bronkolommen en leeswijzer), `AGENTS.md` (aannames en scenario-regel), de skills `okx-oeapi-scenario-uitwerking`, `business-analyse-okx` en `okx-semantiek-review`, `doc/OKx_Projectoverzicht.md` en de meetingverslag-README's. Mechanische controle: `git grep -l "consumer-profiel\|okx-oeapi-consumer-profiel"` moet na afloop alleen historische documenten (meetingverslagen, onderzoeksartifacten) opleveren, met daar een redirectnoot waar nodig.
4. **Opknippen.** Het document (4.520 regels) draagt meer dan één doel. Splitskandidaten, elk een bestand met een doel: begrippenkader en ankertabel (§3.2), scenario-uitwerkingen (§3.4), informatiemodel en catalogus (§12), OEAPI-vertaling (§5, §6, §13, §14), interactiepatronen en sequentiediagrammen (§15 tot en met §19). De leeswijzer van de requirementsboom en de sectie-ankers in de bronkolommen bewegen mee.
5. **Reviews.** Product-flow: requirements voor de refactor (klein: naamgeving, splitsingsgrenzen, geen inhoudsverlies), uitvoering, onafhankelijke tester- en semantiekreview, `validate-docs.py` schoon op de hele repo.

## Buiten scope

Inhoudelijke wijziging van scenario's, begrippen of de OEAPI-mapping zelf. Al het overige valt buiten scope.

## Verificatie

- `python3 scripts/validate-docs.py .` zonder bevindingen; geen dode paden naar de oude mapnaam.
- De requirementsboom-bronlinks resolven naar de nieuwe bestanden met dezelfde sectie-ankers of bijgewerkte ankers.
- Een lezer die alleen de nieuwe inleiding leest weet: AMIGO-positionering, LR1-basis, LR2/3-delta, eisen eerst.

## Status voor volgende sessie

Plan opgesteld; uitvoering nog niet gestart. Eerste stap bij oppakken: naamgeving en splitsingsgrenzen laten vaststellen (stop met de mens), daarna stap 1 en 3 in één commit per verwijzingscluster.
