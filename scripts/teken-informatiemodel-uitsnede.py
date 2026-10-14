#!/usr/bin/env python3
"""Een uitsnede van het informatiemodel tekenen: alleen de objecttypen die een reviewvraag raakt.

Waarom dit script bestaat: de grote informatiemodelplaat draagt tachtig objecttypen en
bijna tweehonderd relaties. Wie daarmee een vraag uit een reviewronde wil beantwoorden,
laat een lezer zoeken. Dit script tekent in plaats daarvan een uitsnede: de handvol
objecttypen die het antwoord dragen, gegroepeerd per begrippenfamilie zoals op de grote
plaat, met de gewijzigde objecten uitgelicht tegen hun context, en onder het beeld een
leeswijzer die per nummer zegt wat die stap voor de vraag betekent.

    python3 scripts/teken-informatiemodel-uitsnede.py \\
        --model architecture/model/informatiemodel/informatiemodel.json \\
        --selectie architecture/model/informatiemodel/uitsneden/public-123-minor.json \\
        --uit architecture/model/informatiemodel/img/uitsneden

De vormtaal komt uit `teken-voorbeeldregels.py` en wordt daar ongewijzigd uit geleend:
dezelfde kleuren, hetzelfde pictogram, dezelfde ruit, driehoek en pijlpunt. De opmaak is
eigen, want die van dat script hangt aan de regeltabel van de voorbeelduitwerking.

De ordening van het beeld, in twee assen:

- van links naar rechts de begrippenfamilies in de volgorde van de grote plaat, elk als
  ArchiMate-groepering met de familienaam op een tab, zodat de kolom herkenbaar blijft;
- van boven naar beneden rijen die de auteur van de uitsnede kiest. Een rij hoort bij een
  onderwerp (het keuzedeel, het generieke opleidingsprogramma, de minor), zodat de
  specialisatie van een bijzonder geval naar zijn algemene type een rechte lijn wordt.
  Staat het algemene type tussen zijn twee bijzondere gevallen in, dan leest het beeld
  wat de vraag vraagt: zij staan naast elkaar en niet onder elkaar.

Op de grote plaat is `Resultaatstructuur` een band onder de kolommen en zweeft een handvol
objecttypen zonder kolom erboven. `Resultaatstructuur` krijgt hier een eigen groepering
rechts in de rij van kolommen; de objecttypen zonder kolom krijgen een band boven de
kolommen, met `Boven de kolommen` op de tab.

Die band is geen restbak maar een ontwerpregel: een objecttype zonder kolom is vaak de
verbindende factor tussen de ene en de andere kolom. `Aanmelding` verbindt aanbod en
verbintenis, want zij is de intentie om deel te nemen; de inschrijving formaliseert die
intentie en staat daarom wel binnen de verbintenis. Zo ook `Verzoek tot Aanbod /
Intekening op specificatie`: de brug tussen de specificatie en het aanbod. Elk vak in de
band komt daarom boven de kolomgrens te staan die het overbrugt, afgeleid uit zijn
relaties: de kolommen van zijn buren in de uitsnede, en zonder zulke buur de kolommen van
zijn buren in het hele model die in de uitsnede voorkomen. Een vak zonder af te leiden
grens komt midden boven het raster.

Wat de band bewust niet doet: zij trekt geen lijn naar een vak in een kolom. Zo'n lijn zou
door de tab van die kolom heen zakken en een eigen stelsel banen in de goot vragen; een
relatie tussen de band en een kolom wordt daarom een verwijzing in het vak en staat in de
melding. Wie die lijn wel wil, geeft het objecttype in de selectie een expliciete `kolom`;
dan staat het in die kolom en loopt de relatie als gewone lijn.

Een gewijzigd objecttype draagt niet dat het gewijzigd is maar wat er met hem gebeurde: het
veld `merk` is een opsomming van soorten wijziging (`toegevoegd`, `verwijderd`, `hernoemd`,
`binnen scope`, `buiten scope`, `herplaatst`). De korte naam staat achter het nummer in het
vak, de hele uitleg in de legenda. De oude waarden `nieuw` en `anders` zijn vervallen; het
script weigert ze met de soorten erbij, want zij zeggen dat er iets veranderde en niet wat.

Twee keuzes die een lezer anders op het verkeerde been zetten:

- grijs volgt `scope`, met een uitzondering voor de expliciete standaardgeel `#ffffb5`.
  De generator van `informatiemodel.json` leidt de scope af uit de vulkleur en merkt
  daardoor elk vak met een vulkleur als buiten scope aan, ook de drie leslaag-objecten
  die op de plaat juist geel zijn. Tekenen op `scope` alleen zet die drie grijs.
- een relatie die het model niet draagt wordt niet stil weggelaten en niet stil
  bijgetekend: zij komt als gestippelde lijn in de accentkleur met het woord `ontbreekt`
  erbij, en het script weigert een `ontbreekt` die wel in het model staat.

Een relatie tussen twee gekozen objecttypen die niet als haakse lijn te lopen is, wordt
een verwijzing in het vak ("Keuzedeel aanbod volgt") en komt in de melding te staan. Zo
verdwijnt zij niet uit het beeld en blijft elke lijn horizontaal of verticaal.

Een relatie van een objecttype naar zichzelf wordt een haakse lus aan de rechterrand van
het vak, met de ArchiMate-kop erop: de open ruit van de aggregatie staat op de bovenste
poot. De lus ligt in de strook die het vak rechts voor zijn pictogram vrijhoudt. Dat is
geen esthetische keuze maar een meetbare: tussen de vakken lopen de horizontale banen en
door de rijgoot de verticale, en geen van beide komt ooit binnen een vak. Een lus die
binnen zijn eigen vak blijft, levert daarmee per constructie geen kruising op, ook niet
wanneer drie vakken naast elkaar er een dragen.

Een vraag als "kan een leeruitkomst het niveau van een competentie uitdrukken?" is met
structuur alleen niet beantwoord. Een selectie mag daarom een `voorbeeld` meegeven: een
ingevuld geval, letterlijk overgenomen uit een bestaand bestand en met zijn vindplaats erbij,
dat als eigen blok rechts naast de kolommen komt te staan. Het blok draagt de zin, de delen
van de vorm onder elkaar, het niveau in de accentkleur als metagegeven ernaast, en onderaan
de vindplaats. Het staat naast het raster en niet eronder, want het is het antwoord en geen
uitleg bij de plaat; zonder vindplaats weigert het script, want een voorbeeld zonder herkomst
is een verzinsel.

De tekst onder het beeld is begrensd, want een uitsnede die zichzelf in proza uitlegt is
geen plaat meer. Per genummerd objecttype staat er een regel van hoogstens twaalf woorden
(de naam meegerekend), de legenda legt de vormtaal uit, en alles bij elkaar blijft onder
MAX_ONDERREGELS regels. Wat niet in zo'n regel past hoort in het beeld: een rijlabel, een
label op een relatie of een tegel in de legenda. Een losse alinea onder het beeld bestaat
niet meer; het script weigert een selectie die er een meegeeft.

Het model wordt alleen gelezen; raak nooit een .archimate-bestand aan.
"""

import argparse
import difflib
import html
import importlib.util
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("teken_voorbeeldregels", WORTEL / "teken-voorbeeldregels.py")
vt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vt)

tw, icon, box, text, slug = vt.tw, vt.icon, vt.box, vt.text, vt.slug
BUS, BUS_L, BUS_T = vt.BUS, vt.BUS_L, vt.BUS_T
GRIJS, GRIJS_L, GRIJS_T = vt.GRIJS, vt.GRIJS_L, vt.GRIJS_T
INK, MUTED, LIJN = vt.INK, vt.MUTED, vt.LIJN

MODEL = pathlib.Path("architecture/model/informatiemodel/informatiemodel.json")
UIT = pathlib.Path("architecture/model/informatiemodel/img/uitsneden")

ACCENT = "#d9531e"            # dezelfde accentkleur als scripts/teken-hoofdplaat-highlight.py
RELATIE = "#444"
KOL_VUL, KOL_RAND, KOL_TAB = "#f4f4f4", "#d8ddda", "#e4e4dc"

BAND_NAAM = "Boven de kolommen"   # de tab van de band met de objecttypen zonder kolom
BAND_RIJ = -1                     # hun rij-index: boven rij 0, buiten de rijen van het raster
# De kolomvolgorde van de grote plaat. Het kwalificatiekader staat er onder beide namen in:
# in het model is `Kwalificatiekader MBO` hernoemd naar `Kwalificatiekader` met MBO en HO als
# subgroepen, en een uitsnede moet op een oudere en een verse informatiemodel.json werken.
KOLOMVOLGORDE = ["Kwalificatiekader", "Kwalificatiekader MBO",
                 "Onderwijskundigkader instelling", "Onderwijsspecificatie", "Onderwijsaanbod",
                 "Onderwijsverbintenis", "Onderwijsresultaat", "Resultaatstructuur"]

MIN_VAK, TEKST_B = 168, 200          # vakbreedte en de breedte waarop een naam afbreekt
VAK_MARGE_L, VAK_PICTOGRAM = 10, 32  # links de tekst, rechts het pictogram
NAAM_MAAT, NAAM_REGEL = 13, 18
NOOT_MAAT, NOOT_REGEL = 11, 16
LABEL_MAAT, LABEL_B = 10, 160        # relatielabel en de breedte waarop het afbreekt
MIN_VAK_H = 40
LUS_B, LUS_H, LUS_GAT = 24, 20, 6    # de lus van een relatie op zichzelf, rechts in het vak
LUS_MARGE = 12                       # de onderste poot ligt zoveel boven de onderrand
LUS_VAK_H = 60                       # een vak met een lus draagt haar onder het pictogram
CEL_GAT = 24                         # twee vakken naast elkaar in dezelfde cel
KOL_MARGE, KOL_GOOT, KOL_TAB_H = 14, 56, 24
BAND_GOOT = 28                       # tussen de onderrand van de band en de tabs van de kolommen
RIJ_GOOT, BAAN, OMWEG_BAAN = 56, 18, 14
DOEK_MARGE = 16
TITEL_MAAT, HERKOMST_MAAT, LEES_MAAT, LEGENDA_MAAT = 17, 12, 13, 11
LEES_GOOT = 14                       # de goot tussen de naamkolom en de redenkolom eronder
MAX_VERWIJZINGEN = 2                 # meer verwijzingen op een vak maken het vak een alinea
VB_MARGE, VB_REGEL = 14, 17          # het voorbeeldblok naast het raster
VB_MAAT, VB_ZIN_MAAT, VB_BRON_MAAT = 12, 13, 10
VB_B = 300                           # de breedte waarop de zin en de slotregel afbreken
VB_LABEL_GOOT = 14                   # tussen de naam van een deel en zijn waarde
MAX_VB_DELEN = 7                     # meer delen maken van de ontleding een tabel
MAX_VB_WOORDEN = 8                   # woorden in de waarde van een deel
MAX_VB_ZINWOORDEN = 20               # woorden in de voorbeeldzin zelf

