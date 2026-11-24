#!/usr/bin/env python3
"""De regels van de voorbeelduitwerking tekenen als SVG in ArchiMate-vormtaal.

Waarom dit script bestaat: het voorbeeld (de opleiding van Jochem, stap voor stap in
het informatiemodel) moet leesbaar zijn als een reeks korte, visuele regels, niet als
tekst. Elke regel uit de regeltabel wordt een zelfdragende SVG (geen externe fonts,
geen scripts), zodat hij op GitHub in markdown rendert en na een modelronde opnieuw
te maken is.

    python3 tools/scripts/teken-leerroute-uitwerking-model.py [--regels PAD] [--uit MAP]

Een planningsvorm naast de regeltabel (leerroute-uitwerking-model-lr1-<vorm>.json) wordt daarna getekend,
naar dezelfde map.

Drie soorten regels, in de kleuren en iconen van ArchiMate:
- ontstaat: rol (geel, rolicoon), processtap (geel, procesicoon), de objecttypen van
  de plaat (geel, business-objecticoon) met de instantie voor Jochem; "bestaat uit"
  als nesting; een aanname gestippeld; een scope-uitzondering grijs;
- verandert: als ontstaat, met de nieuwe toestand op het object;
- stroomt: van (blauw, componenticoon), het object op een gestippelde pijl, naar, met
  de koppeling-ID en de processtap als klein label.
"""

import argparse
import importlib.util
import html
import importlib.util
import json
import pathlib
import re
import sys

_spec = importlib.util.spec_from_file_location("leerroute_uitwerking_model_varianten", pathlib.Path(__file__).resolve().parent / "leerroute-uitwerking-model-varianten.py")
varianten = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(varianten)

REGELS = pathlib.Path("architecture/model/informatiemodel/leerroute-uitwerking-model-lr1.json")
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
SOORTEN = {"ontstaat", "verandert", "stroomt", "bestaat"}
# wat in een beeld met een kolom "eerder ontstaan" hier ontstaat, krijgt de nadruk met een dikkere,
# donkerdere rand; de vulling blijft ArchiMate-geel, zodat beide herkenbaar business objects blijven
NADRUK_L, NADRUK_DIKTE = BUS_T, "2.5"
# waar elk object in het laatst getekende beeld staat: (type, instantie) -> (x, y, breedte); de
# herkomstlijnen lopen daartussen. De laatste tekenronde van een indeling wint, en dat is de getoonde.
POSITIES = {}


def tw(s, size=13, bold=False):
    """Geschatte tekstbreedte in px voor Arial; ruim genoeg zodat tekst niet in het icoon loopt."""
    return len(s) * size * (0.66 if bold else 0.6)


def icon(kind, x, y, kleur="#444"):
    return f'<g transform="translate({x:.0f},{y:.0f})" fill="none" stroke="{kleur}" stroke-width="1.3">{ICONS[kind]}</g>'


def box(x, y, w, h, fill, line, rx=0, dashed=False, patroon="5 3", dik=False):
    """dashed met patroon "5 3" markeert een aanname; relatielabels gebruiken "2 2". dik: de nadruk op
    wat in dit beeld ontstaat, naast een kolom met wat eerder ontstond."""
    d = f' stroke-dasharray="{patroon}"' if dashed else ""
    d += f' stroke-width="{NADRUK_DIKTE}"' if dik else ""
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}" stroke="{line}"{d}/>'


def text(x, y, s, size=13, bold=False, fill=INK, anchor="start"):
    fw = ' font-weight="bold"' if bold else ""
    return f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONT}" font-size="{size}"{fw} fill="{fill}" text-anchor="{anchor}">{html.escape(s)}</text>'


INSTANTIE_MAX_BREEDTE = 430  # een instantie breekt af in plaats van het vak op te rekken; twee vakken van
                             # deze maat passen naast elkaar binnen MAX_BREEDTE, dus de rij blijft leesbaar


def afbreken(tekst, maxw, size=14, bold=True):
    """Een tekst in regels die binnen maxw passen. Een woord dat zelf te breed is krijgt een eigen regel."""
    woorden, regels, huidige = str(tekst).split(), [], ""
    for w in woorden:
        proef = (huidige + " " + w).strip()
        if huidige and tw(proef, size, bold) > maxw:
            regels.append(huidige)
            huidige = w
        else:
            huidige = proef
    if huidige:
        regels.append(huidige)
    return regels or [""]


def element(x, y, kind, label, inst, fill=BUS, line=BUS_L, labelkleur=BUS_T, rx=0, dashed=False, toestand=None, verwijzing=None, verwijzingen=(), dik=False):
    """Eén element: typelabel klein, instantie vet over zo veel regels als nodig, en eronder de toestand
    en de verwijzingen naar objecten buiten het blok. Geeft (svg, w, h).

    De instantie breekt af op INSTANTIE_MAX_BREEDTE. Zonder dat afbreken rekt een zin het vak op tot
    ver voorbij de breedte die een document aankan: een leeruitkomst die volgens het tuning model is
    geformuleerd is een volledige zin, en die maakte een beeld bijna twee keer zo breed.
    """
    extra = _extra(toestand, verwijzing, verwijzingen)
    regels = afbreken(inst, INSTANTIE_MAX_BREEDTE)
    w = max(120, max([tw(label, 12)] + [tw(r, 14, True) for r in regels] + [tw(e, 12) for e in extra]) + 42)
    h = 48 + 18 * (len(regels) - 1) + 17 * len(extra)
    s = box(x, y, w, h, fill, line, rx, dashed, dik=dik) + icon(kind, x + w - 22, y + 5)
    s += text(x + 10, y + 18, label, 12, fill=labelkleur)
    for i, r in enumerate(regels):
        s += text(x + 10, y + 36 + 18 * i, r, 14, True)
    voet = y + 36 + 18 * (len(regels) - 1)
    for i, e in enumerate(extra):
        s += text(x + 10, voet + 17 + 17 * i, e, 12, fill=MUTED)
    return s, w, h


VOORSTEL_MERK = "toe te voegen aan het informatiemodel"


def _merk_voorstel(item, r):
    """Een objecttype dat het informatiemodel nog niet draagt staat als voorstel op de plaat: gestippeld,
    met het merk in het vak. Zonder dat merk leest een voorstel als een feit, en daar bouwt een lezer op."""
    if r.get("voorstel"):
        item["aanname"] = True
        item["verwijzingen"] = [VOORSTEL_MERK] + [v for v in (item.get("verwijzingen") or []) if v]
    return item


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


MAX_BREEDTE = 1000  # daarboven gaat een keten van relaties onder elkaar in plaats van naast elkaar


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


OMWEG_MARGE = 22  # ruimte rechts van het breedste vak waar een omweglijn omhoog loopt
OMWEG_BAAN = 14   # afstand tussen twee omwegbanen, zodat verticale stukken niet samenvallen
OMWEG_REGEL = 14  # hoogte van een labelregel, voor twee omwegen die bij hetzelfde doel uitkomen
# een omweg loopt ver van zijn label af, dus kleur bindt de twee aan elkaar. De uitlijning op de hoogte
# van de pijlpunt blijft ernaast staan, zodat kleur niet het enige onderscheid is. De tinten zijn donker
# en onderling verschillend in helderheid, zodat ze ook op het gele vlak en in grijstint uit elkaar vallen
OMWEG_KLEUREN = ["#1f6fb2", "#b5651d", "#11776b", "#7a3b9e", "#a33a3a", "#4a4a4a"]
# boven de drie omwegen wordt een blok een rangeerterrein: de banen lopen om het hele beeld heen en
# winnen het niet meer van de verwijzing die er anders staat. Daarboven valt de tekenaar dus terug
OMWEG_MAX = 3
# verder terug dan drie objecten is een lijn niet meer te volgen; dan zegt de verwijzing onder het
# object meer, want die noemt de instantie. Draagt de relatie een label, dan is de lijn het wel waard
OMWEG_BEREIK = 3


