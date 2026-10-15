"""Testgevallen voor scripts/controleer-schema-binding.py.

Elk geval bouwt zijn eigen binding, informatiemodel en schemamap, zodat de verwachting uit het
fixture volgt en elk negatief geval precies een regel breekt. Het laatste geval draait de
poort op de binding in deze repository.
"""

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
BINDING = WORTEL / "architecture/model/informatiemodel/schema-binding.json"
MODEL = WORTEL / "architecture/model/informatiemodel/informatiemodel.json"

spec = importlib.util.spec_from_file_location(
    "binding", WORTEL / "scripts/controleer-schema-binding.py")
cb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cb)

OBJECTTYPEN = {"Opleiding specificatie", "Leeruitkomst"}
BRONSOORTEN = {"schema": "x", "ingevuld": "y", "ontbreekt": "z"}


def binding(**af):
    uit = {"bronsoorten": dict(BRONSOORTEN), "schemas": {}, "objecttypen": {}}
    uit.update(af)
    return uit


def attribuut(**af):
    uit = {"naam": "id", "datatype": "identificatie", "kardinaliteit": "1..1",
           "rol": "sleutel", "bron": "schema education-specification.json"}
    uit.update(af)
    return uit


def schemamap(namen):
    map_ = Path(tempfile.mkdtemp())
    for naam in namen:
        (map_ / naam).write_text("{}", encoding="utf-8")
    return cb.schemabestanden([map_])


def waarover(bevindingen):
    return " | ".join(str(b) for b in bevindingen)


class HetSchema(unittest.TestCase):
    """Of een schema een begrip draagt of vervoer is, en of dat klopt."""

    def toets(self, gegeven, bestanden=("x.json",)):
        return cb.controleer(binding(schemas={"x.json": gegeven}), OBJECTTYPEN, schemamap(bestanden))

    def test_given_een_begripsschema_met_objecttypen_when_toetsen_then_blijft_het_zonder_bevinding(self):
        self.assertEqual(self.toets({"soort": "begrip", "draagt": ["Leeruitkomst"]}), [])

    def test_given_een_vervoersschema_met_een_reden_when_toetsen_then_blijft_het_zonder_bevinding(self):
        self.assertEqual(self.toets({"soort": "vervoer", "reden": "richt het kanaal in"}), [])

    def test_given_een_vervoersschema_dat_een_objecttype_draagt_when_toetsen_then_een_bevinding(self):
        """Vervoer en begrip tegelijk kan niet; dan is de indeling fout."""
        uit = self.toets({"soort": "vervoer", "reden": "x", "draagt": ["Leeruitkomst"]})
        self.assertIn("draagt geen objecttype", waarover(uit))

    def test_given_een_vervoersschema_zonder_reden_when_toetsen_then_een_bevinding(self):
        self.assertIn("zegt waarom", waarover(self.toets({"soort": "vervoer"})))

    def test_given_een_begripsschema_zonder_objecttype_when_toetsen_then_een_bevinding(self):
        self.assertIn("noemt de objecttypen", waarover(self.toets({"soort": "begrip"})))

    def test_given_een_objecttype_buiten_het_model_when_toetsen_then_een_bevinding(self):
        uit = self.toets({"soort": "begrip", "draagt": ["Verzonnen type"]})
        self.assertIn("is geen objecttype in het model", waarover(uit))

    def test_given_een_schema_dat_nergens_staat_when_toetsen_then_een_bevinding(self):
        uit = self.toets({"soort": "begrip", "draagt": ["Leeruitkomst"]}, bestanden=())
        self.assertIn("staat in geen van de schemamappen", waarover(uit))

    def test_given_een_onbekende_soort_when_toetsen_then_een_bevinding(self):
        self.assertIn("soort is", waarover(self.toets({"soort": "iets anders"})))

    def test_given_een_discriminator_naar_een_onbekend_type_when_toetsen_then_een_bevinding(self):
        uit = self.toets({"soort": "begrip", "draagt": ["Leeruitkomst"],
                          "discriminator": {"pad": "x", "waarden": {"a": "Verzonnen"}}})
        self.assertIn("discriminator a", waarover(uit))


