# Requirementsboom uitwerkingsronde 2: verantwoording

Relateert aan: #152 (deze ronde), #130 (de boom-PoC). Vormconventies: [skill okx-requirements-boom](../../../.agents/skills/okx-requirements-boom/SKILL.md); eisen: [requirements-document](../design-docs/20260805_1600_requirementsboom-requirements.md).

## Vraag

Welke wijzigingen draagt de tweede uitwerkingsronde van de boom, op welke bron steunt elke nieuwe rij, en wat is er bewust niet gedaan?

## Eisen-delta ten opzichte van het requirements-document

Eis R4 (PoC-diepte) beperkte stories tot vier epics: dat was een fase-eis voor de proof of concept, geen blijvende structuurregel. Deze ronde verruimt R4: **elke epic draagt stories waar de bron hard is**; een epic zonder harde bron blijft zonder stories (E6 en E8 dragen daarom alleen features). De verruiming ligt via de pull request ter vaststelling voor; tot die vaststelling geldt zij als werkafspraak van deze ronde. De overige eisen (R1 tot en met R3, R5 tot en met R12) gelden onverkort en zijn na deze ronde opnieuw getoetst.

## Aanleiding voor de actualisaties

Sinds de extractie van 5 en 6 augustus zijn [Public PR 9](https://github.com/Npuls-OKx/Public/pull/9) (datamodellen en endpointtabellen) en [Public PR 15](https://github.com/Npuls-OKx/Public/pull/15) (ADR 0026) gemerged, en heeft Public de pakketstructuur omgebouwd: de map `Koppelvlakspecificaties/Koppelingspecificaties/` bestaat niet meer; de inhoud leeft nu in [`Interactiepatronen/`, `Applicatiecomponenten/` en `Datamodelschema's/`](https://github.com/Npuls-OKx/Public/tree/dev/Koppelvlakspecificaties). Daardoor waren meerdere bronlinks in de boom dood en meerdere "(in review)"-noten achterhaald.

## Geactualiseerde verwijzingen

| Rij | Was | Is | Reden |
|---|---|---|---|
| F1.2, F3.4 (verwijzing) | payload-onderwijsspecificatie / payload-onderwijsaanbod | Datamodelschema's, secties onderwijsspecificatie en onderwijsaanbod | payload-documenten opgegaan in de schema's |
| F1.3 (bron) | lifecycle-en-versionering.md | Datamodelschema's, regels bij de schema's | lifecycle-document opgegaan in de regels (versionering en manifest) |
| F1.4, F2.4, F3.3, F5.1 (bron of verwijzing) | koppelingspecificatie-oc-lms / -oc-p-en-r / -oc-sis | Interactiepatroon OC-LMS / OC-P&R / OC-SIS | koppelingspecificaties opgevolgd door interactiepatroon-documenten |
| F2.4 (bron) | ADR 0026 in review, Public PR 15 | ADR 0026, directe link | PR 15 gemerged |
| F4.3 (bron) | lifecycle-en-versionering.md | Interactiepatroon OC-SIS, acceptatietoets bij wijziging examenplan | de acceptatietoets is nu vastgelegd gedrag in het interactiepatroon |
| F6.3 (bron) | payload-onderwijsspecificatie §3.2 | Datamodelschema's, regels bij de schema's | ontwerpkeuzes (N:M via regelset, voorwaarden in behaalde leeruitkomsten) leven nu daar |
| F7.2 (bron) | Public PR 9 in review | auth-standaard.md | PR 9 gemerged; de auth-standaard is het vastgestelde document |
| S1.2 (koppeling), S1.3, S3.1, S3.2 (bron en koppeling) | koppelingspecificatie-paden | Interactiepatroon-paden met anker interactieoverzicht; de bron van S1.2 (archief §19) bleef gelijk | zelfde inhoud, nieuwe plek |
| Leeswijzer | PR 9 en PR 15 "in review"; ADR-register tot 0024; uitgangspunten tot U10; "Koppelingspecificaties"; link naar `../principes.md` | directe links; tot 0026 met de noot dat 0025 nog niet is uitgegeven; tot U11; Koppelvlakspecificaties met de drie deelmappen; alleen de Public-architectuurprincipes | merges, herstructurering, en de meta-principes zijn vervallen ten gunste van de Public-principes (commit `392d045`) |
| README en epics-inleiding | "vier tot stories uitgewerkt", "dertig features", "zestien stories" | "zes tot stories uitgewerkt", "vijfendertig features", "tweeëntwintig stories, negen met interactiekoppeling"; plus een legenda voor bronafkortingen (ADR, U, OKx-AP) | standtelling volgt de nieuwe rijen; de E5-uitzonderingszin in epics.md verviel omdat de R4-delta hem overbodig maakt |

**Inhoudelijke aanscherping bij F7.2.** De oude doelzin claimde "conform het Edukoppeling REST-profiel". De gemergde [auth-standaard](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/auth-standaard.md) legt OAuth 2.0 Client Credentials vast maar noemt het Edukoppeling REST-profiel niet; de doelzin is teruggebracht tot wat de vastgestelde bron draagt.

## Nieuwe rijen, elk opnieuw tegen de bron geverifieerd

Patroon conform de [extractieverantwoording](20260806_0837_requirementsboom-extractie.md): elke bron is direct gelezen voordat de rij is opgenomen. FR staat voor functionele eis (functional requirement) in de interactiepatronen van Public.

| Rij | Bron (direct gelezen) | Wat de bron draagt |
|---|---|---|
| F6.6 | [Mapping veldnamen](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/mapping.md) | veldnamen in de schema's zijn Engels (UK) met per model de mapping naar de eerdere Nederlandse veldnaam |
| F8.1 | [Meetingverslag 17 april, POC-scholen](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#voortgang-en-selectie-van-de-poc-scholen) | bevestigde POC-deelname en het valideren van de informatiearchitectuur bij pilotinstellingen |
| F8.2 | zelfde verslag, [MORA en kennisoverdracht](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#uitdagingen-rondom-de-mora-en-kennisoverdracht) | kennisachterstand bij scholen op de referentiearchitectuur en het webinarvoorstel (meetingdiscussie) |
| F8.3 | zelfde verslag, [EduV en borging](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#status-van-eduv-en-potenti%C3%ABle-borging-integratiestandaarden) | "EduV zal een grotere rol gaan spelen in het borgen van afspraken, zodat leveranciers daadwerkelijk de functionaliteiten leveren die zijn overeengekomen"; het verslag schrijft de afkorting wisselend uit |
| F8.4 | zelfde verslag, [adoptiestrategie](../../meetings/20260417_okx_kernteam_inhoud_uitwerken_studentkeuze_roostering_planning_pocs/summary.md#stakeholdermanagement-en-adoptiestrategie) | de feedbackloop met leveranciers en scholen wordt geïntensiveerd om specificaties aan te scherpen |
| S2.6 | [Datamodelschema's, regels bij de schema's](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Datamodelschema%27s/README.md#regels-bij-de-schemas) | "Keuzedelen staan als root ... herbruikbaar over opleidingen heen (N:M via de regelset)"; parkeerlijst-thema keuzedeelhergebruik, geplaatst onder F2.3 |
| S4.1 | [Interactiepatroon OC-SIS, acceptatietoets](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#acceptatietoets-bij-wijziging-examenplan) | FR2 en het patroon acceptatietoets bij wijziging examenplan; interactie S5 |
| S5.3 en S5.4 | [Interactiepatroon OC-SIS, inrichten](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#notify-then-pull-nominaal-template-en-resultaatstructuur-inrichten) | FR1 en de interacties S1 tot en met S4, gesplitst naar het voorbeeld van S3.1/S3.2: ophalen en inrichten (S1 tot en met S3, eigenaar OC) los van de statusmelding (S4, eigenaar SIS) |
| S7.1 | [Interactiepatroon OC-P&R, abonnement registreren](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#abonnement-registreren) | FR7 en interactie I8; parkeerlijst-item "abonnement-endpoint voor registratie op events", nu met vastgestelde bron |
| S7.2 | [Interactiepatroon OC-P&R, reconciliatie](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#reconciliatie-na-gemist-event) | FR6 en interactie I7 |

**Notatie in de kolom Koppeling.** De interacties van de koppeling OC-SIS heten S1 tot en met S5, wat botst met de notatie van story-id's. Daarom staat in alle koppelingcellen voortaan het koppelingsacroniem voorop (`OC-P&R I4, eigenaar OC`); het voorbeeld in de skill is daarop aangepast, net als de tegenstrijdige mermaid-regel in de skill (`flowchart TD` in de conventies tegenover `flowchart LR` in de checklist; het is overal LR geworden, conform de bestaande plaat).

## Onafhankelijke review (product-flow stap 3)

Twee verse agent-contexten hebben gereviewd: een specialist tegen de skill-checklist en een tester tegen R1 tot en met R12, de artefacteisen en de Public-checkout. Verwerkt: de vergeten linkreparatie bij F4.3 (beide reviews, blokkerend); een story die het ouderfeature woordelijk herhaalde is geschrapt (de kandidaat "aanbod en verbintenis per niveau in stadia tegelijk" staat daarmee weer op de parkeerlijst); de keuzedeelhergebruik-story is verplaatst van E6 naar F2.3 omdat hij gedrag draagt en geen terminologie; de inrichtingsstory is gesplitst; F8.2 is beperkt tot kennisopbouw (uniforme definities horen bij E6); de bronankers van F8.2 en F8.3 wijzen nu naar de sectie die de rij werkelijk draagt; en de doelzin van F6.6 claimt niet langer een brug naar het begrippenkader die de bron niet legt. Niet overgenomen: het voorstel om de kolom "Raakt ook" te schrappen; de kolom staat op `dev` al in de E1-storytabel en de lopende skill-uitbreiding (PR #147) beschrijft hem.

## Bewust niet gedaan

- **Verwijzingen naar PR 120 blijven staan** met de noot "in review": die pull request is nog open. De leeswijzer benoemt de omzetting als vervolgpunt.
- **Bestaande stories die "geen" dragen houden "geen".** Per story gecontroleerd: S1.1 (publicatievalidatie, koppeling CO-OC niet uitgewerkt), S2.1 tot en met S2.5 (studentkeuzesysteem heeft nog geen interactiepatroon), S3.3 tot en met S3.6, S5.1 en S5.2 (uitvoerings- en keuze-interacties buiten de drie uitgewerkte koppelingen). Er bestaat voor geen van deze stories een interactie in de gemergde interactiepatronen.
- **De parkeerlijst in de extractieverantwoording is niet herschreven**: dat document is een momentopname. Deze verantwoording legt vast welke items zijn teruggehaald (S2.6, S7.1) en dat de overige kandidaten voorraad blijven.
- **E6 en E8 dragen geen stories**: de E8-bronnen zijn meetingniveau en de E6-features beschrijven taaleigenschappen zonder toetsbare actorwens met harde bron; verzonnen invulling hoort niet in de boom. De onderbouwing van E8 steunt bovendien volledig op één meetingverslag; verdieping is werk voor een volgende ronde.

## Bevinding voor Public

[Uitgangspunt U11](https://github.com/Npuls-OKx/Public/blob/dev/Koppelvlakspecificaties/uitgangspunten.md) verwijst relatief naar `Koppelingspecificaties/oc-p-en-r/koppelingspecificatie-oc-p-en-r.md`; dat pad bestaat op `dev` niet meer. Terug te melden aan Public als correctie.

## Niet geverifieerd

- De Jamie-meetings van na 5 augustus zijn niet opnieuw doorzocht op nieuwe kandidaten; deze ronde beperkte zich tot de bestaande parkeerlijst en de inmiddels gemergde Public-documenten.
- Of het Edukoppeling REST-profiel elders in vastgestelde documenten aan de authenticatiekeuze is verbonden, is niet uitgezocht; alleen vastgesteld dat de auth-standaard het niet noemt en dat de term in de hele Public-checkout niet voorkomt.
- `validate-docs.py` controleert geen absolute `https`-links; de Public-links in de boom zijn daarom handmatig en per review tegen de lokale Public-checkout gecontroleerd. Een scriptmatige controle is een vervolgpunt.
