# Historisch overzicht OKx

Rode draad: OKx begon als specificatieproject en ontdekte dat de kaderstelling eronder ontbrak. Elke verschuiving sindsdien legt die kaderstelling alsnog. De tijdlijn op hoofdlijnen staat in [deel 2 van de leesroute](leesroute.md#deel-2-historisch-overzicht); hieronder staat het moment voor moment, met de bron erbij.

**Werk in uitvoering.** Dit overzicht is nog niet compleet; er horen meer momenten in dan er nu staan. Het aanvullen loopt via [#468](https://github.com/Npuls-OKx/meta/issues/468).

## November 2024 tot februari 2026

Bron: het projectplan en het geheugen van het team. De kennisbank en de meetingverslagen beginnen in maart 2026.

| Wanneer | Wat er gebeurde | Bron |
|---|---|---|
| november 2024 | De opdracht wordt vastgelegd, met zes use-cases voor studentmobiliteit van binnen de eigen opleiding tot over landsgrenzen heen | [OKx in context](context.md) |
| januari 2025 | Een tweedaagse met instellingen, ondersteunende organisaties en leveranciers scherpt de scope aan en kiest voor een hoofdproces met varianten. Het projectplan wordt daarna aangepast tot versie 2.1, en de uitkomst krijgt een eigen advies: *Advies gegevensuitwisseling voor flexibilisering (OKX)*. Daar ontstaan de startflows, en daar ontstaat het uitgangspunt dat OKx op de Open Education API aansluit tenzij een eis dat onmogelijk maakt | [Projectplan, versie 2.1](projectdocumentatie/projectplan-okx.md), [de startflows](img/startflows-doelgebied-20251217.png) |
| najaar 2025 | Onderzoek naar de kaderstelling en de doelstellingen van OKx: wat het project moet opleveren, en hoe die producten zich tot elkaar verhouden. Daar worden de productomschrijvingen gedefinieerd | [Doel en resultaten](img/doel-en-resultaten-20251217.png) |
| najaar 2025 | Het team vormt een interne visie op de hele keten, van onderwijsontwerp tot onderwijsuitvoering en leven lang ontwikkelen. Die procesmodellen dragen alles wat er daarna uit voortkomt | [Leerroute-uitwerking](../architecture/docs/specificatie/leerroute-uitwerking/) |
| najaar 2025 | De definitiemapping tussen MORA en de Open Education API, gericht op het formaliseren van wat OKx van de standaard nodig heeft. Het uitgangspunt OEAPI tenzij ligt er dan al | [Definitiemapping MORA en OEAPI](../architecture/docs/definitie_mapping_MORA_OEAPI_excel/) |
| september tot november 2025 | Architectuurmappingsessies met scholen: procesmapping, informatieobjecten ophalen, het instellingsperspectief ophalen, en de toets of werken vanuit MORA houdbaar is | [Mappingsessies met instellingen](../architecture/docs/mappingsessies-instellingen/) |
| najaar 2025 | Alignment met de architectuurgremia van het mbo via MOKA, de koppelvlakaanpak van MORA. De MOKA-werkgroep wordt daarbij klaargemaakt voor de kaderstellende rol van gatekeeper en reviewer | [MOKA-sjabloon, gearchiveerd](../archief/MOKA/) |
| december 2025 | Het IT-landschap van een instelling wordt voor het eerst beschreven, in de hoofdplaat informatiestromen. Die plaat draagt sindsdien elke uitwerking | [De huidige vorm van onderwijslogistiek](img/onderwijslogistiek-huidige-vorm-20251217.png), [de aandachtspunten](img/aandachtspunten-20251217.png) |
| januari en februari 2026 | De inzichten uit het najaar worden verwerkt. Het team heroverweegt de werkwijze radicaal en richt haar opnieuw in, met agentisch werken als onderdeel daarvan | [AGENTS.md](../AGENTS.md) |

## Maart 2026 tot vandaag

| Wanneer | Wat er gebeurde | Bron |
|---|---|---|
| maart 2026 | De kennisbank wordt ingericht: architectuurprincipes, de procesmodellen uit de mappingsessies, en het studentkeuzesysteem als zelfstandige referentiecomponent | [ADR 0005](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) |
| maart 2026 | Het uitwerken van de kaderstelling begint, te beginnen bij de criteria waarop een student kiest | [Kaderstelling student keuze criteria](../architecture/meetings/20260331_okx_kernteam_inhoud_uitwerken_kaderstelling_student_keuze_criteria/) |
| maart tot mei 2026 | Leveranciers haken aan: eerst een eigen sessie, daarna de challenge op hoofdplaat 1.3 | [Voorbereiding leveranciersessie](../architecture/meetings/20260327_OKx_kernteam_inhoud_voorbereidingleveranciersessie/), [challenge met leveranciers](../architecture/meetings/20260506_challenge_hoofdplaat1.3_leveranciers/) |
| voorjaar 2026 | De kaderstellende rol van de MOKA-werkgroep blijkt op vrijwillige inzet niet te dragen. OKx gaat de kaderstelling zelf maken | [MOKA-sjabloon, gearchiveerd](../archief/MOKA/) |
| april 2026 | Alignment met het initiatief dat de informatiemodellen van MORA en HORA op elkaar afstemt | [Begrippenkader](../architecture/docs/specificatie/leerroute-uitwerking/doc/begrippenkader.md) |
| mei 2026 | De studentreis en de instellingsreis worden de ordening van het werk: elke uitwerking begint bij wat een student of een instelling wil bereiken, en het domein eromheen bepaalt de indeling. De scenario's en het ontwerplab bouwen daarop, net als de sessies van de kerngroep techniek | [Ontwerplab en kerngroepsessies](../architecture/meetings/20260508_OKx_kernteam_inhoud_ontwerplab_scenarios_kerngroep_techniek_sessies/), [leerroute-uitwerking](../architecture/docs/specificatie/leerroute-uitwerking/README.md) |
| juli 2026 | De eerste poging om een koppelvlakspecificatie te releasen. Architectuurbesluiten en koppelingspecificaties verhuizen naar `Npuls-OKx/Public`; meta wordt kennisbank, Public draagt de release | [pull request 127](https://github.com/Npuls-OKx/meta/pull/127) |
| augustus 2026 | De leeruitkomst wordt afgestemd met de andere Npuls-pijlers en vastgelegd in een besluit. OKx is daarbij aanjager van het Npuls-project leeruitkomsten dat op 2 november 2026 start. De requirementsboom wordt als proefopstelling gebouwd om business aan techniek te koppelen | [ADR 0026](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md), [pull request 131](https://github.com/Npuls-OKx/meta/pull/131) |
| september 2026 | Het verdiepende informatiemodel en de begrippenlijst gaan naar Public, met de mapping naar MORA en het Kernmodel Onderwijsinformatie | [pull request 233](https://github.com/Npuls-OKx/meta/pull/233) |
| oktober 2026 | Het informatiemodel bereikt v0.2. De modeldoorloop van leerroute 1 toetst het model aan een echte opleiding. De koppelvlakspecificaties worden herzien naar interactieketens. De productroadmap wordt herijkt en getemporiseerd | [Public pull request 131](https://github.com/Npuls-OKx/Public/pull/131), [meta pull request 252](https://github.com/Npuls-OKx/meta/pull/252), [373](https://github.com/Npuls-OKx/meta/pull/373) en [387](https://github.com/Npuls-OKx/meta/pull/387) |
| oktober 2026 | Het vertrekpunt dat de vorm van OKE na te maken was voor de bredere scope van OKx, blijkt niet te schalen. Bij OKE volgen de functiegebieden uit stromen die vastliggen; bij OKx volgen de stromen pas uit de uitwerking per leerroute | [Onderzoek naar de OKE-vorm](../architecture/agent-artifacts/research/20261027_1248_oke-vorm-tegenover-okx-scope.md) |
| lopend | Een proefopstelling met instellingen haalt userstories op, om de hoofdvraag te beantwoorden: wat moet er gebouwd worden | [Projectstartarchitectuur](https://github.com/Npuls-OKx/meta/issues/421) |

De leeruitkomst draagt het model al langer dan augustus 2026; het besluit van die maand legt vast wat het team eerder in de praktijk al aanhield. Wanneer de kerngroep techniek precies is gestart staat niet in deze repository: het oudste spoor is het ontwerp van haar sessies in mei 2026, het oudste deck is dat van 19 augustus 2026. Die vraag ligt bij Niels van Duin.

Relateert aan: #427.
