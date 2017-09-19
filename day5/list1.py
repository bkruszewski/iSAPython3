# listy

lista = ["jeden", "trzy"]

print(lista)

lista2 = [1, "dwa", "trzy", 5]

lista3 = list(range(2,6))
print(lista3)

lista4 = list("kwiatek")
print(lista4)

flower = ""

for znak in lista4:
    flower += znak.upper()

print(flower)

flower2 = " ".join(lista4)
print(flower2)

