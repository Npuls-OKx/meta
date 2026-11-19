#!/usr/bin/env python3
"""Tekent waar de eisen van OKx ontstaan en waar zij landen.

Een beslisplaat, geen vervanging van de productafbakening: links de producten
die eisen opleveren, rechts de drie soorten eisen, in dezelfde vormtaal.

    python3 tools/scripts/teken-requirementsvoorstel.py

Relateert aan: #554, #558
"""

import argparse
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
UIT = (WORTEL / "architecture/agent-artifacts/requirements-in-de-productafbakening"
       / "gegenereerd/img/requirements-als-artefact.svg")

B, H = 212, 86
LINKS, RECHTS, TOP, RIJ = 40, 400, 72, 116
BUS = LINKS + B + 56
LETTER = "Segoe UI, Arial, sans-serif"
DONKER, GRIJS, ACCENT = "rgb(26, 41, 45)", "rgb(88, 106, 110)", "rgb(221, 120, 75)"
BADGE = {"domein": ("rgb(243, 222, 236)", "rgb(140, 70, 115)", "Domein"),
         "solution": ("rgb(219, 229, 246)", "rgb(40, 75, 140)", "Solution"),
         "eind": ("rgb(214, 238, 222)", "rgb(26, 105, 60)", "Eindproduct")}

# kolom, rij, soort, titel, twee regels uitleg, steekwoorden, is nieuw
VAKKEN = [
    ("l", 0, "domein", "PoC-inbreng", "De gewenste user stories",
     "van de koploperinstellingen", "instelling, story, bron", True),
    ("l", 1, "domein", "Persona's", "Wie de route loopt",
     "en wat hem beweegt", "naam, situatie, drijfveer", False),
    ("l", 2, "domein", "Leerroute scenario", "De route met haar reizen",
     "en processtappen", "reizen, processtappen, rollen", False),
    ("l", 3, "domein", "Leerroute scenario", "uitwerking: de route in",
     "het informatiemodel", "objecttype, relaties, voorbeeld", False),
    ("l", 4, "solution", "Interactieketen", "en interacties: wat er",
     "over de lijn gaat", "bericht, vorm, foutpad", False),
    ("r", 1, "domein", "Instellingseisen", "Wat de instelling moet",
     "kunnen om de route te draaien", "eis, bron, rol", True),
    ("r", 3, "solution", "Functionele eisen", "Wat een component moet",
     "doen met welke gegevens", "eis, bron, component", True),
    ("r", 4, "solution", "Technische eisen", "Wat er over het koppelvlak",
     "gaat en in welke vorm", "eis, bericht, vorm", True),
    ("r", 5, "eind", "Koppelvlakspecificaties", "Wat een leverancier bouwt,",
     "per interactieketen", "interacties, schema's, operaties", False),
]


def xy(kolom: str, rij: int) -> tuple[int, int]:
    return (LINKS if kolom == "l" else RECHTS), TOP + rij * RIJ


def tekst(x, y, inhoud, groot=11.5, vet=400, kleur=DONKER, schuin=False,
          anker="middle"):
    stijl = (f"fill:{kleur};font-size:{groot}px;font-weight:{vet};"
             f"font-family:{LETTER}")
    if schuin:
        stijl += ";font-style:italic"
    return (f'<text x="{x}" y="{y}" text-anchor="{anker}" style="{stijl}">'
            f"{inhoud}</text>")


