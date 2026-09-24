#!/usr/bin/env python3
"""Per fase de informatiestromen van het voorbeeld markeren op de hoofdplaat.

Waarom dit script bestaat: een stroombeeld toont twee componenten en de objecten die
tussen hen bewegen, maar niet waar die lijn op de hoofdplaat loopt. Dit script legt
over een render van hoofdplaat v1.7 een markering per stroom die het voorbeeld in die
fase raakt, met het beeld-ID erbij, en omlijnt de betrokken componenten. Een stroom
die de plaat nog niet kent, staat als gestippelde lijn tussen de twee componenten:
zichtbaar wat er ontbreekt.

    python3 scripts/teken-hoofdplaat-highlight.py --plaat img/hoofdplaat.png

Het model wordt alleen gelezen; raak nooit een .archimate-bestand aan.
"""

import argparse
import base64
import collections
import html
import importlib.util
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("platen", WORTEL / "exporteer-archimate-platen.py")
platen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(platen)

MODEL = pathlib.Path("architecture/model/model.archimate")
REGELS = pathlib.Path("architecture/model/informatiemodel/voorbeeld-lr1-regels.json")
STROMEN = pathlib.Path("architecture/model/informatiemodel/stromen.json")
UITMAP = pathlib.Path("architecture/model/informatiemodel/img/hoofdplaat")
PLAAT = UITMAP / "hoofdplaat-v1.7.jpg"
VIEW = "OKx hoofdplaat v1.7<concept>"
GEEN_PIJL = "geen pijl op de hoofdplaat"
MARGE = 10  # Archi rendert de view met tien pixels marge; met dezelfde marge vallen de markeringen op de pijlen
ACCENT = "#d9531e"
RAND = "#1f6feb"


def norm(s):
    return " ".join(str(s or "").split())


def stromen_per_fase(regels):
    """Per fase de stromen: (van, naar, pijl) met de beeld-ID's die haar gebruiken."""
    uit = collections.OrderedDict()
    for r in regels["regels"]:
        if r["soort"] != "stroomt":
            continue
        sleutel = (norm(r["van"]), norm(r["naar"]), r.get("pijl"))
        rij = uit.setdefault(r["fase"], collections.OrderedDict()).setdefault(sleutel, [])
        if r.get("beeld_id") and r["beeld_id"] not in rij:
            rij.append(r["beeld_id"])
    return uit


def stromen_per_koppeling(regels, namen):
    """De stromen van de gevraagde koppelingen, elk gelabeld met de naam van die koppeling.

    Waarvoor: laten zien wat een koppeling in de keten raakt. Niet de beelden van een fase,
    maar per lijn welke koppeling erover loopt, zodat een plaat de koppelingen naast elkaar zet.
    """
    uit = collections.OrderedDict()
    for r in regels["regels"]:
        if r["soort"] != "stroomt" or r.get("koppeling") not in namen:
            continue
        rij = uit.setdefault((norm(r["van"]), norm(r["naar"]), r.get("pijl")), [])
        if r["koppeling"] not in rij:
            rij.append(r["koppeling"])
    return uit


def knopen_van_component(knopen, elems, naam):
    """Alle knopen op de view die dit applicatiecomponent tonen; een component staat er soms meer dan een keer."""
    return [k for k in knopen.values() if norm(elems.get(k.get("element", ""), ("", ""))[1]) == naam]


def dichtste_paar(knopen, elems, van, naar):
    """Het paar knopen dat het dichtst bij elkaar ligt, zodat de lijn tussen de bedoelde twee vakken loopt."""
    links, rechts = knopen_van_component(knopen, elems, van), knopen_van_component(knopen, elems, naar)
    if not links or not rechts:
        return None, None
    def midden(k):
        return (k["x"] + k["w"] / 2, k["y"] + k["h"] / 2)
    beste = min(((a, b) for a in links for b in rechts),
                key=lambda ab: (midden(ab[0])[0] - midden(ab[1])[0]) ** 2 + (midden(ab[0])[1] - midden(ab[1])[1]) ** 2)
    return beste


