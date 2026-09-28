#!/usr/bin/env python3
"""Een voorstel voor de hoofdplaat informatiestromen, getekend als banenplaat.

Waarom dit script bestaat: hoofdplaat v1.7 zet de systemen neer zoals het gesprek liep, en de
informatiestromen zoeken daar hun weg tussendoor. Dat leest moeilijk: lijnen komen schuin aan,
kruisen elkaar en vallen samen. Deze plaat pakt dezelfde systemen en dezelfde stromen, zet de
systemen op een rij in de volgorde van het verhaal (specificatie, planning, roostering, keuze,
verbintenis, uitvoering, resultaat) en geeft elke stroom een eigen baan boven of onder die rij.
Elke lijn loopt daardoor recht, raakt haaks aan, en valt nergens samen met een andere lijn.

De inhoud komt uit het model: de systemen en de stromen worden gelezen uit de view en uit
stromen.json, en het script controleert of elk applicatiecomponent en elke stroom van de
hoofdplaat een plek heeft gekregen. Het model wordt alleen gelezen; raak nooit een
.archimate-bestand aan.

    python3 scripts/teken-stromen-voorstel.py --uit <pad>.svg
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
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"

# ---------------------------------------------------------------- huisstijl --

INKT = "#12314f"
STIL = "#5b7288"
VAKRAND = "#2a6ebb"
VAKVUL = "#e9f4fb"
DIENSTRAND = "#8fc2e0"
DIENSTVUL = "#f6fbfe"
STILRAND = "#c3ced8"
STILVUL = "#f4f6f8"
GROEPRAND = "#b9c6d2"
BAND_ONTWIKKELING = "#f7f3ec"
BAND_UITVOERING = "#f1f6fa"

# een kleur per bron, zodat te volgen is waar een lijn vandaan komt
KLEUR = {
    "OC": "#d9531e", "P": "#1f6feb", "R": "#0f8a8a", "SKS": "#6b4bb8",
    "KRS": "#2e7d32", "LMS": "#8a5a12", "SVS": "#4a6572", "CAMBO": "#b1268b",
    "EDUHUB": "#7a7f45", "TEP": "#4a6572", "TEA": "#4a6572",
}

# ------------------------------------------------------------------ indeling --

KOLOMMEN = [
    dict(id="bron", naam="bronnen", breedte=232),
    dict(id="oc", naam="catalogus", breedte=244),
    dict(id="p", naam="planning", breedte=322),
    dict(id="r", naam="roostering", breedte=222),
    dict(id="sks", naam="keuze", breedte=366),
    dict(id="krs", naam="verbintenis", breedte=262),
    dict(id="svs", naam="volgen", breedte=232),
    dict(id="lms", naam="uitvoering", breedte=244),
]

# de vakken in de hoofdrij; `deel` verdeelt een kolom over meerdere vakken (van, tot in delen van de rij)
HOOFDRIJ = [
    dict(id="COT", kolom="bron", naam="Curriculum ontwerptool", deel=(0.0, 0.44),
         diensten=["Nominale route meerjaar uitwerking"]),
    dict(id="OPC", kolom="bron", naam="Onderwijsprogrammacatalogus", deel=(0.50, 0.72)),
    dict(id="EDUHUB", kolom="bron", naam="EduHub", deel=(0.78, 1.0)),
    dict(id="OC", kolom="oc", naam="Onderwijscatalogus", deel=(0.0, 1.0), stage="catalogus",
         diensten=["Onderwijsspecificatie uitwerking"]),
    dict(id="P", kolom="p", naam="Planningssysteem", deel=(0.0, 1.0), stage="planning",
         diensten=["(meer) jaar capaciteit planning", "Jaarplanning",
                   "Nominale route schooljaar", "Periode planning"]),
    dict(id="R", kolom="r", naam="Roostersysteem", deel=(0.0, 1.0), stage="roostering"),
    dict(id="SKS", kolom="sks", naam="Student Keuze Systeem (SKS)", deel=(0.0, 1.0), stage="keuze",
         diensten=["Keuze op opleidingseenheid", "Keuze op leergelegenheid",
                   "Keuze op lesgelegenheid", "Accorderen van keuzes"],
         bij="meerdere SKS'en mogelijk"),
    dict(id="KRS", kolom="krs", naam="Kernregistratie systeem studenten (KRS)", deel=(0.0, 1.0), stage="verbintenis",
         diensten=["Inschrijving op opleidingsprogramma"]),
    dict(id="SVS", kolom="svs", naam="Student volg systeem (SVS)", deel=(0.0, 1.0), stage="volgen"),
    dict(id="LMS", kolom="lms", naam="Leer management systeem (LMS)", deel=(0.0, 1.0), stage="uitvoering",
         bij="meerdere LMS'en mogelijk"),
]

# de systemen zonder informatiestroom: context, in een band boven of onder de rij
BOVENBAND = [
    dict(id="PERS", naam="Personeel systeem", kolom="p", rij=0, kant=0.00, breedte=112),
    dict(id="FAC", naam="Faciliteiten beheer systeem", kolom="p", rij=0, kant=0.345, breedte=112),
    dict(id="MID", naam="Middelen planning", kolom="p", rij=0, kant=0.69, breedte=112),
    dict(id="PVI", naam="Plan van inzet systeem", kolom="p", rij=1, kant=0.17, breedte=210),
    dict(id="PROG", naam="Prognose systeem", kolom="p", rij=1, kant=-0.52, breedte=160),
    dict(id="AWR", naam="Aanwezigheidregistratie systeem", kolom="r", rij=0, kant=0.0, breedte=160),
    dict(id="SCS", naam="Student communicatie systeem", kolom="r", rij=1, kant=0.0, breedte=160),
    dict(id="BI", naam="Business intelligence", kolom="sks", rij=0, kant=0.62, breedte=160),
]

ONDERBAND = [
    dict(id="CAMBO", naam="Voorziening Centraal Aanmelden (CAMBO)", kolom="p", rij=0, kant=0.00, breedte=196),
    dict(id="AMS", naam="Aanmeld systeem", kolom="p", rij=0, kant=0.62, breedte=122),
    dict(id="RIO", naam="Register Instellingen en Opleidingen (RIO)", kolom="p", rij=1, kant=0.00, breedte=196),
    dict(id="INT", naam="Intake systeem", kolom="p", rij=1, kant=0.62, breedte=122),
    dict(id="STUDENT", naam="Student", kolom="r", rij=0, kant=0.0, breedte=222, soort="actor"),
    dict(id="IAM", naam="Identity en accessmanagement systeem (IAM)", kolom="sks", rij=0, kant=0.0, breedte=366),
    dict(id="SBS", naam="Student begeleiding systeem", kolom="sks", rij=1, kant=0.0, breedte=366),
    dict(id="FIN", naam="Financieel systeem", kolom="krs", rij=0, kant=0.0, breedte=262),
    dict(id="CML", naam="Commercieel maatwerk / LLO oplossing", kolom="krs", rij=1, kant=0.0, breedte=262),
    dict(id="TEP", naam="Toets- en examenplanning- en inschrijfsysteem", kolom="svs", rij=0, kant=0.0, breedte=232),
    dict(id="TEA", naam="Toets- en examen afname systeem", kolom="svs", rij=1, kant=0.0, breedte=232),
]

# de groeperingen van de hoofdplaat, als kader om een of meer kolommen
GROEPEN = [
    dict(naam="Planning elementen", vakken=["PERS", "FAC", "MID", "PVI"]),
    dict(naam="Student Informatie Systeem", kolommen=["krs", "svs"]),
    dict(naam="RIO / CAMBO / AII", vakken=["CAMBO", "AMS", "RIO", "INT"]),
    dict(naam="Toets- en examen", vakken=["TEP", "TEA"]),
]

# de verbanden zonder informatiestroom: dun en gestippeld, want context
VERBANDEN = [
    ("COT", "OC"), ("OPC", "OC"), ("PROG", "P"), ("PVI", "P"),
    ("PERS", "PVI"), ("FAC", "PVI"), ("MID", "PVI"),
    ("AWR", "R"), ("SCS", "R"), ("SCS", "SKS"), ("BI", "SKS"), ("BI", "OC"),
    ("IAM", "SKS"), ("IAM", "KRS"), ("SBS", "SKS"), ("SBS", "SVS"),
    ("CML", "FIN"), ("TEA", "LMS"),
]

NOTITIES = [
    "Deze plaat zet dezelfde systemen en dezelfde stromen als hoofdplaat v1.7 op een rij in de "
    "volgorde van het verhaal. Elk systeem staat een keer; de catalogus, de kernregistratie en het "
    "studentvolgsysteem stonden op v1.7 twee keer omdat zij in beide processen meedoen.",
    "Elke stroom heeft een eigen baan boven of onder de rij, met de naam erbij. Lijnen lopen recht, "
    "raken haaks aan en vallen nergens samen; een kruising is altijd een rechte hoek.",
    "Open punten van v1.7 blijven staan: hoeveel niet-onderwijsspecificatie in de catalogus hoort, "
    "of EduHub concreet aanbod kent, en hoe tijdigheid tussen keuze en roostering loopt.",
]

# ---------------------------------------------------------------- afmetingen --

MARGE = 46
GAT = 78
BAAN = 42            # afstand tussen twee banen, ruim genoeg voor een naam van twee regels
RIJHOOGTE = 192      # hoogte van de hoofdrij
BANDRIJ = 52         # hoogte van een rij in de contextband
TITELHOOGTE = 58
NOTITIEHOOGTE = 86
STUBSTAP = 30        # afstand tussen twee aanhechtingen op dezelfde zijde
TEKEN = 5.85         # geschatte breedte van een teken bij 11,5 px


def norm(s):
    return " ".join(str(s or "").split())


# ------------------------------------------------------------- model inlezen --

def lees_stromen():
    """De informatiestromen van de hoofdplaat, met de junctions uitgewerkt naar losse lijnen."""
    knopen, connecties, elems = hoofdplaat.lees_geometrie(MODEL)
    boom = ET.parse(MODEL)
    relaties = {e.get("id"): (e.get(XSI, ""), e.get("name", "")) for e in boom.iter() if e.get("id")}
    labels = {s["id"]: s.get("label", "") for s in json.loads(STROMEN.read_text(encoding="utf-8"))["stromen"]}

    def naam_van(kid):
        return norm(elems.get(knopen.get(kid, {}).get("element", ""), ("", ""))[1])

    junctions = {kid for kid in knopen if naam_van(kid) == "Junction"}
    flows = [c for c in connecties if relaties.get(c["relatie"], ("", ""))[0].endswith("FlowRelationship")]
    binnen = collections.defaultdict(list)
    for c in flows:
        if c["doel"] in junctions:
            binnen[c["doel"]].append(c)
    uit = []
    for c in flows:
        if c["doel"] in junctions:
            continue
        if c["bron"] in junctions:
            for aanvoer in binnen[c["bron"]]:
                uit.append((naam_van(aanvoer["bron"]), naam_van(c["doel"]), labels.get(aanvoer["relatie"], "")))
        else:
            uit.append((naam_van(c["bron"]), naam_van(c["doel"]), labels.get(c["relatie"], "")))
    componenten = {naam_van(kid) for kid, k in knopen.items()
                   if elems.get(k.get("element", ""), ("", ""))[0].endswith("ApplicationComponent")}
    return uit, componenten


NAAR_ID = {
    "Onderwijscatalogus": "OC", "Curriculum ontwerptool": "COT", "Onderwijsprogrammacatalogus": "OPC",
    "Planningssysteem": "P", "Roostersysteem": "R", "Student Keuze Systeem (SKS)": "SKS",
    "Kernregistratie systeem studenten (KRS)": "KRS", "Student volg systeem (SVS)": "SVS",
    "Leer management systeem (LMS)": "LMS", "Voorziening Centraal Aanmelden (CAMBO)": "CAMBO",
    "EduHub": "EDUHUB", "Aanmeld systeem": "AMS", "Intake systeem": "INT",
    "Register Instellingen en Opleidingen (RIO)": "RIO", "Commercieel maatwerk / LLO oplossing": "CML",
    "Financieel systeem": "FIN", "Identity en accessmanagement systeem (IAM)": "IAM",
    "Student begeleiding systeem": "SBS", "Prognose systeem": "PROG", "Plan van inzet systeem": "PVI",
    "Personeel systeem": "PERS", "Faciliteiten beheer systeem": "FAC", "Middelen planning": "MID",
    "Aanwezigheidregistratie systeem": "AWR", "Student communicatie systeem": "SCS",
    "Business intelligence": "BI", "Toets- en examen afname systeem": "TEA",
    "Toets- en examenplanning- en inschrijfsysteem": "TEP",
}


# ------------------------------------------------------------------ indeling --

def plaats_kolommen():
    x, uit = MARGE, {}
    for kolom in KOLOMMEN:
        uit[kolom["id"]] = dict(x=x, breedte=kolom["breedte"], naam=kolom["naam"])
        x += kolom["breedte"] + GAT
    return uit, x - GAT + MARGE


def hoogte_van(vak):
    regels = 1 + (len(vak.get("diensten", [])) + 1) // 2
    return 30 + regels * 26


def bouw_vakken(kolommen, y_rij):
    """Elk vak van de hoofdrij op zijn plek, en de contextbanden eromheen."""
    vakken = {}
    for vak in HOOFDRIJ:
        kolom = kolommen[vak["kolom"]]
        van, tot = vak["deel"]
        y = y_rij + van * RIJHOOGTE
        h = (tot - van) * RIJHOOGTE
        vakken[vak["id"]] = dict(vak, x=kolom["x"], y=y, w=kolom["breedte"], h=h, band="rij", vlak="rij")
    return vakken


def bouw_band(kolommen, vakken, lijst, y_start, richting):
    for vak in lijst:
        kolom = kolommen[vak["kolom"]]
        y = y_start + richting * vak["rij"] * BANDRIJ
        if richting < 0:
            y -= BANDRIJ - 12
        vakken[vak["id"]] = dict(vak, x=kolom["x"] + vak["kant"] * kolom["breedte"],
                                 y=y, w=vak["breedte"], h=BANDRIJ - 14, band="context",
                                 vlak="bovenband" if richting < 0 or vak in BOVENBAND else "onderband")
    return vakken


# ------------------------------------------------------------------- banen ----

def kolomindex(vakken, vid, kolommen):
    return list(kolommen).index(next(v["kolom"] for v in HOOFDRIJ + BOVENBAND + ONDERBAND if v["id"] == vid))


def kies_banen(stromen, vakken, kolommen):
    """Elke stroom een eigen baan; stromen die elkaar niet raken delen er een.

    Korte stromen eerst, zodat zij dicht bij de rij komen te liggen en de lange stromen
    buitenom lopen. Zo kruist een aanhechting zo weinig mogelijk banen.
    """
    indexen = {vid: i for i, vid in enumerate(kolommen)}
    def spanne(s):
        a = indexen[vakken[s["van"]]["kolom"]]
        b = indexen[vakken[s["naar"]]["kolom"]]
        return (min(a, b), max(a, b))
    for s in stromen:
        s["span"] = spanne(s)
    per_band = collections.defaultdict(list)
    for s in sorted(stromen, key=lambda s: (s["span"][1] - s["span"][0], s["span"][0])):
        bezet = per_band[s["band"]]
        for baan in range(60):
            botst = any(min(t["span"][1], s["span"][1]) >= max(t["span"][0], s["span"][0])
                        for t in bezet if t["baan"] == baan)
            if not botst:
                s["baan"] = baan
                break
        bezet.append(s)
    boven = max([s["baan"] for s in stromen if s["band"] == "boven"], default=-1) + 1
    onder = max([s["baan"] for s in stromen if s["band"] == "onder"], default=-1) + 1
    return boven, onder


def kies_aanhechting(stromen, vakken):
    """Per vakzijde de aanhechtingen verdelen, gesorteerd op de kant waar de lijn heen gaat."""
    zijden = collections.defaultdict(list)
    for s in stromen:
        zijden[(s["van"], "boven" if s["band"] == "boven" else "onder")].append((s, "uit"))
        zijden[(s["naar"], "boven" if s["band"] == "boven" else "onder")].append((s, "in"))
    for (vid, zijde), rij in zijden.items():
        vak = vakken[vid]
        def sleutel(paar):
            s, rol = paar
            ander = vakken[s["naar"] if rol == "uit" else s["van"]]
            return ander["x"] + ander["w"] / 2
        rij.sort(key=sleutel)
        ruimte = min(STUBSTAP, (vak["w"] - 40) / max(len(rij) - 1, 1))
        start = vak["x"] + vak["w"] / 2 - ruimte * (len(rij) - 1) / 2
        for i, (s, rol) in enumerate(rij):
            s["x_" + rol] = start + i * ruimte


# -------------------------------------------------------------------- tekst ---

def breek(tekst, breedte, teken=TEKEN):
    """De naam van een stroom over hoogstens twee regels, passend binnen de baan."""
    if not tekst:
        return []
    per_regel = max(int(breedte / teken), 12)
    woorden, regels, regel = tekst.split(), [], ""
    for woord in woorden:
        kandidaat = (regel + " " + woord).strip()
        if len(kandidaat) <= per_regel or not regel:
            regel = kandidaat
        else:
            regels.append(regel)
            regel = woord
        if len(regels) == 2:
            break
    if len(regels) < 2 and regel:
        regels.append(regel)
    if len(regels) == 2 and " ".join(regels) != tekst:
        rest = tekst[len(" ".join(regels)):].strip()
        if rest:
            regels[1] = regels[1][:max(per_regel - 2, 4)].rstrip() + "..."
    return regels


def esc(s):
    return html.escape(str(s))


# ---------------------------------------------------------------------- svg ---

def vak_svg(vak):
    if vak.get("soort") == "actor":
        return (f'<rect x="{vak["x"]:.0f}" y="{vak["y"]:.0f}" width="{vak["w"]:.0f}" height="{vak["h"]:.0f}" '
                f'rx="16" fill="{STILVUL}" stroke="{STILRAND}" stroke-width="1.6"/>'
                f'<text x="{vak["x"] + vak["w"] / 2:.0f}" y="{vak["y"] + vak["h"] / 2 + 5:.0f}" '
                f'text-anchor="middle" font-size="13" fill="{STIL}">{esc(vak["naam"])}</text>')
    stil = vak["band"] == "context"
    vul, rand, kleur = (STILVUL, STILRAND, STIL) if stil else (VAKVUL, VAKRAND, INKT)
    delen = [f'<rect x="{vak["x"]:.0f}" y="{vak["y"]:.0f}" width="{vak["w"]:.0f}" height="{vak["h"]:.0f}" '
             f'rx="7" fill="{vul}" stroke="{rand}" stroke-width="{1.4 if stil else 2.2}"/>']
    grootte = 12 if stil else 14.5
    factor = 0.53 if stil else 0.62
    regels = breek(vak["naam"], vak["w"] - 16, grootte * factor)
    langste = max((len(r) for r in regels), default=1)
    grootte = min(grootte, (vak["w"] - 16) / (langste * factor))   # een lang woord past zo altijd
    diensthoog = 0
    if vak.get("diensten"):
        kolommen_d = 2 if len(vak["diensten"]) > 1 else 1
        diensthoog = 26 * ((len(vak["diensten"]) + kolommen_d - 1) // kolommen_d) + 8
    if vak.get("stage"):
        delen.append(f'<text x="{vak["x"] + 10:.0f}" y="{vak["y"] + 16:.0f}" font-size="9.5" '
                     f'font-weight="700" letter-spacing="1.1" fill="{STIL}">{esc(vak["stage"].upper())}</text>')
    midden = vak["y"] + (vak["h"] - diensthoog) / 2 + 5 + (5 if vak.get("stage") else 0)
    y = midden if len(regels) == 1 else midden - 8
    for regel in regels:
        delen.append(f'<text x="{vak["x"] + vak["w"] / 2:.0f}" y="{y:.0f}" text-anchor="middle" '
                     f'font-size="{grootte}" font-weight="{"400" if stil else "700"}" '
                     f'fill="{kleur}">{esc(regel)}</text>')
        y += 15
    diensten = vak.get("diensten", [])
    if diensten:
        kolommen = 2 if len(diensten) > 1 else 1
        bd = (vak["w"] - 16 - (kolommen - 1) * 8) / kolommen
        top = vak["y"] + vak["h"] - 26 * ((len(diensten) + kolommen - 1) // kolommen) - 8
        for i, dienst in enumerate(diensten):
            dx = vak["x"] + 8 + (i % kolommen) * (bd + 8)
            dy = top + (i // kolommen) * 26
            delen.append(f'<rect x="{dx:.0f}" y="{dy:.0f}" width="{bd:.0f}" height="22" rx="11" '
                         f'fill="{DIENSTVUL}" stroke="{DIENSTRAND}"/>')
            kort = dienst if len(dienst) * 5.2 < bd - 10 else dienst[:int((bd - 14) / 5.2)].rstrip() + "..."
            delen.append(f'<text x="{dx + bd / 2:.0f}" y="{dy + 15:.0f}" text-anchor="middle" '
                         f'font-size="10.5" fill="{INKT}">{esc(kort)}</text>')
    if vak.get("bij"):
        delen.append(f'<text x="{vak["x"] + vak["w"] / 2:.0f}" y="{y + 2:.0f}" text-anchor="middle" '
                     f'font-size="10" font-style="italic" fill="{STIL}">{esc(vak["bij"])}</text>')
    return "".join(delen)


def rand_naar_baan(vak, band):
    """De zijde van een vak die naar de banenband kijkt: een vak in de onderband hecht aan zijn bovenkant."""
    if vak["vlak"] == "bovenband":
        return vak["y"] + vak["h"]
    if vak["vlak"] == "onderband":
        return vak["y"]
    return vak["y"] if band == "boven" else vak["y"] + vak["h"]


def recht_tussen(bron, doel):
    """Twee vakken die vlak boven of naast elkaar staan: een rechte lijn ertussen, zonder baan."""
    if bron["vlak"] == "rij" or doel["vlak"] == "rij":
        return None
    deel = min(bron["x"] + bron["w"], doel["x"] + doel["w"]) - max(bron["x"], doel["x"])
    if deel < 40:
        return None
    if bron["y"] > doel["y"]:
        bron, doel = doel, bron
        keer = True
    else:
        keer = False
    x = (max(bron["x"], doel["x"]) + min(bron["x"] + bron["w"], doel["x"] + doel["w"])) / 2
    punten = [(x, bron["y"] + bron["h"]), (x, doel["y"])]
    return list(reversed(punten)) if keer else punten


def stroom_svg(s, vakken, y_baan):
    kleur = KLEUR.get(s["van"], "#4a6572")
    bron, doel = vakken[s["van"]], vakken[s["naar"]]
    ya = rand_naar_baan(bron, s["band"])
    yb = rand_naar_baan(doel, s["band"])
    punten = recht_tussen(bron, doel)
    if punten:
        punten = [(punten[0][0] + (12 if s.get("kant") else -12), punten[0][1]),
                  (punten[1][0] + (12 if s.get("kant") else -12), punten[1][1])]
    else:
        punten = [(s["x_uit"], ya), (s["x_uit"], y_baan), (s["x_in"], y_baan), (s["x_in"], yb)]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punten)
    return (f'<path d="{d}" fill="none" stroke="{kleur}" stroke-width="2.6" stroke-linejoin="round" '
            f'marker-end="url(#punt-{s["van"]})"/>')


def label_svg(s, y_baan, bezet=()):
    regels = breek(s["label"], abs(s["x_in"] - s["x_uit"]) - 24)
    if not regels:
        return ""
    kleur = KLEUR.get(s["van"], "#4a6572")
    breedte = max(len(r) for r in regels) * TEKEN + 14
    hoog = len(regels) * 13 + 6
    top = y_baan - 6 - hoog
    laag, hoogst = sorted((s["x_uit"], s["x_in"]))
    mx = (laag + hoogst) / 2
    for stap in range(0, 26):
        for kant in ((0,) if stap == 0 else (1, -1)):
            kandidaat = mx + kant * stap * 18
            speling = max(breedte / 2 - (hoogst - laag) / 2 + 30, 10)
            if not (laag + breedte / 2 - speling <= kandidaat <= hoogst - breedte / 2 + speling):
                continue
            vak = (kandidaat - breedte / 2, top, breedte, hoog)
            if not any(vak[0] < b[0] + b[2] and b[0] < vak[0] + vak[2]
                       and vak[1] < b[1] + b[3] and b[1] < vak[1] + vak[3] for b in bezet):
                mx = kandidaat
                stap = 99
                break
        if stap == 99:
            break
    if isinstance(bezet, list):
        bezet.append((mx - breedte / 2, top, breedte, hoog))
    delen = [f'<rect x="{mx - breedte / 2:.0f}" y="{top:.0f}" width="{breedte:.0f}" height="{hoog:.0f}" '
             f'rx="3" fill="#ffffff" fill-opacity="0.92"/>']
    for i, regel in enumerate(regels):
        delen.append(f'<text x="{mx:.0f}" y="{top + 12 + i * 13:.0f}" text-anchor="middle" '
                     f'font-size="11" fill="{kleur}">{esc(regel)}</text>')
    return "".join(delen)


def verband_svg(a, b, wijk=0):
    """Een dun gestippeld verband tussen twee vakken: context, geen informatiestroom.

    Ook hier geldt de regel van de plaat: recht waar het kan, en anders een enkele hoek van 90 graden.
    """
    ax1, ay1, ax2, ay2 = a["x"], a["y"], a["x"] + a["w"], a["y"] + a["h"]
    bx1, by1, bx2, by2 = b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]
    deel_x = min(ax2, bx2) - max(ax1, bx1)
    deel_y = min(ay2, by2) - max(ay1, by1)
    if deel_x >= 24:
        x = (max(ax1, bx1) + min(ax2, bx2)) / 2
        y1, y2 = (ay2, by1) if by1 > ay2 else (ay1, by2)
        d = f"M{x:.0f},{y1:.0f} L{x:.0f},{y2:.0f}"
    elif deel_y >= 18:
        y = (max(ay1, by1) + min(ay2, by2)) / 2
        x1, x2 = (ax2, bx1) if bx1 > ax2 else (ax1, bx2)
        d = f"M{x1:.0f},{y:.0f} L{x2:.0f},{y:.0f}"
    else:
        # geen overlap: langs de strook naast de contextband, zodat de lijn geen vak raakt
        x = (ax1 + ax2) / 2
        xb = (bx1 + bx2) / 2
        omhoog = (by1 + by2) / 2 < (ay1 + ay2) / 2
        y1, yb = (ay1, by2) if omhoog else (ay2, by1)
        y = (ay1 - 16 - 6 * wijk) if omhoog else (ay2 + 16 + 6 * wijk)
        d = f"M{x:.0f},{y1:.0f} L{x:.0f},{y:.0f} L{xb:.0f},{y:.0f} L{xb:.0f},{yb:.0f}"
    return f'<path d="{d}" fill="none" stroke="{STILRAND}" stroke-width="1.5" stroke-dasharray="4 4"/>'


def groep_svg(naam, vakken_in, lucht=14):
    x1 = min(v["x"] for v in vakken_in) - lucht
    y1 = min(v["y"] for v in vakken_in) - lucht - 12
    x2 = max(v["x"] + v["w"] for v in vakken_in) + lucht
    y2 = max(v["y"] + v["h"] for v in vakken_in) + lucht
    return (f'<rect x="{x1:.0f}" y="{y1:.0f}" width="{x2 - x1:.0f}" height="{y2 - y1:.0f}" rx="6" '
            f'fill="none" stroke="{GROEPRAND}" stroke-width="1.4" stroke-dasharray="7 5"/>'
            f'<text x="{x1 + 8:.0f}" y="{y1 + 13:.0f}" font-size="11" fill="{STIL}">{esc(naam)}</text>')


# --------------------------------------------------------------------- bouw ---

def bouw():
    ruwe, componenten = lees_stromen()
    kolommen, breedte = plaats_kolommen()

    stromen = []
    onbekend = set()
    for van, naar, label in ruwe:
        a, b = NAAR_ID.get(van), NAAR_ID.get(naar)
        if not a or not b:
            onbekend.add(van if not a else naar)
            continue
        stromen.append(dict(van=a, naar=b, label=label))

    # een stroom loopt boven de rij als zij naar rechts gaat tussen twee vakken van de hoofdrij;
    # alles met een vak uit de onderband loopt onder
    in_rij = {v["id"] for v in HOOFDRIJ}
    volgorde = {k["id"]: i for i, k in enumerate(KOLOMMEN)}
    onder_ids = {v["id"] for v in ONDERBAND}
    plek = {v["id"]: v["kolom"] for v in HOOFDRIJ + BOVENBAND + ONDERBAND}
    for s in stromen:
        naar_onder = s["van"] in onder_ids or s["naar"] in onder_ids or s["van"] == "EDUHUB" or s["naar"] == "EDUHUB"
        vooruit = volgorde[plek[s["naar"]]] > volgorde[plek[s["van"]]]
        s["band"] = "onder" if (naar_onder or not vooruit) else "boven"

    # hoogtes: eerst de banen tellen, dan pas de y-posities vastleggen
    tel_vakken = {}
    for vak in HOOFDRIJ + BOVENBAND + ONDERBAND:
        tel_vakken[vak["id"]] = dict(vak, kolom=vak["kolom"])
    boven_banen, onder_banen = kies_banen(stromen, tel_vakken, [k["id"] for k in KOLOMMEN])

    y_boven_band = TITELHOOGTE
    hoog_bovenband = 2 * BANDRIJ
    y_banen_boven = y_boven_band + hoog_bovenband + 34
    y_rij = y_banen_boven + boven_banen * BAAN + 18
    y_banen_onder = y_rij + RIJHOOGTE + 22
    y_onderband = y_banen_onder + onder_banen * BAAN + 34
    hoog_onderband = 2 * BANDRIJ
    hoogte = y_onderband + hoog_onderband + NOTITIEHOOGTE + MARGE

    vakken = bouw_vakken(kolommen, y_rij)
    bouw_band(kolommen, vakken, BOVENBAND, y_boven_band, +1)
    bouw_band(kolommen, vakken, ONDERBAND, y_onderband + BANDRIJ - 12, +1)
    kies_aanhechting(stromen, vakken)

    def y_van(s):
        return (y_rij - 18 - s["baan"] * BAAN) if s["band"] == "boven" \
            else (y_rij + RIJHOOGTE + 22 + s["baan"] * BAAN)

    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breedte:.0f} {hoogte:.0f}" '
             f'width="{breedte:.0f}" height="{hoogte:.0f}" font-family="Segoe UI, Arial, sans-serif">']
    delen.append("<defs>")
    for sleutel, kleur in KLEUR.items():
        delen.append(f'<marker id="punt-{sleutel}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5.5" '
                     f'markerHeight="5.5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" '
                     f'fill="{kleur}"/></marker>')
    delen.append("</defs>")
    delen.append(f'<rect width="{breedte:.0f}" height="{hoogte:.0f}" fill="#ffffff"/>')

    # de twee zones van de hoofdplaat, als rustige achtergrond
    grens = kolommen["sks"]["x"] - GAT / 2
    zone_top, zone_hoog = y_boven_band - 24, hoogte - NOTITIEHOOGTE - y_boven_band + 12
    for x1, x2, kleur, naam in ((MARGE - 16, grens, BAND_ONTWIKKELING,
                                 "(onderwijsontwikkeling) inrichting van nominale- en keuze aanbod"),
                                (grens, breedte - MARGE + 16, BAND_UITVOERING,
                                 "(onderwijsuitvoering) student studeert en maakt keuzes")):
        delen.append(f'<rect x="{x1:.0f}" y="{zone_top:.0f}" width="{x2 - x1:.0f}" height="{zone_hoog:.0f}" '
                     f'rx="10" fill="{kleur}"/>')
        delen.append(f'<text x="{x1 + 14:.0f}" y="{zone_top + 20:.0f}" font-size="13" font-weight="600" '
                     f'fill="{STIL}">{esc(naam)}</text>')

    for groep in GROEPEN:
        leden = [vakken[v] for v in groep.get("vakken", [])]
        for kid in groep.get("kolommen", []):
            leden += [v for v in vakken.values() if v.get("kolom") == kid and v["band"] == "rij"]
        delen.append(groep_svg(groep["naam"], leden))

    for i, (a, b) in enumerate(VERBANDEN):
        delen.append(verband_svg(vakken[a], vakken[b], i % 5))

    gezien = set()
    for s in stromen:
        paar = tuple(sorted((s["van"], s["naar"])))
        s["kant"] = paar in gezien
        gezien.add(paar)
    for s in stromen:
        delen.append(stroom_svg(s, vakken, y_van(s)))
    for vak in vakken.values():
        delen.append(vak_svg(vak))
    genomen = [(v["x"] - 4, v["y"] - 4, v["w"] + 8, v["h"] + 8) for v in vakken.values()]
    for s in sorted(stromen, key=lambda s: -abs(s["x_in"] - s["x_uit"])):
        delen.append(label_svg(s, y_van(s), genomen))

    # een regel bovenaan; de titel staat op de slide of in het bericht waar de plaat in landt
    delen.append(f'<text x="{MARGE - 16:.0f}" y="26" font-size="15" font-weight="600" fill="{INKT}">'
                 f'{len(stromen)} informatiestromen uit hoofdplaat v1.7, elk in een eigen baan; '
                 f'kleur per bronsysteem</text>')
    ny = hoogte - NOTITIEHOOGTE + 8
    kolombreedte = (breedte - 2 * MARGE) / 3
    for i, notitie in enumerate(NOTITIES):
        x = MARGE - 16 + i * kolombreedte
        delen.append(f'<rect x="{x:.0f}" y="{ny:.0f}" width="{kolombreedte - 18:.0f}" height="{NOTITIEHOOGTE - 28:.0f}" '
                     f'rx="6" fill="#fbfaf6" stroke="{STILRAND}" stroke-width="1.2"/>')
        for j, regel in enumerate(breek_meer(notitie, kolombreedte - 38, 4)):
            delen.append(f'<text x="{x + 10:.0f}" y="{ny + 18 + j * 14:.0f}" font-size="11" '
                         f'fill="{STIL}">{esc(regel)}</text>')
    delen.append("</svg>")

    gemist = sorted(componenten - {v for v in NAAR_ID if NAAR_ID[v] in vakken})
    return "".join(delen), stromen, gemist, sorted(onbekend), (boven_banen, onder_banen)


def breek_meer(tekst, breedte, maximaal):
    per_regel = max(int(breedte / TEKEN), 12)
    regels, regel = [], ""
    for woord in tekst.split():
        kandidaat = (regel + " " + woord).strip()
        if len(kandidaat) <= per_regel or not regel:
            regel = kandidaat
        else:
            regels.append(regel)
            regel = woord
            if len(regels) == maximaal:
                return regels
    if regel and len(regels) < maximaal:
        regels.append(regel)
    return regels


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--uit", required=True, help="pad van het svg-bestand")
    args = p.parse_args()
    svg, stromen, gemist, onbekend, banen = bouw()
    pathlib.Path(args.uit).write_text(svg, encoding="utf-8")
    print(f"{len(stromen)} stromen, {banen[0]} banen boven en {banen[1]} onder de rij")
    for naam in onbekend:
        print(f"geen plek voor: {naam}", file=sys.stderr)
    for naam in gemist:
        print(f"component van de hoofdplaat mist op het voorstel: {naam}", file=sys.stderr)
    return 1 if onbekend or gemist else 0


if __name__ == "__main__":
    sys.exit(main())
