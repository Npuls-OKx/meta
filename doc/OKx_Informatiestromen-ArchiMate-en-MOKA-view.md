# Informatiestromen, ArchiMate-model en MOKA-koppelvlak-view (Basis Model)

Dit document is bedoeld voor **nieuwe aanhakers**: hoe de **hoofdplaat** en de **tabel met informatiestromen** in het [projectoverzicht](OKx_Projectoverzicht.md) samenhangen met het **ArchiMate-model** in deze repository, en **waar** je de grote MOKA-**koppelvlakspecificatie-view** **Basis Model** vindt.

Het is **geen** volledige uitleg van het MOKA-metamodel; zie principes in [`architecture/docs/principes/doc/principes.md`](../architecture/docs/principes/doc/principes.md) en de [ADR’s over keten en fundament](../architecture/dr/0002-prioriteitsketen-catalogus-drielagen-fundament.md).

## Drie lagen: plaat, model, en één view

| Laag | Wat je ziet | Rol |
|------|-------------|-----|
| **Ketenplaat + tabel** | PNG *Hoofdplaat OKx informatiestromen* en de nummering (stromen 1–17) in [OKx_Projectoverzicht](OKx_Projectoverzicht.md) | **Strategisch overzicht**: welke **referentiecomponenten** (systemen/rollen) en welke **semantiek** van de stroom (bijv. *Uitgewerkt aanbod*). |
| **ArchiMate-model** | Bestand [`architecture/model/model.archimate`](../architecture/model/model.archimate) | **Structureel model**: processen, rollen, applicatie- en informatie-elementen en **relaties** in meerdere **views** (diagrammen). Niet alles staat op één plaatje. |
| **MOKA-koppelvlakspecificatie-view** | Één **diagram-view** binnen het model, ingericht volgens het **MOKA-metamodel** voor het koppelvlak *Onderwijsvisie vertalen naar onderwijsaanbod* | **Verdieping** van hoe dit koppelvlak is uitgewerkt: o.a. proces en informatie in samenhang. De view **Basis Model** is één **variant** (naast o.a. Klassiek en Flexibel). |

```mermaid
flowchart LR
  plaat[Hoofdplaat_en_tabel]
  archi[ArchiMate_model_archimate]
  view[Basis_Model_view]

  plaat -->|"conceptueel dezelfde keten"| archi
  archi -->|"opent in tool als views"| view
```

## Waar vind je de view in Archi (of vergelijkbare tool)?

1. Clone of open deze repository en open **Archi** (of een andere ArchiMate-tool die `.archimate` importeert).
2. Open het bestand: **`architecture/model/model.archimate`**.
3. Ga in de **model browser** naar **Views** → map **OKx** → **Onderwijs visie vertalen naar onderwijsaanbod**.
4. Open het diagram met de exacte naam:

   **`01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model`**

In het XML-bestand komt dit diagram overeen met een `ArchimateDiagramModel` met die naam (het canvas is **zeer groot**; gebruik **zoom**, **pan** en eventueel **zoeken op elementnaam**).

## Hoe lees je de Basis Model-view als beginner?

1. **Start bij de hoofdplaat** in het projectoverzicht: zoek **stroom 1** — *Curriculum ontwerptool* → *Onderwijscatalogus*, *Uitgewerkt aanbod*. Dat is de **eerste prioriteitsstroom** (zie ook [ADR 0002](../architecture/dr/0002-prioriteitsketen-catalogus-drielagen-fundament.md)).
2. **In de Basis Model-view** zoek je naar de **zelfde logica**: processen en informatie rond **ontwerp van** en **vastlegging in** de onderwijscatalogus. Namen in ArchiMate kunnen **niet letterlijk** gelijk zijn aan de PNG (afkortingen, synoniemen), maar de **keten** hoort herkenbaar te zijn.
3. **MOKA-koppelvlakspecificatie**-views combineren typisch **proces** (wat gebeurt er) met **informatie** (welke objecten gaan over de lijn). Volg **pijlen/relaties** als “informatiestroom”; koppel ze mentaal aan de **semantische kolom** in de tabel (bijv. *Uitgewerkt aanbod*).

Als je iets niet terugvindt: **geen fout in jouw lezen** — het model groeit iteratief; meld een **issue** of vraag het kernteam.

## Wat dit document niet is

- Geen vervanging van **MOKA-template**-instructies onder `moka-koppelvlakspecificaties/`.
- Geen export van **alle** elementen uit het Basis Model (het bestand is groot).
- Geen wijzigingshandleiding voor `model.archimate`: wijzigingen lopen via **pull requests** (zie [Bijdragen voor beginners](Bijdragen-voor-beginners.md) en [CONTRIBUTING](../CONTRIBUTING.md)).

## Zie ook

- [OKx Architectuurbesluiten en impact](OKx_Architectuurbesluiten-en-impact.md)
- [OKx Informatiestromen](OKx_Informatiesstromen.md)
- [OKx Projectoverzicht](OKx_Projectoverzicht.md)