def lees_geometrie(model):
    import xml.etree.ElementTree as ET
    root = ET.parse(model).getroot()
    XSI = platen.XSI
    elems = {e.get("id"): (e.get(XSI, "").split(":")[-1], norm(e.get("name"))) for e in root.iter("element") if e.get(XSI)}
    view = next(e for e in root.iter("element")
                if e.get(XSI) == "archimate:ArchimateDiagramModel" and e.get("name") == VIEW)
    knopen, connecties = {}, []

    def loop(c, ox, oy):
        b = c.find("bounds")
        x, y = ox + int(b.get("x", 0)), oy + int(b.get("y", 0))
        w, h = int(b.get("width", 120)), int(b.get("height", 55))
        knopen[c.get("id")] = dict(x=x, y=y, w=w, h=h, element=c.get("archimateElement"),
                                   groep=c.get(XSI, "").endswith("Group"))
        for sc in c.findall("sourceConnection"):
            bps = [(int(bp.get("startX", 0)), int(bp.get("startY", 0)), int(bp.get("endX", 0)), int(bp.get("endY", 0)))
                   for bp in sc.findall("bendpoint")]
            connecties.append(dict(bron=c.get("id"), doel=sc.get("target"),
                                   relatie=sc.get("archimateRelationship"), knikpunten=bps))
        for k in c.findall("child"):
            loop(k, x, y)

    for c in view.findall("child"):
        loop(c, 0, 0)
    return knopen, connecties, elems


def connectie_voor(connecties, knopen, elems, pijl, van, naar):
    """De getekende lijn van deze relatie op de view.

    Een relatie kan twee keer op de plaat staan, als een component er twee keer op staat.
    Dan telt de lijn tussen de vakken die de stroom bedoelt.
    """
    def naam(knoop_id):
        return norm(elems.get(knopen[knoop_id].get("element", ""), ("", ""))[1])

    def afstand(c):
        a, b = knopen[c["bron"]], knopen[c["doel"]]
        return ((a["x"] + a["w"] / 2 - b["x"] - b["w"] / 2) ** 2 + (a["y"] + a["h"] / 2 - b["y"] - b["h"] / 2) ** 2)

    lijnen = [c for c in connecties if c.get("relatie") == pijl]
    passend = [c for c in lijnen if naam(c["bron"]) == van and naam(c["doel"]) == naar]
    # staat de relatie meer dan een keer op de plaat, dan de kortste lijn: die houdt de markeringen bij elkaar
    return min(passend or lijnen, key=afstand) if (passend or lijnen) else None


def is_knooppunt(knoop, elems):
    """Een junction op de plaat: een punt waar een relatie zich splitst of samenkomt."""
    return elems.get(knoop.get("element", ""), ("", ""))[0].endswith("Junction")


def vervolglijnen(connecties, knopen, elems, conn, naar, gezien=()):
    """De lijnen voorbij een junction, tot het vak van de ontvanger.

    Een relatie die over een junction loopt is op de plaat in stukken getekend. Zonder
    dit vervolg stopt de markering op het punt en lijkt de lijn halverwege te eindigen.
    """
    if not is_knooppunt(knopen[conn["doel"]], elems):
        return []
    for c in connecties:
        if c["bron"] != conn["doel"] or c["relatie"] in gezien:
            continue
        if norm(elems.get(knopen[c["doel"]].get("element", ""), ("", ""))[1]) == naar:
            return [c]
        verder = vervolglijnen(connecties, knopen, elems, c, naar, gezien + (c["relatie"],))
        if verder:
            return [c] + verder
    return []


def k_vak(k, minx, miny):
    """Een element als bezet vlak, zodat een markeringslabel er niet bovenop landt."""
    return (k["x"] - minx, k["y"] - miny, k["w"], k["h"])


def tekst(x, y, s, kleur=ACCENT):
    breedte = 10 + 9 * len(s)
    return (f'<g><rect x="{x - breedte / 2:.0f}" y="{y - 15:.0f}" width="{breedte}" height="21" rx="4" '
            f'fill="#ffffff" stroke="{kleur}" stroke-width="2"/>'
            f'<text x="{x:.0f}" y="{y:.0f}" font-family="Segoe UI, Arial, sans-serif" font-size="15" '
            f'font-weight="bold" fill="{kleur}" text-anchor="middle">{html.escape(s)}</text></g>')


