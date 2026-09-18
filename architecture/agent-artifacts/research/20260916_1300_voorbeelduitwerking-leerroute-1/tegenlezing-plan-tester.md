## Testrapport

Deliverable: `architecture/agent-artifacts/feature-plans/20260917_1500_jochem-in-het-informatiemodel.md` (worktree `wt-237`, branch `237-voorbeelduitwerking-agent-artifacts`, basis gelijk aan `dev`). Toetsvraag: is het plan uitvoerbaar en haalt het op 30 september het doel (fase 2 tot 4 van Jochem in MIM 1 en 2, naast het eigen model van elk kerngroeplid). Context gelezen: de mock-up, de PoC-scripts en `AGENTS.md`. Aanvullend feitenonderzoek in de repository waar het plan zijn basis noemt (model, branches, scripts).

Voorcontrole: geslaagd. `python3 scripts/validate-docs.py architecture/agent-artifacts/feature-plans` geeft 3 bestanden gecontroleerd, 0 problemen, exitcode 0.

### Feiten uit de repository die het oordeel dragen

| Feit | Waargenomen | Raakt |
|---|---|---|
| `architecture/model/informatiemodel/` (met `informatiemodel.json`), `architecture/docs/specificatie/begrippen/begrippen.json`, `scripts/genereer-informatiemodel-doc.py`, `scripts/publiceer-informatiemodel.py` en de map `tests/` | Bestaan niet op `dev` en niet in de worktree; alleen op de branches `89-informatiemodel-en-begrippenkader` en `232-publiceer-informatiemodel-naar-public` (232 bevat 89; geen van beide zit in `dev`) | R1, R2, R6, R9; features 1, 6, 8 |
| `model.archimate` op `dev` tegenover branch 89 | 1861 regels verschil; op `dev` ontbreken de view "OKx informatiemodel" en het objecttype `Plaatsingsgroep` | Features 1, 3, 4, 8 |
| `informatiemodel.json` (branch 232) | 66 objecttypen met velden `naam`, `kolom`, `scope` (56 binnen, 10 buiten), 156 relaties met `soort`, `van`, `naar`, `label` (105 zonder label); zeven kolommen als families | R1, R2, R5 |
| Leslaag | `Les specificatie`, `Lesgelegenheid`, `Lesgelegenheid verbintenis`, `Lesgelegenheid resultaat` staan op `buiten` | R9 klopt als uitgangspunt |
| Label `bestaat uit` | Staat op precies twee relaties (Kwalificatie naar Kerntaak, Kerntaak naar Werkproces). De nestingparen uit de mock-up (Opleidingaanbod naar Opleidingsprogramma aanbod, Opleidingsprogramma aanbod naar Onderwijseenheid aanbod, Leergelegenheid naar Lesgelegenheid) zijn Aggregations zonder label; Opleiding aanbod verbintenis naar Opleidingsprogramma aanbod verbintenis is een Association met label `Minimaal 1`; tussen Opleidingaanbod en Cohort / periode bestaat geen relatie | R1 |
| Objecttype `Verzoek tot Aanbod` (mock-up, PoC `ontstaat.json`, aanname) | Bestaat in geen enkele versie van het model | R1 |
| `Opleiding aanbod  verbintenis` (dubbele spatie) | Zo in het model en in `informatiemodel.json`; de mock-up gebruikt de naam met een spatie | R1, R9, feature 4 en 8 |
| View "OKx hoofdplaat v1.7<concept>" en "... (zonder context applicaties)" | 33 en 28 flows, geen enkele met naam; 44 en 31 bendpoints, elk met `startX`, `startY`, `endX`, `endY` | R4, R9: de knikpuntclaim in feature 3 klopt |
| Pijlnummers | De tabel in `doc/OKx_Projectoverzicht.md` nummert 1 tot 17 op de plaat v20260317 (png) met andere componenten (Student Kiest, Toets- en examenafname). De mock-up gebruikt hoofdplaat 8, 10 en 13 voor pijlen die in die tabel andere bron en doel hebben | R4, features 3 en 4 |
| Zeven vragen | Staan in `research/.../plan.md` sectie 7 als (a) tot (g); (c), (e) en (f) gaan over berichtstroompatroon, governance en endpoint | R8 |
| `validate-docs.py` | Controleert links naar .md, .json, .py, .png, .jpg; geen .svg | R5 |
| `jsonschema` | Versie 4.26 aanwezig in de container | R1 |
| Kalender | 19 en 20 september zijn zaterdag en zondag | Implementatieplan |

