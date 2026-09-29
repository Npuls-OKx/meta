---
name: okx-plaat-uit-het-model
description: Genereer een architectuurplaat uit het ArchiMate-model als SVG, met haakse routering, aanhechtingen op volgorde, het ArchiMate-kleurenschema en een keuring op leesbaarheid. Gebruik wanneer iemand een informatiestromenplaat, hoofdplaat, landschapsplaat of ander overzicht met componenten en lijnen wil tekenen, bijwerken of leesbaarder maken, en wanneer een bestaande plaat te druk of te schuin is om op een slide te tonen.
---

# Een plaat uit het model

Een architectuurplaat met tientallen componenten en lijnen is met de hand niet bij te houden. Zodra de view verandert klopt de tekening niet meer, en een tekening die niet klopt kost meer dan zij oplevert. Deze skill beschrijft hoe zo'n plaat uit de ArchiMate-view wordt gegenereerd en hoe de leesbaarheid aan een poort hangt in plaats van aan oplettendheid.

De maat waar dit over gaat: dertig tot veertig componenten, dertig tot zestig lijnen, getoond op een slide. Voor een plaat met vijf vakken volstaat handwerk.

## Vaste uitgangspunten

- **Het model is de bron.** Lees de view, raak nooit een `*.archimate`-bestand aan (harde regel 1 uit [AGENTS.md](../../../AGENTS.md)), en genereer opnieuw zodra het model verandert.
- **De opzet van de tekenaar blijft staan.** Groeperingen, de onderlinge ligging van de vakken, de geneste diensten en de kanttekeningen zijn het verhaal. Ruimte opentrekken mag, herschikken niet. Wie de ligging verandert, verandert de boodschap.
- **De namen komen uit de view.** Een `labelExpression`-feature draagt de weergavenaam met de regelafbreking die de tekenaar koos; die gaat voor op de elementnaam. Verzin nooit een naam of een thema dat niet in het model staat.
- **Rechte lijnen en hoeken van 90 graden.** Een schuine lijn leest niet op een drukke plaat.

## De volgorde van de stappen

De stappen grijpen op elkaar in; een andere volgorde levert een slechtere plaat.

1. **Vakken op maat.** Een vak dat te klein is voor zijn eigen naam wordt breder en hoger, rond zijn eigen midden. Gebeurt dit later, dan loopt het vak over een baan heen die er al ligt.
2. **Ruimte opentrekken.** Alleen groepen schalen de plek van hun kinderen; een component houdt zijn eigen maat, zodat de diensten erin strak bij hun component blijven. Daarna schuift alles wat elkaar raakt net zover uit elkaar dat er een baan tussen past, langs de as waarin de vakken ten opzichte van elkaar liggen. Zo blijft links links.
3. **Aanhechtingen plannen.** Zie hieronder; dit gebeurt voordat er ook maar een lijn loopt.
4. **Routeren**, kort voor lang, en de losse verbanden na de informatiestromen.
5. **Kleuren en opschriften.**
6. **Keuren**, en pas daarna opleveren.

## De router

Drie vormen, in deze volgorde, en de eerste die past wint:

| vorm | wanneer | hoeken |
|---|---|---|
| recht | de vakken liggen naast of boven elkaar met genoeg overlap | 0 |
| bocht | haaks het ene vak uit, haaks het andere in | 1 |
| baan | een lang been door de ruimte tussen de twee vakken | 2 |

Binnen een vorm kiest een prijs: de afstand tot de gewenste aanhechting, wat het kost om vlak langs een andere lijn te lopen, wat een kruising kost, en als laatste de lengte. Elk gekozen been blijft daarna bezet, zodat een volgende lijn ernaast gaat lopen in plaats van eroverheen. Een vak is een hindernis: een baan die erdoorheen zou lopen valt af.

### Aanhechtingen op volgorde van hun overkant

Dit is de regel met de grootste opbrengst. **Twee lijnen uit hetzelfde vak kruisen elkaar zodra hun aanhechtingen in de verkeerde volgorde staan.** Wie naar rechts moet en links aanhecht, moet de buurvrouw wel passeren. Een router die lijn voor lijn werkt kent die volgorde niet: wie het eerst komt pakt het midden, en de rest schuift ernaast in volgorde van aankomst.

De oplossing: geef de router alle lijnen voordat hij er een tekent. Per vak en per as krijgt elke overkant haar eigen plek op de rand, gesorteerd op waar die overkant zelf ligt. Op de hoofdplaat informatiestromen halveerde dat het aantal kruisingen.

Twee aandachtspunten:

- **Een rechte lijn hecht aan twee vakken tegelijk aan** en heeft dus twee wensen die elkaar kunnen tegenspreken. Zet ze allebei vooraan in de kandidaten en laat de prijs beslissen.
- **Een junctie is te klein voor een volgorde.** Een vak van vijftien bij vijftien heeft geen rand om aanhechtingen op te spreiden; daar blijft een kruising over. Dat is geen fout in de regel.

