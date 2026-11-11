"""Testgevallen die de mapindeling afdwingen: de hoofdmap leest, bron bewerkt, gegenereerd schrijft.

Waarom dit een testgeval is en geen losse controle: de werkstroom in CI draait de testgevallen,
dus een los bronbestand naast een document laat de pull request falen. Zonder die poort erodeert
de indeling binnen een maand, want niemand ziet een enkel JSON-bestand erbij komen.

De regel staat in .cursor/rules/mapindeling.mdc en in AGENTS.md onder Waar vind ik wat.

Twee controles:

1. Een documentmap draagt geen los bron- of beeldbestand in haar eigen hoofdmap. Een documentmap
   is een map met ten minste een markdownbestand dat niet README.md heet; een README is de
   leeswijzer van wat er staat en maakt een bronmap nog geen documentmap.
2. Geen map draagt een bronbestand naast een gegenereerd beeld. Een selectiebestand hoort niet
   naast het beeld dat eruit volgt.

Twee soorten uitzondering. BLIJVEND voor een plek die buiten ons om vastligt, met de reden erbij.
WACHT voor een map die nog opgeruimd moet worden, met het issuenummer en het huidige
aantal losse bestanden erbij. Een map op WACHT die
inmiddels voldoet laat de test ook falen: anders blijft de lijst staan nadat het werk gedaan is.
Een map die op WACHT staat en een bestand erbij krijgt laat de test eveneens falen, zodat de
schuld niet in de schaduw groeit.
"""

import collections
import pathlib
import subprocess
import unittest

WORTEL = pathlib.Path(__file__).resolve().parent.parent.parent

DATA = {".json", ".yaml", ".yml", ".csv"}
BEELD = {".jpg", ".jpeg", ".png", ".svg", ".gif", ".webp"}

# Een plek die buiten ons om vastligt. Deze lijst krimpt niet.
BLIJVEND = {
    ".": "skills-lock.json hoort in de wortel, want npx skills schrijft hem daar",
    ".agents": "skills.json is het manifest waar AGENTS.md naar wijst; verplaatsen breekt die ingang",
    ".agents/skills/npuls-huisstijl/references": "gevendorde externe skill; die herschikken we niet",
    ".github/ISSUE_TEMPLATE": "GitHub eist config.yml op deze plek",
    "archief/MOKA/Examen Uitvoering en beoordeling/doc": "gearchiveerd materiaal blijft zoals het was",
    "architecture/agent-artifacts/eerste-vertaalpoging-naar-oeapi-met-ai/doc": (
        "bewaard materiaal van de opgeheven fork; blijft zoals het was"),
    "architecture/agent-artifacts/voorbeelduitwerking-leerroute-1/bron": (
        "de proefopstelling: de twee blokvormen en hun beeld horen bij elkaar als een geheel"),
    "tools/tests/voorbeelden": "testfixtures; de invoer en de verwachte uitvoer horen naast elkaar",
}

# Een map die nog opgeruimd moet worden: het issue dat dat doet, en hoeveel bestanden er nu los
# staan. Dat tweede getal houdt de map tegen om erger te worden terwijl zij wacht.
WACHT = {
    "architecture/model/informatiemodel": (542, 12),
    "architecture/docs/specificatie/begrippen": (543, 3),
    "project": (543, 1),
    "project/img/visueel": (543, 17),
}

HULP = ("zie .cursor/rules/mapindeling.mdc: de hoofdmap draagt wat een mens leest, bron/ wat een "
        "mens bewerkt, gegenereerd/ wat een script schrijft")


def bestanden_per_map(wortel=None):
    """De bestanden in de index, gegroepeerd per map. Niet in de index betekent niet van ons."""
    uit = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True,
                         check=True, cwd=wortel or WORTEL).stdout
    per = collections.defaultdict(set)
    for naam in (n for n in uit.split("\0") if n):
        pad = pathlib.PurePosixPath(naam)
        per[str(pad.parent)].add(pad.name)
    return per


def losse_bestanden(per_map):
    """Per documentmap de losse bron- en beeldbestanden in haar eigen hoofdmap."""
    uit = {}
    for mapnaam, namen in per_map.items():
        if not any(n.endswith(".md") and n != "README.md" for n in namen):
            continue
        los = sorted(n for n in namen if pathlib.PurePosixPath(n).suffix.lower() in DATA | BEELD)
        if los:
            uit[mapnaam] = los
    return uit


def bron_naast_beeld(per_map):
    """Per map de bronbestanden en de beelden die daar samen staan."""
    uit = {}
    for mapnaam, namen in per_map.items():
        data = sorted(n for n in namen if pathlib.PurePosixPath(n).suffix.lower() in DATA)
        beeld = sorted(n for n in namen if pathlib.PurePosixPath(n).suffix.lower() in BEELD)
        if data and beeld:
            uit[mapnaam] = data + beeld
    return uit


