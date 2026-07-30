# Sjabloon payload-specificatie

Kopieer dit bestand naar `<koppeling>/<datum>_<naam>-payload-json.md` of naar `gedeeld/` als meerdere koppelingen de payload delen. Lees eerst de [uitgangspunten](uitgangspunten.md).

De kern staat voorin: een lezer heeft de payload binnen twee schermen. Alle motivering komt erachter.

**Instructies staan tussen `<!-- -->` en verdwijnen in de weergave.** Verwijder ze als het onderdeel af is.

---

# \<Objectnaam\> als JSON-payload

Relateert aan: #\<issue\>. Waarden in het voorbeeld zijn indicatief.

## Inhoudsopgave

1. [Inleiding](#1-inleiding) (context, doel, scope)
2. [Payload](#2-payload)
   - [2.1 De vorm](#21-de-vorm)
   - [2.2 Het voorbeeld](#22-het-voorbeeld)
3. [Toelichting bij de keuzes](#3-toelichting-bij-de-keuzes)
4. [Open punten](#4-open-punten)
5. [Gerelateerde uitwerkingen](#5-gerelateerde-uitwerkingen)

## 1. Inleiding

### 1.1 Context

<!-- Wat is dit object in de werkelijkheid, en welke plek heeft het in de ankertabel?
     Wie maakt het, wie gebruikt het? Begin bij het onderwijs, niet bij de JSON. -->

\<Wat is dit object, in twee of drie zinnen die beginnen bij het onderwijs.\>

\<Welke begrippenfamilie uit de ankertabel is dit, en hoe verhoudt het zich tot de buren?\> Zie [U6](uitgangspunten.md#u6-semantiek-uit-de-ankertabel).

Scenario en persona conform [U9](uitgangspunten.md#u9-scenarios-en-personas). Ketenoverzicht en afkortingen: de [instap in de README](README.md#context).

### 1.2 Doel

Deze payload is indicatief en onderbouwt welke velden het koppelvlak nodig heeft ([U1](uitgangspunten.md#u1-indicatief-en-onderbouwend-niet-voorschrijvend)).

Het document beantwoordt \<aantal\> vragen:

- \<vraag over de vorm\>
- \<vraag over de samenhang met andere payloads\>
- \<vraag over een specifiek ontwerpprobleem\>

Geslaagd wanneer \<toetsbaar criterium, bijvoorbeeld: een leverancier bouwt en leest de payload zonder aanvullende uitleg\>.

### 1.3 Scope

In scope is \<positieve afbakening\>.

\<Aantal\> afbakeningen die anders verwarring geven:

- **\<onderwerp\>** \<waarom het er niet in zit\>.

Al het overige valt buiten dit document.

## 2. Payload

<!-- Leeswijzer: geef elk artefact één taak, anders leest het als redundantie. -->

Het **informatiemodel**, het **JSON Schema** en de **schemaboom** leggen samen de vorm vast. De **payload** en de **instantiebomen** geven het voorbeeld.

### 2.1 De vorm

<!-- Eén erDiagram: welke objecten en hoe hangen ze samen. Zet eronder alleen wat
     het model niet kan dragen (bijvoorbeeld: waarom een relatie additief is). -->

```mermaid
erDiagram
    ENTITEIT ||--o{ ENTITEIT : "ouder-verwijzing"
    ENTITEIT {
        uuid id PK
        string \<type\> "discriminator"
        uuid bovenliggend\<Soort\>Id FK "null op root"
    }
```

Het schema legt de exacte vorm vast: welke velden er zijn, welke verplicht zijn en welke waarden een veld mag dragen. Het is **alfa en indicatief** en verandert mee zolang de payload nog niet vaststaat.

<!-- Enums horen HIER, in het schema, niet in een aparte tabel (U8).
     Sleutelconventie: id voor de eigen sleutel, expliciete naam bij verwijzingen (U7). -->

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://okx.npuls.nl/schema/<naam>/alfa",
  "title": "<Objectnaam>",
  "$comment": "Alfa en indicatief. Deze vorm onderbouwt welke velden het koppelvlak nodig heeft en kan wijzigen zolang de payload niet is vastgesteld.",
  "type": "object",
  "required": ["<array>"],
  "properties": {
    "<array>": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "<type>", "versie"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "<type>": { "enum": ["<waarde1>", "<waarde2>"] },
          "versie": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
          "bovenliggend<Soort>Id": { "type": ["string", "null"], "format": "uuid" }
        }
      }
    }
  }
}
```

Dezelfde vorm, leesbaar:

<!-- Laat de marker leeg staan en draai: python3 scripts/json-tree.py --write <bestand> -->

<!-- json-tree:begin kind=schema -->
<!-- json-tree:end -->

### 2.2 Het voorbeeld

Leerroute 1. \<Waar komen de uuid's vandaan als je naar een andere payload verwijst?\>

```json
{
  "<array>": [
    {
      "id": "<uuid>",
      "<type>": "<waarde1>",
      "versie": "0.1.0",
      "bovenliggend<Soort>Id": null
    }
  ]
}
```

De boom die in deze platte lijst verborgen zit, met de verwijzingen opgelost:

<!-- Eén marker per platte array. entity=<naam> alleen als de objecten geen typeveld hebben. -->

<!-- json-tree:begin kind=instance array=<array> id=id parent=bovenliggend<Soort>Id label=naam type=<type> attrs=versie -->
<!-- json-tree:end -->

<!-- Zet hier de duiding die de boom zelf niet geeft: waarom bepaalde objecten losse
     roots zijn, waarom een tak leeg is. De generator levert structuur, de tekst betekenis. -->

\<Duiding bij de boom.\>

## 3. Toelichting bij de keuzes

<!-- Alles wat motiveert komt hier, achter de kern. Verwijs naar de uitgangspunten in
     plaats van ze over te schrijven. -->

### 3.1 Ontwerpkeuzes

- **Plat met verwijzingen** ([U7](uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie)). \<Wat betekent dat specifiek voor deze payload?\>
- **\<keuze\>.** \<motivering\>

### 3.2 \<Deelmodel of achtergrond\>

<!-- Bijvoorbeeld een locatiemodel, een organisatiemodel of de lifecycle. -->

## 4. Open punten

| Vraag | Vervolgstap |
|---|---|
| \<vraag\> | \<wie doet wat, en wanneer\> |

## 5. Gerelateerde uitwerkingen

<!-- Alleen echte verwijzingen. Open punten horen in hoofdstuk 4. -->

- [Uitgangspunten voor koppelingspecificaties](uitgangspunten.md): de gedeelde aannames waarop deze payload steunt.
- \<andere documenten, als echte links\>
