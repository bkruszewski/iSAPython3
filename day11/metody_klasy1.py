class Pracownik(object):

    ilosc_pracownikow = 0
    roczna_podw = 5

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None

        Pracownik.ilosc_pracownikow += 1

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (procent/100)


    @classmethod
    def ustaw_roczna_podwyzka(cls, wartosc):
        cls.roczna_podw = wartosc


    @classmethod
    def pracownik_z_pensja(cls, imie, stanowisko, pensja):

        prac = Pracownik(imie, stanowisko)
        prac.wynagrodzenie = pensja

        return prac

    @staticmethod
    def sprawdz_pesel(pesel):

        if len(str(pesel)) == 11:
            return True
        else:
            return False



    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return f"{self.imie} - {self.stanowisko} ma pensje {self.wynagrodzenie}"

