# Bijlage: objecttypen en relaties

Volledige inhoud van de view `OKx informatiemodel`, als naslag bij het [informatiemodel](informatiemodel.md). De plaat blijft de leesbare weergave; deze bijlage bestaat om te kunnen nazoeken en om wijzigingen te kunnen volgen.

**Bron.** Gegenereerd uit het ArchiMate-model met `python3 scripts/genereer-informatiemodel-doc.py`. Er is niets van de plaat overgetypt. Wijzigt het model, draai het script dan opnieuw.

## Objecttypen

<!-- gegenereerd:objecttypen -->
In totaal 62 objecttypen.

### Kwalificatiekader MBO

| Objecttype | Scope |
|---|---|
| `Kerntaak` | binnen scope |
| `Kwalificatie` | binnen scope |
| `Kwalificatie dossier` | binnen scope |
| `Werkproces` | binnen scope |

### Onderwijskundigkader instelling

| Objecttype | Scope |
|---|---|
| `Competenties / Skills` | binnen scope |
| `Inzicht` | binnen scope |
| `Kennis` | binnen scope |
| `Leeruitkomst` | buiten scope (landelijk belegd) |
| `Vaardigheid` | binnen scope |

### Onderwijsspecificatie

| Objecttype | Scope |
|---|---|
| `Examenonderdeelspecificatie` | binnen scope |
| `Keuzedeel` | binnen scope |
| `Keuzedeelruimte` | binnen scope |
| `Leeronderdeel specificatie` | binnen scope |
| `Les specificatie` | buiten scope (les-laag) |
| `Onderwijseenheid specificatie` | binnen scope |
| `Opleiding specificatie` | binnen scope |
| `Student keuze regelset` | binnen scope |
| `Toetsonderdeel specificatie` | binnen scope |

### Onderwijsaanbod

| Objecttype | Scope |
|---|---|
| `Examengelegenheid` | binnen scope |
| `Keuzedeelaanbod` | binnen scope |
| `Leergelegenheid` | binnen scope |
| `Lesgelegenheid` | buiten scope (les-laag) |
| `Onderwijseenheid aanbod` | binnen scope |
| `Opleidingaanbod` | binnen scope |
| `Opleidingsaanbod van Instelling` | binnen scope |
| `Opleidingsprogramma aanbod` | binnen scope |
| `Toetsgelegenheid` | binnen scope |

### Onderwijsverbintenis

| Objecttype | Scope |
|---|---|
| `Examengelegenheid verbintenis` | binnen scope |
| `Keuzedeel aanbod verbintenis` | binnen scope |
| `Leergelegenheid verbintenis` | binnen scope |
| `Lesgelegenheid verbintenis` | buiten scope (les-laag) |
| `Onderwijseenheid aanbod verbintenis` | binnen scope |
| `Opleiding aanbod  verbintenis` | binnen scope |
| `Opleidingsprogramma aanbod verbintenis` | binnen scope |
| `Toetsgelegenheid verbintenis` | binnen scope |

### Onderwijsresultaat

| Objecttype | Scope |
|---|---|
| `Aanwezigheid` | binnen scope |
| `Examengelegenheid resultaat` | binnen scope |
| `Keuzedeel resultaat` | binnen scope |
| `Leergelegenheid resultaat` | binnen scope |
| `Lesgelegenheid resultaat` | buiten scope (les-laag) |
| `Onderwijseenheid resultaat` | binnen scope |
| `Opleiding aanbod resultaat` | binnen scope |
| `Opleidingsprogramma resultaat` | binnen scope |
| `Toetsgelegenheid resultaat` | binnen scope |

### Resultaatstructuur

