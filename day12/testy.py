from unittest import TestCase
from day12.zawodnik import Zawodnik

class TestZawodnik(TestCase):

    def setUp(self):
        self.zawodnik = Zawodnik("jan", "piłka")


    def test_init(self):

        self.assertEquals("Jan", self.zawodnik.imie)

    def test_ustaw_nr_koszulki(self):

        self.zawodnik.ustaw_nr_koszulki(23)

        faktyczny_numer = self.zawodnik.wypisz_numer()

        self.assertEquals(23, faktyczny_numer)

    def test_ustaw_nieprawidlowy_nr_koszulki(self):

        self.zawodnik.ustaw_nr_koszulki(200)
        faktyczny_numer = self.zawodnik.wypisz_numer()

        self.assertIsNone(faktyczny_numer)


