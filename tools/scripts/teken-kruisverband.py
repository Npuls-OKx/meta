#!/usr/bin/env python3
"""Het kruisverband tussen twee lagen van een JSON-bericht tekenen als matrix.

Waarom dit script bestaat: een bericht dat eruitziet als een boom is dat vaak niet. In het
SBIS-bericht van RijnIJssel bundelt een leereenheid leertaken uit meer dan een
opleidingsonderdeel, en komt een leertaak in meer dan een leereenheid voor. In de tekst is dat
een zin met getallen erin; op een matrix zie je het in een oogopslag, en zie je er meteen bij
welke rijen of kolommen leeg blijven.

De selectie is het werk. Zij zegt welk bericht, welke twee lagen, en waar de verwijzing zit:

    {
      "titel": "...", "herkomst": "...", "versie": "0.1.0",
      "bron": "<pad>.json",
      "rijen":    {"pad": "opleidingseenheid.leereenheden", "verwijst_naar": "leertaken"},
      "kolommen": {"pad": "opleidingseenheid.opleidingsonderdelen", "bevat": "leertaken"}
    }

Een rij draagt een lijst codes; een kolom draagt een lijst objecten met een `code`. Staat een
code van de rij in de lijst van de kolom, dan is er een kruisje. Zo blijft het script los van
het bericht: het kent geen leereenheid en geen opleidingsonderdeel.

    python3 tools/scripts/teken-kruisverband.py --selectie <pad>.json --uit <pad>.svg
"""

import argparse
import html
import importlib.util
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("teken_modeldoorloop", WORTEL / "teken-modeldoorloop.py")
vt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vt)

INK, MUTED, LIJN, FONT = vt.INK, vt.MUTED, vt.LIJN, vt.FONT
ACCENT = "#d9531e"
VAK, VAK_RAND = "#2a6b8a", "#d8ddda"
ZEBRA = "#f7f8f8"

CEL = 15                      # zijde van een cel
MARGE = 18
KOP, HERKOMST_MAAT, LABEL, TEL = 17, 12, 11, 10
RIJLABEL = 250                # breedte van de kolom met de rijnamen
KOPHOOGTE_MIN = 24            # ondergrens voor de strook met de staande kolomlabels
MAX_RIJEN, MAX_KOLOMMEN = 80, 80


def haal(bron, pad):
    for deel in pad.split("."):
        bron = bron[deel]
    return bron


def kolomnaam(k, voorvoegsel, breed=30):
    """De kolom draagt haar naam en niet alleen haar code; een code alleen zegt een lezer niets."""
    naam = k.get("naam", "")
    naam = naam if len(naam) <= breed else naam[:breed - 1] + "\u2026"
    return f'{kort(k["code"], voorvoegsel)}  {naam}'.strip()


def kort(code, voorvoegsel):
    return code[len(voorvoegsel):] if voorvoegsel and code.startswith(voorvoegsel) else code


def gemeen_voorvoegsel(codes):
    """Het stuk dat elke code deelt; dat hoort in de legenda en niet zestig keer op de plaat."""
    codes = sorted(codes)
    if len(codes) < 2:
        return ""
    eerste, laatste = codes[0], codes[-1]
    n = 0
    while n < min(len(eerste), len(laatste)) and eerste[n] == laatste[n]:
        n += 1
    return eerste[:n]


def lees(selectie_pad):
    sel = json.loads(pathlib.Path(selectie_pad).read_text(encoding="utf-8"))
    for sleutel in ("titel", "herkomst", "bron", "rijen", "kolommen"):
        if not sel.get(sleutel):
            sys.exit(f"{selectie_pad}: de selectie draagt geen {sleutel}")
    bron = (pathlib.Path(selectie_pad).parent / sel["bron"]).resolve()
    if not bron.exists():
        bron = pathlib.Path(sel["bron"])
    data = json.loads(bron.read_text(encoding="utf-8"))

    rijen = haal(data, sel["rijen"]["pad"])
    kolommen = haal(data, sel["kolommen"]["pad"])
    if len(rijen) > MAX_RIJEN or len(kolommen) > MAX_KOLOMMEN:
        sys.exit(f"{len(rijen)} rijen en {len(kolommen)} kolommen (hoogstens "
                 f"{MAX_RIJEN} bij {MAX_KOLOMMEN}); kies een deel van het bericht")

    # waar hoort een verwijzing thuis: code van het deel naar code van de kolom
    thuis = {}
    for k in kolommen:
        for deel in k.get(sel["kolommen"]["bevat"], []):
            thuis[deel["code"]] = k["code"]

    paren = set()
    for r in rijen:
        for code in r.get(sel["rijen"]["verwijst_naar"], []):
            code = code["code"] if isinstance(code, dict) else code
            if code in thuis:
                paren.add((r["code"], thuis[code]))
    return sel, rijen, kolommen, paren


