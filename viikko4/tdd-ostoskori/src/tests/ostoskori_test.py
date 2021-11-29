import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        tavaroita = self.kori.tavaroita_korissa()
        self.assertEqual(tavaroita, 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        tavaroita = self.kori.tavaroita_korissa()
        self.assertEqual(tavaroita, 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        hinta = self.kori.hinta()
        self.assertEqual(hinta, 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        tavaroita = self.kori.tavaroita_korissa()
        self.assertEqual(tavaroita, 2)

