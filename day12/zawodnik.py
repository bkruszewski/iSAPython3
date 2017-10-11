class Zawodnik(object):

    def __init__(self, imie, dyscyplina):
        self.imie = imie.capitalize()
        self.dyscyplina = dyscyplina
        self.__zarobki = 0
        self.__numer_koszulki = None


    def ustaw_nr_koszulki(self, numer):

        if numer > 0 and numer < 100:
            self.__numer_koszulki = numer
        else:
            print("Podaj prawidłowy numer koszulki!")

    @staticmethod
    def __sprawdz_numer(numer):

        if numer is None:
            return False
        else:
            return True

    def wypisz_numer(self):

        if Zawodnik.__sprawdz_numer(self.__numer_koszulki):
            return self.__numer_koszulki
        else:
            return None

    def ustaw_zarobki(self, kwota):

        try:
            self.__zarobki = int(kwota)
        except:
            print("Zarobki muszą być podane cyfrowo!")
            self.__zarobki = 0



    def wypisz_zarobki(self):
        if self.__zarobki == 0:
            print("Brak informacji o zarobkach")
        elif self.__zarobki > 100000:
            print("dużo")
        elif self.__zarobki > 10000:
            print("może być")
        else:
            print("przeciętnie")