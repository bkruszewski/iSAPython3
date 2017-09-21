imie = "jola"

def drukuj_imiona(imie_2):
    # tu wskazujemy, że chcemy używać zmiennej imie z poziomu globalnego
    global imie
    # nonlocal
    # tutaj nadpisujemy zmienną imię na poziomie globalnym!
    imie = "ania".capitalize()
    imie_2 = imie_2.capitalize()

    print(imie, imie_2)

drukuj_imiona("gosia")
# zmienna imie została zmieniona wewnątrz funkcji drukuj_imiona!
print(imie)
