class Ksiazka(object):
    def __init__(self, autor, tytul):
        self.autor = autor
        self.tytul = tytul
        self.wypozyczona = None

    def __str__(self):
        return f"Tytuł {self.tytul}, autor: {self.autor}, wypozyczona: {self.wypozyczona}"


    def wypozycz(self):
        self.wypozyczona = True


    def zwroc(self):
        self.wypozyczona = False
