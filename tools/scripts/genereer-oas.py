#!/usr/bin/env python3
"""Per applicatiecomponent een OpenAPI 3.1-document schrijven uit de interactiespecificatie.

Waarom dit script bestaat: een interactiespecificatie draagt per eenheid de operaties met hun
pad, methode, parameters en statuscodes, en de schema's waartegen de berichten valideren. Dat
is alles wat in een OpenAPI-document staat, en een leverancier die dat document krijgt
genereert er een client of een server uit in plaats van de tabellen over te typen. Een
OpenAPI-document dat met de hand naast de specificatie wordt bijgehouden loopt binnen een
ronde uit de pas, en dan dragen twee bestanden twee waarheden. Daarom wordt het gegenereerd,
zoals de platen uit het model komen. Relateert aan: Npuls-OKx/meta#374.

    python3 tools/scripts/genereer-oas.py [--operaties PAD] [--uit MAP]
        [--public-schemas PAD] [--component NAAM] [--alles] [--kort]

Zonder argumenten leest het script
architecture/docs/specificatie/interactie-onderwijsaanbod/operaties.json en schrijft het de
documenten naar de map `oas/` daarnaast, elk component in twee vormen.

Twee vormen, een waarheid
-------------------------
De OpenAPI-specificatie laat JSON en YAML beide toe. Het script schrijft ze beide uit dezelfde
generatorronde, dus zij kunnen niet uiteenlopen, en laadt de YAML terug om dat aan te tonen:
leest zij niet terug als hetzelfde document, dan is dat een bevinding.

De **YAML-vorm is normatief**. Dat is de vorm die gangbaar is voor een OpenAPI-document, die
een mens leest en die de overlay-structuur van OEAPI aanhoudt (`profile.yaml`,
`source/spec.yaml`). De JSON-vorm staat ernaast voor de keuring, de testgevallen en een
werktuig dat geen YAML leest.

Bekijken doet `tools/scripts/bekijk-oas.py`: GitHub rendert een OpenAPI-document niet, en in de
bestandsweergave is een koppelvlak van negen paden met dertig schema's niet te overzien.

Waar de operaties vandaan komen
-------------------------------
Uit `operaties.json`. De zes operatietabellen in de verdiepingsbestanden dragen zes
verschillende koprijen: geen enkele kolom staat in alle zes op dezelfde plek, het component
staat in vijf verschillende vormen, en de kolom met het verzoek- of antwoordschema bestaat
nergens. Juist die velden bepalen in welk document een operatie landt
en met welk contract. Een lezer die de markdown leest mist dat niet, want de tekst eronder
vult het aan; een generator die hem leest vraagt zes parsers, en elke redactieronde op een
tabel kan er een zevende van maken. `operaties.json` zet die vier velden daarom een laag
dieper, in de vorm waarin zij regelmatig staan. Het bestand zegt zelf in `bron` dat het de
bron is voor de documenten hier, en dat de operatietabel voorlopig de bron blijft voor de
lezer; die tabel uit dit bestand laten komen is de vervolgstap.

De voorbeeldpayloads blijven wel in de markdown staan. De afbakening (fence) draagt daar al
de aanduiding `schema=`, zij is de enige machineleesbare binding die er al ligt, en
`tools/scripts/controleer-interactiespec.py` valideert haar daar. Een verwijzing in
`operaties.json` wijst een payload aan op bestand, schemanaam en volgnummer, zodat de payload
op een plek blijft staan.

Een document per component, en wat daarin staat
-----------------------------------------------
Een OpenAPI-document beschrijft de API van een component. De operaties van deze
interactiespecificatie verdelen zich over vijf componenten, dus worden het vijf documenten.
Het script schrijft alleen een document voor een component dat in `operaties.json` op
`afgerond` staat: elke stroom waarin dat component voorkomt staat dan in het bestand. Een
half document is minder waard dan geen, want een leverancier leest de leegte als een keuze.
`--alles` schrijft ook de onvolledige documenten, voor wie de vorm wil zien.

`paths` draagt de aanroepen die het component serveert. `webhooks` draagt de meldingen die
het component verstuurt: OpenAPI 3.1 beschrijft daar de aanroep die buiten een eigen aanroep
om binnenkomt bij wie zich erop abonneert, en `/abonnementen` is precies die registratie.
Een melding die het component zelf ontvangt staat niet in `paths`, want zij komt aan op het
afleveradres dat de ontvanger bij de melder registreert en dat geen pad in dit document is.
Zij staat daarom onder `x-okx-ontvangen-meldingen`, met de melder, het payloadschema en de
stand erbij, zodat de bouwer van dit component ziet welke verwerkers hij maakt. De vorm van
zo'n melding staat onder `webhooks` in het document van de melder.

De schema's gaan ongewijzigd mee, op de bundeling na
----------------------------------------------------
OpenAPI 3.1 gebruikt JSON Schema 2020-12 als dialect, en dat is wat de schema's dragen. Er
wordt dus niets geconverteerd: geen `nullable`, geen `$ref` die alleen mag staan. Wat de
bundeling wel verandert, staat per schema in `x-okx-schemas` en in de uitvoer van dit script:

| Wat | Waarom |
|---|---|
| `$schema` eruit | Die sleutel hoort op de wortel van een schemabron; in de bundel is dat de wortel van het document, en `jsonSchemaDialect` draagt de waarde daar |
| `$id` eruit, bewaard in `x-okx-schemas` | De `$id`-waarden wijzen naar `https://okx.npuls.nl/schema/...` en die resolven niet. Een `$id` die blijft staan zou bovendien het grondadres (base URI) verzetten, waarmee een verwijzing naar `#/components/schemas/...` binnen dat schema nergens meer uitkomt |
| `$ref` naar een ander schema wordt `#/components/schemas/<naam>` | Daarmee staat elk document op zichzelf. Dit raakt beide vormen die de schema's dragen: de absolute `$id` in meta en het relatieve pad in Public |
| `$ref` naar een eigen `$defs` schuift mee | Zonder `$id` rekent zo'n verwijzing vanaf de wortel van het document, dus wordt `#/$defs/x` hier `#/components/schemas/<naam>/$defs/x` |

De stand van een schema volgt uit het laatste deel van zijn `$id`: `alfa` staat in
Npuls-OKx/Public en geldt als vastgelegd, `voorstel` wordt door deze specificatie
voorgesteld.

Wat de specificatie als voorstel draagt, draagt dat ook in het document
-----------------------------------------------------------------------
Een stand is in deze specificatie zelden een enkel woord: vierentwintig van de
vijfendertig rijen kwalificeren een onderdeel van de operatie ("vastgelegd, met de parameter
leeruitkomstId als voorstel"). Juist die kwalificatie is wat een leverancier nodig heeft, dus
draagt elke operatie, parameter en respons drie velden: `x-okx-stand` met `vastgelegd` of
`voorstel`, `x-okx-stand-kwalificatie` met de zin erachter, en `x-okx-werkbrieven` met de
nummers die het beleggen. Dezelfde zin staat ook in `description`, want een mens leest de
beschrijving en niet de eigen velden.

Elke verdieping nummert haar eigen reeks werkbrieven, dus staat W15 van IS-OA-01 naast een
andere W15 van IS-OA-03. Een code draagt in het document daarom haar stroom erbij, en
`x-okx-werkbrieven` op de wortel draagt de legenda: per aangehaalde code wat erbij moet, waar
het landt en de versie-impact, gelezen uit de werkbrieftabel van de verdieping. Zonder die
legenda wijst een code nergens heen voor wie alleen dit document leest, en juist die codes
verbinden een voorstel aan wat er in Public moet landen.

Twee controles die het script zelf afleidt
------------------------------------------
Een abonnementsoperatie draagt een gesloten lijst met de meldingssoorten die te bestellen zijn.
Publiceert het document een melding die buiten die lijst valt, dan is zij voor een gegenereerde
client onbereikbaar: de client leest de lijst, en de proza eronder blijft buiten beeld. Draagt
de lijst een soort waarvoor deze specificatie nergens een vorm legt, dan bestelt een client
iets waarvan het lichaam onbekend is. Beide verschillen komen uit het document zelf en staan in
`x-okx-openstaand`, ook wanneer de verdieping ze al in een werkbrief belegt. Daarnaast meldt
het script een werkbriefcode die bij een operatie staat en wiens tekst in de verdiepingen niet
te vinden is.

Wat niet geplaatst kon worden
-----------------------------
Een gat is geen succes. Het script meldt per document welke respons geen schema draagt, welke
payload geen voorbeeld heeft, welke verwijzing nergens uitkomt en welke operatie met een
andere samenviel. Een plaatshouder draagt zijn eigen reden in zijn `description`, zodat ook de
lezer van het document ziet dat de keuze openstaat.

De controle achteraf
--------------------
Elke `example` in het gegenereerde document gaat tegen het schema waar zij onder staat, elke
`$ref` wordt opgezocht in het document zelf, en het geheel gaat door
`openapi-spec-validator` zodra dat pakket er is.

Exitcodes
---------
0: elk gevraagd document is geschreven en er staat niets open;
1: ten minste een voorbeeld valideert niet, een verwijzing komt nergens uit, een document is
   geen geldige OpenAPI, of twee operaties op hetzelfde pad spreken elkaar tegen;
2: elk gevraagd document is geschreven en er staat iets open;
3: de invoer is niet bruikbaar.
"""

