"""Testgevallen voor scripts/teken-informatiemodel-uitsnede.py.

Elke verwachting volgt uit een fixture-informatiemodel in de test; de SVG wordt als XML
geparst en op inhoud en geometrie getoetst, niet op een momentopname. De plaat draagt
zijn eigen namen in `<title>`-elementen, zodat een test kan nakijken welke objecttypen,
kolommen en relaties er werkelijk op staan.
"""

import importlib.util
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

WORTEL = Path(__file__).resolve().parent.parent


def _laad(naam, bestand):
    spec = importlib.util.spec_from_file_location(naam, WORTEL / bestand)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


tu = _laad("teken_informatiemodel_uitsnede", "scripts/teken-informatiemodel-uitsnede.py")
kp = _laad("keur_plaat", "scripts/keur-plaat.py")

SVG = "{http://www.w3.org/2000/svg}"


def model():
    """Een klein informatiemodel in de vorm van informatiemodel.json: twee kolommen, een
    objecttype zonder kolom, twee objecttypen buiten scope en zeven relaties."""
    return {
        "objecttypen": [
            {"naam": "Opleidingsprogramma specificatie", "kolom": "Onderwijsspecificatie",
             "scope": "binnen", "vulkleur": None, "oeapi": ["Programme"]},
            {"naam": "Keuzedeel", "kolom": "Onderwijsspecificatie",
             "scope": "binnen", "vulkleur": None, "oeapi": ["Programme"]},
            {"naam": "Minor", "kolom": "Onderwijsspecificatie",
             "scope": "binnen", "vulkleur": None, "oeapi": ["Programme"]},
            {"naam": "Les specificatie", "kolom": "Onderwijsspecificatie",
             "scope": "buiten", "vulkleur": "#e8e8e8", "oeapi": None},
            {"naam": "Keuzedeel aanbod", "kolom": "Onderwijsaanbod",
             "scope": "binnen", "vulkleur": None, "oeapi": ["ProgrammeOffering"]},
            {"naam": "Minor aanbod", "kolom": "Onderwijsaanbod",
             "scope": "binnen", "vulkleur": None, "oeapi": ["ProgrammeOffering"]},
            # buiten scope met de expliciete standaardgeel: op de grote plaat geel, in de JSON buiten
            {"naam": "Lesgelegenheid", "kolom": "Onderwijsaanbod",
             "scope": "buiten", "vulkleur": "#ffffb5", "oeapi": None},
            {"naam": "Plaatsingsgroep", "kolom": None,
             "scope": "binnen", "vulkleur": None, "oeapi": None},
        ],
        "relaties": [
            {"soort": "Specialization", "van": "Keuzedeel",
             "naar": "Opleidingsprogramma specificatie", "label": None},
            {"soort": "Specialization", "van": "Minor",
             "naar": "Opleidingsprogramma specificatie", "label": None},
            {"soort": "Association", "van": "Keuzedeel", "naar": "Keuzedeel aanbod",
             "label": "Leidt tot"},
            {"soort": "Association", "van": "Minor", "naar": "Minor aanbod", "label": None},
            {"soort": "Association", "van": "Keuzedeel", "naar": "Plaatsingsgroep", "label": None},
            {"soort": "Aggregation", "van": "Opleidingsprogramma specificatie",
             "naar": "Les specificatie", "label": None},
            {"soort": "Access", "van": "Plaatsingsgroep", "naar": "Lesgelegenheid", "label": None},
        ],
    }


def met_lussen(namen, soort="Aggregation"):
    """Het fixture-model met op elk genoemd objecttype een relatie naar zichzelf."""
    mod = model()
    mod["relaties"] += [{"soort": soort, "van": n, "naar": n, "label": None} for n in namen]
    return mod


def selectie(**anders):
    """De proefuitsnede: het generieke type bovenaan, het keuzedeel en de minor eronder."""
    basis = {
        "id": "proef-minor",
        "titel": "Staat de minor naast het keuzedeel?",
        "herkomst": "Reviewvraag Npuls-OKx/Public#123",
        "rij_labels": ["generiek", "bijzonder"],
        "objecten": [
            {"naam": "Opleidingsprogramma specificatie", "rij": 0},
            {"naam": "Minor", "rij": 1, "merk": "nieuw", "waarom": "staat naast het keuzedeel"},
            {"naam": "Keuzedeel", "rij": 1},
            {"naam": "Keuzedeel aanbod", "rij": 1},
            {"naam": "Minor aanbod", "rij": 1, "merk": "nieuw", "waarom": "de uitvoering ervan"},
        ],
    }
    basis.update(anders)
    return basis


# --------------------------------------------------------------- hulpmiddelen --

def plaat(sel=None, mod=None):
    return tu.bouw(mod or model(), sel or selectie())


def groepen(svg, klasse):
    """De groepen met deze klasse, als (titel, element)."""
    uit = []
    for g in ET.fromstring(svg).iter(f"{SVG}g"):
        if g.get("class") != klasse:
            continue
        titel = g.find(f"{SVG}title")
        uit.append(((titel.text if titel is not None else ""), g))
    return uit


