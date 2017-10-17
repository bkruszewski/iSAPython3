from unittest import TestCase
from day13.kalk import *
from day13.helpers import *

class KalkTesty(TestCase):

    def setUp(self):
        self.a = 10
        self.b = 2

    def test_dodaj(self):
        # arrange
        suma_oczekiwana = self.a + self.b

        # act
        suma_rzeczywista = dodaj(self.a, self.b)

        # assert
        self.assertEqual(suma_oczekiwana, suma_rzeczywista)

    def test_pomnoz(self):
        il_oczekiwany = self.a * self.b

        il_rzeczywisty = pomnoz(self.a, self.b)

        self.assertEqual(il_oczekiwany, il_rzeczywisty)

    def test_odejmij(self):
        wart_oczekiwana = str(self.a - self.b)
        wart_oczekiwana += '\n'
        wart_rzeczywista = get_print_output(odejmij, self.a, self.b)

        self.assertEqual(wart_oczekiwana, wart_rzeczywista)