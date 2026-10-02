"""Testgevallen voor scripts/controleer-modelverlies.py.

De controle moet verlies van een concept melden en tegelijk zwijgen over een view die
anders is ingedeeld. Beide kanten staan hier, want een merge die alleen een weergave
verschuift mag geen alarm geven.
"""

import importlib.util
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("verlies", WORTEL / "scripts/controleer-modelverlies.py")
verlies = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verlies)


def model(elementen=(), kinderen=()):
    """Een minimaal .archimate-bestand met de gevraagde elementen en diagramobjecten."""
    e = "".join(f'<element xsi:type="archimate:BusinessObject" id="{i}" name="{n}"/>'
                for i, n in elementen)
    k = "".join(f'<child xsi:type="archimate:DiagramObject" id="{i}" archimateElement="{a}"/>'
                for i, a in kinderen)
    return f'<?xml version="1.0"?><archimate:model xmlns:archimate="http://www.archimatetool.com/archimate">{e}{k}</archimate:model>'


class ElementenTests(unittest.TestCase):
    def test_given_a_model_when_read_then_elements_come_back_with_their_name(self):
        self.assertEqual(verlies.elementen(model([("id-1", "Leeruitkomst")])), {"id-1": "Leeruitkomst"})

    def test_given_a_diagram_object_when_read_then_it_does_not_count_as_a_concept(self):
        m = model([("id-1", "Leeruitkomst")], [("id-9", "id-1")])
        self.assertEqual(list(verlies.elementen(m)), ["id-1"])

    def test_given_an_element_without_a_name_when_read_then_it_still_counts(self):
        m = '<archimate:model><element id="id-7"/></archimate:model>'
        self.assertEqual(verlies.elementen(m), {"id-7": ""})


class VerschilTests(unittest.TestCase):
    def test_given_an_element_that_disappeared_when_compared_then_it_is_reported(self):
        oud = model([("id-1", "Leeruitkomst"), ("id-2", "Keuzedeel")])
        nieuw = model([("id-1", "Leeruitkomst")])
        self.assertEqual(verlies.verschil(oud, nieuw), [("id-2", "Keuzedeel")])

    def test_given_only_a_moved_view_object_when_compared_then_nothing_is_reported(self):
        oud = model([("id-1", "Leeruitkomst")], [("id-9", "id-1")])
        nieuw = model([("id-1", "Leeruitkomst")], [("id-8", "id-1")])
        self.assertEqual(verlies.verschil(oud, nieuw), [])

    def test_given_an_added_element_when_compared_then_nothing_is_reported(self):
        oud = model([("id-1", "Leeruitkomst")])
        nieuw = model([("id-1", "Leeruitkomst"), ("id-2", "Keuzedeel")])
        self.assertEqual(verlies.verschil(oud, nieuw), [])

    def test_given_several_losses_when_compared_then_they_are_sorted_by_name(self):
        oud = model([("id-1", "Zorgvraag"), ("id-2", "Aanbod"), ("id-3", "Keuzedeel")])
        self.assertEqual([n for _, n in verlies.verschil(oud, model())],
                         ["Aanbod", "Keuzedeel", "Zorgvraag"])


class HoofdTests(unittest.TestCase):
    """De uitvoer en de exitcode, want daarop stuurt de CI."""

    def draai(self, oud, nieuw, *extra):
        import tempfile
        m = Path(tempfile.mkdtemp())
        (m / "oud.archimate").write_text(oud, encoding="utf-8")
        (m / "nieuw.archimate").write_text(nieuw, encoding="utf-8")
        import contextlib, io
        uit = io.StringIO()
        import sys
        bewaard = sys.argv
        sys.argv = ["x", str(m / "oud.archimate"), str(m / "nieuw.archimate"), *extra]
        try:
            with contextlib.redirect_stdout(uit):
                code = verlies.main()
        finally:
            sys.argv = bewaard
        return code, uit.getvalue()

    def test_given_nothing_lost_when_run_then_it_passes(self):
        code, uit = self.draai(model([("id-1", "Leeruitkomst")]), model([("id-1", "Leeruitkomst")]))
        self.assertEqual(code, 0)
        self.assertIn("SCHOON", uit)

    def test_given_a_loss_when_run_then_it_fails_and_names_the_element(self):
        code, uit = self.draai(model([("id-1", "Leeruitkomst")]), model())
        self.assertEqual(code, 1)
        self.assertIn("Leeruitkomst", uit)

    def test_given_a_loss_within_the_allowance_when_run_then_it_passes(self):
        code, uit = self.draai(model([("id-1", "Leeruitkomst")]), model(), "--toegestaan", "1")
        self.assertEqual(code, 0)
        self.assertIn("Toegestaan", uit)

    def test_given_no_earlier_version_when_run_then_there_is_nothing_to_compare(self):
        code, uit = self.draai("", model([("id-1", "Leeruitkomst")]))
        self.assertEqual(code, 0)
        self.assertIn("geen eerdere versie", uit)


if __name__ == "__main__":
    unittest.main()
