# Presentaties

Slidedecks over de voortgang van OKx, in de Npuls huisstijl, opgebouwd uit wat er in de OKx-repositories is gebeurd.

De aanleiding: die decks werden met de hand gemaakt terwijl alle informatie al in de repositories zit. Wie een update geeft aan de kerngroep techniek of aan de programmaleiding, vertelt over besluiten, specificaties en voortgang die daar zwart op wit staan.

## Snel beginnen

Eén commando doet alles. Je hoeft niets te installeren; dat gebeurt de eerste keer vanzelf.

```bash
cd presentaties

./deck                                  # welke decks zijn er?
./deck adviesgroep                      # openen, met live bijwerken tijdens schrijven
./deck adviesgroep statisch             # openen om te presenteren
./deck adviesgroep programma statisch   # allebei tegelijk, op 3030 en 3031
./deck adviesgroep beelden              # een PNG per slide, om te controleren
./deck adviesgroep pdf                  # een PDF om rond te sturen
./deck adviesgroep pptx                 # een PowerPoint, tekst bewerkbaar
```

De bronnen staan in `src/`; de naam mag een fragment zijn, `adviesgroep` vindt `src/260803_adviesgroep.md`. Passen er meerdere, dan vraagt het script om een specifiekere naam.

### Gewoon of statisch?

| | `./deck <naam>` | `./deck <naam> statisch` |
|---|---|---|
| Wijzigingen komen vanzelf door | ja | nee, commando opnieuw draaien |
| Gebruik het om | te schrijven | te **presenteren** |

**Blijft je browser herladen, neem dan `statisch`.** De gewone server houdt een verbinding open om wijzigingen live door te voeren; komt die niet tot stand, dan blijft de pagina opnieuw laden. De statische versie heeft die verbinding niet.

Gebruik **niet** `npx slidev` rechtstreeks: dan luistert de server op een adres waar de browser niet bij kan, met precies dat herlaadgedrag tot gevolg.

## Een nieuw deck maken

Met een agent gaat het snelst:

```
/presentatie
```

Die vraagt voor welk gremium en over welke periode, verzamelt de wijzigingen uit **beide** repositories, en legt je eerst een lijstje onderwerpen voor: *dit zag ik gebeuren, hier wil ik het over hebben, klopt dat?* Pas als jij akkoord bent, schrijft hij het deck.

Met de hand:

```bash
cp src/_template.md src/260803_onderwerp.md
./deck onderwerp
```

Naamgeving: `src/JJMMDD_onderwerp.md`. Het template bevat een werkend voorbeeld van elk slidetype.

## Waar je op let bij het schrijven

Dit zijn de dingen die in de praktijk misgingen. Uitgebreider in de skill [`okx-presentatie`](../.agents/skills/okx-presentatie/SKILL.md), die een agent automatisch meekrijgt.

**Kies je onderwerpen op wat er op tafel moet, niet op wat het meeste werk was.** Een herindeling kan honderden bestanden raken en toch een voetnoot zijn.

**Kernpunt eerst.** Het publiek hoort binnen de eerste minuut wat de sprekers komen brengen: wat er bereikt is, in één concrete zin, vóór het programma. Een subtitel op de titelslide draagt die essentie of vervalt — sfeerzinnen zijn vulling.

**Schrijf over de zaak, niet tegen de zaal.** Geen "u", "je" of "jullie", ook niet in een kop. Een deck informeert over een onderwerp, dus dat onderwerp staat vooraan — dezelfde norm als bij een adviesrapport. "Waar we jullie voor nodig hebben" wordt **Besluit nodig op**, met daaronder *Door* (welke partijen), *Voor* (wanneer) en *Opties*. Zo staat na afloop vast wat er gevraagd is.

**Meta-taal blijft buiten de slide.** "Houd het kort" is een instructie voor de maker, geen slidetekst: een titel als "De aanleiding, kort" vertelt hoe het deck gemaakt is in plaats van wat er staat. Als de slide kort is, ziet de zaal dat vanzelf; de aanwijzing zelf hoort in de sprekersnotitie.

