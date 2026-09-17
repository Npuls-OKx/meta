#!/usr/bin/env python3
"""PoC: tekent een 'ontstaat'- of 'stroomt'-regel als SVG in ArchiMate-vormtaal.
Invoer: JSON (zie onderaan). Uitvoer: SVG zonder externe fonts, dus renderbaar op GitHub."""
import json, sys, html

BUS, BUS_L = "#ffffb5", "#a8a85a"
APP, APP_L = "#b5ffff", "#5aa8a8"
GRIJS, GRIJS_L = "#e8e8e8", "#9a9a9a"
INK, MUTED = "#1c1c1c", "#5b6663"
FONT = "Arial, Helvetica, sans-serif"

def tw(s, size=13, bold=False):
    return len(s) * size * (0.66 if bold else 0.6)

ICONS = {
    "object": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>',
    "proces": '<path d="M2 5h8V2l5 6-5 6v-3H2z"/>',
    "actor": '<circle cx="8" cy="3.5" r="2"/><path d="M8 5.5v5M4 8h8M8 10.5l-3 4M8 10.5l3 4"/>',
    "rol": '<rect x="2" y="5" width="10" height="6" rx="3"/><ellipse cx="12" cy="8" rx="2" ry="3"/>',
    "component": '<rect x="4" y="2" width="10" height="12"/><rect x="2" y="4" width="4" height="2.5"/><rect x="2" y="8.5" width="4" height="2.5"/>',
}

def icon(kind, x, y):
    return f'<g transform="translate({x:.0f},{y:.0f})" fill="none" stroke="#444" stroke-width="1.3">{ICONS[kind]}</g>'

def box(x, y, w, h, fill, line, rx=0, dashed=False):
    d = ' stroke-dasharray="5 3"' if dashed else ''
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}" stroke="{line}"{d}/>'

def text(x, y, s, size=13, bold=False, fill=INK, anchor="start"):
    fw = ' font-weight="bold"' if bold else ''
    return f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{size}"{fw} fill="{fill}" text-anchor="{anchor}">{html.escape(s)}</text>'

def element(x, y, kind, label, inst, fill=BUS, line=BUS_L, rx=0, dashed=False):
    """Eén element: typelabel klein, instantie vet. Geeft (svg, breedte, hoogte)."""
    w = max(120, max(tw(label, 11), tw(inst, 13, True)) + 42)
    h = 46
    s = box(x, y, w, h, fill, line, rx, dashed) + icon(kind, x + w - 22, y + 5)
    s += text(x + 10, y + 17, label, 11, fill="#5a5a2a" if fill == BUS else "#2a5a5a")
    s += text(x + 10, y + 34, inst, 13, True)
    return s, w, h

def objecten(x, y, items):
    """Rij van objecten, relatielabels en geneste containers. Geeft (svg, breedte, hoogte)."""
    out, cx, maxh = "", x, 0
    for it in items:
        if "relatie" in it:
            w = tw(it["relatie"], 11) + 18
            out += box(cx, y + 15, w, 18, "#ffffff", "#c8ccc9", 9, True) + text(cx + w / 2, y + 27, it["relatie"], 11, fill=MUTED, anchor="middle")
            cx += w + 8; maxh = max(maxh, 46); continue
        dashed = it.get("aanname", False)
        if it.get("kinderen"):
            ksvg, kw, kh = objecten(cx + 14, y + 40, it["kinderen"])
            w = max(kw + 24, tw(it["type"], 11) + 42, tw(it["instantie"], 13, True) + 42)
            h = 40 + kh + 10
            out += box(cx, y, w, h, BUS, BUS_L, 0, dashed) + icon("object", cx + w - 22, y + 5)
            out += text(cx + 10, y + 17, it["type"], 11, fill="#5a5a2a") + text(cx + 10, y + 34, it["instantie"], 13, True) + ksvg
        else:
            fill, line = (GRIJS, GRIJS_L) if it.get("buiten") else (BUS, BUS_L)
            s, w, h = element(cx, y, "object", it["type"], it["instantie"], fill, line, 0, dashed)
            out += s
        cx += w + 8; maxh = max(maxh, h)
    return out, cx - x - 8, maxh

def regel_ontstaat(b):
    y0 = 10
    wie, ww, wh = element(12, y0, b["wie"]["type"], b["wie"]["type"], b["wie"]["naam"], BUS, BUS_L, 8)
    x = 12 + ww + 10
    stap, sw, sh = element(x, y0, "proces", "processtap", b["stap"], BUS, BUS_L, 8)
    x += sw + 6
    pijl = text(x, y0 + 30, "→", 18, fill=MUTED); x += 20
    objs, ow, oh = objecten(x, y0, b["objecten"])
    rowh = max(wh, sh, oh)
    zin_y = y0 + rowh + 22
    W = max(x + ow + 12, tw(b.get("zin", ""), 13) + 24)
    H = zin_y + 12
    body = wie + stap + pijl + objs + text(12, zin_y, b.get("zin", ""), 13, fill=MUTED)
    return wrap(W, H, body)

def regel_stroomt(b):
    y0 = 10
    idw = tw(b["id"], 11) + 16
    s = box(12, y0 + 14, idw, 18, "#ffffff", "#c8ccc9", 4) + text(20, y0 + 27, b["id"], 11, fill=MUTED)
    x = 12 + idw + 12
    van, vw, vh = element(x, y0, "component", "bezitter", b["van"], APP, APP_L); x += vw + 6
    lijn = 34
    s += van + f'<path d="M{x} {y0+23}h{lijn}" stroke="#2a5a5a" stroke-width="2" stroke-dasharray="5 4"/>'; x += lijn
    o = b["object"]; ow = max(tw(o["type"], 12), tw(o["instantie"], 12, True)) + 40
    s += box(x, y0 + 8, ow, 32, BUS, BUS_L) + icon("object", x + ow - 20, y0 + 10)
    s += text(x + 8, y0 + 21, o["type"], 12) + text(x + 8, y0 + 34, o["instantie"], 12, True); x += ow
    s += f'<path d="M{x} {y0+23}h{lijn}" stroke="#2a5a5a" stroke-width="2" stroke-dasharray="5 4"/>'
    s += f'<path d="M{x+lijn-2} {y0+17}l10 6-10 6z" fill="#2a5a5a"/>'; x += lijn + 10
    naar, nw, nh = element(x, y0, "component", "afnemer", b["naar"], APP, APP_L); x += nw + 12
    zin_y = y0 + 46 + 22
    W = max(x, tw(b.get("zin", ""), 13) + 24); H = zin_y + 12
    body = f'<rect x="0" y="0" width="4" height="{H}" fill="{APP_L}"/>' + s + naar + text(12, zin_y, b.get("zin", ""), 13, fill=MUTED)
    return wrap(W, H, body)

def wrap(W, H, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">'
            f'<rect x="0.5" y="0.5" width="{W-1:.0f}" height="{H-1:.0f}" rx="10" fill="#ffffff" stroke="#d8ddda"/>{body}</svg>')

if __name__ == "__main__":
    blok = json.load(open(sys.argv[1]))
    svg = regel_ontstaat(blok) if blok["soort"] == "ontstaat" else regel_stroomt(blok)
    open(sys.argv[2], "w").write(svg); print("geschreven", sys.argv[2])
