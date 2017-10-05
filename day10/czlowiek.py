from day10.zwierze import Zwierze

class Czlowiek(Zwierze):

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

        Zwierze.__init__(self, imie)


    def biega(self):
        print(f"Człowiek {self.imie} biega")

    def halasuj(self):
        print(f"{self.imie} mówi \"Dzień dobry\"")

    def podaj_wiek(self):
        print(f"{self.imie} ma {self.wiek} lat")




