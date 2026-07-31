# Presentaties

Slidedecks over de voortgang van OKx, in de Npuls huisstijl, opgebouwd uit wat er in de OKx-repositories is gebeurd.

De aanleiding: die decks werden met de hand gemaakt terwijl alle informatie al in de repositories zit. Wie een update geeft aan de kerngroep techniek of aan programmamanagement, vertelt over besluiten, specificaties en voortgang die daar zwart op wit staan. Dat handwerk is niet nodig.

## Een presentatie maken

```bash
cd presentaties
npm install                              # eenmalig, als node_modules ontbreekt
cp _template.md JJMMDD_onderwerp.md
npx slidev JJMMDD_onderwerp.md --open     # localhost:3030
```

Met een agent: start `/presentatie`. Die volgt de skill [`okx-presentatie`](../.agents/skills/okx-presentatie/SKILL.md), vraagt voor welk gremium en welke periode, en verzamelt de wijzigingen uit beide repositories.

Exporteren:

```bash
npx slidev export JJMMDD_onderwerp.md                  # PDF
npx slidev export JJMMDD_onderwerp.md --format pptx
```

## Wat er in deze map staat

| Onderdeel | Rol |
| --- | --- |
| `_template.md` | Startpunt met werkende voorbeelden van elk slidetype |
| `style.css` | Het designsysteem: Npuls-fonts, kleurtokens en de `np-`-componentbibliotheek |
| `public/npuls/` | Achtergronden, illustraties, logo en lettertypen |
| `JJMMDD_onderwerp.md` | De presentaties zelf |

Pas de huisstijl alleen aan in `style.css`, nooit per presentatie. Bouw slides met de `np-`-classes; verzin geen losse inline-stijlen waar een class bestaat.

## Twee dingen die vastliggen

**De decks blijven hier.** Ze horen niet in `Npuls-OKx/Public`: dat repository draagt releaseartefacten waarmee een afnemer een koppelvlak bouwt. Een presentatie over de voortgang is iets anders en zou dat repository vervuilen. De inhoud van een deck komt wél uit beide repositories.

**Het publiek bepaalt het abstractieniveau.** Programmamanagement krijgt geen payloads te zien en de kerngroep techniek geen managementsamenvatting. De profielen per gremium staan in de skill; maak liever twee decks dan één compromis.

## Herkomst

Het designsysteem, de achtergronden en de componentbibliotheek zijn overgenomen uit [`cedanl/clidev-presentaties`](https://github.com/cedanl/clidev-presentaties), het presentatieproject van CEDA. De werkwijze en de huisstijl komen uit de skills [`clidev`](https://github.com/cedanl/.github/tree/main/.claude/skills/clidev) en [`npuls-huisstijl`](https://github.com/cedanl/.github/tree/main/.claude/skills/npuls-huisstijl) in `cedanl/.github`; die zijn gevendord onder [`.agents/skills/`](../.agents/skills/) en worden niet bewerkt.

De Npuls huisstijl is eigendom van Npuls. OKx is een Npuls-programma, dus het gebruik valt binnen de voorwaarden.
