#!/usr/bin/env python3
"""Leidt een invulsjabloon af uit een uitgewerkt OKx-document.

Het sjabloon is niet met de hand geschreven: het wordt afgeleid uit de
uitwerking die er al ligt. Zo draagt het elke kop en elke tabel van het
origineel, en loopt het niet achter wanneer die uitwerking wijzigt.

Vier dingen gebeuren er per hoofdstuk:

- de kop wordt een feitelijk label, hernummerd, met de termen van die ene
  uitwerking vervangen door een invulhaak;
- er komt een verwachtingsblok onder: welk voorbeeld, welk artefact, welke
  user stories, en wanneer het hoofdstuk klaar is;
- wat de uitwerking daar levert bepaalt welk artefact wordt verwacht, want
  een hoofdstuk met een procesdiagram vraagt om een procesdiagram;
- een beeld gaat als beeld mee en niet als beschrijving van een beeld.

    python3 tools/scripts/maak-sjabloon-uit-document.py
    python3 tools/scripts/maak-sjabloon-uit-document.py --sjabloon persona

Relateert aan: #554
"""

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
MAP = WORTEL / "architecture/docs/sjablonen"
CONFIG = MAP / "bron/sjablonen.json"
UIT = MAP / "gegenereerd"

KOP = re.compile(r"^(#{1,6}) +(.*)$")
TABELRIJ = re.compile(r"^\|.*\|\s*$")
SCHEIDING = re.compile(r"^\|[\s:|-]+\|\s*$")
BEELD = re.compile(r"^!\[([^\]]*)\]\(<?([^)>]*)>?\)\s*$")
FENCE = re.compile(r"^```(\w*)\s*$")
NUMMER = re.compile(r"^\d+(\.\d+)*\.?\s+")
LINK = re.compile(r"\]\((<[^>]*>|[^)]*)\)")
DOEL = re.compile(r"\]\((<[^>]*>|[^)]*)\)")

RUIMTE = "*Schrijf hier de uitwerking.*"

# Een pagina-einde en een inhoudsopgave bestaan niet in markdown. Zij gaan als
# ruw blok mee, en nadrukkelijk als blok: een ruwe regel binnen een alinea
# levert een w:p binnen een w:p op, en dat weigert Word te openen.
PAGINA_EINDE = """```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```"""

def omslagtabel(versie: str) -> str:
    """De velden op de omslag, zonder randen.

    Pandoc geeft elke markdown-tabel dezelfde stijl, en die draagt randen.
    Op een omslag staat dat onrustig, dus deze tabel gaat als ruw blok mee.
    """
    rijen = [("Versie", versie),
             ("Auteurs", "OKx, pijler Leren Zonder Drempels (Npuls)"),
             ("Datum", "datum van invullen")]
    cellen = "".join(
        '<w:tr>'
        f'<w:tc><w:tcPr><w:tcW w:w="2400" w:type="dxa"/></w:tcPr>'
        f'<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>{kop}</w:t></w:r></w:p></w:tc>'
        f'<w:tc><w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr>'
        f'<w:p><w:r><w:t xml:space="preserve">{waarde}</w:t></w:r></w:p></w:tc>'
        '</w:tr>'
        for kop, waarde in rijen)
    return ("```{=openxml}\n"
            '<w:tbl><w:tblPr><w:tblW w:w="8400" w:type="dxa"/>'
            '<w:tblBorders><w:top w:val="none"/><w:left w:val="none"/>'
            '<w:bottom w:val="none"/><w:right w:val="none"/>'
            '<w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders>'
            '<w:tblCellMar><w:left w:w="0" w:type="dxa"/>'
            '<w:right w:w="240" w:type="dxa"/></w:tblCellMar></w:tblPr>'
            f"{cellen}</w:tbl>\n```")


INHOUDSOPGAVE = """```{=openxml}
<w:p><w:pPr><w:pStyle w:val="Kop1zondernummer"/></w:pPr>
<w:r><w:t>Inhoudsopgave</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>
<w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="separate"/></w:r>
<w:r><w:t xml:space="preserve">Werk deze inhoudsopgave bij met Ctrl+A en F9.</w:t></w:r>
<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
```"""
# Een beeld gaat verkleind mee: A4 op 150 dpi is ruim 1200 pixels breed, dus
# boven deze maat draagt een beeld alleen bestandsgrootte en geen scherpte.
MAXBREEDTE = 1600
# Een vectorbeeld wordt een PNG, want het Word-formaat kan geen SVG dragen.
# Een lijntekening heeft weinig kleuren nodig: met een palet van 64 is zij
# niet van het origineel te onderscheiden en een vijfde zo groot.
RASTERBREEDTE = 1200
KLEUREN = 64

# De productafbakening staat in elk sjabloon, met het vak van dit product
# uitgelicht: de invuller ziet waar zijn document in het geheel past.
BREAKDOWN = "architecture/product-breakdown/img/product-breakdown-v0.2.0.svg"
# Onder de uitsnede staat de hele plaat in het klein, met de uitsnede omkaderd.
KAARTBREEDTE = 330
LETTER = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LETTER_VET = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ACCENT = (221, 120, 75)        # Npuls-oranje
DOFHEID = 0.55                 # hoeveel de omgeving naar wit verschuift
# De hele plaat is op paginabreedte onleesbaar. Een uitsnede rond het eigen vak
# toont wat de invuller nodig heeft: de buren en de pijlen ertussen.
MARGE = (430, 250)
# De plaat is een SVG met een viewBox die op -16 begint; op deze breedte komt
# een eenheid uit de SVG overeen met een beeldpunt.
PLAATBREEDTE = 1514
PLAATOFFSET = 16
BLOB = "https://github.com/Npuls-OKx/meta/blob"