| Objecttype | Scope |
|---|---|
| `Examenonderdeel weging` | binnen scope |
| `Formatief resultaat` | binnen scope |
| `Formatieve beoordeling` | binnen scope |
| `Formatieve resultaat structuur` | binnen scope |
| `Persoonlijke ontwikkeling` | binnen scope |
| `Summatief Afrondingscriterium` | binnen scope |
| `Summatief resultaat` | binnen scope |
| `Summatieve beoordeling` | binnen scope |
| `Summatieve resultaat structuur` | binnen scope |
| `Toetsonderdeel weging` | binnen scope |

### Buiten de kolommen

| Objecttype | Scope |
|---|---|
| `Examenplan` | buiten scope (landelijk belegd) |
| `Medewerker` | binnen scope |
| `Opleidingsprogramma specificatie` | binnen scope |
| `Persoon` | binnen scope |
| `Plaatsingsgroep` | binnen scope |
| `Student` | binnen scope |
| `Verzoek tot Aanbod / Intekening op specificatie` | binnen scope |
| `Waarde document (diploma / certificaat)` | binnen scope |
<!-- /gegenereerd -->

## Relaties

<!-- gegenereerd:relaties -->
### Specialization (13)

Het ene objecttype is een verbijzondering van het andere.

| Van | Naar | Label |
|---|---|---|
| `Examenonderdeelspecificatie` | `Toetsonderdeel specificatie` |  |
| `Formatieve beoordeling` | `Toetsgelegenheid resultaat` |  |
| `Keuzedeel` | `Opleidingsprogramma specificatie` |  |
| `Keuzedeel aanbod verbintenis` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Keuzedeel resultaat` | `Opleidingsprogramma resultaat` |  |
| `Keuzedeelaanbod` | `Opleidingsprogramma aanbod` |  |
| `Keuzedeelruimte` | `Opleidingsprogramma specificatie` |  |
| `Leeruitkomst` | `Competenties / Skills` |  |
| `Leeruitkomst` | `Kerntaak` |  |
| `Leeruitkomst` | `Kwalificatie` |  |
| `Leeruitkomst` | `Kwalificatie dossier` |  |
| `Leeruitkomst` | `Werkproces` |  |
| `Summatieve beoordeling` | `Examengelegenheid resultaat` |  |

### Aggregation (25)

Het ene objecttype bestaat uit het andere. De recursieve varianten zijn bewust: structuren kunnen genest zijn.

| Van | Naar | Label |
|---|---|---|
| `Competenties / Skills` | `Inzicht` |  |
| `Competenties / Skills` | `Kennis` |  |
| `Competenties / Skills` | `Vaardigheid` |  |
| `Formatieve resultaat structuur` | `Toetsonderdeel specificatie` |  |
| `Formatieve resultaat structuur` | `Toetsonderdeel weging` |  |
| `Kerntaak` | `Werkproces` | bestaat uit |
| `Kwalificatie` | `Kerntaak` | bestaat uit |
| `Kwalificatie dossier` | `Kwalificatie` | bevat |
| `Leergelegenheid` | `Lesgelegenheid` |  |
| `Leeronderdeel specificatie` | `Les specificatie` |  |
| `Leeruitkomst` | `Leeruitkomst` |  |
| `Onderwijseenheid aanbod` | `Leergelegenheid` |  |
| `Onderwijseenheid specificatie` | `Leeronderdeel specificatie` |  |
| `Onderwijseenheid specificatie` | `Onderwijseenheid specificatie` |  |
| `Opleiding specificatie` | `Opleidingsprogramma specificatie` |  |
| `Opleidingaanbod` | `Opleidingsprogramma aanbod` |  |
| `Opleidingsaanbod van Instelling` | `Opleidingaanbod` |  |
| `Opleidingsprogramma aanbod` | `Onderwijseenheid aanbod` |  |
| `Opleidingsprogramma specificatie` | `Onderwijseenheid specificatie` |  |
| `Opleidingsprogramma specificatie` | `Opleidingsprogramma specificatie` |  |
| `Persoon` | `Medewerker` |  |
| `Persoon` | `Student` |  |
| `Summatieve resultaat structuur` | `Examenonderdeel weging` |  |
| `Summatieve resultaat structuur` | `Examenonderdeelspecificatie` |  |
| `Summatieve resultaat structuur` | `Summatieve resultaat structuur` |  |

### Association (79)

Een inhoudelijke samenhang zonder eigenaarschap of samenstelling.

| Van | Naar | Label |
|---|---|---|
| `Aanwezigheid` | `Lesgelegenheid resultaat` |  |
| `Examengelegenheid` | `Examengelegenheid verbintenis` |  |
| `Examengelegenheid resultaat` | `Aanwezigheid` |  |
| `Examengelegenheid verbintenis` | `Examengelegenheid resultaat` |  |
| `Examenonderdeel weging` | `Examenonderdeelspecificatie` |  |
| `Examenonderdeelspecificatie` | `Examengelegenheid` |  |
| `Examenonderdeelspecificatie` | `Leeruitkomst` |  |
| `Examenonderdeelspecificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Examenplan` | `Kerntaak` |  |
| `Examenplan` | `Summatieve resultaat structuur` | kent |
| `Formatieve beoordeling` | `Formatief resultaat` | kent |
| `Formatieve resultaat structuur` | `Formatief resultaat` | conform |
| `Keuzedeel` | `Keuzedeelaanbod` |  |
| `Keuzedeel` | `Keuzedeelruimte` |  |
| `Keuzedeel` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Keuzedeel aanbod verbintenis` | `Keuzedeel resultaat` |  |
| `Keuzedeelaanbod` | `Keuzedeel aanbod verbintenis` |  |
| `Keuzedeelaanbod` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Keuzedeelruimte` | `Student keuze regelset` |  |
| `Leergelegenheid` | `Leergelegenheid verbintenis` |  |
| `Leergelegenheid` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Leergelegenheid verbintenis` | `Leergelegenheid resultaat` |  |
| `Leeronderdeel specificatie` | `Leergelegenheid` |  |
| `Leeronderdeel specificatie` | `Leeruitkomst` |  |
| `Leeronderdeel specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Les specificatie` | `Leeruitkomst` |  |
| `Les specificatie` | `Lesgelegenheid` |  |
| `Les specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Lesgelegenheid` | `Lesgelegenheid verbintenis` |  |
| `Lesgelegenheid` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Lesgelegenheid verbintenis` | `Lesgelegenheid resultaat` |  |
| `Onderwijseenheid aanbod` | `Onderwijseenheid aanbod verbintenis` |  |
| `Onderwijseenheid aanbod` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Onderwijseenheid aanbod verbintenis` | `Onderwijseenheid resultaat` |  |
| `Onderwijseenheid specificatie` | `Leeruitkomst` |  |
| `Onderwijseenheid specificatie` | `Onderwijseenheid aanbod` |  |
| `Onderwijseenheid specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Opleiding aanbod  verbintenis` | `Opleiding aanbod resultaat` |  |
| `Opleiding aanbod  verbintenis` | `Opleidingsprogramma aanbod verbintenis` | Minimaal 1 |
| `Opleiding specificatie` | `Leeruitkomst` |  |
| `Opleiding specificatie` | `Opleidingaanbod` |  |
| `Opleiding specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Opleidingaanbod` | `Opleiding aanbod  verbintenis` |  |
| `Opleidingsprogramma aanbod` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Opleidingsprogramma aanbod` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Opleidingsprogramma aanbod verbintenis` | `Opleidingsprogramma resultaat` |  |
| `Opleidingsprogramma specificatie` | `Leeruitkomst` |  |
| `Opleidingsprogramma specificatie` | `Opleidingsprogramma aanbod` |  |
| `Persoon` | `Plaatsingsgroep` | Worden gegroepeerd via |
| `Persoonlijke ontwikkeling` | `Competenties / Skills` |  |
| `Persoonlijke ontwikkeling` | `Formatieve resultaat structuur` |  |
| `Plaatsingsgroep` | `Keuzedeel aanbod verbintenis` |  |
| `Plaatsingsgroep` | `Leergelegenheid verbintenis` |  |
| `Plaatsingsgroep` | `Onderwijseenheid aanbod verbintenis` |  |
| `Plaatsingsgroep` | `Opleiding aanbod  verbintenis` |  |
| `Plaatsingsgroep` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Student keuze regelset` | `Keuzedeel` |  |
| `Student keuze regelset` | `Leeronderdeel specificatie` |  |
| `Student keuze regelset` | `Les specificatie` |  |
| `Student keuze regelset` | `Onderwijseenheid specificatie` |  |
| `Student keuze regelset` | `Opleiding specificatie` |  |
| `Student keuze regelset` | `Opleidingsprogramma specificatie` |  |
| `Summatief Afrondingscriterium` | `Waarde document (diploma / certificaat)` |  |
| `Summatieve beoordeling` | `Summatief resultaat` | met |
| `Summatieve resultaat structuur` | `Leeruitkomst` |  |
| `Summatieve resultaat structuur` | `Summatief Afrondingscriterium` |  |
| `Summatieve resultaat structuur` | `Summatief resultaat` | conform |
| `Summatieve resultaat structuur` | `Waarde document (diploma / certificaat)` |  |
| `Toetsgelegenheid` | `Toetsgelegenheid verbintenis` |  |
| `Toetsgelegenheid resultaat` | `Aanwezigheid` |  |
| `Toetsgelegenheid verbintenis` | `Toetsgelegenheid resultaat` |  |
| `Toetsonderdeel specificatie` | `Leeruitkomst` |  |
| `Toetsonderdeel specificatie` | `Toetsgelegenheid` |  |
| `Toetsonderdeel specificatie` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
| `Toetsonderdeel weging` | `Toetsonderdeel specificatie` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Examengelegenheid` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Opleidingaanbod` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Opleidingsprogramma specificatie` |  |
| `Verzoek tot Aanbod / Intekening op specificatie` | `Toetsgelegenheid` |  |