**De opdracht is regie, geen slidetekst.** De briefing van de opdrachtgever ("het idee is dat ze meteen zien wat we komen brengen") is nooit zelf de titel of tekst van de slide. Vertaal de aanwijzing: wat is de essentie voor het publiek, en hoe zou je die zelf willen lezen als je in de zaal zat? Wie de briefing letterlijk terugleest heeft genotuleerd, niet gemaakt.

**Liever leegte dan vulling.** Elke zichtbare zin heeft een bron of sneuvelt. Geen subtitels onder de slidetitel, platte titels, echte beelden boven nagebouwde ASCII-structuren, en wat de spreker kan zeggen staat in de sprekersnotitie — niet geforceerd in een diagram. De volledige anti-bloatregels staan in de skill.

**Stem het register af op intern of extern.** Intern zijn het SI-team, de adviesgroep en de programma- en projectleiding: relatief informeel binnen zakelijke normen, korte zinnen, gewone woorden. Extern zijn de kerngroep techniek OKx, de technische werkgroep OEAPI, leveranciers en instellingen: formeler en preciezer, met bij elke uitspraak de status erbij — vastgesteld, concept of voorstel. Die gremia nemen het materiaal mee naar hun eigen organisatie. Het verschil tussen adviesgroep en leiding zit in de diepgang, niet in het register.

**Gebruik de termen uit de bron.** Het is *leermanagementsysteem (LMS)*, *studentinformatiesysteem (SIS, dat is KRS plus SVS)*, *onderwijscatalogus*. Niet "leeromgeving" of "studentadministratie" als je het systeem bedoelt. De afkortingenlijst staat in de instap van [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md).

**Neem tabellen en cijfers letterlijk over.** Bouw een tabel nooit uit je hoofd na; open het bronbestand en kopieer hem. Bij de ankertabel ging dat een keer mis, en zo'n fout kost geloofwaardigheid precies bij het publiek dat erop let.

**Show, don't tell.** Gebruik de bestaande architectuurplaten in plaats van een eigen diagram: die zijn al besproken en goedgekeurd. Zet er wel een regel bij die zegt waar de kijker naar moet kijken; een plaat zonder leeswijzer is decoratie. Welke platen er zijn, staat hieronder.

**Scheid feit van mening.** Wat uit de repositories komt is feit; wat jij ervan vindt is een inschatting. Zet dat er als zodanig bij, zodat je het in de vergadering niet als vaststaand presenteert.

## De PowerPoint-export

`./deck <naam> pptx` levert een bestand waarin de tekst aan te passen is en de slides eruitzien als het deck. De route loopt via de pdf: LibreOffice leest die in Impress en schrijft hem weg als PowerPoint. Elk element houdt zijn plek, de diagrammen komen als vectorvormen mee.

Wat je merkt: bij een opsomming die over twee regels loopt, staat de tweede regel strak onder de eerste. Dat is een gevolg van de pdf-import en met de regelafstand in PowerPoint zo bijgesteld.

De pptx-export van Slidev zelf zet elke slide als afbeelding in het bestand; die route is daarom niet gebruikt. Wil je een slide als plaatje overnemen, gebruik dan `beelden`.

**Kijk naar je slides voordat je ze deelt.** `./deck <naam> beelden` geeft een PNG per slide. Overflow en te brede tabellen zie je alleen zo.

## Platen die je kunt gebruiken

De architectuurplaten staan verspreid over beide repositories, ze hebben versies, en een afgeleide plaat kan op een oudere versie stoelen dan de plaat die inmiddels leidend is. Daarom staat er één lijst: [`platen.json`](platen.json).

Per plaat lees je daar wat hij toont, bij welk publiek hij werkt, en waar je op moet letten. Onderaan staan de mermaid-diagrammen uit de koppelingspecificaties; die plak je rechtstreeks in een slide, want Slidev rendert ze.

Controleer de lijst voordat je hem gebruikt:

```bash
python3 ../scripts/platen-inventariseren.py
```

