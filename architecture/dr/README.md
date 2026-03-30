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