def boog(a, b, gestippeld=False):
    """Een eigen pijl tussen de randen van twee vakken, met een lichte boog zodat zij naast de plaat leest.
    De routering van Archi is niet te reproduceren, dus markeert dit script de twee vakken en de richting
    in plaats van de bestaande lijn over te tekenen."""
    ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
    cb = (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
    p1 = platen.rand(ca, cb, a)
    p2 = platen.rand(cb, ca, b)
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    lengte = max((dx * dx + dy * dy) ** 0.5, 1)
    # het controlepunt ligt loodrecht op het midden, zodat de boog los van de bestaande pijlen loopt
    cx, cy = mx - dy / lengte * min(lengte * 0.12, 60), my + dx / lengte * min(lengte * 0.12, 60)
    return p1, p2, (cx, cy)


def bouw(knopen, connecties, elems, png, stromen, pijl_van, uitsnede=False):
    minx = min(k["x"] for k in knopen.values()) - MARGE
    miny = min(k["y"] for k in knopen.values()) - MARGE
    W = max(k["x"] + k["w"] for k in knopen.values()) + MARGE - minx
    H = max(k["y"] + k["h"] for k in knopen.values()) + MARGE - miny
    b64 = base64.b64encode(png.read_bytes()).decode()
    soort = png.suffix.lstrip(".").replace("jpg", "jpeg")
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
             f'<defs><marker id="punt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
             f'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{ACCENT}"/></marker></defs>',
             f'<image href="data:image/{soort};base64,{b64}" x="0" y="0" width="{W}" height="{H}"/>',
             # de plaat vervaagt, zodat de markeringen eruit springen
             f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff" fill-opacity="0.6"/>']
    geraakt, ontbreekt, labels, bezet = [], [], [], [k_vak(k, minx, miny) for k in knopen.values() if not k.get("groep")]
    for (van, naar, pijl), beelden in stromen.items():
        label = ", ".join(beelden)
        conn = connectie_voor(connecties, knopen, elems, pijl, van, naar) if pijl != GEEN_PIJL else None
        if conn:
            # over de bestaande pijl heen: hetzelfde pad dat Archi tekent, met een witte onderlaag eronder
            lijnen = [conn] + vervolglijnen(connecties, knopen, elems, conn, naar)
            punten = [(x - minx, y - miny) for c in lijnen for x, y in platen.pad(c, knopen)]
            d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in punten)
            streep = ""
            geraakt += [knopen[conn["bron"]], knopen[lijnen[-1]["doel"]]]
        else:
            a, b = dichtste_paar(knopen, elems, van, naar)
            if not a or not b:
                ontbreekt.append(f"{label}: {van} naar {naar}")
                continue
            # geen lijn om over te trekken: een eigen boog die zichtbaar los van de plaat loopt
            p1, p2, c = boog(a, b)
            punten = [(p1[0] - minx, p1[1] - miny), (c[0] - minx, c[1] - miny), (p2[0] - minx, p2[1] - miny)]
            d = (f'M{punten[0][0]:.0f},{punten[0][1]:.0f} Q{punten[1][0]:.0f},{punten[1][1]:.0f} '
                 f'{punten[2][0]:.0f},{punten[2][1]:.0f}')
            streep = ' stroke-dasharray="12 9"'
            label += " (geen pijl)" if pijl == GEEN_PIJL else ""
            geraakt += [a, b]
        delen.append(f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="11" stroke-opacity="0.85"/>')
        delen.append(f'<path d="{d}" fill="none" stroke="{ACCENT}" stroke-width="5"{streep} '
                     f'marker-end="url(#punt)"/>')
        mx, my, vak = platen.plaats(punten, label, bezet)
        bezet.append(vak)
        labels.append(tekst(mx, my + 6, label))
    for k in geraakt:
        delen.append(f'<rect x="{k["x"]-minx-3:.0f}" y="{k["y"]-miny-3:.0f}" width="{k["w"]+6}" '
                     f'height="{k["h"]+6}" fill="none" stroke="{RAND}" stroke-width="4" rx="4"/>')
    delen += labels   # de namen van de stromen bovenop, zodat zij leesbaar blijven
    delen.append("</svg>")
    if uitsnede and geraakt:
        # op een slide leest de hele plaat niet; snijd uit rond de gemarkeerde vakken, met lucht voor de bogen
        bx, by, bw, bh = venster(geraakt, minx, miny, W, H, buren=knopen.values())
        delen[0] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{bx} {by} {bw} {bh}" '
                    f'width="{bw}" height="{bh}">')
    return "".join(delen), ontbreekt


