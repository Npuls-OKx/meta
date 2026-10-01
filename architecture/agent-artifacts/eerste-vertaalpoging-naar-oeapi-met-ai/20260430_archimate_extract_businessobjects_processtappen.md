---
created: "2026-04-30T16:07:00+02:00"
updated: "2026-04-30T17:29:00+02:00"
type: "agent-artifact"
artifact_kind: "archimate-extract"
source_model: "meta/architecture/model/model.archimate"
source_views:
  - "01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model"
  - "Informatiemodel Onderwijsontwerp"
scope_note: "Alleen BusinessObjects en BusinessProcess uit de genoemde views. Geen OEAPI-termen."
---

## Doel

Dit artefact is een **extract** van de relevante **BusinessObjects** en **processtappen** (BusinessProcess)
uit twee ArchiMate-views. Het is bedoeld als semantische bron voor het herschrijven/herstructureren van
`20260414_1500_okx-oeapi-consumer-profiel.md` naar MORA/sector-taal.

## Dekking (automatisch uit model)

- View `01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model`: **129** BusinessObjects, **160** BusinessProcesses.
- View `Informatiemodel Onderwijsontwerp`: **122** BusinessObjects (in deze view: **0** BusinessProcesses).

## View: 01. Onderwijsvisie vertalen naar onderwijsaanbod - Basis Model

### Processtappen (BusinessProcess) — shortlist met duiding

| ArchiMate id | Processtap (exacte naam in model) | Rol in keten (1 zin) |
|---|---|---|
| `70c5259e-0884-4656-a5fb-ea9666f1b32a` | `Vertalen onderwijsvisie naar onderwijsaanbod` | Schakelt van visie/beleid naar een eerste “grofmazig” onderwijsontwerp dat als aanbod-kader kan dienen. |
| `6bbf7d3b-e653-4b9e-bf3a-54e65e031129` | `Bepalen start/stop opleiding` | Besluitvormingsstap voor (wel/niet) aanbieden of beëindigen van een opleiding. |
| `5d58911d-0972-4c51-81be-f5c7be1f8856` | `Vaststellen opleidingen aanbod` | Formele vaststelling van het opleidingenaanbod (besluit is “normerend” voor planning/uitvoering). |
| `a4d4fa67-910b-48e8-912e-95c8c1501ecf` | `Opstellen businesscase opleiding` | Onderbouwt keuzes rond (nieuw/gewijzigd) aanbod met argumenten en randvoorwaarden. |
| `c5078af8-f5cc-40c8-8331-0825ed099eb3` | `Analyseren kwalificatiedossier en keuzedelen` | Verbindt het kwalificatiekader met ontwerpkeuzes (welke eisen/keuzedelen sturen het ontwerp). |
| `id-027fc73468e943679a34d0e7d32d8060` | `Oriënteren op bestaande lesmethodes` | Verkennende stap richting hergebruik/inkoop/ontwikkeling van lesmethoden. |
| `id-6b7b49e1ac5e424c8a856af32594c2f4` | `Checken functionele fit informatieinrichting Lesmethode t.o.v. informatieinrichting instelling` | Toetst of een lesmethode past in de informatie-inrichting/structuur van de instelling. |
| `id-f99280ec44f0418e948cf3a4816a5f52` | `Migreren lesmethode naar instelling onderwijsspecificaties` | Vertaalt/migreert lesmethode-informatie naar de onderwijsspecificaties van de instelling. |
| `id-b7a31e1956ab41e7a3f19bbd33d2cc42` | `Nominale Leerroutes bepalen` | Legt de nominale leerroute(s) vast als onderdeel van het ontwerp van onderwijsaanbod. |
| `id-829f166b7f134c4796e2872342a396a9` | `Definiëren Leerdoel` | Vastleggen van lesdoelen (formatieve laag) als basis voor lesspecificaties. |
| `id-8cb38da99ffd43f6bfef332a0a0e71d9` | `Definiëren Leertaak` | Beschrijft de leertaak/leeractiviteit als bouwblok in het onderwijsontwerp. |
| `id-a22e086971bf4a8885d09a0e8886dfee` | `Definiëren Leeruitkomst` | Vastleggen van (summatieve) leeruitkomsten als dekkings- en toetsingsbasis. |
| `07d1cd53-033c-4475-9990-888b2eec7756` | `Speceficiering gewenste onderwijskundige leeromgeving` | Specificeert randvoorwaarden van leeromgeving (didactiek/leervorm/omgeving) die later plan- en roosterimpact hebben. |
| `id-9416cab697344512849d7e134041ba1b` | `Specificeren onderwijsvorm` | Concretiseert de onderwijsvorm (leervorm) als ontwerpkeuze met resource-implicaties. |
| `id-e6604ab9294f42c38044a5b2a557cec7` | `Specificeren Toetsvorm` | Concretiseert toetsvorm(en) als onderdeel van ontwerp en toetsplan. |
| `0af6198d-0034-4331-a81a-1dee741b926f` | `Extern verantwoorden` | Processtap in het view aanwezig; mogelijk randvoorwaardelijk (verantwoording) maar geen kernstap voor OKx “Student kiest”. |
| `619bcc8e-e8ae-486f-98a2-005e64e3f2a7` | `Opstellen financiële verantwoording` | Processtap in het view aanwezig; idem als hierboven. |
| `b76ae73d-e10b-44c2-8fa5-f16c2e1e104a` | `Uitwisselen met ROD` | Processtap in het view aanwezig; idem als hierboven. |

### Processtappen (BusinessProcess) — complete lijst (id + naam)

