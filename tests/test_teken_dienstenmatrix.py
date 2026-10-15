"""Testgevallen voor scripts/teken-dienstenmatrix.py.

Elk geval bouwt zijn eigen interactieketenspecificatie met een hoofdstuk Koppelvlakdiensten,
zodat de verwachting uit het fixture volgt. Het laatste geval draait op de keten in deze
repository.
"""

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
KETEN = WORTEL / "architecture/docs/specificatie/interactie-onderwijsaanbod/README.md"

spec = importlib.util.spec_from_file_location(
    "matrix", WORTEL / "scripts/teken-dienstenmatrix.py")
dm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dm)

BEKEND = {"onderwijsspecificatiestructuur", "verwerkingsuitkomst"}


def keten(rijen):
    """Een ketenspecificatie met een hoofdstuk Koppelvlakdiensten en de meegegeven rijen."""
    regels = ["# Een keten", "", "## 4. Koppelvlakdiensten", "",
              "| Component | Dienst | Endpoints en meldingen | Eenheid | Stand |",
              "|---|---|---|---|---|"]
    regels += [f"| {c} | {d} | `{e}` | IS-OA-01 | {s} |" for c, d, e, s in rijen]
    regels += ["", "## 5. Verder", "", "tekst", ""]
    map_ = Path(tempfile.mkdtemp())
    (map_ / "README.md").write_text("\n".join(regels), encoding="utf-8")
    return map_ / "README.md"


def waarover(bevindingen):
    return " | ".join(bevindingen)


class DeClaims(unittest.TestCase):
    """Wat er uit het hoofdstuk Koppelvlakdiensten komt."""

    def test_given_een_aanbieder_when_lezen_then_is_de_rol_aanbieder(self):
        rijen = dm.claims(keten([("Catalogus", "onderwijsspecificatiestructuur-aanbieder", "/x", "Vastgelegd")]))
        self.assertEqual(rijen[0]["rol"], "aanbieder")
        self.assertEqual(rijen[0]["onderwerp"], "onderwijsspecificatiestructuur")

    def test_given_een_afnemer_when_lezen_then_is_de_rol_afnemer(self):
        rijen = dm.claims(keten([("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")]))
        self.assertEqual(rijen[0]["rol"], "afnemer")

    def test_given_een_dienstnaam_met_een_toevoeging_when_lezen_then_komt_die_apart(self):
        rijen = dm.claims(keten([("Catalogus", "onderwijsspecificatiestructuur-aanbieder, voor de leeromgeving", "/x", "Vastgelegd")]))
        self.assertEqual(rijen[0]["onderwerp"], "onderwijsspecificatiestructuur")
        self.assertEqual(rijen[0]["toevoeging"], "voor de leeromgeving")


class DePaartoets(unittest.TestCase):
    """Een dienst zonder tegenhanger is een gat in de keten."""

    def test_given_een_aanbieder_en_een_afnemer_when_toetsen_then_blijft_het_zonder_bevinding(self):
        rijen = dm.claims(keten([
            ("Catalogus", "onderwijsspecificatiestructuur-aanbieder", "/x", "Vastgelegd"),
            ("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")]))
        self.assertEqual(dm.bevindingen_van(rijen, BEKEND), [])

    def test_given_alleen_een_afnemer_when_toetsen_then_een_bevinding(self):
        """Dit gat zat in de keten: twee componenten namen verwerkingsuitkomst af, niemand bood hem aan."""
        rijen = dm.claims(keten([("Planning", "verwerkingsuitkomst-afnemer", "/x", "Vastgelegd")]))
        self.assertIn("door geen enkel component aangeboden", waarover(dm.bevindingen_van(rijen, BEKEND)))

    def test_given_alleen_een_aanbieder_when_toetsen_then_een_bevinding(self):
        rijen = dm.claims(keten([("Planning", "verwerkingsuitkomst-aanbieder", "/x", "Vastgelegd")]))
        self.assertIn("door geen enkel component afgenomen", waarover(dm.bevindingen_van(rijen, BEKEND)))

    def test_given_een_dienstnaam_zonder_rol_when_toetsen_then_een_bevinding(self):
        rijen = dm.claims(keten([("Catalogus", "verwerkingsstatus", "/x", "Vastgelegd")]))
        self.assertIn("eindigt niet op aanbieder of afnemer", waarover(dm.bevindingen_van(rijen, BEKEND)))

    def test_given_een_toevoeging_when_toetsen_then_een_bevinding(self):
        rijen = dm.claims(keten([
            ("Catalogus", "onderwijsspecificatiestructuur-aanbieder, voor de leeromgeving", "/x", "Vastgelegd"),
            ("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")]))
        self.assertIn("twee keer wordt ingezet", waarover(dm.bevindingen_van(rijen, BEKEND)))


