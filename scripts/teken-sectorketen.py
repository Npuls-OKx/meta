#!/usr/bin/env python3
"""De sectorketen tekenen: per laag de partijen en de producten die zij maken.

Waarom dit script bestaat: de beheerketenplaat uit de start van OKx is een export uit een
presentatie, en die veroudert zodra de keten verandert. Deze plaat komt uit
`doc/sectorketen-producten.json`, zodat een actualisatie een wijziging in de bron is en het
beeld nooit uit de pas loopt met de tabel die uit diezelfde bron komt.

De plaat beschrijft wat partijen maken. Een oordeel over wat ontbreekt staat er bewust niet
op; twee kenmerken dragen het beeld. De vulkleur volgt het detailniveau (conceptueel,
logisch, technisch), de randstijl volgt de aard (een onderbroken rand voor een voorschrift,
een doorgetrokken rand voor een herbruikbaar product). De lezer trekt zijn eigen conclusie.

    python3 scripts/teken-sectorketen.py [--bron PAD] [--uit PAD] [--breedte N]

Keuren gaat met scripts/keur-plaat.py; die poort hoort bij elke oplevering.
"""

import argparse
import html
import json
import pathlib
import sys

BRON = pathlib.Path("doc/sectorketen-producten.json")
UIT = pathlib.Path("img/OKx_sectorketen.svg")

# Het ArchiMate-kleurenschema zoals scripts/teken-voorbeeldregels.py het hanteert.
BUS, BUS_L = "#ffffb5", "#a8a85a"
APP, APP_L = "#b5ffff", "#5aa8a8"
CONCEPT, CONCEPT_L = "#efe6ff", "#9b86c9"
GRIJS, GRIJS_L = "#e8e8e8", "#9a9a9a"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#d8ddda"
BAND, BAND_ALT = "#fbfcfb", "#f2f5f3"
PIJL = "#2f5d8a"
FONT = "Arial, Helvetica, sans-serif"

NIVEAU = {
    "conceptueel": (BUS, BUS_L),
    "logisch": (CONCEPT, CONCEPT_L),
    "technisch": (APP, APP_L),
    "niet van toepassing": (GRIJS, GRIJS_L),
}

MARGE_LINKS = 128     # ruimte voor de lijnen die een laag overslaan
KOP_BREEDTE = 232     # de kolom met laagnummer, naam en partijen
GEREEDSCHAP = 300     # de kolom rechts
TUSSEN = 14           # ruimte tussen twee productblokken
RAND = 24


def tw(s, size, bold=False):
    """Geschatte tekstbreedte in px voor Arial, ruim genomen."""
    return len(s) * size * (0.62 if bold else 0.56)


def esc(s):
    return html.escape(str(s))


def text(x, y, s, size=12, bold=False, fill=INK, anchor="start"):
    fw = ' font-weight="bold"' if bold else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{size}"'
            f'{fw} fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')


def box(x, y, w, h, fill, line, rx=0, streep=None, dikte=1.0):
    d = f' stroke-dasharray="{streep}"' if streep else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"'
            f' fill="{fill}" stroke="{line}" stroke-width="{dikte}"{d}/>')


def breek(zin, maxbreedte, size, bold=False, regels=2):
    """Verdeelt een naam over ten hoogste `regels` regels. Geeft None zodra een woord
    zelf te breed is, zodat de aanroeper het blok verbreedt in plaats van de naam af te
    kappen; een afgebroken naam valt pas op als iemand de plaat voorleest."""
    woorden = zin.split()
    uit, huidig = [], ""
    for woord in woorden:
        if tw(woord, size, bold) > maxbreedte:
            return None
        kandidaat = f"{huidig} {woord}".strip()
        if tw(kandidaat, size, bold) <= maxbreedte:
            huidig = kandidaat
        else:
            uit.append(huidig)
            huidig = woord
    uit.append(huidig)
    return uit if len(uit) <= regels else None


def volledig(laag, product):
    """Een product met de gemeenschappelijke velden van zijn laag eronder."""
    samen = dict(laag.get("gemeenschappelijk", {}))
    samen.update(product)
    return samen


def jaar(product):
    datum = product.get("bron_datum")
    return str(datum)[:4] if datum else ""


