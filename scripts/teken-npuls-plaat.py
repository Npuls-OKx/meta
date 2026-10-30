#!/usr/bin/env python3
"""Een plaat tekenen in de Npuls-huisstijl, uit een selectiebestand.

Waarom dit script bestaat: de beelden in deze repository staan in ArchiMate-vormtaal. Die werkt
voor wie het model leest en is onleesbaar voor wie binnenkomt. De presentaties spreken een taal
die mensen wel kennen: het Npuls-palet met kaarten en iconen. Dit script brengt die taal naar de
documenten, zodat een lezer dezelfde vormtaal ziet als in een deck.

De selectie is het werk, het tekenen is een aanroep van een paar seconden. Een plaat hertekenen
na een wijziging kost dus niets.

    python3 scripts/teken-npuls-plaat.py --selectie img/visueel/rijpheid.json

Blokken die een selectie kan dragen:

    ladder      treden onder elkaar, oplopend, met een trede die leeg kan zijn en een
                terugloop die van een hogere trede naar een lagere wijst
    stappen     kaarten naast elkaar met een pijl ertussen
    kolommen    twee kolommen met een lijst, bijvoorbeeld in concept tegenover nog open
    kaarten     een rij kaarten met icoon, titel en een regel
    legenda     een regel met kleurvlakjes en hun betekenis
    tekst       een alinea, voor de regel onder een blok

Het palet komt uit presentaties/src/style.css, de iconen uit img/visueel/iconen.json. Beide zijn
bron: een wijziging daar raakt elke plaat. De achtergrond is altijd expliciet licht, want een SVG
met een doorzichtige achtergrond valt weg in de donkere modus van GitHub.
"""

import argparse
import json
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
STIJL = WORTEL / "presentaties/src/style.css"
ICONEN = WORTEL / "img/visueel/iconen.json"

FONT = "Inter, Segoe UI, Helvetica Neue, Arial, sans-serif"
RAND = 40          # marge rond het doek
REGELHOOGTE = 19


def palet() -> dict:
    """Het Npuls-palet uit de huisstijlbron; het staat niet in dit script."""
    css = STIJL.read_text(encoding="utf-8")
    kleuren = dict(re.findall(r"--(np-[a-z-]+):\s*(#[0-9A-Fa-f]{3,8})", css))
    if not kleuren:
        sys.exit(f"geen palet gevonden in {STIJL}")
    return kleuren


def iconen() -> dict:
    return json.loads(ICONEN.read_text(encoding="utf-8"))


def esc(t: str) -> str:
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def tw(tekst: str, grootte: float, vet: bool = False) -> float:
    """Tekstbreedte bij benadering; genoeg om te weten of iets past."""
    factor = 0.56 if vet else 0.52
    return len(tekst) * grootte * factor


def breek(tekst: str, breedte: float, grootte: float, vet: bool = False) -> list[str]:
    woorden, regels, huidig = tekst.split(), [], ""
    for w in woorden:
        kandidaat = f"{huidig} {w}".strip()
        if tw(kandidaat, grootte, vet) <= breedte or not huidig:
            huidig = kandidaat
        else:
            regels.append(huidig)
            huidig = w
    if huidig:
        regels.append(huidig)
    return regels


def tekst(x, y, t, grootte=14, kleur="#1A1A2E", vet=False, midden=False, cursief=False):
    anker = ' text-anchor="middle"' if midden else ""
    gewicht = ' font-weight="600"' if vet else ""
    stijl = ' font-style="italic"' if cursief else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{grootte}"'
            f' fill="{kleur}"{gewicht}{anker}{stijl}>{esc(t)}</text>')


def kaart(x, y, w, h, vul, rand, straal=10, streep=None, gestippeld=False):
    stip = ' stroke-dasharray="6 5"' if gestippeld else ""
    s = (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{straal}"'
         f' fill="{vul}" stroke="{rand}" stroke-width="1.5"{stip}/>')
    if streep:
        s += (f'<path d="M{x + straal:.0f} {y:.0f}H{x + w - straal:.0f}" stroke="{streep}"'
              f' stroke-width="4" stroke-linecap="round"/>')
    return s


