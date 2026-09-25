---
name: okx-presentatie-visueel
description: >-
  Het verhaal van een OKx-deck visueel maken: eerst de verhaallijn in een
  werkbestand, daarna per slide de kernzin en sleutelwoorden als verhaalhaakjes
  met pictogrammen, kaarten en diagrammen; de spreker vertelt de rest.
  Adaptatie-wrapper van de externe UI/UX-skill ui-ux-pro-max voor
  presentaties in de Npuls-huisstijl. Gebruik bij elk deck, en altijd
  wanneer een slide meer dan een handvol zinnen draagt of een lezer het
  verhaal uit de slide moet halen in plaats van uit de spreker.
---

# Het verhaal visueel maken

Een slide is geen tekst die de zaal leest; het is een verhaalhaakje waar de spreker het verhaal aan ophangt. Mensen lezen blokken tekst op een slide niet. Wat overkomt zijn sleutelwoorden, een pictogram dat ze herkennen en een diagram dat de relatie laat zien. Deze skill legt de werkwijze vast en past de externe UI/UX-skill [`ui-ux-pro-max`](../ui-ux-pro-max/SKILL.md) toe op presentaties; de huisstijl komt uit [`npuls-huisstijl`](../npuls-huisstijl/SKILL.md), de inhoudelijke regels uit [`okx-presentatie`](../okx-presentatie/SKILL.md).

## Werkwijze in vier stappen

1. **Verhaallijn eerst, in een werkbestand.** Schrijf het hele verhaal uit in de scratchpad (of een agent-artifact als het bewaard moet blijven): per slide de boodschap in een of twee zinnen, wat de spreker erbij vertelt, en welk beeld het draagt. Dit bestand is voor de maker en de spreker; het komt niet in de slide.
2. **Kernzin en sleutelwoorden per slide.** Haal uit elke boodschap de kernzin (de conclusie, hooguit een regel) en drie tot vijf sleutelwoorden. Dat zijn de cornerstones: klein, begrijpelijk, in de woorden van het OKx-begrippenkader. Alles wat de spreker kan zeggen, gaat naar de sprekersnotitie.
3. **Visual aid per cornerstone.** Elk sleutelwoord krijgt een drager: een pictogram met een woord eronder, een kaart met een pictogram en twee of drie steekwoorden, een pijplijn van stappen, een trap van niveaus, een diagram van relaties, of een bestaande plaat op een eigen slide. Kies de drager op wat het sleutelwoord is: een component krijgt zijn pictogram, een volgorde een pijplijn, een gelaagdheid een trap, een samenhang een diagram.
4. **Tel en kijk.** Tel eerst de zichtbare woorden: `python3 presentaties/tel-woorden.py presentaties/src/<deck>.md`. Een slide boven de zestig woorden gaat terug naar de tekentafel, rond de veertig is het doel. Exporteer daarna de beelden (`./deck <naam> beelden`) en beoordeel elke slide in acht seconden: staat de kernzin, zijn de sleutelwoorden zichtbaar zonder lezen, is er een beeld om over te praten. Zo niet: tekst eruit, drager erin. Het oog vergeeft te veel tekst; de telling niet. Code valt buiten het woordbudget en heeft een eigen maat: de teller meldt de coderegels per slide en faalt boven de twaalf. Een mermaid-blok telt als plaat, niet als code.

## Tekstbudget

| Element | Budget |
|---|---|
| Titel | een regel, plat en concreet, benoemt wat de slide toont |
| Kernzin | hooguit een regel, in een kaart onderaan of als afsluiting |
| Kaart | pictogram, titel van twee tot vier woorden, hooguit drie steekwoorden van hooguit vijf woorden |
| Pictogram met woord | een of twee woorden eronder, in de taal van de zaal |
| Zichtbare tekst per slide | rond de veertig woorden; boven de zestig gaat de slide in tweeen of gaat tekst naar de notitie. `presentaties/tel-woorden.py` telt het en faalt boven de zestig |
| Code of voorbeeldbericht | hooguit twaalf regels, ingekort tot de velden die het punt maken, met de bron in de notitie |
| Sprekersnotitie | vrij; hier staan het verhaal, de bron en de nuance |

Een zin die "de spreker zegt dit toch" oproept, hoort in de notitie. Een uitleg van wat een large language model kan uitleggen maar de zaal niet leest, hoort er ook.

## Dragers en wanneer