# Wat de uitwerking in een hoofdstuk levert, bepaalt wat het sjabloon daar
# verwacht. De eis erachter is wat het hoofdstuk af maakt.
ARTEFACTEN = {
    "diagram": ("een procesplaat in mermaid, BPMN, UML of vergelijkbaar",
                "het diagram toont de terugweg en het foutpad, en elke stap "
                "noemt de rol die handelt en het systeem dat zij gebruikt"),
    "beeld": ("een beeld",
              "het beeld staat in het document zelf, met een regel eronder die "
              "zegt waar de lezer naar moet kijken"),
    "tabel": ("een ingevulde tabel",
              "elke rij is ingevuld, of doorgehaald met de reden erbij"),
    "opsomming": ("een opsomming",
                  "elk punt is een uitspraak die te toetsen is, geen onderwerp"),
    "tekst": ("een beschrijving in lopende tekst",
              "de tekst noemt wie handelt, met welk systeem, en welke "
              "informatie van waar naar waar beweegt"),
}

# Niet elk hoofdstuk levert hetzelfde aan het pakket van eisen. Een journey
# brengt een behoefte naar boven, een procesbeschrijving zegt wat de instelling
# moet kunnen, een gegevens- of systeemhoofdstuk wat een component moet doen,
# en een interactiehoofdstuk wat er over het koppelvlak gaat.
LAGEN = {
    "user story": "**User stories** *de behoeften die hier naar boven komen; "
                  "schrijf elke behoefte uit als user story, bij de stap waar "
                  "zij ontstaat*",
    "business": "**Instellingseisen** *wat de instelling moet kunnen; schrijf "
                "elke eis uit met zijn nummer, bij de stap, het scenario of de "
                "fase waar hij ontstaat*",
    "functional": "**Functionele eisen** *wat een component moet doen met "
                  "welke gegevens; schrijf elke eis uit met zijn nummer en de "
                  "instellingseis waaruit hij komt*",
    "technical": "**Technische eisen** *wat er over het koppelvlak gaat en in "
                 "welke vorm; die liggen in de interactieketen zelf vast*",
    "context": "**Eisen** *dit hoofdstuk levert geen eis op; het geeft de "
               "context waarin de eisen van de andere hoofdstukken te lezen "
               "zijn*",
}

# Een eis is pas bruikbaar voor de solutionlaag wanneer een leverancier hem kan
# lezen zonder de instelling te bellen. Per soort staat hier waaraan hij
# voldoet, met een zwak en een sterk voorbeeld uit leerroute 1.
EISSOORTEN = {
    "user story": {
        "naam": "Een user story",
        "criteria": [
            "heeft de vorm `Als <persona> wil ik <wat> met als doel dat "
            "<waarde>`",
            "noemt de stap van de reis waarin de behoefte ontstaat",
            "noemt wat de persona wil kunnen en waarom; welk systeem dat "
            "draagt volgt in de eisen",
            "is herkenbaar bij meerdere instellingen; wat bij een instelling "
            "speelt staat onder Afwijkingen per instelling",
        ],
        "voorbeelden": [
            ("Als student wil ik een overzichtelijke app voor mijn keuzedelen",
             "noemt een systeem; de stap en de waarde ontbreken",
             "Als student wil ik bij mijn keuzedeelruimte een geprioriteerde "
             "voorkeurslijst opgeven, met als doel dat ik niet zonder "
             "keuzedeel kom te zitten wanneer mijn eerste keuze vol is"),
            ("Als instelling willen wij beter kunnen plannen",
             "noemt een organisatie in plaats van een persona; de stap en "
             "de waarde ontbreken",
             "Als planner wil ik de haalbaarheid van een opleiding bepalen "
             "voordat het onderwijsaanbod wordt gepubliceerd, met als doel "
             "dat studenten zich alleen oriënteren op aanbod dat de "
             "instelling kan uitvoeren"),
        ],
    },
    "instellingseis": {
        "naam": "Een instellingseis",
        "criteria": [
            "is een zin die opent met `De instelling kan`",
            "noemt een vermogen van de instelling; het systeem dat het draagt "
            "volgt in de functionele eis",
            "is toetsbaar: er is een situatie te noemen waarin vaststaat of "
            "de instelling het kan",
            "noemt zijn herkomst: de persona met de stap, het scenario of de "
            "procesfase",
            "geldt bij meerdere instellingen; wat bij een instelling speelt "
            "staat onder Afwijkingen per instelling",
            "draagt een vermogen; een tweede vermogen krijgt een eigen nummer",
        ],
        "voorbeelden": [
            ("De instelling wil flexibel omgaan met keuzedelen",
             "er is geen situatie waarin vaststaat of het kan",
             "De instelling kan per keuzedeelruimte de voorkeursvolgorde van "
             "de student vastleggen voordat zij plaatst"),
            ("Het roosterpakket stuurt een melding wanneer een keuzedeel vol "
             "zit",
             "noemt een product en een oplossing; het vermogen van de "
             "instelling ontbreekt",
             "De instelling kan signaleren dat de keuzedeelruimte van een "
             "student oningevuld blijft, op een moment dat de student nog "
             "een nieuwe keuze kan maken"),
        ],
    },
    "functionele eis": {
        "naam": "Een functionele eis",
        "criteria": [
            "is een zin die opent met de applicatiecomponent, in de naam van "
            "de [hoofdplaat informatiestromen]"
            "(https://github.com/Npuls-OKx/meta/blob/dev/project/README.md)",
            "noemt wat de component doet en met welke informatieobjecten, "
            "elk met de naam van het objecttype uit de "
            "[begrippenlijst](https://github.com/Npuls-OKx/meta/blob/"
            "dev/architecture/docs/specificatie/begrippen/begrippenlijst.md), "
            "tussen backquotes",
            "kiest het objecttype dat bij het moment past: een `Aanmelding` "
            "op aanbod is een wens, een verbintenis bestaat pas wanneer zij "
            "is aangegaan",
            "noemt de instellingseis waaruit hij komt",
            "beschrijft gedrag; formaat, protocol en veldnamen volgen in de "
            "technische eis",
            "is toetsbaar: er is een invoer te noemen met de uitkomst die de "
            "component dan geeft",
            "draagt een gedrag; een tweede gedrag krijgt een eigen nummer",
        ],
        "voorbeelden": [
            ("Het systeem ondersteunt voorkeuren voor keuzedelen",
             "de component, de gegevens en het gedrag ontbreken",
             "Het Student Keuze Systeem legt per keuzedeelruimte de "
             "`Aanmeldingen` van een student vast in volgorde van voorkeur, "
             "elk op een `Keuzedeel aanbod` met zijn onderwijsperiode en "
             "optioneel de onderwijslocatie"),
            ("Het Student Keuze Systeem stuurt de voorkeuren als JSON-lijst "
             "naar het Planningssysteem",
             "legt het formaat vast; dat hoort in de technische eis",
             "Het Student Keuze Systeem levert per voorkeur van een student "
             "de `Aanmelding` op het `Keuzedeel aanbod` aan het "
             "Planningssysteem, met haar plaats in de volgorde"),
        ],
    },
}