| ArchiMate id | Processtap (exacte naam in model) |
|---|---|
| `013069f8-c22c-4714-9903-700acc9e367d` | `Aanmelden geroosterde activiteit` |
| `07d1cd53-033c-4475-9990-888b2eec7756` | `Speceficiering gewenste onderwijskundige leeromgeving` |
| `0af6198d-0034-4331-a81a-1dee741b926f` | `Extern verantwoorden` |
| `3561f761-fe21-4e35-a433-bce7368f4955` | `Uitvoeren administratieve intake` |
| `3ee4b2f6-b93a-4b74-973a-9ccacac5be40` | `Uitvoeren onderwijs activiteiten` |
| `41b88735-45f7-4f61-a6a8-d0dd639339e7` | `Bepalen leerroute` |
| `42cbd105-e296-4057-8cc2-41ca52f0e470` | `Opstellen visie onderwijs en examinering` |
| `43aa5ed3-f3e9-4cf7-b2b8-f9e67789521e` | `Uitvoeren onderwijs intake` |
| `4a3a6a76-94b1-4b7f-a3e6-a8f104eb70da` | `Besluiten inkopen of construeren` |
| `4c995a67-bae4-4ef6-afed-757e4f928980` | `Publiceren rooster` |
| `4d357449-fb8e-4a84-94c6-a442d8f7e196` | `Construeren examens` |
| `53be1121-ba0d-4ea7-92de-9307b48ab61f` | `Visie bepalen, strategisch plannen en prognosticeren` |
| `5d58911d-0972-4c51-81be-f5c7be1f8856` | `Vaststellen opleidingen aanbod` |
| `5dcd852a-36ff-46b7-950a-460bc3d6a309` | `Inkopen examens` |
| `5eff54c1-60f9-4bbc-95e4-b4f7de23d011` | `Opstellen examen plan` |
| `619bcc8e-e8ae-486f-98a2-005e64e3f2a7` | `Opstellen financiële verantwoording` |
| `6502e011-7d96-4289-9905-2c230ed06de5` | `Persoonlijke leerroute specificeren` |
| `6bbf7d3b-e653-4b9e-bf3a-54e65e031129` | `Bepalen start/stop opleiding` |
| `6f5f1cdb-2734-4f62-a98d-a80063d58d77` | `Plaatsen student` |
| `70c5259e-0884-4656-a5fb-ea9666f1b32a` | `Vertalen onderwijsvisie naar onderwijsaanbod` |
| `7d3d5c9d-7193-4f31-ab65-89ab95a7a935` | `Opstellen bewijs van inschrijving` |
| `a4d4fa67-910b-48e8-912e-95c8c1501ecf` | `Opstellen businesscase opleiding` |
| `b41f5f3a-6bbf-45cd-b7b6-a1193a87abf3` | `Maken rooster` |
| `b76ae73d-e10b-44c2-8fa5-f16c2e1e104a` | `Uitwisselen met ROD` |
| `b942e7e2-4cb4-419e-af8f-8b205d0fdf57` | `Bepalen benodigd examen materiaal` |
| `bc2e5787-52a8-4b82-8ab8-aa26369aba6f` | `Ontvangen digitaal doorstroom dossier` |
| `be1b163a-d974-44a5-a51c-4d48707432ed` | `Registreren vrijstellingen` |
| `c5078af8-f5cc-40c8-8331-0825ed099eb3` | `Analyseren kwalificatiedossier en keuzedelen` |
| `cc66c1b6-7b5d-467b-bae8-6c539894d8ff` | `Intake en plaatsen` |
| `d094f664-46dd-45c1-ac9c-bce5c8604c00` | `Vaststellen examens` |
| `db427e67-33ae-4721-a169-1698ab46c931` | `Vaststellen en uitwerken examinering` |
| `dd69eb81-a99c-4f55-9e8b-f7a5903929cb` | `Formuleren leervraag` |
| `fc0b9ff9-58ba-4afa-bd4f-9f820f0a721a` | `Uitwisselen gegevens met derden` |
| `id-027fc73468e943679a34d0e7d32d8060` | `Oriënteren op bestaande lesmethodes` |
| `id-056128147cda438db2758059f2c47a18` | `Vormgeven onderwijsmodel` |
| `id-071ec5a32a7c4de3b218fdd130591dab` | `content-type filter (leervorm)` |
| `id-08ec294438f2498cab6d5e8f39e53797` | `Definiëren examenregelement` |
| `id-09d52c707fb04d88a3ad00ce9ead4ff8` | `Geografische trechter` |
| `id-09eb8960417d402c928ac28fe89a8ca7` | `toetsvorm filter` |
| `id-0a567058edb94b32a31d214ad8525dfd` | `Specificeren Leeruitkomst tot Lesuitkomsten` |
| `id-0c2ffda90aa041d98c37f25c9961ede6` | `Verzoek tot aanbod van leergelegenheden in dienen` |
| `id-0f04ebebff894f94b7fbb590435167a0` | `Definiëren Lesleerdoel` |
| `id-12509fb688e449e0bbb07986d750e8a8` | `Definiëren Exameninstrument kader` |
| `id-16b5dc4555ce40bda7f91d967c6bc1cd` | `Ophalen nominale leerroute voor student populatie` |
| `id-173923517297401b815f92c84ae65057` | `Definiëren Leeropdracht` |
| `id-173c3417c55d48ce9b7b27f7976a3437` | `gewenste te behalen leeruitkomsten articuleren` |
| `id-1f09e2f716e84d9fb247152b76a5f548` | `Streef collectie leeruitkomsten voorstellen?` |
| `id-1f5fa95a25ce433bbafdbb7c7a888ee6` | `Clusteren lesgroepen` |
| `id-20b23cc0cec740419bb4c8ae89f4fc2a` | `Beleidkeuze omtrend onderwijs aanbod model vast stellen` |
| `id-212ac090b6d849e9999ac3a13afeb328` | `ondersteuningstype filter` |
| `id-22bf0d4632814258a52ba3ebe3e524e9` | `Bekostigingstrechter` |
| `id-2649070cb5db40459c575077fad63423` | `instellingsprestatie filter` |
| `id-2654f9f33a96438cb70a0530bbc3532e` | `Afstemming met facility over vlekkenplan` |
| `id-26e1225014a9423492538baf10f337fd` | `Waardepapier definiëren in termen van SBB gestandaardiseerde lesuitkomsten` |
| `id-2769650df2ca40dca1b2e2e147af82af` | `Leergelegenheid specificaties omzetten to leergelegenheid aanbod` |
| `id-29280af1ef9e4c6b9e68cbe8dd285958` | `Bepalen benodigde toetshulpmiddelen` |
| `id-2a33b3cf19b74339a6da105a5acf19c0` | `Toegang verstrekken tot onderwijsondersteunende applicaties en middelen` |
| `id-2f6ceac8c3004129b93b716a4b7b230f` | `Afstemmen Leervraag en Planningshorizon met onderwijsaanbod instelling` |
| `id-30f3491ceb2b4ffcabaf64b09e1286cb` | `Definiëren Docentendraaiboek` |
| `id-32c096e69b694b17b298f4478f0c4eb1` | `Personaliseren door leeractiviteit / leergelegenheid te kiezen` |
| `id-35be14b0d1b740b6849c22f6196c75d0` | `Fijnmazig onderwijs ontwikkelen` |
| `id-35e2423bf3904addbbb9432cf56a6866` | `Definiëren Strategische Onderwijsomgeving` |
| `id-3756cef8230a421c8cb57f0fc992b93d` | `Oriënteren op leergelegenheden en resulterende leeruitkomsten` |
| `id-38902ebbf7ee4edbb1c952b960e50be9` | `Evalueren Challengen/sparren over initiële leervraag ten tijden van intake` |
| `id-3975bb8733c844519b1525c1cf6943f6` | `Referentie programma's laten zien op basis van arbeidsmarkt vraag` |
| `id-3cd226d6229443a293482de5abe96b3a` | `Definiëren Onderwijsvorm kaders` |
| `id-3e67f7583bdd490da0b10aa0e33be713` | `Specificeren medewerker types` |
| `id-3ea2d117b8f64bafb2172f81edef1e4e` | `Studenten populatie ophalen op basis van prognoses en doorstroom` |
| `id-41b3a848a3a1414e85c1c5c9aeebcb72` | `Gepland aanbod van leergelegenheid ontvangen, analyseren en accepteren` |
| `id-44fa327b90274bd8b0246b2f655c39fe` | `Kiezen van collectie van leeropdrachten` |
| `id-48006fd4205549a6b7e62c872f32873b` | `Plannen` |
| `id-4827a6e29d3c416faeccef866c7188b6` | `Analyseren leercontext potentiële student` |
| `id-48a2e0e8ab0a47d2b85076c1144a1dd1` | `Toetsinstrumentkader` |
| `id-4a1da9a6b7da4643b94f0cc8dabc49c5` | `Medewerker bestand ophalen` |
| `id-4ba69af723274ebb80895cac52a55b07` | `Plannen macro zijde` |
| `id-4e42e6b818524a039bc8bdde5e0655f7` | `Keuze maken uit nominale route of maatwerktraject` |
| `id-4eb026da76ac4665b5fe08ad52d73c8a` | `Vormgeven Toets- en examenkaders` |
| `id-4fc0cbe435aa41f4aa9eafe66b0d117b` | `Kiezen van collectie van lesuitkomsten` |
| `id-5547ed85b0b7410cbd39deda8ed1357e` | `Controleren behaalde credentials` |
| `id-5880c34fec9548449c9812b129178b6d` | `Clusteren van lessen tot leeractiviteit` |
| `id-5b285e60ec654fb3bb34f8399790cbf4` | `Team competenties en capactieit ophalen` |
| `id-5c66a41a4d0c4633aa362f7447181129` | `OER vormgeven` |
| `id-5fa367e4c1e84d45a9763351863412c0` | `Verrijken van aanbod gestuurd periode rooster` |
| `id-604ac1e03ff64301b1b16452f38743c3` | `Fijnmazig orienteren Student op onderwijsaanbod instelling` |
| `id-605e6832e69f4cc78454f52b18ec3c13` | `Opstellen handboek examinering` |
| `id-6060247d988a4914bab60990df05dbb3` | `Volledig vrije keuze` |
| `id-60e3845e96e94210aa0b7633ecc06a05` | `Meerjarenplanning opstellen` |
| `id-630431ceec3f4e52bc08a1bad2825126` | `Rooster principes opstellen` |
| `id-651d354c6f5c48998c262ff187364460` | `Vlekkenplan per onderwijs team ophalen` |
| `id-6561027a652440d5a0407101b024d5ba` | `Factureren` |
| `id-673e3f24d6e1450e9e18a401649e42f7` | `Clusteren leeractiviteiten` |
| `id-68a03e847a214d43bf638f2a29de729d` | `Haalbaarheid collectie potentiële leergelegenheden inschatten` |
| `id-6b650bdc9faa4b1b84efeb98244ee6b1` | `Definiëren Leeractiviteit` |
| `id-6b7b49e1ac5e424c8a856af32594c2f4` | `Checken functionele fit informatieinrichting Lesmethode t.o.v. informatieinrichting instelling` |
| `id-6cc3d035d2d64f849ff857c57c9ba512` | `Modulair examenplan opstellen` |
| `id-6dc3e31a50c745bfa485f9482a5222f8` | `Keuzedeel selecteren` |
| `id-6fa1eb4d36834abdb617ed369c48e10c` | `Overwegen om opleidingsaanbod te wijzigen` |
| `id-704fa29aa6174a29ac4be4cc3c360248` | `Definiëren Toetsvorm kader` |
| `id-70a2a107f81748c9a1203440c222c852` | `Specificeren leermiddelengroepen` |
| `id-731348dc142648d0abab95f3830a63e9` | `Keuze criteria vanuit student context vastleggen` |
| `id-73df2d08cf7943d39f13849335baf316` | `Clusteren lesgroepen` |
| `id-7a55afbe62ad4643881d5b1f7f259a72` | `Bepalen gewenst toetsinstrument` |
| `id-7a69f47f3737483791a97abe663f3e4f` | `Bepalen van benodigde Leermiddelen` |
| `id-7acfd4980f3d40dfbb81b75431907739` | `Leergelegenheid aanbod omzetten tot inschrijving` |
| `id-7f6c1d84f4314562ba7c5af8a77dcc9d` | `Koppelen opleidingsonderdeel specificatie aan examen(s)` |
| `id-80912345f0614c699358db52e481493c` | `Haalbaarheids besluit terugkoppelen` |
| `id-8248f08993c34872934bf704947e8306` | `Functioneel inrichten toetsinstrumenten` |
| `id-829f166b7f134c4796e2872342a396a9` | `Definiëren Leerdoel` |
| `id-85ec89fad52a4a228ab492354653501a` | `Specificeren gewenste medewerker compententie profielen` |
| `id-85ef09bb1a39411c9dd5a8eb6f9c1b42` | `Jaarplanning opstellen` |
| `id-891e1c6d7de8466391a4ed5ff5266b1c` | `Verzamelen van door student behaalde leeruitkomsten` |
| `id-89eb645a97c44196bf1d64071c4e764b` | `Besluiten inkopen/ontwikkelen lesmethode` |
| `id-8a502fd2ee7245c1920ee6604ef417a8` | `Definiëren Leervorm` |
| `id-8a796d17d4ce470990344bad1f691df5` | `Matchen van student keuze criteria met bekend sector aanbod` |
| `id-8cb38da99ffd43f6bfef332a0a0e71d9` | `Definiëren Leertaak` |
| `id-8dc8dad107f74712a814546db7a89955` | `Specificeren Leertaken tot leeropdrachten` |
| `id-8f9617e57d744706872ac2b96bb4b9ae` | `Capaciteitsplanning maken` |
| `id-8febbf93bb3648899892bd2dfb6de822` | `Periode Rooster opstellen` |
| `id-9163591793b34508bf5bf2615236ded7` | `Team Inzetplanningen maken` |
| `id-931f7f6be3fc4ba4bb41cb0481d558da` | `Roosteren en toetsen haalbaarheid gepersonaliseerde vraag naar onderwijsaanbod` |
| `id-9416cab697344512849d7e134041ba1b` | `Specificeren onderwijsvorm` |
| `id-948cc55851104fe88e828f2b0e9f7cc7` | `Micro niveau onderwijsontwikkelen` |
| `id-98ed0a4179824426b8b59ba2a21e1504` | `Verschillen analyseren tussen examenplan en bestaand examen aanbod` |
| `id-a132dfbf768746128c6805e32efb68fe` | `Intentie tot commitment aan subset aan leeruitkomsten administreren` |
| `id-a22e086971bf4a8885d09a0e8886dfee` | `Definiëren Leeruitkomst` |
| `id-a684964b02a644ad86525f69f6101e93` | `Definiëren Toetsmatrijs` |
| `id-a8d136e061e2441d89387bd391cd0f1f` | `Clusteren lesuitkomsten i.c.m leeropdrachten en leervormen` |
| `id-a9b8d6fa028e42bb913c9433dd8c178a` | `Vaststellen voorwaardelijkheden voor het volgen van gekozen onderwijsaanbod` |
| `id-ab1d87eb6290412686d1ca33d0664207` | `Modulaire onderwijsovereenkomst opstellen en ondertekenen` |
| `id-ac9f5d4267a54b25a70ddb17707ace7b` | `Faciliteiten bestand ophalen` |
| `id-ad3dfc22e74344f6a9c09a41415bb1a7` | `Toetsinstrument inkopen` |
| `id-ae94a82f6f5d457e9b6f5a163018a057` | `Definiëren benodigde expertise profielen i.h.k.v. leervorm kaders` |
| `id-b7a31e1956ab41e7a3f19bbd33d2cc42` | `Nominale Leerroutes bepalen` |
| `id-b7deecbc894445d8aef3f0919b42c576` | `Toetsinstrument construeren` |
| `id-c07ec0bffb4b4f46bdbd524cc75d94bd` | `Keuzedelen` |
| `id-c0c99a397aec4eaa8f54a3ab0d3a29fd` | `Specificeren leervormen binnen leeractiviteit` |
| `id-c22eed0fa5e344638e282b2dfb9b4689` | `Toetsinstrument hergebruiken` |
| `id-c5b1dfd01be7478e9ac83492f6cf8d0b` | `Meso niveau onderwijs ontwikkelen` |
| `id-c719daedb36b43e9805d302f87ccb0c0` | `instroomeisen en kwalificatie eisen trechter i.c.m. plannings- en beschikbaarheids horizon` |
| `id-c77a53d8b3a84c9f8763e8a35c1430b6` | `Planningshorizon en beschikbaarheidstrechter` |
| `id-c9bc8738a1af4c93b5281b4d2dc81cf2` | `Duur van begeleiding binnen leervormen specificeren` |
| `id-c9ed0dba538c433980c91c757ad5ae8d` | `Definitief Inzet Teamplan opstellen voor komende periode` |
| `id-cb6d14e2e7374b809dffafd3aa9996f0` | `Besluiten tot toetsinstrument hergebruiken, construeren of inkopen` |
| `id-cf20b3900f1f4ef7a3ebac044a61c361` | `Bekostigingscontext afstemmen` |
| `id-cf707b381cca4ae480e28f0e33160e30` | `Functioneel matchen van exameninstrument aan examens binnen examenplan` |
| `id-d2ff774d6a36436fa267afb9d7a0fb8f` | `Invullen van Student Leerbehoefte en begeleidingsbehoefte` |
| `id-d45ccd30e9dd44028ba1bd7b2726016e` | `Definiëren Examenvormkaders` |
| `id-d4b1bdf5b86747bc9da4e05100788904` | `Sociaal pedagogische achtergrond van student ophalen en analyseren` |
| `id-da1e2e33067a41ea8aeb22eead2e0de1` | `Definiëren type begeleiding` |
| `id-dd967093fbcd44d98f58d38c12493dac` | `Functioneel matchen van examen momenten en gerelateerde toets- of examen instrumenten` |
| `id-dfccdcf3f8de4019b992fbc3d030ed96` | `Bepalen van Toetsvorm` |
| `id-e0430c90c6e949ca8190f6abcdd335bd` | `Toetsing vormgeven` |
| `id-e638d4aa3ee54c82ad1a994dd1499a30` | `Concept Roosteren` |
| `id-e6604ab9294f42c38044a5b2a557cec7` | `Specificeren Toetsvorm` |
| `id-f4b65df3e18a4ecfbd3bc113e9c04775` | `Vergelijken behaalde leeruitkomsten met het door beoogd aanbod benodigde leeruitkomsten` |
| `id-f5f76d0e40eb46998488929986ed972e` | `Grofmazige Student Oriëntatie` |
| `id-f708fdbd26c846e988cf2cfe57248138` | `Kiezen collectie van leeruitkomsten` |
| `id-f70c746775c9427898fd6a89dd552121` | `Specificeren Lesruimte types` |
| `id-f99280ec44f0418e948cf3a4816a5f52` | `Migreren lesmethode naar instelling onderwijsspecificaties` |
| `id-fef95cfadc8745728037819ec0add737` | `Verenigen van Periode onderwijsaanbod Rooster met variabel vraag gedreven aanbod` |

