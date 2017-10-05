from day10.czlowiek import Czlowiek


class Student(Czlowiek):
    def __init__(self, imie, wiek, indeks):
        self.indeks = indeks

        Czlowiek.__init__(self, imie, wiek)

    def biega(self):
        print(f"Student {self.imie} biega po wpisy")

    def halasuj(self):
        print("Pan da trzy!")