def vervang(tekst: str, paren: list[list[str]]) -> str:
    """Vervangt bronspecifieke termen, met de hoofdletter van het origineel.

    De bron schrijft "Leerroute 1" in een kop en "leerroute 1" in een zin; een
    vervanging die dat negeert zet midden in een kop een kleine letter. Een
    linkdoel blijft heel, want daar is de naam een pad en geen inhoud.
    """
    def zelfde_kop(nieuw: str, gevonden: str) -> str:
        if gevonden[:1].isupper() and nieuw[:1].islower():
            return nieuw[:1].upper() + nieuw[1:]
        return nieuw

    doelen: list[str] = []

    def bewaar(m: re.Match) -> str:
        doelen.append(m.group(0))
        return f"\x00{len(doelen) - 1}\x00"

    tekst = DOEL.sub(bewaar, tekst)
    for oud, nieuw in paren:
        tekst = re.sub(re.escape(oud),
                       lambda m: zelfde_kop(nieuw, m.group(0)),
                       tekst, flags=re.I)
    return re.sub(r"\x00(\d+)\x00", lambda m: doelen[int(m.group(1))], tekst)


def zonder_linkdoelen(tekst: str) -> str:
    return DOEL.sub("]()", tekst)


def bronspecifiek(tekst: str, paren: list[list[str]]) -> bool:
    tekst = zonder_linkdoelen(tekst)
    return any(re.search(re.escape(oud), tekst, re.I) for oud, _ in paren)


def anker(kop: str) -> str:
    """De GitHub-verankering van een kop, zodat een voorbeeld aanwijsbaar is."""
    a = kop.lower()
    a = re.sub(r"[^\w\s-]", "", a, flags=re.U)
    return a.strip().replace(" ", "-")


def label(kop: str, labels: dict[str, str]) -> str:
    """Maakt van een kop een feitelijk label.

    Een kop is een naam voor wat eronder staat, geen zin en geen vraag. Een
    vraagkop die niet in de lijst staat wordt afgekapt tot zijn onderwerp; dat
    is een terugval, en de lijst is de plek om het goed te doen.
    """
    kaal = NUMMER.sub("", kop).strip()
    for bron, naar in labels.items():
        if kaal.lower() == bron.lower():
            return naar
    if kaal.endswith("?"):
        kaal = kaal.rstrip("?").strip()
        kaal = re.sub(r"^(Wat is|Wat betekent|Wat levert|Wat doet|Hoe|Waarom|"
                      r"Wanneer|Welke|Wie)\s+", "", kaal, flags=re.I)
        kaal = kaal[:1].upper() + kaal[1:] if kaal else kop
    return kaal


