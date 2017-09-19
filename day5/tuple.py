# tuple - typ niezmienny
# raz utworzonego nie można zmienić
t1 = (1,2,3,4,5)

# błąd bo nie można zmieniać tupli
# t1[2] = "trzy"

# można indeksować i slice'ować
print(t1[3])
print(t1[::-1])


# jednoelementowy tuple, pamiętać o przecinku na końcu
tupelek = 1,
print(type(tupelek))

# pamiętać o przecinku anwet z nawiasami!
tupelek2 = (3,)

tupelek3 = ("jeden", "dwadzieścia", 345, ["ala"], "jeden")

# tuple zawiera tylko 2 metody
ile_jedynek = tupelek3.count("jeden")
print(ile_jedynek)
indeks_elementu = tupelek3.index("dwadzieścia")
print(indeks_elementu)

# rozpakowanie tupli - czyli przypisanie wartości elementów
# do zmiennych

a,b,c,d,e = t1

print(a, b, c, d, e)