def _de_moeite(objecten_in_blok, ander, label):
    """Of een relatie over afstand als lijn te tekenen is in plaats van als verwijzing."""
    if _omwegen_in_blok(objecten_in_blok) >= OMWEG_MAX:
        return False
    types = [it["type"] for it in objecten_in_blok if "type" in it]
    if ander not in types:
        return bool(label)
    return bool(label) or len(types) - types.index(ander) <= OMWEG_BEREIK


def _horizontaal_met_bruggen(x1, x2, y, banen, eigen):
    """Een horizontaal stuk dat met een boogje over elke andere baan heen gaat die het kruist.

    Het stuk stopt vlak voor de baan, maakt een boogje eroverheen en loopt verder. Daardoor raken de
    twee lijnen elkaar niet: wat overblijft is een brug, en geen kruising."""
    heen = x2 > x1
    kruist = sorted((bx for bx, y0, y1 in banen
                     if bx != eigen and min(x1, x2) < bx < max(x1, x2) and y0 <= y <= y1),
                    reverse=not heen)
    d = ""
    for bx in kruist:
        voor, na = (bx - 4, bx + 4) if heen else (bx + 4, bx - 4)
        d += f"H{voor:.0f}A4 4 0 0 {1 if heen else 0} {na:.0f} {y:.0f}"
    return d + f"H{x2:.0f}"


def relatielijn_omweg(x_bron, y_bron, x_doel, y_doel, baan, soort, label, naar_bron=True, banen=(), kleur="#444"):
    """Een relatie naar een object dat niet de buur is: haaks om de blokken heen, langs een goot rechts
    ervan. De baan ligt voorbij de rechterrand van alles ertussen, dus de lijn kruist geen vak.
    naar_bron: de relatie wijst naar het object dat hier wordt getekend (de bron van de lijn); anders
    wijst zij naar het object verder terug (het doel)."""
    heen = _horizontaal_met_bruggen(x_bron, baan, y_bron, banen, baan)
    terug = _horizontaal_met_bruggen(baan, x_doel, y_doel, banen, baan)
    s = (f'<path d="M{x_bron:.0f} {y_bron:.0f}{heen}V{y_doel:.0f}{terug}" '
         f'stroke="{kleur}" stroke-width="1.3" fill="none"/>')
    # het geheel draagt de ruit, het doel van de relatie draagt de punt
    punt_x, punt_y = (x_bron, y_bron) if naar_bron else (x_doel, y_doel)
    heel_x, heel_y = (x_doel, y_doel) if naar_bron else (x_bron, y_bron)
    if soort in ("Aggregation", "Composition"):
        vulling = kleur if soort == "Composition" else "#ffffff"
        s += (f'<path d="M{heel_x:.0f} {heel_y:.0f}l7 -5l7 5l-7 5z" '
              f'fill="{vulling}" stroke="{kleur}" stroke-width="1.3"/>')
    elif soort == "Specialization":
        s += f'<path d="M{punt_x:.0f} {punt_y:.0f}l10 -6v12z" fill="#ffffff" stroke="{kleur}" stroke-width="1.3"/>'
    elif label:
        s += f'<path d="M{punt_x:.0f} {punt_y:.0f}l8 -4v8z" fill="{kleur}"/>'
    return s


def objecten(x, y, items, uitzonderingen):
    """Rij van objecten met de relaties van de plaat als lijnen ertussen; nesting bij kinderen.
    Wordt de rij breder dan MAX_BREEDTE, dan gaat de keten na het eerste object onder elkaar.
    Geeft (svg, w, h)."""
    if any(it.get("over_afstand") for it in items):
        # een omweg vraagt verticale ruimte: dit blok gaat altijd als kolom
        return _objecten_kolom(x, y, items, uitzonderingen, alles_onder=True)
    svg, w, h = _objecten_rij(x, y, items, uitzonderingen)
    objs = [it for it in items if "type" in it]
    if w <= MAX_BREEDTE or len(objs) < 2:
        return svg, w, h
    svg, w, h = _objecten_kolom(x, y, items, uitzonderingen)
    if w <= MAX_BREEDTE:
        return svg, w, h
    # ook eerste object plus kolom te breed: alles onder elkaar
    return _objecten_kolom(x, y, items, uitzonderingen, alles_onder=True)