def overtreders(per_map):
    """De mappen die niet voldoen, met wat er los staat; de twee controles samen."""
    uit = dict(losse_bestanden(per_map))
    for mapnaam, los in bron_naast_beeld(per_map).items():
        uit.setdefault(mapnaam, los)
    return uit


class EchteRepositoryTests(unittest.TestCase):
    """De repository zelf, tegen de twee controles en de twee uitzonderingenlijsten."""

    @classmethod
    def setUpClass(cls):
        cls.per_map = bestanden_per_map()
        cls.overtreders = overtreders(cls.per_map)

    def test_given_the_repository_when_checked_then_no_unlisted_folder_breaks_the_rule(self):
        """Een map die de regel breekt en op geen lijst staat, laat de test falen."""
        onbekend = {m: los for m, los in self.overtreders.items()
                    if m not in BLIJVEND and m not in WACHT}
        if onbekend:
            regels = "\n".join(f"  {m}: {', '.join(los)}" for m, los in sorted(onbekend.items()))
            self.fail(f"{len(onbekend)} map(pen) breken de mapindeling en staan op geen "
                      f"uitzonderingenlijst:\n{regels}\n\n{HULP}\n\nZet de map op BLIJVEND met een "
                      f"reden, of op WACHT met een issuenummer, of ruim hem op.")

    def test_given_a_folder_on_the_waiting_list_when_it_complies_then_the_test_fails(self):
        """Een uitzondering die wacht op werk en inmiddels voldoet, moet eraf."""
        klaar = sorted(m for m in WACHT if m not in self.overtreders)
        if klaar:
            regels = "\n".join(f"  {m} (issue #{WACHT[m][0]})" for m in klaar)
            self.fail(f"{len(klaar)} map(pen) staan op WACHT maar voldoen inmiddels; haal ze uit "
                      f"de lijst zodat zij niet blijft staan nadat het werk gedaan is:\n{regels}")

    def test_given_a_waiting_folder_when_it_gains_a_file_then_the_test_fails(self):
        """Een map die wacht mag niet erger worden; anders groeit de schuld in de schaduw."""
        gegroeid = []
        for mapnaam, (nummer, aantal) in sorted(WACHT.items()):
            nu = len(self.overtreders.get(mapnaam, []))
            if nu > aantal:
                gegroeid.append(f"  {mapnaam}: {aantal} toen, {nu} nu (issue #{nummer})")
        if gegroeid:
            self.fail("een map die op WACHT staat heeft losse bestanden erbij gekregen; leg het "
                      "nieuwe bestand op zijn plek of ruim de map nu op:\n" + "\n".join(gegroeid))

    def test_given_a_waiting_folder_when_it_shrinks_then_the_count_follows(self):
        """Gaat er een bestand af, dan zakt het getal mee; zo blijft de meter eerlijk."""
        gezakt = []
        for mapnaam, (nummer, aantal) in sorted(WACHT.items()):
            nu = len(self.overtreders.get(mapnaam, []))
            if mapnaam in self.overtreders and nu < aantal:
                gezakt.append(f"  {mapnaam}: {aantal} in de lijst, {nu} werkelijk (issue #{nummer})")
        if gezakt:
            self.fail("het getal in WACHT loopt achter op de werkelijkheid; zet het bij zodat de "
                      "meter blijft werken:\n" + "\n".join(gezakt))

    def test_given_a_permanent_exception_when_it_complies_then_the_test_fails(self):
        """Ook een blijvende uitzondering die niets meer uitzondert, moet eraf."""
        klaar = sorted(m for m in BLIJVEND if m not in self.overtreders)
        if klaar:
            regels = "\n".join(f"  {m}: {BLIJVEND[m]}" for m in klaar)
            self.fail(f"{len(klaar)} blijvende uitzondering(en) zijn niet meer nodig:\n{regels}")

    def test_given_every_permanent_exception_when_read_then_it_carries_a_reason(self):
        """Een uitzondering zonder reden is een gat waar later iets door glipt."""
        for mapnaam, reden in BLIJVEND.items():
            with self.subTest(map=mapnaam):
                self.assertGreater(len(reden.split()), 4,
                                   f"{mapnaam}: de reden is te kort om een keuze te verantwoorden")

    def test_given_every_waiting_exception_when_read_then_it_carries_an_issue(self):
        """Een uitzondering die wacht op werk, wijst naar het issue dat dat werk doet."""
        for mapnaam, waarde in WACHT.items():
            with self.subTest(map=mapnaam):
                self.assertIsInstance(waarde, tuple, f"{mapnaam}: verwacht (issue, aantal)")
                nummer, aantal = waarde
                self.assertIsInstance(nummer, int, f"{mapnaam}: issuenummer ontbreekt")
                self.assertGreater(nummer, 0)
                self.assertGreater(aantal, 0, f"{mapnaam}: een map zonder los bestand hoort niet "
                                              f"op WACHT")

    def test_given_the_two_lists_when_compared_then_no_folder_is_on_both(self):
        """Blijvend en wachtend zijn elkaars tegendeel; samen op de lijst is een fout."""
        self.assertEqual(sorted(set(BLIJVEND) & set(WACHT)), [])


