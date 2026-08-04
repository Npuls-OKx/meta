# Requirements: conventie voor identificatienummers

Relateert aan: #135, bouwt voort op #130

Eisen aan een conventie voor identificatienummers van OKx-artefacten, opgesteld voordat de conventie zelf wordt uitgewerkt. Elke eis is toetsbaar: er staat bij waaraan je ziet dat eraan is voldaan.

## 1. Aanleiding en gap-analyse

### Wat er al is

| Soort | Bestaande nummering | Waar |
|---|---|---|
| Uitgangspunt | `U1` tot en met `U10` | [`uitgangspunten.md`](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) |
| Interactie | `I1`-`I5` bij planning, `S1`-`S5` bij het studentinformatiesysteem, `L1`-`L6` bij de leeromgeving | §3 van elke koppelingspecificatie |
| Architectuurbesluit | `0001` tot en met `0024` | [`Referentiemateriaal/adr/`](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr) |
| Requirement | `R1` tot en met `R17` | requirements-document keuzes rond onderwijsspecificaties |
| Schema | `$id` als URI | `Datamodelschema's/*.json` |
| Informatie-object | **geen** | conceptueel gegevensoverzicht, 33 datarijen |
| Informatiestroom | **geen** | verspreid over de fasesecties van leerroute 1 |

### Wat ontbreekt

1. **Geen regel bij hernoemen.** Nergens staat wat er gebeurt als een begrip een andere naam krijgt. Dat is geen theoretisch geval: de ankertabel is al een keer herzien, waarbij een kolom werd toegevoegd en de overige kolommen hernummerd.
2. **Geen regel bij vervallen.** Er is geen status waarmee een ID uit gebruik gaat zonder te verdwijnen.
3. **Geen controle.** Geen van de bestaande nummeringen wordt machinaal getoetst op dubbelen of dode verwijzingen.
4. **Vier gewoonten naast elkaar.** `U4`, `I1`, `0021` en `R7` volgen elk een eigen vorm. Een lezer kan aan `R7` niet zien uit welk document het komt.
5. **Geen plek voor "wij lopen voor op MORA".** Een deel van onze begrippen heeft nog geen equivalent in MORA. Er is geen manier om dat vast te leggen als bewuste stand van zaken in plaats van als omissie.

### Wat géén beperking is

**Bestaande nummers mogen wijzigen.** De conventie wordt nu voor het eerst vastgesteld, dus er is nog geen afspraak die we breken. Een eerdere versie van dit document eiste dat `U1` tot en met `U10`, `I1` tot en met `I5` en de ADR-nummers ongewijzigd moesten kunnen worden opgenomen. Die eis is geschrapt: hij zou vier onderling verschillende nummervormen permanent maken om een eenmalige migratie te vermijden, en dat is de verkeerde ruil.