MAX_VAKKEN, MAX_KOLOMMEN, MAX_RIJEN = 24, 8, 6
MAX_LEESWOORDEN = 12                 # woorden in de regel onder het beeld, de naam meegerekend
MAX_ONDERREGELS = 8                  # regels tekst onder het beeld, de legenda meegerekend

# De soorten wijziging die een modelronde oplevert, elk met de korte naam in het vak en de
# uitleg in de legenda. De opsomming volgt de ronde zelf: het kwalificatiekader van het hoger
# onderwijs en de minor zijn toegevoegd, het cohort is van de student naar de inschrijving
# verhuisd, de leslaag is op de specificatie buiten scope geplaatst en op het aanbod en de
# verbintenis juist erbinnen gehaald, en twee objecttypen zijn hernoemd. `verwijderd` hoort
# erbij omdat een ronde ook objecttypen opruimt.
# De legenda-uitleg opent met het woord dat in het vak staat: de tegels dragen alle dezelfde
# oranje rand, dus het woord is wat een lezer van het vak naar de tegel brengt.
MERKEN = {"toegevoegd": ("toegevoegd", "toegevoegd: nieuw in het model"),
          "verwijderd": ("verwijderd", "verwijderd: uit het model gehaald"),
          "hernoemd": ("hernoemd", "hernoemd: dezelfde plek, een andere naam"),
          "binnen scope": ("binnen scope", "binnen scope: binnen scope van OKx geplaatst"),
          "buiten scope": ("buiten scope", "buiten scope: buiten scope van OKx geplaatst"),
          "herplaatst": ("herplaatst", "herplaatst: aan een ander objecttype gehangen")}
# De oude merken zeiden dat er iets veranderde en niet wat; zij wijzen nu naar een soort.
VERVALLEN_MERKEN = {"nieuw": "toegevoegd", "anders": "herplaatst, binnen scope of buiten scope"}
GESTIPPELD = {"Access": "4 3", "Realization": "4 3", "Influence": "6 4"}
VORMNAAM = {"Specialization": "specialisatie: een bijzonder geval van het algemenere type",
            "Aggregation": "aggregatie: het geheel bestaat uit deze delen",
            "Composition": "compositie: het geheel bestaat uit deze delen",
            "Association": "associatie: inhoudelijke samenhang",
            "Access": "toegang: gebruikt of wijzigt dit objecttype",
            "Realization": "realisatie",
            "Influence": "invloed"}
LUS_VORMNAAM = {"Aggregation": "aggregatie op zichzelf: delen van hetzelfde type",
                "Composition": "compositie op zichzelf: delen van hetzelfde type",
                "Association": "associatie op zichzelf"}


class Fout(Exception):
    """Een uitsnede die niet te tekenen is; main zet de melding om in een foutcode."""


def norm(s):
    """Een naam met genormaliseerde witruimte, voor vergelijken. Getekend wordt de naam zelf."""
    return " ".join(str(s or "").split())


# ----------------------------------------------------------------- vormtaal --

def afbreken(tekst, maxw, size, bold=False):
    """Een naam over meer regels als hij breder wordt dan maxw; een woord dat zelf breder is
    krijgt een eigen regel, zodat de tekst nooit halverwege een woord afbreekt."""
    regels, huidige = [], ""
    for woord in str(tekst).split():
        proef = (huidige + " " + woord).strip()
        if huidige and tw(proef, size, bold) > maxw:
            regels.append(huidige)
            huidige = woord
        else:
            huidige = proef
    if huidige:
        regels.append(huidige)
    return regels or [""]


def _kop_h(x, y, soort, naar, kleur):
    """De kop van een relatie op een horizontaal been. naar is +1 als de relatie naar rechts loopt.

    Elke kop draagt een eigen vulkleur. Dat is niet alleen de ArchiMate-vorm, het houdt de
    kop ook buiten de meting van keur-plaat.py, die alleen paden zonder vulling narekent.
    """
    if soort in ("Aggregation", "Composition"):
        vul = kleur if soort == "Composition" else "#ffffff"
        return (f'<path d="M{x:.0f} {y:.0f}l{7 * naar} -5l{7 * naar} 5l{-7 * naar} 5z" '
                f'fill="{vul}" stroke="{kleur}" stroke-width="1.3"/>')
    if soort in ("Specialization", "Realization"):
        return (f'<path d="M{x:.0f} {y:.0f}l{-10 * naar} -6v12z" '
                f'fill="#ffffff" stroke="{kleur}" stroke-width="1.3"/>')
    return f'<path d="M{x:.0f} {y:.0f}l{-8 * naar} -4v8z" fill="{kleur}"/>'


def _kop_v(x, y, soort, naar, kleur):
    """De kop van een relatie op een verticaal been. naar is +1 als de relatie omlaag loopt."""
    if soort in ("Aggregation", "Composition"):
        vul = kleur if soort == "Composition" else "#ffffff"
        return (f'<path d="M{x:.0f} {y:.0f}l-5 {7 * naar}l5 {7 * naar}l5 {-7 * naar}z" '
                f'fill="{vul}" stroke="{kleur}" stroke-width="1.3"/>')
    if soort in ("Specialization", "Realization"):
        return (f'<path d="M{x:.0f} {y:.0f}l-6 {-10 * naar}h12z" '
                f'fill="#ffffff" stroke="{kleur}" stroke-width="1.3"/>')
    return f'<path d="M{x:.0f} {y:.0f}l-4 {-8 * naar}h8z" fill="{kleur}"/>'


def _been(d, soort, accent):
    """Het been van een relatie, met een witte onderlaag als het uitgelicht is."""
    kleur = ACCENT if accent else RELATIE
    breed = 2.6 if accent else 1.3
    streep = f' stroke-dasharray="{GESTIPPELD[soort]}"' if soort in GESTIPPELD else ""
    uit = ""
    if accent:
        uit += f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="7" stroke-opacity="0.9"/>'
    return uit + f'<path d="{d}" fill="none" stroke="{kleur}" stroke-width="{breed}"{streep}/>'


def _ontbrekend_been(d):
    """Een relatie die het verhaal belooft en het model nog niet draagt: gestippeld in de
    accentkleur, zodat het gat in het model zichtbaar is in plaats van weggelaten."""
    return (f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="7" stroke-opacity="0.9"/>'
            f'<path d="{d}" fill="none" stroke="{ACCENT}" stroke-width="2.6" stroke-dasharray="6 5"/>')


def _label(x, y, regels, accent, anker="middle"):
    kleur = ACCENT if accent else MUTED
    hoog = len(regels) * (LABEL_MAAT + 2)
    return "".join(text(x, y - hoog + 2 + i * (LABEL_MAAT + 2), r, LABEL_MAAT, fill=kleur, anchor=anker)
                   for i, r in enumerate(regels))


def relatie_h(x_bron, x_doel, y, soort, labelregels=(), accent=False, ontbreekt=False):
    """Een horizontale relatie tussen twee vakken op dezelfde rij. Geeft (svg, segmenten).

    Elke relatie draagt een kop, net als op een verticaal been: de ruit van de aggregatie aan
    de kant van het geheel, elke andere kop aan de kant van het doel. Een associatie zonder
    label liet die kop eerder weg, waarmee dezelfde soort relatie liggend anders las dan
    staand en de legenda een pijlpunt beloofde die op het beeld ontbrak.
    """
    kleur = ACCENT if accent else RELATIE
    naar = 1 if x_doel > x_bron else -1
    d = f"M{x_bron:.0f} {y:.0f}H{x_doel:.0f}"
    svg = _ontbrekend_been(d) if ontbreekt else _been(d, soort, accent)
    if soort in ("Aggregation", "Composition"):
        svg += _kop_h(x_bron, y, soort, naar, kleur)
    else:
        svg += _kop_h(x_doel, y, soort, naar, kleur)
    if labelregels:
        svg += _label((x_bron + x_doel) / 2, y - 5, list(labelregels), accent)
    return svg, [((x_bron, y), (x_doel, y))]


def relatie_v(x_bron, y_bron, x_doel, y_doel, baan, soort, labelregels=(), accent=False, ontbreekt=False):
    """Een verticale relatie tussen twee vakken in dezelfde kolom op aangrenzende rijen.

    Liggen de twee vakken niet op dezelfde x, dan loopt het been met twee haakse knikken via
    een baan in de rijgoot. Geeft (svg, segmenten).

    Het label hangt altijd in de rijgoot. Bij een omweg is dat de baan zelf; bij een recht been
    is het het midden tussen de twee aanhechtingen. Dat midden is geen schoonheidskeuze: hecht
    de bron aan op haar bovenrand, dan ligt haar aanhechting tegen een vak aan en verdwijnt het
    opschrift onder de vulling van dat vak, want de vakken worden over de relaties heen
    getekend.
    """
    kleur = ACCENT if accent else RELATIE
    naar = 1 if y_doel > y_bron else -1
    if abs(x_doel - x_bron) < 0.5:
        d = f"M{x_bron:.0f} {y_bron:.0f}V{y_doel:.0f}"
        segmenten = [((x_bron, y_bron), (x_bron, y_doel))]
        knik, label_y = y_bron, (y_bron + y_doel) / 2
    else:
        d = f"M{x_bron:.0f} {y_bron:.0f}V{baan:.0f}H{x_doel:.0f}V{y_doel:.0f}"
        segmenten = [((x_bron, y_bron), (x_bron, baan)), ((x_bron, baan), (x_doel, baan)),
                     ((x_doel, baan), (x_doel, y_doel))]
        knik, label_y = baan, baan
    svg = _ontbrekend_been(d) if ontbreekt else _been(d, soort, accent)
    if soort in ("Aggregation", "Composition"):
        svg += _kop_v(x_bron, y_bron, soort, 1 if knik > y_bron else -1, kleur)
    else:
        svg += _kop_v(x_doel, y_doel, soort, naar, kleur)
    if labelregels:
        svg += _label(max(x_bron, x_doel) + 8, label_y + 4 + len(labelregels) * (LABEL_MAAT + 2),
                      list(labelregels), accent, anker="start")
    return svg, segmenten


