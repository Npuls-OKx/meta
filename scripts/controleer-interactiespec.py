#!/usr/bin/env python3
"""De voorbeeldpayloads in een interactiespecificatie valideren tegen hun schema's.

Waarom dit script bestaat: een interactiespecificatie belooft per eenheid een bericht met
een vorm, en toont die vorm met een voorbeeldpayload. Zolang niets die payload tegen het
schema houdt, kan de payload sleutels dragen die in geen schema staan, en leest een
leverancier een belofte die de specificatie niet waarmaakt. Npuls-OKx/Public#132 wijst die
controle aan als ontbrekend: in de gepubliceerde voorbeeldpayloads valideert het merendeel
van de sleutels tegen geen enkel schema. Dit script vangt dat.

    python3 scripts/controleer-interactiespec.py [MAP]
        [--public-schemas PAD] [--schemas PAD ...] [--kort]

MAP is de map met de interactiespecificatie; standaard
architecture/docs/specificatie/interactie-onderwijsaanbod.

De koppeling tussen een payload en haar schema
----------------------------------------------
De aanduiding staat achter de taalaanduiding van het codeblok, in de informatieregel van de
afbakening (fence). Daarmee blijft zij bij de payload staan als de tekst eromheen verandert,
en blijft het blok in elke markdown-weergave een json-blok:

    ```json schema=intake-outcome
    { "leveringId": "..." }
    ```

De waarde is de bestandsnaam van het schema zonder `.json`. Valideert een payload tegen
meerdere schema's, dan staan zij achter elkaar met een komma ertussen; dat is de vorm voor
een overlay, waar het dragende schema en de overlay samen de payload dekken:

    ```json schema=result-structure,education-design
    ```

Een json-blok zonder aanduiding is een gat: de controle kan over zo'n payload niets zeggen,
en meldt haar daarom apart van de payloads die wel een schema dragen.

Twee toetsen per payload
------------------------
De eerste toets is de validatie met jsonschema: elke payload gaat tegen elk schema dat zij
aanduidt, met de formaatcontrole aan, zodat een uuid, een datum en een versiepatroon
meekomen.

De tweede toets telt de sleutels. De schema's in Npuls-OKx/Public laten een onbekende sleutel
toe, want zij zetten `additionalProperties` niet op `false`. Een payload die een sleutel
verzint komt daarmee door de validatie heen, en dat is precies het gat dat issue #132
aanwijst: daar valideert het merendeel van de sleutels in de gepubliceerde voorbeeldpayloads
tegen geen enkel schema. De tweede toets loopt daarom de payload en haar schema's samen af en
meldt elke sleutel die geen schema verklaart. Een sleutel geldt als verklaard zodra een van de
aangeduide schema's haar in `properties` of in `patternProperties` draagt, of zodra een schema
met `additionalProperties` zegt dat de vorm open is. Bij een overlay is de som van de schema's
de maat: het dragende schema verklaart de bestaande sleutels, de overlay de nieuwe.

Waar een schema vandaan komt
----------------------------
De controle zoekt een schema eerst in de map `schemas/` van de interactiespecificatie zelf,
waar de schema's staan die deze specificatie voorstelt, en daarna in de schema's van
Npuls-OKx/Public, waar de vastgelegde schema's staan. De uitvoer noemt per payload de naam
van het schema met zijn statuslabel erachter, `vastgelegd` of `voorstel`, zodat de stand van
de grond onder die payload zichtbaar blijft.

Een verwijzing (`$ref`) tussen schema's komt langs dezelfde weg binnen: de controle leidt uit
de verwijzing de bestandsnaam af en zoekt dat bestand in dezelfde mappen. Zo werkt zowel een
verwijzing op `$id` (`https://okx.npuls.nl/schema/volume/alfa`) als een verwijzing op een
relatief pad (`./volume.json`), de twee vormen die de schema's in meta en in Public dragen.

Exitcodes
---------
0: elke payload draagt een aanduiding en valideert;
1: ten minste een payload valideert niet, draagt een sleutel die geen schema verklaart, of
   wijst een schema aan dat niet te laden is;
2: elke aangeduide payload valideert, en ten minste een payload draagt geen aanduiding;
3: de invoer is niet bruikbaar (de map ontbreekt, of het pakket jsonschema ontbreekt).
"""

import argparse
import json
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
MAP_STANDAARD = pathlib.Path("architecture/docs/specificatie/interactie-onderwijsaanbod")
PUBLIC_STANDAARD = pathlib.Path("../Public/Informatie-en-gegevensmodellen/schemas")

AFBAKENING = re.compile(r"^(?P<hek>`{3,}|~{3,})(?P<info>.*)$")
AANDUIDING = re.compile(r"\bschema=(?P<namen>[A-Za-z0-9][A-Za-z0-9_.,/-]*)")
PAYLOADTALEN = {"json", "jsonc"}


