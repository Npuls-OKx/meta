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
| `Npuls-OKx/meta` | `/workspaces/OKx/OKx-meta` | Kaderstelling, ArchiMate-model, meeting-notulen, de leerroute-uitwerking |
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

## Schrijf over de zaak, niet tegen de zaal

Een deck informeert over een onderwerp. Het onderwerp is dus het grammaticale onderwerp, niet het publiek. Dat is dezelfde norm als bij een thesis of een adviesrapport: zakelijk, navolgbaar, zonder de lezer aan te spreken.

**Geen tweede persoon.** Geen "u", "je" of "jullie", ook niet in een kop of een bijschrift. Waar de neiging opkomt het publiek aan te spreken, staat bijna altijd een sterkere formulering klaar met het onderwerp voorop.

| Niet | Wel |
|---|---|
| "Waar we jullie voor nodig hebben" | "Besluit nodig op" |
| "Kennen jullie een keuzeregel die niet past?" | "Gezocht: keuzeregels die de huidige vorm niet kan uitdrukken" |
| "Als je iets doorstuurt naar een instelling..." | "Wat naar een instelling gaat, komt uit het publieke repository" |
| "Dat is jullie werk" | "Die vertaalslag ligt bij de onderwijskundige" |

**Eerste persoon spaarzaam.** "We" mag waar het programma echt de handelende partij is ("OKx heeft drie koppelingen beschreven"), maar niet als vulling. "Ik maak me zorgen over de review" wordt "Risico: de reviewcapaciteit in augustus". Een inschatting blijft herkenbaar als inschatting doordat er *risico*, *aanname* of *inschatting* bij staat, niet doordat er "ik" voor staat.

**Meta-taal blijft buiten de slide.** Een aanwijzing van de opdrachtgever over de vorm — "houd het kort", "stip het even aan", "niet te diep" — is een instructie voor de maker, geen slidetekst. Een titel als "De aanleiding, kort" vertelt de zaal hoe het deck gemaakt is in plaats van wat er staat; als de slide kort is, laat dat zichzelf zien. Dus geen "kort", "even", "samengevat" of "in vogelvlucht" in titels of zichtbare tekst; zulke aanwijzingen landen in de sprekersnotitie.

**De opdracht is regie, geen slidetekst.** Wat de opdrachtgever zegt over een slide — het doel, de verwachting, een ad-hoc aanwijzing — is een briefing aan de maker, nooit de tekst van de slide. "Het idee is dat ze meteen zien wat Garik en Niek komen brengen" wordt dus géén titel "Doel: wat Garik en Niek komen brengen in één overzicht"; het wordt een slide die dat idee wáármaakt — een opening die zegt wat er bereikt is. Vertaal elke aanwijzing in twee stappen: eerst, wat is de essentie die het publiek moet meekrijgen? Dan: hoe verwoord je die zoals je hem zelf zou willen lezen als je in de zaal zat — gewaardeerde collega's, geen ontvangers van een werkbon. Wie de briefing letterlijk terugleest in de slide heeft de opdracht niet uitgevoerd maar genotuleerd.

**Besluiten krijgen een vaste vorm.** Een vraag om een besluit is geen alinea maar een blok met vier velden, zodat na afloop vaststaat wat er gevraagd is:

> **Besluit nodig op:** publicatiemoment koppelvlakspecificatie leerroute 1
> **Door:** programmaleiding, in afstemming met kerngroep techniek OKx
> **Voor:** 31 augustus 2026
> **Opties:** publiceren na de kerngroep techniek (september) — of eerder publiceren en wijzigingen accepteren

Zelfde vorm voor een reviewverzoek (*Review gevraagd op / Door / Voor*) en voor kennisname (*Ter kennisname*). Zet nooit een besluit weg als een terloopse zin.

## Slides zijn schaars: de anti-bloatregels

Uit de deckreview van 18 augustus 2026; elke regel is daar in de praktijk misgegaan.

