class Samochod(object):
    """Opisuje cechy samochodu"""

    def __init__(self, marka, model):
        """
        Inicjalizuje obiekt wartościami argumentow
        :param marka:
        :param model:
        """
        self.producent = marka
        self.model = model
        self.czy_jedzie = None

    def ruszaj(self):
        """RUsza samochód"""
        if self.czy_jedzie:
            print("Juz jedzie")
        else:
            self.czy_jedzie = True
            print("Ruszył")

    def trab(self, dlugosc):
        """Trąbi"""
        print(dlugosc * "i")

    def wypisz_info(self):
        """WYpisuje informacje o samochodzie"""
        print(f"Samochód: {self.producent} {self.model}")



