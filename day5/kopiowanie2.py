# importujemy cały moduł
import copy

# lepiej jest importować tylko to co chcemy użyć
#from copy import deepcopy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

# elementy listy zakupy to inne listy - typy złożone
# są one typami referencyjnymi - kopiowany jest ich
# adres pamięci a nie wartości, które w nich są
zakupy_wrzesien = [nabial, chemia]
print("wrzesień:", zakupy_wrzesien)

zakupy_pazdziernik = zakupy_wrzesien.copy()
print("październik:", zakupy_pazdziernik)

zakupy_listopad = [x for x in zakupy_wrzesien]
print("listopad:", zakupy_listopad)

# tworzymy listę, robiąc głęboką kopię
# w ten sposób kopiujemy wszystkie wartości
zakupy_grudzien = copy.deepcopy(zakupy_wrzesien)


zakupy_wrzesien[1].append("gąbki")
print("wrzesień:", zakupy_wrzesien)
print("październik:", zakupy_pazdziernik)
print("listopad:", zakupy_listopad)
print("grudzień:", zakupy_grudzien)
print("----------------\n\n")
# print(id(zakupy_wrzesien))
# print(id(zakupy_pazdziernik))
# print(id(zakupy_listopad))

print("Adresy poszczególnych list:\n")
print(f"wrzesień     - adres: {hex(id(zakupy_wrzesien))} "
      f" adres nabiał: {hex(id(zakupy_wrzesien[0]))} "
      f" adres chemia: {hex(id(zakupy_wrzesien[1]))}"
      )
print(f"październik  - adres: {hex(id(zakupy_pazdziernik))} "
      f" adres nabiał: {hex(id(zakupy_pazdziernik[0]))} "
      f" adres chemia: {hex(id(zakupy_pazdziernik[1]))}"
      )
print(f"listopad     - adres: {hex(id(zakupy_listopad))} "
      f" adres nabiał: {hex(id(zakupy_listopad[0]))} "
      f" adres chemia: {hex(id(zakupy_listopad[1]))}"
      )
print(f"grudzień     - adres: {hex(id(zakupy_grudzien))} "
      f" adres nabiał: {hex(id(zakupy_grudzien[0]))} "
      f" adres chemia: {hex(id(zakupy_grudzien[1]))}"
      )
