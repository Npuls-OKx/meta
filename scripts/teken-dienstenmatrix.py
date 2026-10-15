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

RIJ, KOLOM, NAAMBREEDTE, KOP = 30, 152, 352, 92


def breedte(tekst, grootte=12, vet=False):
    return len(tekst) * grootte * (0.56 if vet else 0.52)


def dienstenlijst():
    """De dienstonderwerpen die Npuls-OKx/Public vastlegt, van het vastgezette commit."""
    if not PUBLIC.is_dir():
        return set()
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


def contract_per_dienst(map_, rijen, aanduiding):
    """Of hoofdstuk 3.1 van een interactiespecificatie per dienst is ingedeeld.

    Criterium 18 van #372 zegt dat het contract per dienst staat, criterium 19 dat de
    operatienummers blijven. Deze toets leest beide terug: elke dienst die de keten voor deze
    interactie claimt draagt een eigen kop in 3.1, en elke operatie uit de tabellen komt daar
    terug. Levert een lijst meldingen op, en een vlag of het document al is omgezet.
    """
    pad = map_ / f"{aanduiding.lower()}.md"
    if not pad.is_file():
        return False, [f"{aanduiding}: {pad.name} ontbreekt"]
    tekst = pad.read_text(encoding="utf-8")
    if "### 3.1 Het contract per dienst" not in tekst:
        return False, []
    begin = tekst.index("### 3.1 Het contract per dienst")
    eind = tekst.index("\n### ", begin + 10)
    blok = tekst[begin:eind]
    koppen = {k.split(",")[0].strip() for k in re.findall(r"^#### (.+)$", blok, re.M)}
    verwacht = {r["dienst"] for r in rijen if aanduiding in r.get("eenheid_vol", "")}
    meldingen = []
    for dienst in sorted(verwacht - koppen):
        meldingen.append(f"{aanduiding}: hoofdstuk 3.1 draagt geen kop voor de dienst {dienst!r}, "
                         f"terwijl de keten hem hier claimt")
    for kop in sorted(koppen - verwacht):
        meldingen.append(f"{aanduiding}: hoofdstuk 3.1 draagt een kop voor {kop!r}, "
                         f"terwijl de keten die dienst hier niet claimt")
    # Criterium 19: elke operatie uit het document komt terug in 3.1.
    alle = set(re.findall(r"^\| (O\d+) \|", tekst, re.M))
    in_31 = set(re.findall(r"^\| (O\d+) \|", blok, re.M))
    for nr in sorted(alle - in_31, key=lambda n: int(n[1:])):
        meldingen.append(f"{aanduiding}: operatie {nr} staat niet in hoofdstuk 3.1")
    return True, meldingen


def tekst_svg(x, y, s, grootte=12, kleur=INK, vet=False, anker="start"):
    gewicht = ' font-weight="600"' if vet else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{grootte}" '
            f'fill="{kleur}" text-anchor="{anker}"{gewicht}>{html.escape(s)}</text>')


