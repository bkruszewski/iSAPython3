class Przedmiot(object):
    """
    Definiuje zachowania i włąściwości przedmiotów w sklepie
    """

    def __init__(self, nazwa, cena, waga):
        self.nazwa = nazwa
        self.cena = cena
        self.waga = waga

    def __str__(self):
        return f"{self.nazwa} - cena: {self.cena}EUR/szt, " \
               f"waga jedn. kg: {self.waga}"


    def __add__(self, other):
        wartosc = self.cena + other.cena
        waga = self.waga + other.waga

        return (wartosc, waga)

    def __lt__(self, other):
        """Informuje czy przedmiot jest lżejszy od drugiego przedmiotu"""
        if self.waga < other.waga:
            return True
        return False

    def __del__(self):
        print(f"Przedmiot {self.nazwa} został usunięty")
        del self


