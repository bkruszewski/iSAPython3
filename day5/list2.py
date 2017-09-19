zdanie = "Ala ma kota i ma cztery łapy"

wyrazy = []
wyraz = ""

for znak in zdanie:
    if znak == " ":
        wyrazy.append(wyraz)
        wyraz = ""
        continue
    else:
        wyraz += znak

wyrazy.append(wyraz)
print(wyrazy)

wyrazy2 = zdanie.split(" ")
print(wyrazy2)


# liczby = [0, 1, 2, 4]
# liczby.insert(3, 3)
# print(liczby)
#
# del liczby[1]
# print(liczby)
#
# del liczby[1:3]
# print(liczby)
#
# del liczby
# # to nie zadziała, bo nie ma już zmiennej liczby
# # print(liczby)