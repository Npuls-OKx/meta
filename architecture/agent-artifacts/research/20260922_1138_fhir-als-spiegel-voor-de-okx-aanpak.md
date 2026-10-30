# FHIR als spiegel: hoe een standaard van deze schaal is opgebouwd, en wat OKx ervan kan gebruiken

Relateert aan: #253

De vraag achter dit verslag: dekken de OKx-aanpak en de beoogde deliverables de scope van een standaard op deze schaal, en welke elementen uit FHIR kunnen de huidige uitdagingen van OKx verkleinen. FHIR (HL7, zorg) dient als spiegel omdat het een uitwisselstandaard is die vanuit een vergelijkbare ambitie begon en vijftien jaar doorontwikkeling achter zich heeft.

Het verslag beslist niets. Het legt vast wat er bij FHIR staat, wat OKx heeft, waar die twee elkaar raken, en welke stappen het overwegen waard zijn. Een besluit hoort in een ADR die hiernaar terugverwijst.

## Werkwijze en bronstatus

Drie onderzoekssporen liepen in verse contexten: de opbouw van de FHIR-specificatie uit de specificatie zelf (R5, v5.0.0, plus de R6-snapshot), de ontstaansgeschiedenis en governance uit HL7-bronnen, blogs van de initiator en onafhankelijke publicaties, en een inventarisatie van de OKx-deliverables uit `Npuls-OKx/meta` en `Npuls-OKx/Public`. De volledige rapporten met alle bronlinks liggen in de sessie-scratchpad; de kern ervan staat hieronder met de bron erbij.

Wat de spiegel beperkt: de HL7 Confluence-pagina's gaven HTTP 405, waardoor de balloteringsdrempels, de acceleratorbeschrijvingen en de lijst met publieke testservers alleen via zoekresultaten bekend zijn. De wetenschappelijke publicaties over profielwildgroei gaven HTTP 403; de cijfers daaruit staan hieronder met die beperking erbij. De vergelijking met OKx steunt op de repo's zoals ze op 22 september 2026 stonden.

Waar hieronder "de spec zegt" staat, gaat het om een letterlijke uitspraak in de bron. Waar "afleiding" staat, is het een gevolgtrekking van dit verslag.

## 1. Waar FHIR vandaan komt, en hoe vergelijkbaar dat is met OKx

### 1.1 De aanleiding was een publiek geconstateerd falen

