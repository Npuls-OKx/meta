# Scenario 2.1: temporiseren by design (anker leerroute 2)

**Doel.** De baseline voor leerroute 2 vastleggen: dezelfde opleiding bewust op lager tempo, als track op de programma-specificatie, met alternatief planbaar aanbod naast het reguliere.

**Scope.** Leerroute 2 (temporiseren by design), zonder incidenten; delta ten opzichte van [scenario 1.1](scenario-1.1-regulier-happyflow.md). Status: pitch, nog uit te werken. Het sjabloon, de casus en de samenhang staan in de [README](README.md). Relateert aan: #137.

> **Status.** *By design, baseline voor leerroute 2.* **Pitch.** *Jochem is dit jaar 24, werkt 24 uur per week in een drogisterij en heeft een gezin. Hij wil dezelfde Apothekersassistent-opleiding doen, maar op **lager tempo by design**: 4 jaar in plaats van 3, met 60% van de nominale studiebelasting per periode. Geen vrijstellingen — alleen meer tijd.*
>
> **Verschil met 1.1 in begrippenkader-taal.** Specificatie van de opleiding (kolom 3 op rij Kwalificatiedossier/Kwalificatie) krijgt een **track "Temporiseren"** — `programmeType: "track"`, `consumer.okx.leerrouteType: "getemporiseerd"`. Onderwijseenheid- en leeronderdeel-specificaties blijven dezelfde objecten, maar de **planbaarheid** (stadium 2a) wijzigt: andere `spreadPattern`, andere `timeAllocation` (zelfde BOT, OOT verspreid), andere periodelengte.
>
> **Wat dit raakt.** Onderwijsontwerper voegt track toe (kolom 3, rij Kwalificatie). Planner maakt **alternatief planbaar aanbod** parallel aan het reguliere (stadium 2a, andere perioden). SLB'er plaatst Jochem op de track "Temporiseren" (kolom 5, rij Kwalificatie — andere verbintenis-attributen). Roostering en docentinzet kunnen — als de instelling slim ontwerpt — gedeeld worden met regulier (zelfde leergelegenheden, andere route door de leergelegenheden).
>
> **9-architectuurlagen-aanvulling t.o.v. 1.1.** Beleid: instelling moet leerroute "Temporiseren" als formele variant erkennen (bekostiging, examenmoment-vrijheid, studieduur-toezicht). Organisatie: SLB'er-capaciteit voor maatwerk-trajecten. Data: `learningRouteType`-attribuut op programma; ABC-relatie tussen track en leergelegenheden expliciet.
>
> *— Volledige uitwerking met §B Given, §D verhaal, §E Then op startmoment, §G placeholder in een vervolgsessie.*