class HetVoorstel(unittest.TestCase):
    """Een dienst die de dienstenlijst nog niet kent, is een stand en geen fout."""

    def test_given_een_onbekende_dienst_when_toetsen_then_staat_hij_als_voorstel(self):
        rijen = dm.claims(keten([
            ("Catalogus", "aanmeldbaar-onderwijsaanbod-aanbieder", "/x", "Voorstel"),
            ("KRS", "aanmeldbaar-onderwijsaanbod-afnemer", "/x", "Voorstel")]))
        self.assertEqual(dm.voorstellen_van(rijen, BEKEND), ["aanmeldbaar-onderwijsaanbod"])
        self.assertEqual(dm.bevindingen_van(rijen, BEKEND), [])

    def test_given_geen_dienstenlijst_when_toetsen_then_komt_er_geen_voorstel(self):
        """Zonder de lijst valt niets voor te stellen, en dan is zwijgen beter dan gokken."""
        rijen = dm.claims(keten([("Catalogus", "iets-aanbieder", "/x", "x"),
                                 ("KRS", "iets-afnemer", "/x", "x")]))
        self.assertEqual(dm.voorstellen_van(rijen, set()), [])


class DePlaat(unittest.TestCase):

    def test_given_claims_when_tekenen_then_staat_elke_rol_in_de_plaat(self):
        rijen = dm.claims(keten([
            ("Catalogus", "onderwijsspecificatiestructuur-aanbieder", "/x", "Vastgelegd"),
            ("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")]))
        svg = dm.teken(rijen, BEKEND, "Titel")
        self.assertEqual(svg.count('r="4.5"'), 2)
        self.assertEqual(svg.count("A5.5 5.5"), 2)

    def test_given_de_rollen_when_tekenen_then_dragen_zij_de_notatie_van_archimate(self):
        """De bal is de geleverde interface, de kom de gevraagde; samen vallen zij in elkaar."""
        self.assertIn('circle', dm.biedt_svg(0, 0, "#000"))
        self.assertIn('A5.5 5.5', dm.neemt_svg(0, 0, "#000"))

    def test_given_een_voorgestelde_dienst_when_tekenen_then_draagt_de_rij_dat_merk(self):
        rijen = dm.claims(keten([("Catalogus", "nieuw-aanbieder", "/x", "Voorstel")]))
        self.assertIn(">voorstel<", dm.teken(rijen, BEKEND, "Titel"))

    def test_given_een_lange_componentnaam_when_tekenen_then_krijgt_de_kop_een_kleinere_letter(self):
        rijen = dm.claims(keten([("Toetsenexamenafnamesysteemvoorinstellingen", "x-aanbieder", "/x", "x")]))
        self.assertIn('font-size="9"', dm.teken(rijen, BEKEND, "Titel"))


