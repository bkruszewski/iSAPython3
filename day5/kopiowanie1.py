# kopiowanie list z typami prostymi

wynik = 3

lista_a = ["zero", "jeden", wynik]
print("lista a:", lista_a)

wynik = 43
# lista_a dalej zawiera wartość 3
print("lista a:", lista_a)

lista_b = lista_a.copy()
print("lista b:", lista_b)

lista_a.append("nowy")
print("lista a:", lista_a)
# lista_b nie zawiera nowego elementu
print("lista b:", lista_b)

# drukujemy adresy pamięci list
# id() - zwraca adres jako liczbe dziesiętną
# hex() - zamienia liczbe dziesietną na szesnastkową
print(hex(id(lista_a)))
print(hex(id(lista_b)))



