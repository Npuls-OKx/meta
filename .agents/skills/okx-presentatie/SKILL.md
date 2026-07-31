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
./deck onderwerp statisch   # bouwen en serveren zonder live-herladen
./deck onderwerp beelden    # PNG per slide, om te controleren
```

Blijft de browser herladen, wijs dan op `statisch`. De dev-server houdt een websocket open voor live wijzigingen; komt die verbinding niet tot stand, dan laadt de browser eindeloos opnieuw. De gebouwde versie heeft die websocket niet en is daarmee de betrouwbare keuze om mee te presenteren.

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
| **Adviesgroep** | Onderwijskundig sterk; wisselend technisch. IM'ers uit instellingen brengen instellingscontext mee | Wat betekent dit voor het onderwijs en voor hun instelling | **Even informeel als bij de leiding, maar met meer uitleg.** Het is een interne groep vakgenoten: "jullie", korte zinnen, geen plechtigheid. Wel elke stap toelichten en bij de leerroute beginnen, niet bij de payload |
| **Leveranciers** | Hun eigen systeem en de integratiepraktijk | Wat moeten wij straks bouwen, wanneer, en wat verandert er nog | Concreet over koppelvlakken en contracten. Wees expliciet over wat vaststaat en wat nog concept is |
| **Kerngroep techniek OKx** | De keten en de architectuur | Klopt de richting, en is de kaderstelling ver genoeg om spec te starten | Diep. Besluiten, alternatieven en open punten. Toon de ankertabel en de payloads |
| **Technische werkgroep OEAPI** | De OEAPI-standaard | Hoe verhoudt OKx zich tot OEAPI, en welke signaleringen komen eruit | Vergelijkend. Benoem waar we afwijken en waarom, en welke wijzigingsverzoeken richting OEAPI gaan |
| **Programma- en projectleiding** | Programmadoelen en planning; **geen** inhoudelijke experts | Lopen we op schema, welke risico's zijn er, welk besluit wordt gevraagd | **Informeel en direct**, alsof je het een collega vertelt. Korte zinnen, "ik" en "jullie", geen plechtige formuleringen. Geen payloads, geen ADR-nummers. Maximaal tien slides |
| **Instellingen** *(komt nog)* | De eigen onderwijspraktijk | Wat verandert er voor ons en wanneer | Nog niet uitgewerkt; stem af met de gebruiker |

Twee regels die voor elk profiel gelden. Vertaal een wijziging altijd naar **wat er nu mogelijk is dat eerst niet kon** — niet naar "document X is bijgewerkt". En sluit af met wat je van dit gremium nodig hebt: een besluit, een review, of alleen kennisname.

## Gebruik de termen uit de bron, niet je eigen omschrijving

Systemen en begrippen hebben in OKx vaste namen. Verzin er geen vriendelijker klinkende variant bij: het publiek kent de echte term, en een eigen woord leest als een fout of als een nieuw begrip.

De afkortingenlijst staat in de instap van [`Koppelvlakspecificaties/README.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/README.md) in Npuls-OKx/Public. De kern:

| Goed | Fout |
|---|---|
| Onderwijscatalogus (OC) | "de catalogus van het onderwijs" |
| Planningssysteem en roostersysteem (P&R) | "planningstool" |
| Leermanagementsysteem (LMS) | "leeromgeving" als het systeem bedoeld is |
| Studentinformatiesysteem (SIS), dat is KRS plus SVS | "studentadministratie" |
| Studentkeuzesysteem (SKS) | "keuzetool" |

Twijfel je of een term bestaat: zoek hem op in de bron. Staat hij er niet, dan verzin je hem.

## Show, don't tell: kies zelf een passende plaat

Elke inhoudelijke uitleg krijgt beeld. Dat is geen extraatje waar iemand om moet vragen: **je zoekt zelf een passende plaat en stelt die voor**. OKx heeft architectuurplaten die het verhaal beter vertellen dan een opsomming, en ze zijn al besproken en goedgekeurd — een zelfgetekend diagram opent een discussie die je niet wilde voeren.

Het overzicht staat in [`presentaties/platen.json`](../../../presentaties/platen.json). Lees dat bestand voordat je slides schrijft. Per plaat staat er wat hij toont, bij welk publiek hij werkt, en waar je op moet letten. Onderaan staan de mermaid-diagrammen die als tekst in de specificaties leven; die plak je rechtstreeks in een slide, want Slidev rendert ze.

Controleer het manifest eerst tegen de werkelijkheid:

```bash
python3 scripts/platen-inventariseren.py
```

Dat meldt bronnen die zijn gewijzigd, versies die zijn ingehaald, en platen die nog nergens beschreven staan. Krijg je meldingen, los die dan op vóór je een plaat kiest; anders zet je een verouderd beeld in een deck.

Werkwijze per onderwerp:

1. Kies een plaat op `gebruik_bij`, niet op wat er toevallig mooi uitziet.
2. Kopieer hem naar `presentaties/public/platen/` en verwijs ernaar met `/platen/<naam>`.
3. Zet er een regel bij die zegt **waar de kijker naar moet kijken**. Een plaat zonder leeswijzer is decoratie.
4. Neem `let_op` over in je afstemming met de aanvrager als daar iets in staat.

Geef een brede plaat de hele slidebreedte:

```html
<img src="/platen/lr1-informatiestromen.jpg" style="width: 100%; max-height: 330px; object-fit: contain;" />
```

**Spar over je keuze.** Bij het voorleggen van de onderwerpen noem je per onderwerp welke plaat je erbij wilt zetten, en waarom die. Degene die het deck vraagt kent het publiek en weet welke plaat er vorige keer vragen opriep. Staat er niets passends in het manifest, zeg dat dan — dan is dat een signaal dat er een plaat ontbreekt, niet een reden om er zelf een te tekenen.

**Houd het manifest actueel.** Komt er een nieuwe versie van een plaat, of teken je er een die vaker bruikbaar is, neem hem dan op in `platen.json` en werk de hashes bij met `--bijwerken`. Dat is onderdeel van het werk, niet iets voor later: een manifest dat achterloopt op de repositories is erger dan geen manifest, want dan wordt met vertrouwen een verouderde plaat gekozen.

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