### Dekkingstoets per eis

| Eis | Oordeel | Bewijs of gebrek |
|---|---|---|
| R1 Regeltabel als bron | deels | Toetsbaar in opzet (schema, naamcontrole, labelcontrole, pijlcontrole). Gebreken: (a) de veldenlijst mist wat een stroomt-regel volgens de mock-up en de PoC draagt: bezitter, afnemer, pijlnummer, koppeling-ID en de zin; (b) het criterium "elke stroomt-regel wijst naar een bestaande pijl" sluit de lege regel "geen pijl op de hoofdplaat" uit die de mock-up als derde principe noemt; (c) "elke objecttypenaam bestaat in informatiemodel.json" faalt op het eerste voorbeeld uit de mock-up (`Verzoek tot Aanbod`, aanname) en op `Opleiding aanbod verbintenis` (dubbele spatie in het model); (d) "elk relatielabel bestaat op de plaat" is niet gedefinieerd voor ongelabelde relaties: `bestaat uit` staat op twee relaties, de nesting in de mock-up leunt op ongelabelde Aggregations, en het paar Opleidingaanbod / Cohort heeft geen relatie; (e) `informatiemodel.json` en `begrippen.json` bestaan niet op de basisbranch; (f) `stromen.json` is een product van feature 3 |
| R2 Dekking | deels | "Binnen scope" is toetsbaar via het veld `scope`. Gebreken: "dat in een fase ontstaat" heeft geen bron buiten de regeltabel zelf, dus de controle kan alleen "elk objecttype binnen scope heeft ergens een ontstaat-regel" afdwingen, niet "in die fase"; "een regel" (precies een) botst met de mock-up, waar Plaatsingsgroep in fase 2 en in fase 3 ontstaat; de lege lijst "voor fase 2 tot 4" vraagt een verwachting per fase die nergens staat |
| R3 Regelrenderer | gehaald | Toetsbaar: per regelsoort een positief geval, drie faalgevallen benoemd, "zonder externe fonts" en "rendert op GitHub" zijn mechanisch te benaderen (welgevormde XML met xmlns, geen `<link>`, `@import`, `url(`, `<script>`, `<foreignObject>`). Opmerking: het faalgeval "onbekend objecttype" overlapt R1; zeg waar die controle leeft |
| R4 Hoofdplaat-renderer | deels | Toetsbaar: de knikpuntclaim is bevestigd in het model (beide offsets aanwezig), een bekend voorbeeld voor de test is beschikbaar, het inlezen van een view en de export zijn testbaar, het akkoord van de modelleur is een stopmoment met vastlegbaar bewijs. Gebreken: de viewnaam in de eis ("OKx hoofdplaat v1.7") is niet de naam in het model; "geen naam valt weg" heeft geen definitie (de PoC kapt na zes regels); het veld `pijlnummer` in `stromen.json` heeft geen bron, en de terugval in feature 4 (tabel projectoverzicht) hoort bij een andere plaat en spoort niet met de nummers in de mock-up |
| R5 Documentgenerator | deels | Toetsbaar: validate-docs groen, acht fasesecties, familietabellen tegen `kolom` (zeven families). Gebreken: `validate-docs.py` controleert geen .svg-verwijzingen, dus "elke SVG-verwijzing lost op" moet in de generatortest, of validate-docs krijgt svg erbij; doel 1 belooft de andere fasen "als samenvatting in chips" op 30 september, terwijl feature 4 die fasen na 30 september vult en feature 5 "stubs" levert: wat tonen de chips dan; de familiebron (veld `kolom`) staat niet in de eis |
| R6 Publicatie | deels | Toetsbaar via de Public-controles en de draft-PR. Gebrek: "het bestaande publiceerscript" bestaat alleen op branch 232 (niet gemerged), en de stapeling op Public PR 104 is een externe afhankelijkheid; het plan noemt geen van beide bij feature 6 |
| R7 Bijlage kerngroep | deels | Toetsbaar: aantal slides, pdf aanwezig, openingsslide, verzenddatum. Gebrek: doel 3 en de risicotabel zeggen hoogstens zes pagina's; R7 zegt zes inhoudelijke slides plus de regels van fase 2 tot 4, en de mock-up telt voor fase 2 en 3 alleen al negen regels; de twee maten spreken elkaar tegen. Doel 4 ("het antwoord per regel kan worden genoteerd") heeft geen eis en geen feature. Feature 7 noemt pptx, R7 niet |
| R8 Vragenpagina | deels | De zeven vragen bestaan (plan.md sectie 7, a tot g) en de criteria zijn toetsbaar: zeven vragen, per vraag een consequentie, geen besluitvraag. Gebrek: de eis verwijst naar "het plan onder Public #106" in plaats van naar de repo-lokale bron; drie vragen (c, e, f) gaan over berichtstroompatroon, governance en endpoint, buiten de scope die feature 5 uitsluit; "consequentie voor het model" is daar niet gedefinieerd |
| R9 Modelhuiswerk | deels | Toetsbaar: `validate-archimate.py`, leslaag van buiten naar binnen (nu vier objecttypen buiten), labeltabel vervalt (nu nul van 33 flows met naam). Gebreken: de generator voor `informatiemodel.json` leeft op branch 89; "de plaatkoppen opschonen" heeft geen criterium; het hernoemen van `Opleiding aanbod  verbintenis` verandert een naam waar feature 4 fase 3 (22 september) al op leunt, en feature 8 heeft geen datum |
| R10 Reviews | gehaald | Toetsbaar: rapporten in de PR-beschrijving, hoogstens drie iteraties. Opmerking: het tijdpad heeft een reviewdag (23 september) terwijl features 1, 2 en 3 eerder en 6 en 7 later een eigen PR krijgen; zeg welke PR's de drie reviews krijgen en of een scriptfeature met tests volstaat |

