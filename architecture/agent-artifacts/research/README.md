# Onderzoek

Onderzoeksverslagen die (mede) met agents zijn opgebouwd en die dienen als **onderbouwing voor een besluit**. Ze leggen vast wat er is uitgezocht, bij welke bron, en wat níet geverifieerd kon worden.

Een onderzoeksverslag is daarmee iets anders dan de andere agent-artifacten. Een [projectaanvraag](../project-requests/) beschrijft wat we willen maken, een [featureplan](../feature-plans/) hoe we dat opknippen en een [ontwerpdocument](../design-docs/) hoe één onderdeel werkt. Een onderzoeksverslag beantwoordt een **vraag** waarvan het antwoord de richting bepaalt, vóórdat er iets ontworpen wordt.

## Eisen aan een verslag

- **Elke bewering draagt een bronvermelding** met volledige URL, en waar mogelijk een paragraaf- of paginanummer.
- **Onderscheid "dit staat er" van "dit leid ik af".** Een afleiding is bruikbaar, maar moet als afleiding herkenbaar zijn.
- **Benoem wat je niet hebt kunnen verifiëren.** Een verslag zonder onzekerheden is verdacht; het onderzoek is dan niet ver genoeg gegaan of de gaten zijn dichtgeschreven.
- **Geen aanbeveling zonder afweging.** Als een verslag tot een advies komt, staan de alternatieven en hun kosten erbij.

Een verslag is invoer voor een **architectuurbesluit**. Het besluit zelf en de afweging horen in een ADR in [`Npuls-OKx/Public`](https://github.com/Npuls-OKx/Public/tree/dev/Referentiemateriaal/adr), dat naar het verslag hier terugverwijst.

## De verslagen

| Verslag | Vraag | Status |
| --- | --- | --- |
| [AMIGO-producten en gat-analyse](20260804_1500_amigo-producten-en-gat-analyse.md) | Wat schrijft AMIGO per stap voor als product, en wat hebben wij daarvan? | Afgerond |
| [Praktijk in standaardisatieprojecten](20260804_1500_praktijk-standaardisatieprojecten.md) | Hoe verbinden andere projecten hun businesslaag aan hun techniek in Git, en wat werkte daar níet? | Afgerond |
| [Gereedschap: requirements, architectuur en documentatie als code](20260804_1500_gereedschap-requirements-architectuur-docs-as-code.md) | Welke gereedschappen maken onze laag machine-interpreteerbaar zonder de markdown-bron op te geven? | Afgerond |
| [Requirementsextractie voor de requirementsboom](20260806_0837_requirementsboom-extractie.md) | Welke geverifieerde kandidaat-requirements dragen de boom onder `architecture/docs/requirements/`, en wat is bewust geparkeerd? | Afgerond |

De drie verslagen bij issue #130 horen bij elkaar: AMIGO zegt wat er gemaakt moet worden, de praktijk laat zien welke koppelmechanismen het volhouden, en het gereedschapsverslag toetst wat daarvan bij onze randvoorwaarden past.

## Ter besluitvorming

| Document | Waarvoor |
| --- | --- |
| [Oplossingsrichtingen business en techniek](20260804_1700_oplossingsrichtingen-business-techniek.md) | Samenvatting van de drie verslagen tot drie oplossingsrichtingen, met wat er afviel, een voorkeur, en een leeslijst om zelf te bekijken vóór het besluit |

Dit is geen vierde verslag maar de **synthese**: het vat samen wat de drie verslagen betekenen voor een keuze. Het besluit zelf hoort daarna in een ADR.

Bestandsnaam en documentconventies: zie de [agent-artifacten-README](../README.md).
