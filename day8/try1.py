# blok try - tu próbujemy najpierw coś zrobić
try:
    with open("lala") as file:
        print(file.read())

# blok except, jeśli pojawi się jakiś błąd, i jeśli ten typ
# błędu przechwytujemy, to kod w danym except będzie wykonany
except FileNotFoundError as e:
    print("Nie znaleziono pliku!\n", e)

except NameError:
    print("nie ma zmiennej")

# to jest najbardziej ogólny typ błedu
# definiujemy go zawsze na końcu
except Exception:
    print("Pojawił się nieoczekiwany błąd!")


