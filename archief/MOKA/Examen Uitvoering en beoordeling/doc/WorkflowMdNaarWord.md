# Workflow: Markdown naar Word (.docx)

De MOKA koppelvlak specificaties staan in Markdown (`.md`). Voor overleg of levering kunnen ze worden geëxporteerd naar Word (`.docx`) zonder dat architecten Markdown hoeven te leren. Deze workflow beschrijft hoe.

## Vereiste

- **Pandoc** moet op uw systeem geïnstalleerd zijn.
  - Download: [https://pandoc.org/installing.html](https://pandoc.org/installing.html)
  - Controle: open een terminal en voer uit: `pandoc --version`

## Script gebruiken (aanbevolen)

In de map `scripts` staan twee scripts:

- **Windows:** `scripts/md2docx.bat`
- **Linux/macOS:** `scripts/md2docx.sh` (maak uitvoerbaar met `chmod +x scripts/md2docx.sh`)

### Gebruik

| Situatie | Commando (Windows) | Commando (Linux/macOS) |
|----------|---------------------|-------------------------|
| Voorbeelduitwerking naar .docx (standaard) | `scripts\md2docx.bat` | `./scripts/md2docx.sh` |
| Template naar .docx | `scripts\md2docx.bat doc\KoppelvlakSpecificatieTemplate.md` | `./scripts/md2docx.sh doc/KoppelvlakSpecificatieTemplate.md` |
| Eigen invoer en uitvoer | `scripts\md2docx.bat doc\mijn.md doc\mijn.docx` | `./scripts/md2docx.sh doc/mijn.md doc/mijn.docx` |

Zonder argumenten wordt `doc/KoppelvlakSpecificatieDocument.md` geconverteerd naar `doc/KoppelvlakSpecificatieDocument.docx`.

## Handmatig met Pandoc

Als u pandoc direct wilt aanroepen:

```bash
# Voorbeelduitwerking
pandoc -o doc/KoppelvlakSpecificatieDocument.docx doc/KoppelvlakSpecificatieDocument.md --from markdown --to docx

# Template
pandoc -o doc/KoppelvlakSpecificatieTemplate.docx doc/KoppelvlakSpecificatieTemplate.md --from markdown --to docx
```

## Opmerkingen

- **Mermaid-diagrammen:** Pandoc zet Mermaid-codeblokken als code in Word; de diagrammen worden niet gerenderd. Voor een volledige weergave kunt u de diagrammen apart als afbeelding exporteren en in het Word-document invoegen, of de Markdown in een viewer gebruiken die Mermaid ondersteunt (bijv. GitHub).
- **Afbeeldingen:** Zorg dat de paden in de Markdown (bijv. `../img/...`) kloppen ten opzichte van het `.md`-bestand; pandoc neemt afbeeldingen mee naar het .docx.
- **Sectienummers:** Standaard voegt pandoc geen sectienummers toe. Dat kunt u later in Word instellen of met pandoc-variabelen verfijnen (zie pandoc-documentatie).