def relatie_lus(e, soort, volgnummer=0):
    """Een relatie van een objecttype naar zichzelf: een haakse lus aan de rechterrand van het
    vak, in de strook die het vak voor zijn pictogram vrijhoudt. Geeft (svg, segmenten).

    De lus blijft binnen het vak, en binnen een vak loopt nooit een andere lijn; zo kruist zij
    per constructie niets. De kop staat op de bovenste poot: de open ruit van de aggregatie aan
    de kant van het geheel, wat bij een relatie op zichzelf hetzelfde vak is.

    De lus krijgt geen accentkleur. Het vak eromheen draagt die al, en de witte onderlaag van
    een accentlijn zou binnen het vak een gat in de vulling slaan.
    """
    rechts = e["x"] + e["w"]
    links = rechts - LUS_B
    onder = e["y"] + e["vak_h"] - LUS_MARGE - volgnummer * (LUS_H + LUS_GAT)
    boven = onder - LUS_H
    d = f"M{rechts:.0f} {boven:.0f}H{links:.0f}V{onder:.0f}H{rechts:.0f}"
    svg = _been(d, soort, False)
    if soort in ("Aggregation", "Composition"):
        svg += _kop_h(rechts, boven, soort, -1, RELATIE)
    else:
        svg += _kop_h(rechts, onder, soort, 1, RELATIE)
    return svg, [((rechts, boven), (links, boven)), ((links, boven), (links, onder)),
                 ((links, onder), (rechts, onder))]


def kruisingen(segmenten):
    """De plekken waar een liggend segment een staand doorsnijdt, met dezelfde regel als
    keur-plaat.py: alleen een snijpunt binnenin beide segmenten telt mee."""
    liggend, staand = [], []
    for n, ((x1, y1), (x2, y2)) in enumerate(segmenten):
        if abs(y1 - y2) <= 0.5 and abs(x1 - x2) > 0.5:
            liggend.append((y1, min(x1, x2), max(x1, x2), n))
        elif abs(x1 - x2) <= 0.5 and abs(y1 - y2) > 0.5:
            staand.append((x1, min(y1, y2), max(y1, y2), n))
    return [(x, y) for y, van, tot, a in liggend for x, boven, onder, b in staand
            if a != b and van + 0.5 < x < tot - 0.5 and boven + 0.5 < y < onder - 0.5]


# -------------------------------------------------------------------- inlezen --

def lees(model_pad, selectie_pad):
    model = json.loads(pathlib.Path(model_pad).read_text(encoding="utf-8"))
    selectie = json.loads(pathlib.Path(selectie_pad).read_text(encoding="utf-8"))
    return model, selectie


def objecten_van(model):
    return {norm(o["naam"]): o for o in model.get("objecttypen", [])}


def kleuren(obj):
    """De vulling, de randkleur en de kleur van het kolomlabel van een vak.

    Buiten scope wordt grijs. De uitzondering is de expliciete standaardgeel `#ffffb5`: de
    generator van informatiemodel.json leidt de scope uit de vulkleur af en merkt elk vak
    met een vulkleur als buiten scope aan, terwijl die drie vakken op de releasebare plaat
    geel zijn. De vulkleur van het model gaat daar dus voor op het afgeleide veld.
    """
    if obj.get("scope") == "buiten" and norm(obj.get("vulkleur")) != BUS:
        return GRIJS, GRIJS_L, GRIJS_T
    return BUS, BUS_L, BUS_T


def _controleer_namen(namen, objecten):
    onbekend = []
    for n in namen:
        if norm(n) not in objecten:
            dichtbij = difflib.get_close_matches(norm(n), objecten, 1, 0.6)
            erbij = f" (lijkt op {dichtbij[0]!r})" if dichtbij else ""
            onbekend.append(f"{n!r}{erbij}")
    if onbekend:
        raise Fout("deze namen staan niet in het model: " + "; ".join(onbekend)
                   + ". Draai eerst python3 scripts/genereer-informatiemodel-doc.py als het "
                     "model net gewijzigd is; een hernoeming valt hier als onbekende naam op.")


def _controleer_waarom(e):
    """De regel onder het beeld blijft een regel. Geteld worden de woorden die getekend
    worden: de naam van het objecttype en de reden erachter; het nummer en het streepje zijn
    opmaak en tellen niet mee."""
    if not e.get("waarom"):
        return
    woorden = len(norm(e["naam"]).split()) + len(norm(e["waarom"]).split())
    if woorden > MAX_LEESWOORDEN:
        raise Fout(f"{e['naam']!r}: de regel onder het beeld telt {woorden} woorden "
                   f"(hoogstens {MAX_LEESWOORDEN}, de naam meegerekend). Kort de waarom in tot "
                   "wat de lezer op het beeld moet zien, en laat de onderbouwing in het issue "
                   "staan")


def _controleer_toelichting(selectie):
    """Een uitsnede legt zichzelf uit met vorm, niet met een alinea eronder."""
    if norm(selectie.get("toelichting")):
        raise Fout("de selectie draagt een toelichting; die alinea onder het beeld bestaat niet "
                   "meer. Zet wat zij zegt in het beeld zelf: een rij krijgt een rij_label, een "
                   "relatie een label, een gewijzigd objecttype een waarom van hoogstens "
                   f"{MAX_LEESWOORDEN} woorden, en de vormtaal staat in de legenda")


def _controleer_merk(e, objecten):
    """Het merk als soort wijziging. Een vervallen merk wijst naar de soort die het vervangt.

    `verwijderd` is de enige soort waarbij de naam juist niet in het model hoort te staan; zij
    kan daarom geen kolom en geen scope uit het model halen en krijgt die van de auteur.
    """
    merk = e.get("merk")
    if merk is None:
        return
    if merk in VERVALLEN_MERKEN:
        raise Fout(f"{e['naam']!r}: merk {merk!r} is vervallen, want het zegt dat er iets "
                   f"veranderde en niet wat. Kies {VERVALLEN_MERKEN[merk]} of een andere soort "
                   f"uit {sorted(MERKEN)}")
    if merk not in MERKEN:
        raise Fout(f"{e['naam']!r}: merk {merk!r} is niet een van {sorted(MERKEN)}")
    if merk != "verwijderd":
        return
    if norm(e["naam"]) in objecten:
        raise Fout(f"{e['naam']!r}: merk 'verwijderd' terwijl het objecttype nog in het model "
                   "staat; kies de soort die bij de wijziging hoort")
    if not e.get("kolom"):
        raise Fout(f"{e['naam']!r}: een verwijderd objecttype staat niet meer in het model en "
                   "haalt zijn kolom daar dus niet uit; geef de kolom in de selectie mee")


def entries(selectie, objecten):
    """De gekozen objecttypen als werklijst, met hun merk, nummer en toelichting."""
    ruwe = selectie.get("objecten")
    if not ruwe:
        raise Fout("de selectie noemt geen objecttypen; vul het veld objecten")
    uit = []
    for ruw in ruwe:
        e = {"naam": ruw} if isinstance(ruw, str) else dict(ruw)
        if not e.get("naam"):
            raise Fout(f"een item in objecten heeft geen naam: {ruw!r}")
        _controleer_merk(e, objecten)
        e["gewijzigd"] = e.get("merk") is not None
        uit.append(e)
    _controleer_namen([e["naam"] for e in uit if e.get("merk") != "verwijderd"], objecten)
    dubbel = [n for n in {norm(e["naam"]) for e in uit}
              if sum(1 for e in uit if norm(e["naam"]) == n) > 1]
    if dubbel:
        raise Fout("deze objecttypen staan meer dan een keer in de selectie: " + "; ".join(sorted(dubbel)))
    if len(uit) > MAX_VAKKEN:
        raise Fout(f"{len(uit)} objecttypen is te veel voor een uitsnede (hoogstens {MAX_VAKKEN}); "
                   "splits de vraag in twee uitsneden")
    nummer = 0
    for volgorde, e in enumerate(uit):
        e["volgorde"] = volgorde
        if e["gewijzigd"]:
            nummer += 1
            e["nummer"] = e.get("nummer") or nummer
        _controleer_waarom(e)
        obj = objecten.get(norm(e["naam"])) or dict(naam=e["naam"], kolom=e.get("kolom"),
                                                    scope="buiten", vulkleur="#e8e8e8", oeapi=None)
        e["obj"] = obj
        e["kolom"] = e.get("kolom") or obj.get("kolom") or BAND_NAAM
        e["band"] = norm(e["kolom"]) == norm(BAND_NAAM)
    return uit


def rijen_toekennen(lijst, relaties_model, selectie):
    """De rij-index per objecttype. De auteur kiest de rijen; zonder keuze komt het algemene
    type dat in de selectie gespecialiseerd wordt bovenaan en de rest eronder.

    De band boven de kolommen doet niet aan rijen mee: zij ligt boven het hele raster en
    draagt een eigen rij-index.
    """
    in_kolom = [e for e in lijst if not e["band"]]
    for e in lijst:
        if e["band"]:
            e["rij_index"] = BAND_RIJ
    met_rij = [e for e in in_kolom if e.get("rij") is not None]
    if met_rij and len(met_rij) != len(in_kolom):
        zonder = [e["naam"] for e in in_kolom if e.get("rij") is None]
        raise Fout("geef een rij voor alle objecttypen of voor geen; deze missen er een: "
                   + "; ".join(zonder))
    if not met_rij:
        gekozen = {norm(e["naam"]) for e in in_kolom}
        algemeen = {norm(r["naar"]) for r in relaties_model
                    if r["soort"] == "Specialization"
                    and norm(r["van"]) in gekozen and norm(r["naar"]) in gekozen}
        for e in in_kolom:
            e["rij"] = 0 if norm(e["naam"]) in algemeen or not algemeen else 1
    waarden = sorted({e["rij"] for e in in_kolom})
    if len(waarden) > MAX_RIJEN:
        raise Fout(f"{len(waarden)} rijen is te veel voor een uitsnede (hoogstens {MAX_RIJEN})")
    index = {w: i for i, w in enumerate(waarden)}
    for e in in_kolom:
        e["rij_index"] = index[e["rij"]]
    labels = selectie.get("rij_labels") or []
    return len(waarden), [labels[i] if i < len(labels) else "" for i in range(len(waarden))]


