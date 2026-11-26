"""Testgevallen die afdwingen dat elk product onder architecture/producten/ zijn versies draagt.

Waarom dit een testgeval is en geen afspraak: een versienummer zonder commit is een etiket
zonder verwijzing. Niemand kan dan nalopen welke staat van het product onder `0.2.0` valt,
en een document dat die versie aanhaalt wijst naar iets wat niet meer terug te vinden is.
Het versiemanifest van de platen (`architecture/model/bron/versiemanifest.json`) loste dat
op voor drie platen; `versies.json` per product maakt er een vorm voor elk product van.

Drie lagen, elk met een eigen controle:

1. `architecture/producten/manifest.json` noemt per product de map, de actuele versie, de
   commit en de tag.
2. Elke productmap draagt `versies.json` met per versie: nummer, commit, tag, datum en de
   verwijzing naar de release-notes.
3. Elke map onder `architecture/producten/` staat in het manifest, en elk product in het
   manifest heeft een map.

Een commit is altijd de volledige veertigtekenhash. Een afkorting is een prefix waarvan de
uniciteit alleen geldt op het moment van schrijven; git schaalt zijn afkortlengte mee met
het aantal objecten in de repository. Dezelfde regel staat in
`tools/scripts/maak-versiemanifest-plaat.py`.

De regel staat in `.cursor/rules/mapindeling.mdc` en in AGENTS.md onder Mapindeling.
"""

import json
import pathlib
import re
import subprocess
import tempfile
import unittest

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent
PRODUCTEN = "architecture/producten"

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
DATUM = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MANIFEST_SLEUTELS = ("map", "huidig", "commit", "tag")
VERSIE_SLEUTELS = ("versie", "commit", "tag", "datum", "release_notes")


def getal(versie):
    return tuple(int(x) for x in versie.split("."))


