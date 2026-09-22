#!/usr/bin/env python3
"""De regeltabel van de voorbeelduitwerking controleren tegen het informatiemodel.

Waarom dit script bestaat: het voorbeeld (de opleiding van Jochem, stap voor stap
in het informatiemodel) mag geen eigen dialect worden naast de plaat. Elke regel
wijst daarom naar een objecttype, een relatie, een rol en een pijl die bestaan;
dit script faalt zodra dat niet zo is, en meldt per fase welke objecttypen binnen
scope nog geen ontstaat-regel hebben.

    python3 scripts/controleer-voorbeeldregels.py [--regels PAD] [--model PAD]
        [--stromen PAD] [--conceptplaat PAD] [--fasen 2,3,4] [--model-commit SHA]

Controles (R1 en R2 uit het featureplan):
1. schema: verplichte velden per soort regel (eigen validatie, geen afhankelijkheid);
2. elke objecttypenaam bestaat in informatiemodel.json (witruimte genormaliseerd);
   een objecttype buiten scope alleen met een scope-uitzondering;
3. elke relatie bestaat als (soort, van, naar); nesting alleen op aggregatie of compositie;
4. elke rol staat in de rollenlijst, elke toestand in de toestandenlijst, elke stap in de fasenlijst;
5. elke stroomt-regel wijst naar een relatie-id in stromen.json of draagt de markering
   "geen pijl op de hoofdplaat";
6. dekking: elk objecttype binnen scope heeft precies een ontstaat-regel, in de fase van de
   verwachting; latere verschijningen zijn verandert-regels; een genest kind van hetzelfde
   objecttype in dezelfde stap (zelfaggregatie) telt niet als tweede ontstaan, en een regel met
   nieuwe_instantie evenmin (een verdere instantie die het scenario nodig heeft);
7. de model-commit in de kop komt overeen met de meegegeven commit (waarschuwing);
8. elke regel draagt het ID en de titel van haar beeld; een beeld is aaneengesloten, ligt in een fase,
   een stap en een soort (ontstaat of stroomt), en komt niet twee keer voor; ID en titel horen
   een-op-een bij elkaar, het ID heeft de vorm F<fase>-<volgnummer> en loopt op binnen de fase;
   verdere relaties (relaties) bestaan op de plaat en dragen geen nesting;
9. een regel met plaat "onderwijsontwerp" hoort bij een verdieping of een stroom en wijst naar een objecttype en
   een relatie op de conceptplaat (conceptplaat-onderwijsontwerp.json); zulke regels tellen niet
   mee in de dekking en kennen geen scope.

Exitcode 0: geen bevindingen; 1: bevindingen; 2: invoer niet leesbaar.
"""

import argparse
import json
import pathlib
import re
import sys

REGELS = pathlib.Path("architecture/model/informatiemodel/voorbeeld-lr1-regels.json")
MODEL = pathlib.Path("architecture/model/informatiemodel/informatiemodel.json")
STROMEN = pathlib.Path("architecture/model/informatiemodel/stromen.json")
CONCEPTPLAAT = pathlib.Path("architecture/model/informatiemodel/conceptplaat-onderwijsontwerp.json")
PLATEN = {"informatiemodel", "onderwijsontwerp"}
GEEN_PIJL = "geen pijl op de hoofdplaat"
NESTING = {"Aggregation", "Composition"}
SOORTEN = {"ontstaat", "verandert", "stroomt"}


def norm(naam):
    return " ".join(str(naam).split())


def lees_json(pad, wat):
    try:
        return json.loads(pathlib.Path(pad).read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"{wat} niet gevonden: {pad}")
    except json.JSONDecodeError as fout:
        print(f"{wat} is geen geldige JSON: {pad}, regel {fout.lineno}: {fout.msg}", file=sys.stderr)
        raise SystemExit(1)


def plek_van(r, i):
    beeld = " - ".join(x for x in (r.get("beeld_id"), r.get("beeld")) if x) or "zonder beeld"
    return f"regel {i + 1} ({beeld}: {r.get('objecttype')})"


