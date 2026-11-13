---
name: okx-voorstel-op-de-hoofdplaat
description: Een voorgestelde stroom of wijziging op de hoofdplaat informatiestromen tekenen als uitsnede, zonder het ArchiMate-model te wijzigen. Gebruik wanneer iemand een concept, een comment of een sparvraag op de hoofdplaat wil zien, wanneer een reviewvraag over een lijn tussen twee applicatiecomponenten gaat, en wanneer om een uitsnede van de hoofdplaat wordt gevraagd.
---

# Een voorstel op de hoofdplaat

Een vraag over het landschap gaat bijna altijd over een lijn: loopt het aanbod via de onderwijscatalogus naar het KRS, of rechtstreeks vanaf planning. Zo'n vraag met woorden stellen kost een alinea en levert een misverstand op. Met een beeld kost het een blik.

De verleiding is dan om de lijn in Archi te zetten. Dat is fout: het model wijzigen voor iets wat nog geen besluit is maakt van een vraag een feit, en de volgende lezer ziet een lijn die niemand heeft afgesproken. Een voorstel staat daarom in een eigen bestand naast het model.

## Vaste uitgangspunten

- **Het model wordt alleen gelezen.** Raak nooit een `*.archimate`-bestand aan (harde regel 1 uit [AGENTS.md](../../../AGENTS.md)). Een voorstel staat in `architecture/model/informatiemodel/voorstellen/`.
- **De plaat wordt getekend, niet overgetekend.** Gebruik `teken-hoofdplaat-ruim.py`, dat de plaat uit het model maakt. Een markering over een foto van de ArchiMate-plaat leest als een kras door het beeld heen.
- **Noem altijd de versie van de hoofdplaat.** Een uitsnede zonder versie is over twee weken niet te plaatsen. De wijzer op de uitsnede draagt haar, en de comment eronder noemt haar ook.
- **Een uitsnede draagt een wijzer.** Twee vakken en een lijn zien er overal op de plaat hetzelfde uit; de wijzer rechtsboven toont waar je kijkt.

## De volgorde van de stappen

1. **Schrijf het voorstel.** Een JSON in `architecture/model/informatiemodel/voorstellen/<issue>-<onderwerp>.json`:

   ```json
   {
     "titel": "De vraag die dit voorstel stelt",
     "herkomst": "sessie met datum, en het issue waar de vraag staat",
     "versie": "0.1.0",
     "objecten": [
       {"naam": "Onderwijsaanbod ontsluiten", "soort": "dienst",
        "bij": "Planningssysteem", "kant": "onder"}
     ],
     "stromen": [
       {"van": "Planningssysteem", "naar": "Kernregistratie systeem studenten (KRS)",
        "label": "wat er over die lijn gaat"}
     ]
   }
   ```

   Een voorstel draagt stromen, objecten, of allebei. Een stroom mag naar een voorgesteld vak wijzen; de vakken worden eerst geplaatst.

2. **Teken.**

   ```bash
   python3 tools/scripts/teken-hoofdplaat-ruim.py \
     --voorstel architecture/model/informatiemodel/voorstellen/<naam>.json --uitsnede \
     --uit architecture/model/informatiemodel/img/hoofdplaat/<naam>.svg
   ```

3. **Kijk ernaar.** Zet de SVG om naar een beeld en open het. Een plaat die zonder melding wordt geschreven kan nog steeds het verkeerde zeggen: een lijn naar het verkeerde van twee vakken met dezelfde naam valt alleen op door te kijken.

4. **Hang hem onder het issue**, gepind op een commit, met de versie van de hoofdplaat erbij en de vraag erboven.

## Een vak voorstellen

De renderer leest de plek van elk vak uit de view, en een vak dat daar niet staat heeft geen plek. Een voorstel zegt daarom bij welk vak het hoort en aan welke kant; de plaat rekent de rest uit. Zo hoeft het model geen coordinaten te leveren voor iets wat nog geen besluit is.

| Sleutel | | Wat het doet |
|---|---|---|
| `naam` | verplicht | Staat in het vak, met het woord `voorstel` eronder |
| `bij` | verplicht | De naam van een vak dat wel op de view staat |
| `kant` | `onder` | `onder`, `boven`, `links` of `rechts` van dat vak |
| `soort` | component | `dienst` voor een applicatiedienst |
| `zone` | | Bij twee vakken met dezelfde naam: in welk procesgebied |
| `breedte`, `hoogte` | de buurman, 80 | Alleen wanneer de plek krap is |

Een vak in een druk gebied duwt de namen van de lijnen opzij. Het script zoekt dan een vrije plek verder van de lijn, maar een naam die ver van zijn lijn staat is lastiger te lezen dan een naam ernaast. Kijk dus naar het beeld, en kies een rustiger `kant` of een kleinere `breedte` wanneer het schuift.

## Wat het script bewaakt

| Wat | Waarom |
|---|---|
| Een voorstel zonder `herkomst` | Een lijn zonder herkomst is over een maand niet te plaatsen en wordt stilletjes waarheid |
| Een stroom zonder label | Een lijn zonder label zegt dat er iets stroomt en niet wat |
| Een component dat niet op de view staat | Dan wijst het voorstel naar iets anders dan de lezer denkt |
| Een voorstel zonder stromen en zonder objecten | Dan valt er niets te zien |
| Een object zonder `naam` of `bij`, of met een `kant` die niet bestaat | Dan is de plek een gok |
| Twee componenten in verschillende procesgebieden | Een stroom blijft binnen haar gebied; dat is het verhaal van deze plaat. Een component dat in beide meedoet staat er twee keer op, en `zone` kiest welke |

## De vorm van de comment

Een voorstel komt onder het issue waar de vraag staat, in de vorm uit [okx-product-flow](../okx-product-flow/SKILL.md): koppen van een woord, bullets, en de vragen genummerd onderaan. Vier dingen staan er altijd in.

1. **Het beeld**, met een alt-tekst die zegt wat er te zien is.
2. **De versie van de hoofdplaat** waarop de uitsnede is gemaakt.
3. **De aanroep**, zodat een lezer hem zelf opnieuw kan tekenen.
4. **Wat er nog niet kan**, wanneer de vraag verder gaat dan de lijn.

Vervalt een eerder beeld, trek het dan in met een regel erboven in plaats van het weg te halen. Een lezer die het al had gezien moet kunnen zien dat het is vervangen.

## Wat er nog niet kan

Een relatie tussen twee voorgestelde vakken onderling, en een vak in een procesgebied waar geen enkel bestaand vak staat. Zeg dat erbij in plaats van het te omzeilen met een getekende schets.

De keuring `keur-plaat.py` leest de breedte en de hoogte van het doek en niet het venster van de uitsnede; op een uitsnede meldt zij daardoor tekst buiten het doek. Keur de volle plaat, niet de uitsnede.

## Verwante skills

| Skill | Verhouding |
|---|---|
| [okx-plaat-uit-het-model](../okx-plaat-uit-het-model/SKILL.md) | Tekent de hoofdplaat zelf uit de view-geometrie; deze skill legt er een voorstel overheen |
| [okx-uitsnede-bij-een-reviewvraag](../okx-uitsnede-bij-een-reviewvraag/SKILL.md) | Hetzelfde idee voor het informatiemodel: objecttypen in plaats van applicatiecomponenten |
| [okx-product-flow](../okx-product-flow/SKILL.md) | De vorm van het issue en de comment waar de uitsnede onder hangt |
