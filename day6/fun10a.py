# jeśli chcę nową listę tu użyję typu None
def dodaj_imie(imie, imiona=None):
    if imiona == None:
        imiona = []
    imiona.append(imie)
    return imiona

baza = dodaj_imie("Marta")
dodaj_imie("Marek", baza)
print(baza)

ang = dodaj_imie("John")
print(ang)
# działa - anglik jest w nowej liście


# zwracamy kilka wartości za jednym razem
# tzn, zwracamy jednego tupla z kilkoma obiektami
def policz(a, b):
    return (a**2, b**3)

x, y = policz(3, 4)

print(x)
print(y)
