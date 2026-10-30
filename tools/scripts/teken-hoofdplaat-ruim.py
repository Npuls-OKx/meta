#!/usr/bin/env python3
"""De hoofdplaat informatiestromen ruimer opgezet en netjes gerouteerd.

Waarom dit script bestaat: hoofdplaat v1.7a vertelt een helder verhaal in twee procesgebieden,
links de onderwijsontwikkeling en rechts de onderwijsuitvoering, met de applicatiecomponenten
die daarin met elkaar praten. Elke informatiestroom blijft binnen haar eigen gebied; daarom
staat een component dat in beide processen meedoet er twee keer op. Dat verhaal blijft hier
overeind: dit script neemt de plaat zoals zij is, houdt elke groep, elk component en elke
dienst op haar eigen plek, en trekt alleen de ruimte ertussen open. Met die ruimte krijgt elke
lijn een eigen baan: recht waar het kan, en anders met een hoek van 90 graden.

De plaat komt uit het model, dus zij loopt mee met elke wijziging van de view. Het model wordt
alleen gelezen; raak nooit een .archimate-bestand aan.

    python3 tools/scripts/teken-hoofdplaat-ruim.py --uit <pad>.svg

Met `--markeer` komt daar een markering over: de plaat vervaagt, de stromen van een casus
worden uitgelicht met wat er overheen gaat, de componenten die meedoen krijgen een omlijning,
en een stroom die de plaat nog niet kent staat als gestippelde lijn.

Een stroom die de plaat wel kent krijgt haar accent in de eerste tekenronde: de stroomlijn zelf
wordt in de accentkleur en dikker getekend, zodat de markering op de pijl van de plaat valt. Een
tweede pad erover komt er niet; dat liep naast de pijl zodra het aanhechtpunt van Archi niet te
herleiden was. Een stroom die de plaat nog niet kent blijft gestippeld, want die heeft geen eerste
lijn om te kleuren; haar baan loopt haaks langs dezelfde router als de plaat zelf. De vormtaal komt
van tools/scripts/teken-hoofdplaat-highlight.py, dat hetzelfde doet over een rasterrender.

    python3 tools/scripts/teken-hoofdplaat-ruim.py --uit <pad>.svg --markeer <casus>.json
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
VIEW = "OKx hoofdplaat v1.7a"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"

INKT = "#1c1c1c"
STIL = "#5b6663"
GROEP_RAND = "#9aa5ae"
ZONE = ("#faf5ee", "#f0f5fa")
ZONE_RAND = ("#e4d8c6", "#d3e0ec")

# Het ArchiMate-kleurenschema per laag: vulkleur, randkleur, tekstkleur, zoals Archi een view
# tekent en zoals tools/scripts/teken-voorbeeldregels.py de platen in deze repository kleurt. Wie in de
# view zelf een kleur meegeeft, houdt die; de rest krijgt de kleur van haar laag.
ARCHIMATE = {
    "Strategy": ("#f5deaa", "#a89460", "#5a4a2a"),
    "Business": ("#ffffb5", "#a8a85a", "#5a5a2a"),
    "Application": ("#b5ffff", "#5aa8a8", "#2a5a5a"),
    "Technology": ("#c9e7b7", "#7aa86a", "#33522a"),
    "Motivation": ("#ccccff", "#7a7ab8", "#33336b"),
    "Overig": ("#ffffff", "#8c9aa6", INKT),
}
LAGEN = (("Business", "Business"), ("Application", "Application"), ("Data", "Application"),
         ("Technology", "Technology"), ("Node", "Technology"), ("Device", "Technology"),
         ("SystemSoftware", "Technology"), ("Artifact", "Technology"), ("Path", "Technology"),
         ("CommunicationNetwork", "Technology"), ("Resource", "Strategy"), ("Capability", "Strategy"),
         ("CourseOfAction", "Strategy"), ("ValueStream", "Strategy"), ("Stakeholder", "Motivation"),
         ("Driver", "Motivation"), ("Assessment", "Motivation"), ("Goal", "Motivation"),
         ("Outcome", "Motivation"), ("Principle", "Motivation"), ("Requirement", "Motivation"),
         ("Constraint", "Motivation"), ("Meaning", "Motivation"), ("Value", "Motivation"))
NOTITIE_VUL = "#fdfbe9"
NOTITIE_RAND = "#d8d4a8"

# een kleur per bronsysteem, zodat te volgen is waar een lijn vandaan komt; donker genoeg
# om ook over een vak van de applicatielaag heen te lezen
PALET = ["#d9531e", "#1f5fd0", "#0d7070", "#6b4bb8", "#2e7d32", "#8a5a12", "#b1268b", "#3a4e63"]

# en een ruimer palet voor de plaat met de koppeling-ID's, waar elk koppelvlak een eigen kleur
# krijgt. De volgorde zet kleuren die op elkaar lijken uit elkaar, zodat twee buren in de
# legenda uit elkaar te houden zijn.
PALET_ID = ["#d9531e", "#1f5fd0", "#2e7d32", "#b1268b", "#a8700a", "#6b4bb8", "#0d7070",
            "#c0392b", "#6e7b1c", "#2a2f8f", "#8a5a12", "#12855f", "#7a2f5e", "#00688c",
            "#b5651d", "#7b3fb8", "#3f7d20", "#9a2b2b", "#4c6272", "#255f85"]
ZONDER_ID = "#93a3ae"   # een lijn die nog geen koppeling-ID draagt

ZONENAAM = {
    "links": "onderwijsontwikkeling · inrichting van nominale- en keuze aanbod",
    "rechts": "onderwijsuitvoering · student studeert en maakt keuzes",
}

LETTER = 15     # de maat van een stroomnaam; de rest van de plaat schaalt hierop mee
BREED = LETTER * 0.55   # geschatte breedte van een teken

# De vormtaal van een markering komt uit teken-hoofdplaat-highlight.py, dat hetzelfde doet over
# een rasterrender: dezelfde accentkleur voor de uitgelichte stroom, dezelfde randkleur om een
# component dat meedoet, en dezelfde witte sluier over de plaat zodat de markering eruit springt.
MARKEER = hoofdplaat.ACCENT
MARKEER_RAND = hoofdplaat.RAND
MARKEER_DIK = 5        # de dikte van een uitgelichte stroomlijn; de gewone stroomlijn is 2,6
SLUIER = 0.62
MARKEER_STROOK = 120   # de ruimte onder de plaat voor de titel en de legenda van een markering


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
                     opschrift=opschrift(c), ouder=ouder, kinderen=[],
                     vul=c.get("fillColor"), lijn=c.get("lineColor"), letter=c.get("fontColor"))
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


# De afkorting per applicatiecomponent, waaruit het voorlopige koppeling-ID wordt opgebouwd.
# Een component zonder afkorting krijgt geen ID; dat is zichtbaar op de plaat en dus bespreekbaar.
AFKORTING = {
    "Onderwijscatalogus": "OC", "Curriculum ontwerptool": "COT", "Planningssysteem": "P",
    "Roostersysteem": "R", "Kernregistratie systeem studenten (KRS)": "KRS",
    "Student volg systeem (SVS)": "SVS", "Leer management systeem (LMS)": "LMS",
    "Student Keuze Systeem (SKS)": "SKS", "Aanmeld systeem": "AMS", "Intake systeem": "INT",
    "Toets- en examen afname systeem": "TEA", "Voorziening Centraal Aanmelden (CAMBO)": "CAMBO",
    "AII (centraal aanmelden)": "AII",
}


def koppeling_id(van, naar):
    """Het voorlopige ID van de koppeling tussen twee componenten: twee afkortingen, catalogus voorop.

    De regel komt uit Public #107: een ID noemt de twee applicatiecomponenten die de koppeling
    verbindt, en beide richtingen vallen onder hetzelfde ID. Zolang de conventie niet vaststaat,
    is dit een werkafspraak, zodat de plaat er alvast mee te lezen is.
    """
    a, b = AFKORTING.get(norm(van)), AFKORTING.get(norm(naar))
    if not a or not b:
        return ""
    return f"{a}-{b}" if a == "OC" or (b != "OC" and a < b) else f"{b}-{a}"


def aanvoer(stromen, knopen):
    """Per junctie de stroom die erin komt; een junctie bundelt een stroom naar meer ontvangers."""
    return {s["doel"]: s for s in stromen if knopen[s["doel"]]["type"] == "Junction"}


def aanvoerbenen(knoopid, knopen, binnen, diepst=4):
    """De benen die naar een junctie toe voeren, van de junctie terug naar haar afzender."""
    uit = []
    while knopen[knoopid]["type"] == "Junction" and knoopid in binnen and len(uit) < diepst:
        uit.append(binnen[knoopid])
        knoopid = binnen[knoopid]["bron"]
    return uit


def zet_koppeling_ids(stromen, knopen):
    """Elke getekende stroom haar koppeling-ID als opschrift geven; geeft de gevonden ID's terug.

    Een junctie bundelt een stroom naar meer ontvangers. De lijnen die de junctie verlaten dragen
    het ID van de afzender ervoor; het aanvoerlijntje ernaartoe blijft onbenoemd, want dat deel
    hoort bij alle ontvangers tegelijk.
    """
    binnen = aanvoer(stromen, knopen)

    def afzender(knoopid):
        benen = aanvoerbenen(knoopid, knopen, binnen)
        eind = benen[-1]["bron"] if benen else knoopid
        return "" if knopen[eind]["type"] == "Junction" else knopen[eind]["naam"]

    gevonden = []
    for s in stromen:
        ident = "" if knopen[s["doel"]]["type"] == "Junction" else koppeling_id(afzender(s["bron"]),
                                                                               knopen[s["doel"]]["naam"])
        s["label"] = ident
        if ident and ident not in gevonden:
            gevonden.append(ident)
    return gevonden


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


def laag(type_):
    """De ArchiMate-laag van een elementsoort; die bepaalt haar kleur."""
    for kop, naam in LAGEN:
        if type_.startswith(kop):
            return naam
    return "Overig"


def donkerder(kleur, factor=0.62):
    """De randkleur die Archi van een vulkleur afleidt: dezelfde kleur, een stuk donkerder."""
    r, g, b = (int(kleur[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % tuple(round(c * factor) for c in (r, g, b))


def kleuren(knoop):
    """Vul-, rand- en tekstkleur van een vak: die van de view, en anders die van haar ArchiMate-laag.

    Zo houdt de plaat de keuzes die Niels zelf maakte, zoals een wit vak voor een component dat
    buiten het verhaal staat, en krijgt al het andere de kleur die Archi eraan geeft.
    """
    vul_laag, rand_laag, tekst_laag = ARCHIMATE[laag(knoop["type"])]
    vul = knoop["vul"] or vul_laag
    rand = knoop["lijn"] or (rand_laag if vul == vul_laag else donkerder(vul))
    return vul, rand, knoop["letter"] or tekst_laag


def merk_svg(x, y, vul, rand):
    """Het ArchiMate-merkteken van een applicatiecomponent, rechtsboven in het vak."""
    return (f'<g transform="translate({x - 24:.0f},{y + 7:.0f})" fill="{vul}" stroke="{rand}" '
            f'stroke-width="1.2"><rect x="4" y="1" width="11" height="13"/>'
            f'<rect x="0" y="3.5" width="6" height="3"/><rect x="0" y="8.5" width="6" height="3"/></g>')


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


def component_svg(knoop):
    vul, rand, kleur = kleuren(knoop)
    ruimte = max((k["y"] for k in knoop["kinderen"]), default=knoop["h"])
    grootte, regels = passend(knoop["opschrift"] or knoop["naam"], knoop["w"] - 34, ruimte - 8,
                              maximaal=20, minimaal=11)
    y = knoop["ay"] + ruimte / 2 + grootte / 2 - (len(regels) - 1) * grootte * 0.6
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="4" fill="{vul}" stroke="{rand}" stroke-width="1.6"/>'
            + merk_svg(knoop["ax"] + knoop["w"], knoop["ay"], vul, rand)
            + tekstblok(knoop["ax"] + knoop["w"] / 2, y, regels, grootte, kleur, dik=True))


def dienst_svg(knoop):
    vul, rand, kleur = kleuren(knoop)
    grootte, regels = passend(knoop["opschrift"] or knoop["naam"], knoop["w"] - 10, knoop["h"] - 6,
                              maximaal=15, minimaal=10)
    y = knoop["ay"] + knoop["h"] / 2 + grootte / 2 - (len(regels) - 1) * grootte * 0.6
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="{min(knoop["h"] / 2, 14):.0f}" fill="{vul}" stroke="{rand}"/>'
            + tekstblok(knoop["ax"] + knoop["w"] / 2, y, regels, grootte, kleur, hoogte=grootte * 1.2))


def notitie_svg(knoop):
    vul = knoop["vul"] if knoop["vul"] and knoop["vul"] != "#ffffff" else NOTITIE_VUL
    grootte, regels = passend(knoop["tekst"] or " ".join(knoop["opschrift"]), knoop["w"] - 16,
                              knoop["h"] - 14, maximaal=15, minimaal=9)
    return (f'<rect x="{knoop["ax"]:.0f}" y="{knoop["ay"]:.0f}" width="{knoop["w"]}" height="{knoop["h"]}" '
            f'rx="4" fill="{vul}" stroke="{knoop["lijn"] or donkerder(vul, 0.78)}"/>'
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


def lijn_svg(punten, kleur, merk, stroom=True, dik=False):
    """De lijn van een stroom of een verband: een pad, met een witte onderlaag zodat zij overal leest.

    Met `dik` krijgt de lijn de dikte van een markering. Zo staat een uitgelichte stroom er in deze
    ene tekenronde al in haar accentkleur, en komt er geen tweede pad overheen.
    """
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punten)
    if stroom:
        breed, onder = (MARKEER_DIK, 11) if dik else (2.6, 7)
        return (f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="{onder}" '
                f'stroke-opacity="0.9" stroke-linejoin="round"/>'
                f'<path d="{d}" fill="none" stroke="{kleur}" stroke-width="{breed}" stroke-linejoin="round" '
                f'marker-end="url(#{merk})"/>')
    return (f'<path d="{d}" fill="none" stroke="#b6c2cd" stroke-width="1.4" stroke-dasharray="5 4" '
            f'stroke-linejoin="round"/>')


def naam_svg(punten, tekst, kleur, bezet, doek=None, maat=LETTER, omlijnd=False):
    """De naam van een stroom langs haar lijn, op de eerste plek die vrij is.

    Staat de naam op de plaat van Niels al met eigen regelafbreking, dan blijft die staan. Een
    koppeling-ID is kort en krijgt een omlijnd plaatje, zodat het op de plaat te tellen is.
    """
    regels = tekst if isinstance(tekst, list) else breek(tekst, 300, maat * 0.55, maximaal=3)
    if not regels:
        return ""
    breedte = max(len(r) for r in regels) * maat * 0.55 + (20 if omlijnd else 14)
    hoog = len(regels) * (maat + 2) + (10 if omlijnd else 8)
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
                return _plaatje(doos, mx, regels, maat, kleur, omlijnd)
    a, b = benen[0]
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    doos = (mx - breedte / 2, my - hoog / 2, breedte, hoog)
    bezet.append(doos)
    return _plaatje(doos, mx, regels, maat, kleur, omlijnd)


def _plaatje(doos, mx, regels, maat, kleur, omlijnd):
    """Het witte vakje met de naam of het ID erin, op de gekozen plek."""
    rand = f' stroke="{kleur}" stroke-width="1.4"' if omlijnd else ""
    return (f'<rect x="{doos[0]:.0f}" y="{doos[1]:.0f}" width="{doos[2]:.0f}" height="{doos[3]:.0f}" '
            f'rx="{5 if omlijnd else 3}" fill="#ffffff" fill-opacity="{0.98 if omlijnd else 0.93}"{rand}/>'
            + tekstblok(mx, doos[1] + maat + (5 if omlijnd else 2), regels, maat, kleur,
                        dik=omlijnd, hoogte=maat + 2))


def legenda_hoogte(aantal, kolommen=6, regel=38, kop=42, rand=18):
    """Hoeveel ruimte de legenda onder de plaat nodig heeft."""
    if not aantal:
        return 0
    return kop + regel * -(-aantal // kolommen) + rand


def legenda_svg(rijen, x, y, breedte, kolommen=6, regel=38, kop=42):
    """De koppeling-ID's onder de plaat: per ID haar kleur en het aantal informatiestromen.

    Waarvoor: op de plaat staat per lijn welk ID erover loopt, maar niet hoeveel stromen er
    onder een ID vallen. Die telling is de vraag die bij het voorstel hoort, dus zij hoort
    naast de plaat te staan en niet in een apart bestand.
    """
    if not rijen:
        return ""
    totaal = sum(a for _, _, a in rijen)
    delen = [f'<text x="{x:.0f}" y="{y + 23:.0f}" font-size="23" font-weight="700" fill="{INKT}">'
             f'{len(rijen)} voorlopige koppeling-ID\u0027s, samen {totaal} informatiestromen</text>']
    vak = breedte / kolommen
    # de telling staat in een eigen kolom, zodat een lang ID er niet overheen loopt
    naast = 54 + max(len(i) for i, _, _ in rijen) * 18 + 18
    for i, (ident, kleur, aantal) in enumerate(rijen):
        kx = x + (i % kolommen) * vak
        ky = y + kop + (i // kolommen) * regel + regel / 2
        delen.append(f'<path d="M{kx:.0f},{ky:.0f} L{kx + 42:.0f},{ky:.0f}" stroke="{kleur}" '
                     f'stroke-width="4" fill="none"/>')
        delen.append(f'<text x="{kx + 54:.0f}" y="{ky + 8:.0f}" font-size="22" font-weight="700" '
                     f'fill="{kleur}">{esc(ident)}</text>')
        delen.append(f'<text x="{kx + naast:.0f}" y="{ky + 8:.0f}" '
                     f'font-size="18" fill="{STIL}">{aantal} '
                     f'{"stroom" if aantal == 1 else "stromen"}</text>')
    return "".join(delen)


# --------------------------------------------------------------- markeren --

def lees_markering(pad):
    """De stromen van een casus uit een eigen bestand, naast het model.

    Waarvoor: welke lijnen een casus raakt en wat er overheen gaat, staat niet in het model.
    Dat hoort bij de casus en blijft daarom een eigen bestand naast de specificatie. Per stroom:
    `van` en `naar` met de componentnaam van de view, `label` met wat er overheen gaat,
    `op_de_plaat` dat zegt of de hoofdplaat de lijn al kent, en `stroom` met het ID van de
    stroomrelatie in het model. Dat ID wijst de lijn aan waar een paar componenten meer stromen
    deelt; zonder dat ID telt het paar vakken.

    Met `ontvangergroep` ligt de ontvangst bij een groep op de plaat in plaats van bij een vak.
    De lijn loopt dan nog steeds naar het vak dat `naar` noemt, en de omlijning komt om elk vak
    in die groep: het Student Informatie Systeem is de kernregistratie en het studentvolgsysteem
    samen, en RIO/CAMBO/AII draagt vier vakken. Wie een van die vakken aansluit, krijgt dezelfde
    informatie, dus hoort de markering ze alle te laten zien.
    """
    gegeven = json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    uit = [dict(van=norm(s["van"]), naar=norm(s["naar"]), label=norm(s.get("label", "")),
                op_de_plaat=bool(s.get("op_de_plaat", True)), stroom=norm(s.get("stroom", "")),
                ontvangergroep=norm(s.get("ontvangergroep", "")))
           for s in gegeven.get("stromen", [])]
    return norm(gegeven.get("naam", "")), uit


def vakken_van_relatie(stromen, knopen, relatie):
    """Het vakkenpaar dat de genoemde stroomrelatie verbindt, of niets.

    Waarvoor: een component staat soms twee keer op de plaat, links in de ontwerpzone en rechts
    in de uitvoeringszone, en dan bestaat dezelfde koppeling er twee keer. Het dichtstbijzijnde
    paar is dan niet het goede paar: de catalogus en de leeromgeving liggen rechts dicht bij
    elkaar, terwijl de lijn die een casus bedoelt links onder het ontwerpblok loopt. Noemt de
    casus het ID van de stroomrelatie, dan wijst dat ID de vakken aan.
    """
    if not relatie:
        return None, None
    been = next((s for s in stromen if s.get("relatie") == relatie), None)
    if been is None:
        return None, None
    b = knopen.get(been["doel"])
    if not b or b["type"] != "ApplicationComponent":
        return None, None
    # Een junctie bundelt een stroom naar meer ontvangers; de afzender ligt dan een been terug.
    bron = been["bron"]
    for _ in range(4):
        knoop = knopen.get(bron)
        if knoop and knoop["type"] == "ApplicationComponent":
            return knoop, b
        vorige = next((s for s in stromen if s["doel"] == bron), None)
        if vorige is None:
            return None, None
        bron = vorige["bron"]
    return None, None


def dichtste_vakken(componenten, van, naar, nabij=None, groepen=None):
    """Het paar vakken dat het dichtst bij elkaar ligt; een component staat soms twee keer op de plaat.

    Een stroom die de plaat nog niet kent, draagt geen relatie-ID, en dan is er niets dat de
    juiste helft aanwijst. Een casus waarvan de andere stromen rechts in de uitvoeringszone
    liggen, krijgt haar voorgestelde stroom anders links getekend, los van de rest. Met `nabij`
    telt de afstand tot die eerder geplaatste vakken mee, zodat de voorgestelde stroom bij zijn
    buren blijft.
    """
    links = [k for k in componenten if norm(k["naam"]) == norm(van)]
    rechts = [k for k in componenten if norm(k["naam"]) == norm(naar)]
    if not links or not rechts:
        return None, None

    def midden(k):
        return (k["ax"] + k["w"] / 2, k["ay"] + k["h"] / 2)


    def zone(k):
        return next((g["id"] for g in (groepen or [])
                     if g["ax"] <= midden(k)[0] <= g["ax"] + g["w"]
                     and g["ay"] <= midden(k)[1] <= g["ay"] + g["h"]), None)

    buren = [zone(k) for k in (nabij or [])]
    buren = [z for z in buren if z is not None]
    helft = max(set(buren), key=buren.count) if buren else None

    def afstand(ab):
        a, b = ab
        anders = sum(1 for k in (a, b) if helft is not None and zone(k) != helft)
        return (anders, (midden(a)[0] - midden(b)[0]) ** 2 + (midden(a)[1] - midden(b)[1]) ** 2)

    return min(((a, b) for a in links for b in rechts if a is not b), key=afstand)


def benen_naar(knoopid, stromen, knopen, doel, diep=0):
    """De benen die een junctie verlaten tot bij de ontvanger; niets als de stroom daar niet uitkomt."""
    if knoopid == doel:
        return []
    if knopen[knoopid]["type"] != "Junction" or diep >= 4:
        return None
    for s in stromen:
        if s["bron"] != knoopid:
            continue
        verder = benen_naar(s["doel"], stromen, knopen, doel, diep + 1)
        if verder is not None:
            return [s] + verder
    return None


def markeerpad(stromen, knopen, a, b, relatie=""):
    """De benen van de plaat die samen de stroom van vak a naar vak b vormen, de afzender eerst.

    Waarvoor: een markering hoort op de lijn te liggen die de plaat al tekent. Daarvoor moet zij
    weten welke benen dat zijn. Een junctie bundelt een stroom naar meer ontvangers, en dan bestaat
    het pad uit de aanvoer naar de junctie plus het been dat bij de ontvanger uitkomt. Noemt de
    casus het ID van de stroomrelatie, dan wijst dat ID de lijn aan; anders telt het paar vakken.
    Geeft een lege lijst als de plaat deze stroom niet kent.
    """
    binnen = aanvoer(stromen, knopen)
    anker = next((s for s in stromen if s["relatie"] == relatie), None) if relatie else None
    if anker:
        verder = benen_naar(anker["doel"], stromen, knopen, b["id"])
        if verder is not None:
            return aanvoerbenen(anker["bron"], knopen, binnen)[::-1] + [anker] + verder
    for s in stromen:
        if s["doel"] != b["id"]:
            continue
        heen = aanvoerbenen(s["bron"], knopen, binnen)
        if (heen[-1]["bron"] if heen else s["bron"]) == a["id"]:
            return heen[::-1] + [s]
    return []


def vakken_in_groep(knopen, naam, binnen=None):
    """Elk componentvak binnen de groep met deze naam waarin het ontvangende vak ligt.

    Een groep staat twee keer op de plaat, links in de ontwerpzone en rechts in de
    uitvoeringszone. Zonder `binnen` zouden beide exemplaren een omlijning krijgen, en dan
    markeert een casus een zone waar zij niet over gaat. Met `binnen` telt de groep waarin het
    ontvangende vak werkelijk ligt.
    """
    uit, gezien = [], set()

    def verzamel(knoop):
        for kind in knoop["kinderen"]:
            if kind["soort"] == "Group":
                verzamel(kind)
            elif kind.get("naam") and kind["id"] not in gezien:
                gezien.add(kind["id"])
                uit.append(kind)

    if binnen is not None:
        knoop = knopen.get(binnen)
        while knoop is not None:
            if knoop["soort"] == "Group" and norm(knoop.get("naam", "")) == norm(naam):
                verzamel(knoop)
                return uit
            knoop = knoop.get("ouder")
        return []

    for knoop in knopen.values():
        if knoop["soort"] == "Group" and norm(knoop.get("naam", "")) == norm(naam):
            verzamel(knoop)
    return uit


def markeer_stromen(markeringen, stromen, knopen, componenten):
    """Elke markering naast de plaat leggen; geeft terug wat uitgelicht wordt en wat ontbreekt.

    Drie uitkomsten: de markeringen met hun vakkenpaar en de benen die zij uitlichten, de
    markeringen waarvoor de plaat geen lijn heeft, en de meldingen voor wie meeleest. Zegt het
    bestand dat de plaat de lijn kent terwijl zij die niet heeft, dan staat dat in de meldingen
    en wordt de stroom gestippeld getekend: de plaat laat zien wat zij werkelijk heeft.
    """
    # De twee panelen van de plaat, als rechthoek: de grootste groepen die naast elkaar liggen.
    panelen = sorted((k for k in knopen.values()
                      if isinstance(k, dict) and not k.get("type")
                      and k.get("w") and k.get("h")),
                     key=lambda g: g["w"] * g["h"], reverse=True)[:2]
    raakt, zonder, ontbreekt, mee = [], [], [], []
    # De vakken die een stroom met een relatie-ID al aanwees, sturen de stromen die de plaat
    # nog niet kent naar dezelfde helft van de plaat.
    geplaatst = []
    for m in sorted(markeringen, key=lambda m: not m.get("stroom")):
        a, b = vakken_van_relatie(stromen, knopen, m.get("stroom", ""))
        if a is None or b is None:
            a, b = dichtste_vakken(componenten, m["van"], m["naar"], geplaatst, panelen)
        if a is None or b is None:
            ontbreekt.append(f"{m['label'] or 'stroom'}: {m['van']} naar {m['naar']} is niet op de "
                             f"plaat te plaatsen")
            continue
        if m.get("ontvangergroep"):
            leden = vakken_in_groep(knopen, m["ontvangergroep"], b["id"])
            if leden:
                mee.extend(leden)
            else:
                ontbreekt.append(f"{m['label'] or 'stroom'}: de groep {m['ontvangergroep']} staat "
                                 f"niet op de plaat")
        geplaatst.extend([a, b])
        benen = markeerpad(stromen, knopen, a, b, m.get("stroom", "")) if m["op_de_plaat"] else []
        if benen:
            raakt.append((m, a, b, benen))
            continue
        zonder.append((m, a, b))
        if m["op_de_plaat"]:
            ontbreekt.append(f"{m['label'] or 'stroom'}: {m['van']} naar {m['naar']} staat in het "
                             f"bestand als lijn die de plaat kent, de plaat heeft deze stroom niet")
    return raakt, zonder, ontbreekt, mee


def markeerlijn_svg(punten):
    """Een stroom die de plaat nog niet kent: een gestippelde accentlijn met een witte onderlaag.

    Zichtbaar wat er ontbreekt. Een stroom die de plaat wel kent krijgt haar accent in de eerste
    tekenronde, van `lijn_svg` met `dik`, en heeft dit tweede pad dus niet nodig.
    """
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punten)
    return (f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="11" stroke-opacity="0.9" '
            f'stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{MARKEER}" stroke-width="{MARKEER_DIK}" '
            f'stroke-dasharray="16 11" stroke-linejoin="round" marker-end="url(#markeerpunt)"/>')


def markeer_legenda_svg(naam, x, y, breedte):
    """De titel van de markering en de drie tekens die zij gebruikt, in de plaat zelf.

    Waarvoor: een plaat die in een specificatie landt wordt los van haar tekst gelezen. Wie
    de legenda in het document zet, levert een plaat die zonder dat document niet te lezen is.
    """
    uitleg = (("lijn", "stroom van deze casus, met wat er overheen gaat"),
              ("stippel", "stroom die deze hoofdplaat nog niet kent"),
              ("rand", "component dat meedoet"))
    delen = [f'<text x="{x:.0f}" y="{y + 30:.0f}" font-size="28" font-weight="700" '
             f'fill="{INKT}">{esc(naam)}</text>'] if naam else []
    vak = breedte / len(uitleg)
    for i, (soort, wat) in enumerate(uitleg):
        kx, ky = x + i * vak, y + 78
        if soort == "rand":
            delen.append(f'<rect x="{kx:.0f}" y="{ky - 14:.0f}" width="48" height="28" fill="none" '
                         f'stroke="{MARKEER_RAND}" stroke-width="4" rx="4"/>')
        else:
            streep = ' stroke-dasharray="16 11"' if soort == "stippel" else ""
            delen.append(f'<path d="M{kx:.0f},{ky:.0f} L{kx + 52:.0f},{ky:.0f}" stroke="{MARKEER}" '
                         f'stroke-width="{MARKEER_DIK}" fill="none"{streep}/>')
        delen.append(f'<text x="{kx + 68:.0f}" y="{ky + 9:.0f}" font-size="22" '
                     f'fill="{STIL}">{esc(wat)}</text>')
    return "".join(delen)


def markeer_svg(raakt, zonder, per_zone, routers, vakken, bezet, doek, mee=()):
    """Wat er over de vervaagde plaat heen komt: de ontbrekende stromen, de omlijning en de namen.

    De stromen die de plaat kent staan hier al in de accentkleur: die kregen hun kleur en dikte in
    de eerste tekenronde, op de lijn van de plaat zelf. Wat de plaat nog niet kent krijgt hier een
    eigen baan, gestippeld en haaks: de router kent de vakken en de banen die de plaat al bezet
    houdt, dus die baan loopt er netjes naast. Daarna de omlijning om elk component dat meedoet, en
    bovenop de namen, zodat zij over de lijnen heen leesbaar blijven.

    `mee` draagt de overige vakken van een ontvangende groep. Die krijgen dezelfde omlijning als
    de afzender en de ontvanger, want zij nemen dezelfde informatie af; de lijn blijft lopen naar
    het vak dat de markering noemt.
    """
    uitgelicht = [(m, [p for been in benen for p in been["punten"]], True)
                  for m, a, b, benen in raakt]
    delen, omlijnd = [], {}
    for m, a, b in zonder:
        router = routers.get(per_zone.get(a["id"], "los")) or next(iter(routers.values()), None)
        va, vb = vakken[a["id"]], vakken[b["id"]]
        punten = router.pad(va, vb) if router else hoofdplaat.haaks_pad(va, vb)
        delen.append(markeerlijn_svg(punten))
        uitgelicht.append((m, punten, False))
    for rij in list(raakt) + list(zonder):
        for k in (rij[1], rij[2]):
            omlijnd.setdefault(k["id"], k)
    # De overige vakken van een ontvangende groep: wie daarop aansluit krijgt dezelfde informatie.
    for k in mee:
        omlijnd.setdefault(k["id"], k)
    for k in omlijnd.values():
        delen.append(f'<rect x="{k["ax"] - 4:.0f}" y="{k["ay"] - 4:.0f}" width="{k["w"] + 8}" '
                     f'height="{k["h"] + 8}" fill="none" stroke="{MARKEER_RAND}" stroke-width="4" rx="5"/>')
    for _, punten, _ in uitgelicht:
        bezet += hoofdplaat.lijnvakken(punten, dikte=10)
    # de namen bovenop, zodat zij over de markeringen heen leesbaar blijven
    for m, punten, bekend in uitgelicht:
        # De onderbroken lijn en de legenda zeggen al dat de plaat deze stroom niet kent;
        # datzelfde in het etiket herhalen maakt het etiket breder dan de ruimte ernaast.
        label = m["label"]
        delen.append(naam_svg(punten, label, MARKEER, bezet, doek, maat=LETTER + 3, omlijnd=True))
    return delen


# -------------------------------------------------------------------- bouw --

def bouw(ruimte_x=1.55, ruimte_y=1.85, tussen=70, marge=30, opschriften="namen", markeer=(),
         markeer_naam=""):
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
    idents = zet_koppeling_ids(stromen, knopen) if opschriften == "ids" else []

    # per zone routeren: eerst de stromen, dan de verbanden, kort voor lang
    def afstand(v):
        a, b = vakken[v["bron"]], vakken[v["doel"]]
        return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"])

    volgorde = sorted(stromen, key=afstand) + sorted(verbanden, key=afstand)
    paren = collections.defaultdict(list)
    for v in volgorde:
        paren[per_zone.get(v["bron"], "los")].append((vakken[v["bron"]], vakken[v["doel"]]))
    # de router kent alle lijnen voordat zij er een tekent, zodat de aanhechtingen per vak
    # op volgorde van hun overkant staan en twee lijnen elkaar niet hoeven te passeren
    routers = {z: hoofdplaat.Haaks(hindernissen[z], paren[z]) for z in hindernissen}
    for v in volgorde:
        zone = per_zone.get(v["bron"], "los")
        v["punten"] = routers[zone].pad(vakken[v["bron"]], vakken[v["doel"]])

    if idents:
        # elk koppelvlak zijn eigen kleur, zodat de lijnen van een ID bij elkaar horen
        kleur_van_id = {i: PALET_ID[n % len(PALET_ID)] for n, i in enumerate(sorted(idents))}
        for s in stromen:
            s["kleur"] = kleur_van_id.get(s["label"], ZONDER_ID)
        telling = collections.Counter(s["label"] for s in stromen if s["label"])
        legenda = [(i, kleur_van_id[i], telling[i]) for i in sorted(telling)]
    else:
        # kleur per bronsysteem
        legenda = []
        bronnen = []
        for s in stromen:
            naam = knopen[s["bron"]]["naam"] or "junctie"
            if naam not in bronnen:
                bronnen.append(naam)
        kleuren = {naam: PALET[i % len(PALET)] for i, naam in enumerate(bronnen)}
        # een lijn uit een junctie krijgt de kleur van de lijn die erin komt
        binnen = aanvoer(stromen, knopen)
        for s in stromen:
            if knopen[s["bron"]]["type"] == "Junction" and s["bron"] in binnen:
                kleuren.setdefault(s["bron"], kleuren[knopen[binnen[s["bron"]]["bron"]]["naam"]])
                s["kleur"] = kleuren[s["bron"]]
            else:
                s["kleur"] = kleuren[knopen[s["bron"]]["naam"] or "junctie"]

    # de markeringen bij de lijnen van de plaat zoeken: een stroom die zij raakt krijgt hieronder
    # haar accentkleur mee in dezelfde tekenronde als alle andere stromen
    raakt, zonder, ontbreekt, meegemarkeerd = [], [], [], []
    if markeer:
        raakt, zonder, ontbreekt, meegemarkeerd = markeer_stromen(
            markeer, stromen, knopen, [k for k in alles if k["type"] == "ApplicationComponent"])
        for _, _, _, benen in raakt:
            for been in benen:
                been["markeer"], been["kleur"] = True, MARKEER

    onderkant = hoogte + legenda_hoogte(len(legenda)) + (MARKEER_STROOK if markeer else 0)
    gebruikt = list(dict.fromkeys(s["kleur"] for s in stromen))
    merk = {kleur: f"pijl{i}" for i, kleur in enumerate(gebruikt)}
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breedte:.0f} {onderkant:.0f}" '
             f'width="{breedte:.0f}" height="{onderkant:.0f}" font-family="Segoe UI, Arial, sans-serif">',
             "<defs>"]
    for kleur, naam in merk.items():
        delen.append(f'<marker id="{naam}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5.5" '
                     f'markerHeight="5.5" orient="auto-start-reverse">'
                     f'<path d="M0 0 L10 5 L0 10 z" fill="{kleur}"/></marker>')
    if markeer:
        delen.append(f'<marker id="markeerpunt" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" '
                     f'markerHeight="5" orient="auto-start-reverse">'
                     f'<path d="M0 0 L10 5 L0 10 z" fill="{MARKEER}"/></marker>')
    delen += ["</defs>", f'<rect width="{breedte:.0f}" height="{onderkant:.0f}" fill="#ffffff"/>']

    for i, z in enumerate(zones):
        delen.append(groep_svg(z, "links" if i == 0 else "rechts"))
    for k in alles:
        if is_groep(k) and k["ouder"] is not None:
            delen.append(groep_svg(k))

    for v in verbanden:
        delen.append(lijn_svg(v["punten"], None, None, stroom=False))
    # een gemarkeerde stroom wordt hier in de accentkleur en dikker getekend, en gaat straks over de
    # sluier heen; zo valt de markering op de lijn van de plaat zelf
    accentlijnen = []
    for s in stromen:
        lijn = lijn_svg(s["punten"], s["kleur"], merk[s["kleur"]], dik=s.get("markeer", False))
        (accentlijnen if s.get("markeer") else delen).append(lijn)
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
            delen.append(component_svg(k))

    bezet = [(vk["x"] - 3, vk["y"] - 3, vk["w"] + 6, vk["h"] + 6) for vk in vakken.values()]
    # de titelstrook van een groepering blijft vrij, anders landt een opschrift op haar naam
    bezet += [(k["ax"], k["ay"], k["w"], 46 if k["ouder"] is None else 26)
              for k in alles if is_groep(k)]
    for s in sorted(stromen, key=lambda s: -len(" ".join(s["label"]) if isinstance(s["label"], list)
                                                 else s["label"])):
        # een gemarkeerde stroom draagt de naam van haar markering, die verderop wordt gezet
        if s.get("markeer"):
            continue
        delen.append(naam_svg(s["punten"], s["label"], s["kleur"], bezet, (breedte, hoogte),
                              maat=LETTER + 5 if opschriften == "ids" else LETTER,
                              omlijnd=opschriften == "ids"))
    if markeer:
        # de plaat vervaagt, zodat de markering eruit springt; daarna de uitgelichte stromen erover
        delen.append(f'<rect x="0" y="0" width="{breedte:.0f}" height="{hoogte:.0f}" fill="#ffffff" '
                     f'fill-opacity="{SLUIER}"/>')
        delen += accentlijnen
        delen += markeer_svg(raakt, zonder, per_zone, routers, vakken, bezet,
                             (breedte, hoogte), meegemarkeerd)
        delen.append(markeer_legenda_svg(markeer_naam, marge, hoogte - marge / 2, breedte - 2 * marge))
    delen.append(legenda_svg(legenda, marge, hoogte - marge / 2, breedte - 2 * marge))
    delen.append("</svg>")
    return ("".join(delen), stromen, verbanden,
            [k for k in alles if k["type"] == "ApplicationComponent"], legenda, ontbreekt,
            dict(gekleurd=len(raakt), gestippeld=len(zonder)))


def kruisingen(lijnen):
    """Hoe vaak twee lijnen elkaar kruisen; de maat voor hoe goed de plaat leest."""
    liggend, staand = [], []
    for lijn in lijnen:
        for (x1, y1), (x2, y2) in zip(lijn, lijn[1:]):
            if abs(y1 - y2) < 0.5 and abs(x1 - x2) > 0.5:
                liggend.append((y1, min(x1, x2), max(x1, x2), id(lijn)))
            elif abs(x1 - x2) < 0.5 and abs(y1 - y2) > 0.5:
                staand.append((x1, min(y1, y2), max(y1, y2), id(lijn)))
    return sum(1 for y, van, tot, a in liggend for x, boven, onder, b in staand
               if a != b and van + 0.5 < x < tot - 0.5 and boven + 0.5 < y < onder - 0.5)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--uit", required=True)
    p.add_argument("--ruimte-x", type=float, default=1.55)
    p.add_argument("--ruimte-y", type=float, default=1.85)
    p.add_argument("--opschriften", choices=("namen", "ids"), default="namen",
                   help="namen: de stroomnamen van de plaat; ids: het voorlopige koppeling-ID per stroom")
    p.add_argument("--markeer", type=pathlib.Path,
                   help="bestand met de stromen van een casus; markeert die op de plaat")
    args = p.parse_args()
    naam, markeringen = lees_markering(args.markeer) if args.markeer else ("", ())
    svg, stromen, verbanden, componenten, legenda, ontbreekt, gemarkeerd = bouw(
        args.ruimte_x, args.ruimte_y, opschriften=args.opschriften,
        markeer=markeringen, markeer_naam=naam)
    pathlib.Path(args.uit).write_text(svg, encoding="utf-8")
    for x in ontbreekt:
        print(f"waarschuwing: {x}", file=sys.stderr)
    haaks = sum(1 for s in stromen for a, b in zip(s["punten"], s["punten"][1:])
                if abs(a[0] - b[0]) > 0.5 and abs(a[1] - b[1]) > 0.5)
    kruis = kruisingen([v["punten"] for v in stromen + verbanden])
    erbij = (f", {sum(a for _, _, a in legenda)} stromen onder {len(legenda)} koppeling-ID's"
             if legenda else "")
    if markeringen:
        erbij += (f", {gemarkeerd['gekleurd'] + gemarkeerd['gestippeld']} gemarkeerde stromen "
                  f"waarvan {gemarkeerd['gestippeld']} gestippeld")
    print(f"{len(componenten)} componenten, {len(stromen)} stromen, {len(verbanden)} verbanden; "
          f"{haaks} schuine segmenten, {kruis} kruisingen{erbij}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
