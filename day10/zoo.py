from day10.zwierze import Zwierze
from day10.czlowiek import Czlowiek
from day10.pies import Pies

# tworzymy zwierzaka
zwierz = Zwierze("pimpuś")

zwierz.biega()
zwierz.halasuj()

# czlowiek
czlek = Czlowiek("Alojzy", 34)

czlek.halasuj()
czlek.biega()

psina = Pies("Azor")

psina.halasuj()

czlek.podaj_wiek()