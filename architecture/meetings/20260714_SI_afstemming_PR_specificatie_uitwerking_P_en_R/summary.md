## Progress

- **Niek Derksen**
    - **Inrichting Claude Code**
        - Heeft Claude Code opgezet en de bijbehorende skill files en setup ingericht om mee te experimenteren.
    - **Uitwerking release management aanpak**
        - Heeft een relatief uitgebreide memo en aanpak voor release management opgesteld in een Markdown-document binnen de openstaande pull request.
        - Heeft op basis van feedback van **Niels van Duin** een uitgangspunt toegevoegd waarin is vastgelegd dat er maximaal twee major versies (de nieuwste en de voorlaatste) actief ondersteund worden.
    - **Semantische definitie mapping**
        - Heeft een conceptuele plaat uitgewerkt die de mapping van het huidige taalgebruik, referentiekader en OEAPI-modellen semantisch in kaart brengt. Hierin is onder andere geconstateerd dat het concept 'vraag-om-ongepland-aanbod' niet direct te mappen is naar een OEAPI-model.
- **Garik Hakopian**
    - **Afstemming met Hans over definitie mapping**
        - Heeft het knelpunt over de definitie mapping en de aansluiting met de fysieke realiteit besproken met Hans. Hieruit is het leidende uitgangspunt overgenomen dat de op te leveren specificatie en definitie mapping leidend zijn en dat de organisatie hiernaartoe moet bewegen.
    - **Inrichting VS Code**
        - Is gestart met het opzetten en inrichten van de Visual Studio Code werkomgeving.
- **Niels van Duin**
    - **Review release management memo**
        - Heeft de conceptversie van de release management memo in de pull request doorgenomen en feedback geleverd over het beperken van de actieve ondersteuning tot maximaal twee major versies.

## Upcoming Priorities

- **Niek Derksen**
    - **Herstructurering van de repository**
        - Het opsplitsen en logischer structureren van het huidige, grote specificatiedocument van circa 50 à 60 pagina's in kleinere Markdown-bestanden binnen een duidelijke mappenstructuur (zoals begripskader, gegevensstandaard, interactieanalyse en scenarioanalyses).
        - Het opzetten van een 'starting point' of gids om lezers te helpen navigeren door de hergestructureerde repository, gebaseerd op een tip van **Garik Hakopian**.
        - Deze herstructurering zal worden opgezet met behulp van Cloud Code in een nieuwe pull request, mits de huidige openstaande pull request eerst is afgerond om merge-conflicten te voorkomen.
    - **Uitwerking leerroute 2**
        - Het verder uitwerken van leerroute 2 op basis van de gedefinieerde persona's.
    - **Definiëren van AI-skills en commando's**
        - Het inrichten van een 'harnas' binnen Cloud Code door skills aan te vullen en commando's te definiëren. Dit moet zorgen voor scherpere formuleringen en een consistent taalgebruik door de AI-assistent, wat ook door **Garik Hakopian** gebruikt kan gaan worden.
- **Garik Hakopian**
    - **Review van openstaande pull requests en documenten**
        - Het inhoudelijk bestuderen en reviewen van de openstaande pull requests en repositories.
        - Het doornemen van de door **Niek Derksen** opgestelde memo over release management om feedback te kunnen leveren.
    - **Inzien van het specificatiedocument**
        - Het opzoeken en bestuderen van het huidige specificatiedocument zodra de herstructurering hiervan door **Niek Derksen** is ingezet.
    - **Plannen van afstemmingsbijeenkomsten**
        - Het inplannen van een terugkerende overlegstructuur met **Niek Derksen** (één of twee keer per week) om samen door de voortgang en inhoud te lopen.
- **Niels van Duin**
    - **Aanmaken van een nieuwe branch voor Issue 82**
        - Het aanmaken van een aparte branch voor Issue 82, het toevoegen van een bijbehorend Markdown-bestand en het indienen van een pull request richting de dev-branch voordat hij met vakantie gaat.

## Blockers & Challenges

- **Risico op merge-conflicten**
    - Er is een verhoogd risico op complexe merge-conflicten op de dev-branch als **Niek Derksen** start met de grote herstructurering van de repository voordat de huidige openstaande pull request volledig is afgerond en gesloten.
- **Weerstand in de sector door communicatiestijl**
    - Er is een risico op weerstand bij architecten in de MBO-sector (zoals signalen van Joël richting **Niek Derksen**) door de communicatiestijl van Hans. Wanneer Hans naar buiten toe claimt dat "wij de MORA gaan veranderen", wekt dit weerstand op omdat de MORA binnen de sector als heilig wordt beschouwd. Dit kan het adoptieproces van de producten bemoeilijken.
- **Onvolledige aansluiting op de OEAPI-standaard**
    - Het concept 'vraag-om-ongepland-aanbod' kan momenteel niet worden gemapt naar de OEAPI-modellen. Dit is geïdentificeerd als een tekortkoming in de beoogde standaard ten opzichte van de eigen kaderstelling en vereist nog verdere afstemming met experts.
- **Beperkingen van één groot specificatiedocument**
    - Het huidige specificatiedocument is met 50 tot 60 pagina's te omvangrijk en onoverzichtelijk geworden. Dit leidt tot renderproblemen in GitHub met inline mermaid-diagrammen en maakt het document lastig te navigeren voor externe lezers.