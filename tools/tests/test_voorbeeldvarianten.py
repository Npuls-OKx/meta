"""Testgevallen voor de planningsvormen naast de basisuitwerking (#401).

Een variant is een eigen regeltabel naast de basis: voorbeeld-lr1-regels-<vorm>.json. Zij erft de kop
van de basis en draagt per fase haar eigen stappen en regels. De gevallen hieronder bouwen een kleine
basis uit de fixtures van de bestaande tests en zetten daar een variant naast; de verwachtingen volgen
uit die fixtures, niet uit de inhoud van de repository.
"""

import copy
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
SCHEMA = WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.schema.json"
VARIANTSCHEMA = WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-variant.schema.json"


def laad(naam, pad):
    spec = importlib.util.spec_from_file_location(naam, WORTEL / pad)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


vv = laad("voorbeeldvarianten", "tools/scripts/voorbeeldvarianten.py")
cv = laad("controleer_voorbeeldregels", "tools/scripts/controleer-voorbeeldregels.py")
gv = laad("genereer_voorbeeld_lr1", "tools/scripts/genereer-voorbeeld-lr1.py")
tv = laad("teken_voorbeeldregels", "tools/scripts/teken-voorbeeldregels.py")
hl = laad("teken_hoofdplaat_highlight", "tools/scripts/teken-hoofdplaat-highlight.py")
fc = laad("test_controleer_voorbeeldregels", "tools/tests/test_controleer_voorbeeldregels.py")
fg = laad("test_genereer_voorbeeld_lr1", "tools/tests/test_genereer_voorbeeld_lr1.py")


