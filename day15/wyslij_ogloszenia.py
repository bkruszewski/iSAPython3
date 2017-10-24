from day15 import ogloszenie
from day15.secrets import *
from day11.poczta_zalacznik import Poczta

# wczytujemy ogłoszenia z pliku
ogloszenie.Ogloszenie.wczytaj_ogloszenia("ogloszenia.dat")
ads = ogloszenie.Ogloszenie.ogloszenia

tekst = ""

# tworzymy tekst wiadomości
for ad in ads:
    tekst += ad.opis + " " + ad.link
    tekst += "---------------\n"

# print(tekst)

# tu wysyłamy tekst wiadomości z ogłoszeniami
# parę linijek i wykonane
# bo mamy raz napisane moduły, które potem możemy
# używac w różnych projektach
mailer = Poczta(moj_login, moje_haslo)
mailer.wyslij_wiadomosc([moj_login], "ogloszenia", tekst)


