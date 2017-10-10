from day8.secrets import *
from day11.poczta import Poczta

poczta = Poczta(login, haslo)

poczta.wyslij_wiadomosc(["lalpololo@gmail.com"], "test", "hello")