class DeAttribuutsoort(unittest.TestCase):
    """Elke attribuutsoort draagt zijn velden en zijn bron."""

    def toets(self, attributen, objecttype="Leeruitkomst"):
        return cb.controleer(binding(objecttypen={objecttype: {"attributen": attributen}}),
                             OBJECTTYPEN, {})

    def test_given_een_volledige_attribuutsoort_when_toetsen_then_blijft_het_zonder_bevinding(self):
        self.assertEqual(self.toets([attribuut()]), [])

    def test_given_een_attribuutsoort_zonder_bron_when_toetsen_then_een_bevinding(self):
        """De bron is het hele punt van dit bestand."""
        self.assertIn("bron ontbreekt", waarover(self.toets([attribuut(bron="")])))

    def test_given_een_attribuutsoort_zonder_kardinaliteit_when_toetsen_then_een_bevinding(self):
        self.assertIn("kardinaliteit ontbreekt", waarover(self.toets([attribuut(kardinaliteit="")])))

    def test_given_een_bronsoort_die_niet_verklaard_is_when_toetsen_then_een_bevinding(self):
        uit = self.toets([attribuut(bron="gokje op basis van ervaring")])
        self.assertIn("is niet verklaard", waarover(uit))

    def test_given_de_bronsoort_ontbreekt_when_toetsen_then_blijft_het_zonder_bevinding(self):
        """Een gat dat benoemd staat is een uitkomst, geen fout."""
        self.assertEqual(self.toets([attribuut(bron="ontbreekt, geen bron in Public of het model")]), [])

    def test_given_dezelfde_naam_tweemaal_when_toetsen_then_een_bevinding(self):
        uit = self.toets([attribuut(), attribuut()])
        self.assertIn("twee keer", waarover(uit))

    def test_given_een_objecttype_buiten_het_model_when_toetsen_then_een_bevinding(self):
        uit = self.toets([attribuut()], objecttype="Verzonnen type")
        self.assertIn("staat niet in het informatiemodel", waarover(uit))


class DeTellingen(unittest.TestCase):

    def test_given_een_binding_when_tellen_then_komt_de_omvang_per_bron(self):
        b = binding(
            schemas={"a.json": {"soort": "begrip", "draagt": ["Leeruitkomst"]},
                     "b.json": {"soort": "vervoer", "reden": "x"}},
            objecttypen={"Leeruitkomst": {"attributen": [attribuut(), attribuut(naam="naam", bron="ingevuld, want de specificatie vraagt hem")]}})
        t = cb.tellingen(b)
        self.assertEqual((t["schemas"], t["per_soort"]["begrip"], t["per_soort"]["vervoer"]), (2, 1, 1))
        self.assertEqual(t["per_bron"], {"schema": 1, "ingevuld": 1})


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return cb.main(argv)

    def schrijf(self, inhoud):
        map_ = Path(tempfile.mkdtemp())
        (map_ / "binding.json").write_text(json.dumps(inhoud), encoding="utf-8")
        (map_ / "model.json").write_text(
            json.dumps({"objecttypen": [{"naam": n} for n in OBJECTTYPEN]}), encoding="utf-8")
        return map_

    def test_given_een_binding_die_aansluit_when_draaien_then_exitcode_nul(self):
        map_ = self.schrijf(binding(objecttypen={"Leeruitkomst": {"attributen": [attribuut()]}}))
        self.assertEqual(self.draai(["--binding", str(map_ / "binding.json"),
                                     "--model", str(map_ / "model.json")]), 0)

    def test_given_een_binding_die_niet_aansluit_when_draaien_then_exitcode_een(self):
        map_ = self.schrijf(binding(objecttypen={"Verzonnen": {"attributen": [attribuut()]}}))
        self.assertEqual(self.draai(["--binding", str(map_ / "binding.json"),
                                     "--model", str(map_ / "model.json")]), 1)

    def test_given_een_bestand_dat_niet_bestaat_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--binding", str(Path(tmp) / "weg.json")]), 2)

    def test_given_een_binding_die_geen_json_is_when_draaien_then_exitcode_twee(self):
        map_ = Path(tempfile.mkdtemp())
        (map_ / "binding.json").write_text("{geen json", encoding="utf-8")
        self.assertEqual(self.draai(["--binding", str(map_ / "binding.json"),
                                     "--model", str(MODEL)]), 2)


class InDezeRepository(unittest.TestCase):

    def test_given_de_binding_in_deze_repository_when_toetsen_then_sluit_zij_aan(self):
        if not BINDING.is_file():
            self.skipTest("schema-binding.json ontbreekt")
        binding_ = json.loads(BINDING.read_text(encoding="utf-8"))
        objecttypen = {o["naam"] for o in json.loads(MODEL.read_text(encoding="utf-8"))["objecttypen"]}
        schemas = cb.schemabestanden([WORTEL / m for m in cb.SCHEMAMAPPEN])
        self.assertEqual([str(b) for b in cb.controleer(binding_, objecttypen, schemas)], [])

    def test_given_de_binding_when_lezen_then_verklaart_zij_elke_bronsoort_die_zij_gebruikt(self):
        if not BINDING.is_file():
            self.skipTest("schema-binding.json ontbreekt")
        binding_ = json.loads(BINDING.read_text(encoding="utf-8"))
        gebruikt = {(a["bron"].split(",")[0].split(" ")[0])
                    for g in binding_["objecttypen"].values() for a in g["attributen"]}
        self.assertTrue(gebruikt <= set(binding_["bronsoorten"]), gebruikt)


if __name__ == "__main__":
    unittest.main()
