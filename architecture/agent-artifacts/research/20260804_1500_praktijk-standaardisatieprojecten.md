# Praktijk: hoe andere standaardisatieprojecten business en techniek verbinden

Relateert aan: #130

Aanleiding: onze businesslaag en techniek hangen los van elkaar, en we wilden weten hoe grote standaardisatie- en koppelvlakprojecten dat oplossen binnen Git — inclusief wat er bij hen **niet** werkte. Alles hieronder is geverifieerd in de echte repositories, tenzij expliciet anders vermeld. Tellingen uit GitHub-codezoekopdrachten zijn bestandstellingen inclusief forks: orde van grootte, geen populatie.

## 1. HL7 FHIR Implementation Guides

De canonieke indeling is `sushi-config.yaml` plus `input/{fsh,pagecontent,images-source,resources,examples}`, met `fsh-generated/` en `output/` als uitvoer. Maar dat plaatje is niet universeel: [HL7/US-Core](https://github.com/HL7/US-Core), de grootste IG ter wereld, heeft **géén** `input/fsh/` — de profielen staan als YAML en JSON in `input/resources-yaml/` en `input/resources/`.

Het schoonste voorbeeld is [IHE/ITI.VHL](https://github.com/IHE/ITI.VHL): `input/fsh/` bevat precies zeven bestanden, één per artefactsoort — `actors.fsh`, `requirements.fsh`, `usecases.fsh`, `testplans.fsh`, `capabilitystatements.fsh`, `operationdefinitions.fsh`, `Aliases.fsh`. De [gepubliceerde artefactindex](https://build.fhir.org/ig/IHE/ITI.VHL/artifacts.html) telt 4 ActorDefinitions, 17 Requirements, 5 TestPlans, 5 ExampleScenarios en **nul** StructureDefinitions: een IG die vrijwel volledig businesslaag is, machineleesbaar gemaakt.

Nederlands: [Nictiz/AZ-IG](https://github.com/Nictiz/AZ-IG) met `input/pagecontent/{use-cases,functional-design,workflow,data-model,data-exchange,design-decisions,testing}.md`, en [minvws/generiekefuncties-docs](https://github.com/minvws/generiekefuncties-docs).

### Vijf koppelmechanismen, sterk verschillend in volwassenheid

1. **ActorDefinition → CapabilityStatement → `supportedProfile` → StructureDefinition.** Werkt en wordt breed toegepast; zie [IHE/pharm-mpd](https://github.com/IHE/pharm-mpd) met één bestand per actor en een exact parallelle `capabilitystatements/`-map.
2. **De `§`-syntaxis.** Auteurs markeren conformance-zinnen in gewone markdown (`§pdex-91: **SHALL** indicates…§`); de IG Publisher scant de gegenereerde HTML en bouwt er een `Requirements`-resource van. Gedocumenteerd op [build.fhir.org/ig/FHIR/ig-guidance/conformance-statements.html](https://build.fhir.org/ig/FHIR/ig-guidance/conformance-statements.html).
3. **[`Requirements.statement.satisfiedBy`](https://hl7.org/fhir/requirements.html)** — het veld dat een eis expliciet aan een profiel of element koppelt.
4. **[Obligations](https://www.hl7.org/fhir/obligations.html)**: conformance-verwachting per veld per actor. Nictiz motiveert het gebruik expliciet: *"support expectations are expressed as obligations bound to actors rather than the single mustSupport boolean"*.
5. **TestPlan met Gherkin.** [ITI.VHL/testplans.fsh](https://github.com/IHE/ITI.VHL/blob/master/input/fsh/testplans.fsh) koppelt `scope` aan een actor en `script.language = #text/x-gherkin` aan een `.feature`-bestand. Dat is de volledigste keten die is gevonden: actor → transactie → sectienummer → scenario.

### Wat er niet werkt

- **`satisfiedBy` wordt door niemand ingevuld.** Codezoekopdracht in `.fsh`: **0 treffers**. De machineleesbare eis-naar-artefact-traceerbaarheid bestaat in de specificatie en is dode letter.
- **US Core's Requirements-resource is een lijst zonder koppeling**: 328 KB, 425 statements, `satisfiedBy` 0×, `actor` als canonical 0×. De enige echte link is `narrativeLink` terug naar het HTML-anker — een index op de proza.
- **`Requirements-fromNarrative.json` blijft leeg zonder dat iemand het merkt.** Bij AZ-IG is het 419 bytes: alleen de header. Grep op `§` in vijf pagecontent-bestanden: 0 markers. Het bestand staat er, doet niets, wordt niet opgeruimd.
- **ExampleScenario is proza in een JSON-jasje.** ITI.VHL heeft 5 ExampleScenarios met samen 9 `process.step` en **0 `instance[]`-entries** — geen enkele koppeling van scenariostap naar voorbeeldresource.
- **Adoptiecijfers** (indicatief, `.fsh`): `Profile:` 6760 · `InstanceOf: Requirements` 1524 · `InstanceOf: ActorDefinition` 896 · `InstanceOf: ExampleScenario` **94** · `InstanceOf: TestPlan` **12** · `satisfiedBy` **0**.

## 2. TM Forum Open APIs

**Git is níét de bronwaarheid.** [tmforum-apis/TMF620_ProductCatalog](https://github.com/tmforum-apis/TMF620_ProductCatalog) is volledig plat, met **vier verschillende naamconventies binnen één repository**. De [gedeelde workflow](https://github.com/tmforum-apis/tmf-api-commons/blob/main/.github/workflows/release-api.yml) haalt nachtelijk een S3-index op, filtert op productiestatus, pakt alleen het swagger-type en commit dat. De repo is een afgeleide van een S3-bucket; alle andere artefacten worden bewust niet meegespiegeld.

Zes artefacttypes per API-versie: `swagger`, `conformance`, `user_guides`, `ctk`, `ri`, `postman`. **Er is geen artefacttype "user stories".** In productie is de set compleet (97×6); in Beta 74 swaggers, 43 conformance-documenten en **0 CTK's** — de techniek loopt structureel voor op de toetsingslaag.

**Op API-niveau: geen traceerbaarheid.** Het conformance profile is een PDF met tabellen, zonder requirement-ID's en zonder verwijzing naar use cases. Niet diffbaar, niet linkbaar, niet automatisch toetsbaar — de testkit moet die eisen dus opnieuw en handmatig coderen.

**Op ODA-niveau: wel, en expliciet.** [tmforum-oda/oda-canvas](https://github.com/tmforum-oda/oda-canvas) heeft `usecase-library/` (UC001–UC016 met PlantUML) naast `feature-definition-and-test-kit/features/`. Het ID staat op drie plekken tegelijk:

```gherkin
@UC003         # tagged as use case 3
@UC003-F001    # tagged as use feature 1 within use case 3
Feature: UC003-F001 Expose APIs: Create API Resource
```

Bestandsnaam, Gherkin-tag en `Feature:`-titel. Grep-baar, CI-selecteerbaar, zichtbaar in het testrapport. De README bevat een koppeltabel use case ↔ feature ↔ **teststatus**, met als motivering: *"This linkage ensures that the features are aligned with the overall design … and that the tests are verifying the correct behavior."*

Het beste artefact van heel TM Forum is de componentspecificatie in [TMForum-ODA-Ready-for-publication](https://github.com/tmforum-rand/TMForum-ODA-Ready-for-publication): een YAML met `componentMetadata` (inclusief eTOM-bedrijfsprocessen) en een `exposedAPIs`-blok dat per API precies de resource/methode-combinaties vastlegt. Dat is **een conformance profile als data**, en er wordt een trace-matrix uit gegenereerd. De organisatie heeft dus twee conformance-mechanismen naast elkaar — een PDF zonder ID's en een YAML als data — die niet aan elkaar geknoopt zijn.

## 3. SEMIC / ISA² Core Vocabularies

Eén repository per vocabulaire. [Core-Person-Vocabulary/releases/2.1.2](https://github.com/SEMICeu/Core-Person-Vocabulary/tree/master/releases/2.1.2) bevat naast de Turtle en SHACL een **binaire Enterprise Architect-file van 4,2 MB** die per release wordt meegecommit: niet diffbaar, niet reviewbaar in een pull request, niet leesbaar zonder commerciële Windows-tool.

De toolchain draait via `informatievlaanderen/oslo-ea-to-rdf` — **SEMIC gebruikt de Vlaamse OSLO-toolchain**, niet iets eigens. De scope-afbakening van een hele specificatie is één JSON-configuratiebestand met een handvol velden.

De [Style Guide](https://github.com/SEMICeu/style-guide/blob/main/docs/modules/ROOT/pages/arhitectural-clarifications.adoc) is de sterkste inhoudelijke bijdrage: expliciet op OMG MDA gebaseerd, met vier zorgen en één artefact elk (conceptueel model in UML, ontologie in OWL 2, data shape in SHACL, specificatiedocument in HTML). Letterlijk: *"UML conceptual models can be used as the **single source of truth** [CMC-R1]. … The other representations are automatically derived."* En eerlijk: *"UML cannot cover all potential needs specific to each derived representation."*

### Wat er niet werkt

- **Use cases bestaan niet als artefact in de specificatie.** De methodologieregel MC-R1 eist wél *"use cases, scenarios, competency questions … referred by the concepts"* en zegt er direct achteraan: *"We do not outline a concrete methodology here"*. De domein-use cases leven in een los handboek.
- **De koppeling application profile naar core vocabulary zit als UML tagged value in het binaire bestand.** De enige validator, [ProfileGuard](https://github.com/SEMICeu/ProfileGuard), zegt in zijn eigen README *"highly experimental … results should not be considered reliable"* en heeft precies één geïmplementeerde regel.
- **31 gearchiveerde repositories**: het hele validator- en harvester-ecosysteem uit de ISA²-tijd is dood. Ook SEMIC's eigen ReSpec-fork ligt sinds 2021 stil — ze hadden ooit die route en hebben hem laten vallen voor de EA-pipeline.
- **De Style Guide is publiek bevroren op 1.0.0 (mei 2023)** terwijl er commits tot juni 2026 zijn op vijftien losse branches. Drie jaar wijzigingen zonder release.
- **SEMIC zoekt zelf een uitweg**: [tooling-evaluation](https://github.com/SEMICeu/tooling-evaluation) bevat vier parallelle experimenten, en [core_person_linkml](https://github.com/SEMICeu/core_person_linkml) is *"a continuous evaluation harness for LinkML itself"*.

## 4. OSLC

Alle specificaties in [één repository](https://github.com/oslc-op/oslc-specs), per domein strak drieledig: Specification (proza plus conformance), Vocabulary, Constraints. Er is een `templates/`-map als kopieerbaar skelet voor een nieuw domein.

**De Turtle is de bron, de HTML-tabel is de projectie — client-side.** Het lichaam van de vocabulairepagina is één lege div met `data-include="./requirements-management-vocab.ttl"`; ReSpec leest de Turtle in en bouwt de termentabel bij het renderen. Geen buildstap, geen synchronisatieprobleem.

**De CI verifieert in plaats van te genereren.** [ShapeChecker](https://github.com/oslc-op/oslc-specs/blob/master/tools/ShapeChecker/README.md): *"It cross-checks the vocabularies and shapes, ensuring that each RDF term used in the shapes … is actually defined in that vocabulary, and that each term defined in the given vocabularies is used somewhere in a shape."* Bidirectioneel, afgedwongen bij elke commit. Dezelfde README is zelfkritisch: *"This is not the easiest of tools to use, and the messages it produces are often obscure."*

Traceerbaarheid zit als gewone properties in de domein-shapes (`elaboratedBy`, `specifiedBy`, `affectedBy`): geen apart traceerbaarheidsmodel, links zijn gewone tripels met de constraint in de shape.

**De scherpste zelfkritiek** staat in de note [Linking Profiles](https://github.com/oslc-op/oslc-specs/blob/master/notes/linking-profiles/link-profiles.md):

> *"OSLC interoperability is not automatically implied by OSLC specifications, as the specifications allow for high degree of conformance variability."*
> *"A key aspect of reducing spec variabilities is converting 'SHOULD' and 'MAY' clauses in the spec to 'MUST' in certain profiles."*

Vier domeinspecificaties zijn expliciet verweesd ("Old specs … help needed!"). Externe adoptiecijfers (van een concurrerende leverancier, dus met voorbehoud): 20% van de 25 meest gangbare tools heeft enige OSLC-capability, **100% heeft wél een REST API**.

## 5. Nederlandse publieke sector

### VNG Realisatie — de businesslaag die verdampte

[gemma-zaken](https://github.com/VNG-Realisatie/gemma-zaken) had precies wat wij zoeken: **GitHub-issue = user story**. [Issue #65](https://github.com/VNG-Realisatie/gemma-zaken/issues/65) is letterlijk *"als gemeentemedewerker wil ik inzage in alle zaken die betrekking hebben op de persoon/aanvrager…"*, met een Definition of Ready die eist dat de story een architectuurschets heeft, een veldmapping naar RGBZ2, en past op GEMMA 2. Het issue linkt naar een markdown-architectuurschets, en die schets linkt terug met `## User story · [User story #65]`.

**Dit is opgegeven.** Commit `8e19656` van **2 mei 2019** heet ":memo: Processen verplaatst naar archief buiten documentatie." De praktijkbeproevingen van Delft, Dimpact, Amsterdam, Rotterdam en Utrecht staan sindsdien in `docs/archief/processen/`. Harde cijfers:

| pad | laatste inhoudelijke commit |
|---|---|
| `docs/archief` | 2025-01-29, alleen opschoning voor linting |
| `docs/community` (sprintdemo's) | bijeenkomstnotulen stoppen bij 2019-06-20 |
| `api-specificatie` | 2026-07-24, meer dan 100 commits |
| `docs/standaard` | 2026-07-29, meer dan 100 commits |

De link in issue #65 naar de architectuurschets geeft nu **404**. Zeven jaar oude linkrot in de enige koppeling tussen user story en architectuur.

Wat wél doorleeft is een handmatige release-matrix die zichtbaar drift, en zeven Spectral-ruleset-varianten naast elkaar met tien uitgecommentarieerde regels — zichtbaar geworstel. Ontwerpbesluiten staan in één groeiend prozabestand zonder ID's, datum of status: het tegendeel van ADR-praktijk.

**Gedocumenteerd retrospectief**: VNG stopte in 2024 met de referentie-implementaties. *"Het onderhouden van deze implementaties kost echter veel tijd terwijl ze weinig gebruikt worden. … De gebruikers gaven aan dat zij liever zien dat de VNG meer tijd besteed aan bijvoorbeeld het verbeteren van de documentatie."* ([eindeontwikkelingris.md](https://github.com/VNG-Realisatie/gemma-zaken/blob/master/docs/beheer/eindeontwikkelingris.md))

### Haal Centraal — het sterkste Nederlandse voorbeeld

[BRP-API/Haal-Centraal-BRP-bevragen](https://github.com/BRP-API/Haal-Centraal-BRP-bevragen): **373 `.feature`-bestanden**, geordend per resource en veld, naast `specificatie/brp-api/` met één schemabestand per concept en een eigen versienummer per concept (`gezagsrelatie-v1.yaml` naast `-v2.yaml`).

De gedragsspecificatie **is** de testsuite **is** de gepubliceerde documentatie. Het [overzicht](https://raw.githubusercontent.com/BRP-API/Haal-Centraal-BRP-bevragen/master/docs/features/index.md) toont **4818 scenario's, 3 gefaald, 4815 geslaagd**, met per functioneel domein een testrapport.

In [Haal-Centraal-common](https://github.com/VNG-Realisatie/Haal-Centraal-common) staat de gedeelde laag, waarbij elk feature-bestand opent met een commentaarblok dat de norm citeert:

```gherkin
# language: nl
# Nederlandse API Strategie:
# API-12 Representatie op maat wordt ondersteund
```

En — meta — `features/spectral_rules/*.feature` zijn Gherkin-scenario's die de **linterregels zelf** testen.

### Logius — één repository per normatief document

Ongeveer 50 repositories, consequent één repo = één document. Verlaten repositories zijn netjes gearchiveerd. Drie ondersteunende repositories dragen de hele vloot: [Automatisering](https://github.com/Logius-standaarden/Automatisering) (herbruikbare workflows plus scripts voor PDF-generatie, eigen spellingwoordenlijst en linkchecker), `publicatie` en `Publicatie-Preview` voor snapshots per pull request. Iedere maandagochtend draait een linkcheck over alle gepubliceerde documenten.

**[API Design Rules](https://github.com/Logius-standaarden/API-Design-Rules) is het beste governance-voorbeeld van Nederland**: `sections/*.md` met de norm, `media/linter.yaml` met de Spectral-ruleset, `linter/testcases/<naam>/{openapi.json,expected-output.txt}` als golden tests op de vertaling zelf, en `examples/{aspnet,express,golang,python,quarkus}` die in de CI-matrix gebouwd én gelint worden. De standaard bewijst bij elke commit dat hij in vijf stacks haalbaar is.

Een regel draagt een ID in een `<div class="rule" id="/core/naming-resources">`, met de oude numerieke ID (`api-05`) als onzichtbaar anker ernaast — een **zichtbaar opgeheven conventie**, netjes afgehandeld. De bijbehorende beheerregel staat bij Geonovum: *"Design rules have unique and permanent numbers. In the event of design rules being deprecated or restructured, they are removed from the list. Therefore, gaps in the sequence can occur."*

De koppeling norm naar check is een **comment plus `documentationUrl`** in de ruleset — grep-baar, maar geen machineleesbaar veld. Dat is de zwakke schakel in een verder sterke keten.

### Geonovum en DSO

Een **vloot van eendocument-repositories onder centrale governance**: 89 Geonovum-repositories plus 8 van het BRO-programma, elk met een gepinde ReSpec-versie in `.github/repos.json`. De drift is meetbaar: 67 op `35.8.0`, 8 nog op de oude build `24.5.2`, en vier versies daartussen.

**Documentstatus is metadata, niet proza**: `specStatus: wv|cv|vv|def|basis` en `specType: NO|ST|IM|PR|HR|WA|BD|AL|BP` in `js/config.js` bepalen de publicatie-URL en de statusparagraaf. Die typologie is precies een artefacttypelijst.

MIM is model-as-code met binaire bron: een Sparx-bestand plus `mim.ttl`, met een generatorketen naar markdown en diagrammen. De DSO-validatiematrix is spreadsheet-als-database: `.xlsx` plus een Python-script naar markdown naar ReSpec. Werkt, maar de bron is binair en de README noemt nog de oude bestandsnamen.

[KP-APIs](https://github.com/Geonovum/KP-APIs) heeft naast de architectuurmodule een volwaardige module **Gebruikerswensen** — een eigen normatief document over developer experience, mét persona. Elk module-mapje volgt hetzelfde patroon, en er is een kopieerbaar `_template/`.

**NORA is een MediaWiki zonder git-repository.** Daarmee ontbreken versionering per artefact, pull request-review, CI-checks en een PDF-pipeline. Dit is het contrastgeval.

## 6. Edustandaard: ROSA, OKE en OEAPI

**ROSA is model-as-code met wiki-als-publicatie.** Het [beheerproces](https://rosa.wikixl.nl/index.php/Beheerproces) stelt: *"De modellen worden ontwikkeld in Archi met behulp van Github voor versiebeheer."* Geverifieerd: [edustandaard/rosa](https://github.com/edustandaard/rosa) staat in **coArchi-formaat** — één XML-bestand per element, bestandsnaam is de UUID — met `CONTRIBUTING.md` en `CODINGGUIDELINES.md`. Die guidelines zijn precies de machine-interpreteerbaarheidsdiscipline:

> *"Er zijn bepaalde conventies die we volgen om de Archimate elementen en relaties netjes in de ROSA wiki te krijgen. We gebruiken hiervoor de documentatie en properties van de elementen."*

met per elementtype de verplichte properties. De [ROSA-scan](https://rosa.wikixl.nl/index.php/Architectuurscan) is het comply-or-explain-toetsinstrument; de OKE-scan toont ook waar het schuurt.

**OKE volgt AMIGO één-op-één.** Het afsprakensetdocument draagt letterlijk de ondertitel *"Afsprakenset op basis van AMIGO-aanpak en OOAPI"* en heeft hoofdstukken die op de AMIGO-stappen mappen. Het gegevensmodel is **dubbelgelabeld**: `ComponentOffering (Planbare toets & Zitting)`, `CourseOffering (Opleidingsdeel)` — links de technieknaam, rechts de mbo-businessnaam. Dat is het semantische scharnier, en het is handmatig proza in een PDF. In [NED-OOAPI](https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI) mappen `doc/flow0.md` tot en met `flow6.md` elke informatiestroom op concrete endpoints.

**OEAPI is puur techniek en inmiddels versieloos**, een bewust besluit vastgelegd als [ADR](https://github.com/open-education-api/governance-decisions/blob/main/adr/0004-restructuring-oeapi-version-management-to-ensure-immutable-release.md): *"Documentation becomes an artefact generated from tagged specification states."* Twee koppelmechanismen: **consumer** (extensie in de payload, per consumer een YAML-bestand, met de Nederlandse businessterm in de `description`) en **profile** (conformance-definitie voor een use case). De [Profiling Guidelines](https://github.com/open-education-api/documentation/blob/main/documentation/technical/consumers-and-profiles/profiling-guidelines.md) beschrijven een eigen AMIGO-achtig proces; de bijbehorende `profiles`-repository is nog leeg.

**Use cases in de OEAPI-repositories zijn drie alinea's proza.** Er is geen scenariomodel, geen ArchiMate, geen requirements-artefact. De businesslaag zit alleen bij de afnemende afsprakensets zoals OKE.

**Verval**: de hele `open-education-api`-organisatie uit 2016 is gearchiveerd. Open Onderwijs API 4.0 staat op "Vervallen / Afgeraden". UWLR — de aanleiding voor AMIGO — heeft gebruiksadvies "Onder voorwaarden", werkgroep beëindigd.

## 7. OpenAPI en AsyncAPI

**[Arazzo](https://github.com/OAI/Arazzo-Specification)** (v1.1.0) is de use case als data: *"the Arazzo Specification enables the ability to articulate **the functional use cases offered by an API (or group of APIs)**."* Het model koppelt `sourceDescriptions` aan `workflows[]` met `steps[]` (elk met een `operationId`), `successCriteria` en expliciete `inputs`/`outputs`. **De dataflow tussen stappen is expliciet gemodelleerd** — precies wat proza-scenario's altijd kwijtraken. Workflows kunnen elkaar aanroepen, dus DRY op scenarioniveau.

Eerlijk: in het voorbeeld staat een commentaarregel *"there is some implied selection here … not totally sure how to indicate that"* — Arazzo kan keuzelogica niet volledig vastleggen. Arazzo hanteert use cases als genummerde, refereerbare issues met een verplichte `USECASE-`-prefix.

**AsyncAPI heeft geen use case-artefact.** Geen `usecase-library`, geen `features/`, geen use case-issuetemplate. De brug voor async loopt via Arazzo, maar het bijbehorende voorbeeld ontbreekt nog.

## 8. Acht patronen die in meerdere projecten terugkomen

**P1. Stabiele, permanente ID's zijn de enige lijm die het volhoudt — en het ID staat op meerdere plekken tegelijk.** TM Forum ODA zet `UC003-F001` in bestandsnaam, Gherkin-tag én `Feature:`-titel. Logius zet de regel-ID in de `<div class="rule">` én als comment in de linterruleset. FHIR zet `§pdex-91` in de proza en `"key": "CONF-0002"` in de gegenereerde resource. De beheerregel is overal hetzelfde: nummers zijn permanent, gaten mogen ontstaan, nooit hergebruiken.

**P2. Het scenario als uitvoerbare test is de sterkste brug die iemand heeft gebouwd.** Haal Centraal (4818 scenario's als publicatie), TM Forum ODA (use case → feature → step definition), IHE VHL (TestPlan → actor → Gherkin), Arazzo (`successCriteria` als data). Waar dit ontbreekt verwatert de eis: TM Forum's PDF-conformance moet handmatig in de testkit worden overgecodeerd, en daar ontstaat de drift.

**P3. Eén doel per bestand of map, conventie boven configuratie.** Logius: één repo = één document. Geonovum: 97 eendocument-repo's met centraal register. IHE VHL: zeven FSH-bestanden, één per artefactsoort. OGC Building Blocks: één map per bouwsteen met vaste bestandsnamen. Haal Centraal: één schemabestand per concept. Het tegenvoorbeeld staat in dezelfde wereld: TMF620 met vier naamconventies in één repo.

**P4. Norm → machine-uitvoerbare check → golden testcases → referentie-implementaties.** Logius ADR is de referentie. Haal Centraal gaat verder met Gherkin-tests vóór de linterregels. OSLC doet de variant zonder generatie met bidirectionele consistentiecheck in CI. Let op de kostenkant: VNG stopte met referentie-implementaties omdat gebruikersonderzoek uitwees dat ze weinig waarde hadden; Logius' variant is veel goedkoper omdat de voorbeelden geen product zijn maar lint-proefkonijn.

**P5. Maak de bron diffbaar; binaire bronnen doden de review.** FSH rechtvaardigt zichzelf met *"meaningful version-to-version differentials … and nimble refactoring"*. Daartegenover: SEMIC commit 4,2 MB Enterprise Architect per release, Geonovum een Sparx-bestand, DSO een spreadsheet. Het contrast is scherp: SEMIC heeft het expressievere bronformaat en de armere praktijk (niemand kan een pull request reviewen; ze zoeken nu actief een vervanger). Bij ROSA is coArchi de tussenvorm die het model wél diffbaar maakt.

**P6. Genereer de publicatie; scheid werkversie van vastgestelde versie; zet de status in de metadata.** Geonovum codeert status en documenttype als enum. Logius scheidt `develop`/`main` met een preview-repo per pull request. FHIR scheidt IG-repo van publicatierepo. De regel die overal geldt: nooit met de hand in gegenereerde bestanden schrijven.

**P7. Vlootbeheer: een templaterepo, centrale CI en een register — met zichtbare drift.** Geonovum beheert 97 documentrepo's met gepinde versies; Logius centraliseert build, check, publish en linkcheck. En de drift is meetbaar: 67 repo's op de actuele ReSpec-versie, 8 nog op een build van jaren terug. Vlootbeheer werkt, maar nooit voor 100%.

**P8. De businesslaag verdampt zonder eigenaar en CI-haak — en de semantische brug blijft handwerk.** Het duidelijkste bewijs staat in gemma-zaken: user stories naar het archief in 2019, terwijl de API-specificatie in 2026 nog wekelijks commits krijgt. Hetzelfde patroon elders: FHIR's `satisfiedBy` nul invullingen tegenover 6760 profielen; TM Forum 74 swaggers en 0 testkits in Beta; SEMIC parkeert use cases in een los handboek; OEAPI's use cases zijn drie alinea's.

> De les die alle deelonderzoeken onafhankelijk trokken: **de businesslaag overleeft alleen als ze (a) een ID heeft dat elders wordt aangeroepen, (b) een CI-haak heeft die faalt als de koppeling breekt, en (c) zichtbaar is in de gepubliceerde output.** Bij Haal Centraal is aan alle drie voldaan, en daar leeft de businesslaag na acht jaar nog.

## Niet geverifieerd

- Kritiek uit de FHIR-community: chat.fhir.org vereist login, HL7 JIRA niet doorzocht. De uitspraken over ExampleScenario en TestPlan berusten op gemeten adoptie en inspectie van de enige serieuze gebruiker, niet op verklaringen van implementeerders.
- De volledige inhoud van de TM Forum conformance- en user guide-PDF's; `tmforum.org` gaf consequent HTTP 403.
- Onafhankelijke kritiek op SEMIC-adoptie: alle zoekresultaten waren materiaal van de Europese Commissie zelf. De interne signalen zijn sterker bewijs dan wat extern beschikbaar is.
- AMIGO's ontwikkelstraat (Sparx EA plus Imvertor): geclaimd in het methodiekdocument, geen publieke repository of output gevonden.
- Een door Edustandaard voorgeschreven documentsjabloon voor een afsprakenset: bestaat voor zover gevonden niet; de AMIGO-artefactenlijst functioneert als de facto structuur en OKE volgt die letterlijk.
- Een NORA-git-repository: niet gevonden.

## Gerelateerde uitwerkingen

- [AMIGO-producten en gat-analyse](20260804_1500_amigo-producten-en-gat-analyse.md)
- [Gereedschap: requirements, architectuur en documentatie als code](20260804_1500_gereedschap-requirements-architectuur-docs-as-code.md)
