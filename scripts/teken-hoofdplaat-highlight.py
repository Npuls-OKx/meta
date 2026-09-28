#!/usr/bin/env python3
"""Per fase de informatiestromen van het voorbeeld markeren op de hoofdplaat.

Waarom dit script bestaat: een stroombeeld toont twee componenten en de objecten die
tussen hen bewegen, maar niet waar die lijn op de hoofdplaat loopt. Dit script legt
over een render van hoofdplaat v1.7 een markering per stroom die het voorbeeld in die
fase raakt, met het beeld-ID erbij, en omlijnt de betrokken componenten. Een stroom
die de plaat nog niet kent, staat als gestippelde lijn tussen de twee componenten:
zichtbaar wat er ontbreekt.

    python3 scripts/teken-hoofdplaat-highlight.py --plaat img/hoofdplaat.png

Het model wordt alleen gelezen; raak nooit een .archimate-bestand aan.
"""

import argparse
import base64
import collections
import html
import importlib.util
import itertools
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("platen", WORTEL / "exporteer-archimate-platen.py")
platen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(platen)

MODEL = pathlib.Path("architecture/model/model.archimate")
REGELS = pathlib.Path("architecture/model/informatiemodel/voorbeeld-lr1-regels.json")
STROMEN = pathlib.Path("architecture/model/informatiemodel/stromen.json")
UITMAP = pathlib.Path("architecture/model/informatiemodel/img/hoofdplaat")
PLAAT = UITMAP / "hoofdplaat-v1.7.jpg"
VIEW = "OKx hoofdplaat v1.7<concept>"
GEEN_PIJL = "geen pijl op de hoofdplaat"
MARGE = 10  # Archi rendert de view met tien pixels marge; met dezelfde marge vallen de markeringen op de pijlen
ACCENT = "#d9531e"
RAND = "#1f6feb"


def norm(s):
    return " ".join(str(s or "").split())


def stromen_per_fase(regels):
    """Per fase de stromen: (van, naar, pijl) met de beeld-ID's die haar gebruiken."""
    uit = collections.OrderedDict()
    for r in regels["regels"]:
        if r["soort"] != "stroomt":
            continue
        sleutel = (norm(r["van"]), norm(r["naar"]), r.get("pijl"))
        rij = uit.setdefault(r["fase"], collections.OrderedDict()).setdefault(sleutel, [])
        if r.get("beeld_id") and r["beeld_id"] not in rij:
            rij.append(r["beeld_id"])
    return uit


def stromen_per_koppeling(regels, namen):
    """De stromen van de gevraagde koppelingen, elk gelabeld met de naam van die koppeling.

    Waarvoor: laten zien wat een koppeling in de keten raakt. Niet de beelden van een fase,
    maar per lijn welke koppeling erover loopt, zodat een plaat de koppelingen naast elkaar zet.
    """
    uit = collections.OrderedDict()
    for r in regels["regels"]:
        if r["soort"] != "stroomt" or r.get("koppeling") not in namen:
            continue
        rij = uit.setdefault((norm(r["van"]), norm(r["naar"]), r.get("pijl")), [])
        if r["koppeling"] not in rij:
            rij.append(r["koppeling"])
    return uit


def knopen_van_component(knopen, elems, naam):
    """Alle knopen op de view die dit applicatiecomponent tonen; een component staat er soms meer dan een keer."""
    return [k for k in knopen.values() if norm(elems.get(k.get("element", ""), ("", ""))[1]) == naam]


def dichtste_paar(knopen, elems, van, naar):
    """Het paar knopen dat het dichtst bij elkaar ligt, zodat de lijn tussen de bedoelde twee vakken loopt."""
    links, rechts = knopen_van_component(knopen, elems, van), knopen_van_component(knopen, elems, naar)
    if not links or not rechts:
        return None, None
    def midden(k):
        return (k["x"] + k["w"] / 2, k["y"] + k["h"] / 2)
    beste = min(((a, b) for a in links for b in rechts),
                key=lambda ab: (midden(ab[0])[0] - midden(ab[1])[0]) ** 2 + (midden(ab[0])[1] - midden(ab[1])[1]) ** 2)
    return beste


