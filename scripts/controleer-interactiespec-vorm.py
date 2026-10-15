#!/usr/bin/env python3
"""De vorm van een interactiespecificatie toetsen: beelden voorop, tekst eronder.

Waarom dit script bestaat: een interactiespecificatie wordt opengeslagen door een
informatiemanager die binnen vijf minuten wil weten of zij deze interactie wil, en binnen
vijftien hoe die werkt. Dat vraagt een document dat zich laat bekijken, met de tekst voor de
details die exact moeten zijn. Die eis is een smaakoordeel zolang zij in woorden staat, dus
staat zij hier als maat. Relateert aan: Npuls-OKx/meta#375.

    python3 scripts/controleer-interactiespec-vorm.py [MAP] [--kort]

Zonder argument toetst het script
architecture/docs/specificatie/interactie-onderwijsaanbod.

De vijf maten
-------------

| Maat | Waarom zij er is |
|---|---|
| Elke kop opent met een beeld, een tabel of een diagram | Een kop die met een alinea opent zet de tekst voorop, en dan draagt het beeld het verhaal niet. Een begripsregel mag ervoor: hoogstens vijfenvijftig woorden, ongeveer drie gerenderde regels, en er moet meteen een beeld, tabel of diagram op volgen. Zonder die uitzondering leest een tabel met een vakterm erin als een lijst zonder sleutel |
| Een beeldregel uit de voorbeelduitwerking staat als beeld | Zes verwijzingen naar `img/regels` stonden als link: zij stonden naast het verhaal in plaats van erin. Een uitsnede van de hoofdplaat blijft een link, want die wijst naar een grotere plaat en toont niet wat deze stap oplevert |
| Een leesregel bij een beeld draagt hoogstens twee zinnen | Een leesregel wijst aan waar de lezer naar kijkt; wie meer nodig heeft, legt het beeld uit in plaats van het te laten werken |
| Geen alinea langer dan vijfenzeventig woorden | Dat is ongeveer vijf gerenderde regels, de hoogte waarop een alinea nog in een oogopslag te overzien is |
| Het hoofddocument draagt hoogstens zevenhonderd woorden buiten de tabellen | De vijftienminutenmaat. Detail hoort in een verdieping, waar de tekst volledig mag zijn |

Vier maten gelden voor het hoofddocument. Een verdieping draagt de operaties, de
berichtvelden en het foutgedrag, en daar hoort de tekst volledig te zijn: een berichtsectie
opent er terecht met de regel die haar schema aanwijst. Van de maten geldt daar alleen die
over een beeld als link, want ook in een verdieping staat een beeld liever in het verhaal dan
ernaast.

Exitcodes
---------
0: elke maat is gehaald;
1: ten minste een maat is niet gehaald;
2: de map is niet bruikbaar.
"""

import argparse
import pathlib
import json
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
STANDAARD = "architecture/docs/specificatie/interactie-onderwijsaanbod"
HOOFDDOCUMENT = "README.md"

# De maten. Een maat die verschuift hoort met de reden erbij te verschuiven.
MAX_ZINNEN_LEESREGEL = 2
MAX_WOORDEN_ALINEA = 75
MAX_WOORDEN_BUITEN_TABELLEN = 700
MAX_WOORDEN_BEGRIPSREGEL = 55

BEELDMAPPEN = re.compile(r"img/")
BEELD = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_NAAR_BEELD = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]*img/regels/[^)]*\.(?:svg|png|jpg|jpeg))\)")
ZINEINDE = re.compile(r"[.!?](?:\s|$)")


class Bevinding:
    """Een maat die niet gehaald is, met de plek erbij."""

    def __init__(self, plek, wat):
        self.plek = plek
        self.wat = wat

    def __str__(self):
        return f"{self.plek}: {self.wat}"


def blokken(tekst):
    """De tekst als blokken, met de regelnummers erbij en de codeblokken als geheel.

    Een codeblok gaat als een blok mee, want een diagram erin telt als beeld en de regels
    erbinnen zijn geen alinea.
    """
    uit = []
    regels = tekst.splitlines()
    i = 0
    while i < len(regels):
        if not regels[i].strip():
            i += 1
            continue
        if regels[i].strip().startswith("```"):
            hek = regels[i].strip()[:3]
            j = i + 1
            while j < len(regels) and not regels[j].strip().startswith(hek):
                j += 1
            uit.append({"regel": i + 1, "tekst": "\n".join(regels[i:j + 1]), "soort": "code"})
            i = j + 1
            continue
        j = i
        while j < len(regels) and regels[j].strip():
            j += 1
        blok = "\n".join(regels[i:j])
        eerste = regels[i].strip()
        soort = ("kop" if eerste.startswith("#") else
                 "tabel" if eerste.startswith("|") else
                 "beeld" if eerste.startswith("![") else
                 "lijst" if re.match(r"^([-*]|\d+\.)\s", eerste) else
                 "alinea")
        uit.append({"regel": i + 1, "tekst": blok, "soort": soort})
        i = j
    return uit