def _objecten_kolom(x, y, items, uitzonderingen, alles_onder=False):
    """Eerste object links; de rest als kolom rechts ervan, met verticale relatielijnen.
    alles_onder: ook het eerste object staat in de kolom."""
    eerste = items[0]
    svg1, w1, h1 = _objecten_rij(x, y, [eerste], uitzonderingen)
    kx = x if alles_onder else x + w1 + RELATIE_AFSTAND
    ky = y + h1 + 28 if alles_onder else y
    out = svg1
    lijnen = ""
    vorige_onder = None
    vorige_mid_x = None
    wachtende_relaties = []
    maxw = w1 if alles_onder else w1 + RELATIE_AFSTAND
    if alles_onder:
        vorige_onder = y + h1
    # waar elk getekend objecttype staat: (rechterrand, middenhoogte); voor een relatie over afstand
    plekken = {eerste["type"]: (x + w1, y + 24)}
    omwegen = []  # (bron_rechts, bron_mid, doel_type, soort, label) om na te tekenen als de goot bekend is
    for it in items[1:]:
        if "relatie" in it and "type" not in it:
            wachtende_relaties.append(it)
            continue
        svg_it, w_it, h_it = _objecten_rij(kx, ky, [it], uitzonderingen)
        out += svg_it
        # meerdere relaties op een object: een naar de buur als lijn, de rest met een omweg
        for i, wacht in enumerate(wachtende_relaties):
            soort = wacht.get("soort", "Association")
            label = wacht["relatie"]
            doel = wacht.get("ander")
            if wacht.get("over_afstand"):
                # het andere eind staat verder terug: haaks eromheen, langs een goot rechts van de blokken
                if doel in plekken:
                    omwegen.append((kx + w_it, ky + 24 + 14 * i, doel, soort, label, wacht.get("naar_rechts", True)))
            elif vorige_onder is None:
                # relatie tussen het eerste object (links) en dit object: horizontaal, op de hoogte van dit object
                lijnen += relatielijn(x + w1, ky + 24, kx, soort, label, wacht.get("naar_rechts", True))
            else:
                lijnen += relatielijn_v(kx + min(w_it, 120) / 2, vorige_onder, ky, soort, label, wacht.get("naar_rechts", True))
        wachtende_relaties = []
        plekken.setdefault(it["type"], (kx + w_it, ky + 24))
        plekken[it["type"]] = (kx + w_it, ky + 24)
        vorige_onder = ky + h_it
        ky += h_it + 28
        maxw = max(maxw, w_it if alles_onder else w1 + RELATIE_AFSTAND + w_it)
    if omwegen:
        # elke omweg krijgt een eigen baan, de langste buitenom, zodat geen twee verticale stukken
        # samenvallen en elke lijn van begin tot eind te volgen is
        op_lengte = sorted(omwegen, key=lambda o: abs(plekken[o[2]][1] - o[1]))
        buitenste = x + maxw + OMWEG_MARGE + (len(op_lengte) - 1) * OMWEG_BAAN
        # elke baan met haar verticale bereik, zodat een lijn die eroverheen moet een brug krijgt
        banen = [(x + maxw + OMWEG_MARGE + i * OMWEG_BAAN,
                  min(o[1], plekken[o[2]][1]), max(o[1], plekken[o[2]][1]))
                 for i, o in enumerate(op_lengte)]
        bezet = {}
        for i, (bron_x, bron_y, doel, soort, label, naar_rechts) in enumerate(op_lengte):
            doel_x, doel_y = plekken[doel]
            # komen er twee omwegen bij hetzelfde doel uit, dan schuift de tweede aankomst een regel op;
            # anders vallen twee pijlpunten samen en is niet te zien welk label bij welke lijn hoort
            rij = bezet.get(doel, 0)
            bezet[doel] = rij + 1
            doel_y += rij * OMWEG_REGEL
            baan = banen[i][0]
            # kleur verschijnt waar zij iets onderscheidt; bij een enkele omweg valt er niets te
            # onderscheiden en blijft het beeld in de gewone lijnkleur
            kleur = OMWEG_KLEUREN[i % len(OMWEG_KLEUREN)] if len(op_lengte) > 1 else "#444"
            lijnen += relatielijn_omweg(bron_x, bron_y, doel_x, doel_y, baan, soort, label, naar_rechts, banen, kleur)
            if label:
                # het label staat op de hoogte van de pijlpunt, voorbij alle banen, in de kleur van de lijn.
                # welk eind de punt draagt hangt af van de richting van de relatie
                punt_y = bron_y if naar_rechts else doel_y
                lijnen += text(buitenste + 8, punt_y + 4, label, 10, fill=kleur)
        breedste = max((tw(lab, 10) for *_, lab, _ in omwegen), default=0)
        maxw = buitenste - x + 8 + (breedste + 10 if breedste else 0)
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
        if it.get("focus"):
            line = NADRUK_L
        if it.get("kinderen"):
            # een container toont, net als een los element, de toestand en verwijzingen onder de instantie
            extra = _extra(it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()))
            kop = 42 + 17 * len(extra)
            inst_regels = afbreken(it["instantie"], INSTANTIE_MAX_BREEDTE)
            kop = 42 + 18 * (len(inst_regels) - 1) + 17 * len(extra)
            ksvg, kw, kh = _kinderen(cx + 14, y + kop, it["kinderen"], uitzonderingen)
            w = max([kw + 24, tw(it["type"], 12) + 42] + [tw(r, 14, True) + 42 for r in inst_regels]
                    + [tw(e, 12) + 42 for e in extra])
            h = kop + kh + 10
            out += box(cx, y, w, h, fill, line, 0, dashed, dik=it.get("focus", False)) + icon("object", cx + w - 22, y + 5)
            out += text(cx + 10, y + 18, it["type"], 12, fill=lk) + ksvg
            for i, r in enumerate(inst_regels):
                out += text(cx + 10, y + 36 + 18 * i, r, 14, True)
            voet = y + 36 + 18 * (len(inst_regels) - 1)
            for i, e in enumerate(extra):
                out += text(cx + 10, voet + 17 + 17 * i, e, 12, fill=MUTED)
        else:
            s, w, h = element(cx, y, "object", it["type"], it["instantie"], fill, line, lk, 0, dashed, it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()), dik=it.get("focus", False))
            out += s
        POSITIES[(it["type"], it["instantie"])] = (cx, y, w)
        vorige_rand = (cx + w, y + 24)
        cx += w + 8
        maxh = max(maxh, h)
    return out + lijnen, cx - x - 8, maxh


STROOM_MAX_BREEDTE = 1000  # breder dan dit: de keten over een pijl loopt door op een volgende rij


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
            label = rel["relatie"] or STANDAARDLABEL.get(rel["soort"], "hangt aan")
            ander = rel.get("ander", "")
            rij[0].setdefault("verwijzingen", []).append(f"{ander} {label}".strip() if rel.get("naar_rechts", True) else f"{label} {ander}".strip())
        svg, w, h = _objecten_rij(x, ry, rij, uitzonderingen, True)
        out += svg
        uit.append((ry, x + w))
        maxw = max(maxw, w)
        ry += h + 28
    return out, maxw, ry - 28 - y, uit


KINDEREN_MAX_BREEDTE = 700  # breder dan dit: de kinderen onder elkaar in plaats van naast elkaar


def _kinderen(x, y, items, uitzonderingen):
    """Kinderen van een container: naast elkaar, of onder elkaar als de rij te breed wordt."""
    svg, w, h = _objecten_rij(x, y, items, uitzonderingen)
    # bestaande objecten staan onder elkaar: elk krijgt een herkomstlijn naar rechts, en naast elkaar
    # liep de lijn van het linker kind dwars door zijn buur
    gestapeld = any(it.get("bestaat") for it in items)
    if (w <= KINDEREN_MAX_BREEDTE and not gestapeld) or len(items) < 2:
        return svg, w, h
    out, ky, maxw = "", y, 0
    for it in items:
        s, iw, ih = _objecten_rij(x, ky, [it], uitzonderingen)
        out += s
        ky += ih + 8
        maxw = max(maxw, iw)
    return out, maxw, ky - 8 - y


KOP = 30  # ruimte bovenin voor de beeldtitel
ZIN_MAX_BREEDTE = 1000  # de zin onder een beeld loopt door op een volgende regel


def alinea(x, y, tekst, size=14, maxw=ZIN_MAX_BREEDTE, fill=MUTED):
    """Een zin over meer regels als hij breder wordt dan maxw. Geeft (svg, breedte, hoogte)."""
    woorden, regels, huidige = tekst.split(), [], ""
    for w in woorden:
        proef = (huidige + " " + w).strip()
        if huidige and tw(proef, size) > maxw:
            regels.append(huidige); huidige = w
        else:
            huidige = proef
    if huidige:
        regels.append(huidige)
    svg = "".join(text(x, y + i * (size + 5), r, size, fill=fill) for i, r in enumerate(regels))
    return svg, max([tw(r, size) for r in regels] + [0]), (len(regels) - 1) * (size + 5) if regels else 0


def wrap(W, H, body, dashed=False, titel=None):
    rand = ' stroke-dasharray="6 4"' if dashed else ""
    kop = text(12, 22, titel, 15, True) if titel else ""
    W = max(W, tw(titel or "", 15, True) + 24)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">'
            f'<rect x="0.5" y="0.5" width="{W-1:.0f}" height="{H-1:.0f}" rx="10" fill="#ffffff" stroke="{LIJN}"{rand}/>{kop}{body}</svg>')


HERKOMST_BAAN = 10  # afstand tussen de verticale stukken van twee herkomstlijnen


