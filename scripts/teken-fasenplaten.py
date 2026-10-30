#!/usr/bin/env python3
"""De hoofdplaat per fase van de voorbeelduitwerking, getekend uit het model.

Waarom dit script bestaat: een stroombeeld toont twee componenten en wat er tussen hen
beweegt, maar niet waar die lijn op de hoofdplaat loopt. Daarvoor stond onder elke fasekop
een markeringslaag over een rasterrender van de plaat (`teken-hoofdplaat-highlight.py`). Die
render en het kader eromheen lopen uiteen zodra de view wijzigt: verdwijnt er een notitie, dan
krimpt het kader en landt elke markering naast haar pijl, zonder dat iets dat meldt. Dit script
tekent de plaat daarom zelf uit het model, met dezelfde markeerstand die de
interactieketenspecificaties gebruiken. Relateert aan: #407.

    python3 scripts/teken-fasenplaten.py [--regels PAD] [--uit MAP] [--fasen 2,3]

Per fase komt er `f<N>.svg` met de stromen van die fase in de accentkleur, de overige lijnen
vervaagd, een omlijning om de componenten die meedoen, en een gestippelde lijn voor een stroom
die de plaat nog niet kent. Daarnaast schrijft het `hoofdplaat.svg`: dezelfde plaat zonder
markering, als kaart boven het document.

Het model wordt alleen gelezen; raak nooit een .archimate-bestand aan.
"""

import argparse
import importlib.util
import json
import pathlib
import sys

WORTEL = pathlib.Path(__file__).resolve().parent


def _laad(naam, bestand):
    spec = importlib.util.spec_from_file_location(naam, WORTEL / bestand)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hoog = _laad("hoofdplaat_highlight", "teken-hoofdplaat-highlight.py")
ruim = _laad("hoofdplaat_ruim", "teken-hoofdplaat-ruim.py")

REGELS = pathlib.Path("architecture/model/informatiemodel/modeldoorloop-lr1.json")
UITMAP = pathlib.Path("architecture/model/informatiemodel/img/hoofdplaat")
OVERZICHT = "hoofdplaat.svg"


def fasenamen(regels):
    """De naam per fasenummer uit de kop van de regeltabel."""
    return {f["nummer"]: f.get("naam", "") for f in regels.get("fasen", [])}


def markeringen_van(stromen, gedeeld=()):
    """De stromen van een fase in de vorm die de markeerstand van de plaat leest.

    Het label draagt de beeld-ID's die de stroom gebruiken, zodat een lezer van de plaat
    terugvindt bij welk beeld in het document de lijn hoort. Een stroom zonder pijl op de
    hoofdplaat draagt geen stroom-ID en komt daarmee gestippeld op de plaat.
    """
    uit = []
    for (van, naar, pijl), beelden in stromen.items():
        op_de_plaat = pijl != hoog.GEEN_PIJL
        stroom = pijl if op_de_plaat and pijl not in gedeeld else ""
        uit.append({"van": van, "naar": naar, "label": ", ".join(beelden),
                    "op_de_plaat": op_de_plaat, "stroom": stroom})
    return uit


def _teken(markeringen, naam):
    svg, _, _, _, _, ontbreekt, gemarkeerd = ruim.bouw(
        markeer=[{**m, "ontvangergroep": ""} for m in markeringen], markeer_naam=naam)
    return svg, ontbreekt, gemarkeerd


def teken(markeringen, naam):
    """De plaat met deze markeringen, als SVG met de meldingen erbij.

    Twee ronden, want een stroom-ID wijst niet altijd een lijn aan. Loopt een stroom over een
    junctie naar meer ontvangers, dan draagt de export datzelfde ID per ontvanger een keer, en
    dan vindt het ID de verkeerde ontvanger. Meldt de eerste ronde zo'n stroom, dan gaat haar ID
    eraf en telt het componentenpaar; dat vindt de lijn die wel door de junctie loopt.
    """
    svg, ontbreekt, gemarkeerd = _teken(markeringen, naam)
    gemist = {m.get("label") for m in markeringen
              if any(str(x).startswith(f"{m.get('label')}:") for x in ontbreekt)}
    if not gemist or not any(m.get("stroom") for m in markeringen if m.get("label") in gemist):
        return svg, ontbreekt, gemarkeerd
    opnieuw = [{**m, "stroom": ""} if m.get("label") in gemist else m for m in markeringen]
    return _teken(opnieuw, naam)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--regels", type=pathlib.Path, default=REGELS)
    p.add_argument("--uit", type=pathlib.Path, default=UITMAP)
    p.add_argument("--fasen", help="komma-gescheiden fasenummers; standaard alle fasen")
    p.add_argument("--zonder-overzicht", action="store_true",
                   help="schrijf alleen de fasenplaten en niet de kaart zonder markering")
    args = p.parse_args(argv)

    regels = json.loads(args.regels.read_text(encoding="utf-8"))
    namen = fasenamen(regels)
    gevraagd = {int(n) for n in args.fasen.split(",")} if args.fasen else None
    args.uit.mkdir(parents=True, exist_ok=True)

    aantal, gestippeld = 0, 0
    for fase, stromen in hoog.stromen_per_fase(regels).items():
        if gevraagd and fase not in gevraagd:
            continue
        naam = f"Fase {fase}: {namen.get(fase, '')}".rstrip(": ")
        svg, ontbreekt, gemarkeerd = teken(markeringen_van(stromen), naam)
        (args.uit / f"f{fase}.svg").write_text(svg, encoding="utf-8")
        aantal += 1
        gestippeld += gemarkeerd["gestippeld"]
        for x in ontbreekt:
            print(f"waarschuwing: fase {fase}: {x}", file=sys.stderr)
    print(f"{aantal} fasenplaten geschreven naar {args.uit}, "
          f"waarvan {gestippeld} stromen gestippeld omdat de plaat ze niet kent")

    if not args.zonder_overzicht:
        svg, _, _, _, _, _, _ = ruim.bouw()
        (args.uit / OVERZICHT).write_text(svg, encoding="utf-8")
        print(f"kaart zonder markering geschreven naar {args.uit / OVERZICHT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
