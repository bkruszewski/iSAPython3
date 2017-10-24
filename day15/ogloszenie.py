class Ogloszenie(object):
    """Klasa reprezentująca ogłoszenie w otodom"""

    # lista zawierajaca instancje ogłoszeń
    ogloszenia = []

    def __init__(self, opis, link):
        """Inicjalizuje ogłoszenie
        opis: string
        link: string
        """
        self.opis = self.__formatuj_opis(opis)
        self.link = link
        # każda instancja jest dodawana do listy
        Ogloszenie.ogloszenia.append(self)

    def __formatuj_opis(self, opis):
        """Formatujemy opis przechwyconego ogłoszenia"""
        o = str(opis).split('\n')
        return ' '.join(o).strip()

    @classmethod
    def zapisz_ogloszenia(cls, nazwa_pliku):
        """Zapisuje ogłoszenia do pliku
        nazwa_pliku: string"""
        import pickle
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(cls.ogloszenia, plik)

    @classmethod
    def wczytaj_ogloszenia(cls, nazwa_pliku):
        """Wczytuje ogłoszenie z pliku
        nazwa_pliku: string
        """
        import pickle
        with open(nazwa_pliku, 'rb') as plik:
            cls.ogloszenia = pickle.load(plik, encoding="utf-8")

    def __str__(self):
        """Własny format print()"""
        return "{} : {}".format(self.opis, self.link)

