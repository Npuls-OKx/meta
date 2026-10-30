# Voorbeelduitwerking leerroute 1: het voorwerk van september 2026

Dit is de verantwoording onder de voorbeelduitwerking van Jochem: de analyse per laag van 16 september 2026, het plan dat daaruit volgde, en de vormtaal die in een proefopstelling is bepaald. Het werk zelf staat elders; dit artifact zegt **waarom het voorbeeld deze vorm heeft**.

De kerngroep techniek vroeg op 15 september 2026 om een opleiding helemaal uit te drukken in het informatiemodel, van abstract naar implementatie, zodat blijkt of iedereen het over hetzelfde heeft. Voordat er iets gebouwd werd, is eerst uitgezocht of dat kon.

**Status: afgesloten.** Het plan is op 18 september 2026 goedgekeurd door de modelleur en uitgevoerd tot de kerngroep van 30 september. Waar het werk verdergaat staat onderaan.

## Wat hier ligt

| Bestand | Wat het draagt |
|---|---|
| [laag-1-proces.md](laag-1-proces.md) | Kaderscenario, persona en scenario: journeystappen, fasen, MORA-processen, ankertabel, specificatieboom |
| [laag-2-componenten-en-diensten.md](laag-2-componenten-en-diensten.md) | Referentiecomponenten en koppelvlakdiensten, met en zonder contract |
| [laag-3-berichtstromen.md](laag-3-berichtstromen.md) | De elf berichtstromen in drie koppelingen, en hun interactiepatronen |
| [laag-4-datamodellen.md](laag-4-datamodellen.md) | Entiteiten, schema's en de voorbeeldpayloads met hun id-keten |
| [laag-5-informatiemodel.md](laag-5-informatiemodel.md) | De 66 objecttypen in zeven families, de relaties en de ontwerpkeuzes |
| [laag-6-verbinding.md](laag-6-verbinding.md) | Wat de lagen aan elkaar bindt, en welke naden niet zijn vastgelegd |
| [plan.md](plan.md) | Het plan van aanpak, versie 3. Sectie 6 draagt twintig besluiten en aannames, sectie 9 wat de tegenlezing veranderde |
| [bron/](bron/) | De vormtaal uit de proefopstelling: een blok dat ontstaat en een blok dat stroomt, elk met de JSON waaruit het is getekend |

## De conclusie van de analyse, in een zin

Een opleiding helemaal uitdrukken lukt **in het informatiemodel**. Het informatiemodel en de bronnen dragen Jochems traject van kwalificatiedossier tot en met het eerste rooster; de koppelvlakspecificatie draagt alleen de inrichting vóór 1 september. Alles wat daarna met Jochem zelf gebeurt, aanmelden, inschrijven, kiezen, resultaat en examen, is in het informatiemodel wel een objecttype en in de koppelvlakspecificatie nog niets.

Het voorbeeld laat dat verschil zien. Dat is de belangrijkste uitkomst van het voorwerk, en zij staat ook vooraan in het deliverable.

## Wat van het plan terecht is gekomen

| Het plan vroeg | Wat er staat | Afwijking |
|---|---|---|
| Een instantiebestand als brug tussen informatiemodel en casus, werknaam `instanties.json`, in Npuls-OKx/Public bij de payloads | `architecture/model/informatiemodel/voorbeeld-lr1-regels.json` in meta: 262 regels, 65 beelden, acht fasen | Andere plek en andere naam. De regeltabel landde in meta omdat zij het model en de platen van meta leest; Public draagt het releasepakket |
| Een generator die de tabellen en diagrammen maakt | `teken-voorbeeldregels.py` voor de beelden, `genereer-voorbeeld-lr1.py` voor het document en het invulblad, `snijd-beeld.py` voor de leesbaarheid op een slide | Uitgevoerd, in drie scripts in plaats van een |
| Een controle naast `check-conventies.py`, met vijf toetsen | `controleer-voorbeeldregels.py`, met testgevallen | Uitgevoerd, in meta in plaats van Public |
| Leemtes, aannames en vragen als eersteklas inhoud | De velden `aanname`, `vraag` en `bron` op de regel, en scope-uitzonderingen met motivering | Uitgevoerd zoals bedoeld |
| De vormtaal uit de proefopstelling | De blokvormen uit [bron/](bron/) zitten in `teken-voorbeeldregels.py` | Uitgevoerd |
| Een kaart per stap die **opent bij het koppelvlak**, met de processtap als context eronder | Een beeld per processtap dat opent bij de **objecten** en hun beweging | Omgedraaid. Zie hieronder |

