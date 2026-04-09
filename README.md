# OKx-meta

Deze repository is de **publieke knowledge base** van **OKx**: hier verzamelen en ontwikkelen we gedeelde kennis, afspraken en (concept-)uitwerkingen rond **gestandaardiseerde koppelvlakken voor onderwijslogistiek**.

## Welkom — waar zijn we nu mee bezig?

Als je hier voor het eerst binnenkomt: we leggen **keteninzicht** en **koppelvlakrichting** vast — samen met de sector, in het open — zodat we geen losse eilandoplossingen per systeem bouwen, maar een **gedeeld minimum** aan afspraken. Concreet werkt het kernteam en de community nu o.a. aan:

- **Informatiestromen (hoofdplaat)**: een overzicht van welke **stromen** tussen referentiecomponenten nog (conceptueel én technisch) beschreven moeten worden. De actuele plaat, uitleg en tabel staan in [`doc/OKx_Projectoverzicht.md`](doc/OKx_Projectoverzicht.md) bij *Hoofdplaat OKx informatiestromen*.
- **Van concept naar techniek**: wat die stromen in de keten **betekenen**, als **invoer** voor latere deliverables zoals **berichtspecificaties**, **klassendiagrammen** en **API-/OEAPI-beschrijvingen** (vergelijkbaar met bestaande sectorpakketten): [`doc/OKx_Informatiesstromen.md`](doc/OKx_Informatiesstromen.md).
- **MOKA & ArchiMate-model**: in [`architecture/model/model.archimate`](architecture/model/model.archimate) staan o.a. de MOKA-koppelvlak-view **`01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model`** en het bijbehorende **informatiemodel**-diagram. Praktische uitleg waar je die vindt: [`doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md`](doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md).
- **Besluiten vastleggen**: belangrijke architectuurkeuzes staan in **ADR’s**: [`architecture/dr/README.md`](architecture/dr/README.md).

Niet alles is al uitgewerkt — dat hoort erbij. Deze repo is **geen directe wijziging van MORA**; goed gedragen uitwerkingen kunnen later als **onderbouwd voorstel** richting sectorprocessen dienen.

Niet elk koppelvlak hoeft via de OKx-kernroute te lopen: **kleinere sectorinitiatieven** kunnen via **MOKA** starten (op basis van **AMIGO** en “**OEAPI, tenzij**”). Zie `doc/OKx_Projectoverzicht.md` voor de actuele positionering en verwijzingen (incl. OKx guidelines).

Wil je meer houvast als nieuwe bijdrager? Lees de sectie *Waar draait deze repository om?* in [`doc/Bijdragen-voor-beginners.md`](doc/Bijdragen-voor-beginners.md) — vriendelijk uitgelegd, met dezelfde lijn.

## Wat is OKx?

**OKx** werkt aan **uniforme, gestandaardiseerde koppelvlakken** zodat systemen in de onderwijsketen beter met elkaar kunnen samenwerken. Het **BOPSI-implementatiepad** is het uitgangspunt; de scope start bij **MBO** en wordt later uitgebreid naar **HO**. We zijn onderdeel van het [groeifondsprogramma Npuls, onder de Leren Zonder Drempels pilaar](https://npuls.nl/project-onderwijskoppelingen).

Meer context en de huidige stand van zaken: [`doc/OKx_Projectoverzicht.md`](doc/OKx_Projectoverzicht.md).

## Wat proberen we te doen?

- **Eenduidige afspraken** mogelijk maken tussen instellingen, leveranciers en andere ketenpartijen.
- Zorgen dat kennis niet versnipperd raakt: besluiten, open vragen en uitwerkingen landen **in deze repo** (en groeien door via issues en pull requests).

## Waar lopen we tegenaan?

- **Veel partijen, veel afhankelijkheden**: onderwijslogistiek raakt processen, beleid en techniek tegelijk.
- **Fasering en prioritering**: we starten in MBO en bouwen stapsgewijs uit.
- **Nog in aanbouw**: delen van het geheel zijn al uitgewerkt, andere onderdelen zijn nog onderwerp van verkenning, ontwerp en besluitvorming.

## Meer lezen en meepraten (GitHub)

- **Wiki**: achtergrond, uitleg en langere how-to’s: `https://github.com/Npuls-OKx/meta/wiki`
- **Discussions**: vragen, ideeën en open gesprekken: `https://github.com/Npuls-OKx/meta/discussions`

Voor concrete wijzigingen werken we via **issues** en **pull requests**. Zie [`CONTRIBUTING.md`](CONTRIBUTING.md) en de beginnershandleiding [`doc/Bijdragen-voor-beginners.md`](doc/Bijdragen-voor-beginners.md).

## Wat staat er in deze repository?

| Onderdeel | Locatie | Inhoud |
|-----------|---------|--------|
| **Projectcontext** | [`doc/`](doc/) en [`img/`](img/) | Overzichten, ketenplaten, bijlagen en contextdocumenten |
| **OKE uitwerking** | [`OKE/`](OKE/) | Eerste subdomein-uitwerking (o.a. examen: uitvoering en beoordeling) |
| **MOKA templates** | [`moka-koppelvlakspecificaties/`](moka-koppelvlakspecificaties/) | Templates en generieke instructies voor koppelvlakspecificaties |
| **Architectuur & besluiten** | [`architecture/`](architecture/) | ArchiMate-model, ADR’s, meeting-notulen en [`architecture/docs/principes/doc/principes.md`](architecture/docs/principes/doc/principes.md) |
| **Agent-artifacten** | [`architecture/agent-artifacts/`](architecture/agent-artifacts/) | Projectaanvragen, featureplannen en ontwerpdocumenten (Cursor slash commands); zie [`architecture/agent-artifacts/README.md`](architecture/agent-artifacts/README.md) |
| **Cursor (AI)** | [`.cursor/commands/`](.cursor/commands/) en [`.cursor/rules/`](.cursor/rules/) | Slash commands (`/…`) en rules; uitleg in [`doc/Bijdragen-voor-beginners.md`](doc/Bijdragen-voor-beginners.md) |

## Relatie met OEAPI

Waar passend sluiten uitwerkingen aan op **OEAPI**. Zie [OEAPI v6.0](https://openonderwijsapi.nl/v6.0/).

## Privacy, meetings en publieke kennis

OKx-sessies die deze knowledge base voeden kunnen **opgenomen en met AI getranscribeerd** worden; de facilitator **kondigt dat vooraf** aan. Bij bezwaar: **anonimisering in het transcript** of **deelneming beëindigen**. Tools worden gekozen met **AVG/privacy** in het oog; zie o.a. [Jamie — data handling](https://docs.meetjamie.ai/pages/faqs_troubleshooting/data). **Deel geen niet-publieke informatie** — deze repo is bedoeld als **publiek** gedachtegoed.

Volledige toelichting: [`doc/Privacy-meetings-en-transcriptie.md`](doc/Privacy-meetings-en-transcriptie.md).

## Status

Deze repository is **in aanbouw**. Contact voor afstemming: **niek.derksen@surf.nl**.