def venster(geraakt, minx, miny, W, H, lucht=90, buren=()):
    """Het deel van de plaat waar de markeringen liggen, met lucht eromheen, binnen de plaat.

    Vakken die de rand van dat deel raken worden er helemaal in getrokken: een half
    afgesneden vak met een half woord erin leest als een fout, niet als een uitsnede.
    Grote vakken blijven buiten die verruiming, want dat zijn de groeperingen.
    """
    x1 = min(k["x"] for k in geraakt) - minx - lucht
    y1 = min(k["y"] for k in geraakt) - miny - lucht
    x2 = max(k["x"] + k["w"] for k in geraakt) - minx + lucht
    y2 = max(k["y"] + k["h"] for k in geraakt) - miny + lucht
    ox1, oy1, ox2, oy2 = x1, y1, x2, y2   # toetsen tegen het oorspronkelijke venster, anders groeit het door
    for k in buren:
        if k.get("groep") or k["w"] > W * 0.4 or k["h"] > H * 0.4:
            continue
        kx1, ky1 = k["x"] - minx, k["y"] - miny
        kx2, ky2 = kx1 + k["w"], ky1 + k["h"]
        if kx2 > ox1 and kx1 < ox2 and ky2 > oy1 and ky1 < oy2:
            x1, y1, x2, y2 = min(x1, kx1 - 8), min(y1, ky1 - 8), max(x2, kx2 + 8), max(y2, ky2 + 8)
    x1, y1 = max(0, round(x1)), max(0, round(y1))
    return x1, y1, min(round(x2), W) - x1, min(round(y2), H) - y1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--stromen", type=pathlib.Path, default=STROMEN)
    parser.add_argument("--plaat", type=pathlib.Path, default=PLAAT, help="render van de hoofdplaat (png of jpg)")
    parser.add_argument("--uit", type=pathlib.Path, default=UITMAP)
    parser.add_argument("--koppelingen", help="komma-gescheiden koppelingen; markeert die op een plaat "
                                              "in plaats van een plaat per fase")
    parser.add_argument("--uitsnede", action="store_true", help="snijd uit rond de gemarkeerde vakken")
    args = parser.parse_args(argv)
    if not args.plaat.exists():
        sys.exit(f"plaat niet gevonden: {args.plaat}; render hem met exporteer-archimate-platen.py")
    regels = json.loads(args.regels.read_text(encoding="utf-8"))
    stromen_json = json.loads(args.stromen.read_text(encoding="utf-8"))
    pijl_van = {s["id"]: s for s in stromen_json.get("stromen", [])}
    knopen, connecties, elems = lees_geometrie(args.model)
    args.uit.mkdir(parents=True, exist_ok=True)
    if args.koppelingen:
        namen = [n.strip() for n in args.koppelingen.split(",") if n.strip()]
        stromen = stromen_per_koppeling(regels, namen)
        if not stromen:
            sys.exit(f"geen stromen gevonden voor {', '.join(namen)}")
        svg, ontbreekt = bouw(knopen, connecties, elems, args.plaat, stromen, pijl_van, args.uitsnede)
        doel = args.uit / "koppelingen.svg"
        doel.write_text(svg, encoding="utf-8")
        for x in ontbreekt:
            print(f"waarschuwing: niet op de plaat te plaatsen: {x}", file=sys.stderr)
        print(f"koppelingenplaat geschreven naar {doel}")
        return 0
    aantal = 0
    for fase, stromen in stromen_per_fase(regels).items():
        svg, ontbreekt = bouw(knopen, connecties, elems, args.plaat, stromen, pijl_van)
        (args.uit / f"f{fase}.svg").write_text(svg, encoding="utf-8")
        aantal += 1
        for x in ontbreekt:
            print(f"waarschuwing: fase {fase}, niet op de plaat te plaatsen: {x}", file=sys.stderr)
    print(f"{aantal} faseplaten geschreven naar {args.uit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
