#!/usr/bin/env python3
"""De indeling van een JSON-bericht tekenen zoals een JSON-viewer hem toont.

Waarom dit script bestaat: OKx krijgt berichten van instellingen en leveranciers om naast de
eigen beschrijving te leggen. Zo'n bericht in een ```json-blok onder een issue zetten werkt
niet: het SBIS-bestand van een enkele opleiding telt ruim veertienhonderd regels, en wie het
opent ziet de structuur juist niet. Een mermaid-boom ernaast is een tweede waarheid die bij de
eerste wijziging uiteenloopt.

Dit script leest het bericht zelf en tekent zijn indeling: per sleutel wat het is, hoeveel het
er zijn, en bij een lijst van objecten welke sleutels zo'n object draagt. De vorm is die van een
JSON-viewer, omdat iedereen die kent.

    python3 tools/scripts/teken-json-structuur.py --bron <pad>.json --uit <pad>.svg \
      --titel "..." --herkomst "..." --versie 0.1.0 [--diepte 3] [--merk a,b]

Standaard komen alleen sleutels, soorten en aantallen op de plaat, en geen waarden. Een bericht
van een instelling draagt haar eigen inhoud; die hoort niet ongevraagd in een publiek
repository. `--waarden` zet de waarden er alsnog bij, en `--waarden-tot` beperkt dat tot de
bovenste niveaus. Een sleutel die in `--merk` staat krijgt de accentkleur, zodat de plaat zegt
waar het gesprek over gaat in plaats van alles even hard te tonen.
"""

import argparse
import html
import importlib.util
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("teken_modeldoorloop", WORTEL / "teken-modeldoorloop.py")
vt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vt)

INK, MUTED, LIJN, FONT = vt.INK, vt.MUTED, vt.LIJN, vt.FONT
ACCENT = "#d9531e"            # dezelfde accentkleur als de andere OKx-platen
MONO = "'DejaVu Sans Mono', 'Liberation Mono', Consolas, monospace"
SLEUTEL, SOORT, GETAL, TEKST = "#1c4f6b", "#5b6663", "#7a4f9b", "#2a6b3a"
ZEBRA = "#f7f8f8"

REGEL = 19                    # hoogte van een regel
INSPRONG = 20                 # inspringing per niveau
MARGE = 18
KOP, HERKOMST_MAAT, MAAT, VORM_MAAT = 17, 12, 13, 11
MONO_BREED = 0.602            # tekenbreedte van de monospace-letter, als deel van de puntmaat
MAX_REGELS = 60               # daarboven is het geen beeld meer maar een bestand
MAX_VORMSLEUTELS = 9          # de sleutels van een object in een lijst, als vorm eronder


def breedte(s, maat=MAAT):
    """Breedte van een regel monospace-tekst in px. Elke letter is even breed; dat is het hele
    punt van een monospace-letter, en het maakt de kolombreedte exact in plaats van geschat."""
    return int(len(s) * maat * MONO_BREED) + 1


def soortnaam(waarde):
    if isinstance(waarde, dict):
        n = len(waarde)
        return f"{{ {n} sleutel{'s' if n != 1 else ''} }}"
    if isinstance(waarde, list):
        if not waarde:
            return "[ leeg ]"
        soorten = sorted({type(x).__name__ for x in waarde})
        wat = "object" if soorten == ["dict"] else "lijst" if soorten == ["list"] else "waarde"
        return f"[ {len(waarde)} x {wat} ]"
    if waarde is None:
        return "leeg"
    return {bool: "ja of nee", int: "getal", float: "getal", str: "tekst"}[type(waarde)]


def waardetekst(waarde, breed=46):
    if isinstance(waarde, str):
        kort = waarde if len(waarde) <= breed else waarde[:breed - 1] + "…"
        return f'"{kort}"'
    if waarde is None:
        return "null"
    if isinstance(waarde, bool):
        return "true" if waarde else "false"
    return str(waarde)


