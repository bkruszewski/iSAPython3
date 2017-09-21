# w bloku definicji, mogę używać dowolne inne elementy języka

def drukuj_kwadraty():
    liczby = range(8, 15)
    for l in liczby:
        print(l**2)

drukuj_kwadraty()

# ta funkcja nie zwraca żadnej wartości, dlatego x ma wartość None
x = drukuj_kwadraty()
print(x)

print(type(x))
x()

# tutaj kopiuje adres funkcji do innej zmiennej
y = drukuj_kwadraty

# a tutaj wywołuje funkcję poprzez inną zmienną
y()