class Payload:
    """Een voorbeeldpayload uit een markdown-bestand, met de plek waar zij staat."""

    def __init__(self, bestand, regel, taal, namen, tekst):
        self.bestand = bestand
        self.regel = regel
        self.taal = taal
        self.namen = namen
        self.tekst = tekst

    @property
    def plek(self):
        """Het bestand met het regelnummer, vanaf de wortel van de repository als dat kan."""
        try:
            pad = self.bestand.resolve().relative_to(WORTEL)
        except ValueError:
            pad = self.bestand
        return f"{pad}:{self.regel}"


def lees_payloads(pad):
    """Elke payload uit de markdown-bestanden van een map halen, in leesvolgorde.

    Een codeblok telt als payload zodra zijn taalaanduiding json is. De aanduiding achter die
    taal levert de schemanamen; zonder aanduiding blijft die lijst leeg en is de payload een gat.
    """
    payloads = []
    for bestand in sorted(pad.rglob("*.md")):
        regels = bestand.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(regels):
            kop = AFBAKENING.match(regels[i])
            if not kop:
                i += 1
                continue
            hek, info = kop.group("hek"), kop.group("info").strip()
            taal = info.split()[0].lower() if info else ""
            j = i + 1
            while j < len(regels) and not regels[j].startswith(hek):
                j += 1
            if taal in PAYLOADTALEN:
                treffer = AANDUIDING.search(info)
                namen = []
                if treffer:
                    namen = [n.strip() for n in treffer.group("namen").split(",") if n.strip()]
                payloads.append(Payload(bestand, i + 1, taal, namen, "\n".join(regels[i + 1:j])))
            i = j + 1
    return payloads


def schemabestand(naam, mappen):
    """Het schemabestand bij een naam, gezocht in de meegegeven mappen op volgorde."""
    kaal = naam[:-5] if naam.endswith(".json") else naam
    kaal = kaal.strip("/").rsplit("/", 1)[-1]
    if not kaal:
        return None
    for map_ in mappen:
        kandidaat = map_ / f"{kaal}.json"
        if kandidaat.is_file():
            return kandidaat
    return None


def maak_register(mappen):
    """Een register (registry) dat een verwijzing tussen schema's naar een bestand herleidt.

    De verwijzingen in de schema's van meta en Public hebben twee vormen: een `$id` met een
    label erachter (`.../volume/alfa`) en een relatief pad (`./volume.json`). Beide eindigen op
    een segment waaruit de bestandsnaam volgt: het laatste segment, of het segment ervoor als
    het laatste het label is. Deze functie probeert die twee op volgorde.
    """
    from referencing import Registry, Resource
    from referencing.exceptions import NoSuchResource
    from referencing.jsonschema import DRAFT202012

    def haal_op(uri):
        segmenten = [s for s in uri.split("#")[0].split("/") if s]
        for kandidaat in (segmenten[-1:] or [None]) + (segmenten[-2:-1] if len(segmenten) > 1 else []):
            if not kandidaat:
                continue
            bestand = schemabestand(kandidaat, mappen)
            if bestand:
                inhoud = json.loads(bestand.read_text(encoding="utf-8"))
                return Resource.from_contents(inhoud, default_specification=DRAFT202012)
        raise NoSuchResource(ref=uri)

    return Registry(retrieve=haal_op)


def valideer(lading, schema, register):
    """De fouten die een payload tegen een schema oplevert, als leesbare regels."""
    import jsonschema

    validator = jsonschema.Draft202012Validator(
        schema, registry=register, format_checker=jsonschema.FormatChecker()
    )
    fouten = []
    try:
        gevonden = sorted(validator.iter_errors(lading), key=lambda f: list(f.absolute_path))
    except Exception as e:
        # Een verwijzing die nergens uitkomt is een bevinding en geen reden om te stoppen.
        # Dat gebeurt wanneer een schema naar Npuls-OKx/Public verwijst en die werkmap
        # ontbreekt, bijvoorbeeld op een bouwmachine die alleen meta uitcheckt.
        uri = getattr(getattr(e, "_cause", None), "ref", None) or getattr(e, "ref", None)
        waar = f": {uri}" if uri else ""
        return [f"/: verwijzing niet te herleiden{waar}; staat de werkmap "
                f"{PUBLIC_STANDAARD} ernaast?"]
    for fout in gevonden:
        plek = "/" + "/".join(str(p) for p in fout.absolute_path) if fout.absolute_path else "/"
        fouten.append(f"{plek}: {fout.message}")
    return fouten