- **Elke zichtbare zin heeft een bron of sneuvelt.** Subtekst die niets toevoegt is bloat; liever leegte dan vulling. Toets elke zin: waar staat dit in de repositories?
- **Geen subtitel onder de slidetitel.** De ruimte gaat naar de plaat of het schema; wat de subtitel wilde zeggen gaat in de titel, de tekst of de sprekersnotitie.
- **Titels plat en concreet.** Geen bedachte constructies ("Elk hoofdstuk in één voorbeeld"); benoem wat de slide toont ("Voorbeeld", "Van bron naar releasepakket").
- **Echte beelden boven nagebouwde.** Een bestaande plaat of een screenshot verslaat een ASCII-boom of een gegenereerd diagram.
- **Bullets eerst, plaat groot.** Vaste leesvolgorde: tekstpunten aan de ene kant, de plaat zo groot mogelijk aan de andere.
- **Geen beloften met een datum.** "Tonen we de volgende sessie" bindt het team vast; planning is aan de spreker.
- **Eén onderwerp per slide.** Inhoud en vraagstelling zijn twee slides, nooit één.
- **Niet alles hoeft getekend.** Wat de spreker kan zeggen, hoort in de sprekersnotitie; losse pijltjes en tekstelementen naast een diagram zijn een gebrek, geen oplossing.

## Compositie en didactiek

Uit de finetunerondes van 18 augustus 2026, vastgesteld door de product owner.

