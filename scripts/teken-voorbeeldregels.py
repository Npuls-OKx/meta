#!/usr/bin/env python3
"""De regels van de voorbeelduitwerking tekenen als SVG in ArchiMate-vormtaal.

Waarom dit script bestaat: het voorbeeld (de opleiding van Jochem, stap voor stap in
het informatiemodel) moet leesbaar zijn als een reeks korte, visuele regels, niet als
tekst. Elke regel uit de regeltabel wordt een zelfdragende SVG (geen externe fonts,
geen scripts), zodat hij op GitHub in markdown rendert en na een modelronde opnieuw
te maken is.

    python3 scripts/teken-voorbeeldregels.py [--regels PAD] [--uit MAP]

Drie soorten regels, in de kleuren en iconen van ArchiMate:
- ontstaat: rol (geel, rolicoon), processtap (geel, procesicoon), de objecttypen van
  de plaat (geel, business-objecticoon) met de instantie voor Jochem; "bestaat uit"
  als nesting; een aanname gestippeld; een scope-uitzondering grijs;
- verandert: als ontstaat, met de nieuwe toestand op het object;
- stroomt: van (blauw, componenticoon), het object op een gestippelde pijl, naar, met
  de koppeling-ID en de processtap als klein label.
"""

import argparse
import html
import json
import pathlib
import re
import sys

REGELS = pathlib.Path("architecture/model/informatiemodel/voorbeeld-lr1-regels.json")
UIT = pathlib.Path("architecture/model/informatiemodel/img/regels")
BUS, BUS_L, BUS_T = "#ffffb5", "#a8a85a", "#5a5a2a"
APP, APP_L, APP_T = "#b5ffff", "#5aa8a8", "#2a5a5a"
GRIJS, GRIJS_L, GRIJS_T = "#e8e8e8", "#9a9a9a", "#666666"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#d8ddda"
FONT = "Arial, Helvetica, sans-serif"
ICONS = {
    "object": '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>',
    "proces": '<path d="M2 5h8V2l5 6-5 6v-3H2z"/>',
    "rol": '<rect x="2" y="5" width="10" height="6" rx="3"/><ellipse cx="12" cy="8" rx="2" ry="3"/>',
    "component": '<rect x="4" y="2" width="10" height="12"/><rect x="2" y="4" width="4" height="2.5"/><rect x="2" y="8.5" width="4" height="2.5"/>',
}
SOORTEN = {"ontstaat", "verandert", "stroomt"}


def tw(s, size=13, bold=False):
    """Geschatte tekstbreedte in px voor Arial; ruim genoeg zodat tekst niet in het icoon loopt."""
    return len(s) * size * (0.66 if bold else 0.6)


def icon(kind, x, y, kleur="#444"):
    return f'<g transform="translate({x:.0f},{y:.0f})" fill="none" stroke="{kleur}" stroke-width="1.3">{ICONS[kind]}</g>'


def box(x, y, w, h, fill, line, rx=0, dashed=False, patroon="5 3"):
    """dashed met patroon "5 3" markeert een aanname; relatielabels gebruiken "2 2"."""
    d = f' stroke-dasharray="{patroon}"' if dashed else ""
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}" stroke="{line}"{d}/>'


def text(x, y, s, size=13, bold=False, fill=INK, anchor="start"):
    fw = ' font-weight="bold"' if bold else ""
    return f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{size}"{fw} fill="{fill}" text-anchor="{anchor}">{html.escape(s)}</text>'


def element(x, y, kind, label, inst, fill=BUS, line=BUS_L, labelkleur=BUS_T, rx=0, dashed=False, toestand=None):
    """Eén element: typelabel klein, instantie vet, optioneel de toestand eronder. Geeft (svg, w, h)."""
    regels = [inst] + ([f"toestand: {toestand}"] if toestand else [])
    w = max(120, max([tw(label, 11)] + [tw(r, 13, True) for r in regels]) + 42)
    h = 46 + (16 if toestand else 0)
    s = box(x, y, w, h, fill, line, rx, dashed) + icon(kind, x + w - 22, y + 5)
    s += text(x + 10, y + 17, label, 11, fill=labelkleur)
    s += text(x + 10, y + 34, inst, 13, True)
    if toestand:
        s += text(x + 10, y + 50, f"toestand: {toestand}", 12, fill=MUTED)
    return s, w, h


