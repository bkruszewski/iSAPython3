# jesli nie podam listy, to ma zostać utworzona nowa lista
# a podane imie do niej włożóne
def dodaj_imie(imie, imiona=[]):
    imiona.append(imie.capitalize())
    return imiona

# baza = ["Ala"]
# dodaj_imie("Ola", baza)
# print(baza)

nowa_baza = dodaj_imie("Marta")
print(nowa_baza)
dodaj_imie("Marek", nowa_baza)
print(nowa_baza)

# co się dzieje - nie utworzyłą się nowa lista!!
anglicy = dodaj_imie("Tommy")
print(anglicy)

# znowu ta sama lista z Martą i Markiem
francuzi = dodaj_imie("Pierre")
print(francuzi)

# argument domyślny tworzy typ referencyjny - tak nie robimy!!!
# Python waliduje argumenty domyślne TYLKO RAZ, przy pierwszy wywołaniu funkcji
# utworzył nową listę przy Marcie, a potem już ją wykorzystywał
# - znaczy, listę wykorzystywał ;)