### De maten die werken

Deze waarden komen uit de hoofdplaat en zijn een bruikbaar vertrekpunt:

- afstand tussen twee banen 24, en 10 als het krap is
- marge tot een vak 12, en een lijn hecht niet binnen 14 van een hoek aan, of binnen een derde van de zijde bij een klein vak
- een hoek weegt zwaar, een kruising ongeveer vijf banen opschuiven, vlak langs een andere lijn lopen ongeveer twee

## Kleuren

Het **ArchiMate-kleurenschema**, zoals Archi een view tekent: de kleur uit de view waar die er staat, en anders die van de laag waar het element toe hoort. Zo blijven de keuzes van de tekenaar overeind, zoals een wit vak voor een component dat buiten het verhaal valt. Vul- en randkleuren per laag staan in `scripts/teken-voorbeeldregels.py`; een randkleur zonder eigen opgave wordt van de vulkleur afgeleid door haar donkerder te maken.

Lijnen zijn de uitzondering. In ArchiMate is een relatie zwart, en dertig zwarte lijnen door elkaar leest niet. Geef een lijn daarom een kleur per bronsysteem, donker genoeg om over een vak van de applicatielaag heen te lezen, met een witte onderlaag eronder zodat een kruising leesbaar blijft.

## Tekst

**Laat de lettermaat meeschalen met de plaat.** Een plaat groter maken zonder de tekst mee te nemen maakt haar slechter leesbaar, niet beter: de verhouding tekst tot breedte daalt. Houd die verhouding rond 0,005 en ten minste 0,0035. Kies per vak de grootste maat waarbij de naam heel binnen het vak past, en wijs een afgebroken naam af in plaats van hem stilletjes af te kappen.

Een opschrift langs een lijn zoekt de eerste vrije plek op het langste been, vanuit het midden, en wijkt zo nodig net naast de lijn. Houd daarbij de vakken, de titelstroken van de groeperingen en de eerder geplaatste opschriften vrij.

## De poort

Leveren gaat via [`scripts/keur-plaat.py`](../../../scripts/keur-plaat.py). Dat harnas leest de SVG terug en meldt wat een plaat onleesbaar maakt: schuine segmenten, tekst buiten het doek, tekst onder de ondergrens, een te ijle verhouding tekst tot plaat, en het aantal kruisende lijnen.

```bash
python3 scripts/keur-plaat.py <plaat>.svg --max-kruisingen <het aantal van nu>
```

Zet het aantal kruisingen van vandaag vast met `--max-kruisingen`, zodat een latere wijziging het niet stilletjes erger maakt. Laat de generator zelf ook haar aantallen afdrukken (componenten, lijnen, schuine segmenten, kruisingen), zodat de winst van een wijziging navolgbaar is.

Daarnaast geldt de vaste werkafspraak: **bekijk de plaat in de vorm waarin de lezer haar krijgt**, dus gerenderd op de slide, niet als XML. Een SVG wordt een PNG met `npx svgexport <plaat>.svg <plaat>.png 2000:`, en een deck levert per slide een beeld met `presentaties/deck <naam> beelden`; zie [okx-presentatie](../okx-presentatie/SKILL.md).

## Valkuilen

- **Een plaat herschikken in plaats van ruimer maken.** Een nieuwe indeling leest voor de tekenaar als een ander verhaal, ook als alle elementen er nog op staan.
- **Ruimte nemen zonder de tekst mee te schalen.** Zie hierboven; dit leest als achteruitgang.
- **Alleen het aantal schuine segmenten meten.** Nul schuine segmenten en dertig kruisingen is nog steeds onleesbaar.
- **Een hoek verkiezen boven een kruising zonder te wegen.** Een extra hoek kost meestal meer dan een kruising; laat de prijs dat beslissen in plaats van een harde regel.
- **Een afgebroken naam accepteren.** "Voorziening Centraal" in plaats van "Voorziening Centraal Aanmelden (CAMBO)" valt pas op als iemand de plaat voorleest.

## Voorbeelden in deze repository

De hoofdplaatscripts landen met #106; wie ze op `dev` niet vindt, kijkt op die branch.

- `scripts/teken-hoofdplaat-ruim.py`: de hoofdplaat informatiestromen uit de view, ruimer opgezet, met een schakelaar voor het opschrift (de stroomnamen of het koppeling-ID).
- `scripts/teken-hoofdplaat-highlight.py`: de router zelf, plus markeringen over een render van de plaat.
- `scripts/teken-voorbeeldregels.py`: de kleuren per ArchiMate-laag.
- `scripts/platen-inventariseren.py`: het manifest dat bijhoudt welke plaat waarvandaan komt.
