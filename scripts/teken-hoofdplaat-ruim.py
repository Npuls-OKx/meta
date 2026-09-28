#!/usr/bin/env python3
"""De hoofdplaat informatiestromen ruimer opgezet en netjes gerouteerd.

Waarom dit script bestaat: hoofdplaat v1.7 vertelt een helder verhaal in twee procesgebieden,
links de onderwijsontwikkeling en rechts de onderwijsuitvoering, met de applicatiecomponenten
die daarin met elkaar praten. Elke informatiestroom blijft binnen haar eigen gebied; daarom
staat een component dat in beide processen meedoet er twee keer op. Dat verhaal blijft hier
overeind: dit script neemt de plaat zoals zij is, houdt elke groep, elk component en elke
dienst op haar eigen plek, en trekt alleen de ruimte ertussen open. Met die ruimte krijgt elke
lijn een eigen baan: recht waar het kan, en anders met een hoek van 90 graden.

De plaat komt uit het model, dus zij loopt mee met elke wijziging van de view. Het model wordt
alleen gelezen; raak nooit een .archimate-bestand aan.

    python3 scripts/teken-hoofdplaat-ruim.py --uit <pad>.svg
"""

import argparse
import collections
import html
import importlib.util
import json
import pathlib
import sys
import xml.etree.ElementTree as ET

WORTEL = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("hoofdplaat", WORTEL / "teken-hoofdplaat-highlight.py")
hoofdplaat = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hoofdplaat)

MODEL = pathlib.Path("architecture/model/model.archimate")
STROMEN = pathlib.Path("architecture/model/informatiemodel/stromen.json")
VIEW = "OKx hoofdplaat v1.7<concept>"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"

INKT = "#12314f"
STIL = "#66798c"
COMPONENT_VUL = "#e6f2fb"
COMPONENT_RAND = "#2a6ebb"
DIENST_VUL = "#f7fbfe"
DIENST_RAND = "#9cc8e4"
GROEP_RAND = "#aebecd"
NOTITIE_VUL = "#fdfbe9"
NOTITIE_RAND = "#d8d4a8"
ZONE = ("#faf5ee", "#f0f5fa")
ZONE_RAND = ("#e4d8c6", "#d3e0ec")

# een gedempte kleur per bronsysteem, zodat te volgen is waar een lijn vandaan komt
PALET = ["#d9531e", "#1f6feb", "#0f8a8a", "#6b4bb8", "#2e7d32", "#8a5a12", "#b1268b", "#44607a"]

ZONENAAM = {
    "links": "onderwijsontwikkeling · inrichting van nominale- en keuze aanbod",
    "rechts": "onderwijsuitvoering · student studeert en maakt keuzes",
}

LETTER = 15     # de maat van een stroomnaam; de rest van de plaat schaalt hierop mee
BREED = LETTER * 0.55   # geschatte breedte van een teken


def norm(s):
    return " ".join(str(s or "").split())


# ------------------------------------------------------------------ inlezen --

def lees(model, viewnaam):
    """De view als boom van knopen, plus de verbindingen en de namen uit het model."""
    boom = ET.parse(model)
    wortel = boom.getroot()
    elems = {e.get("id"): (e.get(XSI, "").split(":")[-1], norm(e.get("name")))
             for e in wortel.iter("element") if e.get(XSI)}
    relaties = {e.get("id"): e.get(XSI, "").split(":")[-1] for e in wortel.iter() if e.get("id")}
    view = next(e for e in wortel.iter("element")
                if e.get(XSI) == "archimate:ArchimateDiagramModel" and e.get("name") == viewnaam)
    knopen, verbindingen = {}, []

    def opschrift(el):
        f = el.find("feature[@name='labelExpression']")
        return [norm(r) for r in f.get("value").splitlines() if norm(r)] if f is not None else []

    def maak(c, ouder):
        b = c.find("bounds")
        soort = c.get(XSI, "").split(":")[-1]
        type_, naam = elems.get(c.get("archimateElement"), ("", ""))
        inhoud = c.find("content")
        knoop = dict(id=c.get("id"), x=int(b.get("x", 0)), y=int(b.get("y", 0)),
                     w=int(b.get("width", 120)), h=int(b.get("height", 55)),
                     soort=soort, type=type_, naam=naam or norm(c.get("name")),
                     tekst=norm(inhoud.text if inhoud is not None else ""),
                     opschrift=opschrift(c), ouder=ouder, kinderen=[])
        knopen[knoop["id"]] = knoop
        for sc in c.findall("sourceConnection"):
            verbindingen.append(dict(bron=c.get("id"), doel=sc.get("target"),
                                     relatie=sc.get("archimateRelationship"),
                                     opschrift=opschrift(sc)))
        for kind in c.findall("child"):
            knoop["kinderen"].append(maak(kind, knoop))
        return knoop

    top = [maak(c, None) for c in view.findall("child")]
    return top, knopen, [v for v in verbindingen if v["doel"] in knopen], relaties


