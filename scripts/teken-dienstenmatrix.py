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
DIENST = "#d6f7f7"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#d8ddda"
FONT = "Arial, Helvetica, sans-serif"

# De iconen van ArchiMate, in de notatie die de standaard aanhoudt.
ICOON_COMPONENT = ('<rect x="4" y="2" width="10" height="12"/>'
                   '<rect x="2" y="4" width="4" height="2.5"/>'
                   '<rect x="2" y="8.5" width="4" height="2.5"/>')
ICOON_DIENST = '<rect x="1.5" y="4.5" width="13" height="7" rx="3.5"/>'
ICOON_INTERFACE = '<path d="M1.5 8h5"/><circle cx="10" cy="8" r="3.5"/>'


def icoon_svg(x, y, pad, kleur, dikte=1.2, vul="none"):
    return (f'<g transform="translate({x:.0f},{y:.0f})" fill="{vul}" stroke="{kleur}" '
            f'stroke-width="{dikte}">{pad}</g>')


def biedt_svg(x, y, kleur):
    """Een geleverde interface: de bal aan een steel, zoals ArchiMate haar tekent."""
    return (f'<g stroke="{kleur}" stroke-width="1.6" fill="none">'
            f'<path d="M{x} {y}h9"/><circle cx="{x + 13}" cy="{y}" r="4.5" fill="{kleur}"/></g>')