import argparse
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent
SPECIFICATIE_STANDAARD = pathlib.Path(
    "architecture/docs/specificatie/interactie-onderwijsaanbod"
)
PUBLIC_STANDAARD = pathlib.Path("../Public/Informatie-en-gegevensmodellen/schemas")
UIT_STANDAARD = "oas"

AFBAKENING = re.compile(r"^(?P<hek>`{3,}|~{3,})(?P<info>.*)$")
AANDUIDING = re.compile(r"\bschema=(?P<namen>[A-Za-z0-9][A-Za-z0-9_.,/-]*)")
PAYLOADTALEN = {"json", "jsonc"}

OPENAPI_VERSIE = "3.1.0"
DIALECT = "https://json-schema.org/draft/2020-12/schema"
BASIS_URI = "urn:okx:oas"
STAND_PER_LABEL = {"alfa": "vastgelegd", "voorstel": "voorstel"}


class Gat:
    """Iets dat het script niet kon plaatsen, met de plek waar het hoort."""

    def __init__(self, waar, wat):
        self.waar = waar
        self.wat = wat

    def __str__(self):
        return f"{self.waar}: {self.wat}"


class Bevinding(Gat):
    """Iets dat niet klopt: een voorbeeld dat niet valideert, een verwijzing die nergens uitkomt."""


# --------------------------------------------------------------------------- de voorbeelden


def lees_fences(map_):
    """Per markdown-bestand de json-afbakeningen (fences) met hun schemanamen, in leesvolgorde.

    De aanduiding staat achter de taalaanduiding van het codeblok, zoals
    `schema=intake-outcome`. Draagt een payload meerdere schema's, dan staan zij achter elkaar
    met een komma ertussen; de payload telt dan mee bij elk van die namen.
    """
    per_bestand = {}
    for bestand in sorted(map_.glob("*.md")):
        regels = bestand.read_text(encoding="utf-8").splitlines()
        gevonden = []
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
                gevonden.append({
                    "regel": i + 1,
                    "namen": namen,
                    "tekst": "\n".join(regels[i + 1:j]),
                })
            i = j + 1
        per_bestand[bestand.name] = gevonden
    return per_bestand


WERKBRIEFRIJ = re.compile(r"^\|\s*(W\d+|WB-\d+)\s*\|(.+)\|\s*$")


def lees_werkbrieven(map_, stromen):
    """Per stroom de werkbrieven uit haar verdiepingsbestand, met hun code als sleutel.

    Een werkbrief zegt wat deze eenheid in Npuls-OKx/Public vraagt bovenop wat daar ligt, en de
    operaties verwijzen ernaar met hun code. Elke verdieping nummert haar eigen reeks, dus staat
    W15 van IS-OA-01 naast een andere W15 van IS-OA-03. De sleutel draagt daarom de stroom erbij.
    Zonder deze legenda wijst een code in het document nergens heen, en juist die codes verbinden
    een voorstel aan wat er in Public moet landen.
    """
    uit = {}
    for stroom, gegeven in stromen.items():
        bestand = map_ / gegeven["bestand"]
        if not bestand.is_file():
            continue
        for regel in bestand.read_text(encoding="utf-8").splitlines():
            treffer = WERKBRIEFRIJ.match(regel)
            if not treffer:
                continue
            delen = [d.strip() for d in treffer.group(2).split("|")]
            if len(delen) != 3:
                continue
            uit[f"{stroom} {treffer.group(1)}"] = {
                "wat": delen[0],
                "waar": delen[1],
                "versie-impact": delen[2],
                "x-okx-stroom": stroom,
            }
    return uit


def kwalificeer(operatie):
    """Elke werkbriefcode in een operatie voorzien van haar stroom, want de reeksen botsen.

    De operatie komt er als kopie uit, zodat het ingelezen bestand ongemoeid blijft wanneer
    dezelfde operatie in meer dan een stroom staat.
    """
    stroom = operatie.get("stroom")
    if not stroom:
        return operatie

    def loop(knoop, in_stand=False):
        if isinstance(knoop, dict):
            uit = {}
            for sleutel, waarde in knoop.items():
                if in_stand and sleutel == "werkbrieven" and isinstance(waarde, list):
                    uit[sleutel] = [f"{stroom} {code}" for code in waarde]
                else:
                    uit[sleutel] = loop(waarde, in_stand or sleutel == "stand")
            return uit
        if isinstance(knoop, list):
            return [loop(item, in_stand) for item in knoop]
        return knoop

    return loop(operatie)


def haal_voorbeeld(verwijzing, fences, waar, gaten):
    """De payload achter een voorbeeldverwijzing, als lading plus de plek waar zij staat."""
    bestand = verwijzing.get("bestand")
    naam = verwijzing.get("schema")
    nummer = verwijzing.get("nummer", 1)
    treffers = [f for f in fences.get(bestand, []) if naam in f["namen"]]
    if len(treffers) < nummer:
        gaten.append(Gat(
            waar,
            f"voorbeeld {nummer} met schema {naam} staat niet in {bestand}; "
            f"dat bestand draagt er {len(treffers)}",
        ))
        return None
    fence = treffers[nummer - 1]
    try:
        lading = json.loads(fence["tekst"])
    except json.JSONDecodeError as fout:
        gaten.append(Bevinding(waar, f"de payload in {bestand}:{fence['regel']} is geen json: {fout}"))
        return None
    return {"lading": lading, "plek": f"{bestand}:{fence['regel']}", "schema": naam}


# ------------------------------------------------------------------------------- de schema's


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