### Access (23)

Een persoon raakt het objecttype, als student of als medewerker.

| Van | Naar | Label |
|---|---|---|
| `Persoon` | `Aanwezigheid` |  |
| `Persoon` | `Examengelegenheid resultaat` |  |
| `Persoon` | `Examengelegenheid verbintenis` |  |
| `Persoon` | `Keuzedeel aanbod verbintenis` |  |
| `Persoon` | `Keuzedeel resultaat` |  |
| `Persoon` | `Keuzedeelaanbod` |  |
| `Persoon` | `Leergelegenheid` |  |
| `Persoon` | `Leergelegenheid resultaat` |  |
| `Persoon` | `Leergelegenheid verbintenis` |  |
| `Persoon` | `Lesgelegenheid resultaat` |  |
| `Persoon` | `Lesgelegenheid verbintenis` |  |
| `Persoon` | `Onderwijseenheid aanbod` |  |
| `Persoon` | `Onderwijseenheid aanbod verbintenis` |  |
| `Persoon` | `Onderwijseenheid resultaat` |  |
| `Persoon` | `Opleiding aanbod  verbintenis` |  |
| `Persoon` | `Opleiding aanbod resultaat` |  |
| `Persoon` | `Opleidingaanbod` |  |
| `Persoon` | `Opleidingsprogramma aanbod` |  |
| `Persoon` | `Opleidingsprogramma aanbod verbintenis` |  |
| `Persoon` | `Opleidingsprogramma resultaat` |  |
| `Persoon` | `Toetsgelegenheid resultaat` |  |
| `Persoon` | `Toetsgelegenheid verbintenis` |  |
| `Persoon` | `Verzoek tot Aanbod / Intekening op specificatie` |  |
<!-- /gegenereerd -->
