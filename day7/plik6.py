# plik w trybie do zapisu i odczytu
with open("dane", "r+") as plik:

    print(plik.tell())
    # odczytuję zawartość całego pliku - kursor jest na końcu
    plik.read()

    # sprawdzam numer pozycji
    poz = plik.tell()
    # ustawiam na przedostatnią pozycję
    plik.seek(poz - 1)

    # odczytuję ostatni znak
    znak = plik.read(1)

    if znak == "\n":
        plik.write("Był znak nowej linii\n")
    else:
        plik.write("\nNie było nowej linii\n")
