#!/usr/bin/env python3
"""Welke applicatiecomponent welke koppelvlakdienst aanbiedt of afneemt, als plaat.

Waarom dit script bestaat: een applicatiecomponent is lastig af te bakenen. Welke
functionaliteit bij een onderwijscatalogus hoort en welke bij een kernregistratie is een vraag
waarover zelden overeenstemming bestaat, en een leverancier draagt die twee soms in een
product. De dienst lost dat op: [de dienstenlijst](
https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties/Applicatiediensten) zegt
dat een dienst vastlegt wat er moet kunnen en niet welk systeem het doet, en dat elk component
hem kan claimen. Een leverancier legt zijn product dan op de dienstlaag in plaats van op de
componentlaag. Relateert aan: Npuls-OKx/meta#372.

    python3 scripts/teken-dienstenmatrix.py [--keten PAD] [--uit PAD] [--kort]

De plaat zet de diensten in rijen en de componenten in kolommen. Een vak zegt of het component
die dienst aanbiedt of afneemt, met de stand erbij: vastgelegd in Npuls-OKx/Public, of een
voorstel van deze keten.

De aanbieder en de afnemer zijn twee diensten
---------------------------------------------
De dienstenlijst houdt ze uit elkaar: wie een gegeven levert implementeert de aanbieder, wie
het gebruikt de afnemer. Beide zijn zelfstandig te claimen en zelfstandig te versioneren. De
plaat zet ze daarom naast elkaar in een rij, zodat per dienst te zien is wie levert en wie
afneemt.

Wat de controle meldt
---------------------
Een dienst die deze keten claimt en die de dienstenlijst niet kent, is een voorstel en staat
als zodanig op de plaat. Een dienstnaam met een toevoeging erachter is geen dienst maar
dezelfde dienst die twee keer wordt ingezet, en dat meldt het script.
"""

import argparse
import collections
import html
import pathlib
import re
import subprocess
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
KETEN = "architecture/docs/specificatie/interactie-onderwijsaanbod/README.md"
UIT = "architecture/docs/specificatie/interactie-onderwijsaanbod/img/dienstenmatrix.svg"
PUBLIC = pathlib.Path("/workspaces/OKx/Public")
DIENSTENLIJST = "Koppelvlakspecificaties/Applicatiediensten/README.md"
COMMIT = "d0c20d99"

APP, APP_L, APP_T = "#b5ffff", "#5aa8a8", "#2a5a5a"
BIEDT, NEEMT = "#cfe8d4", "#e8dfc8"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#d8ddda"
FONT = "Arial, Helvetica, sans-serif"

RIJ, KOLOM, NAAMBREEDTE, KOP = 30, 152, 300, 92


def breedte(tekst, grootte=12, vet=False):
    return len(tekst) * grootte * (0.56 if vet else 0.52)


def dienstenlijst():
    """De dienstonderwerpen die Npuls-OKx/Public vastlegt, van het vastgezette commit."""
    uit = subprocess.run(["git", "show", f"{COMMIT}:{DIENSTENLIJST}"],
                         capture_output=True, text=True, cwd=PUBLIC)
    if uit.returncode != 0:
        return set()
    namen = set()
    for regel in uit.stdout.splitlines():
        if not regel.strip().startswith("|"):
            continue
        for naam in re.findall(r"\[([a-z0-9-]+)\]\([a-z0-9-]+-(?:aanbieder|afnemer)\.md\)", regel):
            namen.add(naam)
    return namen


def claims(pad):
    """Per component de diensten die de keten claimt, met de rol en de stand."""
    tekst = pad.read_text(encoding="utf-8")
    begin = tekst.index("## 4. Koppelvlakdiensten")
    blok = tekst[begin:tekst.index("\n## ", begin + 10)]
    uit, kolommen = [], None
    for regel in blok.splitlines():
        g = regel.strip()
        if not g.startswith("|"):
            continue
        cellen = [c.strip() for c in g.split("|")[1:-1]]
        if kolommen is None:
            kolommen = [c.lower() for c in cellen]
            continue
        if set(g) <= set("|- :") or len(cellen) < 4:
            continue
        component, dienst, endpoints, stand = cellen[0], cellen[1], cellen[2], cellen[3]
        toevoeging = ""
        if "," in dienst:
            dienst, toevoeging = dienst.split(",", 1)
            dienst, toevoeging = dienst.strip(), toevoeging.strip()
        rol = ("aanbieder" if dienst.endswith("-aanbieder")
               else "afnemer" if dienst.endswith("-afnemer") else "")
        onderwerp = re.sub(r"-(aanbieder|afnemer)$", "", dienst)
        uit.append({"component": component, "onderwerp": onderwerp, "rol": rol,
                    "dienst": dienst, "endpoints": endpoints, "stand": stand,
                    "toevoeging": toevoeging})
    return uit