def _herkomstlijnen(blok, rand):
    """Per relatie een haakse lijn van het bestaande object links naar het object dat hier ontstaat: eruit
    op de hoogte van de kop, een eigen verticale baan in de goot, en erin met het label van de plaat.
    Staan de lagen gelijk, dan is de lijn recht. De lijnen komen na de vakken, anders verdwijnt de
    pijlpunt naar een genest object onder zijn ouder."""
    uit = ""
    for i, l in enumerate(blok.get("herkomstlijnen") or []):
        if l["bron"] not in POSITIES or l["doel"] not in POSITIES:
            continue
        bx, by, bw = POSITIES[l["bron"]]
        dx, dy, _ = POSITIES[l["doel"]]
        x1, y1, x2, y2 = bx + bw, by + 24, dx, dy + 24
        baan = rand + 16 + i * HERKOMST_BAAN
        uit += (f'<path class="herkomstlijn" d="M{x1:.0f} {y1:.0f}H{baan:.0f}V{y2:.0f}H{x2:.0f}" '
                f'stroke="#444" stroke-width="1.3" fill="none"/>')
        # dezelfde notatie als relatielijn: ruit aan het geheel, open punt aan het algemene, en een pijlpunt
        # bij een associatie met een richting (label); beide einden lopen horizontaal het vak in
        (gx, gy, gr), (dx_, dy_, dr) = ((x1, y1, 1), (x2, y2, -1)) if l["naar_rechts"] else ((x2, y2, -1), (x1, y1, 1))
        if l["soort"] in ("Aggregation", "Composition"):
            vulling = "#444" if l["soort"] == "Composition" else "#ffffff"
            uit += f'<path d="M{gx:.0f} {gy:.0f}l{7*gr} -5l{7*gr} 5l{-7*gr} 5z" fill="{vulling}" stroke="#444" stroke-width="1.3"/>'
        elif l["soort"] == "Specialization":
            uit += f'<path d="M{dx_:.0f} {dy_:.0f}l{10*dr} -6v12z" fill="#ffffff" stroke="#444" stroke-width="1.3"/>'
        elif l["label"]:
            uit += f'<path d="M{dx_:.0f} {dy_:.0f}l{8*dr} -4v8z" fill="#444"/>'
        if l["label"]:
            # naast de eigen baan, in de goot: bij het doel valt het label achter de rand van zijn ouder
            uit += text(baan + 6, y2 - 5, l["label"], 10, fill=MUTED)
    return uit


def _kleur(it, uitzonderingen):
    """Vulling, rand en labelkleur van een object, zoals _objecten_rij die kiest."""
    fill, line, lk = (GRIJS, GRIJS_L, GRIJS_T) if it["type"] in uitzonderingen else (BUS, BUS_L, BUS_T)
    if it.get("plaat") == "onderwijsontwerp":
        fill, line, lk = CONCEPT, CONCEPT_L, CONCEPT_T
    if it.get("focus"):
        line = NADRUK_L
    return fill, line, lk


def _maat(it):
    """(breedte, kophoogte, hoogte als blad) van een object, met dezelfde rekenregels als element() en de
    container in _objecten_rij; kinderen staan in deze vorm altijd onder elkaar."""
    extra = _extra(it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()))
    regels = afbreken(it["instantie"], INSTANTIE_MAX_BREEDTE)
    eigen = max(120, max([tw(it["type"], 12)] + [tw(r, 14, True) for r in regels] + [tw(e, 12) for e in extra]) + 42)
    kinderen = [k for k in it.get("kinderen", []) if "type" in k]
    w = max([eigen] + [_maat(k)[0] + 28 for k in kinderen])
    return w, 42 + 18 * (len(regels) - 1) + 17 * len(extra), 48 + 18 * (len(regels) - 1) + 17 * len(extra)


def _plat(items, diepte=0):
    """Pre-order: (object, diepte, relatie ervoor). Een relatie-item tussen twee objecten bovenaan hoort
    bij het object erna; een relatie over afstand past niet in deze vorm (None)."""
    uit, wacht = [], None
    for it in items:
        if "type" not in it:
            if it.get("over_afstand"):
                return None
            wacht = it
            continue
        uit.append((it, diepte, wacht))
        wacht = None
        sub = _plat(it.get("kinderen", []), diepte + 1)
        if sub is None:
            return None
        uit += sub
    return uit


class _Kant:
    """De verticale cursor van een kolom: waar het volgende object kan beginnen, met de open containers."""
    def __init__(self, y):
        self.cursor, self.open, self.laatste_bodem = y, [], y

    def sluit_tot(self, diepte):
        while self.open and self.open[-1][1] >= diepte:
            it, d = self.open.pop()
            it["_bodem"] = self.laatste_bodem + 10
            self.laatste_bodem = it["_bodem"]
            self.cursor = it["_bodem"] + (28 if d == 0 else 8)

    def plaats(self, it, diepte, y):
        it["_y"] = y
        _, kop, blad = _maat(it)
        if [k for k in it.get("kinderen", []) if "type" in k]:
            self.open.append((it, diepte))
            self.cursor = y + kop
        else:
            it["_bodem"] = y + blad
            self.laatste_bodem = it["_bodem"]
            self.cursor = it["_bodem"] + (28 if diepte == 0 else 8)


def _uitgelijnd(lx, rx, y, links, rechts, lijnen, uitzonderingen):
    """Beide kolommen onder elkaar, met elk paar uit een herkomstlijn op dezelfde hoogte: de laag van de
    specificatie naast de laag van het aanbod. Geeft (svg links, svg rechts, hoogte), of None als de paren
    niet in dezelfde volgorde staan of een relatie over afstand loopt; dan valt het beeld terug op twee
    gewone kolommen."""
    pl, pr = _plat(links), _plat(rechts)
    if pl is None or pr is None:
        return None
    paar = {l["bron"]: l["doel"] for l in lijnen}
    sleutel = lambda it: (it["type"], it["instantie"])
    volgorde = [sleutel(it) for it, _, _ in pr]
    gepaard = [volgorde.index(paar[sleutel(it)]) for it, _, _ in pl if paar.get(sleutel(it)) in volgorde]
    if gepaard != sorted(gepaard):
        return None
    doelen = set(paar.values())
    kl, kr = _Kant(y), _Kant(y)
    i = j = 0
    while i < len(pl) or j < len(pr):
        l = pl[i] if i < len(pl) else None
        r = pr[j] if j < len(pr) else None
        if l and paar.get(sleutel(l[0])) is not None and r and paar[sleutel(l[0])] == sleutel(r[0]):
            kl.sluit_tot(l[1]); kr.sluit_tot(r[1])
            extra = 16 if r[2] is not None and r[1] == 0 else 0
            yy = max(kl.cursor, kr.cursor + extra)
            kl.plaats(l[0], l[1], yy); kr.plaats(r[0], r[1], yy)
            i += 1; j += 1
        elif l and paar.get(sleutel(l[0])) is None:
            kl.sluit_tot(l[1]); kl.plaats(l[0], l[1], kl.cursor); i += 1
        elif r and sleutel(r[0]) not in doelen or (r and l is None):
            kr.sluit_tot(r[1])
            kr.plaats(r[0], r[1], kr.cursor + (16 if r[2] is not None and r[1] == 0 else 0)); j += 1
        else:
            return None
    kl.sluit_tot(0); kr.sluit_tot(0)

    def teken_kolom(plat, x0):
        out, lijnen_svg, vorige = "", "", None
        for it, diepte, rel in plat:
            x = x0 + 14 * diepte
            w, kop, _ = _maat(it)
            fill, line, lk = _kleur(it, uitzonderingen)
            if [k for k in it.get("kinderen", []) if "type" in k]:
                extra = _extra(it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()))
                regels = afbreken(it["instantie"], INSTANTIE_MAX_BREEDTE)
                out += box(x, it["_y"], w, it["_bodem"] - it["_y"], fill, line, 0, it.get("aanname", False), dik=it.get("focus", False))
                out += icon("object", x + w - 22, it["_y"] + 5) + text(x + 10, it["_y"] + 18, it["type"], 12, fill=lk)
                for k, regel in enumerate(regels):
                    out += text(x + 10, it["_y"] + 36 + 18 * k, regel, 14, True)
                voet = it["_y"] + 36 + 18 * (len(regels) - 1)
                for k, e in enumerate(extra):
                    out += text(x + 10, voet + 17 + 17 * k, e, 12, fill=MUTED)
            else:
                svg, w, _ = element(x, it["_y"], "object", it["type"], it["instantie"], fill, line, lk, 0, it.get("aanname", False),
                                    it.get("toestand"), it.get("verwijzing"), it.get("verwijzingen", ()), dik=it.get("focus", False))
                out += svg
            POSITIES[(it["type"], it["instantie"])] = (x, it["_y"], w)
            if diepte == 0:
                if rel is not None and vorige is not None:
                    lijnen_svg += relatielijn_v(x0 + 60, vorige, it["_y"], rel.get("soort", "Association"), rel["relatie"], rel.get("naar_rechts", True))
                vorige = it["_bodem"]
        return out + lijnen_svg

    hoogte = max([it["_bodem"] for it, _, _ in pl + pr] + [y]) - y
    return teken_kolom(pl, lx), teken_kolom(pr, rx), hoogte


