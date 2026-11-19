#!/usr/bin/env python3
"""Tekent het voorstel om BR, FR en TR als eigen artefacten neer te zetten.

Een beslisplaat, geen vervanging van de productafbakening: alleen de artefacten
die de vraag raken, in dezelfde vormtaal, zodat te zien is wat er verandert
wanneer de drie requirementlagen een eigen plek krijgen.

    python3 tools/scripts/teken-requirementsvoorstel.py

Relateert aan: #554, #558
"""

import argparse
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
UIT = (WORTEL / "architecture/agent-artifacts/requirements-in-de-productafbakening"
       / "gegenereerd/img/requirements-als-artefact.svg")

B, H, KOLOM, RIJ = 196, 88, 286, 150
LETTER = "Segoe UI, Arial, sans-serif"
DONKER, GRIJS = "rgb(26, 41, 45)", "rgb(88, 106, 110)"
VLAK = {"domein": "rgb(248, 238, 245)", "solution": "rgb(233, 238, 248)",
        "eind": "rgb(232, 243, 236)"}
BADGE = {"domein": ("rgb(243, 222, 236)", "rgb(140, 70, 115)"),
         "solution": ("rgb(219, 229, 246)", "rgb(40, 75, 140)"),
         "eind": ("rgb(214, 238, 222)", "rgb(26, 105, 60)")}

# Wat er staat: kolom, rij, soort, titel, twee regels uitleg, steekwoorden.
VAKKEN = [
    (0, 0, "domein", "Persona's", "Wie de route loopt", "en wat hem beweegt",
     "naam, situatie, drijfveer", False),
    (1, 0, "domein", "Leerroute scenario", "De route met haar reizen",
     "en processtappen", "reizen, processtappen, rollen", False),
    (2, 0, "domein", "Informatiemodel-", "uitwerking: per stap",
     "wat er ontstaat", "objecttype, relaties, voorbeeld", False),
    (3, 0, "solution", "Interactieketens", "Welke interacties samen",
     "een keten afmaken", "keten, interacties, volgorde", False),
    (0, 1, "domein", "Pakket van eisen", "De user stories uit de",
     "PoC-sessies, geaggregeerd", "nummer, rol, wens, doel", True),
    (1, 1, "domein", "Business requirements", "Wat de instelling moet",
     "kunnen om de story te halen", "eis, story, rol", True),
    (2, 1, "solution", "Functional requirements", "Wat een component moet",
     "doen met welke gegevens", "eis, component, gegeven", True),
    (3, 1, "solution", "Technical requirements", "Wat er over het koppelvlak",
     "gaat en in welke vorm", "eis, bericht, vorm", True),
    (3, 2, "eind", "Koppelvlakspecificaties", "Wat een leverancier bouwt,",
     "per interactieketen", "interacties, schema's, operaties", False),
]

LIJNEN = [
    ((0, 0), (0, 1), "behoeften uit"),
    ((1, 0), (1, 1), "procesbeschrijving"),
    ((2, 0), (2, 1), "gegevenseisen"),
    ((3, 0), (3, 1), "koppelvlakeisen"),
    ((0, 1), (1, 1), "vertaald naar"),
    ((1, 1), (2, 1), "verfijnd tot"),
    ((2, 1), (3, 1), "verfijnd tot"),
    ((3, 1), (3, 2), "getoetst in"),
]


def xy(kolom: int, rij: int) -> tuple[int, int]:
    return 40 + kolom * KOLOM, 60 + rij * RIJ


def tekst(x, y, inhoud, groot=11.5, vet=400, kleur=DONKER, schuin=False):
    stijl = (f"fill:{kleur};font-size:{groot}px;font-weight:{vet};"
             f"font-family:{LETTER}")
    if schuin:
        stijl += ";font-style:italic"
    return (f'<text x="{x}" y="{y}" text-anchor="middle" style="{stijl}">'
            f"{inhoud}</text>")


