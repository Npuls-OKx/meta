#!/usr/bin/env python3
"""Tekent waar de eisen van OKx ontstaan en waar zij landen.

Een beslisplaat, geen vervanging van de productafbakening: links de producten
die de eisen voeden, rechts de keten van eis naar koppelvlakspecificatie.

    python3 tools/scripts/teken-requirementsvoorstel.py

Relateert aan: #554, #558
"""

import argparse
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
UIT = (WORTEL / "architecture/agent-artifacts/requirements-in-de-productafbakening"
       / "gegenereerd/img/requirements-als-artefact.svg")

B, H = 224, 112
LINKS, RECHTS, TOP, RIJ = 40, 420, 76, 158
BUS = LINKS + B + 48          # de verzamelbaan links
LUS = RECHTS + B + 46         # de lus rechts, voor een overslag
LETTER = "Segoe UI, Arial, sans-serif"
DONKER, GRIJS, ACCENT = "rgb(26, 41, 45)", "rgb(88, 106, 110)", "rgb(221, 120, 75)"
BADGE = {"domein": ("rgb(243, 222, 236)", "rgb(140, 70, 115)", "Domein"),
         "solution": ("rgb(219, 229, 246)", "rgb(40, 75, 140)", "Solution"),
         "eind": ("rgb(214, 238, 222)", "rgb(26, 105, 60)", "Eindproduct")}

# kolom, rij, soort, titelregels (met | gescheiden), uitleg, steekwoorden, nieuw
VAKKEN = [
    ("l", 0, "domein", "PoC-inbreng", "De gewenste user stories van de "
     "koploperinstellingen", "instelling, story, bron", True),
    ("l", 1, "domein", "Persona's", "Wie de route loopt en wat hem beweegt",
     "naam, situatie, drijfveer", False),
    ("l", 2, "domein", "Leerroute scenario", "De route met haar reizen en "
     "processtappen", "reizen, processtappen, rollen", False),
    ("l", 3, "domein", "Leerroute scenario uitwerking|in het informatiemodel",
     "Per processtap wat er ontstaat",
     "objecttype, relaties, voorbeeld", False),
    ("r", 1, "domein", "Instellingseisen", "Wat een instelling wil kunnen "
     "om de scenario's te realiseren", "eis, bron, rol", True),
    ("r", 2, "solution", "Functionele eisen", "Wat een component moet doen "
     "met welke gegevens", "eis, bron, component", True),
    ("r", 3, "solution", "Interactieketens", "Welke interacties samen een "
     "keten afmaken", "keten, interacties, volgorde", False),
    ("r", 4, "solution", "Technische eisen|aan interacties", "Wat er over het "
     "koppelvlak gaat", "eis, bericht, vorm", True),
    ("r", 5, "eind", "Koppelvlakspecificaties", "Wat een leverancier bouwt, "
     "per interactieketen", "interacties, schema's, operaties", False),
]


def xy(kolom: str, rij: int) -> tuple[int, int]:
    return (LINKS if kolom == "l" else RECHTS), TOP + rij * RIJ


def tekst(x, y, inhoud, groot=11.5, vet=400, kleur=DONKER, schuin=False,
          anker="middle", letter=LETTER):
    stijl = (f"fill:{kleur};font-size:{groot}px;font-weight:{vet};"
             f"font-family:{letter}")
    if schuin:
        stijl += ";font-style:italic"
    return (f'<text x="{x}" y="{y}" text-anchor="{anker}" style="{stijl}">'
            f"{inhoud}</text>")


def omwikkel(zin: str, breed: int = 30) -> list[str]:
    regels, nu = [], ""
    for woord in zin.split():
        if len(nu) + len(woord) + 1 > breed:
            regels.append(nu)
            nu = woord
        else:
            nu = f"{nu} {woord}".strip()
    if nu:
        regels.append(nu)
    return regels