def naam_uit_verwijzing(ref):
    """De schemanaam uit een verwijzing, voor de twee vormen die de schema's dragen.

    Een `$id`-verwijzing eindigt op een label (`.../volume/alfa`), een relatieve verwijzing op
    een bestandsnaam (`./volume.json`). De naam is het laatste segment zonder `.json`, of het
    segment ervoor als het laatste een label is.
    """
    zonder_fragment = ref.split("#")[0]
    segmenten = [s for s in zonder_fragment.split("/") if s and s not in (".", "..")]
    if not segmenten:
        return None
    laatste = segmenten[-1]
    if laatste.endswith(".json"):
        return laatste[:-5]
    if laatste in STAND_PER_LABEL and len(segmenten) > 1:
        return segmenten[-2]
    return laatste


def stand_uit_id(schema_id):
    """De stand van een schema, afgeleid uit het laatste deel van zijn `$id`."""
    if not schema_id:
        return None
    return STAND_PER_LABEL.get(schema_id.rstrip("/").rsplit("/", 1)[-1])


def herschrijf(knoop, naam, verwijzingen):
    """Een schema klaarmaken voor de bundel, met de wijzigingen in `verwijzingen` erbij.

    Een verwijzing naar een ander schema wordt een verwijzing binnen het document, en een
    verwijzing naar een eigen `$defs` schuift mee naar de plek die het schema in de bundel
    krijgt. Alle overige sleutels blijven staan, op hun eigen plek en in hun eigen volgorde.
    """
    if isinstance(knoop, list):
        return [herschrijf(item, naam, verwijzingen) for item in knoop]
    if not isinstance(knoop, dict):
        return knoop
    uit = {}
    for sleutel, waarde in knoop.items():
        if sleutel == "$ref" and isinstance(waarde, str):
            if waarde.startswith("#/"):
                nieuw = f"#/components/schemas/{naam}/{waarde[2:]}"
                verwijzingen.append((waarde, nieuw))
            elif waarde.startswith("#"):
                nieuw = waarde
                verwijzingen.append((waarde, "niet verplaatst: een anker, geen pointer"))
            else:
                doel = naam_uit_verwijzing(waarde)
                nieuw = f"#/components/schemas/{doel}"
                verwijzingen.append((waarde, nieuw))
            uit[sleutel] = nieuw
        else:
            uit[sleutel] = herschrijf(waarde, naam, verwijzingen)
    return uit


def bundel_schema(naam, mappen, gaten):
    """Een schema inlezen en klaarmaken voor `components/schemas`, met zijn herkomst erbij."""
    bestand = schemabestand(naam, mappen)
    if bestand is None:
        gaten.append(Bevinding("components/schemas", f"het schema {naam} staat in geen enkele schemamap"))
        return None
    origineel = json.loads(bestand.read_text(encoding="utf-8"))
    schema_id = origineel.get("$id")
    verwijzingen = []
    inhoud = {s: w for s, w in origineel.items() if s not in ("$id", "$schema")}
    inhoud = herschrijf(inhoud, naam, verwijzingen)
    verplaatst = [v for v in verwijzingen if not v[1].startswith("niet verplaatst")]
    gelaten = [v for v in verwijzingen if v[1].startswith("niet verplaatst")]
    for oud, reden in gelaten:
        gaten.append(Gat(f"components/schemas/{naam}", f"de verwijzing {oud} is {reden}"))
    herkomst = {
        "schemaId": schema_id,
        "stand": stand_uit_id(schema_id),
        "bestand": str(bestand).replace(str(WORTEL) + "/", ""),
        "gewijzigd": _gewijzigd(origineel, verplaatst),
        "verwijst_naar": sorted({
            naam_uit_verwijzing(oud) for oud, _ in verplaatst if not oud.startswith("#")
        }),
    }
    if herkomst["stand"] is None:
        gaten.append(Gat(
            f"components/schemas/{naam}",
            f"de stand volgt niet uit de $id {schema_id!r}; het laatste deel is geen label",
        ))
    return {"inhoud": inhoud, "herkomst": herkomst}


def _gewijzigd(origineel, verplaatst):
    """Wat de bundeling aan een schema veranderde, als leesbare lijst."""
    uit = []
    if "$schema" in origineel:
        uit.append("$schema eruit, het document draagt de dialect in jsonSchemaDialect")
    if "$id" in origineel:
        uit.append("$id eruit, bewaard als schemaId hier")
    if verplaatst:
        uit.append(f"{len(verplaatst)} verwijzingen naar het document verplaatst")
    return uit or ["niets, het schema staat hier zoals in zijn bestand"]


def verzamel_schemas(namen, mappen, gaten):
    """De gevraagde schema's met alles waar zij naar verwijzen, als bundel voor een document."""
    bundel = {}
    te_doen = sorted(set(namen))
    while te_doen:
        naam = te_doen.pop(0)
        if naam in bundel:
            continue
        gebundeld = bundel_schema(naam, mappen, gaten)
        if gebundeld is None:
            continue
        bundel[naam] = gebundeld
        for volgende in gebundeld["herkomst"]["verwijst_naar"]:
            if volgende and volgende not in bundel:
                te_doen.append(volgende)
    return dict(sorted(bundel.items()))


# ------------------------------------------------------------------------------- het document


def stand_velden(stand):
    """De drie `x-okx`-velden bij een stand, zodat de kwalificatie niet verdwijnt."""
    if not stand:
        return {}
    uit = {}
    if stand.get("kern"):
        uit["x-okx-stand"] = stand["kern"]
    if stand.get("kwalificatie"):
        uit["x-okx-stand-kwalificatie"] = stand["kwalificatie"]
    if stand.get("werkbrieven"):
        uit["x-okx-werkbrieven"] = list(stand["werkbrieven"])
    return uit


def stand_zin(stand):
    """De stand als zin voor een `description`, want een mens leest de beschrijving."""
    if not stand or not stand.get("kern"):
        return ""
    zin = f"Stand: {stand['kern']}"
    if stand.get("kwalificatie"):
        zin += f", {stand['kwalificatie']}"
    zin += "."
    if stand.get("werkbrieven"):
        zin += f" Werkbrief: {', '.join(stand['werkbrieven'])}."
    return zin


def samen(*delen):
    """De gevulde delen van een beschrijving achter elkaar, met een witregel ertussen."""
    return "\n\n".join(d.strip() for d in delen if d and d.strip())


def parameter_object(parameter, waar, gaten):
    """Een parameter uit `operaties.json` als OpenAPI-parameter."""
    omschrijving = parameter.get("omschrijving", "")
    if parameter.get("gat"):
        gaten.append(Gat(f"{waar}, parameter {parameter['naam']}", parameter["gat"]))
        omschrijving = samen(omschrijving, f"Hier staat iets open: {parameter['gat']}")
    uit = {
        "name": parameter["naam"],
        "in": parameter["plaats"],
        "required": bool(parameter.get("verplicht")),
        "description": samen(omschrijving, stand_zin(parameter.get("stand"))),
        "schema": parameter.get("type", {"type": "string"}),
    }
    uit.update(stand_velden(parameter.get("stand")))
    return uit