def kolommen_van(lijst, selectie):
    """De kolommen die in de uitsnede voorkomen, in de volgorde van de grote plaat.

    De band boven de kolommen is geen kolom en kost dus geen kolombreedte; dat was de reden om
    haar uit de rij van kolommen te halen.
    """
    aanwezig = {e["kolom"] for e in lijst if not e["band"]}
    opgegeven = selectie.get("kolommen")
    if opgegeven:
        ontbreekt = aanwezig - set(opgegeven)
        if ontbreekt:
            raise Fout("de opgegeven kolomvolgorde mist: " + "; ".join(sorted(ontbreekt)))
        uit = [k for k in opgegeven if k in aanwezig]
    else:
        bekend = [k for k in KOLOMVOLGORDE if k in aanwezig]
        onbekend = sorted(aanwezig - set(KOLOMVOLGORDE))
        uit = bekend + onbekend
    if len(uit) > MAX_KOLOMMEN:
        raise Fout(f"{len(uit)} kolommen is te veel voor een uitsnede (hoogstens {MAX_KOLOMMEN})")
    return uit


# ----------------------------------------------------------------------- band --

def band_bruggen(lijst, relaties_model, objecten, kolommen):
    """Per objecttype in de band de kolomgrens die het overbrugt, als (linkerkolom, rechterkolom).

    De grens volgt uit de relaties en niet uit een lijstje in het script: eerst de kolommen van
    de buren die zelf in de uitsnede staan, en zonder zulke buur de kolommen van de buren in het
    hele model die in de uitsnede voorkomen. Zo komt `Aanmelding` boven de grens tussen aanbod en
    verbintenis te staan, en `Verzoek tot Aanbod / Intekening op specificatie` boven de grens
    tussen specificatie en aanbod. Valt er niets af te leiden, dan is de uitkomst None en komt
    het vak midden boven het raster.
    """
    index = {k: i for i, k in enumerate(kolommen)}
    in_kolom = {norm(e["naam"]): e["kolom"] for e in lijst if not e["band"]}
    uit = {}
    for e in (x for x in lijst if x["band"]):
        naam = norm(e["naam"])
        dichtbij, verder = set(), set()
        for r in relaties_model:
            for hier, daar in ((r["van"], r["naar"]), (r["naar"], r["van"])):
                if norm(hier) != naam:
                    continue
                ander = norm(daar)
                if ander in in_kolom:
                    dichtbij.add(in_kolom[ander])
                else:
                    kolom = norm((objecten.get(ander) or {}).get("kolom"))
                    if kolom in index:
                        verder.add(kolom)
        gevonden = sorted(dichtbij or verder, key=lambda k: index[k])
        uit[id(e)] = (gevonden[0], gevonden[-1]) if gevonden else None
    return uit


def band_ordenen(lijst, bruggen, kolommen):
    """De band van links naar rechts, in de volgorde van de grens die elk vak overbrugt.

    De volgorde valt hier en niet bij het plaatsen, want de relaties binnen de band lopen tussen
    buren in de band; wie later nog zou schuiven, zou een lijn over een vak heen leggen. Een vak
    zonder af te leiden grens komt in het midden, op de plek waar het ook getekend wordt.
    """
    midden = (len(kolommen) - 1) / 2 if kolommen else 0
    index = {k: i for i, k in enumerate(kolommen)}

    def sleutel(e):
        brug = bruggen[id(e)]
        plek = midden if not brug else (index[brug[0]] + index[brug[1]]) / 2
        return (plek, e["volgorde"])

    band = sorted((e for e in lijst if e["band"]), key=sleutel)
    return [e for e in lijst if not e["band"]] + band


# ------------------------------------------------------------------ relaties --

def _sleutel(r):
    return (r["soort"], norm(r["van"]), norm(r["naar"]))


def relaties_kiezen(model, selectie, lijst, kolommen):
    """De relaties van het model tussen de gekozen objecttypen, verdeeld over wat als lijn te
    tekenen is en wat een verwijzing in het vak wordt.

    Geeft (horizontaal, verticaal, verwijzingen, weggelaten, lussen, cel).
    """
    per_naam = {norm(e["naam"]): e for e in lijst}
    kolom_index = {k: i for i, k in enumerate(kolommen)}
    cel = {}
    for e in lijst:
        cel.setdefault((e["rij_index"], e["kolom"]), []).append(e)
    for leden in cel.values():
        for i, e in enumerate(leden):
            e["cel_index"], e["cel_leden"] = i, len(leden)

    verborgen = set()
    for v in selectie.get("verberg", []):
        if not v.get("reden"):
            raise Fout(f"verberg zonder reden: {v.get('van')!r} naar {v.get('naar')!r}; "
                       "een weggelaten relatie hoort een reden te dragen")
        verborgen.add((norm(v["van"]), norm(v["naar"])))

    horizontaal, verticaal, verwijzingen, weggelaten, lussen = [], [], [], [], []
    for r in model.get("relaties", []):
        a, b = norm(r["van"]), norm(r["naar"])
        if a not in per_naam or b not in per_naam:
            continue
        if (a, b) in verborgen:
            continue
        if a == b:
            # een relatie van een objecttype naar zichzelf wordt een lus binnen het vak zelf,
            # en geen regel in het vak: zij is een relatie en hoort als relatie te staan
            lussen.append(dict(vak=per_naam[a], soort=r["soort"], label=r.get("label")))
            continue
        bron, doel = per_naam[a], per_naam[b]
        plek = _plek(bron, doel, cel, kolom_index)
        if plek == "horizontaal":
            horizontaal.append(dict(bron=bron, doel=doel, soort=r["soort"], label=r.get("label")))
        elif plek == "verticaal":
            verticaal.append(dict(bron=bron, doel=doel, soort=r["soort"], label=r.get("label")))
        else:
            verwijzingen.append((bron, _verwijzingstekst(r, doel["naam"])))
            weggelaten.append(f"{a} {r['soort']} {b}: niet haaks te lopen, als verwijzing getekend")

    bestaand = {_sleutel(r) for r in model.get("relaties", [])}
    for o in selectie.get("ontbreekt", []):
        for sleutel in ("van", "naar"):
            if norm(o.get(sleutel)) not in per_naam:
                raise Fout(f"ontbreekt verwijst naar {o.get(sleutel)!r}, "
                           "dat niet in de selectie staat")
        soort = o.get("soort", "Specialization")
        if (soort, norm(o["van"]), norm(o["naar"])) in bestaand:
            raise Fout(f"ontbreekt {o['van']!r} naar {o['naar']!r} staat wel in het model; "
                       "een bestaande relatie hoort als lijn getekend te worden")
        if not norm(o.get("label")):
            raise Fout(f"ontbreekt {o['van']!r} naar {o['naar']!r} draagt geen label; de "
                       "gestippelde lijn draagt haar eigen opschrift, zodat onder het beeld "
                       "geen alinea nodig is. Noem in het label wat er ontbreekt, bijvoorbeeld "
                       "'ontbreekt: vindt plaats op'")
        bron, doel = per_naam[norm(o["van"])], per_naam[norm(o["naar"])]
        plek = _plek(bron, doel, cel, kolom_index)
        rij = dict(bron=bron, doel=doel, soort=soort, label=o["label"], waarom=o.get("waarom"),
                   ontbreekt=True, accent=True)
        if plek == "horizontaal":
            horizontaal.append(rij)
        elif plek == "verticaal":
            verticaal.append(rij)
        else:
            raise Fout(f"ontbreekt {o['van']!r} naar {o['naar']!r} is niet haaks te lopen; "
                       "zet de twee objecttypen in dezelfde rij of in aangrenzende rijen van "
                       "dezelfde kolom, en haal er zo nodig een uit de band boven de kolommen "
                       "door het een expliciete kolom te geven")
    for h in horizontaal + verticaal:
        if h.get("ontbreekt"):
            continue
        h["accent"] = h["bron"]["gewijzigd"] and h["doel"]["gewijzigd"]
    return horizontaal, verticaal, verwijzingen, weggelaten, lussen, cel


def _plek(bron, doel, cel, kolom_index):
    """Of een relatie als horizontale lijn, als verticale lijn of niet te tekenen is.

    Horizontaal: dezelfde rij, en het been loopt over geen enkel vak. Binnen een cel moeten de
    twee vakken naast elkaar staan; over cellen heen moet het linker vak het laatste van zijn
    cel zijn, het rechter het eerste van zijn cel, en elke cel ertussen leeg.
    Verticaal: dezelfde kolom, aangrenzende rijen.
    """
    if bron["rij_index"] == doel["rij_index"]:
        if bron["kolom"] == doel["kolom"]:
            return "horizontaal" if abs(bron["cel_index"] - doel["cel_index"]) == 1 else None
        links, rechts = sorted((bron, doel), key=lambda e: kolom_index[e["kolom"]])
        if links["cel_index"] != links["cel_leden"] - 1 or rechts["cel_index"] != 0:
            return None
        kolom_van = {i: k for k, i in kolom_index.items()}
        tussen = range(kolom_index[links["kolom"]] + 1, kolom_index[rechts["kolom"]])
        if any(cel.get((links["rij_index"], kolom_van[i])) for i in tussen):
            return None
        return "horizontaal"
    if bron["kolom"] == doel["kolom"] and abs(bron["rij_index"] - doel["rij_index"]) == 1:
        return "verticaal"
    return None


def _verwijzingstekst(r, ander):
    label = r.get("label") or vt.STANDAARDLABEL.get(r["soort"], "hangt aan")
    return f"{label} {ander}"


# -------------------------------------------------------------------- opmaak --

def maat_vakken(lijst, verwijzingen, lussen, oeapi):
    """Per vak de naamregels, de extra regels en de breedte."""
    per_vak = {}
    for e, t in verwijzingen:
        per_vak.setdefault(id(e), []).append(t)
    for e in lijst:
        e["lussen"] = [lus for lus in lussen if lus["vak"] is e]
    for e in lijst:
        e["naamregels"] = afbreken(e["naam"], TEKST_B, NAAM_MAAT, True)
        extra = []
        if e["gewijzigd"]:
            extra.append((f"{e['nummer']} {MERKEN[e['merk']][0]}", ACCENT, True))
        if oeapi and e["gewijzigd"] and e["obj"].get("oeapi"):
            extra.append(("OEAPI: " + ", ".join(e["obj"]["oeapi"]), MUTED, False))
        if e.get("noot"):
            extra.append((e["noot"], MUTED, False))
        for t in per_vak.get(id(e), [])[:MAX_VERWIJZINGEN]:
            extra.append((t, MUTED, False))
        e["extra"] = extra
        breedtes = [tw(r, NAAM_MAAT, True) for r in e["naamregels"]]
        breedtes += [tw(t, NOOT_MAAT, b) for t, _, b in extra]
        e["w"] = max(MIN_VAK, max(breedtes) + VAK_MARGE_L + VAK_PICTOGRAM)
        e["h"] = max(MIN_VAK_H, 26 + NAAM_REGEL * (len(e["naamregels"]) - 1)
                     + NOOT_REGEL * len(extra) + 12)
        if e["lussen"]:
            # hoog genoeg om elke lus onder het pictogram te laten hangen
            e["h"] = max(e["h"], LUS_VAK_H + (len(e["lussen"]) - 1) * (LUS_H + LUS_GAT))
    return per_vak


