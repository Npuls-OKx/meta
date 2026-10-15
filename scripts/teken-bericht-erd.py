#!/usr/bin/env python3
"""Per bericht in een interactiespecificatie een ERD van de objecttypen die het draagt.

Waarom dit script bestaat: een berichtspecificatie zegt veld voor veld wat er over de lijn
gaat, en laat de lezer zelf uitzoeken hoe die velden zich tot elkaar verhouden. Wie de
koppeling bouwt of verifieert wil dat verband zien: welke objecttypen zitten in dit bericht,
en hoe hangen zij samen in het informatiemodel. Relateert aan: Npuls-OKx/meta#372.

    python3 scripts/teken-bericht-erd.py [--map PAD] [--bestand PAD] [--uit MAP]

Zonder argumenten leest het script de interactiespecificaties in
architecture/docs/specificatie/interactie-onderwijsaanbod en schrijft het de platen naar
`img/erd/` daarnaast.

De inhoud is afgeleid, niet ingevoerd
-------------------------------------
Per berichtsectie leest het script de kolom `Objecttype` van elke tabel, pakt daaruit de
namen tussen backquotes, en houdt de namen over die het [informatiemodel](
architecture/model/informatiemodel/informatiemodel.json) kent. De relaties ertussen komen uit
datzelfde bestand. Wijzigt het model, dan wijzigen de platen mee.

Een bericht waarvan de velden contracteigenschappen zijn, zoals een afkeuring met haar code
en haar plek in de lading, draagt geen objecttype. Daar komt geen plaat: het script meldt dat,
want een lege plaat leest als een gat in het model.

De vorm
-------
Een objecttype is een vak; een relatie is een lijn met haar kardinaliteit aan beide kanten.
De soort uit het model bepaalt die kardinaliteit: een geheel-deelrelatie draagt `1` bij het
geheel en `n` bij het deel, een specialisatie draagt `is een`, en een associatie draagt haar
label uit het model. De rijen volgen de geheel-deelrichting, zodat een boom van boven naar
beneden leest.
"""

import argparse
import collections
import html
import json
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
MAP = "architecture/docs/specificatie/interactie-onderwijsaanbod"
MODEL = "architecture/model/informatiemodel/informatiemodel.json"
UIT = "img/erd"

BUS, BUS_L, BUS_T = "#ffffb5", "#a8a85a", "#5a5a2a"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#9a9a9a"
FONT = "Arial, Helvetica, sans-serif"
ICOON = '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>'

MARGE, GOOT, RIJGOOT = 26, 34, 96
VAKHOOGTE, REGELHOOGTE, TITELHOOGTE = 30, 14, 46
OMLAAG = ("Composition", "Aggregation")


def breedte(tekst, grootte=12, vet=False):
    return len(tekst) * grootte * (0.56 if vet else 0.52)


def lees_model(pad):
    """De objecttypen en de relaties uit het informatiemodel."""
    d = json.loads(pad.read_text(encoding="utf-8"))
    return {o["naam"] for o in d["objecttypen"]}, d["relaties"]


def berichten(tekst, kopniveau=3):
    """De berichtsecties van een document, met hun kop en hun inhoud.

    Een berichtsectie is een kop onder het hoofdstuk dat de berichten draagt. Het hoofdstuk
    heet `De berichten`, `Berichtspecificatie` of `De berichtspecificatie`; dat verschilt per
    document en daarom telt de naam en niet het nummer.
    """
    regels = tekst.splitlines()
    uit, binnen, kop, inhoud = [], False, None, []
    hek = "#" * kopniveau + " "
    for regel in regels:
        gestript = regel.strip()
        if gestript.startswith("## "):
            if kop:
                uit.append((kop, "\n".join(inhoud)))
                kop, inhoud = None, []
            naam = gestript[3:].strip().lower()
            binnen = "bericht" in naam
            continue
        if binnen and gestript.startswith(hek):
            if kop:
                uit.append((kop, "\n".join(inhoud)))
            kop, inhoud = gestript[len(hek):].strip(), []
            continue
        if kop is not None:
            inhoud.append(regel)
    if kop:
        uit.append((kop, "\n".join(inhoud)))
    return uit


def objecttypen_in(blok, bekend):
    """De objecttypen die de kolom Objecttype van een tabel noemt, in leesvolgorde."""
    uit, gezien = [], set()
    kolom = None
    for regel in blok.splitlines():
        gestript = regel.strip()
        if not gestript.startswith("|"):
            kolom = None
            continue
        cellen = [c.strip() for c in gestript.split("|")[1:-1]]
        if kolom is None:
            kolom = next((i for i, c in enumerate(cellen) if c.lower() == "objecttype"), None)
            continue
        if kolom is None or set(gestript) <= set("|- :"):
            continue
        if kolom >= len(cellen):
            continue
        for naam in re.findall(r"`([^`]+)`", cellen[kolom]):
            if naam in bekend and naam not in gezien:
                gezien.add(naam)
                uit.append(naam)
    return uit


