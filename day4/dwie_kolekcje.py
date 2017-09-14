kolekcja_a = "0123456789012345"
kolekcja_b = "Ala ma kota"

# wydrukować elementy z dwóch kolekcji z tych samych indeksów

indeks = 0
for el_a in kolekcja_a:
    # uwaga! problem gdy kolekcja a jest dłuższa niż kolekcja b
    # przy probie pobrania elementu z indeksu, którego nie ma w
    # kolekcji b będzie error!!!
    print(el_a, kolekcja_b[indeks])
    indeks += 1

# zip() daje nam zestaw elementów z tych samych pozycji
# jeśli kolekcje są różnej długości to długość krótszej
# będzie wzięta pod uwagę
for (el_a, el_b) in zip(kolekcja_a, kolekcja_b) :
    print(el_a, el_b)