def labels_van_stromen():
    return {s["id"]: s.get("label", "") for s in json.loads(STROMEN.read_text(encoding="utf-8"))["stromen"]}


# ---------------------------------------------------------------- ruimte ----

def is_groep(knoop):
    return knoop["soort"] == "Group"


def op_maat(knoop, kleinst=14.0):
    """Een vak dat te klein is voor zijn eigen naam wordt breder; de plaat heeft de ruimte."""
    if knoop["kinderen"] or knoop["soort"] == "Note" or knoop["type"] in ("Junction", ""):
        return
    naam = " ".join(knoop["opschrift"]) or knoop["naam"]
    if not naam:
        return
    langste = max((len(w) for w in naam.split()), default=0)
    nodig = langste * kleinst * 0.6 + 16
    if nodig > knoop["w"]:
        knoop["x"] -= round((nodig - knoop["w"]) / 2)
        knoop["w"] = round(nodig)
    regels = breek(naam, knoop["w"] - 14, kleinst * 0.6, maximaal=4)
    hoog = len(regels) * kleinst * 1.2 + 14
    if hoog > knoop["h"]:
        knoop["y"] -= round((hoog - knoop["h"]) / 2)
        knoop["h"] = round(hoog)


def duw_uit_elkaar(knoop, marge, rondes=80):
    """De kinderen van een groep uit elkaar schuiven tot er overal een baan tussen past.

    De richting volgt de huidige ligging, zodat de onderlinge volgorde van de plaat blijft staan.
    """
    kinderen = knoop["kinderen"]
    for _ in range(rondes):
        rustig = True
        for i, a in enumerate(kinderen):
            for b in kinderen[i + 1:]:
                over_x = min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"]) + marge
                over_y = min(a["y"] + a["h"], b["y"] + b["h"]) - max(a["y"], b["y"]) + marge
                if over_x <= 0 or over_y <= 0:
                    continue
                rustig = False
                # langs de as waarin de vakken ten opzichte van elkaar liggen, zodat de opzet blijft staan
                naast = abs((a["x"] + a["w"] / 2) - (b["x"] + b["w"] / 2)) / max(a["w"] + b["w"], 1)
                onder = abs((a["y"] + a["h"] / 2) - (b["y"] + b["h"] / 2)) / max(a["h"] + b["h"], 1)
                if naast >= onder:
                    stap = over_x / 2
                    eerst = a if a["x"] + a["w"] / 2 <= b["x"] + b["w"] / 2 else b
                    laatst = b if eerst is a else a
                    eerst["x"] -= stap
                    laatst["x"] += stap
                else:
                    stap = over_y / 2
                    eerst = a if a["y"] + a["h"] / 2 <= b["y"] + b["h"] / 2 else b
                    laatst = b if eerst is a else a
                    eerst["y"] -= stap
                    laatst["y"] += stap
        if rustig:
            return


