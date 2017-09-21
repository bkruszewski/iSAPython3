# argumenty domyślne
# ta funkcja ma 1 argument domyślny, jeśli go nie podam
# to zostanie użyta domyślna wartość
def wypisz_imie(imie="arek"):
    imie = imie.capitalize()
    print(f"Cześć {imie}")

wypisz_imie()
wypisz_imie("janek")
wypisz_imie("ola")

