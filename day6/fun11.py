# spr czy str jest palindromem
# docstring

# używamy kod, który wcześniej napisaliśmy!!!!
from day6.fun7 import odwroc_str

def czy_palindrom(fraza:str):
    """
    Sprawdza czy podana fraza jest palindromem, czyli
    od przodu i na wspak litery są takie same.
    :param fraza: zdanie do sprawdzenia
    :return: True jeśli fraza jest palindromem
    """
    for litera1, litera2 in zip(fraza, odwroc_str(fraza)):
        if litera1 != litera2:
            return False
        return True

print(czy_palindrom("kajak"))
print(czy_palindrom("bajka"))