### BusinessObjects (BusinessObject) — complete lijst (id + naam)

| ArchiMate id | BusinessObject (exacte naam in model) |
|---|---|
| `14521c7f-0165-4976-9ab8-35faf28dc32c` | `Werkproces` |
| `192fbc79-8d01-4760-b3be-f535680bc275` | `Kerntaak` |
| `31e03ae4-8615-4d5d-84d5-8c6060530b88` | `Opleidings-onderdeel` |
| `6bc5bfb8-fc44-4f14-9bd1-7261fcb18bf1` | `Kwalificatie dossier` |
| `7ae6a4f9-be38-439c-bd8b-32dd9d4a37e6` | `Leervraag` |
| `81bb33e3-21ee-418d-9cd1-918c90c4e989` | `Leertaak` |
| `8a65faa8-d8a9-40ad-9c5d-0b3506f2310e` | `Rooster` |
| `a068d2f1-33b6-4b06-9518-8ecde00ee615` | `Kwalificatie` |
| `a4ab7520-415a-4a69-9ed5-779755b8a65a` | `Persoonlijke leerroute` |
| `id-00ac26508cb742b4adf3d9ee7a53a43f` | `Lesruimte` |
| `id-04e701469cf1410bace7bc4b530c2517` | `Student Beschikbaarheid` |
| `id-04f2ca411b854f088fef07318fe9dc08` | `Concept Persoonlijke Inzet Planning` |
| `id-057b6216387748909503c0572817154d` | `Planningshorizon filter` |
| `id-089b261d3852438caa1aee96454fa262` | `Opleiding` |
| `id-0ab4b0777ee848f4a3ea809295378559` | `Behaalde / Aangetoonde Leertuikomsten / Skills / Vaardigheden` |
| `id-0d904713e8cf4a7989048fd3f8b2ebec` | `vraag naar competenties / leeruitkomsten` |
| `id-0e94fa1614da438a9d1c0e51f8439c89` | `Spreidingspatroon duur onderwijsvorm` |
| `id-0fdba1607f7749c2a0e1ab907ce850c3` | `Leeruitkomst` |
| `id-10993059e739461f8d0f56ac8482260a` | `Examenhandboek` |
| `id-1309f595216e44adbf12b49c266c3a14` | `Examen materiaal` |
| `id-17a5cda84b4d41519ebe13ab9d592b87` | `Examenvormkader` |
| `id-17a78220d3c1466f9f5ad85e6afe86ec` | `Begeleidingsvorm` |
| `id-1899d1e53e7e4edcbf31ad9ae29a52ac` | `Onderwijsvorm specificatie` |
| `id-19e5060117974d41be18ff6ced90fc0e` | `Vaardigheden / Skills` |
| `id-1a5641e8a59446fea9420602b4240ec1` | `Plangroepering / Concept Lesgroep` |
| `id-1ddf1b7c462d4f5f97bd45d32d25d87f` | `Student Persoonlijke Ontwikkelingswallet` |
| `id-2334b2135d434a049504064a70976656` | `Onderwijsvisie` |
| `id-24b3b5d1a4a04f88b4933c67298967a9` | `Keuzedeelprogramma` |
| `id-25ad014e29f44ff193732e771d817d50` | `Afspraken d.m.v. Definitief Inzet Teamplan` |
| `id-2724dff44b1140a29d383966831ca257` | `Flexibel aanbod Docenten Pool` |
| `id-294efc9d0c4847bea76b0941cf917241` | `Collectie van Leeropdrachten` |
| `id-29b240c816a5437ebd74c485f0982fc2` | `Uiterste afstudeer datum` |
| `id-2ef4ca43fa7c425c9e973c001a43b1fc` | `Behaalde / aangetoonde leeruitkomsten uit arbeidscontext` |
| `id-2f5010309447485aae4f5233a8052be8` | `(Didactische) Leervorm` |
| `id-30248c017c174bdbbe003bd9caf14999` | `Debiteur` |
| `id-31eb1115bee94622b4fa077afbceaef6` | `Leeropdracht` |
| `id-32bb2d6343e94e3b99957a64be790655` | `Examen` |
| `id-32c9a3eb9a5d46b8867c1601d859c99a` | `Organisatie Identiteit` |
| `id-34396599514c4c94a96dad2dcd881bd1` | `Faciliteiten` |
| `id-393fb9209a424181a8407a619eea0d2f` | `Team Inzet planning` |
| `id-3b52689ba76749988c8da46e6b0036cb` | `Voorzieningen` |
| `id-3d33e705137a4c2f9a44cb27d719b99c` | `Uiterste inschrijfdatum` |
| `id-3da12c34d8b84c5ebcdf8be97f9623f4` | `Query Limiting` |
| `id-3e5364b419234418b9f406b4e4c4faa7` | `Leergelegenheid aanbod` |
| `id-40b9b73698354de196087b2ef745bd58` | `Leslocatie` |
| `id-41611167936740e2be138df98d54cc3b` | `Toets- of Examen Matrijs / Beoordelingsmodel / Cesuur` |
| `id-445f4b49a7db447494b56d295a3dbf25` | `Prognose aantal student aanmeldingen` |
| `id-45a18a4dae9c4849b84e0820d6c4cb3d` | `Leercontext` |
| `id-4f6fb2715d0b4e1fa3113d8ee5860892` | `Lesbrief` |
| `id-509fb963bfa04d0a989e93b5518cb657` | `Opleidingskosten filter` |
| `id-50e4c3516343479ea91df89da8b34d32` | `Collectie van leeruitkomsten` |
| `id-510afd778cbb400d9a4315adc2d65af3` | `Middelen` |
| `id-51d72ee60bc746ef87f576784b081910` | `Instroom moment opleiding` |
| `id-552add20c64949ec9a0cdd873b49a87d` | `Waarde document (diploma / certificaat)` |
| `id-56f60cf7d29b4cbda6b99d25d38d5c56` | `Roosternaam` |
| `id-59e256e859014d8196975c5b3955aae8` | `Periode Onderwijsaanbod Rooster` |
| `id-5b5b4d1244384b738651c35b0fc5d3b4` | `Opleidingsbudget` |
| `id-5fcb76f5cfb242838cb912eea6b94a0f` | `Formatieve resultaat structuur` |
| `id-60646ec288b44921b3744509c7baf4a8` | `ProgrammaSpecificatie` |
| `id-60b70213e2314868ac20957f866932f1` | `Persoonlijke Ontwikkeling` |
| `id-6345c675bc9b4537a02f27378537e70b` | `Leerdoel` |
| `id-636dc5f45ffc431ebd855bcd9340a0b6` | `Onderwijsplan` |
| `id-6805cabe4c2545b68a8be296020c349f` | `Toetsvormkader` |
| `id-6a6bf608706d4ae898daf4f8e091f6f8` | `Niveau aanduiding` |
| `id-6b72eed06dba47839ac9e1aac067f83e` | `Crediteur - Omzetplaats binnen instelling` |
| `id-6c5e1df40c9146a3a98c56431b0f43cb` | `Strategisch kader start/stop opleidingsaanbod` |
| `id-709ca77f898b400a92a79c752f88455b` | `Werkinstructies` |
| `id-75f3dd546f1a40498cfe4f0cbd30b97d` | `Aan te bieden opleiding` |
| `id-7dcdeccf81854c5e95947da621b26518` | `Capaciteit` |
| `id-7e76de200fb941babe3cb88b9cd23f04` | `Rooster voorwaarden op lesniveau` |
| `id-7f8bd3bca55842a0ab38f6b2985c8ee3` | `Onderwijsteam` |
| `id-7fa1dcba58be40aea3b37eb3a4e92526` | `Toetsvormspecificatie` |
| `id-7ff02d7ffc1b41c882e3d5a817809f37` | `Concept Persoonlijk Inzet Rooster` |
| `id-838c82c2157649aa8c1f3d2c6b157efe` | `Team Inzet Capaciteiten overzicht` |
| `id-85bcb71c3d3a4b7b9064b7db01afa955` | `Microcredential` |
| `id-884a220dd7504edba207cb37fbf95ceb` | `Maximale reistijd` |
| `id-8a4da6622adc405687118b6aaeccc6dc` | `Student Keuze Criteria` |
| `id-8a8af3e6891149b4bb252587b3e6b49b` | `Studiebelasting en begeleide onderwijstijd indicatie` |
| `id-8db88f95a16949b9b291bfec4703eab2` | `Sociaal-Pedagogosche achtergrond` |
| `id-92ac20a74fa24e8991a40bdc9ae02478` | `Toetsvorm` |
| `id-93854848573d4c2e9aca37e750f0cc5c` | `Opleidingsonderdeelspecificatie` |
| `id-9760b498895c4fb49b69dabe27addec4` | `Door Student Gewenste Leervorm` |
| `id-9878a2a82d2c4a99ade0ffce831b83ec` | `Bekostigingscontext` |
| `id-9a4cac7c6f894d3fa4e2e520b6d8c6a0` | `Gewenste onderwijskundige gestandaardiseerde leeruitkomsten` |
| `id-9a77a0aa896e495684105afaa5cb7d79` | `Medewerker bestand` |
| `id-9aa7958766e64412979d91c36450ddba` | `Nominale Leerroute` |
| `id-9ac825f63e8a4db09ddc2cab59d85e53` | `Lesgroep` |
| `id-9c3684d262e14e7ba0e76b4d432663e5` | `Regulier aanbod Docenten Pool` |
| `id-9c6b211e92b74e4995e29514b23798e5` | `Lesplan / Leeronderdeelspecificatie` |
| `id-a02c959b6a534d3ea1c152da6a8f05c2` | `Doelgroep opleiding` |
| `id-a2e6cfdab822470e8cdcf85ef266d22a` | `Student Belastbaarheid` |
| `id-a440eeff33e34bba821a9d78191e1292` | `Gewenste Onderwijskundige Leeromgeving` |
| `id-a53b6c53a25f41fdb6123ea469609cd9` | `Onderwijsvormkader` |
| `id-a6126427a4da4ee1bc27f4bc4abcb323` | `Toetsplankader` |
| `id-ac7be3c68ce44339a80ea277c554afd6` | `Gewenst medewerker competentieprofiel` |
| `id-ac93907e90414c7aa1693662945dbcea` | `Onderwijsteam Vlekkenplan` |
| `id-b4c6199b76c144428ec56a734325e5c0` | `Lesleerdoel` |
| `id-bc4441a2a2674fa3a4edfbbc398a8632` | `Door Student gewenste verhouding BOT/OOT` |
| `id-bdcc9db0ef2a4102a9ffcc99c67b74b8` | `Duur onderwijsvorm binnen periode` |
| `id-bfbfb64fb6084bdf9f4d3f922dfc4360` | `Raamleerplan` |
| `id-c372b58295834733b726e989703f539a` | `Toetshulpmiddel` |
| `id-c6bc47e85f754894b6633383d0ee9786` | `Student Studie Termijn` |
| `id-c6efe6bc1514409d9f38b809f8fb97cf` | `Geografisch filter` |
| `id-c71cb97759ed4209b57b98bc4b2bb636` | `Les` |
| `id-c8d693e99c324898b1d83692a58cb430` | `Toetsinstrument` |
| `id-cc90d10634bc407fbd6f3d44f333a283` | `Onderwijsprofessional` |
| `id-cf3e5502fc1b41499749f5930fae4899` | `Examenplankader` |
| `id-cf5a00e4dae647ceaef44a9cd77d1a5c` | `Examenregelement` |
| `id-d0e4bebbc648445696d4eed7e6cce4fe` | `Collectie van Lesuitkomsten` |
| `id-d40c8ec1f3054a999003b489efbb5efd` | `Leermiddelgroep` |
| `id-d4494540b7cf466da4ca7352d6ef9eb1` | `Leeractiviteit` |
| `id-d5595003d603499fb3838645472e91c2` | `Strategische Onderwijsomgeving kaders` |
| `id-d875828568f34447a07eacb7f489a1df` | `Lesmateriaal` |
| `id-da9b96bc787e4e9d9110d5155dcb00b0` | `Exameninstrumentkader` |
| `id-df0a22ce7a95413c8b00857f2abab107` | `Student streef leeruitkomsten` |
| `id-e02512067a044e44bb6886b0cec444de` | `Stamgroep / Klas` |
| `id-e337efe34d514e36b50e04af969d9b4a` | `Capaciteitsplanning` |
| `id-e4c1b079d41148398e5f5d6171c86f30` | `Kostenplaats ROD` |
| `id-e766343d240c4da9b6c5ea0c5177abdd` | `OP Competentieprofiel` |
| `id-ebf7b3638e754098bd2fca79de355735` | `Student en Organisatie associatie` |
| `id-ec03e3cd2e5b47549925842d86181f67` | `Standplaats` |
| `id-ef73b0de226a4969a317e4c245a567af` | `Onderwijsontwerpprincipes` |
| `id-f198b9912ab24b03a5707078de350c15` | `Student persoonlijke planning` |
| `id-f4788b64b89241cc86d099d383e5d83e` | `Lesplanning` |
| `id-f4b9c42e13e7443da0f46960023e2093` | `Toetsinstrumentkader` |
| `id-fae39bc46fb949b2b11ef78e656525e3` | `Student Identiteit` |
| `id-fccf38291cd34a81a1b9b8d107c53f1c` | `Toetsmatrijs` |
| `id-fd9ce43448134efdad2c84d251854c3c` | `Beordelingsmodel` |
| `id-fe270c45f9b24c078bb8157a82abcfe8` | `Examen instrument` |

