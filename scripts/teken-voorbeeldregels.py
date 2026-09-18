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
CONCEPT, CONCEPT_L, CONCEPT_T = "#efe6ff", "#9b86c9", "#4a3a78"  # objecttype van de conceptplaat
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


def element(x, y, kind, label, inst, fill=BUS, line=BUS_L, labelkleur=BUS_T, rx=0, dashed=False, toestand=None, verwijzing=None, verwijzingen=(), rid=None):
    """Eén element: typelabel klein (met het regel-ID rechts), instantie vet, en eronder de toestand en de
    verwijzingen naar objecten buiten het blok. Geeft (svg, w, h)."""
    extra = _extra(toestand, verwijzing, verwijzingen)
    w = max(120, max([tw(label, 11) + (tw(rid, 10) + 12 if rid else 0), tw(inst, 13, True)] + [tw(e, 11) for e in extra]) + 42)
    h = 46 + 16 * len(extra)
    s = box(x, y, w, h, fill, line, rx, dashed) + icon(kind, x + w - 22, y + 5)
    s += text(x + 10, y + 17, label, 11, fill=labelkleur)
    if rid:
        s += text(x + w - 28, y + 17, rid, 10, fill=MUTED, anchor="end")
    s += text(x + 10, y + 34, inst, 13, True)
    for i, e in enumerate(extra):
        s += text(x + 10, y + 50 + 16 * i, e, 11, fill=MUTED)
    return s, w, h


def _extra(toestand, verwijzing, verwijzingen):
    uit = [f"toestand: {toestand}"] if toestand else []
    if verwijzing:
        uit.append(verwijzing)
    uit += [v for v in verwijzingen if v]
    return uit


RELATIE_AFSTAND = 56  # ruimte tussen twee objecten waar een relatielijn loopt
CONCEPTPLAAT = "Informatiemodel Onderwijsontwerp"


def relatielijn(x1, y, x2, soort, label, naar_rechts=True):
    """Een ArchiMate-relatie tussen twee objecten op dezelfde hoogte. naar_rechts: de relatie loopt van het
    linker object (van) naar het rechter (naar). Aggregatie: open ruit aan de kant van het geheel (van);
    compositie: gevulde ruit; specialisatie: open pijlpunt aan de kant van het algemene (naar);
    associatie: lijn, met een kleine pijlpunt als de plaat een richting geeft."""
    s = f'<path d="M{x1:.0f} {y:.0f}H{x2:.0f}" stroke="#444" stroke-width="1.3" fill="none"/>'
    geheel, deel = (x1, x2) if naar_rechts else (x2, x1)
    if soort in ("Aggregation", "Composition"):
        vulling = "#444" if soort == "Composition" else "#ffffff"
        r = 1 if geheel < deel else -1
        s += f'<path d="M{geheel:.0f} {y:.0f}l{7*r} -5l{7*r} 5l{-7*r} 5z" fill="{vulling}" stroke="#444" stroke-width="1.3"/>'
    elif soort == "Specialization":
        r = 1 if geheel < deel else -1
        s += f'<path d="M{deel:.0f} {y:.0f}l{-10*r} -6v12z" fill="#ffffff" stroke="#444" stroke-width="1.3"/>'
    elif label:
        r = 1 if geheel < deel else -1
        s += f'<path d="M{deel:.0f} {y:.0f}l{-8*r} -4v8z" fill="#444"/>'
    if label:
        s += text((x1 + x2) / 2, y - 5, label, 10, fill=MUTED, anchor="middle")
    return s


MAX_BREEDTE = 1500  # daarboven gaat een keten van relaties onder elkaar in plaats van naast elkaar


