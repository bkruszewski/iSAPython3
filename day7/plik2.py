# otwieramy plik ze wskazaniem trybu
# r - tylko do odczytu
plik = open("dane", "r", encoding='utf8')

print(plik.readline(), end="", )

# readlines() zwraca listę stringów (linijek)
linijki = plik.readlines()
# zobacz, że linijki mają znaki nowej linii!
print(linijki)


plik.close()