| Sleutelwoord is | Drager | Vorm in de huisstijl |
|---|---|---|
| Een referentiecomponent of voorziening | pictogram met het woord eronder | witte kaart met rand, pictogram 2rem, woord 0.78rem vet |
| Een volgorde of proces | pijplijn | `np-pipeline` met `np-step` en `np-arrow`, per stap een pictogram, een titel en een regel klein |
| Een gelaagdheid | trap | rijen met oplopende inspringing, genummerde `np-num`, de laag buiten scope grijs en gestippeld zonder tekst erachter |
| Een raakvlak of thema | kaart met pictogram en steekwoorden | `np-card` met accentkleur, pictogram in de kop, hooguit drie bullets |
| Een endpoint, bericht of schema | codefragment | `<code>` voor een endpoint in de lopende tekst, `<pre>` voor een bericht: lichtgrijze achtergrond, 0.62rem, sleutels in `--np-blue` |
| Een samenhang tussen begrippen | klein diagram | inline SVG met vier tot zes vakken en lijnen, of een mermaid-diagram |
| Een uitwisseling tussen twee systemen | sequentiediagram | mermaid `sequenceDiagram` met twee deelnemers en hooguit vier berichten, `theme: 'base'` met de huisstijlkleuren in `themeVariables`, `scale` rond 0.6 en een `<style scoped>` die de svg op `max-width: 100%` houdt |
| Een architectuurplaat | de plaat zelf, paginavullend | eigen slide, witte achtergrond, een bijschrift van een regel; de plaat krijgt nooit een tekstkolom ernaast |
| Een afspraak of vraag | kaart met een kernzin en steekwoorden als pillen | `np-card accent-orange`, pillen in `border-radius:999px` |
| Een verwijzing naar de kennisbasis | QR-code met de korte URL | `segno` genereert de PNG; naast de code twee of drie ingangen als kaarten |

Pictogrammen komen uit de iconify-sets die Slidev meekrijgt (`carbon-*`, `mdi-*`); geen emoji. Een pictogram staat nooit alleen: er staat altijd een woord bij.

## Pictogramvocabulaire OKx

Gebruik voor dezelfde component steeds hetzelfde pictogram, over decks heen.

| Component of begrip | Pictogram |
|---|---|
| Onderwijscatalogus | `carbon-catalog` |
| Planning en rooster | `carbon-calendar` |
| Studentkeuze | `carbon-user-favorite` |
| Kernregistratie (KRS) | `carbon-data-base` |
| Studentvolgsysteem (SVS) | `carbon-chart-line` |
| LMS | `carbon-education` |
| Examinering | `carbon-task-complete` |
| Aanmelden, AII, CAMBO | `carbon-user-follow` |
| Identiteit, IAM, EduID | `carbon-user-identification` |
| Federatie, eduXchange, EduHub | `carbon-network-3` |
| RIO | `carbon-building` |
| Leeruitkomst als sleutel | `mdi-key-variant` |
| Specificatie, document | `carbon-document` |
| Bouwstenen, modulair | `carbon-assembly-cluster` |
| Leerroutes, reis | `carbon-map` |
| Koploperscholen, gebruikers | `carbon-user-multiple` |
| Afstemming, samenwerking | `carbon-partnership` |
| Kennisbasis, GitHub | `carbon-logo-github`, `carbon-book` |
| AI | `carbon-machine-learning-model` |

## Wat de UI/UX-skill hier toevoegt

Raadpleeg `ui-ux-pro-max` met een gerichte vraag als een slide visueel niet werkt; de zoekopdracht loopt via het script in die skill:

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<vraag>" --domain ux
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<vraag>" --domain icons
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<vraag>" --domain typography
```

Wat daaruit voor presentaties geldt: contrast van tekst op de achtergrond (donker op licht, nooit grijs op grijs), pictogrammen als SVG met een tekstlabel, lettergrootte in een geprojecteerde slide minstens 0.78rem voor bijschriften en 0.84rem voor lopende tekst, een leesrichting van links naar rechts en van boven naar beneden, een accentkleur per betekenis en steeds dezelfde. Wat daaruit hier buiten beeld blijft: alles over interactie, formulieren, navigatie, animatie en implementatiestacks; een slide is statisch.

## De valkuilen die deze skill wegneemt

- **Het verhaal op de slide vertellen.** Alinea's, volzinnen en uitleg in kaarten. Dat is voor de notitie.
- **Een plaat met een tekstkolom ernaast.** De plaat wordt onleesbaar; de plaat krijgt een eigen slide.
- **Termen van buiten het begrippenkader** omdat een opdrachtgever ze gebruikt. De cornerstones dragen de OKx-termen; de term van de ander mag in de notitie of als citaat.
- **Interne planning en intern werk** als inhoud voor een externe zaal. Alleen wat de zaal ermee kan.
- **Een grens formuleren als wat het niet is.** Zeg wie het wel doet (zie de schrijfstijlregel over positief formuleren).
- **Een afsluiting die niets vraagt.** De laatste slide draagt de afspraak of de vraag, met de verwijzing naar de kennisbasis.

## Definitie van klaar

- Verhaallijn in een werkbestand, sprekersnotitie per slide gevuld.
- Elke slide binnen het tekstbudget, met minstens een drager uit de tabel.
- Platen paginavullend op eigen slides.
- `tel-woorden.py` groen (geen slide boven de zestig woorden), beelden geexporteerd en per slide in acht seconden beoordeeld; pdf en bewerkbare pptx in `presentaties/export/`.
- Schrijfstijl en positief formuleren getoetst, huisstijl uit `npuls-huisstijl`.
