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
PUBLIC = "https://github.com/Npuls-OKx/Public/blob/dev/"
BRONNEN = {
    "leerroute-1-regulier.md": PUBLIC + "Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md",
    "voorbeeldpayloads.md": PUBLIC + "Koppelvlakspecificaties/Datamodelschema's/voorbeeldpayloads.md",
    "scenario-1.1-regulier-happyflow.md": "../../docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md",
    "informatiemodel.md": "informatiemodel.md",
}


def bronlinks(bron, faselinks=None):
    """De bron als tekst met links: het bestand naar zijn plek, elk regelnummer (r1046) naar die regel,
    en 'Fase n' in het kaderscenario naar de fasekop. Onbekende bronnen blijven tekst."""
    m = re.match(r"([\w\-.']+\.md)(.*)", bron)
    if not m or m.group(1) not in BRONNEN:
        return bron
    bestand, rest = m.group(1), m.group(2)
    url = BRONNEN[bestand]
    rest = re.sub(r"\br(\d+)\b", lambda x: f"[r{x.group(1)}]({url}?plain=1#L{x.group(1)})", rest)
    rest = re.sub(r"\btot (\d+)\b", lambda x: f"tot [{x.group(1)}]({url}?plain=1#L{x.group(1)})", rest)
    if bestand == "leerroute-1-regulier.md" and faselinks:
        rest = re.sub(r"\bFase (\d)\b", lambda x: f"[Fase {x.group(1)}]({faselinks[int(x.group(1))]})" if int(x.group(1)) in faselinks else x.group(0), rest)
    return f"[{bestand}]({url}){rest}"


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
        uit[blok["fase"]].append({"naam": teken.bestandsnaam(blok, n), "stap": blok["stap"], "soort": blok["soort"], "verdieping": blok.get("verdieping"),
                                  "beeld": blok.get("beeld"), "beeld_id": blok.get("beeld_id")})
    return uit


def leeswijzer(regels, model):
    k = regels["koppelingen"]
    mapping = "; ".join(f"{v} is {kk.replace(' > ', ' naar ')}" for kk, v in k.items())
    return f"""# De opleiding van Jochem in het informatiemodel

Relateert aan: het [kaderscenario leerroute 1](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md) (persona Jochem, Apothekersassistent, cohort 2026), het architectuurkader van OKx, en het [informatiemodel OKx](informatiemodel.md). Gegenereerd uit `voorbeeld-lr1-regels.json`; gecontroleerd tegen `informatiemodel.json` op commit {regels['model']['informatiemodel_commit']} en `begrippen.json` op commit {regels['model']['begrippen_commit']}.

## Leeswijzer

Dit document loopt stap voor stap door de instellingsreis van het kaderscenario en toont per stap wat er in het informatiemodel ontstaat en wat er tussen systemen beweegt, met de waarde voor Jochem erin. Het is een leeshulp op conceptueel niveau (MIM 1 en 2): geen payloads, geen endpoints, geen diensten. Eén instantie per objecttype toont het type, niet het aantal.

Elk beeld heeft een ID en een titel die zegt wat het toont: F1-02 is het tweede beeld van fase 1. Beide staan in het beeld zelf, als kop erboven (met een eigen anker in dit document) en in het regelregister achterin; de bijlage en het invulblad noemen het ID. Verwijs naar een beeld met zijn ID, en naar een regel met dat ID en het objecttype.

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

Een **verdieping** (zelfde rol en stap, met "verdieping" op de processtap) zoomt in op een regel erboven. Een paars objecttype komt van de conceptplaat "Informatiemodel Onderwijsontwerp" in het ArchiMate-model (een verdieping daaruit heeft ook een gestippelde rand en een chip): het laat zien waar de informatiemodelplaat kan groeien en telt niet mee in de bijlage en het invulblad.

Koppeling-ID's op hoofdplaat v1.7: {mapping}. Een pijl die op de hoofdplaat staat maar geen koppelingspecificatie heeft, staat als "zonder koppelingspecificatie"; een stroom uit het kaderscenario zonder pijl op de hoofdplaat staat als "geen pijl op de hoofdplaat".

De fasenamen zijn de sectiekoppen "Fase 1" tot "Fase 8" van het kaderscenario. Het kaderscenario noemt fase 3 in de fasenlijst "Instroom, afstemming en plaatsing" en in de sectiekop "Instroom, intake en plaatsing"; hier geldt de sectiekop.

Wat hier staat is feedback, geen commitment: het voorbeeld beslist niets over het model. Per objecttype staan in de bijlage twee lege kolommen, "heet bij u" en "hangt bij u onder", voor wie het naast het eigen model legt.
"""