def relatielijn_v(x, y1, y2, soort, label, omlaag=True):
    """Verticale variant van relatielijn: van het object erboven (y1) naar het object eronder (y2)."""
    s = f'<path d="M{x:.0f} {y1:.0f}V{y2:.0f}" stroke="#444" stroke-width="1.3" fill="none"/>'
    geheel, deel = (y1, y2) if omlaag else (y2, y1)
    r = 1 if geheel < deel else -1
    if soort in ("Aggregation", "Composition"):
        vulling = "#444" if soort == "Composition" else "#ffffff"
        s += f'<path d="M{x:.0f} {geheel:.0f}l-5 {7*r}l5 {7*r}l5 {-7*r}z" fill="{vulling}" stroke="#444" stroke-width="1.3"/>'
    elif soort == "Specialization":
        s += f'<path d="M{x:.0f} {deel:.0f}l-6 {-10*r}h12z" fill="#ffffff" stroke="#444" stroke-width="1.3"/>'
    elif label:
        s += f'<path d="M{x:.0f} {deel:.0f}l-4 {-8*r}h8z" fill="#444"/>'
    if label:
        s += text(x + 8, (y1 + y2) / 2 + 4, label, 10, fill=MUTED)
    return s


def objecten(x, y, items, uitzonderingen):
    """Rij van objecten met de relaties van de plaat als lijnen ertussen; nesting bij kinderen.
    Wordt de rij breder dan MAX_BREEDTE, dan gaat de keten na het eerste object onder elkaar.
    Geeft (svg, w, h)."""
    svg, w, h = _objecten_rij(x, y, items, uitzonderingen)
    if w <= MAX_BREEDTE or len(items) < 3:
        return svg, w, h
    return _objecten_kolom(x, y, items, uitzonderingen)


def _objecten_kolom(x, y, items, uitzonderingen):
    """Eerste object links; de rest als kolom rechts ervan, met verticale relatielijnen."""
    eerste = items[0]
    svg1, w1, h1 = _objecten_rij(x, y, [eerste], uitzonderingen)
    kx = x + w1 + RELATIE_AFSTAND
    ky = y
    out = svg1
    lijnen = ""
    vorige_onder = None
    vorige_mid_x = None
    wachtende_relatie = None
    maxw = w1 + RELATIE_AFSTAND
    for it in items[1:]:
        if "relatie" in it and "type" not in it:
            wachtende_relatie = it
            continue
        svg_it, w_it, h_it = _objecten_rij(kx, ky, [it], uitzonderingen)
        out += svg_it
        if wachtende_relatie is not None:
            if vorige_onder is None:
                # relatie tussen het eerste object (links) en dit object: horizontaal, op de hoogte van dit object
                lijnen += relatielijn(x + w1, ky + 23, kx, wachtende_relatie.get("soort", "Association"), wachtende_relatie["relatie"], wachtende_relatie.get("naar_rechts", True))
            else:
                lijnen += relatielijn_v(kx + min(w_it, 120) / 2, vorige_onder, ky, wachtende_relatie.get("soort", "Association"), wachtende_relatie["relatie"], wachtende_relatie.get("naar_rechts", True))
            wachtende_relatie = None
        vorige_onder = ky + h_it
        ky += h_it + 28
        maxw = max(maxw, w1 + RELATIE_AFSTAND + w_it)
    return out + lijnen, maxw, max(h1, ky - 28 - y)


STROOMGAT = 24  # tussenruimte tussen objecten die samen over een pijl gaan en geen relatielijn delen


