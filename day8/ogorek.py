import os

JPG_START = bytes.fromhex('FFD8FF')
JPG_END = bytes.fromhex('FFD9')
JPG_ROZNICA_DL = 1

PNG_START = bytes((137, 80, 78, 71, 13, 10, 26, 10))
PNG_END = bytes((73,69,78,68))
PNG_ROZNICA_DL = 4

# podaje indeksy (mniejsze) duplikatów na liście
def duplikaty(lista):
    lista_indeksow = []
    i = 0
    while i != len(lista) - 1:
        if lista[i] == lista[i + 1]:
            lista_indeksow.append(i)
        i += 1
    return lista_indeksow


# te sama funkcje uzyje do znalezienia JPG i PNG
def dekoduj(ukryty_typ, nazwa_pliku):
    # listy będą trzymać indeksy, na których zaczyna sie bajt START albo kończy bajt END dla danego typu obrazka
    # początkowo tych indeksów będzie rożna liczba. będę musiał to potem jakoś uporządkować więc mam jeszcze 2 kolejne listy
    start_indeksy = []
    end_indeksy = []
    ostateczny_start = []
    ostateczny_koniec = []

    # na podstawie 'co' ustawie sobie zmienne, na razie tylko obsługuję JPG i PNG więc
    if ukryty_typ == "JPG":
        poczatek = JPG_START
        koniec = JPG_END
        roznica = JPG_ROZNICA_DL
    else:
        poczatek = PNG_START
        koniec = PNG_END
        roznica = PNG_ROZNICA_DL

    with open(nazwa_pliku, "rb") as plik:
        #szukam indeksów gdzie zaczyna/konczy sie obrazek
        for i in range(os.path.getsize(nazwa_pliku)):
            plik.seek(i)
            # najpierw czytam bajty konca (koniec jest krótszy) i dodaje pozycje kursora do listy
            bajty = plik.read(len(koniec))
            if bajty == koniec:
                end_indeksy.append(plik.tell())
            else:
                # jezeli nie byl to koniec to czytam jeszcze i zczytuje pozycje kursora
                bajty += plik.read(roznica)
                if bajty == poczatek:
                    # odejmuję długość bajtow startowych bo po read() kursor mi się już przestawił
                    start_indeksy.append(plik.tell() - len(poczatek))

        # ponieważ mogę mieć więcej START lub END to muszę je w pary połączyć. Ja sprawdzamm czy START jest mniejsze od END
        # potem chcę usunąć takie przypadki jak START START END albo START START START END
        # Do tego posłuży mi funkcja duplikaty() - znajde indeksy (mniejsze) na liscie ostateczny_koniec i usunę elementy z list
        for i in start_indeksy:
            for j in end_indeksy:
                if i < j:
                    ostateczny_start.append(i)
                    ostateczny_koniec.append(j)
                    break

        indeksy_do_usuniecia = duplikaty(ostateczny_koniec)
        ostateczny_start = [i for j, i in enumerate(ostateczny_start) if j not in indeksy_do_usuniecia]
        ostateczny_koniec = [i for j, i in enumerate(ostateczny_koniec) if j not in indeksy_do_usuniecia]

        # petla for ustawi mnie w miejscu gdzie zaczynam czytac plik
        for indeks, element in enumerate(ostateczny_start):
            plik.seek(element)
            # zczytuje pierwszy bajt tutaj, musze jakos tę zmienną zainicjować...
            nowy_plik = plik.read(1)

            # czytam do momentu aż znajdę znacznik konca. Nie muszę nic inkrementować w pętli bo read() mi przestawia kursor
            while plik.tell() != ostateczny_koniec[indeks]:
                nowy_plik += plik.read(1)

            # teraz muszę to zapisać do pliku
            with open("odzyskany" + str(indeks) +"." + ukryty_typ, "wb") as plik2:
                plik2.write(nowy_plik)
                print("Utworzylem nowy plik")

if __name__ == '__main__':
    print("Zaczynam. Zaczekaj chwilkę.")
    dekoduj("JPG", "treasure_inside")
    dekoduj("PNG", "treasure_inside")
    print("Koniec pracy.")