def lees_geometrie(model):
    import xml.etree.ElementTree as ET
    root = ET.parse(model).getroot()
    XSI = platen.XSI
    elems = {e.get("id"): (e.get(XSI, "").split(":")[-1], norm(e.get("name"))) for e in root.iter("element") if e.get(XSI)}
    view = next(e for e in root.iter("element")
                if e.get(XSI) == "archimate:ArchimateDiagramModel" and e.get("name") == VIEW)
    knopen, connecties = {}, []

    def loop(c, ox, oy):
        b = c.find("bounds")
        x, y = ox + int(b.get("x", 0)), oy + int(b.get("y", 0))
        w, h = int(b.get("width", 120)), int(b.get("height", 55))
        knopen[c.get("id")] = dict(x=x, y=y, w=w, h=h, element=c.get("archimateElement"),
                                   groep=c.get(XSI, "").endswith("Group"))
        for sc in c.findall("sourceConnection"):
            bps = [(int(bp.get("startX", 0)), int(bp.get("startY", 0)), int(bp.get("endX", 0)), int(bp.get("endY", 0)))
                   for bp in sc.findall("bendpoint")]
            connecties.append(dict(bron=c.get("id"), doel=sc.get("target"),
                                   relatie=sc.get("archimateRelationship"), knikpunten=bps))
        for k in c.findall("child"):
            loop(k, x, y)

    for c in view.findall("child"):
        loop(c, 0, 0)
    return knopen, connecties, elems


def connectie_voor(connecties, knopen, elems, pijl, van, naar):
    """De getekende lijn van deze relatie op de view.

    Een relatie kan twee keer op de plaat staan, als een component er twee keer op staat.
    Dan telt de lijn tussen de vakken die de stroom bedoelt.
    """
    def naam(knoop_id):
        return norm(elems.get(knopen[knoop_id].get("element", ""), ("", ""))[1])

    def afstand(c):
        a, b = knopen[c["bron"]], knopen[c["doel"]]
        return ((a["x"] + a["w"] / 2 - b["x"] - b["w"] / 2) ** 2 + (a["y"] + a["h"] / 2 - b["y"] - b["h"] / 2) ** 2)

    lijnen = [c for c in connecties if c.get("relatie") == pijl]
    passend = [c for c in lijnen if naam(c["bron"]) == van and naam(c["doel"]) == naar]
    # staat de relatie meer dan een keer op de plaat, dan de kortste lijn: die houdt de markeringen bij elkaar
    return min(passend or lijnen, key=afstand) if (passend or lijnen) else None


def is_knooppunt(knoop, elems):
    """Een junction op de plaat: een punt waar een relatie zich splitst of samenkomt."""
    return elems.get(knoop.get("element", ""), ("", ""))[0].endswith("Junction")


def vervolglijnen(connecties, knopen, elems, conn, naar, gezien=()):
    """De lijnen voorbij een junction, tot het vak van de ontvanger.

    Een relatie die over een junction loopt is op de plaat in stukken getekend. Zonder
    dit vervolg stopt de markering op het punt en lijkt de lijn halverwege te eindigen.
    """
    if not is_knooppunt(knopen[conn["doel"]], elems):
        return []
    for c in connecties:
        if c["bron"] != conn["doel"] or c["relatie"] in gezien:
            continue
        if norm(elems.get(knopen[c["doel"]].get("element", ""), ("", ""))[1]) == naar:
            return [c]
        verder = vervolglijnen(connecties, knopen, elems, c, naar, gezien + (c["relatie"],))
        if verder:
            return [c] + verder
    return []


def k_vak(k, minx, miny):
    """Een element als bezet vlak, zodat een markeringslabel er niet bovenop landt."""
    return (k["x"] - minx, k["y"] - miny, k["w"], k["h"])


