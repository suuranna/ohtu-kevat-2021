from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        self.koko_hinta = 0
        self.maara = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self._ostokset:
            maara = maara + ostos._lukumaara
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset:
            hinta = hinta + ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos1 = Ostos(lisattava)
        for ostos in self._ostokset:
            if ostos.tuote.nimi == ostos1.tuote.nimi and ostos.tuote.hinta == ostos1.tuote.hinta:
                ostos.muuta_lukumaaraa(1)
                return
        self._ostokset.append(ostos1)

    def poista_tuote(self, poistettava: Tuote):
        ostos2 = Ostos(poistettava)
        for ostos in self._ostokset:
            if ostos2.tuotteen_nimi() == ostos.tuotteen_nimi():
                if ostos.lukumaara() == 1:
                    self._ostokset.remove(ostos)
                else:
                    ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self._ostokset.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
