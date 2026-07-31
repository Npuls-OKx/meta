---
name: okx-presentatie
description: Maak een OKx-presentatie of update-deck in Slidev, op basis van de wijzigingen in de OKx-repositories. Gebruik wanneer iemand een presentatie, slidedeck, voortgangsupdate of business update over OKx wil, of wanneer de gebruiker /presentatie start. Kent de stakeholderprofielen (SI-team, adviesgroep, leveranciers, kerngroep techniek, technische werkgroep OEAPI, programmamanagement) en haalt wijzigingen op uit zowel Npuls-OKx/meta als Npuls-OKx/Public.
---

# OKx-presentatie

Adaptatie-wrapper rond de externe skills [`clidev`](../clidev/SKILL.md) (Slidev-workflow) en [`npuls-huisstijl`](../npuls-huisstijl/SKILL.md) (merkbronwaarheid). Die twee zijn gevendord en worden **niet** bewerkt; wat OKx-specifiek is staat hier.

Wat deze skill toevoegt: waar het project staat, hoe je de inhoud uit twee repositories haalt, en voor wie je schrijft.

## Het project

De presentaties leven in [`presentaties/`](../../../presentaties/) in `Npuls-OKx/meta`. Daar staan `style.css`, `_template.md` en de achtergronden onder `public/npuls/`.

```bash
cd presentaties
npm install                              # eenmalig, als node_modules ontbreekt
cp _template.md JJMMDD_onderwerp.md
npx slidev JJMMDD_onderwerp.md --open
```

Naamconventie `JJMMDD_onderwerp.md`, bijvoorbeeld `260731_update_kerngroep_techniek.md`. Voor de opbouw van slides, de `np-`-componentbibliotheek en de technische valkuilen: lees `clidev`. Die regels gelden hier onverkort.

**De slidedecks blijven in `Npuls-OKx/meta`.** Ze horen niet in `Npuls-OKx/Public`: dat repository draagt releaseartefacten waarmee een afnemer bouwt, geen presentaties over de voortgang. Genereer dus nooit een deck in de Public-werkmap, ook niet als de inhoud daarvandaan komt.

## Inhoud ophalen uit twee repositories

OKx werkt met twee repositories die naast elkaar in de workspace staan:

| Repository | Werkmap | Wat je eruit haalt |
|---|---|---|
| `Npuls-OKx/meta` | `/workspaces/OKx/OKx-meta` | Kaderstelling, ArchiMate-model, meeting-notulen, het OEAPI consumer-profiel |
| `Npuls-OKx/Public` | `/workspaces/OKx/Public` | Releaseartefacten: koppelvlakspecificaties, referentiemateriaal, besluiten |

Een update-deck gaat over wat er in **beide** is gebeurd. Verzamel per repository over de gevraagde periode:

```bash
# gemergde pull requests, met titel en datum
gh pr list --repo Npuls-OKx/meta   --state merged --limit 50 \
  --json number,title,mergedAt,url --jq '.[] | select(.mergedAt > "JJJJ-MM-DD")'
gh pr list --repo Npuls-OKx/Public --state merged --limit 50 \
  --json number,title,mergedAt,url --jq '.[] | select(.mergedAt > "JJJJ-MM-DD")'

# welke bestanden zijn erbij gekomen of gewijzigd
git -C /workspaces/OKx/OKx-meta log --since=JJJJ-MM-DD --name-status --oneline dev
git -C /workspaces/OKx/Public   log --since=JJJJ-MM-DD --name-status --oneline dev
```

Staat een repository niet lokaal, val dan terug op de GitHub API via `gh`.

Lees niet alleen de commit-titels. Een titel zegt *wat* er is gewijzigd; een deck moet zeggen **wat het betekent**. Open de gewijzigde documenten en de pull request-beschrijvingen: daar staat de aanleiding en de afweging. Noem in het deck geen PR-nummers of bestandsnamen tenzij het publiek daar iets aan heeft.

