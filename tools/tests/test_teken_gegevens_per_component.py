"""Testgevallen voor tools/scripts/teken-gegevens-per-component.py.

Elk geval bouwt zijn eigen paar bestanden: een markeerbestand met de stromen van een keten en
een regelbestand met de voorbeeldregels. De verwachting volgt daarmee uit het fixture, en de
laatste twee gevallen draaien op de bestanden van deze repository.
"""

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
STROMEN = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod/stromen-onderwijsaanbod.json"
REGELS = WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json"

spec = importlib.util.spec_from_file_location(
    "teken_gegevens", WORTEL / "tools/scripts/teken-gegevens-per-component.py"
)
tg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tg)


def stroom(aanduiding, van, naar, beeld, kort=""):
    return {"aanduiding": aanduiding, "van": van, "naar": naar, "beeld": beeld,
            "naam_kort": kort or aanduiding.lower()}


def regel(beeld, van, naar, objecttype, soort="stroomt"):
    return {"beeld_id": beeld, "soort": soort, "van": van, "naar": naar,
            "objecttype": objecttype, "instantie": "een waarde"}


def maak(stromen, regels):
    """De twee bronbestanden als fixture op schijf, met hun paden terug."""
    map_ = Path(tempfile.mkdtemp())
    (map_ / "stromen.json").write_text(json.dumps({"stromen": stromen}), encoding="utf-8")
    (map_ / "regels.json").write_text(json.dumps({"regels": regels}), encoding="utf-8")
    return map_ / "stromen.json", map_ / "regels.json"


class WatEenComponentBezit(unittest.TestCase):
    """Een component bezit het objecttype waarvan hij het bronsysteem is."""

    def test_given_een_stroom_in_de_keten_when_lezen_then_bezit_de_bron_dat_objecttype(self):
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst")])
        kolommen, _ = tg.lees(*paden)
        bezit = dict(kolommen)
        self.assertEqual(bezit["Ontwerptool"], {"IS-OA-01": {"Leeruitkomst"}})
        self.assertEqual(bezit["Catalogus"], {})

    def test_given_een_beeld_buiten_de_keten_when_lezen_then_telt_het_niet_mee(self):
        """Een beeld dat deze keten niet draagt, hoort niet op deze plaat."""
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst"),
                      regel("F4-02", "Catalogus", "LMS", "Lesmateriaal")])
        bezit = dict(tg.lees(*paden)[0])
        self.assertNotIn("LMS", bezit)
        self.assertEqual(bezit["Catalogus"], {})

    def test_given_een_ontstaat_regel_when_lezen_then_telt_zij_niet_als_bezit(self):
        """Bezit volgt uit stromen: wie het verstuurt, is de bron ervan."""
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
                     [regel("F1-12", None, None, "Kerntaak", soort="ontstaat")])
        self.assertEqual(dict(tg.lees(*paden)[0])["Ontwerptool"], {})

    def test_given_twee_stromen_uit_een_component_when_lezen_then_blijven_zij_apart(self):
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12"),
                      stroom("IS-OA-02", "Ontwerptool", "Catalogus", "F1-13")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst"),
                      regel("F1-13", "Ontwerptool", "Catalogus", "Onderwijsvorm specificatie")])
        self.assertEqual(sorted(dict(tg.lees(*paden)[0])["Ontwerptool"]), ["IS-OA-01", "IS-OA-02"])

    def test_given_hetzelfde_objecttype_tweemaal_when_lezen_then_staat_het_er_een_keer(self):
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst"),
                      regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst")])
        self.assertEqual(dict(tg.lees(*paden)[0])["Ontwerptool"]["IS-OA-01"], {"Leeruitkomst"})


class DePlaat(unittest.TestCase):
    """Wat er in de svg terechtkomt."""

    def test_given_een_component_dat_alleen_ontvangt_when_tekenen_then_zegt_de_plaat_dat(self):
        """Een leeg vak leest als een gegeven dat vergeten is."""
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst")])
        kolommen, namen = tg.lees(*paden)
        svg = tg.teken(kolommen, namen, "Een titel")
        self.assertIn("ontvangt, bezit hier niets", svg)

    def test_given_een_korte_naam_bij_een_stroom_when_tekenen_then_staat_die_bij_de_groep(self):
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12", kort="ontwerp")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst")])
        svg = tg.teken(*tg.lees(*paden), "Een titel")
        self.assertIn("IS-OA-01 ontwerp", svg)

    def test_given_een_lange_objecttypenaam_when_tekenen_then_valt_zij_over_twee_regels(self):
        lang = "Studiebelasting en begeleide onderwijstijd indicatie"
        self.assertEqual(len(tg.knip(lang, tg.KOLOM - 44)), 2)

    def test_given_een_naam_die_in_twee_regels_niet_past_when_knippen_then_eindigt_zij_met_een_beletselteken(self):
        self.assertTrue(tg.knip("woord " * 40, 100)[-1].endswith("…"))

    def test_given_de_plaat_when_tekenen_then_draagt_zij_haar_herkomst(self):
        """Een plaat die niet zegt waar zij vandaan komt, leest als een bewering."""
        paden = maak([stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
                     [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst")])
        self.assertIn("voorbeeld-lr1-regels.json", tg.teken(*tg.lees(*paden), "Een titel"))


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return tg.main(argv)

    def test_given_beide_bronbestanden_when_tekenen_then_exitcode_nul_en_een_svg(self):
        stromen_pad, regels_pad = maak(
            [stroom("IS-OA-01", "Ontwerptool", "Catalogus", "F1-12")],
            [regel("F1-12", "Ontwerptool", "Catalogus", "Leeruitkomst")])
        uit = stromen_pad.parent / "plaat.svg"
        self.assertEqual(self.draai(["--stromen", str(stromen_pad), "--regels", str(regels_pad),
                                     "--uit", str(uit)]), 0)
        self.assertTrue(uit.read_text(encoding="utf-8").startswith("<svg"))

    def test_given_een_bronbestand_dat_ontbreekt_when_tekenen_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--stromen", str(Path(tmp) / "weg.json")]), 2)

    def test_given_een_markeerbestand_zonder_stroom_when_tekenen_then_exitcode_twee(self):
        stromen_pad, regels_pad = maak([], [])
        self.assertEqual(
            self.draai(["--stromen", str(stromen_pad), "--regels", str(regels_pad),
                        "--uit", str(stromen_pad.parent / "p.svg")]), 2)


class InDezeRepository(unittest.TestCase):

    def test_given_de_keten_van_deze_repository_when_lezen_then_bezit_elk_component_zijn_gegevens(self):
        kolommen, namen = tg.lees(STROMEN, REGELS)
        bezit = dict(kolommen)
        self.assertIn("Curriculum ontwerptool", bezit)
        self.assertIn("Onderwijscatalogus", bezit)
        alle = set().union(*bezit["Curriculum ontwerptool"].values())
        self.assertIn("Leeruitkomst", alle)
        self.assertIn("IS-OA-01", namen)
        self.assertNotEqual(namen["IS-OA-01"], "IS-OA-01")

    def test_given_de_getekende_plaat_when_lezen_then_staat_zij_naast_de_specificatie(self):
        plaat = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod/img/gegevens-per-component.svg"
        if not plaat.is_file():
            self.skipTest("de plaat ontbreekt; draai eerst het script")
        tekst = plaat.read_text(encoding="utf-8")
        self.assertIn("Curriculum ontwerptool", tekst)
        self.assertIn("ontvangt, bezit hier niets", tekst)


if __name__ == "__main__":
    unittest.main()