def _objecten_rij(x, y, items, uitzonderingen, verbind=False):
    """verbind: de objecten gaan samen over een pijl; waar geen relatielijn loopt, staan ze iets verder uit elkaar."""
    out, cx, maxh = "", x, 0
    lijnen = ""
    vorige_rand = None  # rechterrand en middenhoogte van het vorige object
    na_relatie = False
    for it in items:
        if "relatie" in it and "type" not in it:
            # een relatie tussen het vorige en het volgende object: lijn met ruit of pijl
            it_soort = it.get("soort", "Association")
            if vorige_rand:
                x1, ym = vorige_rand
                afstand = max(RELATIE_AFSTAND, tw(it["relatie"], 10) + 24)  # de lijn is minstens zo lang als het label
                lijnen += relatielijn(x1, ym, x1 + afstand, it_soort, it["relatie"], it.get("naar_rechts", True))
                cx = x1 + afstand
                na_relatie = True
            continue
        if verbind and vorige_rand and not na_relatie:
            cx = vorige_rand[0] + STROOMGAT
        na_relatie = False
        dashed = it.get("aanname", False)
        buiten = it["type"] in uitzonderingen
        fill, line, lk = (GRIJS, GRIJS_L, GRIJS_T) if buiten else (BUS, BUS_L, BUS_T)
        if it.get("plaat") == "onderwijsontwerp":
            fill, line, lk = CONCEPT, CONCEPT_L, CONCEPT_T
        if it.get("kinderen"):
            # een container toont, net als een los element, de toestand en verwijzingen onder de instantie
            extra = _extra(it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()))
            kop = 40 + 16 * len(extra)
            ksvg, kw, kh = _kinderen(cx + 14, y + kop, it["kinderen"], uitzonderingen)
            rid = it.get("id")
            w = max([kw + 24, tw(it["type"], 11) + (tw(rid, 10) + 12 if rid else 0) + 42, tw(it["instantie"], 13, True) + 42] + [tw(e, 11) + 42 for e in extra])
            h = kop + kh + 10
            out += box(cx, y, w, h, fill, line, 0, dashed) + icon("object", cx + w - 22, y + 5)
            out += text(cx + 10, y + 17, it["type"], 11, fill=lk) + text(cx + 10, y + 34, it["instantie"], 13, True) + ksvg
            if rid:
                out += text(cx + w - 28, y + 17, rid, 10, fill=MUTED, anchor="end")
            for i, e in enumerate(extra):
                out += text(cx + 10, y + 50 + 16 * i, e, 11, fill=MUTED)
        else:
            s, w, h = element(cx, y, "object", it["type"], it["instantie"], fill, line, lk, 0, dashed, it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()), it.get("id"))
            out += s
        vorige_rand = (cx + w, y + 23)
        cx += w + 8
        maxh = max(maxh, h)
    return out + lijnen, cx - x - 8, maxh


STROOM_MAX_BREEDTE = 1700  # breder dan dit: de keten over een pijl loopt door op een volgende rij


def _objecten_rijen(x, y, items, uitzonderingen, maxbreedte=STROOM_MAX_BREEDTE):
    """De objecten over een pijl, naast elkaar; wordt de rij breder dan maxbreedte, dan gaat de keten
    verder op een volgende rij. Een relatie blijft bij het object dat volgt.
    Geeft (svg, w, h, rijen) met per rij (y, rechterrand)."""
    groepen, wacht = [], []
    for it in items:
        wacht.append(it)
        if "type" in it:
            groepen.append(wacht)
            wacht = []
    rijen, huidige = [], []
    for g in groepen:
        proef = huidige + g
        _, w, _ = _objecten_rij(x, y, proef, uitzonderingen, True)
        if huidige and w > maxbreedte:
            rijen.append(huidige)
            huidige = list(g)
        else:
            huidige = proef
    if huidige:
        rijen.append(huidige)
    out, ry, maxw, uit = "", y, 0, []
    for i, rij in enumerate(rijen):
        # een relatie aan het begin van een vervolgrij hoort bij het vorige object: als verwijzing tonen
        if rij and "type" not in rij[0]:
            rel = rij.pop(0)
            rij[0].setdefault("verwijzingen", []).append(f"{rel['relatie'] or STANDAARDLABEL.get(rel['soort'], 'hangt aan')} (vorige rij)")
        svg, w, h = _objecten_rij(x, ry, rij, uitzonderingen, True)
        out += svg
        uit.append((ry, x + w))
        maxw = max(maxw, w)
        ry += h + 28
    return out, maxw, ry - 28 - y, uit


