# print("Hello world!")

# to jest komentarz on nie zostanie wypisany

# to jest moja pierwsza zmienna
# znak = to znak przypisania
# zawsze najpierw wykona się to co po prawej stronie
# wynik prawej strony zostanie przypisany do zmiennej
imie = "Ola"

print(imie)
print(3*imie)
print(3 * "Ala")
nazwisko = "kowalska"

# formatowanie stringa
print(imie + " " + nazwisko.capitalize())
print("{} {}".format(imie, nazwisko.capitalize()))
print("{0} {0}".format(imie, nazwisko))

# stringi są typami nie zmiennymi
# używając funkcje na stringu tworzymy nową wersję stringa
nazwisko_duze = nazwisko.capitalize()

print("Nazwisko z dużej: ", nazwisko_duze)
print("Nazwisko oryg: ", nazwisko)