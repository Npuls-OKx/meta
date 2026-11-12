"""Testgevallen die afdwingen dat de geexporteerde hoofdplaat bij het model hoort.

Waarom dit een testgeval is en geen losse controle: de viewnamen dragen geen versie
meer, dus de versie hangt aan de export. Public haalt die versie aan, in de tekst en
in bestandsnamen. Verandert de view zonder dat de plaat opnieuw wordt geexporteerd,
dan wijst `hoofdplaat v1.7.1` naar een beeld dat iets anders laat zien dan het model.
Dat is precies het stille verschil dat niemand aan de bestandsnaam ziet.

De hash dekt de inhoud van de view en niet het hele modelbestand, zodat een wijziging
elders in het model geen export afdwingt.
"""

import importlib.util
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
MANIFEST = WORTEL / "architecture/model/informatiestromen hoofdplaat OKx/herkomst.json"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
# Een viewnaam draagt geen versie meer: die hoort bij de export. Deze vormen vangen
# zowel v1.7, 1.7a als 1.7.1 af, en ook de (obv 1.7)-verwijzing van een koppelvlakview.
VERSIE_IN_NAAM = re.compile(r"\bv?\d+\.\d+(\.\d+)?[a-z]?\b")
# Oude views die met opzet een versie houden, op id zodat een hernoeming ze niet raakt.
UITGEZONDERD = {
    "id-140ced0690894291acfbd86453fa6e57": "oude MOKA-view, uitgezonderd door de modelleur (#405)",
}


def laad():
    spec = importlib.util.spec_from_file_location(
        "plaatherkomst", WORTEL / "tools/scripts/plaatherkomst.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def eigen_views(wortel):
    """De views van OKx zelf: de hoofdplaat, haar koppelvlakken en het informatiemodel.

    De MOKA- en examineringsviews blijven erbuiten; die zijn overgenomen werk en hun
    namen dragen een eigen versienummering die niet van OKx is.
    """
    for e in wortel.iter("element"):
        if e.get(XSI) != "archimate:ArchimateDiagramModel":
            continue
        naam = e.get("name") or ""
        if e.get("id") in UITGEZONDERD:
            continue
        if naam.startswith("OKx ") or naam.startswith("Koppelvlak "):
            yield e


class ViewnaamZonderVersie(unittest.TestCase):
    def test_given_own_views_when_named_then_no_version_in_the_name(self):
        """De versie hoort bij de export en niet bij de view; zie plaatherkomst.py."""
        wortel = ET.parse(MODEL).getroot()
        fout = sorted((e.get("name") or "") for e in eigen_views(wortel)
                      if VERSIE_IN_NAAM.search(e.get("name") or ""))
        self.assertEqual(fout, [], "viewnamen met een versie erin; de versie hoort in herkomst.json")

    def test_given_own_views_when_listed_then_no_two_share_a_name(self):
        """Zonder versie in de naam is een dubbele naam stil: elk script pakt de eerste.

        Dat is geen theoretisch risico. Toen de vier hoofdplaatviews hun versie verloren
        heetten zij alle vier `OKx hoofdplaat`, en de eerste in documentvolgorde was de
        oudste uit de map `oud`. De tekenaars zouden dus de verkeerde plaat tekenen
        zonder dat iets het meldt. Oude views horen weg; git draagt hun historie.
        """
        from collections import Counter
        wortel = ET.parse(MODEL).getroot()
        telling = Counter((e.get("name") or "") for e in eigen_views(wortel))
        dubbel = sorted(n for n, k in telling.items() if k > 1)
        self.assertEqual(dubbel, [], "twee views met dezelfde naam; elk script pakt de eerste")

    def test_given_the_exception_list_when_checked_then_each_id_still_in_the_model(self):
        """Een uitzondering die niets meer uitzondert, moet verdwijnen."""
        ids = {e.get("id") for e in ET.parse(MODEL).getroot().iter("element")}
        self.assertEqual(set(UITGEZONDERD) - ids, set())


class HerkomstVanDeExport(unittest.TestCase):
    def test_given_the_manifest_when_read_then_it_carries_version_and_hash(self):
        self.assertTrue(MANIFEST.exists(),
                        "herkomst.json ontbreekt; draai plaatherkomst.py --schrijf --versie <v>")
        m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for sleutel in ("view", "versie", "viewhash", "export"):
            self.assertIn(sleutel, m)
        self.assertRegex(m["versie"], SEMVER, "de versie van de export is geen MAJOR.MINOR.PATCH")

    def test_given_the_view_when_hashed_then_it_matches_the_exported_plate(self):
        """Wijkt de view af, dan toont de geexporteerde plaat iets anders dan het model."""
        m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        nu = laad().viewhash(MODEL, m["view"])
        self.assertIsNotNone(nu, f"view niet gevonden: {m['view']}")
        self.assertEqual(
            nu, m["viewhash"],
            "de hoofdplaat is gewijzigd zonder nieuwe export; exporteer en draai "
            "python3 tools/scripts/plaatherkomst.py --schrijf")

    def test_given_the_manifest_when_read_then_the_export_file_exists(self):
        m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertTrue((MANIFEST.parent / m["export"]).exists(),
                        f"de export die het manifest noemt bestaat niet: {m['export']}")


class DeHashIsPrecies(unittest.TestCase):
    """De hash dekt de view en niet het hele bestand; anders dwingt elke modelwijziging een export af."""

    def test_given_a_view_that_does_not_exist_when_hashed_then_none(self):
        self.assertIsNone(laad().viewhash(MODEL, "bestaat niet"))

    def test_given_two_different_views_when_hashed_then_the_hashes_differ(self):
        mod = laad()
        wortel = ET.parse(MODEL).getroot()
        namen = [e.get("name") for e in wortel.iter("element")
                 if e.get(XSI) == "archimate:ArchimateDiagramModel"][:2]
        if len(namen) < 2:
            self.skipTest("minder dan twee views in het model")
        self.assertNotEqual(mod.viewhash(MODEL, namen[0]), mod.viewhash(MODEL, namen[1]))

    def test_given_the_same_view_twice_when_hashed_then_the_hash_is_stable(self):
        mod = laad()
        naam = json.loads(MANIFEST.read_text(encoding="utf-8"))["view"] if MANIFEST.exists() else "OKx informatiemodel"
        self.assertEqual(mod.viewhash(MODEL, naam), mod.viewhash(MODEL, naam))


if __name__ == "__main__":
    unittest.main()