def sleutelvorm(knoop):
    """De sleutels die een knoop draagt, als een regel: de vorm achter een dichtgeklapt vak.

    Bij een lijst zijn dat de sleutels van het eerste object erin, want daar hebben alle
    elementen dezelfde vorm. Zonder deze regel zegt een dichtgeklapte tak alleen hoeveel het
    er zijn, en dat is precies niet wat iemand wil weten die de indeling bekijkt.
    """
    if isinstance(knoop, list):
        knoop = next((x for x in knoop if isinstance(x, dict)), None)
    if not isinstance(knoop, dict) or not knoop:
        return None
    sleutels = list(knoop)
    if len(sleutels) > MAX_VORMSLEUTELS:
        sleutels = sleutels[:MAX_VORMSLEUTELS] + [f"en nog {len(knoop) - MAX_VORMSLEUTELS}"]
    return ", ".join(sleutels)


def regels_van(knoop, diepte, waarden_tot, merk, niveau=0, sleutel=None):
    """De plaat als lijst regels: (niveau, sleutel, soort, waarde, vorm, gemerkt)."""
    uit = []
    gemerkt = sleutel in merk
    if sleutel is not None:
        waarde = (waardetekst(knoop) if not isinstance(knoop, (dict, list))
                  and niveau <= waarden_tot else None)
        vorm = sleutelvorm(knoop) if niveau >= diepte else None
        uit.append((niveau, sleutel, soortnaam(knoop), waarde, vorm, gemerkt))
    if niveau >= diepte:
        return uit
    if isinstance(knoop, dict):
        for k, v in knoop.items():
            uit += regels_van(v, diepte, waarden_tot, merk, niveau + 1, k)
    elif isinstance(knoop, list) and knoop:
        eerste = next((x for x in knoop if isinstance(x, dict)), None)
        if eerste is not None:
            uit += regels_van(eerste, diepte, waarden_tot, merk, niveau + 1, "elk element")
    return uit