**Noem altijd om welke repository het gaat** als je een branch, pull request of issue noemt. Beide repositories hebben eigen nummering; `#7` alleen is dubbelzinnig.

## Voor wie schrijf je

Het publiek bepaalt het abstractieniveau, niet de inhoud die toevallig voorhanden is. Vraag de gebruiker voor welk gremium het deck is en gebruik het passende profiel. Bij meerdere gremia: maak aparte decks, geen compromis.

| Gremium | Weet al | Wil weten | Toon en diepgang |
|---|---|---|---|
| **SI-team (intern)** | De hele context, het jargon, de historie | Wat is er af, wat loopt vast, waar is een besluit nodig | Kort en direct. Openstaande punten en blokkades voorop. Details mogen |
| **Adviesgroep** | Onderwijskundig sterk; wisselend technisch. IM'ers uit instellingen brengen instellingscontext mee | Wat betekent dit voor het onderwijs en voor hun instelling | Begin bij de leerroute en de student, niet bij de payload. Leg technische termen uit bij eerste gebruik |
| **Leveranciers** | Hun eigen systeem en de integratiepraktijk | Wat moeten wij straks bouwen, wanneer, en wat verandert er nog | Concreet over koppelvlakken en contracten. Wees expliciet over wat vaststaat en wat nog concept is |
| **Kerngroep techniek OKx** | De keten en de architectuur | Klopt de richting, en is de kaderstelling ver genoeg om spec te starten | Diep. Besluiten, alternatieven en open punten. Toon de ankertabel en de payloads |
| **Technische werkgroep OEAPI** | De OEAPI-standaard | Hoe verhoudt OKx zich tot OEAPI, en welke signaleringen komen eruit | Vergelijkend. Benoem waar we afwijken en waarom, en welke wijzigingsverzoeken richting OEAPI gaan |
| **Programmamanagement** | Programmadoelen en planning; **geen** inhoudelijke experts | Lopen we op schema, welke risico's zijn er, welk besluit wordt gevraagd | Business-taal. Geen payloads, geen ADR-nummers. Voortgang, risico's, beslispunten. Maximaal tien slides |
| **Instellingen** *(komt nog)* | De eigen onderwijspraktijk | Wat verandert er voor ons en wanneer | Nog niet uitgewerkt; stem af met de gebruiker |

Twee regels die voor elk profiel gelden. Vertaal een wijziging altijd naar **wat er nu mogelijk is dat eerst niet kon** — niet naar "document X is bijgewerkt". En sluit af met wat je van dit gremium nodig hebt: een besluit, een review, of alleen kennisname.

## Opbouw van een update-deck

Een werkbare basisvorm; wijk af waar de inhoud daarom vraagt.

1. **Titel** — periode en gremium
2. **Waar we stonden** — één slide, zodat het deck zelfstandig te lezen is
3. **Wat er is gebeurd** — per thema, niet per repository of per pull request. Het publiek denkt in onderwerpen
4. **Wat dat betekent** — de consequentie voor dit gremium
5. **Openstaande punten en risico's** — eerlijk over wat vastloopt
6. **Wat we vragen** — besluit, review of kennisname
7. **Afsluitslide**

Voor programmamanagement schuiven 5 en 6 naar voren; voor de kerngroep techniek is 3 en 4 het zwaartepunt.

## Voor je oplevert

- Draai het deck en kijk ernaar. Overflow zie je alleen in de browser.
- Controleer of elke bewering in het deck terug te voeren is op iets in een van beide repositories. Verzin geen voortgang.
- Meld de gebruiker het pad en het commando om het deck te openen.

```bash
npx slidev JJMMDD_onderwerp.md --open        # bekijken op localhost:3030
npx slidev export JJMMDD_onderwerp.md        # PDF
npx slidev export JJMMDD_onderwerp.md --format pptx
```
