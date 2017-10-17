def dodaj(a, b):
    return a + b

def pomnoz(a, b):
    return a * b

def odejmij(a, b):
    if a > b:
        print(a - b)
    else:
        print(-1)


def main():
    wynik = odejmij(10, 2)
    print(wynik)
    print(type(wynik))


if __name__ == '__main__':
    main()
