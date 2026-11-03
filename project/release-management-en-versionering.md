# Release en versionering

Meta releaset niets. Hier ontstaat een product en hier itereert het; [Npuls-OKx/Public](https://github.com/Npuls-OKx/Public) draagt de release. Wat daar op `dev` staat is gepubliceerd en leidend, en de regels daarvoor staan in [Release management, algemene regels](https://github.com/Npuls-OKx/Public/blob/dev/Algemeen/release-management/Release-management-algemeen.md): wat een release is, hoe een pakket wordt samengesteld en hoe het wordt gecommuniceerd.

Dit document legt vast wat in meta zelf geldt. De SemVer-conventie hieronder is besloten en wordt afgedwongen; de verhouding tot het releasepakket volgt het document in Public.

## Waar een product landt

| | |
|---|---|
| Meta | De werkplek. Een product ontstaat hier, wordt hier gereviewd en itereert hier. Een wijziging is klaar zodra zij op `dev` staat, en wordt niet apart getagd |
| Public | Het releasepakket, met zijn manifest `release.json`, de werkstroom die het bouwt en het versielabel. Een afnemer bouwt hiertegen |
| De overgang | Een product gaat over zodra een leverancier of een instelling ermee moet bouwen. Laag 1 en 2 van het informatiemodel gaan automatisch mee met `tools/scripts/publiceer-informatiemodel.py` |

Een agent merget nooit op Public, ook niet met groen licht in een gesprek. Zie [`AGENTS.md`](../AGENTS.md).

## SemVer

Alles wat kan landen of dat gaat itereren draagt een versie volgens [SemVer](https://semver.org/lang/nl/): `MAJOR.MINOR.PATCH`.

| Bump | Wanneer |
|---|---|
| Eerste versie | `0.1.0`. Een releasepakket dat nog niemand heeft gezien begint op `0.0.1` |
| Patch | Een correctie die de betekenis niet raakt: een tekstfout, een verduidelijking, een voorbeeld dat klopt |
| Minor | Nieuwe inhoud die niets breekt: een objecttype erbij, een scenario erbij, een optioneel veld |
| Major | Een uitspraak die iets anders zegt dan de vorige versie, waardoor een afnemer moet migreren |

Twee regels eromheen. Zolang iets op `0.x` staat mag een minor breken; dat wordt dan expliciet gemeld. En de zwaarste wijziging bepaalt de bump: een enkele brekende wijziging maakt de hele uitgave een major.

## Wat een versie draagt

| Wat | Waar de versie staat |
|---|---|
| Een plaat of uitsnede | Het veld `versie` in het selectiebestand, en zichtbaar op het beeld: rechts in de voetregel bij een plaat in de Npuls-vormtaal, rechtsboven bij een uitsnede uit het informatiemodel. Draagt de bestandsnaam een aanduiding, dan is dat die versie en geen datum: `sectorketen-v0.2.0.svg` |
| Een releasepakket in Public | Het manifest `release.json` van dat pakket |
| Een koppelvlakspecificatie | Een verwijzing naar een vastgelegde versie van het modellenpakket, onder `afhankelijkheden`. Verhoogt dat pakket zijn versie, dan beweegt die vermelding mee |

Een versie is geen status. Een versie zegt welke uitgave je leest, een status hoe hard de inhoud is; een document kan versie 0.2 dragen en op status 3 staan. De zeven statussen staan in [Status](status.md).

## Afdwinging

`tools/tests/test_plaatversies.py` draait in de werkstroom `model.yml` en laat een pull request falen op drie dingen: een selectiebestand zonder `versie`, een versie die niet op `MAJOR.MINOR.PATCH` lijkt, en een plaat die een andere versie draagt dan haar bron. De regel zelf staat in [`.cursor/rules/architecture-artifacts.mdc`](../.cursor/rules/architecture-artifacts.mdc).

Voor de overige producten is de bump nog handwerk: de indiener stelt hem voor in de pull request, en het team bevestigt hem bij het samenstellen van de release in Public.
