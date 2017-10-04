from day9.samochod import Samochod

# tworzymy obiekt Samochod
auto = Samochod("Volvo", "V40")

print(type(auto))

# tak dostajemy się do atrybutów obiektu
print(auto.model)
print(auto.producent)
print(auto.czy_jedzie)

# zmieniamy wartość zmiennej instancji
auto.czy_jedzie = True

print(auto.czy_jedzie)

# tworzymy drugą instancję klasy Samochod
auto2 = Samochod("Fiat", "125p")
print(auto2.producent)
print(auto2.model)

auto2.czy_jedzie = "jedzie"
print(auto2.czy_jedzie)