- **Eén doorlopende voorbeeldlijn.** Kies één casus en laat die door het hele deck lopen (opbouw, voorbeeld, vooruitblik); herkenning stapelt, losse voorbeelden per slide niet.
- **Opdrachten bij de stof, geen apart werkdeel.** Een interactieve opdracht hangt aan de content-slide zelf, met QR-code en link ter plekke.
- **Verken, herken, vind.** Bij kennismaking met nieuw materiaal drie opdrachten in deze volgorde: vrij kijken (wat valt op), iets bekends terugvinden (draagt de continuïteitsboodschap) en benoemen wat niet vindbaar is (voedt de issues). De ophaal-slide erna stelt dezelfde vragen terug.
- **Een vraag aan de zaal krijgt een eigen opvallende kaart**, met vraagicoon en de doelgroepnaam erin.
- **Blokreeksen wisselen accentkleuren af**; nooit twee dezelfde naast elkaar. Elk blok draagt één ondertitel, zonder aankondigwoorden als "bijvoorbeeld".
- **Diagrammen volledig of niet.** Een sequentiediagram toont ook de terugweg, het eigen proces en het foutpad; JSON-voorbeelden gebruiken echte veldnamen en types uit het schema, met een beletselteken voor de rest.
- **Backlog en planning worden afgeleid, niet verzonnen.** Toon de afleidingslijn (leerroutes en scenario's naar features, stories en functionele eisen) en stel de toetsvraag aan de zaal in plaats van zelf een lijst te bedenken.

## Voor wie schrijf je

Het publiek bepaalt het abstractieniveau én het register, niet de inhoud die toevallig voorhanden is. Vraag de gebruiker voor welk gremium het deck is. Bij meerdere gremia: maak aparte decks, geen compromis.

Het onderscheid dat het register bepaalt is **intern of extern**:

- **Intern** — SI-team, adviesgroep, programma- en projectleiding. Relatief informeel *binnen zakelijke normen*: korte zinnen, gewone woorden, geen plechtige formuleringen. Wel nog steeds over de zaak, zonder aanspreekvorm.
- **Extern** — kerngroep techniek OKx, technische werkgroep OEAPI, leveranciers, instellingen. Formeler en preciezer. Volledige termen, expliciete status bij elke uitspraak (vastgesteld, concept, voorstel), en geen luchtige formuleringen. Deze gremia nemen het materiaal mee naar hun eigen organisatie; wat daar overkomt als losse opmerking, gaat een eigen leven leiden.

| Gremium | | Weet al | Wil weten | Diepgang |
|---|---|---|---|---|
| **SI-team** | intern | De hele context, het jargon, de historie | Wat is af, wat loopt vast, waar een besluit nodig is | Kort en direct. Openstaande punten en blokkades voorop. Details mogen |
| **Adviesgroep** | intern | Onderwijskundig sterk, wisselend technisch. IM'ers brengen instellingscontext mee | Wat dit betekent voor het onderwijs en voor de instelling | Elke stap toelichten, beginnen bij de leerroute en niet bij de payload. Meer uitleg dan bij de leiding, zelfde register |
| **Programma- en projectleiding** | intern | Programmadoelen en planning; **geen** inhoudelijke experts | Of het op schema loopt, welke risico's er zijn, welk besluit gevraagd wordt | Geen payloads, geen ADR-nummers. Maximaal tien slides. Risico's en besluitpunten naar voren |
| **Kerngroep techniek OKx** | extern | De keten en de architectuur | Of de richting klopt, en of de kaderstelling ver genoeg is om spec te starten | Diep. Besluiten, alternatieven en open punten. Ankertabel en payloads horen erbij |
| **Technische werkgroep OEAPI** | extern | De OEAPI-standaard | Hoe OKx zich tot OEAPI verhoudt, en welke signaleringen eruit komen | Vergelijkend. Benoem afwijkingen met de onderbouwing, en welke wijzigingsverzoeken richting OEAPI gaan |
| **Leveranciers** | extern | Het eigen systeem en de integratiepraktijk | Wat er gebouwd moet worden, wanneer, en wat er nog verandert | Concreet over koppelvlakken en contracten. Expliciet over wat vaststaat en wat concept is |
| **Instellingen** *(komt nog)* | extern | De eigen onderwijspraktijk | Wat er verandert en wanneer | Nog niet uitgewerkt; stem af met de gebruiker |

Twee regels die voor elk profiel gelden. Vertaal een wijziging altijd naar **wat er nu mogelijk is dat eerst niet kon** — niet naar "document X is bijgewerkt". En sluit af met wat er van dit gremium gevraagd wordt, in de vaste vorm hierboven: een besluit, een review, of kennisname.

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

**Voorbehouden horen in platen.json.** Ondergrond-eisen (transparant of donker getekend), terminologie-afwijkingen in de plaat en de bronstatus staan in het manifest bij de plaat, zodat het volgende deck ze kent zonder de fout te herhalen.

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

**Versienummers letterlijk uit het releasemanifest.** Het manifest zegt v0.0.1; schrijf dan nooit v0.01 of een eigen notatie.

## Onderscheid feit en inschatting

Wat uit de repositories komt is feit: aantallen open punten, deadlines, wat er gemerged is. Wat jij ervan vindt is een inschatting: of een deadline haalbaar is, waar het knelt, wat het grootste risico is.

Beide mogen in een deck, maar niet door elkaar. Formuleer een inschatting als inschatting, en meld de aanvrager welke uitspraken van jou zijn, zodat die ze kan overrulen voordat hij ze als projectstandpunt presenteert.

## Opbouw van een update-deck

**Kernpunt eerst.** Het publiek hoort binnen de eerste minuut wat de sprekers komen brengen: wat er bereikt is, in één concrete zin ("de eerste structuur voor het eindproduct: de koppelvlakspecificatie"). Die essentie staat vóór het programma — als eigen openingsslide of als de subtitel van de titelslide. Een subtitel die niet de essentie draagt, vervalt; sfeerzinnen zijn vulling. Pas daarna volgen agenda en uitwerking.

Een werkbare basisvorm; wijk af waar de inhoud daarom vraagt.

1. **Titel** — periode en gremium, met de essentie als subtitel of direct erna als openingsslide
2. **Waar we stonden** — één slide, zodat het deck zelfstandig te lezen is
3. **Wat er is gebeurd** — per thema, niet per repository of per pull request. Het publiek denkt in onderwerpen
4. **Wat dat betekent** — de consequentie voor dit gremium
5. **Openstaande punten en risico's** — eerlijk over wat vastloopt
6. **Wat we vragen** — besluit, review of kennisname
7. **Afsluitslide**

Voor programmamanagement schuiven 5 en 6 naar voren; voor de kerngroep techniek is 3 en 4 het zwaartepunt.

## Voor je oplevert: kijk er zelf naar

**Na elke geautomatiseerde tekstveeg een bouwcontrole.** Een script dat leestekens of woorden vervangt kan de YAML-frontmatter breken; de dev-server toont dan stil de laatste goede versie en de wijzigingen lijken te verdwijnen. Parse na een veegronde minimaal de frontmatter of herbouw het deck.

**Vraag eerst of het release-klaar is.** Finetunen en opleveren zijn twee fasen. Exporteer, deel of publiceer een visueel product (deck, plaat, PDF, deellink) pas nadat de opdrachtgever expliciet heeft gezegd dat het release-klaar is; tot dat moment is elke versie werkmateriaal.

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