def zinnen(tekst):
    """Het aantal zinnen in een alinea, met een afkorting als `v1.7` buiten de telling."""
    schoon = re.sub(r"\[[^\]]*\]\([^)]*\)", "x", tekst)
    schoon = re.sub(r"`[^`]*`", "x", schoon)
    schoon = re.sub(r"\b[a-zA-Z]\.", "x", schoon)
    schoon = re.sub(r"\d+\.\d+", "x", schoon)
    return len([z for z in ZINEINDE.split(schoon) if z.strip()])


def woorden_buiten_tabellen(tekst):
    """De woorden in de alinea's en de lijsten, dus buiten de tabellen, koppen en code."""
    return sum(
        len(b["tekst"].split()) for b in blokken(tekst) if b["soort"] in ("alinea", "lijst")
    )


def mermaid_bevindingen(tekst):
    """Of elk attribuut in een erDiagram een datatype draagt dat mermaid aanneemt.

    De veldtabel schrijft een datatype uit: `enum: ontwerp, vastgesteld` of `string, 36 tekens`.
    Blijft die dubbele punt of komma staan, dan breekt de parser af met "Expecting
    ATTRIBUTE_WORD" en toont GitHub alleen "Unable to render rich display". Dat is goedkoper hier
    te vangen dan met een browser.
    """
    uit = []
    for blok in re.findall(r"```mermaid\n(erDiagram\n.*?)\n```", tekst, re.S):
        binnen = False
        for nr, regel in enumerate(blok.splitlines(), 1):
            gestript = regel.strip()
            if gestript.endswith("{"):
                binnen = True
                continue
            if gestript == "}":
                binnen = False
                continue
            if not binnen or not gestript:
                continue
            woord = gestript.split()[0]
            if not re.fullmatch(r"[A-Za-z0-9_\[\]]+", woord):
                uit.append(f"het datatype {woord!r} in een erDiagram draagt een leesteken dat "
                           f"mermaid niet aanneemt (regel {nr} van het diagram)")
    return uit


def enum_bevindingen(bestand):
    """Of elke enumwaarde uit een aangehaald schema ook in de tekst staat.

    Een codelijst die zowel in een schema als in een tabel leeft, loopt uiteen. Het schema is
    leidend; deze toets kijkt of de tabel compleet is gebleven. Zij draait alleen op de schema's
    waarvan het document zegt dat het hun enum beschrijft, herkenbaar aan de zin die de enum
    aanwijst.
    """
    tekst = bestand.read_text(encoding="utf-8")
    uit = []
    genoemd = set(re.findall(r"^\| `([A-Za-z]+)` \|", tekst, re.M))
    for veld, schema in re.findall(r"enum `properties\.([a-zA-Z]+)` van\s+\[([a-z-]+\.json)\]", tekst):
        pad = bestand.parent / "schemas" / schema
        if not pad.is_file():
            uit.append(f"{schema} wordt aangehaald als bron van een enum maar staat niet in "
                       f"schemas/")
            continue
        try:
            waarden = set(json.loads(pad.read_text(encoding="utf-8"))["properties"][veld]["enum"])
        except (KeyError, ValueError):
            uit.append(f"{schema} draagt geen enum op `properties.{veld}`")
            continue
        for ontbreekt in sorted(waarden - genoemd):
            uit.append(f"de waarde {ontbreekt!r} staat in de enum van {schema} en niet in de "
                       f"tabel die hem beschrijft")
    return uit