def inhoud_object(blok, waar, fences, gaten, schemas_gevraagd):
    """Het `content`-blok bij een verzoek of een respons, met de voorbeelden erbij.

    Draagt een bericht een overlay, dan geldt het dragende schema en de overlay samen, en dat
    is in OpenAPI een `allOf` van beide. De specificatie zet die twee naast elkaar achter
    `schema=` op de afbakening van haar voorbeeldpayload; die payload gaat hier tegen dezelfde
    twee.
    """
    if blok.get("lijst_van"):
        schemas_gevraagd.add(blok["lijst_van"])
        schema = {"type": "array", "items": {"$ref": f"#/components/schemas/{blok['lijst_van']}"}}
    elif blok.get("schema"):
        schemas_gevraagd.add(blok["schema"])
        schema = {"$ref": f"#/components/schemas/{blok['schema']}"}
    else:
        return None
    if blok.get("overlay"):
        for naam in blok["overlay"]:
            schemas_gevraagd.add(naam)
        schema = {"allOf": [schema] + [
            {"$ref": f"#/components/schemas/{naam}"} for naam in blok["overlay"]
        ]}
    voorbeelden = {}
    for sleutel in ("voorbeeld", "tweede_voorbeeld"):
        if not blok.get(sleutel):
            continue
        gevonden = haal_voorbeeld(blok[sleutel], fences, waar, gaten)
        if gevonden is None:
            continue
        voorbeelden[f"voorbeeld-{len(voorbeelden) + 1}"] = {
            "summary": f"Uit {gevonden['plek']}",
            "value": gevonden["lading"],
        }
    media = {"schema": schema}
    if voorbeelden:
        media["examples"] = voorbeelden
    return {"application/json": media}


def antwoorden_object(operatie, waar, fences, gaten, schemas_gevraagd):
    """De `responses` bij een operatie, met een gat per respons zonder schema."""
    uit = {}
    for antwoord in operatie.get("antwoorden", []):
        code = str(antwoord["code"])
        omschrijving = antwoord.get("omschrijving", "")
        if antwoord.get("gat"):
            gaten.append(Gat(f"{waar}, respons {code}", antwoord["gat"]))
            omschrijving = samen(omschrijving, f"Hier staat iets open: {antwoord['gat']}")
        elif antwoord.get("zonder_lichaam"):
            # Een respons zonder lichaam is geen gat zodra de specificatie dat zo bedoelt, zoals
            # bij de bevestiging van een melding. Alleen de reden gaat mee in de beschrijving.
            omschrijving = samen(omschrijving, antwoord["zonder_lichaam"])
        elif not antwoord.get("schema") and not antwoord.get("lijst_van"):
            gaten.append(Gat(
                f"{waar}, respons {code}",
                "de specificatie noemt geen antwoordlichaam, dus draagt deze respons geen schema",
            ))
        object_ = {"description": samen(omschrijving, stand_zin(antwoord.get("stand")))}
        inhoud = inhoud_object(antwoord, f"{waar}, respons {code}", fences, gaten, schemas_gevraagd)
        if inhoud:
            object_["content"] = inhoud
        object_.update(stand_velden(antwoord.get("stand")))
        uit[code] = object_
    return uit


def verzoek_object(operatie, waar, fences, gaten, schemas_gevraagd):
    """De `requestBody` bij een operatie, met de voorgestelde vorm ernaast als die er is."""
    verzoek = operatie.get("verzoek")
    if not verzoek:
        return None
    omschrijving = verzoek.get("omschrijving", "")
    if verzoek.get("gat"):
        gaten.append(Gat(f"{waar}, verzoek", verzoek["gat"]))
        omschrijving = samen(omschrijving, f"Hier staat iets open: {verzoek['gat']}")
    inhoud = inhoud_object(verzoek, f"{waar}, verzoek", fences, gaten, schemas_gevraagd)
    if inhoud is None:
        return None
    uit = {"required": True, "description": omschrijving, "content": inhoud}
    voorstel = verzoek.get("voorstel_vorm")
    if voorstel:
        gaten.append(Gat(
            f"{waar}, verzoek",
            f"twee vormen voor een bericht: {verzoek['schema']} staat vastgelegd en "
            f"{voorstel['schema']} wordt voorgesteld; de keuze staat open",
        ))
        voorstel_inhoud = inhoud_object(
            voorstel, f"{waar}, verzoek op voorstel", fences, gaten, schemas_gevraagd
        )
        uit["x-okx-voorstel-vorm"] = {
            "description": samen(voorstel.get("omschrijving", ""), stand_zin(voorstel.get("stand"))),
            "content": voorstel_inhoud,
            **stand_velden(voorstel.get("stand")),
        }
    return uit


def operatie_object(operatie, fences, gaten, schemas_gevraagd, herkomst):
    """Een operatie uit `operaties.json` als OpenAPI-operatie.

    De beschrijving komt er pas later in, met `maak_beschrijving`: een operatie die in meer dan
    een stroom staat wordt eerst samengevoegd, en haar beschrijving volgt daarna uit de
    samengevoegde stand in een keer. Anders zou zij de samenvatting per stroom herhalen.
    """
    waar = operatie["id"]
    uit = {
        "summary": operatie.get("samenvatting", waar),
        "operationId": operatie_id(operatie),
        "x-okx-stroom": operatie.get("stroom"),
        "x-okx-herkomst": herkomst,
        "_delen": {
            "standen": [(operatie["stroom"], operatie.get("stand", {}).get("kwalificatie"))],
            "foutgedrag": [operatie.get("foutgedrag")],
            "diensten": [operatie.get("dienst")],
        },
    }
    uit.update(stand_velden(operatie.get("stand")))
    parameters = [
        parameter_object(p, waar, gaten) for p in operatie.get("parameters", [])
    ]
    if parameters:
        uit["parameters"] = parameters
    verzoek = verzoek_object(operatie, waar, fences, gaten, schemas_gevraagd)
    if verzoek:
        uit["requestBody"] = verzoek
    uit["responses"] = antwoorden_object(operatie, waar, fences, gaten, schemas_gevraagd)
    return uit


def operatie_id(operatie):
    """Een `operationId` die uit het pad of de meldingsnaam volgt, en niet uit een rijnummer."""
    if operatie["soort"] == "melding":
        return f"melding-{operatie['melding']}"
    deel = operatie["pad"].strip("/").replace("/", "-").replace("{", "").replace("}", "")
    return f"{operatie['methode']}-{deel}"


def maak_beschrijving(object_):
    """De beschrijving van een operatie, een keer, uit de delen die zij verzamelde.

    Een operatie die uit meer dan een stroom komt draagt de stand per stroom, en elke zin over
    het foutgedrag een keer. Zo blijft de beschrijving even lang als wat zij toevoegt.
    """
    delen = object_.pop("_delen")
    stand = object_.get("x-okx-stand")
    regels = []
    if stand:
        meervoudig = len([s for s in delen["standen"] if s[1]]) > 1
        kwalificaties = []
        for stroom, kwalificatie in delen["standen"]:
            if not kwalificatie:
                continue
            kwalificaties.append(f"{kwalificatie} ({stroom})" if meervoudig else kwalificatie)
        zin = f"Stand: {stand}"
        if kwalificaties:
            zin += ", " + "; ".join(kwalificaties)
        regels.append(zin + ".")
    if object_.get("x-okx-werkbrieven"):
        regels.append(f"Werkbrief: {', '.join(object_['x-okx-werkbrieven'])}.")
    foutgedrag = [f for f in dict.fromkeys(delen["foutgedrag"]) if f]
    if foutgedrag:
        regels.append("Foutgedrag: " + " ".join(foutgedrag))
    diensten = [d for d in dict.fromkeys(delen["diensten"]) if d]
    if diensten:
        regels.append(f"Dienst: {', '.join(diensten)}.")
    regels.append(f"Herkomst: {', '.join(object_['x-okx-herkomst'])}.")
    object_["description"] = "\n\n".join(regels)
    return object_