### Afhankelijkheden en volgorde (sectie 3 en 5)

| Feature | Plan zegt | Waargenomen | Oordeel |
|---|---|---|---|
| 1 Regeltabel en controle | Hangt af van: geen; werkt op de huidige `informatiemodel.json` | `informatiemodel.json` en `begrippen.json` bestaan alleen op branch 89; de stroomt-controle heeft `stromen.json` uit feature 3 nodig, dat op 18 september nog niet bestaat | niet |
| 2 Regelrenderer | Feature 1 (schema) | Klopt | gehaald |
| 3 Hoofdplaat-renderer | Hangt af van: geen; alleen-lezen | Klopt voor het tekenen; het veld `pijlnummer` in de export hangt aan de keuze in feature 8 (zonder datum) of aan een tussenregel die er niet is | deels |
| 4 Regels vullen | Feature 1; feature 3 voor pijlnummers, tot die tijd de tabel in het projectoverzicht | De tabel in het projectoverzicht hoort bij plaat v20260317 met andere componenten; de mock-up nummert anders. Fase 3 gebruikt de naam `Opleiding aanbod verbintenis` die pas na feature 8 in het model staat | deels |
| 5 Documentgenerator | Features 1, 2 en 4 | Mist feature 3 voor "de plaat als beeld" (terugval op de JPG bestaat, dus geen blokkade) | deels |
| 6 Publicatie | Feature 5 | Mist branch 232 (publiceerscript) en Public PR 104 | deels |
| 7 Bijlage en deck | Features 2, 4 en 5 | Klopt; Slidev en playwright-chromium staan in `presentaties/package.json`, `node_modules` moet nog geinstalleerd worden in de container | gehaald |
| 8 Modelhuiswerk | Hangt af van: geen; loopt parallel | Heeft de generator van branch 89 nodig; heeft geen datum terwijl R1 (naamcontrole) en feature 4 fase 3 op de hernoeming wachten | deels |
| Volgorde 18 september: feature 1 en 2 voor feature 3 | Feature 1 levert de controle op R1 inclusief stroomt | De stroomt-controle kan pas na feature 3 draaien | niet |
| 19 tot 22 september: feature 3 en fase 2 | Twee dagen gebudgetteerd | 19 en 20 september vallen in het weekend; 21 en 22 september blijven over, en 22 september draagt ook fase 3 en 4 en feature 5 | deels |
| Milestone | Features 1 tot 7 onder een milestone | Feature 8 en sub-issue 9 vallen erbuiten; werkafspraak 4 wil elk issue onder een milestone | deels |

