# AMIGO: voorgeschreven producten per stap, en wat OKx daarvan heeft

Relateert aan: #130

Aanleiding: de businesskant en de techniekkant van OKx hangen los van elkaar, en bij het opstellen van een herstructureringsplan bleek dat we mapindelingen aan het bedenken waren zonder te weten wat AMIGO — de methodiek waaraan we ons via [OKx-AP03](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/principes/principes.md) hebben verbonden — eigenlijk voorschrijft. Dit verslag legt dat vast op basis van de bron, en zet er onze eigen artefacten naast.

## Bronstatus

De AMIGO-methodiek is een PDF die niet via een gewone fetch te lezen was; de tekst is uit de PDF-streams gehaald. Bron: **AMIGO-methodiek v1.1.0, "Methodiek om middels het Edustandaard Lagenmodel te komen tot bouwbare uitwisselspecificaties", status vastgesteld (Architectuurraad 16-10-2025), Bureau Edustandaard / ROSA Beheerteam, 21 pagina's** — <https://www.edustandaard.nl/app/uploads/2025/10/AMIGO-methodiek-1.1.0-1.pdf>. Paginanummers hieronder zijn die uit de PDF-koptekst.

Niet bereikbaar (403/404): `edustandaard.nl/afspraken/`, `/standaarden/afspraken/`, `/afspraken/uitleg-filters/`, `/onze-werkwijze/`.

## 1. Twee lijsten die niet door elkaar mogen lopen

AMIGO kent **vijf onderdelen van de specificatie** (het product) en **zes stappen** (het proces). Ze corresponderen niet één-op-één: stap 2 en stap 4 hebben geen eigen onderdeel in de vijf.

De vijf onderdelen, letterlijk (§3, p.7):

> *"Onderdelen van zo'n specificatie zijn: **Scenariobeschrijving**: een situatiebeschrijving waaruit blijkt welke gegevensstromen wel en welke niet binnen scope van de beoogde gegevensuitwisseling vallen · **Berichtspecificatie**: welke gegevens worden uitgewisseld (structuur, constraints, syntax) · **Vocabulairespecificatie/-selectie**: welke waardenlijsten worden gehanteerd · **Interactiespecificatie**: hoe de gegevens worden uitgewisseld · **Interfacespecificatie**: welke endpoints er zijn en hoe die aangeroepen kunnen worden"*

## 2. De zes stappen, met voorgeschreven product en modeltaal

Uit §6 *Werken met AMIGO*, p.16.

| # | Stap (AMIGO-term) | Voorgeschreven product | Modeltaal, letterlijk |
|---|---|---|---|
| 1 | **Scenario-analyse** | *"afbakening van de scope"*, met antwoord op: welke systemen en partijen zijn betrokken, hoe lopen de gegevensstromen, welke gegevens gaan van A naar B, en in welke volgorde | *"(vorm: **ArchiMate-model** o.b.v. referentiecomponenten en informatieobjecten)"*; §6.1 p.17 voegt **gegevensstromen** toe |
| 2 | **Gegevensanalyse** | *"logisch model van uit te wisselen gegevens, o.b.v. selectie uit (en eventueel aanvulling op) generieke AMIGO-gegevensmodellen"* plus *"selectie van toe te passen vocabulaires / waardenlijsten"*; §6.2 p.17 noemt het product **uitwisselingsgegevensmodel** | *"(vorm: **UML-klassendiagram**)"* |
| 3 | **Interactie-analyse** | *"Specificatie van interactie tussen de betrokken systemen / partijen o.b.v. transactiepatronen, inclusief inhoud van notificatie-, vraag- en antwoordberichten"* | *"(vorm: **UML-sequencediagrammen plus UML-klassendiagrammen per bericht**)"* |
| 4 | **Technologie-/paradigmakeuze** | *"Keuze tussen SOAP en/of REST + rationale/afweging"* | geen modeltaal genoemd |
| 5 | **Berichtspecificatie** | *"Technische specificatie van berichten (syntax)"* | *"(**mogelijke** vormen: XSD, JSON Schema, VDEX, XSLT, voorbeeld-XML, voorbeeld-JSON)"* |
| 6 | **Interfacespecificatie** | *"Technische API-/endpointspecificatie"* | *"(**mogelijke** vormen: WSDL, OAS)"* |