def icoon(naam, x, y, maat, kleur, set_):
    ic = set_["iconen"].get(naam)
    if not ic:
        return ""
    bron = ic.get("width", 32)
    schaal = maat / bron
    body = re.sub(r'fill="(?!none)[^"]*"', f'fill="{kleur}"', ic["body"])
    body = re.sub(r'stroke="(?!none)[^"]*"', f'stroke="{kleur}"', body)
    if "fill=" not in body:
        body = f'<g fill="{kleur}">{body}</g>'
    return f'<g transform="translate({x:.0f} {y:.0f}) scale({schaal:.4f})">{body}</g>'


def pijl(x1, y1, x2, kleur):
    return (f'<path d="M{x1:.0f} {y1:.0f}H{x2 - 9:.0f}" stroke="{kleur}" stroke-width="2"/>'
            f'<path d="M{x2:.0f} {y1:.0f}l-10 -5v10z" fill="{kleur}"/>')


# ---------------------------------------------------------------- blokken

def blok_ladder(b, x, y, w, p, ic):
    """Treden die oplopen. Een trede met leeg: true staat gestippeld en in grijs.

    Een ladder met terugloop houdt links een goot vrij voor de pijl die van een hogere trede
    terugwijst naar een lagere. Die pijl is de uitspraak zelf: werk dat hoger kwam en na een
    onbeantwoorde vraag opnieuw begint. Zonder goot zou de pijl door de treden heen lopen,
    want een hogere trede springt naar rechts in en laat links juist geen ruimte over.
    """
    treden = b["treden"]
    hoog = b.get("tredehoogte", 54)
    gat = 10
    inspring = b.get("inspring", 26)
    terug = b.get("terugloop")
    goot = 58 if terug else 0
    x += goot
    w -= goot
    svg = ""
    for i, t in enumerate(reversed(treden)):
        n = len(treden) - i
        leeg = t.get("leeg", False)
        tx = x + inspring * (n - 1)
        tw_ = w - inspring * (n - 1)
        ty = y + i * (hoog + gat)
        vul = p["np-bg"] if leeg else "#ffffff"
        rand = p["np-mid-gray"] if leeg else p["np-light-gray"]
        streep = p["np-light-gray"] if leeg else t.get("kleur", p["np-blue"])
        svg += kaart(tx, ty, tw_, hoog, vul, rand, streep=streep, gestippeld=leeg)
        bol = p["np-mid-gray"] if leeg else t.get("kleur", p["np-blue"])
        svg += f'<circle cx="{tx + 26:.0f}" cy="{ty + hoog / 2:.0f}" r="13" fill="{bol}"/>'
        svg += tekst(tx + 26, ty + hoog / 2 + 5, str(t["nummer"]), 13, "#ffffff", vet=True, midden=True)
        naamkleur = p["np-mid-gray"] if leeg else p["np-ink"]
        svg += tekst(tx + 50, ty + hoog / 2 - 3, t["naam"], 15, naamkleur, vet=True)
        if t.get("toelichting"):
            svg += tekst(tx + 50, ty + hoog / 2 + 15, t["toelichting"], 12, p["np-mid-gray"])
        if t.get("merk"):
            mb = tw(t["merk"], 11) + 18
            svg += kaart(tx + tw_ - mb - 14, ty + hoog / 2 - 11, mb, 22, p["np-pink"], p["np-pink"], straal=11)
            svg += tekst(tx + tw_ - mb - 14 + 9, ty + hoog / 2 + 4, t["merk"], 11, p["np-orange"], vet=True)
    if terug:
        svg += _terugloop(terug, treden, x, y, hoog, gat, inspring, goot, p)
    return svg, len(treden) * (hoog + gat) - gat


def _terugloop(terug, treden, x, y, hoog, gat, inspring, goot, p):
    """De pijl in de goot, van een hogere trede terug naar een lagere."""
    nummers = [t["nummer"] for t in treden]
    for sleutel in ("van", "naar"):
        if terug[sleutel] not in nummers:
            sys.exit(f"terugloop verwijst naar trede {terug[sleutel]}, die de ladder niet heeft")

    def linkerrand(nummer):
        i = len(treden) - nummers.index(nummer) - 1
        return x + inspring * nummers.index(nummer), y + i * (hoog + gat) + hoog / 2

    vx, vy = linkerrand(terug["van"])
    nx, ny = linkerrand(terug["naar"])
    gx = x - goot + 26
    kleur = p["np-mid-gray"]
    svg = (f'<path d="M{vx:.0f} {vy:.0f}H{gx + 10:.0f}q-10 0 -10 10V{ny - 10:.0f}'
           f'q0 10 10 10H{nx - 11:.0f}" fill="none" stroke="{kleur}" stroke-width="2"/>'
           f'<path d="M{nx - 2:.0f} {ny:.0f}l-10 -5v10z" fill="{kleur}"/>')
    if terug.get("tekst"):
        mx, my = gx - 13, (vy + ny) / 2
        svg += (f'<text x="{mx:.0f}" y="{my:.0f}" font-family="{FONT}" font-size="11"'
                f' fill="{kleur}" font-weight="600" text-anchor="middle"'
                f' transform="rotate(-90 {mx:.0f} {my:.0f})">{esc(terug["tekst"])}</text>')
    return svg


