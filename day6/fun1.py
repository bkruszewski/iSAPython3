# funkcje definiujemy słowem kluczowym def
# poniższa funkcja nic nie robi, nie przyjmuje danych wejściowych
# nie zwraca danych wyjściowych
def moja_funkcja():
    pass

# funkcję wywołujemy z nawiasami
moja_funkcja()

# ta funkcja wypisuje na ekranie moje imie
def wypisz_moje_imie():
    print("Jestem Arek")

# raz napisałem, używam wiele razy
wypisz_moje_imie()
wypisz_moje_imie()
wypisz_moje_imie()
wypisz_moje_imie()
wypisz_moje_imie()

# nawet w pętli
for i in range(100):
    wypisz_moje_imie()