def _regel_herkomst(blok, uitzonderingen):
    """Een beeld met een kolom eerder ontstaan: links de processtap waarin het object ontstond met zijn
    objecten, rechts de processtap van dit beeld met wat hier ontstaat, en per relatie een lijn ertussen.
    De lagen die bij elkaar horen staan op dezelfde hoogte."""
    y0 = 10 + KOP
    kop = blok.get("herkomst_kop")
    POSITIES.clear()
    # links: de processtap van herkomst, of een kaal label als de kolom uit meer beelden komt
    if kop:
        lwie, lww, lwh = element(12, y0, "rol", "rol", kop["wie"] or "", BUS, BUS_L, BUS_T, 8)
        lstap, lsw, lsh = element(12 + lww + 10, y0, "proces", "processtap", kop["stap"], BUS, BUS_L, BUS_T, 8,
                                  verwijzing=f"eerder ontstaan, in {kop['beeld_id']}")
        links_kop, links_rand, links_h = lwie + lstap, 12 + lww + 10 + lsw, max(lwh, lsh)
    else:
        links_kop, links_rand, links_h = text(12, y0 + 16, "Eerder ontstaan", 12, fill=MUTED), 12 + tw("Eerder ontstaan", 12), 22
    lijnen = blok.get("herkomstlijnen") or []
    labelw = max((tw(l["label"], 10) for l in lijnen), default=0)
    goot = 16 + HERKOMST_BAAN * len(lijnen) + labelw + 24
    lx = 40
    bw = max([_maat(it)[0] for it in blok["bestaand"]] + [0])
    rx = max(lx + bw + goot, links_rand + 58)
    rwie, rww, rwh = element(rx - 28, y0, "rol", "rol", blok["wie"] or "", BUS, BUS_L, BUS_T, 8)
    verdieping = f"verdieping: {blok['verdieping']}" if blok.get("verdieping") else None
    rstap, rsw, rsh = element(rx - 28 + rww + 10, y0, "proces", "processtap", blok["stap"], BUS, BUS_L, BUS_T, 8,
                              verwijzing=verdieping or "ontstaat hier")
    kop_h = max(links_h, rwh, rsh)
    oy = y0 + kop_h + 24
    gelijk = _uitgelijnd(lx, rx, oy, blok["bestaand"], blok["objecten"], lijnen, uitzonderingen)
    if gelijk:
        lsvg, rsvg, oh = gelijk
        rw = max([_maat(it)[0] for it in blok["objecten"] if "type" in it] + [0])
    else:
        POSITIES.clear()
        lsvg, bw, bh = objecten(lx, oy, blok["bestaand"], uitzonderingen)
        rx = max(rx, lx + bw + goot)
        rsvg, rw, rh = objecten(rx, oy, blok["objecten"], uitzonderingen)
        oh = max(bh, rh)
    haken = ""
    # de ophanging loopt tot het eerste object van de kolom; door het uitlijnen begint die soms lager
    eerste = lambda items: next((POSITIES.get((it["type"], it["instantie"])) for it in items if "type" in it), None)
    for hx, top, items in ((lx + 24, y0 + links_h, blok["bestaand"]), (rx + 24, y0 + kop_h, blok["objecten"])):
        if items is blok["bestaand"] and not kop:
            continue
        doel = (eerste(items) or (0, oy, 0))[1]
        haken += (f'<path d="M{hx} {top} V{doel - 4}" stroke="{BUS_L}" stroke-width="1.5" stroke-dasharray="3 3"/>'
                  f'<path d="M{hx - 5} {doel - 10} l5 6 5 -6" fill="none" stroke="{BUS_L}" stroke-width="1.5"/>')
    herkomst = _herkomstlijnen(blok, lx + bw)
    zin_y = oy + oh + 22
    zin, zw, zh = alinea(12, zin_y, blok.get("zin", ""), 14, min(ZIN_MAX_BREEDTE, max(360, rx + rw - 12)))
    W = max(rx - 28 + rww + 10 + rsw + 12, rx + rw + 12, 12 + zw + 12)
    H = zin_y + zh + 12
    return wrap(W, H, links_kop + rwie + rstap + haken + lsvg + rsvg + herkomst + zin, titel=beeldtitel(blok))


def regel_ontstaat(blok, uitzonderingen):
    """Bovenaan de rol en de processtap; eronder, aan een stippellijn, de objecten die ontstaan of
    veranderen, met hun relaties; te brede ketens gaan in een kolom."""
    if blok.get("bestaand"):
        return _regel_herkomst(blok, uitzonderingen)
    y0 = 10 + (KOP if blok.get("beeld") else 0)
    wie, ww, wh = element(12, y0, "rol", "rol", blok["wie"] or "", BUS, BUS_L, BUS_T, 8)
    x = 12 + ww + 10
    verdieping = f"verdieping: {blok['verdieping']}" if blok.get("verdieping") else None
    stap, sw, sh = element(x, y0, "proces", "processtap", blok["stap"], BUS, BUS_L, BUS_T, 8, verwijzing=verdieping)
    kop_h = max(wh, sh)
    ox, oy = 40, y0 + kop_h + 24
    objs, ow, oh = objecten(ox, oy, blok["objecten"], uitzonderingen)
    # de ophanging: van de processtap naar de objecten
    hx = ox + 24
    haak = (f'<path d="M{hx} {y0 + kop_h} V{oy - 4}" stroke="{BUS_L}" stroke-width="1.5" stroke-dasharray="3 3"/>'
            f'<path d="M{hx - 5} {oy - 10} l5 6 5 -6" fill="none" stroke="{BUS_L}" stroke-width="1.5"/>')
    zin_y = oy + oh + 22
    concept = blok.get("plaat") == "onderwijsontwerp"
    chip, zin_x = "", 12
    if concept:
        # een verdieping op de conceptplaat: gestippelde rand en een chip voor de zin
        tekst = f"conceptplaat: {CONCEPTPLAAT}"
        cw = tw(tekst, 12) + 16
        chip = box(12, zin_y - 14, cw, 19, "#ffffff", "#c8ccc9", 9, True, "2 2") + text(20, zin_y, tekst, 12, fill=MUTED)
        zin_x = 12 + cw + 10
    zin, zw, zh = alinea(zin_x, zin_y, blok.get("zin", ""), 14, min(ZIN_MAX_BREEDTE, max(360, ox + ow - zin_x)))
    W = max(x + sw + 12, ox + ow + 12, zin_x + zw + 12)
    H = zin_y + zh + 12
    return wrap(W, H, wie + stap + haak + objs + chip + zin, dashed=concept, titel=beeldtitel(blok))