def blok_stappen(b, x, y, w, p, ic):
    stappen = b["stappen"]
    n = len(stappen)
    pijlbreed = 34
    kb = (w - pijlbreed * (n - 1)) / n
    hoog = b.get("hoogte", 96)
    svg = ""
    for i, s in enumerate(stappen):
        kx = x + i * (kb + pijlbreed)
        kleur = s.get("kleur", p["np-blue"])
        svg += kaart(kx, y, kb, hoog, "#ffffff", p["np-light-gray"], streep=kleur)
        if s.get("icoon"):
            svg += icoon(s["icoon"], kx + kb / 2 - 11, y + 18, 22, kleur, ic)
        regels = breek(s["naam"], kb - 20, 13, True)
        for j, r in enumerate(regels[:2]):
            svg += tekst(kx + kb / 2, y + 60 + j * 16, r, 13, p["np-ink"], vet=True, midden=True)
        if s.get("toelichting"):
            onder = y + 60 + len(regels[:2]) * 16 + 2
            for j, r in enumerate(breek(s["toelichting"], kb - 16, 11)[:2]):
                svg += tekst(kx + kb / 2, onder + j * 13, r, 11, p["np-mid-gray"], midden=True)
        if i < n - 1:
            svg += pijl(kx + kb + 8, y + hoog / 2, kx + kb + pijlbreed - 8, p["np-orange"])
    return svg, hoog


def blok_kolommen(b, x, y, w, p, ic):
    kols = b["kolommen"]
    gat = 24
    kb = (w - gat * (len(kols) - 1)) / len(kols)
    hoogtes = []
    svg_delen = []
    for i, k in enumerate(kols):
        kx = x + i * (kb + gat)
        kleur = k.get("kleur", p["np-blue"])
        inhoud = ""
        yy = 46
        for regel in k["regels"]:
            isvraag = regel.get("open", False)
            bullet = "?" if isvraag else "•"
            bk = p["np-orange"] if isvraag else kleur
            inhoud += f'<circle cx="{kx + 20:.0f}" cy="{y + yy - 4:.0f}" r="8" fill="{bk}" fill-opacity="0.14"/>'
            inhoud += tekst(kx + 20, y + yy, bullet, 11, bk, vet=True, midden=True)
            for j, r in enumerate(breek(regel["tekst"], kb - 50, 12.5)):
                inhoud += tekst(kx + 36, y + yy + j * 16, r, 12.5, p["np-dark-gray"])
            yy += 16 * max(1, len(breek(regel["tekst"], kb - 50, 12.5))) + 10
            if regel.get("bron"):
                inhoud += tekst(kx + 36, y + yy - 6, regel["bron"], 10.5, p["np-mid-gray"], cursief=True)
                yy += 14
        hoogtes.append(yy + 8)
        svg_delen.append((kx, kb, kleur, k["titel"], inhoud))
    hoog = max(hoogtes)
    svg = ""
    for kx, kb, kleur, titel, inhoud in svg_delen:
        svg += kaart(kx, y, kb, hoog, "#ffffff", p["np-light-gray"], streep=kleur)
        svg += tekst(kx + 18, y + 28, titel, 14, kleur, vet=True)
        svg += inhoud
    return svg, hoog


