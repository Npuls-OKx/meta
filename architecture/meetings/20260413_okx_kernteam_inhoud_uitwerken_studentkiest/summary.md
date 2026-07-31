## Meeting: OKx Kernteam – Inhoud uitwerken StudentKiest

Datum: 2026-04-13

Aanwezig: Niek Derksen, Niels van Duin, Mark Hoogenboom, Alda Kroneman

Doel: Uitwerken van het keuzemoment en de leerroute binnen het StudentKiest-proces (SKS), met focus op het procesontwerp van macro naar micro.

### Samenvatting

Het team heeft het keuzemoment van de student in het StudentKiest-proces uitgewerkt op drie niveaus (macro, meso, micro). Op **macroniveau** filtert de student het aanbod op geolocatie, afstand, budget en globale leeruitkomsten. Dit leidt tot een selectie van instellingen met een match-percentage. Vervolgens start de **intake** bij een instelling, waarbij behaalde credentials uit de ontwikkelingswallet worden gecontroleerd en de leervraag wordt geëvalueerd.

Na de intake volgt een **keuzegate**: volgt de student een nominale (standaard) leerroute, of wordt er een volledig maatwerk-leertraject samengesteld? Bij nominaal krijgt de student een voorgeladen route met beperkte personalisatie (differentiatie op leeractiviteitniveau). Bij maatwerk stelt de student zelf leeractiviteiten samen in een "sandbox".

Mark bracht in dat de leerroute als **losse entiteit** vóór inschrijving bij een specifieke instelling moet kunnen bestaan — een globale route waarmee de student bij meerdere scholen kan "shoppen". Het team is het erover eens dat het procesmodel dit ondersteunt: je kunt meerdere parallelle trajecten bij verschillende scholen lopen.

Over **microcredentials** is besloten dat OKx de invulling daarvan (wat is een leeruitkomst precies?) bij de sector laat. De instelling is de issuer; Edubadges.nl is het register. Microcredentials zijn pas relevant bij toetsing, niet in de huidige fase van het keuzemoment — behalve bij de intake, waar behaalde credentials als **toelatingsvoorwaarde** worden gecontroleerd.

Het keuzeniveau voor de student is vastgesteld op de **leeractiviteit**: een collectie van leeropdrachten en bijbehorende lesuitkomsten. Daaronder (individuele leeropdrachten, lesvorm) is te fijnmazig voor de voorkant.

### Besluiten

- De student kiest op het niveau van **leeractiviteit** (collectie van leeropdrachten + lesuitkomsten), niet dieper.
- Een **leerroute** moet een losse entiteit zijn die vóór inschrijving bij een instelling kan bestaan (cross-instelling).
- Het gedetailleerde **leertraject** (planning, dagen, logistiek) wordt pas binnen de instelling uitgewerkt.
- **Microcredentials**: de issuer is de instelling; de definitie van een leeruitkomst/microcredential valt buiten scope van OKx.
- Bij de intake moeten behaalde **credentials gecontroleerd** worden (als toelatingsvoorwaarde).
- Nominale route vs. maatwerk is primair een **systeem/proceskeuze**, geen onomkeerbare beslissing — studenten kunnen later alsnog switchen (continuous change of state).
- Leervormen (WPV, school, online) zijn **kenmerken van het aanbod** in de onderwijscatalogus, geen apart keuzemoment.

### Open vragen

- Hoe ziet de UX eruit voor studenten op MBO niveau 1-2-3 die beperkt zelf kunnen kiezen? (oriëntatiefase eerst?)
- Hoe verhoudt de overkoepelende leerroute zich tot de instelling-specifieke leertrajecten in het datamodel?
- In hoeverre kan AI/ChatGPT het samenstellen en adviseren van leerroutes automatiseren?
- Welke rol speelt het Rijnlands model (bijv. keuze WPV vs. school) bij de nominale leerroute?

### Actiepunten

- Niek stuurt transcript en samenvatting naar Alda - eigenaar: Niek Derksen - deadline: 2026-04-14
- Procesplaat bijwerken met credential-controle vóór intake en keuzegate nominaal/maatwerk - eigenaar: Niek Derksen / Niels van Duin - deadline: TBD
- Vervolgsessie plannen (volgende week vrijdag) - eigenaar: Alda Kroneman - deadline: 2026-04-18

### Links (verplicht)

- Issues: TBD
- ADR's: `https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md`, `https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md`, `https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/0013-microcredentials-scope-en-credentialcontrole-intake.md`
- OKx/OKE docs: TBD
- ArchiMate impact: ja – de keuzegate nominaal/maatwerk, leeractiviteit als keuzeniveau en de rol van de ontwikkelingswallet/credentials moeten in het model verwerkt worden
- Transcript: `architecture/meetings/20260413_okx_kernteam_inhoud_uitwerken_studentkiest/transcript.md`