"""Testgevallen voor tools/scripts/bekijk-oas.py.

De pagina's komen uit functies die geen server nodig hebben, dus toetst het merendeel die
functies rechtstreeks. Twee gevallen starten een server op een vrije poort en halen er een
pagina op, want de keuze tussen een document en de keuzelijst zit in de verzoekbehandeling.
"""

import contextlib
import importlib.util
import io
import json
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
OAS = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod/oas"

spec = importlib.util.spec_from_file_location("bekijk_oas", WORTEL / "tools/scripts/bekijk-oas.py")
bo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bo)


def maak_map(namen):
    """Een map met per naam een leeg OpenAPI-document, in de vorm die de naam zegt."""
    map_ = Path(tempfile.mkdtemp())
    for naam in namen:
        (map_ / naam).write_text("openapi: 3.1.0\n", encoding="utf-8")
    return map_


@contextlib.contextmanager
def server(map_):
    """Een draaiende server op een vrije poort, met het adres erbij."""
    srv, per_component = bo.maak_server(map_, 0)
    draad = threading.Thread(target=srv.serve_forever, daemon=True)
    draad.start()
    try:
        yield f"http://127.0.0.1:{srv.server_address[1]}", per_component
    finally:
        srv.shutdown()
        srv.server_close()
        draad.join(timeout=5)


def haal(adres):
    """Een pagina ophalen, met de tekst terug."""
    with urllib.request.urlopen(adres, timeout=10) as antwoord:
        return antwoord.read().decode("utf-8")


class DeDocumentenInDeMap(unittest.TestCase):
    """Welk bestand per component naar de renderer gaat."""

    def test_given_beide_vormen_when_zoeken_then_gaat_de_yaml_naar_de_renderer(self):
        """De YAML-vorm is normatief, dus is zij ook de vorm die het beeld draagt."""
        map_ = maak_map(["onderwijscatalogus.openapi.json", "onderwijscatalogus.openapi.yaml"])
        gevonden = bo.documenten(map_)
        self.assertEqual(list(gevonden), ["onderwijscatalogus"])
        self.assertEqual(gevonden["onderwijscatalogus"].suffix, ".yaml")

    def test_given_alleen_een_json_when_zoeken_then_gaat_die_naar_de_renderer(self):
        map_ = maak_map(["onderwijscatalogus.openapi.json"])
        self.assertEqual(bo.documenten(map_)["onderwijscatalogus"].suffix, ".json")

    def test_given_meer_componenten_when_zoeken_then_staan_zij_er_elk_een_keer(self):
        map_ = maak_map([
            "onderwijscatalogus.openapi.yaml", "onderwijscatalogus.openapi.json",
            "planningssysteem.openapi.yaml",
        ])
        self.assertEqual(sorted(bo.documenten(map_)), ["onderwijscatalogus", "planningssysteem"])

    def test_given_een_bestand_dat_geen_document_is_when_zoeken_then_blijft_het_erbuiten(self):
        map_ = maak_map(["onderwijscatalogus.openapi.yaml"])
        (map_ / "leeswijzer.md").write_text("tekst", encoding="utf-8")
        (map_ / "onderwijscatalogus.openapi.txt").write_text("tekst", encoding="utf-8")
        self.assertEqual(list(bo.documenten(map_)), ["onderwijscatalogus"])


class DePaginas(unittest.TestCase):
    """Wat er in de pagina staat die de renderer draagt."""

    def test_given_een_document_when_de_pagina_bouwen_then_richt_redoc_erop(self):
        html = bo.pagina_redoc("onderwijscatalogus.openapi.yaml", "onderwijscatalogus")
        self.assertIn('spec-url="onderwijscatalogus.openapi.yaml"', html)
        self.assertIn("<title>onderwijscatalogus</title>", html)

    def test_given_de_pagina_when_lezen_then_staat_redoc_op_een_vaste_versie(self):
        """Een beeld dat onder het werk verschuift is geen beeld om een besluit op te nemen."""
        html = bo.pagina_redoc("x.yaml", "x")
        self.assertIn(bo.REDOC, html)
        self.assertRegex(bo.REDOC, r"redoc@\d+\.\d+\.\d+")

    def test_given_de_pagina_when_lezen_then_toont_redoc_de_eigen_velden(self):
        """Redoc zet dat standaard uit, en dan verdwijnt de stand per veld uit het beeld."""
        self.assertIn('show-extensions="true"', bo.pagina_redoc("x.yaml", "x"))

    def test_given_meer_componenten_when_de_keuze_bouwen_then_draagt_zij_een_regel_per_component(self):
        map_ = maak_map(["onderwijscatalogus.openapi.yaml", "planningssysteem.openapi.yaml"])
        html = bo.pagina_keuze(bo.documenten(map_), map_)
        self.assertIn('href="/onderwijscatalogus"', html)
        self.assertIn('href="/planningssysteem"', html)