def fijnste(een, ander):
    """Van twee schema's het schema dat het andere als overlay omvat, of None.

    Een bericht met een overlay staat hier als `allOf` van het dragende schema en de overlay.
    Draagt de ene stroom die `allOf` en de andere alleen het dragende schema, dan spreken zij
    elkaar niet tegen: de een is fijner dan de ander.
    """
    for kandidaat, grover in ((een, ander), (ander, een)):
        leden = kandidaat.get("allOf") if isinstance(kandidaat, dict) else None
        if leden and grover in leden:
            return kandidaat
    return None


def voeg_samen(bestaand, nieuw, waar, gaten, opgelost):
    """Twee operaties op hetzelfde pad en dezelfde methode tot een operatie maken.

    Dezelfde aanroep staat in meer dan een stroom: `/abonnementen` in drie, en de opvraag op
    een specificatie in twee. Een document draagt haar daarom een keer, met de parameters en
    de statuscodes van beide stromen bij elkaar. Spreken twee stromen elkaar tegen over
    hetzelfde antwoordlichaam, dan is dat een bevinding en geen keuze van dit script.
    """
    herkomst_voor = list(bestaand["x-okx-herkomst"])
    bestaand["x-okx-herkomst"] = herkomst_voor + nieuw["x-okx-herkomst"]
    stroom = nieuw.get("x-okx-stroom")
    if stroom and stroom not in str(bestaand.get("x-okx-stroom", "")):
        bestaand["x-okx-stroom"] = f"{bestaand.get('x-okx-stroom')}, {stroom}"
    for sleutel in ("standen", "foutgedrag", "diensten"):
        bestaand["_delen"][sleutel] += nieuw["_delen"][sleutel]
    namen = {p["name"] for p in bestaand.get("parameters", [])}
    for parameter in nieuw.get("parameters", []):
        if parameter["name"] not in namen:
            bestaand.setdefault("parameters", []).append(parameter)
    for code, antwoord in nieuw.get("responses", {}).items():
        if code not in bestaand["responses"]:
            bestaand["responses"][code] = antwoord
            continue
        oud = bestaand["responses"][code]
        oud_schema = oud.get("content", {}).get("application/json", {}).get("schema")
        nieuw_schema = antwoord.get("content", {}).get("application/json", {}).get("schema")
        if nieuw_schema and not oud_schema:
            oud["content"] = antwoord["content"]
            oud["description"] = antwoord["description"]
            for sleutel in ("x-okx-stand", "x-okx-stand-kwalificatie", "x-okx-werkbrieven"):
                if sleutel in antwoord:
                    oud[sleutel] = antwoord[sleutel]
            # Het gat dat deze respons bij de eerdere stroom opleverde is hiermee gevuld: een
            # andere stroom draagt het antwoordlichaam wel. Zonder deze regel zou het script
            # een punt open laten staan dat het zelf net heeft gesloten.
            opgelost.update(f"{eerder}, respons {code}" for eerder in herkomst_voor)
        elif nieuw_schema and oud_schema and nieuw_schema != oud_schema:
            fijner = fijnste(oud_schema, nieuw_schema)
            if fijner is not None:
                # De een draagt een overlay over de ander: dan is de overlay het fijnere
                # contract, en dat is wat het document draagt. Welke stroom de overlay bij deze
                # resource noemt en welke niet blijft een punt voor de specificatie.
                oud["content"] = antwoord["content"] if fijner is nieuw_schema else oud["content"]
                gaten.append(Gat(
                    waar,
                    f"op {code} draagt de ene stroom een overlay over het schema van de andere; "
                    f"dit document draagt de overlay, en welke stroom haar bij deze resource "
                    f"noemt blijft een punt voor de specificatie",
                ))
            else:
                gaten.append(Bevinding(
                    waar,
                    f"twee stromen dragen een ander antwoordlichaam op {code}: "
                    f"{oud_schema} en {nieuw_schema}",
                ))
        elif nieuw_schema and oud_schema and "examples" in antwoord.get("content", {}).get(
            "application/json", {}
        ):
            oud["content"]["application/json"].setdefault(
                "examples", antwoord["content"]["application/json"]["examples"]
            )
    if nieuw.get("x-okx-stand") and nieuw.get("x-okx-stand") != bestaand.get("x-okx-stand"):
        bestaand["x-okx-stand"] = "voorstel" if "voorstel" in (
            bestaand.get("x-okx-stand"), nieuw.get("x-okx-stand")
        ) else bestaand.get("x-okx-stand")
    for sleutel in ("x-okx-stand-kwalificatie",):
        extra = nieuw.get(sleutel)
        if extra and extra not in (bestaand.get(sleutel) or ""):
            bestaand[sleutel] = samen(bestaand.get(sleutel, ""), extra)
    werkbrieven = set(bestaand.get("x-okx-werkbrieven", [])) | set(nieuw.get("x-okx-werkbrieven", []))
    if werkbrieven:
        bestaand["x-okx-werkbrieven"] = sorted(werkbrieven)
    return bestaand


def bestellijsten(schema):
    """De gesloten lijsten met meldingssoorten uit een abonnementsschema, elk met zijn sleutel."""
    gevonden = []
    for naam, eigenschap in (schema.get("properties") or {}).items():
        if not isinstance(eigenschap, dict):
            continue
        items = eigenschap.get("items")
        waarden = items.get("enum") if isinstance(items, dict) else None
        if isinstance(waarden, list) and waarden and all(isinstance(w, str) for w in waarden):
            gevonden.append((naam, waarden))
    return gevonden


def controleer_bestellijst(operaties, sleutel, meldingen, schemas, gaten):
    """De lijst waarop een partij zich abonneert, tegen de meldingen die dit document publiceert.

    Een abonnementsoperatie draagt een gesloten lijst met de meldingssoorten die te bestellen
    zijn. Publiceert het document een melding die buiten die lijst valt, dan is zij voor een
    gegenereerde client onbereikbaar: de client leest de lijst en de proza eronder blijft buiten
    beeld. Draagt de lijst een soort waarvoor deze specificatie nergens een vorm legt, dan
    bestelt een client iets waarvan het lichaam onbekend is. De verdiepingen beleggen die
    uitbreiding per stroom in een werkbrief; deze controle leidt het verschil af uit het document
    zelf, zodat het ook zonder die werkbrief in `x-okx-openstaand` staat.

    Staat dezelfde abonnementsoperatie in meer dan een stroom, dan voegt het document haar samen
    tot een pad. Een verschil komt daarom een keer in de uitvoer, met de stromen die haar dragen.
    """
    in_de_snede = {o["melding"] for o in operaties if o["soort"] == "melding"}
    lijsten = {}
    for operatie in operaties:
        if operatie.get("component") != sleutel or operatie["soort"] != "aanroep":
            continue
        naam = (operatie.get("verzoek") or {}).get("schema")
        if not naam or naam not in schemas:
            continue
        gevonden = bestellijsten(schemas[naam]["inhoud"])
        if len(gevonden) > 1:
            gaten.append(Gat(
                operatie["id"],
                f"schema {naam} draagt meer dan een gesloten lijst, waardoor onbepaald blijft "
                f"welke de meldingssoorten bestelt: "
                + ", ".join(sleutelnaam for sleutelnaam, _ in gevonden),
            ))
            continue
        if not gevonden:
            continue
        sleutelnaam, waarden = gevonden[0]
        lijst = lijsten.setdefault(f"{naam}.{sleutelnaam}", {"waarden": set(waarden), "uit": []})
        lijst["uit"].append(operatie["id"])

    for waar, lijst in sorted(lijsten.items()):
        herkomst = ", ".join(lijst["uit"])
        for melding in sorted(set(meldingen) - lijst["waarden"]):
            gaten.append(Gat(
                f"{waar} op {herkomst}",
                f"dit document publiceert de melding {melding} en de lijst waarop een partij "
                f"zich abonneert draagt haar niet, waarmee zij voor een gegenereerde client "
                f"onbereikbaar blijft",
            ))
        for melding in sorted(lijst["waarden"] - in_de_snede):
            gaten.append(Gat(
                f"{waar} op {herkomst}",
                f"de lijst draagt de meldingssoort {melding}, waarvoor deze specificatie "
                f"nergens een vorm legt",
            ))


