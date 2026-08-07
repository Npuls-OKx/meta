# Gereedschap: requirements, architectuur en documentatie als code

Relateert aan: #130

Aanleiding: we willen de businesslaag machine-interpreteerbaar en onderhoudbaar maken zonder de markdown-bron op te geven. Dit verslag toetst de beschikbare gereedschappen aan onze randvoorwaarden: Nederlandstalig, renderbaar op GitHub, exporteerbaar naar PDF, en werkbaar voor architecten en onderwijskundigen die geen softwareontwikkelaar zijn.

## Kalibratie: wat we nu hebben

- **66 markdown-bestanden, ongeveer 8.100 regels** in `Npuls-OKx/Public`. Dat is klein. Elke aanbeveling die een build-pipeline vereist moet zich tegen die omvang verantwoorden.
- **Er draait niets in CI.** `Public/.github/` bevat alleen issue-templates en een PR-template. De drie controlescripts draaien handmatig. Een pull request die de conventies breekt komt er vandaag gewoon door. Dit is het grootste en goedkoopste gat.
- **Zeven eigen scripts in twee repositories**, alle met exitcode 1. Dit is een volwassen eigen linter-suite, geen prototype.
- **Interacties dragen al ID's** (`I1` tot en met `I5` in de koppelingspecificatie met planning, `X1`/`X2` in het template). Dat is een handgeschreven traceerbaarheidsschema dat nergens machinaal wordt gecontroleerd.
- **Het ArchiMate-model is één bestand van 40.478 regels.** ADR 0010 documenteert dat bij een handmatige merge in juli 2026 **276 elementdefinities wegvielen en 295 dode verwijzingen ontstonden, verspreid over 9 views**. Dat is het scherpste aantoonbare probleem in het hele landschap.

## 1. Requirements als code

### OpenFastTrace

Trekt requirement-definities en dekkingstags uit gewone brontekst en berekent een dekkingsmatrix over de keten. Het is een tracer, geen documentatiesysteem: het schrijft niets, het rekent na.

