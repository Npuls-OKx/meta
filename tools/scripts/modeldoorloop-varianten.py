#!/usr/bin/env python3
"""De planningsvormen naast de basisuitwerking vinden en met de basis samenvoegen.

Waarom dit bestand bestaat: de voorbeelduitwerking van leerroute 1 volgt de vraaggestuurde vorm uit
het kaderscenario, maar een instelling plant ook capaciteitsgestuurd of kiest op een al geroosterde
gelegenheid (#401). Zo'n vorm staat als eigen regeltabel naast de basis,
modeldoorloop-lr1-<vorm>.json, en erft daarvan de kop: rollen, toestanden, koppelingen,
scope-uitzonderingen en de modelcommit. De controle, de tekenaars en de generator lezen de varianten
hier, zodat zij alle vier dezelfde samengevoegde tabel zien.

Geen eigen opdrachtregel; de scripts laden dit bestand.
"""

import json
import pathlib
import sys

# de leesvolgorde in het document, en de letter in het beeld-ID; de basis is de vraaggestuurde vorm.
# Een vorm erbij gaat mee in modeldoorloop-variant.schema.json (enum van vorm, en [CR] in de patronen)
# en in het patroon van beeld_id in $defs/regel van modeldoorloop-lr1.schema.json.
VORMEN = {"capaciteitsgestuurd": "C", "geroosterd": "R"}
KOP = ("model", "rollen", "toestanden", "scope_uitzonderingen", "koppelingen", "thema_toelichting")
# wat een fase van de basis over een volledige reis zegt, en dus niet voor een delta geldt
ALLEEN_BASIS = ("verwacht", "uitwisselingen", "dekking")


def paden(basispad):
    """De variantbestanden naast de basis: (gevonden als [(vorm, pad)], onbekend als [pad])."""
    basispad = pathlib.Path(basispad)
    gevonden = [(vorm, basispad.parent / f"{basispad.stem}-{vorm}.json") for vorm in VORMEN]
    gevonden = [(vorm, pad) for vorm, pad in gevonden if pad.exists()]
    bekend = {pad for _, pad in gevonden}
    onbekend = sorted(p for p in basispad.parent.glob(f"{basispad.stem}-*.json") if p not in bekend)
    return gevonden, onbekend


def samenvoegen(basis, variant):
    """Een tabel die de scripts lezen als een gewone regeltabel: de kop uit de basis, per fase de naam en
    de overige velden uit de basis met de stappen, de bron en de verwijzingen van de variant, en de regels
    van de variant. Wat alleen voor een volledige reis geldt, valt weg; verwacht blijft een lege lijst."""
    tabel = {k: kopie(basis[k]) for k in KOP if k in basis}
    tabel["vorm"] = variant.get("vorm")
    per_nummer = {f["nummer"]: f for f in basis.get("fasen", [])}
    tabel["fasen"] = []
    for vf in variant.get("fasen", []):
        f = {k: kopie(v) for k, v in per_nummer.get(vf.get("nummer"), {"naam": f"fase {vf.get('nummer')}"}).items()
             if k not in ALLEEN_BASIS}
        f.update({"nummer": vf.get("nummer"), "bron": vf.get("bron"), "stappen": list(vf.get("stappen", [])),
                  "verwacht": [], "voorafgegaan_door": list(vf.get("voorafgegaan_door", [])),
                  "vervangt": list(vf.get("vervangt", []))})
        if vf.get("toelichting"):
            f["toelichting"] = vf["toelichting"]
        tabel["fasen"].append(f)
    tabel["regels"] = kopie(variant.get("regels", []))
    tabel["bevindingen"] = []
    return tabel


def laad(basispad, basis=None):
    """De varianten naast de basis, in de volgorde van VORMEN: ([{vorm, pad, bron, tabel}], onbekend).

    De vorm komt uit de bestandsnaam; wijkt het veld vorm daarvan af, dan meldt de controle dat."""
    basispad = pathlib.Path(basispad)
    if basis is None:
        basis = json.loads(basispad.read_text(encoding="utf-8"))
    gevonden, onbekend = paden(basispad)
    uit = []
    for vorm, pad in gevonden:
        try:
            bron = json.loads(pad.read_text(encoding="utf-8"))
        except json.JSONDecodeError as fout:
            print(f"variant is geen geldige JSON: {pad}, regel {fout.lineno}: {fout.msg}", file=sys.stderr)
            raise SystemExit(1)
        tabel = samenvoegen(basis, bron)
        tabel["vorm"] = vorm
        uit.append({"vorm": vorm, "pad": pad, "bron": bron, "tabel": tabel})
    return uit, onbekend


def beeld_ids(basis, varianten):
    """Alle beeld-ID's in de basis en de geladen varianten."""
    ids = {r.get("beeld_id") for r in basis.get("regels", [])}
    for v in varianten:
        ids |= {r.get("beeld_id") for r in v["tabel"].get("regels", [])}
    return ids - {None}


def eerdere_beelden(basis, varianten, v, fase):
    """De beelden waar een verwijzing in fase `fase` van variant `v` naar mag wijzen: de basis, de varianten
    die eerder in VORMEN staan, en de eigen beelden in een eerdere fase. Zo linkt het document altijd naar
    iets wat erboven staat, en verwijst geen variant naar zichzelf of vooruit."""
    volgorde = [x["vorm"] for x in varianten]
    eerder = [x for x in varianten if volgorde.index(x["vorm"]) < volgorde.index(v["vorm"])]
    ids = beeld_ids(basis, eerder)
    ids |= {r.get("beeld_id") for r in v["tabel"].get("regels", []) if (r.get("fase") or 0) < fase}
    return ids - {None}


def plaatnaam(fase, vorm):
    """De hoofdplaat van een variant in een fase; de tekenaar schrijft hem, de generator toont hem."""
    return f"f{fase}-{vorm}.svg"


def ontstaan_in(basis):
    """De objecttypen die in de basis ontstaan; een variant mag daar een nieuwe_instantie van maken."""
    return {" ".join(str(r.get("objecttype", "")).split()) for r in basis.get("regels", [])
            if r.get("soort") == "ontstaat" and r.get("plaat", "informatiemodel") == "informatiemodel"}


def kopie(waarde):
    return json.loads(json.dumps(waarde))
