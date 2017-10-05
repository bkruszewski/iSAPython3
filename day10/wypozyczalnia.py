from day10.klient import Klient
from day10.film import Film


kl1 = Klient("Adam", 897688473621)
kl2 = Klient("Joanna", 984574859438)

film1 = Film("Rambo 3", 15.99)
film2 = Film("Polowanie na czerwony październik", 9.99)
film3 = Film("Narcos", 39.99)

kl1.wypozycz(film1)

print(film1)
print(film2)
print(film3)

film3.kategoria = "Dramat"

print(film3.kategoria)
print(film2.kategoria)