**Let op de asymmetrie in dwingendheid.** Stap 1 tot en met 3 schrijven `"vorm:"` (enkelvoud, één taal). Stap 5 en 6 schrijven `"mogelijke vormen:"` (meervoud, niet-limitatief). Dat is een letterlijk tekstueel verschil in de bron, geen interpretatie — en het betekent dat onze vrijheid aan de technische kant groter is dan aan de analysekant.

Over de samenhang, p.16: *"De stappen kennen onderlinge verbanden en zijn iteratief; de uitkomsten uit de verschillende analyses kunnen elkaar beïnvloeden."* En: ontbrekende of tekortschietende standaarden worden *"ingebracht bij de betreffende werkgroepen"*, niet lokaal opgelost.

## 3. De normatieve kern: modelgedreven met traceerbaarheid

Dit is de scherpste uitspraak in het document, en ze staat niet op de webpagina. §5.4, p.15:

> *"De specificaties binnen AMIGO worden **modelgedreven** ontwikkeld: 1. Er is een strikte relatie tussen conceptuele informatiemodellen en logische gegevensmodellen. Ieder logisch model is een nadere uitwerking van een conceptueel model. Alle entiteiten uit logische modellen refereren aan entiteiten uit een conceptueel model. 2. **Technische modellen worden gegenereerd uit logische gegevensmodellen** d.m.v. gestructureerde transformaties. Dit houdt in dat **wijzigingen in technische modellen altijd op logisch niveau worden aangevangen**. […] Hiertoe worden tussen de modellen **traceerbaarheidsrelaties** aangebracht."*

Dit is precies het antwoord op de vraag "hoe verbinden we business en techniek", en het antwoord van de methodiek waaraan we ons hebben verbonden is: **via een logisch model, met generatie omlaag en traceerbaarheidsrelaties ertussen**. OKx doet dit op dit moment omgekeerd — de technische schema's worden met de hand geschreven en er worden leesweergaven uit gegenereerd.

Bijbehorend kader:

