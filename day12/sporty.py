from day12.zawodnik import Zawodnik

z1 = Zawodnik("Lewy", "noga")

print(z1.imie)
print(z1.dyscyplina)

z1.ustaw_nr_koszulki(123)

z1.wypisz_numer()

z1.ustaw_zarobki("milion")

z1.wypisz_zarobki()
