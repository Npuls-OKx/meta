# PoC: de interne uitwisseling van een instelling naast de OKx-doorloop

RijnIJssel levert vier JSON-berichten aan waarmee haar onderwijscatalogus de rest van haar landschap voedt. Die berichten zijn hier het randgeval waarmee de OKx-doorloop wordt getoetst: wat dekt de grootst gemene deler al, en wat blijft lokale variant. De uitwerking loopt in [Npuls-OKx/meta#522](https://github.com/Npuls-OKx/meta/issues/522).

## De vier berichten

Alle vier dragen dezelfde envelop, `opleidingseenheid`, met hetzelfde kopblok: opleidingscode, crebo, naam, niveau, onderwijstype, waarderoute, cohort, versie en een PeopleSoft-sleutel. Wat erin zit verschilt per ontvangend systeem.

| Bericht | Opleiding | Wat het draagt |
|---|---|---|
| [`sbis.json`](RijnIJssel/sbis.json) | DV127058, Leidinggevende Tourism | kwalificatiedossier, 36 opleidingsonderdelen met 115 leertaken, 3 beroepstaken, 42 leereenheden, 32 roosterbare eenheden, rubrieken, een leeg examenplan |
| [`peoplesoft.json`](RijnIJssel/peoplesoft.json) | DV127140, Leidinggevende facilitaire dienstverlening | kwalificatiedossier, 27 opleidingsonderdelen zonder leertaken, 4 beroepstaken, 69 rubrieken op leertaakniveau, 1 examenitem |
| [`xedule.json`](RijnIJssel/xedule.json) | DV127140, dezelfde | 27 opleidingsonderdelen, woordelijk gelijk aan die in `peoplesoft.json`, en een lege lijst roosterbare eenheden |
| [`peilstok.json`](RijnIJssel/peilstok.json) | DV127140, dezelfde | alleen rubrieken, woordelijk gelijk aan die in `peoplesoft.json` |

Drie berichten beschrijven dus dezelfde opleiding vanuit drie systemen; het vierde is een ander voorbeeld.

## De platen

| Beeld | Wat het toont |
|---|---|
| [`indeling-sbis.svg`](img/indeling-sbis.svg) | De indeling van het SBIS-bericht, als JSON-viewer |
| [`indeling-peoplesoft.svg`](img/indeling-peoplesoft.svg) | Dezelfde envelop, zonder leereenheden en zonder roosterbare eenheden |
| [`indeling-xedule.svg`](img/indeling-xedule.svg) | Alleen de opleidingsonderdelen, en nul roosterbare eenheden |
| [`indeling-peilstok.svg`](img/indeling-peilstok.svg) | Alleen de rubrieken, en daarvan alleen die op leertaakniveau |
| [`okx-overlap-catalogus-naar-drie-systemen.svg`](img/okx-overlap-catalogus-naar-drie-systemen.svg) | Waar de berichten de hoofdplaat raken: OC-LMS, OC-P&R en OC-KRS gemarkeerd |
| [`kruisverband-leereenheid-opleidingsonderdeel.svg`](img/kruisverband-leereenheid-opleidingsonderdeel.svg) | Welke leereenheid uit welk opleidingsonderdeel put: 42 bij 36, met 106 verbindingen |

Hertekenen na een nieuwe aanlevering:

```bash
for n in sbis peoplesoft xedule peilstok; do
  python3 tools/scripts/teken-json-structuur.py \
    --bron architecture/docs/onderzoek/PoC/RijnIJssel/$n.json \
    --uit architecture/docs/onderzoek/PoC/img/indeling-$n.svg \
    --titel "Indeling van het $n-bericht" --versie 0.1.0 --diepte 3 --waarden
done

python3 tools/scripts/teken-hoofdplaat-highlight.py \
  --koppelingen "OC-LMS,OC-P&R,OC-KRS" --uitsnede --haaks --lucht 8 \
  --uit architecture/docs/onderzoek/PoC/img/

python3 tools/scripts/teken-kruisverband.py \
  --selectie architecture/docs/onderzoek/PoC/kruisverbanden/sbis-leereenheid-opleidingsonderdeel.json \
  --uit architecture/docs/onderzoek/PoC/img/kruisverband-leereenheid-opleidingsonderdeel.svg
```

De werkwijze staat in de skill [okx-json-bericht-in-beeld](../../../../.agents/skills/okx-json-bericht-in-beeld/SKILL.md). De platen dragen hier wel de waarden van het kopblok, omdat RijnIJssel heeft gezegd dat de bestanden openbaar mogen.

## Waar dit op aansluit

De tegenhanger in de eigen uitwerking is doorloopstap **F4-02**, `Onderwijscatalogus naar Leer management systeem`, in de [modeldoorloop van Jochem](../../../model/informatiemodel/modeldoorloop-leerroute-1-jochem.md). Daar draagt de stroom de leeronderdeel-, les- en toetsonderdeelspecificatie plus de formatieve resultaatstructuur. De berichten hier dragen daarnaast de planning, die in OKx over OC-P&R loopt, en de administratieve kant, die over OC-KRS loopt.

Welk systeem de berichten maakt en wanneer zij gaan is nog niet bekend; die vragen staan uit bij de inbrenger. Tot die antwoorden er zijn is de richting op de uitsnede een aanname en geen vastgesteld feit.
