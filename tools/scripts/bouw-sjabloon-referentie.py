#!/usr/bin/env python3
"""Bouwt de Word-referentie in de Npuls-huisstijl waartegen pandoc de sjablonen rendert.

De referentie wordt niet met de hand onderhouden: pandoc levert zijn eigen
reference.docx en dit script zet daar de Npuls-waarden in. Zo is hij opnieuw te
bouwen wanneer pandoc of de huisstijl wijzigt.

    python3 tools/scripts/bouw-sjabloon-referentie.py
"""

import argparse
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

WORTEL = pathlib.Path(__file__).resolve().parents[2]
UIT = WORTEL / "architecture/docs/sjablonen/gegenereerd/npuls-referentie.docx"

# De primaire kleuren uit .agents/skills/npuls-huisstijl/SKILL.md.
ORANJE = "DD784B"   # primair accent, koppen
BLAUW = "3D68EC"    # links
GRIJS = "BFBFBF"    # celranden, zodat een lege invulcel zichtbaar is
LETTER = "General Sans"

# Pandoc levert een tabel met alleen een streep onder de kopregel. In een
# sjabloon is dat onbruikbaar: de invuller ziet niet waar een cel begint.
RANDEN = (
    "<w:tblBorders>"
    + "".join(f'<w:{kant} w:val="single" w:sz="4" w:space="0" '
              f'w:color="{GRIJS}" />'
              for kant in ("top", "left", "bottom", "right",
                           "insideH", "insideV"))
    + "</w:tblBorders>"
)


def default_referentie(doel: pathlib.Path) -> None:
    uit = subprocess.run(
        ["pandoc", "--print-default-data-file", "reference.docx"],
        capture_output=True, check=True,
    )
    doel.write_bytes(uit.stdout)


def huisstijl(thema: str, stijlen: str) -> tuple[str, str]:
    """Zet de Npuls-kleuren en de letter in het thema en de stijlen."""
    # De koppen verwijzen naar accent1; een kleur in het thema dekt H1 tot en met H3.
    thema = thema.replace('<a:accent1><a:srgbClr val="4F81BD" /></a:accent1>',
                          f'<a:accent1><a:srgbClr val="{ORANJE}" /></a:accent1>')
    thema = re.sub(r'(<a:(?:major|minor)Font>\s*<a:latin typeface=")[^"]*(")',
                   rf'\1{LETTER}\2', thema)

    # De koppen dragen naast w:themeColor een letterlijke kleur, en die wint bij
    # een lezer die het thema niet oplost. Allebei dus.
    stijlen = stijlen.replace('<w:color w:val="4F81BD" w:themeColor="accent1" />',
                              f'<w:color w:val="{ORANJE}" w:themeColor="accent1" />')

    # Randen om elke cel, en lucht erin.
    stijlen = stijlen.replace(
        '<w:tblPr>\n      <w:tblInd w:w="0" w:type="dxa" />',
        f'<w:tblPr>{RANDEN}\n      <w:tblInd w:w="0" w:type="dxa" />')
    stijlen = stijlen.replace('<w:top w:w="0" w:type="dxa" />',
                              '<w:top w:w="60" w:type="dxa" />')
    stijlen = stijlen.replace('<w:bottom w:w="0" w:type="dxa" />',
                              '<w:bottom w:w="60" w:type="dxa" />')

    # Links in Npuls-blauw.
    def blauw(m: re.Match) -> str:
        return re.sub(r'<w:color w:val="[0-9A-Fa-f]{6}"[^/]*/>',
                      f'<w:color w:val="{BLAUW}" />', m.group(0))

    stijlen = re.sub(r'<w:style [^>]*w:styleId="Hyperlink".*?</w:style>',
                     blauw, stijlen, flags=re.S)
    # Nederlands, zodat Word niet elk woord onderstreept.
    stijlen = stijlen.replace('w:val="en-US" w:eastAsia="en-US"',
                              'w:val="nl-NL" w:eastAsia="nl-NL"')
    return thema, stijlen


def bouw(uit: pathlib.Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        bron = tmp / "default.docx"
        default_referentie(bron)
        with zipfile.ZipFile(bron) as z:
            onderdelen = {n: z.read(n) for n in z.namelist()}

        thema = onderdelen["word/theme/theme1.xml"].decode("utf-8")
        stijlen = onderdelen["word/styles.xml"].decode("utf-8")
        thema, stijlen = huisstijl(thema, stijlen)
        if (ORANJE not in thema or ORANJE not in stijlen
                or BLAUW not in stijlen or LETTER not in thema
                or GRIJS not in stijlen):
            raise SystemExit("de huisstijl is niet toegepast; pandoc heeft zijn "
                             "referentie gewijzigd en dit script moet mee")
        onderdelen["word/theme/theme1.xml"] = thema.encode("utf-8")
        onderdelen["word/styles.xml"] = stijlen.encode("utf-8")

        tussen = tmp / "npuls.docx"
        with zipfile.ZipFile(tussen, "w", zipfile.ZIP_DEFLATED) as z:
            for naam, inhoud in onderdelen.items():
                z.writestr(naam, inhoud)
        uit.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tussen), uit)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--uit", type=pathlib.Path, default=UIT)
    a = p.parse_args(argv)
    bouw(a.uit)
    print(f"  {a.uit.relative_to(WORTEL)}  ({a.uit.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