class DePlaatPerInteractie(unittest.TestCase):
    """Een plaat per interactiespecificatie, met de aanbieder links en de afnemer rechts."""

    def rijen(self, rijen):
        return dm.claims(keten(rijen))

    def test_given_een_dienstpaar_in_een_eenheid_when_tekenen_then_komt_de_plaat_eruit(self):
        svg, meldingen = dm.teken_interactie(self.rijen([
            ("Catalogus", "onderwijsspecificatiestructuur-aanbieder", "/x", "Vastgelegd"),
            ("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")]), "IS-OA-01")
        self.assertEqual(meldingen, [])
        self.assertIn("IS-OA-01", svg)
        self.assertIn("Catalogus", svg)
        self.assertIn("Planning", svg)

    def test_given_een_dienst_zonder_afnemer_in_de_eenheid_when_tekenen_then_een_melding(self):
        """Dit gat zat in IS-OA-01: de ontwerptool haalde de structuur op zonder die rol te dragen."""
        _, meldingen = dm.teken_interactie(self.rijen([
            ("Catalogus", "onderwijsspecificatiestructuur-aanbieder", "/x", "Vastgelegd"),
            ("Catalogus", "verwerkingsuitkomst-aanbieder", "/x", "Vastgelegd"),
            ("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")]), "IS-OA-01")
        self.assertEqual(meldingen, ["IS-OA-01: de dienst 'verwerkingsuitkomst' draagt hier geen afnemer"])

    def test_given_een_eenheid_die_niet_voorkomt_when_tekenen_then_geen_plaat(self):
        svg, meldingen = dm.teken_interactie(self.rijen([
            ("Catalogus", "x-aanbieder", "/x", "x")]), "IS-OA-99")
        self.assertIsNone(svg)
        self.assertEqual(meldingen, [])

    def test_given_meer_endpoints_when_tekenen_then_staat_het_aantal_erachter(self):
        svg, _ = dm.teken_interactie(dm.claims(keten([
            ("Catalogus", "x-aanbieder", "/een, /twee, /drie", "x"),
            ("Planning", "x-afnemer", "/een", "x")])), "IS-OA-01")
        self.assertIn("(+2)", svg)


class Exitcode(unittest.TestCase):

    def draai(self, argv):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return dm.main(argv)

    def test_given_een_keten_die_aansluit_when_draaien_then_exitcode_nul(self):
        pad = keten([("Catalogus", "onderwijsspecificatiestructuur-aanbieder", "/x", "Vastgelegd"),
                     ("Planning", "onderwijsspecificatiestructuur-afnemer", "/x", "Vastgelegd")])
        self.assertEqual(self.draai(["--keten", str(pad), "--uit", str(pad.parent / "m.svg")]), 0)

    def test_given_een_dienst_zonder_tegenhanger_when_draaien_then_exitcode_een(self):
        pad = keten([("Planning", "verwerkingsuitkomst-afnemer", "/x", "Vastgelegd")])
        self.assertEqual(self.draai(["--keten", str(pad), "--uit", str(pad.parent / "m.svg")]), 1)

    def test_given_een_keten_die_niet_bestaat_when_draaien_then_exitcode_twee(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.draai(["--keten", str(Path(tmp) / "weg.md")]), 2)


class InDezeRepository(unittest.TestCase):

    def test_given_de_keten_in_deze_repository_when_toetsen_then_heeft_elke_dienst_beide_rollen(self):
        rijen = dm.claims(KETEN)
        self.assertEqual(dm.bevindingen_van(rijen, dm.dienstenlijst()), [])

    def test_given_elke_interactie_in_deze_repository_when_toetsen_then_draagt_elke_dienst_beide_rollen(self):
        rijen = dm.claims(KETEN)
        for n in range(1, 8):
            svg, meldingen = dm.teken_interactie(rijen, f"IS-OA-0{n}")
            self.assertIsNotNone(svg, f"IS-OA-0{n} levert geen plaat")
            self.assertEqual(meldingen, [], f"IS-OA-0{n}")

    def test_given_de_keten_when_lezen_then_claimt_zij_diensten_op_zes_componenten(self):
        rijen = dm.claims(KETEN)
        self.assertGreaterEqual(len({r["component"] for r in rijen}), 6)
        self.assertTrue(all(r["rol"] for r in rijen))


if __name__ == "__main__":
    unittest.main()