KINDEREN_MAX_BREEDTE = 900  # breder dan dit: de kinderen onder elkaar in plaats van naast elkaar


def _kinderen(x, y, items, uitzonderingen):
    """Kinderen van een container: naast elkaar, of onder elkaar als de rij te breed wordt."""
    svg, w, h = _objecten_rij(x, y, items, uitzonderingen)
    if w <= KINDEREN_MAX_BREEDTE or len(items) < 2:
        return svg, w, h
    out, ky, maxw = "", y, 0
    for it in items:
        s, iw, ih = _objecten_rij(x, ky, [it], uitzonderingen)
        out += s
        ky += ih + 8
        maxw = max(maxw, iw)
    return out, maxw, ky - 8 - y


def wrap(W, H, body, dashed=False):
    rand = ' stroke-dasharray="6 4"' if dashed else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">'
            f'<rect x="0.5" y="0.5" width="{W-1:.0f}" height="{H-1:.0f}" rx="10" fill="#ffffff" stroke="{LIJN}"{rand}/>{body}</svg>')


def regel_ontstaat(blok, uitzonderingen):
    y0 = 10
    wie, ww, wh = element(12, y0, "rol", "rol", blok["wie"], BUS, BUS_L, BUS_T, 8)
    x = 12 + ww + 10
    verdieping = f"verdieping: {blok['verdieping']}" if blok.get("verdieping") else None
    stap, sw, sh = element(x, y0, "proces", "processtap", blok["stap"], BUS, BUS_L, BUS_T, 8, verwijzing=verdieping)
    x += sw + 6
    pijl = text(x, y0 + 30, "→", 18, fill=MUTED)
    x += 20
    objs, ow, oh = objecten(x, y0, blok["objecten"], uitzonderingen)
    rowh = max(wh, sh, oh)
    zin_y = y0 + rowh + 22
    concept = blok.get("plaat") == "onderwijsontwerp"
    chip, zin_x = "", 12
    if concept:
        # een verdieping op de conceptplaat: gestippelde rand en een chip voor de zin
        tekst = f"conceptplaat: {CONCEPTPLAAT}"
        cw = tw(tekst, 11) + 16
        chip = box(12, zin_y - 13, cw, 18, "#ffffff", "#c8ccc9", 9, True, "2 2") + text(20, zin_y, tekst, 11, fill=MUTED)
        zin_x = 12 + cw + 10
    W = max(x + ow + 12, zin_x + tw(blok.get("zin", ""), 13) + 12)
    H = zin_y + 12
    return wrap(W, H, wie + stap + pijl + objs + chip + text(zin_x, zin_y, blok.get("zin", ""), 13, fill=MUTED), dashed=concept)