def bouw_document(sleutel, data, fences, mappen, gaten, werkbrieven=None):
    """Het OpenAPI-document van een component, met de schema's die het nodig heeft erin."""
    component = data["componenten"][sleutel]
    operaties = [kwalificeer(o) for o in data["operaties"]]
    schemas_gevraagd = set()
    paden = {}
    samengevoegd = []
    opgelost = set()

    for operatie in operaties:
        if operatie["soort"] != "aanroep" or operatie.get("component") != sleutel:
            continue
        pad, methode = operatie["pad"], operatie["methode"]
        object_ = operatie_object(operatie, fences, gaten, schemas_gevraagd, [operatie["id"]])
        if methode in paden.get(pad, {}):
            samengevoegd.append((f"{methode.upper()} {pad}", operatie["id"]))
            voeg_samen(paden[pad][methode], object_, f"{methode.upper()} {pad}", gaten, opgelost)
        else:
            paden.setdefault(pad, {})[methode] = object_
        if operatie.get("tevens_op"):
            gaten.append(Gat(
                operatie["id"],
                f"dezelfde operatie staat ook op {operatie['tevens_op']}; die kant landt in "
                f"het document van dat component",
            ))

    meldingen = {}
    ontvangen = []
    for operatie in operaties:
        if operatie["soort"] != "melding":
            continue
        if operatie.get("melder") == sleutel:
            object_ = operatie_object(operatie, fences, gaten, schemas_gevraagd, [operatie["id"]])
            object_["x-okx-ontvanger"] = operatie["ontvanger"]
            # De aflevering van een melding gaat de andere kant op, dus haalt de melder zijn
            # token bij de ontvanger. De auth-standaard past dezelfde regel omgekeerd toe.
            object_["security"] = [{"okxAfleverCredentials": []}]
            naam = operatie["melding"]
            if naam in meldingen:
                samengevoegd.append((f"melding {naam}", operatie["id"]))
                voeg_samen(
                    meldingen[naam][operatie["methode"]], object_, f"melding {naam}", gaten, opgelost
                )
            else:
                meldingen[naam] = {operatie["methode"]: object_}
        elif operatie.get("ontvanger") == sleutel:
            verzoek = operatie.get("verzoek", {})
            inhoud = inhoud_object(
                verzoek, f"{operatie['id']}, ontvangen melding", fences, gaten, schemas_gevraagd
            )
            if verzoek.get("gat"):
                gaten.append(Gat(f"{operatie['id']}, ontvangen melding", verzoek["gat"]))
            ontvangen.append({
                "melding": operatie["melding"],
                "melder": operatie["melder"],
                "description": samen(
                    operatie.get("samenvatting", ""),
                    verzoek.get("omschrijving", ""),
                    stand_zin(operatie.get("stand")),
                    "Deze melding komt aan op het afleveradres dat dit component bij de melder "
                    "registreert, en dat adres is een inrichtingskeuze in plaats van een pad in "
                    "dit document. Haar vorm staat onder `webhooks` in het document van de "
                    "melder, en haar payloadschema staat hieronder.",
                ),
                "content": inhoud,
                "x-okx-herkomst": [operatie["id"]],
                **stand_velden(operatie.get("stand")),
            })

    for groep in list(paden.values()) + list(meldingen.values()):
        for object_ in groep.values():
            maak_beschrijving(object_)
    gaten[:] = [g for g in gaten if g.waar not in opgelost]

    schemas = verzamel_schemas(schemas_gevraagd, mappen, gaten)
    controleer_bestellijst(operaties, sleutel, meldingen, schemas, gaten)
    document = {
        "openapi": OPENAPI_VERSIE,
        "jsonSchemaDialect": DIALECT,
        "info": {
            "title": f"{component['naam']}, koppelvlak onderwijsaanbod",
            "version": data["versie"],
            "summary": (
                f"Het koppelvlak van {component.get('naam_in_zin', component['naam'])}: de "
                f"operaties die dit component serveert en de meldingen die het verstuurt, uit de "
                f"interactiespecificatie ontwerpen en ontsluiten van onderwijsaanbod."
            ),
            "description": samen(
                "Dit document is afgeleid en wordt niet onderhouden: het komt uit "
                "operaties.json van de interactiespecificatie, met "
                "tools/scripts/genereer-oas.py. Een wijziging hoort in de specificatie, "
                "waarna dit document opnieuw wordt gegenereerd.",
                component.get("toelichting", ""),
                "Wat deze specificatie als voorstel draagt, draagt dat ook hier: elke operatie, "
                "parameter en respons noemt haar stand in haar beschrijving en in "
                "x-okx-stand, met de kwalificatie erbij waar de stand een onderdeel van de "
                "operatie betreft.",
            ),
        },
        "servers": [{
            "url": "{basis}",
            "description": (
                "Plaatshouder. " + data["servers"]["openstaand"]
            ),
            "variables": {
                "basis": {
                    "default": data["servers"]["plaatshouder"],
                    "description": "Het adres waarop de instelling dit component ontsluit.",
                }
            },
        }],
        "security": [{"okxClientCredentials": []}],
        "paths": dict(sorted(paden.items())),
    }
    if meldingen:
        document["webhooks"] = dict(sorted(meldingen.items()))
    document["components"] = {
        "securitySchemes": beveiliging(data),
        "schemas": {naam: inhoud["inhoud"] for naam, inhoud in schemas.items()},
    }
    if ontvangen:
        document["x-okx-ontvangen-meldingen"] = sorted(ontvangen, key=lambda m: m["melding"])
    document["x-okx-schemas"] = {naam: inhoud["herkomst"] for naam, inhoud in schemas.items()}
    document["x-okx-bron"] = {
        "bestand": "operaties.json",
        "script": "tools/scripts/genereer-oas.py",
        **data["bron"],
    }
    if samengevoegd:
        document["x-okx-samengevoegd"] = [
            {"operatie": pad, "herkomst": herkomst} for pad, herkomst in samengevoegd
        ]
    aangehaald = sorted(aangehaalde_werkbrieven(document))
    if aangehaald:
        legenda = {}
        for code in aangehaald:
            if code in (werkbrieven or {}):
                legenda[code] = (werkbrieven or {})[code]
            else:
                gaten.append(Gat(
                    code,
                    "deze werkbriefcode staat bij een operatie en haar tekst is in de "
                    "verdiepingsbestanden niet gevonden",
                ))
        if legenda:
            document["x-okx-werkbrieven"] = legenda
    document["x-okx-openstaand"] = [str(g) for g in gaten]
    return document, schemas, samengevoegd


