def dodaj(a, b):
    return a + b

def pomnoz(a, b):
    return a * b

# tutaj kilka razy przekazuję wynik działania funkcji jako argument do innej funkcji
print(pomnoz(dodaj(2,3), dodaj(4, 1)))

