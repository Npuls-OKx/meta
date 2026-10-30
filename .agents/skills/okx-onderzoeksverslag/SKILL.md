---
name: okx-onderzoeksverslag
description: Een onderzoeksverslag schrijven of herzien dat een openstaande vraag onderbouwt zonder haar te beslissen: bronplicht per bewering, het onderscheid tussen wat er staat en wat je afleidt, de alternatieven met hun kosten, en een advies in plaats van een besluit. Gebruik bij elk verslag onder architecture/agent-artifacts/research/, en wanneer een bestaand verslag een besluit formuleert dat het team nog moet nemen.
---

# Een onderzoeksverslag in OKx

Een onderzoeksverslag beantwoordt een vraag waarvan het antwoord de richting bepaalt, voordat er iets ontworpen wordt. Het levert de onderbouwing; het besluit valt elders.

Dat onderscheid is de hele skill. Een verslag dat een besluit formuleert neemt het team iets af: de afweging is dan al gemaakt, en wie het leest kan alleen nog instemmen of tegenspreken. Een verslag dat adviseert geeft het team waar het om vroeg, namelijk het materiaal om zelf te kiezen.

```text
onderzoeksverslag   wat is er, wat leid ik daaruit af, welke richtingen zijn er
   (meta)           advies met de alternatieven en hun kosten
        |
        v
      ADR           het besluit, met de afweging en de gevolgen
   (Public)         verwijst terug naar het verslag
```

## Woorden en koppen

De vorm verraadt zich in de werkwoorden. Links hoort in het verslag, rechts in het architectuurbesluit dat erop volgt. Deze tabel is de snelste controle op een concept.

| In een verslag | In een ADR |
|---|---|
| "De opbouw van OKE is navolgbaar, en zij werkt omdat het aantal stromen vastligt" | "OKx neemt de opbouw over" |
| "Wat ertegen pleit is de omvang: bij dertien componenten loopt de bundeling vast" | "De bundeling draagt niet over" |
| "Drie richtingen liggen open, met per richting wat zij kost" | "Het besluit is richting twee" |
| "Dit verslag raadt aan om eerst X te doen, omdat Y" | "Wij doen eerst X" |
| "Hier kan dit verslag niets over zeggen, want Z is niet uitgezocht" | "Z valt buiten dit besluit" |

Kopteksten volgen dezelfde regel. `Advies`, `Suggesties` en `Open punten` horen bij een verslag. `Besluit`, `Besluitvoorstel` en `Gevolgen` horen in een ADR.

Een kop is een label en geen zin, net als overal in OKx. De val bij een verslag zit in de koppen die het oordeel dragen.

| Zin | Label |
|---|---|
| Wat dit verslag aanraadt | Advies |
| Wat dit verslag openlaat | Open punten |
| Wat er niet geverifieerd kon worden | Onzekerheden |
| Waarom de ander dit wel kan | De afbakening bij `<naam>` |
| Wat de vergelijking oplevert | Vergelijking |

## Eisen

Deze staan in de [index van de onderzoeksverslagen](../../../architecture/agent-artifacts/research/README.md) en gelden onverkort.

- **Elke bewering draagt een bronvermelding**, met volledige URL en waar mogelijk een paragraaf- of paginanummer. Een paragraafnummer maakt een uitspraak naslaanbaar; een link naar een document van honderd paginas niet.
- **Onderscheid wat er staat van wat je afleidt.** Beide mogen, maar een afleiding is herkenbaar als afleiding. De eenvoudigste vorm: de bron in een eigen kolom of in een eigen zin, en de afleiding als aparte zin ervoor of erna.
- **Benoem wat je niet hebt kunnen verifieren.** Een verslag zonder onzekerheden is verdacht: het onderzoek ging niet ver genoeg, of de gaten zijn dichtgeschreven.
- **Geen aanbeveling zonder afweging.** Komt het verslag tot een advies, dan staan de alternatieven en hun kosten erbij.