def gedeelde_omvang(laag):
    """De omvang die alle getoonde producten van een laag delen, of een lege tekst.
    Staat die er, dan draagt de laagkop hem een keer in plaats van elk blok apart."""
    waarden = {(volledig(laag, p).get("omvang") or "").strip()
               for p in laag["producten"] if volledig(laag, p).get("op_plaat")}
    return waarden.pop() if len(waarden) == 1 and len(laag["producten"]) > 1 else ""


# ------------------------------------------------------------------- opmaak --

def meet_blok(product, maxbreedte, toon_omvang=True):
    """De maat van een productblok, en de regels die erin passen. Het jaartal staat
    linksonder naast de omvang; beide krijgen hun eigen ruimte, zodat geen tekst over
    een andere heen valt."""
    naam = product["naam"]
    omvang = (product.get("omvang") or "").strip() if toon_omvang else ""
    merk = jaar(product)
    merkbreedte = tw(merk, 9) + 10 if merk else 0
    for breedte in range(150, int(maxbreedte) + 1, 10):
        regels = breek(naam, breedte - 22, 12, True)
        if regels is None:
            continue
        omvangregels = breek(omvang, breedte - 22 - merkbreedte, 10, regels=3) if omvang else []
        if omvang and omvangregels is None:
            continue
        nodig = max(tw(r, 12, True) for r in regels) + 22
        for regel in omvangregels or []:
            nodig = max(nodig, tw(regel, 10) + 22 + merkbreedte)
        if not omvang:
            nodig = max(nodig, merkbreedte + 22)
        breedte = max(150, min(maxbreedte, nodig))
        return breedte, blokhoogte(regels, omvangregels, merk), regels, omvangregels
    regels = breek(naam, maxbreedte - 22, 12, True, regels=3) or [naam]
    omvangregels = breek(omvang, maxbreedte - 22 - merkbreedte, 10, regels=3) if omvang else []
    return maxbreedte, blokhoogte(regels, omvangregels, merk), regels, omvangregels or []


def blokhoogte(regels, omvangregels, merk):
    staart = max(len(omvangregels or []), 1 if merk else 0)
    return 16 + 15 * len(regels) + 13 * staart


def leg_uit(producten, x0, breedte, y0, toon_omvang=True):
    """Legt de blokken van een laag in rijen. Geeft de blokken en de gebruikte hoogte."""
    maxblok = min(248.0, breedte)
    gelegd, x, y, rijhoogte = [], x0, y0, 0
    for product in producten:
        w, h, regels, omvang = meet_blok(product, maxblok, toon_omvang)
        if x > x0 and x + w > x0 + breedte:
            x, y = x0, y + rijhoogte + TUSSEN
            rijhoogte = 0
        gelegd.append((product, x, y, w, h, regels, omvang))
        x += w + TUSSEN
        rijhoogte = max(rijhoogte, h)
    return gelegd, (y + rijhoogte) - y0


def teken_blok(product, x, y, w, h, regels, omvangregels):
    vul, rand = NIVEAU.get(product.get("detailniveau", "niet van toepassing"), (GRIJS, GRIJS_L))
    streep = "5 3" if product.get("aard") == "voorschrift" else None
    s = box(x, y, w, h, vul, rand, 4, streep, 1.2)
    for i, regel in enumerate(regels):
        s += text(x + 11, y + 17 + 15 * i, regel, 12, True)
    staart = y + 17 + 15 * len(regels)
    for i, regel in enumerate(omvangregels or []):
        s += text(x + 11, staart + 9 + 13 * i, regel, 10, fill=MUTED)
    merk = jaar(product)
    if merk:
        s += text(x + w - 8, staart + 9, merk, 9, fill=MUTED, anchor="end")
    return s


def teken_gereedschap(gereedschap, x, y, breedte, minimumhoogte):
    inhoud, onder = _gereedschap_inhoud(gereedschap, x, y, breedte)
    hoogte = max(minimumhoogte, onder - y + 14)
    s = box(x, y, breedte, hoogte, "#ffffff", "#b9c2bd", 8, "4 3", 1.4)
    return s + inhoud, y + hoogte


