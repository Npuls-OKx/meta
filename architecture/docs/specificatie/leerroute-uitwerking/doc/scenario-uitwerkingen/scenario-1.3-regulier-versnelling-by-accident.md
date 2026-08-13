# Scenario 1.3: regulier, versnelling by accident

**Doel.** Toetsen hoe de keten een niet-ontworpen versnelling verwerkt: eerder roosteren en toetsen zonder dat er een formele versnelde route bestaat.

**Scope.** Leerroute 1 met versnelling by accident; delta ten opzichte van [scenario 1.1](scenario-1.1-regulier-happyflow.md). Status: pitch, nog uit te werken. Het sjabloon, de casus en de samenhang staan in de [README](README.md).

**Persona.** [Jochem](../persona_jochem.md), in de levensloopvariant van dit scenario (zie het sjabloon in de [README](README.md)).

**Verantwoordt.** De bijbehorende story-id's volgen bij de scenario-story-verantwoording, na de hernummering van de requirementsboom.

> **Status.** *By accident, alleen versnelling.* **Pitch.** *Jochem blijkt tijdens periode 1 sneller te leren dan verwacht. Hij rondt twee leergelegenheden vroeg af, kan in periode 2 alvast werkprocessen uit periode 3 oppakken en is — zonder dat dit ooit als route ontworpen is — drie maanden vóór op het cohort.*
>
> **Verschil met 1.1.** De specificatie verandert niet. **Aanbod-stadium**: Planner moet eerder dan ontworpen leergelegenheden uit P3 ophogen voor P2 (capaciteit + roostering). **Verbintenis**: extra `Association` op niet-cohortgebonden offerings; toetsgelegenheden eerder geactiveerd. **Resultaat**: dezelfde LO-dekking, eerder behaald.
>
> **Architectuurlagen-impact.** Beleid t.a.v. afwijken van cohortritme (mag dit zonder formele "versnel-track"?), Proces t.a.v. tussentijds bijplannen, Systeem t.a.v. of OC en planningssysteem mid-period mutaties op `*Offering` toestaan.
>
> *— Volledige uitwerking in een vervolgsessie.*