FHIR begon met een blogbericht van Grahame Grieve op 20 augustus 2011, getiteld ["HL7 needs a fresh look because V3 has failed"](https://www.healthintersections.com.au/2011/08/20/hl7-needs-a-fresh-look-because-v3-has-failed.html). De zes oorzaken die hij noemt zijn herkenbaar voor elk standaardisatietraject: het proces legde consistentie op waar de inconsistentie buiten de standaard lag, technologieneutraliteit maakte implementeren duurder, alle modellering moest vooraf ("the price of change is too scary"), en het referentiemodel leverde "semantic interoperability but not clinical interoperability".

De omkering die daarop volgde is de kern van het ontwerp: in v3 was interoperabiliteit "a transform away from the RIM"; in het voorstel geldt ["interoperability is the focus, and the RIM is a transform away"](https://www.healthintersections.com.au/2011/08/20/a-comparison-of-v3-and-rfh.html). De vuistregel binnen het kernteam was dat software-ontwikkelaars het in een weekend werkend moesten krijgen ([Firely](https://fire.ly/blog/the-early-days-of-fhir/)).

### 1.2 De vergelijking met OKx, punt voor punt

| Aspect | FHIR | OKx |
|---|---|---|
| Aanleiding | Falen van een voorganger (v3), vastgesteld door de gemeenschap zelf | Opdracht binnen het Npuls-groeifondsprogramma, pijler Leren zonder Drempels, met drie projectdoelen (opdracht.md) |
| Startpunt | Voorstel van een individu (18 augustus 2011), overgenomen als HL7-werkitem op 11 september 2011 | Programmaopdracht met kernteam, kerngroep techniek en adviesgroep |
| Verhouding tot het bestaande referentiemodel | RIM blijft bestaan, maar komt achter de uitwisseling te liggen | MORA blijft leidend: "Deze repo is geen directe wijziging van MORA" (meta/README.md) |
| Domeinbreedte | Alle zorg wereldwijd, 157 resources in R5 | Onderwijslogistiek, mbo eerst, leerroutes 1 tot 3, 66 objecttypen in het informatiemodel v0.1 |
| Semantiek | Grotendeels extern (SNOMED CT, LOINC, ICD); FHIR levert de structuur en de bindingen | Zelf ontwikkeld: begrippenlijst v0.2 (73 begrippen) en informatiemodel v0.1, gelegd naast MORA, ROSA-KOI en HORA |
| Governance | HL7 International, ANSI-geaccrediteerde ballotage, ruim 4.000 leden in meer dan 50 landen | Kerngroep techniek en SI-team, AMIGO als route (OKx-AP03), Edustandaard-architectuurraad als bestemming |
| Licentie | CC0, vrij te gebruiken | Publieke repository, open |
| Financiering | Contributies, vrijwilligers, betaalde acceleratorprogramma's (500 tot 50.000 dollar per jaar bij Vulcan) | Groeifondsprogramma met einddatum |
| Adoptiedwang | Wetgeving en certificering: ONC-criterium 170.315(g)(10) verplicht FHIR 4.0.1 en US Core; EHDS-verordening 2025/327 in Europa | Vrijwillig, via koploperinstellingen en koploperleveranciers, met BOPSI als implementatiepad |
| Doorlooptijd | Eerste implementeerbare versie na drie jaar (DSTU1, 2014), volledig normatief na vijftien jaar (R6, in ballotage 2026) | Eerste releasepakket koppelvlakspecificatie v0.0.1 in augustus 2026, bouw bij leveranciers voorzien in Q1 2027 |

### 1.3 Waar de vergelijking houdt, en waar zij wringt

Houdt: beide standaarden zetten implementeerbaarheid voorop, beide werken met een 80/20-afbakening, en beide verhouden zich tot een bestaand referentiemodel dat zij intact laten. De formulering "de RIM is een transformatie verderop" en de OKx-lijn dat MORA leidend blijft terwijl OKx de uitwisseling beschrijft, zijn dezelfde beweging (afleiding).

Wringt op drie punten, en dat bepaalt wat overneembaar is:

1. **FHIR standaardiseert de uitwisseling bovenop bestaande semantiek; OKx bouwt de semantiek zelf.** De zorg had codestelsels en een referentiemodel; het onderwijs heeft MORA en ROSA, maar het begrippenkader voor flexibel onderwijs is juist wat OKx aan het leggen is (milestone 7 telt 18 open issues over semantiek). Het zwaartepunt van het werk ligt daardoor bij OKx een laag hoger.
2. **FHIR heeft vijftien jaar en een wettelijke stok; OKx heeft een programmaperiode en vrijwillige adoptie.** Wat FHIR via certificering afdwong, moet OKx via bruikbaarheid en afspraken bereiken. De Nederlandse zorgroute laat zien dat het ook anders kan: zibs en nl-core worden centraal gevalideerd, en pas de Wegiz met NEN-normen legt het wettelijk vast.
3. **FHIR is een platformspecificatie die per context wordt aangescherpt; OKx specificeert per koppeling.** De spec zegt dat zij "a common platform or foundation" biedt waarop verschillende oplossingen worden gebouwd. OKx kiest de omgekeerde volgorde: eerst een concrete koppeling (OC naar P&R, OC naar SIS, OC naar LMS) volledig uitwerken. Dat is verdedigd in de AMIGO-gat-analyse, met de beeindigde UWLR-werkgroep als les dat een brede "one size fits all"-afspraak onwerkbaar bleek.

## 2. Hoe de FHIR-specificatie is opgebouwd

De spec deelt zichzelf op drie manieren in, wat op zichzelf een observatie is: modules in vijf niveaus (Infrastructure, Content, Reasoning), vier componenten voor de architect (Information Model, Constraints, Terminology, Usage) en zes lagen voor de resources zelf. De vuistregel voor verwijzingen luidt dat resources verwijzen binnen dezelfde laag of hoger.

De bouwdelen die er voor deze vergelijking toe doen:

| Bouwdeel | Wat het is |
|---|---|
| Resource | "The basic building block in FHIR is a Resource. All exchangeable content is defined as a resource." 157 stuks in R5 |
| Datatypes en references | Vijf categorieen datatypes; verwijzingen bouwen een web van informatie, uitdrukkelijk niet transitief |
| Profiel (StructureDefinition) | Gebruiksregels bovenop een resource, met harde grenzen: geen nieuwe elementen, geen defaults, en "It must be safe to process a resource without knowing the profile" |
| ImplementationGuide | De verzameling regels plus documentatie voor een context, computeerbaar zodat validators ertegen kunnen valideren |
| CapabilityStatement | Wat een systeem daadwerkelijk ondersteunt, in drie vormen: een concrete installatie, een softwareproduct, en een gewenste oplossing (bruikbaar in een aanbesteding) |
| Terminologie | CodeSystem, ValueSet en ConceptMap, met vier bindingsterktes (required, extensible, preferred, example) |
| Volwassenheid (FMM) | Een schaal 0 tot 5 plus normatief, met telbare criteria per trede |
| Extensies | Elk element mag extensies dragen; onbekende extensies zijn geen reden tot afwijzen; modifierExtension kent harde regels |
| Validatie en testen | Acht validatie-aspecten, zes methoden, TestScript als uitvoerbaar testkader |

Drie uitspraken uit de spec zijn voor OKx direct relevant (de tekst zelf, geen afleiding):

- Over conformiteit: ["Assertions of conformance to FHIR in the absense of a CapabilityStatement have little meaning because they cannot be tested/verified."](https://www.hl7.org/fhir/conformance-rules.html)
- Over de grens van validatie: ["Note that all these validation methods are incomplete; they can only validate the computable aspects of conformance."](https://www.hl7.org/fhir/validation.html), met Postel als leidraad: conservatief in wat een systeem verstuurt, ruimhartig in wat het accepteert.
- Over extensies: ["Applications should not reject resources merely because they contain extensions"](https://www.hl7.org/fhir/extensibility.html), en tegelijk: ["there is strict governance applied to the definition and use of extensions"](https://www.hl7.org/fhir/extensibility.html).

### 2.1 Het volwassenheidsmodel, omdat dat de meest overneembare vondst is

FMM kent telbare criteria per trede: FMM 2 vraagt interoperabiliteitstests met minimaal drie onafhankelijk ontwikkelde systemen en minstens 80 procent van de kerngegevenselementen; FMM 3 vraagt een balloteringsronde met minimaal tien implementeerreacties uit minstens drie organisaties; FMM 5 vraagt vijf onafhankelijke productiesystemen in meer dan een land. De koppeling met stabiliteit staat er expliciet bij: ["the higher the maturity level, the more controls are enforced to restrict breaking changes"](https://www.hl7.org/fhir/versions.html).

Daarnaast draagt elke pagina haar eigen status (Normative, Trial Use, Draft, Informative, Deprecated), en gelden de compatibiliteitsregels pas zodra een artefact normatief is.

## 3. De bouwdelen van FHIR naast de OKx-deliverables

Per bouwdeel: heeft OKx dit, in welke vorm, en wat ontbreekt. "Aanwezig" betekent dat er een artefact is dat dezelfde functie vervult, niet dat het even ver is.

| FHIR-bouwdeel | Bij OKx aanwezig | In welke vorm | Wat ontbreekt |
|---|---|---|---|
| Scenario dat de scope afbakent | Ja, sterker dan FHIR | Kaderscenario's per leerroute met persona's; leerroute 1 volledig, 2 en 3 in overdracht | Zes van de negen leerroutes; de verbinding met de requirementsboom (#143) |
| Informatiemodel | Ja | Informatiemodel v0.1: 66 objecttypen, 156 relaties, 7 begrippenfamilies, MIM-niveau 2 | Bekrachtiging door de kerngroep; 17 ontwerpkeuzes staan op "Voorstel" |
| Semantische bouwstenen met herkomst | Ja, sterker dan FHIR | Begrippenlijst v0.2: 73 begrippen, elk gelegd naast MORA, ROSA-KOI en HORA | 33 begrippen zonder definitie; HORA overal "nog niet onderzocht" |
| Berichtstructuur | Ja | 24 JSON Schema's (draft 2020-12) met `DutchName` per veld, plus voorbeeldpayloads | Drie payloadschema's nog niet uitgewerkt |
| Interactiepatroon | Ja | 3 interactiepatroondocumenten, 19 interacties, patroontaal uit Enterprise Integration Patterns | Vier van de zeven applicatiecomponenten hebben nog geen endpointtabel |
| Interfacespecificatie (OAS) | Nee | Verwijzing naar `Npuls-OKx/specification` | De OpenAPI-specificatie zelf; de AMIGO-gat-analyse noteerde al "nul OAS-bestanden in Public" |
| Vocabulaire en waardenlijsten | Deels | Enumeraties binnen de schema's; open lijsten als `$comment`; knelpuntcodes als "aanzet" | Waardenlijsten als zelfstandig artefact; een equivalent van bindingsterkte |
| Conformance-verklaring per component | Nee | Applicatiecomponentdocumenten beschrijven endpoints en events | Een verklaring van wat een implementatie ondersteunt, en dus iets om tegen te toetsen |
| Profiel- of variantmechanisme | Deels | Gebruiksprofielen per koppeling, open lijsten, U11 (volledige structuur naast delta), U5 (kanaalvrijheid) | Governance op uitbreidingen: wie beoordeelt, waar staat het, hoe reageert een ontvanger op onbekende velden |
| Volwassenheidsschaal met criteria | Deels | Statuslabels per artefact ("Voorstel", "Alfa en indicatief", "concept"), semver per artefact, U10 | Telbare criteria per trede, en daarmee een antwoord op "waar kan een leverancier op bouwen" |
| Versie- en compatibiliteitsregels | Deels | Semver per specificatie, `changeClass` met vijf waarden, `geldigVanaf`/`geldigTot`, "deactiveren, niet verwijderen" | De vraag uit #101: wat gebeurt er met lopende inschrijvingen bij een nieuwe versie |
| Validatie | Ja, voor de eigen artefacten | CI in Public op elke pull request (links, conventies, drift, releasebouw); in meta validatiescripts zonder workflow (#203) | Validatie van een payload van een leverancier tegen de specificatie |
| Uitvoerbare tests | Nee | Unittests voor het eigen gereedschap; testpersona en given-when-then voor scripts | Testgevallen voor de koppeling zelf; #66 staat open zonder milestone |
| Praktijktest met meerdere partijen | In voorbereiding | Vier koploperleveranciers en zes tot acht koploperinstellingen; bouw voorzien Q1 2027 | Een herhaalde testvorm met terugkoppeling naar de specificatie |
| Besluitvastlegging | Ja, sterker dan FHIR | 26 ADR's met status en vervanging, plus 13 principes en 11 uitgangspunten | Alle ADR's staan op "voorstel" |

### 3.2 Het dekkingsoordeel

De bovenkant van de keten is bij OKx sterker uitgewerkt dan bij FHIR: kaderscenario's met persona's, een begrippenlijst met herkomst per begrip en expliciete ontwerpkeuzes zijn artefacten die FHIR in deze vorm niet kent. FHIR begint bij de resource en laat de semantiek aan externe codestelsels.

De onderkant ontbreekt of is nog aanzet: conformance-verklaring, waardenlijsten, uitvoerbare tests en de interfacespecificatie. Dat is precies hetzelfde gat dat de AMIGO-gat-analyse in augustus 2026 vond (stap 4 ongebundeld, vocabulairespecificatie ontbreekt, stap 6 als product afwezig). Twee onafhankelijke spiegels wijzen dus dezelfde drie gaten aan, wat de kans klein maakt dat het aan de meetlat ligt (afleiding).

Antwoord op de vraag of de deliverables de scope van een standaard op deze schaal dekken: voor het gedeelte dat betekenis en samenhang vastlegt wel, en dat deel is verder dan gebruikelijk voor een standaard van deze leeftijd. Voor het gedeelte dat een implementatie toetsbaar maakt nog niet, en dat is het deel waar leveranciers zich op vastleggen.

## 4. Wat dit betekent voor de huidige uitdagingen van OKx

De inventarisatie noemde zeven terugkerende knelpunten. Vijf ervan raken direct aan iets dat FHIR heeft opgelost of juist expliciet als open probleem benoemt.

| Uitdaging bij OKx | Wat de spiegel laat zien |
|---|---|
| Discussie tussen 80 procent volwaardige specificaties en een MVP-benadering, met de waarschuwing dat percentages onzekerheid uitstralen (meeting 13 juli) | FMM vervangt het percentage door telbare criteria per artefact. Een leverancier leest dan niet "80 procent af" maar "dit deel is getest met drie systemen, dat deel nog niet" |
| Testen van koppelingen is een open vraag (#66) | FHIR koppelt testen aan volwassenheid: FMM 2 vereist een interoperabiliteitstest met drie onafhankelijke systemen, en connectathons voeden de specificatie direct terug |
| Versionering tegenover lopende inschrijvingen (#101) | FHIR maakt compatibiliteitsregels pas hard zodra iets normatief is, en houdt de rest bewust wijzigbaar. Voor R6 is de lijn: eerst onvolwassen delen uit de kern halen, dan de kern vastzetten |
| Het specificatiedocument is met 50 tot 60 pagina's te omvangrijk (meeting 14 juli) | FHIR houdt de kernspecificatie bewust beknopt, verplaatst ondersteunend materiaal naar buiten en geeft een expliciete leesvolgorde. Vanaf R5 zijn zelfs de extensies uit de kern gehaald |
| Instellingsvariatie en dieptereductie (#97, complexiteitsreductie 26 juni) | Het extensiemechanisme met governance is precies daarvoor gebouwd: de kern klein houden en lokale eisen apart opvangen, met de erkenning dat extensies zelf ook een drempel vormen |
| Semantiek nog in beweging (milestone 7) | FHIR laat semantiek grotendeels buiten de standaard. Dat is voor OKx geen route, maar het scheidingsmodel uit de Nederlandse zorg wel: zibs als semantische laag, profielen als technische laag, elk met een eigen beheerder |

Wat FHIR niet oplost en OKx dus zelf moet dragen: kennis blijft de grootste gemelde belemmering (75 procent van de respondenten in de enquete van 2026, vier jaar op rij, boven investeringskosten en onduidelijke regelgeving). Een betere specificatie verkleint dat maar deels.

## 5. Aanbevelingen

Elke aanbeveling staat met de afweging erbij: wat het kost, wat het oplevert, en wat ertegen pleit.

### 5.1 Kandidaat voor overname

**A1. Een volwassenheidsschaal met telbare criteria, per artefact.** Nu draagt elk artefact een label ("Voorstel", "Alfa en indicatief", "concept") zonder criterium erachter. Een schaal van vier tredes met telbare eisen (bijvoorbeeld: beschreven; beoordeeld door de kerngroep; met minstens twee leveranciers doorgesproken; in twee onafhankelijke implementaties getest) maakt zichtbaar waarop een partij kan bouwen.
*Kost*: een afspraak in de kerngroep techniek en een veld in `release.json` en op de artefacten zelf. *Levert*: het einde van de percentagediscussie, en een gedeelde taal met leveranciers over bouwbaarheid. *Tegen*: elke trede vraagt bewijs, en bewijs verzamelen kost tijd die nu naar inhoud gaat. *Afweging*: begin met de schaal alleen op de payloadschema's en de interactiepatronen, waar leveranciers zich op vastleggen.

**A2. Een conformance-verklaring per referentiecomponent.** FHIR's CapabilityStatement in de vorm "Requirements" is letterlijk bedoeld voor een aanbesteding: dit is wat wij van een systeem verwachten. OKx heeft de bouwstenen al (applicatiecomponentdocumenten met endpoints en events); de stap is een machineleesbare verklaring per component van welke koppelingen en interacties worden ondersteund.
*Kost*: een schema plus een verklaring per component. *Levert*: iets om tegen te toetsen, wat #66 concreet maakt, en een instrument voor instellingen bij inkoop. *Tegen*: spanning met U1 ("indicatief en onderbouwend, niet voorschrijvend"). *Afweging*: een verklaring beschrijft wat een leverancier zelf zegt te ondersteunen en schrijft niets voor; de norm blijft bij de leverancier, de toetsbaarheid komt erbij.

**A3. Waardenlijsten als zelfstandig artefact, met een expliciete bindingsterkte.** FHIR's vier sterktes (required, extensible, preferred, example) zijn de knop waarmee vrijheid per veld wordt geregeld. OKx heeft die vrijheid nu impliciet in `$comment`-teksten bij open lijsten.
*Kost*: een codelijstmap in Public, verwijzingen vanuit de schema's, en per lijst een keuze over de sterkte. *Levert*: het ontbrekende AMIGO-onderdeel (vocabulairespecificatie), en een einde aan de vraag of een instelling een eigen waarde mag toevoegen. *Tegen*: waardenlijsten vragen beheer, en beheer vraagt een eigenaar. *Afweging*: begin met de lijsten die nu al enumeraties zijn in de schema's; die hebben de facto al een beheerder.

**A4. Een afspraak over onbekende velden.** FHIR legt vast dat een ontvanger een bericht niet afwijst om de enkele aanwezigheid van een extensie, en dat onbekende elementen behouden blijven. Voor OKx is het equivalent een regel bij de schema's over hoe een ontvanger omgaat met velden die zij niet kent.
*Kost*: een regel in de uitgangspunten en in `Datamodelschema's/README.md`. *Levert*: instellingsvariatie zonder dat de koppeling breekt, en een antwoord op de dieptereductie-vraag (#97). *Tegen*: ruimhartig ontvangen maakt fouten later zichtbaar. *Afweging*: Postel's leidraad met een expliciete uitzondering voor velden die de betekenis wijzigen, zoals FHIR met modifierExtension doet.

**A5. Een herhaalde praktijktest met de koplopers, met terugkoppeling naar de specificatie.** De connectathon-vorm is bij FHIR geen bijzaak maar onderdeel van het volwassenheidsmodel.
*Kost*: organisatie van een testronde rond de bouw in Q1 2027. *Levert*: bewijs voor de volwassenheidsschaal uit A1, en vroege ontdekking van interpretatieverschillen. *Tegen*: leveranciers zijn schaars in tijd. *Afweging*: koppel de testronde aan het moment waarop zij toch bouwen.

### 5.2 Eerst verder onderzoeken

**B1. Wat is het OKx-equivalent van een profiel, en wie valideert het.** De zorgsector in Nederland scheidt de semantische laag (zibs, beheer bij Nictiz) van de technische laag (FHIR-profielen, validatie bij HL7 Nederland), juist om wildgroei te voorkomen. OKx heeft beide lagen in eigen hand (begrippenlijst en informatiemodel tegenover schema's). Onderzoeksvraag: helpt die scheiding hier, en wie zou de validerende partij zijn.

**B2. Hoe groot het profielrisico is.** Onafhankelijk onderzoek stelt vast dat conformiteit aan een profiel geen uitwisselbaarheid tussen twee partijen garandeert, en dat de 80/20-regel in de praktijk eerder 65/35 is (cijfers uit zoekresultaten over de publicatie; de volledige tekst was niet op te halen). Voor OKx is dat een waarschuwing bij elke vorm van gebruiksprofielen. Onderzoeksvraag: welke variatie laten de huidige drie gebruiksprofielen al toe, en wat gebeurt er als vier leveranciers die elk anders invullen.

**B3. Welke testvorm past.** FHIR kiest TestScript (uitvoerbaar, FMM 2, status Draft); Haal Centraal publiceert 4818 Gherkin-scenario's als product (vastgesteld in het eerdere praktijkonderzoek). Onderzoeksvraag: welke vorm past bij de OKx-schaal en bij wat leveranciers al gebruiken.

**B4. Normatief maken als instrument.** R6 zet het hele kernpakket normatief en haalt onvoldoende volwassen delen eruit. Onderzoeksvraag: welk deel van de OKx-specificatie zou een vergelijkbare vastzetting aankunnen, en wat zou er dan uit moeten.

### 5.3 Bewust laten liggen, met reden

- **De granulariteit van het resourcemodel.** 157 resources en 1239 zoekparameters horen bij een mondiale standaard voor een hele sector. De OKx-lijn is juist complexiteitsreductie ("een eenvoudig, iteratief model in drie tot vijf stappen dat scholen kunnen begrijpen", meeting 26 juni). Overnemen van die granulariteit werkt die lijn tegen.
- **Meerdere uitwisselparadigma's naast elkaar.** FHIR kent er zes, waarvan messaging, documents en services laag-volwassen zijn en services zelfs buiten de conformiteitsclaim vallen. OKx heeft met notify-then-pull (U4) en kanaalvrijheid (U5) een werkbare keuze gemaakt.
- **Een eigen ballotage- en accreditatieproces.** OKx heeft met AMIGO en de Edustandaard-architectuurraad een bestaande route (OKx-AP03). Een tweede consensusproces daarnaast zou dubbelen.
- **Een eigen pakket- of profielregister.** Dat is een antwoord op schaal die OKx niet heeft; de gecureerde HL7-lijst telt 128 gidsen tegenover 1319 publieke pakketten uit 602 projecten, wat laat zien hoe snel zoiets zijn eigen beheerlast schept.

## 6. Onderzoeksagenda en evaluatiemomenten

| Wanneer | Wat | Waarom dan |
|---|---|---|
| Kerngroep techniek 30 september 2026 | A1 (volwassenheidsschaal) als voorstel voorleggen, samen met de uitkomst van de voorbeelduitwerking | De kerngroep bekrachtigt op dat moment toch al het informatiemodel; de schaal bepaalt wat "bekrachtigd" betekent |
| Bij het vaststellen van de payloads | A3 (waardenlijsten) en A4 (onbekende velden) | Zolang de schema's "alfa en indicatief" zijn, is een codelijst goedkoop te introduceren |
| Voor de bouw in Q1 2027 | A2 (conformance-verklaring) en A5 (praktijktest) | Leveranciers leggen zich dan vast; een verklaring en een testronde horen bij dat moment |
| Na de eerste implementaties | B2 (profielrisico) en B4 (normatief maken) | Beide vragen praktijkervaring die er nu nog niet is |
| Doorlopend | B1 (wie valideert) en B3 (testvorm) | Beide raken aan beheer na het programma, wat eigen besluitvorming vraagt |

Standaarden die dezelfde spiegelbehandeling verdienen, in volgorde van verwachte opbrengst: **de Nederlandse zorgketen** (zibs, nl-core, MedMij, Twiin, Wegiz) omdat die het dichtst bij de OKx-situatie ligt qua landelijke regie en wettelijke verankering; **1EdTech** (Edu-API, OneRoster, CLR) omdat dat hetzelfde domein raakt; **Haal Centraal en Logius** omdat die de Nederlandse praktijk van toetsbare specificaties tonen; en **OOAPI en OEAPI** in hun eigen governance, omdat OKx daar direct op aansluit.

## 7. Wat dit verslag niet heeft kunnen vaststellen

- De balloteringsdrempels, het acceleratorprogramma en de lijst met publieke testservers van HL7 staan op Confluence, dat HTTP 405 gaf. Die punten rusten op zoekresultaten.
- De onderzoekscijfers over profielwildgroei (bijna 3000 profielen uit 125 gidsen, 49 procent Extension en Observation, 33 tot 38 procent nieuwe data-elementen) komen uit zoekresultaten over de publicatie; de volledige tekst gaf HTTP 403.
- Een totaalbedrag voor de ontwikkeling van FHIR is in geen enkele bron gevonden, en daarmee ontbreekt een kostenvergelijking met een programma als OKx.
- Het aantal FHIR-implementatiegidsen wereldwijd is niet vast te stellen; het gecureerde register telt er 128, een commercieel platform telt 1319 pakketten.
- De vergelijking met OKx steunt op de repository-inhoud van 22 september 2026. Artefacten die daarna verschijnen, kunnen gaten dichten die hier open staan.
- Dit verslag heeft de OKx-schema's niet inhoudelijk vergeleken met FHIR-resources. De vergelijking gaat over de opbouw van een specificatie, niet over de modellering van een domein.