def _relatienaam(rel):
    """De naam van een relatie als zweeftekst, in de notatie van de begrippenlijst.

    Bij een ontbrekende relatie staat de reden erachter in de zweeftekst. Zo blijft zij bij de
    plaat horen zonder dat zij onder het beeld een alinea kost.
    """
    staart = " (ontbreekt nog in het model)" if rel.get("ontbreekt") else ""
    if rel.get("ontbreekt") and rel.get("waarom"):
        staart = f" (ontbreekt nog in het model: {rel['waarom']})"
    return f"{rel['soort']}: {rel['bron']['naam']} naar {rel['doel']['naam']}{staart}"


def _lusnaam(lus):
    """De naam van een relatie op zichzelf als zweeftekst."""
    staart = f" ({lus['label']})" if norm(lus.get("label")) else ""
    return f"{lus['soort']}: {lus['vak']['naam']} naar zichzelf{staart}"


def labelregels(rel):
    return afbreken(rel["label"], LABEL_B, LABEL_MAAT) if rel.get("label") else []


def label_rechterrand(rel):
    """De rechterrand van het label van een verticale relatie, of 0 zonder label.

    Het label van een verticale relatie staat met de ankering links naast de lijn en steekt
    daarmee buiten het raster uit. Een relatie in de rechtste kolom schuift haar label dus
    voorbij de rand van het doek, en keur-plaat.py meldt dat als BUITEN. Het doek rekent deze
    rand mee, zodat elke tekst binnen het doek blijft ongeacht in welke kolom zij valt.
    """
    regels = labelregels(rel)
    if not regels:
        return 0
    rand = max(rel["x_bovenrand"], rel["x_onderrand"]) + 8
    return rand + max(tw(r, LABEL_MAAT) for r in regels)


def plaatsen(lijst, kolommen, rijen, horizontaal, verticaal, cel, bruggen=None):
    """De plek van elk vak, elke rijbaan en elke rijgoot; alles in pixels op het doek.

    De maatvoering is optelwerk en geen zoekproces: de kolom volgt uit het veld kolom, de rij
    uit de selectie, en de plek in de cel uit de volgorde in de selectie. De band boven de
    kolommen komt er als laatste bij, want haar ankers hangen aan de kolombreedtes.

    De y van een vak is hier nog de hoogte binnen het raster; `bouw` schuift alles naar beneden.
    De band ligt boven het raster en krijgt daarom een negatieve y.
    """
    lijst, band = [e for e in lijst if not e["band"]], [e for e in lijst if e["band"]]
    cel = {sleutel: leden for sleutel, leden in cel.items() if sleutel[0] != BAND_RIJ}
    horizontaal, band_h = ([h for h in horizontaal if h["bron"]["rij_index"] != BAND_RIJ],
                           [h for h in horizontaal if h["bron"]["rij_index"] == BAND_RIJ])

    # 1. gaten binnen een cel: breder waar een relatie met een label tussen twee vakken loopt
    gat = {}
    for h in horizontaal:
        if h["bron"]["kolom"] == h["doel"]["kolom"]:
            links, rechts = sorted((h["bron"], h["doel"]), key=lambda e: e["cel_index"])
            sleutel = (links["rij_index"], links["kolom"], links["cel_index"])
            nodig = max(CEL_GAT, max([tw(r, LABEL_MAAT) for r in labelregels(h)] or [0]) + 24)
            gat[sleutel] = max(gat.get(sleutel, CEL_GAT), nodig)

    # 2. celbreedte en kolombreedte
    cel_breedte = {}
    for (rij, kolom), leden in cel.items():
        breed = sum(e["w"] for e in leden)
        breed += sum(gat.get((rij, kolom, i), CEL_GAT) for i in range(len(leden) - 1))
        cel_breedte[(rij, kolom)] = breed
    kol_breedte = {}
    for kolom in kolommen:
        inhoud = max([cel_breedte.get((r, kolom), 0) for r in range(rijen)] or [0])
        kop = tw(kolom, 12, True) + 20
        kol_breedte[kolom] = max(inhoud + 2 * KOL_MARGE, kop)

    # 3. kolomgoten: minstens zo breed als het breedste label dat erdoor loopt
    goot = {k: KOL_GOOT for k in kolommen[:-1]}
    kolom_index = {k: i for i, k in enumerate(kolommen)}
    for h in horizontaal:
        if h["bron"]["kolom"] == h["doel"]["kolom"]:
            continue
        links, rechts = sorted((h["bron"], h["doel"]), key=lambda e: kolom_index[e["kolom"]])
        tussen = kolommen[kolom_index[links["kolom"]]:kolom_index[rechts["kolom"]]]
        nodig = max([tw(r, LABEL_MAAT) for r in labelregels(h)] or [0]) + 24
        deel = max(KOL_GOOT, (nodig - sum(kol_breedte[k] for k in tussen[1:])) / len(tussen))
        for k in tussen:
            goot[k] = max(goot[k], deel)

    # 4. x per kolom en per vak
    x = DOEK_MARGE
    kol_x = {}
    for i, kolom in enumerate(kolommen):
        kol_x[kolom] = x
        x += kol_breedte[kolom] + (goot[kolom] if i < len(kolommen) - 1 else 0)
    raster_breed = x - DOEK_MARGE
    for (rij, kolom), leden in cel.items():
        cx = kol_x[kolom] + KOL_MARGE
        for i, e in enumerate(leden):
            e["x"] = cx
            cx += e["w"] + gat.get((rij, kolom, i), CEL_GAT)

    # 5. banen voor horizontale relaties: per gat een eigen baan, zodat twee relaties in
    #    dezelfde rij nooit op dezelfde lijn vallen
    banen = {}
    for h in horizontaal:
        links, rechts = sorted((h["bron"], h["doel"]), key=lambda e: e["x"])
        sleutel = (links["rij_index"], round(links["x"] + links["w"]), round(rechts["x"]))
        banen.setdefault(sleutel, []).append(h)
    rij_banen = {r: 1 for r in range(rijen)}
    for sleutel, groep in banen.items():
        for n, h in enumerate(groep):
            h["baan"] = n
        rij_banen[sleutel[0]] = max(rij_banen[sleutel[0]], len(groep))

    # 6. rijhoogte: de hoogste vakhoogte, maar hoog genoeg voor alle banen in die rij
    rij_h = {}
    for r in range(rijen):
        hoog = max([e["h"] for e in lijst if e["rij_index"] == r] or [MIN_VAK_H])
        rij_h[r] = max(hoog, 20 + (rij_banen[r] - 1) * BAAN + 10)

    # 7. verticale relaties: het vak op de bovenste rij hecht aan op zijn onderrand, dat op de
    #    onderste rij op zijn bovenrand. Twee lijnen naar dezelfde rand worden over de breedte
    #    van het vak verdeeld, zodat zij niet samenvallen.
    for v in verticaal:
        boven, onder = sorted((v["bron"], v["doel"]), key=lambda e: e["rij_index"])
        v["boven"], v["onder"] = boven, onder
        v["gat"] = boven["rij_index"]
    def _midden(e):
        return e["x"] + e["w"] / 2

    aanhechting = {}
    for v in verticaal:
        aanhechting.setdefault((id(v["boven"]), "onderrand"), []).append((_midden(v["onder"]), v))
        aanhechting.setdefault((id(v["onder"]), "bovenrand"), []).append((_midden(v["boven"]), v))
    for (_, rand), leden in aanhechting.items():
        # de aanhechtingen staan in de volgorde van het andere eind. Daarmee loopt een bundel
        # lijnen naar hetzelfde vak als een vlechtloze vouw: kruisen zij op de ene rand niet,
        # dan kruisen zij op de andere ook niet.
        leden.sort(key=lambda p: p[0])
        vak_e = leden[0][1]["boven"] if rand == "onderrand" else leden[0][1]["onder"]
        ruimte = max(vak_e["w"] - 40, 0)
        for i, (_, v) in enumerate(leden):
            deel = (i + 1) / (len(leden) + 1)
            v["x_" + rand] = vak_e["x"] + 20 + ruimte * deel

    # 8. y per rij; de rijgoot groeit mee met het aantal omwegen dat erin ligt
    omwegen = {}
    for v in verticaal:
        if abs(v["x_bovenrand"] - v["x_onderrand"]) >= 0.5:
            omwegen.setdefault(v["gat"], []).append(v)
    rij_y, y = {}, 0
    for r in range(rijen):
        rij_y[r] = y
        y += rij_h[r]
        if r < rijen - 1:
            y += RIJ_GOOT + max(0, len(omwegen.get(r, [])) - 1) * OMWEG_BAAN
    raster_hoog = y

    for e in lijst:
        e["y"] = rij_y[e["rij_index"]]
        e["vak_h"] = rij_h[e["rij_index"]]
    for h in horizontaal:
        h["y"] = rij_y[h["bron"]["rij_index"]] + 20 + h["baan"] * BAAN
    for v in verticaal:
        v["y_onderrand"] = rij_y[v["gat"]] + rij_h[v["gat"]]
        v["y_bovenrand"] = rij_y[v["gat"] + 1]
    # de kortste omweg knikt het dichtst bij de onderste rij; zo liggen de omwegen genest en
    # kruist het been van de ene omweg nooit de knik van de andere
    for g, groep in omwegen.items():
        groep.sort(key=lambda v: abs(v["x_bovenrand"] - v["x_onderrand"]))
        onder = rij_y[g + 1]
        for i, v in enumerate(groep):
            v["baan_y"] = onder - 14 - i * OMWEG_BAAN

    # 9. de band boven de kolommen: elk vak boven de grens die het overbrugt
    band_hoog, band_rand = plaats_band(band, band_h, bruggen or {}, kol_x, kol_breedte,
                                       raster_breed)
    return dict(kol_x=kol_x, kol_breedte=kol_breedte, rij_y=rij_y, rij_h=rij_h,
                breed=raster_breed, hoog=raster_hoog, band_hoog=band_hoog, band_rand=band_rand)


