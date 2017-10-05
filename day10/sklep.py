from day10.przedmiot import Przedmiot

art1 = Przedmiot("Woda mineralna 1l", 2.30, 1)

polka_z_woda = []

# for i in range(100):
#     woda = Przedmiot("Woda mineralna 1l", 2.30, 1)
#     polka_z_woda.append(woda)

print(art1)
# print(polka_z_woda)

# wartosc, ciezar = polka_z_woda[34] + polka_z_woda[50]

# print(f"wartosc przedmiotow: {wartosc}")
# print(f"ciężar przedmiotów: {ciezar}")

art2 = Przedmiot("chleb", 3.20, 0.5)

print(art1 < art2)

zakupy = art1 + art2

print(f"Zakupy kosztują: {zakupy[0]} EUR i ważą: {zakupy[1]} kg")

del art2

# print(art2.nazwa)

print("-------Koniec programu-----------\n")

