---
name: okx-koppelingspecificatie
description: >-
  Vaste opbouw en conventies voor OKx-koppelingspecificaties (de informatiestroom
  tussen twee referentiecomponenten) en payload-specificaties (de JSON die over
  die koppeling gaat). Bevat de verplichte inleiding met context, doel en scope,
  de indeling met de kern naar voren, de veldnaamgeving in payloads, de
  schema- en boomconventies, en een indienchecklist. Gebruik bij het schrijven,
  herzien of reviewen van een koppelingspecificatie of payload-specificatie
  onder architecture/agent-artifacts/design-docs/koppelingspecificaties/.
---

# Koppeling- en payload-specificaties

Twee documentsoorten met een vaste opbouw. Terminologie volgt [ADR 0021](../../../architecture/dr/0021-koppeling-versus-koppelvlak-terminologie.md): een **koppeling** is de informatiestroom tussen twee referentiecomponenten, een **koppelvlak** is de verzameling koppelingen van één component.

## Doelbinding (waarom deze documenten bestaan)

Koppelingspecificaties zijn **indicatief en onderbouwend, niet voorschrijvend**. OKx legt de sector niet op hoe een koppeling gerealiseerd moet worden. We bestuderen het ecosysteem koppeling voor koppeling en scenario voor scenario om te ontdekken welke operaties, endpoints en data nodig zijn. De som van de koppelingbeschrijvingen leidt tot de **koppelvlakspecificatie** per component, en er blijft ruimte voor behoeften die nu nog niet uit de scenario's naar voren komen.

Zet die binding in elk document in §1.2, zodat een lezer niet denkt dat we koppelingen dichttimmeren.

## Opbouw koppelingspecificatie

1. Inleiding (1.1 Context, 1.2 Doel, 1.3 Scope)
2. Procesbeeld
3. Interactieoverzicht
4. Informatiemodel
5. Sequentiediagrammen
6. Payload-specificaties (verwijzing) en gebruiksprofiel
7. Endpointbeschrijvingen (REST)
8. Reviewvragen
9. Open punten
10. Gerelateerde uitwerkingen

Alle drie de koppelingspecificaties volgen deze nummering, ook wanneer een sectie nog leeg is. Zijn de endpoints nog niet uitgewerkt, zet dan onder §7 waarom niet en wanneer wel, in plaats van de sectie weg te laten. Dan blijft een verwijzing als "§7" over de documenten heen kloppen.

## Opbouw payload-specificatie

De kern staat voorin. Een lezer heeft de payload binnen twee schermen.

1. Inleiding (1.1 Context, 1.2 Doel, 1.3 Scope)
2. Payload
   - 2.1 De vorm: informatiemodel (ERD), JSON Schema, schemaboom
   - 2.2 Het voorbeeld: payload (JSON) en instantieboom
3. Toelichting bij de keuzes (ontwerpkeuzes, deelmodellen, achtergrond)
4. Open punten, als tabel met per vraag een vervolgstap
5. Gerelateerde uitwerkingen, alleen echte verwijzingen

## De inleiding

Eén hoofdstuk met drie subsecties. Na het lezen daarvan weet een nieuwkomer waar het document voor is, wat er wel en niet in staat, en hoe het is ontstaan.

- **1.1 Context.** Waar de koppeling in de keten zit (met stroomnummer uit het projectoverzicht), voor wie het document is, en hoe het is ontstaan: werksessie, afgeleid, of voortbouwend op een ander document. Verwijs naar het scenario en de persona. Geen opsomming van losse bronnen; een bron is invoer, geen context.
- **1.2 Doel.** In twee vormen: **welke vragen beantwoordt dit document**, en **wanneer is het geslaagd**. Neem geen doelen op die buiten het document liggen.
- **1.3 Scope.** Positief geformuleerd: wat er in scope is. Sluit af met de regel dat al het overige buiten scope valt, zodat de lezer niet hoeft te raden of iets vergeten of bewust weggelaten is. Noem uitzonderingen die verwarring wekken expliciet.

## Payload-conventies