def regel_stroomt(blok, uitzonderingen):
    """De stroom: bovenaan de pijl van component naar component als horizontale stippellijn, met de
    koppeling-ID en de processtap; eronder, aan de lijn gehangen, de objecten die samen overgaan."""
    y0 = 10 + (KOP if blok.get("beeld") else 0)
    lijn = 34
    idtekst = blok.get("koppeling") or ("geen pijl op de hoofdplaat" if blok.get("pijl") == "geen pijl op de hoofdplaat" else "zonder koppelingspecificatie")
    idw = tw(idtekst, 12) + 16
    s = box(12, y0 + 14, idw, 19, "#ffffff", "#c8ccc9", 4) + text(20, y0 + 27, idtekst, 12, fill=MUTED)
    x = 12 + idw + 12
    van, vw, vh = element(x, y0, "component", "van", blok["van"], APP, APP_L, APP_T)
    s += van
    x_lijn = x + vw + 6
    # de objecten onder de lijn, iets ingesprongen; ze hangen met een stippellijn aan de pijl
    ox, oy = 40, y0 + vh + 34
    osvg, ow, oh, rijen = _objecten_rijen(ox, oy, blok["objecten"], uitzonderingen)
    naar, nw, nh = element(0, 0, "component", "naar", blok["naar"], APP, APP_L, APP_T)
    stap_tekst = "na: " + blok["stap"]
    stapw = tw(stap_tekst, 12) + 16
    x_naar = max(x_lijn + 240, ox + ow - nw)
    s += f'<path d="M{x_lijn} {y0+24}H{x_naar - 10}" stroke="{APP_T}" stroke-width="2" stroke-dasharray="5 4"/>'
    s += f'<path d="M{x_naar - 12} {y0+18}l10 6-10 6z" fill="{APP_T}"/>'
    naar, nw, nh = element(x_naar, y0, "component", "naar", blok["naar"], APP, APP_L, APP_T)
    s += naar
    sx = 12
    s += box(sx, y0 + vh + 2, stapw, 19, "#ffffff", "#c8ccc9", 9, True, "2 2") + text(sx + 8, y0 + vh + 16, stap_tekst, 12, fill=MUTED)
    # de ophanging: van de pijl naar de bovenkant van de eerste rij, en langs de linkerkant van elke rij
    hx = x_lijn + 14
    s += f'<path d="M{hx} {y0+24}V{oy - 4}" stroke="{APP_T}" stroke-width="1.5" stroke-dasharray="3 3"/>'
    for ry, _ in rijen[1:]:
        s += f'<path d="M{ox + 24} {oy}V{ry - 4}" stroke="{APP_T}" stroke-width="1.5" stroke-dasharray="3 3"/>'
    s += osvg
    zin_y = oy + oh + 22
    zin, zw, zh = alinea(12, zin_y, blok.get("zin", ""), 14, min(ZIN_MAX_BREEDTE, max(360, ox + ow - 12)))
    W = max(x_naar + nw + 12, ox + ow + 12, zw + 24)
    H = zin_y + zh + 12
    body = f'<rect x="0" y="0" width="4" height="{H:.0f}" fill="{APP_L}"/>' + s + zin
    return wrap(W, H, body, titel=beeldtitel(blok))


STANDAARDLABEL = {"Specialization": "is een", "Aggregation": "bevat", "Composition": "bevat"}


def _verwijzing(rel, objecttype):
    """De tekst van een verwijzing: het label van de plaat (of een standaardlabel) en het andere eind,
    in leesrichting; met de instantie aan het andere eind als de regel die geeft."""
    ander = rel["naar"] if rel["van"] == objecttype else rel["van"]
    label = rel.get("label") or STANDAARDLABEL.get(rel["soort"], "hangt aan")
    tekst = f"{label} {ander}" if rel["van"] == objecttype else f"{ander} {label}"
    return f"{tekst}: {rel['instantie']}" if rel.get("instantie") else tekst


def _omwegen_in_blok(objecten_in_blok):
    """Hoeveel relaties over afstand dit blok al draagt."""
    return sum(1 for it in objecten_in_blok if it.get("over_afstand"))


def _types_in_blok(objecten_in_blok):
    """Alle objecttypen die al in dit blok staan, kinderen meegerekend. Een relatie naar zo'n type is
    met een omweg te tekenen; een relatie naar iets daarbuiten blijft een verwijzing."""
    uit = set()
    for it in objecten_in_blok:
        if "type" in it:
            uit.add(it["type"])
            uit |= _types_in_blok(it.get("kinderen", []))
    return uit


def _specialiseert(r):
    """De generalisatie van het object, uit relatie of relaties: een specialisatie erft de nesting van
    haar generalisatie, ook als zij met een andere relatie aan de buur hangt (F6-04)."""
    for x in [r.get("relatie") or {}] + list(r.get("relaties", [])):
        if x.get("soort") == "Specialization" and x.get("van") == r["objecttype"]:
            return x["naar"]
    return None


def _zoek_bestaand(items, objecttype, instantie=None):
    """Het bestaande object van dit type (of met dit type als generalisatie) in de kolom links, het
    laatst getoonde eerst; met instantie alleen dat ene object."""
    for it in reversed(items):
        gevonden = _zoek_bestaand(it.get("kinderen", []), objecttype, instantie)
        if gevonden is not None:
            return gevonden
        if objecttype in (it.get("type"), it.get("specialiseert")) and instantie in (None, it.get("instantie")):
            return it
    return None


def _herkomstlijn(blok, r, x):
    """Een relatie van een nieuw object naar een object in de kolom links wordt een lijn tussen de twee,
    geen verwijzing onder het object. Geeft True als dat zo is."""
    ander = x["naar"] if x["van"] == r["objecttype"] else x["van"]
    bron = _zoek_bestaand(blok.get("bestaand", []), ander, x.get("instantie"))
    if bron is None:
        return False
    blok["herkomstlijnen"].append({"bron": (bron["type"], bron["instantie"]), "doel": (r["objecttype"], r["instantie"]),
                                   "soort": x["soort"], "label": x.get("label") or "",
                                   "naar_rechts": x["naar"] == r["objecttype"]})
    return True


