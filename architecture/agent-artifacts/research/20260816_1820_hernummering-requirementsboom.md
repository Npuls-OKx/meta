# Hernummering requirementsboom: oud naar nieuw

Verantwoording van de mechanische hernummering van de requirementsboom naar de vastgestelde id-conventie: plat per soort, voluit met vier cijfers, zonder oudernummer in het id. Relateert aan: #148 (uitvoering), #135/PR 136 (conventie), #152/PR 153 (uitwerkingsronde 2, de stand waarop deze hernummering is uitgevoerd).

## Wat er is gebeurd

1. **Doelen herordend** (besluit Niek, 16 augustus, comment op #148): doel-0001 gezamenlijke taal, doel-0002 gegevensuitwisseling ten behoeve van studentmobiliteit, doel-0003 keuze en personalisering.
2. **Epics hernummerd in doel-volgorde**, van boven naar onder: binnen doel-0002 de ketenvolgorde (specificeren, plannen, koppelingen, piloteren), binnen doel-0003 de studentreis (kiezen, verbintenis, resultaat).
3. **Features en stories hernummerd in de volgorde van hun epic**; stories binnen een epic gegroepeerd per feature (in featurevolgorde), binnen een feature in de bestaande volgorde. De tabellen en secties in `epics.md`, `features.md` en `stories.md` zijn in dezelfde volgorde gezet.
4. **Veegronde**: issueverwijzingen ("Relateert aan: #...") uit de zes boomdocumenten gestript conform de zelfstandige-documenten-afspraak in AGENTS.md; de skill `okx-requirements-boom` draagt de conventie nu zelf in plaats van de hernummering-aankondiging; de mermaid-plaat en de conventiesectie in de README zijn bijgewerkt.

Vaste vervolgregel uit de skill: een nieuwe rij krijgt het eerstvolgende vrije nummer van zijn soort; bestaande nummers schuiven nooit op, ook niet bij opknippen of parkeren (dan ontstaat een gat).

## Buiten scope

- **Uitgangspunten U1-U10** leven in Npuls-OKx/Public en volgen daar via een eigen issue (`uitgangspunt-0001` en verder).
- **Agent-artifacten en meetingverslagen** houden de oude id-vormen: het zijn momentopnamen. Deze tabel is de vertaalsleutel.
- **GitHub-issues** die oude id's noemen (#149, #150, #151) zijn niet herschreven; bij oppakken geldt deze tabel.
- **Valse vrienden** zijn bewust onaangeraakt: de faalmodi F1-F12 in het archief van de leerroute-uitwerking (§19), de OC-SIS-interactienummers S1-S5, OC-P&R I-nummers, OC-LMS L-nummers en mermaid-node-id's elders.

## Reviewronde 16 augustus (na de mechanische hernummering)

Nieks review op de PR leidde tot wijzigingen bovenop de mechanische stap; die staan hier apart, zodat de mechanische claim hierboven zuiver blijft:

- `features.md`: kolomkop "Doel" is "Omschrijving" geworden (het doel leeft op epicniveau; de featurekolom beschrijft het gedrag) en elke rij draagt een anker om het id heen, zodat stories er direct op linken.
- `stories.md`: de kolom "Koppeling" heet in alle secties "Functionele eisen" en verwijst naar de FR-nummers in de sectie Functionele eisen van het betreffende interactiepatroon in Public (koppelingsacroniem voorop; de negen interactieverwijzingen zijn omgezet naar hun dragende FR's); de featurecel is een ankerlink naar de feature; de kolom "Raakt ook" is geschrapt — een story traceert via zijn feature terug naar de epic, en de opknip van story-0002/feature-0027 blijft geborgd in het opknip-issue.
- epic-0005 heet "Standaard beproeven en adopteren" (was "Standaard piloteren en adopteren"; naam liep niet).
- feature-0034 is hernoemd en herformuleerd naar de bron (keuze-requirement R7): "Voorwaarden vooraf uitgedrukt in behaalde leeruitkomsten".
- De skill `okx-requirements-boom` is op al deze punten bijgewerkt (tabelformats, aansluiting op de techniek, checklist).

## Doelen

| Oud | Nieuw | Doel |
|---|---|---|
| D2 | doel-0001 | Gezamenlijke taal en standaarden voor gegevensuitwisseling |
| D3 | doel-0002 | Gegevensuitwisseling ten behoeve van studentmobiliteit |
| D1 | doel-0003 | Keuze, personalisering en ketenoverstijgende routes |

## Epics

| Oud | Nieuw | Epic | Doel |
|---|---|---|---|
| E6 | epic-0001 | Gezamenlijke taal en standaard | doel-0001 |
| E1 | epic-0002 | Onderwijsaanbod specificeren en ontsluiten | doel-0002 |
| E3 | epic-0003 | Aanbod plannen en roosteren | doel-0002 |
| E7 | epic-0004 | Betrouwbare en vervangbare koppelingen | doel-0002 |
| E8 | epic-0005 | Standaard beproeven en adopteren (bij de hernummering: Standaard piloteren en adopteren) | doel-0002 |
| E2 | epic-0006 | Student kiest onderwijsspecificaties | doel-0003 |
| E4 | epic-0007 | Keuze en verbintenis vastleggen | doel-0003 |
| E5 | epic-0008 | Voortgang en resultaat op leeruitkomsten | doel-0003 |

## Features

| Oud | Nieuw | Epic (nieuw) |
|---|---|---|
| F6.1 | feature-0001 | epic-0001 |
| F6.2 | feature-0002 | epic-0001 |
| F6.3 | feature-0003 | epic-0001 |
| F6.4 | feature-0004 | epic-0001 |
| F6.5 | feature-0005 | epic-0001 |
| F6.6 | feature-0006 | epic-0001 |
| F1.1 | feature-0007 | epic-0002 |
| F1.2 | feature-0008 | epic-0002 |
| F1.3 | feature-0009 | epic-0002 |
| F1.4 | feature-0010 | epic-0002 |
| F3.1 | feature-0011 | epic-0003 |
| F3.2 | feature-0012 | epic-0003 |
| F3.3 | feature-0013 | epic-0003 |
| F3.4 | feature-0014 | epic-0003 |
| F3.5 | feature-0015 | epic-0003 |
| F7.1 | feature-0016 | epic-0004 |
| F7.2 | feature-0017 | epic-0004 |
| F7.3 | feature-0018 | epic-0004 |
| F7.4 | feature-0019 | epic-0004 |
| F8.1 | feature-0020 | epic-0005 |
| F8.2 | feature-0021 | epic-0005 |
| F8.3 | feature-0022 | epic-0005 |
| F8.4 | feature-0023 | epic-0005 |
| F2.1 | feature-0024 | epic-0006 |
| F2.2 | feature-0025 | epic-0006 |
| F2.3 | feature-0026 | epic-0006 |
| F2.4 | feature-0027 | epic-0006 |
| F2.5 | feature-0028 | epic-0006 |
| F2.6 | feature-0029 | epic-0006 |
| F4.1 | feature-0030 | epic-0007 |
| F4.2 | feature-0031 | epic-0007 |
| F4.3 | feature-0032 | epic-0007 |
| F5.1 | feature-0033 | epic-0008 |
| F5.2 | feature-0034 | epic-0008 |
| F5.3 | feature-0035 | epic-0008 |
| F5.4 | feature-0036 | epic-0008 |

## Stories

| Oud | Nieuw | Feature (nieuw) |
|---|---|---|
| S1.1 | story-0001 | feature-0008 |
| S1.2 | story-0002 | feature-0009 |
| S1.3 | story-0003 | feature-0010 |
| S3.4 | story-0004 | feature-0011 |
| S3.5 | story-0005 | feature-0011 |
| S3.1 | story-0006 | feature-0013 |
| S3.2 | story-0007 | feature-0013 |
| S3.3 | story-0008 | feature-0013 |
| S3.6 | story-0009 | feature-0015 |
| S7.1 | story-0010 | feature-0016 |
| S7.2 | story-0011 | feature-0016 |
| S2.1 | story-0012 | feature-0024 |
| S2.2 | story-0013 | feature-0024 |
| S2.3 | story-0014 | feature-0024 |
| S2.4 | story-0015 | feature-0026 |
| S2.5 | story-0016 | feature-0026 |
| S2.6 | story-0017 | feature-0026 |
| S2.8 | story-0018 | feature-0026 |
| S2.7 | story-0019 | feature-0029 |
| S4.1 | story-0020 | feature-0032 |
| S5.1 | story-0021 | feature-0033 |
| S5.3 | story-0022 | feature-0033 |
| S5.4 | story-0023 | feature-0033 |
| S5.2 | story-0024 | feature-0036 |

## Bewijs

- Restcontrole oude vormen in de boomdocumenten en de skill: `grep -rnE '\b([EFS][0-9]+\.[0-9]+|E[1-8]\b|D[1-3])\b' architecture/docs/requirements .agents/skills/okx-requirements-boom` levert alleen nog de bewuste voorbeelden van oude vormen op (de vertaalregel in de README en de checklistregel in de skill).
- `python3 scripts/validate-docs.py` schoon op `architecture/docs/requirements/`, dit artifact en de skill.
- Tellingen ongewijzigd: 3 doelen, 8 epics, 36 features, 24 stories.
