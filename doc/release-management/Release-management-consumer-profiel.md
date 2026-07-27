# OKx: release management, toepassing consumer-profiel

## 1. Introductie

Dit document is de toepassing van het [OKx: Release management template](Release-management-template.md) voor het artifact **OKx OEAPI consumer-profiel** ([`architecture/docs/specificatie/okx-oeapi-consumer-profiel/`](../../architecture/docs/specificatie/okx-oeapi-consumer-profiel/)), beheerd door het **Kernteam OKx**. De regels die voor alle OKx-artifacts gelden staan in [OKx: Release management, algemene regels](Release-management-algemeen.md); hier alleen wat specifiek is voor dit artifact. Dit document wordt pas afspraak na review en merge door de eigenaren.

**Dit artifact is bewust kleiner dan "meta" ([Release-management-meta.md](Release-management-meta.md)).** Meta's huidige releasepakket-definitie omvat de hele repo, inclusief ADR's en meeting-notulen; die zijn **bronmateriaal** (hoe een besluit tot stand kwam), niet het **product** dat een implementatiepartij consumeert. Het consumer-profiel hieronder is dat product wél: het is de kaderstellende specificatie waarop de OpenAPI-specificatie (spec) gebouwd wordt. Zie de open vraag in [§9](#9-openstaande-punten) over hoe dit zich verhoudt tot meta's huidige scope.

## Inhoudsopgave

1. [Introductie](#1-introductie)
2. [Releasepakket](#2-releasepakket)
3. [Eigenaarschap](#3-eigenaarschap)
4. [Versiebeheer](#4-versiebeheer)
5. [Compatibiliteit met spec](#5-compatibiliteit-met-spec)
6. [Communicatie](#6-communicatie)
7. [Releaseproces](#7-releaseproces)
8. [Openstaande punten](#8-openstaande-punten)

---

## 2. Releasepakket

Het **OKx OEAPI consumer-profiel** (`consumerKey: "okx"`) is de kaderstellende technische specificatie en het implementatieverzoek voor het OEAPI-profiel: begrippenkader, ankertabel, scenario's per Npuls-leerroute, persona's en signaleringen. Het releasepakket bestaat uit:

- het specificatiedocument ([`20260501_Specificatie_document_OKx_OEAPI_profiel.md`](../../architecture/docs/specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md));
- de persona's (`persona_jochem.md`, `persona_larissa.md`, `persona_linda.md`) die als rode draad door de scenario's lopen;
- de bijbehorende proces- en informatiediagrammen (`doc/img/`, `doc/bpmn/`).

Dit is **niet** hetzelfde als "meta als geheel": ADR's, meeting-notulen, agent-artifacten en contributor-documentatie leven in dezelfde repository maar zijn bronmateriaal voor hoe dit profiel tot stand komt, niet zelf onderdeel van wat hier als versie wordt gepubliceerd. Het releasepakket komt tot stand via iteratieve uitwerking volgens de AMIGO-aanpak (scenario-analyse → gegevens-/interactie-analyse → technologiekeuze → bericht-/interfacespecificatie), vastgelegd in issues en PR's op de bestanden hierboven.

Dit profiel **vormt de bron** waarop spec (de OpenAPI-specificatie) wordt gebouwd, zie [§5](#5-compatibiliteit-met-spec).

---

## 3. Eigenaarschap

| Repository | Eigenaar / verantwoordelijk team |
|------------|-----------------------------------|
| **OKx OEAPI consumer-profiel** (binnen `Npuls-OKx/meta`) | **Kernteam OKx** ([GitHub-team `kernteam-okx`](https://github.com/orgs/Npuls-OKx/teams/kernteam-okx)) |

Uitgangspunt: **iedereen** mag issues en PR's indienen; **alleen Kernteam OKx merget** in deze repo (zie [`CONTRIBUTING.md`](../../CONTRIBUTING.md) en [`.cursor/rules/okx-governance.mdc`](../../.cursor/rules/okx-governance.mdc)).

Ingevulde RACI (template: [Release management template §3](Release-management-template.md#3-eigenaarschap)):

| Activiteit | Kernteam OKx | Technische werkgroep OKx | PM |
|------------|:---:|:---:|:---:|
| Inhoud consumer-profiel | R/A | C | I |
| Release consumer-profiel (versie bepalen, taggen) | R/A | C, expliciet bij `v0.1.0` (eerste reviewbare versie) | I |
| Vaststellen major/breaking wijziging | A | R | C, commitment tijdens refinement ([algemene regels §3](Release-management-algemeen.md#3-versienummering-semver-schema)) |
| Communicatie naar belanghebbenden | C | C | R/A |

---

## 4. Versiebeheer

Het consumer-profiel volgt het SemVer-schema en de generieke definities uit [algemene regels §3-4](Release-management-algemeen.md#3-versienummering-semver-schema) zonder afwijkingen. Concreet voor dit artifact:

**Breaking als het bestaande implementaties of interpretaties ongeldig maakt:**

- wijziging of hernoeming van een **begrip** of van een rij/kolom in de **ankertabel** (§3.2.6 van het profiel) waardoor eerdere mapping niet meer klopt;
- wijziging van een **cardinaliteit** of van de grens tussen *specificatie / aanbod / verbintenis / resultaat*;
- een eerder **optioneel** kaderelement **verplicht** maken.

**Niet-breaking (minor):** nieuw **optioneel** veld of endpoint; nieuwe enum-waarde via `x-ooapi-extensible-enum`; nieuw optioneel koppelvlak; toevoegen van een scenario of persona.

**Patch:** typefix, verduidelijkte omschrijving, gecorrigeerd voorbeeld, gerepareerde `$ref` of link **zonder** contractwijziging.

---

## 5. Compatibiliteit met spec

**spec deelt de MAJOR-versie van het consumer-profiel** als compatibiliteitssignaal: bij profiel-MAJOR `X` blijft spec ook op MAJOR `X`, ongeacht spec's eigen MINOR/PATCH-stand. Dat betekent:

- **Zelfde MAJOR = compatibel**: spec is gebouwd tegen dit profiel.
- **profiel-MAJOR-bump → spec-MAJOR-bump** (re-baseline), ook als spec zelf geen breaking wijziging heeft.
- **spec mag zelfstandig MINOR/PATCH bumpen** binnen dezelfde MAJOR, voor eigen additieve features of correcties in de OpenAPI-implementatie.

Leg de gedeelde MAJOR vast in het OpenAPI-document en herhaal dit in de README/`COMPATIBILITY.md` van de spec-repo:

```yaml
info:
  version: 1.2.0   # spec-versie (SemVer); MAJOR gedeeld met consumer-profiel
```

> **Open punt:** dit is een vereenvoudiging van het eerdere baseline-model. Nadere uitwerking en impact-inschatting (onder meer wat te doen als spec een eigen breaking wijziging nodig heeft zonder dat het profiel breekt) volgt na de OKx impact- en ontwerplab-sessie, zie [issue #117](https://github.com/Npuls-OKx/meta/issues/117).

---

## 6. Communicatie

Dit artifact volgt de standaardroute uit [algemene regels §6](Release-management-algemeen.md#6-communicatie-naar-belanghebbenden): PM is eigenaar van de communicatie. Geen afwijkingen, met één uitzondering:

**Vroege fase.** Tot en met `v0.0.x` (opbouw op `dev` en vroege tags) is er nog geen externe belanghebbende om te informeren; de eerste communicatie is de eerste reviewbare minor (`v0.1.0`), wanneer de Technische werkgroep OKx beoordeelt of het profiel voldoende is om spec te starten.

---

## 7. Releaseproces

Dit artifact volgt het proces uit [algemene regels §7](Release-management-algemeen.md#7-releaseproces-samengevat). Eén aanvulling specifiek voor dit artifact:

Het profiel groeit eerst als **verzameling van patches** op `dev` (losse issues en PR's op het specificatiedocument, persona's en diagrammen); die iteraties worden niet gecommuniceerd naar de Technische werkgroep OKx. Pas bij de eerste reviewbare minor volgt een **release-PR** `dev` → `main`: de Technische werkgroep OKx beoordeelt of het profiel voldoende is om spec te starten.

---

## 8. Openstaande punten

- **Verhouding tot meta.** Meta's releasepakket ([Release-management-meta.md §2](Release-management-meta.md#2-releasepakket)) omvat op dit moment de hele repository, inclusief dit consumer-profiel. Als dit artifact zelfstandig versioneert, moet meta's releasepakket-definitie worden versmald (bijv. tot referentiekader/business-architectuur en governance, exclusief dit profiel, exclusief ADR's/meetings als bronmateriaal). Dat is nog niet doorgevoerd.
- Vastleggen als **ADR** in [`architecture/dr/`](../../architecture/dr/) zodra geaccepteerd.
- **[OKx: Support-beleid](../Support-beleid.md)** nog uit te werken: aantal ondersteunde major-versies, deprecatietermijn, migratievenster.
- **[§5](#5-compatibiliteit-met-spec)** (gedeelde MAJOR als compatibiliteitssignaal) is een vereenvoudiging; impact-inschatting en edge cases volgen na de OKx impact- en ontwerplab-sessie ([issue #117](https://github.com/Npuls-OKx/meta/issues/117)).

Reageren of bijdragen? Open een issue of PR; koppel die aan dit document (`See also #...`). Zie [`doc/Bijdragen-voor-beginners.md`](../Bijdragen-voor-beginners.md).