def ontvouw(groep):
    """Elk subschema dat op dezelfde plek in de payload geldt, achter verwijzingen aan.

    Een verwijzing (`$ref`), een `allOf`, een `anyOf`, een `oneOf` en de takken van een
    voorwaarde gelden allemaal op de plek waar zij staan. De sleutels die zij verklaren tellen
    daarom samen.
    """
    uit, gezien, stapel = [], set(), list(groep)
    while stapel:
        schema, resolver = stapel.pop()
        if not isinstance(schema, dict) or id(schema) in gezien:
            continue
        gezien.add(id(schema))
        uit.append((schema, resolver))
        if "$ref" in schema:
            try:
                opgelost = resolver.lookup(schema["$ref"])
            except Exception:
                opgelost = None
            if opgelost is not None:
                stapel.append((opgelost.contents, opgelost.resolver))
        for naam in ("allOf", "anyOf", "oneOf"):
            for tak in schema.get(naam) or []:
                stapel.append((tak, resolver))
        for naam in ("if", "then", "else"):
            if isinstance(schema.get(naam), dict):
                stapel.append((schema[naam], resolver))
        for tak in (schema.get("dependentSchemas") or {}).values():
            stapel.append((tak, resolver))
    return uit


def _dek_object(lading, groep, pad, ongedekt):
    """De sleutels van een object langs de schema's die daar gelden."""
    open_vorm = any(
        schema.get(naam) not in (None, False)
        for schema, _ in groep
        for naam in ("additionalProperties", "unevaluatedProperties")
        if naam in schema
    )
    for sleutel, waarde in lading.items():
        kind = []
        for schema, resolver in groep:
            eigenschappen = schema.get("properties") or {}
            if sleutel in eigenschappen:
                kind.append((eigenschappen[sleutel], resolver))
            for patroon, sub in (schema.get("patternProperties") or {}).items():
                if re.search(patroon, sleutel):
                    kind.append((sub, resolver))
            extra = schema.get("additionalProperties")
            if isinstance(extra, dict) and sleutel not in eigenschappen:
                kind.append((extra, resolver))
        if not kind and not open_vorm:
            ongedekt.append(f"{pad}/{sleutel}")
            continue
        dek(waarde, kind, f"{pad}/{sleutel}", ongedekt)


def _dek_array(lading, groep, pad, ongedekt):
    """De elementen van een array langs de schema's die daar gelden."""
    for index, waarde in enumerate(lading):
        kind = []
        for schema, resolver in groep:
            voorste = schema.get("prefixItems") or []
            if index < len(voorste):
                kind.append((voorste[index], resolver))
            elif isinstance(schema.get("items"), dict):
                kind.append((schema["items"], resolver))
        dek(waarde, kind, f"{pad}/{index}", ongedekt)


def dek(lading, groep, pad, ongedekt):
    """Elke sleutel in een payload die geen schema verklaart in `ongedekt` zetten."""
    groep = ontvouw(groep)
    if isinstance(lading, dict):
        _dek_object(lading, groep, pad, ongedekt)
    elif isinstance(lading, list):
        _dek_array(lading, groep, pad, ongedekt)


def ongedekte_sleutels(lading, schemas, register):
    """De sleutels in een payload die geen van de meegegeven schema's verklaart."""
    groep = [(schema, register.resolver(base_uri=str(schema.get("$id", "")))) for schema in schemas]
    ongedekt = []
    dek(lading, groep, "", ongedekt)
    return ongedekt


def controleer(pad, mappen):
    """Elke payload in een interactiespecificatie langs haar schema's halen.

    Levert de uitkomst per payload, de payloads zonder aanduiding en de bevindingen.
    """
    uitkomsten, gaten, bevindingen = [], [], []
    register = maak_register(mappen)
    for payload in lees_payloads(pad):
        if not payload.namen:
            gaten.append(payload)
            continue
        try:
            lading = json.loads(payload.tekst)
        except json.JSONDecodeError as fout:
            bevindingen.append(f"{payload.plek}: de payload is geen geldige json ({fout})")
            uitkomsten.append((payload, ",".join(payload.namen), "onleesbaar"))
            continue
        schemas = []
        for naam in payload.namen:
            bestand = schemabestand(naam, mappen)
            if bestand is None:
                bevindingen.append(
                    f"{payload.plek}: schema {naam} staat in geen van de schemamappen"
                )
                uitkomsten.append((payload, naam, "schema ontbreekt"))
                continue
            try:
                schema = json.loads(bestand.read_text(encoding="utf-8"))
            except json.JSONDecodeError as fout:
                bevindingen.append(f"{payload.plek}: schema {bestand} is geen geldige json ({fout})")
                uitkomsten.append((payload, naam, "schema onleesbaar"))
                continue
            schemas.append(schema)
            fouten = valideer(lading, schema, register)
            label = f"{naam} ({etiket(schema)})"
            if fouten:
                for regel in fouten:
                    bevindingen.append(f"{payload.plek} tegen {naam}: {regel}")
                uitkomsten.append((payload, label, "valideert niet"))
            else:
                uitkomsten.append((payload, label, "valideert"))
        for sleutel in ongedekte_sleutels(lading, schemas, register) if schemas else []:
            bevindingen.append(
                f"{payload.plek}: sleutel {sleutel} staat in geen van de schema's "
                f"{', '.join(payload.namen)}"
            )
    return uitkomsten, gaten, bevindingen