def vak_in_de_plaat(svg: str, titel: str) -> tuple[int, int, int, int]:
    """Zoekt het vak van een product op in de plaat.

    Het vak wordt niet met de hand opgemeten maar afgeleid: zoek de kop met
    deze naam, en neem de rechthoek van productformaat die haar omsluit. Zo
    blijft de uitlichting kloppen wanneer de plaat verschuift.
    """
    kop = re.search(
        r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>%s</text>' % re.escape(titel), svg)
    if not kop:
        raise SystemExit(f"de plaat kent geen vak {titel!r}")
    tx, ty = float(kop.group(1)), float(kop.group(2))
    vakken = [tuple(float(x) for x in m.groups()) for m in re.finditer(
        r'<rect x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"',
        svg)]
    omsluit = [v for v in vakken
               if 140 < v[2] < 260 and 60 < v[3] < 120
               and v[0] <= tx <= v[0] + v[2] and v[1] <= ty <= v[1] + v[3]]
    if not omsluit:
        raise SystemExit(f"geen vak gevonden om de kop {titel!r} heen")
    x, y, b, h = omsluit[0]
    return (round(x) + PLAATOFFSET, round(y) + PLAATOFFSET,
            round(x + b) + PLAATOFFSET, round(y + h) + PLAATOFFSET)


def uitgelicht(bron: pathlib.Path, doel: pathlib.Path,
               vak: tuple[int, int, int, int]) -> None:
    """Zet de productafbakening neer met een vak uitgelicht.

    De omgeving verschuift naar wit en het eigen vak blijft staan, met een
    accentrand eromheen. Zo blijft zichtbaar waar het product in het geheel
    hangt, zonder dat de rest de aandacht trekt.
    """
    from PIL import Image, ImageDraw
    if not shutil.which("rsvg-convert"):
        raise SystemExit("rsvg-convert ontbreekt; installeer librsvg2-bin in "
                         "de dev-container")
    tussen = doel.with_suffix(".tussen.png")
    kop = re.search(r'viewBox="-?[\d.]+ -?[\d.]+ ([\d.]+) [\d.]+"',
                    bron.read_text(encoding="utf-8"))
    breedte = round(float(kop.group(1))) if kop else PLAATBREEDTE
    subprocess.run(["rsvg-convert", "-w", str(breedte), str(bron),
                    "-o", str(tussen)], check=True, capture_output=True)
    with Image.open(tussen) as beeld:
        plat = Image.new("RGB", beeld.size, "white")
        plat.paste(beeld, mask=beeld.split()[-1] if beeld.mode == "RGBA" else None)
        dof = Image.blend(plat, Image.new("RGB", plat.size, "white"), DOFHEID)
        dof.paste(plat.crop(vak), (vak[0], vak[1]))
        tekenaar = ImageDraw.Draw(dof)
        rand = 4
        tekenaar.rectangle(
            [vak[0] - rand, vak[1] - rand, vak[2] + rand, vak[3] + rand],
            outline=ACCENT, width=rand)
        venster = (max(0, vak[0] - MARGE[0]), max(0, vak[1] - MARGE[1]),
                   min(dof.width, vak[2] + MARGE[0]),
                   min(dof.height, vak[3] + MARGE[1]))
        met_kaart(dof, vak, venster, plat).quantize(colors=128).save(doel, optimize=True)
    tussen.unlink()


def met_kaart(plaat, vak, venster, helder):
    """Zet onder de uitsnede de hele plaat in het klein, met de uitsnede omkaderd.

    Een uitsnede alleen zegt niet waar zij in het geheel ligt. De kleine plaat
    eronder is de kaart: het kader is het stuk waarop is ingezoomd, het
    gevulde vlak het product van dit sjabloon.
    """
    from PIL import Image, ImageDraw, ImageFont
    uitsnede = plaat.crop(venster)
    schaal = KAARTBREEDTE / plaat.width
    kaart = helder.resize((KAARTBREEDTE, round(plaat.height * schaal)),
                         Image.LANCZOS)
    t = ImageDraw.Draw(kaart)
    t.rectangle([round(c * schaal) for c in venster], outline=ACCENT, width=3)
    t.rectangle([round(c * schaal) for c in vak], fill=ACCENT)
    t.rectangle([0, 0, kaart.width - 1, kaart.height - 1],
                outline=(88, 106, 110), width=1)
    marge = 16
    doek = Image.new("RGB", (uitsnede.width,
                             uitsnede.height + kaart.height + 3 * marge),
                     "white")
    doek.paste(uitsnede, (0, 0))
    onder = uitsnede.height + 2 * marge
    doek.paste(kaart, (marge, onder))
    t = ImageDraw.Draw(doek)
    t.line([0, uitsnede.height + marge // 2, doek.width,
            uitsnede.height + marge // 2], fill=(200, 205, 208), width=1)
    try:
        vet = ImageFont.truetype(LETTER_VET, 17)
        gewoon = ImageFont.truetype(LETTER, 15)
    except OSError:
        vet = gewoon = ImageFont.load_default()
    x = KAARTBREEDTE + 3 * marge
    t.text((x, onder), "U bent hier", font=vet, fill=(26, 41, 45))
    regels = [("kader", "de uitsnede hierboven, binnen de hele productafbakening"),
              ("vlak", "het product dat u met dit sjabloon beschrijft"),
              (None, "de rest van de plaat staat links in het klein")]
    y = onder + 34
    for soort, tekst in regels:
        if soort == "kader":
            t.rectangle([x, y + 2, x + 22, y + 16], outline=ACCENT, width=3)
        elif soort == "vlak":
            t.rectangle([x, y + 2, x + 22, y + 16], fill=ACCENT)
        t.text((x + 34, y), tekst, font=gewoon, fill=(26, 41, 45))
        y += 28
    return doek


def raster(bron: pathlib.Path, doel: pathlib.Path) -> None:
    """Zet een vectorbeeld om naar een PNG die Word kan dragen."""
    if not shutil.which("rsvg-convert"):
        raise SystemExit(
            f"rsvg-convert ontbreekt en {bron.name} is een vectorbeeld; "
            "installeer librsvg2-bin in de dev-container")
    tussen = doel.with_suffix(".tussen.png")
    subprocess.run(["rsvg-convert", "-w", str(RASTERBREEDTE),
                    str(bron), "-o", str(tussen)], check=True,
                   capture_output=True)
    try:
        from PIL import Image
    except ImportError:
        tussen.replace(doel)
        return
    with Image.open(tussen) as beeld:
        plat = Image.new("RGB", beeld.size, "white")
        plat.paste(beeld, mask=beeld.split()[-1] if beeld.mode == "RGBA" else None)
        plat.quantize(colors=KLEUREN).save(doel, optimize=True)
    tussen.unlink()


def verklein(bron: pathlib.Path, doel: pathlib.Path) -> None:
    """Kopieert een beeld, verkleind wanneer het breder is dan nodig."""
    if doel.suffix.lower() == ".png" and bron.suffix.lower() == ".svg":
        raster(bron, doel)
        return
    try:
        from PIL import Image
    except ImportError:
        shutil.copy2(bron, doel)
        return
    with Image.open(bron) as beeld:
        if beeld.width <= MAXBREEDTE and bron.stat().st_size < 200_000:
            shutil.copy2(bron, doel)
            return
        breedte = min(beeld.width, MAXBREEDTE)
        hoogte = round(beeld.height * breedte / beeld.width)
        klein = beeld.convert("RGB").resize((breedte, hoogte), Image.LANCZOS)
        if doel.suffix.lower() == ".png":
            # Een procesplaat is vlakke kleur; een palet haalt er een
            # veelvoud af zonder dat je het ziet.
            klein.quantize(colors=256).save(doel, optimize=True)
        else:
            klein.save(doel, quality=85, optimize=True)


class Sjabloon:
    def __init__(self, naam: str, cfg: dict, uitmap: pathlib.Path = UIT):
        self.naam = naam
        self.cfg = cfg
        self.uitmap = uitmap
        self.bronnaam = cfg["bron"]
        self.paren = [list(p) for p in cfg.get("vervang", [])]
        self.koppen_paren = self.paren + [list(x) for x in cfg.get("kop_vervang", [])]
        self.labels = cfg.get("kop_labels", {})
        self.hoofdstukken = cfg.get("hoofdstukken", {})
        self.weg_koppen = [k.lower() for k in cfg.get("kop_weglaten", [])]
        self.weg_tot = cfg.get("weglaten_tot")
        self.weg_vanaf = cfg.get("weglaten_vanaf")
        self.uit: list[str] = []
        self.teller = [0] * 7
        self.beelden: list[tuple[pathlib.Path, str]] = []

    # -- de bron --------------------------------------------------------------

    def ref(self) -> str:
        return self.cfg.get("bron_ref", "dev")

    def bronmap(self) -> pathlib.PurePosixPath:
        return pathlib.PurePosixPath(self.bronnaam).parent

    def brontekst(self) -> str:
        ref = self.cfg.get("bron_ref")
        if ref:
            uit = subprocess.run(["git", "show", f"{ref}:{self.bronnaam}"],
                                 cwd=WORTEL, capture_output=True, text=True)
            if uit.returncode:
                raise SystemExit(
                    f"de bron {self.bronnaam} staat niet op {ref}; haal de tak "
                    "op met git fetch")
            return uit.stdout
        pad = WORTEL / self.bronnaam
        if not pad.exists():
            raise SystemExit(f"de bron {self.bronnaam} bestaat niet")
        return pad.read_text(encoding="utf-8")

    def absoluut(self, tekst: str) -> str:
        """Maakt elke verwijzing volledig; een Word-bestand staat niet in de repository."""
        basis = self.bronmap()

        def een(m: re.Match) -> str:
            doel = m.group(1).strip().strip("<>")
            if doel.startswith(("http://", "https://", "#", "mailto:", "img/")):
                return m.group(0)
            pad, _, ank = doel.partition("#")
            if not pad:
                return m.group(0)
            heel = str(basis / pad)
            while "/../" in heel:
                heel = re.sub(r"[^/]+/\.\./", "", heel, count=1)
            staart = f"#{ank}" if ank else ""
            return f"]({BLOB}/{self.ref()}/{heel}{staart})"

        return LINK.sub(een, tekst)

    # -- de vaste delen -------------------------------------------------------

    def aanhef(self) -> list[str]:
        c = self.cfg
        return [
            # Pagina 1 draagt alleen de omslag: titel, ondertitel, versie en
            # wie het uitgeeft en invult. De titel en de ondertitel komen uit
            # de documenteigenschappen en staan daarom niet in deze lijst.
            omslagtabel(c.get("versie", "0.0.1")),
            "",
            PAGINA_EINDE,
            "",
            "# Inleiding",
            "",
            "| Onderdeel | Inhoud |",
            "|---|------------------------------------------------|",
            f"| Wie dit invult | {c['wie']} |",
            f"| Voorbeeld | {c['voorbeeld']} |",
            f"| Inleveren | {c.get('inleveren', 'terug naar OKx SI als Word-bestand')} |",
            "",
            *self.afbakening(),
            "## Doelstelling document",
            "",
            c["doel"],
            "",
            f"Elk {self.eenheid()} opent met een opdrachtblok: waar hetzelfde "
            "al is uitgewerkt, de acceptatiecriteria waaraan de invulling "
            "voldoet, en welke soort eis het oplevert. Het opdrachtblok blijft "
            "staan; de uitwerking komt eronder.",
            "",
            "## Eisen uit dit document",
            "",
            "OKx kent drie soorten eisen. **Instellingseisen** zeggen wat de "
            "instelling moet kunnen; zij komen uit de inbreng van de "
            "koploperinstellingen in de proef (de PoC-inbreng), de persona's "
            "en de leerroute scenario's "
            "samen. **Functionele eisen** zeggen wat een component moet doen "
            "met welke gegevens; zij komen uit de instellingseisen en de "
            "leerroute scenario uitwerking samen. **Technische eisen** zeggen "
            "wat er over het koppelvlak gaat; zij komen uit de "
            "interactieketens, die zelf uit de eisen voortkomen, en zijn "
            "onderdeel van de koppelvlakspecificatie.",
            "",
            "**De solutionlaag bouwt op wat hier als eis staat.** De "
            "solutionlaag is het deel van OKx dat de koppelvlakken ontwerpt: "
            "het team systeem en informatie (OKx SI), samen met de "
            "leveranciers. OKx SI neemt de instellingseisen en de functionele "
            "eisen over en vertaalt ze met de leveranciers naar technische "
            "eisen. Een behoefte bereikt de leveranciers via een "
            "uitgeschreven eis in dit pakket.",
            "",
            "Elk onderdeel levert een eigen soort. De reis van een persona "
            "brengt een behoefte naar boven en levert user stories. Een "
            "procesbeschrijving zegt wat de instelling moet kunnen. Een "
            "gegevens- of systeemonderdeel zegt wat een component moet doen. "
            "Een interactie zegt wat er over het koppelvlak gaat. Het "
            "opdrachtblok noemt welke soort daar hoort.",
            "",
            "| Soort | Komt uit | Zegt wat |",
            "|---|---|------------------------------------|",
            "| Instellingseis | de PoC-inbreng, de persona's en de leerroute "
            "scenario's samen | de instelling moet kunnen om de scenario's te "
            "realiseren |",
            "| Functionele eis | de instellingseisen en de leerroute scenario "
            "uitwerking | een component moet doen met welke gegevens |",
            "| Technische eis | de interactieketens, die zelf uit de eisen "
            "voortkomen | er over het koppelvlak gaat en in welke vorm |",
            "",
            f"Dit document levert {c['levert']}. Zo ziet zo'n eis eruit, met "
            "de keten erboven en eronder:",
            "",
            "| Soort | Voorbeeld |",
            "|---|------------------------------------------------|",
        ] + [f"| {soort} | {voorbeeld} |" for soort, voorbeeld in c["keten"]] + [
            "",
            *self.kwaliteit(),
            "## Business analyse en aggregatie van pakket van eisen",
            "",
            c["aggregatie"],
            "",
            "Een instelling spreekt voor haar eigen praktijk en niet voor de "
            "sector. Noteer daarom apart wat afwijkt, onder "
            "[Afwijkingen per instelling](#afwijkingen-per-instelling).",
            "",
            "Een hoofdstuk is een interactie, en de business analist bepaalt "
            "waar hij begint en eindigt. Kies de kleinst mogelijke eenheid die "
            "waarde oplevert voor zowel de student als de instelling: groter "
            "dan een enkele interactie, kleiner dan het hele ecosysteem. Een "
            "scope die daarboven zit levert een eis die niemand kan bouwen, "
            "een scope die daaronder zit levert een eis die niemand mist.",
            "",
            INHOUDSOPGAVE,
            "",
            PAGINA_EINDE,
            "",
        ]

    def eenheid(self) -> str:
        return "sjabloononderdeel" if self.cfg.get("opbouw") else "hoofdstuk"

    def kwaliteit(self) -> list[str]:
        """Waaraan een eis voldoet, voor de soorten die dit sjabloon levert."""
        soorten = self.cfg.get("eissoorten", [])
        if not soorten:
            return []
        uit = [
            "## Kwaliteit van een eis",
            "",
            "Een eis is bruikbaar wanneer een leverancier hem kan lezen "
            "zonder de instelling te bellen. Wat hier staat is een voorstel "
            "voor een sectorafspraak: opgesteld uit de inbreng van "
            "afzonderlijke instellingen, vastgelegd als afspraak, en daarna "
            "de grond voor de technische specificatie. Schrijf elke eis uit "
            "op de plek waar hij ontstaat, en toets hem aan de criteria "
            "hieronder.",
            "",
        ]
        for soort in soorten:
            e = EISSOORTEN[soort]
            uit += [f"**{e['naam']}:**", ""]
            uit += [f"{i}. {c};" if i < len(e["criteria"]) else f"{i}. {c}."
                    for i, c in enumerate(e["criteria"], 1)]
            uit.append("")
        uit += ["| Soort | Zwak | Wat eraan ontbreekt | Sterk |",
                "|---|--------|------|------------|"]
        for soort in soorten:
            for zwak, reden, sterk in EISSOORTEN[soort]["voorbeelden"]:
                uit.append(f"| {soort} | {zwak} | {reden} | {sterk} |")
        uit.append("")
        return uit

    def afbakening(self) -> list[str]:
        """De productafbakening, met het vak van dit product uitgelicht."""
        if not self.cfg.get("breakdown_vak"):
            return []
        c = self.cfg
        return [
            "## Productplaatsing",
            "",
            f"![De producten rond {c['titel'].lower()}, met dit product "
            f"uitgelicht](<{self.breakdownpad()}>)",
            "",
            "Het uitgelichte vak is het product dat u met dit sjabloon "
            "beschrijft. De kleine plaat eronder toont de hele "
            "productafbakening, met een kader om deze uitsnede.",
            "",
            f"Het {c['plek']}.",
            "",
            "Het cijfer rechtsboven in een vak is de prioriteit, waarbij lager "
            "eerder is; de hele plaat staat in de "
            "[productafbakening](https://github.com/Npuls-OKx/meta/blob/dev/"
            "architecture/product-breakdown/README.md).",
            "",
        ]

    def slot(self) -> list[str]:
        return [
            "# Afwijkingen per instelling",
            "",
            "Wat bij een instelling anders gaat dan hierboven staat, per regel "
            "met de instelling erbij. Dit is geen restcategorie: hier staat het "
            "materiaal waaruit blijkt of de grootst gemene deler houdbaar is.",
            "",
            "| Instelling | Hoofdstuk | Wat daar anders gaat |",
            "|---|---|------------------------------------|",
            "| | | |",
            "| | | |",
            "| | | |",
            "",
            "# Observaties en signaleringen",
            "",
            "Wat tijdens het invullen opviel en wat openstaat, genummerd. Een "
            "observatie is wat u zag; een signalering is wat daarmee moet "
            "gebeuren, bijvoorbeeld richting OKx, richting een standaard of "
            "richting het eigen bestuur.",
            "",
            "| Nummer | Hoofdstuk | Observatie | Wat er nodig is |",
            "|---|---|---|------------------------------------|",
            "| 1 | | | |",
            "| 2 | | | |",
            "| 3 | | | |",
            "",
        ]

    # -- de doorloop ----------------------------------------------------------

    def nummer(self, niveau: int) -> str:   # niet meer gebruikt; Word telt
        """Hernummert de koppen, want de bron telt op drie plekken 3.2.1.1."""
        i = niveau - 2
        self.teller[i] += 1
        for j in range(i + 1, len(self.teller)):
            self.teller[j] = 0
        return ".".join(str(n) for n in self.teller[:i + 1] if True)

    def verwachting(self, kop_bron: str, kop: str,
                    inhoud: list[str]) -> list[str]:
        eigen = self.hoofdstukken.get(kop, {})
        soorten = []
        tekst = "\n".join(inhoud)
        if "```mermaid" in tekst:
            soorten.append("diagram")
        if re.search(r"^!\[", tekst, re.M):
            soorten.append("beeld")
        if re.search(r"^\|", tekst, re.M):
            soorten.append("tabel")
        if re.search(r"^\s*[-*+] ", tekst, re.M):
            soorten.append("opsomming")
        if not soorten:
            soorten.append("tekst")
        verwacht = eigen.get("artefact") or ", ".join(
            ARTEFACTEN[s][0] for s in soorten)
        eis = eigen.get("eis") or "; ".join(ARTEFACTEN[s][1] for s in soorten)
        context = eigen.get("context")
        if context:
            verwacht = f"{verwacht}, {context}"
        url = f"{BLOB}/{self.ref()}/{self.bronnaam}#{anker(kop_bron)}"
        naam = self.cfg.get("voorbeeld_naam", "de voorbeelduitwerking")
        plek = eigen.get("anker", kop)
        laag = LAGEN[eigen.get("laag", self.cfg.get("laag", "context"))]

        blok = []
        if eigen.get("optioneel"):
            blok += [f"*Optioneel: {eigen['optioneel']}. Geldt het niet voor "
                     "deze route, laat de kop staan met die reden eronder.*", ""]
        criteria = eigen.get("criteria") or (
            [f"er staat {verwacht}"] + [d.strip() for d in eis.split(";")])
        eenheid = self.eenheid()
        blok += [
            f"**Voorbeeld** [{naam}, {plek}]({url})",
            "",
            f"**Acceptatiecriteria** Dit {eenheid} is af wanneer dit klopt:",
            "",
        ]
        blok += [f"{i}. {c};" if i < len(criteria) else f"{i}. {c}."
                 for i, c in enumerate(criteria, 1)]
        blok += ["", laag, ""]
        return blok

    def beeld(self, alt: str, pad: str) -> None:
        """Zet het beeld in het document, niet een beschrijving ervan."""
        bron = WORTEL / self.bronmap() / pad
        if not bron.exists() and (WORTEL / pad).exists():
            # Een sjabloononderdeel noemt zijn voorbeeldbeeld vanaf de wortel, want
            # dat beeld hoeft niet bij de bron van dit sjabloon te liggen.
            bron = WORTEL / pad
        if not bron.exists():
            self.uit += [f"*Beeld ontbreekt in de bron: {alt}.*", ""]
            return
        naam = bron.name
        if bron.suffix.lower() == ".svg":
            naam = bron.with_suffix(".png").name   # Word draagt geen SVG
        doel = f"img/{self.naam}/{naam}"
        self.beelden.append((bron, doel))
        self.uit += [f"![{vervang(alt, self.paren)}](<{doel}>)", ""]

    def tabel(self, blok: list[str]) -> None:
        kop = blok[0]
        scheiding = blok[1] if len(blok) > 1 and SCHEIDING.match(blok[1]) else None
        rijen = blok[2:] if scheiding else blok[1:]
        self.uit.append(vervang(kop, self.paren))
        self.uit.append(scheiding or "|" + "---|" * (kop.count("|") - 1))
        kolommen = kop.count("|") - 1
        for _ in range(max(1, min(len(rijen), 15))):
            self.uit.append("|" + " |" * kolommen)
        self.uit.append("")

    def onderdelen(self) -> str:
        """Een sjabloon dat niet de koppen van een bron volgt.

        Sommige producten zijn geen hoofdstukkenreeks maar een herhaling van
        dezelfde twee blokken tot het onderwerp gedekt is. Dan komt de opbouw
        uit de configuratie en niet uit een bron.
        """
        self.uit = self.aanhef()
        # De eigen criteria van een sjabloononderdeel staan in zijn eigen regel; het
        # verwachtingsblok leest ze uit hoofdstukken.
        self.hoofdstukken = dict(self.hoofdstukken)
        self.hoofdstukken.update(self.cfg["opbouw"])
        for kop, cfg in self.cfg["opbouw"].items():
            self.uit += ["#" * cfg.get("niveau", 1) + f" {kop}", ""]
            if cfg.get("toelichting"):
                self.uit += [cfg["toelichting"], ""]
            if cfg.get("blok", True):
                self.uit += self.verwachting(
                    cfg.get("anker", kop), kop, cfg.get("inhoud", []))
            if cfg.get("voorbeeld_tabel"):
                self.uit += [f"**Ingevuld voorbeeld** uit "
                             f"{cfg.get('voorbeeld_uit', self.cfg['voorbeeld_naam'])}:",
                             "", *cfg["voorbeeld_tabel"], ""]
                for extra in cfg.get("voorbeeld_extra", []):
                    self.uit += [f"**Ingevuld voorbeeld** uit {extra['uit']}:",
                                 "", *extra["tabel"], ""]
                if cfg.get("tabel"):
                    self.uit += ["**Vul in:**", ""]
            if cfg.get("tabel"):
                self.uit += list(cfg["tabel"]) + [""]
            if cfg.get("voorbeeld_beeld"):
                self.beeld(cfg.get("beeld_alt", kop), cfg["voorbeeld_beeld"])
            if cfg.get("ruimte", True):
                self.uit += [RUIMTE, ""]
        self.uit += self.slot()
        tekst = self.absoluut("\n".join(self.uit))
        return re.sub(r"\n{3,}", "\n\n", tekst).strip() + "\n"

    def maak(self) -> str:
        if self.cfg.get("opbouw"):
            return self.onderdelen()
        regels = self.brontekst().splitlines()
        self.uit = self.aanhef()
        secties: list[tuple[int, str, list[str]]] = []
        huidig: tuple[int, str] | None = None
        buffer: list[str] = []

        for regel in regels:
            m = KOP.match(regel)
            if m:
                if huidig:
                    secties.append((huidig[0], huidig[1], buffer))
                huidig, buffer = (len(m.group(1)), m.group(2).strip()), []
                continue
            buffer.append(regel)
        if huidig:
            secties.append((huidig[0], huidig[1], buffer))

        gekozen: list[tuple[int, str, list[str]]] = []
        begonnen = self.weg_tot is None
        for niveau, kop_bron, inhoud in secties:
            if not begonnen:
                if self.weg_tot.lower() in kop_bron.lower():
                    begonnen = True
                else:
                    continue
            if self.weg_vanaf and self.weg_vanaf.lower() in kop_bron.lower():
                break
            if any(w in kop_bron.lower() for w in self.weg_koppen):
                continue
            gekozen.append((niveau, kop_bron, inhoud))
        if not gekozen:
            raise SystemExit(f"{self.naam}: geen enkel hoofdstuk blijft over; "
                             "weglaten_tot of weglaten_vanaf wijst verkeerd")
        basis = min(n for n, _, _ in gekozen)
        for niveau, kop_bron, inhoud in gekozen:
            self.hoofdstuk(1 + niveau - basis, kop_bron, inhoud)

        self.uit += self.slot()
        tekst = self.absoluut("\n".join(self.uit))
        return re.sub(r"\n{3,}", "\n\n", tekst).strip() + "\n"

    def hoofdstuk(self, niveau: int, kop_bron: str, inhoud: list[str]) -> None:
        niveau = max(1, min(6, niveau))

        tekst = vervang(label(kop_bron, self.labels), self.koppen_paren)
        self.uit += [f"{'#' * niveau} {tekst}", ""]
        self.uit += self.verwachting(kop_bron, tekst, inhoud)

        # De beelden en de tabellen van de bron gaan mee; de rest is uitwerking.
        blok: list[str] = []
        in_fence = False
        for regel in inhoud:
            if FENCE.match(regel):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            b = BEELD.match(regel)
            if b:
                if blok:
                    self.tabel(blok)
                    blok = []
                self.beeld(b.group(1), b.group(2))
                continue
            if TABELRIJ.match(regel):
                blok.append(regel)
                continue
            if blok:
                self.tabel(blok)
                blok = []
        if blok:
            self.tabel(blok)
        self.uit += [RUIMTE, ""]

    def schrijf(self) -> pathlib.Path:
        tekst = self.maak()
        doel = self.uitmap / f"{self.naam}.md"
        doel.write_text(tekst, encoding="utf-8")
        beeldmap = self.uitmap / "img" / self.naam
        if beeldmap.exists():
            shutil.rmtree(beeldmap)
        for bron, pad in self.beelden:
            uit = self.uitmap / pad
            uit.parent.mkdir(parents=True, exist_ok=True)
            verklein(bron, uit)
        titel = self.cfg.get("breakdown_vak")
        if titel:
            plaat = WORTEL / BREAKDOWN
            vak = vak_in_de_plaat(plaat.read_text(encoding="utf-8"), titel)
            uit = self.uitmap / self.breakdownpad()
            uit.parent.mkdir(parents=True, exist_ok=True)
            uitgelicht(plaat, uit, vak)
        return doel

    def breakdownpad(self) -> str:
        return f"img/{self.naam}/product-breakdown.png"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", type=pathlib.Path, default=CONFIG)
    p.add_argument("--uit", type=pathlib.Path, default=UIT)
    p.add_argument("--sjabloon", help="alleen dit sjabloon")
    a = p.parse_args(argv)

    config = json.loads(a.config.read_text(encoding="utf-8"))
    namen = [a.sjabloon] if a.sjabloon else list(config)
    onbekend = [n for n in namen if n not in config]
    if onbekend:
        raise SystemExit(f"onbekend sjabloon: {', '.join(onbekend)}")
    a.uit.mkdir(parents=True, exist_ok=True)
    for naam in namen:
        s = Sjabloon(naam, config[naam], a.uit)
        doel = s.schrijf()
        tekst = doel.read_text(encoding="utf-8")
        print(f"  {doel.relative_to(WORTEL)}  "
              f"({len(tekst.splitlines())} regels, "
              f"{len([r for r in tekst.splitlines() if r.startswith('#')])} koppen, "
              f"{len(s.beelden)} beelden)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
