#slicowanie
slowo = "czarymary"

# możemy indeksować od tyłu
ostatnia = slowo[-1]
print(ostatnia)

# przedziały - slicowanie
# od : do(bez tego indeksu) : krok
print(slowo[2:5])
print(slowo[:5])
print(slowo[2:])

# od 2go indeksu do 6go, co 3ci element
print(slowo[2:7:3])

# ord podaje nam numer znaku w tabeli utf
kod = ord("D")
print(kod)

# chr zwraca znak o danym kodzie
nowa_literka = chr(100)
print(nowa_literka)

# możemy manipulować kodami i znakami i tworzyć nowe
print(chr(kod + 4))