def _gereedschap_inhoud(gereedschap, x, y, breedte):
    s = text(x + 14, y + 24, "Gereedschap", 14, True)
    s += text(x + 14, y + 41, "gekozen door de solutionlaag", 11, fill=MUTED)
    cursor = y + 60
    for soort in gereedschap["soorten"]:
        s += text(x + 14, cursor, soort["soort"], 12, True, fill=PIJL)
        cursor += 15
        for regel in breek(soort["toelichting"], breedte - 28, 10) or []:
            s += text(x + 14, cursor, regel, 10, fill=MUTED)
            cursor += 12
        cursor += 2
        for item in soort["items"]:
            naam = item["naam"]
            laagje = item.get("lagenmodel", "")
            samen = tw(naam, 11, True) + tw(laagje, 9) + 30 <= breedte - 28
            hoogte = 22 if samen or not laagje else 34
            s += box(x + 14, cursor, breedte - 28, hoogte, "#f6f8f7", "#c4ccc8", 3)
            s += text(x + 22, cursor + 15, naam, 11, True)
            if laagje and samen:
                s += text(x + breedte - 22, cursor + 15, laagje, 9, fill=MUTED, anchor="end")
            elif laagje:
                s += text(x + 22, cursor + 28, laagje, 9, fill=MUTED)
            cursor += hoogte + 4
        cursor += 10
    return s, cursor


def teken_lijnen(lijnen, banden, links, rechts):
    """De lijnen die een laag overslaan of terugkeren, haaks gerouteerd in de linkermarge.
    Elke lijn krijgt haar eigen baan, zodat twee lijnen nooit samenvallen."""
    s = ""
    for i, lijn in enumerate(lijnen):
        baan = links + 16 + i * 24
        van, naar = banden.get(lijn["van"]), banden.get(lijn["naar"])
        if not van or not naar:
            continue
        y1 = van[0] + van[1] / 2
        y2 = naar[0] + naar[1] / 2
        streep = ' stroke-dasharray="6 4"' if lijn["soort"] != "overslaand" else ""
        punt = "url(#pijl)"
        s += (f'<path d="M{rechts:.0f} {y1:.0f} H{baan:.0f} V{y2:.0f} H{rechts:.0f}"'
              f' fill="none" stroke="{PIJL}" stroke-width="1.6"{streep}'
              f' marker-end="{punt}"/>')
        tekst_y = min(y1, y2) + abs(y1 - y2) / 2
        s += (f'<text x="{baan - 6:.0f}" y="{tekst_y:.0f}" font-family="{FONT}"'
              f' font-size="10" fill="{PIJL}" text-anchor="middle"'
              f' transform="rotate(-90 {baan - 6:.0f} {tekst_y:.0f})">{esc(lijn["label"])}</text>')
    return s


LEGENDA = ["Vulkleur: detailniveau", "Rand: aard van het product", "Rechtsonder in een blok"]


def teken_legenda(x, y, breedte):
    kolom = x + max(tw(k, 11, True) for k in LEGENDA) + 24
    s = text(x, y, "Legenda", 13, True)
    rij = y + 14
    s += text(x, rij + 12, LEGENDA[0], 11, True)
    kx = kolom
    for naam, (vul, rand) in NIVEAU.items():
        s += box(kx, rij + 1, 16, 14, vul, rand, 3)
        s += text(kx + 22, rij + 12, naam, 11, fill=MUTED)
        kx += 34 + tw(naam, 11)
    rij += 24
    s += text(x, rij + 12, LEGENDA[1], 11, True)
    s += box(kolom, rij + 1, 16, 14, "#ffffff", MUTED, 3, "5 3")
    s += text(kolom + 22, rij + 12, "voorschrift", 11, fill=MUTED)
    tweede = kolom + 32 + tw("voorschrift", 11) + 20
    s += box(tweede, rij + 1, 16, 14, "#ffffff", MUTED, 3)
    s += text(tweede + 22, rij + 12, "herbruikbaar product", 11, fill=MUTED)
    rij += 24
    s += text(x, rij + 12, LEGENDA[2], 11, True)
    s += text(kolom, rij + 12,
              "het jaar van vaststelling of laatste wijziging, zoals de bron die geeft",
              11, fill=MUTED)
    return s, rij + 24


