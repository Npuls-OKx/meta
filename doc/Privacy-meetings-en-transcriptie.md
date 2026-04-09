# Privacy, meetings en transcriptie (OKx-meta)

Dit document beschrijft hoe we omgaan met **opname en AI-gestuurde transcriptie** in sessies die bedoeld zijn om deze **publieke knowledge base** uit te breiden. Het is bedoeld voor **deelnemers** (instellingen, leveranciers, ketenpartijen, teamleden). Het is **geen juridisch advies**; bij concrete privacy- of contractvragen: neem contact op met je eigen organisatie en/of de sessiefacilitator.

---

## 1. Doel van deze repository

Deze repository heeft als doel het **verbreden van een publiek gedachtegoed**: gedeelde kennis over koppelvlakken en onderwijslogistiek die voor de sector bruikbaar is. Daarbij hoort dat we kennis **vastleggen en doorontwikkelen** — onder meer via documentatie, issues en pull requests, en soms via **meetings** waarvan inhoud in de repo terug kan komen (notulen, transcripten, vervolgissues).

---

## 2. Meetings kunnen worden opgenomen en getranscribeerd (AI)

Voor OKx-gerelateerde meetings kan gebruik worden gemaakt van **opname en automatische transcriptie** (waaronder met **AI**), zodat:

- de inhoud **navolgbaar** en **herbruikbaar** is voor asynchrone samenwerking;
- notulen en vervolgacties beter te ondersteunen zijn.

**Facilitator**: de facilitator van de sessie **kondigt voorafgaand aan de opname** duidelijk aan dat er **opgenomen** gaat worden en (indien van toepassing) dat er **AI-transcriptie** wordt ingezet.

---

## 3. Wat leggen we vast in de notulen (en bijbehorende bestanden)?

In de repository kunnen na een sessie — naast eventuele ruwe opnamebestanden buiten de repo — met name de volgende **gegevens** in notulen en documentatie terechtkomen:

| Gegeven | Toelichting |
|---------|-------------|
| **Sprekersnaam** | Wie het woord voert, zoals herkend door de transcriptietool of handmatig toegevoegd (voor leesbaarheid en navolgbaarheid). |
| **Verbatim transcript** | Een zo **getrouw mogelijke weergave** van wat er gezegd is (woordelijk of quasi-woordelijk), afhankelijk van kwaliteit van opname en spraakherkenning. |
| **LLM-gebaseerde samenvatting** | Een door een **large language model (LLM)** gegenereerde **samenvatting** van het transcript, bedoeld om snel te kunnen lezen wat besproken is; dit is **geen** juridisch of formeel proces-verbaal en kan **onvolledigheden of interpretaties** bevatten. |

Er wordt **GEEN** video materiaal verzameld bij gebruik van Jamie.ai. 

**Let op**: de primaire bron voor “wat is er gezegd?” is het **transcript**; de **samenvatting** is een hulpmiddel. Bij twijfel: raadpleeg het transcript of vraag na bij deelnemers.

**Let op**: De verbatim transcriptie legt geen emotionele context of andere communicatie dimensies (bijv. lichaamstaal) vast. Bij twijfel over de bedoeling, intentie of emotionele impact van een verbatim boodschap; zoek altijd persoonlijk contact met de genoemde spreker, aannames in deze verbreken je verbinding met de persoon en kunnen leiden tot miscommunicatie.

---

## 4. Bezwaar, anonimisering en verlaten van de sessie

Ben je het **niet eens** met opname/transcriptie, dan kun je dat **melden** (bij voorkeur vóór of direct aan het begin van de opname).

**Beleid**:

- Je hebt het recht om in de transcriptie **geanonimiseerd** te worden (bijv. naam/sprekerlabel vervangen door een neutrale aanduiding), **of**
- Je kunt de **meeting verlaten** als je niet wilt dat jouw bijdrage op die wijze wordt verwerkt.

Concrete uitvoering (wie anonimiseert, binnen welke termijn) stem je af met de **facilitator** / **OKx-organisatie**.

---

## 5. Deelname aan sessies voor deze knowledge base

**Door deelname** aan een sessie die expliciet is bedoeld voor het **uitbreiden of onderhouden van deze publieke knowledge base**, ga je akkoord met de hier beschreven **werkwijze rond opname/transcriptie**, tenzij je tijdig bezwaar maakt zoals hierboven.

*(Als je namens een organisatie deelneemt: check intern of je bevoegd bent om gevoelige informatie te delen — zie ook paragraaf 7.)*

---

## 6. Toolkeuze, AVG en leveranciersdocumentatie

Tools voor transcriptie en notities worden **geselecteerd met aandacht voor privacy en AVG** (o.a. verwerking in de EU, encryptie, geen training op jouw inhoud waar dat door de leverancier zo wordt toegezegd).

Momenteel wordt er gebruik gemaakt van Jamie.ai.
Voorbeeld van leveranciersinformatie over gegevensverwerking (ter inzage voor deelnemers):

- [Jamie — Data handling (FAQ)](https://docs.meetjamie.ai/pages/faqs_troubleshooting/data)

Afhankelijk van de facilitator kan de AI transcriptie tool welke in een concrete sessie wordt gebruikt, afwijken. Vraag de organisatie/facilitator welke tool gebruikt wordt, vraag waar nodig om vastlegging van deze tool in de notulen. 

---

## 7. Strikte inhoudelijke waarschuwing: geen niet-publieke informatie

Omdat uitwerkingen in deze repo **publiek** kunnen worden en AI-hulpmiddelen bij transcriptie/notities kunnen zijn betrokken:

- **Deel geen** strikt vertrouwelijke, persoonsgevoelige of anderszins **niet-publieke** informatie die je niet in de openbare kennisbaan wilt zien.
- Werk **vanuit het principe**: alles wat je zegt, kan (al dan niet na bewerking) **terugkomen in tekst** die met anderen wordt gedeeld.

Maak een risico inschatting: 
- Wat is het risico dat deze informatie op straat komt te liggen? *Note:* In het geval van getranscribeerde meetings binnen de context van deze repo is deze kans dus 1.0 (100%).
- Wat zijn de consequenties voor mezelf, mijn omgeving en mijn organisatie; wanneer dit publiekelijk bekend word?
- $risico\_indicatie = omvang\_van\_risico\_consequentie * kans\_op\_publiek\_beschikbaar\_worden\_informatie$

Dit sluit aan bij het doel van OKx: **publiek** gedachtegoed en sectorbrede afspraken — niet een besloten achterkamer.

---

## 8. Gerelateerde documenten

- [`README.md`](../README.md) — korte verwijzing en context
- [`architecture/docs/principes/doc/principes.md`](../architecture/docs/principes/doc/principes.md) — o.a. machine-interpreteerbare formaten en AI-ondersteuning van de repo
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — vastleggen van meetings in `architecture/meetings/`
