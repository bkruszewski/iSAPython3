# ta funkcja przyjmuje 2 argumenty
def drukuj_kwadraty(od, do):
    for l in range(od, do + 1):
        print(l**2)

# oba argumenty muszą być podane przy wywołaniu
drukuj_kwadraty(0, 5)
drukuj_kwadraty(6, 10)
drukuj_kwadraty(3, 12)

# nie mogę podać za mało
drukuj_kwadraty(7)
# nie mogę podać za dużo
drukuj_kwadraty(2,5,6)
