#!/usr/bin/env python3
"""Per bericht in een interactiespecificatie een ERD in mermaid, uit het informatiemodel.

Waarom dit script bestaat: een berichtspecificatie zegt veld voor veld wat er over de lijn
gaat, en laat de lezer zelf uitzoeken hoe die velden zich tot elkaar verhouden. Wie de
koppeling bouwt of verifieert wil dat verband zien: welke objecttypen zitten in dit bericht,
welke sleutels en verwijzingen dragen zij, en met welke multipliciteit hangen zij samen.
Relateert aan: Npuls-OKx/meta#372.

    python3 tools/scripts/teken-bericht-erd.py [--map PAD] [--bestand PAD] [--controleer]

Zonder argumenten werkt het script de ERDs bij in de interactiespecificaties in
architecture/docs/specificatie/interactieketen-onderwijsaanbod. Met `--controleer` schrijft het
niets en meldt het alleen welk blok zou wijzigen; dat is de poort voor een bouwmachine.

De namen komen uit het model, de attributen uit het bericht
-----------------------------------------------------------
Een entiteit draagt de naam van het objecttype zoals het [informatiemodel](
architecture/model/informatiemodel/informatiemodel.json) hem schrijft, letterlijk, zodat
beide documenten over hetzelfde praten. De relaties ertussen komen uit datzelfde bestand, met
de multipliciteit uit de soort: een geheel-deelrelatie wordt een-op-veel, een specialisatie
een-op-een met het opschrift `is een`, en een associatie veel-op-veel met haar eigen label.

De attributen komen uit de veldtabel van het bericht zelf, want daar staat wat er werkelijk
over de lijn gaat: de sleutel, het type, de multipliciteit en of het veld verplicht is. Een
veld landt bij het objecttype dat zijn rij in de kolom `Objecttype` noemt. `id` is de sleutel
(PK), en een veld dat op `Id` of `Ids` eindigt is een verwijzing (FK).

Het blok staat tussen twee merktekens in de markdown:

    <!-- erd -->
    ```mermaid
    ...
    ```
    <!-- /erd -->

Alles ertussen wordt overschreven; de rest van het document blijft. Een bericht met
merktekens en zonder objecttype krijgt geen diagram maar de reden, want een leeg diagram
leest als een gat in het model. Een bericht met objecttypen en zonder merktekens staat in de
uitvoer, zodat het niet stil overgeslagen wordt.
"""

import argparse
import collections
import html
import json
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent
MAP = "architecture/docs/specificatie/interactieketen-onderwijsaanbod"
MODEL = "architecture/model/informatiemodel/informatiemodel.json"
BINDING = "architecture/model/informatiemodel/schema-binding.json"
UIT = "img/erd"

BUS, BUS_L, BUS_T = "#ffffb5", "#a8a85a", "#5a5a2a"
INK, MUTED, LIJN = "#1c1c1c", "#5b6663", "#9a9a9a"
FONT = "Arial, Helvetica, sans-serif"
ICOON = '<rect x="2" y="3" width="12" height="10"/><path d="M2 6.5h12"/>'

MARGE, GOOT, RIJGOOT = 26, 34, 96
VAKHOOGTE, REGELHOOGTE, TITELHOOGTE = 30, 14, 46
OMLAAG = ("Composition", "Aggregation")


def breedte(tekst, grootte=12, vet=False):
    return len(tekst) * grootte * (0.56 if vet else 0.52)


def lees_model(pad):
    """De objecttypen en de relaties uit het informatiemodel."""
    d = json.loads(pad.read_text(encoding="utf-8"))
    return {o["naam"] for o in d["objecttypen"]}, d["relaties"]


def lees_binding(pad):
    """De binding tussen de schema's en het model, als die er is.

    Waarvoor: een berichtsectie noemt de schema's waartegen haar payload valideert, en de
    binding zegt per schema welke objecttypen het draagt. Daarmee komt de inhoud van een
    diagram uit het model en niet uit de kolom Objecttype van de tabel eronder. Die kolom
    droeg bij 69 van de 276 rijen proza, en dan bleef het objecttype uit het diagram.
    """
    if not pad or not pad.is_file():
        return {"schemas": {}, "objecttypen": {}}
    return json.loads(pad.read_text(encoding="utf-8"))