### Testgevallen per scriptfeature

De methodenamen zijn Engels, de meldingen die het script geeft Nederlands. Elke verwachting wordt in de test berekend uit een eigen fixture (een kleine `informatiemodel.json`, `stromen.json` en regeltabel in een tijdelijke map), nooit uit de inhoud van de repository. Locatie `tests/test_<script>.py`, stdlib `unittest`. Waar een geval van een open beslissing afhangt, staat dat erbij; de maker kiest, de test volgt.

**Feature 1, `tests/test_controleer_voorbeeldregels.py`**

| Methode | Given | Then |
|---|---|---|
| test_given_valid_table_when_checked_then_exit_zero_and_no_findings | Fixture met drie objecttypen binnen scope, een gelabelde relatie, een pijl in `stromen.json`; tabel met een ontstaat-regel per type en een stroomt-regel op die pijl | Exitcode 0, lege bevindingenlijst |
| test_given_rule_without_required_field_when_checked_then_schema_error_names_rule_and_field | Ontstaat-regel zonder `instantie` | Exitcode 1, melding noemt de regel (fase, stap) en het veld |
| test_given_unknown_objecttype_when_checked_then_error_names_type | Regel met objecttype dat niet in de fixture staat | Exitcode 1, melding noemt de naam en de regel |
| test_given_name_differing_only_in_whitespace_when_checked_then_error_names_both | Fixture kent `A  B` (dubbele spatie), regel gebruikt `A B` | Melding noemt beide schrijfwijzen (randgeval, raakt R9) |
| test_given_assumed_objecttype_not_on_plate_when_checked_then_outcome_per_decision | Regel met `aanname: ja` en een objecttype buiten de fixture | Beslissing M1: geweigerd, of toegestaan en apart gerapporteerd |
| test_given_label_on_pair_when_checked_then_accepted | Relatielabel dat in de fixture op precies dat paar (van, naar) staat | Geen bevinding |
| test_given_label_existing_elsewhere_but_not_on_pair_when_checked_then_error | Label bestaat in de fixture op een ander paar | Exitcode 1, melding noemt het paar (beslissing M2 legt vast dat de controle op het paar werkt) |
| test_given_unlabeled_aggregation_when_nesting_used_then_accepted | Ouder en kind met een Aggregation zonder label; regel nest het kind | Geen bevinding (beslissing M2: `bestaat uit` staat voor Aggregation of Composition) |
| test_given_nesting_without_relation_when_checked_then_error | Nesting tussen twee typen zonder relatie in de fixture | Exitcode 1 |
| test_given_stroomt_rule_on_unknown_arrow_when_checked_then_error | Stroomt-regel met pijlnummer dat niet in `stromen.json` staat | Exitcode 1, melding noemt het nummer |
| test_given_stroomt_rule_marked_no_arrow_when_checked_then_accepted_and_listed | Stroomt-regel met de markering "geen pijl op de hoofdplaat" | Geen fout, wel een regel in de rapportage (beslissing M1) |
| test_given_in_scope_type_without_rule_when_checked_then_listed_as_missing | Fixture met n typen binnen scope, tabel dekt n minus 1 | Ontbrekende lijst is precies het ene type; exitcode 1 |
| test_given_out_of_scope_type_without_rule_when_checked_then_not_listed | Type met `scope: buiten` zonder regel | Niet in de ontbrekende lijst |
| test_given_type_with_two_ontstaat_rules_when_checked_then_outcome_per_decision | Twee ontstaat-regels voor een type in twee fasen | Beslissing M3: fout, of toegestaan |
| test_given_fase_expectation_when_checked_then_missing_list_per_fase | Verwachting per fase in de fixture, een type ontbreekt in fase 2 | Lijst noemt fase 2 en het type (beslissing M3) |
| test_given_empty_table_when_checked_then_missing_list_equals_all_in_scope_types | Lege tabel met alleen de fasen | Ontbrekende lijst gelijk aan de scope-set van de fixture (randgeval) |
| test_given_unknown_fase_or_step_when_checked_then_error | Regel met fase 9 of een stap die niet in de fasenlijst staat | Exitcode 1 |
| test_given_missing_informatiemodel_json_when_checked_then_exit_two_with_dutch_message | Pad naar een niet-bestaand bestand | Exitcode 2, Nederlandse melding (ontbrekende afhankelijkheid) |
| test_given_missing_stromen_json_when_checked_then_outcome_per_decision | `stromen.json` ontbreekt | Beslissing M5: stroomt-controle overgeslagen met waarschuwing, of exitcode 2 |
| test_given_invalid_json_when_checked_then_exit_one_names_position | Regeltabel met syntaxfout | Exitcode 1, melding met regelnummer |

