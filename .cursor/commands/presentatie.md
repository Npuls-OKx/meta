Maak een OKx-presentatie of update-deck. $ARGUMENTS

Volg de skill [`okx-presentatie`](../../.agents/skills/okx-presentatie/SKILL.md) stap voor stap.

Vraag de gebruiker eerst om drie dingen, tenzij ze al uit de opdracht blijken:

1. **Voor welk gremium** — SI-team, adviesgroep, leveranciers, kerngroep techniek OKx, technische werkgroep OEAPI of programmamanagement. Dat bepaalt het abstractieniveau. Bij meerdere gremia: aparte decks, geen compromis.
2. **Welke periode** — vanaf welke datum verzamel je de wijzigingen.
3. **Waarvoor** — voortgangsupdate, besluitvraag of kennisoverdracht. Dat bepaalt waar het deck op uitkomt.

Daarna:

- Verzamel de wijzigingen uit **beide** repositories, `Npuls-OKx/meta` en `Npuls-OKx/Public`. Lees niet alleen de titels: open de gewijzigde documenten en de pull request-beschrijvingen, want daar staat de aanleiding.
- Groepeer per **thema**, niet per repository of per pull request.
- Vertaal elke wijziging naar wat er nu mogelijk is dat eerst niet kon.
- Bouw het deck met de `np-`-componenten uit `presentaties/style.css`; verzin geen losse inline-stijlen waar een class bestaat.
- Sla het op in `presentaties/JJMMDD_onderwerp.md`, nooit in de Public-werkmap.

Sluit af met het pad en het commando waarmee de gebruiker het deck opent.

Verzin geen voortgang. Elke bewering in het deck moet terug te voeren zijn op iets in een van beide repositories; kun je iets niet staven, laat het weg of benoem het als open punt.
