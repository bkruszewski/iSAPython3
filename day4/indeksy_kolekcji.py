# czasem chcemy wiedziec, z którym elemeentem mamy doczynienia
# chcemy znać jego indeks

imie = "Hermenegilda"

# tworzymy licznik zawierający indeks aktualnego elementu
indeks = 0

for c in imie:
    print(indeks, c)
    # musimy pamiętać o aktualizacji indeksu!
    indeks += 1

# enumerate zwraca dwie wartości:
# indeks elementu w kolekcji oraz
# wartość elementu pod tym indeksem
for (indeks, litera) in enumerate(imie):
    print(indeks, litera)