def blok_kaarten(b, x, y, w, p, ic):
    items = b["items"]
    n = len(items)
    gat = 16
    kb = (w - gat * (n - 1)) / n
    nodig = 0
    for it in items:
        tr = len(breek(it["titel"], kb - 32, 13.5, True)[:2])
        to = len(breek(it.get("toelichting", ""), kb - 32, 11)[:3]) if it.get("toelichting") else 0
        nodig = max(nodig, 60 + tr * 16 + (10 + to * 13 if to else 0) + 12)
    hoog = max(b.get("hoogte", 104), nodig)
    svg = ""
    for i, it in enumerate(items):
        kx = x + i * (kb + gat)
        kleur = it.get("kleur", p["np-blue"])
        svg += kaart(kx, y, kb, hoog, "#ffffff", p["np-light-gray"], streep=kleur)
        if it.get("icoon"):
            svg += icoon(it["icoon"], kx + 16, y + 18, 22, kleur, ic)
        titelregels = breek(it["titel"], kb - 32, 13.5, True)[:2]
        for j, r in enumerate(titelregels):
            svg += tekst(kx + 16, y + 60 + j * 16, r, 13.5, p["np-ink"], vet=True)
        if it.get("toelichting"):
            onder = y + 60 + len(titelregels) * 16 + 10
            for j, r in enumerate(breek(it["toelichting"], kb - 32, 11)[:3]):
                svg += tekst(kx + 16, onder + j * 13, r, 11, p["np-mid-gray"])
    return svg, hoog


def blok_legenda(b, x, y, w, p, ic):
    svg = ""
    cx = x
    for item in b["items"]:
        kleur = item.get("kleur", p["np-blue"])
        if item.get("gestippeld"):
            svg += kaart(cx, y - 11, 22, 16, p["np-bg"], p["np-mid-gray"], straal=4, gestippeld=True)
        else:
            svg += kaart(cx, y - 11, 22, 16, kleur, kleur, straal=4)
        svg += tekst(cx + 30, y + 2, item["tekst"], 12, p["np-dark-gray"])
        cx += 30 + tw(item["tekst"], 12) + 26
    return svg, 18


def blok_tekst(b, x, y, w, p, ic):
    svg, yy = "", 0
    for r in breek(b["tekst"], w, b.get("grootte", 13)):
        svg += tekst(x, y + yy + 11, r, b.get("grootte", 13), p.get(b.get("kleur", "np-dark-gray"), p["np-dark-gray"]))
        yy += REGELHOOGTE
    return svg, yy


BLOKKEN = {"ladder": blok_ladder, "stappen": blok_stappen, "kolommen": blok_kolommen,
           "kaarten": blok_kaarten, "legenda": blok_legenda, "tekst": blok_tekst}


def teken(sel: dict) -> str:
    p, ic = palet(), iconen()
    w = sel.get("breedte", 1200)
    binnen = w - 2 * RAND
    y = RAND
    svg = ""
    svg += tekst(RAND, y + 26, sel["titel"], 26, p["np-ink"], vet=True)
    y += 36
    if sel.get("ondertitel"):
        svg += tekst(RAND, y + 14, sel["ondertitel"], 14, p["np-mid-gray"])
        y += 26
    y += 16
    for b in sel["blokken"]:
        fn = BLOKKEN.get(b["soort"])
        if not fn:
            sys.exit(f"onbekend bloksoort: {b['soort']}")
        if b.get("kop"):
            svg += tekst(RAND, y + 13, b["kop"], 14, p["np-dark-blue"], vet=True)
            y += 26
        deel, hoog = fn(b, RAND, y, binnen, p, ic)
        svg += deel
        y += hoog + b.get("ruimte", 28)
    if sel.get("voet"):
        y += 2
        svg += f'<path d="M{RAND} {y:.0f}H{w - RAND}" stroke="{p["np-light-gray"]}" stroke-width="1"/>'
        y += 14
        for r in breek(sel["voet"], binnen, 12.5):
            svg += tekst(RAND, y + 11, r, 12.5, p["np-mid-gray"])
            y += 18
    h = y + RAND - 10
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h:.0f}" width="{w}"'
            f' height="{h:.0f}" role="img" aria-label="{esc(sel["titel"])}">'
            f'<rect width="{w}" height="{h:.0f}" fill="#ffffff"/>'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1:.0f}" rx="12" fill="none"'
            f' stroke="{p["np-light-gray"]}"/>{svg}</svg>')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selectie", required=True)
    ap.add_argument("--uit")
    ap.add_argument("--stil", action="store_true")
    a = ap.parse_args()
    pad = pathlib.Path(a.selectie)
    sel = json.loads(pad.read_text(encoding="utf-8"))
    uit = pathlib.Path(a.uit) if a.uit else pad.with_suffix(".svg")
    uit.parent.mkdir(parents=True, exist_ok=True)
    svg = teken(sel)
    uit.write_text(svg, encoding="utf-8")
    if not a.stil:
        m = re.search(r'height="(\d+)"', svg)
        print(f"{uit}: {sel.get('breedte', 1200)} bij {m.group(1) if m else '?'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
