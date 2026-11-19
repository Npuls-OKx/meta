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
# Een beeld gaat verkleind mee: A4 op 150 dpi is ruim 1200 pixels breed, dus
# boven deze maat draagt een beeld alleen bestandsgrootte en geen scherpte.
MAXBREEDTE = 1600
# Een vectorbeeld wordt een PNG, want het Word-formaat kan geen SVG dragen.
# Een lijntekening heeft weinig kleuren nodig: met een palet van 64 is zij
# niet van het origineel te onderscheiden en een vijfde zo groot.
RASTERBREEDTE = 1200
KLEUREN = 64
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
    "user story": "**User stories** *vul de nummers in uit het pakket van "
                  "eisen die dit hoofdstuk naar boven brengt; een story noemt "
                  "de rol, de wens en het doel*",
    "business": "**Business requirements** *wat de instelling moet kunnen om "
                "de stories van dit hoofdstuk waar te maken; verwijs naar het "
                "nummer van de story*",
    "functional": "**Functional requirements** *wat een component moet doen "
                  "met welke gegevens; verwijs naar het nummer van de story*",
    "technical": "**Technical requirements** *wat er over het koppelvlak gaat "
                 "en in welke vorm; verwijs naar het nummer van de story*",
    "context": "**Pakket van eisen** *dit hoofdstuk levert geen eis op; het "
               "geeft de context waarin de eisen van de andere hoofdstukken "
               "te lezen zijn*",
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
            # De omslag en de inhoudsopgave krijgen een eigen pagina.
            "`<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>`{=openxml}",
            "",
            "# Invullen",
            "",
            "| Onderdeel | Inhoud |",
            "|---|------------------------------------------------|",
            f"| Wat dit wordt | {c['wat']} |",
            f"| Wie dit invult | {c['wie']} |",
            f"| Voorbeeld | {c['voorbeeld']} |",
            "| Inleveren | terug naar OKx SI als Word-bestand |",
            "",
            "Elk hoofdstuk opent met een blok dat zegt wat er van dat hoofdstuk "
            "wordt verwacht: waar hetzelfde al is uitgewerkt, welk artefact "
            "hier hoort en waaraan het voldoet, en wat dit hoofdstuk aan het "
            "pakket van eisen bijdraagt. Dat blok blijft staan; het is de "
            "opdracht en niet de uitwerking. Een hoofdstuk dat niet van "
            "toepassing is houdt zijn kop, met de reden eronder.",
            "",
            "# Van user story naar eis",
            "",
            "Het pakket van eisen komt uit de gedeelde analyse van alles wat "
            "scholen hebben ingebracht, geinventariseerd in de PoC-sessies met "
            "de koploperscholen. De grootst gemene deler daaruit is wat OKx "
            "vastlegt.",
            "",
            "Niet elk hoofdstuk levert hetzelfde. Een journey brengt een "
            "behoefte naar boven en levert user stories. Een procesbeschrijving "
            "zegt wat de instelling moet kunnen. Een gegevens- of "
            "systeemhoofdstuk zegt wat een component moet doen. Een "
            "interactiehoofdstuk zegt wat er over het koppelvlak gaat. Het blok "
            "boven elk hoofdstuk noemt welke laag daar hoort.",
            "",
            "| Laag | Waar die ontstaat | Voorbeeld |",
            "|---|---|------------------------------------|",
            "| User story | in een journey of een scenario | Als student wil "
            "ik bij mijn keuzedeelruimte een geprioriteerde voorkeurslijst "
            "opgeven, met als doel dat ik niet zonder keuzedeel kom te zitten "
            "wanneer mijn eerste keuze vol is |",
            "| Business requirement | in een procesbeschrijving | de instelling "
            "kent per keuzedeelruimte de voorkeursvolgorde van de student "
            "voordat zij plaatst |",
            "| Functional requirement | in een gegevens- of systeemhoofdstuk | "
            "het studentkeuzesysteem legt per keuzedeelruimte een geordende "
            "lijst voorkeuren vast, met per voorkeur het onderdeel, de periode "
            "en de locatie |",
            "| Technical requirement | in een interactiehoofdstuk | de "
            "voorkeurslijst gaat als geordende verzameling over het koppelvlak, "
            "met de volgorde expliciet in het bericht en niet afgeleid uit de "
            "positie |",
            "",
            "Vul in dit document de laag in die boven het hoofdstuk staat. De "
            "lagen eronder volgen in een eigen ronde, met dit document als bron.",
            "",
            "# De grootst gemene deler",
            "",
            c["aggregatie"],
            "",
            "Een instelling spreekt voor haar eigen praktijk en niet voor de "
            "sector. Noteer daarom apart wat afwijkt, onder "
            "[Afwijkingen per instelling](#afwijkingen-per-instelling).",
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
            "# Vragen aan OKx",
            "",
            "Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar "
            "het speelt.",
            "",
            "| Nummer | Hoofdstuk | Vraag |",
            "|---|---|------------------------------------|",
            "| 1 | | |",
            "| 2 | | |",
            "| 3 | | |",
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
        laag = LAGEN[eigen.get("laag", self.cfg.get("laag", "context"))]

        blok = []
        if eigen.get("optioneel"):
            blok += [f"*Optioneel: {eigen['optioneel']}. Geldt het niet voor "
                     "deze route, laat de kop staan met die reden eronder.*", ""]
        blok += [
            f"**Voorbeeld** [{naam}, {kop}]({url})",
            "",
            f"**Acceptatiecriteria** {verwacht}, en {eis}",
            "",
            laag,
            "",
        ]
        return blok

    def beeld(self, alt: str, pad: str) -> None:
        """Zet het beeld in het document, niet een beschrijving ervan."""
        bron = WORTEL / self.bronmap() / pad
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

    def maak(self) -> str:
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
        return doel


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