def aangehaalde_werkbrieven(document):
    """Elke werkbriefcode die ergens in het document staat, zodat de legenda niets te veel draagt."""
    gevonden = set()

    def loop(knoop):
        if isinstance(knoop, dict):
            for sleutel, waarde in knoop.items():
                if sleutel == "x-okx-werkbrieven" and isinstance(waarde, list):
                    gevonden.update(waarde)
                else:
                    loop(waarde)
        elif isinstance(knoop, list):
            for item in knoop:
                loop(item)

    loop(document)
    return gevonden


def beveiliging(data):
    """De beveiligingsschema's, uit de auth-standaard van Npuls-OKx/Public."""
    grond = data["beveiliging"]
    return {
        "okxClientCredentials": {
            "type": "oauth2",
            "description": samen(
                grond["grond"],
                f"Vindplaats: {grond['verwijzing']}",
                f"Hier staat iets open: {grond['openstaand']}",
            ),
            "flows": {
                "clientCredentials": {
                    "tokenUrl": data["servers"]["plaatshouder"] + "/token",
                    "scopes": {},
                }
            },
        },
        "okxAfleverCredentials": {
            "type": "oauth2",
            "description": samen(
                "Voor de aflevering van een melding geldt dezelfde regel omgekeerd: de melder "
                "haalt een token bij de token-endpoint van de ontvanger, met de gegevens die "
                "bij de registratie van het abonnement zijn afgesproken.",
                f"Vindplaats: {grond['verwijzing']}",
                "Hier staat iets open: de token-endpoint van de ontvanger staat per "
                "abonnement open.",
            ),
            "flows": {
                "clientCredentials": {
                    "tokenUrl": "https://ontvanger.invalid/okx/token",
                    "scopes": {},
                }
            },
        },
    }


# -------------------------------------------------------------------------------- de controle


def verwijzingen_in(knoop, pad="#"):
    """Elke `$ref` in een document, met de plek waar zij staat."""
    if isinstance(knoop, dict):
        for sleutel, waarde in knoop.items():
            if sleutel == "$ref" and isinstance(waarde, str):
                yield pad, waarde
            else:
                yield from verwijzingen_in(waarde, f"{pad}/{sleutel}")
    elif isinstance(knoop, list):
        for i, item in enumerate(knoop):
            yield from verwijzingen_in(item, f"{pad}/{i}")


def los_pointer_op(document, pointer):
    """Een JSON Pointer in het document opzoeken, of None als hij nergens uitkomt."""
    knoop = document
    for deel in pointer.lstrip("#").lstrip("/").split("/"):
        if not deel:
            continue
        deel = deel.replace("~1", "/").replace("~0", "~")
        if isinstance(knoop, dict) and deel in knoop:
            knoop = knoop[deel]
        elif isinstance(knoop, list) and deel.isdigit() and int(deel) < len(knoop):
            knoop = knoop[int(deel)]
        else:
            return None
    return knoop


def controleer_verwijzingen(document, waar, gaten):
    """Elke verwijzing in het document opzoeken in het document zelf."""
    for plek, ref in verwijzingen_in(document):
        if not ref.startswith("#"):
            gaten.append(Bevinding(f"{waar} {plek}", f"de verwijzing {ref} wijst buiten het document"))
        elif los_pointer_op(document, ref) is None:
            gaten.append(Bevinding(f"{waar} {plek}", f"de verwijzing {ref} komt nergens uit"))


def deel(sleutel):
    """Een sleutel als deel van een JSON Pointer, met de tekens die daar betekenis hebben."""
    return str(sleutel).replace("~", "~0").replace("/", "~1")


def voorbeelden_in(document):
    """Elk voorbeeld in het document, met de plek van het schema waar het onder staat.

    De plek is een JSON Pointer in het document. Daarmee rekent een verwijzing binnen dat
    schema vanaf de wortel van het document, en komt `#/components/schemas/...` uit waar hij
    hoort. Een kopie van het schema zou die verwijzing in zichzelf laten zoeken.
    """
    def loop(knoop, pad=""):
        if isinstance(knoop, dict):
            if "schema" in knoop and isinstance(knoop.get("examples"), dict):
                for naam, voorbeeld in knoop["examples"].items():
                    if isinstance(voorbeeld, dict) and "value" in voorbeeld:
                        yield (
                            f"#{pad}/examples/{deel(naam)}",
                            f"#{pad}/schema",
                            voorbeeld["value"],
                        )
            for sleutel, waarde in knoop.items():
                yield from loop(waarde, f"{pad}/{deel(sleutel)}")
        elif isinstance(knoop, list):
            for i, item in enumerate(knoop):
                yield from loop(item, f"{pad}/{i}")

    return loop(document)


def controleer_voorbeelden(document, waar, gaten):
    """Elk voorbeeld tegen het schema waar het onder staat, met de bundel als register."""
    try:
        import jsonschema
        from referencing.jsonschema import DRAFT202012
        from referencing import Registry
    except ImportError:
        gaten.append(Gat(waar, "het pakket jsonschema ontbreekt, dus bleven de voorbeelden ongetoetst"))
        return 0
    register = Registry().with_resource(BASIS_URI, DRAFT202012.create_resource(document))
    geteld = 0
    for plek, schemaplek, lading in voorbeelden_in(document):
        geteld += 1
        validator = jsonschema.Draft202012Validator(
            {"$ref": BASIS_URI + schemaplek},
            registry=register,
            format_checker=jsonschema.FormatChecker(),
        )
        try:
            fouten = sorted(validator.iter_errors(lading), key=lambda f: list(f.absolute_path))
        except Exception as fout:
            gaten.append(Bevinding(f"{waar} {plek}", f"de validatie liep vast: {fout}"))
            continue
        for fout in fouten:
            plekje = "/" + "/".join(str(p) for p in fout.absolute_path) if fout.absolute_path else "/"
            gaten.append(Bevinding(f"{waar} {plek}", f"{plekje}: {fout.message}"))
    return geteld


def controleer_openapi(document, waar, gaten):
    """Het document door `openapi-spec-validator`, zodra dat pakket er is."""
    try:
        from openapi_spec_validator import validate
    except ImportError:
        gaten.append(Gat(
            waar,
            "het pakket openapi-spec-validator ontbreekt, dus bleef het document ongetoetst "
            "als OpenAPI; installeer het in de dev-container",
        ))
        return False
    try:
        validate(document)
    except Exception as fout:
        eerste = str(fout).splitlines()[0]
        gaten.append(Bevinding(waar, f"het document is geen geldige OpenAPI: {eerste}"))
        return False
    return True


# ------------------------------------------------------------------------------- de uitvoering


def schrijf_yaml(document, bestand, waar, gaten):
    """Hetzelfde document als YAML ernaast, want dat is de vorm die OEAPI aanhoudt.

    De OpenAPI-specificatie laat JSON en YAML beide toe, en de twee zijn hier geen twee
    waarheden: zij komen uit dezelfde generatorronde en kunnen daarmee niet uiteenlopen. De
    JSON is wat de keuring en de testgevallen lezen, de YAML is wat een mens leest en wat de
    overlay-structuur van OEAPI draagt (`profile.yaml`, `source/spec.yaml`).

    Het script laadt de weggeschreven YAML terug en vergelijkt haar met het document. Een
    verschil is een bevinding: dan draagt een van de twee vormen iets anders dan de ander, en
    dat is precies wat deze opzet moet voorkomen.

    Ontbreekt PyYAML, dan blijft het bij de JSON-vorm. Die melding staat al in de openstaande
    punten van het document, want zij hoort erin te staan voordat het wordt weggeschreven.
    """
    if yaml is None:
        return None
    tekst = yaml.safe_dump(
        document, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100
    )
    bestand.write_text(tekst, encoding="utf-8")
    terug = yaml.safe_load(tekst)
    if terug != document:
        gaten.append(Bevinding(
            waar, "de YAML-vorm leest niet terug als hetzelfde document als de JSON-vorm"
        ))
    return bestand


