Maak een OKx-presentatie of update-deck. $ARGUMENTS

Volg de skill [`okx-presentatie`](../../.agents/skills/okx-presentatie/SKILL.md) stap voor stap.

Vraag eerst **voor welk gremium** en **welke periode**, tenzij dat al uit de opdracht blijkt.

## Inventariseer, en stem daarna af

Ga niet meteen schrijven. Verzamel eerst wat er is gebeurd, en **leg de inhoud voor** aan degene die het deck vraagt:

1. Draai `python3 scripts/wijzigingen-verzamelen.py --sinds JJJJ-MM-DD` en lees de pull request-beschrijvingen en de gewijzigde documenten.
2. Draai `python3 scripts/platen-inventariseren.py` en lees `presentaties/platen.json`, zodat je weet welk beeld beschikbaar is voordat je onderwerpen kiest.
3. Groepeer wat je vindt in **drie tot zes onderwerpen**, met per onderwerp een zin over wat het betekent **en welke plaat je erbij wilt zetten**.
4. Leg die lijst voor: *"dit zag ik gebeuren, hier wil ik het over hebben, met dit beeld erbij — klopt dat?"* Noem er expliciet bij wat je zou **weglaten** en waarom, en bij welk onderwerp je geen passende plaat kon vinden.
5. Wacht op het antwoord. Wat technisch de grootste wijziging is, is zelden waar het gesprek over moet gaan; alleen de aanvrager weet wat er maandag op tafel moet, en welke plaat er vorige keer vragen opriep.

Pas als de onderwerpen vaststaan ga je schrijven.

Daarna:

- Verzamel de wijzigingen uit **beide** repositories, `Npuls-OKx/meta` en `Npuls-OKx/Public`. Lees niet alleen de titels: open de gewijzigde documenten en de pull request-beschrijvingen, want daar staat de aanleiding.
- Groepeer per **thema**, niet per repository of per pull request.
- Vertaal elke wijziging naar wat er nu mogelijk is dat eerst niet kon.
- Bouw het deck met de `np-`-componenten uit `presentaties/src/style.css`; verzin geen losse inline-stijlen waar een class bestaat.
- **Neem tabellen, cijfers en citaten letterlijk over uit de bron.** Bouw een tabel nooit uit je hoofd na; open het bestand en kopieer hem. Een verzonnen kolom in een ankertabel ondermijnt het hele deck.
- **Schrijf over de zaak, niet tegen de zaal.** Geen "u", "je" of "jullie", ook niet in koppen en bijschriften; het onderwerp is het grammaticale onderwerp. "Waar we jullie voor nodig hebben" wordt **Besluit nodig op**. Gebruik "we" alleen waar het programma echt de handelende partij is, en formuleer een oordeel als *risico*, *aanname* of *inschatting* in plaats van als "ik denk".
- **Vraag een besluit in vaste vorm**: *Besluit nodig op / Door / Voor / Opties*. Zelfde voor *Review gevraagd op* en *Ter kennisname*. Nooit een besluit wegstoppen in een lopende zin.
- **Stem het register af op het gremium.** Intern (SI-team, adviesgroep, programma- en projectleiding) is relatief informeel binnen zakelijke normen: korte zinnen, gewone woorden. Extern (kerngroep techniek OKx, technische werkgroep OEAPI, leveranciers, instellingen) is formeler en preciezer, met bij elke uitspraak de status erbij: vastgesteld, concept of voorstel. Het verschil tussen adviesgroep en leiding zit in de **diepgang**, niet in het register.
- **Gebruik de termen uit de bron.** Verzin geen vriendelijker klinkende variant voor een systeem of begrip. Het is LMS, SIS (dat is KRS plus SVS), onderwijscatalogus; niet "leeromgeving" of "studentadministratie" als het systeem bedoeld is. Twijfel je: zoek de term op in de instap van Koppelvlakspecificaties.
- **Show, don't tell, zonder dat iemand erom vraagt.** Elke inhoudelijke uitleg krijgt beeld. Kies zelf een passende plaat uit `presentaties/platen.json` op het veld `gebruik_bij`, kopieer hem naar `presentaties/src/public/platen/` en zet er een regel bij die zegt waar de kijker naar moet kijken. Staat er in `let_op` een voorbehoud, meld dat aan de aanvrager. Voeg een nieuwe of nieuwere plaat toe aan het manifest, met `--bijwerken` voor de hashes.
- **Scheid feit van inschatting.** Wat uit de repositories komt is feit; wat jij ervan vindt is een oordeel. Meld aan het eind welke uitspraken van jou zijn.
- Sla het op in `presentaties/src/JJMMDD_onderwerp.md`, nooit in de Public-werkmap.

Sluit af met **het resultaat laten zien**, niet met een mededeling dat het klaar is:

1. Draai `./deck <onderwerp> beelden` in `presentaties/`.
2. Bekijk de afbeeldingen zelf, in elk geval de slides met een tabel of veel tekst; los overflow op voordat je oplevert.
3. Toon de gebruiker een of twee slides, en geef daarna het commando `./deck <onderwerp>` om het deck zelf te openen.

Verzin geen voortgang. Elke bewering in het deck moet terug te voeren zijn op iets in een van beide repositories; kun je iets niet staven, laat het weg of benoem het als open punt.