def band_anker(brug, kol_x, kol_breedte, raster_breed):
    """De x waar het midden van een bandvak hoort te liggen: boven de grens die het overbrugt.

    Bij twee kolommen is dat het midden tussen de rechterrand van de linkerkolom en de
    linkerrand van de rechterkolom, en dus de goot ertussen wanneer zij naast elkaar staan. Bij
    een kolom is het het midden van die kolom, en zonder grens het midden van het raster.
    """
    if not brug:
        return DOEK_MARGE + raster_breed / 2
    links, rechts = brug
    if links == rechts:
        return kol_x[links] + kol_breedte[links] / 2
    return ((kol_x[links] + kol_breedte[links]) + kol_x[rechts]) / 2


def plaats_band(band, band_h, bruggen, kol_x, kol_breedte, raster_breed):
    """De plek van elk vak in de band en van elke lijn erbinnen. Geeft (hoogte, rechterrand).

    De band is een rij boven het raster: elk vak komt met zijn midden op zijn anker, en schuift
    naar rechts zodra het anker het tegen zijn linkerbuur zou aanleggen. De vakken staan al in
    de volgorde van hun anker, dus dat schuiven gaat een kant op en legt geen lijn over een vak.
    """
    if not band:
        return 0, DOEK_MARGE
    for e in band:
        e["brug"] = bruggen.get(id(e))
        e["anker"] = band_anker(e["brug"], kol_x, kol_breedte, raster_breed)
    # het gat tussen twee buren is breed genoeg voor het opschrift van de lijn ertussen
    plek = {id(e): i for i, e in enumerate(band)}
    gat = {}
    for h in band_h:
        i = min(plek[id(h["bron"])], plek[id(h["doel"])])
        nodig = max([tw(r, LABEL_MAAT) for r in labelregels(h)] or [0]) + 24
        gat[i] = max(gat.get(i, CEL_GAT), nodig)

    links_grens = DOEK_MARGE + KOL_MARGE
    x, laatste = links_grens, CEL_GAT
    for i, e in enumerate(band):
        e["x"] = max(e["anker"] - e["w"] / 2, x)
        laatste = gat.get(i, CEL_GAT)
        x = e["x"] + e["w"] + laatste
    # een vak dat zijn buurman wegduwt, duwt de band aan de rechterkant buiten het raster; de
    # hele band schuift dan terug tot zij er weer binnen past of tot zij links aanloopt
    overloop = max(0, x - laatste + KOL_MARGE - (DOEK_MARGE + raster_breed))
    terug = min(overloop, band[0]["x"] - links_grens)
    for e in band:
        e["x"] -= terug
    banen = {}
    for h in band_h:
        links, rechts = sorted((h["bron"], h["doel"]), key=lambda e: e["x"])
        banen.setdefault((round(links["x"] + links["w"]), round(rechts["x"])), []).append(h)
    for groep in banen.values():
        for n, h in enumerate(groep):
            h["baan"] = n
    hoog = max([e["h"] for e in band]
               + [20 + (max([len(g) for g in banen.values()] or [1]) - 1) * BAAN + 10])
    for e in band:
        e["vak_h"] = hoog
        e["y"] = -(KOL_TAB_H + BAND_GOOT + hoog)
    for h in band_h:
        h["y"] = -(KOL_TAB_H + BAND_GOOT + hoog) + 20 + h["baan"] * BAAN
    rand = max(e["x"] + e["w"] for e in band) + KOL_MARGE
    return hoog, rand


# ------------------------------------------------------------------ tekenen --

def groep(klasse, titel, inhoud):
    """Een getekend onderdeel met een naam erin, zodat de SVG zichzelf uitlegt: een lezer ziet
    de naam als zweeftekst en een controlescript kan de plaat op inhoud nakijken."""
    kop = f"<title>{html.escape(titel)}</title>" if titel else ""
    return f'<g class="{klasse}">{kop}{inhoud}</g>'


