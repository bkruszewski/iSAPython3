# drukujemy liczby na ekranie
for liczba in range(30, 43765, 4):
    print(liczba * 343)


wyraz = "konstantynopolitanka"

# bierzemy każdą literę i coś z nią robimy
for litera in wyraz[::-1]:
    print(litera.upper())

# tutaj nic nie robimy z otrzymanym elementem kolekcji
# wykorzystujemy długość kolekcji do wykonania kodu len(wyraz) razy
for litera in wyraz:
   print("Nie robię nic z literą")


imie = "Joanna"
indeks = 0

for litera in imie:
    print(indeks, litera * (indeks + 1))
    indeks += 1

# enumerate daje 2 wartości (indeks, element na tym indeksie)
for (indeks, litera) in enumerate(imie):
    print(indeks, litera * (indeks + 1))








