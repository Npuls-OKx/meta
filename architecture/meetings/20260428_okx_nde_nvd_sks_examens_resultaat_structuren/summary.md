Executive Summary

Sequentiediagrammen OCP worden deze week door Niek Derksen afgestemd op basis van de specificatierepo; verwerking van werk van Aldaen Niels van Duin in procesdiagrammen volgt.

Onderwijsarchitectuur massa-maatwerk vs volledige personalisatie: kernvraag is of studenten stapje-voor-stapje kiezen of complete route vooraf uitstippelen; procesketen loopt van intake/leerbehoefte via request-for-offering naar haalbaarheidscheck (capaciteit, docenten, lokalen) en roostering.

Leeruitkomsten en examenstructuur vereisen gestandaardiseerde wegingen (ECTS, SBU's) voor modulair systeem; SKS stuurt gekozen onderwijsspecificaties + exameninstrumenten naar SVS die resultaatstructuur opbouwt, LMS-integratie levert leerpad met resources terug op basis van specificatiestructuur.

Full Summary
Werkaantal en Tooling

Niek Derksen werkt aan sequentiediagrammen voor OCP op basis van specificatierepo en integreert werk van Alda en Niels van Duin in procesdiagrammen

Onderwijsontwerp en Studentenpaden

Massa-maatwerk betekent aanbodgedreven macro-ontwerp met voorgeprogrammeerde leerroutes waar studenten uit kiezen

Volledige personalisatie is bottom-up waarbij student eigen samenstelling bepaalt

Kernvraag: stapje voor stapje kiezen versus complete route vooraf uitstippelen

Grofmazige oriëntatie bepaalt richting, fijnmazige oriëntatie specificeert onderdelen en volgorde

Planning horizon definieert hoe ver vooruit wordt gepland

Procesmapping Student naar Aanbod

Intake en registratie: student geeft leerbehoefte aan, begeleiding en bekostiging worden bepaald

Concretisering: onderdelen, beschikbaarheid en planningshorizon worden bepaald via request for offering

Planning en haalbaarheid: controleren of aanbod realiseerbaar is met beschikbare docenten, lokalen en middelen

Roostering: onderscheid tussen periode-rooster (aanbodgedreven) en persoonlijk rooster (filter)

Niek Derksen geeft aan dat roosteren een NP-Hard probleem is en daarmee een soort zwarte box die problemen oplost, Niels van Duin is realistischer dat automatisering meestal één iteratie draait en dan handmatig wordt aangepast

Examenstructuur en Resultaten

Examen is abstracte container, toetsinstrument is concrete evaluatiemethode, resultaatstructuur is verzameling leeruitkomsten, gekoppeld via examen, gerealiseerd met exameninstrumenten

Modulair examenontwerp heeft drie niveaus: macro (programmaspecificatie), meso (opleidingsonderdeel linkt aan examens), micro (leeractiviteit met toets-/examen instrumenten)

Hoge automatisering nodig voor modulaire opbouw

Voor personalisering moet dynamisch exameninstrumenten kiezen, en daarmee je eigen resultaatstructuur samenstellen mogelijk zijn

Naming verwarring bestaat tussen opleidingsonderdeel, onderwijseenheid, leeronderdeel en leeractiviteit. Gerelateerd aan allignment initiatief MORA <> HORA onder mom van klus 57 MBODigitaal 

Leeruitkomsten en Onderwijs Specificaties

Architect van hogeschool waarschuwt dat leeruitkomsten en onderwijs specificaties niet direct verenigbaar zijn. Veel terugkomend argument.

Leeruitkomsten bepalen grootte/waarde, onderwijs specificaties bepalen hoe. Vraag blijft open vanuit OKx, waarom zijn deze lastig te verenigen?

Relatie via ECTS, SBU's, BOT, OOT en BPV's is complex

Wegingen moeten gestandaardiseerd zijn op basis van studiebelasting en grootte leeruitkomst

Zonder standardisatie ontstaan inconsistenties die veel scholen niet goed begrijpen

LMS Integratie

LMS is niet alleen leermiddelen maar leermanagementsysteem met hiërarchische structuur per aggregatieniveau

LMS ontvangt request for learning materials structure en geeft beschikbare leermiddelen per onderwijsspecificatie terug

LMS krijgt specificatiestructuur en levert leerpad met resources in gewenste volgorde

Publieke catalogus kan snippet van LMS-content tonen, volledige content achter paywall voor ingeschreven studenten

Niels van Duin wil niet in detail over LMS-beheer omdat ervaring beperkt is

Systeem Interacties

SKS (Studiekeuzesysteem) vraagt beschikbare toetsinstrumenten voor gekozen onderwijs en stuurt naar SVS

SVS (Studentenvolgsysteem) ontvangt onderwijsspecificaties, examens en exameninstrumenten en maakt resultaatstructuur met wegingen

Toets- en examenmateriaalbeheer moet beschikbare instrumenten teruggeven op basis van onderwijsspecificatie maar wordt als "black magic" beschouwd

Vraag blijft open of studenten exameninstrument moeten kunnen kiezen

Open Vragen

Hoe match aanbod met variabele vragen van studenten en is capaciteitscontrole iteratief of eenmalig?

Moeten leermiddelen zichtbaar zijn in publieke catalogus of pas na inschrijving?

Hoe diep moet roostering gedetailleerd worden versus als zwarte doos behandeld?

Hoe verkrijgen SKS en toets/examenbeheer access tot exameninstrumenten?

Hoe officieel leeruitkomsten en onderwijsspecificaties koppelen gegeven de complexiteit?