def schemas_in(blok):
    """De schemabestanden waartegen de payload van dit bericht valideert, in leesvolgorde.

    Alleen de aanhef telt: de regels tussen de kop en de eerste tabel of het eerste codeblok,
    waar een bericht zijn schema aanwijst met "Volgt x.json" of "Schema x.json". Verderop in
    een sectie staat een schemanaam vaak als vergelijking ("dezelfde vorm als location.json"),
    en die hoort niet in het diagram: hij bracht het vak Onderwijslocatie in een bericht over
    leermiddelgroepen.
    """
    aanhef, in_code = [], False
    for regel in blok.splitlines():
        gestript = regel.strip()
        if gestript.startswith("```"):
            in_code = not in_code
            if not aanhef:
                continue
            break
        if in_code:
            continue
        if gestript.startswith("|") or gestript.startswith("#"):
            if aanhef:
                break
            continue
        if gestript.startswith("<!--") or not gestript:
            continue
        aanhef.append(gestript)
    uit, gezien = [], set()
    for naam, doel in re.findall(
            r"\[`?([a-z0-9][a-z0-9-]*\.json)`?\]\(([^)]*)\)", "\n".join(aanhef)):
        if "voorbeeldpayloads/" in doel:
            continue
        if naam not in gezien:
            gezien.add(naam)
            uit.append(naam)
    return uit


def objecttypen_uit_binding(blok, binding):
    """De objecttypen die de schema's van dit bericht dragen, volgens de binding."""
    uit, gezien = [], set()
    for naam in schemas_in(blok):
        gegeven = (binding.get("schemas") or {}).get(naam)
        if not gegeven:
            continue
        for objecttype in (gegeven.get("draagt") or []) + (gegeven.get("landt_op") or []):
            if objecttype not in gezien:
                gezien.add(objecttype)
                uit.append(objecttype)
    return uit


def attributen_uit_binding(blok, binding):
    """Per objecttype de attribuutsoorten waarvan de bron een schema van dit bericht noemt."""
    namen = set(schemas_in(blok))
    uit = collections.defaultdict(list)
    for objecttype, gegeven in (binding.get("objecttypen") or {}).items():
        for a in gegeven.get("attributen") or []:
            if any(n in a.get("bron", "") for n in namen):
                uit[objecttype].append({
                    "naam": a["naam"],
                    "type": mermaid_type(a.get("datatype")),
                    "sleutel": {"sleutel": "PK", "verwijzing": "FK"}.get(a.get("rol"), a.get("rol") or ""),
                    "opmerking": a.get("kardinaliteit") or "",
                })
    return uit


def mermaid_type(datatype):
    """Het datatype teruggebracht tot wat mermaid in een attribuutblok aanneemt.

    De veldtabel schrijft een datatype uit: `enum: ontwerp, vastgesteld` of `string, 36 tekens`.
    Het eerste woord daarvan draagt nog de dubbele punt of de komma, en daarop breekt de parser
    af met "Expecting ATTRIBUTE_WORD". Hier blijft alleen het woord over.
    """
    eerste = (datatype or "string").split()[0] if (datatype or "").strip() else "string"
    schoon = re.sub(r"[^A-Za-z0-9_\[\]]", "", eerste).lower()
    return schoon or "string"


def berichten(tekst, kopniveau=3):
    """De berichtsecties van een document, met hun kop en hun inhoud.

    Een berichtsectie is een kop onder het hoofdstuk dat de berichten draagt. Het hoofdstuk
    heet `De berichten`, `Berichtspecificatie` of `De berichtspecificatie`; dat verschilt per
    document en daarom telt de naam en niet het nummer.
    """
    regels = tekst.splitlines()
    uit, binnen, kop, inhoud = [], False, None, []
    hek = "#" * kopniveau + " "
    for regel in regels:
        gestript = regel.strip()
        if gestript.startswith("## "):
            if kop:
                uit.append((kop, "\n".join(inhoud)))
                kop, inhoud = None, []
            naam = gestript[3:].strip().lower()
            binnen = "bericht" in naam
            continue
        if gestript.startswith("##### ") and kop:
            uit.append((kop, "\n".join(inhoud)))
            kop, inhoud = None, []
            continue
        if gestript.startswith("**Bericht: ") and gestript.endswith("**"):
            if kop:
                uit.append((kop, "\n".join(inhoud)))
            kop, inhoud, binnen = gestript[2:-2], [], True
            continue
        if binnen and gestript.startswith(hek):
            if kop:
                uit.append((kop, "\n".join(inhoud)))
            kop, inhoud = gestript[len(hek):].strip(), []
            continue
        if kop is not None:
            inhoud.append(regel)
    if kop:
        uit.append((kop, "\n".join(inhoud)))
    return uit


