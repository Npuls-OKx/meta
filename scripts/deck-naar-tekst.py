"""Breng een Slidev-deck terug tot kop en inhoud, als tussenstap naar PowerPoint.

Slidev-decks bestaan grotendeels uit HTML met inline-stijlen, mermaid-diagrammen
en eigen componenten. Dat zijn geen PowerPoint-vormen, dus een export die de
opmaak behoudt levert plaatjes op en geen bewerkbare tekst.

Dit script haalt de opmaak eruit en houdt over wat pandoc wel naar echte
tekstvakken kan schrijven: koppen, opsommingen en tabellen. De diagrammen
vervallen; die haal je met `./deck <naam> beelden` als losse afbeelding op.

Gebruik:
    python3 scripts/deck-naar-tekst.py <deck>.md <uit>.md
"""

import pathlib
import re
import sys

bron = pathlib.Path(sys.argv[1])
doel = pathlib.Path(sys.argv[2])

tekst = bron.read_text(encoding="utf-8")

# Metadatakop en sprekersnotities weg.
tekst = re.sub(r"\A---\n.*?\n---\n", "", tekst, flags=re.S)
tekst = re.sub(r"<!--.*?-->", "", tekst, flags=re.S)

uit = []
for slide in re.split(r"^---$", tekst, flags=re.M):
    regels = []
    for regel in slide.splitlines():
        # Mermaid-blokken vervallen: PowerPoint kan er niets mee.
        if regel.strip().startswith("```"):
            regels.append("```")
            continue
        # HTML-tags eruit, de tekst ertussen blijft.
        schoon = re.sub(r"<[^>]+>", "", regel).strip()
        if schoon:
            regels.append(schoon)
    # Alles binnen een codeblok overslaan.
    binnen, bewaard = False, []
    for regel in regels:
        if regel == "```":
            binnen = not binnen
            continue
        if not binnen:
            bewaard.append(regel)
    if not bewaard:
        continue
    # Zonder kop krijgt de slide er een, anders vouwt pandoc hem samen.
    if not bewaard[0].startswith("#"):
        bewaard.insert(0, "# " + bewaard.pop(0))
    uit.append("\n".join(bewaard))

doel.write_text("\n\n".join(uit) + "\n", encoding="utf-8")
print(f"{len(uit)} slides naar {doel}")