class LosseBestandenTests(unittest.TestCase):
    """De eerste controle, op een gemaakte mapstructuur."""

    def per_map(self, *paden):
        per = collections.defaultdict(set)
        for p in paden:
            pad = pathlib.PurePosixPath(p)
            per[str(pad.parent)].add(pad.name)
        return per

    def test_given_a_document_folder_with_a_loose_json_when_checked_then_it_is_reported(self):
        uit = losse_bestanden(self.per_map("map/doc.md", "map/data.json"))
        self.assertEqual(uit, {"map": ["data.json"]})

    def test_given_a_document_folder_with_a_loose_image_when_checked_then_it_is_reported(self):
        uit = losse_bestanden(self.per_map("map/doc.md", "map/plaat.svg"))
        self.assertEqual(uit, {"map": ["plaat.svg"]})

    def test_given_a_document_folder_with_only_markdown_when_checked_then_nothing_is_reported(self):
        self.assertEqual(losse_bestanden(self.per_map("map/doc.md", "map/README.md")), {})

    def test_given_a_source_folder_with_only_a_readme_when_checked_then_nothing_is_reported(self):
        """Een README is de leeswijzer van wat er staat en maakt een bronmap geen documentmap."""
        self.assertEqual(losse_bestanden(self.per_map("map/README.md", "map/data.json")), {})

    def test_given_the_data_in_a_subfolder_when_checked_then_nothing_is_reported(self):
        uit = losse_bestanden(self.per_map("map/doc.md", "map/bron/data.json"))
        self.assertEqual(uit, {})

    def test_given_a_generated_document_in_the_main_folder_when_checked_then_it_is_allowed(self):
        """Het gaat om de lezer en niet om de maker."""
        uit = losse_bestanden(self.per_map("map/gegenereerd-doc.md", "map/gegenereerd/data.json"))
        self.assertEqual(uit, {})


class BronNaastBeeldTests(unittest.TestCase):
    """De tweede controle: een selectiebestand hoort niet naast het beeld dat eruit volgt."""

    def per_map(self, *paden):
        per = collections.defaultdict(set)
        for p in paden:
            pad = pathlib.PurePosixPath(p)
            per[str(pad.parent)].add(pad.name)
        return per

    def test_given_a_selection_next_to_its_image_when_checked_then_it_is_reported(self):
        uit = bron_naast_beeld(self.per_map("img/keuze.json", "img/keuze.svg"))
        self.assertEqual(uit, {"img": ["keuze.json", "keuze.svg"]})

    def test_given_only_images_when_checked_then_nothing_is_reported(self):
        self.assertEqual(bron_naast_beeld(self.per_map("img/a.svg", "img/b.svg")), {})

    def test_given_only_selections_when_checked_then_nothing_is_reported(self):
        self.assertEqual(bron_naast_beeld(self.per_map("bron/a.json", "bron/b.json")), {})

    def test_given_them_split_over_two_folders_when_checked_then_nothing_is_reported(self):
        uit = bron_naast_beeld(self.per_map("bron/keuze.json", "gegenereerd/img/keuze.svg"))
        self.assertEqual(uit, {})

    def test_given_a_folder_with_both_when_checked_then_it_names_both_sides(self):
        uit = bron_naast_beeld(self.per_map("m/a.json", "m/b.yaml", "m/c.png"))
        self.assertEqual(uit, {"m": ["a.json", "b.yaml", "c.png"]})


class SamenTests(unittest.TestCase):
    """De twee controles samen: een map die beide breekt staat er een keer in."""

    def test_given_a_folder_breaking_both_checks_when_combined_then_it_appears_once(self):
        per = collections.defaultdict(set)
        per["m"] = {"doc.md", "keuze.json", "keuze.svg"}
        uit = overtreders(per)
        self.assertEqual(sorted(uit), ["m"])
        self.assertEqual(uit["m"], ["keuze.json", "keuze.svg"])


if __name__ == "__main__":
    unittest.main()