def objecttypen_in(blok, bekend):
    """De objecttypen die de kolom Objecttype van een tabel noemt, in leesvolgorde."""
    uit, gezien = [], set()
    kolom = None
    for regel in blok.splitlines():
        gestript = regel.strip()
        if not gestript.startswith("|"):
            kolom = None
            continue
        cellen = [c.strip() for c in gestript.split("|")[1:-1]]
        if kolom is None:
            kolom = next((i for i, c in enumerate(cellen) if c.lower() == "objecttype"), None)
            continue
        if kolom is None or set(gestript) <= set("|- :"):
            continue
        if kolom >= len(cellen):
            continue
        for naam in re.findall(r"`([^`]+)`", cellen[kolom]):
            if naam in bekend and naam not in gezien:
                gezien.add(naam)
                uit.append(naam)
    return uit


def uitklappen(namen, relaties, diepte=6):
    """De namen aangevuld met wat eronder hangt in de geheel-deelketen van het model.

    Waarom: een bericht dat een specificatiestructuur draagt, draagt haar hele boom. De
    veldtabel noemt daarvan de wortel, want de velden staan per rij op dat niveau; de lezer
    moet zien hoe diep die boom gaat. Van `Opleiding specificatie` loopt hij in het model door
    via opleidingsprogramma, onderwijseenheid en leeronderdeel tot `Les specificatie`.
    """
    kinderen = collections.defaultdict(list)
    for r in relaties:
        if r["soort"] in OMLAAG:
            kinderen[r["van"]].append(r["naar"])
    uit, gezien = list(namen), set(namen)
    rand = list(namen)
    for _ in range(diepte):
        volgende = []
        for naam in rand:
            for kind in kinderen.get(naam, []):
                if kind not in gezien:
                    gezien.add(kind)
                    uit.append(kind)
                    volgende.append(kind)
        if not volgende:
            break
        rand = volgende
    return uit


def legenda(relaties):
    """De betekenis van de lijnen die op dit diagram voorkomen, en alleen die."""
    soorten = {r["soort"] for r in relaties}
    rijen = []
    if soorten & set(OMLAAG):
        rijen.append(r"| `\|\|--o{` | het eerste bestaat uit nul of meer van het tweede |")
    if "Specialization" in soorten:
        rijen.append(r"| `\|\|--\|\|` | het tweede is een soort van het eerste |")
    if soorten - set(OMLAAG) - {"Specialization"}:
        rijen.append("| `}o--o{` | de twee hangen samen, met het opschrift erbij |")
    if not rijen:
        return ""
    return ("\n| Lijn | Betekenis |\n|---|---|\n" + "\n".join(rijen)
            + "\n| `PK` en `FK` | de sleutel van het object, en een verwijzing naar een ander object |"
            + "\n| tekst achter een attribuut | de multipliciteit in dit bericht, en of het veld verplicht is |\n")


def relaties_tussen(namen, relaties):
    """De relaties van het model waarvan beide kanten in deze selectie staan."""
    binnen = set(namen)
    uit, gezien = [], set()
    for r in relaties:
        sleutel = (r["van"], r["naar"], r["soort"])
        if r["van"] in binnen and r["naar"] in binnen and r["van"] != r["naar"] \
                and sleutel not in gezien:
            gezien.add(sleutel)
            uit.append(r)
    return uit


def kardinaliteit(relatie):
    """Wat er aan beide kanten van de lijn staat, afgeleid uit de soort."""
    soort = relatie["soort"]
    if soort in OMLAAG:
        return "1", "n", relatie.get("label") or "bestaat uit"
    if soort == "Specialization":
        return "", "", relatie.get("label") or "is een"
    return "", "", relatie.get("label") or ""


def rijen_van(namen, relaties):
    """De objecttypen in rijen, met een geheel boven zijn delen."""
    omlaag = [r for r in relaties if r["soort"] in OMLAAG]
    diepte = {n: 0 for n in namen}
    for _ in range(len(namen)):
        veranderd = False
        for r in omlaag:
            if diepte[r["naar"]] < diepte[r["van"]] + 1:
                diepte[r["naar"]] = diepte[r["van"]] + 1
                veranderd = True
        if not veranderd:
            break
    per_rij = collections.defaultdict(list)
    for naam in namen:
        per_rij[diepte[naam]].append(naam)
    return [per_rij[d] for d in sorted(per_rij)]


TYPEWOORD = re.compile(r"[a-zA-Z][a-zA-Z0-9_]*")
MERKTEKEN = re.compile(r"<!-- erd -->.*?<!-- /erd -->", re.S)


