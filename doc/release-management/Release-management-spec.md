## Inhoudsopgave

1. [Introductie](#1-introductie)
2. [Releasepakket](#2-releasepakket)
3. [Eigenaarschap](#3-eigenaarschap)
4. [Versiebeheer](#4-versiebeheer)
5. [Compatibiliteit met meta](#5-compatibiliteit-met-meta)
6. [Communicatie](#6-communicatie)
7. [Releaseproces](#7-releaseproces)

---

## 1. Introductie

Dit document is de toepassing van het [OKx: Release management template](Release-management-template.md) voor het artifact **spec** ([`Npuls-OKx/specification`](https://github.com/Npuls-OKx/specification)), beheerd door de **Technische werkgroep OKx**. De regels die voor alle OKx-artifacts gelden staan in [OKx: Release management, algemene regels](Release-management-algemeen.md). Omdat spec in een eigen repository leeft, is dit een **voorstel vanuit meta**: de werkgroep reviewt het en neemt het over in de spec-repo (bijv. als `COMPATIBILITY.md` of eigen release-managementdocument).

## 2. Releasepakket

**spec** ([`Npuls-OKx/specification`](https://github.com/Npuls-OKx/specification)) is de technische implementatie van het OEAPI-profiel: de OpenAPI-specificatie, een bouwbaar en testbaar koppelvlak. Het releasepakket is het OpenAPI-document (en bijbehorende bestanden) van deze repo; het komt tot stand **op basis van meta**, zie [meta §5](Release-management-meta.md#5-compatibiliteit-met-spec) en [§5](#5-compatibiliteit-met-meta) hieronder.

---

## 3. Eigenaarschap

| Repository | Eigenaar / verantwoordelijk team |
|------------|-----------------------------------|
| **spec** | **Technische werkgroep OKx** |

Uitgangspunt: **iedereen** mag issues en PR's indienen; **alleen de Technische werkgroep OKx merget** in deze repo.

Ingevulde RACI (template: [Release management template §3](Release-management-template.md#3-eigenaarschap)):

| Activiteit | Technische werkgroep OKx | Kernteam OKx | PM |
|------------|:---:|:---:|:---:|
| Inhoud spec (OpenAPI) | R/A | C | I |
| Release spec (versie bepalen, taggen) | R/A | I | I |
| Vaststellen major/breaking wijziging in spec | A | C | C, commitment tijdens refinement ([algemene regels §3](Release-management-algemeen.md#3-versienummering-semver-schema)) |
| Communicatie naar belanghebbenden | C | C | R/A |

---

## 4. Versiebeheer

Spec volgt het SemVer-schema en de generieke definities uit [algemene regels §3-4](Release-management-algemeen.md#3-versienummering-semver-schema) zonder afwijkingen. Concreet voor spec:

**Breaking als bestaande clients breken:**

We volgen hierin het [beleid van OEAPI op het gebied van versioning en de relatie met consumers](https://oeapi.eu/v6.0/#/governance/version-management?id=start), zoals vastgelegd in [ADR-0005 over versieonderhandeling](https://github.com/open-education-api/governance-decisions/blob/main/adr/0005-version-negotiation-via-http-header.md). Het hier ontwikkelde profiel en de bijbehorende consumers hanteren dat beleid en die principes. Op hoofdlijnen:

- een veld/endpoint **verwijderen** of **hernoemen**;
- een type **versmallen** of een veld van optioneel naar **`required`** zetten;
- een **enum-waarde verwijderen** of de betekenis ervan wijzigen;
- response-/request-structuur of -semantiek wijzigen waardoor bestaande aanroepen anders uitpakken.

**Niet-breaking (minor):** nieuw **optioneel** veld of endpoint; nieuwe enum-waarde via `x-ooapi-extensible-enum`; nieuw optioneel koppelvlak.

**Patch:** typefix, verduidelijkte omschrijving, gecorrigeerd voorbeeld, gerepareerde `$ref` of link **zonder** contractwijziging.

---

## 5. Compatibiliteit met meta

**spec deelt de MAJOR-versie van meta** als compatibiliteitssignaal: bij meta-MAJOR `X` blijft spec ook op MAJOR `X`, ongeacht spec's eigen MINOR/PATCH-stand. Dat betekent:

- **Zelfde MAJOR = compatibel**: spec is gebouwd tegen dat kader.
- **meta-MAJOR-bump → spec-MAJOR-bump** (re-baseline), ook als spec zelf geen breaking wijziging heeft.
- **spec mag zelfstandig MINOR/PATCH bumpen** binnen dezelfde MAJOR, voor eigen additieve features of correcties in de OpenAPI-implementatie.

Leg de gedeelde MAJOR vast in het OpenAPI-document en herhaal dit in de README/`COMPATIBILITY.md` van deze repo:

```yaml
info:
  version: 1.2.0   # spec-versie (SemVer); MAJOR gedeeld met meta
```

> **Open punt:** dit is een vereenvoudiging van het eerdere baseline-model. Nadere uitwerking en impact-inschatting (onder meer wat te doen als spec een eigen breaking wijziging nodig heeft zonder dat meta breekt) volgt na de OKx impact- en ontwerplab-sessie, zie [issue #117](https://github.com/Npuls-OKx/meta/issues/117).

---

## 6. Communicatie

Spec volgt de standaardroute uit [algemene regels §6](Release-management-algemeen.md#6-communicatie-naar-belanghebbenden): PM is eigenaar van de communicatie. Geen afwijkingen.

---

## 7. Releaseproces

Spec volgt het proces uit [algemene regels §7](Release-management-algemeen.md#7-releaseproces-samengevat). Geen afwijkingen.

---

Reageren of bijdragen? Open een issue of PR in de meta-repo en koppel die aan dit document (`See also #...`), of neem contact op met het Kernteam OKx.
