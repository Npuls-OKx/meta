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


def pad(conn, knopen):
    """Het pad zoals Archi het tekent: een knikpunt ligt op het midden van de bron plus zijn eigen offset.
    De end-offsets zijn dezelfde punten gerekend vanaf het doel; het gemiddelde van beide nemen verschuift
    de lijn, wat bij brede vakken zichtbaar naast de pijl uitkomt."""
    a, b = knopen[conn["bron"]], knopen[conn["doel"]]
    ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
    cb = (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
    punten = [ca] + [(ca[0] + sx, ca[1] + sy) for sx, sy, _, _ in conn["knikpunten"]] + [cb]
    punten[0] = platen.rand(ca, punten[1], a)
    punten[-1] = platen.rand(cb, punten[-2], b)
    return punten


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


def bouw(knopen, connecties, elems, png, stromen, pijl_van):
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
    geraakt, ontbreekt = [], []
    for (van, naar, pijl), beelden in stromen.items():
        label = ", ".join(beelden)
        a, b = dichtste_paar(knopen, elems, van, naar)
        if not a or not b:
            ontbreekt.append(f"{label}: {van} naar {naar}")
            continue
        p1, p2, c = boog(a, b)
        streep = ' stroke-dasharray="12 9"' if pijl == GEEN_PIJL else ""
        d = f'M{p1[0]-minx:.0f},{p1[1]-miny:.0f} Q{c[0]-minx:.0f},{c[1]-miny:.0f} {p2[0]-minx:.0f},{p2[1]-miny:.0f}'
        delen.append(f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="11" stroke-opacity="0.85"/>')
        delen.append(f'<path d="{d}" fill="none" stroke="{ACCENT}" stroke-width="5"{streep} '
                     f'marker-end="url(#punt)"/>')
        delen.append(tekst(c[0] - minx, c[1] - miny - 6, label + (" (geen pijl)" if pijl == GEEN_PIJL else "")))
        geraakt += [a, b]
    for k in geraakt:
        delen.append(f'<rect x="{k["x"]-minx-3:.0f}" y="{k["y"]-miny-3:.0f}" width="{k["w"]+6}" '
                     f'height="{k["h"]+6}" fill="none" stroke="{RAND}" stroke-width="4" rx="4"/>')
    delen.append("</svg>")
    return "".join(delen), ontbreekt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--stromen", type=pathlib.Path, default=STROMEN)
    parser.add_argument("--plaat", type=pathlib.Path, default=PLAAT, help="render van de hoofdplaat (png of jpg)")
    parser.add_argument("--uit", type=pathlib.Path, default=UITMAP)
    args = parser.parse_args(argv)
    if not args.plaat.exists():
        sys.exit(f"plaat niet gevonden: {args.plaat}; render hem met exporteer-archimate-platen.py")
    regels = json.loads(args.regels.read_text(encoding="utf-8"))
    stromen_json = json.loads(args.stromen.read_text(encoding="utf-8"))
    pijl_van = {s["id"]: s for s in stromen_json.get("stromen", [])}
    knopen, connecties, elems = lees_geometrie(args.model)
    args.uit.mkdir(parents=True, exist_ok=True)
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
