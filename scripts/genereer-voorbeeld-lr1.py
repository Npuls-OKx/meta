#!/usr/bin/env python3
"""Het document van de voorbeelduitwerking bouwen uit de regeltabel.

Waarom dit script bestaat: het document dat de opleiding van Jochem stap voor stap
in het informatiemodel toont moet bij elke modelronde opnieuw te maken zijn, met zo
weinig mogelijk tekst. Alles komt uit de regeltabel, informatiemodel.json en
begrippen.json; de regels zelf zijn de SVG's van teken-voorbeeldregels.py.

    python3 scripts/genereer-voorbeeld-lr1.py [--regels PAD] [--uit PAD]

Opbouw: leeswijzer (vier termen, legenda, koppeling-ID's, aannames), per fase de
chips en de regels, een stub voor fasen zonder regels, een tabel per begrippenfamilie
met twee lege kolommen voor de lezer, en de vragenpagina.
"""

import argparse
import collections
import importlib.util
import json
import pathlib
import re
import sys

_spec = importlib.util.spec_from_file_location("teken_voorbeeldregels", pathlib.Path(__file__).resolve().parent / "teken-voorbeeldregels.py")
teken = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(teken)

REGELS = pathlib.Path("architecture/model/informatiemodel/voorbeeld-lr1-regels.json")
MODEL = pathlib.Path("architecture/model/informatiemodel/informatiemodel.json")
BEGRIPPEN = pathlib.Path("architecture/docs/specificatie/begrippen/begrippen.json")
UIT = pathlib.Path("architecture/model/informatiemodel/voorbeeld-leerroute-1-jochem.md")
REGELMAP = "img/regels"
KOLOMVOLGORDE = ["Kwalificatiekader MBO", "Onderwijskundigkader instelling", "Onderwijsspecificatie", "Onderwijsaanbod",
                 "Onderwijsverbintenis", "Onderwijsresultaat", "Resultaatstructuur", None]
KOLOMNAAM = {None: "Buiten de kolommen (persoon, groep, cohort, verzoek)", "Kwalificatiekader MBO": "Kwalificatiekader mbo",
             "Onderwijskundigkader instelling": "Onderwijskundig kader instelling"}
STUBZIN = "Regels volgen na 30 september."


def norm(s):
    return " ".join(str(s).split())


def lees(pad, wat):
    try:
        return json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"{wat} niet gevonden: {pad}")


def blokken_per_fase(regels):
    """De groepering en bestandsnamen van de renderer, zodat verwijzingen en bestanden gelijk lopen."""
    uit = collections.defaultdict(list)
    for n, blok in enumerate(teken.groepeer(regels), 1):
        uit[blok["fase"]].append({"naam": teken.bestandsnaam(blok, n), "stap": blok["stap"], "soort": blok["soort"]})
    return uit