def tekst(x, y, s, kleur=ACCENT):
    breedte = 10 + 9 * len(s)
    return (f'<g><rect x="{x - breedte / 2:.0f}" y="{y - 15:.0f}" width="{breedte}" height="21" rx="4" '
            f'fill="#ffffff" stroke="{kleur}" stroke-width="2"/>'
            f'<text x="{x:.0f}" y="{y:.0f}" font-family="Segoe UI, Arial, sans-serif" font-size="15" '
            f'font-weight="bold" fill="{kleur}" text-anchor="middle">{html.escape(s)}</text></g>')


def boog(a, b, gestippeld=False):
    """Een eigen pijl tussen de randen van twee vakken, met een lichte boog zodat zij naast de plaat leest.
    De routering van Archi is niet te reproduceren, dus markeert dit script de twee vakken en de richting
    in plaats van de bestaande lijn over te tekenen."""
    ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
    cb = (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
    p1 = platen.rand(ca, cb, a)
    p2 = platen.rand(cb, ca, b)
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    lengte = max((dx * dx + dy * dy) ** 0.5, 1)
    # het controlepunt ligt loodrecht op het midden, zodat de boog los van de bestaande pijlen loopt
    cx, cy = mx - dy / lengte * min(lengte * 0.12, 60), my + dx / lengte * min(lengte * 0.12, 60)
    return p1, p2, (cx, cy)


def _rechthoek(v):
    return (v["x"], v["y"], v["x"] + v["w"], v["y"] + v["h"])


def _lengte(punten):
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in zip(punten, punten[1:]))


def _knip(punten):
    """Dubbele punten en rechte knikken eruit, zodat een baan van nul lang geen hoek achterlaat."""
    uit = []
    for p in punten:
        if not uit or abs(p[0] - uit[-1][0]) > 0.5 or abs(p[1] - uit[-1][1]) > 0.5:
            uit.append(p)
    i = 1
    while i < len(uit) - 1:
        (x1, y1), (x2, y2), (x3, y3) = uit[i - 1], uit[i], uit[i + 1]
        if (x1 == x2 == x3) or (y1 == y2 == y3):
            uit.pop(i)
        else:
            i += 1
    return uit