def vak(kolom, rij, soort, titel, een, twee, steek, nieuw):
    x, y = xy(kolom, rij)
    rand = (f"stroke:{ACCENT};stroke-width:2.5px" if nieuw
            else "stroke:rgb(214, 220, 226);stroke-width:1.5px")
    vul, letterkleur, merk = BADGE[soort]
    return (
        f'<rect x="{x}" y="{y}" width="{B}" height="{H}" rx="7" '
        f'style="fill:rgb(255,255,255);{rand}"/>'
        f'<rect x="{x + 10}" y="{y + 8}" width="{12 + len(merk) * 6}" '
        f'height="14" rx="7" style="fill:{vul}"/>'
        + tekst(x + 16, y + 18, merk, 9.5, 600, letterkleur, anker="start")
          .replace(LETTER, "Consolas, monospace")
        + (tekst(x + B - 14, y + 18, "nieuw", 9.5, 600, ACCENT, anker="end")
           if nieuw else "")
        + tekst(x + B // 2, y + 37, titel, 13, 700)
        + tekst(x + B // 2, y + 52, een)
        + tekst(x + B // 2, y + 65, twee)
        + tekst(x + B // 2, y + 79, steek, 11, 400, GRIJS))


def lijn(pad: str, opschrift="", lx=0, ly=0, stippel=False, anker="middle"):
    stijl = f"fill:none;stroke:{DONKER};stroke-width:1.5px"
    if stippel:
        stijl += ";stroke-dasharray:5px, 4px"
    uit = f'<path d="{pad}" style="{stijl}" marker-end="url(#punt)"/>'
    if opschrift:
        uit += tekst(lx, ly, opschrift, 11, 400, GRIJS, True, anker)
    return uit


def teken() -> str:
    breed = RECHTS + B + 40
    hoog = TOP + 5 * RIJ + H + 56
    delen = [
        f'<svg viewBox="0 0 {breed} {hoog}" width="{breed}" height="{hoog}" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Links de producten die eisen opleveren, rechts de drie '
        'soorten eisen: instellingseisen, functionele eisen en technische '
        'eisen">',
        '<defs><marker id="punt" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" style="fill:{DONKER}"/>'
        "</marker></defs>",
        f'<rect width="{breed}" height="{hoog}" style="fill:rgb(255,255,255)"/>',
        tekst(breed // 2, 34, "Waar de eisen ontstaan en waar zij landen",
              14.5, 700),
        tekst(LINKS + B // 2, 56, "levert eisen op", 11, 400, GRIJS, True),
        tekst(RECHTS + B // 2, 56, "de eis zelf", 11, 400, GRIJS, True),
    ]

    # De eerste drie producten voeden samen de instellingseisen.
    doel = xy("r", 1)
    for rij in (0, 1, 2):
        x, y = xy("l", rij)
        delen.append(
            f'<path d="M{x + B},{y + H // 2} L{BUS},{y + H // 2}" '
            f'style="fill:none;stroke:{DONKER};stroke-width:1.5px"/>')
    boven, onder = xy("l", 0)[1] + H // 2, xy("l", 2)[1] + H // 2
    delen.append(f'<path d="M{BUS},{boven} L{BUS},{onder}" '
                 f'style="fill:none;stroke:{DONKER};stroke-width:1.5px"/>')
    delen.append(lijn(f"M{BUS},{doel[1] + H // 2} L{doel[0] - 6},{doel[1] + H // 2}",
                      "samen", BUS + 26, doel[1] + H // 2 - 8))

    # De andere twee leveren elk hun eigen soort.
    for rij in (3, 4):
        x, y = xy("l", rij)
        r = xy("r", rij)
        delen.append(lijn(f"M{x + B},{y + H // 2} L{r[0] - 6},{y + H // 2}",
                          "levert", (x + B + r[0]) // 2, y + H // 2 - 8))

    # De technische eisen zijn onderdeel van de koppelvlakspecificatie.
    x, y = xy("r", 4)
    delen.append(lijn(f"M{x + B // 2},{y + H} L{x + B // 2},{xy('r', 5)[1] - 6}",
                      "onderdeel van", x + B // 2 + 6, y + H + 22, True, "start"))

    # De inbreng voedt zowel de persona's als het scenario.
    px, py = xy("l", 0)
    delen.append(lijn(f"M{px + B // 2},{py + H} L{px + B // 2},{xy('l', 1)[1] - 6}",
                      "voedt", px + B // 2 + 6, py + H + 20, anker="start"))
    delen.append(lijn(
        f"M{px},{py + H - 18} L{px - 22},{py + H - 18} "
        f"Q{px - 28},{py + H - 18} {px - 28},{py + H - 12} "
        f"L{px - 28},{xy('l', 2)[1] + 30} "
        f"Q{px - 28},{xy('l', 2)[1] + 36} {px - 22},{xy('l', 2)[1] + 36} "
        f"L{px - 6},{xy('l', 2)[1] + 36}", ""))

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
