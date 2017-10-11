from day11.animal import Animal

class Horse(Animal):
    def __init__(self, imie):

        super().__init__(imie)
        # Animal.__init__(self, imie)

    def say(self):
        print(f"{self.name} rży")

    def jump(self):
        print(f"Koń {self.name} skacze!")