**Feature 2, `tests/test_teken_voorbeeldregels.py`**

| Methode | Given | Then |
|---|---|---|
| test_given_ontstaat_rule_when_drawn_then_svg_contains_role_step_and_each_instance | Ontstaat-regel met rol, stap en drie objecten | Elke naam en instantie komt als tekst voor; exact een processtap-icoon |
| test_given_stroomt_rule_when_drawn_then_svg_contains_owner_object_consumer_and_arrow_id | Stroomt-regel met bezitter, object, afnemer, pijl-ID | Alle vier als tekst; een pijlpunt |
| test_given_nested_objects_when_drawn_then_child_rect_within_parent_rect | Ouder met twee kinderen | Uit de `rect`-attributen berekend: kindrechthoek ligt binnen de ouderrechthoek |
| test_given_assumption_when_drawn_then_rect_has_dasharray | Object met `aanname: ja` | Bijbehorende `rect` heeft `stroke-dasharray`; de andere niet |
| test_given_out_of_scope_type_when_drawn_then_grey_fill | Object gemarkeerd buiten scope | Grijze vulling, geen bedrijfslaagkleur |
| test_given_business_and_application_elements_when_drawn_then_layer_colours_match | Rol (bedrijfslaag) en component (applicatielaag) | Geel voor de bedrijfslaag, blauw voor de applicatielaag |
| test_given_any_rule_when_drawn_then_svg_is_wellformed_and_self_contained | Elke regelsoort | Parsebaar als XML met xmlns; geen `<link>`, `@import`, `url(`, `<script>`, `<foreignObject>` (R3: rendert op GitHub) |
| test_given_long_instance_name_when_drawn_then_text_fits_box | Instantie van 60 tekens | Breedte van de rechthoek is minstens de geschatte tekstbreedte plus de icoonmarge (randgeval kalibratie) |
| test_given_special_characters_when_drawn_then_escaped | Naam met `&`, `<`, `'` | XML parsebaar, tekens ontsnapt |
| test_given_empty_relation_label_when_drawn_then_error | Relatie-item met lege string | Exitcode 1, Nederlandse melding |
| test_given_missing_instance_when_drawn_then_error_names_objecttype | Object zonder instantie | Exitcode 1, melding noemt het objecttype |
| test_given_unknown_kind_when_drawn_then_error | `soort` anders dan ontstaat of stroomt | Exitcode 1 |
| test_given_table_with_n_rules_when_run_then_n_svgs_with_deterministic_names | Tabel met n regels (n uit de fixture) | Precies n bestanden, naam afgeleid van fase, stap en volgnummer |
| test_given_same_input_twice_when_drawn_then_identical_output | Twee runs op dezelfde invoer | Byte-gelijk (randgeval, houdt diffs in PR's schoon) |

**Feature 3, `tests/test_teken_archimate_view.py`**

| Methode | Given | Then |
|---|---|---|
| test_given_bendpoint_with_start_and_end_offsets_when_translated_then_matches_archi | Minimaal `.archimate`-fixture met twee elementen en een bendpoint met `startX`, `startY`, `endX`, `endY`; de verwachte absolute positie is met de hand uit Archi afgelezen | Berekend punt gelijk aan het afgelezen punt (tolerantie 1 px) |
| test_given_bendpoint_when_only_start_offset_used_then_differs | Zelfde fixture | De oude PoC-formule wijkt af (bewijst dat de test de fout dekt) |
| test_given_view_when_read_then_all_children_and_connections_found | Fixture met drie elementen, een genest, twee connecties | Aantallen gelijk aan de fixture |
| test_given_nested_element_when_rendered_then_absolute_position_adds_parent_offset | Kind op (10, 10) in ouder op (100, 100) | `rect` op (110, 110) |
| test_given_element_names_when_rendered_then_every_name_fully_present | Namen uit de fixture, waaronder een die over drie regels breekt | Elke naam is, na samenvoegen van de tekstregels, volledig terug te vinden (R4: geen naam valt weg) |
| test_given_very_long_name_when_rendered_then_no_line_dropped | Naam die meer dan zes regels vraagt | Geen woord ontbreekt (randgeval, de PoC kapt na zes regels) |
| test_given_flow_with_name_when_rendered_then_label_from_flow_name | Flow met naam en een tabel met een andere waarde | Label is de flow-naam; de tabel wordt genegeerd (R9: tabel vervalt) |
| test_given_flow_without_name_and_table_entry_when_rendered_then_label_from_table | Flow zonder naam, tabel heeft het paar | Label uit de tabel |
| test_given_flow_without_name_and_no_table_when_rendered_then_no_label_and_reported | Flow zonder naam, geen tabel | Geen label; het paar staat in de rapportage |
| test_given_label_when_placed_then_on_longest_segment_with_background | Verbinding met drie segmenten van verschillende lengte | Label-`rect` ligt op het middelpunt van het langste segment |
| test_given_view_when_exported_then_stromen_json_has_entry_per_flow | Fixture met n flows | Precies n regels met bron, doel, informatieobject (of leeg) en pijlnummer (bron van het nummer per beslissing M4) |
| test_given_unknown_view_name_when_rendered_then_exit_one_lists_views | Naam die niet bestaat | Exitcode 1, melding somt de beschikbare views op |
| test_given_missing_model_when_rendered_then_exit_two | Niet-bestaand pad | Exitcode 2 |
| test_given_model_when_rendered_then_model_file_unchanged | Hash van het modelbestand voor en na | Gelijk (harde regel 1: alleen lezen) |
| test_given_connection_to_missing_target_when_rendered_then_skipped_with_warning | Connectie naar een id buiten de view | Render slaagt, waarschuwing noemt de id |
| test_given_note_when_rendered_then_text_wrapped_left_aligned | Note met lange inhoud | Meerdere tekstregels, `text-anchor` start |

**Feature 5, `tests/test_genereer_voorbeeld_lr1.py`**

| Methode | Given | Then |
|---|---|---|
| test_given_filled_table_when_generated_then_fase_sections_in_order | Fixture met de fasenlijst uit het schema | Een sectie per fase, in de volgorde van de lijst (aantal uit de fixture, niet hardgecodeerd) |
| test_given_rules_when_generated_then_every_svg_reference_resolves | Regels met gegenereerde SVG's in een tijdelijke map | Elke `![](...svg)` wijst naar een bestaand bestand (validate-docs dekt .svg niet) |
| test_given_scope_when_generated_then_family_tables_cover_all_in_scope_types | Fixture met typen per `kolom` | Verzameling typen in de tabellen gelijk aan de scope-set per familie |
| test_given_type_without_rule_when_generated_then_marked_empty | Een type zonder regel | Rij aanwezig met de lege markering |
| test_given_fase_without_rules_when_generated_then_stub_per_decision | Fase zonder regels | Sectie aanwezig; inhoud van de chips volgens beslissing M9 |
| test_given_chips_when_generated_then_equal_to_objecttypes_of_rules_in_fase | Fase met drie ontstaat-regels en een stroomt-regel | Chips gelijk aan de objecttypen en de stroom van die regels |
| test_given_questions_source_when_generated_then_one_entry_per_question_with_consequence | Vragenbron met n vragen | n items, elk met een consequentie-regel (n uit de bron) |
| test_given_generated_document_when_validate_docs_run_then_zero_problems | Het gegenereerde document | `validate-docs.py` exitcode 0 |
| test_given_document_when_generated_then_no_frontmatter_and_relateert_aan_present | Het gegenereerde document | Begint niet met `---`; bevat de regel "Relateert aan" |
| test_given_document_when_generated_then_no_dash_characters | Het gegenereerde document | Geen gedachtestreepjes (mechanische schrijfstijlcontrole) |
| test_given_same_input_twice_when_generated_then_identical_output | Twee runs | Byte-gelijk |
| test_given_missing_svg_directory_when_generated_then_exit_two | Map ontbreekt | Exitcode 2, Nederlandse melding |

**Feature 6, uitbreiding van `tests/test_publiceer_informatiemodel.py` (bestaat op branch 232)**

| Methode | Given | Then |
|---|---|---|
| test_given_document_and_svgs_when_published_then_land_in_package_dir | Tijdelijke Public-map, document en `img/regels/` | Document en alle SVG's staan in `Informatie-en-gegevensmodellen/` op de afgesproken paden |
| test_given_svg_reference_when_published_then_rewritten_and_resolves | Verwijzing naar `img/regels/x.svg` | Herschreven pad lost op binnen het pakket |
| test_given_reference_outside_link_table_when_published_then_fails_naming_it | Verwijzing die niet in de tabel staat en niet binnen het pakket oplost | Exitcode 1, melding noemt de verwijzing (bestaand gedrag, nu ook voor het nieuwe document) |
| test_given_meta_commit_when_published_then_pinned_links_contain_sha | `--meta-commit` met een sha | Elke gepinde link bevat die sha |
| test_given_release_json_when_published_twice_then_section_added_once | Twee runs | Sectie precies een keer aanwezig (idempotent) |
| test_given_controleer_flag_when_run_then_nothing_written | `--controleer` | Doelmap ongewijzigd (hash van de map) |
| test_given_existing_package_documents_when_published_then_unchanged | Bestaande documenten in de doelmap | Hash voor en na gelijk (feature 6 sluit wijzigingen uit) |
| test_given_missing_document_when_published_then_exit_and_dutch_message | Document ontbreekt in meta | Exitcode 2 |
| test_given_public_dir_missing_when_published_then_exit_two | `--doel` bestaat niet | Exitcode 2 |

### Bevindingen die de maker moet oplossen

Blokkerend

1. **Het plan noemt zijn basis niet.** `informatiemodel.json`, `begrippen.json`, de generator, de map `tests/` en het publiceerscript bestaan alleen op de branches 89 en 232; op `dev` ontbreken bovendien de view "OKx informatiemodel" en `Plaatsingsgroep`. Feature 1 ("hangt af van: geen; werkt op de huidige informatiemodel.json") loopt op 18 september vast als de branch niet klopt. Oplossing: noem in sectie 3 en 5 de basisbranch of de PR's die eerst mergen (89, 232) en in welke volgorde, en zet dat als eerste regel op 18 september.

Moet

2. **R1, schema.** Vul de veldenlijst aan met wat de mock-up en de PoC dragen (bezitter, afnemer, pijlnummer, koppeling-ID, zin; bij een relatie ook het doelobject). Beslis of "geen pijl op de hoofdplaat" een geldige lege regel is (mock-up zegt ja, R1 zegt nee) en of een aanname-objecttype buiten de plaat mag (`Verzoek tot Aanbod` staat in geen enkel model; feature 4 zegt "geen nieuwe objecttypen", de mock-up doet het wel).
3. **R1, relatielabels.** Leg vast hoe de controle werkt bij ongelabelde relaties: `bestaat uit` bestaat op twee relaties, de nesting in de mock-up leunt op Aggregations zonder label, het verbintenispaar heeft label `Minimaal 1` en Opleidingaanbod / Cohort heeft geen relatie. Voorstel: controle op het paar (van, naar) met `bestaat uit` als synoniem voor Aggregation of Composition, en een bevinding in plaats van een fout waar de plaat geen relatie kent.
4. **R2, dekking.** Definieer de bron voor "welk objecttype in welke fase ontstaat" (bijvoorbeeld een verwachting per fase in de lege tabel van feature 1) en kies tussen precies een en minstens een ontstaat-regel per type (Plaatsingsgroep staat in de mock-up in fase 2 en 3).
5. **R4 en feature 3 en 4, pijlnummers.** De bron van `pijlnummer` ontbreekt; de terugval (tabel projectoverzicht, plaat v20260317) hoort bij een andere plaat met andere componenten, en de mock-up nummert anders (8, 10, 13). Voorstel: een deterministische tussenregel in `stromen.json` (nummering van de 33 flows van v1.7) die feature 8 bevestigt of vervangt.
6. **Volgorde feature 1 en 3.** De stroomt-controle van feature 1 heeft `stromen.json` uit feature 3 nodig. Splits feature 1 (schema en ontstaat-controle op 18 september, stroomt-controle na feature 3) of draai de volgorde om.
7. **Feature 8 zonder datum.** R1 (naamcontrole) en feature 4 fase 3 (22 september) gebruiken `Opleiding aanbod verbintenis`, die pas na het opschonen van de dubbele spatie in het model staat. Geef feature 8 een datum voor 22 september of leg vast dat de regeltabel tot die tijd de modelnaam van dat moment gebruikt.
8. **Omvang bijlage.** Doel 3 en de risicotabel zeggen hoogstens zes pagina's, R7 zegt zes slides plus de regels van fase 2 tot 4. Maak een maat leidend en toetsbaar.
9. **Doel 4 zonder eis.** "Het antwoord op wat heet bij u anders kan per regel worden genoteerd" heeft geen eis en geen feature. Neem het op in R7 of R8 met een waarneembaar criterium (per regel een notitieregel of kolom in bijlage en deck).
10. **Doel 1 tegenover feature 4 en 5.** De andere fasen "als samenvatting in chips" op 30 september, terwijl de regels voor fase 1 en 5 tot 8 na 30 september komen. Zeg wat de chips dan tonen (stappen uit de lege tabel, of niets) en pas doel 1 of feature 5 aan.

Kan

11. R4: gebruik de exacte viewnamen "OKx hoofdplaat v1.7<concept>" en "OKx hoofdplaat v1.7<concept> (zonder context applicaties)".
12. R4: maak "geen naam valt weg" concreet (elke elementnaam volledig als tekst aanwezig; de PoC kapt na zes regels).
13. R5: benoem dat `validate-docs.py` geen .svg controleert en dat de generatortest dit dekt, of voeg svg toe aan de regex; noem het veld `kolom` als bron van de families.
14. R3: zeg waar de controle op een onbekend objecttype leeft (controlescript, renderer of beide).
15. R8: verwijs naar de repo-lokale bron van de zeven vragen (`plan.md` sectie 7, a tot g) en zeg wat "consequentie voor het model" betekent voor de drie vragen over patroon, governance en endpoint, die feature 5 buiten scope zet.
16. R9: "de plaatkoppen opschonen" heeft geen criterium.
17. R10 en tijdpad: een reviewdag (23 september) voor meerdere PR's; zeg welke PR's de drie reviews krijgen en of een scriptfeature met tests volstaat.
18. Tijdpad: 19 en 20 september zijn weekend; feature 3 krijgt feitelijk 21 en 22 september, en 22 september draagt ook fase 3 en 4 en feature 5.
19. Milestone: "features 1 tot 7" laat feature 8 en sub-issue 9 buiten de milestone; werkafspraak 4 wil elk issue eronder.
20. R1: `jsonschema` 4.26 staat in de container; zeg of het controlescript die gebruikt (een afhankelijkheid, alleen in de container) of zelf valideert, omdat de tests stdlib-only zijn.
21. Feature 5: noem feature 3 als afhankelijkheid voor "de plaat als beeld", met de JPG als terugval.

Eindoordeel: GEFAALD. Bevinding 1 laat het plan op de eerste werkdag vastlopen; bevindingen 2 tot 10 maken R1, R2, R4 en R7 in hun huidige vorm niet eenduidig toetsbaar en zetten doel 1, 3 en 4 zonder drager. Na verwerking van 1 tot 10 is het plan uitvoerbaar; de kan-punten verbeteren de toetsbaarheid maar houden de uitvoering niet tegen.

### Samenvatting

Voorcontrole groen. Het plan is helder en de features dekken de eisen, maar de basis ontbreekt: de JSON-bronnen, de generator en het publiceerscript leven alleen op de niet-gemergede branches 89 en 232, wat het plan nergens noemt (blokkerend). Negen moet-punten: het schema en de labelcontrole van R1 spreken de mock-up tegen, R2 mist een bron voor fase-toewijzing, de pijlnummers hebben geen bron, feature 1 leunt op feature 3, feature 8 heeft geen datum, en de omvang van de bijlage en de notitieruimte per regel (doel 3 en 4) zijn niet consistent belegd. Per scriptfeature staat een tabel met testgevallen klaar om over te nemen. Eindoordeel: GEFAALD, uitvoerbaar na verwerking van bevinding 1 tot 10.
