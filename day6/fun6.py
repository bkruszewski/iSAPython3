def drukuj_kwadrat(x):
    # ta funkcja tylko drukuje na ekranie
    print(x**2)

# drukuj_kwadrat(4)

def oblicz_kwadrat(x):
    # ta funkcja za pomocą słowa return zwraca informacje
    return x**2

# aby użyć zwróconą informację zapisuję do zmiennej
y = oblicz_kwadrat(3)
print(y)

z = y **3
print(z)

print(y % 4)

# mogę też zwracaną wartość przekazać od razu jako argument
# innej funkcji
print(oblicz_kwadrat(4))





