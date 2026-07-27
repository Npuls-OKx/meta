## Inhoudsopgave

1. [Introductie](#1-introductie)
2. [Wat is een release?](#2-wat-is-een-release)
3. [Versienummering: SemVer-schema](#3-versienummering-semver-schema)
4. [Breaking, minor of patch: generieke criteria](#4-breaking-minor-of-patch-generieke-criteria)
5. [Compatibiliteit tussen afhankelijke artifacts](#5-compatibiliteit-tussen-afhankelijke-artifacts)
6. [Communicatie naar belanghebbenden](#6-communicatie-naar-belanghebbenden)
7. [Releaseproces (samengevat)](#7-releaseproces-samengevat)

---

## 1. Introductie

Dit document beschrijft de regels voor release management en versionering die voor **alle** OKx-artifacts gelden. Er valt hier niets in te vullen: dit is de vaste basis. Wat per artifact verschilt (eigenaarschap/RACI, wat "breaking" concreet betekent, compatibiliteit met andere artifacts) definieer je met het [OKx: Release management template](Release-management-template.md), zoals gedaan voor [meta](Release-management-meta.md) en [spec](Release-management-spec.md). Dat is een bewuste keuze: iets als de RACI-tabel of de criteria voor "wat is breaking" kunnen niet voor alle artifacts hetzelfde zijn, dus die worden per artifact ingevuld; de regels die wél voor ieder artifact hetzelfde zijn, staan hier één keer vastgelegd.

Zie ook: [OKx: Support-beleid](../Support-beleid.md) en [OKx: Development lifecycle](../Development-lifecycle.md) (beide in ontwikkeling, expliciet buiten de scope van release management zelf).

Dit document wordt pas afspraak na review en merge door de eigenaren. Leg een geaccepteerd besluit vast als ADR in [`architecture/dr/`](../../architecture/dr/).

## 2. Wat is een release?

Dit document onderscheidt vier begrippen:

- **Artifact**: het versiebeheerde geheel (bijv. meta, spec).
- **Versie**: een unieke, onveranderlijke identifier voor een specifieke stand van dat artifact (`MAJOR.MINOR.PATCH`).
- **Baseline**: de vastgelegde inhoud van het artifact bij die versie.
- **Release**: het besluit om een baseline beschikbaar te stellen aan afnemers.

Een release vereist:

1. de baseline voldoet aan de acceptatiecriteria ([§4](#4-breaking-minor-of-patch-generieke-criteria); bij afhankelijke artifacts ook de compatibiliteitscheck, [§5](#5-compatibiliteit-tussen-afhankelijke-artifacts));
2. bekrachtiging door het eigenaar-team (zie eigenaarschap/RACI, [template §3](Release-management-template.md#3-eigenaarschap));
3. communicatie aan belanghebbenden ([§6](#6-communicatie-naar-belanghebbenden)).

Het versielabel (`vMAJOR.MINOR.PATCH`) markeert de baseline, niet de release. Hoe een baseline technisch tot stand komt: zie [Bijdragen voor beginners §9](../Bijdragen-voor-beginners.md#9-branchstrategie-main-dev-feature-branches-tags).

---

## 3. Versienummering: SemVer-schema

Elk OKx-artifact gebruikt **Semantic Versioning** (SemVer): een release-label heeft de vorm `MAJOR.MINOR.PATCH` (bijv. `v1.4.2`). De algemene regels staan op [semver.org](https://semver.org/lang/nl/); hieronder de OKx-brede toepassing.

- **MAJOR: breaking.** Een niet-backward-compatibele wijziging: bestaande implementaties of clients die de wijziging niet volgen, wordt geadviseerd te migreren naar de nieuwe MAJOR.
- **MINOR: nieuwe, niet-breaking functionaliteit.** Nieuw concept, nieuw optioneel veld, nieuwe enum-waarde, nieuw scenario, nieuw optioneel koppelvlak, zonder bestaande afnemers te breken.
- **PATCH: correctie zonder semantische wijziging.** Tekstcorrecties, verduidelijkingen, voorbeeldfixes en bugfixes die het contract en de betekenis niet veranderen.
- **Eén release, één bumptype.** De zwaarste wijziging in een release bepaalt de bump (één breaking change maakt de hele release major).
- **Nog niet klaar voor een echte release?** Gebruik een pre-release-label (`v0.1.0-alpha.1`, `v1.5.0-rc.1`) of houd het ongepubliceerd. Zodra iets een `vMAJOR.MINOR.PATCH`-label krijgt, gelden de regels hierboven **onverkort**: een release is een release, niet gedeeltelijk breaking "omdat het nog vroeg is".
- **Bump zo vroeg mogelijk bepalen.** Hoe realistisch dat is, hangt af van andere afspraken: de branchstrategie ([Bijdragen voor beginners §9](../Bijdragen-voor-beginners.md#9-branchstrategie-main-dev-feature-branches-tags)) en hoe changes vorm krijgen (klein, incrementeel via losse PR's, of in grotere feature-brokken) bepalen hoe vroeg een major al zichtbaar is. Vooral bij een (mogelijk) major/breaking wijziging geldt: dat hoort al helder te zijn tijdens **refinement**, met commitment vanuit **PM**, niet pas wanneer de PR er ligt. De PR draagt daarna het voorgestelde semver-label; het eigenaar-team ([template §3](Release-management-template.md#3-eigenaarschap)) bevestigt dit bij het samenstellen van de release.

Wat "breaking" concreet betekent, verschilt per artifact: zie [§4](#4-breaking-minor-of-patch-generieke-criteria) en het toepassingsdocument van het artifact.

**Support en deprecatie** (hoeveel major-versies tegelijk ondersteund blijven, deprecatietermijnen, migratievensters) is een apart vraagstuk. Zie [OKx: Support-beleid](../Support-beleid.md) *(in ontwikkeling)*.

---

## 4. Breaking, minor of patch: generieke criteria

- **Niet-breaking (minor):** een nieuwe, optionele mogelijkheid die niets stukmaakt voor bestaande afnemers (bijv. nieuw optioneel veld, endpoint, concept of scenario).
- **Breaking (major):** een wijziging die bestaande implementaties, interpretaties of clients ongeldig maakt of ze anders laat werken dan voorheen.
- **Patch:** een correctie zonder inhoudelijke of contractwijziging (typefix, verduidelijking, gerepareerde link of voorbeeld).

Dit zijn generieke categorieën. **Wat concreet "breaking" is, verschilt per artifact.** Voor meta gaat het bijvoorbeeld om een wijziging in de ankertabel; voor spec om het verwijderen van een OpenAPI-veld. Werk dit per artifact uit in het toepassingsdocument (zie [meta §4](Release-management-meta.md#4-versiebeheer) en [spec §4](Release-management-spec.md#4-versiebeheer)).

---

## 5. Compatibiliteit tussen afhankelijke artifacts

Wanneer artifact B gebouwd wordt op basis van, of afhankelijk is van, artifact A, leg dan expliciet vast hoe hun versienummers zich tot elkaar verhouden. Een bruikbaar patroon: **B deelt de MAJOR-versie van A** als compatibiliteitssignaal; MINOR en PATCH blijven onafhankelijk per artifact.

Niet elk artifact heeft zulke afhankelijkheden; als een artifact op zichzelf staat, is deze paragraaf niet van toepassing. Zie het concrete voorbeeld tussen meta en spec in [meta §5](Release-management-meta.md#5-compatibiliteit-met-spec) en [spec §5](Release-management-spec.md#5-compatibiliteit-met-meta).

---

## 6. Communicatie naar belanghebbenden

Elke release (major, minor of patch) wordt via dezelfde **standaardroute** gecommuniceerd: een vaste, herkenbare plek per artifact (bijv. GitHub Releases), met release notes in een vast format (versie, datum, wat is gewijzigd, impact, eventuele actie voor afnemers). Patches krijgen een korte, feitelijke regel; minor/major releases krijgen een uitgebreidere toelichting, en bij major een migratiehandleiding (wat breekt, wat te doen, deprecatietermijn, zie [OKx: Support-beleid](../Support-beleid.md)).

**Eigenaar van de communicatie: PM**, tenzij het toepassingsdocument van een artifact iets anders vastlegt. PM stemt inhoud en timing af met het eigenaar-team ([template §3](Release-management-template.md#3-eigenaarschap)) en is er verantwoordelijk voor dat release notes daadwerkelijk verschijnen en bij belanghebbenden landen.

---

## 7. Releaseproces (samengevat)

Hoe een baseline technisch tot stand komt, staat in [Bijdragen voor beginners §9-10](../Bijdragen-voor-beginners.md#9-branchstrategie-main-dev-feature-branches-tags). Vanuit release-management-oogpunt komen daar deze stappen bij:

1. Bepaal de bump (zwaarste wijziging wint, [§3](#3-versienummering-semver-schema)); voor afhankelijke artifacts: check de compatibiliteit ([§5](#5-compatibiliteit-tussen-afhankelijke-artifacts)).
2. Laat het eigenaar-team ([template §3](Release-management-template.md#3-eigenaarschap)) de wijzigingen reviewen en de baseline vaststellen.
3. Ken het versielabel (`vMAJOR.MINOR.PATCH`) toe aan de vastgestelde baseline.
4. Publiceer release notes via de standaardroute ([§6](#6-communicatie-naar-belanghebbenden)); PM is eigenaar.

**Cross-artifact:** bij een MAJOR-bump van artifact A opent het eigenaar-team van elk afhankelijk artifact B een issue/milestone voor de bijbehorende re-baseline en plant het migratievenster samen met PM.

---

Reageren of bijdragen? Open een issue of PR; koppel die aan dit document (`See also #...`). Zie [`doc/Bijdragen-voor-beginners.md`](../Bijdragen-voor-beginners.md).
