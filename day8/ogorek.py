# pickle pozwala na zapisywanie do pliku całych obiektów
import pickle

baza = [
    ["Adam", "Kowalski", 34],
    ["Joanna", "Łąckęść", 48]
]

# pamiętać o trybie binarnym
with open("baza.pkl","wb") as plik:
    pickle.dump(baza, plik)
    print("zapisano!")


