# formuła with pozwala na niepamiętanie o zamykaniu pliku
# python sam zadba o zamknięcie pliku
with open("dane") as plik:
    # tell() mówi na jakiej pozycji jest obecnie kursor
    print(plik.tell())
    linijka = plik.readline()
    print(plik.tell())

    # read(n) - możemy podać ilość znakóœ do przeczytania
    znak = plik.read(1)
    print(znak)

    print(plik.tell())

    # seek() służy do ustawienia kursora w na danej pozycji
    plik.seek(2)

    print(plik.read(1))
    print(plik.tell())



