---
name: okx-uitsnede-bij-een-reviewvraag
description: Maak een uitsnede van het OKx-informatiemodel die een vraag uit een reviewronde beantwoordt: alleen de objecttypen die de vraag raakt, met de aard van elke wijziging en een ingevuld voorbeeld ernaast. Gebruik wanneer een inbrenger een vraag heeft gesteld over het informatiemodel, wanneer een antwoord onder een issue een beeld verdient, of wanneer de volledige informatiemodelplaat te druk is om een enkel punt mee te maken.
---

# Een uitsnede bij een reviewvraag

De informatiemodelplaat draagt tachtig objecttypen en ruim tweehonderd relaties. Volledig, en onder een issue niet te lezen: een inbrenger moet zelf zoeken waar zijn vraag beantwoord wordt. Een uitsnede toont alleen wat de vraag raakt, met de wijziging uitgelicht en een ingevuld geval ernaast.

De maat waar dit over gaat: een vraag, hoogstens vierentwintig objecttypen, en een beeld dat binnen vijf seconden zijn antwoord prijsgeeft. Voor een vraag die de hele keten raakt is dit het verkeerde gereedschap; die vraagt om de volle plaat of om twee uitsnedes.

## Vaste uitgangspunten

- **Het model is de bron.** De tekenaar leest `architecture/model/informatiemodel/informatiemodel.json`, dat uit het ArchiMate-model gegenereerd wordt. Raak nooit een `*.archimate`-bestand aan (harde regel 1 uit [AGENTS.md](../../../AGENTS.md)); een wijziging in het model maakt de modelleur in Archi.
- **De selectie is het werk, niet de code.** Een uitsnede is een JSON-bestand onder `architecture/model/informatiemodel/uitsneden/`. Het tekenen is een scriptaanroep van een paar seconden, dus hertekenen na een modelronde kost niets.
- **Een beeld beantwoordt een vraag en vat geen hoofdstuk samen.** De titel is de vraag van de inbrenger, letterlijk genoeg dat hij hem herkent.
- **Nul kruisingen.** `tools/scripts/keur-plaat.py --max-kruisingen 0` is de poort. Een kruising betekent dat de rijen of de kolommen anders moeten, niet dat de maat soepeler moet.

## De volgorde van de stappen

1. **Lees de vraag en bepaal het antwoord.** Welke objecttypen en welke relatie dragen het antwoord. Dat is de kern; de rest is context.
2. **Schrijf de selectie.** Titel, herkomst, rijlabels, objecttypen met hun rij.
3. **Teken en keur.**

   ```bash
   python3 tools/scripts/teken-informatiemodel-uitsnede.py \
     --selectie architecture/model/informatiemodel/uitsneden/public-123-minor.json \
     --uit architecture/model/informatiemodel/img/uitsneden/public-123-minor.svg
   python3 tools/scripts/keur-plaat.py <de svg> --max-kruisingen 0
   ```

4. **Kijk ernaar.** Een plaat die de keuring haalt kan nog steeds het verkeerde zeggen. Zet hem om naar een afbeelding en bekijk hem.
5. **Hang hem onder het issue**, gepind op een commit, met het antwoord erboven.

## De relatie die het antwoord draagt mag nooit een verwijzing worden

Dit is de regel die het vaakst misgaat. Het script tekent een relatie als lijn wanneer de twee objecttypen in dezelfde rij staan, of in aangrenzende rijen van dezelfde kolom. Lukt dat niet, dan wordt zij een tekstregel in het vak: `hangt aan Plaatsingsgroep`. Dat is een nette terugval voor context, en een stille fout wanneer juist die relatie het antwoord is.

Bij de vraag of een leeruitkomst het niveau van een competentie uitdrukt liep `Eindkwalificatie` naar `Leeruitkomst` over een kolomgrens en belandde als tekst in een vak, terwijl die relatie de vraag beantwoordde. Door beide in dezelfde rij te zetten werd zij een lijn.

Loop daarom na het tekenen de melding langs. Staat de dragende relatie onder `als verwijzing in het vak`, herschik dan de rijen. De uitweg die het script zelf aanbiedt: geef een objecttype een expliciete `kolom`, dan verlaat het de band boven de kolommen en lopen zijn relaties als lijn.

## Zeg wat er veranderde, niet dat er iets veranderde

Een vak met een accentrand zegt dat er iets gebeurd is. Dat is te weinig: de inbrenger wil weten wat. `merk` draagt daarom een soort, en die soort staat als woord in het vak en opent de uitleg in de legenda.

| merk | In het vak | Wanneer |
|---|---|---|
| `toegevoegd` | `1 toegevoegd` | het objecttype is er deze ronde bij gekomen |
| `verwijderd` | `1 verwijderd` | het is uit het model gehaald; de naam staat er dus niet meer in en de kolom komt uit de selectie |
| `hernoemd` | `1 hernoemd` | dezelfde plek, een andere naam |
| `binnen scope` | `1 binnen scope` | het is binnen de scope van OKx geplaatst |
| `buiten scope` | `1 buiten scope` | het is erbuiten geplaatst |
| `herplaatst` | `1 herplaatst` | het hangt aan een ander objecttype dan eerst |
| `voorstel` | `1 voorstel` | deze uitsnede stelt het voor; het staat nog niet in het model |

`voorstel` is de soort voor het antwoord dat verder gaat dan het model nu draagt. Een reviewvraag eindigt vaak in een objecttype dat ontbreekt, en dat hoort op de plaat te staan als voorstel: wit vak, onderbroken accentrand, met een expliciete `kolom` omdat het model er geen voor kent. De relaties ernaartoe gaan in `ontbreekt`, zodat zij gestippeld lopen.

