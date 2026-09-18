#!/usr/bin/env python3
"""Platen uit het ArchiMate-model exporteren met Archi headless.

Waarom dit script bestaat: een plaat die met de hand uit Archi is geexporteerd
raakt stilletjes achter op het model. Archi kan headless draaien en rendert via
het HTML-rapport elke view als PNG, pixelgelijk aan wat de modelleur in Archi
ziet. Dit script roept Archi aan op een kopie van het model (het bestand in de
repository blijft byte-gelijk), haalt de PNG's van de gevraagde views uit het
rapport en zet ze op de gevraagde paden. Optioneel legt het per view een laag
met informatieobjecten over de plaat: per flow (relatie-id uit Archi) een
objectvak op het langste segment van de pijl, als SVG met de PNG ingebed.

    python3 scripts/exporteer-archimate-platen.py --view "OKx hoofdplaat v1.7<concept>" --uit pad.png
    python3 scripts/exporteer-archimate-platen.py --view NAAM --uit pad.svg --objecten objecten.json

Met --objecten worden de pijlteksten (labelexpressies) op de kopie weggelaten, zodat
alleen de informatieobjecten op de pijlen staan; --ruimte N schuift de elementen
op de kopie N procent uit elkaar zodat de objectvakken niet over de elementen vallen.
Beide bewerkingen raken alleen de kopie; het model in de repository blijft gelijk.

Vereist Archi in de dev-container (Dockerfile: /opt/Archi, commando `archi`).
Het model wordt alleen gelezen, nooit geschreven.
"""

import argparse
import base64
import html
import json
import math
import pathlib
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
# Zonder deze registratie schrijft ElementTree ns0: in plaats van archimate: en laadt Archi de kopie niet.
ET.register_namespace("archimate", "http://www.archimatetool.com/archimate")
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
MODEL = pathlib.Path("architecture/model/model.archimate")
ARCHI = shutil.which("archi") or "/opt/Archi/Archi"
MARGE = 10  # Archi exporteert een view met 10 px rondom de elementen
HOUDERS = {"ApplicationComponent", "BusinessActor", "BusinessRole", "Grouping", "Group", "Node"}


def views_in(model):
    root = ET.parse(model).getroot()
    return {e.get("name"): e.get("id") for e in root.iter("element") if e.get(XSI) == "archimate:ArchimateDiagramModel"}


def orthogonaliseer(view, middens, dozen, ouder_van):
    """Vervangt elk schuin segment van een flow door een rechte hoek. Per schuin segment twee
    kandidaten (eerst horizontaal dan verticaal, of andersom); gekozen wordt de kandidaat waarvan
    het hoekpunt buiten alle elementen ligt, en bij gelijke stand de kandidaat die de richting van
    het vorige segment voortzet, zodat buurpijlen evenwijdig lopen."""
    def binnen(punt, eigen):
        return any(d["x"] < punt[0] < d["x"] + d["w"] and d["y"] < punt[1] < d["y"] + d["h"] for k, d in dozen.items() if k not in eigen)

    for conn in view.iter("sourceConnection"):
        bron_id, doel_id = ouder_van.get(conn.get("id")), conn.get("target")
        if bron_id not in middens or doel_id not in middens:
            continue
        ca, cb = middens[bron_id], middens[doel_id]
        oud = [(ca[0] + int(bp.get("startX", 0)), ca[1] + int(bp.get("startY", 0))) for bp in conn.findall("bendpoint")]
        punten = [ca] + oud + [cb]
        nieuw = []
        vorige_richting = None
        for i in range(len(punten) - 1):
            (x1, y1), (x2, y2) = punten[i], punten[i + 1]
            dx, dy = abs(x2 - x1), abs(y2 - y1)
            schuin = dx > 6 and dy > 6
            if schuin:
                kandidaten = [((x2, y1), "h"), ((x1, y2), "v")]
                if vorige_richting == "v":
                    kandidaten.reverse()
                gekozen = next((k for k, r in kandidaten if not binnen(k, {bron_id, doel_id})), kandidaten[0][0])
                nieuw.append(gekozen)
                vorige_richting = "v" if gekozen[0] == x2 else "h"
            else:
                vorige_richting = "h" if dx > dy else "v"
            if i + 1 < len(punten) - 1:
                nieuw.append(punten[i + 1])
        for bp in list(conn.findall("bendpoint")):
            conn.remove(bp)
        for px, py in nieuw:
            bp = ET.SubElement(conn, "bendpoint")
            bp.set("startX", str(round(px - ca[0]))); bp.set("startY", str(round(py - ca[1])))
            bp.set("endX", str(round(px - cb[0]))); bp.set("endY", str(round(py - cb[1])))


