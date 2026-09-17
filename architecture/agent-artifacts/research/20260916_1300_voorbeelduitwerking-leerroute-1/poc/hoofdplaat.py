#!/usr/bin/env python3
"""PoC: rendert een ArchiMate-view uit model.archimate (alleen lezen) als SVG,
met de posities en knikpunten uit Archi en de relatienaam als label op de pijl."""
import sys, html, math, json
import xml.etree.ElementTree as ET

XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
FONT = "Arial, Helvetica, sans-serif"
FILL = {"ApplicationComponent": "#b5ffff", "ApplicationService": "#b5ffff", "ApplicationInterface": "#b5ffff",
        "BusinessActor": "#ffffb5", "BusinessRole": "#ffffb5", "BusinessProcess": "#ffffb5", "BusinessObject": "#ffffb5", "BusinessEvent": "#ffffb5",
        "DataObject": "#b5ffff", "Node": "#c9e7b7", "Grouping": "none", "Group": "none", "Note": "#ffffff"}
LINE = {"#b5ffff": "#5aa8a8", "#ffffb5": "#a8a85a", "#c9e7b7": "#7aa86a", "none": "#888", "#ffffff": "#888"}
ICON = {"ApplicationComponent": '<rect x="4" y="2" width="10" height="12"/><rect x="2" y="4" width="4" height="2.5"/><rect x="2" y="8.5" width="4" height="2.5"/>',
        "ApplicationService": '<rect x="2" y="5" width="12" height="6" rx="3"/>',
        "BusinessActor": '<circle cx="8" cy="3.5" r="2"/><path d="M8 5.5v5M4 8h8M8 10.5l-3 4M8 10.5l3 4"/>',
        "BusinessProcess": '<path d="M2 5h8V2l5 6-5 6v-3H2z"/>',
        "BusinessObject": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>',
        "DataObject": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>',
        "BusinessEvent": '<path d="M2 4h9l3 4-3 4H2l2-4z"/>'}

def parse(path):
    root = ET.parse(path).getroot()
    elems, rels = {}, {}
    for e in root.iter("element"):
        t = e.get(XSI)
        if not t: continue
        t = t.split(":")[1]
        if t.endswith("Relationship"):
            rels[e.get("id")] = dict(type=t.replace("Relationship", ""), source=e.get("source"), target=e.get("target"), name=e.get("name"))
        elif t != "ArchimateDiagramModel":
            elems[e.get("id")] = dict(type=t, name=e.get("name") or "")
    views = {e.get("name"): e for e in root.iter("element") if e.get(XSI) == "archimate:ArchimateDiagramModel"}
    return elems, rels, views

def wrap_text(s, width, size=12):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) * size * 0.53 > width - 28 and cur: lines.append(cur); cur = w
        else: cur = t
    if cur: lines.append(cur)
    return lines

def clip(p, q, r):
    """Punt op de rand van rechthoek r=(x,y,w,h) op de lijn van p (binnen) naar q (buiten)."""
    x, y, w, h = r; cx, cy = p; dx, dy = q[0] - cx, q[1] - cy
    if dx == dy == 0: return p
    ts = []
    if dx: ts += [(x - cx) / dx, (x + w - cx) / dx]
    if dy: ts += [(y - cy) / dy, (y + h - cy) / dy]
    ts = [t for t in ts if t > 0]
    t = min(ts) if ts else 0
    return (cx + dx * t, cy + dy * t)