def relaties_tussen(namen, relaties):
    """De relaties van het model waarvan beide kanten in deze selectie staan."""
    binnen = set(namen)
    uit, gezien = [], set()
    for r in relaties:
        sleutel = (r["van"], r["naar"], r["soort"])
        if r["van"] in binnen and r["naar"] in binnen and r["van"] != r["naar"] \
                and sleutel not in gezien:
            gezien.add(sleutel)
            uit.append(r)
    return uit


def kardinaliteit(relatie):
    """Wat er aan beide kanten van de lijn staat, afgeleid uit de soort."""
    soort = relatie["soort"]
    if soort in OMLAAG:
        return "1", "n", relatie.get("label") or "bestaat uit"
    if soort == "Specialization":
        return "", "", relatie.get("label") or "is een"
    return "", "", relatie.get("label") or ""


def rijen_van(namen, relaties):
    """De objecttypen in rijen, met een geheel boven zijn delen."""
    omlaag = [r for r in relaties if r["soort"] in OMLAAG]
    diepte = {n: 0 for n in namen}
    for _ in range(len(namen)):
        veranderd = False
        for r in omlaag:
            if diepte[r["naar"]] < diepte[r["van"]] + 1:
                diepte[r["naar"]] = diepte[r["van"]] + 1
                veranderd = True
        if not veranderd:
            break
    per_rij = collections.defaultdict(list)
    for naam in namen:
        per_rij[diepte[naam]].append(naam)
    return [per_rij[d] for d in sorted(per_rij)]


def knip(tekst, ruimte, grootte=12, regels=2):
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


def tekst_svg(x, y, s, grootte=12, kleur=INK, vet=False, anker="middle"):
    gewicht = ' font-weight="600"' if vet else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{grootte}" '
            f'fill="{kleur}" text-anchor="{anker}"{gewicht}>{html.escape(s)}</text>')


def teken(namen, relaties, titel):
    """De ERD als SVG, met de vakken in rijen en de lijnen haaks ertussen."""
    rijen = rijen_van(namen, relaties)
    maten = {}
    for naam in namen:
        regels = knip(naam, 190)
        maten[naam] = (max(breedte(r, 12) for r in regels) + 46,
                       VAKHOOGTE + (REGELHOOGTE if len(regels) > 1 else 0), regels)

    # Een relatie binnen de bovenste rij loopt erboven langs, dus daar moet ruimte voor zijn.
    boven = sum(1 for r in relaties if r["van"] in rijen[0] and r["naar"] in rijen[0])
    kop = TITELHOOGTE + (boven * 15 + 20 if boven else 0)
    plek, y = {}, kop
    # Het doek is minstens zo breed als de titel, anders valt die erbuiten.
    breed = MARGE * 2 + breedte(titel, 15, True)
    for rij in rijen:
        rijbreedte = sum(maten[n][0] for n in rij) + GOOT * (len(rij) - 1)
        breed = max(breed, rijbreedte + MARGE * 2)
        hoog = max(maten[n][1] for n in rij)
        y += hoog + RIJGOOT
    hoogte = y - RIJGOOT + MARGE

    y = kop
    for rij in rijen:
        rijbreedte = sum(maten[n][0] for n in rij) + GOOT * (len(rij) - 1)
        x = (breed - rijbreedte) / 2
        hoog = max(maten[n][1] for n in rij)
        for naam in rij:
            b, h, regels = maten[naam]
            plek[naam] = (x, y, b, h, regels)
            x += b + GOOT
        y += hoog + RIJGOOT

    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed:.0f}" '
             f'height="{hoogte:.0f}" viewBox="0 0 {breed:.0f} {hoogte:.0f}" role="img">',
             f'<rect width="{breed:.0f}" height="{hoogte:.0f}" fill="#ffffff"/>',
             tekst_svg(MARGE, 28, titel, 15, INK, True, "start")]

    # Elke relatie tussen hetzelfde rijenpaar krijgt haar eigen baanhoogte, anders vallen de
    # etiketten op elkaar en loopt elke lijn over dezelfde horizontale baan.
    banen = collections.defaultdict(int)
    for r in relaties:
        ax, ay, ab, ah, _ = plek[r["van"]]
        bx, by, bb, bh, _ = plek[r["naar"]]
        van_mid, naar_mid = ax + ab / 2, bx + bb / 2
        sleutel = (min(ay, by), max(ay, by))
        trap = banen[sleutel] * 15
        banen[sleutel] += 1
        if abs(ay - by) < 1:
            y0 = ay - 16 - trap
            punten = [(van_mid, ay), (van_mid, y0), (naar_mid, y0), (naar_mid, by)]
        elif ay < by:
            tussen = ay + ah + 20 + trap
            punten = [(van_mid, ay + ah), (van_mid, tussen), (naar_mid, tussen), (naar_mid, by)]
        else:
            tussen = by + bh + 20 + trap
            punten = [(van_mid, ay), (van_mid, tussen), (naar_mid, tussen), (naar_mid, by + bh)]
        pad = " ".join(f"{'M' if i == 0 else 'L'}{px:.0f} {py:.0f}" for i, (px, py) in enumerate(punten))
        delen.append(f'<path d="{pad}" fill="none" stroke="{LIJN}" stroke-width="1.4"/>')
        bij_van, bij_naar, label = kardinaliteit(r)
        if bij_van:
            delen.append(tekst_svg(van_mid + 12, punten[0][1] + (14 if ay < by else -6), bij_van, 11, MUTED))
        if bij_naar:
            delen.append(tekst_svg(naar_mid + 12, punten[-1][1] - (6 if ay < by else -14), bij_naar, 11, MUTED))
        if label:
            mx = (punten[1][0] + punten[2][0]) / 2
            my = punten[1][1]
            delen.append(f'<rect x="{mx - breedte(label, 11) / 2 - 4:.0f}" y="{my - 9:.0f}" '
                         f'width="{breedte(label, 11) + 8:.0f}" height="14" fill="#ffffff"/>')
            delen.append(tekst_svg(mx, my + 2, label, 11, MUTED))

    for naam in namen:
        x, y, b, h, regels = plek[naam]
        delen.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{b:.0f}" height="{h:.0f}" rx="3" '
                     f'fill="{BUS}" stroke="{BUS_L}" stroke-width="1"/>')
        delen.append(f'<g transform="translate({x + 10:.0f},{y + (h - 14) / 2:.0f})" fill="none" '
                     f'stroke="{BUS_T}" stroke-width="1.2">{ICOON}</g>')
        basis = y + (19 if len(regels) > 1 else 20)
        for i, regel in enumerate(regels):
            delen.append(tekst_svg(x + b / 2 + 14, basis + i * REGELHOOGTE, regel, 12, BUS_T))

    delen.append("</svg>")
    return "\n".join(delen)