def bewerkte_kopie(model, kopie, viewnaam, zonder_pijltekst=False, ruimte=0, orthogonaal=False):
    """Schrijft een kopie van het model waarin, alleen voor de gegeven view, de pijlteksten zijn
    weggelaten en de elementen uit elkaar zijn geschoven. Geeft de schaalfactor terug."""
    boom = ET.parse(model)
    root = boom.getroot()
    view = next(e for e in root.iter("element") if e.get(XSI) == "archimate:ArchimateDiagramModel" and e.get("name") == viewnaam)
    factor = 1 + ruimte / 100
    if zonder_pijltekst:
        for conn in view.iter("sourceConnection"):
            for feature in list(conn.findall("feature")):
                if feature.get("name") == "labelExpression":
                    conn.remove(feature)
    if ruimte:
        # Eerst de absolute middens van alle diagramobjecten, voor en na het schuiven.
        def middens(knoop, ox, oy, uit):
            b = knoop.find("bounds")
            x, y = ox + int(b.get("x", 0)), oy + int(b.get("y", 0))
            uit[knoop.get("id")] = (x + int(b.get("width", 0)) / 2, y + int(b.get("height", 0)) / 2)
            for kind in knoop.findall("child"):
                middens(kind, x, y, uit)
        voor = {}
        for kind in view.findall("child"):
            middens(kind, 0, 0, voor)
        # Een knikpunt is in Archi een punt, opgeslagen als offset ten opzichte van bron en van doel
        # (beide wijzen naar hetzelfde punt). Bewaar het absolute punt voordat er iets schuift.
        knikken = {}
        for conn in view.iter("sourceConnection"):
            knikken[conn.get("id")] = [(int(bp.get("startX", 0)), int(bp.get("startY", 0))) for bp in conn.findall("bendpoint")]
        ouder_van = {}
        for knoop in view.iter("child"):
            for conn in knoop.findall("sourceConnection"):
                ouder_van[conn.get("id")] = knoop.get("id")
        # De bovenste laag en de groepen schuiven uit elkaar; elementen binnen een groep of component
        # bewegen mee met hun ouder en houden hun maat. Een groep groeit mee zodat zijn kinderen erin blijven.
        def schaal(knoop, groep_of_top):
            b = knoop.find("bounds")
            if groep_of_top:
                b.set("x", str(round(int(b.get("x", 0)) * factor)))
                b.set("y", str(round(int(b.get("y", 0)) * factor)))
            is_groep = knoop.get(XSI, "").endswith("Group")
            if is_groep:
                b.set("width", str(round(int(b.get("width", 0)) * factor)))
                b.set("height", str(round(int(b.get("height", 0)) * factor)))
            for kind in knoop.findall("child"):
                schaal(kind, is_groep)
        for kind in view.findall("child"):
            schaal(kind, True)
        na = {}
        for kind in view.findall("child"):
            middens(kind, 0, 0, na)
        # Elk knikpunt: absoluut punt schalen zoals de posities, en opnieuw als offset opslaan.
        for conn in view.iter("sourceConnection"):
            bron_id, doel_id = ouder_van.get(conn.get("id")), conn.get("target")
            if bron_id not in voor or doel_id not in voor:
                continue
            for bp, (sx, sy) in zip(conn.findall("bendpoint"), knikken[conn.get("id")]):
                px, py = voor[bron_id][0] + sx, voor[bron_id][1] + sy
                nx, ny = px * factor, py * factor
                bp.set("startX", str(round(nx - na[bron_id][0]))); bp.set("startY", str(round(ny - na[bron_id][1])))
                bp.set("endX", str(round(nx - na[doel_id][0]))); bp.set("endY", str(round(ny - na[doel_id][1])))
    if orthogonaal:
        def verzamel(knoop, ox, oy, mid, doos):
            b = knoop.find("bounds")
            x, y = ox + int(b.get("x", 0)), oy + int(b.get("y", 0))
            w, h = int(b.get("width", 0)), int(b.get("height", 0))
            mid[knoop.get("id")] = (x + w / 2, y + h / 2)
            if not knoop.get(XSI, "").endswith("Group"):
                doos[knoop.get("id")] = dict(x=x, y=y, w=w, h=h)
            for kind in knoop.findall("child"):
                verzamel(kind, x, y, mid, doos)
        mid, doos = {}, {}
        for kind in view.findall("child"):
            verzamel(kind, 0, 0, mid, doos)
        ouders = {}
        for knoop in view.iter("child"):
            for conn in knoop.findall("sourceConnection"):
                ouders[conn.get("id")] = knoop.get("id")
        orthogonaliseer(view, mid, doos, ouders)
    boom.write(kopie, encoding="UTF-8", xml_declaration=True)
    return factor