def etiket(schema):
    """Het statuslabel uit de `$id` van een schema: vastgelegd bij alfa, voorstel bij voorstel."""
    staart = str(schema.get("$id", "")).rstrip("/").rsplit("/", 1)[-1]
    return {"alfa": "vastgelegd", "voorstel": "voorstel"}.get(staart, staart or "zonder label")


def rapporteer(uitkomsten, gaten, bevindingen, kort):
    """De uitkomst per payload, de gaten en de bevindingen naar de uitvoer schrijven."""
    if not kort:
        print("Payloads en hun schema")
        for payload, naam, stand in uitkomsten:
            print(f"  {payload.plek}  {naam}  {stand}")
        print()
    if gaten:
        print("Payloads zonder schema-aanduiding")
        for payload in gaten:
            print(f"  {payload.plek}  geen aanduiding achter de taal van het codeblok")
        print()
    if bevindingen:
        print("Bevindingen")
        for regel in bevindingen:
            print(f"  {regel}")
        print()
    geldig = sum(1 for _, _, stand in uitkomsten if stand == "valideert")
    met_schema = {payload.plek for payload, _, _ in uitkomsten}
    print(
        f"Payloads: {len(met_schema) + len(gaten)}; "
        f"met schema: {len(met_schema)}; zonder schema: {len(gaten)}; "
        f"toetsen tegen een schema: {len(uitkomsten)}, waarvan geldig {geldig}; "
        f"bevindingen: {len(bevindingen)}"
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("map", nargs="?", default=None, help="de map met de interactiespecificatie")
    parser.add_argument(
        "--schemas", action="append", default=None,
        help="extra map met schema's, voor de map schemas/ van de specificatie"
    )
    parser.add_argument(
        "--public-schemas", default=None,
        help="de schemamap van Npuls-OKx/Public; standaard ../Public/Informatie-en-gegevensmodellen/schemas"
    )
    parser.add_argument("--kort", action="store_true", help="alleen de gaten, de bevindingen en de telling")
    args = parser.parse_args(argv)

    try:
        import jsonschema  # noqa: F401
        import referencing  # noqa: F401
    except ImportError:
        print("Het pakket jsonschema ontbreekt; installeer het in de dev-container.", file=sys.stderr)
        return 3

    pad = pathlib.Path(args.map) if args.map else WORTEL / MAP_STANDAARD
    if not pad.is_dir():
        print(f"De map {pad} bestaat niet.", file=sys.stderr)
        return 3

    mappen = [pathlib.Path(m) for m in (args.schemas or [])]
    eigen = pad / "schemas"
    if eigen.is_dir() and eigen not in mappen:
        mappen.append(eigen)
    public = pathlib.Path(args.public_schemas) if args.public_schemas else WORTEL / PUBLIC_STANDAARD
    if public.is_dir():
        mappen.append(public)
    else:
        print(f"De schemamap van Public staat niet op {public}; de vastgelegde schema's blijven buiten de controle.")
    if not mappen:
        print("Geen enkele schemamap is gevonden.", file=sys.stderr)
        return 3

    uitkomsten, gaten, bevindingen = controleer(pad, mappen)
    # Een verwijzing die nergens uitkomt zegt niets over de payload: zij zegt dat de
    # vastgelegde schema's ontbreken. Zo n uitkomst is geen oordeel, en daarom eindigt de
    # controle dan met de code voor niet uitvoerbaar in plaats van met die voor afgekeurd.
    onherleidbaar = [b for b in bevindingen if "verwijzing niet te herleiden" in str(b)]
    if onherleidbaar and not public.is_dir():
        print(f"\n{len(onherleidbaar)} van de {len(bevindingen)} bevindingen komen voort uit "
              f"een verwijzing die zonder {public} nergens uitkomt. Deze controle geeft daarmee "
              f"geen oordeel; zet Npuls-OKx/Public ernaast en draai opnieuw.", file=sys.stderr)
        return 3
    rapporteer(uitkomsten, gaten, bevindingen, args.kort)
    if bevindingen:
        return 1
    if gaten:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