def neemt_svg(x, y, kleur):
    """Een gevraagde interface: de kom aan een steel, die om de bal van de aanbieder valt."""
    return (f'<g stroke="{kleur}" stroke-width="1.6" fill="none">'
            f'<path d="M{x} {y}h9"/>'
            f'<path d="M{x + 9} {y - 5.5}A5.5 5.5 0 0 1 {x + 9} {y + 5.5}"/></g>')

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
        eenheid = cellen[3] if len(cellen) > 4 else ""
        uit.append({"component": component, "onderwerp": onderwerp, "rol": rol,
                    "dienst": dienst, "endpoints": endpoints, "stand": cellen[-1],
                    "eenheid": re.sub(r"IS-OA-", "", eenheid).replace(", ", "."),
                    "eenheid_vol": eenheid,
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
        delen.append(f'<rect x="{x}" y="{KOP - 48}" width="{KOLOM - 8}" height="44" rx="3" '
                     f'fill="{APP}" stroke="{APP_L}"/>')
        delen.append(icoon_svg(x + KOLOM - 28, KOP - 43, ICOON_COMPONENT, APP_T))
        ruimte = KOLOM - 20
        langste = max((breedte(w, 10, True) for w in component.split()), default=0)
        letter = 10 if langste <= ruimte else 9
        regels = _knip(component, ruimte, letter)
        basis = KOP - 24 if len(regels) > 1 else KOP - 18
        for j, regel in enumerate(regels):
            delen.append(tekst_svg(x + 8, basis + j * (letter + 2), regel,
                                   letter, APP_T, True, "start"))

    for r, onderwerp in enumerate(onderwerpen):
        y = KOP + r * RIJ
        if r % 2:
            delen.append(f'<rect x="12" y="{y}" width="{breed - 24}" height="{RIJ}" '
                         f'fill="#fafbfa"/>')
        voorstel = bekend and onderwerp not in bekend
        delen.append(f'<rect x="16" y="{y + 4}" width="{NAAMBREEDTE - 30}" height="{RIJ - 9}" '
                     f'rx="3" fill="{DIENST}" stroke="{APP_L}" stroke-width="0.8"'
                     + (' stroke-dasharray="4 3"' if voorstel else "") + '/>')
        delen.append(icoon_svg(22, y + 7, ICOON_INTERFACE, APP_T))
        delen.append(icoon_svg(40, y + 7, ICOON_DIENST, APP_T))
        delen.append(tekst_svg(60, y + 20, onderwerp, 11, APP_T))
        if voorstel:
            delen.append(tekst_svg(NAAMBREEDTE - 20, y + 20, "voorstel", 9, MUTED, False, "end"))
        for i, component in enumerate(componenten):
            gevonden = per.get((onderwerp, component)) or []
            if not gevonden:
                continue
            x = NAAMBREEDTE + i * KOLOM
            w = (KOLOM - 14) / max(1, len(gevonden))
            for k, g in enumerate(sorted(gevonden, key=lambda g: g["rol"])):
                mx = x + k * w + 4
                delen.append(biedt_svg(mx, y + 15, APP_T) if g["rol"] == "aanbieder"
                             else neemt_svg(mx, y + 15, APP_T))
                eenheden = g.get("eenheid", "")
                if eenheden:
                    delen.append(tekst_svg(mx + 26, y + 19, eenheden, 9, MUTED))
        delen.append(f'<line x1="12" y1="{y + RIJ}" x2="{breed - 12}" y2="{y + RIJ}" '
                     f'stroke="{LIJN}" stroke-width="0.6"/>')

    y = KOP + len(onderwerpen) * RIJ + 26
    delen.append(biedt_svg(20, y - 4, APP_T))
    delen.append(tekst_svg(44, y, "biedt de dienst aan, een geleverde interface", 11, MUTED))
    delen.append(neemt_svg(300, y - 4, APP_T))
    delen.append(tekst_svg(324, y, "neemt de dienst af, een gevraagde interface", 11, MUTED))
    delen.append(icoon_svg(584, y - 11, ICOON_INTERFACE, APP_T))
    delen.append(icoon_svg(602, y - 11, ICOON_DIENST, APP_T))
    delen.append(tekst_svg(624, y, "de dienst met de interface waarop zij wordt aangeboden",
                           11, MUTED))
    delen.append(icoon_svg(948, y - 11, ICOON_COMPONENT, APP_T))
    delen.append(tekst_svg(970, y, "applicatiecomponent", 11, MUTED))
    delen.append(tekst_svg(20, y + 24,
                           "Een dienst zegt wat er moet kunnen, niet welk systeem het doet; elk "
                           "component kan hem claimen.", 11, MUTED))
    delen.append("</svg>")
    return "\n".join(delen)


def teken_interactie(rijen, aanduiding):
    """Een plaat voor een interactiespecificatie: twee componenten met de diensten ertussen.

    Waarvoor: per interactie wil een bouwer zien welke diensten er over de lijn gaan en wie
    welke kant op staat. De aanbieder draagt de geleverde interface, de afnemer de gevraagde,
    en samen vallen zij in elkaar zoals ArchiMate ze tekent.
    """
    eigen = [r for r in rijen if aanduiding in r.get("eenheid_vol", "")]
    if not eigen:
        return None, []
    per = collections.defaultdict(dict)
    for r in eigen:
        per[r["onderwerp"]][r["rol"]] = r
    onderwerpen = [o for o in dict.fromkeys(r["onderwerp"] for r in eigen)]

    links, rechts = [], []
    for onderwerp in onderwerpen:
        for rol, kant in (("aanbieder", links), ("afnemer", rechts)):
            r = per[onderwerp].get(rol)
            if r and r["component"] not in kant:
                kant.append(r["component"])
    if not links or not rechts:
        return None, [f"{aanduiding}: de diensten dragen geen aanbieder en afnemer samen"]
    # Binnen een interactie hoort elke dienst beide rollen te dragen. Deze toets vond dat de
    # ontwerptool in IS-OA-01 de structuur ophaalt zonder dat haar afnemersrol was belegd.
    meldingen = [f"{aanduiding}: de dienst {o!r} draagt hier geen "
                 f"{'afnemer' if 'aanbieder' in per[o] else 'aanbieder'}"
                 for o in onderwerpen if len(per[o]) < 2]

    VAK, MIDDEN, RIJHOOGTE = 190, 330, 54
    breed = VAK * 2 + MIDDEN + 60
    hoog = 70 + max(1, len(onderwerpen)) * RIJHOOGTE + 60
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}" '
             f'viewBox="0 0 {breed} {hoog}" role="img">',
             f'<rect width="{breed}" height="{hoog}" fill="#ffffff"/>',
             tekst_svg(20, 28, f"{aanduiding}: de diensten over deze koppeling", 15, INK, True)]

    def vak(x, naam, y0, hoogte):
        uit = [f'<rect x="{x}" y="{y0}" width="{VAK}" height="{hoogte}" rx="4" fill="{APP}" '
               f'stroke="{APP_L}"/>', icoon_svg(x + VAK - 26, y0 + 10, ICOON_COMPONENT, APP_T)]
        for j, regel in enumerate(_knip(naam, VAK - 24, 12, regels=3)):
            uit.append(tekst_svg(x + 12, y0 + 42 + j * 15, regel, 12, APP_T, True))
        return uit

    y0, hoogte = 56, len(onderwerpen) * RIJHOOGTE
    delen += vak(20, " en ".join(links), y0, hoogte)
    delen += vak(20 + VAK + MIDDEN + 20, " en ".join(rechts), y0, hoogte)

    for i, onderwerp in enumerate(onderwerpen):
        y = y0 + i * RIJHOOGTE + RIJHOOGTE / 2
        a, b = per[onderwerp].get("aanbieder"), per[onderwerp].get("afnemer")
        x1, x2 = 20 + VAK, 20 + VAK + MIDDEN + 20
        delen.append(f'<rect x="{x1 + 46}" y="{y - 13}" width="{MIDDEN - 92}" height="26" rx="3" '
                     f'fill="{DIENST}" stroke="{APP_L}" stroke-width="0.8"/>')
        delen.append(icoon_svg(x1 + 52, y - 8, ICOON_DIENST, APP_T))
        delen.append(tekst_svg(x1 + MIDDEN / 2, y + 4, onderwerp, 10, APP_T, False, "middle"))
        if a:
            delen.append(biedt_svg(x1 + 6, y, APP_T))
        if b:
            delen.append(neemt_svg(x2 - 26, y, APP_T))
        delen_endpoint = [d.strip() for d in (a or b).get("endpoints", "").replace("`", "")
                          .split(",") if d.strip()]
        endpoint = delen_endpoint[0] if delen_endpoint else ""
        if len(endpoint) > 52:
            endpoint = endpoint[:52].rsplit(" ", 1)[0] + " ..."
        if len(delen_endpoint) > 1:
            endpoint += f"  (+{len(delen_endpoint) - 1})"
        delen.append(tekst_svg(x1 + MIDDEN / 2, y + 22, endpoint, 9, MUTED, False, "middle"))

    y = y0 + hoogte + 34
    delen.append(biedt_svg(20, y - 4, APP_T))
    delen.append(tekst_svg(44, y, "biedt aan", 11, MUTED))
    delen.append(neemt_svg(130, y - 4, APP_T))
    delen.append(tekst_svg(154, y, "neemt af", 11, MUTED))
    delen.append(tekst_svg(240, y, "de dienst staat in het midden, met haar endpoint eronder",
                           11, MUTED))
    delen.append("</svg>")
    return "\n".join(delen), meldingen


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
    parser.add_argument("--per-interactie", action="store_true",
                        help="schrijf daarnaast een plaat per interactiespecificatie")
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
    if args.per_interactie:
        aanduidingen = sorted({a for r in rijen
                               for a in re.findall(r"IS-OA-\d+", r.get("eenheid_vol", ""))})
        for aanduiding in aanduidingen:
            svg, meldingen = teken_interactie(rijen, aanduiding)
            bevindingen += meldingen
            if svg:
                doel = uit.parent / f"diensten-{aanduiding.lower()}.svg"
                doel.write_text(svg + "\n", encoding="utf-8")
                if not args.kort:
                    print(f"  {doel.name}")
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
