#!/usr/bin/env python3
"""Maakt van het Npuls Word-sjabloon een referentie waar pandoc tegen bouwt.

Het Npuls-sjabloon is de bron van de huisstijl: omslag, logo, kleuren, de
koppen met hun nummering en de kop- en voetteksten. Pandoc zoekt daarnaast
een handvol stijlen op hun Engelse naam die dat sjabloon niet kent; die worden
hier toegevoegd, met Npuls-waarden en niet met die van pandoc.

Het sjabloon zelf wordt niet bewerkt: het blijft staan zoals Npuls het levert.

    python3 tools/scripts/bouw-sjabloon-referentie.py

Relateert aan: #554
"""

import argparse
import pathlib
import re
import shutil
import sys
import tempfile
import zipfile

WORTEL = pathlib.Path(__file__).resolve().parents[2]
MAP = WORTEL / "architecture/docs/sjablonen"
NPULS = MAP / "Npuls Word template uitgebreid.dotx"
UIT = MAP / "gegenereerd/npuls-referentie.docx"

# De primaire kleuren uit .agents/skills/npuls-huisstijl/SKILL.md, zoals het
# Npuls-sjabloon ze zelf in zijn thema zet.
ORANJE = "DD784B"
BLAUW = "3D68EC"
GRIJS = "BFBFBF"
ZWART = "000000"
LETTER = "Arial"

# Pandoc zoekt deze stijlen op hun Engelse naam. Het Npuls-sjabloon kent ze
# niet, en zonder deze toevoeging valt een tabel zonder randen uit en staat een
# citaat niet ingesprongen.
RANDEN = "".join(
    f'<w:{kant} w:val="single" w:sz="4" w:space="0" w:color="{GRIJS}" />'
    for kant in ("top", "left", "bottom", "right", "insideH", "insideV"))

AANVULLING = f"""
  <w:style w:type="table" w:styleId="Table">
    <w:name w:val="Table" />
    <w:basedOn w:val="Standaardtabel" />
    <w:uiPriority w:val="99" />
    <w:tblPr>
      <w:tblBorders>{RANDEN}</w:tblBorders>
      <w:tblCellMar>
        <w:top w:w="60" w:type="dxa" /><w:left w:w="108" w:type="dxa" />
        <w:bottom w:w="60" w:type="dxa" /><w:right w:w="108" w:type="dxa" />
      </w:tblCellMar>
    </w:tblPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="BodyText">
    <w:name w:val="Body Text" /><w:basedOn w:val="Standaard" />
    <w:pPr><w:spacing w:before="120" w:after="120" /></w:pPr>
    <w:rPr><w:color w:val="{ZWART}" /></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="FirstParagraph">
    <w:name w:val="First Paragraph" /><w:basedOn w:val="BodyText" />
  </w:style>
  <w:style w:type="paragraph" w:styleId="Compact">
    <w:name w:val="Compact" /><w:basedOn w:val="Standaard" />
    <w:pPr><w:spacing w:before="0" w:after="0" /></w:pPr>
    <w:rPr><w:color w:val="{ZWART}" /></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="BlockText">
    <w:name w:val="Block Text" /><w:basedOn w:val="Standaard" />
    <w:pPr>
      <w:ind w:left="454" />
      <w:pBdr><w:left w:val="single" w:sz="12" w:space="12"
        w:color="{ORANJE}" /></w:pBdr>
      <w:spacing w:before="120" w:after="120" />
    </w:pPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ImageCaption">
    <w:name w:val="Image Caption" /><w:basedOn w:val="Standaard" />
    <w:pPr><w:spacing w:before="0" w:after="200" /></w:pPr>
    <w:rPr><w:i /><w:sz w:val="18" /></w:rPr>
  </w:style>
  <w:style w:type="character" w:styleId="Hyperlink">
    <w:name w:val="Hyperlink" />
    <w:rPr><w:color w:val="{BLAUW}" /><w:u w:val="single" /></w:rPr>
  </w:style>
"""


