# Lezerspersona's

Een lezerspersona is de lezer door wiens ogen een deliverable geschreven en gereviewd wordt. De maker kiest de persona vooraf, de reviewer neemt dezelfde rol aan bij het toetsen. Elke persona beschrijft de rol, de kennis en vaardigheden die de lezer meebrengt, zijn afstand tot OKx en de kennisbank, zijn leesdoel en de punten waarop hij afhaakt. Waar belangen meespelen staan die er ook bij.

## Gelaagdheid

Sommige persona's zijn een verzamelrol: zij beschrijven een gremium of team en verwijzen naar de onderliggende rollen met hun eigen accenten. Ken je de concrete lezer, kies dan de onderliggende rol. Gaat een document het hele gremium aan, kies dan de verzamelrol.

## Afbakening

Een lezerspersona is geen domeinpersona. Jochem, Larissa en Linda in de [leerroute-uitwerking](../../architecture/docs/specificatie/leerroute-uitwerking/doc/) zijn studenten in een scenario; een lezerspersona is degene die een OKx-document leest.

## Persona kiezen

De keuze volgt meestal uit het deliverable: een architectuurbesluit is voor de informatiemanager en de enterprise architect, een interactiepatroon voor de softwarearchitect bij een leverancier, een kaderscenario voor de onderwijskundig procesbespecialist. Raakt een document meerdere lezers, kies dan de lezer met de grootste afstand tot OKx; die bepaalt hoeveel uitleg nodig is. Afleiden uit de context mag. De maker benoemt de gekozen persona altijd ter controle in de PR-beschrijving of op een stopmoment; de reviewer benoemt in het rapport welke persona hij heeft aangenomen.

## Binnen het OKx-kernteam

[Kernteamlid](kernteamlid.md) is de verzamelrol voor werkafspraken die het hele team aangaan.

| Persona | Team | Leest vooral |
|---|---|---|
| [Solution architect](solution-architect-si.md) | SI | Alle deliverables, besluiten en specificaties |
| [Informatiearchitect](informatiearchitect.md) | BOP, met SI | Begrippenkader, datamodelschema's, gegevenssets |
| [Onderwijskundig procesbespecialist](bop-procesbespecialist.md) | BOP | Kaderscenario's, leerroute-uitwerking, bovenste boomlagen |
| [Testcoördinator](testcoordinator.md) | BOP, met SI | Functionele eisen, interactiepatronen, acceptatiecriteria |

## Sturing op het project

Beiden zijn geen specialist. Zij willen keuzes voorgelegd krijgen als korte afweging: A, B of C, met per optie het gevolg in een of twee zinnen en een aanbeveling.

| Persona | Verantwoordelijkheid | Leest vooral |
|---|---|---|
| [Projectmanager](projectmanager.md) | Operationeel: planning, capaciteit, scope | Milestones, voortgang, bovenste boomlagen |
| [Programmamanager en opdrachtgever](programmamanager-opdrachtgever.md) | Strategisch: richting, mandaat, besluiten | Opdracht en doelen, besluitpunten, samenvattingen |

## In de gremia rond OKx

[Lid kerngroep techniek](lid-kerngroep-techniek.md) is de verzamelrol voor de kerngroep; de deelnemers zijn architect, technisch specialist of product owner.

| Persona | Belang | Leest vooral |
|---|---|---|
| [Lid technische werkgroep, sector](lid-technische-werkgroep-sector.md) | Een standaard die overal werkt, leveranciersonafhankelijk | Specificaties, mapping, standaardbesluiten |
| [Lid technische werkgroep, leverancier](lid-technische-werkgroep-leverancier.md) | Samenhang eigen productlandschap, lagere beheerlast | Interactiepatronen, gegevenssets, afbakening |

## Bij instellingen en leveranciers

| Persona | Rol | Leest vooral |
|---|---|---|
| [Informatiemanager van een instelling](informatiemanager-instelling.md) | Bepaalt impact op de eigen instelling | Besluiten, uitgangspunten, releases |
| [Enterprise architect van een instelling](enterprise-architect-instelling.md) | Toetst doelarchitectuur en semantische samenhang | Besluiten, principes, afbakening, componentindeling |
| [Softwarearchitect bij een leverancier](softwarearchitect-leverancier.md) | Bouwt de koppeling in een product | Koppelvlakspecificaties, interactiepatronen, schema's |
