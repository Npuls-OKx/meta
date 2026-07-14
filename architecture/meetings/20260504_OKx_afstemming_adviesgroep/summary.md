## Executive Summary

- **Aanpassing architectuurplaat (v1.5):** De _Onderwijscatalogus_ is van de linker- naar de rechterkant verplaatst om aan te sluiten bij de studentreis, waarbij de focus ligt op fijnmazige specificaties zodra een student keuzes maakt.
- **Strategie voor leveranciersoverleg:** **Ruud** en **Niek Derksen** besloten om vanmiddag een luisterende houding aan te nemen richting Jan Hennik van Schaik; fundamentele wijzigingsvoorstellen moeten door leveranciers zelf via een gap-analyse en het _Kerngroep Techniek_ worden ingediend.
- **Planning Werkgroep OKX:** Een nieuwe sessie wordt gepland in de week van **25 mei** om voortgang te tonen, bevindingen van de koploperronde te delen en de nieuwe versies (1.4/1.5) van de hoofdplaat te bespreken.
- **Koploperonderzoek:** **Niels van Duin** start een ronde langs scholen om vier scenario's (waaronder werken zonder _SKS_) scherp te krijgen en de effecten van groepsdynamiek op de technische architectuur te valideren.
- **Status testomgeving:** **Niek Derksen** wacht nog op een reactie van _Educator_ over het opzetten van een sandbox-omgeving na het voorstel van **16 april**.

## Full Summary

### AI-integratie en Governance

- **Ruud** deelt ervaringen met de implementatie van Microsoft Copilot en uit frustratie over de beperkte automatisering in Outlook.
    - Het handmatig moeten kopiëren van door AI gegenereerde teksten naar e-mails wordt als een significant gemis in gebruiksgemak ervaren.
    - **Niek Derksen** legt uit dat deze beperkingen voortvloeien uit Europese wetgeving en aansprakelijkheid rondom governance.
        - Technologiebedrijven bouwen zelfbescherming in om te voorkomen dat AI-agenten zelfstandig foutieve afspraken maken of ongepaste mails versturen (hallucinaties).
        - Er wordt verwacht dat een human in the loop het komende jaar de standaard blijft voor acties zoals het versturen van e-mails binnen de EU.

### Strategie en Stakeholdermanagement voor de Middagsessie

- Voor de sessie met Jan Hennik van Schaik adviseert **Ruud** een luisterende maar begrensde houding aan te nemen.
    - Er moet gewaakt worden voor te veel dominantie vanuit leveranciers; de samenwerking moet tweezijdig blijven.
    - Hans heeft via een telefoontje aangegeven dat individuele leveranciers niet eenzijdig de koers mogen bepalen.
    - Wijzigingsvoorstellen vanuit leveranciers zijn welkom, mits zij zelf een gap-analyse uitvoeren tussen hun huidige uitwerking en de voorgestelde delta.
- **Niels van Duin** merkt op dat er een aanzienlijke kloof (gap) zit tussen de huidige status van de architectuur en de informatie die leveranciers op basis van eerdere sessies hebben.
    - Leveranciers kijken nu pas naar de ontwikkelingen op GitHub, terwijl de discussie daar al verder gevorderd is.
    - Er is consensus dat de richting van de ontwikkeling (zoals de scheiding van componenten) inmiddels breed wordt gedeeld.

### Technische Architectuur en de Hoofdplaat

- De ontwikkeling van de architectuurplaten vordert van versie 1.3 (publiek) naar conceptversies 1.4 en 1.5.
    - De belangrijkste wijziging is de positionering van de Onderwijscatalogus (OC), die is verplaatst van de voorbereidende fase (links) naar de uitvoeringsfase (rechts).
    - Het Student Keuzesysteem (SKS) is losgekoppeld van het Student Volgsysteem (SVS) om meer flexibiliteit in de studentreis te faciliteren.
- Er is een lopende discussie over de eigenaarschap en definitie van groepen binnen de systemen.
    - Groepen ontstaan enerzijds vanuit planningsperspectief voor de uitvoering en anderzijds vanuit het onderwijsconcept (KRS).
    - **Niek Derksen** stelt dat sociale cohesie een secundaire voorwaarde (constraint) is die volgt op de gemaakte keuzes van studenten, in plaats van een leidend principe voor de planning.
    - **Ronald Kollen** benadrukt dat het essentieel is om vast te stellen welk referentiecomponent leidend is voor het beheer van groepen, zeker met het oog op Identiteits- en Toegangsbeheer (IAM).

### Operationele Updates en Planning

- De status van de testomgeving voor Educator en Topicus blijft onduidelijk.
    - **Niek Derksen** heeft op 16 april een voorstel gestuurd voor een overleg over de sandbox-omgeving, maar heeft hier nog geen reactie op ontvangen.
- De agenda voor de komende periode wordt bemoeilijkt door vakanties en externe evenementen.
    - Op woensdag 13 mei is een netwerksessie van MBO Digitaal, waardoor leveranciers tussen 13:30 en 15:00 uur onbereikbaar zijn.
    - De voorkeur gaat uit naar sessies op woensdag, hoewel 20 mei als alternatief wordt gezien.
    - **Niek Derksen** is vanaf 3 juni voor ongeveer 15 dagen afwezig wegens vakantie in Portugal.
- De volgende Werkgroep OKX wordt voorlopig gepland in de week van 25 mei of begin juli.
    - Het doel van deze sessie is primair een voortgangsupdate over de versies 1.4 en 1.5 van de platen en het delen van bevindingen uit de koploperronde.
    - **Niels van Duin** zal tijdens de koploperronde specifiek navraag doen naar de huidige groepsdynamiek en de visie op flexibilisering bij de instellingen.