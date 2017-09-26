# pamiętać gdzie się znajdujemy, od tego zależy ścieżka do otwieranego
# pliku
print("aktualny folder roboczy:", os.getcwd)

# otwieramy plik, jeśli nie podamy trybu, to
# plik zostanie otworzony w trybie tylko do odczytu
plik = open("dane")

# readline() - odczytuje jedną linijkę
# kursor czeka po odczytanej linijce na dalsze polecenia
linijka = plik.readline()
# linijki mają niewidzialne znaki nowej linii
print(linijka)

# znowu odczytujemy linijkę
linijka2 = plik.readline()
# jeśli nie chcemy pustej linii to usuwamy \n z printa
print(linijka2, end='')

# read() odczytuje zawartośc, od kursora do końca pliku
# zwraca stringa
pozostaly_tekst = plik.read()
print(pozostaly_tekst)

# pamiętamy o zamykaniu plików
plik.close()