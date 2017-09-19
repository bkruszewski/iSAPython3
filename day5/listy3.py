# kolejka - pierwszy przyszło pierwsze poszło
# FiFo
kolejka = []

kolejka.append(1)
kolejka.append(56)
kolejka.append(23)

print(kolejka)

element = kolejka.pop(0)
print(element)
print(kolejka)
kolejka.append(45)
kolejka.pop(0)
print(kolejka)
print("----------------------\n\n")
# stos
# LiFo

stos = [4335, 5443, 345, 4334]

stos.append(87)
stos.append(854)
stos.append(567)
print(stos)

element2 = stos.pop()
print(element2)
print(stos)





