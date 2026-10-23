#!/usr/bin/env python3
"""De sectorketen tekenen: per laag de partijen en de producten die zij maken.

Waarom dit script bestaat: de beheerketenplaat uit de start van OKx is een export uit een
presentatie, en die veroudert zodra de keten verandert. Deze plaat komt uit
`doc/sectorketen-producten.json`, zodat een actualisatie een wijziging in de bron is en het
beeld meeloopt met de catalogus die uit diezelfde bron komt.

Drie kenmerken dragen het beeld; het oordeel laat de plaat aan de lezer:

  vulkleur    de ArchiMate-laag van het elementtype, met het standaardpalet van Archi
  rand        de aard: onderbroken voor een voorschrift, doorgetrokken voor een product
  staafje     het MIM-niveau, van begrippen tot technisch gegevensmodel

Daarnaast verbindt de modelketen dezelfde inhoud op vier MIM-niveaus, dwars door de lagen
heen, zoals AMIGO paragraaf 5.4 die route voorschrijft.

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

# Het standaardpalet van Archi, per ArchiMate-laag.
LAAGKLEUR = {
    "motivatie": ("#ccccff", "#8a8ad6"),
    "strategie": ("#f5deaa", "#bf9b4e"),
    "business": ("#ffffb5", "#a8a85a"),
    "applicatie": ("#b5ffff", "#5aa8a8"),
    "technologie": ("#c9e7b7", "#7aa864"),
    "implementatie": ("#ffe0e0", "#d49a9a"),
    "composiet": ("#f2f2f2", "#9a9a9a"),
}

ELEMENTLAAG = {
    "Principle": "motivatie", "Requirement": "motivatie", "Constraint": "motivatie",
    "Goal": "motivatie", "Driver": "motivatie", "Outcome": "motivatie",
    "Meaning": "motivatie", "Stakeholder": "motivatie",
    "Resource": "strategie", "Capability": "strategie", "Course of Action": "strategie",
    "Value Stream": "strategie",
    "Business Actor": "business", "Business Role": "business", "Business Process": "business",
    "Business Object": "business", "Contract": "business", "Representation": "business",
    "Application Component": "applicatie", "Application Interface": "applicatie",
    "Data Object": "applicatie", "Application Service": "applicatie",
    "Node": "technologie", "Artifact": "technologie",
    "Deliverable": "implementatie", "Plateau": "implementatie", "Gap": "implementatie",
    "Work Package": "implementatie",
    "Grouping": "composiet", "Location": "composiet",
}

# De pictogrammen van ArchiMate, in een vak van 16 bij 16.
PICTOGRAM = {
    "Principle": '<rect x="2" y="2" width="12" height="12" rx="1"/><path d="M8 5v4"/><path d="M8 11v0.6"/>',
    "Requirement": '<path d="M4 4h10l-2 8H2z"/>',
    "Constraint": '<path d="M4 4h10l-2 8H2z"/><path d="M11 3L5 13"/>',
    "Goal": '<circle cx="8" cy="8" r="6"/><circle cx="8" cy="8" r="2.5"/>',
    "Driver": '<circle cx="8" cy="8" r="6"/><path d="M8 2v12M2 8h12"/>',
    "Meaning": '<path d="M4 11a3 3 0 0 1 0-5a3.5 3.5 0 0 1 6-2a3 3 0 0 1 2.5 7z"/>',
    "Value Stream": '<path d="M2 3h8l4 5l-4 5H2l4-5z"/>',
    "Capability": '<rect x="2" y="7" width="12" height="7" rx="1"/><rect x="2" y="2" width="5" height="4"/><rect x="8" y="2" width="6" height="4"/>',
    "Course of Action": '<circle cx="8" cy="8" r="6"/><circle cx="8" cy="8" r="2"/><path d="M8 8l5-5"/>',
    "Resource": '<rect x="2" y="4" width="12" height="8" rx="1"/><path d="M5 7h6M5 10h6"/>',
    "Business Actor": '<circle cx="8" cy="4.5" r="2.5"/><path d="M3 14v-1a5 5 0 0 1 10 0v1"/>',
    "Business Process": '<path d="M2 5h8V2l5 6l-5 6v-3H2z"/>',
    "Business Object": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>',
    "Contract": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6h12M2 10h12"/>',
    "Data Object": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>',
    "Application Component": '<rect x="4" y="2" width="10" height="12"/><rect x="2" y="4" width="4" height="2.5"/><rect x="2" y="8.5" width="4" height="2.5"/>',
    "Application Interface": '<circle cx="11" cy="8" r="3"/><path d="M2 8h6"/>',
    "Artifact": '<path d="M3 2h7l3 3v9H3z"/><path d="M10 2v3h3"/>',
    "Deliverable": '<path d="M3 2h10v10q-2.5 2-5 0t-5 0z"/>',
    "Grouping": '<path d="M2 5h5V3h7v10H2z" stroke-dasharray="3 2"/>',
    "Work Package": '<rect x="2" y="5" width="12" height="7" rx="3.5"/>',
    "Plateau": '<path d="M2 4h12M2 8h12M2 12h12"/>',
    "Gap": '<ellipse cx="8" cy="8" rx="6" ry="4"/><path d="M2 8h12"/>',
}

MIM = ["begrippen", "conceptueel informatiemodel", "logisch gegevensmodel",
       "technisch gegevensmodel"]
INHOUD = ["onderwijsbreed", "toepassingsgebied", "inrichting"]

INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#d8ddda"
BAND, BAND_ALT = "#fbfcfb", "#f2f5f3"
PIJL, KETEN = "#2f5d8a", "#b1552a"
VOL, LEEG = "#4a4a4a", "#ffffff"
FONT = "Arial, Helvetica, sans-serif"

MARGE_LINKS = 140     # ruimte voor de lijnen die een laag overslaan
KOP_BREEDTE = 240     # de kolom met laagnummer, soort en partijen
GEREEDSCHAP = 300     # de kolom rechts
TUSSEN = 14           # ruimte tussen twee productblokken in een rij
BANDGAT = 34          # ruimte tussen twee banden, waar de ketenlijnen lopen
RAND = 24
STAART = 8            # ruimte onder de laatste tekstregel in een blok
PICTOGRAM_RUIMTE = 28  # ruimte rechtsboven in een blok voor het pictogram
GOOT = 44             # vrije baan links van de blokken, waar een ketenlijn loopt
MIMBREEDTE = 4 * 7 + 3 * 2
INHOUDBREEDTE = 42


def tw(s, size, bold=False):
    """Geschatte tekstbreedte in px, ruim genomen. De plaat wordt ook gerenderd met een
    vervangend lettertype dat breder zet dan Arial; de marge vangt dat op."""
    return len(s) * size * (0.68 if bold else 0.60)


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


def pictogramsleutel(soort):
    return "pic-" + soort.lower().replace(" ", "-")


def pictogrammen():
    """De pictogrammen staan een keer in `defs` en worden met `use` geplaatst. Dat scheelt
    herhaling, en de keuring kijkt niet in `defs`: een glyph mag schuine lijntjes dragen,
    een verbindingslijn op de plaat niet."""
    return "".join(f'<g id="{pictogramsleutel(soort)}" stroke-linejoin="round"'
                   f' stroke-width="1.2">{vorm}</g>'
                   for soort, vorm in PICTOGRAM.items())


def pictogram(soort, x, y, kleur):
    if soort not in PICTOGRAM:
        return ""
    return (f'<use href="#{pictogramsleutel(soort)}" x="{x:.0f}" y="{y:.0f}"'
            f' fill="none" stroke="{kleur}"/>')


def mimbalk(x, y, niveau, kleur):
    """Vier segmenten, gevuld tot het MIM-niveau. Hoe dieper het niveau, hoe voller."""
    if niveau not in MIM:
        return ""
    tot = MIM.index(niveau) + 1
    s = ""
    for i in range(4):
        s += (f'<rect x="{x + i * 9:.0f}" y="{y:.0f}" width="7" height="5" rx="1"'
              f' fill="{VOL if i < tot else LEEG}" stroke="{kleur}" stroke-width="0.8"/>')
    return s


def inhoudwig(x, y, gebied, kleur):
    """De horizontale as van de AMIGO-modellenmatrix als wig: breed bij onderwijsbreed en
    smal bij inrichting, met het eigen vak gevuld. De vorm is bewust een wig, zodat zij op
    het eerste oog verschilt van het rechthoekige MIM-staafje ernaast."""
    if gebied not in INHOUD:
        return ""
    tot = INHOUD.index(gebied)
    s, breed = "", INHOUDBREEDTE / 3
    for i in range(3):
        links, rechts = 5.0 - i * 1.0, 5.0 - (i + 1) * 1.0
        x0 = x + i * breed
        punten = (f"{x0:.1f},{y + 3 - links:.1f} {x0 + breed - 1:.1f},{y + 3 - rechts:.1f} "
                  f"{x0 + breed - 1:.1f},{y + 3 + rechts:.1f} {x0:.1f},{y + 3 + links:.1f}")
        s += (f'<polygon points="{punten}" fill="{VOL if i == tot else LEEG}"'
              f' stroke="{kleur}" stroke-width="0.8"/>')
    return s


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


def breek_ruim(zin, maxbreedte, size, bold=False):
    """Breekt een naam zonder bovengrens op het aantal regels. De aanroeper gebruikt dit
    pas nadat `breek` het heeft opgegeven, zodat een naam altijd heel blijft."""
    for regels in range(2, 7):
        uit = breek(zin, maxbreedte, size, bold, regels)
        if uit is not None:
            return uit
    return [zin]


def volledig(laag, product):
    """Een product met de gemeenschappelijke velden van zijn laag eronder."""
    samen = dict(laag.get("gemeenschappelijk", {}))
    samen.update(product)
    return samen


def jaar(product):
    datum = product.get("bron_datum")
    return str(datum)[:4] if datum else ""


def tweede_regel(product):
    """De invulling waar die er is, anders het aantal deelproducten. Een absoluut aantal
    objecten in een model zegt in deze plaat weinig; de MIM-diepte doet dat wel."""
    if product.get("invulling"):
        return product["invulling"]
    deel = product.get("deelproducten") or []
    if len(deel) == 1:
        return "1 deelproduct"
    return f"{len(deel)} deelproducten" if deel else ""


def kleur(product):
    return LAAGKLEUR[ELEMENTLAAG.get(product.get("archimate"), "composiet")]


# ------------------------------------------------------------------- opmaak --

def meet_blok(product, maxbreedte):
    """De maat van een productblok en de regels die erin passen. Het pictogram staat
    rechtsboven, het MIM-staafje linksonder en het jaartal rechtsonder; alle drie krijgen
    hun eigen ruimte, zodat geen tekst over een andere heen valt."""
    naam, tweede = product["naam"], tweede_regel(product)
    merk = "voorgenomen" if product.get("voorgenomen") else jaar(product)
    wig = INHOUDBREEDTE + 8 if product.get("inhoudsgebied") in INHOUD else 0
    voet = MIMBREEDTE + wig + (tw(merk, 10) + 10 if merk else 0) + 8
    # Een enkel woord dat breder is dan het blok mag het blok verbreden; afkappen hoort niet.
    langste = max(tw(w, 12, True) for w in naam.split()) + 22 + PICTOGRAM_RUIMTE
    maxbreedte = max(maxbreedte, langste)
    for breedte in range(160, int(maxbreedte) + 1, 10):
        regels = breek(naam, breedte - 22 - PICTOGRAM_RUIMTE, 12, True)
        if regels is None:
            continue
        tweederegels = breek(tweede, breedte - 22, 10, regels=2) if tweede else []
        if tweede and tweederegels is None:
            continue
        nodig = max(tw(r, 12, True) for r in regels) + 22 + PICTOGRAM_RUIMTE
        for regel in tweederegels or []:
            nodig = max(nodig, tw(regel, 10) + 22)
        nodig = max(nodig, voet + 22)
        return (max(160, min(maxbreedte, nodig)),
                blokhoogte(regels, tweederegels, product), regels, tweederegels)
    regels = breek_ruim(naam, maxbreedte - 22 - PICTOGRAM_RUIMTE, 12, True)
    tweederegels = breek_ruim(tweede, maxbreedte - 22, 10) if tweede else []
    return maxbreedte, blokhoogte(regels, tweederegels, product), regels, tweederegels or []


def blokhoogte(regels, tweederegels, product):
    voet = 15 if (product.get("mim_niveau") in MIM or jaar(product)
                  or product.get("voorgenomen")
                  or product.get("inhoudsgebied") in INHOUD) else 0
    return 11 + STAART + 15 * len(regels) + 13 * len(tweederegels or []) + voet


def leg_uit(producten, x0, breedte, y0):
    """Legt de blokken van een laag in rijen. Een product dat in een keten zit komt vooraan,
    zodat de leden van een keten over de banden heen op een lijn liggen en de verbindende
    tand geen ander blok doorsnijdt."""
    maxblok = min(252.0, breedte)
    producten = sorted(producten, key=lambda p: 0 if p.get("familie") else 1)
    gelegd, x, y, rijhoogte = [], x0, y0, 0
    for product in producten:
        w, h, regels, tweede = meet_blok(product, maxblok)
        if x > x0 and x + w > x0 + breedte:
            x, y = x0, y + rijhoogte + TUSSEN
            rijhoogte = 0
        gelegd.append((product, x, y, w, h, regels, tweede))
        x += w + TUSSEN
        rijhoogte = max(rijhoogte, h)
    return gelegd, (y + rijhoogte) - y0


def teken_blok(product, x, y, w, h, regels, tweederegels):
    vul, rand = kleur(product)
    streep = "5 3" if product.get("aard") == "voorschrift" else None
    s = box(x, y, w, h, "#ffffff", rand, 4, streep, 1.2)
    dekking = ' fill-opacity="0.35"' if product.get("voorgenomen") else ""
    s += (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4"'
          f' fill="{vul}"{dekking} stroke="none"/>')

    if not product.get("voorgenomen"):
        s += pictogram(product.get("archimate"), x + w - 20, y + 5, rand)
    for i, regel in enumerate(regels):
        s += text(x + 11, y + 17 + 15 * i, regel, 12, True)
    staart = y + 17 + 15 * len(regels)
    for i, regel in enumerate(tweederegels or []):
        s += text(x + 11, staart + 9 + 13 * i, regel, 10, fill=MUTED)
    voet = y + h - STAART
    s += mimbalk(x + 11, voet - 5, product.get("mim_niveau"), rand)
    wig_x = x + 11 + (MIMBREEDTE + 8 if product.get("mim_niveau") in MIM else 0)
    s += inhoudwig(wig_x, voet - 5, product.get("inhoudsgebied"), rand)
    merk = "voorgenomen" if product.get("voorgenomen") else jaar(product)
    if merk:
        s += text(x + w - 8, voet, merk, 10, fill=MUTED, anchor="end")
    return s


def teken_keten(keten, plekken, goot):
    """De leden van een keten als kam tekenen: een ruggengraat in de goot, met een tand naar
    elk lid. Omdat de leden in hun band vooraan staan, liggen hun linkerranden op een lijn en
    snijdt geen tand een blok. De volgorde leest af aan het MIM-staafje in de blokken zelf."""
    punten = [plekken[naam] for naam in keten["leden"] if naam in plekken]
    if len(punten) < 2:
        return "", 0
    ruggengraat = goot + 14
    rijen = {}
    for x, y, w, h in punten:
        rijen.setdefault(round(y), []).append((x, y, w, h))
    middens = [y + h / 2 for _, y, _, h in punten]
    s = (f'<path d="M{ruggengraat:.0f} {min(middens):.0f} V{max(middens):.0f}"'
         f' fill="none" stroke="{KETEN}" stroke-width="1.8"/>')
    segmenten = 0
    for leden in rijen.values():
        leden.sort(key=lambda b: b[0])
        x, y, w, h = leden[0]
        s += (f'<path d="M{ruggengraat:.0f} {y + h / 2:.0f} H{x:.0f}" fill="none"'
              f' stroke="{KETEN}" stroke-width="1.8" marker-end="url(#keten)"/>')
        segmenten += 1
        for (x1, y1, w1, h1), (x2, y2, _, h2) in zip(leden, leden[1:]):
            s += (f'<path d="M{x1 + w1:.0f} {y1 + h1 / 2:.0f} H{x2:.0f}" fill="none"'
                  f' stroke="{KETEN}" stroke-width="1.8" marker-end="url(#keten)"/>')
            segmenten += 1
    s += text(ruggengraat - 4, min(middens) - 9, keten["naam"], 10, True,
              fill=KETEN, anchor="end")
    return s, segmenten


def teken_gereedschap(gereedschap, x, y, breedte, minimumhoogte):
    inhoud, onder = _gereedschap_inhoud(gereedschap, x, y, breedte)
    hoogte = max(minimumhoogte, onder - y + 14)
    return box(x, y, breedte, hoogte, "#ffffff", "#b9c2bd", 8, "4 3", 1.4) + inhoud, y + hoogte


def _gereedschap_inhoud(gereedschap, x, y, breedte):
    s = text(x + 14, y + 24, "Gereedschap", 14, True)
    s += text(x + 14, y + 40, "gekozen door de solutionlaag", 11, fill=MUTED)
    s += text(x + 14, y + 54, "rechts: de laag in het Edustandaard Lagenmodel", 10, fill=MUTED)
    cursor = y + 74
    for soort in gereedschap["soorten"]:
        s += text(x + 14, cursor, soort["soort"], 12, True, fill=PIJL)
        cursor += 15
        for regel in breek(soort["toelichting"], breedte - 28, 10) or []:
            s += text(x + 14, cursor, regel, 10, fill=MUTED)
            cursor += 12
        cursor += 2
        for item in soort["items"]:
            naam, laagje = item["naam"], item.get("lagenmodel", "")
            fundament = item.get("fundament", "")
            samen = tw(naam, 11, True) + tw(laagje, 10) + 30 <= breedte - 28
            hoogte = (22 if samen or not laagje else 34) + (13 if fundament else 0)
            s += box(x + 14, cursor, breedte - 28, hoogte, "#f6f8f7", "#c4ccc8", 3)
            s += text(x + 22, cursor + 15, naam, 11, True)
            if laagje and samen:
                s += text(x + breedte - 22, cursor + 15, laagje, 10, fill=MUTED, anchor="end")
            elif laagje:
                s += text(x + 22, cursor + 28, laagje, 10, fill=MUTED)
            if fundament:
                s += text(x + 22, cursor + hoogte - 5, f"op {fundament}", 10, fill=PIJL)
            cursor += hoogte + 4
        cursor += 10
    return s, cursor


def teken_ladder(banden, rechts):
    """De gewone levering: elke laag levert aan de laag eronder. Een doorgaande lijn vlak
    langs de banden, met een pijlpunt in elk gat. Zonder deze lijn toont de plaat alleen de
    uitzonderingen, en leest de ketting als een verzameling losse banden."""
    nummers = sorted(banden)
    x = rechts - 12
    boven = banden[nummers[0]][0] + 20
    onder = banden[nummers[-1]][0] + banden[nummers[-1]][1] - 20
    s = f'<path d="M{x:.0f} {boven:.0f} V{onder:.0f}" fill="none" stroke="{PIJL}" stroke-width="1.6"/>'
    for a, b in zip(nummers, nummers[1:]):
        gat = banden[a][0] + banden[a][1]
        s += (f'<path d="M{x:.0f} {gat:.0f} V{gat + BANDGAT - 6:.0f}" fill="none"'
              f' stroke="{PIJL}" stroke-width="1.6" marker-end="url(#pijl)"/>')
    midden = (boven + onder) / 2
    s += (f'<rect x="{x - 13:.0f}" y="{midden - 36:.0f}" width="13" height="72" fill="#ffffff"/>')
    s += (f'<text x="{x - 6:.0f}" y="{midden:.0f}" font-family="{FONT}" font-size="10"'
          f' fill="{PIJL}" text-anchor="middle"'
          f' transform="rotate(-90 {x - 6:.0f} {midden:.0f})">levert aan de laag eronder</text>')
    return s


def teken_lijnen(lijnen, banden, rechts):
    """De lijnen die een laag overslaan of terugkeren, haaks gerouteerd in de linkermarge.
    Elke lijn krijgt haar eigen baan, en elk opschrift een witte onderlaag, zodat een
    dwarssegment van een buurbaan er niet doorheen leest."""
    s = ""
    for i, lijn in enumerate(lijnen):
        baan = 16 + i * 26
        van, naar = banden.get(lijn["van"]), banden.get(lijn["naar"])
        if not van or not naar:
            continue
        y1, y2 = van[0] + van[1] / 2, naar[0] + naar[1] / 2
        streep = ' stroke-dasharray="6 4"' if lijn["soort"] != "overslaand" else ""
        heen = ' marker-start="url(#pijl-terug)"' if lijn["soort"] == "tweezijdig" else ""
        s += (f'<path d="M{rechts:.0f} {y1:.0f} H{baan:.0f} V{y2:.0f} H{rechts:.0f}"'
              f' fill="none" stroke="{PIJL}" stroke-width="1.6"{streep}'
              f'{heen} marker-end="url(#pijl)"/>')
        midden = min(y1, y2) + abs(y1 - y2) / 2
        lx, label = baan - 7, lijn["label"]
        halve = tw(label, 10) / 2 + 4
        s += (f'<rect x="{lx - 7:.0f}" y="{midden - halve:.0f}" width="13"'
              f' height="{2 * halve:.0f}" fill="#ffffff"/>')
        s += (f'<text x="{lx:.0f}" y="{midden:.0f}" font-family="{FONT}" font-size="10"'
              f' fill="{PIJL}" text-anchor="middle"'
              f' transform="rotate(-90 {lx:.0f} {midden:.0f})">{esc(label)}</text>')
    return s


def teken_legenda(x, y, ketens):
    kop = ["Vulkleur: ArchiMate-laag", "Rand: aard", "Staafje: MIM-niveau",
           "Jaartal: ouderdom", "Lijn langs de ladder", "Oranje lijn",
           "Lichte vulling", "Blauwe ladder"]
    kolom = x + max(tw(k, 11, True) for k in kop) + 24
    s = text(x, y, "Legenda", 13, True)
    rij = y + 14
    s += text(x, rij + 12, kop[0], 11, True)
    kx = kolom
    for naam, (vul, rand) in LAAGKLEUR.items():
        s += box(kx, rij + 1, 16, 14, vul, rand, 3)
        s += text(kx + 21, rij + 12, naam, 10, fill=MUTED)
        kx += 28 + tw(naam, 10)
    rij += 24
    s += text(x, rij + 12, kop[1], 11, True)
    s += box(kolom, rij + 1, 16, 14, "#ffffff", MUTED, 3, "5 3")
    s += text(kolom + 21, rij + 12, "voorschrift", 10, fill=MUTED)
    tweede = kolom + 31 + tw("voorschrift", 10) + 20
    s += box(tweede, rij + 1, 16, 14, "#ffffff", MUTED, 3)
    s += text(tweede + 21, rij + 12, "herbruikbaar product", 10, fill=MUTED)
    rij += 24
    s += text(x, rij + 12, kop[2], 11, True)
    kx = kolom
    for niveau in MIM:
        s += mimbalk(kx, rij + 3, niveau, MUTED)
        s += text(kx + MIMBREEDTE + 6, rij + 12, niveau, 10, fill=MUTED)
        kx += MIMBREEDTE + 14 + tw(niveau, 10)
    rij += 24
    s += text(x, rij + 12, "Wig: AMIGO-inhoudsgebied", 11, True)
    kx = kolom
    for gebied in INHOUD:
        s += inhoudwig(kx, rij + 3, gebied, MUTED)
        s += text(kx + INHOUDBREEDTE + 6, rij + 12, gebied, 10, fill=MUTED)
        kx += INHOUDBREEDTE + 14 + tw(gebied, 10)
    rij += 24
    s += text(x, rij + 12, kop[3], 11, True)
    s += text(kolom, rij + 12, "het jaar van vaststelling of laatste wijziging zoals de bron "
              "die geeft; rechtsboven staat het ArchiMate-elementtype", 10, fill=MUTED)
    rij += 20
    s += text(x, rij + 12, kop[4], 11, True)
    s += text(kolom, rij + 12, "doorgetrokken waar een laag wordt overgeslagen, gestreept bij "
              "terugkoppeling en bij uitwisseling in twee richtingen", 10, fill=MUTED)
    rij += 20
    s += text(x, rij + 12, kop[7], 11, True)
    s += text(kolom, rij + 12, "de gewone levering: elke laag levert aan de laag eronder",
              10, fill=MUTED)
    rij += 20
    s += text(x, rij + 12, kop[6], 11, True)
    s += text(kolom, rij + 12, "voorgenomen werk, nog zonder opgeleverd product", 10, fill=MUTED)
    rij += 20
    s += text(x, rij + 12, kop[5], 11, True)
    for keten in ketens:
        for i, regel in enumerate(breek(f"{keten['naam']}: {keten['toelichting']}",
                                        1180, 10, regels=3) or []):
            s += text(kolom, rij + 12 + 13 * i, regel, 10, fill=KETEN)
        rij += 13 * len(breek(f"{keten['naam']}: {keten['toelichting']}", 1180, 10, regels=3) or [1])
    return s, rij + 20


def teken(data, breedte):
    lagen = data["lagen"]
    goot = MARGE_LINKS + KOP_BREEDTE
    inhoud_x = goot + GOOT
    inhoud_breedte = breedte - inhoud_x - GEREEDSCHAP - RAND - 16

    y = 96
    banden, blokken, plekken, aantal = {}, [], {}, 0
    for laag in lagen:
        producten = [volledig(laag, p) for p in laag["producten"]
                     if volledig(laag, p).get("op_plaat")]
        gelegd, hoogte = leg_uit(producten, inhoud_x, inhoud_breedte, y + 16)
        bandhoogte = max(hoogte + 32, 92)
        banden[laag["nummer"]] = (y, bandhoogte)
        blokken.append((laag, y, bandhoogte, gelegd))
        for product, px, py, pw, ph, _, _ in gelegd:
            plekken[product["naam"]] = (px, py, pw, ph)
        aantal += len(gelegd)
        y += bandhoogte + BANDGAT

    ladder_onder = y - BANDGAT
    s_ger, ger_onder = teken_gereedschap(data["gereedschap"], breedte - GEREEDSCHAP - RAND,
                                         banden[5][0], GEREEDSCHAP,
                                         max(ladder_onder - banden[5][0], 320))
    ketens = data.get("ketens", [])
    s_leg, onder = teken_legenda(MARGE_LINKS, max(ladder_onder, ger_onder) + 28, ketens)
    hoogte = onder + 40

    uit = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{breedte}" height="{hoogte:.0f}" '
           f'viewBox="0 0 {breedte} {hoogte:.0f}">',
           '<defs>' + pictogrammen() +
           '<marker id="pijl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
           f'markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="{PIJL}"/></marker>'
           '<marker id="pijl-terug" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" '
           f'markerHeight="7" orient="auto"><path d="M10 1L1 5L10 9z" fill="{PIJL}"/></marker>'
           '<marker id="keten" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
           f'markerHeight="6" orient="auto"><path d="M0 1L9 5L0 9z" fill="{KETEN}"/></marker>'
           '</defs>',
           f'<rect width="{breedte}" height="{hoogte:.0f}" fill="#ffffff"/>']

    uit.append(text(MARGE_LINKS, 42, "De sectorketen en haar producten", 24, True))
    uit.append(text(MARGE_LINKS, 66,
                    "Wie maakt wat, van overheidsbreed kader tot koppelingimplementatie. "
                    f"Peildatum {data['peildatum']}.", 13, fill=MUTED))
    uit.append(text(breedte - RAND, 66,
                    f"{len(lagen)} lagen, {aantal} producten getoond", 12,
                    fill=MUTED, anchor="end"))

    for i, (laag, by, bh, gelegd) in enumerate(blokken):
        vul = BAND if i % 2 == 0 else BAND_ALT
        uit.append(box(MARGE_LINKS, by, breedte - MARGE_LINKS - RAND, bh, vul, LIJN, 6))
        uit.append(text(MARGE_LINKS + 14, by + 24, f"{laag['nummer']}  {laag['naam']}", 14, True))
        onderkant = by + 40
        for regel in breek(laag["soort"], KOP_BREEDTE - 24, 10, regels=2) or []:
            uit.append(text(MARGE_LINKS + 14, onderkant, regel, 10, fill=MUTED))
            onderkant += 12
        partijen = ", ".join(laag["partijen"])
        for regel in breek(partijen, KOP_BREEDTE - 24, 11, True, regels=3) or [partijen]:
            uit.append(text(MARGE_LINKS + 14, onderkant + 10, regel, 11, True, fill=PIJL))
            onderkant += 14
        for product, x, py, w, h, regels, tweede in gelegd:
            uit.append(teken_blok(product, x, py, w, h, regels, tweede))

    uit.append(s_ger)
    for nummer in data["gereedschap"].get("raakt_lagen", [6]):
        if nummer not in banden:
            continue
        raak = banden[nummer][0] + banden[nummer][1] / 2
        uit.append(f'<path d="M{breedte - GEREEDSCHAP - RAND:.0f} {raak:.0f} '
                   f'H{breedte - GEREEDSCHAP - RAND - 16:.0f}" fill="none" stroke="{PIJL}" '
                   f'stroke-width="1.6" marker-end="url(#pijl)"/>')
    uit.append(teken_ladder(banden, MARGE_LINKS))
    uit.append(teken_lijnen(data.get("lijnen", []), banden, MARGE_LINKS - 24))
    segmenten = 0
    for keten in ketens:
        svg, n = teken_keten(keten, plekken, goot)
        uit.append(svg)
        segmenten += n
    uit.append(s_leg)
    uit.append("</svg>")
    return "\n".join(uit), aantal, segmenten


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--bron", type=pathlib.Path, default=BRON)
    p.add_argument("--uit", type=pathlib.Path, default=UIT)
    p.add_argument("--breedte", type=int, default=1680)
    a = p.parse_args()

    data = json.loads(a.bron.read_text(encoding="utf-8"))
    svg, aantal, segmenten = teken(data, a.breedte)
    a.uit.parent.mkdir(parents=True, exist_ok=True)
    a.uit.write_text(svg + "\n", encoding="utf-8")

    soorten = {volledig(laag, p).get("archimate")
               for laag in data["lagen"] for p in laag["producten"]}
    print(f"{a.uit}: {len(data['lagen'])} lagen, {aantal} producten, "
          f"{len(soorten)} ArchiMate-typen, {segmenten} ketensegmenten, "
          f"{len(data.get('lijnen', []))} laaglijnen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
