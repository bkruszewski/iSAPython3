from day9.samochod import Samochod

auto1 = Samochod("BMW", "3")
auto2 = Samochod("Mercedes", "C")

auto1.czy_jedzie = True

auto1.ruszaj()
auto2.ruszaj()

auto1.trab(6)
auto2.trab(10)