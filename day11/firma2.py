from day11.metody_klasy1 import Pracownik

prac1 = Pracownik("John Turturo", "aktor")
prac2 = Pracownik("John Travolta", "stara gwiazda")

print(prac1)
print(prac2)

prac2.ustaw_pensje(10500)
print(prac2)

prac2.daj_podwyzke(5)
print(prac2)

prac1.roczna_podw = 7

Pracownik.ustaw_roczna_podwyzka(12)

print(prac1.roczna_podw)
print(prac2.roczna_podw)

prac3 = Pracownik.pracownik_z_pensja("Jan", "kamerzysta", 3000)

print(type(prac3))

poprawny = Pracownik.sprawdz_pesel(12345675456)
print(poprawny)