def capaciteit():
    """Een variant op de checker-fixture: in fase 4 een stap die de basis niet kent, met een stroom erbij."""
    return {"basis": "voorbeeld-lr1-regels.json", "vorm": "capaciteitsgestuurd",
            "fasen": [{"nummer": 4, "bron": "instellingspraktijk", "stappen": ["Op capaciteit plannen"],
                       "voorafgegaan_door": ["F3-01"]}],
            "regels": [
                {"beeld_id": "F4-C01", "beeld": "Lesgelegenheid op capaciteit", "fase": 4, "stap": "Op capaciteit plannen",
                 "soort": "ontstaat", "wie": "planner", "objecttype": "Lesgelegenheid", "instantie": "di 13:00, max 24",
                 "nieuwe_instantie": True, "bron": "instellingspraktijk"},
                {"beeld_id": "F4-C02", "beeld": "Aanbod op capaciteit naar de catalogus", "fase": 4, "stap": "Op capaciteit plannen",
                 "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1",
                 "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "Apothekersassistent 2026", "bron": "b"}]}


def geroosterd():
    return {"basis": "voorbeeld-lr1-regels.json", "vorm": "geroosterd",
            "fasen": [{"nummer": 4, "bron": "instellingspraktijk", "stappen": ["Op het rooster opnemen"],
                       "voorafgegaan_door": ["F3-01", "F4-C01", "F4-99"]}],
            "regels": [
                {"beeld_id": "F4-R01", "beeld": "Opgenomen op de les", "fase": 4, "stap": "Op het rooster opnemen",
                 "soort": "verandert", "wie": "planner", "objecttype": "Lesgelegenheid", "instantie": "di 13:00, lokaal 2.14",
                 "toestand": "geroosterd", "bron": "instellingspraktijk"}]}


def schrijf(map_, basis, *varianten, namen=None):
    """De basis en haar varianten als bestanden in een map, zoals ze in de repository naast elkaar staan."""
    map_ = Path(map_)
    pad = map_ / "voorbeeld-lr1-regels.json"
    pad.write_text(json.dumps(basis), encoding="utf-8")
    for i, v in enumerate(varianten):
        naam = (namen or {}).get(i) or f"voorbeeld-lr1-regels-{v['vorm']}.json"
        (map_ / naam).write_text(json.dumps(v), encoding="utf-8")
    return pad


class Variantcontrole(unittest.TestCase):
    """Criteria 1 tot en met 4: erven, verwijzen, beeld-ID's en controle."""

    def controleer(self, *varianten, namen=None, stromen="standaard"):
        with tempfile.TemporaryDirectory() as map_:
            basis = fc.regels()
            pad = schrijf(map_, basis, *varianten, namen=namen)
            geladen, onbekend = vv.laad(pad, basis)
            uit = []
            for v in geladen:
                b, _ = cv.controleer_variant(v, basis, geladen, fc.model(), fc.stromen() if stromen == "standaard" else stromen,
                                             schema_pad=SCHEMA, variantschema=VARIANTSCHEMA)
                uit += b
            return uit, onbekend

    def test_given_variant_without_own_roles_when_checked_then_role_from_basis_counts(self):
        b, _ = self.controleer(capaciteit())
        self.assertEqual([x for x in b if "rol" in x], [])
        self.assertEqual(b, [])

    def test_given_variant_with_unknown_vorm_when_loaded_then_reported(self):
        v = capaciteit(); v["vorm"] = "vrij"
        b, _ = self.controleer(v, namen={0: "voorbeeld-lr1-regels-capaciteitsgestuurd.json"})
        self.assertTrue(any("vrij" in x for x in b))
        _, onbekend = self.controleer(capaciteit(), namen={0: "voorbeeld-lr1-regels-vrij.json"})
        self.assertEqual([p.name for p in onbekend], ["voorbeeld-lr1-regels-vrij.json"])

    def test_given_references_to_basis_variant_and_nothing_when_checked_then_only_the_missing_one_is_found(self):
        b, _ = self.controleer(capaciteit(), geroosterd())
        verwijzing = [x for x in b if "voorafgegaan" in x]
        self.assertEqual(len(verwijzing), 1)
        self.assertIn("F4-99", verwijzing[0])

    def test_given_reference_forward_to_a_later_variant_when_checked_then_found(self):
        v = capaciteit(); v["fasen"][0]["voorafgegaan_door"] = ["F4-R01"]
        b, _ = self.controleer(v, geroosterd())
        self.assertTrue(any("F4-R01" in x and x.startswith("voorbeeld-lr1-regels-capaciteitsgestuurd.json") for x in b))

    def test_given_vervangt_when_checked_then_existing_earlier_image_passes_and_unknown_is_found(self):
        v = geroosterd(); v["fasen"][0]["voorafgegaan_door"] = ["F3-01"]; v["fasen"][0]["vervangt"] = ["F4-01", "F4-77"]
        b, _ = self.controleer(capaciteit(), v)
        vervangt = [x for x in b if "vervangt" in x]
        self.assertEqual(len(vervangt), 1)
        self.assertIn("F4-77", vervangt[0])

    def test_given_variant_fase_not_in_basis_when_checked_then_found(self):
        v = capaciteit(); v["fasen"].append({"nummer": 7, "bron": "b", "stappen": ["Bijsturen"]})
        self.assertTrue(any("fase 7" in x and "basis" in x for x in self.controleer(v)[0]))

    def test_given_variant_that_is_no_valid_json_when_loaded_then_clean_exit(self):
        with tempfile.TemporaryDirectory() as map_:
            pad = schrijf(map_, fc.regels())
            (Path(map_) / "voorbeeld-lr1-regels-geroosterd.json").write_text("{kapot", encoding="utf-8")
            with self.assertRaises(SystemExit):
                vv.laad(pad, fc.regels())

    def test_given_variant_beeld_id_when_validated_then_letter_required_and_must_match_vorm(self):
        self.assertEqual(self.controleer(capaciteit())[0], [])
        v = capaciteit(); v["regels"][0]["beeld_id"] = "F4-01"
        self.assertTrue(any("F4-01" in x for x in self.controleer(v)[0]))
        v = capaciteit(); v["regels"][0]["beeld_id"] = "F4-R01"
        self.assertTrue(any("F4-R01" in x and "capaciteitsgestuurd" in x for x in self.controleer(v)[0]))

    def test_given_variant_with_unknown_arrow_when_checked_then_finding_names_variant_file(self):
        v = capaciteit(); v["regels"][1]["pijl"] = "rel-onbekend"
        b, _ = self.controleer(v)
        self.assertTrue(any(x.startswith("voorbeeld-lr1-regels-capaciteitsgestuurd.json") and "rel-onbekend" in x for x in b))

    def test_given_new_instance_of_type_from_basis_when_checked_then_no_finding(self):
        self.assertFalse(any("nieuwe_instantie" in x for x in self.controleer(capaciteit())[0]))

    def test_given_variant_that_does_not_cover_every_type_when_checked_then_no_coverage_finding(self):
        b, _ = self.controleer(capaciteit())
        self.assertFalse(any("geen ontstaat-regel" in x or "fase-verwachting" in x or "uitwisseling" in x for x in b))

    def test_given_basis_alone_when_checked_then_result_equal_to_before(self):
        voor = fc.bevindingen()
        with tempfile.TemporaryDirectory() as map_:
            pad = schrijf(map_, fc.regels())
            self.assertEqual(vv.laad(pad, fc.regels()), ([], []))
        self.assertEqual(fc.bevindingen(), voor)


def gen_variant():
    """Een variant op de generator-fixture: in fase 3 een eigen stap, voorafgegaan door F3-01 uit de basis."""
    return {"basis": "voorbeeld-lr1-regels.json", "vorm": "capaciteitsgestuurd",
            "fasen": [{"nummer": 3, "bron": "instellingspraktijk", "stappen": ["Op capaciteit kiezen"],
                       "voorafgegaan_door": ["F3-01"], "toelichting": "De keuze landt op een geplande gelegenheid."}],
            "regels": [
                {"beeld_id": "F3-C01", "beeld": "Keuze op de geplande gelegenheid", "fase": 3, "stap": "Op capaciteit kiezen",
                 "soort": "stroomt", "van": "Planningssysteem", "naar": "Onderwijscatalogus", "pijl": "rel-1",
                 "koppeling": "OC-P&R", "objecttype": "Opleidingaanbod", "instantie": "AA 2026, max 24", "bron": "b"}]}


class VariantDocument(unittest.TestCase):
    """Criteria 5, 6 en 8: het deel van de variant in het document, de hoofdplaat per vorm, en niets
    verandert zolang er geen variant is."""

    def geladen(self):
        basis = fg.regels()
        return basis, [{"vorm": "capaciteitsgestuurd", "pad": Path("voorbeeld-lr1-regels-capaciteitsgestuurd.json"),
                        "bron": gen_variant(), "tabel": vv.samenvoegen(basis, gen_variant())}]

    def test_given_variant_in_fase_3_when_generated_then_part_under_basis_with_reference_first(self):
        basis, varianten = self.geladen()
        doc = gv.bouw(basis, fg.model(), fg.begrippen(), varianten=varianten)
        fase3 = doc.split("## Fase 3:")[1].split("## Fase 4:")[0]
        self.assertLess(fase3.index("### F3-01 - De aanmelding"), fase3.index("### Variant capaciteitsgestuurd"))
        deel = fase3.split("### Variant capaciteitsgestuurd")[1]
        self.assertIn("De keuze landt op een geplande gelegenheid.", deel)
        self.assertIn("(#f3-01---de-aanmelding)", deel)
        self.assertLess(deel.index("#f3-01---de-aanmelding"), deel.index("#### F3-C01 - Keuze op de geplande gelegenheid"))
        self.assertIn("img/regels/f3-c01-keuze-op-de-geplande-gelegenheid.svg", deel)

    def test_given_vervangt_when_generated_then_shown_as_link_after_the_reference(self):
        basis = fg.regels()
        v = gen_variant(); v["fasen"][0]["vervangt"] = ["F3-01"]
        varianten = [{"vorm": "capaciteitsgestuurd", "pad": Path("x.json"), "bron": v, "tabel": vv.samenvoegen(basis, v)}]
        deel = gv.bouw(basis, fg.model(), fg.begrippen(), varianten=varianten).split("### Variant capaciteitsgestuurd")[1]
        self.assertIn("Vervalt in deze vorm of schuift hierheen: [F3-01](#f3-01---de-aanmelding).", deel)
        self.assertLess(deel.index("Hieraan gaan vooraf"), deel.index("Vervalt in deze vorm"))

    def test_given_variant_when_drawn_then_file_names_match_document(self):
        basis, varianten = self.geladen()
        doc = gv.bouw(basis, fg.model(), fg.begrippen(), varianten=varianten)
        verwezen = sorted(set(re.findall(r"img/regels/([^)]+)", doc)))
        with tempfile.TemporaryDirectory() as map_:
            getekend = [n for n, _ in tv.teken(basis, map_)] + [n for n, _ in tv.teken(varianten[0]["tabel"], map_)]
        self.assertEqual(verwezen, sorted(getekend))

    def test_given_variant_when_plates_listed_then_one_per_fase_and_vorm_with_only_its_flows(self):
        _, varianten = self.geladen()
        platen = hl.platen_per_variant(varianten)
        self.assertEqual([naam for naam, _ in platen], ["f3-capaciteitsgestuurd.svg"])
        stromen = platen[0][1]
        self.assertEqual(list(stromen), [("Planningssysteem", "Onderwijscatalogus", "rel-1")])
        self.assertEqual(stromen[("Planningssysteem", "Onderwijscatalogus", "rel-1")], ["F3-C01"])

    def test_given_variant_plate_on_disk_when_generated_then_shown_in_variant_part(self):
        basis, varianten = self.geladen()
        with tempfile.TemporaryDirectory() as map_:
            oud, gv.PLATEN = gv.PLATEN, Path(map_)
            try:
                (Path(map_) / "f3-capaciteitsgestuurd.svg").write_text("<svg/>", encoding="utf-8")
                doc = gv.bouw(basis, fg.model(), fg.begrippen(), varianten=varianten)
            finally:
                gv.PLATEN = oud
        deel = doc.split("### Variant capaciteitsgestuurd")[1].split("## Fase 4:")[0]
        self.assertIn("img/hoofdplaat/f3-capaciteitsgestuurd.svg", deel)

    def test_given_no_variant_when_generated_then_document_unchanged(self):
        basis = fg.regels()
        self.assertEqual(gv.bouw(basis, fg.model(), fg.begrippen()),
                         gv.bouw(basis, fg.model(), fg.begrippen(), varianten=[]))
        self.assertNotIn("Variant", gv.bouw(basis, fg.model(), fg.begrippen()))


class Persona(unittest.TestCase):
    """Criterium 7."""

    def test_given_personas_readme_when_read_then_onderwijsplanner_linked(self):
        tekst = (WORTEL / ".agents/personas/README.md").read_text(encoding="utf-8")
        self.assertIn("[Onderwijsplanner](onderwijsplanner.md)", tekst)
        self.assertTrue((WORTEL / ".agents/personas/onderwijsplanner.md").exists())


if __name__ == "__main__":
    unittest.main()
