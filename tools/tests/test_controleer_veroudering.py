"""Testgevallen voor tools/scripts/controleer-veroudering.py.

Een controle die meldt wat niet verouderd is, wordt genegeerd. Per veroudergang staat daarom
een geval dat meldt naast een geval dat zwijgt.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
spec = importlib.util.spec_from_file_location("veroudering", WORTEL / "tools/scripts/controleer-veroudering.py")
vero = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vero)


class Basis(unittest.TestCase):
    def meld(self, tekst, hoogste="1.7a"):
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "doc.md"
            pad.write_text(tekst, encoding="utf-8")
            meldingen, _, _ = vero.controleer([pad], Path(tmp), hoogste)
        return meldingen


class PlaatversieTests(Basis):
    def test_given_an_older_plaatversie_when_checked_then_it_reports_the_version(self):
        meldingen = self.meld("Zie de hoofdplaat informatiestromen v1.7 hieronder.")
        self.assertEqual(len(meldingen), 1)
        self.assertIn("v1.7 en de hoogste is v1.7a", meldingen[0])

    def test_given_the_highest_plaatversie_when_checked_then_it_is_silent(self):
        self.assertEqual(self.meld("Zie de hoofdplaat v1.7a hieronder."), [])

    def test_given_a_version_far_from_the_word_hoofdplaat_when_checked_then_it_is_silent(self):
        self.assertEqual(self.meld("De koppelvlakspecificatie staat op v0.0.2."), [])


class FasebeweringTests(Basis):
    def test_given_a_claim_about_the_phase_when_checked_then_it_reports(self):
        meldingen = self.meld("Het project bevindt zich nu in de fase business architectuur.")
        self.assertTrue(any("stand van het project" in m for m in meldingen))

    def test_given_a_sentence_about_a_phase_of_the_scenario_when_checked_then_it_is_silent(self):
        self.assertEqual(self.meld("In fase 3 meldt de student zich aan."), [])


class VervangenNaamTests(Basis):
    def test_given_a_replaced_name_when_checked_then_it_names_the_decision(self):
        meldingen = self.meld("De stroom loopt naar Student Kiest.")
        self.assertEqual(len(meldingen), 1)
        self.assertIn("ADR 0005", meldingen[0])

    def test_given_the_current_name_when_checked_then_it_is_silent(self):
        self.assertEqual(self.meld("De stroom loopt naar het studentkeuzesysteem."), [])


class UitzonderingTests(Basis):
    def test_given_an_exception_with_a_reason_when_checked_then_it_is_silent(self):
        tekst = ("<!-- veroudering-uitzondering: dit verslag legt de stand van juni 2026 vast -->\n"
                 "Het project bevindt zich nu in de fase business architectuur.")
        self.assertEqual(self.meld(tekst), [])

    def test_given_an_exception_without_a_reason_when_checked_then_it_reports_that(self):
        tekst = "<!-- veroudering-uitzondering: -->\nDe stroom loopt naar Student Kiest."
        meldingen = self.meld(tekst)
        self.assertEqual(len(meldingen), 1)
        self.assertIn("zonder reden", meldingen[0])


class LeestAlleenTests(unittest.TestCase):
    def test_given_a_run_when_it_finishes_then_no_file_changed(self):
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "doc.md"
            pad.write_text("De hoofdplaat v1.6 staat hier.", encoding="utf-8")
            voor = pad.read_bytes(), pad.stat().st_mtime_ns
            vero.controleer([pad], Path(tmp), "1.7a")
            self.assertEqual((pad.read_bytes(), pad.stat().st_mtime_ns), voor)

    def test_given_a_repository_without_the_model_when_asked_then_the_version_is_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(vero.hoogste_plaatversie(Path(tmp) / "stromen.json"))

    def test_given_no_known_version_when_checked_then_plaatversie_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "doc.md"
            pad.write_text("De hoofdplaat v1.6 staat hier.", encoding="utf-8")
            meldingen, _, _ = vero.controleer([pad], Path(tmp), None)
        self.assertEqual(meldingen, [])
