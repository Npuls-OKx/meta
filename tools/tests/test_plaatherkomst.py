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
    """Het manifest is de enige brug tussen een uitgebrachte plaat en de modelstaat erachter."""

    def manifest(self):
        self.assertTrue(MANIFEST.exists(),
                        "herkomst.json ontbreekt; draai plaatherkomst.py --retrofit")
        return json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_given_the_manifest_when_read_then_every_version_carries_its_fields(self):
        for v in self.manifest()["versies"]:
            for sleutel in ("versie", "export", "commit", "viewhash", "herkomst"):
                self.assertIn(sleutel, v, f"versie {v.get('versie')} mist {sleutel}")
            self.assertRegex(v["versie"], re.compile(r"^\d+\.\d+(\.\d+)?$"))

    def test_given_a_commit_when_recorded_then_it_is_the_full_forty_characters(self):
        """Een afkorting is een prefix waarvan de uniciteit alleen nu geldt.

        Git schaalt zijn afkortlengte mee met het aantal objecten in de repository;
        in deze repository staat die al op acht tekens in plaats van zeven. Een
        verwijzing die jaren mee moet, slaat daarom de volle hash op.
        """
        for v in self.manifest()["versies"]:
            if v["commit"] is not None:
                self.assertRegex(v["commit"], re.compile(r"^[0-9a-f]{40}$"),
                                 f"versie {v['versie']} draagt geen volledige commithash")

    def test_given_a_version_when_it_claims_provenance_then_it_carries_a_hash(self):
        """Wie zegt waar hij vandaan komt, moet dat kunnen aantonen."""
        for v in self.manifest()["versies"]:
            if v["herkomst"] in ("vastgelegd bij export", "nagemeten"):
                self.assertIsNotNone(v["viewhash"], f"versie {v['versie']} zegt {v['herkomst']} zonder hash")
                self.assertIsNotNone(v["view"])

    def test_given_each_version_when_read_then_its_export_exists(self):
        for v in self.manifest()["versies"]:
            self.assertIsNotNone(v["export"], f"versie {v['versie']} noemt geen export")
            self.assertTrue((MANIFEST.parent / v["export"]).exists(),
                            f"de export die het manifest noemt bestaat niet: {v['export']}")

    def test_given_the_current_view_when_hashed_then_it_matches_the_current_export(self):
        """Wijkt de view af, dan toont de uitgebrachte plaat iets anders dan het model."""
        m = self.manifest()
        huidig = m.get("huidig")
        if not huidig:
            self.skipTest("nog geen versie vastgelegd bij export; draai --schrijf na de eerste export")
        v = next(x for x in m["versies"] if x["versie"] == huidig)
        nu = laad().viewhash(MODEL, m["view"])
        self.assertIsNotNone(nu, f"view niet gevonden: {m['view']}")
        self.assertEqual(nu, v["viewhash"],
                         "de hoofdplaat is gewijzigd zonder nieuwe export; exporteer en draai "
                         "python3 tools/scripts/plaatherkomst.py --schrijf --versie <versie>")

    def test_given_a_retrofitted_version_when_rehashed_then_it_still_matches(self):
        """De nagemeten hashes moeten reproduceerbaar zijn, anders is de historie waardeloos."""
        mod = laad()
        for v in self.manifest()["versies"]:
            if v["herkomst"] == "nagemeten":
                self.assertEqual(mod.viewhash_op_commit(v["commit"], v["view"]), v["viewhash"],
                                 f"versie {v['versie']} is niet opnieuw na te meten")


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

    def test_given_a_moved_box_when_rehashed_then_the_hash_changes(self):
        """De poort moet een plaat vinden die achterloopt. Dit bewijst dat zij dat kan.

        Een verschoven vak is de kleinste wijziging die de plaat zichtbaar verandert
        en die een bestandsvergelijking op naam of datum niet opmerkt.
        """
        import shutil
        import tempfile
        mod = laad()
        naam = json.loads(MANIFEST.read_text(encoding="utf-8"))["view"]
        with tempfile.TemporaryDirectory() as map_:
            kopie = Path(map_) / "model.archimate"
            shutil.copy(MODEL, kopie)
            voor = mod.viewhash(kopie, naam)
            boom = ET.parse(kopie)
            view = mod.view_element(boom.getroot(), naam)
            vak = next(c for c in view.iter() if c.find("bounds") is not None)
            b = vak.find("bounds")
            b.set("x", str(int(b.get("x") or 0) + 1))
            boom.write(kopie, encoding="utf-8", xml_declaration=True)
            self.assertNotEqual(voor, mod.viewhash(kopie, naam),
                                "een verschoven vak verandert de hash niet; de poort is blind")

    def test_given_a_change_outside_the_view_when_rehashed_then_the_hash_is_unchanged(self):
        """En zij mag geen export afdwingen voor een wijziging die de plaat niet raakt."""
        import shutil
        import tempfile
        mod = laad()
        m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        naam = m["view"]
        with tempfile.TemporaryDirectory() as map_:
            kopie = Path(map_) / "model.archimate"
            shutil.copy(MODEL, kopie)
            voor = mod.viewhash(kopie, naam)
            boom = ET.parse(kopie)
            wortel = boom.getroot()
            ander = next(e for e in wortel.iter("element")
                         if e.get(XSI) == "archimate:ArchimateDiagramModel"
                         and e.get("name") != naam)
            vak = next(c for c in ander.iter() if c.find("bounds") is not None)
            b = vak.find("bounds")
            b.set("x", str(int(b.get("x") or 0) + 37))
            boom.write(kopie, encoding="utf-8", xml_declaration=True)
            self.assertEqual(voor, mod.viewhash(kopie, naam),
                             "een wijziging in een andere view verandert de hash; dat dwingt "
                             "een export af die niets met de hoofdplaat te maken heeft")

    def test_given_the_same_view_twice_when_hashed_then_the_hash_is_stable(self):
        mod = laad()
        naam = json.loads(MANIFEST.read_text(encoding="utf-8"))["view"] if MANIFEST.exists() else "OKx informatiemodel"
        self.assertEqual(mod.viewhash(MODEL, naam), mod.viewhash(MODEL, naam))


if __name__ == "__main__":
    unittest.main()
