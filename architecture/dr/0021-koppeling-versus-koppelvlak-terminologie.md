## Koppeling versus koppelvlak: terminologie en documentindeling

Status: Voorstel

Datum: 2026-07-23

### Context

Bij het uitwerken van de eerste koppelingspecificatie (OC naar P, #98) en de payload-specificaties (#119) bleek de term "koppelvlak" op twee manieren gebruikt te worden: voor de gestandaardiseerde informatiestroom tussen twee componenten, en voor de technische aansluiting van één component. De AMIGO-ladder (informatiestroom, koppeling, koppelvlak) in het agent-harnas maakte dit onderscheid al deels, maar de documenten en mapnamen niet.

### Beslissing

1. **Koppeling**: de gestandaardiseerde informatiestroom tussen twee referentiecomponenten (bv. OC naar P&R, OC naar SIS, OC naar LMS). Een **koppelingspecificatie** beschrijft die koppeling: procesbeeld, interactiepatronen, conceptueel informatiemodel, sequentiediagrammen, payload-specificaties en endpoints.
2. **Koppelvlak**: de verzameling van álle koppelingspecificaties, endpoints en operaties die één component raken. Het koppelvlak van de OC is dus de optelsom van de koppelingen OC-P&R, OC-SIS, OC-LMS, enzovoort.
3. **Documentindeling**: koppelingspecificaties staan per koppeling in een eigen map (`koppelingspecificaties/<koppeling>/`), met daarin de koppelingspecificatie en de payload-specificaties voor de data binnen het afgekaderde informatiemodel van die koppeling. Payload-specificaties worden per koppeling **gedupliceerd**, omdat structuur en attributen per koppeling kunnen divergeren; elke kopie vermeldt expliciet bij welke koppeling hij hoort.

### Alternatieven

- Optie A: "koppelvlak" blijven gebruiken voor beide betekenissen. Afgewezen: veroorzaakt spraakverwarring zodra meerdere koppelingen per component bestaan.
- Optie B: gedeelde payload-specificaties centraal beheren met verwijzingen. Afgewezen voor nu: attributen gaan per koppeling verschillen; expliciete duplicatie maakt eigenaarschap en divergentie zichtbaar.

### Consequenties

- Bestaande documenten hernoemen van "koppelvlakspecificatie" naar "koppelingspecificatie" waar ze één koppeling beschrijven.
- Het AMIGO-harnas (`.cursor/skills/amigo-aanpak/SKILL.md`) hanteert dezelfde definities.
- De interfacespecificatie (AMIGO-stap 6) per component aggregeert straks de koppelingspecificaties tot het koppelvlak van dat component.

### Relaties en links

- Issues: #98, #119, #105
- Docs: `architecture/agent-artifacts/design-docs/koppelingspecificaties/`
- Agent-harnas: `.cursor/skills/amigo-aanpak/SKILL.md` (ladder informatiestroom, koppeling, koppelvlak)
- ArchiMate model: `architecture/model/model.archimate` (koppelvlak-views per component, bv. `Koppelvlak: Onderwijscatalogus (obv 1.7)`)

### Vervangt (optioneel)

- Geen; verfijnt de ladder uit de AMIGO-aanpak.