def regel_stroomt(blok, uitzonderingen):
    """De stroom: bovenaan de pijl van component naar component als horizontale stippellijn, met de
    koppeling-ID en de processtap; eronder, aan de lijn gehangen, de objecten die samen overgaan."""
    y0 = 10
    lijn = 34
    idtekst = blok.get("koppeling") or ("geen pijl op de hoofdplaat" if blok.get("pijl") == "geen pijl op de hoofdplaat" else "zonder koppelingspecificatie")
    idw = tw(idtekst, 11) + 16
    s = box(12, y0 + 14, idw, 18, "#ffffff", "#c8ccc9", 4) + text(20, y0 + 27, idtekst, 11, fill=MUTED)
    x = 12 + idw + 12
    van, vw, vh = element(x, y0, "component", "van", blok["van"], APP, APP_L, APP_T)
    s += van
    x_lijn = x + vw + 6
    # de objecten onder de lijn, iets ingesprongen; ze hangen met een stippellijn aan de pijl
    ox, oy = x_lijn + 20, y0 + vh + 26
    osvg, ow, oh, rijen = _objecten_rijen(ox, oy, blok["objecten"], uitzonderingen)
    naar, nw, nh = element(0, 0, "component", "naar", blok["naar"], APP, APP_L, APP_T)
    stap_tekst = "na: " + blok["stap"]
    stapw = tw(stap_tekst, 11) + 16
    x_naar = max(x_lijn + 240, ox + ow + lijn) 
    s += f'<path d="M{x_lijn} {y0+23}H{x_naar - 10}" stroke="{APP_T}" stroke-width="2" stroke-dasharray="5 4"/>'
    s += f'<path d="M{x_naar - 12} {y0+17}l10 6-10 6z" fill="{APP_T}"/>'
    naar, nw, nh = element(x_naar, y0, "component", "naar", blok["naar"], APP, APP_L, APP_T)
    s += naar
    sx = x_naar + nw + 10
    s += box(sx, y0 + 14, stapw, 18, "#ffffff", "#c8ccc9", 9, True, "2 2") + text(sx + 8, y0 + 27, stap_tekst, 11, fill=MUTED)
    # de ophanging: van de pijl naar de bovenkant van de eerste rij, en langs de linkerkant van elke rij
    hx = ox + 24
    s += f'<path d="M{hx} {y0+23}V{oy - 4}" stroke="{APP_T}" stroke-width="1.5" stroke-dasharray="3 3"/>'
    for ry, _ in rijen[1:]:
        s += f'<path d="M{hx} {oy}V{ry - 4}" stroke="{APP_T}" stroke-width="1.5" stroke-dasharray="3 3"/>'
    s += osvg
    zin_y = oy + oh + 22
    W = max(sx + stapw + 12, ox + ow + 12, tw(blok.get("zin", ""), 13) + 24)
    H = zin_y + 12
    body = f'<rect x="0" y="0" width="4" height="{H:.0f}" fill="{APP_L}"/>' + s + text(12, zin_y, blok.get("zin", ""), 13, fill=MUTED)
    return wrap(W, H, body)


STANDAARDLABEL = {"Specialization": "is een", "Aggregation": "bevat", "Composition": "bevat"}


def _verwijzing(rel, objecttype):
    """De tekst van een verwijzing: het label van de plaat (of een standaardlabel) en het andere eind,
    in leesrichting; met de instantie aan het andere eind als de regel die geeft."""
    ander = rel["naar"] if rel["van"] == objecttype else rel["van"]
    label = rel.get("label") or STANDAARDLABEL.get(rel["soort"], "hangt aan")
    tekst = f"{label} {ander}" if rel["van"] == objecttype else f"{ander} {label}"
    return f"{tekst}: {rel['instantie']}" if rel.get("instantie") else tekst


