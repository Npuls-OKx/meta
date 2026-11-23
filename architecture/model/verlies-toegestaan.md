# Elementen die met opzet uit het model zijn gehaald

`tools/scripts/controleer-modelverlies.py` vergelijkt het model met de versie ervoor en faalt zodra er een element verdwijnt. Die controle bestaat omdat een regelgebaseerde merge in juli 2026 276 elementdefinities liet wegvallen in een bestand dat intern bleef kloppen.

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

## Ronde 13 november 2026

De verantwoording staat in pull request [#553](https://github.com/Npuls-OKx/meta/pull/553), met per groep de reden en de meting erbij. Hieronder alleen de ids, want het script leest niets anders uit dit bestand.

Drieendertig elementen in vier groepen: drie stromen uit #393 opnieuw getekend met een nieuw id, vijf views opgeruimd omdat de versie naar de export verhuisde, twee views opnieuw opgezet, een relatie vervangen door PR 391, en tweeentwintig objecten en relaties die volgens het model niet gebruikt werden.

- `id-01169a4550f4491c950c7d18f2ccdad3`
- `id-191d2f54dbef4e1f8377e54c53c53c5b`
- `id-223b51dd43fb43f993a1a9a5a9ca5aa1`
- `id-27120176cd824664ac866d6b5a02031f`
- `id-3a4c2ab1a1a3441ebf4980b132773497`
- `id-3cffa1e310244d1caae04d22d1669431`
- `id-484978f94b064e89bd6f62c4acb35660`
- `id-4f41b8be8e0a430fb109c3ea65638528`
- `id-53df0b18fd3d40a3b4b56a3ce8d8bcba`
- `id-560522d89f0d4f48b01c74189b9e502e`
- `id-597083de91fb4828a8f4b9cf00b467fd`
- `id-67b13ef05330492ab7400abb8044a6f0`
- `id-688164805dd5462c86fb4164f5b28f28`
- `id-6afd6145090f49359ca10cdf382427ba`
- `id-73277c8522ca4573aa625ad308445f12`
- `id-756fd7922f6444bda3efc40b47c0c0d6`
- `id-76b57ef5740e48de8cb7d1e679d783cb`
- `id-7d38428481ae4ec1950530397e37e31c`
- `id-965bdcd610454fd09fcccdfd0742f5cf`
- `id-9d62e38754e74f9f9bcec451d559288c`
- `id-b9aba75ae4ee4a7bb52297b181817094`
- `id-bfd91786e3bc4fea8842438cc0d4b97f`
- `id-c49e2b71aab34a1193a536adf36bea28`
- `id-ce02acba3ebb4e959d9d5723c25546fe`
- `id-ceec4b79167c43bb8b7042775576d0ea`
- `id-cf0ba8feb4a54605a6c31a3cf4ed0308`
- `id-cf386efb216448fc9d8643c7d6587c78`
- `id-d262de8a69ec4b10bcd63f2e5e47052f`
- `id-dc14c45bf8c94c1ba7b428ca2a2d5de2`
- `id-f527e61690404f5dba90db56543874b2`
- `id-f6b2a952c77e4c2d850bae94c5db1582`
- `id-faa572af06224df69996f8850d39c698`
- `id-fdc38824408246a89ff9f0c0f9d33556`
