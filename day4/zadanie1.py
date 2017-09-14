# policzyc ilosc liczb parzystych i nieparzystych w zakresie

zakres = range(23, 38945)

ilosc_parzyste = 0
ilosc_nieparzyste = 0

for i in zakres:
    if i % 2 == 0:
        ilosc_parzyste += 1
    else:
        ilosc_nieparzyste += 1

# drukuj ilosc
print("Ilosc parzystych: {}, nieparzystych {}".format(ilosc_parzyste, ilosc_nieparzyste))