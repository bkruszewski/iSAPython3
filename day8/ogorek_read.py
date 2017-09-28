import pickle

baza_odtworzona = None

with open("baza.pkl", "rb") as plik:
    baza_odtworzona = pickle.load(plik)

# pickle odtwarza dokładny typ zapisanego obiektu
print(type(baza_odtworzona))

print(baza_odtworzona)

# locals pokazuje słownik z lokalnymi wartościami
print(locals())