- **Nederlands.** Veldnamen en waarden in het Nederlands. Wijkt dat af van de OEAPI-vorm, noteer dat als signalering in plaats van het stil te laten.
- **Sleutels.** `id` voor de eigen sleutel van een object binnen zijn array; een expliciete getypeerde naam zodra je ergens anders heen wijst (`bovenliggendSpecificatieId`, `leeruitkomstId`, `specificatieVerwijzing.specificatieId`). Een kaal `bovenliggendId` is context-gevoelig en dus verboden.
- **Plat met verwijzingen.** Objecten staan in platte arrays met een zelfverwijzende ouder-pointer, niet fysiek genest. Daardoor is de boom in de JSON onzichtbaar; de instantieboom maakt hem weer zichtbaar. Beide horen erbij.
- **JSON Schema.** Elke payload-specificatie draagt een JSON Schema (draft 2020-12) dat de vorm vastlegt: types, verplicht of optioneel, enums, patronen. Enumeraties horen in het schema, niet in een aparte tabel. Markeer de volwassenheid **in het schema zelf** (`$comment`, `description`) met alfa en indicatief; die markering hoort niet in de documenttitel of de doelstelling.
- **Gebruiksprofiel.** Gedeelde payloads staan éénmaal centraal. Elke koppelingspecificatie benoemt welke objecten en velden zij gebruikt.

## Schema- en instantiebomen

Gegenereerd met `scripts/json-tree.py`, tussen HTML-comment-markers zodat de bomen bij de JSON blijven kloppen:

```
<!-- json-tree:begin kind=schema -->
<!-- json-tree:begin kind=instance array=aanbodInstanties id=id parent=bovenliggendAanbodId label=naam type=aanbodType attrs=versie,status -->
```

Draai `python3 scripts/json-tree.py --check <document>` vóór de commit; het script meldt ook dode ouder-verwijzingen en cykels, en valideert het voorbeeld tegen het schema.

Gebruik géén `<details>`-inklapblokken voor payloads. De documentatie moet ook als PDF werken, en daar verdwijnt de inhoud van een `<details>` (pandoc laat raw HTML vallen, print-to-PDF drukt dichtgeklapt af).

Boomstijl volgt de ASCII-conventies uit [`mbo-informatie-modelleur`](../mbo-informatie-modelleur/SKILL.md): ```text-fence, `+--`, `` `-- ``, `|`, entiteit in HOOFDLETTERS, instantie met `=`.

Zet onder een gegenereerde boom een korte duiding van wat de structuur zelf niet vertelt, bijvoorbeeld waarom bepaalde objecten losse roots zijn. De generator levert structuur, de tekst levert betekenis.

## Diagrammen

- Mermaid **zonder puntkomma's**; die breken de GitHub-parser.
- Eén diagramstijl per documentsoort. Een informatiemodel is overal een `erDiagram`, een procesbeeld overal een `flowchart`.
- Diagram, tabel en alinea die hetzelfde zeggen is redundantie. Kies één drager.

## Indienchecklist

Loop dit af voordat je een document ter review aanbiedt.

- [ ] Inleiding is zelfdragend: context, doel en scope staan er, en de scope sluit af.
- [ ] Kern staat voorin (payload-specificaties: payload in hoofdstuk 2).
- [ ] Geen vulwoorden ("kort", "conceptueel", "een eerste") in kopjes of zinnen.
- [ ] Geen statusaanduiding ("alpha") in titel, doel of scope; wel op het schema.
- [ ] Afkortingen voluit bij eerste gebruik; mapnamen toegelicht.
- [ ] Verwijzingen naar besluiten en documenten zijn echte links.
- [ ] Geen diagram plus tabel plus alinea met dezelfde inhoud.
- [ ] Elk kopje dekt de lading; "Context" geeft context.
- [ ] De tekst is leesbaar zonder er een issue bij te halen.
- [ ] Open punten hebben een concrete vraag en een vervolgstap.
- [ ] `json-tree.py --check` en de linkcontrole zijn schoon.

Bredere schrijfstijl staat in [`docs-style`](../../rules/docs-style.mdc).

## Verhuisnotitie

Deze skill staat in `.cursor/skills/` omdat dat de indeling van deze branch is. Branch 115 verplaatst alle skills naar de canonieke map `.agents/skills/` met symbolische links vanuit `.cursor` en `.claude`. Verplaats deze skill na die merge mee, en laat de indienchecklist opgaan in de `okx-semantiek-review`-skill zodat de reviewer en de schrijver dezelfde maatstaf hanteren.