Wat de negen tegenlezingen veranderden staat in sectie 9 van [plan.md](plan.md), per persona met de drie zwaarste punten en waar elk is verwerkt; de losse rapporten zijn daarmee opgenomen in het plan. De proefopstelling is teruggebracht tot de twee blokvormen in [bron/](bron/); de beeldexports eruit zijn opgevolgd door de echte beelden, en de twee proefscripts door `teken-voorbeeldregels.py` en de hoofdplaatscripts.

## Wat het nieuwe doel verandert

Op 2 oktober 2026 is de story van de voorbeelduitwerking herschreven, en dat raakt de oplossingsrichting uit dit plan op drie punten.

**De leesrichting draait om.** Het plan zette het koppelvlak vooraan, met de processtap als context eronder, met als reden dat de kerngroep vroeg om bij het koppelvlak te beginnen. De nieuwe story zet de informatiemanager van een instelling als primaire lezer, die wil zien hoe informatieobjecten ontstaan en zich door het ecosysteem bewegen om zijn eigen informatievoorziening daarop te kunnen mappen. Dan is het object en zijn reis het begin, en is het koppelvlak de uitkomst. De inhoud blijft gelijk, want dezelfde regels dragen beide lezingen. Wat verschuift is wat er bovenaan staat en wat een beeld moet tonen.

**De kolom voor de eigen term wordt de kern.** Het plan had hem al, als lege kolom "uw term" naast het objecttype, en als een van de vijf regels per kaart. Met mappen als doel is dat het punt van het hele product. Daar volgt ook een harde eis uit die het plan niet kende: elk component draagt zijn vaste referentienaam met afkorting, want een instelling kan haar eigen systeem alleen naast een herkenbare component leggen.

**De indeling van het werk verschuift van bouwstappen naar reisdelen.** Het plan knipte het werk in negen werkpakketten, die als issues #239 tot #248 zijn uitgevoerd en op 2 oktober 2026 met bewijs zijn gesloten. In de plaats daarvan staat een indeling per fase van de reis, acht issues met dezelfde tien criteria, plus vijf issues voor de engine eronder en een voor het kaderscenario. De eenheid van oplevering is daarmee een deel van de reis dat een instelling kan mappen; een werkpakket kon alleen de maker aftekenen.

**En er is nu een meetbare poort op de inhoud.** Het plan toetste op volledigheid en op bronvermelding. Daar is een eis bij gekomen die uit het mapdoel volgt: de beelden moeten kloppen met het kaderscenario leerroute 1 in Npuls-OKx/Public, dat met de hand is samengesteld en als waar geldt. De eerste meting daartegen, op 2 oktober 2026, gaf 116 afwijkingen over de acht fasen, naast de 42 reviewbevindingen van Niels van Duin. Dat is precies het soort uitkomst waarvoor het voorbeeld bestaat: fouten die boven water komen voordat iemand ze bouwt.

**Wat onveranderd geldt.** De conclusie van de analyse, de twintig besluiten en aannames uit sectie 6 van het plan, en de vijf dingen die nodig zijn om het informatiemodel aan de leerroute te koppelen. Verschillende van die besluiten staan nog open en zijn door de broncheck opnieuw opgeworpen: de leslaag en ontwerpkeuze 8, de groepen, cohort op de specificatie of op het aanbod, en het intekenen op ongepland aanbod.

## Waar het werk verdergaat

| Waar | Wat |
|---|---|
| Milestone "Voorbeelduitwerking leerroute 1 per fase afmaken" | Acht fase-issues met hun bevindingen en fixplan, vijf engine-issues en een voor het kaderscenario |
| `architecture/model/informatiemodel/voorbeeld-lr1-regels.json` | De regeltabel, de enige bron van het voorbeeld |
| [Kaderscenario leerroute 1 in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/kaderscenario%27s/leerroute-1-regulier.md) | De bron van waarheid over hoe het proces loopt en hoe de informatieobjecten ontstaan |

Relateert aan: #237, Npuls-OKx/Public#106.