def titels(svg, klasse):
    return [t for t, _ in groepen(svg, klasse)]


def doos(element):
    """De eerste rechthoek in een groep: het vak zelf of het vlak van de groepering."""
    r = element.find(f"{SVG}rect")
    return {k: (float(v) if k in ("x", "y", "width", "height") else v) for k, v in r.attrib.items()}


def vak_van(svg, naam):
    for titel, g in groepen(svg, "vak"):
        if titel == naam:
            return g
    raise AssertionError(f"vak {naam!r} staat niet op de plaat")


def teksten(svg):
    return [(t.text or "") for t in ET.fromstring(svg).iter(f"{SVG}text")]


def onder_het_beeld(svg):
    """De tekstregels onder het beeld: de leeswijzer en de legenda, elk op hun eigen hoogte.

    Regels op dezelfde y horen bij dezelfde regel, want een leeswijzerregel staat in drie
    stukken naast elkaar en een legendategel draagt haar tekst naast haar vorm.
    """
    hoogtes = []
    for klasse in ("leeswijzer", "legenda"):
        for _, g in groepen(svg, klasse):
            hoogtes += [round(float(t.get("y"))) for t in g.iter(f"{SVG}text")]
    return sorted(set(hoogtes))


def paden(element):
    return [p.attrib for p in element.iter(f"{SVG}path")]


