#!/usr/bin/env python3
"""Bouw een pandoc-referentiebestand uit het Npuls PowerPoint-sjabloon.

Pandoc kan een bestaande PowerPoint als basis nemen voor een bewerkbare export,
maar zoekt daarin lay-outs op vaste Engelse namen. Het Npuls-sjabloon draagt
Nederlandse namen, waardoor pandoc terugvalt op zijn eigen kale standaard en de
huisstijl wegvalt.

Dit script maakt een werkkopie waarin de gekozen Npuls-lay-outs de namen dragen
die pandoc verwacht. Het sjabloon zelf blijft ongemoeid, zodat een nieuwe versie
van Npuls er zonder handwerk overheen kan.

Gebruik:
    python3 scripts/bouw-pandoc-referentie.py

Exitcode 0 = klaar, 1 = probleem gevonden.
"""

import pathlib
import re
import shutil
import sys
import zipfile

WORTEL = pathlib.Path(__file__).resolve().parent.parent
SJABLOON = WORTEL / "presentaties" / "src" / "templates" / "Npuls PPT template 2024.potx"
REFERENTIE = WORTEL / "presentaties" / "src" / "templates" / "npuls-pandoc-referentie.pptx"

# Welke Npuls-lay-out pandoc onder welke naam moet vinden. Pandoc plaatst de
# inhoud op de lay-out die bij de vorm van een slide past; zonder deze namen
# valt hij terug op zijn eigen standaard.
# Een lay-out moet genoeg tekstvakken hebben voor wat pandoc erin zet: Two
# Content en Comparison vragen er meerdere. "Inhoud van twee" draagt ondanks
# zijn naam alleen een titel, vandaar "Stappen" voor de tweekolomsvorm.
KOPPELING = {
    "Title Slide": "Titeldia",
    "Section Header": "Sectiescheider",
    "Title and Content": "Titel en tekst",
    "Two Content": "Stappen",
    "Comparison": "Tekst klein - 2 koloms",
    "Content with Caption": "Tekst en afbeelding 1",
    "Blank": "Einddia",
}

# Een potx is een sjabloon, een pptx een presentatie. Alleen het inhoudstype
# verschilt; de rest van de verpakking is gelijk.
TYPE_SJABLOON = "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
TYPE_PRESENTATIE = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"

RE_NAAM = re.compile(rb'(<p:cSld name=")([^"]*)(")')
# Pandoc herkent een inhoudsvak aan het ontbreken van een type: <p:ph idx="1"/>.
# Het Npuls-sjabloon zet er type="body" of type="obj" bij, waardoor pandoc het
# vak niet vindt en afbreekt. In de hernoemde lay-outs halen we dat type weg.
RE_VAK = re.compile(rb'<p:ph ([^>]*?)type="(?:body|obj)"([^>]*?)/>')


def bouw() -> int:
    if not SJABLOON.exists():
        print(f"Sjabloon niet gevonden: {SJABLOON}", file=sys.stderr)
        return 1

    with zipfile.ZipFile(SJABLOON) as bron:
        namen = bron.namelist()
        inhoud = {naam: bron.read(naam) for naam in namen}

    # Per gezochte pandoc-naam de eerste lay-out met de Npuls-naam omdopen.
    nog_te_doen = dict(KOPPELING)
    hernoemd = {}
    for bestand in sorted(n for n in namen if n.startswith("ppt/slideLayouts/slideLayout")):
        treffer = RE_NAAM.search(inhoud[bestand])
        if not treffer:
            continue
        huidig = treffer.group(2).decode("utf-8")
        for pandoc_naam, npuls_naam in list(nog_te_doen.items()):
            if huidig == npuls_naam:
                gewijzigd = RE_NAAM.sub(
                    lambda m: m.group(1) + pandoc_naam.encode("utf-8") + m.group(3),
                    inhoud[bestand],
                    count=1,
                )
                gewijzigd, vakken = RE_VAK.subn(
                    lambda m: b"<p:ph " + m.group(1) + m.group(2) + b"/>", gewijzigd
                )
                inhoud[bestand] = gewijzigd
                hernoemd[pandoc_naam] = (
                    f"{npuls_naam} ({pathlib.Path(bestand).name}, {vakken} inhoudsvakken)"
                )
                del nog_te_doen[pandoc_naam]
                break

    inhoud["[Content_Types].xml"] = inhoud["[Content_Types].xml"].replace(
        TYPE_SJABLOON.encode("utf-8"), TYPE_PRESENTATIE.encode("utf-8")
    )

    tijdelijk = REFERENTIE.with_suffix(".pptx.nieuw")
    with zipfile.ZipFile(tijdelijk, "w", zipfile.ZIP_DEFLATED) as doel:
        for naam in namen:
            doel.writestr(naam, inhoud[naam])
    shutil.move(tijdelijk, REFERENTIE)

    print(f"Referentie : {REFERENTIE.relative_to(WORTEL)}")
    print(f"Sjabloon   : {SJABLOON.name}")
    print(f"Lay-outs   : {len(hernoemd)} van {len(KOPPELING)} gekoppeld")
    for pandoc_naam, herkomst in sorted(hernoemd.items()):
        print(f"  {pandoc_naam:22} <- {herkomst}")
    for pandoc_naam, npuls_naam in sorted(nog_te_doen.items()):
        print(f"  ONTBREEKT {pandoc_naam}: geen lay-out met de naam {npuls_naam!r}")

    return 1 if nog_te_doen else 0


if __name__ == "__main__":
    sys.exit(bouw())
