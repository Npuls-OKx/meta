"""Testgevallen voor de maatvoering van kaderscenario 1.1 en de regeltabel.

De aantallen in het scenario en in de regeltabel moeten hetzelfde verhaal vertellen: verandert het
cohort, dan verandert het overal mee. Een lezer die het scenario naast een beeld legt en twee getallen
ziet, vertrouwt geen van beide meer. Deze gevallen houden die twee aan elkaar, en bewaken dat elke
overgenomen waarde haar bron draagt.
"""

import json
import re
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent
SCENARIO = WORTEL / "architecture/docs/specificatie/leerroute-uitwerking/doc/scenario-uitwerkingen/scenario-1.1-regulier-happyflow.md"
REGELS = WORTEL / "architecture/model/informatiemodel/voorbeeld-lr1-regels.json"


def scenario():
    return SCENARIO.read_text(encoding="utf-8")


def instanties():
    tabel = json.loads(REGELS.read_text(encoding="utf-8"))
    uit = []
    for r in tabel["regels"]:
        uit.append(r.get("instantie", ""))
        uit.append(r.get("zin") or "")
        for houder in [r.get("relatie")] + list(r.get("relaties") or []):
            if isinstance(houder, dict):
                uit.append(houder.get("instantie") or "")
    return uit


class CohortTests(unittest.TestCase):
    def test_given_the_scenario_when_read_then_the_cohort_lies_between_twenty_and_forty(self):
        m = re.search(r"cohortgrootte (\d+) studenten in twee groepen van (\d+)", scenario())
        self.assertIsNotNone(m, "het scenario noemt geen cohortgrootte")
        cohort, groep = int(m.group(1)), int(m.group(2))
        self.assertGreaterEqual(cohort, 20)
        self.assertLessEqual(cohort, 40)
        self.assertEqual(cohort, groep * 2)

    def test_given_the_scenario_when_read_then_the_distribution_over_the_leerroutes_stands_there(self):
        tekst = scenario()
        self.assertIn("70 procent leerroute 1", tekst)
        self.assertIn("leerroute 2 en 3 elk ongeveer 15 procent", tekst)

    def test_given_the_rule_table_when_read_then_it_uses_the_cohort_of_the_scenario(self):
        cohort = int(re.search(r"cohortgrootte (\d+) studenten", scenario()).group(1))
        groep = cohort // 2
        alles = " | ".join(instanties())
        self.assertIn(f"{cohort} plaatsen", alles)
        self.assertIn(f"{groep} tot {cohort} studenten", alles)
        self.assertIn(f"twee groepen van {groep}", alles)
        self.assertIn(f"prognose {cohort} instromers", alles)

    def test_given_the_rule_table_when_read_then_no_instance_carries_the_old_numbers(self):
        """De oude getallen kwamen uit een inschatting die Niels te hoog noemde."""
        for s in instanties():
            self.assertNotRegex(s, r"\b48 (plaatsen|studenten|instromers)\b", s)
            self.assertNotIn("24 tot 48", s)
            self.assertNotIn("twee groepen van 24", s)

    def test_given_a_room_capacity_when_read_then_it_keeps_the_number_of_the_kaderscenario(self):
        """Een lokaalcapaciteit is een eigenschap van de ruimte en komt uit het kaderscenario zelf
        (r723 en r736: simulatieruimte apotheekbalie, maximaal 24 studenten); die beweegt niet mee."""
        alles = " | ".join(instanties())
        self.assertIn("Balie-simulatie (skillslab), 24 plaatsen", alles)
        self.assertIn("Simulatiegeschikte praktijkruimte voor 24 studenten", alles)


class DocentTests(unittest.TestCase):
    def test_given_the_teacher_when_read_then_appointment_side_task_and_care_time_stand_there(self):
        tekst = scenario()
        self.assertIn("0,8 FTE", tekst)
        self.assertIn("een dag per week niet inzetbaar", tekst)
        self.assertIn("200 uur", tekst)
        self.assertIn("10 minuten voor- en nazorg", tekst)

    def test_given_the_lesson_hour_when_read_then_it_is_a_choice_of_the_institution(self):
        tekst = scenario()
        self.assertIn("35, 45 of 50 minuten", tekst)
        self.assertIn("blokuur van twee eenheden", tekst)
        self.assertIn("keuze van de instelling en geen gegeven", tekst)

    def test_given_the_deployment_planning_when_read_then_the_maturing_rounds_stand_there(self):
        self.assertRegex(scenario(), r"neventaken.{0,200}ronden van rijping")


class BronTests(unittest.TestCase):
    def test_given_every_adopted_value_when_read_then_it_carries_the_review_comment(self):
        """Criterium 6: elke overgenomen waarde draagt de comment waaruit zij komt."""
        tekst = scenario()
        for comment in ("4122687194", "4122816686", "4122878371"):
            self.assertIn(f"https://github.com/Npuls-OKx/meta/pull/252#discussion_r{comment}", tekst)

    def test_given_the_changed_instances_when_read_then_they_point_at_the_scenario(self):
        tabel = json.loads(REGELS.read_text(encoding="utf-8"))
        cohort = int(re.search(r"cohortgrootte (\d+) studenten", scenario()).group(1))
        geraakt = [r for r in tabel["regels"] if f"{cohort} plaatsen" in r.get("instantie", "")
                   or f"{cohort // 2} tot {cohort}" in r.get("instantie", "")]
        self.assertTrue(geraakt)
        for r in geraakt:
            self.assertIn("scenario-1.1-regulier-happyflow.md", r["bron"])


if __name__ == "__main__":
    unittest.main()