class Haaks:
    """Orthogonale routering van de markeringen: rechte lijnen, en waar een hoek moet een hoek van 90 graden.

    Waarvoor: op een plaat met tientallen markeringen leest een schuine lijn niet, en twee lijnen die over
    elkaar heen lopen lezen evenmin. Deze router kent de vakken op de plaat en de banen die al bezet zijn,
    en kiest per stroom de route met de minste hoeken die in vrije baan past: eerst een rechte lijn, dan
    een route met een enkele hoek, en pas daarna een route met twee hoeken door de ruimte tussen de vakken.
    Een lijn naar een vak hogerop verlaat het vak bij voorkeur aan de bovenkant en loopt haar lange been
    bovenlangs, weg van de drukte in het midden van de plaat.
    """

    STAP = 24      # afstand tussen twee banen; zo blijven twee lijnen naast elkaar leesbaar
    MARGE = 12     # een baan blijft zo ver van een vak dat zij niet raakt
    RAND = 14      # een lijn hecht niet in de hoek van een vak aan
    SPLEET = 8     # zoveel ruimte is er minstens nodig voor een rechte lijn tussen twee vakken
    GAT = 28       # en zoveel voor een baan die tussen twee vakken door loopt
    KRAP = 10      # is er geen ruimte voor de volle afstand, dan mogen twee banen zo dicht naast elkaar
    BOCHT = 1000   # een route met minder hoeken wint altijd
    BOVENLANGS = 220  # voorkeur voor de route die bovenlangs loopt naar een vak hogerop

    def __init__(self, vakken=()):
        self.vakken = [(_rechthoek(v), id(v)) for v in vakken]
        self.banen = []

    def pad(self, a, b):
        """De route van vak a naar vak b; de gekozen banen blijven daarna bezet.

        De vorm met de minste hoeken gaat voor, en per vorm de ruimste spreiding: liever een lijn
        die een stuk naast de vorige loopt dan een lijn die er vlak langs of bovenop komt.
        """
        eigen = {id(a), id(b)}
        for vorm in (self._recht, self._bocht, self._baan):
            for afstand in (self.STAP, self.KRAP):
                routes = [r for r in vorm(a, b, eigen, afstand) if r]
                if routes:
                    return self._bezet(min(routes)[1])
        return self._bezet(self._nood(a, b))

    # -- vormen ---------------------------------------------------------------

    def _recht(self, a, b, eigen, afstand):
        """Een rechte lijn: de vakken liggen naast of boven elkaar met genoeg overlap."""
        ax1, ay1, ax2, ay2 = _rechthoek(a)
        bx1, by1, bx2, by2 = _rechthoek(b)
        uit = []
        if bx1 - ax2 >= self.SPLEET or ax1 - bx2 >= self.SPLEET:
            xa, xb = (ax2, bx1) if bx1 > ax2 else (ax1, bx2)
            uit.append(self._zoek([self._band(ay1, ay2, by1, by2)],
                                  lambda w: [(xa, w[0]), (xb, w[0])], eigen, afstand))
        if by1 - ay2 >= self.SPLEET or ay1 - by2 >= self.SPLEET:
            ya, yb = (ay2, by1) if by1 > ay2 else (ay1, by2)
            uit.append(self._zoek([self._band(ax1, ax2, bx1, bx2)],
                                  lambda w: [(w[0], ya), (w[0], yb)], eigen, afstand))
        return uit

    def _bocht(self, a, b, eigen, afstand):
        """Een route met een enkele hoek: haaks het ene vak uit, haaks het andere in."""
        ax1, ay1, ax2, ay2 = _rechthoek(a)
        bx1, by1, bx2, by2 = _rechthoek(b)
        uit = []
        if by1 - ay2 >= self.GAT or ay1 - by2 >= self.GAT:
            yb = by1 if by1 > ay2 else by2
            zij = ((ax2, max(bx1 + self.RAND, ax2 + self.MARGE), bx2 - self.RAND),
                   (ax1, bx1 + self.RAND, min(bx2 - self.RAND, ax1 - self.MARGE)))
            for xa, laag, hoog in zij:
                uit.append(self._zoek([(self._mid(ay1, ay2), ay1 + self.RAND, ay2 - self.RAND),
                                       (self._mid(bx1, bx2), laag, hoog)],
                                      lambda w, xa=xa, yb=yb: [(xa, w[0]), (w[1], w[0]), (w[1], yb)], eigen, afstand))
        if bx1 - ax2 >= self.GAT or ax1 - bx2 >= self.GAT:
            xb = bx1 if bx1 > ax2 else bx2
            zij = ((ay2, max(by1 + self.RAND, ay2 + self.MARGE), by2 - self.RAND, 0),
                   (ay1, by1 + self.RAND, min(by2 - self.RAND, ay1 - self.MARGE),
                    self.BOVENLANGS if by2 <= ay1 else 0))
            for ya, laag, hoog, korting in zij:
                route = self._zoek([(self._mid(ax1, ax2), ax1 + self.RAND, ax2 - self.RAND),
                                    (self._mid(by1, by2), laag, hoog)],
                                   lambda w, ya=ya, xb=xb: [(w[0], ya), (w[0], w[1]), (xb, w[1])], eigen, afstand)
                uit.append((route[0] - korting, route[1]) if route else None)
        return uit

    def _baan(self, a, b, eigen, afstand):
        """Een route met twee hoeken: een lange baan door de ruimte tussen de twee vakken."""
        ax1, ay1, ax2, ay2 = _rechthoek(a)
        bx1, by1, bx2, by2 = _rechthoek(b)
        uit = []
        if bx1 - ax2 >= self.GAT or ax1 - bx2 >= self.GAT:
            xa, xb = (ax2, bx1) if bx1 > ax2 else (ax1, bx2)
            laag, hoog = sorted((xa, xb))
            uit.append(self._zoek([(self._mid(ay1, ay2), ay1 + self.RAND, ay2 - self.RAND),
                                   (self._mid(by1, by2), by1 + self.RAND, by2 - self.RAND),
                                   (self._mid(laag, hoog), laag + self.MARGE, hoog - self.MARGE)],
                                  lambda w: [(xa, w[0]), (w[2], w[0]), (w[2], w[1]), (xb, w[1])], eigen, afstand))
        if by1 - ay2 >= self.GAT or ay1 - by2 >= self.GAT:
            ya, yb = (ay2, by1) if by1 > ay2 else (ay1, by2)
            laag, hoog = sorted((ya, yb))
            korting = self.BOVENLANGS if by2 <= ay1 else 0
            route = self._zoek([(self._mid(ax1, ax2), ax1 + self.RAND, ax2 - self.RAND),
                                (self._mid(bx1, bx2), bx1 + self.RAND, bx2 - self.RAND),
                                (self._mid(laag, hoog), laag + self.MARGE, hoog - self.MARGE)],
                               lambda w: [(w[0], ya), (w[0], w[2]), (w[1], w[2]), (w[1], yb)], eigen, afstand)
            uit.append((route[0] - korting, route[1]) if route else None)
        return uit

    def _nood(self, a, b):
        """Geen vrije baan te vinden: de kortste orthogonale route, hoe druk het er ook is."""
        ax1, ay1, ax2, ay2 = _rechthoek(a)
        bx1, by1, bx2, by2 = _rechthoek(b)
        ya, yb = self._mid(ay1, ay2), self._mid(by1, by2)
        if bx1 > ax2 or ax1 > bx2:
            xa, xb = (ax2, bx1) if bx1 > ax2 else (ax1, bx2)
            xm = (xa + xb) / 2
            return _knip([(xa, ya), (xm, ya), (xm, yb), (xb, yb)])
        xa, xb = self._mid(ax1, ax2), self._mid(bx1, bx2)
        ya, yb = (ay2, by1) if by1 > ay2 else (ay1, by2)
        ym = (ya + yb) / 2
        return _knip([(xa, ya), (xa, ym), (xb, ym), (xb, yb)])

    # -- banen kiezen en vrijhouden -------------------------------------------

    @staticmethod
    def _mid(v1, v2):
        return (v1 + v2) / 2

    def _band(self, a1, a2, b1, b2):
        """Het venster waarin een rechte lijn tussen twee vakken past; None als zij te weinig overlappen."""
        laag, hoog = max(a1, b1) + self.RAND, min(a2, b2) - self.RAND
        return None if hoog < laag else (self._mid(max(a1, b1), min(a2, b2)), laag, hoog)

    def _banen(self, venster):
        """De banen rond het midden op een raster, met de randen van het venster als laatste uitwijk."""
        if venster is None:
            return []
        midden, laag, hoog = venster
        if hoog < laag:
            return []
        midden = min(max(midden, laag), hoog)
        uit = []
        for n in range(8):
            for richting in ((0,) if n == 0 else (1, -1)):
                w = midden + richting * n * self.STAP
                if laag <= w <= hoog and all(abs(w - q) > 1 for _, q in uit):
                    uit.append((len(uit), w))
        for w in (laag, hoog):
            if all(abs(w - q) > 1 for _, q in uit):
                uit.append((len(uit), w))
        return uit

    def _zoek(self, vensters, maak, eigen, afstand):
        """De route met de kleinste afwijking van het midden waarvan elk segment in vrije baan ligt."""
        lijsten = [self._banen(v) for v in vensters]
        if not all(lijsten):
            return None
        for combi in sorted(itertools.product(*lijsten), key=lambda c: sum(i for i, _ in c)):
            punten = _knip(maak([w for _, w in combi]))
            if len(punten) > 1 and self._vrij(punten, eigen, afstand):
                afwijking = sum(i for i, _ in combi)
                return (len(punten) - 2) * self.BOCHT + afwijking * 30 + _lengte(punten) * 0.05, punten
        return None

    def _vrij(self, punten, eigen, afstand):
        for (x1, y1), (x2, y2) in zip(punten, punten[1:]):
            soort = "v" if abs(x1 - x2) < 0.5 else "h"
            coord, van, tot = (x1, y1, y2) if soort == "v" else (y1, x1, x2)
            if not self._vrije_baan(soort, coord, van, tot, eigen, afstand):
                return False
        return True

    def _vrije_baan(self, soort, coord, van, tot, eigen, afstand):
        laag, hoog = sorted((van, tot))
        for (x1, y1, x2, y2), bron in self.vakken:
            if bron in eigen:
                continue
            k1, k2, s1, s2 = (x1, x2, y1, y2) if soort == "v" else (y1, y2, x1, x2)
            if k1 - self.MARGE < coord < k2 + self.MARGE and hoog > s1 + 1 and laag < s2 - 1:
                return False
        for baan, c, v, t in self.banen:
            if baan != soort or abs(c - coord) >= afstand:
                continue
            if min(hoog, max(v, t)) - max(laag, min(v, t)) > 0:
                return False
        return True

    def _bezet(self, punten):
        """De route vastleggen, zodat een volgende lijn ernaast gaat lopen in plaats van eroverheen."""
        for (x1, y1), (x2, y2) in zip(punten, punten[1:]):
            if abs(x1 - x2) < 0.5:
                self.banen.append(("v", x1, y1, y2))
            else:
                self.banen.append(("h", y1, x1, x2))
        return punten


