Maak een OKx-presentatie of update-deck. $ARGUMENTS

Volg de skill [`okx-presentatie`](../../.agents/skills/okx-presentatie/SKILL.md) stap voor stap.

Vraag eerst **voor welk gremium** en **welke periode**, tenzij dat al uit de opdracht blijkt.

## Inventariseer, en stem daarna af

Ga niet meteen schrijven. Verzamel eerst wat er is gebeurd, en **leg de inhoud voor** aan degene die het deck vraagt:

1. Draai `python3 scripts/wijzigingen-verzamelen.py --sinds JJJJ-MM-DD` en lees de pull request-beschrijvingen en de gewijzigde documenten.
2. Groepeer wat je vindt in **drie tot zes onderwerpen**, met per onderwerp een zin over wat het betekent.
3. Leg die lijst voor: *"dit zag ik gebeuren, hier wil ik het over hebben, klopt dat?"* Noem er expliciet bij wat je zou **weglaten** en waarom.
4. Wacht op het antwoord. Wat technisch de grootste wijziging is, is zelden waar het gesprek over moet gaan; alleen de aanvrager weet wat er maandag op tafel moet.

Pas als de onderwerpen vaststaan ga je schrijven.

Daarna:

- Verzamel de wijzigingen uit **beide** repositories, `Npuls-OKx/meta` en `Npuls-OKx/Public`. Lees niet alleen de titels: open de gewijzigde documenten en de pull request-beschrijvingen, want daar staat de aanleiding.
- Groepeer per **thema**, niet per repository of per pull request.
- Vertaal elke wijziging naar wat er nu mogelijk is dat eerst niet kon.
- Bouw het deck met de `np-`-componenten uit `presentaties/style.css`; verzin geen losse inline-stijlen waar een class bestaat.
- **Neem tabellen, cijfers en citaten letterlijk over uit de bron.** Bouw een tabel nooit uit je hoofd na; open het bestand en kopieer hem. Een verzonnen kolom in een ankertabel ondermijnt het hele deck.
- **Stem de toon af op het gremium.** Zowel programma- en projectleiding als de adviesgroep zijn interne gremia: informeel en direct, alsof je het een collega vertelt. Geen plechtige formuleringen. Het verschil zit in de **diepgang**, niet in de toon: de adviesgroep krijgt meer uitleg per stap, de leiding minder detail.
- **Gebruik de termen uit de bron.** Verzin geen vriendelijker klinkende variant voor een systeem of begrip. Het is LMS, SIS (dat is KRS plus SVS), onderwijscatalogus; niet "leeromgeving" of "studentadministratie" als het systeem bedoeld is. Twijfel je: zoek de term op in de instap van Koppelvlakspecificaties.
- **Show, don't tell.** OKx heeft architectuurplaten; gebruik die in plaats van een eigen diagram. De informatiestromenplaat van leerroute 1, de leerroutes, de hoofdplaat en de koppelvlakviews per component staan in beide repositories. Kopieer wat je gebruikt naar `presentaties/public/platen/` en zet er een regel bij die zegt waar de kijker naar moet kijken.
- **Scheid feit van inschatting.** Wat uit de repositories komt is feit; wat jij ervan vindt is een oordeel. Meld aan het eind welke uitspraken van jou zijn.
- Sla het op in `presentaties/JJMMDD_onderwerp.md`, nooit in de Public-werkmap.

Sluit af met **het resultaat laten zien**, niet met een mededeling dat het klaar is:

1. Draai `./deck <onderwerp> beelden` in `presentaties/`.
2. Bekijk de afbeeldingen zelf, in elk geval de slides met een tabel of veel tekst; los overflow op voordat je oplevert.
3. Toon de gebruiker een of twee slides, en geef daarna het commando `./deck <onderwerp>` om het deck zelf te openen.

Verzin geen voortgang. Elke bewering in het deck moet terug te voeren zijn op iets in een van beide repositories; kun je iets niet staven, laat het weg of benoem het als open punt.