def ruimer(knoop, fx, fy, diep=0, rand=24, kop=52):
    """De ruimte tussen de kinderen van een groep opentrekken; vakken houden hun eigen maat.

    Een component wordt niet uitgerekt: de diensten erin horen strak bij hun component. Alleen
    groepen en de view zelf krijgen meer lucht, zodat de onderlinge ligging gelijk blijft en er
    ruimte ontstaat voor de banen waarin de lijnen lopen. Daarna schuift alles wat elkaar raakt
    nog net zover uit elkaar dat er een baan tussen past.
    """
    groep = is_groep(knoop)
    for kind in knoop["kinderen"]:
        if groep:
            kind["x"] = round(kind["x"] * fx)
            kind["y"] = round(kind["y"] * fy)
            op_maat(kind)
        ruimer(kind, fx if groep else 1, fy if groep else 1, diep + (1 if groep else 0), rand, kop)
    if groep and knoop["kinderen"]:
        duw_uit_elkaar(knoop, marge=36 if diep == 0 else 22)
        dx = rand - min(k["x"] for k in knoop["kinderen"])
        dy = kop - min(k["y"] for k in knoop["kinderen"])
        for kind in knoop["kinderen"]:
            kind["x"] = round(kind["x"] + dx)
            kind["y"] = round(kind["y"] + dy)
        knoop["w"] = round(max(k["x"] + k["w"] for k in knoop["kinderen"]) + rand)
        knoop["h"] = round(max(k["y"] + k["h"] for k in knoop["kinderen"]) + rand)


def plat(knoop, ox=0, oy=0):
    """Elke knoop met zijn plek op de plaat, in leesvolgorde."""
    knoop["ax"], knoop["ay"] = ox + knoop["x"], oy + knoop["y"]
    uit = [knoop]
    for kind in knoop["kinderen"]:
        uit += plat(kind, knoop["ax"], knoop["ay"])
    return uit


def vak(knoop):
    return dict(x=knoop["ax"], y=knoop["ay"], w=knoop["w"], h=knoop["h"])


# ----------------------------------------------------------------- tekenen --

def esc(s):
    return html.escape(str(s))


def breek(tekst, breedte, teken=BREED, maximaal=3):
    """De tekst over hoogstens `maximaal` regels; wat niet past valt eraf."""
    if not tekst:
        return []
    per_regel = max(int(breedte / teken), 8)
    regels, regel = [], ""
    for woord in str(tekst).split():
        kandidaat = (regel + " " + woord).strip()
        if len(kandidaat) <= per_regel or not regel:
            regel = kandidaat
        else:
            regels.append(regel)
            regel = woord
            if len(regels) == maximaal:
                return regels
    if regel:
        regels.append(regel)
    return regels


def passend(regels_of_tekst, breedte, hoogte, maximaal=15.0, minimaal=8.5):
    """De grootste lettermaat waarbij de naam binnen het vak past, en de regels die daarbij horen."""
    vast = isinstance(regels_of_tekst, list)
    grootte = maximaal
    while grootte >= minimaal:
        regels = regels_of_tekst if vast else breek(regels_of_tekst, breedte, grootte * 0.6,
                                                    maximaal=max(int(hoogte / (grootte * 1.2)), 1))
        heel = vast or " ".join(regels) == " ".join(str(regels_of_tekst).split())
        past_breed = all(len(r) * grootte * 0.6 <= breedte for r in regels)
        if heel and past_breed and len(regels) * grootte * 1.2 <= hoogte:
            return grootte, regels
        grootte -= 0.5
    regels = regels_of_tekst if vast else breek(regels_of_tekst, breedte, minimaal * 0.6,
                                                maximaal=max(int(hoogte / (minimaal * 1.2)), 1))
    return minimaal, regels


def tekstblok(x, y, regels, grootte, kleur, dik=False, midden=True, hoogte=None):
    hoogte = hoogte or grootte * 1.22
    delen = []
    for i, regel in enumerate(regels):
        delen.append(f'<text x="{x:.0f}" y="{y + i * hoogte:.0f}" font-size="{grootte}" '
                     f'{"text-anchor=\"middle\" " if midden else ""}'
                     f'font-weight="{"600" if dik else "400"}" fill="{kleur}">{esc(regel)}</text>')
    return "".join(delen)


def component_svg(knoop, stil):
    vul, rand = ("#f6f8fa", "#c2ccd6") if stil else (COMPONENT_VUL, COMPONENT_RAND)
    kleur = STIL if stil else INKT
    ruimte = max((k["y"] for k in knoop["kinderen"]), default=knoop["h"])
    grootte, regels = passend(knoop["opschrift"] or knoop["naam"], knoop["w"] - 14, ruimte - 8,
                              maximaal=20 if not stil else 17, minimaal=11)
    y = knoop["ay"] + ruimte / 2 + grootte / 2 - (len(regels) - 1) * grootte * 0.6
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="6" fill="{vul}" stroke="{rand}" stroke-width="{1.4 if stil else 2}"/>'
            + tekstblok(knoop["ax"] + knoop["w"] / 2, y, regels, grootte, kleur, dik=not stil))