def render_rapport(model, werkmap, viewnaam=None, zonder_pijltekst=False, ruimte=0, orthogonaal=False):
    """Laat Archi het HTML-rapport maken op een kopie van het model; geeft de map met PNG's."""
    kopie = werkmap / "model.archimate"
    if viewnaam and (zonder_pijltekst or ruimte or orthogonaal):
        bewerkte_kopie(model, kopie, viewnaam, zonder_pijltekst, ruimte, orthogonaal)
    else:
        shutil.copy(model, kopie)
    rapport = werkmap / "rapport"
    opdracht = [ARCHI, "-application", "com.archimatetool.commandline.app", "-consoleLog", "-nosplash",
                "--loadModel", str(kopie), "--html.createReport", str(rapport)]
    try:
        uit = subprocess.run(opdracht, capture_output=True, text=True, timeout=600)
    except FileNotFoundError:
        sys.exit(f"Archi niet gevonden ({ARCHI}); zie .devcontainer/Dockerfile")
    if uit.returncode != 0 or "Report generated" not in uit.stdout + uit.stderr:
        sys.exit("Archi-rapport mislukt:\n" + (uit.stdout + uit.stderr)[-2000:])
    mappen = [m for m in rapport.iterdir() if (m / "images").is_dir()]
    if not mappen:
        sys.exit("geen images-map in het Archi-rapport")
    return mappen[0] / "images"


def lees_view(model, viewnaam):
    root = ET.parse(model).getroot()
    elems = {e.get("id"): (e.get(XSI, "").split(":")[-1], e.get("name") or "") for e in root.iter("element") if e.get(XSI)}
    rels = {e.get("id"): e for e in root.iter("element") if e.get(XSI, "").endswith("Relationship")}
    view = next(e for e in root.iter("element") if e.get(XSI) == "archimate:ArchimateDiagramModel" and e.get("name") == viewnaam)
    knopen, connecties = {}, []

    def loop(c, ox, oy):
        b = c.find("bounds")
        x, y = ox + int(b.get("x", 0)), oy + int(b.get("y", 0))
        w, h = int(b.get("width", 120)), int(b.get("height", 55))
        knopen[c.get("id")] = dict(x=x, y=y, w=w, h=h, groep=c.get(XSI, "").endswith("Group"))
        for sc in c.findall("sourceConnection"):
            bps = [(int(bp.get("startX", 0)), int(bp.get("startY", 0)), int(bp.get("endX", 0)), int(bp.get("endY", 0)))
                   for bp in sc.findall("bendpoint")]
            connecties.append(dict(bron=c.get("id"), doel=sc.get("target"), relatie=sc.get("archimateRelationship"), knikpunten=bps))
        for k in c.findall("child"):
            loop(k, x, y)

    for c in view.findall("child"):
        loop(c, 0, 0)
    return knopen, connecties, rels