- **§5.1, p.13** — vier modelniveaus conform **MIM** (Metamodel Informatie Modellering, <https://docs.geostandaarden.nl/mim/mim/>): begrippenmodellen, conceptuele informatiemodellen, logische gegevensmodellen, technische gegevensmodellen.
- **§5.2, p.13** — drie inhoudsgebieden: Onderwijsbreed, Toepassingsgebied (*"komt overeen met de scope van een Ketenprocesmodel of Keteninrichtingsscenario uit ROSA"*) en Inrichting.
- **§5.3, p.13** — de eenheid: *"een specifieke gegevensuitwisseling […] tussen twee of meer ketenpartners binnen een bepaald toepassingsgebied."*
- **§5.4, p.14** — modellenmatrix; voor inrichtingsgegevensmodellen en berichtspecificaties *"sluiten we aan bij het metamodel dat hiervoor door **VNG** wordt gehanteerd."*
- **§7.6, p.21** — de logische gegevensmodellen zijn gepubliceerd in ROSA (<https://rosa.wikixl.nl/index.php/ROSA_Logische_gegevensmodellen>); *"de inhoudelijke governance van deze modellen ligt bij de Architectuurraad Edustandaard."*

## 4. Leidraden die wij zelfstandig opnieuw hebben afgeleid

Twee AMIGO-leidraden staan inhoudelijk al in onze uitgangspunten, zonder dat we de bron noemen:

| AMIGO | OKx-equivalent |
|---|---|
| **G2, p.11** — *"Aanbiedende partijen kunnen hun afnemers door middel van een notificatie berichten dat ze het initiatief kunnen nemen […] zonder deze gegevens daadwerkelijk te versturen. De afnemende partij reageert, op eigen gelegenheid, met een verzoek om gegevens."* | U4 notify-then-pull, en ADR 0020 |
| **G4, p.12** — volledige sets én delta's toegestaan; *"Gegevenssets bevatten unieke en stabiele identificerende kenmerken ('identifier') en versie-informatie."* | U7 sleutelconventie, en de lifecycle-uitwerking |
| **G1, p.11** — interacties opgebouwd uit **Edukoppeling-transactiepatronen**; §7.1 p.19–20 noemt Request-Response, Melding-Bevestiging en Asynchrone uitwisseling | Geen equivalent; Edukoppeling komt in `Public` nergens voor |

Dat we hetzelfde hebben afgeleid is geen fout, maar wel gemiste borging: door naar G2 en G4 te verwijzen wordt het een AMIGO-conforme invulling in plaats van een eigen vinding.

Verder in hoofdstuk 7 (p.19–21): identificatie en autorisatie, informatiebeveiliging via het Certificeringsschema met BIV-classificatie, mandatering en routering via OSR *of* decentraal (*"zoals dat in het afsprakenstelsel Edu-V en ook OKE wordt toegepast"*), en ECKiD, Nummervoorziening en eduID. Geen van deze bouwblokken komt in `Public` voor.

## 5. AMIGO naast MOKA, MORA, ROSA en NORA

| Kader | Schrijft artefacttypes voor? | Bron |
|---|---|---|
| **AMIGO** | **Ja, expliciet.** Vijf specificatie-onderdelen en zes stappen met per stap product en modeltaal | PDF v1.1.0 p.7 en p.16; <https://www.edustandaard.nl/amigo/aanpak/> |
| **ROSA** | Nee — levert bouwstenen (KOI, logische gegevensmodellen, keteninrichtingsscenario's) en ontwerpkaders | <https://rosa.wikixl.nl/index.php/ROSA_metamodel> |
| **MORA** | Nee — levert referentiebouwstenen en drie uitgewerkte koppelvlakken als voorbeeld, geen sjabloon | <https://mora.mbodigitaal.nl/index.php/MORA_metamodel> |
| **MOKA** | Deels, en in ontwikkeling | <https://mora.mbodigitaal.nl/index.php/Koppelvlak_Perspectief_MOKA> |
| **NORA** | Nee — vijflaagsmodel en principes, geen verplichte deliverables voor dochterarchitecturen | <https://www.noraonline.nl/wiki/NORA_dochters> |

**Over MOKA past een waarschuwing.** Publiek staat er weinig: de enige opgehaalde MOKA-pagina beschrijft één perspectief (*"Beschrijft op conceptueel niveau welke informatieobjecten tussen referentiecomponenten (applicaties) worden uitgewisseld zonder procesmatige volgorde"*, detailniveau *"Niveau 3: Contextueel"*, gebruikstype *"Keteninrichtingssjabloon"*), zonder metamodel, viewlijst of modeltaal. Het MOKA-werkplan van 2024 zette "Principes, Koppelvlakken aanpak, Overzichtsplaat, Datamodel, Website, Scan aanpak" nog op de planning en noemde AMIGO daarbij niet (<https://mbodigitaal.nl/2024/02/update-over-moka-en-mora/>).

De gedetailleerde MOKA-opbouw die wij hanteren komt uit ons eigen `moka-koppelvlakspecificaties/Template/doc/KoppelvlakSpecificatieTemplate.md` (auteur: "MOKA Werkgroep"). Dat template schrijft wél een volledige artefactenset voor. **Behandel dat als werkgroepsproduct, niet als vastgestelde sectorstandaard**, zolang er geen publieke MOKA-publicatie tegenover staat.

Het scherpste stuk over de samenhang staat op de ROSA-wiki (<https://rosa.wikixl.nl/index.php/Adviesdocument_samenhang_koppelvlakkenarchitectuur>): *"In de MORA worden bijvoorbeeld koppelvlakken op een hoger, referentieniveau uitgewerkt, terwijl in de MOKA een meer concrete uitwerking plaatsvindt"* en *"Er is geen eenduidige strategie en samenhangende semantiek voor het modelleren van koppelvlakken binnen het onderwijs."* Het advies is bredere toepassing van AMIGO met een **comply or explain**-aanpak.

**AMIGO is in ROSA geregistreerd als Requirement met gebruiksadvies "Verplicht"** (<https://rosa.wikixl.nl/index.php/Id-2efe8b23fa1041ab955597e8f684c1d5>). Dat is een hardere onderbouwing onder OKx-AP03 dan de webpagina die daar nu wordt aangehaald.

## 6. De vorm van een afsprakenset

**Wat AMIGO zegt** (§1, p.5): *"Met AMIGO komen ketenpartijen stapsgewijs tot een verzameling afspraken (afsprakenset) over de uitwisseling van gegevens in een specifiek toepassingsgebied."* De onderdelen zijn de vijf uit p.7. **Verder zegt AMIGO niets over publicatievorm, versionering, repo-indeling, conformiteitseisen of het beheer van de afsprakenset zelf.**

**Wat de praktijk laat zien** — drie publicatiemodellen naast elkaar:

| Afsprakenset | Publicatievorm | Beheer |
|---|---|---|
| **UWLR 2.3** | Alleen PDF en ZIP op edustandaard.nl: Algemene Beschrijving, Technische Beschrijving, Profielen-document, `UWLR2.3_Technische_bestanden_v20241213.zip`. Geen GitHub. <https://www.edustandaard.nl/standaard_afspraken/uitwisseling-leerlinggegevens-en-resultaten-uwlr/uwlr2-3/> | **Werkgroep beëindigd** |
| **OEAPI 6.0 / OOAPI 5.0** | Hybride: registratie op edustandaard.nl, normatieve techniek op <https://github.com/open-education-api/specification> (EUPL-1.2), ADR's op <https://github.com/open-education-api/governance-decisions>, **profielen** op <https://github.com/open-education-api/profiles>, site <https://oeapi.eu/specification/v6.0/index> | Werkgroep OEAPI met SURF; git tags |
| **OKE MBO-toetsafname** | Hybride: PDF op edustandaard.nl (v1.0.1, vastgesteld 27-05-2026), OAS op <https://github.com/NetwerkExamineringDigitalisering/NED-OOAPI> (CC0-1.0), Redoc-site | Werkgroep OKE en Kerngroep Techniek; GitHub releases |

Twee bevindingen die er direct toe doen:

1. **De UWLR-motivering legitimeert onze aanpak.** De werkgroep is beëindigd omdat één brede "one size fits all"-afspraak onwerkbaar bleek; Edustandaard koos daarna voor AMIGO met per scenario een smallere afspraak (<https://www.edustandaard.nl/standaard_werkgroepen/werkgroep-uitwisseling-leerlinggegevens-en-resultaten/>). Onze keuze om per koppeling te specificeren in plaats van één brede standaard te bouwen, is daarmee expliciet gedekt.
2. **`open-education-api/profiles` is de plek waar ons OEAPI consumer-profiel hoort te landen.** Dat is nu een intern meta-document. Dit is de duidelijkste ontbrekende schakel naar sectorborging.

Statusassen die Edustandaard hanteert: registratiestatus, versiestatus en gebruiksadvies. Bestuurlijke vaststelling via de Standaardisatieraad, inhoudelijke bewaking via de Architectuurraad. Edustandaard volgt **BOMOS** (<https://rosa.wikixl.nl/index.php/Edustandaard>).

## 7. Gat-analyse: AMIGO-product naast OKx-artefact

| Stap | Product | OKx-equivalent | Oordeel |
|---|---|---|---|
| **1** | Scenariobeschrijving (ArchiMate) | `Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md`, `persona's/jochem.md`, informatiestromenplaat als JPG | **Inhoudelijk gedekt, vorm wijkt af.** Alle AMIGO-vragen worden beantwoord, maar het product is proza plus mermaid plus een JPG-export; **het ArchiMate-model zelf staat in de private meta-repo** en is voor een externe lezer onbereikbaar |
| **2** | Uitwisselingsgegevensmodel (UML) plus vocabulaireselectie | §4 Informatiemodel per koppelingspecificatie (mermaid `erDiagram`), ankertabel, concept-informatiemodel | **Gedeeltelijk.** Geen zelfstandig herbruikbaar logisch model; geen aantoonbare selectie uit of aanvulling op de ROSA logische gegevensmodellen; **vocabulaireselectie ontbreekt volledig** |
| **3** | Interactiespecificatie (sequence- plus klassendiagram per bericht) | §3 Interactieoverzicht en §5 Sequentiediagrammen, met faalpaden | **Gedekt; onze sterkste analysestap.** Twee afwijkingen: geen klassendiagram per bericht, en de patronen zijn niet gemapt op de Edukoppeling-transactiepatronen |
| **4** | Keuze SOAP/REST plus rationale | Verspreid: "OEAPI, tenzij", ADR 0018, U5 | **Gedeeltelijk en ongebundeld.** REST is impliciet; nergens als expliciete stap-4-uitkomst vastgelegd. De randvoorwaardelijke bouwblokken uit hoofdstuk 7 ontbreken volledig |
| **5** | Berichtspecificatie | De drie payload-documenten met JSON Schema draft 2020-12 | **Gedekt; verst ontwikkeld.** Twee spanningen met §5.4: de generatierichting is omgekeerd, en de Nederlandstalige veldnamen belasten de voorgeschreven traceerbaarheidsrelaties naar OEAPI |
| **5b** | Vocabulairespecificatie (eigen onderdeel in de vijf) | — | **Ontbreekt.** Geen enkele waardenlijst of codelijst in `Public` |
| **6** | Interfacespecificatie (OAS) | §7 Endpointbeschrijvingen, met de tekst *"een uitgewerkte OpenAPI-beschrijving volgt later"* | **Ontbreekt als product.** Nul OAS-bestanden in `Public`. Bewust uitgesteld, maar de afsprakenset is daarmee nog niet "bouwbaar" in AMIGO-zin |

## 8. Onze artefacten die géén AMIGO-product zijn

| Artefact | Onderbouwing of ballast? |
|---|---|
| **Persona's** | Onderbouwing. AMIGO noemt ze niet, maar §6.1 vraagt om afbakening op *"conceptueel hoog niveau"*; een persona is een legitieme manier. Buiten het releasepakket houden |
| **Kaderscenario's per leerroute** | Onderbouwing, met een waarschuwing. AMIGO kent één uitwisselscenario per afsprakenset (§5.3). Negen leerroutes zijn negen scenario's — dat vermenigvuldigt de cyclus. De delta-aanpak is de juiste mitigatie en verdient explicieter te worden als methodische keuze |
| **Architectuurprincipes AP01–AP13** | Ballast-risico. AMIGO heeft eigen kaders (A1–A3, I1–I4, G1–G4, p.9–12) die wij nergens aanhalen. Overweeg te mappen en dubbelingen te schrappen |
| **Uitgangspunten U1–U10** | Deels herhaling van G2 en G4, zelfstandig afgeleid zonder bronvermelding |
| **ADR's 0001–0024** | Onderbouwing, en ons sterkste artefacttype. Geen AMIGO-product, wel exact wat stap 4 vraagt, en er is sectorprecedent: `open-education-api/governance-decisions` |
| **ADR 0021, koppeling versus koppelvlak** | Eigen constructie. AMIGO gebruikt geen van beide termen; "koppelvlak" is MORA/MOKA-taal. De ladder is verdedigbaar en nuttig, maar is een brug tussen twee vocabulaires, geen AMIGO-begrip |
| **Gebruiksprofiel per koppeling** | Onderbouwing, AMIGO-conform van geest (h3 p.8 vraagt *"voldoende vrijheidsgraden om, via het gebruik van extensies en vocabulaires, specifieke toepassingen te kunnen ondersteunen"*). De sectorterm is **profiel**; overweeg die over te nemen |
| **Onze eigen AMIGO-skill** | Ballast-risico en feitelijk onnauwkeurig. De stapbeschrijvingen wijken op vier punten van de bron af: stap 1 noemt geen ArchiMate, stap 2 noemt UML noch vocabulaireselectie, stap 3 noemt geen klassendiagram per bericht, en stap 4 heet "Technologiekeuze" waar AMIGO "Technologie-/paradigmakeuze" schrijft met "SOAP en/of REST plus rationale" als uitkomst |

## 9. Repo-indeling

**Wat uit de bron volgt** (weinig, maar hard):

- De **logische gegevensmodellen horen in ROSA**, niet in de projectrepo (§5.4 p.15, §7.6 p.21), met governance bij de Architectuurraad.
- Ontbrekende standaarden worden **teruggelegd bij de werkgroep** (p.16, p.19), niet lokaal opgelost. Voor ons: OEAPI-gaten naar werkgroep OEAPI, transactiepatroon-gaten naar Edukoppeling.
- **Over private versus publieke repo's, releasepakketten of mapstructuur zegt AMIGO niets.** Volledig vrije ruimte.

**Wat hieruit wordt afgeleid** (op basis van de OEAPI-, OKE- en UWLR-precedenten en het iteratieve karakter van de stappen):

| Laag | Wat erin hoort | Redenering |
|---|---|---|
| **Private source** | Werksessies, notulen, het levende ArchiMate-werkmodel, concept-scenario's, skills, het consumer-profiel zolang het concept is | De stappen zijn iteratief (p.16); tussenversies horen niet in een gereleased pakket |
| **Public source** | Alle zes producten in bronvorm, **inclusief het ArchiMate-exportbestand van stap 1** en de OAS-bron van stap 6, plus de onderbouwing | Precedent: OEAPI en NED-OOAPI publiceren de bron, niet alleen een PDF. **Het gat: het stap-1-product staat nu in de private repo** — de scherpste inconsistentie in de huidige verdeling |
| **Releasepakket** | Precies de vijf onderdelen van p.7, plus changelog en versiestatus. Géén ADR's, principes, persona's of templates | AMIGO noemt exact vijf onderdelen als "de specificatie" |

Afleiding over analyse versus specificatie: AMIGO trekt die scheiding niet expliciet, maar uit de modellenmatrix volgt dat stap 1–2 conceptueel/logisch zijn en stap 5–6 technisch. **Stap 1–3 zijn dan de onderbouwing, stap 4–6 het releasepakket** — stap 4 hoort erbij, want zonder technologiekeuze kan een implementeerder niets bouwen.

## 10. Wat AMIGO expliciet openlaat

Deze punten mogen wij naar eigen inzicht invullen zonder van de methodiek af te wijken:

1. **De vorm van bericht- en interfacespecificatie** — p.16 zegt *"mogelijke vormen"*, en JSON Schema en OAS staan er bij naam in.
2. **Aantal en indeling van documenten** — vijf *onderdelen*, geen vijf documenten. Bundelen mag.
3. **Granulariteit van de eenheid** — §5.3 laat "tussen twee of meer ketenpartners" toe; onze koppeling tussen twee referentiecomponenten past daarin. De term "koppelvlak" is niet van AMIGO en hoeft dus niet AMIGO-conform te zijn.
4. **Bulk versus delta** — G4 laat beide toe.
5. **Verwerkingsaanduiding** — G4: *"hetzij via verwerkingsvlaggen […] hetzij via separate acties of gescheiden endpoints."*
6. **Centrale versus decentrale mandatering** — §7.4: *"De keuze […] hangt erg af van de aard van de transacties"*, met Edu-V en OKE als decentrale voorbeelden.
7. **Extensies en eigen vocabulaires** bovenop een generieke structuur — h3 p.8.
8. **Gefaseerde invoering** — principe I1 p.10: *"Bestaande interacties en uitwisselingen kunnen stapsgewijs naar een op AMIGO gebaseerde structuur worden overgezet."* Dit dekt dat stap 5 af is en stap 6 nog niet.
9. **Publicatievorm, versionering, repo-indeling, conformiteitseisen** — volledig vrij; alleen BOMOS en de Edustandaard-statusassen sturen.

**En wat AMIGO níét openlaat, waar wij nu wel vrij invullen:**

- De **generatierichting logisch naar technisch** (§5.4 p.15) is dwingend, met expliciete traceerbaarheidsrelaties. Wij hebben geen logisch niveau als eigen product en genereren niet.
- De **modeltalen van stap 1 tot en met 3** staan als `"vorm:"` genoteerd. Mermaid is een pragmatische invulling; het ArchiMate-model van stap 1 hoort daadwerkelijk mee gepubliceerd.
- **Hergebruik van de ROSA-gegevenscatalogus** is het uitgangspunt van stap 2. Wij modelleren nu vanuit het consumer-profiel en de eigen ankertabel.

## Gerelateerde uitwerkingen

- [Gereedschap: requirements, architectuur en documentatie als code](20260804_1500_gereedschap-requirements-architectuur-docs-as-code.md) — het tweede onderzoeksverslag bij dit issue.
- [`.agents/skills/amigo-aanpak/`](../../../.agents/skills/amigo-aanpak/SKILL.md) — onze eigen AMIGO-harnas; zie §8 voor de afwijkingen ten opzichte van de bron.
- ADR volgt: dit verslag is onderbouwing, geen besluit.