def teken(sel, rijen, kolommen, paren):
    rv = gemeen_voorvoegsel([r["code"] for r in rijen])
    kv = gemeen_voorvoegsel([k["code"] for k in kolommen])
    # de strook boven de matrix is zo hoog als het langste staande kolomlabel; een vaste
    # hoogte laat een plaat met korte codes met een lege band erboven staan
    langste = max((len(kolomnaam(k, kv)) for k in kolommen), default=0)
    kophoogte = max(KOPHOOGTE_MIN, int(langste * LABEL * 0.62) + 10)
    breed = MARGE + RIJLABEL + len(kolommen) * CEL + 90 + MARGE
    hoog = (MARGE + KOP + HERKOMST_MAAT + 10 + kophoogte + len(rijen) * CEL + 52 + MARGE
            + (28 if sel.get("leesregel") else 0))
    x0, y0 = MARGE + RIJLABEL, MARGE + KOP + HERKOMST_MAAT + 10 + kophoogte

    d = [f'<rect x="0.5" y="0.5" width="{breed - 1}" height="{hoog - 1}" rx="10" '
         f'fill="#ffffff" stroke="{LIJN}"/>',
         vt.text(MARGE, MARGE + KOP - 2, sel["titel"], KOP, bold=True),
         vt.text(MARGE, MARGE + KOP + HERKOMST_MAAT + 2, sel["herkomst"], HERKOMST_MAAT, fill=MUTED)]
    if sel.get("versie"):
        d.append(vt.text(breed - MARGE, MARGE + KOP - 2, f"v{sel['versie']}", HERKOMST_MAAT,
                         fill=MUTED, anchor="end"))

    per_rij = {r["code"]: sum(1 for p in paren if p[0] == r["code"]) for r in rijen}
    per_kolom = {k["code"]: sum(1 for p in paren if p[1] == k["code"]) for k in kolommen}

    for j, k in enumerate(kolommen):
        x = x0 + j * CEL + CEL / 2
        kleur = ACCENT if per_kolom[k["code"]] == 0 else INK
        d.append(f'<text transform="translate({x:.0f},{y0 - 8}) rotate(-90)" font-family="{FONT}" '
                 f'font-size="{LABEL}" fill="{kleur}" text-anchor="start">'
                 f'{html.escape(kolomnaam(k, kv))}</text>')
        d.append(vt.text(x, y0 + len(rijen) * CEL + 16, str(per_kolom[k["code"]]), TEL,
                         fill=MUTED, anchor="middle"))
    d.append(vt.text(MARGE, y0 - 8, sel["rijen"].get("opschrift", "rijen"), LABEL,
                     bold=True, fill=MUTED))
    d.append(f'<text transform="translate({x0 + len(kolommen) * CEL + 40},{y0 - 8}) rotate(-90)" '
             f'font-family="{FONT}" font-size="{LABEL}" font-weight="bold" fill="{MUTED}" '
             f'text-anchor="start">{html.escape(sel["kolommen"].get("opschrift", "kolommen"))}</text>')

    for i, r in enumerate(rijen):
        y = y0 + i * CEL
        if i % 2:
            d.append(f'<rect x="{MARGE}" y="{y}" width="{breed - 2 * MARGE}" height="{CEL}" '
                     f'fill="{ZEBRA}"/>')
        n = per_rij[r["code"]]
        kleur = ACCENT if n > 1 else INK
        naam = r.get("naam", r["code"])
        if len(naam) > 30:
            naam = naam[:29] + "…"
        d.append(vt.text(MARGE + 4, y + CEL - 4, f'{kort(r["code"], rv)}  {naam}', LABEL, fill=kleur))
        d.append(vt.text(x0 + len(kolommen) * CEL + 14, y + CEL - 4, str(n), TEL,
                         fill=ACCENT if n > 1 else MUTED))
        for j, k in enumerate(kolommen):
            if (r["code"], k["code"]) in paren:
                d.append(f'<rect x="{x0 + j * CEL + 2}" y="{y + 2}" width="{CEL - 4}" '
                         f'height="{CEL - 4}" rx="2" fill="{VAK}"/>')

    for j in range(len(kolommen) + 1):
        d.append(f'<path d="M{x0 + j * CEL} {y0}V{y0 + len(rijen) * CEL}" stroke="{LIJN}"/>')
    for i in range(len(rijen) + 1):
        d.append(f'<path d="M{x0} {y0 + i * CEL}H{x0 + len(kolommen) * CEL}" stroke="{LIJN}"/>')

    meer = sum(1 for v in per_rij.values() if v > 1)
    leeg = sum(1 for v in per_kolom.values() if v == 0)
    if sel.get("leesregel"):
        d.append(f'<rect x="{MARGE}" y="{hoog - MARGE - 42}" width="11" height="11" rx="2" '
                 f'fill="{VAK}"/>')
        d.append(vt.text(MARGE + 18, hoog - MARGE - 33, sel["leesregel"], LABEL, fill=INK))
    d.append(vt.text(MARGE, hoog - MARGE - 14,
                     f"{len(paren)} verbindingen; {meer} van de {len(rijen)} rijen raken meer dan "
                     f"een kolom; {leeg} kolommen blijven leeg, in de accentkleur", LABEL, fill=MUTED))
    d.append(vt.text(MARGE, hoog - MARGE,
                     f"rijcodes zonder {rv!r}, kolomcodes zonder {kv!r}" if rv or kv else "",
                     LABEL, fill=MUTED))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breed} {hoog}" '
            f'width="{breed}" height="{hoog}">' + "".join(d) + "</svg>"), len(paren), meer, leeg


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selectie", required=True)
    p.add_argument("--uit", required=True)
    a = p.parse_args()
    sel, rijen, kolommen, paren = lees(a.selectie)
    svg, n, meer, leeg = teken(sel, rijen, kolommen, paren)
    pathlib.Path(a.uit).write_text(svg, encoding="utf-8")
    print(f"{a.uit}: {len(rijen)} bij {len(kolommen)}, {n} verbindingen, "
          f"{meer} rijen met meer dan een kolom, {leeg} lege kolommen")


if __name__ == "__main__":
    main()