def groepeer(regels):
    """Regels met dezelfde fase, stap en soort worden één blok; ontstaat en verandert samen. Een regel met
    het veld verdieping vormt met zijn gelijken een eigen blok onder dezelfde stap."""
    blokken = []
    for r in regels["regels"]:
        soort = r["soort"]
        if soort == "stroomt":
            laatste = blokken[-1] if blokken else None
            item = {"type": r["objecttype"], "instantie": r["instantie"], "aanname": r.get("aanname", False),
                    "plaat": r.get("plaat", "informatiemodel"), "verwijzingen": [_verwijzing(x, r["objecttype"]) for x in r.get("relaties", [])]}
            _merk_voorstel(item, r)
            if _specialiseert(r):
                item["specialiseert"] = _specialiseert(r)
            if r.get("toestand"):
                item["toestand"] = r["toestand"]
            rel = r.get("relatie")
            if laatste and laatste["soort"] == "stroomt" and (laatste["fase"], laatste["stap"], laatste["van"], laatste["naar"], laatste.get("beeld")) == (r["fase"], r["stap"], r["van"], r["naar"], r.get("beeld")):
                buur_s = next((it for it in reversed(laatste["objecten"]) if "type" in it), None)
                in_blok_s = ({buur_s["type"]} | {k.get("type") for k in buur_s.get("kinderen", [])}) if buur_s else set()
                if rel and not rel.get("nesting"):
                    ander = rel["naar"] if rel["van"] == r["objecttype"] else rel["van"]
                    if ander in in_blok_s:
                        laatste["objecten"].append({"relatie": rel.get("label") or "", "soort": rel["soort"], "naar_rechts": rel["naar"] == r["objecttype"], "ander": ander})
                    else:
                        item["verwijzing"] = _verwijzing(rel, r["objecttype"])
                if rel and rel.get("nesting"):
                    def zoek_s(items):
                        for it in reversed(items):
                            # zoals bij ontstaan: een specialisatie erft de nesting van haar generalisatie
                            if rel["van"] in (it.get("type"), it.get("specialiseert")):
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
                            "beeld": r.get("beeld"), "beeld_id": r.get("beeld_id"),
                            "koppeling": r.get("koppeling"), "pijl": r.get("pijl"), "objecten": [item], "zin": r.get("zin", "")})
            continue
        laatste = blokken[-1] if blokken else None
        # een beeld is een blok en dus een bestand. Draagt een regel een beeld, dan telt de rol niet mee
        # in de sleutel: anders vallen de regels van hetzelfde beeld in twee blokken met dezelfde
        # bestandsnaam, en overschrijft het tweede het eerste. Zonder beeld blijft de rol de grens.
        if r.get("beeld"):
            zelfde = (laatste and laatste["soort"] == "ontstaat"
                      and (laatste["fase"], laatste["stap"], laatste.get("verdieping"), laatste.get("beeld"))
                      == (r["fase"], r["stap"], r.get("verdieping"), r["beeld"]))
        else:
            zelfde = (laatste and laatste["soort"] == "ontstaat" and not laatste.get("beeld")
                      and (laatste["fase"], laatste["stap"], laatste.get("rollen"), laatste.get("verdieping"))
                      == (r["fase"], r["stap"], [r.get("wie")], r.get("verdieping")))
        if not zelfde:
            laatste = {"soort": "ontstaat", "fase": r["fase"], "stap": r["stap"], "wie": r.get("wie"),
                       "rollen": [], "verdieping": r.get("verdieping"),
                       "beeld": r.get("beeld"), "beeld_id": r.get("beeld_id"),
                       "plaat": r.get("plaat", "informatiemodel"), "objecten": [], "zin": r.get("zin", ""),
                       "bestaand": [], "herkomstlijnen": []}
            blokken.append(laatste)
        if r.get("wie") and r["wie"] not in laatste["rollen"]:
            laatste["rollen"].append(r["wie"])
            laatste["wie"] = ", ".join(laatste["rollen"])
        if soort == "bestaat":
            # eerder ontstaan: een eigen kolom links, wit, met het beeld van herkomst; de structuur
            # (nesting) komt terug zoals zij ontstond
            item = {"type": r["objecttype"], "instantie": r["instantie"], "bestaat": True, "herkomst": r["herkomst"],
                    "aanname": r.get("aanname", False), "plaat": r.get("plaat", "informatiemodel"), "verwijzingen": []}
            if r.get("toestand"):
                item["toestand"] = r["toestand"]
            if _specialiseert(r):
                item["specialiseert"] = _specialiseert(r)
            rel = r.get("relatie")
            if rel and not rel.get("nesting"):
                item["verwijzingen"].append(_verwijzing(rel, r["objecttype"]))
            item["verwijzingen"] += [_verwijzing(x, r["objecttype"]) for x in r.get("relaties", [])]
            ouder = _zoek_bestaand(laatste["bestaand"], rel["van"]) if rel and rel.get("nesting") else None
            if ouder is not None:
                ouder.setdefault("kinderen", []).append(item)
            else:
                laatste["bestaand"].append(item)
            if r.get("zin") and not laatste["zin"]:
                laatste["zin"] = r["zin"]
            continue
        # een extra relatie waarvan het andere eind al in dit blok staat wordt een lijn met een omweg;
        # de rest blijft een verwijzing onder het object
        _reeds = _types_in_blok(laatste["objecten"])
        _ver, _omweg = [], []
        for x in r.get("relaties", []):
            if _herkomstlijn(laatste, r, x):
                continue
            _ander = x["naar"] if x["van"] == r["objecttype"] else x["van"]
            if _ander in _reeds and _de_moeite(laatste["objecten"] + _omweg, _ander, x.get("label")):
                _omweg.append({"relatie": x.get("label") or "", "soort": x["soort"],
                               "naar_rechts": x["naar"] == r["objecttype"], "ander": _ander, "over_afstand": True})
            else:
                _ver.append(_verwijzing(x, r["objecttype"]))
        laatste["objecten"] += _omweg
        item = {"type": r["objecttype"], "instantie": r["instantie"], "aanname": r.get("aanname", False),
                "plaat": r.get("plaat", "informatiemodel"), "verwijzingen": _ver}
        _merk_voorstel(item, r)
        if _specialiseert(r):
            item["specialiseert"] = _specialiseert(r)
        if r.get("toestand"):
            # ook een object dat al in een bepaalde rijpheid ontstaat draagt zijn toestand
            item["toestand"] = r["toestand"]
        rel = r.get("relatie")
        # een relatielijn loopt alleen naar het object ernaast (of een kind daarvan); een relatie naar een
        # object verder terug in het blok, of uit een eerdere stap, staat als verwijzing op het object
        buur = next((it for it in reversed(laatste["objecten"]) if "type" in it), None)
        in_blok = ({buur["type"]} | {k.get("type") for k in buur.get("kinderen", [])}) if buur else set()
        if rel and rel.get("nesting"):
            def zoek(items):
                # van achteren naar voren: een kind hangt onder het laatst getoonde object van dat type,
                # zodat een tweede eenheid haar eigen leeronderdelen krijgt
                for it in reversed(items):
                    # een specialisatie erft de nesting van haar generalisatie (Keuzedeel onder Opleidingsprogramma specificatie)
                    if rel["van"] in (it.get("type"), it.get("specialiseert")):
                        return it
                    gevonden = zoek(it.get("kinderen", []))
                    if gevonden is not None:
                        return gevonden
                return None
            ouder = zoek(laatste["objecten"])
            if ouder is not None:
                ouder.setdefault("kinderen", []).append(item)
                continue
        if rel and not rel.get("nesting") and _herkomstlijn(laatste, r, rel):
            pass
        elif rel and not rel.get("nesting"):
            ander = rel["naar"] if rel["van"] == r["objecttype"] else rel["van"]
            if ander in in_blok:
                # het andere eind staat ernaast in dit blok: relatielijn ertussen; naar_rechts als dit object het doel is
                laatste["objecten"].append({"relatie": rel.get("label") or "", "soort": rel["soort"], "naar_rechts": rel["naar"] == r["objecttype"], "ander": ander})
            elif ander in _types_in_blok(laatste["objecten"]) and _de_moeite(laatste["objecten"], ander, rel.get("label")):
                # het andere eind staat verder terug in dit blok: een lijn met een omweg in plaats van een verwijzing
                laatste["objecten"].append({"relatie": rel.get("label") or "", "soort": rel["soort"], "naar_rechts": rel["naar"] == r["objecttype"], "ander": ander, "over_afstand": True})
            else:
                item["verwijzing"] = _verwijzing(rel, r["objecttype"])
        laatste["objecten"].append(item)
        if r.get("zin") and not laatste["zin"]:
            laatste["zin"] = r["zin"]
    for blok in blokken:
        if blok.get("bestaand"):
            _herkomst_afronden(blok, regels["regels"])
    return blokken


def _alle(items):
    for it in items:
        if "type" in it:
            yield it
            yield from _alle(it.get("kinderen", []))


def _herkomst_afronden(blok, regels):
    """Boven de kolom links staat de processtap waarin het bestaande object ontstond, als dat voor de hele
    kolom een beeld is; een object uit een ander beeld draagt dan zelf "uit Fx-yy". Wat hier ontstaat
    krijgt de nadruk."""
    herkomsten = list(dict.fromkeys(it["herkomst"] for it in blok["bestaand"]))
    bron = [r for r in regels if r.get("beeld_id") == herkomsten[0]] if len(herkomsten) == 1 else []
    blok["herkomst_kop"] = ({"beeld_id": herkomsten[0], "stap": bron[0]["stap"],
                             "wie": ", ".join(dict.fromkeys(r["wie"] for r in bron if r.get("wie")))} if bron else None)
    kop = (blok["herkomst_kop"] or {}).get("beeld_id")
    def chips(items, ouder=None):
        for it in items:
            if it["herkomst"] != kop and it["herkomst"] != ouder:
                it["verwijzingen"].insert(0, f"uit {it['herkomst']}")
            chips(it.get("kinderen", []), it["herkomst"])
    chips(blok["bestaand"])
    for it in _alle(blok["objecten"]):
        it["focus"] = True


