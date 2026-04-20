## Hierarchisch datamodel onderwijsaanbod: structuur, leeruitkomsten en SBU/EC-aggregatie

Status: Voorstel

Datum: 2026-04-20

### Context

In het overleg over **studentkeuze, roostering, planning en POC’s** is benadrukt dat de planning alleen kan werken wanneer onderwijsaanbod voldoende **gestructureerd** en **datagedreven** wordt vastgelegd. Daarbij is een hiërarchische opbouw genoemd (programma → opleidingsonderdelen → leergelegenheden → lessen) en expliciet dat de **som van studiebelasting** op onderdelen moet optellen naar het macro-ontwerp (bijv. een nominaal programma met 4800 SBU).

In een eerdere meeting over **StudentKiest** is daarnaast een onderwijs-/aanbodhiërarchie benoemd die aansluit op het keuzeniveau: programma → leertaak → leeractiviteit → lesopdracht (waarbij de student kiest op leeractiviteitniveau; zie [0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md)).

Deze ADR legt vast dat OKx voor het informatiemodel en de koppelvlakspecificaties een **hiërarchisch datamodel** hanteert waarin:

- elk niveau een relatie met **leeruitkomsten** kan dragen, en
- de studiebelasting (SBU/EC) als **logistieke maat** consistent kan worden geaggregeerd (zie [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md)).

Bronnen:
- `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs_20260417/summary.md`
- `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_20260413/summary.md`

### Beslissing

We leggen vast dat OKx voor onderwijsaanbod en route/traject-uitwerking een **hiërarchisch datamodel** hanteert met de volgende eigenschappen:

1. **Hiërarchie als uitgangspunt:** onderwijsaanbod wordt gemodelleerd als een boom/hiërarchie van samenstellende onderdelen (van macro naar micro). Naamgeving van niveaus kan per sector/instelling verschillen, maar het model ondersteunt ten minste het onderscheid macro-structuur (programma) en het keuzeniveau (leeractiviteit).
2. **Leeruitkomsten als sleutel:** elk relevant niveau kan gekoppeld zijn aan één of meer leeruitkomsten (inhoudelijke betekenis), consistent met [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md).
3. **SBU/EC per niveau:** elk niveau kan een studiebelasting (SBU in mbo / EC in ho) dragen, conform [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md).
4. **Aggregatie-invariant:** voor een samengesteld onderdeel geldt dat de studiebelasting van het bovenliggende niveau consistent is met (bijv. gelijk aan) de som van de studiebelasting van de onderliggende delen, binnen afgesproken toleranties/afronding. Dit is een expliciet te hanteren constraint in modellen en uitwisseling: “som van delen telt op naar bovenliggend niveau”.
5. **Extern referentiekader:** waar van toepassing kan het model refereren aan externe begrippenkaders/taxonomieën (in meeting genoemd: CompetentNL, kwalificatiedossiers; en eventueel Bloom-niveaus voor complexiteit), zonder dat OKx deze kaders inhoudelijk definieert.

### Alternatieven

| Optie | Voordeel | Nadeel / risico |
|-------|----------|------------------|
| **A. Plat model zonder hiërarchie** (losse lijst aanboditems) | Eenvoudig datamodel | Onvoldoende voor planning/roostering en aggregatie; onduidelijk keuzeniveau; lastig om studiebelasting en dependencies te begrijpen |
| **B. Hiërarchie zonder aggregatie-constraint** | Flexibel in inrichting | Risico op inconsistentie (macro en micro tellen niet op); planners kunnen niet vertrouwen op studiebelasting; complexe reconciliatie |
| **C. (Gekozen richting)** **Hiërarchie + leeruitkomsten + SBU/EC + aggregatie-invariant** | Consistentie voor planning, analyse en koppelvlakken; ondersteunt PoC OC–Schedule; sluit aan op keuzeniveau leeractiviteit | Vereist datakwaliteit en governance; vraagt expliciete mapping naar OEAPI-constructen |

### Consequenties

- **Validatie via OC–Schedule uitwerking:** in gesprekken is expliciet benoemd dat een eerste concrete uitwerking/validatie van de keten rond **Onderwijscatalogus (OC)** en **Planning/Roostering (Schedule)** nuttig is om te toetsen of dit datamodel planning daadwerkelijk kan voeden. Dit ADR schrijft geen operationele PoC-aanpak of planning voor; het benoemt alleen dat deze koppeling een logisch validatiekader vormt.
- **Koppelvlakken:** specificaties moeten ruimte bieden om zowel macro (programma/onderdeel) als micro (leeractiviteit) eenduidig uit te wisselen, inclusief studiebelasting en leeruitkomstkoppelingen.
- **Mapping naar OEAPI:** waar OEAPI termen (program/course/learning component) worden gebruikt, moet de mapping naar deze hiërarchie expliciet worden gemaakt (conform principes in `architecture/docs/principes.md`).

### Relaties en links

- **Gerelateerde ADR’s:**
  - [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) — SBU/EC als logistieke maatstaf
  - [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) — leeruitkomsten als sleutel
  - [0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md) — leeractiviteit als keuzeniveau
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs_20260417/summary.md`
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_20260413/summary.md`
- ArchiMate model: `architecture/model/model.archimate` (voeg informatie-objecten toe voor de hiërarchieniveaus; modelleer aggregatie/part-of relaties; leg studiebelasting (SBU/EC) en leeruitkomstkoppelingen vast; leg mapping naar OEAPI-constructen vast in views/documentatie)