## De opbouw

Een vaste volgorde, zodat een lezer weet waar hij is.

| Hoofdstuk | Wat erin staat |
|---|---|
| Inleiding | Context (waarom nu), doel (de vragen, genummerd), scope (wat erbuiten valt en waar dat dan wel ligt) |
| Wat de bron is | Het onderzochte materiaal feitelijk beschreven, met de paragraafnummers erbij |
| Wat onze situatie is | Hetzelfde voor OKx, met per uitspraak de vindplaats in de eigen repositories |
| De vergelijking | Per as wat beide kanten doen en wat dat betekent. Een tabel, geen betoog |
| De open keuze | Waar het materiaal geen antwoord geeft, met de kandidaten en wat tegen elk pleit |
| Advies | De aanbevelingen met hun reden, de suggesties, en de punten die open blijven |
| Bronnen | Elke bron met waarvoor hij gebruikt is |

Voor een vergelijkend verslag is de as de bouwsteen. Houd de assen gelijk aan beide kanten, en zet per as in een eigen kolom wat het betekent. Een as waarop de ene kant niets heeft is informatie en geen leemte in het onderzoek.

## Vergelijkende verslagen

De valkuil bij een vergelijkend verslag: de ene kant heeft iets opgelost dat bij ons nog open staat, en dan ligt de conclusie voor de hand dat wij het net zo moeten doen. Dat is zelden waar, en het verslag kan het niet weten.

Zeg in dat geval drie dingen uit elkaar.

1. **Wat de ander oplost**, feitelijk, met de bron.
2. **Waarom dat daar werkt**, met de eigenschap die het mogelijk maakt. Vaak is dat een afbakening die wij niet hebben.
3. **Wat er bij ons voor nodig zou zijn**, als open punt, zonder te doen alsof dat al besloten is.

Zo blijft zichtbaar dat de vraag bij het team ligt, en krijgt het team wel het materiaal om hem te beantwoorden.

## Plaats, naam en status

| | |
|---|---|
| Map | `architecture/agent-artifacts/research/` |
| Bestandsnaam | `JJJJMMDD_UUMM_onderwerp.md`, met het tijdstip waarop het onderzoek startte |
| Index | Een rij in de [README](../../../architecture/agent-artifacts/research/README.md) met het verslag, de vraag en de status |
| Status | `In uitwerking`, `Ter bespreking` of `Afgerond`. Een verslag draagt geen status die suggereert dat het zelf iets beslist |

Boven in het verslag staat de regel `Relateert aan:` met de issues die het raakt. Een metadatakop komt er niet in: GitHub draagt auteurschap en datum.

## Controlelijst

- [ ] Geen kop of zin die een besluit formuleert; de tabel met werkwoorden hierboven langsgelopen.
- [ ] Elke bewering over de bron draagt een paragraaf- of paginanummer.
- [ ] Elke bewering over OKx draagt een vindplaats in meta of Public.
- [ ] De alternatieven staan er met wat tegen elk pleit.
- [ ] Wat niet verifieerbaar was staat benoemd.
- [ ] De index draagt de rij, met een status die klopt.
- [ ] `python3 tools/scripts/validate-docs.py <pad>` slaagt.

## Verwante skills

| Skill | Verhouding |
|---|---|
| [okx-referentiearchitectuur-eerst](../okx-referentiearchitectuur-eerst/SKILL.md) | Legt elk begrip eerst tegen ROSA, MORA en HORA; een verslag dat een begrip introduceert passeert die toets |
| [okx-product-flow](../okx-product-flow/SKILL.md) | Het verslag is invoer voor stap 1 en 2; de review in stap 3 toetst of het advies een advies gebleven is |
| [okx-schrijfstijl-review](../okx-schrijfstijl-review/SKILL.md) | Toetst de tekst op de schrijfstijl; deze skill toetst de stand van het oordeel |
