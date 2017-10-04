class Ksiazka(object):
    """Opisuje zachowania i własciwości książki"""

    def __init__(self, autor, tytul):
        """
        Inicjalizuje obiekt Książka podanymi argumentami
        :param autor: str - Autor książki
        :param tytul: str - Tytuł książki
        """
        self.autor = autor
        self.tytul = tytul
        self.wypozyczona = None

    def __str__(self):
        """Zwraca sformatowany str, który będzie wypisany na ekranie po użyciu
            print(obiekt_ksiazka)"""
        return f"Tytuł {self.tytul}, autor: {self.autor}, wypozyczona: {self.wypozyczona}"

    def wypozycz(self):
        """Zmienia stan książki na wypożyczona"""
        self.wypozyczona = True

    def zwroc(self):
        """Zmienia stan książki na dostępna"""
        self.wypozyczona = False

    def czy_dostepna(self):
        """Wypisuje informacje czy książka jest wypożyczona czy dostępna"""

        stan = "dostępna"
        if self.wypozyczona:
            stan = "wypożyczona"

        print(f"Książka {self.tytul} jest {stan}.")
