# Scenario 1.2: regulier, vertraging by accident

**Doel.** Toetsen hoe de keten een incidentele vertraging verwerkt terwijl specificatie en aanbod ongewijzigd blijven: alleen de verbintenis muteert en er komt een inhaalgelegenheid.

**Scope.** Leerroute 1 met vertraging by accident; delta ten opzichte van [scenario 1.1](scenario-1.1-regulier-happyflow.md). Status: pitch, nog uit te werken. Het sjabloon, de casus en de samenhang staan in de [README](README.md). Relateert aan: #137.

> **Status.** *By accident, alleen vertraging.* **Pitch.** *Halverwege periode 2 wordt Jochem ziek (lange griep, daarna concentratieproblemen). Hij mist drie weken onderwijs, haalt twee leergelegenheden niet op tijd, en moet in periode 3 of 4 inhalen — waardoor hij voor één werkproces uit ritme raakt en uiteindelijk twee maanden uitloopt op zijn diploma.*
>
> **Verschil met 1.1 in begrippenkader-taal.** Aanbod en specificatie blijven gelijk. De **verbintenis-state** muteert anders: `participating → onderbroken → participating`. Voor minstens één werkproces wordt een **extra** `Association` aangemaakt op een latere `Leergelegenheid`-periode (planbaar werd opnieuw geroosterd voor Jochem). De toetsrij krijgt een tweede `Toetsgelegenheid-verbintenis`.
>
> **Wat dit raakt in het sjabloon.** D (verhaal): SLB'er en Planner krijgen een rol als bemiddelaar; Onderwijsontwerper níet. E (Then op startmoment van periode 3): één rij toont `participating` waar de baseline `completed` zou tonen. F (architectuurlagen): Beleid t.a.v. langdurige uitval, Organisatie t.a.v. inhaaltrajecten, Data t.a.v. resultaat-overdracht tussen perioden.
>
> *— Volledige uitwerking in een vervolgsessie.*
