from day10.zwierze import Zwierze

class Czlowiek(Zwierze):
    """Definiuje czlowieka"""

    def __init__(self, imie, wiek):
        """Inicjalizuje obiekt czlowiek"""
        self.imie = imie
        self.wiek = wiek

        # inicjalizujemy Czlowieka jako Zwierze
        Zwierze.__init__(self, imie)


    def biega(self):
        """Biegnie"""
        print(f"Człowiek {self.imie} biega")

    def halasuj(self):
        """Wydaje dźwięki"""
        print(f"{self.imie} mówi \"Dzień dobry\"")

    def podaj_wiek(self):
        """Wypisuje wiek człowieka"""
        print(f"{self.imie} ma {self.wiek} lat")




