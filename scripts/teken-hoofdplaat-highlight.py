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
VIEW = "OKx hoofdplaat v1.7<concept>"
GEEN_PIJL = "geen pijl op de hoofdplaat"
MARGE = 20
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


def knoop_van_component(knopen, elems, naam):
    """De knoop op de view die dit applicatiecomponent toont."""
    for kid, k in knopen.items():
        if norm(elems.get(k.get("element", ""), ("", ""))[1]) == naam:
            return k
    return None


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


def tekst(x, y, s, kleur=ACCENT):
    breedte = 10 + 9 * len(s)
    return (f'<g><rect x="{x - breedte / 2:.0f}" y="{y - 15:.0f}" width="{breedte}" height="21" rx="4" '
            f'fill="#ffffff" stroke="{kleur}" stroke-width="2"/>'
            f'<text x="{x:.0f}" y="{y:.0f}" font-family="Segoe UI, Arial, sans-serif" font-size="15" '
            f'font-weight="bold" fill="{kleur}" text-anchor="middle">{html.escape(s)}</text></g>')


def bouw(knopen, connecties, elems, png, stromen, pijl_van):
    minx = min(k["x"] for k in knopen.values()) - MARGE
    miny = min(k["y"] for k in knopen.values()) - MARGE
    W = max(k["x"] + k["w"] for k in knopen.values()) + MARGE - minx
    H = max(k["y"] + k["h"] for k in knopen.values()) + MARGE - miny
    b64 = base64.b64encode(png.read_bytes()).decode()
    soort = png.suffix.lstrip(".").replace("jpg", "jpeg")
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
             f'<image href="data:image/{soort};base64,{b64}" x="0" y="0" width="{W}" height="{H}"/>',
             # de plaat vervaagt, zodat de gemarkeerde stromen eruit springen
             f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff" fill-opacity="0.62"/>']
    conn_van_relatie = {c["relatie"]: c for c in connecties if c["relatie"]}
    geraakt, ontbreekt = set(), []
    for (van, naar, pijl), beelden in stromen.items():
        label = ", ".join(beelden)
        conn = conn_van_relatie.get(pijl) if pijl != GEEN_PIJL else None
        if conn and conn["bron"] in knopen and conn["doel"] in knopen:
            punten = platen.pad(conn, knopen)
            d = " ".join(("M" if i == 0 else "L") + f"{x - minx:.0f},{y - miny:.0f}" for i, (x, y) in enumerate(punten))
            delen.append(f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="13" stroke-opacity="0.9" '
                         f'stroke-linecap="round"/>')
            delen.append(f'<path d="{d}" fill="none" stroke="{ACCENT}" stroke-width="7" stroke-linecap="round"/>')
            mx, my = punten[len(punten) // 2]
            delen.append(tekst(mx - minx, my - miny - 10, label))
            geraakt |= {conn["bron"], conn["doel"]}
        else:
            a = knoop_van_component(knopen, elems, van)
            b = knoop_van_component(knopen, elems, naar)
            if not a or not b:
                ontbreekt.append(f"{label}: {van} naar {naar}")
                continue
            ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
            cb = (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
            p = platen.rand(ca, cb, a)
            q = platen.rand(cb, ca, b)
            delen.append(f'<line x1="{p[0]-minx:.0f}" y1="{p[1]-miny:.0f}" x2="{q[0]-minx:.0f}" y2="{q[1]-miny:.0f}" '
                         f'stroke="{ACCENT}" stroke-width="6" stroke-dasharray="12 9"/>')
            delen.append(tekst((p[0] + q[0]) / 2 - minx, (p[1] + q[1]) / 2 - miny - 10, label + " (geen pijl)"))
            geraakt |= {id(a), id(b)}
            for k in (a, b):
                delen.append(f'<rect x="{k["x"]-minx-3:.0f}" y="{k["y"]-miny-3:.0f}" width="{k["w"]+6}" '
                             f'height="{k["h"]+6}" fill="none" stroke="{RAND}" stroke-width="4" rx="4"/>')
    for kid in geraakt:
        k = knopen.get(kid)
        if k:
            delen.append(f'<rect x="{k["x"]-minx-3:.0f}" y="{k["y"]-miny-3:.0f}" width="{k["w"]+6}" '
                         f'height="{k["h"]+6}" fill="none" stroke="{RAND}" stroke-width="4" rx="4"/>')
    delen.append("</svg>")
    return "".join(delen), ontbreekt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--stromen", type=pathlib.Path, default=STROMEN)
    parser.add_argument("--plaat", type=pathlib.Path, required=True, help="render van de hoofdplaat (png of jpg)")
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