def attributen_in(blok, bekend):
    """Per objecttype de velden die het bericht erover draagt, in leesvolgorde.

    De veldtabel van een bericht draagt de sleutel, het type, de multipliciteit en of het veld
    verplicht is. Dat is wat er werkelijk over de lijn gaat, en daarmee wat een bouwer nodig
    heeft. Een tabel zonder kolom `Veld` levert alleen entiteiten op.
    """
    uit = collections.defaultdict(list)
    kolommen = None
    for regel in blok.splitlines():
        gestript = regel.strip()
        if not gestript.startswith("|"):
            kolommen = None
            continue
        cellen = [c.strip() for c in gestript.split("|")[1:-1]]
        if kolommen is None:
            kolommen = {c.lower(): i for i, c in enumerate(cellen)}
            continue
        if set(gestript) <= set("|- :") or "objecttype" not in kolommen:
            continue

        def cel(naam):
            i = kolommen.get(naam)
            return cellen[i] if i is not None and i < len(cellen) else ""

        typen = [n for n in re.findall(r"`([^`]+)`", cel("objecttype")) if n in bekend]
        velden = re.findall(r"`([^`]+)`", cel("veld"))
        if not typen or not velden:
            continue
        soort = TYPEWOORD.search(re.sub(r"`[^`]*`", "", cel("type")) or cel("type"))
        opmerking = ", ".join(x for x in (cel("kardinaliteit"),
                                          "verplicht" if cel("verplicht").startswith("ja") else "")
                              if x)
        naam = velden[0]
        kort = naam.split(".")[-1] if "." in naam else naam
        # Een pad met twee array-niveaus, zoals `placementGroups[].members[].studentId`, draagt
        # binnen het voorvoegsel nog een punt. Die punt wordt een liggend streepje; zonder die
        # stap haalde de opruiming hieronder haar weg en plakten de twee niveaus aan elkaar.
        voorvoegsel = (naam[: naam.rindex(".")].replace("[]", "").replace(".", "_") + "_"
                       if "." in naam else "")
        attribuut = {
            "naam": re.sub(r"[^A-Za-z0-9_]", "", voorvoegsel + kort) or "veld",
            "type": (soort.group(0) if soort else "string").lower(),
            "sleutel": "PK" if kort == "id" else ("FK" if re.search(r"Ids?$", kort) else ""),
            "opmerking": opmerking,
        }
        for objecttype in typen:
            if attribuut["naam"] not in [a["naam"] for a in uit[objecttype]]:
                uit[objecttype].append(attribuut)
    return uit


def verbinding(relatie):
    """De mermaid-notatie en het opschrift bij een relatiesoort uit het model."""
    soort = relatie["soort"]
    if soort in OMLAAG:
        return "||--o{", relatie.get("label") or "bestaat uit"
    if soort == "Specialization":
        return "||--||", relatie.get("label") or "is een"
    return "}o--o{", relatie.get("label") or "hangt samen met"


def mermaid(namen, relaties, attributen):
    """Het erDiagram-blok: de entiteiten met hun attributen, en de relaties ertussen."""
    regels = ["```mermaid", "erDiagram"]
    for r in relaties:
        notatie, opschrift = verbinding(r)
        regels.append(f'    "{r["van"]}" {notatie} "{r["naar"]}" : "{opschrift}"')
    for naam in namen:
        velden = attributen.get(naam) or []
        if not velden:
            regels.append(f'    "{naam}" {{ }}' if not relaties else f'    "{naam}" {{ }}')
            continue
        regels.append(f'    "{naam}" {{')
        for a in velden:
            staart = f' {a["sleutel"]}' if a["sleutel"] else ""
            opmerking = f' "{a["opmerking"]}"' if a["opmerking"] else ""
            regels.append(f'        {a["type"]} {a["naam"]}{staart}{opmerking}')
        regels.append("    }")
    regels.append("```")
    return "\n".join(regels)


def blok_voor(namen, relaties, attributen):
    """Wat er tussen de merktekens komt: een diagram, of de reden dat er geen is."""
    if not namen:
        return ("Dit bericht draagt geen objecttype uit het informatiemodel: de velden zijn "
                "eigenschappen van het contract.")
    return mermaid(namen, relaties, attributen) + "\n" + legenda(relaties)