def fase_sectie(f, blokken, regels_in_fase):
    kop = f"## Fase {f['nummer']}: {f['naam']}\n\n"
    if f.get("link"):
        kop += f"De fase in detail: [kaderscenario leerroute 1, fase {f['nummer']}]({f['link']}).\n\n"
    mora = f.get("mora_hoofdproces")
    chips_obj = [norm(r["objecttype"]) for r in regels_in_fase if r["soort"] in ("ontstaat", "verandert") and r.get("plaat", "informatiemodel") == "informatiemodel"]
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
        alt = f"{b['soort']}: {b['stap']}" + (f", verdieping: {b['verdieping']}" if b.get("verdieping") else "")
        if b.get("beeld"):
            uit += f"### {teken.beeldtitel(b)}\n\n"
        uit += f"![{alt}]({REGELMAP}/{b['naam']})\n\n"
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
        if r["soort"] in ("ontstaat", "verandert") and n not in eerste and r.get("plaat", "informatiemodel") == "informatiemodel":
            eerste[n] = r
    verwachting = {norm(v): f["nummer"] for f in regels["fasen"] for v in f["verwacht"]}
    uit = "## Bijlage: alle objecttypen per begrippenfamilie\n\nPer objecttype het beeld waarin hij verschijnt (het ID uit de kop), de instantie voor Jochem, de fase, de status van de definitie in de begrippenlijst en het OEAPI-object uit de mapping. De laatste twee kolommen zijn voor de lezer.\n\n"
    for kolom in KOLOMVOLGORDE:
        rijen = [n for n, o in typen.items() if o.get("kolom") == kolom and (o.get("scope") == "binnen" or n in uitz)]
        if not rijen:
            continue
        uit += f"### {KOLOMNAAM.get(kolom, kolom)}\n\n| Objecttype | Beeld | Jochem | Fase | Aanname | Definitie | OEAPI | Heet bij u | Hangt bij u onder |\n|---|---|---|---|---|---|---|---|---|\n"
        for n in sorted(rijen):
            r = eerste.get(n)
            inst = r["instantie"] if r else STUBZIN.lower().rstrip(".")
            fase = r["fase"] if r else verwachting.get(n, "")
            aanname = "ja" if r and r.get("aanname") else ""
            defin = definitie.get(n, "")
            defin = {"gedefinieerd": "ja", "open": "nog niet"}.get(defin, defin or "nog niet")
            beeld = r.get("beeld_id", "") if r else ""
            uit += f"| {n} | {beeld} | {inst} | {fase} | {aanname} | {defin} | {', '.join(oeapi.get(n, [])) or 'geen equivalent'} | | |\n"
        uit += "\n"
    return uit


def vragenpagina(regels):
    vragen = []
    for r in regels["regels"]:
        if r.get("vraag") and r["vraag"] not in [v for v, _ in vragen]:
            vragen.append((r["vraag"], f"{r.get('beeld_id', '')}, `{norm(r['objecttype'])}`"))
    uit = "## Vragen aan de kerngroep\n\nDe vragen die de regels zelf oproepen, met de regel waar de vraag zichtbaar wordt. Feedback, geen commitment.\n\n"
    for i, (v, plek) in enumerate(vragen[:7], 1):
        uit += f"{i}. {v} ({plek})\n"
    for v, plek in vragen[7:]:
        print(f"waarschuwing: vraag buiten de zeven, niet in het document: {plek}", file=sys.stderr)
    uit += "\nVragen over patronen, schema's, de toetslijst en endpoints horen bij de koppelvlakspecificatie en staan hier niet.\n\n"
    uit += "### Invulblad\n\nPer regel één van vier antwoorden: herken ik dit; heet bij ons anders (welke term); hangt bij ons anders (waaronder); ontbreekt. De kolom Beeld draagt het beeld-ID uit de kop erboven.\n\n| Fase | Beeld | Objecttype | Herken | Heet anders | Hangt anders | Ontbreekt |\n|---|---|---|---|---|---|---|\n"
    for r in regels["regels"]:
        if r["soort"] in ("ontstaat", "verandert") and r.get("plaat", "informatiemodel") == "informatiemodel":
            uit += f"| {r['fase']} | {r.get('beeld_id', '')} | {norm(r['objecttype'])} | | | | |\n"
    return uit + "\n"


def regelregister(regels, per_fase):
    """Elke regel onder de titel van haar beeld, met bestand en bron als links, om naar te verwijzen."""
    faselinks = {f["nummer"]: f["link"] for f in regels["fasen"] if f.get("link")}
    bestand = {b["beeld"]: b["naam"] for blokken in per_fase.values() for b in blokken if b.get("beeld")}
    uit = "## Regelregister\n\nElke regel onder het ID en de titel van haar beeld (fase, stap, bestand) met de bron. Verwijs naar een beeld met zijn ID en naar een regel met dat ID en het objecttype.\n\n"
    vorige = None
    for r in regels["regels"]:
        beeld = r.get("beeld", "")
        if beeld != vorige:
            b = bestand.get(beeld)
            kop = " - ".join(x for x in (r.get("beeld_id"), beeld) if x)
            uit += (("\n" if vorige else "") + f"**{kop}** (fase {r['fase']}, {r['stap']}" + (f"; [{b}]({REGELMAP}/{b})" if b else "") + ")\n\n"
                    "| Soort | Objecttype | Instantie | Bron |\n|---|---|---|---|\n")
            vorige = beeld
        soort = r["soort"] + (" (conceptplaat)" if r.get("plaat") == "onderwijsontwerp" else "")
        uit += f"| {soort} | {norm(r['objecttype'])} | {r['instantie']} | {bronlinks(r['bron'], faselinks)} |\n"
    return uit + "\n"


def bouw(regels, model, begrippen):
    per_fase = blokken_per_fase(regels)
    uit = leeswijzer(regels, model)
    for f in regels["fasen"]:
        regels_in_fase = [r for r in regels["regels"] if r["fase"] == f["nummer"]]
        uit += fase_sectie(f, per_fase.get(f["nummer"], []), regels_in_fase)
    uit += familietabellen(regels, model, begrippen)
    uit += vragenpagina(regels)
    uit += regelregister(regels, per_fase)
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
