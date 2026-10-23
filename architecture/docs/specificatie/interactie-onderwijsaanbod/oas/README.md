# De OpenAPI-documenten van de keten onderwijsaanbod

Deze map draagt het koppelvlak van een component als OpenAPI 3.1-document. De documenten zijn gegenereerd en worden nooit met de hand bijgewerkt: een wijziging gaat naar de bron en daarna draait de generator opnieuw. Relateert aan: #374.

| Bestand | Waarvoor |
|---|---|
| `onderwijscatalogus.openapi.yaml` | Het koppelvlak van de onderwijscatalogus, de vorm om te lezen |
| `onderwijscatalogus.openapi.json` | Dezelfde inhoud, voor de keuring, de testgevallen en een werktuig dat geen YAML leest |

Alleen een component waarvan het hele koppelvlak in de bron staat krijgt een document. Een half document is minder waard dan geen, want een leverancier leest de leegte als een keuze.

## Bekijken

VS Code rendert een OpenAPI-document niet uit zichzelf, en GitHub ook niet. Er zijn twee wegen.

**In de editor**, met de extensie die de dev container meelevert ([`42Crunch.vscode-openapi`](https://github.com/42Crunch/vscode-openapi)). Na een rebuild staat zij er; los installeren gaat met `code --install-extension 42Crunch.vscode-openapi` in de container. Open het YAML-bestand en kies de voorbeeldweergave. Welke generator die weergave gebruikt, SwaggerUI of Redoc, staat in Preferences, Settings, Extensions, OpenAPI, onder "Default Preview Renderer". De extensie doet daarnaast codenavigatie, linting en schemacontrole.

**In de browser**, zonder extensie:

```bash
python3 scripts/bekijk-oas.py
```

Dat dient deze map op `http://localhost:8088` met een pagina die Redoc op het document richt. Er wordt niets naar schijf geschreven. Draait er al iets op die poort, geef dan `--poort 8089`. De server bindt op `0.0.0.0` en niet op de loopback alleen: een dev container stuurt de poort over IPv4 door, en een server die alleen op `[::1]` staat is daar niet te bereiken.

**Wat een weergave laat vallen.** Redoc zet het tonen van eigen velden standaard uit, en aangezet toont hij ze alleen bij de verzoekdetails en per veld. Het document draagt 119 `x-okx`-velden. De stand per operatie overleeft, want die staat ook in de `description`; de openstaande punten en de legenda van de werkbrieven verdwijnen, want die staan alleen in de eigen velden. Een weergave is daarmee een werkbeeld en geen publicatie: wie alleen het beeld leest ziet een contract zonder te zien wat eraan vastligt. Zie #380.

## Genereren

```bash
python3 scripts/genereer-oas.py
```

De generator leest `../operaties.json`, bundelt de schema's uit `../schemas/` en uit Npuls-OKx/Public, keurt het resultaat als OpenAPI 3.1 en schrijft beide vormen. Met `--alles` schrijft hij ook de componenten die nog niet volledig in de bron staan, voor wie de vorm wil zien.

De eigen velden die het document draagt:

| Veld | Wat erin staat |
|---|---|
| `x-okx-bron` | Welke interactiespecificatie en welke commit het document opleverde |
| `x-okx-openstaand` | De punten die nog een besluit vragen |
| `x-okx-werkbrieven` | De legenda per aangehaalde werkbriefcode, met haar eenheid ervoor, omdat elke eenheid haar eigen reeks nummert |
| `x-okx-ontvangen-meldingen` | Een melding die het component ontvangt. Haar adres is de `callbackUrl` uit `/abonnementen` en geen pad, dus OpenAPI heeft er geen plek voor |

`servers` draagt een plaatshouder op het gereserveerde `.invalid` (RFC 2606). `securitySchemes` is echt en volgt de auth-standaard uit Npuls-OKx/Public.
