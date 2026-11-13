# Modelversie terugvinden

Zet het ArchiMate-model terug op de staat achter een uitgebrachte plaatversie, of zoek op welke commit een plaat is gemaakt. Gebruik dit wanneer iemand vraagt "hoe zag de hoofdplaat er bij v1.6 uit" of "zet me op het model van informatiemodel v0.1".

## Waarom dit een commando is

De viewnamen in het model dragen geen versie. De versie hangt aan de **export**, want dat is wat Public aanhaalt. De brug tussen die twee is [`architecture/model/informatiestromen hoofdplaat OKx/herkomst.json`](../../architecture/model/informatiestromen%20hoofdplaat%20OKx/herkomst.json): per uitgebrachte versie de commit, de viewnaam zoals die toen heette, en een hash over de inhoud van de view.

Zonder dat manifest is een oude versie alleen op datum terug te vinden, en dat is gokwerk.

## Aanpak

1. **Lees het manifest.**

   ```bash
   python3 -c "import json;[print(f\"{v['versie']:7s} {v['herkomst']:12s} {v['commit']}\") for v in json.load(open('architecture/model/informatiestromen hoofdplaat OKx/herkomst.json'))['versies']]"
   ```

   Drie soorten herkomst, en zij zeggen hoe hard de verwijzing is:

   | `herkomst` | Betekenis |
   |---|---|
   | `vastgelegd bij export` | op het moment van exporteren geschreven; dit is de echte verwijzing |
   | `nagemeten` | achteraf gereconstrueerd uit de modelstaat van die commit |
   | `onbekend` | geen modelstaat gevonden; alleen de afbeelding bestaat |

2. **Zet het model terug, zonder je tak te verlaten.**

   ```bash
   git checkout <commit> -- architecture/model/model.archimate
   ```

   **Sluit Archi eerst.** Archi houdt het bestand in geheugen en schrijft bij het opslaan zijn eigen versie er weer overheen.

3. **Terug naar de huidige staat:**

   ```bash
   git restore architecture/model/model.archimate
   ```

4. **Staat de gevraagde versie niet in het manifest**, zoek dan op datum en zeg erbij dat het een benadering is:

   ```bash
   git log --format="%H %ad %s" --date=short -- architecture/model/model.archimate
   ```

   Noem in het antwoord altijd dat dit op datum is gevonden en niet op een vastgelegde verwijzing.

## Harde regels

- **Noem altijd de volledige veertigtekenhash**, nooit een afkorting. Git schaalt zijn afkortlengte mee met het aantal objecten in de repository; in deze repository staat die al op acht tekens. Een afkorting die vandaag uniek is, hoeft dat over een jaar niet te zijn, en een verwijzing in een manifest of in een document moet jaren mee.
- **Raak het `.archimate`-bestand niet aan** anders dan met `git checkout` of `git restore` van een hele versie; zie harde regel 1 in [AGENTS.md](../../AGENTS.md).
- Een versie die als `onbekend` staat, is niet te herleiden. Zeg dat, in plaats van een commit te noemen die er toevallig omheen ligt.

## Een versie vastleggen

Na een nieuwe export:

```bash
python3 tools/scripts/plaatherkomst.py --schrijf --versie 1.7.1
```

De controle hangt in `tools/tests/test_plaatherkomst.py` en loopt mee in CI: wijzigt de view zonder dat er een nieuwe export is, dan faalt de pull request.