def haaks_pad(a, b, aanhecht=None, spreiding=None):
    """Een orthogonaal pad tussen twee vakken, zonder kennis van de rest van de plaat.

    `bouw` gebruikt Haaks met alle vakken erbij; deze ingang is er voor een losse berekening en
    houdt via `aanhecht` de al gekozen banen vast, zodat twee lijnen niet over elkaar heen lopen.
    """
    if aanhecht is None:
        return Haaks().pad(a, b)
    return aanhecht.setdefault("banen", Haaks()).pad(a, b)


def label_plek(punten, naam, bezet, stap=18):
    """De eerste vrije plek voor het naamvakje langs de route: het langste been eerst, vanuit het midden.

    Waarom niet de kandidaten van `platen.plaats`: die kent per been alleen het midden, en met tientallen
    markeringen naast elkaar landen twee namen dan op dezelfde plek. Dit schuift de naam over het been tot
    zij vrij staat van de vakken, de eerdere namen en de eerder getekende lijnen, en zet haar zo nodig
    net naast de lijn in plaats van erop.
    """
    w, h = 10 + 9 * len(naam), 23
    benen = sorted(zip(punten, punten[1:]), key=lambda s: -(abs(s[1][0] - s[0][0]) + abs(s[1][1] - s[0][1])))
    for a, b in benen:
        staand = abs(b[0] - a[0]) < abs(b[1] - a[1])
        n = max(int((abs(b[0] - a[0]) + abs(b[1] - a[1])) // stap), 1)
        opzij = (w / 2 + 8) if staand else (h + 4)
        plekken = [(opzij * kant, i) for kant in (0, 1, -1) for i in range(n + 1)]
        for kant, i in sorted(plekken, key=lambda p: (abs(p[0]), abs(p[1] - n / 2))):
            f = i / n
            mx = a[0] + (b[0] - a[0]) * f + (kant if staand else 0)
            my = a[1] + (b[1] - a[1]) * f + (0 if staand else kant)
            vak = (mx - w / 2, my - h / 2, w, h)
            if not platen.overlapt(vak, bezet):
                return mx, my, vak
    a, b = benen[0]
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    return mx, my, (mx - w / 2, my - h / 2, w, h)


def lijnvakken(punten, dikte=8):
    """De getekende lijn als bezette vakjes, zodat een volgende naam er niet bovenop landt."""
    uit = []
    for (x1, y1), (x2, y2) in zip(punten, punten[1:]):
        x, y = min(x1, x2), min(y1, y2)
        uit.append((x - dikte / 2, y - dikte / 2, abs(x2 - x1) + dikte, abs(y2 - y1) + dikte))
    return uit


def bouw(knopen, connecties, elems, png, stromen, pijl_van, uitsnede=False, haaks=False):
    minx = min(k["x"] for k in knopen.values()) - MARGE
    miny = min(k["y"] for k in knopen.values()) - MARGE
    W = max(k["x"] + k["w"] for k in knopen.values()) + MARGE - minx
    H = max(k["y"] + k["h"] for k in knopen.values()) + MARGE - miny
    b64 = base64.b64encode(png.read_bytes()).decode()
    soort = png.suffix.lstrip(".").replace("jpg", "jpeg")
    delen = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
             f'<defs><marker id="punt" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
             f'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{ACCENT}"/></marker></defs>',
             f'<image href="data:image/{soort};base64,{b64}" x="0" y="0" width="{W}" height="{H}"/>',
             # de plaat vervaagt, zodat de markeringen eruit springen
             f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff" fill-opacity="0.6"/>']
    geraakt, ontbreekt, labels, bezet = [], [], [], [k_vak(k, minx, miny) for k in knopen.values() if not k.get("groep")]
    # de router kent alle vakken, zodat een baan niet door een vak loopt en niet op een andere baan valt
    router = Haaks([k for k in knopen.values() if not k.get("groep")])
    for (van, naar, pijl), beelden in stromen.items():
        label = ", ".join(beelden)
        conn = None if haaks else (connectie_voor(connecties, knopen, elems, pijl, van, naar) if pijl != GEEN_PIJL else None)
        if haaks:
            a, b = dichtste_paar(knopen, elems, van, naar)
            if not a or not b:
                ontbreekt.append(f"{label}: {van} naar {naar}")
                continue
            punten = [(x - minx, y - miny) for x, y in router.pad(a, b)]
            d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in punten)
            streep = ""
            geraakt += [a, b]
        elif conn:
            # over de bestaande pijl heen: hetzelfde pad dat Archi tekent, met een witte onderlaag eronder
            lijnen = [conn] + vervolglijnen(connecties, knopen, elems, conn, naar)
            punten = [(x - minx, y - miny) for c in lijnen for x, y in platen.pad(c, knopen)]
            d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in punten)
            streep = ""
            geraakt += [knopen[conn["bron"]], knopen[lijnen[-1]["doel"]]]
        else:
            a, b = dichtste_paar(knopen, elems, van, naar)
            if not a or not b:
                ontbreekt.append(f"{label}: {van} naar {naar}")
                continue
            # geen lijn om over te trekken: een eigen boog die zichtbaar los van de plaat loopt
            p1, p2, c = boog(a, b)
            punten = [(p1[0] - minx, p1[1] - miny), (c[0] - minx, c[1] - miny), (p2[0] - minx, p2[1] - miny)]
            d = (f'M{punten[0][0]:.0f},{punten[0][1]:.0f} Q{punten[1][0]:.0f},{punten[1][1]:.0f} '
                 f'{punten[2][0]:.0f},{punten[2][1]:.0f}')
            streep = ' stroke-dasharray="12 9"'
            label += " (geen pijl)" if pijl == GEEN_PIJL else ""
            geraakt += [a, b]
        delen.append(f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="11" stroke-opacity="0.85"/>')
        delen.append(f'<path d="{d}" fill="none" stroke="{ACCENT}" stroke-width="5"{streep} '
                     f'marker-end="url(#punt)"/>')
        mx, my, vak = label_plek(punten, label, bezet) if haaks else platen.plaats(punten, label, bezet)
        bezet.append(vak)
        if haaks:
            bezet += lijnvakken(punten)
        labels.append(tekst(mx, my + 6, label))
    for k in geraakt:
        delen.append(f'<rect x="{k["x"]-minx-3:.0f}" y="{k["y"]-miny-3:.0f}" width="{k["w"]+6}" '
                     f'height="{k["h"]+6}" fill="none" stroke="{RAND}" stroke-width="4" rx="4"/>')
    delen += labels   # de namen van de stromen bovenop, zodat zij leesbaar blijven
    delen.append("</svg>")
    if uitsnede and geraakt:
        # op een slide leest de hele plaat niet; snijd uit rond de gemarkeerde vakken, met lucht voor de bogen
        bx, by, bw, bh = venster(geraakt, minx, miny, W, H, buren=knopen.values())
        delen[0] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{bx} {by} {bw} {bh}" '
                    f'width="{bw}" height="{bh}">')
    return "".join(delen), ontbreekt