Dat vergelijkt het manifest met wat er werkelijk in beide repositories staat en meldt: een bron die is **verdwenen**, een bron die is **gewijzigd** sinds de omschrijving werd geschreven, een **nieuwere versie** die ernaast is verschenen, een plaat die nog **niet in het manifest** staat, en een kopie in `public/platen/` die is gaan **afwijken van zijn bron**. Los meldingen op voordat je een plaat kiest.

Kopieer wat je nodig hebt naar `public/platen/` en verwijs ernaar met `/platen/<naam>`. Een brede plaat geef je de hele slidebreedte:

```html
<img src="/platen/lr1-informatiestromen.jpg" style="width: 100%; max-height: 330px; object-fit: contain;" />
```

### Waarom `public/platen/` kopieën bevat

Slidev serveert alleen wat onder `public/` staat; een slide kan niet naar een bestand buiten dit project wijzen. Elke plaat die je gebruikt is daarom een kopie, en dat is bewust: de decks zijn zo zelfstandig te bouwen en de map hoort in git.

De prijs is dat een kopie stil kan achterlopen op zijn bron. Daarom noemt elke manifestregel die in gebruik is zijn kopie in het veld `kopie`, en vergelijkt het controlescript beide. Wat er ligt zonder dat een manifestregel het opeist, wordt gemeld als losse kopie — zo blijft de map een gebruikslijst en geen aanslibsel.

Gebruik je een plaat niet meer, haal de kopie dan weg en laat het veld `kopie` leeg. De manifestregel zelf blijft staan: de plaat bestaat nog, hij wordt alleen even niet getoond.

### Als je zelf een plaat toevoegt

Zet hem in het manifest en werk daarna de vingerafdrukken bij:

```bash
python3 ../scripts/platen-inventariseren.py --bijwerken
```

Twee velden doen het werk. `gebruik_bij` is waar een agent op selecteert, dus schrijf daar het publiek en de situatie, niet de inhoud. `let_op` is waar het voorbehoud staat; wat daar staat komt terug in de afstemming voordat er een deck wordt geschreven.

Hoort een plaat níet in presentaties thuis — een schermafdruk, een tussenresultaat, een ingehaalde versie — zet hem dan onder `overslaan` met de reden erbij. Dan blijft de melding "nog niet in het manifest" betekenen dat er echt iets nieuws is.

## Wat er in deze map staat

| Onderdeel | Rol |
| --- | --- |
| `deck` | Het enige commando dat je nodig hebt |
| `_template.md` | Startpunt met werkende voorbeelden van elk slidetype |
| `style.css` | Het designsysteem: Npuls-fonts, kleurtokens en de `np-`-componentbibliotheek |
| `public/npuls/` | Achtergronden, illustraties, logo en lettertypen |
| `public/platen/` | Architectuurplaten die in decks worden gebruikt |
| `public/shots/` | Schermafdrukken |
| `JJMMDD_onderwerp.md` | De presentaties zelf |

Pas de huisstijl alleen aan in `style.css`, nooit per presentatie. Bouw slides met de `np-`-classes; verzin geen losse inline-stijlen waar een class bestaat. De map `export/` bevat gegenereerde bestanden en blijft buiten git.

## Twee dingen die vastliggen

**De decks blijven hier.** Ze horen niet in `Npuls-OKx/Public`: dat repository draagt releaseartefacten waarmee een afnemer een koppelvlak bouwt. Een presentatie over de voortgang zou dat vervuilen. De inhoud van een deck komt wél uit beide repositories.

**Het publiek bepaalt het abstractieniveau.** Maak liever twee decks dan één compromis.

## Herkomst

Het designsysteem, de achtergronden en de componentbibliotheek komen uit [`cedanl/clidev-presentaties`](https://github.com/cedanl/clidev-presentaties). De werkwijze en de huisstijl uit de skills [`clidev`](https://github.com/cedanl/.github/tree/main/.claude/skills/clidev) en [`npuls-huisstijl`](https://github.com/cedanl/.github/tree/main/.claude/skills/npuls-huisstijl); die zijn gevendord onder [`.agents/skills/`](../.agents/skills/) en worden niet bewerkt.

De Npuls huisstijl is eigendom van Npuls. OKx is een Npuls-programma, dus het gebruik valt binnen de voorwaarden.
