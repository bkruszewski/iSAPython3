from day8.secrets import *
from day11.poczta import Poczta

poczta = Poczta(login, haslo)

pliki = [r"/home/trener/PycharmProjects/iSAPython3/kotek.py"]

poczta.wyslij_wiadomosc(["lalpololo@gmail.com"], "test", "hello", pliki)


