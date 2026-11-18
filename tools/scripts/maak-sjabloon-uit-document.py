#!/usr/bin/env python3
"""Leidt een invulsjabloon af uit een uitgewerkt OKx-document.

Het sjabloon is niet met de hand geschreven: het wordt uit de uitwerking
gegenereerd die er al ligt. Zo draagt het elke kop en elke tabel van het
origineel, en loopt het niet achter wanneer de uitwerking wijzigt.

Wat er per onderdeel gebeurt:

- een kop blijft staan, met de bronspecifieke termen vervangen;
- een alinea zonder bronspecifieke term blijft staan, want die geldt voor elke
  uitwerking; een alinea met zo'n term wordt een verwijzing naar wat de bron
  daar zegt, met schrijfruimte eronder;
- een tabel houdt haar kopregel; haar rijen blijven staan wanneer zij algemeen
  zijn en worden leeg wanneer zij bronspecifiek zijn, evenveel rijen als de
  bron had, zodat zichtbaar is hoeveel er wordt verwacht;
- een beeld en een diagram worden een regel die zegt dat daar een beeld hoort.

    python3 tools/scripts/maak-sjabloon-uit-document.py            # alle vijf
    python3 tools/scripts/maak-sjabloon-uit-document.py --sjabloon persona

Relateert aan: #554
"""

import argparse
import json
import pathlib
import re
import subprocess
import sys

WORTEL = pathlib.Path(__file__).resolve().parents[2]
MAP = WORTEL / "architecture/docs/sjablonen"
CONFIG = MAP / "bron/sjablonen.json"
UIT = MAP / "gegenereerd"

KOP = re.compile(r"^(#{1,6}) +(.*)$")
TABELRIJ = re.compile(r"^\|.*\|\s*$")
SCHEIDING = re.compile(r"^\|[\s:|-]+\|\s*$")
BEELD = re.compile(r"^!\[([^\]]*)\]\(([^)]*)\)\s*$")
FENCE = re.compile(r"^```(\w*)\s*$")

RUIMTE = "*Schrijf hier de uitwerking.*"
BLOB = "https://github.com/Npuls-OKx/meta/blob"
LINK = re.compile(r"\]\(([^)]+)\)")


DOEL = re.compile(r"\]\([^)]*\)")


def zonder_linkdoelen(tekst: str) -> str:
    """De tekst zonder de bestemming van een link.

    Een link naar persona_larissa.md draagt een naam die ook in de
    vervangingen staat; zonder deze stap telt een verwijzing als inhoud en
    wordt een algemene alinea ten onrechte leeggemaakt.
    """
    return DOEL.sub("]()", tekst)