def objecten(x, y, items, uitzonderingen):
    """Rij van objecten en relatielabels; nesting bij kinderen. Geeft (svg, w, h)."""
    out, cx, maxh = "", x, 0
    for it in items:
        if "relatie" in it and "type" not in it:
            w = tw(it["relatie"], 11) + 18
            out += box(cx, y + 15, w, 18, "#ffffff", "#c8ccc9", 9, True, "2 2") + text(cx + w / 2, y + 27, it["relatie"], 11, fill=MUTED, anchor="middle")
            cx += w + 8
            maxh = max(maxh, 46)
            continue
        dashed = it.get("aanname", False)
        buiten = it["type"] in uitzonderingen
        fill, line, lk = (GRIJS, GRIJS_L, GRIJS_T) if buiten else (BUS, BUS_L, BUS_T)
        if it.get("kinderen"):
            ksvg, kw, kh = objecten(cx + 14, y + 40, it["kinderen"], uitzonderingen)
            w = max(kw + 24, tw(it["type"], 11) + 42, tw(it["instantie"], 13, True) + 42)
            h = 40 + kh + 10
            out += box(cx, y, w, h, fill, line, 0, dashed) + icon("object", cx + w - 22, y + 5)
            out += text(cx + 10, y + 17, it["type"], 11, fill=lk) + text(cx + 10, y + 34, it["instantie"], 13, True) + ksvg
        else:
            s, w, h = element(cx, y, "object", it["type"], it["instantie"], fill, line, lk, 0, dashed, it.get("toestand"))
            out += s
        cx += w + 8
        maxh = max(maxh, h)
    return out, cx - x - 8, maxh


def wrap(W, H, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">'
            f'<rect x="0.5" y="0.5" width="{W-1:.0f}" height="{H-1:.0f}" rx="10" fill="#ffffff" stroke="{LIJN}"/>{body}</svg>')


def regel_ontstaat(blok, uitzonderingen):
    y0 = 10
    wie, ww, wh = element(12, y0, "rol", "rol", blok["wie"], BUS, BUS_L, BUS_T, 8)
    x = 12 + ww + 10
    stap, sw, sh = element(x, y0, "proces", "processtap", blok["stap"], BUS, BUS_L, BUS_T, 8)
    x += sw + 6
    pijl = text(x, y0 + 30, "→", 18, fill=MUTED)
    x += 20
    objs, ow, oh = objecten(x, y0, blok["objecten"], uitzonderingen)
    rowh = max(wh, sh, oh)
    zin_y = y0 + rowh + 22
    W = max(x + ow + 12, tw(blok.get("zin", ""), 13) + 24)
    H = zin_y + 12
    return wrap(W, H, wie + stap + pijl + objs + text(12, zin_y, blok.get("zin", ""), 13, fill=MUTED))


def regel_stroomt(blok, uitzonderingen):
    y0 = 10
    idtekst = blok.get("koppeling") or "zonder koppelingspecificatie"
    idw = tw(idtekst, 11) + 16
    s = box(12, y0 + 14, idw, 18, "#ffffff", "#c8ccc9", 4) + text(20, y0 + 27, idtekst, 11, fill=MUTED)
    x = 12 + idw + 12
    van, vw, vh = element(x, y0, "component", "van", blok["van"], APP, APP_L, APP_T)
    x += vw + 6
    lijn = 34
    s += van + f'<path d="M{x} {y0+23}h{lijn}" stroke="{APP_T}" stroke-width="2" stroke-dasharray="5 4"/>'
    x += lijn
    o = blok["object"]
    buiten = o["type"] in uitzonderingen
    fill, line = (GRIJS, GRIJS_L) if buiten else (BUS, BUS_L)
    ow = max(tw(o["type"], 12), tw(o["instantie"], 12, True)) + 40
    s += box(x, y0 + 8, ow, 32, fill, line) + icon("object", x + ow - 20, y0 + 10)
    s += text(x + 8, y0 + 21, o["type"], 12) + text(x + 8, y0 + 34, o["instantie"], 12, True)
    x += ow
    s += f'<path d="M{x} {y0+23}h{lijn}" stroke="{APP_T}" stroke-width="2" stroke-dasharray="5 4"/>'
    s += f'<path d="M{x+lijn-2} {y0+17}l10 6-10 6z" fill="{APP_T}"/>'
    x += lijn + 10
    naar, nw, nh = element(x, y0, "component", "naar", blok["naar"], APP, APP_L, APP_T)
    x += nw + 10
    stapw = tw("na: " + blok["stap"], 11) + 16
    s += naar + box(x, y0 + 14, stapw, 18, "#ffffff", "#c8ccc9", 9, True, "2 2") + text(x + 8, y0 + 27, "na: " + blok["stap"], 11, fill=MUTED)
    x += stapw + 12
    zin_y = y0 + 46 + 22
    W = max(x, tw(blok.get("zin", ""), 13) + 24)
    H = zin_y + 12
    body = f'<rect x="0" y="0" width="4" height="{H:.0f}" fill="{APP_L}"/>' + s + text(12, zin_y, blok.get("zin", ""), 13, fill=MUTED)
    return wrap(W, H, body)