def _beeld_id(r, plek, beeld, nieuw, ids):
    """Het ID hoort een-op-een bij de titel, heeft de vorm F<fase>-<volgnummer> en loopt op binnen de fase."""
    uit, bid, fase = [], r.get("beeld_id"), r.get("fase")
    titel_van_id, id_van_titel, hoogste = ids
    if not bid:
        return uit
    if not re.fullmatch(r"F[1-8]-\d{2}", bid):
        return [f"{plek}: beeld-ID {bid!r} heeft niet de vorm F<fase>-<volgnummer>, bijvoorbeeld F1-02"]
    if bid[1] != str(fase):
        uit.append(f"{plek}: beeld-ID {bid!r} noemt een andere fase dan {fase}")
    if titel_van_id.setdefault(bid, beeld) != beeld:
        uit.append(f"{plek}: beeld-ID {bid!r} hoort al bij beeld {titel_van_id[bid]!r}")
    if id_van_titel.setdefault(beeld, bid) != bid:
        uit.append(f"{plek}: beeld {beeld!r} draagt twee ID's ({id_van_titel[beeld]} en {bid})")
    if nieuw:
        nr = int(bid.split("-")[1])
        if nr <= hoogste.get(fase, 0):
            uit.append(f"{plek}: beeld-ID {bid!r} loopt niet op binnen fase {fase}")
        hoogste[fase] = max(nr, hoogste.get(fase, 0))
    return uit


def schema(regels):
    """Verplichte velden en typen; geeft bevindingen."""
    uit = []
    for sleutel in ("model", "fasen", "rollen", "toestanden", "scope_uitzonderingen", "koppelingen", "regels"):
        if sleutel not in regels:
            uit.append(f"kop: veld {sleutel} ontbreekt")
    beelden, vorige, ids = {}, None, ({}, {}, {})
    for i, r in enumerate(regels.get("regels", [])):
        plek = plek_van(r, i)
        for veld in ("beeld_id", "beeld", "fase", "stap", "soort", "objecttype", "instantie", "bron"):
            if veld not in r or r[veld] in ("", None):
                uit.append(f"{plek}: veld {veld} ontbreekt")
        beeld = r.get("beeld")
        if beeld:
            sleutel = (r.get("fase"), r.get("stap"), "stroomt" if r.get("soort") == "stroomt" else "ontstaat", r.get("verdieping"))
            if beeld in beelden and beelden[beeld] != sleutel:
                uit.append(f"{plek}: beeld {beeld!r} ligt ook in een andere fase, stap, soort of verdieping")
            elif beeld in beelden and vorige != beeld:
                uit.append(f"{plek}: beeld {beeld!r} is niet aaneengesloten; regels van een beeld staan bij elkaar")
            uit += _beeld_id(r, plek, beeld, beeld not in beelden, ids)
            beelden.setdefault(beeld, sleutel)
        vorige = beeld
        soort = r.get("soort")
        if soort not in SOORTEN:
            uit.append(f"{plek}: soort {soort!r} is niet ontstaat, verandert of stroomt")
        if soort in ("ontstaat", "verandert") and not r.get("wie"):
            uit.append(f"{plek}: veld wie ontbreekt")
        if soort == "verandert" and not r.get("toestand"):
            uit.append(f"{plek}: veld toestand ontbreekt bij verandert")
        if soort == "stroomt":
            for veld in ("van", "naar", "pijl"):
                if not r.get(veld):
                    uit.append(f"{plek}: veld {veld} ontbreekt bij stroomt")
        if r.get("plaat", "informatiemodel") not in PLATEN:
            uit.append(f"{plek}: plaat {r.get('plaat')!r} is niet informatiemodel of onderwijsontwerp")
        if r.get("plaat") == "onderwijsontwerp" and not r.get("verdieping") and r.get("soort") != "stroomt":
            uit.append(f"{plek}: de conceptplaat mag alleen in een verdieping of in een stroomt-regel")
        rel = r.get("relatie")
        if rel is not None and (not isinstance(rel, dict) or not all(k in rel for k in ("soort", "van", "naar"))):
            uit.append(f"{plek}: relatie moet soort, van en naar hebben")
        if rel is not None and isinstance(rel, dict) and rel.get("label") == "":
            uit.append(f"{plek}: relatielabel is leeg; laat het veld weg of vul het")
        for x in r.get("relaties") or []:
            if not isinstance(x, dict) or not all(k in x for k in ("soort", "van", "naar")):
                uit.append(f"{plek}: elke relatie in relaties moet soort, van en naar hebben")
            elif x.get("nesting"):
                uit.append(f"{plek}: nesting hoort in relatie, niet in relaties")
    return uit


