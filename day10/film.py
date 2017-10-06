class Film(object):
    """Film"""

    def __init__(self, tytul: str, cena: float):
        """
        Inicjalizuje nowy film
        :param tytul: str - tytuł filmu
        :param cena: float - cena wypożyczenia za dobę
        """
        self.tytul = tytul
        self.cena = cena
        self.klient = None

    def czy_wypozyczony(self):
        """Czy film jest wypoyczony"""
        if self.klient is None:
            return False
        return True

    def __str__(self):
        """Drukuje informacje o filmie"""
        osoba = "nikogo"

        if self.czy_wypozyczony():
            osoba = self.klient.imie

        return f"{self.tytul} wypozyczony przez {osoba}"
