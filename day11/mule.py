from day11.horse import Horse
from day11.donkey import Donkey
from day11.animal import Animal

class Mule(Donkey, Horse):
    def say(self):
        print("Muł mówi coś takiego:", end="")
        #super().say()
        Animal.say(self)

