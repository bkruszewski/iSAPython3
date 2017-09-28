import os

sciezka = "ogorek.py"

# najpierw sprawdzamy czy plik istnieje,
# jeśli tak to go otwieramy
if os.path.exists(sciezka):

    with open(sciezka) as plik:
        zawartosc = plik.read()
        print(zawartosc)
else:
    print("plik mie istnieje")