def voorstellen_van(rijen, bekend):
    """De diensten die deze keten claimt en die de dienstenlijst nog niet kent."""
    if not bekend:
        return []
    return sorted({r["onderwerp"] for r in rijen if r["onderwerp"] not in bekend})


def bevindingen_van(rijen, bekend):
    """Wat er in de claims niet aansluit, en wat er binnen de keten ontbreekt.

    Een voorgestelde dienst telt hier niet mee: dat is een stand en geen fout. Wat wel meetelt
    is een dienst die wordt afgenomen zonder aanbieder, een dienst die wordt aangeboden zonder
    afnemer, en een dienstnaam die niet zegt wie wat levert.
    """
    uit = []
    # Een dienst die wordt afgenomen zonder aanbieder is een gat in de keten, en andersom.
    rollen = collections.defaultdict(set)
    for r in rijen:
        rollen[r["onderwerp"]].add(r["rol"])
    for onderwerp, gevonden in sorted(rollen.items()):
        if "afnemer" in gevonden and "aanbieder" not in gevonden:
            uit.append(f"de dienst {onderwerp!r} wordt in deze keten afgenomen en door geen enkel "
                       f"component aangeboden")
        if "aanbieder" in gevonden and "afnemer" not in gevonden:
            uit.append(f"de dienst {onderwerp!r} wordt in deze keten aangeboden en door geen enkel "
                       f"component afgenomen")
    for r in rijen:
        if not r["rol"]:
            uit.append(f"{r['component']}: {r['dienst']!r} eindigt niet op aanbieder of afnemer, "
                       f"dus is onbepaald wie wat levert")

        if r["toevoeging"]:
            uit.append(f"{r['component']}: {r['dienst']!r} draagt de toevoeging "
                       f"{r['toevoeging']!r}; dat is dezelfde dienst die twee keer wordt "
                       f"ingezet en geen eigen dienst")
    return uit


def tekst_svg(x, y, s, grootte=12, kleur=INK, vet=False, anker="start"):
    gewicht = ' font-weight="600"' if vet else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{grootte}" '
            f'fill="{kleur}" text-anchor="{anker}"{gewicht}>{html.escape(s)}</text>')


