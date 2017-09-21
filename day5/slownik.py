osoby = {"Ania":"Kowalska", 2:234.4, "9238732": 4}

liczby = {1:2, 2:3, 3:4}

# osoby = dict()
print(liczby[1])
# print(osoby[2])

osoby["Joanna"] = "policja"
print(osoby)
osoby["Joanna"] = "straż"
print(osoby)

# print(liczby[4])

print(osoby.keys())
print(osoby.values())

for key, value in osoby.items():
    print(f"klucz: {key} - wartość: {value}")