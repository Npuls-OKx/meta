# Elementen die met opzet uit het model zijn gehaald

`scripts/controleer-modelverlies.py` vergelijkt het model met de versie ervoor en faalt zodra er een element verdwijnt. Die controle bestaat omdat een regelgebaseerde merge in juli 2026 276 elementdefinities liet wegvallen in een bestand dat intern bleef kloppen.

Een modelleur die in Archi iets weghaalt of vervangt laat datzelfde signaal afgaan. Dat is geen fout, en de reden hoort vastgelegd te zijn. Elke regel hieronder draagt een id en waarom dat element weg mocht. Het script leest de ids en laat ze door; de rest van de regel is voor een lezer.

Een regel vervalt vanzelf. Zodra de basis waarmee vergeleken wordt het element zelf niet meer kent, komt het niet meer in de melding voor en doet de regel niets meer.

## Ronde 14 oktober 2026

Drie aggregaties zijn vervangen door een compositie met een cardinaliteit, omdat een opleiding zonder programma geen opleiding is:

- `id-beacee61c73c496f8010fa0712e374b9` aggregatie `Opleiding specificatie` naar `Opleidingsprogramma specificatie`, nu een compositie `minimaal 1`
- `id-9e56a8dcda314208b0ff285f9c9d7c31` aggregatie `Opleidingaanbod` naar `Opleidingsprogramma aanbod`, nu een compositie `Minimaal 1`
- `id-7f9ac2ae25d249fd9ed92a73ace2ede9` aggregatie `Opleidingsaanbod van Instelling` naar `Opleidingaanbod`, nu een compositie `Minimaal 1`

Vier relaties zijn herzien in dezelfde ronde:

- `id-a5b3a1e33fbc4c119c31ce0bc97764ef` associatie `Opleiding aanbod  verbintenis` naar `Opleidingsprogramma aanbod verbintenis`; het objecttype is hernoemd en de relatie is een compositie geworden
- `id-8a0eec6a98e94725a5bf6e46e3eb3928` toegang `Student` naar `Cohort / periode`; het cohort hangt nu aan de `Inschrijving`, zie ontwerpkeuze 17
- `id-2d834170aa604d8dae8f830319a1a61c` associatie `Keuzedeelruimte` naar `Student keuze regelset`, opnieuw gelegd
- `id-a49f5827ce794cf39c5bf87a1bd22a29` specialisatie `Aanmelding` naar `Inschrijving`, opnieuw gelegd
- `id-37baf66a4b9347b2a1583e5d92ec3784` associatie vanaf `Programme` aan de OEAPI-kant van de mapping

De view `OKx informatiemodel` is opnieuw opgezet en draagt daardoor een nieuw id:

- `id-dd5f9cefb94e4727a3a366f25db7bd8b` de oude view, met 81 vakken en 273 verbindingen; de nieuwe draagt er 97 en 404
