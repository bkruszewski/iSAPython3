try:
    with open("dane.txt") as plik:
        print(plik.read())

except FileNotFoundError as e:
    print(e)
    print("Podany plik nie istnieje!")

    # sami zgłaszamy wyjątek
    raise ValueError("Błedna wartość ścieżki")

except Exception:
    print("Nieoczekiwany błąd")

print("dalsza część programu")