def dienst_svg(knoop):
    grootte, regels = passend(knoop["opschrift"] or knoop["naam"], knoop["w"] - 10, knoop["h"] - 6,
                              maximaal=15, minimaal=10)
    y = knoop["ay"] + knoop["h"] / 2 + grootte / 2 - (len(regels) - 1) * grootte * 0.6
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="{min(knoop["h"] / 2, 14):.0f}" fill="{DIENST_VUL}" stroke="{DIENST_RAND}"/>'
            + tekstblok(knoop["ax"] + knoop["w"] / 2, y, regels, grootte, INKT, hoogte=grootte * 1.2))


def notitie_svg(knoop):
    grootte, regels = passend(knoop["tekst"] or " ".join(knoop["opschrift"]), knoop["w"] - 16,
                              knoop["h"] - 14, maximaal=15, minimaal=9)
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="4" fill="{NOTITIE_VUL}" stroke="{NOTITIE_RAND}"/>'
            + tekstblok(knoop["ax"] + 8, knoop["ay"] + 8 + grootte, regels, grootte, STIL,
                        midden=False, hoogte=grootte * 1.25))


def junctie_svg(knoop):
    return (f'<circle cx="{knoop["ax"] + knoop["w"] / 2:.0f}" cy="{knoop["ay"] + knoop["h"] / 2:.0f}" '
            f'r="{max(knoop["w"] / 2, 6):.0f}" fill="{STIL}"/>')


def groep_svg(knoop, zone=None):
    if zone:
        vul, rand = ZONE[zone == "rechts"], ZONE_RAND[zone == "rechts"]
        return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
                f'rx="14" fill="{vul}" stroke="{rand}" stroke-width="2"/>'
                f'<text x="{knoop["ax"] + 24:.0f}" y="{knoop["ay"] + 36:.0f}" font-size="26" font-weight="700" '
                f'fill="{INKT}">{esc(" ".join(knoop["opschrift"]) or ZONENAAM[zone])}</text>')
    naam = " ".join(knoop["opschrift"]) or ("" if knoop["naam"] in ("", "Group") else knoop["naam"])
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="8" fill="#ffffff" fill-opacity="0.45" stroke="{GROEP_RAND}" stroke-width="1.4" '
            f'stroke-dasharray="7 5"/>'
            + (f'<text x="{knoop["ax"] + 12:.0f}" y="{knoop["ay"] + 22:.0f}" font-size="16" '
               f'fill="{STIL}">{esc(naam)}</text>' if naam else ""))


def lijn_svg(punten, kleur, merk, stroom=True):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punten)
    if stroom:
        return (f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="7" stroke-opacity="0.9" '
                f'stroke-linejoin="round"/>'
                f'<path d="{d}" fill="none" stroke="{kleur}" stroke-width="2.6" stroke-linejoin="round" '
                f'marker-end="url(#{merk})"/>')
    return (f'<path d="{d}" fill="none" stroke="#b6c2cd" stroke-width="1.4" stroke-dasharray="5 4" '
            f'stroke-linejoin="round"/>')


