#!/usr/bin/env python3
"""Een gegenereerd OpenAPI-document in de browser bekijken, met Redoc.

Waarom dit script bestaat: GitHub rendert een OpenAPI-document niet. In de bestandsweergave
staat de kale JSON of YAML, en daarmee is een koppelvlak van negen paden met dertig schema's
niet te overzien. Een leverancier die erop offreert wil de operaties naast hun berichten zien,
en dat is precies wat een renderer doet. Relateert aan: Npuls-OKx/meta#374.

    python3 scripts/bekijk-oas.py [--map PAD] [--poort 8088] [--document NAAM]

Zonder argumenten dient het de map
architecture/docs/specificatie/interactie-onderwijsaanbod/oas en opent het de keuze op
http://localhost:8088. Draait er al iets op die poort, geef dan een andere.

Hoe het werkt
-------------
Het script start een server op de map met de documenten en levert op de wortel een pagina die
[Redoc](https://github.com/Redocly/redoc) van een CDN haalt en op het document richt. De
documenten zelf gaan ongewijzigd over de lijn; er wordt niets naar schijf geschreven, dus de
map met de artefacten blijft zoals de generator haar achterliet.

De server bindt op elk adres (`0.0.0.0`) en niet op de loopback alleen. Een dev-container
verbindt de doorgestuurde poort over IPv4, en een server die alleen op `[::1]` staat is daar
niet te bereiken; de browser blijft dan herladen. Dezelfde valkuil staat in de
presentatieskill voor de Slidev-server.

Wat een renderer laat vallen
----------------------------
Redoc zet het tonen van eigen velden (`x-`) standaard uit, en aangezet rendert hij ze alleen
bij de verzoekdetails en per veld. Het document draagt honderdnegentien `x-okx`-velden: de
stand per operatie, de werkbrieven, de openstaande punten en de herkomst. Daarvan overleeft
de stand, want die staat ook in de `description` van elke operatie; de openstaande punten en
de legenda van de werkbrieven staan alleen in de eigen velden en blijven in het beeld dus
onzichtbaar.

Dit is daarom een werkbeeld en geen publicatie. Een afnemer die alleen het gerenderde beeld
leest, ziet het contract zonder te zien wat eraan vastligt en wat een voorstel is. Publiceren
vraagt eerst een antwoord op die vraag.

Drie andere wegen naar hetzelfde beeld
--------------------------------------

| Weg | Wanneer die past |
|---|---|
| `npx @redocly/cli preview-docs <het document>` | De officiele opdrachtregel van Redocly, met live herladen terwijl de specificatie verandert. Haalt een pakket op bij de eerste aanroep |
| Een extensie in de editor, bijvoorbeeld OpenAPI (Swagger) Editor | Naast de specificatie werken, met de keuring erbij in hetzelfde venster |
| Publiceren op GitHub Pages | Voor een afnemer die geen gereedschap wil installeren. Dat hoort bij het releasepakket in Npuls-OKx/Public en niet hier, want dit document is nog een voorstel |
"""

import argparse
import functools
import http.server
import pathlib
import socketserver
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
STANDAARD = "architecture/docs/specificatie/interactie-onderwijsaanbod/oas"
POORT = 8088

# Redoc op een vastgezette versie, zodat het beeld niet onder het werk verschuift.
REDOC = "https://cdn.jsdelivr.net/npm/redoc@2.1.5/bundles/redoc.standalone.js"

STIJL = """
    body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .keuze { max-width: 44rem; margin: 3rem auto; padding: 0 1.5rem; line-height: 1.55; }
    .keuze h1 { font-size: 1.4rem; margin-bottom: 0.3rem; }
    .keuze p { color: #444; margin-top: 0; }
    .keuze ul { list-style: none; padding: 0; }
    .keuze li { border: 1px solid #ddd; border-radius: 6px; margin: 0.5rem 0; }
    .keuze a { display: block; padding: 0.9rem 1.1rem; text-decoration: none; color: #15437a; }
    .keuze a:hover { background: #f4f7fb; }
    .keuze small { color: #666; display: block; margin-top: 0.2rem; }
"""


def documenten(map_):
    """De OpenAPI-documenten in een map, met de YAML-vorm voorop per component.

    Een component levert twee bestanden met dezelfde inhoud. De YAML-vorm gaat naar de
    renderer, want zij is kleiner over de lijn en zij is de vorm die OEAPI aanhoudt.
    """
    per_component = {}
    for bestand in sorted(map_.glob("*.openapi.*")):
        if bestand.suffix not in (".yaml", ".yml", ".json"):
            continue
        naam = bestand.name.split(".openapi.")[0]
        if naam not in per_component or bestand.suffix in (".yaml", ".yml"):
            per_component[naam] = bestand
    return per_component


