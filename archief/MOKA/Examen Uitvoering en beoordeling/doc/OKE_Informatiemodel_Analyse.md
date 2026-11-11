# Analyse: OKE MBO-toetsafname vs. MOKA informatiemodel

Dit document is een **losse analyse** van de OKE MBO-toetsafname specificatie ten opzichte van het MOKA informatiemodel (InformatiemodelOverzicht.json / koppelvlak specifiek informatiemodel view). Doel: potentiële **gemiste gegevensgroeptypes** (gebaseerd op OKE-attributen) benoemen en aangeven binnen welke **processcope** deze vallen. Deze analyse is bedoeld voor een volgende iteratie om het informatiemodel eventueel aan te vullen.

**Bronnen:**
- [OKE MBO-toetsafname specificatie v1.0 (concept, 9 sept 2024)](https://www.edustandaard.nl/app/uploads/2024/09/OKE-MBO-toetsafname-specs-v1.0_20240909conceptversie.pdf)
- InformatiemodelOverzicht.json (MOKA informatiemodel view)
- MORA procesketen Examineren (uitvoeren examen t/m diplomeren/certificeren)

**Processcopes (MORA, in scope koppelvlak):**
- Voorbereiden uitvoering examen
- Uitvoeren examen
- Beoordelen examen
- Vaststellen resultaat examen
- Bepalen diploma/certificaat recht
- Besluiten diplomeren/certificeren
- Diplomeren/certificeren

---

## 1. Samenvatting bevindingen

In de OKE-specificatie komen objecten en attributen voor die in het huidige informatiemodel niet als apart **gegevensgroeptype** zijn opgenomen. Hieronder staan ze gegroepeerd per **gegevensgroep/informatieobject** waar ze logisch in passen, met de **processcope** waarin ze het meest relevant zijn.

---

## 2. Potentiële gemiste gegevensgroeptypes (op basis van OKE)

### 2.1 Student Gegevens (informatieobject: Student)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **ToegewezenHulpmiddelen** | Person.consumers – assignedNeeds (code, omschrijving, startDatum, eindDatum) | Voorbereiden uitvoering examen / Uitvoeren examen | Voor afname: toegewezen voorzieningen/hulpmiddelen (extra tijd, aangepast materiaal). Nu niet als gegevensgroeptype in Student Gegevens. |

---

### 2.2 Examenafname gegevens (informatieobject: Examenafname)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **Aanbiedingsstatus** | ComponentOffering.consumers – offeringState (actief, geannuleerd) | Voorbereiden uitvoering examen / Uitvoeren examen | Status van de zitting/aanbieding; relevant voor planning en afname. |
| **Resultaatverwachting** | ComponentOffering.consumers – resultExpected, resultValueType | Voorbereiden uitvoering examen | Of en welk type resultaat verwacht wordt bij deze afname. |

---

### 2.3 Zittingsverslag gegevens (informatieobject: Zittingsverslag)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **Documenten** (als gegevensgroeptype) | ComponentOffering.consumers – documents (documentId, documentType, documentNaam) | Beoordelen examen | In het informatiemodel is de koppeling naar documenten wel in het referentieklassendiagram opgenomen, maar niet als expliciet gegevensgroeptype onder Zittingsverslag gegevens. |

---

### 2.4 Te beoordelen werk gegevens (informatieobject: Te beoordelen werk)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **ExtraTijdEnPoging** | ComponentOfferingAssociation.consumers – additionalTimeInMin, attempt, orgAssociationId | Uitvoeren examen / Beoordelen examen | Extra tijd, pogingsnummer en koppeling aan eerdere poging. Nu niet als apart gegevensgroeptype. |
| **PersoonlijkeHulpmiddelen** | ComponentOfferingAssociation.consumers – personalNeeds | Uitvoeren examen | Tijdens afname gebruikte persoonlijke hulpmiddelen. |

---

### 2.5 Examen deelname gegevens (informatieobject: Examen deelname)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **OpleidingsinschrijvingContext** | ComponentOfferingAssociation – programOfferingAssociationId, courseOfferingAssociationId | Voorbereiden uitvoering examen / Uitvoeren examen | Koppeling naar opleidingsinschrijving en deelinschrijving. Nu niet als gegevensgroeptype benoemd. |
| **OrigineleKoppeling** | ComponentOfferingAssociation – orgAssociationId | Uitvoeren examen / Beoordelen examen | Verwijzing naar eerdere poging (bij herkansing). |

---

### 2.6 Summatieve beoordeling gegevens (informatieobject: Summatieve beoordeling)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **OnregelmatighedenBijResultaat** | Result.consumers – irregularities | Beoordelen examen / Vaststellen resultaat examen | Tekstuele vermelding van onregelmatigheden bij het resultaat. Kan naast VerslagTotStandkoming (Zittingsverslag) ook bij het resultaat zelf horen. |
| **Documenten** (als gegevensgroeptype) | Result.consumers – documents | Beoordelen examen / Vaststellen resultaat | In het diagram is documenten opgenomen; niet als apart gegevensgroeptype in Summatieve beoordeling gegevens. |

---

### 2.7 Summatief resultaat gegevens (informatieobject: Summatief resultaat)

| Potentieel gemist gegevensgroeptype | OKE-bron / attributen | Processcope | Toelichting |
|-------------------------------------|------------------------|-------------|-------------|
| **Resultaatgewicht** | Result – weight | Vaststellen resultaat examen / Bepalen diploma recht | Weging van het resultaat t.o.v. andere resultaten. Kan ook in Onderwijsresultaat zitten; OKE kent weight op Result. |
| **Documenten** | Result.consumers – documents | Vaststellen resultaat examen | Bewijsstukken gekoppeld aan het vastgestelde resultaat. |

---

### 2.8 Overige OKE-objecten zonder directe gegevensgroep in het informatiemodel

| OKE-object / -attribuut | Processcope | Toelichting |
|--------------------------|-------------|-------------|
| **Component** (toetsdefinitie) – componentId, name, type, etc. | Voorbereiden uitvoering examen | Het informatiemodel heeft Examenafname (zitting/aanbod) en RelatieTotOpleidingen/componentId, maar geen aparte gegevensgroep “Toetsdefinitie” of “Exameninstrument”. OKE onderscheidt Component (toets) en ComponentOffering (zitting). |
| **Program / ProgramOffering** (opleiding, aanbod) | Voorbereiden uitvoering / gehele keten | RelatieTotOpleidingen en OnderwijsprogrammaContext dekken een deel; OKE heeft expliciete Program- en ProgramOffering-objecten. Eventueel als gegevensgroeptype onder Examenafname of Examendossier. |

---

## 3. Aanbeveling voor volgende iteratie

- **Prioriteit 1 (sterk aan te raden):** Gegevensgroeptypes die direct de keten **uitvoeren examen → beoordelen → vaststellen resultaat** raken: **ToegewezenHulpmiddelen** (Student), **ExtraTijdEnPoging** / **PersoonlijkeHulpmiddelen** (Te beoordelen werk), **OpleidingsinschrijvingContext** / **OrigineleKoppeling** (Examen deelname), **Documenten** en **OnregelmatighedenBijResultaat** bij beoordeling/resultaat.
- **Prioriteit 2:** **Aanbiedingsstatus** en **Resultaatverwachting** (Examenafname) voor betere planbaarheid en status.
- **Prioriteit 3:** Expliciet maken van **Document** als gegevensgroeptype waar van toepassing (Zittingsverslag, Summatieve beoordeling, Summatief resultaat), indien het informatiemodel dit niveau van detaillering wenst.
- **Bewust buiten scope (of later):** Component/Toetsdefinitie en Program/ProgramOffering als aparte informatieobjecten opnemen vergt mogelijk een bredere MOKA/MORA-afstemming.

---

**Status:** Conceptanalyse voor gebruik in volgende iteratie.  
**Datum:** 2026-02-06
