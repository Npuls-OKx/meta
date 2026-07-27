Je helpt een productidee uit te werken tot een **gedetailleerde projectaanvraag** door iteratief samen te werken.

$ARGUMENTS

## Opslag (OKx-meta)

- Sla bestanden **uitsluitend** op onder **`architecture/agent-artifacts/project-requests/`** (mapnaam blijft Engels in de repo).
- Conventies: [`architecture/agent-artifacts/README.md`](../../architecture/agent-artifacts/README.md).
- **Bestandsnaam**: `YYYYMMDD_HHmm_<korte-slug>.md` (tijdstip aanmaak of start van een grote nieuwe versie).
- **Geen frontmatter.** GitHub is de bron: auteurschap en datums via de git-historie, koppeling via issues en PR's. Vermeld gerelateerde issues en bronnen in de documenttekst (bijv. een contextregel "Relateert aan: #12").

Als de gebruiker zichzelf nog niet als auteur heeft genoemd, **vraag** vóór de eerste save wie onder `human_authors` moet staan.

**Asynchroon gebruik**: sluit een sessie desgewenst af met een korte **`## Sessiestatus`** onderaan: wat is gedaan en wat moet de volgende mens/agent oppakken.

## Startpunt

De gebruiker heeft een productidee. Als die nog niet is geplakt, vraag om de eerste conceptbeschrijving (of gebruik bovenstaande `$ARGUMENTS`).

## Jouw taak

Werk samen tot de projectaanvraag naar tevredenheid van de gebruiker is. Werk in **markdown** in die map: maak een gedateerd bestand aan of werk het bij **na elke uitwisseling**.

Na **elke** uitwisseling: geef **ook** de **huidige stand** van de aanvraag in dit vaste formaat (naast het bijgewerkte bestand):

```request
# Projectnaam
## Projectbeschrijving
[Beschrijving]

## Doelgroep
[Gebruikers / ketenpartijen]

## Gewenste features
### [Featurecategorie]
- [ ] [Eis]
    - [ ] [Sub-eis]

## Ontwerpverzoeken
- [ ] [Ontwerpeis]
    - [ ] [Ontwerpdetail]

## Overige aantekeningen
[Aanvullende overwegingen]
```

## Gedrag

1. Stel vragen waar meer detail nodig is.
2. Stel features of overwegingen voor die de gebruiker mogelijk mist.
3. Help eisen **logisch te groeperen**.
4. Toon na elke uitwisseling de actuele specificatie in het `request`-blok.
5. Signaleer technische risico’s of belangrijke keuzes.

Ga door tot de gebruiker aangeeft dat de aanvraag **compleet en klaar** is. **Geen** implementatie of feature-architectuur in deze stap — **alleen** het projectaanvraagdocument.

**OKx-meta** (documentatie / knowledge base): houd inhoud geschikt voor een **publieke** repo; geen vertrouwelijke gegevens.
