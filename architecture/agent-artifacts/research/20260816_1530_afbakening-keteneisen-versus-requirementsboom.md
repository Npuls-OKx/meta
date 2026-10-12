# Kunnen de keten-eisen in Public opgaan in de requirementsboom?

Relateert aan: #152 en [Public-issue 33](https://github.com/Npuls-OKx/Public/issues/33) (overheveling van de boom, uitgesteld). Invoer voor een later architectuurbesluit (ADR in Public); dit verslag besluit niets.

## Vraag

Kan de requirementsboom de rol overnemen van de keten-eisen K1 tot en met K5 in [`afbakening.md` §2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/afbakening.md) van het Public-releasepakket, gegeven twee randvoorwaarden: het pakket wordt als één gebundeld document (PDF) opgeleverd, en vanuit de functionele eisen (FR) in dat document moet naar stories in de boom verwezen kunnen worden?

## Wat er nu staat

Dit staat er, per bron:

- **De K-laag.** [`afbakening.md` §2](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/afbakening.md) draagt vijf keten-eisen (K1 tot en met K5), elk afgesloten met een regel "Afgeleid: FR… bij …" naar de FR-tabellen: bij K1 en K2 naar alle drie de interactiepatronen, bij K3 en K4 naar twee, bij K5 naar één, met de expliciete noot dat SIS en LMS die eis nog niet in functionele eisen hebben uitgewerkt. De inleiding van §2 benoemt de bedoeling: de eisen staan bij het interactiepatroon "zodat de keten eis → interactiepatroon → endpoint bij elkaar blijft". Dat K5-gat is relevant voor optie 2 hieronder: wie de K-laag vervangt, neemt ook de openstaande dekking mee.
- **De FR-laag.** Elk interactiepatroon opent met een tabel `| # | Functionele eis | Interactiepatroon |`; de FR-nummers zijn per document genummerd en dus niet globaal uniek (FR1 bestaat drie keer). Story-id's in de boom (S3.1) zijn wél globaal uniek.
- **De K-laag wordt buiten `afbakening.md` niet aangehaald.** `grep -rn '\bK[1-5]\b'` over de volledige pakketmap `Koppelvlakspecificaties/` treft buiten `afbakening.md` alleen kerntaakcodes in `Datamodelschema's/voorbeeldpayloads.md` (zoals `B1-K1`), geen keten-eisen. Vervanging raakt dus één document (gecontroleerd op Public `dev` d.d. 16 augustus 2026).
- **De releasebundel.** [`release.json`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/release.json) bepaalt de bundelvolgorde; `afbakening.md` is een top-level document in de bundel. Alle paden in het manifest liggen binnen `Koppelvlakspecificaties/`. [`build-release.py`](https://github.com/Npuls-OKx/Public/blob/dev/scripts/build-release.py) herschrijft interne relatieve verwijzingen naar ankers binnen het gebundelde document.
- **De boom.** De vier lagen met bronplicht staan in [`Referentiemateriaal/requirementsboom/`](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/requirementsboom/README.md) (destijds op meta, sinds 28 augustus op Public); 22 stories waarvan een deel met interactie- en eigenaarverwijzing naar de Public-interactiepatronen.

## De inhoudelijke overlap tussen K-laag en boom

Dit is een afleiding, geen brontekst. De K-eisen en de boom-features beschrijven deels hetzelfde gedrag:

| Keten-eis | Dichtstbijzijnde boomrijen |
|---|---|
| K1 vastgestelde specificatie bereikt elk systeem | E1-doel, F1.4; stories S3.1, S5.3 |
| K2 elk systeem meldt terug wat het ermee deed | stories S3.2, S5.4; F3.4 |
| K3 wijziging werkt door zonder alles opnieuw | F1.3; story S1.2 |
| K4 wijziging raakt lopende uitvoering niet ongecontroleerd | F4.3; story S4.1 |
| K5 uitval kost geen informatie | F7.1; stories S7.1, S7.2 |

De dekking is niet volledig symmetrisch: de K-teksten dragen motiverende prosa (waarom de eis bestaat) die de boomtabellen bewust niet dragen, en de boom dekt domeinen (keuze, taal, adoptie) die buiten de K-laag vallen.

## Randvoorwaarde: het gebundelde document moet op zichzelf staan

Public-documenten worden gereleased voor een lezer zonder toegang tot het werkproces, en verwijzingen vanuit Public naar meta moeten op een commit gepind worden. Zolang de boom in meta leeft, kan het gebundelde document dus alleen via gepinde externe URL's naar stories verwijzen: de PDF-lezer moet online, en elke uitwerkingsronde van de boom veroudert de pin. Verwijzen de FR-tabellen naar stories, dan hoort de boom dus in Public te leven (het plan in [Public-issue 33](https://github.com/Npuls-OKx/Public/issues/33)), en wil je het relevante deel van de boom in de bundel zelf hebben.

**Niet geverifieerd:** of `build-release.py` paden buiten `Koppelvlakspecificaties/` (zoals `../Referentiemateriaal/…`) in het manifest accepteert. Alle huidige manifestpaden liggen binnen de pakketmap; opname van boommateriaal in de bundel vergt dus mogelijk een build-aanpassing of een plek binnen de pakketmap.

## Opties

1. **K-laag behouden, boom als extra bovenlaag.** FR-tabellen krijgen een story-kolom; K1 tot en met K5 blijven de ketencontext in de bundel. Minste verbouwing, maar drie eisenlagen (K, feature/story, FR) met aantoonbare overlap en twee onderhoudspunten voor hetzelfde gedrag.
2. **K-laag laten opgaan in de boom.** De boom verhuist naar Public ([Public-issue 33](https://github.com/Npuls-OKx/Public/issues/33)); §2 van `afbakening.md` wordt vervangen door een compact boom-extract in de bundel: per koppeling de dragende features en stories, met de motiverende prosa van de K-teksten ondergebracht bij de betreffende feature of in de inleiding; FR-tabellen verwijzen per rij naar het story-id. Eén eisenlaag boven de FR's, en de verwijzing FR → story is releasebaar omdat het extract meebundelt. Kosten: overheveling plus herschrijving van §2, en de vraag hierboven over de bundelbouw.
3. **K-laag vervangen door een verwijzing naar de boom buiten het pakket.** Minste werk, maar het gebundelde document verliest zijn eisencontext als eigen inhoud en leunt op een gepinde externe link die elke boomronde veroudert. Strijdig met het zelfdragende karakter van de release.

## Advies

Optie 2, in twee stappen en pas nadat de boom in meta is uitgehard: eerst de overheveling ([Public-issue 33](https://github.com/Npuls-OKx/Public/issues/33)), daarna de ombouw van `afbakening.md` §2. Richt de verwijzing van FR naar story-id in (S-id's zijn globaal uniek; de FR-nummers hoeven dan niet hernummerd), en houd de omgekeerde richting aan die de boom al draagt: de story noemt interactie en eigenaar. Optie 1 is het terugvalpad wanneer de bundelbouw boommateriaal niet kan opnemen; optie 3 valt af op het zelfdragende karakter. Het besluit zelf hoort in een ADR in Public, met dit verslag als invoer.
