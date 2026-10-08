# De voorbeelduitwerking van leerroute 1

Deze map draagt het informatiemodel van OKx en de voorbeelduitwerking die erbij hoort: de opleiding van Jochem, stap voor stap door acht fasen, met per stap wie er handelt, welk objecttype ontstaat of stroomt, en met welke waarde.

## Een bron, de rest is uitvoer

Alleen `voorbeeld-lr1-regels.json` wijzigt met de hand. Al het andere wordt eruit gegenereerd en wordt nooit met de hand bijgewerkt, want een handmatige correctie in de uitvoer is bij de volgende generatie weg.

```
voorbeeld-lr1-regels.json         de bron: 262 regels over 8 fasen
voorbeeld-lr1-regels.schema.json  het contract waar elke regel aan moet voldoen
         |
         +--> controleer-voorbeeldregels.py
         |      toetst de bron tegen het informatiemodel en tegen het schema
         |      uitkomst: bevindingen (blokkerend) en signaleringen (een signaal)
         |
         +--> teken-voorbeeldregels.py
         |      maakt per beeld een SVG in ArchiMate-vormtaal
         |      uitvoer: img/
         |
         +--> teken-hoofdplaat-highlight.py
         |      markeert per fase de informatiestromen op de hoofdplaat
         |      uitvoer: img/
         |
         +--> genereer-voorbeeld-lr1.py
                bouwt het document en het invulblad
                uitvoer: voorbeeld-leerroute-1-jochem.md
                         voorbeeld-leerroute-1-jochem-invulblad.md
```

De drie bestanden `informatiemodel.json`, `componenten.json` en `stromen.json` komen uit het ArchiMate-model en zijn de maat waartegen de controle toetst. Het model zelf wijzigt alleen de modelleur in Archi.

## Wat een regel is

Een regel is een stap in het verhaal, en draagt tien velden:

| Veld | Wat erin staat |
|---|---|
| `beeld_id`, `beeld` | Het beeld waar de regel bij hoort, en de titel ervan |
| `fase`, `stap` | Waar in de leerroute de stap valt |
| `soort` | `ontstaat` of `stroomt` |
| `wie` | De rol die handelt, of het component dat verstuurt |
| `objecttype` | Een objecttype uit het informatiemodel |
| `instantie` | De waarde in het voorbeeld, bijvoorbeeld een leeruitkomst voluit |
| `koppeling` | Bij `stroomt`: welke koppelingspecificatie de lijn draagt |
| `bron`, `zin` | Waar de stap op steunt, en de zin in het document |

Uit die regels volgen de beelden en het document. Een beeld is een blok regels met hetzelfde `beeld_id`, en de generator zet er de tekst bij uit `zin`.

## Werkafspraken

Drie afspraken gelden bij deze bron. Zij zijn hier vastgelegd en niet als ADR, omdat zij over een bronbestand in meta gaan en niet over de architectuur van een koppelvlak.

**Het schema is het contract, en het sluit af.** `additionalProperties` staat op `false`, dus een typefout in een veldnaam valt op in plaats van stil door te glippen. Een nieuw veld gaat eerst in het schema en daarna in de bron.

**Een ontbrekend objecttype is een signalering en geen fout.** Noemt het voorbeeld een objecttype dat het informatiemodel nog niet draagt, dan meldt de controle dat met de plek in de lijn en loopt door. Zo blijft het voorbeeld vooruit kunnen lopen op het model, en wordt het verschil een signaal richting de modelronde.

**De bevindingen van een reviewronde leven in de bron.** De sleutel `bevindingen` draagt per bevinding het beeld, de lezer, de datum, de bron, de tekst zoals de lezer die schreef, de thema's en de status `open`, `doorgevoerd` of `geparkeerd`, waarbij een geparkeerde bevinding een reden draagt. Dat wijkt af van de afspraak in [AGENTS.md](../../../AGENTS.md) dat GitHub de bron is voor auteurschap en datums. De reden: alleen zo kan de controle toetsen dat elke bevinding naar een bestaand beeld wijst en dat elk thema bekend is, in plaats van dat een commitbericht belooft dat een bevinding is opgelost. Dit geldt voor een afgeronde reviewronde op deze bron, niet als algemeen patroon.

## Werken aan het voorbeeld

In de dev-container, na elke wijziging aan de bron:

```bash
python3 scripts/controleer-voorbeeldregels.py
python3 scripts/teken-voorbeeldregels.py
python3 scripts/genereer-voorbeeld-lr1.py
python3 -m unittest discover -s tests -p "test_*.py"
```

De werkwijze per fase staat in de skill [`okx-voorbeeld-in-het-informatiemodel`](../../../.agents/skills/okx-voorbeeld-in-het-informatiemodel/SKILL.md).
