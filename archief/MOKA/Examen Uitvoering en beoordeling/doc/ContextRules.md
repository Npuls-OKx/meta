# Context en werkwijze voor MOKA koppelvlakdocumenten

Dit document legt de context, regels en werkwijze vast voor het opstellen van MOKA koppelvlak specificaties, zodat toekomstige documenten consistent, herhaalbaar en afgebakend zijn.

## Context en scope
- Documenten zijn MORA-gebaseerd, ArchiMate-gericht en implementatie-onafhankelijk.
- Doelgroep is architecten.
- De scope wordt expliciet begrensd tot het procesdeelgebied en de MORA referentiecomponenten die in de platen zijn opgenomen.
- Alleen terminologie uit MORA en de koppelvlakplaten is toegestaan; geen OOAPI/OKE-terminologie of API-termen in de kerntekst.
- Eenduidig taalgebruik en semantiek zijn vereist: één term per begrip; alleen MORA/datamodel-terminologie in de kerntekst.

## Twee documenttypen
- **Template**: generiek, herhaalbaar, richtinggevend document. Bevat placeholders en instructies per sectie (wat invullen, welke modeltaal, welk niveau). Geen domeinspecifieke invulling. Doel: bieden van een template ter invulling en richting voor het beschrijven van sectorkoppelvlakken (waar ook instellingen gebruik van kunnen maken). Onderaan referentie naar een voorbeelduitwerking.
- **Voorbeelduitwerking (invulling)**: concrete instantie van het template voor één koppelvlak of deelproces. Vult alle secties in met domeinspecifieke inhoud. Doel: koppelvlak beschrijven volgens de MOKA-template voor strategische duiding of adaptie/implementatie van logische/technische implementaties. Eenduidige terminologie uit MORA en de platen; geen view en viewpoint door elkaar halen.

## View, viewpoint en viewpointbeschrijving
- **View** = een concreet diagram of plaat (een "product"); de figuur of diagramnaam.
- **Viewpoint** = het kader waarmee een view wordt beschreven: doel, concerns, scope, modeltaal, objecttypen/relaties, verantwoording; vaak aangeduid met type (bijv. "ArchiMate Application Cooperation view").
- **Viewpointbeschrijving** = de tekst die bij een view hoort en het viewpoint expliciet invult (doel, concerns, scope, gebruikte modeltaal, relevante objecttypen/relaties, verantwoording).
- Regel: bij elke view hoort één viewpointbeschrijving. Gebruik de term "view" alleen voor het diagram/plaat en "viewpoint" voor het kader; niet door elkaar halen bij verschillende diagrammen.

## Terminologie en ArchiMate objecten
- Gebruik ArchiMate-objecten en -relaties waar mogelijk, en label deze expliciet in captions/legend.
- Gebruik alleen informatieobjecten/dataobjecten uit het informatiemodel en het referentie objectdiagram.
- Voorbeelden van kernobjecten (indien aanwezig in de plaat): Student, Examenafname, Te beoordelen werk, Zittingsverslag, Summatieve beoordeling, Resultaat, Onderwijsresultaat, Examendossier, Medewerker.
- Componenten benoemen zoals in MORA: Toets- en examenafname systeem, Toets- en examen inlever- en beoordelingssysteem, Studentvolgsysteem, Document Management Systeem, Kernregistratie Systeem Studenten.
- ArchiMate-termen die vaak voorkomen: Business Process, Business Role, Application Component, Application Service, Data Object, Business Object, Association, Flow, Access, Realization.

## Documentopbouw (markdown)
- Document moet renderbaar zijn op GitHub markdown.
- Geen HTML page-breaks.
- Gebruik een vaste hoofdstukstructuur met korte, duidelijke koppen.
- Placeholders zijn korte, inhoudelijke tekst (max 2-3 regels).
- Inleiding bevat het documentdoel en het viewpoint (koppelvlak referentiearchitectuur).
- Leeswijzer alleen opnemen indien expliciet gevraagd.

## AMIGO modellenmatrix en modeltalen
- Hanteer de scheidslijn tussen conceptuele modellen en logische/inrichtingsmodellen.
- Conceptueel: ArchiMate (processen, componenten, concepten).
- Logisch/inrichting: UML/ERD voor gegevensstructuur en klassendiagrammen.
- Interacties: Mermaid om de uitwisseling richting berichtspecificatie te structureren.
- Plaats bij voorkeur de AMIGO modellenmatrix als afbeelding voor herkenbaarheid; voeg een tekstuele mapping toe.
- Gebruik een eenvoudige mappingtabel (Markdown) om MOKA-views te relateren aan AMIGO kolom/rij.

## Afbeeldingen
- Gebruik uitsluitend afbeeldingen uit de `img` folder.
- Plaats afbeeldingen bij het relevante hoofdstuk en voeg een figuurcaption toe.
- Voeg per afbeelding een korte viewpoint-beschrijving en legenda met ArchiMate-objecten toe.
- Bestandsnamen met spaties escapen in links.
 - Als een machine-leesbare variant verwarrend is, kies voor afbeelding + mappingtabel.