def groepeer(regels):
    """Regels met dezelfde fase, stap en soort worden één blok; ontstaat en verandert samen. Een regel met
    het veld verdieping vormt met zijn gelijken een eigen blok onder dezelfde stap."""
    blokken = []
    for r in regels["regels"]:
        soort = r["soort"]
        if soort == "stroomt":
            laatste = blokken[-1] if blokken else None
            item = {"type": r["objecttype"], "instantie": r["instantie"], "aanname": r.get("aanname", False), "id": r.get("id"),
                    "plaat": r.get("plaat", "informatiemodel"), "verwijzingen": [_verwijzing(x, r["objecttype"]) for x in r.get("relaties", [])]}
            rel = r.get("relatie")
            if laatste and laatste["soort"] == "stroomt" and (laatste["fase"], laatste["stap"], laatste["van"], laatste["naar"]) == (r["fase"], r["stap"], r["van"], r["naar"]):
                buur_s = next((it for it in reversed(laatste["objecten"]) if "type" in it), None)
                in_blok_s = ({buur_s["type"]} | {k.get("type") for k in buur_s.get("kinderen", [])}) if buur_s else set()
                if rel and not rel.get("nesting"):
                    ander = rel["naar"] if rel["van"] == r["objecttype"] else rel["van"]
                    if ander in in_blok_s:
                        laatste["objecten"].append({"relatie": rel.get("label") or "", "soort": rel["soort"], "naar_rechts": rel["naar"] == r["objecttype"]})
                    else:
                        item["verwijzing"] = _verwijzing(rel, r["objecttype"])
                if rel and rel.get("nesting"):
                    def zoek_s(items):
                        for it in items:
                            if it.get("type") == rel["van"]:
                                return it
                            g = zoek_s(it.get("kinderen", []))
                            if g is not None:
                                return g
                        return None
                    ouder = zoek_s(laatste["objecten"])
                    if ouder is not None:
                        ouder.setdefault("kinderen", []).append(item)
                        continue
                laatste["objecten"].append(item)
                continue
            if rel and not rel.get("nesting"):
                # het eerste object van een stroom: zijn relatie wijst altijd buiten het blok
                item["verwijzing"] = _verwijzing(rel, r["objecttype"])
            blokken.append({"soort": "stroomt", "fase": r["fase"], "stap": r["stap"], "van": r["van"], "naar": r["naar"],
                            "koppeling": r.get("koppeling"), "pijl": r.get("pijl"), "objecten": [item], "zin": r.get("zin", "")})
            continue
        laatste = blokken[-1] if blokken else None
        if not laatste or laatste["soort"] != "ontstaat" or (laatste["fase"], laatste["stap"], laatste["wie"], laatste.get("verdieping")) != (r["fase"], r["stap"], r.get("wie"), r.get("verdieping")):
            laatste = {"soort": "ontstaat", "fase": r["fase"], "stap": r["stap"], "wie": r.get("wie"), "verdieping": r.get("verdieping"),
                       "plaat": r.get("plaat", "informatiemodel"), "objecten": [], "zin": r.get("zin", "")}
            blokken.append(laatste)
        item = {"type": r["objecttype"], "instantie": r["instantie"], "aanname": r.get("aanname", False), "id": r.get("id"),
                "plaat": r.get("plaat", "informatiemodel"), "verwijzingen": [_verwijzing(x, r["objecttype"]) for x in r.get("relaties", [])]}
        if soort == "verandert":
            item["toestand"] = r.get("toestand")
        rel = r.get("relatie")
        # een relatielijn loopt alleen naar het object ernaast (of een kind daarvan); een relatie naar een
        # object verder terug in het blok, of uit een eerdere stap, staat als verwijzing op het object
        buur = next((it for it in reversed(laatste["objecten"]) if "type" in it), None)
        in_blok = ({buur["type"]} | {k.get("type") for k in buur.get("kinderen", [])}) if buur else set()
        if rel and rel.get("nesting"):
            def zoek(items):
                for it in items:
                    if it.get("type") == rel["van"]:
                        return it
                    gevonden = zoek(it.get("kinderen", []))
                    if gevonden is not None:
                        return gevonden
                return None
            ouder = zoek(laatste["objecten"])
            if ouder is not None:
                ouder.setdefault("kinderen", []).append(item)
                continue
        if rel and not rel.get("nesting"):
            ander = rel["naar"] if rel["van"] == r["objecttype"] else rel["van"]
            if ander in in_blok:
                # het andere eind staat ernaast in dit blok: relatielijn ertussen; naar_rechts als dit object het doel is
                laatste["objecten"].append({"relatie": rel.get("label") or "", "soort": rel["soort"], "naar_rechts": rel["naar"] == r["objecttype"]})
            else:
                item["verwijzing"] = _verwijzing(rel, r["objecttype"])
        laatste["objecten"].append(item)
        if r.get("zin") and not laatste["zin"]:
            laatste["zin"] = r["zin"]
    return blokken


def bestandsnaam(blok, volgnummer):
    slug = re.sub(r"[^a-z0-9]+", "-", blok["stap"].lower()).strip("-")
    if blok.get("verdieping"):
        slug += "-verdieping"
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
