## Leeruitkomsten en SBU/EC als maatstaf voor logistieke containergrootte van programma-onderdelen

Status: Voorstel

Datum: 2026-03-27

### Context

In OKx wordt flexibel onderwijs **inhoudelijk** grotendeels **via leeruitkomsten** beschreven en **logistiek** verbonden aan catalogus, planning, volgsystemen en toetsketens (zie [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) en de prioriteitsketen in [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md)). Tegelijkertijd moeten uitwisseling en tooling **herkenbare eenheden** hebben voor **omvang** en **aggregatie**: wat is een “klein” versus “groot” onderdeel in de keten (rooster, studiebelasting, bekostiging- en rapportagehooks), zonder terug te vallen op **alleen** traditionele begrippen als vast **vak**, **opleidingsonderdeel** of **programma** in de zin van één vaste administratieve structuur?

In de voorbereiding op de **leverancierssessie** (27 maart 2026) is benadrukt dat **leeruitkomsten** de **centrale sleutel** voor onderwijsverbinding vormen en de **schaling** van een leertraject bepalen — **van zeer korte leeractiviteit tot meerjarig programma** — en dat de **kwantificering** daarbij in de praktijk via **EC’s (hoger onderwijs)** en **SBU’s / studiebelastingsuren (mbo)** verloopt (zie samenvatting en bespreking mockups). In hetzelfde spoor wordt in overleg erkend dat **standaarddata‑API’s** (zoals OEAPI) **constructies** als programma, course en learning component hanteren: in **ontwerp** is niet altijd meteen duidelijk welke administratieve “container” past bij wat de student kiest — terwijl de keten wél **studielast** en **leeruitkomsten** moet kunnen uitwisselen.

**Probleem zonder expliciete keuze:** leveranciers en instellingen **mapperen** leeruitkomsten en flexibele routes **ongelijk** op hun eigen module-/vakstructuur, waardoor **planning**, **voortgang** en **aggregatie** in koppelvlakken **niet vergelijkbaar** zijn. Omgekeerd leidt **alleen studielast zonder leeruitkomst** tot verlies van **onderwijskundige** betekenis (strijdig met [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md)).

### Beslissing (concept)

1. **Leeruitkomsten** blijven de **primaire inhoudelijke categorisering** van wat een onderwijsprogramma-onderdeel **betekent** in de keten (wat de student moet kunnen aantonen).
2. **SBU (mbo)** en **EC (hbo)** worden gehanteerd als de **genormeerde maatstaf voor de logistieke containergrootte** van dat onderdeel: de **studielast** (in de voor de sector geldende eenheid) is het **verplichte attribuut** om onderwijsprogramma-onderdelen **onderling vergelijkbaar** te maken voor **logistiek** (planning, bundeling, voortgang op aggregatieniveau, interfaces naar catalogus/SVS/planning), **naast** de leeruitkomstidentiteit.
3. **Sectoruitsplitsing:** in specificaties en het model wordt **expliciet** onderscheid gemaakt tussen **mbo (SBU)** en **hbo (EC)** waar dat voor interpretatie en rapportage nodig is; generieke koppelvlaktermen (“studielast”, “omvang”) **vertalen** naar deze eenheden in profielen of implementatierichtlijnen.
4. Deze combinatie is een **OKx-richting** voor **koppelvlakken en informatiemodel**; **wettelijke of bekostigingsdefinities** (bijv. ROD, opleidingscodes) kunnen **aanvullende** eisen stellen — die worden in latere uitwerking **gemapt**, niet stilzwijgend gelijkgeschakeld met deze logistieke maatstaf.

### Alternatieven


| Optie                                                                                                     | Voordeel                                                                                                                                          | Nadeel / risico                                                                                                             |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **A. Alleen traditionele containers** (vak, module, opleidingsonderdeel als enige eenheid)                | Sluit aan bij legacy-administratie                                                                                                                | **Inflexibel** bij flexibele routes en hergebruik van leeruitkomsten; **mismatch** met mockups en LLO-praktijk              |
| **B. Alleen leeruitkomsten, geen verplichte studielast in het koppelvlak**                                | Simpeler datamodel                                                                                                                                | **Geen gedeelde schaal** voor planning en aggregatie; **haperende** aansluiting op rooster en bekostigings-/rapportagelagen |
| **C. Alleen klokuren/contacturen zonder SBU/EC**                                                          | Fijnkorrelig voor rooster                                                                                                                         | **Niet sectorbreed vergelijkbaar** met kwalificatie- en examenlogica; dubbeling met bestande EC/SBU-praktijk                |
| **D. (Gekozen richting)** **Leeruitkomst + SBU of EC** als standaardpaar voor inhoud + logistieke grootte | **Samenhang** onderwijskundig en logistiek; aansluiting op [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) en leveranciersgesprekken | **Mappingwerk** naar OEAPI- en legacy-begrippen; **mbo/hbo** moeten beide worden ondersteund                                |


### Consequenties

- **Stakeholders:** **Leveranciers** kunnen **minimumuitwisseling** afspreken: iedere uitwisselbare **eenheid** van aanbod/keuze heeft **leeruitkomst(referenties)** en **studielast in SBU of EC** (conform sector).
- **Werk:** Technische werkgroepen en MOKA-uitwerking moeten **attributen en cardinaliteit** (1:N leeruitkomsten per container, of omgekeerd) **uitschrijven** in berichten en API-profielen; **geen** stilzwijgende vereenzelviging van “learning component” met één vaste administratieve betekenis zonder deze maatstaf.
- **Risico’s:** **Vaag geformuleerde** leeruitkomsten (breed herbruikbaar) vergroten overlap; mitigatie via **indicatoren**, **context** en **governance** op definities — buiten scope van dit ADR, wel **herkenbaar** in keten. **Overlap** tussen leeruitkomsten blijft een **inhoudelijk** vraagstuk, niet door studielast alleen op te lossen.

### Impact op `architecture/model/model.archimate`

- **Informatie-elementen:** Entiteiten of objecttypen voor **onderwijsaanbod** / **programma-onderdelen** moeten **studielast** (SBU of EC, met **sector** of **onderwijssector-attribuut**) en **koppeling aan leeruitkomst(en)** kunnen dragen in relevante views (catalogus, onderwijsontwerp, student-kiest-context).
- **Relaties:** Aggregaties (bijv. “studieplan”, “bundel”, “leerroute”) moeten **traceerbaar** zijn naar **som of samenstelling** van **logistieke grootte** op basis van SBU/EC, naast leeruitkomstset — consistent met de **schaling** genoemd in de meeting-samenvatting.
- **OEAPI / standaarden:** Waar het model **consumer/producer**-rollen toont, moet de **mapping** naar OEAPI-begrippen (bijv. program, course, learning component) **expliciet** gemaakt worden in documentatie of vervolg-ADR, **zonder** dit ADR te vervangen.

### Relaties en links

- **Gerelateerde ADR’s:** [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md), [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/OKx_kernteam_inhoud_voorbereidingleveranciersessie_20260327/summary.md` — o.a. leeruitkomsten als standaard; SBU/EC; schaling leertraject
  - `architecture/meetings/OKx_kernteam_inhoud_voorbereidingleveranciersessie_20260327/transcript.md` — o.a. EC’s in mockups, studieplan, leeruitkomsten/indicatoren
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md` (context leeruitkomsten in keten)
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)`, `[architecture/docs/principes.md](../docs/principes.md)`, [OEAPI v6.0](https://openonderwijsapi.nl/v6.0/)

### Vervangt (optioneel)

- —

