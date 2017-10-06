from day10.czlowiek import Czlowiek
from day10.film import Film


class Klient(Czlowiek):
    """
    Klient wypożyczalni
    """

    def __init__(self, imie, pesel):
        """Tworzy nowego klienta
            (str, int) -> Klient"""
        self.pesel = pesel
        wiek = str(pesel)[0:2]
        Czlowiek.__init__(self, imie, wiek)

    def wypozycz(self, film: Film, dni: int):
        """Wypozycza film

        :param film: Film wypożyczny przez klienta
        :param dni: ilość dni wypożyczenia
        """
        # asercja - sprawdzenie - założenie typu obiektu
        assert type(film) is Film
        film.klient = self

        print(f"Koszt wypożyczenia: {film.cena * dni} zł")
