from day9.ksiazka import Ksiazka

# tworzymy obiekty typu Ksiazka
# inaczej - tworzymy instancje klasy Ksiazka
ks1 = Ksiazka("Brzechwa", "Lokomotywa")
ks2 = Ksiazka("Forsyth", "Akta Odessy")

ks1.wypozycz()

print(f"ksiązka {ks1.tytul} wypozyczona? {ks1.wypozyczona}")
print(f"ksiązka {ks2.tytul} wypozyczona? {ks2.wypozyczona}")

print()
print(ks1)
print(ks2)
