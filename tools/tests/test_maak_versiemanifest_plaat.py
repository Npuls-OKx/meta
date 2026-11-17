"""Testgevallen die afdwingen dat elke uitgebrachte plaat bij het model hoort.

Waarom dit een testgeval is en geen afspraak: de viewnamen dragen geen versie meer, dus
de versie hangt aan de export. Public haalt die versie aan, in de tekst en in
bestandsnamen. Verandert een view zonder dat de plaat opnieuw wordt uitgebracht, dan wijst
`hoofdplaat v1.7.1` naar een beeld dat iets anders laat zien dan het model. Dat is het
stille verschil dat niemand aan de bestandsnaam ziet.

De hash dekt de inhoud van de view en niet het hele modelbestand, zodat een wijziging
elders in het model geen export afdwingt.
"""

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
MANIFEST = WORTEL / "architecture/model/bron/versiemanifest.json"
SCRIPT = WORTEL / "tools/scripts/maak-versiemanifest-plaat.py"
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
BEELD = {".jpg", ".jpeg", ".png", ".svg"}
# Een viewnaam draagt geen versie meer: die hoort bij de export. Deze vorm vangt v1.7,
# 1.7a en 1.7.1 af, en ook de (obv 1.7)-verwijzing van een koppelvlakview.
VERSIE_IN_NAAM = re.compile(r"\bv?\d+\.\d+(\.\d+)?[a-z]?\b")
# Oude views die met opzet een versie houden, op id zodat een hernoeming ze niet raakt.
UITGEZONDERD = {
    "id-140ced0690894291acfbd86453fa6e57": "oude MOKA-view, uitgezonderd door de modelleur (#405)",
}


