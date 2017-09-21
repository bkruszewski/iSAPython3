def pole_trojkata(podstawa, wysokosc):
    # pole to zmienna lokalna - jest tylko w bloku
    # definicji funkcji
    pole = 0.5 * podstawa * wysokosc
    print(pole, "cm2")

pole_trojkata(23, 20)


# zmienna pole istnieje tylko wewnątrz definicji funkcji
print(pole)