def teken(rijen, bekend, titel):
    """De matrix: een rij per dienstonderwerp, een kolom per component."""
    onderwerpen, componenten = [], []
    for r in rijen:
        if r["onderwerp"] not in onderwerpen:
            onderwerpen.append(r["onderwerp"])
        if r["component"] not in componenten:
            componenten.append(r["component"])
    per = collections.defaultdict(list)
    for r in rijen:
        per[(r["onderwerp"], r["component"])].append(r)

    breed = NAAMBREEDTE + len(componenten) * KOLOM + 40
    hoog = KOP + len(onderwerpen) * RIJ + 76
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}" '
             f'viewBox="0 0 {breed} {hoog}" role="img">',
             f'<rect width="{breed}" height="{hoog}" fill="#ffffff"/>',
             tekst_svg(20, 30, titel, 16, INK, True)]

    for i, component in enumerate(componenten):
        x = NAAMBREEDTE + i * KOLOM
        delen.append(f'<rect x="{x}" y="{KOP - 44}" width="{KOLOM - 8}" height="38" rx="3" '
                     f'fill="{APP}" stroke="{APP_L}"/>')
        langste = max((breedte(w, 11, True) for w in component.split()), default=0)
        letter = 11 if langste <= KOLOM - 20 else 9
        regels = _knip(component, KOLOM - 20, letter)
        for j, regel in enumerate(regels):
            delen.append(tekst_svg(x + (KOLOM - 8) / 2, KOP - 30 + j * (letter + 2) + 6, regel,
                                   letter, APP_T, True, "middle"))

    for r, onderwerp in enumerate(onderwerpen):
        y = KOP + r * RIJ
        if r % 2:
            delen.append(f'<rect x="12" y="{y}" width="{breed - 24}" height="{RIJ}" '
                         f'fill="#fafbfa"/>')
        voorstel = bekend and onderwerp not in bekend
        delen.append(tekst_svg(20, y + 20, onderwerp, 12, MUTED if voorstel else INK))
        if voorstel:
            delen.append(tekst_svg(NAAMBREEDTE - 14, y + 20, "voorstel", 10, MUTED, False, "end"))
        for i, component in enumerate(componenten):
            gevonden = per.get((onderwerp, component)) or []
            if not gevonden:
                continue
            x = NAAMBREEDTE + i * KOLOM
            for k, g in enumerate(sorted(gevonden, key=lambda g: g["rol"])):
                vul = BIEDT if g["rol"] == "aanbieder" else NEEMT
                w = (KOLOM - 14) / max(1, len(gevonden))
                delen.append(f'<rect x="{x + k * w}" y="{y + 5}" width="{w - 4}" height="{RIJ - 11}" '
                             f'rx="3" fill="{vul}" stroke="{LIJN}"/>')
                merk = "biedt" if g["rol"] == "aanbieder" else "neemt af"
                delen.append(tekst_svg(x + k * w + (w - 4) / 2, y + 20, merk, 10, INK, False,
                                       "middle"))
        delen.append(f'<line x1="12" y1="{y + RIJ}" x2="{breed - 12}" y2="{y + RIJ}" '
                     f'stroke="{LIJN}" stroke-width="0.6"/>')

    y = KOP + len(onderwerpen) * RIJ + 26
    for i, (vul, wat) in enumerate(((BIEDT, "biedt de dienst aan"), (NEEMT, "neemt de dienst af"))):
        delen.append(f'<rect x="{20 + i * 220}" y="{y - 11}" width="26" height="14" rx="3" '
                     f'fill="{vul}" stroke="{LIJN}"/>')
        delen.append(tekst_svg(52 + i * 220, y, wat, 11, MUTED))
    delen.append(tekst_svg(20, y + 24,
                           "Een dienst zegt wat er moet kunnen, niet welk systeem het doet; elk "
                           "component kan hem claimen.", 11, MUTED))
    delen.append("</svg>")
    return "\n".join(delen)


def _knip(tekst, ruimte, grootte=11, regels=2):
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
    return uit


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--keten", default=None, help="de interactieketenspecificatie")
    parser.add_argument("--uit", default=None, help="de svg die geschreven wordt")
    parser.add_argument("--kort", action="store_true", help="alleen de bevindingen")
    args = parser.parse_args(argv)

    keten = pathlib.Path(args.keten) if args.keten else WORTEL / KETEN
    if not keten.is_file():
        print(f"De interactieketenspecificatie staat niet op {keten}.", file=sys.stderr)
        return 2
    rijen = claims(keten)
    if not rijen:
        print("De keten claimt geen enkele dienst.", file=sys.stderr)
        return 2
    bekend = dienstenlijst()
    uit = pathlib.Path(args.uit) if args.uit else WORTEL / UIT
    uit.parent.mkdir(parents=True, exist_ok=True)
    uit.write_text(teken(rijen, bekend, "Wie biedt en wie neemt welke koppelvlakdienst af") + "\n",
                   encoding="utf-8")

    bevindingen = bevindingen_van(rijen, bekend)
    if not args.kort:
        onderwerpen = {r["onderwerp"] for r in rijen}
        print(str(uit).replace(str(WORTEL) + "/", ""))
        print(f"  {len(rijen)} claims over {len(onderwerpen)} diensten en "
              f"{len({r['component'] for r in rijen})} componenten")
        print(f"  de dienstenlijst van Public kent er {len(bekend)}; "
              f"{len(onderwerpen - bekend)} daarvan stelt deze keten voor")
    for v in voorstellen_van(rijen, bekend):
        print(f"  voorstel: de dienst {v!r} staat nog niet in de dienstenlijst van Public")
    for b in bevindingen:
        print(f"  sluit niet aan: {b}")
    print(f"\n{len(bevindingen)} claims die niet aansluiten.")
    return 1 if bevindingen else 0


if __name__ == "__main__":
    sys.exit(main())