def laad():
    spec = importlib.util.spec_from_file_location("maak_versiemanifest_plaat", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def eigen_views(wortel):
    """De views van OKx zelf. MOKA- en examineringsviews blijven erbuiten: dat is
    overgenomen werk met een eigen versienummering die niet van OKx is."""
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
        """De versie hoort bij de export en niet bij de view."""
        fout = sorted((e.get("name") or "") for e in eigen_views(ET.parse(MODEL).getroot())
                      if VERSIE_IN_NAAM.search(e.get("name") or ""))
        self.assertEqual(fout, [], "viewnamen met een versie erin; die hoort in het versiemanifest")

    def test_given_own_views_when_listed_then_no_two_share_a_name(self):
        """Zonder versie in de naam is een dubbele naam stil: elk script pakt de eerste.

        Toen de vier hoofdplaatviews hun versie verloren heetten zij alle vier
        `OKx hoofdplaat`, en de eerste in documentvolgorde was de oudste uit de map `oud`.
        """
        from collections import Counter
        telling = Counter((e.get("name") or "") for e in eigen_views(ET.parse(MODEL).getroot()))
        self.assertEqual(sorted(n for n, k in telling.items() if k > 1), [],
                         "twee views met dezelfde naam; elk script pakt de eerste")

    def test_given_the_exception_list_when_checked_then_each_id_still_in_the_model(self):
        ids = {e.get("id") for e in ET.parse(MODEL).getroot().iter("element")}
        self.assertEqual(set(UITGEZONDERD) - ids, set())


class ElkePlaatInHetManifest(unittest.TestCase):
    """Het manifest dekt elke plaat die wij uitbrengen, en elke versie daarvan."""

    def test_given_the_script_when_read_then_every_plate_has_a_block(self):
        m = manifest()
        self.assertEqual(sorted(m["platen"]), sorted(laad().PLATEN),
                         "een plaat in het script zonder blok in het manifest, of omgekeerd")

    def test_given_each_plate_when_read_then_its_view_exists_in_the_model(self):
        namen = {e.get("name") for e in ET.parse(MODEL).getroot().iter("element")
                 if e.get(XSI) == "archimate:ArchimateDiagramModel"}
        for naam, b in manifest()["platen"].items():
            with self.subTest(plaat=naam):
                self.assertIn(b["view"], namen, f"view van {naam} bestaat niet in het model")

    def test_given_each_version_when_read_then_it_carries_its_fields(self):
        for naam, b in manifest()["platen"].items():
            for v in b["versies"]:
                with self.subTest(plaat=naam, versie=v["versie"]):
                    for sleutel in ("versie", "export", "beeld_bron", "beeld_commit",
                                    "reproduceerbaar", "viewhash", "model_herkomst"):
                        self.assertIn(sleutel, v)
                    # Drie delen, want een letterversie wordt semver: 1.6a werd 1.6.1 en
                    # 1.7 werd 1.7.0. Twee delen laat open of er nog een patch volgt.
                    self.assertRegex(v["versie"], SEMVER, f"{v['versie']} is geen MAJOR.MINOR.PATCH")

    def test_given_a_commit_when_recorded_then_it_is_the_full_forty_characters(self):
        """Een afkorting is een prefix waarvan de uniciteit alleen nu geldt.

        Git schaalt zijn afkortlengte mee met het aantal objecten in de repository; hier
        staat die al op acht tekens. Een verwijzing die jaren mee moet, slaat de volle
        hash op.
        """
        for naam, b in manifest()["platen"].items():
            for v in b["versies"]:
                for sleutel in ("beeld_commit", "model_commit"):
                    if v.get(sleutel) is not None:
                        with self.subTest(plaat=naam, versie=v["versie"], sleutel=sleutel):
                            self.assertRegex(v[sleutel], re.compile(r"^[0-9a-f]{40}$"))

    def test_given_a_version_claiming_provenance_then_it_carries_a_hash(self):
        """Wie zegt waar hij vandaan komt, moet dat kunnen aantonen."""
        for naam, b in manifest()["platen"].items():
            for v in b["versies"]:
                if v["model_herkomst"].startswith(("vastgelegd", "nagemeten")):
                    with self.subTest(plaat=naam, versie=v["versie"]):
                        self.assertIsNotNone(v["viewhash"])
                        self.assertIsNotNone(v["view"])
                        self.assertIsNotNone(v["model_commit"])

    def test_given_each_version_when_read_then_its_export_exists(self):
        for naam, b in manifest()["platen"].items():
            for v in b["versies"]:
                with self.subTest(plaat=naam, versie=v["versie"]):
                    self.assertTrue((WORTEL / v["export"]).exists(),
                                    f"de export die het manifest noemt bestaat niet: {v['export']}")

    def test_given_what_is_on_disk_when_compared_then_the_manifest_matches(self):
        """Een uitgebrachte plaat zonder regel is er een die niemand kan herleiden.

        Dat gebeurde: `hoofdplaat 1.6b.jpg` stond samen met `1.6a` in de map `1.6`, en het
        script nam de eerste op alfabet.
        """
        mod = laad()
        for naam, plaat in mod.PLATEN.items():
            with self.subTest(plaat=naam):
                op_schijf = set(mod.versies_op_schijf(plaat))
                genoemd = {v["versie"] for v in manifest()["platen"][naam]["versies"]}
                self.assertEqual(op_schijf - genoemd, set(), "uitgebrachte plaat zonder regel")
                self.assertEqual(genoemd - op_schijf, set(), "regel zonder uitgebrachte plaat")


class DePlaatHoortBijHetModel(unittest.TestCase):
    def test_given_the_current_view_when_hashed_then_it_matches_the_current_version(self):
        """Wijkt de view af, dan toont de uitgebrachte plaat iets anders dan het model."""
        mod = laad()
        for naam, b in manifest()["platen"].items():
            with self.subTest(plaat=naam):
                huidig = b.get("huidig")
                self.assertIsNotNone(huidig, f"{naam} heeft geen huidige versie")
                v = next(x for x in b["versies"] if x["versie"] == huidig)
                nu = mod.viewhash(MODEL, b["view"])
                self.assertEqual(nu, v["viewhash"],
                                 f"{naam} is gewijzigd zonder nieuwe uitgave; exporteer en draai "
                                 f"maak-versiemanifest-plaat.py --plaat {naam} --schrijf "
                                 f"--versie <hoger dan {huidig}>")

    def test_given_a_retrofitted_version_when_rehashed_then_it_still_matches(self):
        """De nagemeten hashes moeten reproduceerbaar zijn, anders is de historie waardeloos."""
        mod = laad()
        for naam, b in manifest()["platen"].items():
            for v in b["versies"]:
                if v["model_herkomst"].startswith("nagemeten"):
                    with self.subTest(plaat=naam, versie=v["versie"]):
                        self.assertEqual(mod.viewhash_op_commit(v["model_commit"], v["view"]),
                                         v["viewhash"])


class EenGewijzigdePlaatKrijgtEenNieuwNummer(unittest.TestCase):
    """Zonder deze regel kun je het beeld van de huidige versie overschrijven en dezelfde
    versie opnieuw vastleggen; de hash klopt dan weer en de controle zwijgt, terwijl een
    afnemer iets anders geleverd krijgt onder hetzelfde nummer."""

    def gewijzigd_model(self, map_, view):
        kopie = Path(map_) / "model.archimate"
        shutil.copy(MODEL, kopie)
        mod = laad()
        boom = ET.parse(kopie)
        el = mod.view_element(boom.getroot(), view)
        vak = next(c for c in el.iter() if c.find("bounds") is not None)
        b = vak.find("bounds")
        b.set("x", str(int(b.get("x") or 0) + 7))
        boom.write(kopie, encoding="utf-8", xml_declaration=True)
        return kopie

    def test_given_a_changed_view_when_the_same_version_is_recorded_then_it_refuses(self):
        b = manifest()["platen"]["hoofdplaat"]
        with tempfile.TemporaryDirectory() as map_:
            kopie = self.gewijzigd_model(map_, b["view"])
            uit = subprocess.run([sys.executable, str(SCRIPT), "--plaat", "hoofdplaat",
                                  "--schrijf", "--versie", b["huidig"], "--model", str(kopie)],
                                 cwd=WORTEL, capture_output=True, text=True)
            self.assertNotEqual(uit.returncode, 0, "hetzelfde nummer werd geaccepteerd")
            self.assertIn("te laag", uit.stdout + uit.stderr)

    def test_given_a_higher_version_without_an_export_then_it_refuses(self):
        """Een hoger nummer volstaat niet: er moet ook een beeld zijn."""
        with tempfile.TemporaryDirectory() as map_:
            kopie = self.gewijzigd_model(map_, manifest()["platen"]["hoofdplaat"]["view"])
            uit = subprocess.run([sys.executable, str(SCRIPT), "--plaat", "hoofdplaat",
                                  "--schrijf", "--versie", "9.9.9", "--model", str(kopie)],
                                 cwd=WORTEL, capture_output=True, text=True)
            self.assertNotEqual(uit.returncode, 0)
            self.assertIn("geen beeld gevonden", uit.stdout + uit.stderr)

    def test_given_a_version_that_is_not_semver_then_it_refuses(self):
        uit = subprocess.run([sys.executable, str(SCRIPT), "--plaat", "hoofdplaat",
                              "--schrijf", "--versie", "1.8"], cwd=WORTEL,
                             capture_output=True, text=True)
        self.assertNotEqual(uit.returncode, 0)
        self.assertIn("MAJOR.MINOR.PATCH", uit.stdout + uit.stderr)

    def test_given_the_manifest_when_untouched_then_the_refusals_changed_nothing(self):
        """Een geweigerde vastlegging mag het manifest niet half bijwerken."""
        voor = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
        subprocess.run([sys.executable, str(SCRIPT), "--plaat", "hoofdplaat",
                        "--schrijf", "--versie", "1.8"], cwd=WORTEL, capture_output=True)
        self.assertEqual(voor, hashlib.sha256(MANIFEST.read_bytes()).hexdigest())


class DeHashIsPrecies(unittest.TestCase):
    def test_given_a_view_that_does_not_exist_when_hashed_then_none(self):
        self.assertIsNone(laad().viewhash(MODEL, "bestaat niet"))

    def test_given_two_different_views_when_hashed_then_the_hashes_differ(self):
        mod = laad()
        self.assertNotEqual(mod.viewhash(MODEL, "OKx hoofdplaat"),
                            mod.viewhash(MODEL, "OKx informatiemodel"))

    def test_given_the_same_view_twice_when_hashed_then_the_hash_is_stable(self):
        mod = laad()
        self.assertEqual(mod.viewhash(MODEL, "OKx hoofdplaat"),
                         mod.viewhash(MODEL, "OKx hoofdplaat"))

    def test_given_a_moved_box_when_rehashed_then_the_hash_changes(self):
        """De controle moet een plaat vinden die achterloopt. Dit bewijst dat zij dat kan."""
        mod = laad()
        with tempfile.TemporaryDirectory() as map_:
            kopie = Path(map_) / "model.archimate"
            shutil.copy(MODEL, kopie)
            voor = mod.viewhash(kopie, "OKx hoofdplaat")
            boom = ET.parse(kopie)
            el = mod.view_element(boom.getroot(), "OKx hoofdplaat")
            b = next(c for c in el.iter() if c.find("bounds") is not None).find("bounds")
            b.set("x", str(int(b.get("x") or 0) + 1))
            boom.write(kopie, encoding="utf-8", xml_declaration=True)
            self.assertNotEqual(voor, mod.viewhash(kopie, "OKx hoofdplaat"),
                                "een verschoven vak verandert de hash niet; de controle is blind")

    def test_given_a_change_outside_the_view_when_rehashed_then_the_hash_is_unchanged(self):
        """En zij mag geen uitgave afdwingen voor een wijziging die de plaat niet raakt."""
        mod = laad()
        with tempfile.TemporaryDirectory() as map_:
            kopie = Path(map_) / "model.archimate"
            shutil.copy(MODEL, kopie)
            voor = mod.viewhash(kopie, "OKx hoofdplaat")
            boom = ET.parse(kopie)
            ander = mod.view_element(boom.getroot(), "OKx informatiemodel")
            b = next(c for c in ander.iter() if c.find("bounds") is not None).find("bounds")
            b.set("x", str(int(b.get("x") or 0) + 37))
            boom.write(kopie, encoding="utf-8", xml_declaration=True)
            self.assertEqual(voor, mod.viewhash(kopie, "OKx hoofdplaat"),
                             "een wijziging in een andere view dwingt een uitgave af")


if __name__ == "__main__":
    unittest.main()