def naam_svg(punten, tekst, kleur, bezet, doek=None):
    """De naam van een stroom langs haar lijn, op de eerste plek die vrij is.

    Staat de naam op de plaat van Niels al met eigen regelafbreking, dan blijft die staan.
    """
    regels = tekst if isinstance(tekst, list) else breek(tekst, 300, BREED, maximaal=3)
    if not regels:
        return ""
    breedte = max(len(r) for r in regels) * BREED + 14
    hoog = len(regels) * (LETTER + 2) + 8
    benen = sorted(zip(punten, punten[1:]), key=lambda s: -(abs(s[1][0] - s[0][0]) + abs(s[1][1] - s[0][1])))
    for a, b in benen:
        staand = abs(b[0] - a[0]) < abs(b[1] - a[1])
        n = max(int((abs(b[0] - a[0]) + abs(b[1] - a[1])) // 16), 1)
        opzij = (breedte / 2 + 9) if staand else (hoog / 2 + 8)
        plekken = [(kant * opzij, i) for kant in (0, 1, -1) for i in range(n + 1)]
        for kant, i in sorted(plekken, key=lambda p: (abs(p[0]), abs(p[1] - n / 2))):
            f = i / n
            mx = a[0] + (b[0] - a[0]) * f + (kant if staand else 0)
            my = a[1] + (b[1] - a[1]) * f + (0 if staand else kant)
            doos = (mx - breedte / 2, my - hoog / 2, breedte, hoog)
            if doek and not (2 <= doos[0] and doos[0] + breedte <= doek[0] - 2
                             and 2 <= doos[1] and doos[1] + hoog <= doek[1] - 2):
                continue
            if not any(doos[0] < q[0] + q[2] and q[0] < doos[0] + doos[2]
                       and doos[1] < q[1] + q[3] and q[1] < doos[1] + doos[3] for q in bezet):
                bezet.append(doos)
                return (f'<rect x="{doos[0]:.0f}" y="{doos[1]:.0f}" width="{breedte:.0f}" height="{hoog:.0f}" '
                        f'rx="3" fill="#ffffff" fill-opacity="0.93"/>'
                        + tekstblok(mx, doos[1] + LETTER + 2, regels, LETTER, kleur, hoogte=LETTER + 2))
    a, b = benen[0]
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    bezet.append((mx - breedte / 2, my - hoog / 2, breedte, hoog))
    return (f'<rect x="{mx - breedte / 2:.0f}" y="{my - hoog / 2:.0f}" width="{breedte:.0f}" '
            f'height="{hoog:.0f}" rx="3" fill="#ffffff" fill-opacity="0.93"/>'
            + tekstblok(mx, my - hoog / 2 + LETTER + 2, regels, LETTER, kleur, hoogte=LETTER + 2))


# -------------------------------------------------------------------- bouw --

def bouw(ruimte_x=1.55, ruimte_y=1.85, tussen=70, marge=30):
    top, knopen, verbindingen, relaties = lees(MODEL, VIEW)
    labels = labels_van_stromen()

    zones = [k for k in top if is_groep(k)]
    zones.sort(key=lambda k: k["x"])
    losse = [k for k in top if not is_groep(k)]
    for k in zones:
        ruimer(k, ruimte_x, ruimte_y)

    # de twee procesgebieden naast elkaar, de losse notities op een strook eronder
    x = marge
    for k in zones:
        k["x"], k["y"] = x, marge
        x += k["w"] + tussen
    breedte = x - tussen + marge
    hoogte_zones = max(k["h"] for k in zones)
    x = marge
    for k in losse:
        k["x"], k["y"] = x, marge + hoogte_zones + 24
        k["w"], k["h"] = max(k["w"], 300), 104
        x += k["w"] + 20
    hoogte = marge + hoogte_zones + 24 + (104 + marge if losse else marge)

    alles = []
    for k in zones + losse:
        alles += plat(k)
    per_zone = {}
    for i, z in enumerate(zones):
        for k in plat(z):
            per_zone[k["id"]] = "links" if i == 0 else "rechts"

    # de vakken waar een lijn omheen moet: componenten, juncties en notities, niet de groepen
    hindernissen = collections.defaultdict(list)
    vakken = {}
    for k in alles:
        if is_groep(k) or k["ouder"] is None:
            continue
        if k["type"] == "ApplicationService":
            continue
        vakken[k["id"]] = vak(k)
        hindernissen[per_zone.get(k["id"], "los")].append(vakken[k["id"]])

    stromen, verbanden = [], []
    for v in verbindingen:
        soort = relaties.get(v["relatie"], "")
        if v["bron"] not in vakken or v["doel"] not in vakken:
            continue
        if soort == "FlowRelationship":
            stromen.append(dict(v, label=v["opschrift"] or labels.get(v["relatie"], "")))
        elif soort == "AssociationRelationship":
            verbanden.append(v)

    # per zone routeren: eerst de stromen, dan de verbanden, kort voor lang
    def afstand(v):
        a, b = vakken[v["bron"]], vakken[v["doel"]]
        return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"])

    routers = {z: hoofdplaat.Haaks(hindernissen[z]) for z in hindernissen}
    for v in sorted(stromen, key=afstand) + sorted(verbanden, key=afstand):
        zone = per_zone.get(v["bron"], "los")
        v["punten"] = routers[zone].pad(vakken[v["bron"]], vakken[v["doel"]])

    # kleur per bronsysteem
    bronnen = []
    for s in stromen:
        naam = knopen[s["bron"]]["naam"] or "junctie"
        if naam not in bronnen:
            bronnen.append(naam)
    kleuren = {naam: PALET[i % len(PALET)] for i, naam in enumerate(bronnen)}
    # een lijn uit een junctie krijgt de kleur van de lijn die erin komt
    binnen = {s["doel"]: s for s in stromen if knopen[s["doel"]]["type"] == "Junction"}
    for s in stromen:
        if knopen[s["bron"]]["type"] == "Junction" and s["bron"] in binnen:
            kleuren.setdefault(s["bron"], kleuren[knopen[binnen[s["bron"]]["bron"]]["naam"]])
            s["kleur"] = kleuren[s["bron"]]
        else:
            s["kleur"] = kleuren[knopen[s["bron"]]["naam"] or "junctie"]

    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breedte:.0f} {hoogte:.0f}" '
             f'width="{breedte:.0f}" height="{hoogte:.0f}" font-family="Segoe UI, Arial, sans-serif">',
             "<defs>"]
    for i, kleur in enumerate(PALET):
        delen.append(f'<marker id="pijl{i}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5.5" '
                     f'markerHeight="5.5" orient="auto-start-reverse">'
                     f'<path d="M0 0 L10 5 L0 10 z" fill="{kleur}"/></marker>')
    delen += ["</defs>", f'<rect width="{breedte:.0f}" height="{hoogte:.0f}" fill="#ffffff"/>']

    for i, z in enumerate(zones):
        delen.append(groep_svg(z, "links" if i == 0 else "rechts"))
    for k in alles:
        if is_groep(k) and k["ouder"] is not None:
            delen.append(groep_svg(k))

    stil = {k["id"] for k in alles
            if k["type"] == "ApplicationComponent"
            and not any(v["bron"] == k["id"] or v["doel"] == k["id"] for v in stromen)}
    for v in verbanden:
        delen.append(lijn_svg(v["punten"], None, None, stroom=False))
    for s in stromen:
        delen.append(lijn_svg(s["punten"], s["kleur"], f"pijl{PALET.index(s['kleur'])}"))
    for k in alles:
        if is_groep(k):
            continue
        if k["soort"] == "Note":
            delen.append(notitie_svg(k))
        elif k["type"] == "Junction":
            delen.append(junctie_svg(k))
        elif k["type"] == "ApplicationService":
            delen.append(dienst_svg(k))
        elif k["ouder"] is not None:
            delen.append(component_svg(k, k["id"] in stil))

    bezet = [(vk["x"] - 3, vk["y"] - 3, vk["w"] + 6, vk["h"] + 6) for vk in vakken.values()]
    for s in sorted(stromen, key=lambda s: -len(" ".join(s["label"]) if isinstance(s["label"], list)
                                                 else s["label"])):
        delen.append(naam_svg(s["punten"], s["label"], s["kleur"], bezet, (breedte, hoogte)))
    delen.append("</svg>")
    return "".join(delen), stromen, verbanden, [k for k in alles if k["type"] == "ApplicationComponent"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--uit", required=True)
    p.add_argument("--ruimte-x", type=float, default=1.55)
    p.add_argument("--ruimte-y", type=float, default=1.85)
    args = p.parse_args()
    svg, stromen, verbanden, componenten = bouw(args.ruimte_x, args.ruimte_y)
    pathlib.Path(args.uit).write_text(svg, encoding="utf-8")
    haaks = sum(1 for s in stromen for a, b in zip(s["punten"], s["punten"][1:])
                if abs(a[0] - b[0]) > 0.5 and abs(a[1] - b[1]) > 0.5)
    print(f"{len(componenten)} componenten, {len(stromen)} stromen, {len(verbanden)} verbanden; "
          f"{haaks} schuine segmenten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
