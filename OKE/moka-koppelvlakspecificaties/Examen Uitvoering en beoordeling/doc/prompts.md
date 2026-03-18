# Prompts voor MOKA koppelvlak specificaties

Dit bestand legt de belangrijkste, resultaathoudende prompts vast die de essentie van de werkwijze en iteraties vastleggen. Gebruik ze als geaggregeerde, consistente instructies voor volgende sessies.

---

## 1. Referentie klassendiagram ↔ informatiemodel (semantische 1-op-1)

**Prompt:**  
Zorg dat het referentie klassendiagram **100% semantisch overeenkomt** met het informatiemodel (InformatiemodelOverzicht.json / koppelvlak specifiek informatiemodel view). Werk het **hele** klassendiagram bij volgens deze methodiek: gebruik de **exacte gegevensgroeptype-namen** uit het informatiemodel als interne secties (met `--` in Mermaid); onder elk gegevensgroeptype de bijbehorende **referentie-attributen** (zoals bij Zittingsverslag: VerslagTotStandkoming → toelichting, onregelmatigheden; RelatieTotOpsteller → medewerkerId; RelatieTotExamenAfname → examenZittingId). Verwijder tabellen met aantallen gegevensgroeptypes. Label relaties tussen klassen waar van toepassing met de **gegevensgroeptype-naam** (bijv. RelatieTotExamenAfname, RelatieTotOpsteller). Neem elk informatieobject uit het informatiemodel op (inclusief Examen deelname, Beoordelaar).

---

## 2. OKE-attributen en apart overzicht

**Prompt:**  
Vul de gegevensgroeptypes die in het informatiemodel staan aan met belangrijke **OKE-attributen** (Nederlandse vertaling), gebaseerd op de OKE MBO-toetsafname specificatie. Maak een **apart overzicht** (bijv. OKE_Gegevensgroeptypes_Overzicht.md) met per gegevensgroep de gegevensgroeptypes en de OKE-bron (Person, ComponentOffering, Result, Document, enz.) met attributen in het Nederlands. Voeg eventuele gegevensgroeptypes die uit OKE passen binnen de gegevensgroepen van het informatiemodel toe en maak daar een apart overzicht van. In het hoofddocument alleen een korte verwijzing naar dit overzicht bij het informatiemodel en bij het referentie klassendiagram; geen OKE-terminologie in de kerntekst.

---

## 3. OKE vs. informatiemodel – analyse voor volgende iteratie

**Prompt:**  
Vergelijk de OKE-specificatie met het informatiemodel. Maak een **apart markdown-document** (bijv. OKE_Informatiemodel_Analyse.md) met een analyse waarin: (1) **potentiële gemiste gegevensgroeptypes** worden benoemd op basis van OKE-attributen die nog niet als gegevensgroeptype in het informatiemodel staan; (2) per item de **processcope** wordt aangegeven (bijv. Voorbereiden uitvoering examen, Uitvoeren examen, Beoordelen examen, Vaststellen resultaat, Diplomeren/certificeren). Dit is een losse analyse voor een volgende iteratie; niet opnemen in de kerntekst van de koppelvlak specificatie.

---

## 4. Relaties in klassendiagram benoemen met gegevensgroeptypes

**Prompt:**  
Zorg dat in het referentie klassendiagram de **relatie tot de in het informatiemodel benoemde gegevensgroeptypes** expliciet terugkomt: elke relatie tussen klassen die overeenkomt met een gegevensgroeptype moet gelabeld zijn met die **gegevensgroeptype-naam** (niet met aantallen). Voorbeeld: Zittingsverslag → Medewerker : RelatieTotOpsteller; Zittingsverslag → Examenafname : RelatieTotExamenAfname; SummatieveBeoordeling → Beoordelaar : RelatieTotBeoordelaar; Onderwijsresultaat → Examendossier : OnderwijsresultaatRegistratie.

---

## 5. Procesplaatsing en scope (MORA)

**Prompt:**  
Beschrijf de MORA procesplaatsing voor het koppelvlak: de procesketen Examineren (uitvoeren examen tot en met diplomeren/certificeren) met alle subprocesstappen. Geef "Diplomeren en certificeren" weer als **overkoepelende stap** met sub-stappen (bepalen diploma/certificaat recht, besluiten diplomeren/certificeren, diplomeren/certificeren), bij voorkeur in een Mermaid-subgraph. Vermeld expliciet wat **buiten scope** valt (bijv. Afgeven mbo-verklaring).

---

## 6. ContextRules en werkwijze bijwerken

**Prompt:**  
Verwerk de inzichten uit onze conversatie in ContextRules.md: regels voor de koppeling informatiemodel ↔ klassendiagram (exacte gegevensgroeptype-namen, referentie-attributen, geen aantallen, relatielabels), omgang met OKE (apart overzicht, Nederlandse vertaling, aparte OKE-analyse), en procesplaatsing (Diplomeren en certificeren als overkoepelende stap, buiten scope benoemen). Schrijf de belangrijkste resultaathoudende prompts geaggregeerd en consistent naar prompts.md.

---

## 7. Template vs. voorbeelduitwerking

**Prompt:**  
Houd twee documenttypen strikt gescheiden: (1) **Template** – generiek, herhaalbaar, met placeholders en instructies per sectie; referentie onderin naar een voorbeelduitwerking. (2) **Voorbeelduitwerking** – concrete invulling van het template voor één koppelvlak/deelproces (bijv. Examen uitvoering en beoordeling). Alleen MORA/datamodel-terminologie in de kerntekst; view en viewpoint niet door elkaar halen; bij elke view één viewpointbeschrijving.

---

## 8. View, viewpoint en legenda

**Prompt:**  
Gebruik "view" alleen voor het concreet diagram of de plaat; "viewpoint" voor het kader (doel, concerns, scope, modeltaal, objecttypen/relaties, verantwoording). Bij elke view hoort één viewpointbeschrijving. Voeg bij afbeeldingen een figuurcaption, korte viewpointbeschrijving en legenda met ArchiMate-objecten toe.

---

*Laatste bijwerking: na iteratie klassendiagram (gegevensgroeptype-methodiek), OKE-overzicht, OKE-analyse en ContextRules/prompts.*
