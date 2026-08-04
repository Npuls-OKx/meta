# Business en techniek verbinden: waar we staan en drie oplossingsrichtingen

Relateert aan: #130

Dit document bereidt een besluit voor. Het vat samen waar OKx staat, zet de drie oplossingsrichtingen naast elkaar die uit het onderzoek naar voren komen, benoemt welke opties zijn afgevallen en waarom, en sluit af met een voorkeur. Het is bedoeld om samen met collega's een keuze te maken; het besluit zelf hoort daarna in een ADR.

Onderbouwing: [AMIGO-producten en gat-analyse](20260804_1500_amigo-producten-en-gat-analyse.md), [Praktijk in standaardisatieprojecten](20260804_1500_praktijk-standaardisatieprojecten.md) en [Gereedschap](20260804_1500_gereedschap-requirements-architectuur-docs-as-code.md).

---

## 1. Waar we nu staan

### Wat er ligt

Ongeveer 8.100 regels markdown in 66 bestanden in [`Npuls-OKx/Public`](https://github.com/Npuls-OKx/Public), plus een kennisbasis in meta. De inhoudelijke kwaliteit is niet het probleem: de interactie-analyse (sequentiediagrammen met faalpaden) en de berichtspecificatie (JSON Schema met voorbeelden) zijn de verst ontwikkelde delen en zijn AMIGO-conform van vorm.

### Het probleem, in één zin

**Er is geen mechanisme dat de businesslaag aan de techniek bindt.** Een kaderscenario en een payload-specificatie staan naast elkaar zonder dat iets afdwingt dat ze over hetzelfde gaan, en zonder dat een wijziging in het ene zichtbaar maakt wat het in het andere raakt.

### Vier feiten die de urgentie bepalen

| Feit | Bron |
|---|---|
| **Er draait niets in CI.** `Public/.github/` bevat alleen issue- en PR-templates, terwijl er zeven werkende controlescripts liggen. Een pull request die de conventies breekt komt er vandaag gewoon door | [Gereedschapsverslag §0](20260804_1500_gereedschap-requirements-architectuur-docs-as-code.md#kalibratie-wat-we-nu-hebben) |
| **Het ArchiMate-model heeft al een keer geld gekost.** Bij een handmatige merge in juli 2026 vielen 276 elementdefinities weg en ontstonden 295 dode verwijzingen over 9 views. `validate-archimate.py` detecteert dat achteraf; het onderliggende probleem — één bestand van 40.478 regels — is met geen enkel script op te lossen | ADR 0010, [`scripts/validate-archimate.py`](../../../scripts/validate-archimate.py) |
| **Twee AMIGO-producten ontbreken volledig**: de vocabulairespecificatie (een van de vijf onderdelen) en de interfacespecificatie (nul OAS-bestanden in Public) | [AMIGO-verslag §7](20260804_1500_amigo-producten-en-gat-analyse.md#7-gat-analyse-amigo-product-naast-okx-artefact) |
| **Het product van AMIGO-stap 1 staat in de verkeerde repository.** AMIGO schrijft ArchiMate voor als scenariobeschrijving; ons [`model.archimate`](../../../architecture/model/model.archimate) staat in meta en is voor een externe lezer onbereikbaar | idem |

### De ene bevinding die alles stuurt

AMIGO beantwoordt onze vraag al, en het antwoord is normatief. [AMIGO-methodiek v1.1.0](https://www.edustandaard.nl/app/uploads/2025/10/AMIGO-methodiek-1.1.0-1.pdf), §5.4, p.15:

> *"Technische modellen worden gegenereerd uit logische gegevensmodellen d.m.v. gestructureerde transformaties. Dit houdt in dat **wijzigingen in technische modellen altijd op logisch niveau worden aangevangen**. […] Hiertoe worden tussen de modellen **traceerbaarheidsrelaties** aangebracht."*

Wij doen dit omgekeerd: we schrijven het technische schema met de hand en genereren er leesweergaven uit. Dat is geen detail — het is precies de as waarop de drie richtingen hieronder uiteenlopen.

En AMIGO is geen vrijblijvend advies: het staat [in ROSA geregistreerd als Requirement met gebruiksadvies "Verplicht"](https://rosa.wikixl.nl/index.php/Id-2efe8b23fa1041ab955597e8f684c1d5). Tegelijk laat principe I1 (p.10) gefaseerde invoering expliciet toe: *"Bestaande interacties en uitwisselingen kunnen stapsgewijs naar een op AMIGO gebaseerde structuur worden overgezet."*

---

## 2. Drie oplossingsrichtingen

De vraag achter elke richting is dezelfde: **wat draagt de koppeling tussen business en techniek?** Er zijn drie antwoorden, en elk heeft in het onderzoek een sterk voorbeeld én een waarschuwend voorbeeld.

### Richting A — Het **ID** draagt de koppeling

Elke eis, elk uitgangspunt en elke processtap krijgt een permanent identificatienummer. Documenten verderop in de keten roepen dat nummer aan. Een controle in CI faalt zodra een eis nergens wordt afgedekt of een verwijzing naar een niet-bestaand nummer wijst. De markdown blijft de bron; er komt alleen notatie bij.

**Hoe dat er in de praktijk uitziet.** Bij [Logius API Design Rules](https://github.com/Logius-standaarden/API-Design-Rules) draagt elke regel een ID in de tekst (`<div class="rule" id="/core/naming-resources">`), datzelfde ID staat als comment in de Spectral-ruleset, en er liggen golden testcases per regel plus vijf referentie-implementaties die in de CI-matrix worden gelint. Bij [TM Forum ODA](https://github.com/tmforum-oda/oda-canvas) staat `UC003-F001` op drie plekken tegelijk: bestandsnaam, Gherkin-tag en `Feature:`-titel — grep-baar, CI-selecteerbaar, zichtbaar in het testrapport.

**Wat wij er al van hebben.** De interacties in de koppelingspecificaties dragen al `I1` tot en met `I5`. Dat is een handgeschreven versie van dit patroon, die nergens machinaal wordt gecontroleerd. Vijftig regels script controleren dat elk ID uit de interactietabel in een sequentiediagram voorkomt en omgekeerd.

**Waarschuwing uit het onderzoek.** Een ID-mechanisme dat niemand aanroept, sterft stil. FHIR heeft met `Requirements.statement.satisfiedBy` precies dit veld in de standaard, en de codezoekopdracht over alle publieke implementation guides levert **nul** invullingen op tegenover 6760 profielen. Het bestaat, en het is dode letter.

| | |
|---|---|
| **Kost** | Laag tot middel. Bijdragers leren twee regels notatie. Twee tot drie weken, plus gewenning |
| **Levert** | Een wijziging in een uitgangspunt laat zien welke specificaties, payloads en scenario's meebewegen |
| **Risico** | Zichtbare ruis: ID's staan als inline code in een gereleased document. En: een tracer die niet faalt, wordt genegeerd |
| **Gereedschap** | [OpenFastTrace](https://github.com/itsallcode/openfasttrace/blob/main/doc/user_guide.md) — leest markdown als eersterangs bron, dekkingstags in HTML-comments die op GitHub én in pandoc onzichtbaar zijn. GPL-3.0, 157 sterren: reële bus-factor, maar de tags zijn regex en dus zelf na te rekenen |

---

### Richting B — Het **model** draagt de koppeling

Er komt een logisch gegevensmodel als eigen product tussen scenario en schema. Technische artefacten worden daaruit gegenereerd; wijzigingen beginnen altijd bovenaan. Dit is wat AMIGO §5.4 voorschrijft, en het is de enige richting die volledig methodiek-conform is.

**Hoe dat er in de praktijk uitziet.** [SEMIC Core Vocabularies](https://github.com/SEMICeu/Core-Person-Vocabulary/tree/master/releases/2.1.2/uml) doet dit expliciet: het UML-model is *"the single source of truth"*, de andere representaties (OWL, SHACL, HTML) worden afgeleid. [ROSA zelf](https://github.com/edustandaard/rosa) doet het ook — het ArchiMate-model staat in git in coArchi-formaat, één XML-bestand per element, met `CODINGGUIDELINES.md` die per elementtype de verplichte properties voorschrijft.

**Het waarschuwende voorbeeld is scherp, en het komt uit dezelfde hoek.** SEMIC commit per release een binair Enterprise Architect-bestand van 4,2 MB. Niemand kan een pull request reviewen; er is geen diff. De enige validator voor de koppeling tussen profiel en vocabulaire zegt in zijn eigen README *"highly experimental … results should not be considered reliable"*. 31 repositories in die organisatie zijn gearchiveerd, de style guide is publiek bevroren sinds 2023 terwijl er commits tot 2026 zijn, en SEMIC [zoekt zelf actief een vervanger](https://github.com/SEMICeu/tooling-evaluation). **De organisatie met het expressiefste bronformaat heeft de armste praktijk.**

De tegenpool laat zien dat het wél kan zonder generatie: [OSLC](https://github.com/oslc-op/oslc-specs/blob/master/tools/ShapeChecker/README.md) houdt de Turtle als bron en de HTML-tabel als projectie, en laat CI *bidirectioneel* verifiëren dat elke term in de shapes in de vocabulaire staat én andersom. Dezelfde README is eerlijk: *"This is not the easiest of tools to use, and the messages it produces are often obscure."*

| | |
|---|---|
| **Kost** | Hoog. Een logisch model als eigen product, een generatieketen, en iemand die de toolchain bezit. Zes tot tien weken plus blijvende onderhoudslast |
| **Levert** | Volledige AMIGO-conformiteit, en de enige richting die de ROSA-gegevenscatalogus echt hergebruikt |
| **Risico** | Het aangetoonde patroon: een binaire of moeilijk reviewbare bron doodt de bijdrage. Bij ons zou dat het ArchiMate-model zijn |
| **Deelbesluit dat los urgent is** | [coArchi](https://github.com/archimatetool/archi-modelrepository-plugin/wiki/Understand-the-Basics) lost ADR 0010 op — één bestand per element in plaats van 40.478 regels — maar zegt letterlijk: *"you shouldn't use merge, pull requests or similar features from your Git server as this would most certainly lead to model corruption."* Dat botst met ADR 0001. [MinBZK](https://github.com/MinBZK/gdi-gegevensuitwisseling) hanteert de tussenvorm: model in coArchi, per release een uitwisselformaat-export plus views naar de publieke repo |

---

### Richting C — De **test** draagt de koppeling

Het scenario wordt uitvoerbaar. Een happy flow en een faalpad worden geschreven in `Gegeven / Als / Dan`, en dat bestand is tegelijk de specificatie, de test en de gepubliceerde documentatie. Wat niet getest kan worden, is niet gespecificeerd.

**Het sterkste voorbeeld uit het hele onderzoek.** [Haal Centraal BRP-bevragen](https://github.com/BRP-API/Haal-Centraal-BRP-bevragen) heeft 373 feature-bestanden en publiceert het testrapport als onderdeel van de documentatie: **4818 scenario's, 3 gefaald, 4815 geslaagd**. In [Haal-Centraal-common](https://github.com/VNG-Realisatie/Haal-Centraal-common) opent elk feature-bestand met een commentaarblok dat de norm citeert (`# API-12 Representatie op maat wordt ondersteund`), en er staan zelfs [Gherkin-scenario's die de linterregels zélf testen](https://github.com/VNG-Realisatie/Haal-Centraal-common/tree/master/features/spectral_rules).

**Gherkin kan Nederlands.** Geverifieerd in [`gherkin-languages.json`](https://raw.githubusercontent.com/cucumber/gherkin/main/gherkin-languages.json), taalcode `nl`: `Functionaliteit`, `Achtergrond`, `Scenario`, `Gegeven`, `Als`, `Wanneer`, `Dan`, `Voorbeelden`. Voor onderwijskundigen is dat aantoonbaar toegankelijker dan een modelleertaal.

**Waarschuwing uit het onderzoek.** Waar dit ontbreekt, verwatert de eis meetbaar. TM Forum's conformance profile is een PDF met tabellen zonder ID's; de testkit moet die eisen handmatig overcoderen, en in de Beta-status staan 74 API-specificaties tegenover **nul** testkits. FHIR's ExampleScenario is een tweede geval: 5 exemplaren bij de serieuste gebruiker, met samen 9 processtappen en **nul** koppelingen naar voorbeeldresources — proza in een JSON-jasje.

| | |
|---|---|
| **Kost** | Middel. De vorm is leesbaar zonder training; de investering zit in het uitvoerbaar maken tegen een echte implementatie |
| **Levert** | De enige richting die alle drie de overlevingsvoorwaarden uit het onderzoek tegelijk invult: een ID dat elders wordt aangeroepen, een CI-haak die faalt, en zichtbaarheid in de gepubliceerde output |
| **Risico** | Zonder implementatie om tegen te draaien is een `.feature`-bestand niet meer dan een net gestructureerd scenario. De waarde ontstaat pas als er iets te toetsen valt |
| **Voorbeeld om te bestuderen** | [IHE ITI.VHL](https://github.com/IHE/ITI.VHL) koppelt TestPlan aan actor aan Gherkin-bestand — de volledigste keten die is gevonden binnen FHIR |

---

### De drie naast elkaar

| | A — ID draagt | B — Model draagt | C — Test draagt |
|---|---|---|---|
| **Bron blijft markdown** | ja | nee | ja, plus `.feature` |
| **AMIGO-conform** | deels (traceerbaarheid wel, generatie niet) | volledig | deels |
| **Adoptiedrempel bijdrager** | twee regels notatie | modelleertaal en tool | Nederlandse zinnen |
| **Faalt CI als de koppeling breekt** | ja | alleen met eigen checker | ja |
| **Zichtbaar in gepubliceerde output** | nee, rapport is CI-artefact | ja | ja |
| **Sterkste voorbeeld** | Logius API Design Rules | ROSA / OSLC | Haal Centraal |
| **Waarschuwend voorbeeld** | FHIR `satisfiedBy`: 0 invullingen | SEMIC: binaire bron, praktijk verschraald | TM Forum: 74 specs, 0 testkits |
| **Doorlooptijd** | 2–3 weken | 6–10 weken | 3–5 weken |

---

## 3. Wat is afgevallen, en waarom voor OKx

| Optie | Waarom niet |
|---|---|
| **[Sphinx-Needs](https://eclipse.dev/score/docs.html)** | De zwaarste referentie in het onderzoek (Eclipse S-CORE, ISO 26262), maar gebouwd voor domeinen waar een documentatie-build vanzelfsprekend is. Bij ons is het contract *"de markdown op GitHub is het document"* — dit draait die bronwaarheid om |
| **StrictDoc** | Markdown is er expliciet als **experimenteel** gemarkeerd. Wel onthouden als vangnet: de ReqIF-export is de brug als een leverancier ooit met DOORS of Polarion aankomt |
| **Doorstop** | Zet elke eis als los YAML-bestand buiten het document. Botst frontaal met onze regel dat een gereleased document zelfdragend is |
| **OSLC als integratielaag** | Vereist een draaiende server. Wij hebben geen ALM-keten om te integreren. Ter kalibratie: 20% van de gangbare tools heeft OSLC-ondersteuning, 100% heeft een REST API |
| **Bikeshed** | Functioneel het rijkst voor spec-schrijven, maar GitHub rendert `.bs` niet en er is geen PDF. Beide zijn bij ons harde randvoorwaarden |
| **Antora** | Vereist migratie van markdown naar AsciiDoc en levert geen specificatie-functie terug. Geen enkele standaardisatieorganisatie gebruikt het |
| **Spec-Up-T** | Het idee is bruikbaar — één bestand per begrip met `[[def:]]`, precies wat onze ankertabel nodig heeft — maar er is geen PDF-pad |
| **C4-PlantUML** | Diagram-as-code zonder onderliggend model. We winnen niets boven de mermaid die er al staat, en verliezen diffbaarheid in het document |
| **Mermaid C4** | De documentatie zegt zelf *"experimental … syntax and properties can change"*. Slecht fundament onder een document dat jaren mee moet |
| **Structurizr DSL / LikeC4** | Technisch prima, maar het zou een **derde** modelbron toevoegen naast ArchiMate en mermaid. Dat botst met "less is more", en ArchiMate kunnen we niet opgeven: de [ROSA Handreiking](https://rosa.wikixl.nl/index.php/Handreiking_voor_domeinarchitectuur) eist aanlevering in het ArchiMate-uitwisselformaat |
| **Referentie-implementaties** | Aantrekkelijk, maar VNG is er in 2024 mee gestopt na gebruikersonderzoek: *"veel tijd terwijl ze weinig gebruikt worden … liever meer tijd aan documentatie"*. Logius' goedkopere variant — voorbeelden als lint-proefkonijn, geen product — is wél het overwegen waard |

Eén optie is **niet** afgevallen maar apart gezet: [NL-ReSpec](https://github.com/Geonovum/NL-ReSpec-template) als publicatielaag. Het laat markdown intact, hoofdstukken blijven renderen op GitHub, en PDF wordt automatisch gegenereerd — de enige route die GitHub-render en PDF zonder mitsen oplost. Logius en Geonovum draaien er samen bijna honderd documenten op, met [één gedeelde automatiseringsrepo](https://github.com/Logius-standaarden/Automatisering). Dat is een besluit voor het moment waarop we een tweede releasepakket krijgen, niet voor nu.

---

## 4. Mijn voorkeur

**C als ruggengraat, A als bindweefsel, B gefaseerd — en het ArchiMate-besluit nú los trekken.**

### Waarom niet B, terwijl AMIGO dat voorschrijft

Omdat het bewijs tegen ons pleit en de methodiek ons de ruimte geeft. AMIGO-principe I1 (p.10) staat stapsgewijze overgang expliciet toe. En het onderzoek laat zien wat er gebeurt als je aan modelgedreven werken begint zonder de toolchain te kunnen dragen: SEMIC heeft het expressiefste bronformaat en de armste praktijk, en zoekt na drie jaar zelf een uitweg. Wij hebben op dit moment één persoon die het ArchiMate-model beheert en zeven scripts die niet in CI draaien. Dat is geen basis voor een generatieketen.

Wat we wél meteen doen richting AMIGO-conformiteit is goedkoop: het ArchiMate-model exporteren naar Public (dan staat het stap-1-product waar het hoort), en U4 en U7 laten verwijzen naar leidraad G2 en G4 in plaats van ze zelfstandig af te leiden. Dat is een middag werk en het maakt van eigen vindingen AMIGO-conforme invullingen.

### Waarom C als ruggengraat

Het onderzoek trok in alle drie de lijnen onafhankelijk dezelfde conclusie: een businesslaag overleeft alleen met **(a)** een ID dat elders wordt aangeroepen, **(b)** een CI-haak die faalt als de koppeling breekt, en **(c)** zichtbaarheid in de gepubliceerde output. Richting C is de enige die alle drie tegelijk invult. Haal Centraal doet dit al acht jaar en daar leeft de businesslaag nog; VNG had precies onze constructie — user story als issue, met architectuurschets die terugverwees — en [archiveerde die op 2 mei 2019](https://github.com/VNG-Realisatie/gemma-zaken/issues/65) terwijl de API-specificatie tot vandaag wekelijks commits krijgt.

Dat contrast is het scherpste argument in het hele onderzoek, en het gaat niet over gereedschap maar over of iets faalt als je het laat vallen.

### Waarom A erbij en niet in plaats daarvan

Een `.feature`-bestand toont dat een scenario werkt, maar niet welk uitgangspunt het afdekt. De ID-laag legt dat verband, en OpenFastTrace leest `.feature` als dekkingsbron — de twee richtingen sluiten letterlijk op elkaar aan. Bovendien hebben we de helft al: `I1` tot en met `I5` staan er, ongecontroleerd.

### Volgorde

| Wanneer | Wat | Waarom nu |
|---|---|---|
| **Deze week** | De zeven scripts in GitHub Actions, plus markdownlint | Grootste winst per uur in het hele onderzoek; er draait vandaag niets |
| **Deze week** | Besluit over het ArchiMate-model als aparte ADR | Het probleem is aangetoond en heeft al een keer 276 elementen gekost. Niet middelen: leg coArchi versus de pull request-workflow expliciet voor |
| **Voor de oplevering** | Eén koppelingspecificatie voorzien van eis-ID's en één happy flow als Nederlandse Gherkin — als proef, niet als uitrol | Zo weten we of de ruis in het document acceptabel is vóórdat we het overal doen |
| **Na de oplevering** | Uitrollen als de proef bevalt, plus Vale met een Nederlandse regelset uit `docs-style.mdc` | Haalt de schrijfstijlregels uit de agent-context en maakt ze voor iedereen afdwingbaar |
| **Wanneer er aanleiding is** | NL-ReSpec als publicatielaag; AsyncAPI naast OpenAPI | Bij een ROSA-scan, een tweede releasepakket, of een leverancier die het contract machinaal wil consumeren |

### Wat deze keuze níét oplost

De **vocabulairespecificatie** en de **interfacespecificatie** ontbreken; geen van de drie richtingen vult dat. Dat zijn losse gaten die inhoudelijk werk vragen. En het profiel hoort te landen in [`open-education-api/profiles`](https://github.com/open-education-api/profiles) — nu nog leeg, maar het is de duidelijkste ontbrekende schakel naar sectorborging.

---

## 5. Om zelf te bekijken vóór het besluit

Zeven dingen, ongeveer een uur, in deze volgorde:

1. **[Haal Centraal — het gepubliceerde testrapport](https://raw.githubusercontent.com/BRP-API/Haal-Centraal-BRP-bevragen/master/docs/features/index.md)** · 5 min · *Dit is richting C in productie. Kijk naar de kolommen: per functioneel domein het aantal scenario's en pass/fail. De specificatie ís de test ís de publicatie.*
2. **[TM Forum — één feature-bestand](https://raw.githubusercontent.com/tmforum-oda/oda-canvas/master/feature-definition-and-test-kit/features/UC003-F001-Expose-APIs-Create-API-Resource.feature)** · 3 min · *Let op de eerste drie regels: `@UC003`, `@UC003-F001`, `Feature: UC003-F001`. Hetzelfde ID op drie plekken. Dit is richting A en C tegelijk.*
3. **[VNG gemma-zaken, issue #65](https://github.com/VNG-Realisatie/gemma-zaken/issues/65)** · 5 min · *Een user story als issue, met een Definition of Ready die een architectuurschets eist. Precies wat wij willen. Volg dan de link naar de schets: 404. Dit is het waarschuwende voorbeeld.*
4. **[Logius API Design Rules](https://github.com/Logius-standaarden/API-Design-Rules)** · 10 min · *Kijk in `sections/designRules.md` (de norm met ID), `media/linter.yaml` (de check), `linter/testcases/` (golden tests op de vertaling zelf) en `examples/` (vijf stacks in de CI-matrix). De beste governance-keten van Nederland.*
5. **[IHE ITI.VHL](https://github.com/IHE/ITI.VHL)** · 10 min · *Zeven FSH-bestanden, één per artefactsoort, en [nul StructureDefinitions in de artefactindex](https://build.fhir.org/ig/IHE/ITI.VHL/artifacts.html). Een specificatie die vrijwel volledig businesslaag is, machineleesbaar gemaakt.*
6. **[ROSA in coArchi](https://github.com/edustandaard/rosa)** · 10 min · *Onze eigen sectorbeheerder doet model-as-code. Lees `CODINGGUIDELINES.md`: per elementtype de verplichte properties. Dat is de discipline waar wij het over hebben, en het is de referentie voor het ArchiMate-besluit.*
7. **[SEMIC Core Person, map `uml/`](https://github.com/SEMICeu/Core-Person-Vocabulary/tree/master/releases/2.1.2/uml)** · 2 min · *Een binair bestand van 4,2 MB per release. Probeer je voor te stellen hoe je hier een pull request op reviewt. Dit is waarom ik richting B nu niet aanraad.*

Voor wie dieper wil: de [AMIGO-methodiek v1.1.0](https://www.edustandaard.nl/app/uploads/2025/10/AMIGO-methodiek-1.1.0-1.pdf) is 21 pagina's; §5.4 (p.14–15) en §6 (p.16) zijn de kern. En [NED-OOAPI](https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI) laat zien hoe OKE dezelfde methodiek in dezelfde sector heeft toegepast — `doc/flow0.md` tot en met `flow6.md` mappen elke informatiestroom op concrete endpoints.

---

## 6. De vraag die voorligt

**Welke richting draagt bij OKx de koppeling tussen business en techniek: het ID, het model, of de test?**

Mijn voorstel is de test, met het ID als bindweefsel en het model gefaseerd — en het ArchiMate-besluit daarvan losgekoppeld omdat het zijn eigen urgentie heeft.

Is die keuze gemaakt, dan volgt een ADR met dit document en de drie onderzoeksverslagen als onderbouwing, en pas daarna een herstructureringsplan.