class DeServer(unittest.TestCase):
    """De keuze tussen een document en de keuzelijst, en wat een onbekend pad doet."""

    def test_given_een_map_met_een_document_when_de_wortel_opvragen_then_komt_het_beeld(self):
        with server(maak_map(["onderwijscatalogus.openapi.yaml"])) as (adres, _):
            html = haal(adres + "/")
            self.assertIn('spec-url="onderwijscatalogus.openapi.yaml"', html)

    def test_given_een_map_met_twee_documenten_when_de_wortel_opvragen_then_komt_de_keuze(self):
        map_ = maak_map(["onderwijscatalogus.openapi.yaml", "planningssysteem.openapi.yaml"])
        with server(map_) as (adres, _):
            html = haal(adres + "/")
            self.assertIn('href="/planningssysteem"', html)
            self.assertNotIn("spec-url", html)

    def test_given_een_componentnaam_when_opvragen_then_komt_het_beeld_van_dat_component(self):
        map_ = maak_map(["onderwijscatalogus.openapi.yaml", "planningssysteem.openapi.yaml"])
        with server(map_) as (adres, _):
            self.assertIn('spec-url="planningssysteem.openapi.yaml"', haal(adres + "/planningssysteem"))

    def test_given_het_document_zelf_when_opvragen_then_komt_het_ongewijzigd_over_de_lijn(self):
        with server(maak_map(["onderwijscatalogus.openapi.yaml"])) as (adres, _):
            self.assertEqual(haal(adres + "/onderwijscatalogus.openapi.yaml"), "openapi: 3.1.0\n")

    def test_given_een_onbekend_pad_when_opvragen_then_volgt_een_404(self):
        with server(maak_map(["onderwijscatalogus.openapi.yaml"])) as (adres, _):
            with self.assertRaises(urllib.error.HTTPError) as gevangen:
                haal(adres + "/bestaat-niet")
            self.assertEqual(gevangen.exception.code, 404)


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return bo.main(argv)

    def test_given_een_map_die_niet_bestaat_when_starten_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--map", str(Path(tmp) / "weg")]), 2)

    def test_given_een_map_zonder_document_when_starten_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--map", tmp, "--poort", "0"]), 2)

    def test_given_een_onbekend_component_when_starten_then_exitcode_twee(self):
        map_ = maak_map(["onderwijscatalogus.openapi.yaml"])
        self.assertEqual(
            self.draai(["--map", str(map_), "--poort", "0", "--document", "bestaat-niet"]), 2
        )


class InDezeRepository(unittest.TestCase):

    def test_given_de_gegenereerde_map_when_zoeken_then_draagt_zij_de_onderwijscatalogus(self):
        if not OAS.is_dir():
            self.skipTest("oas/ ontbreekt; draai eerst tools/scripts/genereer-oas.py")
        gevonden = bo.documenten(OAS)
        self.assertIn("onderwijscatalogus", gevonden)
        self.assertEqual(gevonden["onderwijscatalogus"].suffix, ".yaml")

    def test_given_beide_vormen_when_vergelijken_then_dragen_zij_hetzelfde_document(self):
        import yaml
        in_yaml = OAS / "onderwijscatalogus.openapi.yaml"
        in_json = OAS / "onderwijscatalogus.openapi.json"
        if not (in_yaml.is_file() and in_json.is_file()):
            self.skipTest("de documenten ontbreken; draai eerst tools/scripts/genereer-oas.py")
        self.assertEqual(
            yaml.safe_load(in_yaml.read_text(encoding="utf-8")),
            json.loads(in_json.read_text(encoding="utf-8")),
        )


if __name__ == "__main__":
    unittest.main()