def venster(geraakt, minx, miny, W, H, lucht=90, buren=()):
    """Het deel van de plaat waar de markeringen liggen, met lucht eromheen, binnen de plaat.

    Vakken die de rand van dat deel raken worden er helemaal in getrokken: een half
    afgesneden vak met een half woord erin leest als een fout, niet als een uitsnede.
    Grote vakken blijven buiten die verruiming, want dat zijn de groeperingen.
    """
    x1 = min(k["x"] for k in geraakt) - minx - lucht
    y1 = min(k["y"] for k in geraakt) - miny - lucht
    x2 = max(k["x"] + k["w"] for k in geraakt) - minx + lucht
    y2 = max(k["y"] + k["h"] for k in geraakt) - miny + lucht
    ox1, oy1, ox2, oy2 = x1, y1, x2, y2   # toetsen tegen het oorspronkelijke venster, anders groeit het door
    for k in buren:
        if k.get("groep") or k["w"] > W * 0.4 or k["h"] > H * 0.4:
            continue
        kx1, ky1 = k["x"] - minx, k["y"] - miny
        kx2, ky2 = kx1 + k["w"], ky1 + k["h"]
        if kx2 > ox1 and kx1 < ox2 and ky2 > oy1 and ky1 < oy2:
            x1, y1, x2, y2 = min(x1, kx1 - 8), min(y1, ky1 - 8), max(x2, kx2 + 8), max(y2, ky2 + 8)
    x1, y1 = max(0, round(x1)), max(0, round(y1))
    return x1, y1, min(round(x2), W) - x1, min(round(y2), H) - y1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--stromen", type=pathlib.Path, default=STROMEN)
    parser.add_argument("--plaat", type=pathlib.Path, default=PLAAT, help="render van de hoofdplaat (png of jpg)")
    parser.add_argument("--uit", type=pathlib.Path, default=UITMAP)
    parser.add_argument("--koppelingen", help="komma-gescheiden koppelingen; markeert die op een plaat "
                                              "in plaats van een plaat per fase")
    parser.add_argument("--uitsnede", action="store_true", help="snijd uit rond de gemarkeerde vakken")
    parser.add_argument("--haaks", action="store_true", help="teken de markeringen orthogonaal in plaats van over de bestaande pijlen")
    args = parser.parse_args(argv)
    if not args.plaat.exists():
        sys.exit(f"plaat niet gevonden: {args.plaat}; render hem met exporteer-archimate-platen.py")
    regels = json.loads(args.regels.read_text(encoding="utf-8"))
    stromen_json = json.loads(args.stromen.read_text(encoding="utf-8"))
    pijl_van = {s["id"]: s for s in stromen_json.get("stromen", [])}
    knopen, connecties, elems = lees_geometrie(args.model)
    args.uit.mkdir(parents=True, exist_ok=True)
    if args.koppelingen:
        namen = [n.strip() for n in args.koppelingen.split(",") if n.strip()]
        stromen = stromen_per_koppeling(regels, namen)
        if not stromen:
            sys.exit(f"geen stromen gevonden voor {', '.join(namen)}")
        svg, ontbreekt = bouw(knopen, connecties, elems, args.plaat, stromen, pijl_van, args.uitsnede, args.haaks)
        doel = args.uit / "koppelingen.svg"
        doel.write_text(svg, encoding="utf-8")
        for x in ontbreekt:
            print(f"waarschuwing: niet op de plaat te plaatsen: {x}", file=sys.stderr)
        print(f"koppelingenplaat geschreven naar {doel}")
        return 0
    aantal = 0
    for fase, stromen in stromen_per_fase(regels).items():
        svg, ontbreekt = bouw(knopen, connecties, elems, args.plaat, stromen, pijl_van)
        (args.uit / f"f{fase}.svg").write_text(svg, encoding="utf-8")
        aantal += 1
        for x in ontbreekt:
            print(f"waarschuwing: fase {fase}, niet op de plaat te plaatsen: {x}", file=sys.stderr)
    print(f"{aantal} faseplaten geschreven naar {args.uit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
