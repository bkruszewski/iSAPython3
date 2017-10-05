class Film(object):

    def __init__(self, tytul, cena):
        self.tytul = tytul
        self.cena = cena
        self.klient = None


    def czy_wypozyczony(self):
        if self.klient is None:
            return False
        return True


    def __str__(self):
        osoba = "nikogo"

        if self.czy_wypozyczony():
            osoba = self.klient.imie

        return f"{self.tytul} wypozyczony przez {osoba}"