## View: Informatiemodel Onderwijsontwerp

### BusinessObjects (BusinessObject) — shortlist met duiding

| ArchiMate id | BusinessObject (exacte naam in model) | Sector-interpretatie (1 zin) |
|---|---|---|
| `id-0adef78ff8c64379a6b5977f0ee61ad1` | `Onderwijsaanbod Model` | Beleidskeuze voor hoe onderwijsspecificaties worden omgezet naar aanbod (planning/roostering). |
| `id-f3b6da2b1a4043a9b9c15cf0afc13f99` | `Jaarplanning` | Jaarplanning (tactisch) als kader voor planbaarheid en (her)verdeling over perioden. |
| `id-6493408c3d7a41b09b6a153df836dc0a` | `Jaarplanningsbeperkingen` | Constraints/regels die het plannen begrenzen (input voor “roosterautomaat/CSP”). |
| `id-1a5641e8a59446fea9420602b4240ec1` | `Plangroepering / Concept Lesgroep` | Groepeerlogica van deelnemers/lesgroepen tussen planbaar aanbod en concrete roostering. |
| `id-7c09e9944be447c59c41bd0a3c139551` | `Lokalenvlek / cluster` | Cluster/profiel van ruimtes (geen lokaal-instantie), gebruikt om te matchen op ruimtetype/requirements. |
| `id-ac93907e90414c7aa1693662945dbcea` | `Onderwijsteam Vlekkenplan` | Team-/inzetprofiel (beschikbaarheid/competenties) gebruikt voor planning/roostering. |
| `id-407a7374a54345cd91666f586d7a0765` | `Medewerker` | Individuele medewerker (resource-instantie) relevant bij roostering/toewijzing. |
| `id-4a2d82877b5947a99ac15cc2c38caf6e` | `Schaarste van middelen` | Bottleneck-informatie die planbaarheid en roostering beperkt. |
| `id-972c5dec1d5347b9bb205e706d5ce4f7` | `Jaarplanning examens` | Jaarplanning specifiek voor examens/toetsmomenten. |
| `id-cf3e5502fc1b41499749f5930fae4899` | `Examenplankader` | Kaderobject voor examenplanning (normerend voor toets-/examenaanbod). |
| `id-17a5cda84b4d41519ebe13ab9d592b87` | `Examenvormkader` | Kader voor examenvormen (vormkeuze heeft impact op resources/afname). |
| `id-cf5a00e4dae647ceaef44a9cd77d1a5c` | `Examenregelement` | Regels/regelementen rond examinering (doorwerken in planning en uitvoering). |
| `id-da9b96bc787e4e9d9110d5155dcb00b0` | `Exameninstrumentkader` | Kader voor welke exameninstrumenten ingezet mogen/kunnen worden. |
| `id-fe270c45f9b24c078bb8157a82abcfe8` | `Examen instrument` | Het gekozen instrument (bijv. toets/exameninstrument) om uitkomsten te valideren. |
| `id-32bb2d6343e94e3b99957a64be790655` | `Examen` | Examen als object in de keten (gericht op valideren van leeruitkomsten). |
| `id-b7eee02a645f4d62bc01cf0e30562e33` | `Summatieve beoordeling` | Beoordeling op summatief niveau (input naar resultaatvaststelling). |
| `id-01c2f076f0cc4dabb5718ded270e4b74` | `Summatief resultaat` | Resultaatobject op summatief niveau (uitkomst van beoordeling/besluit). |

