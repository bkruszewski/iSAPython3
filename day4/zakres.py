# range(stop)
# range(start, stop)
# range(start, stop, krok)
# pamiętamy, że wartosc stop jest nie bedzie wygenerowana

import math

zakres = range(20)

# wydrukuje nam informację o zakresie a nie wartosci!!!
print(zakres)

# range daje nam kolejne elementy z żadanego zakresu wraz z kolejnym
# przebiegiem pętli

for i in range(1, 100):
    print(i ** 2)