## Student Keuze Systeem (SKS) als zelfstandige referentiecomponent

Status: Voorstel

Datum: 2026-03-27

### Context

[0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) benoemt **Student Kiest** als leidend uitgangspunt en het **Student Keuze Systeem (SKS)** als randvoorwaarde die in specificaties en model **herkenbaar** moet zijn. De **hoofdplaat OKx** en de interpretatietabel hanteren **Student Kiest (nog niet in MORA)** als **eigen** referentiecomponent met stromen o.a. naar **onderwijscatalogus**, **SVS**, **KRS** en **student** (zie `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)`).

In het kernteamoverleg ter **voorbereiding leverancierssessie** (27 maart 2026) is vastgehouden dat er **formeel** richting wordt gegeven aan een **SKS** en dat o.a. een **SVS daaraan gekoppeld** wordt. De **belangrijke conclusie** in datzelfde overleg is dat **student kiest** nu **echt een losse referentiecomponent** moet worden — zodat er **meer expliciete koppelinteractie** ontstaat dan wanneer keuze-implementatie **verspreid** of **verborgen** zit in andere bouwstenen (portaal, catalogus-only, LMS). Tegelijkertijd is afgesproken dat OKx **niet** verantwoordelijk is om het SKS **volledig** uit te schrijven, maar wél **voldoende informatie** moet leveren voor een **MVP** voor leveranciers: het **fundament** en **minimuminformatie**, vergelijkbaar met een **snelweg zonder volledige routebeschrijving** (zie transcript).

**Risico zonder expliciete keuze:** leveranciers en instellingen implementeren **keuze** in **willekeurige** producten zonder gedeelde **componentgrens**, waardoor **ketenstromen** (catalogus, wallet/intake, inschrijving, voortgang) **niet interoperabel** zijn en [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) niet afdwingbaar blijft.

### Beslissing (concept)

1. **SKS** (**Student Keuze Systeem**) wordt in OKx-architectuur (hoofdplaat, ArchiMate-model, koppelvlakbeschrijvingen) gehanteerd als **zelfstandige referentiecomponent**: de plek waar **studentkeuze** (articulatie, selectie, meta-data rond gevraagd/aangeboden aanbod) **primair** als **ketenzichtbare** bouwsteen wordt gemodelleerd — **niet** stilzwijgend **samengevoegd** met alleen **onderwijscatalogus**, **LMS**, **studieportaal** of **SVS** zonder expliciete latere ADR.
2. De **koppeling SKS ↔ SVS** (en andere buren zoals catalogus, KRS, wallet/intake waar van toepassing) blijft een **bewuste relatie tussen afzonderlijke componenten** in model en specs, conform de overleglijn dat **SVS aan SKS gekoppeld** wordt.
3. **OKx-scope:** dit ADR legt de **architectuurgrens** vast; **volledige functionele of technische specificatie** van het SKS valt **buiten** de volledige verantwoordelijkheid van OKx, maar **minimuminformatie**, **interfaces** en **ketenhooks** worden **wel** in backlog/specs uitgewerkt zodat leveranciers een **MVP** kunnen invullen.
4. Wijzigingen aan de **hoofdplaat** die **Student Kiest** raken, worden **getoetst** op deze componentafbakening (zoals in het overleg benoemd: effect op plaat expliciet meenemen).

### Alternatieven


| Optie                                                                                        | Voordeel                                                                                                                                                | Nadeel / risico                                                                                                                                             |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A. Geen aparte component** — keuze alleen als UI boven catalogus                           | Minder complexe tekening                                                                                                                                | **Geen** gedeelde **semantiek** voor keuze-articulatie en **meta-informatie** (o.a. BI/journey); haaks op conclusie **losse referentiecomponent**           |
| **B. SKS samenvoegen met SVS**                                                               | Eén leveranciersproduct denkbaar in sommige instellingen                                                                                                | **Verschillende verantwoordelijkheden** (kiezen vs. volgen/voortgang) **vervagen**; strijdig met uitgesproken **koppeling** SKS–SVS als **twee** onderdelen |
| **C. SKS alleen als proces in MORA zonder eigen systeemcomponent**                           | Aansluiting op procesarchitectuur                                                                                                                       | **Onvoldoende** voor **API- en data-afspraken** in OKx-koppelvlakken                                                                                        |
| **D. (Gekozen richting)** **SKS als eigen referentiecomponent** met expliciete koppelvlakken | **Traceerbare** stromen; **MVP-fundament** voor leveranciers; consistent met hoofdplaat en [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) | **Meer** koppelvlakken te beschrijven; **MORA-gap** (“nog niet in MORA”) blijft **signalering** tot sectorale borging                                       |


### Consequenties

- **Stakeholders:** **Leveranciers** weten dat **keuze** een **eigen** integratiepunt is; **instellingen** kunnen **eisen** formuleren op **grenzen** tussen SKS en naburige systemen.
- **Werk:** Issues/specs voor stromen met **Student Kiest** in de tabel (o.a. richting **SVS**, **KRS**, **student**, en interactie met **catalogus**/aanbod) worden **expliciet** onder **SKS**-component gemodelleerd waar dat semantisch klopt.
- **Risico’s:** **Overlap** met bestaande portals; mitigatie door **rol van de referentiecomponent** (wat **moet** over de keten) vs. **implementatie** (één product kan delen combineren **mits** interfaces kloppen).

### Impact op `architecture/model/model.archimate`

- **Referentiecomponent:** **SKS** moet als **onderscheiden** applicatie-/systeemelement (conform gekozen ArchiMate-conventie in het model) **zichtbaar** zijn waar **studentkeuze** centraal staat — **gescheiden** van **Onderwijscatalogus**, **SVS**, **LMS** en **KRS**, tenzij een **later** ADR een herindeling vastlegt met migratiepad.
- **Views / relaties:** Stromen uit `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)` die **Student Kiest** als bron of doel hebben, moeten in relevante views **terug te vinden** zijn als relaties naar/van het **SKS**-element.
- **Niet in dit ADR:** volledige berichtdefinities of OEAPI-consumerprofielen — die volgen uit technische uitwerking onder deze grens.

### Relaties en links

- **Gerelateerde ADR’s:** [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md) (keten naar downstream componenten), [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) (domeinprincipes student kiest, SKS genoemd als randvoorwaarde)
- Issues: #(te koppelen)
- PR: #(te vullen)
- Meetings:
  - `architecture/meetings/OKx_kernteam_inhoud_voorbereidingleveranciersessie_20260327/transcript.md` (o.a. SKS formeel; SVS gekoppeld; student kiest als **losse referentiecomponent**; MVP/fundament SKS)
  - `architecture/meetings/OKx_kernteam_inhoud_voorbereidingleveranciersessie_20260327/summary.md`
  - `architecture/meetings/okx_kernteam_inhoud_uitwerken_studentkiest_flexibelonderwijs_overeenkomst_20260325/summary.md` (context student kiest / keten)
- ArchiMate: `architecture/model/model.archimate`
- Docs: `[doc/OKx_Projectoverzicht.md](../../doc/OKx_Projectoverzicht.md)`, `[doc/OKx_Informatiesstromen.md](../../doc/OKx_Informatiesstromen.md)`

### Vervangt (optioneel)

- —