def teken(rijen, bekend, titel):
    """De matrix: een rij per koppelvlakdienst, een kolom per applicatiecomponent.

    De aanbieder en de afnemer zijn twee zelfstandige diensten, elk met een eigen naam, een
    eigen pagina in de dienstenlijst en een eigen versie. Zij krijgen daarom elk een eigen rij,
    met hun tegenhanger ernaast zodat het paar leesbaar blijft.
    """
    diensten, componenten = [], []
    for r in rijen:
        if r["component"] not in componenten:
            componenten.append(r["component"])
    for onderwerp in dict.fromkeys(r["onderwerp"] for r in rijen):
        for rol in ("aanbieder", "afnemer"):
            naam = f"{onderwerp}-{rol}"
            if any(r["dienst"] == naam for r in rijen):
                diensten.append((onderwerp, rol, naam))
    per = collections.defaultdict(list)
    for r in rijen:
        per[(r["dienst"], r["component"])].append(r)

    breed = NAAMBREEDTE + len(componenten) * KOLOM + 40
    hoog = KOP + len(diensten) * RIJ + 76
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}" '
             f'viewBox="0 0 {breed} {hoog}" role="img">',
             f'<rect width="{breed}" height="{hoog}" fill="#ffffff"/>',
             tekst_svg(20, 30, titel, 16, INK, True)]

    for i, component in enumerate(componenten):
        x = NAAMBREEDTE + i * KOLOM
        delen.append(f'<rect x="{x}" y="{KOP - 48}" width="{KOLOM - 8}" height="44" rx="3" '
                     f'fill="{APP}" stroke="{APP_L}"/>')
        delen.append(icoon_svg(x + KOLOM - 28, KOP - 43, ICOON_COMPONENT, APP_T))
        ruimte = KOLOM - 44
        langste = max((breedte(w, 10, True) for w in component.split()), default=0)
        letter = 10 if langste <= ruimte else 9
        regels = _knip(component, ruimte, letter)
        basis = KOP - 24 if len(regels) > 1 else KOP - 18
        for j, regel in enumerate(regels):
            delen.append(tekst_svg(x + 8, basis + j * (letter + 2), regel, letter, APP_T, True))

    vorig = None
    for r_i, (onderwerp, rol, naam) in enumerate(diensten):
        y = KOP + r_i * RIJ
        if vorig is not None and onderwerp != vorig:
            delen.append(f'<line x1="12" y1="{y}" x2="{breed - 12}" y2="{y}" stroke="{APP_L}" '
                         f'stroke-width="0.9"/>')
        vorig = onderwerp
        voorstel = bekend and onderwerp not in bekend
        delen.append(f'<rect x="16" y="{y + 4}" width="{NAAMBREEDTE - 30}" height="{RIJ - 9}" '
                     f'rx="3" fill="{DIENST}" stroke="{APP_L}" stroke-width="0.8"'
                     + (' stroke-dasharray="4 3"' if voorstel else "") + '/>')
        delen.append(icoon_svg(22, y + 7, ICOON_DIENST, APP_T))
        delen.append(biedt_svg(42, y + 15, APP_T) if rol == "aanbieder"
                     else neemt_svg(42, y + 15, APP_T))
        delen.append(tekst_svg(66, y + 20, naam, 10, APP_T))
        if voorstel:
            delen.append(tekst_svg(NAAMBREEDTE - 20, y + 20, "voorstel", 9, MUTED, False, "end"))
        for i, component in enumerate(componenten):
            gevonden = per.get((naam, component)) or []
            if not gevonden:
                continue
            x = NAAMBREEDTE + i * KOLOM
            eenheden = ".".join(g["eenheid"] for g in gevonden if g["eenheid"])
            delen.append(f'<rect x="{x}" y="{y + 6}" width="{KOLOM - 16}" height="{RIJ - 13}" '
                         f'rx="3" fill="{DIENST}" stroke="{APP_L}" stroke-width="0.8"/>')
            delen.append(tekst_svg(x + (KOLOM - 16) / 2, y + 20,
                                   eenheden or "claimt", 10, APP_T, False, "middle"))

    y = KOP + len(diensten) * RIJ + 26
    delen.append(biedt_svg(20, y - 4, APP_T))
    delen.append(tekst_svg(44, y, "een aanbiedersdienst, de geleverde interface", 11, MUTED))
    delen.append(neemt_svg(310, y - 4, APP_T))
    delen.append(tekst_svg(334, y, "een afnemersdienst, de gevraagde interface", 11, MUTED))
    delen.append(icoon_svg(590, y - 11, ICOON_COMPONENT, APP_T))
    delen.append(tekst_svg(612, y, "applicatiecomponent", 11, MUTED))
    delen.append(tekst_svg(760, y, "een vak noemt de interacties waarin het component claimt",
                           11, MUTED))
    delen.append(tekst_svg(20, y + 24,
                           "De aanbieder en de afnemer zijn twee zelfstandige diensten, elk met "
                           "een eigen naam en een eigen versie.", 11, MUTED))
    delen.append("</svg>")
    return "\n".join(delen)


