"""Testgevallen die afdwingen dat geen enkel script het ArchiMate-model wijzigt.

Waarom dit een testgeval is en geen afspraak: harde regel 1 uit AGENTS.md zegt dat
alleen de modelleur het `.archimate`-bestand wijzigt, in Archi. Elf scripts lezen dat
bestand, en drie daarvan hadden een eigen hash-vergelijking. Voor de rest gold de regel
op papier en niets in de uitvoering.

Dat is precies het soort fout dat stil blijft. Een script dat het model aanraakt levert
een bestand op dat nog opent en nog valideert; de modelleur merkt het pas wanneer Archi
bij de volgende ronde iets anders toont dan hij achterliet, en dan is niet meer te zien
welke ronde het deed. De verliescontrole vangt alleen wat verdwijnt, niet wat verschuift.

Elk geval hier draait het script op een **kopie** van het echte model en vergelijkt de
sha256 ervoor en erna. Een kopie, omdat het echte bestand dan ook bij een falend geval
onaangeraakt blijft.
"""

import hashlib
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent.parent
MODEL = WORTEL / "architecture/model/model.archimate"
SCRIPTS = WORTEL / "tools/scripts"

# Per script: de argumenten waarmee het op een kopie draait. {model} en {uit} worden
# vervangen. Een script zonder --model leest het echte bestand en staat hieronder bij
# ZONDER_MODELVLAG; dat is zelf een bevinding.
MET_MODELVLAG = {
    "exporteer-archimate-view.py": ["--model", "{model}", "--uit", "{uit}/stromen.json"],
    "exporteer-componenten.py": ["--model", "{model}", "--uit", "{uit}/componenten.json"],
    "exporteer-conceptplaat.py": ["--model", "{model}", "--uit", "{uit}/conceptplaat.json"],
    "plaatherkomst.py": ["--model", "{model}"],
}

# Scripts die het model lezen zonder een --model-vlag. Zij kunnen niet op een kopie
# draaien, dus hier bewijst de test alleen dat zij het bestand na een ronde niet
# gewijzigd hebben. Een vlag erbij zou beter zijn; zie de vraag in issue #551.
ZONDER_MODELVLAG = {
    "genereer-informatiemodel-doc.py": [],
    "teken-hoofdplaat-ruim.py": ["--uit", "{uit}/plaat.svg"],
    "teken-fasenplaten.py": ["--uit", "{uit}"],
}


def sha(pad):
    return hashlib.sha256(Path(pad).read_bytes()).hexdigest()


class OpEenKopie(unittest.TestCase):
    """Een script dat --model kent, mag die kopie niet wijzigen."""

    def loop(self, script, argumenten):
        with tempfile.TemporaryDirectory() as map_:
            kopie = Path(map_) / "model.archimate"
            shutil.copy(MODEL, kopie)
            voor = sha(kopie)
            args = [str(x).format(model=kopie, uit=map_) for x in argumenten]
            uit = subprocess.run([sys.executable, str(SCRIPTS / script)] + args,
                                 cwd=WORTEL, capture_output=True, text=True)
            self.assertEqual(voor, sha(kopie),
                             f"{script} wijzigde het model; zie harde regel 1 in AGENTS.md")
            return uit

    def test_given_each_script_with_a_model_flag_when_run_then_the_model_is_untouched(self):
        for script, argumenten in MET_MODELVLAG.items():
            with self.subTest(script=script):
                self.loop(script, argumenten)

    def test_given_the_list_when_read_then_every_script_exists(self):
        """Een lijst die een script noemt dat niet bestaat, dekt niets."""
        for script in list(MET_MODELVLAG) + list(ZONDER_MODELVLAG):
            with self.subTest(script=script):
                self.assertTrue((SCRIPTS / script).exists(), script)


class OpHetEchteModel(unittest.TestCase):
    """Een script zonder --model leest het echte bestand; ook dan blijft het gelijk."""

    def test_given_each_script_without_a_model_flag_when_run_then_the_model_is_untouched(self):
        voor = sha(MODEL)
        with tempfile.TemporaryDirectory() as map_:
            for script, argumenten in ZONDER_MODELVLAG.items():
                with self.subTest(script=script):
                    args = [str(x).format(uit=map_) for x in argumenten]
                    subprocess.run([sys.executable, str(SCRIPTS / script)] + args,
                                   cwd=WORTEL, capture_output=True, text=True)
                    self.assertEqual(voor, sha(MODEL),
                                     f"{script} wijzigde het model; zie harde regel 1 in AGENTS.md")


class DeDekkingIsVolledig(unittest.TestCase):
    """Een controle die een script mist, geeft valse zekerheid."""

    def test_given_every_script_reading_the_model_when_listed_then_it_is_covered(self):
        gedekt = set(MET_MODELVLAG) | set(ZONDER_MODELVLAG)
        # Scripts met een eigen hash-vergelijking in hun eigen testbestand, en scripts
        # die het model alleen via een ander script raken.
        ELDERS = {
            "exporteer-archimate-platen.py": "eigen hash-vergelijking in test_exporteer_archimate_platen.py",
            "validate-archimate.py": "leest alleen en schrijft niets; toetst het model zelf",
            "controleer-modelverlies.py": "leest alleen en vergelijkt met een eerdere versie",
            "teken-hoofdplaat-highlight.py": "draait via teken-fasenplaten.py op dezelfde view",
            "teken-informatiemodel-uitsnede.py": "leest informatiemodel.json en niet het model",
            "publiceer-informatiemodel.py": "leest de afgeleide bestanden en niet het model",
            "genereer-leerroute-uitwerking-model-lr1.py": "leest informatiemodel.json en niet het model",
        }
        lezers = {p.name for p in sorted(SCRIPTS.glob("*.py"))
                  if "model.archimate" in p.read_text(encoding="utf-8")}
        ongedekt = sorted(lezers - gedekt - set(ELDERS))
        self.assertEqual(ongedekt, [],
                         "deze scripts lezen het model en staan in geen enkele controle; "
                         "zet ze in MET_MODELVLAG, ZONDER_MODELVLAG of ELDERS met de reden")

    def test_given_the_elsewhere_list_when_read_then_each_script_still_exists(self):
        for script in ("exporteer-archimate-platen.py", "validate-archimate.py",
                       "controleer-modelverlies.py", "teken-hoofdplaat-highlight.py"):
            with self.subTest(script=script):
                self.assertTrue((SCRIPTS / script).exists(), script)


if __name__ == "__main__":
    unittest.main()