def genereer(data, map_, uit, mappen, gevraagd, alles):
    """Per gevraagd component een document bouwen, controleren en wegschrijven."""
    fences = lees_fences(map_)
    werkbrieven = lees_werkbrieven(map_, data.get("stromen") or {})
    verslagen = []
    for sleutel, component in data["componenten"].items():
        if gevraagd and sleutel not in gevraagd:
            continue
        if not gevraagd and not component.get("afgerond") and not alles:
            verslagen.append({
                "component": sleutel,
                "geschreven": None,
                "gaten": [Gat(sleutel, f"geen document: {component['toelichting']}")],
            })
            continue
        gaten = []
        document, schemas, samengevoegd = bouw_document(
            sleutel, data, fences, mappen, gaten, werkbrieven
        )
        controleer_verwijzingen(document, sleutel, gaten)
        aantal_voorbeelden = controleer_voorbeelden(document, sleutel, gaten)
        geldig = controleer_openapi(document, sleutel, gaten)
        if yaml is None:
            gaten.append(Gat(
                sleutel,
                "het pakket PyYAML ontbreekt, dus blijft het bij de JSON-vorm; zet het in "
                ".devcontainer/requirements.txt en bouw de container opnieuw",
            ))
        document["x-okx-openstaand"] = [str(g) for g in gaten]
        uit.mkdir(parents=True, exist_ok=True)
        bestand = uit / f"{sleutel}.openapi.json"
        bestand.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        in_yaml = schrijf_yaml(document, uit / f"{sleutel}.openapi.yaml", sleutel, gaten)
        verslagen.append({
            "component": sleutel,
            "geschreven": bestand,
            "yaml": in_yaml,
            "paden": len(document.get("paths", {})),
            "operaties": sum(len(v) for v in document.get("paths", {}).values()),
            "meldingen": len(document.get("webhooks", {})),
            "ontvangen": len(document.get("x-okx-ontvangen-meldingen", [])),
            "schemas": len(schemas),
            "voorbeelden": aantal_voorbeelden,
            "geldig": geldig,
            "samengevoegd": samengevoegd,
            "gaten": gaten,
        })
    return verslagen


def rapporteer(verslagen, kort):
    """Wat er is geschreven, en wat er niet geplaatst kon worden."""
    bevindingen = 0
    gaten = 0
    for verslag in verslagen:
        if verslag["geschreven"] is None:
            print(f"\n{verslag['component']}: geen document geschreven")
            for gat in verslag["gaten"]:
                print(f"  open: {gat.wat}")
            gaten += len(verslag["gaten"])
            continue
        pad = str(verslag["geschreven"]).replace(str(WORTEL) + "/", "")
        print(f"\n{verslag['component']}: {pad}")
        if verslag.get("yaml"):
            vorm = str(verslag["yaml"]).replace(str(WORTEL) + "/", "")
            print(f"  en als YAML: {vorm}")
        print(
            f"  {verslag['paden']} paden met {verslag['operaties']} operaties, "
            f"{verslag['meldingen']} meldingen onder webhooks, "
            f"{verslag['ontvangen']} ontvangen meldingen, "
            f"{verslag['schemas']} schema's, {verslag['voorbeelden']} voorbeelden"
        )
        print(f"  geldige OpenAPI: {'ja' if verslag['geldig'] else 'niet vastgesteld'}")
        for pad_, herkomst in verslag["samengevoegd"]:
            print(f"  samengevoegd: {pad_} draagt ook {herkomst}")
        eigen_bevindingen = [g for g in verslag["gaten"] if isinstance(g, Bevinding)]
        eigen_gaten = [g for g in verslag["gaten"] if not isinstance(g, Bevinding)]
        bevindingen += len(eigen_bevindingen)
        gaten += len(eigen_gaten)
        for bevinding in eigen_bevindingen:
            print(f"  BEVINDING {bevinding}")
        if kort:
            print(f"  {len(eigen_gaten)} punten staan open; laat --kort weg om ze te zien")
        else:
            for gat in eigen_gaten:
                print(f"  open: {gat}")
    print(f"\n{bevindingen} bevindingen, {gaten} punten die openstaan.")
    return bevindingen, gaten


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--operaties", default=None, help="het bestand met de operaties")
    parser.add_argument("--uit", default=None, help="de map voor de documenten; standaard oas/ naast de specificatie")
    parser.add_argument(
        "--public-schemas", default=None,
        help="de schemamap van Npuls-OKx/Public; standaard ../Public/Informatie-en-gegevensmodellen/schemas",
    )
    parser.add_argument(
        "--component", action="append", default=None,
        help="alleen dit component; herhaalbaar",
    )
    parser.add_argument(
        "--alles", action="store_true",
        help="ook de componenten die in operaties.json nog niet afgerond zijn",
    )
    parser.add_argument("--kort", action="store_true", help="alleen de tellingen en de bevindingen")
    args = parser.parse_args(argv)

    bestand = pathlib.Path(args.operaties) if args.operaties else (
        WORTEL / SPECIFICATIE_STANDAARD / "operaties.json"
    )
    if not bestand.is_file():
        print(f"Het bestand {bestand} bestaat niet.", file=sys.stderr)
        return 3
    try:
        data = json.loads(bestand.read_text(encoding="utf-8"))
    except json.JSONDecodeError as fout:
        print(f"Het bestand {bestand} is geen json: {fout}", file=sys.stderr)
        return 3
    for sleutel in ("componenten", "operaties", "versie", "bron", "servers", "beveiliging"):
        if sleutel not in data:
            print(f"Het bestand {bestand} draagt geen {sleutel}.", file=sys.stderr)
            return 3

    map_ = bestand.parent
    uit = pathlib.Path(args.uit) if args.uit else map_ / UIT_STANDAARD
    mappen = []
    eigen = map_ / "schemas"
    if eigen.is_dir():
        mappen.append(eigen)
    public = pathlib.Path(args.public_schemas) if args.public_schemas else WORTEL / PUBLIC_STANDAARD
    if public.is_dir():
        mappen.append(public)
    else:
        print(
            f"De schemamap van Public staat niet op {public}. Zonder de vastgelegde schema's "
            f"blijft een bundel onvolledig, en dan zegt dit script niets over het document.",
            file=sys.stderr,
        )
        return 3
    if not mappen:
        print("Geen enkele schemamap is gevonden.", file=sys.stderr)
        return 3

    gevraagd = set(args.component or [])
    onbekend = gevraagd - set(data["componenten"])
    if onbekend:
        print(f"Onbekend component: {', '.join(sorted(onbekend))}", file=sys.stderr)
        return 3

    verslagen = genereer(data, map_, uit, mappen, gevraagd, args.alles)
    bevindingen, gaten = rapporteer(verslagen, args.kort)
    if bevindingen:
        return 1
    if gaten:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