## Objecttypen zonder kolom staan in een band boven de kolommen

Dertien objecttypen hangen in het model aan geen begrippenfamilie, meestal omdat zij er twee verbinden: een aanmelding verbindt aanbod en verbintenis, een verzoek tot aanbod verbindt specificatie en aanbod. Zij komen in een band over de volle breedte boven de kolomtabs, elk met zijn midden op de grens die het overbrugt.

Twee dingen om te weten. De band trekt geen lijn naar een vak in een kolom; zo'n relatie wordt een verwijzing in het vak. En een bandvak dat niets overbrugt staat er zonder lijn, wat de legenda dan ook zegt. Moet zo'n objecttype wel een lijn hebben, geef het dan een expliciete `kolom`.

## Een voorbeeld is een ingevuld vak, geen eigen kader

Een vraag als "kan een leeruitkomst het niveau van een competentie uitdrukken" is met structuur alleen niet te beantwoorden. Daar hoort een ingevuld geval naast, en dat geval krijgt een eigen blok naast het raster.

Drie regels houden dat blok een voorbeeld.

**Het leent de vormtaal van de plaat.** Een blok met een eigen kolomtab leest als een achtste begrippenfamilie, terwijl het een invulling van een objecttype is. Het draagt daarom de vulling, het pictogram en de naam van een vak, dezelfde taal die `tools/scripts/teken-voorbeeldregels.py` gebruikt voor de instanties van de voorbeelduitwerking. De naam van het vak is het objecttype; waar het voorbeeld vandaan komt staat klein eronder.

**Het hangt aan zijn objecttype.** Een grijze onderbroken lijn met het opschrift `voorbeeld uitwerking` loopt van het vak op het raster naar de voorbeelden, zodat zichtbaar is waarvan zij een invulling zijn. Bij twee voorbeelden stijgt die lijn naar een eigen baan erboven en laat per voorbeeld een stomp zakken.

**Het mag gelaagd zijn.** Onder een voorbeeld past een laag: hetzelfde geval een trap dieper, in een eigen kader, met een specialisatielijn ertussen. Een leeruitkomst draagt een NLQF-niveau; de vaardigheid eronder draagt dat niet, en hoort in CompetentNL thuis. Elke laagregel draagt kader, code en omschrijving.

Twee voorbeelden naast elkaar krijgen dezelfde hoogte voor hun bovenste vak, zodat de rijen op dezelfde lijn liggen en het verschil per rij af te lezen is. Dat is de vorm voor een vraag die een vergelijking is: hetzelfde begrip in twee stelsels, dezelfde ontleding, een andere lat.

## Een voorbeeld zonder herkomst is een verzinsel

Het script weigert een voorbeeld zonder `vindplaats` en een laagregel zonder `code`. Dat is geen formaliteit: een omschrijving zonder identificatie leest als een verwijzing naar een landelijk kader terwijl zij dat niet is, en daar bouwt een leverancier op.

Neem de zin daarom letterlijk over uit een bestand in deze repository of uit een genoemde bron, en zeg in de vindplaats welke. Ontbreekt de bron en moet het werk toch door, merk de laag dan als `voorlopig` met de reden erbij; die reden komt in de accentkleur op het beeld te staan en verdwijnt zodra de echte bron er is. Gebruik dat spaarzaam en nooit zonder dat de opdrachtgever het weet.

## De maten, en waarom zij er zijn

| Maat | Waarde | Waarom |
|---|---|---|
| Objecttypen | hoogstens 24 | daarboven is het geen uitsnede meer; splits de vraag |
| Kolommen, rijen | hoogstens 8 en 6 | |
| Regels onder het beeld | hoogstens 8, legenda meegerekend | wie meer uitleg nodig heeft, moet het beeld veranderen |
| Woorden per leesregel | hoogstens 12 | een regel is een aanwijzing, geen alinea |
| Delen in een voorbeeld | hoogstens 7 | een langere ontleding is een tabel |
| Regels in een laag | hoogstens 6 | |
| Kruisingen | nul | |

De legenda toont alleen de tegels die op dit beeld voorkomen. Een legenda die meer uitlegt dan er staat, laat een lezer zoeken naar iets wat er niet is.

## Na een modelronde

Een modelronde verandert namen, relaties en scope. Hertekenen is een lus over de selectiebestanden en kost seconden:

```bash
for f in architecture/model/informatiemodel/uitsneden/*.json; do
  n=$(basename "$f" .json)
  python3 tools/scripts/teken-informatiemodel-uitsnede.py --selectie "$f" \
    --uit "architecture/model/informatiemodel/img/uitsneden/$n.svg"
done
```

Loop daarna twee dingen na. Een gat dat een uitsnede gestippeld aanwees kan gedicht zijn; haal die regel dan uit `ontbreekt`, anders stippelt het beeld een relatie die er wel is. En een hernoemd objecttype laat het script weigeren met de nieuwe naam erbij, wat precies het signaal is dat de selectie bijwerking vraagt.

## Verwante skills

| Skill | Verhouding |
|---|---|
| [okx-plaat-uit-het-model](../okx-plaat-uit-het-model/SKILL.md) | tekent de informatiestromenplaat uit de view-geometrie; deze skill tekent uit de objecttypen en relaties |
| [okx-voorbeeld-in-het-informatiemodel](../okx-voorbeeld-in-het-informatiemodel/SKILL.md) | de voorbeelduitwerking per fase, waar de vormtaal van de instanties vandaan komt |
| [okx-product-flow](../okx-product-flow/SKILL.md) | de vorm van het antwoord onder het issue waar de uitsnede bij hoort |