def verwerk(bestand, bekend, relaties, controleer=False, binding=None):
    """De ERDs van een document bijwerken; geeft per bericht terug wat er gebeurde.

    De objecttypen komen uit de binding wanneer die het schema van dit bericht kent, en
    anders uit de kolom Objecttype van de tabel. De attribuutsoorten komen uit beide: de
    veldtabel draagt de kardinaliteit van dit bericht, de binding vult aan wat zij niet noemt.
    """
    binding = binding or {"schemas": {}, "objecttypen": {}}
    tekst = bestand.read_text(encoding="utf-8")
    verslag, gewenste = [], []
    for kop, blok in berichten(tekst):
        uit_tabel = objecttypen_in(blok, bekend)
        gezien, samen = set(), []
        for naam in uit_tabel + objecttypen_uit_binding(blok, binding):
            if naam not in gezien:
                gezien.add(naam)
                samen.append(naam)
        namen = uitklappen(samen, relaties)
        eigen = relaties_tussen(namen, relaties)
        merk = MERKTEKEN.search(blok)
        if merk is None:
            verslag.append((kop, "geen merktekens",
                            f"{len(namen)} objecttypen; zet <!-- erd --> en <!-- /erd --> in de sectie"))
            continue
        attributen = dict(attributen_uit_binding(blok, binding))
        for objecttype, velden in attributen_in(blok, bekend).items():
            # De veldtabel gaat voor: zij draagt de kardinaliteit van dit bericht.
            uit_tabel = {a["naam"]: a for a in velden}
            overig = [a for a in attributen.get(objecttype, []) if a["naam"] not in uit_tabel]
            attributen[objecttype] = velden + overig
        nieuw_blok = f"<!-- erd -->\n{blok_voor(namen, eigen, attributen)}\n<!-- /erd -->"
        gewenste.append(nieuw_blok)
        verslag.append((kop, "ongewijzigd" if merk.group(0) == nieuw_blok
                        else ("zou wijzigen" if controleer else "bijgewerkt"),
                        f"{len(namen)} objecttypen, {len(eigen)} relaties"))

    # Op plek vervangen en niet op inhoud: twee lege blokken zijn letterlijk gelijk, en dan
    # raakt een vervanging op inhoud steeds hetzelfde blok.
    rest = list(gewenste)
    if len(MERKTEKEN.findall(tekst)) != len(gewenste):
        print(f"  {bestand.name}: er staan merktekens buiten een berichtsectie; niets geschreven",
              file=sys.stderr)
        return verslag, False
    nieuw = MERKTEKEN.sub(lambda _: rest.pop(0), tekst)
    if not controleer and nieuw != tekst:
        bestand.write_text(nieuw, encoding="utf-8")
    return verslag, nieuw != tekst


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--map", default=None, help="de map met de interactiespecificaties")
    parser.add_argument("--bestand", default=None, help="alleen dit document")
    parser.add_argument("--model", default=None, help="het informatiemodel")
    parser.add_argument("--binding", default=None, help="de binding tussen schema's en model")
    parser.add_argument("--controleer", action="store_true",
                        help="schrijf niets en meld alleen wat zou wijzigen")
    args = parser.parse_args(argv)

    map_ = pathlib.Path(args.map) if args.map else WORTEL / MAP
    model = pathlib.Path(args.model) if args.model else WORTEL / MODEL
    if not model.is_file():
        print(f"Het informatiemodel staat niet op {model}.", file=sys.stderr)
        return 2
    if args.bestand:
        gekozen = pathlib.Path(args.bestand)
        bestanden = [gekozen if gekozen.is_file() else map_ / gekozen.name]
    else:
        bestanden = sorted(map_.glob("is-??-*.md"))
    if not bestanden or not all(b.is_file() for b in bestanden):
        print(f"Geen interactiespecificatie gevonden in {map_}.", file=sys.stderr)
        return 2

    bekend, relaties = lees_model(model)
    binding = lees_binding(pathlib.Path(args.binding) if args.binding else WORTEL / BINDING)
    gewijzigd, zonder = False, 0
    for bestand in bestanden:
        print(f"\n{bestand.name}")
        verslag, veranderd = verwerk(bestand, bekend, relaties, args.controleer, binding)
        gewijzigd = gewijzigd or veranderd
        for kop, stand, wat in verslag:
            print(f"  {kop[:58]:60} {stand:14} {wat}")
            zonder += 1 if stand == "geen merktekens" else 0
    if zonder:
        print(f"\n{zonder} berichten zonder merktekens; daar staat geen ERD.")
    if args.controleer and gewijzigd:
        print("\nDe ERDs lopen achter op het informatiemodel.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
