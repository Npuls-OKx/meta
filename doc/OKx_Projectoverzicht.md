# OKx Projectoverzicht

## Doelbinding
Project OKx is een onderdeel van het [groeifonds programma NPuls](https://npuls.nl/project-onderwijskoppelingen), zoals bekrachtigd door het Nederlandse ministerie van Onderwijs, Cultuur en Wetenschap. De repository dient als een knowledge base voor het inhoudelijke component van dit project.

OKx heeft als doel **uniforme en gestandaardiseerde koppelvlakken** voor onderwijslogistiek te realiseren, met het BOPSI-implementatiepad als uitgangspunt. De scope start bij **MBO**; **HO** (hoger onderwijs) volgt in een later stadium. Door koppelvlakken eenduidig te specificeren ontstaat interoperabiliteit tussen systemen en partijen in de onderwijsketen.

## Scope: OKx vs OKE

- **OKx** is de overkoepelende projectcontext: visie, besluitvorming, ketenplaten, fasering en informatiestromen. Alles wat de *waarom* en *waarbinnen* van de koppelvlakken beschrijft, hoort bij OKx.
- **OKE** (Onderwijs Koppeling Examinering) is een **subdomein** binnen OKx. Binnen deze repository hebben we voor OKE een concrete MOKA-koppelvlakspecificatie als voorbeeld uitwerking gemaakt. Met als doel te testen of de modeleringsaanpak van het MOKA koppelvlak ook echt werkt, om koppelvlakken te beschrijven namens de onderwijssector. De voorbeeld uitwerking richt zich op het een deel van de gehele procesketen [Examineren en Diplomering en certificeren](https://mora.mbodigitaal.nl/index.php/Procesketen_Examineren) binnen de MORA. Namelijk de processtappen *Examen uitvoeren* tot en met *diplomeren/certificeren*  (en eventuele andere MORA en OKE gerelateerde procesketen delen later). OKE is een eerdere uitwerking van een sector initiatief om digitaal examineren te realiseren binnen het mbo. De OKx aanpak is gebaseerd op eerdere ervaring van OKE.
- De deliverables (MOKA koppelvlakspecificaties, informatiemodellen, templates) staan dus onder OKx, met een deel van OKE als voorbeeld uitwerking om te testen of de aanpakt werkt.

## Projectaanpak

De projectaanpak van het OKx-kernteam volgt een vaste lijn van **begrijpen** naar **ontwerpen** naar **realiseren**. Het project bevindt zich **nu** in de fase **begrijpen**, met een lichte start in de **ontwerpfase** (onder meer door de MOKA-koppelvlakspecificatie voor OKE, en de initiatieven om de OKx uitwerking te realiseren).

![OKx kernteam projectaanpak](../img/OKx_kernteam_project_aanpak_v20260317.jpg)

### Standaardiseren met AMIGO (status)

OKx volgt de **AMIGO-aanpak** voor het komen tot (sectorale) standaardafspraken: `https://www.edustandaard.nl/amigo/aanpak/`.

- **Nu bezig met**: **scenario-analyse**, **gegevensanalyse** en **interactie-analyse** (AMIGO stappen 1–3), zodat we gezamenlijk helder krijgen *wat* er moet gebeuren in de keten vóór we de technische specificaties en interfaces uitwerken.
- **Technologiekeuze (OEAPI, tenzij)**: in de AMIGO stap *technologiekeuze* is onze voorkeur **OEAPI**, tenzij OEAPI aangeeft dat de wensen niet passend zijn.

### Kleinere initiatieven via MOKA (naast OKx-kern)

Niet alle koppelvlakken hoeven te wachten op de volledige OKx-projectaanpak. Voor **kleinere of vroege initiatieven** (bijv. start met minimaal 2 instellingen en 2 verschillende leveranciers) is er een route via de **werkgroep MOKA** (Middelbaar Onderwijs Koppelvlakken Architectuur; subdomein onder **MORA**). Een voorbeeld is **OKD** (Onderwijskoppeling Documentmanagement): `https://github.com/Onderwijs-Koppelingen-OKx/OKD-Document-Management`. Dit initiatief is echter nadrukkelijk nog *geen* sector standaard. Tot dat de sector architectuur gremia hierop akkoord geven en de specificaties volgens Edustandaard standaarden zijn beschreven en aangemeld bij dit orgaan.

De AMIGO-aanpak is ook daar de basis; voor praktische richtlijnen en werkwijze verwijzen we naar de (gereleasde) **OKx guidelines**: [`moka-koppelvlakspecificaties/guidelines/doc/OKx-guidelines-v01-09-25.md`](../moka-koppelvlakspecificaties/guidelines/doc/OKx-guidelines-v01-09-25.md).

Voor vragen neem contact op met de MOKA. Tijdelijk via doorverwijzing via niek.derksen@surf.nl.

## Hoofdplaat OKx informatiestromen

Het projectteam OKx wil de vraagstelling van de **sector** (van de instellingen) kanaliseren richting de **leveranciers** van onderwijsondersteunende software. De onderstaande hoofdplaat geeft een indicatie van alle informatiestromen die in samenwerking — en volgens de MOKA-koppelvlakspecificaties — uitgewerkt kunnen worden. Daarmee geeft ze richting en ondersteunt ze goed geïnformeerde architectuur- en technische besluiten.

**Keten en concept (invoer voor technische specs):** wat de stromen in de keten betekenen en hoe dat richting geeft aan berichtspecificaties, klassendiagrammen en API-uitwerking, staat in [OKx Informatiestromen (ketenconcept)](OKx_Informatiesstromen.md).

**Architectuur en model:** hoe besluiten en informatiestromen samenhangen met documentatie en het ArchiMate-model staat in [OKx Architectuurbesluiten en impact](OKx_Architectuurbesluiten-en-impact.md) en [Informatiestromen, ArchiMate en MOKA-view](OKx_Informatiestromen-ArchiMate-en-MOKA-view.md).

**In de plaat: rood = eerste prioriteit.**

![Hoofdplaat OKx informatiestromen](../img/Hoofdplaat%20OKx%20informatiestromen%20v20260317.png)

Deze hoofdplaat is in aanbouw, het bron bestand kan worden gevonden in het OKx [architectuur model](../architecture/model/model.archimate), door het te openen binnen [Archi](https://www.archimatetool.com/). Onder *MORA (OKx Knowledgebase) > Views > Koppelvlakken > OKx hoofdplaat*. 

### Interpretatie van de informatiestromen (uit de hoofdplaat)

De onderstaande tabel interpreteert de plaat **"Hoofdplaat OKx informatiestromen v20260317.png"**. Alleen de flowlijnen die **niet blauw** (procedureel) en **niet oranje** (o.a. OKE/Edubroker) zijn, zijn opgenomen — dit zijn de informatiestromen die verder gespecificeerd moeten worden. De semantische beschrijving op of bij elke lijn in de plaat is overgenomen en waar nodig kort uitgebreid. **Context:** linkervlak = onderwijsontwikkeling, inrichting van nominale- en keuze aanbod; rechter (grijs) vlak = student studeert en maakt keuzes / onderwijsuitvoering (flexibel onderwijs).

| Nr | Referentie component (van) | Referentie component (naar) | Semantische beschrijving informatiestroom | Context | Prioriteit |
|----|----------------------------|-----------------------------|------------------------------------------|---------|------------|
| 1 | Curriculum ontwerptool | Onderwijscatalogus | Uitgewerkt aanbod | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | 0 (Basis, voedt alle andere systemen) |
| 2 | Onderwijscatalogus | Planningssysteem (meer jarenplanning) | Te plannen aanbod | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod |1 |
| 3 | Onderwijscatalogus | Student volg systeem (SVS) | Nominale leerroute (detail), keuze aanbod (detail) en resultaatstructuren | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | 2 |
| 4 | Leer management systeem (LMS) | Onderwijscatalogus | Van leermiddel te voorziene aanbod | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | 3  |
| 5 | Planningssysteem (meer jarenplanning) | Student volg systeem (SVS) | Mogelijke keuzes | Onderwijsontwikkeling, inrichting nominale- en keuze aanbod | - |
| 6 | Planningssysteem (jaar/periode) | Student Kiest (nog niet in MORA) | Inschrijving/intekening op te plannen opleidingsonderdeel / leeractiviteit | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 7 | Roostersysteem (periode) | Student Kiest (nog niet in MORA) | Aanbod beschikbare capaciteit | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 8 | Onderwijscatalogus | Roostersysteem (periode) | Acceptatie inschrijving/intekening Lesgroep | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 9 | Onderwijscatalogus | Student volg systeem (SVS) | Actualiseren resultaatstructuren obv keuzes | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 10 | Student Kiest (nog niet in MORA) | Student volg systeem (SVS) | Inschrijving op opleidingsprogramma | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 11 | Student Kiest (nog niet in MORA) | Kernregistratie systeem studenten (KRS) | Studenten, inschrijving nominale leerroute en initiële keuzes | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 12 | Student volg systeem (SVS) | Leer management systeem (LMS) | Toewijzing van leermiddelen obv keuzes | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 13 | Student volg systeem (SVS) | Toets- en examen afname systeem | Voortgang uitkomsten en resultaten | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 14 | Kernregistratie systeem studenten (KRS) | Student | Is ingeschreven | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 15 | Student | Student Kiest (nog niet in MORA) | *In aanbouw* (impliciete keuze-interactie door de student) | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 16 | Planningssysteem (jaar/periode) | Roostersysteem (periode) | Planning | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |
| 17 | Roostersysteem (periode) | Planningssysteem (jaar/periode) | Realisatie | Student studeert, maakt keuzes / onderwijsuitvoering (flexibel onderwijs) | - |

*Waar uit de plaat geen eenduidige tekst of component kon worden afgeleid staat *in aanbouw*; overige rijen kunnen door het kernteam worden aangevuld of verfijnd (circa 20 lijnen in de plaat).*

## Relatie tot ArchiMate-model (in deze repo)

Het functionele en technische ontwerp wordt ondersteund door een **ArchiMate-model** in [`architecture/model/model.archimate`](../architecture/model/model.archimate). Dit model bevat o.a. **MOKA-koppelvlakspecificatie-views**; de view **01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model** is een groot diagram om stroom **1** (curriculumontwerp → onderwijscatalogus) t/m 17 en aanverwante processen te verdiepen — zie [Informatiestromen, ArchiMate en MOKA-view](OKx_Informatiestromen-ArchiMate-en-MOKA-view.md).



## Werkwijze: async ontwikkelen

- Ontwikkeling verloopt **asynchroon**: documentatie en specificaties worden iteratief bijgewerkt op basis van input uit de keten en vanuit BOPSI.
- Wijzigingen gaan via **issues** en **pull requests**; geen directe commits op de hoofdbranch zonder review waar dat van toepassing is.
- Versiebeheer en historie blijven zichtbaar in Git.

## Bijdragen: issues en PRs

- Voorstellen, vragen en fouten: graag via **issues** in deze repository.
- Concrete wijzigingen in documenten of specificaties: via **pull requests**, bij voorkeur gekoppeld aan een issue.
- Contact voor toegang en afstemming: **niek.derksen@surf.nl**.

## Repo-inhoud (kort)

| Onderdeel | Locatie | Inhoud |
|-----------|---------|--------|
| OKx context | `doc/`, `img/` | Projectoverzicht, besluitboom/historie, informatiestromen, bijlagen |
| Architectuurbesluiten (samenvatting) | [`doc/OKx_Architectuurbesluiten-en-impact.md`](OKx_Architectuurbesluiten-en-impact.md) | ADR’s, impact op keten/model |
| ArchiMate en MOKA-view (gids) | [`doc/OKx_Informatiestromen-ArchiMate-en-MOKA-view.md`](OKx_Informatiestromen-ArchiMate-en-MOKA-view.md) | Hoofdplaat ↔ model ↔ Basis Model-view |
| OKE uitwerking | `OKE/` | Eerste subdomein-uitwerking (o.a. examen: uitvoering en beoordeling) |
| Generiek template | `moka-koppelvlakspecificaties/Template/` | MOKA-template en generieke instructies |

Zie ook de [root README](../README.md) voor de generieke intro, repo-indeling en de verwijzingen naar Wiki/Discussions, en [Bijdragen voor beginners](Bijdragen-voor-beginners.md) voor git/GitHub, branches en PR’s.