def teken(regels, titel, herkomst, versie, bron):
    if len(regels) > MAX_REGELS:
        sys.exit(f"de plaat telt {len(regels)} regels (hoogstens {MAX_REGELS}). Verlaag --diepte "
                 f"of kies een deel van het bericht; daarboven is het geen beeld meer")
    # De kolommen schuiven mee met wat er in staat: de sleutelkolom zo breed als de diepste
    # sleutel, de soortkolom zo breed als het langste soortwoord. Een vaste kolom laat een
    # lange sleutel in de kolom ernaast lopen, en dat is precies wat een viewer nooit doet.
    sleutel_eind = max(MARGE + 10 + (n - 1) * INSPRONG + breedte(str(s)) for n, s, *_ in regels)
    kolom = sleutel_eind + 26
    soort_eind = kolom + max(breedte(so) for _, _, so, *_ in regels)
    derde = soort_eind + 26
    staart = max((breedte(w) if w else breedte(v, VORM_MAAT) if v else 0
                  for *_, w, v, _ in regels), default=0)
    breed = max(derde + staart + MARGE, MARGE * 2 + int(len(titel) * KOP * 0.56),
                MARGE * 2 + int(len(herkomst) * HERKOMST_MAAT * 0.52))
    boven = MARGE + KOP + (HERKOMST_MAAT + 8 if herkomst else 0) + 14
    hoog = boven + len(regels) * REGEL + MARGE + 22

    delen = [f'<rect x="0.5" y="0.5" width="{breed - 1}" height="{hoog - 1}" rx="10" '
             f'fill="#ffffff" stroke="{LIJN}"/>',
             vt.text(MARGE, MARGE + KOP - 2, titel, KOP, bold=True)]
    if herkomst:
        delen.append(vt.text(MARGE, MARGE + KOP + HERKOMST_MAAT + 2, herkomst, HERKOMST_MAAT,
                             fill=MUTED))
    if versie:
        delen.append(vt.text(breed - MARGE, MARGE + KOP - 2, f"v{versie}", HERKOMST_MAAT,
                             fill=MUTED, anchor="end"))

    rijen, geleiders = [], []
    for i, (niveau, sleutel, soort, waarde, vorm, gemerkt) in enumerate(regels):
        y = boven + i * REGEL
        if i % 2:
            rijen.append(f'<rect x="{MARGE}" y="{y:.0f}" width="{breed - 2 * MARGE}" '
                         f'height="{REGEL}" fill="{ZEBRA}"/>')
        if gemerkt:
            rijen.append(f'<rect x="{MARGE}" y="{y:.0f}" width="{breed - 2 * MARGE}" '
                         f'height="{REGEL}" fill="#ffffff" stroke="{ACCENT}" stroke-width="1.4"/>')
        x = MARGE + 10 + (niveau - 1) * INSPRONG
        for n in range(1, niveau):
            gx = MARGE + 10 + (n - 1) * INSPRONG + 3
            geleiders.append(f'<path d="M{gx} {y:.0f}V{y + REGEL:.0f}" stroke="{LIJN}"/>')
        basis = y + REGEL - 5
        kleur = ACCENT if gemerkt else SLEUTEL
        rijen.append(f'<text x="{x:.0f}" y="{basis:.0f}" font-family="{MONO}" font-size="{MAAT}" '
                     f'font-weight="bold" fill="{kleur}">{html.escape(str(sleutel))}</text>')
        soortkleur = ACCENT if gemerkt else SOORT
        rijen.append(f'<text x="{kolom}" y="{basis:.0f}" font-family="{MONO}" '
                     f'font-size="{MAAT}" fill="{soortkleur}">{html.escape(soort)}</text>')
        if waarde is not None:
            wk = TEKST if waarde.startswith('"') else MUTED if waarde == "null" else GETAL
            rijen.append(f'<text x="{derde}" y="{basis:.0f}" font-family="{MONO}" '
                         f'font-size="{MAAT}" fill="{wk}">{html.escape(waarde)}</text>')
        elif vorm:
            rijen.append(f'<text x="{derde}" y="{basis:.0f}" font-family="{MONO}" '
                         f'font-size="{VORM_MAAT}" fill="{MUTED}">{html.escape(vorm)}</text>')

    delen += geleiders + rijen
    delen.append(vt.text(MARGE, hoog - MARGE + 6,
                         f"indeling van {bron}; sleutels, soorten en aantallen, geen inhoud",
                         HERKOMST_MAAT, fill=MUTED))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breed} {hoog}" '
            f'width="{breed}" height="{hoog}">' + "".join(delen) + "</svg>")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--bron", required=True)
    p.add_argument("--uit", required=True)
    p.add_argument("--titel", default="Indeling van het bericht")
    p.add_argument("--herkomst", default="")
    p.add_argument("--versie", default="")
    p.add_argument("--diepte", type=int, default=3)
    p.add_argument("--waarden", action="store_true", help="waarden van losse velden erbij")
    p.add_argument("--waarden-tot", type=int, default=2,
                   help="tot welk niveau waarden meegaan, met --waarden")
    p.add_argument("--merk", default="", help="komma-gescheiden sleutels in de accentkleur")
    a = p.parse_args()

    bron = pathlib.Path(a.bron)
    data = json.loads(bron.read_text(encoding="utf-8"))
    merk = {s.strip() for s in a.merk.split(",") if s.strip()}
    regels = regels_van(data, a.diepte, a.waarden_tot if a.waarden else -1, merk)
    if not regels:
        sys.exit(f"{bron}: het bericht draagt geen sleutels om te tekenen")
    onbekend = merk - {s for _, s, *_ in regels}
    if onbekend:
        sys.exit(f"deze sleutels staan niet op de plaat: {', '.join(sorted(onbekend))}. "
                 f"Verhoog --diepte of corrigeer de naam")
    svg = teken(regels, a.titel, a.herkomst, a.versie, bron.name)
    pathlib.Path(a.uit).write_text(svg, encoding="utf-8")
    print(f"{a.uit}: {len(regels)} regels, diepte {a.diepte}, {len(merk)} gemerkt")


if __name__ == "__main__":
    main()