## Mermaid diagrammen
- Diagrammen zijn implementatie-onafhankelijk.
- Gebruik alleen MORA-terminologie en objecten uit het klassendiagram/objectdiagram.
- Benoem interacties inclusief reacties (bijv. "verwerkt", "ontvangen", "documentlocatie retour").
- Externe specificaties mogen als bron dienen, maar vertaal altijd naar MORA-terminologie.

## Interactiepatronen (regels)
- Voorbereiding: maak expliciet of gegevens al aanwezig zijn en in welke component de voorbereiding plaatsvindt.
- Afname: toon de overdracht van "te beoordelen werk".
- Beoordeling: expliciteer de rol van medewerker, summatieve beoordeling en vaststelling door gemachtigd orgaan.
- Resultaat: onderscheid "beoordeling" versus "resultaat".
- Dossiervorming: onderwijsresultaat bundelt resultaten en bewijsstukken (zoals zittingsverslag en verwijzing naar beoordeeld werk) en leidt tot examendossier in DMS.
- Verwijs waar mogelijk naar relaties uit het referentie objectdiagram.

## Werkwijze (stapsgewijs)
1. Lees de platen en noteer de exacte termen en objecten.
2. Bepaal de MORA-componenten in scope.
3. Zet de hoofdstukstructuur klaar en plaats de afbeeldingen.
4. Vul alle placeholders met korte, inhoudelijke tekst.
5. Maak een mermaid interactiediagram met MORA-termen en reacties.
6. Controleer dat er geen OOAPI/OKE-termen in de kerntekst staan.
7. Zorg dat alles GitHub-markdown compatible is.
8. Check na iedere prompt of je de prompter goed begrijpt, door je beredenatie uit te leggen. 
9. Formuleer de volgende stap die je gaat zetten vanuit je plan van aanpak en vraag altijd om goedkeuring voor het uitvoeren van die stap aan de prompter.

## Afbakening
- Geen nieuwe begrippen introduceren die niet in de platen voorkomen.
- Geen technische API-uitwerking opnemen in de kerntekst.
- Externe documenten alleen in een apart "Gerelateerde implementaties" stuk, zonder termen over te nemen in de hoofdtekst.

---

## Informatiemodel en referentie klassendiagram (1-op-1 semantiek)

- **Bron van waarheid:** Het machine-leesbare overzicht (bijv. `InformatiemodelOverzicht.json`) en de informatiemodel view (plaat) zijn leidend. Het referentie klassendiagram moet **100% semantisch overeenkomen** met dit informatiemodel.
- **Gegevensgroeptypes in het diagram:** Geen aparte klassen voor gegevensgroeptypes; wel als **interne subcontainers** binnen het betreffende object. Gebruik de **exacte gegevensgroeptype-namen** uit het informatiemodel (zelfde benaming als in de view). Onder elk gegevensgroeptype staan de **referentie-attributen** (zoals in het bijlagevoorbeeld bij Zittingsverslag: `VerslagTotStandkoming` gevolgd door toelichting, onregelmatigheden; `RelatieTotOpsteller` door medewerkerId; enz.).
- **Geen aantallen:** Geen tabel of tekst die "aantal gegevensgroeptypes" benoemt in het hoofddocument. De koppeling tot het informatiemodel wordt getoond door de exacte namen en attributen, niet door tellingen.
- **Relatielabels:** Relaties in het klassendiagram worden waar van toepassing gelabeld met de **naam van het gegevensgroeptype** (bijv. `RelatieTotExamenAfname`, `RelatieTotOpsteller`, `RelatieTotSummatiefResultaat`, `OnderwijsresultaatRegistratie`).
- **Volledigheid:** Elk in het informatiemodel benoemd informatieobject en elke gegevensgroep/gegevensgroeptype moet in het diagram terugkomen (inclusief bv. Examen deelname, Beoordelaar). Document (OKE-object) mag gebruikt worden voor koppeling documenten bij Zittingsverslag en SummatieveBeoordeling.

## OKE en externe specificaties

- **OKE-terminologie in kerntekst:** Niet gebruiken; alleen MORA/datamodel-terminologie in de kerntekst.
- **OKE als referentie:** OKE MBO-toetsafname (en vergelijkbare specs) mogen als **bron** dienen voor referentie-attributen. Nederlandse vertaling van OKE-attributen in een **apart overzicht** (bijv. `OKE_Gegevensgroeptypes_Overzicht.md`); in het hoofddocument alleen een korte verwijzing naar dit overzicht (bij informatiemodel en bij het klassendiagram).
- **OKE vs. informatiemodel analyse:** Een vergelijking "OKE-specificatie vs. informatiemodel" (potentiële gemiste gegevensgroeptypes, processcope) hoort in een **apart analyse-document** (bijv. `OKE_Informatiemodel_Analyse.md`). Dit is een losse analyse voor een volgende iteratie; niet in de kerntekst van de koppelvlak specificatie.

## Procesplaatsing (MORA)

- **Diplomeren en certificeren:** Als overkoepelende processtap met sub-stappen weergeven (bepalen diploma/certificaat recht, besluiten diplomeren/certificeren, diplomeren/certificeren). Bij voorkeur in een Mermaid-subgraph.
- **Buiten scope:** Expliciet vermelden wat buiten scope valt (bijv. "Afgeven mbo-verklaring").