def leeswijzer(regels, model):
    k = regels["koppelingen"]
    mapping = "; ".join(f"{v} is {kk.replace(' > ', ' naar ')}" for kk, v in k.items())
    return f"""# De opleiding van Jochem in het informatiemodel

Relateert aan: het kaderscenario leerroute 1 (persona Jochem, Apothekersassistent, cohort 2026) en het [informatiemodel OKx](informatiemodel.md). Gegenereerd uit `voorbeeld-lr1-regels.json`; gecontroleerd tegen `informatiemodel.json` op commit {regels['model']['informatiemodel_commit']} en `begrippen.json` op commit {regels['model']['begrippen_commit']}.

## Leeswijzer

Dit document loopt stap voor stap door de instellingsreis van het kaderscenario en toont per stap wat er in het informatiemodel ontstaat en wat er tussen systemen beweegt, met de waarde voor Jochem erin. Het is een leeshulp op conceptueel niveau (MIM 1 en 2): geen payloads, geen endpoints, geen diensten. Eén instantie per objecttype toont het type, niet het aantal.

Vier termen, overal gelijk:

| Term | Betekenis |
|---|---|
| Objecttype | Element van de informatiemodelplaat (ArchiMate business object), met de plaatnaam letterlijk |
| Instantie | De waarde voor Jochem: een leesbare naam |
| Applicatiedienst | De ArchiMate-applicatiedienst op de hoofdplaat en in MORA; alleen context |
| Koppeling | Een pijl op hoofdplaat v1.7 tussen twee componenten; met de koppeling-ID uit Public waar die er is |

Twee soorten regels, in de vormtaal van de plaat:

- **Ontstaat**: een rol (geel, rolicoon) voert een processtap uit (geel, procesicoon) en daaruit ontstaan objecttypen (geel, objecticoon) met Jochems waarde. "Bestaat uit" is nesting; een relatielabel van de plaat staat tussen twee objecten of als verwijzing op een object dat aan een eerdere stap hangt. Een gestippelde rand is een aanname; grijs is een objecttype dat de plaat buiten de uitwisseling zet en dit voorbeeld toch meeneemt.
- **Stroomt** (blauwe rand): van welk systeem naar welk systeem gaat welk object, met de koppeling-ID of "zonder koppelingspecificatie", en de processtap waarna het gebeurt.

Koppeling-ID's op hoofdplaat v1.7: {mapping}. Een pijl die op de hoofdplaat staat maar geen koppelingspecificatie heeft, staat als "zonder koppelingspecificatie"; een stroom uit het kaderscenario zonder pijl op de hoofdplaat staat als "geen pijl op de hoofdplaat".

De fasenamen zijn de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario. Het kaderscenario noemt fase 3 in de fasenlijst "Instroom, afstemming en plaatsing" en in de sectiekop "Instroom, intake en plaatsing"; hier geldt de sectiekop.

Wat hier staat is feedback, geen commitment: het voorbeeld beslist niets over het model. Per objecttype staan in de bijlage twee lege kolommen, "heet bij u" en "hangt bij u onder", voor wie het naast het eigen model legt.
"""


def fase_sectie(f, blokken, regels_in_fase):
    kop = f"## Fase {f['nummer']}: {f['naam']}\n\n"
    mora = f.get("mora_hoofdproces")
    chips_obj = [norm(r["objecttype"]) for r in regels_in_fase if r["soort"] in ("ontstaat", "verandert")]
    chips_obj = list(dict.fromkeys(chips_obj))
    chips_str = list(dict.fromkeys(f"{r['van']} naar {r['naar']}" for r in regels_in_fase if r["soort"] == "stroomt"))
    if not regels_in_fase:
        chips_obj = [norm(v) for v in f["verwacht"]]
    regel = "**Ontstaat:** " + (", ".join(f"`{c}`" for c in chips_obj) or "geen nieuwe objecttypen; deze fase raakt bestaande objecttypen")
    if chips_str:
        regel += ". **Stroomt:** " + "; ".join(chips_str)
    if mora:
        regel += f". **MORA-hoofdproces:** {mora}"
    uit = kop + regel + ".\n\n"
    if not regels_in_fase:
        return uit + STUBZIN + "\n\n"
    for b in blokken:
        uit += f"![{b['soort']}: {b['stap']}]({REGELMAP}/{b['naam']})\n\n"
    return uit


def familietabellen(regels, model, begrippen):
    typen = {norm(o["naam"]): o for o in model["objecttypen"]}
    uitz = {norm(u["objecttype"]) for u in regels["scope_uitzonderingen"]}
    oeapi = collections.defaultdict(list)
    for m in model.get("oeapi_mapping", []):
        oeapi[norm(m["okx"])].append(m["oeapi"])
    definitie = {}
    for b in begrippen.get("begrippen", []):
        for naam in [b["naam"]] + b.get("varianten", []):
            definitie[norm(naam)] = b.get("status", "")
    eerste = {}
    for r in regels["regels"]:
        n = norm(r["objecttype"])
        if r["soort"] in ("ontstaat", "verandert") and n not in eerste:
            eerste[n] = r
    verwachting = {norm(v): f["nummer"] for f in regels["fasen"] for v in f["verwacht"]}
    uit = "## Bijlage: alle objecttypen per begrippenfamilie\n\nPer objecttype de instantie voor Jochem, de fase waarin hij verschijnt, de status van de definitie in de begrippenlijst en het OEAPI-object uit de mapping. De laatste twee kolommen zijn voor de lezer.\n\n"
    for kolom in KOLOMVOLGORDE:
        rijen = [n for n, o in typen.items() if o.get("kolom") == kolom and (o.get("scope") == "binnen" or n in uitz)]
        if not rijen:
            continue
        uit += f"### {KOLOMNAAM.get(kolom, kolom)}\n\n| Objecttype | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |\n|---|---|---|---|---|---|---|---|\n"
        for n in sorted(rijen):
            r = eerste.get(n)
            inst = r["instantie"] if r else STUBZIN.lower().rstrip(".")
            fase = r["fase"] if r else verwachting.get(n, "")
            aanname = "ja" if r and r.get("aanname") else ""
            defin = definitie.get(n, "")
            defin = {"gedefinieerd": "ja", "open": "nog niet"}.get(defin, defin or "nog niet")
            uit += f"| {n} | {inst} | {fase} | {aanname} | {defin} | {', '.join(oeapi.get(n, [])) or 'geen equivalent'} | | |\n"
        uit += "\n"
    return uit


