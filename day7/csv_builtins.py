import csv

with open("osoby.csv") as plik:
    # tworzymy czytnik
    czytnik_csv = csv.reader(plik)

    for line in czytnik_csv:
        print(line)

dane = ["Adam", "Kowalski", 33]

with open("osoby.csv", "a") as plik:
    # tworze zapisywacz
    zapisywacz_csv = csv.writer(plik)
    zapisywacz_csv.writerow(dane)