class UitsnedeTests(unittest.TestCase):

    # --------------------------------------------------------------- selectie --

    def test_given_een_selectie_when_getekend_then_staan_precies_die_objecttypen_op_de_plaat(self):
        svg, _ = plaat()
        self.assertEqual(sorted(titels(svg, "vak")),
                         ["Keuzedeel", "Keuzedeel aanbod", "Minor", "Minor aanbod",
                          "Opleidingsprogramma specificatie"])
        self.assertNotIn("Plaatsingsgroep", titels(svg, "vak"))
        self.assertNotIn("Les specificatie", titels(svg, "vak"))

    def test_given_een_naam_die_het_model_niet_kent_when_getekend_then_stopt_het_met_de_dichtstbijzijnde_naam(self):
        sel = selectie(objecten=[{"naam": "Keuzedeelaanbod"}])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn("Keuzedeelaanbod", str(fout.exception))
        self.assertIn("Keuzedeel aanbod", str(fout.exception))

    def test_given_meer_objecttypen_dan_het_plafond_when_getekend_then_stopt_het_met_een_melding(self):
        mod = model()
        mod["objecttypen"] += [{"naam": f"Proef {i}", "kolom": "Onderwijsaanbod", "scope": "binnen",
                                "vulkleur": None, "oeapi": None} for i in range(tu.MAX_VAKKEN + 1)]
        sel = selectie(objecten=[{"naam": f"Proef {i}"} for i in range(tu.MAX_VAKKEN + 1)])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel, mod)
        self.assertIn("te veel voor een uitsnede", str(fout.exception))

    def test_given_een_merk_buiten_de_woordenlijst_when_getekend_then_stopt_het_met_een_melding(self):
        sel = selectie(objecten=[{"naam": "Minor", "merk": "verbouwd"}])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn("verbouwd", str(fout.exception))

    # ------------------------------------------------------------ groepering --

    def test_given_twee_kolommen_when_getekend_then_krijgt_elke_kolom_een_eigen_groepering(self):
        svg, _ = plaat()
        self.assertEqual(titels(svg, "groepering"), ["Onderwijsspecificatie", "Onderwijsaanbod"])
        self.assertIn("Onderwijsspecificatie", teksten(svg))
        self.assertIn("Onderwijsaanbod", teksten(svg))

    def test_given_de_kolomvolgorde_van_de_grote_plaat_when_getekend_then_staat_specificatie_links_van_aanbod(self):
        svg, _ = plaat()
        x = {t: doos(g)["x"] for t, g in groepen(svg, "groepering")}
        self.assertLess(x["Onderwijsspecificatie"], x["Onderwijsaanbod"])

    def test_given_een_objecttype_in_een_kolom_when_getekend_then_ligt_het_vak_binnen_de_groepering(self):
        svg, _ = plaat()
        groep = {t: doos(g) for t, g in groepen(svg, "groepering")}
        for naam, kolom in (("Keuzedeel", "Onderwijsspecificatie"),
                            ("Minor aanbod", "Onderwijsaanbod")):
            v, k = doos(vak_van(svg, naam)), groep[kolom]
            self.assertGreaterEqual(v["x"], k["x"])
            self.assertLessEqual(v["x"] + v["width"], k["x"] + k["width"])
            self.assertGreaterEqual(v["y"], k["y"])
            self.assertLessEqual(v["y"] + v["height"], k["y"] + k["height"])

    def test_given_een_objecttype_zonder_kolom_when_getekend_then_krijgt_het_een_eigen_groepering(self):
        sel = selectie(objecten=[{"naam": "Keuzedeel", "rij": 0}, {"naam": "Plaatsingsgroep", "rij": 0}])
        svg, _ = plaat(sel)
        self.assertIn(tu.GEEN_KOLOM, titels(svg, "groepering"))

    # ----------------------------------------------------------------- accent --

    def test_given_een_gewijzigd_en_een_contextobject_when_getekend_then_krijgt_alleen_het_gewijzigde_een_accentrand(self):
        svg, _ = plaat()
        randen = {naam: [p for p in paden(vak_van(svg, naam))]
                  for naam in ("Minor", "Keuzedeel")}
        self.assertEqual(randen["Minor"], randen["Keuzedeel"])  # alleen het pictogram is een pad
        accent = {}
        for naam in ("Minor", "Keuzedeel"):
            rects = vak_van(svg, naam).findall(f"{SVG}rect")
            accent[naam] = [r for r in rects if r.get("stroke") == tu.ACCENT]
        self.assertEqual(len(accent["Minor"]), 1)
        self.assertEqual(accent["Keuzedeel"], [])

    def test_given_een_gewijzigd_object_when_getekend_then_staat_het_nummer_met_het_merk_in_het_vak(self):
        svg, _ = plaat()
        inhoud = [(t.text or "") for t in vak_van(svg, "Minor").iter(f"{SVG}text")]
        self.assertIn("1 nieuw", inhoud)
        self.assertNotIn("1 nieuw", [(t.text or "") for t in vak_van(svg, "Keuzedeel").iter(f"{SVG}text")])

    def test_given_een_gewijzigd_object_when_getekend_then_staat_zijn_naam_vet_en_die_van_de_context_niet(self):
        svg, _ = plaat()
        def vet(naam):
            return {t.get("font-weight") for t in vak_van(svg, naam).iter(f"{SVG}text")
                    if (t.text or "") == naam}
        self.assertEqual(vet("Minor"), {"bold"})
        self.assertEqual(vet("Keuzedeel"), {None})

    def test_given_een_gewijzigd_object_met_een_waarom_when_getekend_then_staat_die_regel_in_de_leeswijzer(self):
        svg, _ = plaat()
        regels = [(t.text or "") for _, g in groepen(svg, "leeswijzer")
                  for t in g.iter(f"{SVG}text")]
        self.assertEqual(regels, ["1", "Minor", "staat naast het keuzedeel",
                                  "2", "Minor aanbod", "de uitvoering ervan"])

    def test_given_een_leeswijzerregel_when_getekend_then_staat_zij_in_een_regel_naast_elkaar(self):
        svg, _ = plaat()
        regel = [t for _, g in groepen(svg, "leeswijzer") for t in g.iter(f"{SVG}text")][:3]
        self.assertEqual({t.get("y") for t in regel}, {regel[0].get("y")})
        self.assertEqual([t.get("fill") for t in regel], [tu.ACCENT, tu.INK, tu.MUTED])
        self.assertLess(float(regel[0].get("x")), float(regel[1].get("x")))
        self.assertLess(float(regel[1].get("x")), float(regel[2].get("x")))

    def test_given_twee_leeswijzerregels_when_getekend_then_staan_hun_kolommen_onder_elkaar(self):
        # de leeswijzer leest als een tabelletje: de naam begint op dezelfde x en de reden ook,
        # ook wanneer de ene naam veel korter is dan de andere
        svg, _ = plaat()
        stukken = [t for _, g in groepen(svg, "leeswijzer") for t in g.iter(f"{SVG}text")]
        eerste, tweede = stukken[:3], stukken[3:6]
        self.assertEqual([t.text for t in tweede], ["2", "Minor aanbod", "de uitvoering ervan"])
        for kolom in range(3):
            self.assertEqual(eerste[kolom].get("x"), tweede[kolom].get("x"))

    def test_given_een_leeswijzerregel_when_getekend_then_begint_de_reden_voorbij_de_breedste_naam(self):
        svg, _ = plaat()
        stukken = [t for _, g in groepen(svg, "leeswijzer") for t in g.iter(f"{SVG}text")]
        breedste = max(tu.tw(t.text, tu.LEES_MAAT, True) for t in (stukken[1], stukken[4]))
        self.assertGreaterEqual(float(stukken[2].get("x")) - float(stukken[1].get("x")),
                                breedste + tu.LEES_GOOT)

    def test_given_een_waarom_langer_dan_het_woordbudget_when_getekend_then_weigert_het_script(self):
        lang = " ".join(f"woord{i}" for i in range(tu.MAX_LEESWOORDEN))
        sel = selectie(objecten=[{"naam": "Minor", "rij": 0, "merk": "nieuw", "waarom": lang}],
                       rij_labels=[])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn(str(tu.MAX_LEESWOORDEN + 1), str(fout.exception))
        self.assertIn("woorden", str(fout.exception))

    def test_given_een_waarom_op_het_woordbudget_when_getekend_then_staat_hij_er_gewoon_op(self):
        kort = " ".join(f"woord{i}" for i in range(tu.MAX_LEESWOORDEN - 1))
        sel = selectie(objecten=[{"naam": "Minor", "rij": 0, "merk": "nieuw", "waarom": kort}],
                       rij_labels=[])
        self.assertIn(kort, teksten(plaat(sel)[0]))

    def test_given_een_selectie_met_een_toelichting_when_getekend_then_weigert_het_script(self):
        sel = selectie(toelichting="Beide bijzondere gevallen wijzen naar hetzelfde type.")
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn("toelichting", str(fout.exception))
        self.assertIn("rij_label", str(fout.exception))

    # --------------------------------------------------- de tekst onder het beeld --

    def test_given_een_uitsnede_when_getekend_then_blijft_de_tekst_eronder_binnen_het_budget(self):
        svg, melding = plaat()
        self.assertLessEqual(melding["onderregels"], tu.MAX_ONDERREGELS)
        self.assertEqual(len(onder_het_beeld(svg)), melding["onderregels"])

    def test_given_meer_genummerde_objecten_dan_het_budget_when_getekend_then_weigert_het_script(self):
        mod = model()
        mod["objecttypen"] += [{"naam": f"Proef {i}", "kolom": "Onderwijsaanbod", "scope": "binnen",
                                "vulkleur": None, "oeapi": None}
                               for i in range(tu.MAX_ONDERREGELS + 1)]
        sel = selectie(objecten=[{"naam": f"Proef {i}", "rij": 0, "merk": "nieuw",
                                  "waarom": "een reden"} for i in range(tu.MAX_ONDERREGELS + 1)],
                       rij_labels=[])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel, mod)
        self.assertIn("regels", str(fout.exception))
        self.assertIn(str(tu.MAX_ONDERREGELS), str(fout.exception))

    def test_given_oeapi_aan_when_getekend_then_draagt_alleen_het_gewijzigde_vak_de_oeapi_regel(self):
        svg, _ = plaat(selectie(oeapi=True))
        self.assertIn("OEAPI: Programme",
                      [(t.text or "") for t in vak_van(svg, "Minor").iter(f"{SVG}text")])
        self.assertNotIn("OEAPI: Programme",
                         [(t.text or "") for t in vak_van(svg, "Keuzedeel").iter(f"{SVG}text")])

    # ------------------------------------------------------------------ scope --

    def test_given_een_objecttype_buiten_scope_when_getekend_then_krijgt_het_de_grijze_vulling(self):
        sel = selectie(objecten=[{"naam": "Opleidingsprogramma specificatie", "rij": 0},
                                 {"naam": "Les specificatie", "rij": 0},
                                 {"naam": "Keuzedeel", "rij": 1}])
        svg, _ = plaat(sel)
        self.assertEqual(doos(vak_van(svg, "Les specificatie"))["fill"], tu.GRIJS)
        self.assertEqual(doos(vak_van(svg, "Keuzedeel"))["fill"], tu.BUS)

    def test_given_buiten_scope_met_de_standaardgeel_when_getekend_then_blijft_het_vak_geel(self):
        sel = selectie(objecten=[{"naam": "Keuzedeel", "rij": 0},
                                 {"naam": "Lesgelegenheid", "rij": 0}])
        svg, _ = plaat(sel)
        self.assertEqual(doos(vak_van(svg, "Lesgelegenheid"))["fill"], tu.BUS)

    def test_given_de_legenda_when_er_geen_grijs_vak_op_staat_then_noemt_zij_buiten_scope_niet(self):
        svg, _ = plaat()
        self.assertNotIn("Buiten scope binnen OKx", teksten(svg))
        sel = selectie(objecten=[{"naam": "Opleidingsprogramma specificatie", "rij": 0},
                                 {"naam": "Les specificatie", "rij": 0}])
        self.assertIn("Buiten scope binnen OKx", teksten(plaat(sel)[0]))

    # --------------------------------------------------------------- relaties --

    def test_given_relaties_binnen_en_buiten_de_selectie_when_getekend_then_worden_alleen_de_binnenste_lijnen(self):
        svg, _ = plaat()
        self.assertEqual(sorted(titels(svg, "relatie")), [
            "Association: Keuzedeel naar Keuzedeel aanbod",
            "Specialization: Keuzedeel naar Opleidingsprogramma specificatie",
            "Specialization: Minor naar Opleidingsprogramma specificatie",
        ])
        self.assertNotIn("Plaatsingsgroep", " ".join(titels(svg, "relatie")))

    def test_given_een_relatie_die_niet_haaks_te_lopen_is_when_getekend_then_komt_zij_als_verwijzing_in_het_vak(self):
        svg, melding = plaat()
        # Minor staat niet aan de rand van zijn cel, dus de lijn naar Minor aanbod zou over
        # het vak Keuzedeel lopen; zij wordt een verwijzing in plaats van stil te verdwijnen
        self.assertNotIn("Association: Minor naar Minor aanbod", titels(svg, "relatie"))
        self.assertIn("hangt aan Minor aanbod",
                      [(t.text or "") for t in vak_van(svg, "Minor").iter(f"{SVG}text")])
        self.assertTrue(any("Minor aanbod" in r for r in melding["weggelaten"]))

    def test_given_een_verwijzing_in_een_vak_when_getekend_then_legt_de_legenda_uit_wat_die_regel_is(self):
        uitleg = "regel in een vak: relatie buiten dit raster"
        self.assertIn(uitleg, teksten(plaat()[0]))
        sel = selectie(objecten=[{"naam": "Keuzedeel", "rij": 0}], rij_labels=[])
        self.assertNotIn(uitleg, teksten(plaat(sel)[0]))

    def test_given_een_label_op_een_relatie_when_getekend_then_staat_het_letterlijk_boven_de_lijn(self):
        svg, _ = plaat()
        self.assertIn("Leidt tot", teksten(svg))

    def test_given_een_associatie_zonder_label_when_liggend_getekend_then_draagt_zij_dezelfde_kop_als_staand(self):
        # een liggende associatie zonder label liet haar kop eerder weg; dan las dezelfde soort
        # relatie liggend anders dan staand en beloofde de legenda een pijlpunt die ontbrak
        sel = selectie(objecten=[{"naam": "Keuzedeel", "rij": 0},
                                 {"naam": "Plaatsingsgroep", "rij": 0}], rij_labels=[])
        svg, _ = plaat(sel)
        g = [x for t, x in groepen(svg, "relatie")
             if t == "Association: Keuzedeel naar Plaatsingsgroep"][0]
        koppen = [p for p in paden(g) if p.get("fill") == tu.RELATIE]
        self.assertEqual(len(koppen), 1)
        doel = doos(vak_van(svg, "Plaatsingsgroep"))
        self.assertAlmostEqual(float(koppen[0]["d"][1:].split()[0]), doel["x"] + doel["width"],
                               delta=0.5)

    def test_given_een_specialisatie_when_getekend_then_staat_de_holle_driehoek_bij_het_algemene_type(self):
        svg, _ = plaat()
        algemeen = doos(vak_van(svg, "Opleidingsprogramma specificatie"))
        onderrand = algemeen["y"] + algemeen["height"]
        for titel, g in groepen(svg, "relatie"):
            if not titel.startswith("Specialization"):
                continue
            koppen = [p for p in paden(g) if p.get("fill") == "#ffffff"]
            self.assertEqual(len(koppen), 1, titel)
            punt_y = float(koppen[0]["d"].split()[1].split("l")[0])
            self.assertAlmostEqual(punt_y, onderrand, delta=0.5)

    def test_given_een_aggregatie_when_getekend_then_staat_de_open_ruit_bij_het_geheel(self):
        sel = selectie(objecten=[{"naam": "Opleidingsprogramma specificatie", "rij": 0},
                                 {"naam": "Les specificatie", "rij": 0}])
        svg, _ = plaat(sel)
        geheel = doos(vak_van(svg, "Opleidingsprogramma specificatie"))
        g = [x for t, x in groepen(svg, "relatie") if t.startswith("Aggregation")][0]
        ruit = [p for p in paden(g) if p.get("fill") == "#ffffff"][0]
        self.assertAlmostEqual(float(ruit["d"][1:].split()[0]), geheel["x"] + geheel["width"],
                               delta=0.5)

    def test_given_een_toegangsrelatie_when_getekend_then_loopt_het_been_gestippeld(self):
        sel = selectie(objecten=[{"naam": "Plaatsingsgroep", "rij": 0},
                                 {"naam": "Lesgelegenheid", "rij": 0}])
        svg, _ = plaat(sel)
        g = [x for t, x in groepen(svg, "relatie") if t.startswith("Access")][0]
        self.assertTrue(any(p.get("stroke-dasharray") == tu.GESTIPPELD["Access"] for p in paden(g)))

    def test_given_een_ontbrekende_relatie_when_getekend_then_staat_zij_gestippeld_in_de_accentkleur(self):
        sel = selectie(ontbreekt=[{"van": "Minor aanbod", "naar": "Keuzedeel aanbod",
                                   "soort": "Specialization", "label": "ontbreekt: is een",
                                   "waarom": "het model draagt die specialisatie nog niet"}])
        svg, _ = plaat(sel)
        g = [x for t, x in groepen(svg, "relatie") if "ontbreekt" in t][0]
        self.assertTrue(any(p.get("stroke") == tu.ACCENT and p.get("stroke-dasharray")
                            for p in paden(g)))
        self.assertIn("ontbreekt nog in het model", " ".join(teksten(svg)))

    def test_given_een_ontbrekende_relatie_when_getekend_then_draagt_de_lijn_het_opschrift_en_de_zweeftekst_de_reden(self):
        # de reden kost onder het beeld geen alinea meer: de lijn draagt haar opschrift en de
        # reden staat als zweeftekst bij de relatie
        sel = selectie(ontbreekt=[{"van": "Minor aanbod", "naar": "Keuzedeel aanbod",
                                   "soort": "Specialization", "label": "ontbreekt: is een",
                                   "waarom": "het model draagt die specialisatie nog niet"}])
        svg, _ = plaat(sel)
        self.assertEqual([t for t in titels(svg, "relatie") if "ontbreekt" in t],
                         ["Specialization: Minor aanbod naar Keuzedeel aanbod (ontbreekt nog in "
                          "het model: het model draagt die specialisatie nog niet)"])
        self.assertIn("ontbreekt: is een", teksten(svg))
        self.assertNotIn("het model draagt die specialisatie nog niet", teksten(svg))

    def test_given_een_staande_relatie_met_een_bron_op_de_onderste_rij_when_getekend_then_staat_haar_opschrift_in_de_rijgoot(self):
        # de vakken worden over de relaties heen getekend; een opschrift dat aan de aanhechting
        # van de bron hangt, verdwijnt daarmee onder de vulling van het vak eronder
        sel = selectie(rij_labels=["aanbod", "bijzonder aanbod"],
                       objecten=[{"naam": "Keuzedeel aanbod", "rij": 0},
                                 {"naam": "Minor aanbod", "rij": 1}],
                       ontbreekt=[{"van": "Minor aanbod", "naar": "Keuzedeel aanbod",
                                   "soort": "Specialization", "label": "ontbreekt: is een",
                                   "waarom": "het model draagt die specialisatie nog niet"}])
        svg, _ = plaat(sel)
        opschrift = [float(t.get("y")) for t in ET.fromstring(svg).iter(f"{SVG}text")
                     if (t.text or "") == "ontbreekt: is een"]
        self.assertEqual(len(opschrift), 1)
        boven, onder = doos(vak_van(svg, "Keuzedeel aanbod")), doos(vak_van(svg, "Minor aanbod"))
        self.assertGreater(opschrift[0], boven["y"] + boven["height"])
        self.assertLess(opschrift[0], onder["y"])

    def test_given_een_ontbrekende_relatie_zonder_label_when_getekend_then_weigert_het_script(self):
        sel = selectie(ontbreekt=[{"van": "Minor aanbod", "naar": "Keuzedeel aanbod",
                                   "soort": "Specialization"}])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn("label", str(fout.exception))

    def test_given_een_ontbreekt_die_wel_in_het_model_staat_when_getekend_then_weigert_het_script(self):
        sel = selectie(ontbreekt=[{"van": "Minor", "naar": "Opleidingsprogramma specificatie",
                                   "soort": "Specialization"}])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn("staat wel in het model", str(fout.exception))

    def test_given_verberg_zonder_reden_when_getekend_then_weigert_het_script(self):
        sel = selectie(verberg=[{"van": "Keuzedeel", "naar": "Keuzedeel aanbod"}])
        with self.assertRaises(tu.Fout) as fout:
            plaat(sel)
        self.assertIn("reden", str(fout.exception))

    def test_given_verberg_met_een_reden_when_getekend_then_valt_die_relatie_weg(self):
        sel = selectie(verberg=[{"van": "Keuzedeel", "naar": "Keuzedeel aanbod",
                                 "reden": "hoort bij de vraag over aanbod"}])
        svg, _ = plaat(sel)
        self.assertNotIn("Association: Keuzedeel naar Keuzedeel aanbod", titels(svg, "relatie"))

    # -------------------------------------------------------------- geometrie --

    def test_given_geen_rijen_in_de_selectie_when_getekend_then_staat_het_algemene_type_boven_zijn_specialisaties(self):
        sel = selectie(objecten=["Opleidingsprogramma specificatie", "Keuzedeel", "Minor"],
                       rij_labels=[])
        svg, _ = plaat(sel)
        algemeen = doos(vak_van(svg, "Opleidingsprogramma specificatie"))
        for naam in ("Keuzedeel", "Minor"):
            self.assertGreater(doos(vak_van(svg, naam))["y"], algemeen["y"])

    def test_given_twee_objecttypen_in_dezelfde_rij_en_kolom_when_getekend_then_staan_zij_naast_elkaar(self):
        svg, _ = plaat()
        minor, keuzedeel = doos(vak_van(svg, "Minor")), doos(vak_van(svg, "Keuzedeel"))
        self.assertEqual(minor["y"], keuzedeel["y"])
        self.assertGreaterEqual(keuzedeel["x"], minor["x"] + minor["width"])

    def test_given_een_getekende_uitsnede_when_gekeurd_then_loopt_elk_segment_haaks_en_kruist_er_niets(self):
        svg, melding = plaat(selectie(oeapi=True))
        self.assertEqual(melding["kruisingen"], 0)
        with tempfile.TemporaryDirectory() as map:
            pad = Path(map) / "uitsnede.svg"
            pad.write_text(svg, encoding="utf-8")
            bevindingen, maat = kp.keur(pad, max_kruisingen=0)
        self.assertEqual([str(b) for b in bevindingen], [])
        self.assertEqual(maat["kruisingen"], 0)

    def test_given_een_uitsnede_met_een_omweg_when_gekeurd_then_blijft_zij_zonder_bevindingen(self):
        # vier specialisaties naar een vak: de aanhechtingen worden verdeeld, dus er lopen
        # omwegen in de rijgoot; die mogen elkaar niet kruisen
        mod = model()
        mod["objecttypen"] += [{"naam": f"Soort {i}", "kolom": "Onderwijsspecificatie",
                                "scope": "binnen", "vulkleur": None, "oeapi": None}
                               for i in range(4)]
        mod["relaties"] += [{"soort": "Specialization", "van": f"Soort {i}",
                             "naar": "Opleidingsprogramma specificatie", "label": None}
                            for i in range(4)]
        sel = selectie(objecten=[{"naam": "Opleidingsprogramma specificatie", "rij": 0}]
                       + [{"naam": f"Soort {i}", "rij": 1} for i in range(4)], rij_labels=[])
        svg, melding = plaat(sel, mod)
        self.assertEqual(melding["verticaal"], 4)
        self.assertEqual(melding["kruisingen"], 0)
        with tempfile.TemporaryDirectory() as map:
            pad = Path(map) / "omweg.svg"
            pad.write_text(svg, encoding="utf-8")
            bevindingen, _ = kp.keur(pad, max_kruisingen=0)
        self.assertEqual([str(b) for b in bevindingen], [])

    def test_given_een_lang_label_op_een_verticale_relatie_in_de_rechtste_kolom_when_getekend_then_blijft_het_binnen_het_doek(self):
        # het label van een verticale relatie staat naast de lijn en steekt buiten het raster
        # uit; in de rechtste kolom schoof het voorheen voorbij de rand van het doek
        mod = model()
        mod["objecttypen"].append({"naam": "Minor aanbod verbintenis", "kolom": "Onderwijsaanbod",
                                   "scope": "binnen", "vulkleur": None, "oeapi": None})
        mod["relaties"].append({"soort": "Association", "van": "Minor aanbod",
                                "naar": "Minor aanbod verbintenis",
                                "label": "Groepeert Studenten op toepasbare"})
        sel = selectie(objecten=[{"naam": "Minor aanbod", "rij": 0},
                                 {"naam": "Minor aanbod verbintenis", "rij": 1}],
                       rij_labels=[], ontbreekt=[])
        svg, melding = plaat(sel, mod)
        self.assertEqual(melding["verticaal"], 1)
        with tempfile.TemporaryDirectory() as map:
            pad = Path(map) / "label.svg"
            pad.write_text(svg, encoding="utf-8")
            bevindingen, _ = kp.keur(pad, max_kruisingen=0)
        self.assertEqual([str(b) for b in bevindingen], [])

    def test_given_een_herkomst_breder_dan_het_raster_when_getekend_then_blijft_zij_binnen_het_doek(self):
        lang = ("Reviewvraag Npuls-OKx/Public#114 van een inbrenger uit de leveranciersreview, "
                "werkbrief Npuls-OKx/meta#332")
        sel = selectie(herkomst=lang, objecten=[{"naam": "Keuzedeel", "rij": 0}], rij_labels=[])
        svg, melding = plaat(sel)
        self.assertGreaterEqual(melding["breed"],
                                round(tu.tw(lang, tu.HERKOMST_MAAT) + 2 * tu.DOEK_MARGE))
        with tempfile.TemporaryDirectory() as map:
            pad = Path(map) / "herkomst.svg"
            pad.write_text(svg, encoding="utf-8")
            bevindingen, _ = kp.keur(pad, max_kruisingen=0)
        self.assertEqual([str(b) for b in bevindingen], [])

    # ------------------------------------------------ de relatie op zichzelf --

    def test_given_een_relatie_op_zichzelf_when_getekend_then_wordt_zij_een_lus_en_geen_regel_in_het_vak(self):
        mod = met_lussen(["Keuzedeel"])
        svg, melding = plaat(selectie(), mod)
        self.assertEqual(melding["lussen"], 1)
        self.assertEqual(melding["zelf"], ["Keuzedeel: Aggregation op zichzelf"])
        self.assertIn("Aggregation: Keuzedeel naar zichzelf", titels(svg, "relatie"))
        inhoud = [(t.text or "") for t in vak_van(svg, "Keuzedeel").iter(f"{SVG}text")]
        self.assertNotIn("bevat zichzelf", inhoud)
        self.assertEqual(inhoud, ["Keuzedeel"])

    def test_given_een_aggregatie_op_zichzelf_when_getekend_then_draagt_de_lus_de_open_ruit(self):
        svg, _ = plaat(selectie(), met_lussen(["Keuzedeel"]))
        g = [x for t, x in groepen(svg, "relatie") if "zichzelf" in t][0]
        been = [p for p in paden(g) if p.get("fill") == "none"]
        ruit = [p for p in paden(g) if p.get("fill") == "#ffffff"]
        self.assertEqual(len(been), 1)
        self.assertEqual(len(ruit), 1)
        self.assertEqual(been[0]["d"].count("H"), 2)   # heen, omlaag, terug: een haakse lus
        self.assertEqual(been[0]["d"].count("V"), 1)
        vak = doos(vak_van(svg, "Keuzedeel"))
        self.assertAlmostEqual(float(ruit[0]["d"][1:].split()[0]), vak["x"] + vak["width"],
                               delta=0.5)

    def test_given_een_lus_when_getekend_then_ligt_zij_binnen_het_vak_waar_geen_lijn_komt(self):
        svg, _ = plaat(selectie(), met_lussen(["Keuzedeel"]))
        g = [x for t, x in groepen(svg, "relatie") if "zichzelf" in t][0]
        been = [p for p in paden(g) if p.get("fill") == "none"][0]
        punten = kp.polylijn(been["d"])
        vak = doos(vak_van(svg, "Keuzedeel"))
        for x, y in punten:
            self.assertGreaterEqual(x, vak["x"])
            self.assertLessEqual(x, vak["x"] + vak["width"])
            self.assertGreaterEqual(y, vak["y"])
            self.assertLessEqual(y, vak["y"] + vak["height"])

    def test_given_drie_vakken_naast_elkaar_met_een_lus_when_gekeurd_then_raken_de_lussen_elkaar_niet(self):
        mod = met_lussen(["Keuzedeel", "Minor", "Minor aanbod"])
        svg, melding = plaat(selectie(), mod)
        self.assertEqual(melding["lussen"], 3)
        self.assertEqual(melding["kruisingen"], 0)
        with tempfile.TemporaryDirectory() as map:
            pad = Path(map) / "lussen.svg"
            pad.write_text(svg, encoding="utf-8")
            bevindingen, maat = kp.keur(pad, max_kruisingen=0)
        self.assertEqual([str(b) for b in bevindingen], [])
        self.assertEqual(maat["kruisingen"], 0)

    def test_given_twee_lussen_op_een_vak_when_getekend_then_liggen_zij_onder_elkaar_in_het_vak(self):
        mod = met_lussen(["Keuzedeel"])
        mod["relaties"].append({"soort": "Association", "van": "Keuzedeel", "naar": "Keuzedeel",
                                "label": None})
        svg, melding = plaat(selectie(), mod)
        self.assertEqual(melding["lussen"], 2)
        banden = []
        for titel, g in groepen(svg, "relatie"):
            if "zichzelf" not in titel:
                continue
            punten = kp.polylijn([p for p in paden(g) if p.get("fill") == "none"][0]["d"])
            banden.append((min(p[1] for p in punten), max(p[1] for p in punten)))
        banden.sort()
        self.assertLess(banden[0][1], banden[1][0])
        self.assertEqual(melding["kruisingen"], 0)

    def test_given_een_lus_op_de_plaat_when_getekend_then_legt_de_legenda_de_vorm_uit(self):
        svg, _ = plaat(selectie(), met_lussen(["Keuzedeel"]))
        self.assertIn(tu.LUS_VORMNAAM["Aggregation"], teksten(svg))
        self.assertNotIn(tu.LUS_VORMNAAM["Aggregation"], teksten(plaat()[0]))

    def test_given_een_lange_objecttypenaam_when_getekend_then_breekt_hij_af_zonder_woord_te_splitsen(self):
        naam = "Werkveld of beroepenveld of deelnemer competentie"
        mod = model()
        mod["objecttypen"].append({"naam": naam, "kolom": "Onderwijsspecificatie",
                                   "scope": "binnen", "vulkleur": None, "oeapi": None})
        svg, _ = plaat(selectie(objecten=[{"naam": naam, "rij": 0}], rij_labels=[]), mod)
        regels = [(t.text or "") for t in vak_van(svg, naam).iter(f"{SVG}text")]
        self.assertGreater(len(regels), 1)
        self.assertEqual(" ".join(regels), naam)

    # ---------------------------------------------------------------- uitvoer --

    def test_given_een_uitsnede_when_weggeschreven_then_heet_het_bestand_naar_de_uitsnede(self):
        with tempfile.TemporaryDirectory() as map:
            doel, melding = tu.teken(model(), selectie(), Path(map))
            self.assertEqual(doel.name, "proef-minor.svg")
            self.assertEqual(melding["vakken"], 5)
            self.assertEqual(melding["kolommen"], 2)
            self.assertEqual(melding["rijen"], 2)
            self.assertTrue(doel.read_text(encoding="utf-8").startswith("<svg"))

    def test_given_de_titel_en_de_herkomst_when_getekend_then_staan_zij_boven_het_beeld(self):
        svg, _ = plaat()
        regels = teksten(svg)
        self.assertEqual(regels[0], "Staat de minor naast het keuzedeel?")
        self.assertEqual(regels[1], "Reviewvraag Npuls-OKx/Public#123")

    def test_given_de_plaat_when_getekend_then_draagt_zij_geen_externe_fonts_of_scripts(self):
        svg, _ = plaat()
        for verboden in ("<script", "@import", "xlink:href", "<image"):
            self.assertNotIn(verboden, svg)


if __name__ == "__main__":
    unittest.main()
