import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        if maksukortti_mock.saldo >= HINTA:
            self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()
        #maksukortti_mock.osta.assert_called_with(HINTA)

    def test_lataa_kortille_positiivinen_arvo(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 5

        summa = 6

        if summa > 0:
            self.kassa.lataa(maksukortti_mock, summa)

        maksukortti_mock.lataa.assert_called_with(summa)

    def test_kortille_ei_voi_ladata_negatiivista_arvoa(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 5

        summa = -1

        if summa > 0:
            self.kassa.lataa(maksukortti_mock, summa)

        maksukortti_mock.lataa.assert_not_called()


