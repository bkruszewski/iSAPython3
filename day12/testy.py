from unittest import TestCase
from day12.zawodnik import Zawodnik

# testy piszemy w klasie testów - dziedziczymy z TestCase
class TestZawodnik(TestCase):

    def setUp(self):
        """Ta metoda jest wykonywana przed każdym testem.
        W niej najlepiej inicjalizować rzeczy potrzebne,
        które będą wykorzystane w wielu testach

        Każdy z testów otrzyma 'świeżr' obiekty"""
        self.zawodnik = Zawodnik("jan", "piłka")


    # to jest metoda testowa - jeden test
    # nazwa zaczyna się od test_ następnie najlepiej podać nazwę testowanej metody
    def test_init(self):

        self.assertEqual("Jan", self.zawodnik.imie)

    def test_ustaw_nr_koszulki(self):

        self.zawodnik.ustaw_nr_koszulki(23)

        faktyczny_numer = self.zawodnik.wypisz_numer()

        self.assertEqual(23, faktyczny_numer)

    def test_ustaw_nieprawidlowy_nr_koszulki(self):

        self.zawodnik.ustaw_nr_koszulki(200)
        faktyczny_numer = self.zawodnik.wypisz_numer()

        self.assertIsNone(faktyczny_numer)