def lees_json(pad, fouten):
    try:
        return json.loads(pad.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as fout:
        fouten.append(f"{pad.name}: niet te lezen als JSON ({fout})")
        return None


def controleer_versie(product, v, fouten):
    """Een versie draagt alle sleutels, een semver-nummer en een volledige commit."""
    naam = f"{product} {v.get('versie', '?')}"
    for sleutel in VERSIE_SLEUTELS:
        if sleutel not in v:
            fouten.append(f"{naam}: sleutel '{sleutel}' ontbreekt")
    nummer = v.get("versie") or ""
    if not SEMVER.match(nummer):
        fouten.append(f"{naam}: versie '{nummer}' is geen MAJOR.MINOR.PATCH")
    commit = v.get("commit") or ""
    if not commit:
        fouten.append(f"{naam}: versie zonder commit")
    elif not COMMIT.match(commit):
        fouten.append(f"{naam}: commit '{commit}' is geen volledige veertigtekenhash")
    if "datum" in v and not DATUM.match(v.get("datum") or ""):
        fouten.append(f"{naam}: datum '{v.get('datum')}' is geen JJJJ-MM-DD")
    if "tag" in v and not isinstance(v["tag"], str):
        fouten.append(f"{naam}: tag is een tekst, leeg zolang er geen tag is")


def controleer(wortel):
    """Alle fouten in de productenmap onder `wortel`, als lijst van regels."""
    wortel = pathlib.Path(wortel)
    basis = wortel / PRODUCTEN
    fouten = []
    manifest = lees_json(basis / "manifest.json", fouten)
    if manifest is None:
        return fouten
    producten = manifest.get("producten", {})

    mappen = sorted(p.name for p in basis.iterdir() if p.is_dir())
    for naam in mappen:
        if naam not in producten:
            fouten.append(f"{naam}: map onder {PRODUCTEN}/ zonder regel in manifest.json")

    for naam, regel in sorted(producten.items()):
        for sleutel in MANIFEST_SLEUTELS:
            if sleutel not in regel:
                fouten.append(f"{naam}: sleutel '{sleutel}' ontbreekt in manifest.json")
        verwacht = f"{PRODUCTEN}/{naam}"
        if regel.get("map") != verwacht:
            fouten.append(f"{naam}: map in manifest.json is '{regel.get('map')}', verwacht '{verwacht}'")
        productmap = wortel / verwacht
        if not productmap.is_dir():
            fouten.append(f"{naam}: product in manifest.json zonder map")
            continue
        if not (productmap / "README.md").is_file():
            fouten.append(f"{naam}: map zonder README.md")
        versiepad = productmap / "versies.json"
        if not versiepad.is_file():
            fouten.append(f"{naam}: map zonder versies.json")
            continue
        versies = lees_json(versiepad, fouten)
        if versies is None:
            continue
        lijst = versies.get("versies", [])
        for v in lijst:
            controleer_versie(naam, v, fouten)
        nummers = [v.get("versie") for v in lijst if SEMVER.match(v.get("versie") or "")]
        if nummers != sorted(nummers, key=getal) or len(set(nummers)) != len(nummers):
            fouten.append(f"{naam}: versies staan niet oplopend of dubbel in versies.json")

        huidig = regel.get("huidig") or ""
        if not lijst:
            if huidig or regel.get("commit") or regel.get("tag"):
                fouten.append(f"{naam}: manifest noemt een versie, versies.json is leeg")
            continue
        laatste = lijst[-1]
        if versies.get("huidig") != laatste.get("versie"):
            fouten.append(f"{naam}: 'huidig' in versies.json is niet de laatste versie")
        if huidig != laatste.get("versie"):
            fouten.append(f"{naam}: manifest noemt {huidig or 'geen versie'}, "
                          f"versies.json {laatste.get('versie')}")
        if regel.get("commit") != laatste.get("commit"):
            fouten.append(f"{naam}: commit in manifest.json wijkt af van versies.json")
        if regel.get("tag") != laatste.get("tag"):
            fouten.append(f"{naam}: tag in manifest.json wijkt af van versies.json")
    return fouten


class EchteRepositoryTests(unittest.TestCase):
    """De productenmap zelf."""

    def test_given_the_products_folder_when_checked_then_there_are_no_findings(self):
        fouten = controleer(WORTEL)
        self.assertEqual(fouten, [], "\n".join(fouten))

    def test_given_every_recorded_commit_when_looked_up_then_it_exists(self):
        """Een volledige hash die niet bestaat is net zo leeg als een afkorting."""
        basis = WORTEL / PRODUCTEN
        manifest = json.loads((basis / "manifest.json").read_text(encoding="utf-8"))
        for naam in manifest["producten"]:
            versies = json.loads((basis / naam / "versies.json").read_text(encoding="utf-8"))
            for v in versies["versies"]:
                with self.subTest(product=naam, versie=v["versie"]):
                    uit = subprocess.run(["git", "cat-file", "-e", f"{v['commit']}^{{commit}}"],
                                         cwd=WORTEL, capture_output=True)
                    self.assertEqual(uit.returncode, 0, f"commit {v['commit']} bestaat niet")

    def test_given_the_reader_guide_when_read_then_it_links_every_product_folder(self):
        """De README van de productenmap is de ingang: elk product staat erin."""
        basis = WORTEL / PRODUCTEN
        tekst = (basis / "README.md").read_text(encoding="utf-8")
        manifest = json.loads((basis / "manifest.json").read_text(encoding="utf-8"))
        for naam in manifest["producten"]:
            with self.subTest(product=naam):
                self.assertIn(f"]({naam}/", tekst)


class GemaakteMapTests(unittest.TestCase):
    """De controles op een gemaakte productenmap, een geval per fout."""

    COMMIT_A = "a" * 40
    COMMIT_B = "b" * 40

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.wortel = pathlib.Path(self._tmp.name)
        self.basis = self.wortel / PRODUCTEN
        self.basis.mkdir(parents=True)
        self.regels = {}

    def tearDown(self):
        self._tmp.cleanup()

    def versie(self, nummer="0.1.0", commit=None, tag=""):
        return {"versie": nummer, "commit": self.COMMIT_A if commit is None else commit,
                "tag": tag, "datum": "2026-11-19", "release_notes": "README.md#versies"}

    def product(self, naam="plaat", versies=None, manifest=True, versiebestand=True, map_=True):
        versies = [self.versie()] if versies is None else versies
        if map_:
            productmap = self.basis / naam
            productmap.mkdir()
            (productmap / "README.md").write_text("# Plaat\n", encoding="utf-8")
            if versiebestand:
                huidig = versies[-1]["versie"] if versies else ""
                (productmap / "versies.json").write_text(
                    json.dumps({"product": naam, "huidig": huidig, "versies": versies}),
                    encoding="utf-8")
        if manifest:
            laatste = versies[-1] if versies else {"versie": "", "commit": "", "tag": ""}
            self.regels[naam] = {"map": f"{PRODUCTEN}/{naam}", "huidig": laatste["versie"],
                                 "commit": laatste.get("commit", ""), "tag": laatste["tag"]}
        self.schrijf_manifest()

    def schrijf_manifest(self):
        (self.basis / "manifest.json").write_text(json.dumps({"producten": self.regels}),
                                                  encoding="utf-8")

    def test_given_a_complete_product_when_checked_then_there_are_no_findings(self):
        self.product()
        self.assertEqual(controleer(self.wortel), [])

    def test_given_a_version_without_commit_when_checked_then_it_fails(self):
        self.product(versies=[self.versie(commit="")])
        self.assertTrue(any("zonder commit" in f for f in controleer(self.wortel)))

    def test_given_a_version_with_a_missing_commit_key_when_checked_then_it_fails(self):
        v = self.versie()
        del v["commit"]
        self.product(versies=[v])
        self.assertTrue(any("'commit' ontbreekt" in f for f in controleer(self.wortel)))

    def test_given_an_abbreviated_commit_when_checked_then_it_fails(self):
        self.product(versies=[self.versie(commit="241d165")])
        self.assertTrue(any("veertigtekenhash" in f for f in controleer(self.wortel)))

    def test_given_a_product_in_the_manifest_without_folder_when_checked_then_it_fails(self):
        self.product(map_=False)
        self.assertTrue(any("zonder map" in f for f in controleer(self.wortel)))

    def test_given_a_product_without_versions_file_when_checked_then_it_fails(self):
        self.product(versiebestand=False)
        self.assertTrue(any("zonder versies.json" in f for f in controleer(self.wortel)))

    def test_given_a_folder_without_manifest_entry_when_checked_then_it_fails(self):
        self.product(manifest=False)
        self.assertTrue(any("zonder regel in manifest.json" in f for f in controleer(self.wortel)))

    def test_given_a_manifest_behind_the_versions_file_when_checked_then_it_fails(self):
        self.product(versies=[self.versie(), self.versie("0.2.0", self.COMMIT_B)])
        self.regels["plaat"]["huidig"] = "0.1.0"
        self.schrijf_manifest()
        self.assertTrue(any("manifest noemt 0.1.0" in f for f in controleer(self.wortel)))

    def test_given_versions_out_of_order_when_checked_then_it_fails(self):
        self.product(versies=[self.versie("0.2.0"), self.versie("0.1.0", self.COMMIT_B)])
        self.assertTrue(any("oplopend" in f for f in controleer(self.wortel)))

    def test_given_a_version_that_is_not_semver_when_checked_then_it_fails(self):
        self.product(versies=[self.versie("0.2")])
        self.assertTrue(any("MAJOR.MINOR.PATCH" in f for f in controleer(self.wortel)))

    def test_given_a_product_without_released_version_when_checked_then_it_passes(self):
        """Een product zonder uitgebrachte versie draagt een lege lijst en lege velden."""
        self.product(versies=[])
        self.assertEqual(controleer(self.wortel), [])


if __name__ == "__main__":
    unittest.main()