def vak(e):
    """Een objecttype als ArchiMate-bedrijfsobject: vulling naar scope, pictogram rechtsboven,
    de naam vet en eronder het merk, de OEAPI-tegenhanger en de verwijzingen."""
    vul, lijn, _ = kleuren(e["obj"])
    x, y, w, h = e["x"], e["y"], e["w"], e["vak_h"]
    uit = box(x, y, w, h, vul, lijn) + icon("object", x + w - 22, y + 5)
    naam_vet = e["gewijzigd"]
    for i, r in enumerate(e["naamregels"]):
        uit += text(x + VAK_MARGE_L, y + 26 + i * NAAM_REGEL, r, NAAM_MAAT, naam_vet,
                    INK if naam_vet else MUTED)
    basis = y + 26 + NAAM_REGEL * (len(e["naamregels"]) - 1)
    for i, (t, kleur, vet) in enumerate(e["extra"]):
        uit += text(x + VAK_MARGE_L, basis + NOOT_REGEL * (i + 1), t, NOOT_MAAT, vet, kleur)
    if e["gewijzigd"]:
        uit += (f'<rect x="{x - 3:.0f}" y="{y - 3:.0f}" width="{w + 6:.0f}" height="{h + 6:.0f}" '
                f'rx="4" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    return groep("vak", e["naam"], uit)


def groepering(kolom, x, breed, y, hoog):
    """Een begrippenfamilie als ArchiMate-groepering: een tab met de naam en een vlak eronder."""
    tab_b = tw(kolom, 12, True) + 20
    return groep("groepering", kolom,
                 box(x, y, breed, hoog, KOL_VUL, KOL_RAND)
                 + box(x, y - KOL_TAB_H, min(tab_b, breed), KOL_TAB_H, KOL_TAB, KOL_RAND)
                 + text(x + 10, y - 8, kolom, 12, True, BUS_T))


def legenda_regels(lijst, horizontaal, verticaal, lussen=(), verwijzingen=()):
    """Alleen de tegels die op dit beeld voorkomen; een legenda die meer uitlegt dan er staat,
    laat een lezer zoeken naar iets wat er niet is.

    De legenda draagt de uitleg die vroeger in de alinea onder het beeld stond: wat een lus is,
    en wat een regel in een vak betekent die naar een ander objecttype verwijst.
    """
    uit = []
    if any(kleuren(e["obj"])[0] == BUS for e in lijst):
        uit.append(("vak", BUS, BUS_L, "OKx referentiekader"))
    if any(kleuren(e["obj"])[0] == GRIJS and e.get("merk") != "verwijderd" for e in lijst):
        uit.append(("vak", GRIJS, GRIJS_L, "Buiten scope binnen OKx"))
    # per soort wijziging een eigen tegel: een lezer ziet zo niet dat er iets veranderde maar wat.
    # De vulling van de tegel is die van het vak zelf, zodat de twee scopetegels uit elkaar
    # te houden zijn aan de kleur die zij op het beeld opleveren.
    vulling = {"binnen scope": BUS, "buiten scope": GRIJS, "verwijderd": GRIJS}
    for merk, (_, uitleg) in MERKEN.items():
        if any(e.get("merk") == merk for e in lijst):
            uit.append(("rand", vulling.get(merk, "#ffffff"), ACCENT, uitleg))
    if any(e["band"] for e in lijst):
        # de tegel belooft alleen een brug zodra er een vak boven een grens staat; een band
        # zonder brug draagt een objecttype dat in het model aan geen kolom hangt, en een
        # belofte die het beeld niet waarmaakt laat een lezer zoeken naar een lijn die er is.
        brug = any(e["band"] and e.get("brug") and e["brug"][0] != e["brug"][1] for e in lijst)
        uit.append(("band", None, KOL_RAND,
                    "band boven de kolommen: verbindt twee kolommen" if brug
                    else "band boven de kolommen: hangt in het model aan geen kolom"))
    if any(r.get("ontbreekt") for r in horizontaal + verticaal):
        uit.append(("ontbreekt", None, ACCENT, "ontbreekt nog in het model"))
    for soort in ("Specialization", "Aggregation", "Composition", "Association", "Access",
                  "Realization", "Influence"):
        if any(r["soort"] == soort and not r.get("ontbreekt") for r in horizontaal + verticaal):
            uit.append(("relatie", soort, RELATIE, VORMNAAM[soort]))
    for soort in sorted({lus["soort"] for lus in lussen}):
        uit.append(("lus", soort, RELATIE, LUS_VORMNAAM.get(soort, f"{soort} op zichzelf")))
    if verwijzingen:
        uit.append(("verwijzing", None, MUTED, "regel in een vak: relatie buiten dit raster"))
    return uit


def legenda(x, y, regels, maxw):
    """De tegels naast elkaar, over meer regels als zij breder worden dan het doek."""
    uit, cx, cy, hoogte = "", x, y, 0
    for soort, a, b, tekst in regels:
        breed = 44 + tw(tekst, LEGENDA_MAAT) + 18
        if cx > x and cx + breed > x + maxw:
            cx, cy = x, cy + 24
            hoogte += 24
        if soort == "vak":
            uit += box(cx, cy - 10, 18, 12, a, b)
        elif soort == "rand":
            uit += box(cx, cy - 10, 18, 12, a or "#ffffff", b, 2) + \
                f'<rect x="{cx - 2:.0f}" y="{cy - 12:.0f}" width="22" height="16" rx="3" ' \
                f'fill="none" stroke="{b}" stroke-width="2"/>'
        elif soort == "band":
            # de tegel toont wat op de plaat staat: een band over twee kolommen heen
            uit += box(cx, cy - 16, 32, 8, KOL_TAB, b)
            uit += box(cx, cy - 5, 14, 9, KOL_VUL, b) + box(cx + 18, cy - 5, 14, 9, KOL_VUL, b)
        elif soort == "ontbreekt":
            uit += (f'<path d="M{cx:.0f} {cy - 4:.0f}H{cx + 30:.0f}" fill="none" stroke="{b}" '
                    f'stroke-width="2.6" stroke-dasharray="6 5"/>')
        elif soort == "lus":
            # de tegel toont wat op de plaat staat: een vak met de lus aan de binnenkant van
            # zijn rechterrand
            uit += box(cx, cy - 16, 32, 24, BUS, BUS_L)
            uit += (f'<path d="M{cx + 32:.0f} {cy - 10:.0f}H{cx + 12:.0f}V{cy + 2:.0f}'
                    f'H{cx + 32:.0f}" fill="none" stroke="{b}" stroke-width="1.3"/>')
            uit += (_kop_h(cx + 32, cy - 10, a, -1, b) if a in ("Aggregation", "Composition")
                    else _kop_h(cx + 32, cy + 2, a, 1, b))
        elif soort == "verwijzing":
            uit += box(cx + 2, cy - 13, 26, 18, BUS, BUS_L)
            uit += (f'<path d="M{cx + 7:.0f} {cy - 3:.0f}H{cx + 23:.0f}" fill="none" '
                    f'stroke="{b}" stroke-width="1.3"/>')
        else:
            uit += (f'<path d="M{cx:.0f} {cy - 4:.0f}H{cx + 30:.0f}" fill="none" stroke="{b}" '
                    f'stroke-width="1.3"'
                    + (f' stroke-dasharray="{GESTIPPELD[a]}"' if a in GESTIPPELD else "") + "/>")
            uit += _kop_h(cx + 30, cy - 4, a, 1, b) if a not in ("Aggregation", "Composition") \
                else _kop_h(cx, cy - 4, a, 1, b)
        uit += text(cx + 44, cy, tekst, LEGENDA_MAAT, fill=MUTED)
        cx += breed
    return uit, hoogte


# --------------------------------------------------------------- voorbeeld --

def voorbeeld_lezen(selectie, lijst):
    """Het voorbeeldblok uit de selectie, gecontroleerd en gemeten. Geeft None zonder blok.

    Een uitsnede toont de structuur; een vraag als "kan een leeruitkomst het niveau van een
    competentie uitdrukken?" is pas beantwoord zodra er een ingevuld geval naast staat. Dat
    geval krijgt een eigen blok naast het raster, en geen alinea onder het beeld: het is geen
    uitleg bij de plaat maar het antwoord zelf, ontleed in de delen van de vorm.

    Vier eisen houden het blok een voorbeeld en maken er geen betoog van: het hangt aan een
    objecttype dat op de plaat staat (`bij`), het draagt zijn vindplaats, elk deel blijft
    binnen MAX_VB_WOORDEN woorden en er zijn er hoogstens MAX_VB_DELEN. Zonder vindplaats
    weigert het script, want een voorbeeld zonder herkomst is een verzinsel.
    """
    vb = selectie.get("voorbeeld")
    if not vb:
        return None
    per_naam = {norm(e["naam"]): e for e in lijst}
    bij = norm(vb.get("bij"))
    if not bij:
        raise Fout("het voorbeeld noemt geen bij; zeg bij welk objecttype op de plaat het hoort")
    if bij not in per_naam:
        raise Fout(f"het voorbeeld hoort bij {vb['bij']!r}, dat niet in de selectie staat")
    zin = norm(vb.get("zin"))
    if not zin:
        raise Fout("het voorbeeld draagt geen zin; neem het voorbeeld letterlijk over")
    if len(zin.split()) > MAX_VB_ZINWOORDEN:
        raise Fout(f"de voorbeeldzin telt {len(zin.split())} woorden (hoogstens "
                   f"{MAX_VB_ZINWOORDEN}); neem een voorbeeld dat op het blok past")
    if not norm(vb.get("vindplaats")):
        raise Fout("het voorbeeld draagt geen vindplaats; een voorbeeld zonder herkomst is een "
                   "verzinsel, neem er een over uit een bestaand bestand en noem dat erbij")
    delen = list(vb.get("delen") or [])
    if not delen:
        raise Fout("het voorbeeld draagt geen delen; ontleed de zin in de delen van de vorm")
    if len(delen) > MAX_VB_DELEN:
        raise Fout(f"het voorbeeld telt {len(delen)} delen (hoogstens {MAX_VB_DELEN}); een "
                   "langere ontleding is een tabel en geen voorbeeld")
    rijen = []
    for d in delen:
        naam, waarde = norm(d.get("deel")), norm(d.get("waarde"))
        if not naam or not waarde:
            raise Fout(f"een deel van het voorbeeld mist deel of waarde: {d!r}")
        if len(waarde.split()) > MAX_VB_WOORDEN:
            raise Fout(f"het deel {naam!r} telt {len(waarde.split())} woorden (hoogstens "
                       f"{MAX_VB_WOORDEN}); houd de waarde bij wat in de zin staat")
        rijen.append((naam, waarde, False))
    niveau = norm(vb.get("niveau"))
    if niveau:
        if len(niveau.split()) > MAX_VB_WOORDEN:
            raise Fout(f"het niveau telt {len(niveau.split())} woorden (hoogstens "
                       f"{MAX_VB_WOORDEN})")
        rijen.append(("niveau", niveau, True))
    doel = per_naam[bij]
    kop = f"Voorbeeld bij {doel['nummer']} {doel['naam']}" if doel.get("nummer") \
        else f"Voorbeeld bij {doel['naam']}"
    return dict(kop=kop, bij=doel["naam"], zin=zin, rijen=rijen,
                zinregels=afbreken(zin, VB_B, VB_ZIN_MAAT, True),
                gradatie=afbreken(vb["gradatie"], VB_B, VB_MAAT) if norm(vb.get("gradatie")) else [],
                vindplaats=afbreken(vb["vindplaats"], VB_B, VB_BRON_MAAT))


def voorbeeld_maat(vb):
    """De breedte en de hoogte van het voorbeeldblok, in pixels."""
    label_b = max(tw(naam, VB_MAAT) for naam, _, _ in vb["rijen"]) + VB_LABEL_GOOT
    vb["label_b"] = label_b
    breed = max([tw(r, VB_ZIN_MAAT, True) for r in vb["zinregels"]]
                + [label_b + tw(waarde, VB_MAAT, vet) for _, waarde, vet in vb["rijen"]]
                + [tw(r, VB_MAAT) for r in vb["gradatie"]]
                + [tw(r, VB_BRON_MAAT) for r in vb["vindplaats"]]
                + [tw(vb["kop"], 12, True)])
    hoog = (VB_MARGE + VB_REGEL * len(vb["zinregels"]) + 8
            + VB_REGEL * len(vb["rijen"]) + (8 if vb["gradatie"] else 0)
            + VB_REGEL * len(vb["gradatie"]) + 8
            + (VB_BRON_MAAT + 4) * len(vb["vindplaats"]) + VB_MARGE)
    return breed + 2 * VB_MARGE, hoog


def voorbeeld_blok(vb, x, y, breed, hoog):
    """Het voorbeeldblok als ArchiMate-groepering naast de kolommen: de zin bovenaan, eronder
    de delen van de vorm in twee kolommen, en onderaan de vindplaats.

    Het niveau staat in de accentkleur onder de delen: het is geen deel van de zin maar het
    metagegeven ernaast, en dat is precies wat de vraag van de reviewronde raakt.
    """
    tab_b = tw(vb["kop"], 12, True) + 20
    uit = (box(x, y, breed, hoog, KOL_VUL, KOL_RAND)
           + box(x, y - KOL_TAB_H, min(tab_b, breed), KOL_TAB_H, KOL_TAB, KOL_RAND)
           + text(x + 10, y - 8, vb["kop"], 12, True, ACCENT))
    cy = y + VB_MARGE + VB_ZIN_MAAT
    for r in vb["zinregels"]:
        uit += text(x + VB_MARGE, cy, r, VB_ZIN_MAAT, True, INK)
        cy += VB_REGEL
    cy += 8
    for naam, waarde, vet in vb["rijen"]:
        uit += text(x + VB_MARGE, cy, naam, VB_MAAT, False, MUTED)
        uit += text(x + VB_MARGE + vb["label_b"], cy, waarde, VB_MAAT, vet,
                    ACCENT if vet else INK)
        cy += VB_REGEL
    if vb["gradatie"]:
        cy += 8
        for r in vb["gradatie"]:
            uit += text(x + VB_MARGE, cy, r, VB_MAAT, False, MUTED)
            cy += VB_REGEL
    cy += 8
    for r in vb["vindplaats"]:
        uit += text(x + VB_MARGE, cy, r, VB_BRON_MAAT, False, MUTED)
        cy += VB_BRON_MAAT + 4
    return groep("voorbeeld", vb["kop"], uit)


def _leesregels(lijst):
    """De regels onder het beeld, met per regel de plek van de drie stukken en de breedte.

    De drie stukken staan in drie kolommen die over alle regels dezelfde x houden: de breedste
    naam bepaalt waar de reden begint. Zo leest de leeswijzer als een tabelletje in plaats van
    als een rafelige lijst, en zoekt het oog per regel niet opnieuw waar de reden staat.

    De breedte telt mee in de maat van het doek, zodat een regel nooit hoeft af te breken: een
    genummerd objecttype houdt het bij een regel en de telling onder het beeld klopt.
    """
    gekozen = sorted((e for e in lijst if e["gewijzigd"] and e.get("waarom")),
                     key=lambda e: e["nummer"])
    if not gekozen:
        return []
    x_naam = max(tw(str(e["nummer"]), LEES_MAAT, True) for e in gekozen) + 10
    x_waarom = x_naam + max(tw(e["naam"], LEES_MAAT, True) for e in gekozen) + LEES_GOOT
    return [dict(nummer=e["nummer"], naam=e["naam"], waarom=e["waarom"], x_naam=x_naam,
                 x_waarom=x_waarom, breed=x_waarom + tw(e["waarom"], LEES_MAAT))
            for e in gekozen]


def bouw(model, selectie):
    """De uitsnede als SVG, met de melding over wat niet als lijn getekend kon worden."""
    _controleer_toelichting(selectie)
    objecten = objecten_van(model)
    lijst = entries(selectie, objecten)
    rijen, rij_labels = rijen_toekennen(lijst, model.get("relaties", []), selectie)
    kolommen = kolommen_van(lijst, selectie)
    bruggen = band_bruggen(lijst, model.get("relaties", []), objecten, kolommen)
    lijst = band_ordenen(lijst, bruggen, kolommen)
    horizontaal, verticaal, verwijzingen, weggelaten, lussen, cel = relaties_kiezen(
        model, selectie, lijst, kolommen)
    maat_vakken(lijst, verwijzingen, lussen, selectie.get("oeapi", False))
    opmaak = plaatsen(lijst, kolommen, rijen, horizontaal, verticaal, cel, bruggen)
    vb = voorbeeld_lezen(selectie, lijst)
    vb_breed, vb_inhoud = voorbeeld_maat(vb) if vb else (0, 0)

    titel = selectie.get("titel") or selectie.get("vraag") or "Uitsnede uit het informatiemodel"
    herkomst = selectie.get("herkomst") or ""
    label_b = max([tw(t, 12) for t in rij_labels if t] or [0])
    verschuif = (label_b + 16) if label_b else 0
    kop_h = 22 + (HERKOMST_MAAT + 8 if herkomst else 0) + 16
    band_hoog = opmaak["band_hoog"]
    band_totaal = (KOL_TAB_H + band_hoog + BAND_GOOT) if band_hoog else 0
    raster_y = DOEK_MARGE + kop_h + KOL_TAB_H + KOL_MARGE + band_totaal

    for e in lijst:
        e["x"] += verschuif
        e["y"] += raster_y
    for h in horizontaal:
        h["y"] += raster_y
    for v in verticaal:
        v["x_bovenrand"] += verschuif
        v["x_onderrand"] += verschuif
        v["y_bovenrand"] += raster_y
        v["y_onderrand"] += raster_y
        if "baan_y" in v:
            v["baan_y"] += raster_y

    body = ""
    if band_hoog:
        # de band spant over de kolommen die zij verbindt, en minstens over het hele raster
        band_breed = max(opmaak["breed"], opmaak["band_rand"] - DOEK_MARGE)
        body += groepering(BAND_NAAM, DOEK_MARGE + verschuif, band_breed,
                           raster_y - KOL_TAB_H - BAND_GOOT - band_hoog, band_hoog + KOL_MARGE)
    for kolom in kolommen:
        body += groepering(kolom, opmaak["kol_x"][kolom] + verschuif, opmaak["kol_breedte"][kolom],
                           raster_y, opmaak["hoog"] + KOL_MARGE)
    # het voorbeeldblok staat rechts van de kolommen, met zijn tab op dezelfde hoogte als de
    # hunne, en reikt minstens zo ver omlaag als het raster
    vb_hoog = max(vb_inhoud, opmaak["hoog"] + KOL_MARGE) if vb else 0
    vb_x = DOEK_MARGE + verschuif + opmaak["breed"] + KOL_GOOT
    if vb:
        body += voorbeeld_blok(vb, vb_x, raster_y, vb_breed, vb_hoog)
    for r, label in enumerate(rij_labels):
        if label:
            body += text(DOEK_MARGE, raster_y + opmaak["rij_y"][r] + 22, label, 12, fill=MUTED)

    segmenten = []
    lijnen = ""
    for h in horizontaal:
        links, rechts = sorted((h["bron"], h["doel"]), key=lambda e: e["x"])
        x1, x2 = links["x"] + links["w"], rechts["x"]
        bron_links = h["bron"] is links
        svg, seg = relatie_h(x1 if bron_links else x2, x2 if bron_links else x1, h["y"],
                             h["soort"], labelregels(h), h.get("accent", False),
                             h.get("ontbreekt", False))
        lijnen += groep("relatie", _relatienaam(h), svg)
        segmenten += seg
    for v in verticaal:
        # de bron hecht aan op de rand die naar de rijgoot wijst: onderrand als de bron op de
        # bovenste rij staat, bovenrand als zij op de onderste staat
        bron_rand = "onderrand" if v["bron"] is v["boven"] else "bovenrand"
        doel_rand = "bovenrand" if bron_rand == "onderrand" else "onderrand"
        svg, seg = relatie_v(v["x_" + bron_rand], v["y_" + bron_rand],
                             v["x_" + doel_rand], v["y_" + doel_rand],
                             v.get("baan_y", v["y_" + bron_rand]), v["soort"], labelregels(v),
                             v.get("accent", False), v.get("ontbreekt", False))
        lijnen += groep("relatie", _relatienaam(v), svg)
        segmenten += seg
    body += groep("relaties", "", lijnen)
    body += groep("vakken", "", "".join(vak(e) for e in lijst))

    # de lussen gaan over de vakken heen: zij liggen binnen het vak en zouden anders onder de
    # vulling verdwijnen
    lusvormen = ""
    for e in lijst:
        for n, lus in enumerate(e["lussen"]):
            svg, seg = relatie_lus(e, lus["soort"], n)
            lusvormen += groep("relatie", _lusnaam(lus), svg)
            segmenten += seg
    body += groep("lussen", "", lusvormen)

    # de leeswijzer: per genummerd objecttype een regel, in drie stukken op dezelfde hoogte.
    # Het nummer staat in de accentkleur en de naam vet, zodat de regel bij het vak hoort dat
    # hetzelfde nummer draagt; de reden staat grijs erachter.
    leesregels = _leesregels(lijst)

    # het doek is zo breed als het breedste dat erop staat: het raster, de kop, de labels van
    # de verticale relaties, die naast hun lijn staan en in de rechtste kolom voorbij het raster
    # schuiven, en de regels van de leeswijzer, die elk op een regel blijven.
    breed = max(DOEK_MARGE + verschuif + opmaak["breed"] + DOEK_MARGE,
                DOEK_MARGE + verschuif + (opmaak["band_rand"] - DOEK_MARGE) + DOEK_MARGE,
                DOEK_MARGE + tw(titel, TITEL_MAAT, True) + DOEK_MARGE,
                DOEK_MARGE + tw(herkomst, HERKOMST_MAAT) + DOEK_MARGE,
                max([label_rechterrand(v) for v in verticaal] or [0]) + DOEK_MARGE,
                DOEK_MARGE + max([r["breed"] for r in leesregels] or [0]) + DOEK_MARGE,
                (vb_x + vb_breed + DOEK_MARGE) if vb else 0)
    y = raster_y + max(opmaak["hoog"] + KOL_MARGE, vb_hoog) + 28

    onder = ""
    for r in leesregels:
        onder += text(DOEK_MARGE, y, str(r["nummer"]), LEES_MAAT, True, ACCENT)
        onder += text(DOEK_MARGE + r["x_naam"], y, r["naam"], LEES_MAAT, True, INK)
        onder += text(DOEK_MARGE + r["x_waarom"], y, r["waarom"], LEES_MAAT, fill=MUTED)
        y += LEES_MAAT + 9
    body += groep("leeswijzer", "", onder)

    tegels = legenda_regels(lijst, horizontaal, verticaal, lussen, verwijzingen)
    svg, extra = legenda(DOEK_MARGE, y + 10, tegels, breed - 2 * DOEK_MARGE)
    body += groep("legenda", "", svg)
    hoog_doek = y + 10 + extra + 14

    onderregels = len(leesregels) + (extra // 24 + 1 if tegels else 0)
    if onderregels > MAX_ONDERREGELS:
        raise Fout(f"de tekst onder het beeld telt {onderregels} regels (hoogstens "
                   f"{MAX_ONDERREGELS}, de legenda meegerekend). Haal een genummerd objecttype "
                   "uit de selectie of laat het beeld zelf zeggen wat de regel zegt")

    kop = text(DOEK_MARGE, DOEK_MARGE + 20, titel, TITEL_MAAT, True, INK)
    if herkomst:
        kop += text(DOEK_MARGE, DOEK_MARGE + 20 + HERKOMST_MAAT + 8, herkomst, HERKOMST_MAAT,
                    fill=MUTED)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breed:.0f} {hoog_doek:.0f}" '
           f'width="{breed:.0f}" height="{hoog_doek:.0f}">'
           f'<rect x="0.5" y="0.5" width="{breed - 1:.0f}" height="{hoog_doek - 1:.0f}" rx="10" '
           f'fill="#ffffff" stroke="{LIJN}"/>{kop}{body}</svg>')
    band_melding = []
    for e in lijst:
        if not e["band"]:
            continue
        brug = bruggen.get(id(e))
        if not brug:
            plek = "midden boven het raster, geen grens af te leiden uit zijn relaties"
        elif brug[0] == brug[1]:
            plek = f"boven de kolom {brug[0]}"
        else:
            plek = f"boven de grens tussen {brug[0]} en {brug[1]}"
        band_melding.append(f"{e['naam']}: {plek}")
    melding = dict(vakken=len(lijst), kolommen=len(kolommen), rijen=rijen, band=band_melding,
                   voorbeeld=(f"{vb['kop']}: {vb['zin']}" if vb else None),
                   horizontaal=len(horizontaal), verticaal=len(verticaal), lussen=len(lussen),
                   weggelaten=weggelaten, onderregels=onderregels,
                   zelf=[f"{lus['vak']['naam']}: {lus['soort']} op zichzelf" for lus in lussen],
                   kruisingen=len(kruisingen(segmenten)),
                   breed=round(breed), hoog=round(hoog_doek))
    return svg, melding


