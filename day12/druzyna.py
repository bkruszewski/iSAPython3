class Druzyna(object):

    def __init__(self, nazwa, trener):
        self.nazwa = nazwa
        self.trener = trener
        self.__budzet = None
        self.__transfery = []

    # getter
    @property
    def budzet(self):
        if self.__budzet is None:
            return "Brak budżetu"
        else:
            return self.__budzet


    @property
    def transfery(self):
        if len(self.__transfery) == 0:
            return "brak transferów"
        else:
            return self.__transfery

