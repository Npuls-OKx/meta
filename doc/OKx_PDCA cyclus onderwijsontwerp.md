# Onderwijs PDCA-cyclus

Onderwijsontwikkeling kent een PDCA-cyclus: **Plan, Do, Check en Act**. Deze cyclus wordt gebruikt om onderwijs te ontwerpen, uit te voeren, te evalueren en continu te verbeteren. In de ontwerp- en ontwikkelfase worden onderwijsspecificaties opgesteld op basis van onder andere het kwalificatiedossier, de WEB/urennormen en de onderwijsvisie van de instelling. In de evaluatie- en borgingsfase wordt beoordeeld of het ontwerp goed werkt en of het voldoet aan de kwaliteitseisen die onder meer vanuit het Onderzoekskader van de Onderwijsinspectie worden gesteld.

Wijzigingen in onderwijsspecificaties kunnen verschillende oorzaken hebben. Grote wijzigingen ontstaan meestal door herziening van externe of interne kaders, zoals een nieuw of aangepast kwalificatiedossier, gewijzigde urennormen of een aangepaste onderwijsvisie. In de praktijk lijken kwalificatiedossiers jaarlijks vooral kleine wijzigingen te kennen, terwijl grotere herzieningen minder vaak voorkomen(3-8 jaar) en afhankelijk zijn van de snelheid waarmee een vakgebied verandert

Bij dergelijke fundamentele wijzigingen ontstaat er altijd een nieuwe specificatie. De nieuwe/herziene specificatie geldt dan enkel voor de nieuwe instroom. De oude specificatie, met lopend aanbod en student verbintenissen dienen te worden uitgefaseerd. Dit kan bij niveau 3-4 opleidingen meerdere jaren duren.

Wanneer het oude aanbod niet meer uitvoerbaar is, kan migratie van achterblijvende studenten nodig zijn. Dat scenario is vaak sterk afhankelijk van het applicatielandschap en valt daarom niet vanzelfsprekend binnen de standaard scope van OKx. Anderzijds maakt modern modulair en flexibiel onderwijs met microcredentials en aangetoonde leeruitkomsten het beduidend makkelijker om studenten over te plaatsen naar een nieuwe opleiding. Individueel gezien is dit een scenario waar Jochem (LR1) over gaat naar Michelle (LR9).

Kleinere wijzigingen komen vaker voor. Vooral nieuwe of nog beperkt uitgevoerde onderwijsontwerpen zullen iteratief worden getoetst op kwaliteit, haalbaarheid en betaalbaarheid. Dit kan leiden tot aanpassingen zonder dat direct een volledig nieuwe opleidingsspecificatie nodig is.

Een belangrijk uitgangspunt is dat er niet zomaar wijzigingen kunnen worden doorgevoerd in een opleiding wanneer het SIS al lopende verbintenissen kent. Tegelijkertijd is een opleiding het hoogste niveau in de specificatiestructuur. Een wijziging aan een opleidingsonderdeel, leerspecificatie of lesspecificatie hoeft daarom niet automatisch een breaking change voor de volledige opleiding te zijn. Idealiter hebben deze onderdelen een eigen lifecycle, zodat een opleiding kan bestaan uit actieve, herbruikbare onderdelen die ook in andere opleidingen of zelfs los aangeboden kunnen worden.

Daarom is het essentieel om **identificerende codering** en **versionering** strikt van elkaar te scheiden. Een minor update aan een onderwijseenheid hoeft niet te betekenen dat ook de volledige opleidingsspecificatie wijzigt. De vraag is steeds of er sprake is van een nieuwe specificatie, een nieuwe versie van een onderdeel, of alleen een niet-brekende aanpassing binnen dezelfde lifecycle.

De curriculum ontwerptool of onderwijscatalogus speelt hierin een cruciale rol. Deze moet helpen bepalen of een wijziging leidt tot een breaking change, of de ontwerper bewust gemaakt moet worden van de impact, en of er sprake is van een versie-update of van een nieuw onderdeel.

Voor het examenplan (of OER) geldt het zwaarste uitgangspunt. Dit mag niet zomaar wijzigen, omdat het in principe een contractuele afspraak is met de student. Het examenplan beschrijft de summatieve resultaatstructuur, zoals scope, relatie met kerntaken, wegingen en formules.

De leren zonder drempels visie vraagt daarbij wel om meer dynamische en modulaire resultaatstructuren, bijvoorbeeld wanneer keuzes kunnen worden ingevuld met onderdelen die nog niet bestaan op het moment dat de OER wordt vastgesteld. Het is een reële verwachting dat wetgeving (zie ook VABA) en de werking van SIS’en hierop verder anticiperen.

Voor acceptatie van wijzigingen zijn daarom duidelijke uitgangspunten nodig:

- Een wijziging mag lopende verbintenissen niet ongecontroleerd raken.

- Een examenplan/OER en onderliggende summatieve structuur mag niet zonder zorgvuldige afweging worden aangepast.

- Specificaties waarop al aanbod heeft plaatsgevonden, worden niet handmatig verwijderd maar gedeactiveerd.

- Meerdere versies van dezelfde specificatie kunnen gelijktijdig actief zijn.

- Elke versie heeft een eigen lifecycle.

- De onderwijscatalogus is verantwoordelijk voor versionering en releasemanagement van specificaties.

Naast de inhoudelijke systematiek is organisatorische afstemming noodzakelijk. Ontwikkelen, plannen en roosteren kennen vooral een ketenafhankelijk proces waarin tijd en capaciteit beschikbaar moeten zijn om vervolgstappen tijdig af te ronden. Het fijnmazige aanbod kent geen wettelijke vaststelling. De wendbaarheid van de organisatie en het applicatielandschap is daarin leidend. Het is vooral beleid dat duidelijk dient te maken tot welk moment wijzigingen nog worden geaccepteerd, wanneer uitzonderingen mogelijk zijn en welke afstemming nodig is met planning, roostering en uitvoering.

Een aantal concrete voorbeelden:

- Kan een ontwikkelaar al starten met de uitwerking van een leerspecificatie wanneer het curriculum ontwerp nog in concept staat en wijzigingen reëel zijn?

- Tot wanneer worden er nog wijziging geaccepteerd aan een leerspecificaties en aanbodplanning ten opzichte van de (wenselijke) publicatie van roosters?

- Hoeveel tijd heeft een docent nodig om een nieuwe leerspecificatie eigen te maken?

Een uitwerking van beleid dient allerminst een classificatie van beoogde wijzigingen te bevatten en vereisten van acceptatie: 

| Type wijziging | Casus | Acceptatie |
| --- | --- | --- |
| Fundamentele wijziging | Nieuw kwalificatiedossier, gewijzigde wettelijke eisen, nieuwe onderwijsvisie | Nieuwe specificatie; meestal alleen voor nieuwe instroom |
| Wijziging met | Aanpassing in examenplan, summatieve resultaatstructuur of administratieve eigenschappen | Alleen accepteren na expliciete impactanalyse en besluitvorming |
| Niet-brekende wijziging | Actualisatie van lessen, materiaal, didactische uitwerking of uitvoeringsvorm | Kan als versie-update binnen bestaande lifecycle |
| Wijziging | Update van leerspecificatie of onderwijseenheid | Alleen het onderdeel krijgt een nieuwe versie, tenzij afhankelijkheden breken |
| Wijziging na planning/roostering | Aanpassing nadat aanbod of rooster al is gepubliceerd | Alleen bij uitzondering en na ketenafstemming |
