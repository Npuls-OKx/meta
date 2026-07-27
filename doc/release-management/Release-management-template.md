# OKx: release management template

Dit is het **template** om release management te definiëren voor een nieuw OKx-artifact: kopieer dit bestand naar een eigen toepassingsdocument (bijv. `OKx_Release-management-<artifact>.md`) en vul de placeholders in. De regels die voor **alle** OKx-artifacts gelden staan in [OKx: Release management, algemene regels](Release-management-algemeen.md) en hoeven hier niet herhaald te worden.

Ingevulde voorbeelden: [meta](Release-management-meta.md), [spec](Release-management-spec.md) *(voorstel)*.

## Inhoudsopgave

1. [Introductie](#1-introductie)
2. [Releasepakket](#2-releasepakket)
3. [Eigenaarschap](#3-eigenaarschap)
4. [Versiebeheer](#4-versiebeheer)
5. [Compatibiliteit](#5-compatibiliteit)
6. [Communicatie](#6-communicatie)
7. [Releaseproces](#7-releaseproces)

---

## 1. Introductie

*Beschrijf hier kort en to-the-point wat dit document is: de release-managementafspraken voor artifact [naam], welk team dit beheert, en dat het pas een afspraak is na review en merge door de eigenaren.*

---

## 2. Releasepakket

*Beschrijf hier wat het releasepakket van dit artifact precies is: welke onderdelen samen als één releasebare eenheid worden gebouwd en gepubliceerd, en hoe dit releasepakket tot stand komt (bijv. een verzameling documentatie/modellen in een repo die als geheel getagd wordt, of een gegenereerde specificatie).*

Voorbeelden: [meta §2](Release-management-meta.md#2-releasepakket), [spec §2](Release-management-spec.md#2-releasepakket).

---

## 3. Eigenaarschap

Benoem het **eigenaar-team** (het team dat merget in de betreffende repo, zie [`CONTRIBUTING.md`](../../CONTRIBUTING.md)) en vul de RACI in met de daadwerkelijke teams en rollen (**R** = voert uit, **A** = eindverantwoordelijk, **C** = wordt geraadpleegd, **I** = wordt geïnformeerd):

| Activiteit | Eigenaar-team | Review-/consulterend team | Communicatie-rol |
|------------|:---:|:---:|:---:|
| Inhoud van het artifact | R/A | C | I |
| Release (versie bepalen, publiceren) | R/A | C | I |
| Vaststellen major/breaking wijziging | A | R | C |
| Communicatie naar belanghebbenden | C | C | R/A |

*Vervang "Eigenaar-team" en "Review-/consulterend team" door de daadwerkelijke teams.* Voorbeelden: [meta §3](Release-management-meta.md#3-eigenaarschap), [spec §3](Release-management-spec.md#3-eigenaarschap).

---

## 4. Versiebeheer

Dit artifact volgt het SemVer-schema en de generieke MAJOR/MINOR/PATCH-definities uit [algemene regels §3-4](Release-management-algemeen.md#3-versienummering-semver-schema). Beschrijf hier alleen wat **aanvullend of specifiek** is voor dit releasepakket:

*Concreet: wat betekent "breaking" voor dit artifact? Zijn er afwijkingen van de generieke regels (bijv. een eigen pre-release-conventie)?*

Voorbeelden: [meta §4](Release-management-meta.md#4-versiebeheer) (wijzigingen in de ankertabel), [spec §4](Release-management-spec.md#4-versiebeheer) (OpenAPI-contractwijzigingen).

---

## 5. Compatibiliteit

*Alleen relevant als dit artifact gebouwd wordt op basis van, of afhankelijk is van, een ander artifact; anders is deze sectie niet van toepassing. Beschrijf de relatie tussen de versienummers. Het patroon "gedeelde MAJOR-versie" staat toegelicht in [algemene regels §5](Release-management-algemeen.md#5-compatibiliteit-tussen-afhankelijke-artifacts).*

Voorbeeld: [meta §5](Release-management-meta.md#5-compatibiliteit-met-spec) / [spec §5](Release-management-spec.md#5-compatibiliteit-met-meta).

---

## 6. Communicatie

Standaard geldt [algemene regels §6](Release-management-algemeen.md#6-communicatie-naar-belanghebbenden): PM is eigenaar van de communicatie, via een standaardroute. *Beschrijf hier alleen als dit voor dit artifact anders is (andere eigenaar, ander kanaal, extra doelgroep).*

---

## 7. Releaseproces

Standaard geldt het proces uit [algemene regels §7](Release-management-algemeen.md#7-releaseproces-samengevat). *Beschrijf hier alleen artifact-specifieke afwijkingen of aanvullingen.*

---

Reageren of bijdragen? Open een issue of PR; koppel die aan dit document (`See also #...`). Zie [`doc/Bijdragen-voor-beginners.md`](../Bijdragen-voor-beginners.md).