def groepeer(regels):
    """Regels met dezelfde fase en stap en soort worden één blok; ontstaat en verandert samen."""
    blokken = []
    for r in regels["regels"]:
        soort = r["soort"]
        if soort == "stroomt":
            blokken.append({"soort": "stroomt", "fase": r["fase"], "stap": r["stap"], "van": r["van"], "naar": r["naar"],
                            "koppeling": r.get("koppeling"), "object": {"type": r["objecttype"], "instantie": r["instantie"]},
                            "zin": r.get("zin", "")})
            continue
        laatste = blokken[-1] if blokken else None
        if not laatste or laatste["soort"] != "ontstaat" or (laatste["fase"], laatste["stap"], laatste["wie"]) != (r["fase"], r["stap"], r.get("wie")):
            laatste = {"soort": "ontstaat", "fase": r["fase"], "stap": r["stap"], "wie": r.get("wie"), "objecten": [], "zin": r.get("zin", "")}
            blokken.append(laatste)
        item = {"type": r["objecttype"], "instantie": r["instantie"], "aanname": r.get("aanname", False)}
        if soort == "verandert":
            item["toestand"] = r.get("toestand")
        rel = r.get("relatie")
        if rel and rel.get("nesting"):
            ouder = next((it for it in laatste["objecten"] if it.get("type") == rel["van"]), None)
            if ouder is not None:
                ouder.setdefault("kinderen", []).append(item)
                continue
        elif rel and rel.get("label"):
            laatste["objecten"].append({"relatie": rel["label"]})
        laatste["objecten"].append(item)
        if r.get("zin") and not laatste["zin"]:
            laatste["zin"] = r["zin"]
    return blokken


def bestandsnaam(blok, volgnummer):
    slug = re.sub(r"[^a-z0-9]+", "-", blok["stap"].lower()).strip("-")
    return f"f{blok['fase']}-{volgnummer:02d}-{slug}.svg"


def teken(regels, uitmap):
    """Schrijft per blok een SVG; geeft de lijst (bestandsnaam, blok)."""
    uitzonderingen = {u["objecttype"] for u in regels.get("scope_uitzonderingen", [])}
    uitmap = pathlib.Path(uitmap)
    uitmap.mkdir(parents=True, exist_ok=True)
    uit = []
    for n, blok in enumerate(groepeer(regels), 1):
        if blok["soort"] == "stroomt":
            svg = regel_stroomt(blok, uitzonderingen)
        else:
            svg = regel_ontstaat(blok, uitzonderingen)
        naam = bestandsnaam(blok, n)
        (uitmap / naam).write_text(svg, encoding="utf-8")
        uit.append((naam, blok))
    return uit


def valideer(regels):
    """Wat de renderer zelf nodig heeft; de inhoudelijke controle doet controleer-voorbeeldregels.py."""
    for i, r in enumerate(regels.get("regels", []), 1):
        if r.get("soort") not in SOORTEN:
            sys.exit(f"regel {i}: soort {r.get('soort')!r} is niet ontstaat, verandert of stroomt")
        if not r.get("instantie"):
            sys.exit(f"regel {i}: objecttype {r.get('objecttype')!r} heeft geen instantie")
        rel = r.get("relatie")
        if rel and "label" in rel and rel["label"] == "":
            sys.exit(f"regel {i}: relatielabel is leeg")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    args = parser.parse_args(argv)
    if not args.regels.exists():
        print(f"regeltabel niet gevonden: {args.regels}", file=sys.stderr)
        return 2
    regels = json.loads(args.regels.read_text(encoding="utf-8"))
    valideer(regels)
    uit = teken(regels, args.uit)
    print(f"{len(uit)} regels getekend naar {args.uit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
