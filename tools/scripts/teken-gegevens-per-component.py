#!/usr/bin/env python3
"""Per applicatiecomponent de gegevens die daar ontstaan, in de vormtaal van een voorbeeldregel.

Waarom dit script bestaat: een interactieketen is pas te begrijpen wanneer vaststaat wie welk
gegeven bezit. Uitgangspunt U3 van OKx legt dat vast als regel (elk systeem is de enige bron
van zijn eigen resource), en een tabel met vier regels proza maakt daar geen beeld van. Deze
plaat zet per component de objecttypen die hij in deze keten ontsluit, gegroepeerd naar de
interactiespecificatie die ze over de lijn brengt. Relateert aan: Npuls-OKx/meta#372.

    python3 tools/scripts/teken-gegevens-per-component.py [--stromen PAD] [--uit PAD]

De gegevens zijn afgeleid, niet ingevoerd
-----------------------------------------
Twee bestanden dragen de inhoud, en geen ervan is voor deze plaat gemaakt:

| Bestand | Wat eruit komt |
|---|---|
| `stromen-onderwijsaanbod.json` van de interactieketen | welke interactiespecificatie welk beeld draagt, en tussen welke componenten zij loopt |
| `voorbeeld-lr1-regels.json` van de voorbeelduitwerking | per beeld de regels `stroomt`, met het bronsysteem en het objecttype |

Een component bezit in deze plaat het objecttype waarvan hij in een regel `stroomt` het
bronsysteem is. Dat is de waarneming uit de voorbeelduitwerking en geen toekenning door dit
script: verschuift een objecttype daar naar een ander systeem, dan verschuift het hier mee.

Een component die in deze keten alleen ontvangt, staat er met die mededeling in plaats van met
een leeg vak. Een leeg vak leest als een gegeven dat vergeten is.

De vormtaal komt van `tools/scripts/teken-voorbeeldregels.py`: een component is blauw met het
componenticoon, een objecttype geel met het objecticoon, in de kleuren die ArchiMate voor de
applicatielaag en de bedrijfslaag aanhoudt.
"""

import argparse
import html
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent
STROMEN = "architecture/docs/specificatie/interactie-onderwijsaanbod/stromen-onderwijsaanbod.json"
REGELS = "architecture/model/informatiemodel/voorbeeld-lr1-regels.json"
UIT = "architecture/docs/specificatie/interactie-onderwijsaanbod/img/gegevens-per-component.svg"

# De vormtaal van teken-voorbeeldregels.py: de applicatielaag blauw, de bedrijfslaag geel.
BUS, BUS_L, BUS_T = "#ffffb5", "#a8a85a", "#5a5a2a"
APP, APP_L, APP_T = "#b5ffff", "#5aa8a8", "#2a5a5a"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#d8ddda"
FONT = "Arial, Helvetica, sans-serif"
ICOON_COMPONENT = ('<rect x="4" y="2" width="10" height="12"/>'
                   '<rect x="2" y="4" width="4" height="2.5"/>'
                   '<rect x="2" y="8.5" width="4" height="2.5"/>')
ICOON_OBJECT = '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>'

KOLOM, MARGE, GOOT = 236, 28, 18
KOPHOOGTE, VAKHOOGTE, REGELHOOGTE = 46, 22, 13
GROEPHOOGTE, TITELHOOGTE = 20, 56


def breedte(tekst, grootte=12, vet=False):
    """Een schatting van de tekstbreedte, genoeg om te weten of een regel past."""
    factor = 0.56 if vet else 0.52
    return len(tekst) * grootte * factor


def knip(tekst, ruimte, grootte=12, regels=2):
    """Een naam over hoogstens `regels` regels verdelen, op woordgrenzen."""
    woorden, uit, huidig = tekst.split(), [], ""
    for woord in woorden:
        kandidaat = f"{huidig} {woord}".strip()
        if huidig and breedte(kandidaat, grootte) > ruimte:
            uit.append(huidig)
            huidig = woord
            if len(uit) == regels:
                break
        else:
            huidig = kandidaat
    if huidig and len(uit) < regels:
        uit.append(huidig)
    if len(uit) == regels and len(" ".join(uit)) < len(tekst):
        uit[-1] = uit[-1][: max(4, len(uit[-1]) - 1)] + "…"
    return uit


def lees(stromen_pad, regels_pad):
    """Per component de objecttypen die hij ontsluit, gegroepeerd per interactiespecificatie."""
    stromen = json.loads(stromen_pad.read_text(encoding="utf-8"))["stromen"]
    regels = json.loads(regels_pad.read_text(encoding="utf-8"))["regels"]
    per_beeld = {s["beeld"]: s for s in stromen if s.get("beeld")}

    componenten, orde = {}, []
    for stroom in stromen:
        for sleutel in ("van", "naar"):
            naam = stroom[sleutel]
            if naam not in componenten:
                componenten[naam] = {}
                orde.append(naam)

    for regel in regels:
        if regel.get("soort") != "stroomt":
            continue
        stroom = per_beeld.get(regel.get("beeld_id"))
        if stroom is None or regel.get("van") not in componenten:
            continue
        aanduiding = stroom["aanduiding"]
        componenten[regel["van"]].setdefault(aanduiding, set()).add(regel["objecttype"])

    namen = {s["aanduiding"]: s.get("naam_kort", s["aanduiding"]) for s in stromen}
    return [(naam, componenten[naam]) for naam in orde], namen


