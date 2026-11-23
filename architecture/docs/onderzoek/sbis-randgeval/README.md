# SBIS-randgeval: de uitwisseling van een instelling naast de OKx-doorloop

Een instelling levert een JSON-bestand van het bestandstype `SBIS` van haar onderwijscatalogus aan haar leermanagementsysteem, om daar een voortgangsmeter te voeden. Dat bericht is hier het randgeval waarmee de OKx-doorloop wordt getoetst: wat dekt de grootst gemene deler al, en wat blijft lokale variant. De uitwerking loopt in [Npuls-OKx/meta#522](https://github.com/Npuls-OKx/meta/issues/522).

## Wat hier staat

| Beeld | Wat het toont |
|---|---|
| [`sbis-indeling.svg`](img/sbis-indeling.svg) | De indeling van het bericht zoals een JSON-viewer hem toont: per sleutel het type uit RFC 8259 en JSON Schema, het aantal, en bij een lijst elke sleutel die een element draagt |
| [`okx-overlap-oc-lms-en-oc-pr.svg`](img/okx-overlap-oc-lms-en-oc-pr.svg) | Waar dat bericht de hoofdplaat raakt: de koppelingen OC-LMS en OC-P&R gemarkeerd, uitgesneden rond de drie componenten die het betreft |

## Het bericht zelf staat hier nog niet

De plaat met de indeling is getekend uit het aangeleverde bestand, dat buiten dit repository ligt zolang de instelling niet heeft gezegd dat het hier mag landen. Daarom draagt de plaat alleen sleutels, typen en aantallen, en geen waarden: de inhoud van een instelling hoort niet ongevraagd in een publiek repository. De werkwijze staat in de skill [okx-json-bericht-in-beeld](../../../../.agents/skills/okx-json-bericht-in-beeld/SKILL.md).

Zodra dat akkoord er is komt het bestand hiernaast te staan en is de plaat met een enkele aanroep opnieuw te maken:

```bash
python3 tools/scripts/teken-json-structuur.py \
  --bron architecture/docs/onderzoek/sbis-randgeval/sbis.json \
  --uit architecture/docs/onderzoek/sbis-randgeval/img/sbis-indeling.svg \
  --titel "Indeling van het SBIS-bericht" --versie 0.1.0 --diepte 3 \
  --merk beroepstaken,leereenheden,roosterbare_eenheden,rubrics

python3 tools/scripts/teken-hoofdplaat-highlight.py \
  --koppelingen "OC-LMS,OC-P&R" --uitsnede --haaks --lucht 16 \
  --uit architecture/docs/onderzoek/sbis-randgeval/img/
```

## Waar dit op aansluit

De tegenhanger in de eigen uitwerking is doorloopstap **F4-02**, `Onderwijscatalogus naar Leer management systeem`, in de [modeldoorloop van Jochem](../../../model/informatiemodel/modeldoorloop-leerroute-1-jochem.md). Daar draagt de stroom de leeronderdeel-, les- en toetsonderdeelspecificatie plus de formatieve resultaatstructuur. Het SBIS-bericht draagt daarnaast de planning, die in OKx over OC-P&R loopt; vandaar dat beide koppelingen op de uitsnede staan.