def teken_interactie(rijen, aanduiding):
    """Een plaat voor een interactiespecificatie: twee componenten met hun diensten ertussen.

    Waarvoor: per interactie wil een bouwer zien welke diensten er over de lijn gaan en welke
    kant zij op staan. De aanbiedersdienst en de afnemersdienst staan als twee eigen blokken
    tegenover elkaar, met de bal en de kom die in elkaar vallen zoals ArchiMate ze tekent.
    """
    eigen = [r for r in rijen if aanduiding in r.get("eenheid_vol", "")]
    if not eigen:
        return None, []
    per = collections.defaultdict(dict)
    for r in eigen:
        per[r["onderwerp"]][r["rol"]] = r
    onderwerpen = list(dict.fromkeys(r["onderwerp"] for r in eigen))

    links, rechts = [], []
    for onderwerp in onderwerpen:
        for rol, kant in (("aanbieder", links), ("afnemer", rechts)):
            r = per[onderwerp].get(rol)
            if r and r["component"] not in kant:
                kant.append(r["component"])
    if not links or not rechts:
        return None, [f"{aanduiding}: de diensten dragen geen aanbieder en afnemer samen"]
    # Binnen een interactie hoort elke dienst zijn tegenhanger te hebben. Deze toets vond dat de
    # ontwerptool in IS-OA-01 de structuur ophaalt zonder dat haar afnemersdienst was belegd.
    meldingen = [f"{aanduiding}: de dienst {o!r} draagt hier geen "
                 f"{'afnemer' if 'aanbieder' in per[o] else 'aanbieder'}"
                 for o in onderwerpen if len(per[o]) < 2]

    VAK, BLOK, GAT, RIJHOOGTE = 168, 234, 46, 58
    breed = VAK * 2 + BLOK * 2 + GAT + 72
    hoog = 72 + len(onderwerpen) * RIJHOOGTE + 60
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
    xl, xa, xb, xr = 20, 20 + VAK + 16, 20 + VAK + 16 + BLOK + GAT, breed - 20 - VAK
    delen += vak(xl, " en ".join(links), y0, hoogte)
    delen += vak(xr, " en ".join(rechts), y0, hoogte)

    for i, onderwerp in enumerate(onderwerpen):
        y = y0 + i * RIJHOOGTE + RIJHOOGTE / 2
        for r, x in ((per[onderwerp].get("aanbieder"), xa), (per[onderwerp].get("afnemer"), xb)):
            if not r:
                continue
            delen.append(f'<rect x="{x}" y="{y - 14}" width="{BLOK}" height="28" rx="3" '
                         f'fill="{DIENST}" stroke="{APP_L}" stroke-width="0.8"/>')
            delen.append(icoon_svg(x + 6, y - 9, ICOON_DIENST, APP_T))
            delen.append(tekst_svg(x + 26, y + 4, r["dienst"], 9, APP_T))
        if per[onderwerp].get("aanbieder"):
            delen.append(biedt_svg(xa + BLOK + 4, y, APP_T))
        if per[onderwerp].get("afnemer"):
            delen.append(neemt_svg(xb - 26, y, APP_T))
        bron = per[onderwerp].get("aanbieder") or per[onderwerp].get("afnemer")
        stukken = [d.strip() for d in bron.get("endpoints", "").replace("`", "").split(",")
                   if d.strip()]
        endpoint = stukken[0] if stukken else ""
        if len(endpoint) > 52:
            endpoint = endpoint[:52].rsplit(" ", 1)[0] + " ..."
        if len(stukken) > 1:
            endpoint += f"  (+{len(stukken) - 1})"
        delen.append(tekst_svg((xa + xb + BLOK) / 2, y + 24, endpoint, 9, MUTED, False, "middle"))

    y = y0 + hoogte + 34
    delen.append(biedt_svg(20, y - 4, APP_T))
    delen.append(tekst_svg(44, y, "aanbiedersdienst", 11, MUTED))
    delen.append(neemt_svg(170, y - 4, APP_T))
    delen.append(tekst_svg(194, y, "afnemersdienst", 11, MUTED))
    delen.append(tekst_svg(300, y, "twee zelfstandige diensten die in elkaar vallen, met het "
                                   "endpoint eronder", 11, MUTED))
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
        omgezet = []
        for aanduiding in aanduidingen:
            klaar, contractmeldingen = contract_per_dienst(uit.parent.parent, rijen, aanduiding)
            if klaar:
                omgezet.append(aanduiding)
                bevindingen += contractmeldingen
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
        print(f"  {len(rijen)} claims over {len({r['dienst'] for r in rijen})} diensten "
              f"({len(onderwerpen)} onderwerpen) en "
              f"{len({r['component'] for r in rijen})} componenten")
        print(f"  de dienstenlijst van Public kent {len(bekend) * 2} diensten; "
              f"{len(onderwerpen - bekend) * 2} stelt deze keten voor")
    if args.per_interactie and not args.kort:
        print(f"  hoofdstuk 3.1 per dienst: {len(omgezet)} van {len(aanduidingen)} omgezet"
              + (f", nog te doen {', '.join(a for a in aanduidingen if a not in omgezet)}"
                 if len(omgezet) < len(aanduidingen) else ""))
    for v in voorstellen_van(rijen, bekend):
        print(f"  voorstel: de dienst {v!r} staat nog niet in de dienstenlijst van Public")
    for b in bevindingen:
        print(f"  sluit niet aan: {b}")
    print(f"\n{len(bevindingen)} claims die niet aansluiten.")
    return 1 if bevindingen else 0


if __name__ == "__main__":
    sys.exit(main())