def rand(p, q, r):
    """Snijpunt van de lijn p naar q met de rand van rechthoek r (p ligt binnen r)."""
    cx, cy = p
    dx, dy = q[0] - cx, q[1] - cy
    if dx == dy == 0:
        return p
    ts = []
    if dx:
        ts += [(r["x"] - cx) / dx, (r["x"] + r["w"] - cx) / dx]
    if dy:
        ts += [(r["y"] - cy) / dy, (r["y"] + r["h"] - cy) / dy]
    ts = [t for t in ts if t > 0]
    return (cx + dx * min(ts), cy + dy * min(ts)) if ts else p


def pad(conn, knopen):
    """Het pad van een connectie zoals Archi het tekent: knikpunt is het gemiddelde van bron- en doeloffset."""
    a, b = knopen[conn["bron"]], knopen[conn["doel"]]
    ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
    cb = (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
    punten = [ca] + [((ca[0] + sx + cb[0] + ex) / 2, (ca[1] + sy + cb[1] + ey) / 2) for sx, sy, ex, ey in conn["knikpunten"]] + [cb]
    punten[0] = rand(ca, punten[1], a)
    punten[-1] = rand(cb, punten[-2], b)
    return punten


def kandidaten(punten):
    """Middens van de segmenten, langste eerst; daarna de kwartpunten van het langste segment."""
    segmenten = sorted(((punten[i], punten[i + 1]) for i in range(len(punten) - 1)),
                       key=lambda s: -math.hypot(s[1][0] - s[0][0], s[1][1] - s[0][1]))
    uit = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in segmenten]
    a, b = segmenten[0]
    uit += [(a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f) for f in (0.3, 0.7, 0.2, 0.8)]
    return uit


def overlapt(vak, bezet):
    x, y, w, h = vak
    return any(x < bx + bw and bx < x + w and y < by + bh and by < y + h for bx, by, bw, bh in bezet)


def plaats(punten, naam, bezet):
    """Eerste kandidaatpositie waar het objectvak niets raakt wat al bezet is (elementen en eerdere vakken)."""
    w, h = len(naam) * 7.0 + 32, 22
    for mx, my in kandidaten(punten):
        vak = (mx - w / 2, my - h / 2, w, h)
        if not overlapt(vak, bezet):
            return mx, my, vak
    mx, my = kandidaten(punten)[0]
    return mx, my, (mx - w / 2, my - h / 2, w, h)


def objectvak(mx, my, naam):
    w, h = len(naam) * 7.0 + 32, 22
    return (f'<g><rect x="{mx-w/2:.0f}" y="{my-h/2:.0f}" width="{w:.0f}" height="{h}" fill="#ffffb5" stroke="#a8a85a"/>'
            f'<g transform="translate({mx+w/2-20:.0f},{my-h/2+3:.0f})" fill="none" stroke="#444" stroke-width="1.2">'
            f'<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/></g>'
            f'<text x="{mx-w/2+8:.0f}" y="{my+4:.0f}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#1c1c1c">{html.escape(naam)}</text></g>')