def hoogte_van(groepen):
    """De hoogte die een kolom nodig heeft, met twee regels per objecttype."""
    hoog = KOPHOOGTE + 10
    if not groepen:
        return hoog + GROEPHOOGTE + 8
    for _, types in sorted(groepen.items()):
        hoog += GROEPHOOGTE
        for naam in sorted(types):
            hoog += VAKHOOGTE + (REGELHOOGTE if len(knip(naam, KOLOM - 44)) > 1 else 0) + 5
        hoog += 8
    return hoog


def vak(x, y, b, h, vul, lijn):
    return (f'<rect x="{x}" y="{y}" width="{b}" height="{h}" rx="3" fill="{vul}" '
            f'stroke="{lijn}" stroke-width="1"/>')


def icoon(x, y, pad, kleur):
    return (f'<g transform="translate({x},{y})" fill="none" stroke="{kleur}" '
            f'stroke-width="1.2">{pad}</g>')


def tekst(x, y, s, grootte=12, kleur=INK, vet=False, anker="start"):
    gewicht = ' font-weight="600"' if vet else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{grootte}" '
            f'fill="{kleur}" text-anchor="{anker}"{gewicht}>{html.escape(s)}</text>')


def teken(kolommen, namen, titel):
    """De plaat als SVG: een kolom per component, met zijn objecttypen eronder."""
    breed = MARGE * 2 + len(kolommen) * KOLOM + (len(kolommen) - 1) * GOOT
    hoog = TITELHOOGTE + max(hoogte_van(g) for _, g in kolommen) + MARGE
    delen = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}" '
        f'viewBox="0 0 {breed} {hoog}" role="img">',
        f'<rect width="{breed}" height="{hoog}" fill="#ffffff"/>',
        tekst(MARGE, 30, titel, 16, INK, True),
    ]

    x = MARGE
    for naam, groepen in kolommen:
        y = TITELHOOGTE
        delen.append(vak(x, y, KOLOM, KOPHOOGTE, APP, APP_L))
        delen.append(icoon(x + 10, y + 9, ICOON_COMPONENT, APP_T))
        for i, regel in enumerate(knip(naam, KOLOM - 40, 13)):
            delen.append(tekst(x + 32, y + 20 + i * 15, regel, 13, APP_T, True))
        y += KOPHOOGTE + 10

        if not groepen:
            delen.append(tekst(x + 4, y + 12, "ontvangt, bezit hier niets", 11, MUTED))
            x += KOLOM + GOOT
            continue

        for aanduiding, types in sorted(groepen.items()):
            delen.append(tekst(x + 4, y + 12, f"{aanduiding} {namen.get(aanduiding, '')}".strip(),
                               11, MUTED, True))
            y += GROEPHOOGTE
            for objecttype in sorted(types):
                regels = knip(objecttype, KOLOM - 44)
                h = VAKHOOGTE + (REGELHOOGTE if len(regels) > 1 else 0)
                delen.append(vak(x, y, KOLOM, h, BUS, BUS_L))
                delen.append(icoon(x + 8, y + (h - 14) / 2, ICOON_OBJECT, BUS_T))
                basis = y + (16 if len(regels) > 1 else 15)
                for i, regel in enumerate(regels):
                    delen.append(tekst(x + 28, basis + i * REGELHOOGTE, regel, 12, BUS_T))
                y += h + 5
            y += 8
        x += KOLOM + GOOT

    delen.append(
        tekst(MARGE, hoog - 10,
              "Afgeleid uit voorbeeld-lr1-regels.json: een component bezit het objecttype "
              "waarvan hij het bronsysteem is.", 11, MUTED)
    )
    delen.append("</svg>")
    return "\n".join(delen)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--stromen", default=None, help="het markeerbestand van de keten")
    parser.add_argument("--regels", default=None, help="de voorbeeldregels van de leerroute")
    parser.add_argument("--uit", default=None, help="de svg die geschreven wordt")
    parser.add_argument("--titel", default="Wie bezit welk gegeven in deze keten")
    args = parser.parse_args(argv)

    stromen_pad = pathlib.Path(args.stromen) if args.stromen else WORTEL / STROMEN
    regels_pad = pathlib.Path(args.regels) if args.regels else WORTEL / REGELS
    uit = pathlib.Path(args.uit) if args.uit else WORTEL / UIT
    for pad in (stromen_pad, regels_pad):
        if not pad.is_file():
            print(f"Het bestand {pad} bestaat niet.", file=sys.stderr)
            return 2

    kolommen, namen = lees(stromen_pad, regels_pad)
    if not kolommen:
        print(f"In {stromen_pad.name} staat geen stroom met een component.", file=sys.stderr)
        return 2
    uit.parent.mkdir(parents=True, exist_ok=True)
    uit.write_text(teken(kolommen, namen, args.titel) + "\n", encoding="utf-8")

    pad = str(uit).replace(str(WORTEL) + "/", "")
    print(f"{pad}")
    for naam, groepen in kolommen:
        alle = set().union(*groepen.values()) if groepen else set()
        print(f"  {naam}: {len(alle)} objecttypen over {len(groepen)} interactiespecificaties")
    return 0


if __name__ == "__main__":
    sys.exit(main())
