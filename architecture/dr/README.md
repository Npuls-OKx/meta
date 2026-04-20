# Architecture Decision Records (`architecture/dr`)

Deze map hoort bij **OKx-meta**: de **open kennisbasis** rond **onderwijslogistieke ketens**, **MOKA-koppelvlakken** en **informatiestromen** tussen referentiecomponenten. In het [ArchiMate-model](../model/model.archimate) staan o.a. de MOKA-view **`01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model`** en het bijbehorende **informatiemodel**-diagram (zelfde koppelvlak); de **hoofdplaat** en tabel met nog te beschrijven stromen staan in het [OKx-projectoverzicht](../../doc/OKx_Projectoverzicht.md). ADR’s leggen hier vast **welke architectuurkeuzes** we maken op weg naar **technische uitwerking** (o.a. berichtspecificaties, modellen, **OEAPI**-passende endpointbeschrijvingen) — traceerbaar en besprekbaar met de sector en architectuurgremia.

---

## ADR's (decision records)

In deze map leggen we Architecture Decision Records (ADR's) vast.

Doel: architectuurkeuzes traceerbaar maken en onderbouwen vanuit issues en meetings.

Werkwijze:

- Start met een issue (bij voorkeur issue template "ADR-voorstel").
- Maak daarna een PR met een nieuw ADR bestand of een wijziging.
- Link altijd naar:
  - issue(s)
  - relevante meeting-notulen (als het uit een meeting komt)
  - relevante OKx/OKE documentatie
  - impact op het ArchiMate model (`architecture/model/model.archimate`)

Bestandsnaamconventie:

- `NNNN-korte-titel.md` (bijv. `0001-plaats-van-adrs.md`)

Template:

- Gebruik `template.md` als basis.

### ADR’s in deze map (concept)

| Nr | Bestand | Onderwerp |
|----|---------|-----------|
| 0001 | [`0001-publieke-repo-en-samenwerkingsmodel.md`](0001-publieke-repo-en-samenwerkingsmodel.md) | Publieke repo als bron van waarheid, PR’s, issues, review |
| 0002 | [`0002-prioriteitsketen-catalogus-drielagen-fundament.md`](0002-prioriteitsketen-catalogus-drielagen-fundament.md) | Eerste keten curriculum–catalogus; MORA/MOKA-drielagen-fundament |
| 0003 | [`0003-student-kiest-leeruitkomsten-domeinprincipes.md`](0003-student-kiest-leeruitkomsten-domeinprincipes.md) | Student kiest, leeruitkomsten, onderwijskundige laag + journeys |
| 0004 | [`0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md`](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) | Leeruitkomsten + SBU/EC als logistieke containergrootte (mbo/hbo) |
| 0005 | [`0005-student-keuze-systeem-zelfstandige-referentiecomponent.md`](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) | SKS als eigen referentiecomponent; MVP-fundament; koppeling SVS |
| 0006 | [`0006-studentorientatie-trechter-ketenfase.md`](0006-studentorientatie-trechter-ketenfase.md) | Studentoriëntatie als ketenfase; trechter naar leeruitkomsten *(concept)* |
| 0007 | [`0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md`](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) | Studentkeuzecriteria als queryparameters (SKS -> OC) *(concept)* |
| 0008 | [`0008-scope-planning-eerst-intra-instelling.md`](0008-scope-planning-eerst-intra-instelling.md) | Eerst intra-instelling; federatie gefaseerd *(concept)* |
| 0009 | [`0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md`](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) | SKS vs SVS rollen (keuze vs resultaat/LMS) *(concept)* |
| 0010 | [`0010-archimate-moka-informatiemodel-werkafspraken.md`](0010-archimate-moka-informatiemodel-werkafspraken.md) | Werkafspraken model.archimate + MOKA-IM *(concept)* |
| 0011 | [`0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md`](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md) | Student kiest op leeractiviteitniveau; leervormen als aanbodkenmerk |
| 0012 | [`0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md`](0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md) | Leerroute instellingsonafhankelijk; keuzegate nominaal vs maatwerk |
| 0013 | [`0013-microcredentials-scope-en-credentialcontrole-intake.md`](0013-microcredentials-scope-en-credentialcontrole-intake.md) | Microcredentials scope-afbakening; credentialcontrole bij intake |
| 0014 | [`0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md`](0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md) | Splitsing inschrijving (ROD/KRS) en onderwijskundige keuze (SKS) |
| 0015 | [`0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md`](0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md) | Request for Offering: haalbaarheidstoets tussen SKS en planning/roostering |
| 0016 | [`0016-ontwikkelingswallet-edu-wallet-eigenaarschap-toestemming-en-ontsluiting.md`](0016-ontwikkelingswallet-edu-wallet-eigenaarschap-toestemming-en-ontsluiting.md) | Ontwikkelingswallet (EDU-wallet): eigenaarschap, toestemming en EduID-ontsluiting |
| 0017 | [`0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md`](0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md) | Hiërarchisch aanboddatamodel: leeruitkomsten en SBU/EC-aggregatie |
| 0018 | [`0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md`](0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md) | Enterprise messaging patronen: delivery, idempotentie, dead-letter, ordering |

