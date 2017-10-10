from day11.animal import Animal

class Donkey(Animal):
    def __init__(self, imie):
        Animal.__init__(self, imie)

    def say(self):
        print("iiiiiiiihaaaa jestem osioł")

    def run(self):
        print("Jestem osioł, nie biegam!!!")