def controleer(regels, model, stromen=None, fasen_filter=None, model_commit=None, conceptplaat=None):
    """Alle controles; geeft (bevindingen, waarschuwingen, ontbrekend per fase)."""
    bevindingen = schema(regels)
    waarschuwingen = []
    if bevindingen and any(b.startswith("kop:") for b in bevindingen):
        return bevindingen, waarschuwingen, {}

    typen = {norm(o["naam"]): o for o in model["objecttypen"]}
    relaties = {(r["soort"], norm(r["van"]), norm(r["naar"])): (r.get("label") or "") for r in model["relaties"]}
    concept_typen = {norm(o["naam"]) for o in (conceptplaat or {}).get("objecttypen", [])}
    concept_relaties = {(r["soort"], norm(r["van"]), norm(r["naar"])): (r.get("label") or "") for r in (conceptplaat or {}).get("relaties", [])}
    uitzonderingen = {norm(u["objecttype"]) for u in regels["scope_uitzonderingen"]}
    binnen = {n for n, o in typen.items() if o.get("scope") == "binnen"} | uitzonderingen
    rollen = set(regels["rollen"])
    toestanden = {t["naam"] for t in regels["toestanden"]}
    fasen = {f["nummer"]: f for f in regels["fasen"]}
    pijlen = {s["id"] for s in (stromen or {}).get("stromen", [])}

    for u in uitzonderingen:
        if u not in typen:
            bevindingen.append(f"scope-uitzondering {u!r} bestaat niet in het informatiemodel")
    for f in regels["fasen"]:
        for v in f["verwacht"]:
            if norm(v) not in typen:
                bevindingen.append(f"fase {f['nummer']}: verwacht objecttype {v!r} bestaat niet in het informatiemodel")
    if model_commit and regels["model"].get("informatiemodel_commit") != model_commit:
        waarschuwingen.append(f"kop noemt informatiemodel_commit {regels['model'].get('informatiemodel_commit')}, gecontroleerd tegen {model_commit}")

    ontstaan = {}
    for i, r in enumerate(regels["regels"]):
        plek = plek_van(r, i)
        naam = norm(r.get("objecttype", ""))
        concept = r.get("plaat") == "onderwijsontwerp"
        if concept and conceptplaat is None:
            bevindingen.append(f"{plek}: regel op de conceptplaat, maar de conceptplaat is niet geladen")
            continue
        plaat_typen, plaat_relaties = (concept_typen, concept_relaties) if concept else (typen, relaties)
        plaatnaam = "de conceptplaat" if concept else "de plaat"
        if naam not in plaat_typen:
            bevindingen.append(f"{plek}: objecttype {r.get('objecttype')!r} bestaat niet " + ("op de conceptplaat" if concept else "in het informatiemodel"))
            continue
        if not concept and naam not in binnen:
            bevindingen.append(f"{plek}: objecttype {naam!r} staat buiten scope en heeft geen scope-uitzondering")
        fase = fasen.get(r.get("fase"))
        if fase is None:
            bevindingen.append(f"{plek}: fase {r.get('fase')} staat niet in de fasenlijst")
        elif r.get("stap") not in fase["stappen"]:
            bevindingen.append(f"{plek}: stap {r.get('stap')!r} staat niet in fase {r.get('fase')}")
        if r.get("soort") in ("ontstaat", "verandert") and r.get("wie") not in rollen:
            bevindingen.append(f"{plek}: rol {r.get('wie')!r} staat niet in de rollenlijst")
        if r.get("soort") == "verandert" and r.get("toestand") not in toestanden:
            bevindingen.append(f"{plek}: toestand {r.get('toestand')!r} staat niet in de toestandenlijst")
        if r.get("soort") == "stroomt":
            if r.get("pijl") != GEEN_PIJL and stromen is not None and r.get("pijl") not in pijlen:
                bevindingen.append(f"{plek}: pijl {r.get('pijl')!r} staat niet in stromen.json")
            if r.get("pijl") == GEEN_PIJL:
                waarschuwingen.append(f"{plek}: geen pijl op de hoofdplaat ({r.get('van')} naar {r.get('naar')})")
        rel = r.get("relatie")
        if isinstance(rel, dict) and all(k in rel for k in ("soort", "van", "naar")):
            sleutel = (rel["soort"], norm(rel["van"]), norm(rel["naar"]))
            if sleutel not in plaat_relaties:
                bevindingen.append(f"{plek}: relatie {rel['soort']} van {rel['van']!r} naar {rel['naar']!r} staat niet op {plaatnaam}")
            elif rel.get("label") and plaat_relaties[sleutel] != rel["label"]:
                bevindingen.append(f"{plek}: relatielabel {rel['label']!r} wijkt af van {plaatnaam} ({plaat_relaties[sleutel]!r})")
            if rel.get("nesting") and rel["soort"] not in NESTING:
                bevindingen.append(f"{plek}: nesting alleen op een aggregatie of compositie, niet op {rel['soort']}")
        for x in r.get("relaties") or []:
            if not isinstance(x, dict) or not all(k in x for k in ("soort", "van", "naar")):
                continue
            sleutel = (x["soort"], norm(x["van"]), norm(x["naar"]))
            if sleutel not in plaat_relaties:
                bevindingen.append(f"{plek}: relatie {x['soort']} van {x['van']!r} naar {x['naar']!r} (relaties) staat niet op {plaatnaam}")
            elif x.get("label") and plaat_relaties[sleutel] != x["label"]:
                bevindingen.append(f"{plek}: relatielabel {x['label']!r} (relaties) wijkt af van {plaatnaam} ({plaat_relaties[sleutel]!r})")
            if naam not in (norm(x["van"]), norm(x["naar"])):
                bevindingen.append(f"{plek}: relatie in relaties raakt het objecttype {naam!r} niet")
        if r.get("soort") == "ontstaat" and not concept:
            # een genest kind van hetzelfde objecttype (zelfaggregatie op de plaat, bijvoorbeeld een
            # leeruitkomst onder een leeruitkomst) in dezelfde stap telt niet als tweede ontstaan
            zelf = isinstance(rel, dict) and rel.get("nesting") and norm(rel.get("van", "")) == naam == norm(rel.get("naar", ""))
            if r.get("nieuwe_instantie") and naam not in ontstaan:
                bevindingen.append(f"{plek}: nieuwe_instantie, maar {naam!r} is nog niet eerder ontstaan")
            if not zelf and not r.get("nieuwe_instantie"):
                ontstaan.setdefault(naam, []).append((r.get("fase"), plek))

    for naam, plekken in ontstaan.items():
        if len(plekken) > 1:
            bevindingen.append(f"objecttype {naam!r} heeft {len(plekken)} ontstaat-regels; een latere verschijning is een verandert-regel")
    verwachting = {norm(v): f["nummer"] for f in regels["fasen"] for v in f["verwacht"]}
    for naam, plekken in ontstaan.items():
        fase, plek = plekken[0]
        if naam in verwachting and verwachting[naam] != fase:
            bevindingen.append(f"{plek}: objecttype {naam!r} ontstaat in fase {fase}, verwacht in fase {verwachting[naam]}")
    ontbrekend = {}
    for naam in sorted(binnen):
        if naam in ontstaan:
            continue
        fase = verwachting.get(naam)
        if fase is None:
            bevindingen.append(f"objecttype {naam!r} binnen scope staat in geen enkele fase-verwachting")
            continue
        if fasen_filter and fase not in fasen_filter:
            continue
        ontbrekend.setdefault(fase, []).append(naam)
    for fase in sorted(ontbrekend):
        bevindingen.append(f"fase {fase}: geen ontstaat-regel voor {', '.join(ontbrekend[fase])}")
    return bevindingen, waarschuwingen, ontbrekend


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--regels", type=pathlib.Path, default=REGELS)
    parser.add_argument("--model", type=pathlib.Path, default=MODEL)
    parser.add_argument("--stromen", type=pathlib.Path, default=STROMEN)
    parser.add_argument("--conceptplaat", type=pathlib.Path, default=CONCEPTPLAAT, help="export van de view Informatiemodel Onderwijsontwerp")
    parser.add_argument("--fasen", help="alleen de dekking van deze fasen melden, bijvoorbeeld 2,3,4")
    parser.add_argument("--model-commit", help="commit van informatiemodel.json om tegen de kop te toetsen")
    args = parser.parse_args(argv)
    for pad, wat in ((args.regels, "regeltabel"), (args.model, "informatiemodel")):
        if not pathlib.Path(pad).exists():
            print(f"{wat} niet gevonden: {pad}", file=sys.stderr)
            return 2
    regels = lees_json(args.regels, "regeltabel")
    model = lees_json(args.model, "informatiemodel")
    stromen = lees_json(args.stromen, "stromen") if pathlib.Path(args.stromen).exists() else None
    if stromen is None:
        print(f"waarschuwing: {args.stromen} ontbreekt; pijlen niet gecontroleerd", file=sys.stderr)
    conceptplaat = lees_json(args.conceptplaat, "conceptplaat") if pathlib.Path(args.conceptplaat).exists() else None
    fasen_filter = {int(x) for x in args.fasen.split(",")} if args.fasen else None
    bevindingen, waarschuwingen, _ = controleer(regels, model, stromen, fasen_filter, args.model_commit, conceptplaat)
    for w in waarschuwingen:
        print(f"waarschuwing: {w}")
    for b in bevindingen:
        print(f"bevinding: {b}")
    n = len(regels.get("regels", []))
    print(f"{n} regels gecontroleerd, {len(bevindingen)} bevindingen, {len(waarschuwingen)} waarschuwingen")
    return 1 if bevindingen else 0


if __name__ == "__main__":
    sys.exit(main())