def vak(kolom, rij, soort, titel, een, twee, steek, nieuw):
    x, y = xy(kolom, rij)
    rand = ("stroke:rgb(221, 120, 75);stroke-width:2.5px"
            if nieuw else "stroke:rgb(255, 255, 255);stroke-width:2px")
    vul, letterkleur = BADGE[soort]
    merk = {"domein": "Domein", "solution": "Solution", "eind": "Eindproduct"}[soort]
    return (
        f'<rect x="{x}" y="{y}" width="{B}" height="{H}" rx="7" '
        f'style="fill:rgb(255,255,255);{rand}"/>'
        f'<rect x="{x + 10}" y="{y + 8}" width="{9 + len(merk) * 6}" height="14" '
        f'rx="7" style="fill:{vul}"/>'
        f'<text x="{x + 14}" y="{y + 18}" style="fill:{letterkleur};'
        f'font-size:9.5px;font-weight:600;font-family:Consolas, monospace">'
        f"{merk}</text>"
        + (tekst(x + B - 22, y + 19, "nieuw", 9.5, 600, "rgb(221, 120, 75)")
           if nieuw else "")
        + tekst(x + B // 2, y + 38, titel, 13, 700)
        + tekst(x + B // 2, y + 53, een)
        + tekst(x + B // 2, y + 66, twee)
        + tekst(x + B // 2, y + 81, steek, 11, 400, GRIJS))


def lijn(van, naar, opschrift, alleen_label=False):
    vx, vy = xy(*van)
    nx, ny = xy(*naar)
    stijl = "fill:none;stroke:rgb(26, 41, 45);stroke-width:1.5px"
    if van[1] != naar[1]:                      # omlaag
        x = vx + B // 2
        pad = f'M{x},{vy + H} L{x},{ny - 6}'
        label = tekst(x + 4, (vy + H + ny) // 2 + 4, opschrift, 11, 400,
                      GRIJS, True)
        label = label.replace('text-anchor="middle"', 'text-anchor="start"')
    else:                                      # naar rechts
        y = vy + H // 2
        pad = f'M{vx + B},{y} L{nx - 6},{y}'
        label = tekst((vx + B + nx) // 2, y - 8, opschrift, 11, 400, GRIJS, True)
    if alleen_label:
        return label
    return f'<path d="{pad}" style="{stijl}" marker-end="url(#punt)"/>' 


def teken() -> str:
    breed = 40 * 2 + 3 * KOLOM + B
    hoog = 60 + 2 * RIJ + H + 56
    delen = [
        f'<svg viewBox="0 0 {breed} {hoog}" width="{breed}" height="{hoog}" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Voorstel: business, functional en technical requirements '
        'als eigen artefacten, met de bron waaruit elk voortkomt">',
        '<defs><marker id="punt" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" style="fill:rgb(26, 41, 45)"/>'
        "</marker></defs>",
        f'<rect width="{breed}" height="{hoog}" style="fill:rgb(255,255,255)"/>',
        tekst(breed // 2, 32,
              "Voorstel: de drie requirementlagen als eigen artefact", 14, 700),
    ]
    delen += [lijn(a, b, t) for a, b, t in LIJNEN]
    delen += [vak(*v) for v in VAKKEN]
    delen += [lijn(a, b, t, alleen_label=True) for a, b, t in LIJNEN]
    delen.append(tekst(breed // 2, hoog - 18,
                       "Een vak met een oranje rand bestaat nog niet; de "
                       "pijl zegt waar de eis vandaan komt.", 11, 400, GRIJS,
                       True))
    return "\n".join(delen) + "\n</svg>\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--uit", type=pathlib.Path, default=UIT)
    a = p.parse_args(argv)
    a.uit.parent.mkdir(parents=True, exist_ok=True)
    a.uit.write_text(teken(), encoding="utf-8")
    print(f"  {a.uit.relative_to(WORTEL)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