def render(path, viewname, out, labels=None):
    elems, rels, views = parse(path)
    v = views[viewname]
    nodes, conns = {}, []
    def walk(child, ox, oy, depth):
        b = child.find("bounds"); x = ox + int(b.get("x", 0)); y = oy + int(b.get("y", 0))
        w = int(b.get("width", 120)); h = int(b.get("height", 55))
        eid = child.get("archimateElement"); t = child.get(XSI, "").split(":")[-1]
        el = elems.get(eid, {"type": t, "name": child.get("name") or ""})
        nodes[child.get("id")] = dict(x=x, y=y, w=w, h=h, type=el["type"], name=el["name"], fill=child.get("fillColor"), depth=depth, note=(child.find("content").text if child.find("content") is not None else None))
        for sc in child.findall("sourceConnection"):
            bps = [(int(bp.get("startX", 0)), int(bp.get("startY", 0))) for bp in sc.findall("bendpoint")]
            conns.append(dict(src=child.get("id"), tgt=sc.get("target"), rel=rels.get(sc.get("archimateRelationship")), bps=bps, name=sc.get("name")))
        for c in child.findall("child"): walk(c, x, y, depth + 1)
    for c in v.findall("child"): walk(c, 0, 0, 0)
    minx = min(n["x"] for n in nodes.values()) - 20; miny = min(n["y"] for n in nodes.values()) - 20
    maxx = max(n["x"] + n["w"] for n in nodes.values()) + 20; maxy = max(n["y"] + n["h"] for n in nodes.values()) + 20
    W, H = maxx - minx, maxy - miny
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx} {miny} {W} {H}" width="{W}" height="{H}" font-family="{FONT}">',
         '<defs><marker id="flow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 0L10 5L0 10z" fill="#333"/></marker>'
         '<marker id="open" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M0 0L10 5L0 10" fill="none" stroke="#333"/></marker>'
         '<marker id="hollow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" orient="auto"><path d="M0 0L10 5L0 10z" fill="#fff" stroke="#333"/></marker>'
         '<marker id="diamond" viewBox="0 0 12 10" refX="1" refY="5" markerWidth="12" markerHeight="10" orient="auto"><path d="M1 5L6 1L11 5L6 9z" fill="#fff" stroke="#333"/></marker>'
         '<marker id="diamondf" viewBox="0 0 12 10" refX="1" refY="5" markerWidth="12" markerHeight="10" orient="auto"><path d="M1 5L6 1L11 5L6 9z" fill="#333" stroke="#333"/></marker></defs>',
         f'<rect x="{minx}" y="{miny}" width="{W}" height="{H}" fill="#ffffff"/>']
    for nid, n in sorted(nodes.items(), key=lambda kv: kv[1]["depth"]):
        t = n["type"]; fill = n["fill"] or FILL.get(t, "#f4f4f4"); line = LINE.get(fill, "#666")
        if t == "Junction":
            s.append(f'<circle cx="{n["x"]+n["w"]/2}" cy="{n["y"]+n["h"]/2}" r="{n["w"]/2}" fill="#333"/>'); continue
        if t in ("Group", "Grouping"):
            s.append(f'<rect x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" fill="none" stroke="#888" stroke-dasharray="4 3"/>'
                     f'<text x="{n["x"]+6}" y="{n["y"]+14}" font-size="12" fill="#444">{html.escape(n["name"])}</text>'); continue
        rx = 8 if t in ("ApplicationService", "BusinessActor", "BusinessRole", "BusinessProcess") else 0
        s.append(f'<rect x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="{rx}" fill="{fill}" stroke="{line}"/>')
        if t in ICON: s.append(f'<g transform="translate({n["x"]+n["w"]-20},{n["y"]+4})" fill="none" stroke="#444" stroke-width="1.2">{ICON[t]}</g>')
        lines = wrap_text(n["note"] or n["name"] if t == "Note" else n["name"], n["w"])
        y0 = n["y"] + n["h"] / 2 - (len(lines) - 1) * 7 + 4 if t != "Note" else n["y"] + 16
        for i, ln in enumerate(lines[:6]):
            s.append(f'<text x="{n["x"]+n["w"]/2 if t!="Note" else n["x"]+6}" y="{y0+i*14}" font-size="12" text-anchor="{"middle" if t!="Note" else "start"}" fill="#1c1c1c">{html.escape(ln)}</text>')
    for c in conns:
        a, b = nodes.get(c["src"]), nodes.get(c["tgt"])
        if not a or not b: continue
        ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2); cb = (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
        pts = [ca] + [(ca[0] + bx, ca[1] + by) for bx, by in c["bps"]] + [cb]
        pts[0] = clip(ca, pts[1], (a["x"], a["y"], a["w"], a["h"])); pts[-1] = clip(cb, pts[-2], (b["x"], b["y"], b["w"], b["h"]))
        rt = (c["rel"] or {}).get("type", "Association")
        dash = ' stroke-dasharray="6 4"' if rt in ("Flow", "Realization", "Access") else ''
        end = {"Flow": "flow", "Triggering": "flow", "Serving": "open", "Realization": "hollow", "Specialization": "hollow", "Access": "open"}.get(rt)
        start = {"Composition": "diamondf", "Aggregation": "diamond"}.get(rt)
        attrs = (f' marker-end="url(#{end})"' if end else '') + (f' marker-start="url(#{start})"' if start else '')
        d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
        s.append(f'<path d="{d}" fill="none" stroke="#333" stroke-width="1.4"{dash}{attrs}/>')
        label = (labels or {}).get(f'{a["name"]}>{b["name"]}') or c["name"] or (c["rel"] or {}).get("name")
        if label:
            m = pts[len(pts) // 2 - 1], pts[len(pts) // 2]; mx, my = (m[0][0] + m[1][0]) / 2, (m[0][1] + m[1][1]) / 2
            w = len(label) * 6.4 + 12
            s.append(f'<rect x="{mx-w/2:.0f}" y="{my-10:.0f}" width="{w:.0f}" height="18" fill="#ffffb5" stroke="#a8a85a"/>'
                     f'<text x="{mx:.0f}" y="{my+3:.0f}" font-size="11" text-anchor="middle" fill="#1c1c1c">{html.escape(label)}</text>')
    s.append("</svg>")
    open(out, "w").write("".join(s))
    return len(nodes), len(conns), W, H

if __name__ == "__main__":
    labels = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else None
    print(render(sys.argv[1], sys.argv[2], sys.argv[3], labels))