def vragenpagina(regels):
    vragen = []
    for r in regels["regels"]:
        if r.get("vraag") and r["vraag"] not in [v for v, _ in vragen]:
            vragen.append((r["vraag"], f"fase {r['fase']}, {r['stap']}, `{norm(r['objecttype'])}`"))
    uit = "## Vragen aan de kerngroep\n\nDe vragen die de regels zelf oproepen, met de regel waar de vraag zichtbaar wordt. Feedback, geen commitment.\n\n"
    for i, (v, plek) in enumerate(vragen[:7], 1):
        uit += f"{i}. {v} ({plek})\n"
    uit += "\nVragen over patronen, schema's, de toetslijst en endpoints horen bij de koppelvlakspecificatie en staan hier niet.\n\n"
    uit += "### Invulblad\n\nPer regel één van vier antwoorden: herken ik dit; heet bij ons anders (welke term); hangt bij ons anders (waaronder); ontbreekt.\n\n| Fase | Stap | Objecttype | Herken | Heet anders | Hangt anders | Ontbreekt |\n|---|---|---|---|---|---|---|\n"
    for r in regels["regels"]:
        if r["soort"] in ("ontstaat", "verandert"):
            uit += f"| {r['fase']} | {r['stap']} | {norm(r['objecttype'])} | | | | |\n"
    return uit + "\n"


def bouw(regels, model, begrippen):
    per_fase = blokken_per_fase(regels)
    uit = leeswijzer(regels, model)
    for f in regels["fasen"]:
        regels_in_fase = [r for r in regels["regels"] if r["fase"] == f["nummer"]]
        uit += fase_sectie(f, per_fase.get(f["nummer"], []), regels_in_fase)
    uit += familietabellen(regels, model, begrippen)
    uit += vragenpagina(regels)
    return uit


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--begrippen", type=pathlib.Path, default=BEGRIPPEN)
    parser.add_argument("--uit", type=pathlib.Path, default=UIT)
    args = parser.parse_args(argv)
    for pad, wat in ((args.regels, "regeltabel"), (args.model, "informatiemodel"), (args.begrippen, "begrippen")):
        if not pathlib.Path(pad).exists():
            print(f"{wat} niet gevonden: {pad}", file=sys.stderr)
            return 2
    regelmap = args.uit.parent / REGELMAP
    if not regelmap.is_dir():
        print(f"regelmap ontbreekt: {regelmap}; draai eerst teken-voorbeeldregels.py", file=sys.stderr)
        return 2
    tekst = bouw(lees(args.regels, "regeltabel"), lees(args.model, "informatiemodel"), lees(args.begrippen, "begrippen"))
    ontbrekend = [m.group(1) for m in re.finditer(r"\]\((img/regels/[^)]+)\)", tekst) if not (args.uit.parent / m.group(1)).exists()]
    if ontbrekend:
        print("regels zonder SVG: " + ", ".join(ontbrekend), file=sys.stderr)
        return 1
    args.uit.write_text(tekst, encoding="utf-8")
    print(f"document geschreven: {args.uit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
