class Animal(object):
    def __init__(self, imie):
        self.name = imie

    def say(self):
        print(f"Zwierzak {self.name} nie mówi")

    def capitalize_name(self):
        self.name = self.name.capitalize()

        