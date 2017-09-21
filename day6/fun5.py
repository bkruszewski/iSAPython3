# ta funkcja ma 2 argumenty wymagane i 2 domyślne
# argumenty wymagane MUSZĄ być zdefiniowane przed domyślnymi
def wypisz_dane(imie, nazwisko, kurs="Python", il_dni=15):
    print(imie, nazwisko, kurs, il_dni)

# argumenty wymagane (pozycyjne) musze podać
wypisz_dane("Arek","g")

# argumenty domyślne mogę podać w dowolnej ilości i kolejności
wypisz_dane("Anna", "Kowalska", "Java")
wypisz_dane("Jan", "MAtejko", "malarstwo", 3657)

wypisz_dane("Paulina", "K", 30)

wypisz_dane("Marek", "O", il_dni=25)

# mogę zmienić kolejność argumentów wszystkich, ale muszę użyć ich nazw
wypisz_dane(kurs="JavaScript", imie="Olaf", il_dni=34, nazwisko="p")