def beeldtitel(blok):
    """Het ID voor de titel, zodat een beeld kort aan te halen is: "F1-02 - Het kwalificatiedossier ontleed"."""
    return " - ".join(x for x in (blok.get("beeld_id"), blok.get("beeld")) if x) or None


def slug(tekst):
    tekst = tekst.lower().replace("ë", "e").replace("é", "e").replace("ï", "i").replace("ö", "o").replace("ü", "u")
    return re.sub(r"[^a-z0-9]+", "-", tekst).strip("-")


def bestandsnaam(blok, volgnummer=None):
    """De bestandsnaam is het beeld-ID met de titel (stabiel, leesbaar, op leesvolgorde gesorteerd);
    zonder titel de stap met een volgnummer."""
    if blok.get("beeld"):
        kop = slug(blok.get("beeld_id") or f"f{blok['fase']}")
        return f"{kop}-{slug(blok['beeld'])}.svg"
    s = slug(blok["stap"]) + ("-verdieping" if blok.get("verdieping") else "")
    return f"f{blok['fase']}-{volgnummer or 0:02d}-{s}.svg"


def _snijd():
    """tools/scripts/snijd-beeld.py als module, zodat de renderer de banen per beeld kan noemen."""
    pad = pathlib.Path(__file__).resolve().parent / "snijd-beeld.py"
    spec = importlib.util.spec_from_file_location("snijd_beeld", pad)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def teken(regels, uitmap, opruimen=False):
    """Schrijft per blok een SVG; geeft de lijst (bestandsnaam, blok).

    Een beeld is een bestand. Leveren twee blokken dezelfde naam, dan stopt dit met de namen erbij in
    plaats van het eerste bestand te overschrijven: dan verdwijnt een deel van het beeld zonder dat
    iemand het ziet. Met opruimen verdwijnt een SVG die geen blok meer draagt, zodat een beeld dat van
    naam verandert geen tweeling achterlaat.
    """
    uitzonderingen = {u["objecttype"] for u in regels.get("scope_uitzonderingen", [])}
    uitmap = pathlib.Path(uitmap)
    uitmap.mkdir(parents=True, exist_ok=True)
    uit, gezien = [], {}
    for n, blok in enumerate(groepeer(regels), 1):
        if blok["soort"] == "stroomt":
            svg = regel_stroomt(blok, uitzonderingen)
        else:
            svg = regel_ontstaat(blok, uitzonderingen)
        naam = bestandsnaam(blok, n)
        if naam in gezien:
            sys.exit(f"twee blokken leveren hetzelfde bestand {naam}: "
                     f"{gezien[naam]} en {beeldtitel(blok) or blok['stap']}; een beeld is een bestand")
        gezien[naam] = beeldtitel(blok) or blok["stap"]
        (uitmap / naam).write_text(svg, encoding="utf-8")
        uit.append((naam, blok))
    if opruimen:
        for pad in sorted(uitmap.glob("*.svg")):
            if pad.name not in gezien:
                pad.unlink()
                print(f"opgeruimd: {pad.name} draagt geen regel meer")
    return uit


def maten(uitmap, namen):
    """Per beeld de breedte, de hoogte, de hoogte van elke baan en de reden als het niet te snijden is.

    De baanhoogtes staan erbij omdat ze niet gelijk kunnen uitvallen: een snede ligt altijd in
    witruimte, dus waar een beeld dicht getekend staat liggen de grenzen vast. Ongelijke banen zijn
    daarmee een teken dat het beeld zelf te dicht is, en dat is werk aan het beeld.
    """
    snijd = _snijd()
    uit = []
    for naam in namen:
        svg = (pathlib.Path(uitmap) / naam).read_text(encoding="utf-8")
        _, _, breedte, hoogte = snijd.doek(svg)
        hoogtes = [snijd.doek(deel)[3] for deel in snijd.banen(svg, marge=0)]
        uit.append((naam, breedte, hoogte, hoogtes, snijd.knelpunt(svg)))
    return uit


def valideer(regels):
    """Wat de renderer zelf nodig heeft; de inhoudelijke controle doet controleer-leerroute-uitwerking-model.py."""
    for i, r in enumerate(regels.get("regels", []), 1):
        if r.get("soort") not in SOORTEN:
            sys.exit(f"regel {i}: soort {r.get('soort')!r} is niet ontstaat, verandert, stroomt of bestaat")
        if not r.get("instantie"):
            sys.exit(f"regel {i}: objecttype {r.get('objecttype')!r} heeft geen instantie")
        rel = r.get("relatie")
        if rel and "label" in rel and rel["label"] == "":
            sys.exit(f"regel {i}: relatielabel is leeg")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    parser.add_argument("--houd-verweesde-beelden", action="store_true",
                        help="een SVG die geen regel meer draagt laten staan; standaard verdwijnt hij")
    parser.add_argument("--stil", action="store_true", help="alleen de slotregel, zonder de maat per beeld")
    parser.add_argument("--streng", action="store_true",
                        help="eindigen met een foutcode zodra een beeld niet te snijden is; standaard is "
                             "het een melding, zodat een bestaande plaat de keten niet stillegt")
    args = parser.parse_args(argv)
    if not args.regels.exists():
        print(f"regeltabel niet gevonden: {args.regels}", file=sys.stderr)
        return 2
    regels = json.loads(args.regels.read_text(encoding="utf-8"))
    valideer(regels)
    uit = teken(regels, args.uit, opruimen=not args.houd_verweesde_beelden)
    knel = []
    for naam, breedte, hoogte, hoogtes, reden in maten(args.uit, [n for n, _ in uit]):
        if not args.stil:
            banen = f"{len(hoogtes)} {'baan' if len(hoogtes) == 1 else 'banen'}"
            verdeling = f" ({', '.join(f'{h:g}' for h in hoogtes)})" if len(hoogtes) > 1 else ""
            print(f"  {naam}: {breedte:g} bij {hoogte:g}, {banen}{verdeling}"
                  + (f", niet te snijden: {reden}" if reden else ""))
        if reden:
            knel.append(naam)
    print(f"{len(uit)} beelden getekend naar {args.uit}")
    # een planningsvorm naast de basis tekent naar dezelfde map; het beeld-ID met de letter van de vorm
    # (f6-c01-...) houdt de bestandsnamen uit elkaar. Dit gaat na de basisronde, want die ruimt een SVG
    # op die geen regel meer draagt, en de beelden van een vorm staan niet in de basistabel.
    geladen, onbekend = varianten.laad(args.regels, regels)
    for pad in onbekend:
        print(f"waarschuwing: {pad.name} is geen bekende planningsvorm en wordt niet getekend", file=sys.stderr)
    for v in geladen:
        valideer(v["tabel"])
        print(f"{len(teken(v['tabel'], args.uit))} beelden van variant {v['vorm']} getekend naar {args.uit}")
    if knel:
        print(f"{len(knel)} beelden passen niet in banen en worden op een slide te klein; voor het "
              f"document is dat geen gebrek: {', '.join(knel)}", file=sys.stderr)
        return 1 if args.streng else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