def met_objecten(model, viewnaam, png, objecten):
    """model: het (bewerkte) modelbestand waaruit de PNG is gerenderd, zodat geometrie en beeld gelijk lopen."""
    """SVG: de Archi-PNG als achtergrond met per flow (relatie-id) een objectvak. Geeft (svg, aantal, ongebruikt)."""
    knopen, connecties, rels = lees_view(model, viewnaam)
    minx = min(k["x"] for k in knopen.values()) - MARGE
    miny = min(k["y"] for k in knopen.values()) - MARGE
    W = max(k["x"] + k["w"] for k in knopen.values()) + MARGE - minx
    H = max(k["y"] + k["h"] for k in knopen.values()) + MARGE - miny
    b64 = base64.b64encode(png.read_bytes()).decode()
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
             f'<image href="data:image/png;base64,{b64}" x="0" y="0" width="{W}" height="{H}"/>']
    # bezet: alle elementen (behalve groepen, die zijn achtergrond) en de vakken die al staan
    bezet = [(k["x"], k["y"], k["w"], k["h"]) for kid, k in knopen.items() if not k.get("groep")]
    gebruikt = set()
    for conn in connecties:
        rel = rels.get(conn["relatie"])
        naam = objecten.get(conn["relatie"])
        if rel is None or not rel.get(XSI, "").endswith("FlowRelationship") or not naam:
            continue
        if conn["bron"] not in knopen or conn["doel"] not in knopen:
            continue
        mx, my, vak = plaats(pad(conn, knopen), naam, bezet)
        bezet.append(vak)
        delen.append(objectvak(mx - minx, my - miny, naam))
        gebruikt.add(conn["relatie"])
    delen.append("</svg>")
    return "".join(delen), len(gebruikt), sorted(set(objecten) - gebruikt)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--view", required=True, action="append", help="viewnaam; herhaalbaar, in volgorde van --uit")
    parser.add_argument("--uit", required=True, action="append", type=pathlib.Path, help="doelpad (.png, of .svg met --objecten)")
    parser.add_argument("--objecten", type=pathlib.Path, help="JSON {relatie-id: objecttype}; alleen voor .svg-uitvoer")
    parser.add_argument("--ruimte", type=int, default=0, help="elementen N procent uit elkaar schuiven (alleen op de kopie)")
    parser.add_argument("--orthogonaal", action="store_true", help="schuine pijlsegmenten vervangen door rechte hoeken (alleen op de kopie)")
    args = parser.parse_args(argv)
    if len(args.view) != len(args.uit):
        sys.exit("geef evenveel --view als --uit")
    if not args.model.exists():
        print(f"model niet gevonden: {args.model}", file=sys.stderr)
        return 2
    bekend = views_in(args.model)
    onbekend = [v for v in args.view if v not in bekend]
    if onbekend:
        sys.exit("view niet gevonden: " + ", ".join(onbekend) + "\nbeschikbaar:\n  " + "\n  ".join(sorted(bekend)))
    objecten = json.loads(args.objecten.read_text(encoding="utf-8")) if args.objecten else {}
    with tempfile.TemporaryDirectory() as werk:
        werkmap = pathlib.Path(werk)
        gedeeld = None  # een rapport voor alle onbewerkte views
        for viewnaam, doel in zip(args.view, args.uit):
            bewerkt = doel.suffix.lower() == ".svg" and (bool(objecten) or args.ruimte or args.orthogonaal)
            if bewerkt:
                eigen = werkmap / bekend[viewnaam]
                eigen.mkdir()
                beelden = render_rapport(args.model, eigen, viewnaam, zonder_pijltekst=bool(objecten), ruimte=args.ruimte, orthogonaal=args.orthogonaal)
                bron = eigen / "model.archimate"
            else:
                if gedeeld is None:
                    gedeeld = render_rapport(args.model, werkmap)
                beelden, bron = gedeeld, args.model
            png = beelden / f"{bekend[viewnaam]}.png"
            if not png.exists():
                sys.exit(f"Archi leverde geen beeld voor view {viewnaam}")
            doel.parent.mkdir(parents=True, exist_ok=True)
            if doel.suffix.lower() == ".svg":
                svg, aantal, ongebruikt = met_objecten(bron, viewnaam, png, objecten)
                doel.write_text(svg, encoding="utf-8")
                print(f"{doel}: {aantal} objecten op de plaat" + (f"; niet op deze view: {', '.join(ongebruikt)}" if ongebruikt else ""))
            else:
                shutil.copy(png, doel)
                print(f"{doel}: geexporteerd")
    return 0


if __name__ == "__main__":
    sys.exit(main())