def vak(kolom, rij, soort, titel, uitleg, steek, nieuw):
    x, y = xy(kolom, rij)
    rand = (f"stroke:{ACCENT};stroke-width:2.5px" if nieuw
            else "stroke:rgb(214, 220, 226);stroke-width:1.5px")
    vul, letterkleur, merk = BADGE[soort]
    koppen = titel.split("|")
    uit = [
        f'<rect x="{x}" y="{y}" width="{B}" height="{H}" rx="7" '
        f'style="fill:rgb(255,255,255);{rand}"/>',
        f'<rect x="{x + 10}" y="{y + 8}" width="{12 + len(merk) * 6}" '
        f'height="14" rx="7" style="fill:{vul}"/>',
        tekst(x + 16, y + 18, merk, 9.5, 600, letterkleur, anker="start",
              letter="Consolas, monospace"),
    ]
    if nieuw:
        uit.append(tekst(x + B - 14, y + 18, "nieuw", 9.5, 600, ACCENT,
                         anker="end"))
    regel = y + 36
    for kop in koppen:
        uit.append(tekst(x + B // 2, regel, kop, 13, 700))
        regel += 15
    regel += 2
    for stuk in omwikkel(uitleg, 30):
        uit.append(tekst(x + B // 2, regel, stuk))
        regel += 13
    if regel > y + H - 14:
        raise SystemExit(f"de tekst van {koppen[0]!r} loopt uit het vak")
    uit.append(tekst(x + B // 2, y + H - 10, steek, 11, 400, GRIJS))
    return "".join(uit)


def pad(d: str, stippel: bool = False) -> str:
    stijl = f"fill:none;stroke:{DONKER};stroke-width:1.5px"
    if stippel:
        stijl += ";stroke-dasharray:5px, 4px"
    return f'<path d="{d}" style="{stijl}" marker-end="url(#punt)"/>'


def kaal(d: str) -> str:
    return (f'<path d="{d}" style="fill:none;stroke:{DONKER};'
            'stroke-width:1.5px"/>')


def teken() -> str:
    breed = LUS + 40
    hoog = TOP + 5 * RIJ + H + 54
    delen = [
        f'<svg viewBox="0 0 {breed} {hoog}" width="{breed}" height="{hoog}" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Links de producten die de eisen voeden, rechts de keten '
        'van instellingseisen via functionele eisen en interactieketens naar '
        'technische eisen en de koppelvlakspecificatie">',
        '<defs><marker id="punt" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" style="fill:{DONKER}"/>'
        "</marker></defs>",
        f'<rect width="{breed}" height="{hoog}" style="fill:rgb(255,255,255)"/>',
        tekst(breed // 2, 36, "Waar de eisen ontstaan en waar zij landen",
              15, 700),
    ]

    # De eerste drie producten definieren samen de instellingseisen.
    for rij in (0, 1, 2):
        x, y = xy("l", rij)
        delen.append(kaal(f"M{x + B},{y + H // 2} L{BUS},{y + H // 2}"))
    delen.append(kaal(f"M{BUS},{xy('l', 0)[1] + H // 2} "
                      f"L{BUS},{xy('l', 2)[1] + H // 2}"))
    doel = xy("r", 1)
    delen.append(pad(f"M{BUS},{doel[1] + H // 2} L{doel[0] - 6},{doel[1] + H // 2}"))
    delen.append(tekst(doel[0] - 14, doel[1] + H // 2 - 9, "definieren samen",
                       11, 400, GRIJS, True, "end"))

    # De uitwerking voedt de functionele eisen en de interactieketens.
    ux, uy = xy("l", 3)
    fx, fy = xy("r", 2)
    delen.append(pad(f"M{ux + B},{uy + 24} L{BUS + 24},{uy + 24} "
                     f"Q{BUS + 30},{uy + 24} {BUS + 30},{uy + 18} "
                     f"L{BUS + 30},{fy + H // 2 + 6} "
                     f"Q{BUS + 30},{fy + H // 2} {BUS + 36},{fy + H // 2} "
                     f"L{fx - 6},{fy + H // 2}"))
    kx, ky = xy("r", 3)
    delen.append(pad(f"M{ux + B},{ky + H // 2} L{kx - 6},{ky + H // 2}"))
    delen.append(tekst((ux + B + kx) // 2, ky + H // 2 - 9, "voedt",
                       11, 400, GRIJS, True))

    # De keten rechts, van boven naar beneden.
    for van, naar, opschrift in ((1, 2, "samen met de uitwerking"),
                                 (2, 3, "samen met de instellingseisen"),
                                 (3, 4, "leiden tot")):
        x, y = xy("r", van)
        delen.append(pad(f"M{x + B // 2},{y + H} L{x + B // 2},{xy('r', naar)[1] - 6}"))
        delen.append(tekst(x + B // 2 + 10, y + H + 27, opschrift, 11, 400,
                           GRIJS, True, "start"))

    # De instellingseisen slaan de functionele eisen over en voeden ook de keten.
    ix, iy = xy("r", 1)
    delen.append(pad(f"M{ix + B},{iy + 28} L{LUS - 6},{iy + 28} "
                     f"Q{LUS},{iy + 28} {LUS},{iy + 34} "
                     f"L{LUS},{ky + H // 2 - 6} "
                     f"Q{LUS},{ky + H // 2} {LUS - 6},{ky + H // 2} "
                     f"L{kx + B + 6},{ky + H // 2}"))

    # De technische eisen zijn onderdeel van de koppelvlakspecificatie.
    tx, ty = xy("r", 4)
    delen.append(pad(f"M{tx + B // 2},{ty + H} L{tx + B // 2},{xy('r', 5)[1] - 6}",
                     True))
    delen.append(tekst(tx + B // 2 + 10, ty + H + 27, "onderdeel van", 11, 400,
                       GRIJS, True, "start"))

    delen += [vak(*v) for v in VAKKEN]
    delen.append(tekst(breed // 2, hoog - 18,
                       "Een vak met een oranje rand bestaat nog niet.",
                       11, 400, GRIJS, True))
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
