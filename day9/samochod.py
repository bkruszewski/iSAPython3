class Samochod(object):
    def __init__(self, marka, model):
        self.producent = marka
        self.model = model
        self.czy_jedzie = None

    def ruszaj(self):
        if self.czy_jedzie:
            print("Juz jedzie")
        else:
            self.czy_jedzie = True
            print("Ruszył")

    def trab(self, dlugosc):
        print(dlugosc * "i")

    def wypisz_info(self):
        print(f"Samochód: {self.producent} {self.model}")