def toets_bestand(bestand, hoofddocument):
    """Een markdown-bestand langs de maten, met de bevindingen en de tellingen terug."""
    # Buiten de maten om: een diagram dat niet parseert laat GitHub leeg.
    tekst = bestand.read_text(encoding="utf-8")
    bevindingen = []
    delen = blokken(tekst)

    for index, blok in enumerate(delen):
        if blok["soort"] != "kop" or not hoofddocument:
            continue
        volgende = delen[index + 1] if index + 1 < len(delen) else None
        if volgende is None:
            continue
        if volgende["soort"] == "alinea":
            daarna = delen[index + 2] if index + 2 < len(delen) else None
            woorden = len(volgende["tekst"].split())
            begrip = (woorden <= MAX_WOORDEN_BEGRIPSREGEL
                      and daarna is not None
                      and daarna["soort"] in ("tabel", "beeld", "code"))
            if begrip:
                continue
            kop = blok["tekst"].lstrip("# ").strip()
            reden = (f"deze alinea draagt {woorden} woorden, en een begripsregel mag er "
                     f"{MAX_WOORDEN_BEGRIPSREGEL}"
                     if daarna is not None and daarna["soort"] in ("tabel", "beeld", "code")
                     else "er volgt geen beeld, tabel of diagram op")
            bevindingen.append(Bevinding(
                f"{bestand.name}:{volgende['regel']}",
                f"de kop {kop} opent met een alinea in plaats van een beeld, een tabel of een "
                f"diagram: {reden}",
            ))

    for treffer in LINK_NAAR_BEELD.finditer(tekst):
        regel = tekst[:treffer.start()].count("\n") + 1
        bevindingen.append(Bevinding(
            f"{bestand.name}:{regel}",
            f"{treffer.group(1)} staat als link en niet als beeld, waarmee het beeld naast het "
            f"verhaal staat",
        ))

    beelden = 0
    if hoofddocument:
        for index, blok in enumerate(delen):
            if blok["soort"] != "beeld":
                continue
            beelden += 1
            volgende = delen[index + 1] if index + 1 < len(delen) else None
            if volgende is None or volgende["soort"] != "alinea":
                bevindingen.append(Bevinding(
                    f"{bestand.name}:{blok['regel']}",
                    "dit beeld draagt geen leesregel die aanwijst waar de lezer naar kijkt",
                ))
                continue
            aantal = zinnen(volgende["tekst"])
            if aantal > MAX_ZINNEN_LEESREGEL:
                bevindingen.append(Bevinding(
                    f"{bestand.name}:{volgende['regel']}",
                    f"de leesregel bij dit beeld draagt {aantal} zinnen, en de maat is "
                    f"{MAX_ZINNEN_LEESREGEL}",
                ))

        for blok in delen:
            if blok["soort"] != "alinea":
                continue
            aantal = len(blok["tekst"].split())
            if aantal > MAX_WOORDEN_ALINEA:
                bevindingen.append(Bevinding(
                    f"{bestand.name}:{blok['regel']}",
                    f"deze alinea draagt {aantal} woorden, en de maat is {MAX_WOORDEN_ALINEA}",
                ))

        buiten = woorden_buiten_tabellen(tekst)
        if buiten > MAX_WOORDEN_BUITEN_TABELLEN:
            bevindingen.append(Bevinding(
                bestand.name,
                f"{buiten} woorden buiten de tabellen, en de maat is "
                f"{MAX_WOORDEN_BUITEN_TABELLEN}",
            ))

    for melding in enum_bevindingen(bestand):
        bevindingen.append(Bevinding(bestand.name, melding))

    for melding in mermaid_bevindingen(tekst):
        bevindingen.append(Bevinding(bestand.name, melding))

    return bevindingen, {
        "beelden": len(BEELD.findall(tekst)),
        "buiten_tabellen": woorden_buiten_tabellen(tekst),
        "woorden": len(tekst.split()),
    }


def controleer(map_):
    """Elk markdown-bestand in een map langs de maten."""
    verslagen = []
    for bestand in sorted(map_.glob("*.md")):
        hoofd = bestand.name == HOOFDDOCUMENT
        bevindingen, tellingen = toets_bestand(bestand, hoofd)
        verslagen.append({
            "bestand": bestand.name,
            "hoofddocument": hoofd,
            "bevindingen": bevindingen,
            **tellingen,
        })
    return verslagen


def rapporteer(verslagen, kort):
    """De tellingen per bestand en de bevindingen eronder."""
    alle = []
    for verslag in verslagen:
        alle.extend(verslag["bevindingen"])
        if not kort:
            rol = "hoofddocument" if verslag["hoofddocument"] else "verdieping"
            print(
                f"{verslag['bestand']} ({rol}): {verslag['woorden']} woorden, "
                f"{verslag['buiten_tabellen']} buiten de tabellen, {verslag['beelden']} beelden"
            )
    for bevinding in alle:
        print(f"  niet gehaald: {bevinding}")
    print()
    print(f"{len(verslagen)} bestanden, {len(alle)} maten niet gehaald.")
    return alle


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("map", nargs="?", default=None, help="de map met de interactiespecificatie")
    parser.add_argument("--kort", action="store_true", help="alleen de bevindingen")
    args = parser.parse_args(argv)

    map_ = pathlib.Path(args.map) if args.map else WORTEL / STANDAARD
    if not map_.is_dir():
        print(f"De map {map_} bestaat niet.", file=sys.stderr)
        return 2
    verslagen = controleer(map_)
    if not verslagen:
        print(f"In {map_} staat geen markdown-bestand.", file=sys.stderr)
        return 2
    return 1 if rapporteer(verslagen, args.kort) else 0


if __name__ == "__main__":
    sys.exit(main())
