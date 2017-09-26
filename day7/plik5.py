# plik w trybie do zapisu (nadpisywania)
# niebezpieczny!!!
# usuwa zawartość pliku, kursor ustawia się na początku pliku
with open("dane", "w") as plik:
    print(plik.tell())

    s1 = "Ala ma kota"
    s2 = "Antoni gąbka"
    s3 = "policjanci z majami\n"

    lista = [s1, s2, s3]

    # to zapisze stringi ciągiem
    plik.writelines(lista)

    # musimy sami pamiętać o dodaniu znakóœ nowej linii na końcu
    # zapisywanych stringów
    plik.writelines([s+'\n' for s in lista])