def pagina_redoc(bestandsnaam, titel):
    """De pagina die Redoc op een document richt."""
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<style>{STIJL}</style>
</head>
<body>
<redoc spec-url="{bestandsnaam}" show-extensions="true"></redoc>
<script src="{REDOC}"></script>
</body>
</html>
"""


def pagina_keuze(per_component, map_):
    """De pagina met een regel per component, voor een map met meer dan een document."""
    regels = []
    for naam, bestand in sorted(per_component.items()):
        maat = bestand.stat().st_size // 1024 if bestand.exists() else 0
        regels.append(
            f'      <li><a href="/{naam}">{naam}'
            f"<small>{bestand.name}, {maat} kB</small></a></li>"
        )
    lijst = "\n".join(regels)
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>De koppelvlakken van deze interactiespecificatie</title>
<style>{STIJL}</style>
</head>
<body>
  <div class="keuze">
    <h1>De koppelvlakken van deze interactiespecificatie</h1>
    <p>Een document per applicatiecomponent, afgeleid uit {map_.name}.</p>
    <ul>
{lijst}
    </ul>
  </div>
</body>
</html>
"""


class Handler(http.server.SimpleHTTPRequestHandler):
    """Dient de documenten uit de map, met een gerenderde pagina op elke componentnaam."""

    per_component = {}
    map_ = None

    def do_GET(self):  # noqa: N802, de naam komt uit de bibliotheek
        pad = self.path.split("?")[0].rstrip("/")
        if pad in ("", "/"):
            if len(self.per_component) == 1:
                naam, bestand = next(iter(self.per_component.items()))
                return self.stuur(pagina_redoc(bestand.name, naam))
            return self.stuur(pagina_keuze(self.per_component, self.map_))
        naam = pad.lstrip("/")
        if naam in self.per_component:
            return self.stuur(pagina_redoc(self.per_component[naam].name, naam))
        return super().do_GET()

    def stuur(self, html):
        """Een pagina uit het geheugen, zodat er niets naar schijf gaat."""
        lading = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(lading)))
        self.end_headers()
        self.wfile.write(lading)

    def log_message(self, formaat, *args):
        """Stil, want een aanroep per bestand zegt de kijker niets."""


def maak_server(map_, poort):
    """De server op een map, gebonden op elk adres zodat de doorgestuurde poort werkt."""
    per_component = documenten(map_)
    klasse = type("GebondenHandler", (Handler,), {
        "per_component": per_component,
        "map_": map_,
    })
    handler = functools.partial(klasse, directory=str(map_))
    socketserver.TCPServer.allow_reuse_address = True
    return socketserver.TCPServer(("", poort), handler), per_component


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--map", default=None, help="de map met de OpenAPI-documenten")
    parser.add_argument("--poort", type=int, default=POORT, help=f"de poort, standaard {POORT}")
    parser.add_argument(
        "--document", default=None, help="alleen dit component, zonder de keuzepagina"
    )
    args = parser.parse_args(argv)

    map_ = pathlib.Path(args.map) if args.map else WORTEL / STANDAARD
    if not map_.is_dir():
        print(
            f"De map {map_} bestaat niet. Draai eerst python3 scripts/genereer-oas.py.",
            file=sys.stderr,
        )
        return 2
    try:
        server, per_component = maak_server(map_, args.poort)
    except OSError as fout:
        print(f"De poort {args.poort} is niet te openen: {fout}", file=sys.stderr)
        return 2
    if not per_component:
        print(f"In {map_} staat geen OpenAPI-document.", file=sys.stderr)
        server.server_close()
        return 2
    if args.document and args.document not in per_component:
        print(
            f"Onbekend component: {args.document}. "
            f"Beschikbaar: {', '.join(sorted(per_component))}",
            file=sys.stderr,
        )
        server.server_close()
        return 2

    poort = server.server_address[1]
    pad = f"/{args.document}" if args.document else ""
    print(f"De documenten in {map_.name}: {', '.join(sorted(per_component))}", flush=True)
    print(f"Te bekijken op http://localhost:{poort}{pad}", flush=True)
    print("Stoppen met Ctrl+C.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nGestopt.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