def teken(model, selectie, uit):
    """Schrijft de uitsnede; geeft (pad, melding)."""
    svg, melding = bouw(model, selectie)
    uit = pathlib.Path(uit)
    if uit.suffix.lower() == ".svg":
        doel = uit
        doel.parent.mkdir(parents=True, exist_ok=True)
    else:
        uit.mkdir(parents=True, exist_ok=True)
        doel = uit / f"{slug(selectie.get('id') or selectie.get('titel') or 'uitsnede')}.svg"
    doel.write_text(svg, encoding="utf-8")
    return doel, melding


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--selectie", type=pathlib.Path, required=True)
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    parser.add_argument("--streng", action="store_true",
                        help="eindig met een foutcode zodra er een kruising of een weggelaten relatie is")
    args = parser.parse_args(argv)
    for pad in (args.model, args.selectie):
        if not pad.exists():
            print(f"bestand niet gevonden: {pad}", file=sys.stderr)
            return 2
    model, selectie = lees(args.model, args.selectie)
    try:
        doel, melding = teken(model, selectie, args.uit)
    except Fout as fout:
        print(f"uitsnede niet getekend: {fout}", file=sys.stderr)
        return 2
    print(f"{doel}: {melding['breed']} bij {melding['hoog']}, {melding['vakken']} objecttypen in "
          f"{melding['kolommen']} kolommen en {melding['rijen']} rijen, "
          f"{melding['horizontaal'] + melding['verticaal'] + melding['lussen']} relaties "
          f"waarvan {melding['lussen']} op zichzelf, {melding['kruisingen']} kruisingen, "
          f"{melding['onderregels']} regels onder het beeld")
    for regel in melding["weggelaten"]:
        print(f"  als verwijzing in het vak: {regel}")
    for regel in melding["zelf"]:
        print(f"  als lus in het vak: {regel}")
    for regel in melding["band"]:
        print(f"  in de band boven de kolommen: {regel}")
    if melding["voorbeeld"]:
        print(f"  als blok naast het raster: {melding['voorbeeld']}")
    if args.streng and (melding["kruisingen"] or melding["weggelaten"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
