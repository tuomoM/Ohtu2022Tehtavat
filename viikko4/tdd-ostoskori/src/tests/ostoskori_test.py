import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),3)   
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito",3)
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)
        self.assertEqual(self.kori.tavaroita_korissa(),2)    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_kahden_tuotteen_hintojen_summa(self):
        maito = Tuote("Maito",3)
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)
        self.assertEqual(self.kori.hinta(),7)  
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_on_2_kertaa_tuotteen_hinta(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)
        self.assertEqual(self.kori.hinta(),8)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),1)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(),"Maito")
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta_joilla_samat_nimet(self):
        maito = Tuote("Maito",3)
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(bisse)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(),"Maito" )
        self.assertEqual(ostokset[1].tuotteen_nimi(),"Bisse" )  
    def test_Kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)    
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),1)
    def test_Kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen_jonka_maara_om_2(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)    
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(),2)
    def test_Kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_ostoksen_jolla_sama_nimi_kuin_tuotteella(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)    
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(),"Bisse")
    def test_Jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_näistä_poistetaan_jää_koriin_ostos_jossa_on_tuotetta_1_kpl(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.lisaa_tuote(bisse)
        self.kori.poista_tuote(bisse)    
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(),1)
    def test_Jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_tämän_jälkeen_tyhja(self):
        bisse = Tuote("Bisse",4)
        self.kori.lisaa_tuote(bisse)
        self.kori.poista_tuote(bisse)    
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),0)
    def test_Metodi_tyhjenna_tyhjentää_korin(self):
        bisse = Tuote("Bisse",4)
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(bisse)
        self.kori.poista_tuote(bisse) 
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()),0)