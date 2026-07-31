Maak één of meerdere concept-ADR's op basis van meeting-transcripties, samenvattingen en bestaande besluiten. $ARGUMENTS

**De besluiten leven niet in deze repository.** Architectuurbesluiten staan sinds juli 2026 in [`Referentiemateriaal/adr/` in Npuls-OKx/Public](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr). Een besluit onderbouwt wat er in het releasepakket staat, dus het hoort bij wat gepubliceerd wordt.

Werkwijze:

1. Lees hier in deze repository de bron: de meeting-notulen in `architecture/meetings/`, het [ArchiMate-model](../../architecture/model/) en de betrokken documentatie in `doc/`.
2. Werk het besluit uit in **Npuls-OKx/Public**, op een feature branch vanaf `dev` daar, met het [ADR-template](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/template.md) als basis.
3. Neem het eerstvolgende vrije nummer uit de [index](https://github.com/Npuls-OKx/Public/blob/dev/Referentiemateriaal/adr/README.md) en werk die index bij.

Eisen aan het besluit:

- Neem de overwogen alternatieven op, met hun afweging. Een besluit zonder alternatieven is een mededeling.
- Benoem expliciet de impact op `architecture/model/model.archimate` in deze repository.
- Link naar de meeting-notulen waar het besluit uit voortkomt, en naar de relevante OKx- en OKE-documentatie.
- Vergelijk met de bestaande besluiten op overlap, en benoem die overlap met bronverwijzing.

Let op: in Npuls-OKx/Public gelden de conventies voor gereleasde documenten. Geen issueverwijzingen in de tekst zelf; die horen in de commit message en de pull request. Draai daar `scripts/check-links.py` en `scripts/check-conventies.py` voordat je de pull request opent.