### BusinessObjects (BusinessObject) — complete lijst (id + naam)

| ArchiMate id | BusinessObject (exacte naam in model) |
|---|---|
| `0f9706e1-5311-48e7-b531-d22ea506f6db` | `Module` |
| `14521c7f-0165-4976-9ab8-35faf28dc32c` | `Werkproces` |
| `16fddf6a-7e29-47d1-b520-d836d1f7b42b` | `Inschrijving` |
| `192fbc79-8d01-4760-b3be-f535680bc275` | `Kerntaak` |
| `1b667d54-7a99-4b2b-b47c-8247d45e9222` | `Student` |
| `31e03ae4-8615-4d5d-84d5-8c6060530b88` | `Opleidings-onderdeel` |
| `6bc5bfb8-fc44-4f14-9bd1-7261fcb18bf1` | `Kwalificatie dossier` |
| `6ea81a60-8e54-4b56-9fec-7bbb285637c7` | `Onderwijs aanbieder` |
| `73b4165f-a592-4cf7-80da-bbf055f7df86` | `Keuzedeel` |
| `7ae6a4f9-be38-439c-bd8b-32dd9d4a37e6` | `Leervraag` |
| `7cde48dd-2814-4b32-8139-bea067af746a` | `Onderwijs locatie` |
| `803a3bcd-098f-482c-9fcc-5734e445f3e1` | `Onderwijs programma` |
| `81bb33e3-21ee-418d-9cd1-918c90c4e989` | `Leertaak` |
| `8a65faa8-d8a9-40ad-9c5d-0b3506f2310e` | `Rooster` |
| `a068d2f1-33b6-4b06-9518-8ecde00ee615` | `Kwalificatie` |
| `a4ab7520-415a-4a69-9ed5-779755b8a65a` | `Persoonlijke leerroute` |
| `d9b796c2-755a-4a48-82cc-7b6bc139e3fd` | `Eenheid met waardedocument` |
| `e43a49cf-e25d-4aa2-8948-d25c3d7204a2` | `OER` |
| `id-01c2f076f0cc4dabb5718ded270e4b74` | `Summatief resultaat` |
| `id-0ab4b0777ee848f4a3ea809295378559` | `Behaalde / Aangetoonde Leertuikomsten / Skills / Vaardigheden` |
| `id-0adef78ff8c64379a6b5977f0ee61ad1` | `Onderwijsaanbod Model` |
| `id-0c1cfde5039544c88a9d450873d1acf6` | `Leeronderdeel / Leeractiviteit specificatie` |
| `id-0d904713e8cf4a7989048fd3f8b2ebec` | `vraag naar competenties / leeruitkomsten` |
| `id-0fdba1607f7749c2a0e1ab907ce850c3` | `Leeruitkomst` |
| `id-106e9ff41b1149eaa5f5cb8df5d1dca1` | `Student keuze` |
| `id-1513533199c845bfb86e18b28790efbf` | `Vaardigheid` |
| `id-17a5cda84b4d41519ebe13ab9d592b87` | `Examenvormkader` |
| `id-1899d1e53e7e4edcbf31ad9ae29a52ac` | `Onderwijsvorm specificatie` |
| `id-1a5641e8a59446fea9420602b4240ec1` | `Plangroepering / Concept Lesgroep` |
| `id-1ddf1b7c462d4f5f97bd45d32d25d87f` | `Student Persoonlijke Ontwikkelingswallet` |
| `id-24d65069a1824ac9b0b99ffee3d476e2` | `Onderwijsruimte type` |
| `id-294efc9d0c4847bea76b0941cf917241` | `Collectie van Leeropdrachten` |
| `id-2f5010309447485aae4f5233a8052be8` | `(Didactische) Leervorm` |
| `id-31eb1115bee94622b4fa077afbceaef6` | `Leeropdracht` |
| `id-32bb2d6343e94e3b99957a64be790655` | `Examen` |
| `id-36f43fa5bab243388acd8706fa8d3a5a` | `Docent` |
| `id-386fee11b40b4fdfb012d71e81873939` | `Schaartste van mensen` |
| `id-3e6532839e7f4381a54bd7807db0a7b8` | `Les specificatie / toets specificatie` |
| `id-407a7374a54345cd91666f586d7a0765` | `Medewerker` |
| `id-43bb01b43c2341e8af4a425c054c1844` | `Examenmoment` |
| `id-450c916b36c0413092626359aeeb976b` | `Programma Specificatie` |
| `id-4a2d82877b5947a99ac15cc2c38caf6e` | `Schaarste van middelen` |
| `id-4a5a5dc53a7e4dadb5b29ff164d16d97` | `Persoonlijke ontwikkeling` |
| `id-4be8a96526f94ab4a26ea0dbcd235558` | `Formatieve beoordeling` |
| `id-4c3403108739418988e7b97b336dc6b2` | `Examenplan` |
| `id-4d07b94d28194a9e9c873a3f66cae959` | `Toetsplan` |
| `id-4e06285a66654ac3a54447841c2f55da` | `Collectie van Leermiddelgroepen` |
| `id-50e4c3516343479ea91df89da8b34d32` | `Collectie van leeruitkomsten` |
| `id-5110d5bbaead4d209dc6a1c9762ffb92` | `Collectie van Medewerkertypes` |
| `id-51a1ec6086054de2ad3b1b09039da5a7` | `Beoordeling` |
| `id-51d72ee60bc746ef87f576784b081910` | `Instroom moment opleiding` |
| `id-552add20c64949ec9a0cdd873b49a87d` | `Waarde document (diploma / certificaat)` |
| `id-57d9474087ee49d3a4300678c4d623f4` | `Kennis` |
| `id-5dee25def74a41e1b2294494017fd046` | `Summatieve resultaat structuur` |
| `id-5fcb76f5cfb242838cb912eea6b94a0f` | `Formatieve resultaat structuur` |
| `id-5fecfe47e131473fac96987b8b02f247` | `Duur Leervorm` |
| `id-61ac8213cf9e4e0fb4d9216364201334` | `Toets` |
| `id-6345c675bc9b4537a02f27378537e70b` | `Leerdoel` |
| `id-636dc5f45ffc431ebd855bcd9340a0b6` | `Onderwijsplan` |
| `id-643ca2c9aa794cf584d59f13172347dc` | `Cursusregelement` |
| `id-6493408c3d7a41b09b6a153df836dc0a` | `Jaarplanningsbeperkingen` |
| `id-6805cabe4c2545b68a8be296020c349f` | `Toetsvormkader` |
| `id-68d2ba42fa8045558646391734764e16` | `Start- en eind datumtijd les` |
| `id-6a4a4bd9a219452295bcf8eeacb99aed` | `Formatief resultaat` |
| `id-6c5e1df40c9146a3a98c56431b0f43cb` | `Strategisch kader start/stop opleidingsaanbod` |
| `id-709ca77f898b400a92a79c752f88455b` | `Werkinstructies` |
| `id-74d479d8b80a4937bafabd93a72b6bbe` | `Onderwijseenheid / Opleidingsonderdeel` |
| `id-7a83347dcab9475b8e7a8789c012b343` | `Lokaal` |
| `id-7c09e9944be447c59c41bd0a3c139551` | `Lokalenvlek / cluster` |
| `id-7d3efb39ec704087a32f27ed7a9a3ecd` | `SBU en BOT van verzamelde leervormen` |
| `id-7dcb06c9e8ed4665aebb178f2c446fd2` | `Leeractiviteitregelement` |
| `id-7fa1dcba58be40aea3b37eb3a4e92526` | `Toetsvormspecificatie` |
| `id-801f14cdc8e24583b7114aa68b51ecde` | `Leervormstrategie` |
| `id-83cc7323dd344e88910bb43213d077fa` | `Lokaaltypes` |
| `id-84ef7ea2d90c4e81b33c5d4e46067791` | `Leeromgeving` |
| `id-87604d9b18514ee683b2e6a4a0635c31` | `Opleiding` |
| `id-8a8af3e6891149b4bb252587b3e6b49b` | `Studiebelasting en begeleide onderwijstijd indicatie` |
| `id-8db88f95a16949b9b291bfec4703eab2` | `Sociaal-Pedagogosche achtergrond` |
| `id-92ac20a74fa24e8991a40bdc9ae02478` | `Toetsvorm` |
| `id-972c5dec1d5347b9bb205e706d5ce4f7` | `Jaarplanning examens` |
| `id-9760b498895c4fb49b69dabe27addec4` | `Door Student Gewenste Leervorm` |
| `id-9aa7958766e64412979d91c36450ddba` | `Nominale Leerroute` |
| `id-9ac825f63e8a4db09ddc2cab59d85e53` | `Lesgroep` |
| `id-9c92f2be1c274ac1ad49636a6582a745` | `Programma Aanbod` |
| `id-a02c959b6a534d3ea1c152da6a8f05c2` | `Doelgroep opleiding` |
| `id-a1696c2a66224c0986e89f104fe56492` | `Lesuitkomst` |
| `id-a1c5898fd1cc42abab687cf351581ac2` | `Competenties / skills` |
| `id-a440eeff33e34bba821a9d78191e1292` | `Gewenste Onderwijskundige Leeromgeving` |
| `id-a53b6c53a25f41fdb6123ea469609cd9` | `Onderwijsvormkader` |
| `id-a6126427a4da4ee1bc27f4bc4abcb323` | `Toetsplankader` |
| `id-ac7be3c68ce44339a80ea277c554afd6` | `Gewenst medewerker competentieprofiel` |
| `id-ac93907e90414c7aa1693662945dbcea` | `Onderwijsteam Vlekkenplan` |
| `id-b4c6199b76c144428ec56a734325e5c0` | `Lesleerdoel` |
| `id-b7eee02a645f4d62bc01cf0e30562e33` | `Summatieve beoordeling` |
| `id-bc4441a2a2674fa3a4edfbbc398a8632` | `Door Student gewenste verhouding BOT/OOT` |
| `id-c372b58295834733b726e989703f539a` | `Toetshulpmiddel` |
| `id-c71cb97759ed4209b57b98bc4b2bb636` | `Les` |
| `id-c8d693e99c324898b1d83692a58cb430` | `Toetsinstrument` |
| `id-ca25fff2caf14ce589c79a7eb175614f` | `Meerjaren planning` |
| `id-cf3e5502fc1b41499749f5930fae4899` | `Examenplankader` |
| `id-cf5a00e4dae647ceaef44a9cd77d1a5c` | `Examenregelement` |
| `id-d0e4bebbc648445696d4eed7e6cce4fe` | `Collectie van Lesuitkomsten` |
| `id-d40c8ec1f3054a999003b489efbb5efd` | `Leermiddelgroep` |
| `id-d416fe8624c84ba18b4acf49a12fd21e` | `Instroomstrategie` |
| `id-d4494540b7cf466da4ca7352d6ef9eb1` | `Leeractiviteit` |
| `id-d5595003d603499fb3838645472e91c2` | `Strategische Onderwijsomgeving kaders` |
| `id-d9e0b4c11d864c8bae6bc819fd0895d5` | `Programmaregelement` |
| `id-da9b96bc787e4e9d9110d5155dcb00b0` | `Exameninstrumentkader` |
| `id-e02512067a044e44bb6886b0cec444de` | `Stamgroep / Klas` |
| `id-e0dffac14ecf48fc9e3a85bfc5949c65` | `Medewerker Type / Expertise Profiel` |
| `id-e2f1190b4ac9449e98eb467770a88405` | `Collectie aan volgordelijke deelname vereisten` |
| `id-e3bacf4123824e84b03ac57a1b2c581f` | `Collectie van Leervormen` |
| `id-e766343d240c4da9b6c5ea0c5177abdd` | `OP Competentieprofiel` |
| `id-e7b4ca19b9ab450db8870ea1b282a1cc` | `Deelname vereisten` |
| `id-eaef3cdce41d4d658d820f19bc920584` | `Collectie van Leerdoelen` |
| `id-f1d75ff9b7f44402bb7d484bfc51c923` | `Toetsmoment` |
| `id-f3b6da2b1a4043a9b9c15cf0afc13f99` | `Jaarplanning` |
| `id-f4788b64b89241cc86d099d383e5d83e` | `Lesplanning` |
| `id-f7953f4d6f734d53b128eb7523ea2ed8` | `Context` |
| `id-fc8cd6e7d5884b8fa964fefc23e1fb54` | `Inzicht` |
| `id-fccf38291cd34a81a1b9b8d107c53f1c` | `Toetsmatrijs` |
| `id-fe270c45f9b24c078bb8157a82abcfe8` | `Examen instrument` |

## Implicaties voor herschrijven (korte duiding)

- Het view `Informatiemodel Onderwijsontwerp` dwingt een onderscheid af tussen:
  - **planbaarheid** (werken met profielen, kaders, beperkingen, vlekken) en
  - **roostering** (werken met concrete resource-instanties zoals `Medewerker` en uiteindelijk concrete ruimte-instanties).
- Examenplanning is expliciet een eigen cluster (kaders + instrumenten + jaarplanning), wat vraagt om een duidelijke plek in scenario’s/flows vóórdat techniek wordt besproken.