Markdown is een eersterangs invoerformaat, geverifieerd in de [user guide](https://github.com/itsallcode/openfasttrace/blob/main/doc/user_guide.md): een eis is een kop met daaronder `` `req~naam~1` `` en een regel `Covers:`. Dekkingstags elders staan in een **HTML-comment**, die onzichtbaar is op GitHub én door pandoc wordt weggelaten — hier precies gewenst. Ook JSON, YAML, PlantUML en Gherkin worden als tag-bron gelezen.

- **Adoptiedrempel**: laag om te lezen, middel om te schrijven. Een architect leert twee dingen: één ID-regel onder een kop, en één `Covers:`-regel.
- **GitHub-render en PDF**: ja, volledig. De rapporten zijn `plain`, `html` of XML — geen markdown, dus het traceerrapport wordt een CI-artefact, geen document in de repo.
- **Wie gebruikt het**: [itsallcode/openfasttrace](https://github.com/itsallcode/openfasttrace) traceert zichzelf. **157 sterren, GPL-3.0, Java 17.** Dat is een reële bus-factor-waarschuwing.
- **Oordeel**: passend, en het enige gereedschap in dit onderzoek dat zonder compromis op onze bestaande markdown past. De `I1`–`I5`-nummering die er al is, is een handgeschreven versie van wat dit automatiseert. Valt het project stil, dan zijn de tags triviaal zelf na te rekenen — het is regex.

### Sphinx-Needs

Requirements, specificaties en testgevallen als "needs" in de documentatie, met traceermatrices en `needflow`-diagrammen, plus export naar `needs.json`.

- **Bronformaat**: primair reStructuredText; via MyST-Parser in markdown. **Onzeker**: geen pagina gevonden waarin Sphinx-Needs MyST expliciet ondersteunt of test — het volgt uit MyST's algemene directive-ondersteuning.
- **Adoptiedrempel**: hoog. Ook in MyST schrijf je directives met opties, en zonder lokale Sphinx-build zie je het resultaat niet. De bron toont op GitHub ruwe directive-blokken.
- **Wie gebruikt het**: [Eclipse S-CORE](https://eclipse.dev/score/docs.html) (automotive, ASPICE/ISO 26262) noemt het de "digital thread" van eis tot testresultaat. Dat is de zwaarste referentie in dit onderzoek.
- **Oordeel**: niet passend. Gebouwd voor genormeerde veiligheidsdomeinen waar een documentatie-build vanzelfsprekend is. Voor een repo waarvan het contract is "de markdown op GitHub *is* het document" draait het de bronwaarheid om.

### StrictDoc

Zelfstandig requirements-managementsysteem met eigen tekstgrammatica (`.sdoc`), webinterface en export naar HTML, PDF, RST, **ReqIF**, Excel en JSON.

Letterlijk uit de [user guide](https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide.html): *"StrictDoc supports two input document formats: SDoc (\*.sdoc) and Markdown (\*.md, ... experimental)"*. Markdown is dus expliciet experimenteel.

- **Oordeel**: niet passend nu, wél het beste vangnet. De ReqIF-export is de reden om het te onthouden: moeten we ooit eisen aanleveren aan een partij met DOORS of Polarion, dan is dit de brug. Bouwen op een experimentele markdown-frontend is te riskant.

### Doorstop, ReqIF en OSLC

- **[Doorstop](https://doorstop.readthedocs.io/en/latest/)**: elke eis als los YAML-bestand in een mappenboom. Splitst de eis van het document en botst frontaal met "één bestand, één doel" en met de regel dat een gereleased document zelfdragend is. **Niet passend.**
- **[ReqIF](https://www.omg.org/spec/ReqIF/1.2/About-ReqIF/)** (OMG, v1.2 juli 2016): uitwisselformaat, geen auteursformaat. Niemand schrijft het met de hand. **Niet passend als bron, wel als exit-optie.**
- **[OSLC](https://open-services.net/)** (OASIS, RM v2.1 juni 2021): tool-integratie via REST en RDF. Vereist een draaiende server. **Niet passend** — we hebben geen ALM-keten om te integreren.

### Twee lichte aanvullingen die beter passen

**EARS** (Easy Approach to Requirements Syntax) is geen gereedschap maar een schrijfpatroon met vaste vormen. Ontwikkeld bij Rolls-Royce, gepubliceerd op RE'09 — [alistairmavin.com/ears](https://alistairmavin.com/ears/). Kost nul infrastructuur, maakt eisen regex-herkenbaar, en werkt in het Nederlands. Er is al een `requirements-engineering`-skill voor.

**Gherkin met Nederlandse sleutelwoorden.** Geverifieerd in [`gherkin-languages.json`](https://raw.githubusercontent.com/cucumber/gherkin/main/gherkin-languages.json), taalcode `nl`: `Functionaliteit`, `Achtergrond`, `Scenario`, `Abstract Scenario`, `Gegeven` / `Als` / `Wanneer` / `Dan`, `En` / `Maar`, `Voorbeelden`. Dit past precies op onze §5.1 happy flow en §5.2 faalpaden, en OpenFastTrace leest `.feature` als dekkingsbron. Voor onderwijskundigen is `Gegeven/Als/Dan` in het Nederlands aantoonbaar toegankelijker dan een eigen grammatica.

## 2. Architectuur als code

### Structurizr DSL

Tekstuele DSL waaruit meerdere consistente C4-views worden afgeleid. **Let op: de toolchain is per februari 2026 verbouwd** — [`structurizr/cli` is gearchiveerd op 4 februari 2026](https://github.com/structurizr/cli) met *"please migrate to the new consolidated tooling"*; Structurizr Lite staat op [End of life](https://docs.structurizr.com/lite), opvolger is [`structurizr local`](https://docs.structurizr.com/local).

Mermaid-export bestaat, met twee waarschuwingen. De [exportpagina](https://docs.structurizr.com/export/mermaid) zegt: *"Your Mermaid configuration will need to include `"securityLevel": "loose"` to render the diagrams correctly."* GitHub laat die configuratie **niet** zetten. En: *"export formats do not support all available shapes/features."* Testen vóór erop bouwen.

- **Oordeel**: deels. Sterk als je views uit één model wilt afleiden, maar we hebben al ArchiMate voor het model en mermaid voor de documenten. Een derde modelbron botst met "less is more" — tenzij we ArchiMate opgeven, en dat kan niet (zie hieronder).

### LikeC4

Moderne variant met live preview in VS Code — de laagste drempel van de architectuurtools. Export: `png|jpg|json|drawio` en `gen mmd|dot|d2|plantuml`; **geen SVG** ([open request](https://github.com/likec4/likec4/discussions/1804)). MIT, ~5.3k sterren, zeer actief. **Oordeel**: deels; technisch het prettigst, zelfde bezwaar van een extra modelbron.

### C4-PlantUML

Diagram-as-code, niet model-as-code: er is geen onderliggend model. Laatste release v2.13.0, januari 2025. **Oordeel**: niet passend — we winnen niets boven de mermaid die er al staat, en verliezen diffbaarheid in het document zelf.

### ArchiMate Open Exchange Format

[Open Group-standaard](https://www.opengroup.org/open-group-archimate-model-exchange-file-format) voor modeluitwisseling; ondersteuning verplicht voor gecertificeerde tools sinds juni 2018.

**Dit is voor ons geen theoretische kwestie.** De [ROSA Handreiking voor domeinarchitectuur](https://rosa.wikixl.nl/index.php/Handreiking_voor_domeinarchitectuur) zegt letterlijk: *"Maak de architectuurmodellen en/of views die ondersteunend zijn aan het te scannen object in ArchiMate en zorg dat deze in lijn zijn met het ROSA metamodel. **Aanleveren in The Open Group ArchiMate Model Exchange File Format.**"* Bij een ROSA-scan is dit een harde eis.

- **Oordeel**: passend, maar als export en niet als bron. Voeg een export toe aan het releaseproces van het model.

### Archi met coArchi — de scherpste afweging in dit onderzoek

coArchi deelt een Archi-model in git in het **GRAFICO**-formaat. Letterlijk van de [coArchi-wiki](https://github.com/archimatetool/archi-modelrepository-plugin/wiki/Understand-the-Basics): *"Each file contains the description of a single object (element, relationship or view)."*

**Dat is de remedie voor ADR 0010.** Eén XML-bestand per element in plaats van 40.478 regels in één bestand. De 276 weggevallen elementen waren dan 276 zichtbare bestandsverwijderingen in een diff geweest.

**Maar dezelfde pagina zegt**: *"**Important: you shouldn't use merge, pull requests or similar features from your Git server as this would most certainly lead to model corruption.**"* Dat is onverenigbaar met onze hele werkwijze, die op feature branch → pull request → review → merge staat (ADR 0001).

Het Nederlandse peer-voorbeeld dat dit oplost: [MinBZK/gdi-gegevensuitwisseling](https://github.com/MinBZK/gdi-gegevensuitwisseling), de GDI-domeinarchitectuur van BZK. Het model is *"beschikbaar in verschillende vormen: als ArchiMate bestand in het ArchiMate uitwisselformaat, als Archi bestand, als Archi HTML report"*, plus een PDF per release en een gepubliceerde site. Ook **ROSA zelf** doet dit: [edustandaard/rosa](https://github.com/edustandaard/rosa) staat in coArchi-formaat, met `CODINGGUIDELINES.md` die per elementtype de verplichte properties voorschrijft.

- **Oordeel**: passend, maar dwing de keuze af in een ADR en middel hem niet weg. Tussenvorm: model in coArchi in de private repo, per release een uitwisselformaat-export plus views naar de publieke repo, waar de pull request-workflow wél geldt.

### Mermaid C4

Bestaat officieel maar de [documentatie](https://mermaid.js.org/syntax/c4.html) zegt: *"This is an experimental diagram for now. The syntax and properties can change in future releases."* Het zit in de core-bundel en wordt gemoderniseerd ([issue #7849](https://github.com/mermaid-js/mermaid/issues/7849)). **Niet empirisch getest of GitHub het rendert.** **Oordeel**: deels — "experimenteel, syntaxis kan wijzigen" is een slecht fundament onder een gereleased document.

### De pandoc-kink die al ons architectuuradvies bepaalt

**Wat op GitHub rendert, rendert niet automatisch in een pandoc-PDF.**

| Vorm | GitHub | pandoc naar PDF |
|---|---|---|
| ```` ```mermaid ```` blok | ja, native | **nee** — komt als letterlijk codeblok; vereist [mermaid-filter](https://github.com/raghur/mermaid-filter), die een headless browser meetrekt |
| ingecheckte SVG | ja | alleen met `rsvg-convert` op het PATH |
| **ingecheckte PNG** | **ja** | **ja, zonder extra afhankelijkheid** |

PNG is de enige gemeenschappelijke deler. Als de PDF-eis serieus is — en U8 gebruikt hem juist om `<details>` af te wijzen — dan hebben we nu al een gat: alle bestaande mermaid-diagrammen vallen zonder filter uit de PDF. Dat is een concreet, verifieerbaar probleem dat losstaat van elke toolkeuze.

## 3. Documentatie als code voor standaarden

### NL-ReSpec — de Nederlandse fork verandert het oordeel volledig

De W3C-versie van ReSpec is voor ons ongeschikt: je redigeert HTML, en dat rendert niet op GitHub. **Maar Logius onderhoudt een [eigen fork](https://github.com/Logius-standaarden/respec) die Geonovum ook gebruikt.** Het patroon, geverifieerd in het [NL-ReSpec-template](https://github.com/Geonovum/NL-ReSpec-template):

- hoofdstukken staan in **losse markdown-bestanden**, ingeladen via `<section data-include-format="markdown" data-include="ch01.md">`;
- er is een `mermaid.md` in het template — **mermaid werkt in fenced blokken binnen die markdown-hoofdstukken**;
- instellingen in `js/config.js`, huisstijl en boilerplate centraal;
- **PDF wordt automatisch gegenereerd** in GitHub Actions via `alternateFormats`.

De markdown-bestanden blijven dus renderen op GitHub, en er komt een gepubliceerde HTML plus PDF bovenop.

Gebruikt door Logius ([Digikoppeling REST-API](https://github.com/Logius-standaarden/Digikoppeling-Koppelvlakstandaard-REST-API), [API Design Rules](https://github.com/Logius-standaarden/API-Design-Rules)) en Geonovum, met **BOMOS** als beheermodel.

- **Adoptiedrempel**: voor een bijdrager nul — hij redigeert een `.md` zoals nu. Voor de redacteur: één `index.html` en één `config.js` per releasepakket.
- **Oordeel**: passend, en de sterkste kandidaat voor een publicatielaag. We sluiten aan bij de de-facto stack van de Nederlandse (semi-)overheid en houden markdown als bron.

### De overige vier

- **[Bikeshed](https://speced.github.io/bikeshed/)** (WHATWG, CSSWG): functioneel het rijkst voor spec-schrijven, maar GitHub rendert `.bs` niet en er is **geen PDF**. Beide zijn harde randvoorwaarden. **Niet passend.**
- **Spec-Up / Spec-Up-T** (DIF, Trust over IP): markdown met `[[def:]]`/`[[ref:]]` en **één bestand per begrip** ([ToIP-glossary](https://github.com/trustoverip/ctwg-main-glossary/tree/main/spec/terms-definitions)). Dat patroon is exact wat onze ankertabel nodig heeft om "geen verzonnen termen" (U6) machinaal af te dwingen. Maar PDF is niet gedocumenteerd. **Het idee is bruikbaar, het gereedschap niet.**
- **[Antora](https://docs.antora.org/)**: vereist migratie naar AsciiDoc en levert geen enkele specificatie-functie terug. Alle bekende gebruikers zijn productdocumentatie, geen standaardisatieorganisaties. **Niet passend.**
- **Sphinx**: de enige met een ingebouwde PDF-builder, maar directives blijven ruwe tekst op GitHub. **Niet passend als hoofdstack, wel de enige route naar Sphinx-Needs.**
- **MkDocs Material**: laagste drempel, pure markdown; PDF alleen via third-party plugins. VNG Realisatie gebruikt het voor Common Ground-architectuurpatronen. Maar **geen enkele standaardisatieorganisatie publiceert er normatieve specificaties mee** — dat negatieve resultaat is een signaal. **Deels**; als je toch een publicatielaag toevoegt geeft NL-ReSpec voor dezelfde moeite meer terug.

### Het Nederlandse veld, ter kalibratie

| Organisatie | Bron | Publicatie | PDF |
|---|---|---|---|
| **Logius / KOOP** | markdown-secties plus `index.html` | ReSpec-fork naar gitdocumentatie.logius.nl | ja |
| **Geonovum** | idem | zelfde fork naar docs.geostandaarden.nl | ja, via Actions |
| **VNG Realisatie** | markdown | MkDocs Material met mermaid | onbekend |
| **MinBZK (GDI)** | ArchiMate met coArchi | HTML-report en eigen site | ja, per release |
| **Kennisnet / Edustandaard** | CMS-pagina's en MediaWiki | edustandaard.nl | PDF/Word |
| **SURF (OOAPI)** | OpenAPI YAML/JSON | Zudoku naar oeapi.eu | nee |

Twee dingen springen eruit. Er is een **de-facto gedeelde stack in het Nederlandse publieke domein**. En **Edustandaard staat daar juist buiten** met CMS, wiki en PDF. Wij zitten met markdown-op-GitHub dichter bij Logius dan bij onze eigen sectorpeer.

## 4. Governance-linting

### Vale — de hoogste opbrengst per geïnvesteerde dag

Brengt code-achtige linting naar proza. Eén Go-binary, geen runtime. Regels zijn YAML met extension points: `existence`, `substitution`, `occurrence`, `conditional`, `capitalization`, `spelling`, `sequence`.

**Meerdere regels uit onze eigen `docs-style.mdc` zijn letterlijk `existence`-regels met een regex**: het verbod op vulwoorden, het verbod op statusaanduidingen in koppen (U10), afkortingen voluit bij eerste gebruik. Bovendien lint Vale **frontmatter native** ([docs](https://docs.vale.sh/formats/front-matter)), met scoping op `heading`, `paragraph`, `table.cell` en meer; codeblokken worden genegeerd.

**Er bestaat geen Nederlandstalig Vale-pakket** — de [Package Explorer](https://vale.sh/explorer) bevat alleen Engelse stijlen. Maar de regex-checks zijn taal-agnostisch. Alleen `sequence` (POS-tagging) en de leesbaarheidsformules zijn op Engels geijkt. Spelling via Hunspell met eigen woordenboek; of een OpenTaal-set out of the box werkt is **niet geverifieerd**.

Gebruikt door [GitLab](https://docs.gitlab.com/development/documentation/testing/vale/) met error-level regels in de pipeline, Linode, Datadog, Elastic en Grafana.

- **Oordeel**: passend. Het haalt de schrijfstijlregels uit `.cursor/rules/` — waar ze alleen werken als iemand met een agent schrijft — en maakt ze voor iedereen afdwingbaar. Reken op een dag voor een bruikbare eerste set.

### markdownlint-cli2, lychee en check-jsonschema

- **[markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2)**: 60+ regels, veel auto-fixbaar, eigen regels in JavaScript met toegang tot de AST. Daar landen structurele regels het goedkoopst ("elk koppelingspecificatie-document heeft §1 tot en met §10 in deze volgorde"). Nul conceptuele kosten. **Passend, direct.**
- **[lychee](https://github.com/lycheeverse/lychee)**: aanvullend, niet vervangend. `check-links.py` doet iets wat lychee **niet** kan — het lost paden lexicaal op zoals GitHub, en vangt links die met genoeg `../` buiten de repository wijzen of door een symlink lopen. Voeg lychee toe voor **externe** links.
- **[check-jsonschema](https://check-jsonschema.readthedocs.io/en/latest/usage.html)**: `--check-metaschema` valideert de schema's zélf; `$ref`-resolutie lokaal en remote; JSON en YAML. Belangrijk onderscheid: een `$ref` die niet resolvet is een harde fout in elke tool, maar een `$ref` die wél resolvet en naar het verkeerde wijst wordt alleen gevangen door instantie-validatie tegen echte voorbeelddata — precies wat `json-tree.py` al doet. Wat ontbreekt is de metaschema-check. **Passend, één regel in CI.**
- **[Spectral](https://github.com/stoplightio/spectral)**: werkt op willekeurige YAML/JSON, **niet op markdown** (de CLI laadt alleen YAML of JSON). **SURF gebruikt het al voor OOAPI** — als wij binden op "OEAPI, tenzij" is dezelfde linter een goedkope brug.
- **Frontmatter tegen een JSON Schema**: [`remark-lint-frontmatter-validation`](https://github.com/Nick2bad4u/remark-lint-frontmatter-validation) heeft een standalone CLI en `--format github` voor PR-annotaties. Voor markdown-*tabellen* tegen een schema bestaat **geen kant-en-klare tool** — wel de bouwstenen (remark met `remark-gfm`, of een markdownlint custom rule), orde vijftig regels code.

## 5. Hoe ver kom je met platte markdown?

**Wie dit succesvol doet:**

- **De OpenAPI Specification.** Elke versie is een gewoon `.md`-bestand: [`versions/3.1.1.md`](https://github.com/OAI/OpenAPI-Specification/tree/main/versions). Geen build, geen generator, geen DSL. Waarschijnlijk de meest gebruikte technische specificatie ter wereld.
- **De JSON Schema-specificatie.** Bron is markdown in [`specs/`](https://github.com/json-schema-org/json-schema-spec); de build gebruikt Remark-plugins voor sectienummering en inhoudsopgave. Exact de middenweg: bron blijft markdown, de build voegt alleen conventies toe.
- **CommonMark.** De spec is markdown; `tools/makespec.py` genereert HTML, en dezelfde voorbeelden worden als [JSON-testsuite geëxtraheerd](https://github.com/commonmark/commonmark-spec). **De voorbeelden in het document *zijn* de testsuite** — dat is "show don't tell" in zuiverste vorm, en het is waar `json-tree.py` al naartoe werkt.
- **[MADR 4.0.0](https://adr.github.io/madr/)**: platte markdown met optionele YAML-frontmatter (`status`, `date`, `decision-makers`). Direct relevant voor onze 24 ADR's, die nu `Status:` en `Datum:` als losse tekstregels dragen.
- **IETF**: Internet-Drafts in markdown via [kramdown-rfc](https://github.com/cabo/kramdown-rfc); de officiële [Author Tools](https://author-tools.ietf.org/) accepteren `.md`.

**Waar het stuk loopt** — minder snel dan de vakliteratuur suggereert, en om andere redenen:

- **Onderhoudslast van eigen gereedschap.** De kritiek is reëel: [docs-as-code vereist "a decent amount of custom tooling"](https://passo.uno/docs-as-code-tools-open-standards/). Wij hebben er nu zeven. Nog beheersbaar, maar de curve is duidelijk.
- **Bus-factor, niet regels code.** `check-links.py` bevat een eigen implementatie van GitHub's anchor-algoritme, inclusief de subtiliteit dat een em-streep een dubbele koppelstreep oplevert. Goede code — en kennis die in één hoofd zit.
- **Waar eigen scripts principieel tekortschieten: cross-document identiteit.** Een script kan controleren dat een link bestaat; niet dat de eis achter die link nog dezelfde eis is. Zodra je wilt weten "welke koppelingspecificaties raakt een wijziging aan U4", heb je een ID-model nodig.
- **Waar we nu al tegenaan lopen** is niet de markdown maar het ArchiMate-model: 276 verloren elementen. `validate-archimate.py` detecteert dat achteraf; het onderliggende probleem is met geen enkel script op te lossen.

**Oordeel: de lichtgewicht aanpak is voor onze markdown de juiste keuze, en er is geen aanwijzing dat hij op korte termijn stukloopt.** Twee zwakke plekken: de scripts draaien niet in CI, en het architectuurmodel valt buiten de aanpak.

## 6. Drie varianten

### Minimaal — wat we hebben, aangescherpt

Geen nieuw bronformaat, geen leercurve voor bijdragers.

1. **Zet de zeven scripts in GitHub Actions.** Grootste winst per uur in het hele onderzoek.
2. **markdownlint-cli2** toevoegen; structurele regels als custom rule.
3. **Vale met een eigen Nederlandse regelset** uit `docs-style.mdc`. Reken op een dag.
4. **`check-jsonschema --check-metaschema`** over alle schema's, en **lychee** voor externe links.
5. **Maak de interactie-ID's controleerbaar.** Vijftig regels script controleren dat elk ID uit §3 in §5 voorkomt en omgekeerd — de goedkoopste vorm van traceerbaarheid die bestaat.
6. **Los het pandoc-gat op.** Verifieer of de PDF-eis in U8 vandaag klopt.
7. Twee kleine correcties: U8 markeert volwassenheid op `$comment`, maar de [JSON Schema-spec](https://json-schema.org/draft/2020-12/json-schema-core) zegt *"Implementations MUST NOT take any other action based on the presence, absence, or contents of `$comment`"* — een eigen sleutel als `x-okx-volwassenheid` is spec-conform. En de ADR's kunnen naar MADR-frontmatter.

**Kost**: drie tot vijf dagen. Eén nieuwe afhankelijkheid met leercurve (Vale), de rest configuratie.

### Gemiddeld — echte traceerbaarheid, zelfde bronformaat

1. **OpenFastTrace.** U1–U10 en de processtappen krijgen een ID, koppelingspecificaties krijgen `Covers:`, `oft trace` faalt in CI bij ongedekte eisen. Alles blijft markdown en blijft renderen.
2. **Gherkin met Nederlandse sleutelwoorden** voor de happy flow en faalpaden; OFT leest die als testdekking, waarmee de keten sluit.
3. **YAML-frontmatter met JSON Schema** per document, gevalideerd met `remark-lint-frontmatter-validation`. Dan wordt "welke documenten raakt een wijziging in U4" een query in plaats van een grep.
4. **Beslis over het ArchiMate-model** in een expliciete ADR, met de MinBZK-tussenvorm als optie.

**Kost**: twee tot drie weken plus gewenning. Bijdragers leren één tag-syntaxis. Reken op zichtbare ruis: de eis-ID's staan als inline code in het document.

### Maximaal — publicatielaag en volledige machine-interpreteerbaarheid

1. **NL-ReSpec als publicatielaag.** De enige route die zowel GitHub-render als PDF zonder mitsen oplost, met aansluiting op de Logius/Geonovum-stack en BOMOS.
2. **AsyncAPI naast OpenAPI.** U4 en U5 beschrijven events die nu alleen in prozatabellen staan; de §3- en §7-tabellen worden dan gegenereerd in plaats van bijgehouden.
3. **Architectuur-as-code voor de koppelvlak-views**, met ingecheckte PNG's als artefact; ArchiMate blijft de ROSA-bron.
4. **Volledige OFT-keten** met dekkingsrapport als release-artefact.

**Kost**: hoog, en niet alleen in uren. Minstens drie extra bronformaten, één persoon die de toolchain bezit, en het scherpste risico: **"less is more" en "één bestand, één doel" komen onder druk te staan.** Zes tot tien weken plus blijvende onderhoudslast.

## Aanbeveling

Doe **minimaal** meteen — dat is bijna vrij geld en het dicht een echt gat.

Neem uit **gemiddeld** twee dingen los mee: het OFT-experiment op één koppelingspecificatie om te voelen of de tag-ruis acceptabel is, en de ArchiMate-beslissing, want dat probleem is aangetoond en heeft al een keer geld gekost.

Houd **maximaal** op de plank tot er een aanleiding is — een ROSA-scan, een leverancier die het contract machinaal wil consumeren, of een tweede releasepakket. NL-ReSpec is dan het eerste dat ik zou pakken, omdat het als enige de markdown-bron intact laat.

## Niet geverifieerd

- Of GitHub's mermaid daadwerkelijk `C4Context` rendert. Eén commit geeft uitsluitsel.
- Of de Structurizr mermaid-export goed rendert op GitHub, gegeven de `securityLevel`-eis.
- Of Sphinx-Needs officieel MyST-markdown ondersteunt.
- Of een OpenTaal-Hunspell-set out of the box in Vale werkt.
- Of `check-jsonschema` in zijn eigen documentatie draft 2020-12 letterlijk noemt (het volgt uit python-jsonschema).
- Of er een Spectral-plugin voor markdown-frontmatter bestaat (niet gevonden).
- Of er een tool bestaat die markdown-tabellen tegen een JSON Schema valideert (niet gevonden; zoektocht niet uitputtend).

## Gerelateerde uitwerkingen

- [AMIGO-producten en gat-analyse](20260804_1500_amigo-producten-en-gat-analyse.md)
- [Praktijk in standaardisatieprojecten](20260804_1500_praktijk-standaardisatieprojecten.md)