def vervang(tekst: str, paren: list[list[str]]) -> str:
    """Vervangt bronspecifieke termen, met de hoofdletter van het origineel.

    De bron schrijft "Leerroute 1" in een kop en "leerroute 1" in een zin; een
    vervanging die dat negeert zet midden in een kop een kleine letter.
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


def bronspecifiek(tekst: str, paren: list[list[str]]) -> bool:
    """Noemt dit stuk een term die bij deze ene uitwerking hoort."""
    tekst = zonder_linkdoelen(tekst)
    return any(re.search(re.escape(oud), tekst, re.I) for oud, _ in paren)


def eerste_zin(blok: list[str]) -> str:
    """De eerste zin van een blok, zonder opmaak.

    De bron opent een blok ook wel met een opsommingsteken, een citaat of een
    vette aanhef; die tekens zeggen de invuller niets en gaan eraf.
    """
    schoon = []
    for r in blok:
        r = re.sub(r"^\s*[>*+-]+\s*", "", r)
        schoon.append(r)
    tekst = " ".join(r.strip() for r in schoon if r.strip())
    tekst = re.sub(r"\*\*([^*]*)\*\*", r"\1", tekst)
    tekst = re.sub(r"\*([^*]*)\*", r"\1", tekst)
    tekst = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", tekst)
    tekst = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", tekst)
    tekst = re.sub(r"\s+", " ", tekst).strip()
    zinnen = re.findall(r".+?(?:[.;:]|$)(?:\s|$)", tekst)
    uit = ""
    for zin in zinnen:
        uit = (uit + " " + zin).strip()
        if len(uit) >= 60:
            break
    uit = uit.strip()
    if len(uit) > 320:
        uit = uit[:320].rsplit(" ", 1)[0].rstrip(" ,;:") + " ..."
    return uit


class Sjabloon:
    def __init__(self, naam: str, cfg: dict):
        self.naam = naam
        self.cfg = cfg
        self.paren = [list(p) for p in cfg.get("vervang", [])]
        self.koppen_paren = self.paren + [list(x) for x in cfg.get("kop_vervang", [])]
        # Alles vanaf deze kop is de uitwerking zelf en wordt schrijfruimte, ook
        # waar de tekst geen bronspecifieke term noemt. Wat ervoor staat is het
        # kader dat voor elke uitwerking hetzelfde is en blijft dus staan.
        self.vanaf = cfg.get("invullen_vanaf")
        self.verwijzing = cfg.get("verwijzing", "In de voorbeelduitwerking staat hier")
        self.in_uitwerking = self.vanaf is None
        self.bronnaam = cfg["bron"]
        self.uit: list[str] = []
        # Een schrijfruimte per hoofdstuk, niet na elke alinea: een invuller
        # schrijft zijn uitwerking in een stuk en niet in losse snippers.
        self.ruimte_open = False
        self.verwezen = False

    # -- de vaste kop die elk sjabloon draagt ---------------------------------

    def aanhef(self) -> list[str]:
        c = self.cfg
        return [
            f"# {c['titel']}",
            "",
            "## Invullen",
            "",
            "| Onderdeel | Inhoud |",
            "|---|------------------------------------------------|",
            f"| Wat dit wordt | {c['wat']} |",
            f"| Wie dit invult | {c['wie']} |",
            f"| Voorbeelduitwerking | {c['voorbeeld']} |",
            "| Inleveren | terug naar OKx SI als Word-bestand |",
            "",
            "## Vaste koppen",
            "",
            "De koppen in dit document blijven staan zoals zij hier staan. In het "
            "agent-harnas komt een lezer (parser) die een ingevuld document per kop "
            "terugvertaalt naar de kennisbank; een kop die is herschreven of "
            "weggehaald maakt zijn hoofdstuk onleesbaar. Een hoofdstuk dat niet van "
            "toepassing is houdt dus zijn kop, met de reden eronder.",
            "",
            "Dit sjabloon is afgeleid uit "
            f"{c['voorbeeld']}, dus het draagt elke kop en elke tabel van die "
            "uitwerking. Wat daar algemeen was staat er nog. Wat daar aan die ene "
            "uitwerking hing, staat er als ingesprongen citaat, met "
            f"*{RUIMTE.strip('*')}* eronder: daar hoort de eigen uitwerking. Een "
            "lege tabel heeft evenveel rijen als de uitwerking had, zodat "
            "zichtbaar is hoeveel er wordt verwacht.",
            "",
            "## De grootst gemene deler",
            "",
            c["aggregatie"],
            "",
            "Een instelling spreekt voor haar eigen praktijk en niet voor de sector. "
            "Noteer daarom apart wat afwijkt, onder "
            "[Afwijkingen per instelling](#afwijkingen-per-instelling).",
            "",
        ]

    def slot(self) -> list[str]:
        return [
            "## Afwijkingen per instelling",
            "",
            "Wat bij een instelling anders gaat dan hierboven staat, per regel met "
            "de instelling erbij. Dit is geen restcategorie: hier staat het "
            "materiaal waaruit blijkt of de grootst gemene deler houdbaar is.",
            "",
            "| Instelling | Hoofdstuk | Wat daar anders gaat |",
            "|---|---|------------------------------------|",
            "| | | |",
            "| | | |",
            "| | | |",
            "",
            "## Vragen aan OKx",
            "",
            "Wat onduidelijk bleef, genummerd, met per vraag het hoofdstuk waar het "
            "speelt.",
            "",
            "| Nummer | Hoofdstuk | Vraag |",
            "|---|---|------------------------------------|",
            "| 1 | | |",
            "| 2 | | |",
            "| 3 | | |",
            "",
        ]

    # -- de onderdelen van de bron -------------------------------------------

    def alinea(self, blok: list[str]) -> None:
        tekst = "\n".join(blok).strip()
        if not tekst:
            return
        if not self.in_uitwerking and not bronspecifiek(tekst, self.paren):
            # Algemeen, dus het geldt ook voor de volgende uitwerking.
            self.uit += [vervang(r, self.paren) for r in blok] + [""]
            return
        zin = eerste_zin(blok)
        if zin:
            # De verwijzing staat eenmaal per hoofdstuk; daarna spreekt het
            # citaatblok voor zichzelf.
            aanhef = f"{self.verwijzing}: " if not self.verwezen else ""
            self.uit += [f"> {aanhef}{zin}", ""]
            self.verwezen = True
        self.ruimte_open = True

    def tabel(self, blok: list[str]) -> None:
        kop = blok[0]
        scheiding = blok[1] if len(blok) > 1 and SCHEIDING.match(blok[1]) else None
        rijen = blok[2:] if scheiding else blok[1:]
        self.uit.append(vervang(kop, self.paren))
        self.uit.append(scheiding or "|" + "---|" * (kop.count("|") - 1))
        if (rijen and not self.in_uitwerking
                and not bronspecifiek("\n".join(rijen), self.paren)):
            self.uit += [vervang(r, self.paren) for r in rijen]
        else:
            kolommen = kop.count("|") - 1
            for _ in range(max(1, min(len(rijen), 15))):
                self.uit.append("|" + " |" * kolommen)
        self.uit.append("")

    def sluit_ruimte(self) -> None:
        if self.ruimte_open:
            self.uit += [RUIMTE, ""]
            self.ruimte_open = False
        self.verwezen = False

    def beeld(self, alt: str) -> None:
        alt = vervang(alt, self.paren) or "een beeld"
        self.uit += [f"*Beeld: {alt}. Voeg hier het beeld in.*", ""]
        if self.in_uitwerking:
            self.ruimte_open = True

    def blok(self, taal: str, inhoud: list[str]) -> None:
        if taal == "mermaid":
            eerste = next((r.strip() for r in inhoud if r.strip()), "een diagram")
            self.uit += [f"*Diagram: de bron tekent hier een {eerste.split()[0]}. "
                         "Voeg hier het diagram in.*", ""]
            if self.in_uitwerking:
                self.ruimte_open = True
            return
        tekst = "\n".join(inhoud)
        if self.in_uitwerking or bronspecifiek(tekst, self.paren):
            self.uit += ["*Voorbeeld: de bron toont hier een fragment. Voeg hier "
                         "het eigen fragment in.*", ""]
            return
        self.uit += [f"```{taal}"] + inhoud + ["```", ""]

    # -- de doorloop ----------------------------------------------------------

    def absoluut(self, tekst: str) -> str:
        """Maakt elke verwijzing volledig.

        Een Word-bestand staat niet in de repository, dus een pad als
        persona_jochem.md wijst daar nergens heen. Een anker naar een kop in
        hetzelfde document blijft staan.
        """
        ref = self.cfg.get("bron_ref", "dev")
        basis = pathlib.PurePosixPath(self.bronnaam).parent

        def een(m: re.Match) -> str:
            doel = m.group(1).strip()
            if doel.startswith(("http://", "https://", "#", "mailto:")):
                return m.group(0)
            pad, _, anker = doel.partition("#")
            if not pad:
                return m.group(0)
            heel = str((basis / pad)).replace("\\", "/")
            while "/../" in heel:
                heel = re.sub(r"[^/]+/\.\./", "", heel, count=1)
            staart = f"#{anker}" if anker else ""
            return f"]({BLOB}/{ref}/{heel}{staart})"

        return LINK.sub(een, tekst)

    def brontekst(self) -> str:
        """De bron uit de werkmap, of uit een git-verwijzing wanneer de
        uitwerking nog op een andere tak staat."""
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

    def maak(self) -> str:
        regels = self.brontekst().splitlines()
        self.uit = self.aanhef()
        buffer: list[str] = []
        soort = None
        i = 0
        eerste_kop_gezien = False

        def leeg() -> None:
            nonlocal buffer, soort
            if buffer:
                (self.tabel if soort == "tabel" else self.alinea)(buffer)
            buffer, soort = [], None

        while i < len(regels):
            regel = regels[i]
            m = KOP.match(regel)
            if m:
                leeg()
                niveau = len(m.group(1))
                tekst = vervang(m.group(2), self.koppen_paren)
                if not eerste_kop_gezien and niveau == 1:
                    eerste_kop_gezien = True  # de eigen titel staat al in de aanhef
                    i += 1
                    continue
                self.sluit_ruimte()
                if self.vanaf and self.vanaf.lower() in tekst.lower():
                    self.in_uitwerking = True
                self.uit += ["#" * max(2, niveau) + " " + tekst, ""]
                i += 1
                continue
            f = FENCE.match(regel)
            if f:
                leeg()
                taal, inhoud = f.group(1), []
                i += 1
                while i < len(regels) and not regels[i].startswith("```"):
                    inhoud.append(regels[i])
                    i += 1
                self.blok(taal, inhoud)
                i += 1
                continue
            b = BEELD.match(regel)
            if b:
                leeg()
                self.beeld(b.group(1))
                i += 1
                continue
            if TABELRIJ.match(regel):
                if soort != "tabel":
                    leeg()
                    soort = "tabel"
                buffer.append(regel)
                i += 1
                continue
            if not regel.strip():
                leeg()
                i += 1
                continue
            if soort == "tabel":
                leeg()
            soort = "alinea"
            buffer.append(regel)
            i += 1
        leeg()
        self.sluit_ruimte()
        self.uit += self.slot()

        tekst = "\n".join(self.uit)
        tekst = self.absoluut(tekst)
        tekst = re.sub(r"\n{3,}", "\n\n", tekst).strip() + "\n"
        return tekst


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
        tekst = Sjabloon(naam, config[naam]).maak()
        doel = a.uit / f"{naam}.md"
        doel.write_text(tekst, encoding="utf-8")
        print(f"  {doel.relative_to(WORTEL)}  "
              f"({len(tekst.splitlines())} regels, "
              f"{len([r for r in tekst.splitlines() if r.startswith('#')])} koppen)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