def teken(data, breedte):
    lagen = data["lagen"]
    inhoud_x = MARGE_LINKS + KOP_BREEDTE + 16
    inhoud_breedte = breedte - inhoud_x - GEREEDSCHAP - RAND - 16

    y = 96
    banden, blokken, aantal = {}, [], 0
    for laag in lagen:
        producten = [volledig(laag, p) for p in laag["producten"]
                     if volledig(laag, p).get("op_plaat")]
        gedeeld = gedeelde_omvang(laag)
        gelegd, hoogte = leg_uit(producten, inhoud_x, inhoud_breedte, y + 16, not gedeeld)
        bandhoogte = max(hoogte + 32, 76)
        banden[laag["nummer"]] = (y, bandhoogte)
        blokken.append((laag, y, bandhoogte, gelegd, gedeeld))
        aantal += len(gelegd)
        y += bandhoogte + 10

    ladder_onder = y
    gereedschap_top = banden[5][0]
    s_ger, ger_onder = teken_gereedschap(data["gereedschap"],
                                         breedte - GEREEDSCHAP - RAND,
                                         gereedschap_top,
                                         GEREEDSCHAP,
                                         max(ladder_onder - gereedschap_top - 10, 320))
    legenda_y = max(ladder_onder, ger_onder) + 24
    s_leg, onder = teken_legenda(MARGE_LINKS, legenda_y, breedte)
    hoogte = onder + 40

    uit = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{breedte}" height="{hoogte:.0f}" '
           f'viewBox="0 0 {breedte} {hoogte:.0f}">',
           '<defs><marker id="pijl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
           f'markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="{PIJL}"/></marker></defs>',
           f'<rect width="{breedte}" height="{hoogte:.0f}" fill="#ffffff"/>']

    uit.append(text(MARGE_LINKS, 42, "De sectorketen en haar producten", 24, True))
    uit.append(text(MARGE_LINKS, 66,
                    "Wie maakt wat, van overheidsbreed kader tot koppelingimplementatie. "
                    f"Peildatum {data['peildatum']}.", 13, fill=MUTED))
    uit.append(text(breedte - RAND, 66,
                    f"{len(lagen)} lagen, {aantal} producten op de plaat", 12,
                    fill=MUTED, anchor="end"))

    for i, (laag, by, bh, gelegd, gedeeld) in enumerate(blokken):
        vul = BAND if i % 2 == 0 else BAND_ALT
        uit.append(box(MARGE_LINKS, by, breedte - MARGE_LINKS - RAND, bh, vul, LIJN, 6))
        uit.append(text(MARGE_LINKS + 14, by + 24, f"{laag['nummer']}  {laag['naam']}", 14, True))
        uit.append(text(MARGE_LINKS + 14, by + 41, laag["soort"], 10, fill=MUTED))
        partijen = ", ".join(laag["partijen"])
        regels = breek(partijen, KOP_BREEDTE - 24, 11, True, regels=3) or [partijen]
        for j, regel in enumerate(regels):
            uit.append(text(MARGE_LINKS + 14, by + 58 + 14 * j, regel, 11, True, fill=PIJL))
        if gedeeld:
            onderkant = by + 58 + 14 * len(regels)
            for j, regel in enumerate(breek(gedeeld, KOP_BREEDTE - 24, 10, regels=2) or []):
                uit.append(text(MARGE_LINKS + 14, onderkant + 4 + 12 * j, regel, 10, fill=MUTED))
        for product, x, py, w, h, regels, omvang in gelegd:
            uit.append(teken_blok(product, x, py, w, h, regels, omvang))

    uit.append(s_ger)
    kiest_y = banden[6][0] + banden[6][1] / 2
    uit.append(f'<path d="M{breedte - GEREEDSCHAP - RAND:.0f} {kiest_y:.0f} '
               f'H{breedte - GEREEDSCHAP - RAND - 16:.0f}" fill="none" stroke="{PIJL}" '
               f'stroke-width="1.6" marker-end="url(#pijl)"/>')
    uit.append(teken_lijnen(data.get("lijnen", []), banden, 0, MARGE_LINKS))
    uit.append(s_leg)
    uit.append("</svg>")
    return "\n".join(uit), aantal


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--bron", type=pathlib.Path, default=BRON)
    p.add_argument("--uit", type=pathlib.Path, default=UIT)
    p.add_argument("--breedte", type=int, default=1680)
    a = p.parse_args()

    data = json.loads(a.bron.read_text(encoding="utf-8"))
    svg, aantal = teken(data, a.breedte)
    a.uit.parent.mkdir(parents=True, exist_ok=True)
    a.uit.write_text(svg + "\n", encoding="utf-8")

    lijnen = len(data.get("lijnen", []))
    gereedschap = sum(len(s["items"]) for s in data["gereedschap"]["soorten"])
    print(f"{a.uit}: {len(data['lagen'])} lagen, {aantal} producten, "
          f"{gereedschap} standaarden, {lijnen} lijnen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
