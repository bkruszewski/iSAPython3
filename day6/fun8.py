# ta zmienna imie jest na poziomie globalnym
imie = "ola"

def duza_litera(imie="ala"):
    # ta zmienna imie jest na poziomie lokalnym
    # imie globalne i imie lokalne to dwa różne obszary pamięci
    # tylko nazywają się tak samo
    # imie lokalne nie istnieje poza definicją funkcji
    imie=imie.capitalize()
    wiek = 23
    return imie

print(duza_litera())

# tutaj istnieje tylko imie globalne
print(imie)
# print(wiek)