def anker(kop):
    """Een bestandsnaam uit een kop, zonder de operatieverwijzing ertussen haakjes."""
    schoon = re.sub(r"\([^)]*\)", "", kop).lower()
    schoon = re.sub(r"[`\"']", "", schoon)
    schoon = re.sub(r"[^a-z0-9]+", "-", schoon)
    return schoon.strip("-")


def verwerk(bestand, bekend, relaties, uit):
    """De platen van een document, met per bericht wat er gebeurde."""
    tekst = bestand.read_text(encoding="utf-8")
    verslag = []
    for kop, blok in berichten(tekst):
        namen = objecttypen_in(blok, bekend)
        if not namen:
            verslag.append((kop, None, "draagt geen objecttype; de velden zijn contracteigenschappen"))
            continue
        eigen = relaties_tussen(namen, relaties)
        naam = f"{bestand.stem}-{anker(kop)}.svg"
        uit.mkdir(parents=True, exist_ok=True)
        (uit / naam).write_text(teken(namen, eigen, kop) + "\n", encoding="utf-8")
        verslag.append((kop, naam, f"{len(namen)} objecttypen, {len(eigen)} relaties"))
    return verslag


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--map", default=None, help="de map met de interactiespecificaties")
    parser.add_argument("--bestand", default=None, help="alleen dit document")
    parser.add_argument("--model", default=None, help="het informatiemodel")
    parser.add_argument("--uit", default=None, help="de map voor de platen")
    args = parser.parse_args(argv)

    map_ = pathlib.Path(args.map) if args.map else WORTEL / MAP
    model = pathlib.Path(args.model) if args.model else WORTEL / MODEL
    if not model.is_file():
        print(f"Het informatiemodel staat niet op {model}.", file=sys.stderr)
        return 2
    bestanden = ([pathlib.Path(args.bestand)] if args.bestand
                 else sorted(map_.glob("is-oa-*.md")))
    if not bestanden or not all(b.is_file() for b in bestanden):
        print(f"Geen interactiespecificatie gevonden in {map_}.", file=sys.stderr)
        return 2
    uit = pathlib.Path(args.uit) if args.uit else bestanden[0].parent / UIT

    bekend, relaties = lees_model(model)
    geschreven = 0
    for bestand in bestanden:
        print(f"\n{bestand.name}")
        for kop, naam, wat in verwerk(bestand, bekend, relaties, uit):
            print(f"  {kop[:54]:56} {naam or 'geen plaat':46} {wat}")
            geschreven += 1 if naam else 0
    print(f"\n{geschreven} platen geschreven in {uit}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
