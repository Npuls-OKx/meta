# Overzicht gegevensgroeptypes en OKE-attributen

Dit document koppelt de **gegevensgroepen en gegevensgroeptypes** uit het MOKA informatiemodel view (figuur 5.3) aan de **OKE MBO-toetsafname specificatie** ([OKE-MBO-toetsafname-specs v1.0](https://www.edustandaard.nl/app/uploads/2024/09/OKE-MBO-toetsafname-specs-v1.0_20240909conceptversie.pdf)). Per gegevensgroep zijn de relevante gegevensgroeptypes opgenomen, aangevuld met belangrijke OKE/OOAPI-attributen in Nederlandse vertaling. Waar uit de OKE-specificatie aanvullende gegevensgroeptypes passen binnen een gegevensgroep, zijn deze toegevoegd.

**Legenda OKE-objecten (Nederlandse vertaling):**
- **Person** → Persoon (student of medewerker)
- **Component** → Toets
- **ComponentOffering** → Planbare toets / Zitting
- **ComponentOfferingAssociation** → Toetsinschrijving / Deelname
- **Result** → Resultaat (toetsresultaat)
- **Document** → Document

---

## 1. Medewerkergegevens (informatieobject: Medewerker)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| MedewerkerId | Person | **persoonId** (uuid), **primaireCode** (codeType, code), weergavenaam (displayName) |
| DeelnameRolBinnenMedewerker | ComponentOfferingAssociation | **rol** (role: coördinator/afnameleider, surveillant, beoordelaar), **status** (state) |
| *Toegevoegd uit OKE* | Person | **voornaam** (givenName), **achternaam** (surname), **roepnaam** (preferredName, consumers) |

---

## 2. Student Gegevens (informatieobject: Student)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| StudentNaam | Person | **voornaam** (givenName), **achternaam** (surname), **voorvoegsel** (surnamePrefix), **weergavenaam** (displayName), **roepnaam** (preferredName), **legitimatieNaam** (idCheckName, consumers) |
| StudentNummer | Person.primaryCode | **codeType** (bijv. studentNumber), **code** |
| StudentOpleidingId | ProgramOfferingAssociation / ProgramOffering | **opleidingsaanbodId** (offeringId), **opleidingsprogrammaId** (programId) |
| OnderwijsprogrammaRegioStudentId | Person.otherCodes / Association | **codeType**, **code** (bijv. regionale studentId) |
| *Toegevoegd uit OKE* | Person.consumers | **toegewezenHulpmiddelen** (assignedNeeds: code, omschrijving, startDatum, eindDatum) |

---

## 3. Examenafname gegevens (informatieobject: Examenafname)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| AfnameNaamEnAanduiding | ComponentOffering | **aanbodId** (offeringId), **primaireCode** (codeType: offeringCode, code), **naam** (name), **afkorting** (abbreviation) |
| AfnameOnderwijslogistiekeContext | ComponentOffering | **locatiecode** (locationCode, consumers), **organisatieId** (organization), **onderwijstaal** (teachingLanguage) |
| ExamenWindowRelaties | ComponentOffering | **startDatumTijd** (startDateTime), **eindDatumTijd** (endDateTime), **duur** (duration, consumers) |
| RelatieTotOpleidingen | ComponentOffering | **toetsId** (component / componentId), **opleidingsaanbodId** (programOffering), **opleidingsdeelId** (courseOffering) |
| *Toegevoegd uit OKE* | ComponentOffering.consumers | **aanbiedingsstatus** (offeringState: actief, geannuleerd), **resultaatVerwacht** (resultExpected), **resultaatwaardetype** (resultValueType) |

---

## 4. Zittingsverslag gegevens (informatieobject: Zittingsverslag)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| RelatieTotExamenAfname | ComponentOffering | **aanbodId** (offeringId) – verwijzing naar de zitting |
| VerslagTotStandkoming | ComponentOffering.consumers | **onregelmatigheden** (irregularities – tekstuele toelichting) |
| RelatieTotOpsteller | Person | **persoonId** (medewerker die het verslag opstelt) |
| *Toegevoegd uit OKE* | ComponentOffering.consumers | **documenten** (documents: **documentId**, **documentType**, **documentNaam**) |

---

## 5. Te beoordelen werk gegevens (informatieobject: Te beoordelen werk)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| IndieningsGegevens | ComponentOfferingAssociation | **koppelingId** (associationId), **status** (state: gekoppeld, geannuleerd, beëindigd), **rol** (role: student) |
| WerkAanduiding | ComponentOfferingAssociation / Result | **omschrijving** (comment), verwijzing naar werk |
| BeoordelingsContext | ComponentOfferingAssociation | **aanbodId** (offeringId – zitting), **persoonId** (personId) |
| *Toegevoegd uit OKE* | ComponentOfferingAssociation.consumers | **extraTijdInMinuten** (additionalTimeInMin), **persoonlijkeHulpmiddelen** (personalNeeds), **poging** (attempt) |

---

## 6. Examen deelname gegevens (informatieobject: Examen deelname)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| RelatieTotStudent | ComponentOfferingAssociation | **persoonId** (personId) |
| AanwezigheidsIndicatie | Result.consumers | **aanwezigheid** (attendance: notKnown, notPresent, notStarted, notFinished, present) |
| RelatieTotExamenAfnameContext | ComponentOfferingAssociation | **aanbodId** (offeringId), **koppelingId** (associationId) |
| *Toegevoegd uit OKE* | ComponentOfferingAssociation | **opleidingsinschrijvingId** (programOfferingAssociationId), **deelinschrijvingId** (courseOfferingAssociationId), **origineleKoppelingId** (orgAssociationId, voor extra pogingen) |

---

## 7. Summatieve beoordeling gegevens (informatieobject: Summatieve beoordeling)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| BeoordelingsOordeelIndicatie | Result | **geslaagd** (pass: unknown, passed, failed), **status** (state: in progress, completed, etc.) |
| BeoordelingsOordeelSpecificatie | Result | **score** (score – resultaatwaarde), **ruweScore** (rawScore), **maxRuweScore** (maxRawScore) |
| MetaDateringOpmaakEnBeoordelingsDatum | Result | **resultaatDatum** (resultDate), **toetsDatum** (testDate, consumers), **vastgesteld** (final, consumers) |
| RelatieTotBeoordelaar | Result.consumers | **beoordelaarId** (assessorId), **beoordelaarCode** (assessorCode) |
| RelatieTotTeBeoordelenWerk | ComponentOfferingAssociation | **koppelingId** (associationId) |
| *Toegevoegd uit OKE* | Result.consumers | **uitgevoerdeZittingNaam** (executedOfferingName), **onregelmatigheden** (irregularities), **documenten** (documents: documentId, documentType, documentNaam) |

---

## 8. Beoordelaar gegevens (informatieobject: Beoordelaar)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| BeoordelaarNaam | Person | **weergavenaam** (displayName), **voornaam** (givenName), **achternaam** (surname) |
| OnderwijskwalificatieBevoegdBeoordelaar | Person / otherCodes | **codeType**, **code** (kwalificatie) |
| *Toegevoegd uit OKE* | Result.consumers | **beoordelaarId** (assessorId), **beoordelaarCode** (assessorCode) – gebruikt in beoordeling |

---

## 9. Summatief resultaat gegevens (informatieobject: Summatief resultaat)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| ResultaatSamenstelling | Result | **score** (score), **ruweScore** (rawScore), **maxRuweScore** (maxRawScore), **geslaagd** (pass) |
| ResultaatAfnameTijdvak | Result.consumers | **toetsDatum** (testDate), **uitgevoerdeZittingNaam** (executedOfferingName) |
| ResultaatVaststelling | Result.consumers | **resultaatDatum** (resultDate), **vastgesteld** (final) |
| *Toegevoegd uit OKE* | Result | **status** (state), **gewicht** (weight), **documenten** (documents) |

---

## 10. Onderwijsresultaat gegevens (geaggregeerd onder Summatief resultaat)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| RelatieTotOnderwijsProgramma | Program / ProgramOffering | **opleidingsprogrammaId** (programId), **opleidingsaanbodId** (offeringId) |
| RelatieTotSummatiefResultaat | Result | **koppelingId** (associationId), **resultaat** (result) |
| RelatieTotBeoordeeldWerk | ComponentOfferingAssociation | **koppelingId** (associationId) |
| RelatieTotExamenDossier | – | **examendossierId** (verwijzing naar dossier) |

---

## 11. Examendossier gegevens (informatieobject: Examendossier)

| Gegevensgroeptype (informatiemodel) | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------------------------|----------|------------------------------------|
| DossierIdentificatie | – | **examendossierId**, **dossiernummer** (primaryCode) |
| OnderwijsprogrammaContext | ProgramOffering | **opleidingsaanbodId**, **cohort** (consumers), **locatie** (consumers) |
| OnderwijsresultaatRegistratie | – | Verzameling resultaten / onderwijsresultaten |
| DossierBeheerContext | – | **status**, **aanmaakDatum**, **bewerkingscontext** |

*Opmerking:* Het Examendossier heeft in de OKE-specificatie geen directe equivalent; de koppeling verloopt via Toetsinschrijving en Resultaat (Studentresultaat-informatiestroom).

---

## 12. Document (OKE-object, gebruikt in Zittingsverslag en Resultaat)

| Gegevensgroeptype | OKE-bron | Attributen (Nederlandse vertaling) |
|-------------------|----------|------------------------------------|
| Document | Document | **documentId**, **documentType** (assessmentForm, assessmentFormWithAnswers, assessmentModel, other), **documentNaam** |

---

**Bron:** OKE MBO-toetsafname afsprakenset, conceptversie 1.0 (9 september 2024), [Edustandaard](https://www.edustandaard.nl/app/uploads/2024/09/OKE-MBO-toetsafname-specs-v1.0_20240909conceptversie.pdf).  
Dit overzicht is een koppeling tussen het MOKA informatiemodel view en de OKE-specificatie; niet alle OKE-attributen zijn in het informatiemodel view uitgewerkt. Het referentie klassendiagram (sectie 5.6) is waar relevant met deze attributen aangevuld.