def tekst_in_het_zwart(stijlen: str) -> str:
    """Zet de tekstkleur expliciet op zwart.

    Het Npuls-sjabloon laat de kleur op automatisch staan. Word kiest dan zelf,
    en op de gekleurde omslag levert dat witte tekst op; die is daar niet te
    lezen. Een expliciete kleur haalt die keuze weg.
    """
    return re.sub(
        r'(<w:style w:type="paragraph" w:default="1" w:styleId="Standaard">'
        r'(?:(?!</w:style>).)*?)(</w:style>)',
        rf'\1<w:rPr><w:color w:val="{ZWART}" /></w:rPr>\2',
        stijlen, count=1, flags=re.S)


def titel_onder_het_logo(stijlen: str) -> str:
    """Zet de titel onder het logo van de omslag.

    Het Npuls-sjabloon plaatst zijn titel met de hand lager op de omslag;
    pandoc zet hem bovenaan, en dan loopt hij door het logo heen.
    """
    # De stijl draagt geen alinea-eigenschappen; die komen er hier bij.
    return re.sub(
        r'(<w:style [^>]*w:styleId="Titel">(?:(?!</w:style>).)*?)(<w:rPr>)',
        r'\1<w:pPr><w:spacing w:before="2400" w:after="480" />'
        r'<w:keepNext /></w:pPr>\2',
        stijlen, count=1, flags=re.S)


def aanvullen(stijlen: str) -> str:
    """Zet de stijlen erbij die pandoc zoekt, zonder de Npuls-stijlen te raken."""
    for sid in re.findall(r'w:styleId="(\w+)"', AANVULLING):
        stijlen = re.sub(
            r'<w:style [^>]*w:styleId="%s".*?</w:style>\s*' % sid, "",
            stijlen, flags=re.S)
    stijlen = stijlen.replace("</w:styles>", AANVULLING + "</w:styles>")
    # Nederlands, zodat Word niet elk woord onderstreept.
    return re.sub(r'w:val="en-[A-Z]{2}"', 'w:val="nl-NL"', stijlen)


def bouw(uit: pathlib.Path, npuls: pathlib.Path = NPULS) -> None:
    if not npuls.exists():
        raise SystemExit(f"het Npuls-sjabloon ontbreekt op {npuls}")
    with zipfile.ZipFile(npuls) as z:
        onderdelen = {n: z.read(n) for n in z.namelist()}

    stijlen = tekst_in_het_zwart(titel_onder_het_logo(
        aanvullen(onderdelen["word/styles.xml"].decode("utf-8"))))
    if f'<w:color w:val="{ZWART}" />' not in stijlen:
        raise SystemExit("de tekstkleur is niet op zwart gezet; op de omslag "
                         "wordt de tekst dan wit en onleesbaar")
    for sid in ("Table", "BodyText", "BlockText", "Hyperlink"):
        if f'w:styleId="{sid}"' not in stijlen:
            raise SystemExit(f"de stijl {sid} is niet toegevoegd; het "
                             "Npuls-sjabloon is gewijzigd en dit script moet mee")
    onderdelen["word/styles.xml"] = stijlen.encode("utf-8")

    with tempfile.TemporaryDirectory() as tmp:
        tussen = pathlib.Path(tmp) / "referentie.docx"
        with zipfile.ZipFile(tussen, "w", zipfile.ZIP_DEFLATED) as z:
            for naam, inhoud in onderdelen.items():
                z.writestr(naam, inhoud)
        uit.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tussen), uit)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--uit", type=pathlib.Path, default=UIT)
    p.add_argument("--npuls", type=pathlib.Path, default=NPULS)
    a = p.parse_args(argv)
    bouw(a.uit, a.npuls)
    print(f"  {a.uit.relative_to(WORTEL)}  ({a.uit.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
