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
```

De naam mag een fragment zijn: `adviesgroep` vindt `260803_adviesgroep.md`. Passen er meerdere, dan vraagt het script om een specifiekere naam.

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
cp _template.md 260803_onderwerp.md
./deck onderwerp
```

Naamgeving: `JJMMDD_onderwerp.md`. Het template bevat een werkend voorbeeld van elk slidetype.

## Waar je op let bij het schrijven

Dit zijn de dingen die in de praktijk misgingen. Uitgebreider in de skill [`okx-presentatie`](../.agents/skills/okx-presentatie/SKILL.md), die een agent automatisch meekrijgt.

**Kies je onderwerpen op wat er op tafel moet, niet op wat het meeste werk was.** Een herindeling kan honderden bestanden raken en toch een voetnoot zijn.

**Stem de toon af op het gremium.** De interne gremia, adviesgroep en programmaleiding, krijgen allebei een informele toon: korte zinnen, "ik" en "jullie". Het verschil zit in de diepgang, niet in de plechtigheid. De adviesgroep krijgt meer uitleg per stap, de leiding minder detail en meer beslispunten.

**Gebruik de termen uit de bron.** Het is *leermanagementsysteem (LMS)*, *studentinformatiesysteem (SIS, dat is KRS plus SVS)*, *onderwijscatalogus*. Niet "leeromgeving" of "studentadministratie" als je het systeem bedoelt. De afkortingenlijst staat in de instap van [Koppelvlakspecificaties](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md).

**Neem tabellen en cijfers letterlijk over.** Bouw een tabel nooit uit je hoofd na; open het bronbestand en kopieer hem. Bij de ankertabel ging dat een keer mis, en zo'n fout kost geloofwaardigheid precies bij het publiek dat erop let.

**Show, don't tell.** Gebruik de bestaande architectuurplaten in plaats van een eigen diagram. Zet er wel een regel bij die zegt waar de kijker naar moet kijken; een plaat zonder leeswijzer is decoratie.

**Scheid feit van mening.** Wat uit de repositories komt is feit; wat jij ervan vindt is een inschatting. Zet dat er als zodanig bij, zodat je het in de vergadering niet als vaststaand presenteert.

**Kijk naar je slides voordat je ze deelt.** `./deck <naam> beelden` geeft een PNG per slide. Overflow en te brede tabellen zie je alleen zo.

## Platen die je kunt gebruiken

Kopieer wat je nodig hebt naar `public/platen/` en verwijs ernaar met `/platen/<naam>`.

| Plaat | Waar |
|---|---|
| Informatiestromen leerroute 1, plus acht uitsneden per procesfase | `Referentiemateriaal/kaderscenario's/img/` in Npuls-OKx/Public |
| De negen Npuls-leerroutes | idem |
| MORA-hoofdprocesmodel | idem |
| Persona Jochem | `Referentiemateriaal/persona's/img/` in Npuls-OKx/Public |
| Hoofdplaat informatiestromen | `architecture/model/informatiestromen hoofdplaat OKx/1.7/` in Npuls-OKx/meta |
| Koppelvlak per component (OC, P&R, LMS, SIS, SKS) | `architecture/model/Koppelvlak views obv 1.7/` in Npuls-OKx/meta |

Een brede plaat geef je de hele slidebreedte:

```html
<img src="/platen/lr1-informatiestromen.jpg" style="width: 100%; max-height: 330px; object-fit: contain;" />
```

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
