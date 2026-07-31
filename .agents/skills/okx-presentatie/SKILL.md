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
cp _template.md JJMMDD_onderwerp.md
./deck onderwerp            # start de server en toont de URL's
./deck onderwerp beelden    # PNG per slide, om te controleren
```

**Roep `npx slidev` niet rechtstreeks aan.** De dev-server bindt dan op `[::1]`, alleen IPv6-loopback binnen de dev-container, terwijl de poortforwarding via IPv4 verbindt: de browser blijft dan herladen. Het script zet de vlag die dat oplost. `./deck` zonder argumenten toont welke decks er zijn.

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

**Stem de onderwerpen af voordat je schrijft.** Verzamel eerst, groepeer in drie tot zes onderwerpen met per onderwerp een zin over wat het betekent, en leg die lijst voor aan degene die het deck vraagt. Wat technisch de grootste wijziging is, is zelden waar het gesprek over moet gaan. Een repo-herindeling of een release-afspraak kan honderden bestanden raken en toch een voetnoot zijn, terwijl het inhoudelijke werk waar de sector op wacht in een paar documenten zit. Sorteer dus niet op omvang maar op **wat er voor dit gremium op het spel staat**. Alleen de aanvrager weet wat er op tafel moet. Noem er expliciet bij wat je zou weglaten.

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
| **Programma- en projectleiding** | Programmadoelen en planning; **geen** inhoudelijke experts | Lopen we op schema, welke risico's zijn er, welk besluit wordt gevraagd | **Informeel en direct**, alsof je het een collega vertelt. Korte zinnen, "ik" en "jullie", geen plechtige formuleringen. Geen payloads, geen ADR-nummers. Maximaal tien slides |
| **Instellingen** *(komt nog)* | De eigen onderwijspraktijk | Wat verandert er voor ons en wanneer | Nog niet uitgewerkt; stem af met de gebruiker |

Twee regels die voor elk profiel gelden. Vertaal een wijziging altijd naar **wat er nu mogelijk is dat eerst niet kon** — niet naar "document X is bijgewerkt". En sluit af met wat je van dit gremium nodig hebt: een besluit, een review, of alleen kennisname.

## Neem tabellen, cijfers en citaten letterlijk over

Bouw een tabel **nooit uit je hoofd na**. Open het bronbestand, kopieer de tabel, en kort daarna hooguit celteksten in met behoud van betekenis. Bij een ankertabel of een begrippenlijst is een verzonnen kolom of een weggelaten rij geen schoonheidsfoutje: het publiek toetst juist die tabel, en een fout ondermijnt het hele deck.

Dat ging hier al een keer mis. Een ankertabel werd uit het geheugen nagemaakt met zeven kolommen in plaats van zes, vier rijen in plaats van zeven, verzonnen korte labels en een ontbrekende examenrij. Het zag er plausibel uit en klopte niet.

Zelfde regel voor cijfers, data en citaten: haal ze uit de bron en controleer ze. Zet in de sprekersnotities waar iets vandaan komt, zodat het bij doorvragen na te lopen is.

## Onderscheid feit en inschatting

Wat uit de repositories komt is feit: aantallen open punten, deadlines, wat er gemerged is. Wat jij ervan vindt is een inschatting: of een deadline haalbaar is, waar het knelt, wat het grootste risico is.

Beide mogen in een deck, maar niet door elkaar. Formuleer een inschatting als inschatting, en meld de aanvrager welke uitspraken van jou zijn, zodat die ze kan overrulen voordat hij ze als projectstandpunt presenteert.

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

## Voor je oplevert: kijk er zelf naar

Een deck dat bouwt is niet hetzelfde als een deck dat klopt. Overflow, een tabel die te breed is, een kaart die uit beeld valt: dat zie je alleen door ernaar te kijken.

```bash
./deck onderwerp beelden
```

Dat levert een PNG per slide in `export/`. **Open die afbeeldingen en bekijk ze**, in elk geval de slides met een tabel, een pipeline of veel tekst. Toon de gebruiker daarna een of twee ervan, zodat die het resultaat ziet zonder eerst een server te hoeven starten.

Verder:

- Controleer of elke bewering terug te voeren is op iets in een van beide repositories. Verzin geen voortgang.
- Maak onderscheid tussen wat je uit de repositories hebt gehaald en wat je eigen inschatting is. Benoem dat laatste als zodanig, zodat de gebruiker het kan overrulen voordat hij het als standpunt presenteert.
- Sluit af met het commando waarmee de gebruiker het deck opent.

```bash
./deck onderwerp            # bekijken op localhost:3030
./deck onderwerp beelden    # PNG per slide
./deck onderwerp pdf        # PDF
```