Vanaf het moment dat de conventie is vastgesteld geldt [R2](#r2--een-id-wordt-nooit-hergebruikt) onverkort. De vrijheid om te hernummeren bestaat dus precies één keer, en nu.

### Beperkingen die gelden

- De documenten worden **gereleased**. Een ID dat een leverancier aanhaalt, moet jaren later nog hetzelfde ding aanwijzen.
- Bijdragers zijn architecten en onderwijskundigen. Een conventie die een register-lookup vereist voor elke verwijzing, wordt niet gevolgd.
- Er draait op dit moment **niets in CI**. Elke eis die op machinale controle steunt, veronderstelt dat die controle er komt.
- Het aantal begrippen groeit: examenplanspecificatie, resultaatstructuren en de vormen van resultaten staan al op de rol.

## 2. Requirements

"MOET" in de zin van RFC 2119.

### R1 — Eén ID per aangehaald ding

Elk artefact dat vanuit een ander document wordt aangehaald, MOET precies één identificatienummer dragen.

*Voorbeeld.* Uitgangspunt U4 (notify-then-pull) wordt aangehaald vanuit de koppelingspecificatie met planning, vanuit de payload-specificatie en straks vanuit een scenario. Alle drie halen hetzelfde ID aan.

*Acceptatie.* Voor elk soort artefact in de tabel van §1 is aanwijsbaar welk veld het ID draagt, en er is geen artefact met twee ID's.

### R2 — Een ID wordt nooit hergebruikt

Een uitgegeven ID MOET permanent aan hetzelfde ding gebonden blijven, ook nadat dat ding is vervallen. Gaten in de reeks zijn toegestaan en verwacht.

*Voorbeeld.* Wordt begrip 014 vervangen door een nieuwe opzet, dan krijgt de opvolger nummer 041 en blijft 014 bestaan met de status vervallen. Nummer 014 komt nooit terug op iets anders.

*Acceptatie.* Een controle meldt het als een ID in het register verdwijnt of van betekenis wisselt ten opzichte van de vorige versie.

*Herkomst.* Dit volgt de vastgelegde praktijk bij Geonovum: *"Design rules have unique and permanent numbers. In the event of design rules being deprecated or restructured, they are removed from the list. Therefore, gaps in the sequence can occur."* ([bron](https://github.com/Geonovum/KP-APIs/blob/master/API-strategie-governance/APIDesignRuleNumbering.md)). Wij wijken op één punt af: bij Geonovum verdwijnt de vervallen regel uit de lijst, bij ons blijft hij staan met status en opvolger. Zie R11.

### R3 — Identiteit staat los van naam

Het deel van het ID dat de identiteit draagt MOET ongewijzigd blijven wanneer de naam of omschrijving van het artefact wijzigt.

*EARS.* WANNEER een begrip wordt hernoemd, MOET het identificerende deel van zijn ID ongewijzigd blijven.

*Voorbeeld.* Heet `Leeronderdeel-specificatie` morgen `Leeractiviteit-specificatie`, dan blijven alle bestaande verwijzingen geldig zonder één document aan te passen.

*Acceptatie.* Een naamswijziging in het register leidt tot nul wijzigingen in verwijzende documenten.

### R4 — Leesbaar zonder register

Een ID MOET in de context waarin het voorkomt te begrijpen zijn zonder het register erbij te pakken.

*Voorbeeld.* Een verwijzing moet zeggen wat voor soort ding wordt aangehaald. `S4` doet dat niet: dat kan een stroom, een stap of een systeem zijn.

*Acceptatie.* Leg een willekeurige verwijzing voor aan iemand die het register niet kent; die kan zeggen wat voor soort ding het is en waar het ongeveer over gaat.

### R5 — Machinaal herkenbaar

Een ID MOET met één reguliere expressie uit vrije tekst, uit JSON en uit een codeblok te halen zijn.

*Acceptatie.* Eén patroon vindt alle ID's in de repository, zonder valse treffers op koppen, ankers, hexkleuren of versienummers.

*Aandachtspunt.* De bestaande issue-controle in `check-conventies.py` laat zien hoe fout dit kan gaan: het patroon daar mist `(#119)` doordat een haakje ervoor wordt uitgesloten. Het ID-patroon moet expliciet op zulke randgevallen worden getoetst.

### R6 — De soort is af te lezen

Uit het ID zelf MOET blijken om wat voor soort artefact het gaat.

*Voorbeeld.* Aan `R7` is niet te zien of het een requirement uit het keuzedocument is of uit een ander document. Aan een ID met een soortaanduiding vooraan wel.

*Acceptatie.* Er bestaan geen twee soorten artefacten waarvan de ID's dezelfde vorm hebben.

### R7 — Een ID identificeert over documentgrenzen heen

Een ID MOET binnen de hele repository naar precies één artefact wijzen. Een nummering die alleen binnen één document uniek is, is geen ID.

*Voorbeeld.* Dit document nummert zijn eisen R1 tot en met R13. Het requirements-document *keuzes rond onderwijsspecificaties* doet dat ook, met R1 tot en met R17. `R7` wijst dus naar twee verschillende dingen. Zonder aanvullende aanduiding kan geen payload, geen schema en geen scenario naar "R7" verwijzen.

*Acceptatie.* Voor elk ID in de repository geldt dat een zoekopdracht op dat ID precies één declaratie oplevert.

*Gevolg.* De conventie moet aangeven welke artefacten een geregistreerd ID krijgen en welke met documentlokale nummering toe kunnen. Niet elk genummerd ding hoeft een ID te zijn.

### R8 — Ruimte voor voorlopen op MORA

Het register MOET kunnen vastleggen dat een begrip nog geen equivalent in MORA heeft, onderscheiden van "nog niet ingevuld".

*Voorbeeld.* `Leergelegenheid` bestaat bij ons en staat nog niet in de MORA-omgeving. Dat is een bewuste stand van zaken, geen omissie, en het is tegelijk invoer voor klus 53.

*Acceptatie.* Er zijn ten minste drie onderscheiden waarden mogelijk: een verwijzing, "bestaat niet in MORA", en "nog niet nagelopen". Een overzicht van alle begrippen zonder MORA-equivalent is met één opdracht te maken.

### R9 — Uitgifte zonder centrale coördinatie

Een nieuw ID MOET uitgegeven kunnen worden door de bijdrager zelf, zonder een beheerder te vragen.

*Voorbeeld.* Wie een begrip toevoegt, kijkt in het register wat het hoogste nummer is en neemt het volgende.

*Acceptatie.* Twee bijdragers die in verschillende branches hetzelfde ID uitgeven, worden door de uniciteitscontrole gemeld. Git vangt dit niet: bij losse bestanden per artefact voegt de merge beide toe zonder conflict.

### R10 — Dubbelen en dode verwijzingen worden gedetecteerd

Elk dubbel ID en elke verwijzing naar een niet-bestaand ID MOET machinaal worden gemeld, met exitcode 1.

*Acceptatie.* Een testgeval met een bewust dubbel ID en een testgeval met een bewuste dode verwijzing falen allebei.

### R11 — Vervallen ID's blijven vindbaar

Een vervallen ID MOET in het register blijven staan, met zijn status en waar van toepassing zijn opvolger.

*Voorbeeld.* Iemand leest een specificatie uit 2026 die naar begrip 014 verwijst en moet in 2029 kunnen achterhalen wat daarmee is gebeurd.

*Acceptatie.* Voor elk vervallen ID is de opvolger of de reden van vervallen in het register te vinden.

### R12 — Het register is de bron

Voor elk soort artefact MOET één register de gezaghebbende lijst van ID's zijn; documenten verwijzen ernaar en houden geen eigen lijst bij.

*Acceptatie.* Er is geen tweede plek waar dezelfde ID-lijst wordt bijgehouden.

### R13 — De vorm belast het document niet

Een ID in de lopende tekst MOET leesbaar blijven voor wie de conventie niet kent, en MAG de weergave op GitHub of in een PDF-export niet verstoren.

*Voorbeeld.* Een gereleased document wordt gelezen door een architect bij een instelling die niets van onze conventie weet. Ziet die pagina eruit als een technisch logbestand, dan is de eis niet gehaald.

*Acceptatie.* Leg een gerenderde pagina met ID's voor aan iemand van buiten; die noemt de ID's niet als storend.

## 3. Wat buiten scope valt

- **Welk gereedschap** de controle uitvoert. De conventie moet met een eigen script van beperkte omvang te controleren zijn; of we later OpenFastTrace of iets anders gebruiken is een aparte afweging.
- **Het aanleggen van de registers zelf.** Dit document stelt eisen aan de vorm, niet aan de inhoud.
- **Welke artefacten een ID krijgen.** Dat volgt uit de registers; hier staat alleen wat een ID moet kunnen zodra het bestaat.
- **De koppeling naar HORA en OEAPI.** Dezelfde mechaniek als de MORA-verwijzing uit R8, maar de invulling is inhoudelijk werk.

## 4. Open vragen voor het kernteam

| Vraag | Waarom het uitmaakt |
|---|---|
| Is het identificerende deel het nummer, of de hele tekenreeks inclusief de naam? | Bepaalt of hernoemen gratis is (R3) of een nieuw ID kost |
| Nummeren we per soort of doorlopend over alles heen? | Per soort leest prettiger; doorlopend maakt een ID uniek zonder de soortaanduiding |
| Geldt de conventie ook voor ADR's, die al een eigen vierciiferige nummering hebben? | Uniformiteit tegenover R7 |
| Wie stelt vast dat een begrip vervalt? | R11 veronderstelt een besluitmoment; nu is dat nergens belegd |

## 5. Acceptatie

Vastgesteld door het kernteam OKx. Dit document is geslaagd wanneer twee mensen onafhankelijk van elkaar bij dezelfde voorgestelde conventie tot hetzelfde oordeel komen over of eraan is voldaan.
